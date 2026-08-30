#!/usr/bin/env python3
"""Aula 14 — Script 5/5: desafio — injete um bug de codegen e veja o SIL pegá-lo.

O que este script faz
----------------------
A Aula 14 inteira defende que a equivalência SIL é uma REDE DE SEGURANÇA:
se alguém editar `pid_controller.c.j2` e introduzir um erro sutil, a
suíte de regressão deve detectar. Este script prova isso na prática: gera
um C "quase certo" com um bug clássico de tradução -- o sinal do termo de
anti-windup trocado (`u_unsat - u` em vez de `u - u_unsat`) -- compila,
compara contra o modelo, e mostra que o erro deixa de ser zero.

DESAFIO: complete `injetar_bug_sinal_trocado` (o `.replace(...)` que injeta
o bug) e rode o script para ver a suíte de equivalência reprovar OS CASOS
com saturação ativa (onde o termo de anti-windup importa) e aprovar os
demais (onde ele nunca entra em ação) -- uma lição sobre por que um único
cenário de teste "no regime linear" não bastaria para pegar este bug.

Como rodar
----------
    .venv/bin/python aula_14/05_desafio.py

Saída esperada (resumo)
------------------------
Com o bug injetado, a comparação para uma sequência QUE SATURA mostra erro
grande (não mais ~0); a comparação para uma sequência que nunca satura
continua dando erro ~0 -- ilustrando por que a suíte de regressão da Aula
14 varia os ganhos e as entradas, e não usa um único caso "fácil".
"""

from __future__ import annotations

import ctypes
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

from nexabot.codegen.generate import generate_pid_controller  # noqa: E402
from nexabot.controllers import DiscretePID  # noqa: E402
from nexabot.sil import SILController, compile_shared_library  # noqa: E402


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def injetar_bug_sinal_trocado(codigo_c: str) -> str:
    """DESAFIO: injete o bug clássico de anti-windup com sinal trocado.

    O contrato correto é:
        pid->integral += pid->Kaw * (u - u_unsat) * pid->Ts;

    Um erro de tradução comum (o "off-by-sign") escreve o oposto:
        pid->integral += pid->Kaw * (u_unsat - u) * pid->Ts;

    Ambas COMPILAM sem aviso -- só uma revisão de código ou uma comparação
    numérica contra o modelo pega a diferença.
    """
    # --- solução de referência (apague e reescreva como exercício) ---
    original = "pid->integral += pid->Kaw * (u - u_unsat) * pid->Ts;"
    trocado = "pid->integral += pid->Kaw * (u_unsat - u) * pid->Ts;"
    if original not in codigo_c:
        raise AssertionError("trecho esperado não encontrado -- o template mudou?")
    return codigo_c.replace(original, trocado, 1)


class _PidCStruct(ctypes.Structure):
    _fields_ = [(n, ctypes.c_double) for n in (
        "Kp", "Ki", "Kd", "Ts", "u_max", "tau_f", "Kaw", "integral", "e_prev", "d_state")]


def _carregar_controlador_com_bug(pid: DiscretePID, build_dir: Path) -> ctypes.CDLL:
    gerado = generate_pid_controller(pid, output_dir=build_dir)
    codigo_com_bug = injetar_bug_sinal_trocado(gerado.source_path.read_text(encoding="utf-8"))
    gerado.source_path.write_text(codigo_com_bug, encoding="utf-8")

    lib_path = compile_shared_library(gerado.source_path, build_dir)
    lib = ctypes.CDLL(str(lib_path))
    lib.pid_init.argtypes = [ctypes.POINTER(_PidCStruct)] + [ctypes.c_double] * 7
    lib.pid_init.restype = None
    lib.pid_step.argtypes = [ctypes.POINTER(_PidCStruct), ctypes.c_double, ctypes.c_double]
    lib.pid_step.restype = ctypes.c_double
    return lib


def _rodar_com_bug(lib: ctypes.CDLL, pid: DiscretePID, r: np.ndarray, y: np.ndarray) -> np.ndarray:
    estado = _PidCStruct()
    lib.pid_init(ctypes.byref(estado), pid.Kp, pid.Ki, pid.Kd, pid.Ts, pid.u_max, pid.tau_f, pid.Kaw)
    saida = np.empty(len(r))
    for k in range(len(r)):
        saida[k] = lib.pid_step(ctypes.byref(estado), float(r[k]), float(y[k]))
    return saida


def main() -> None:
    print(linha("="))
    print("Aula 14 — Desafio: injetando um bug de anti-windup e vendo o SIL pegá-lo")
    print(linha("="))

    ganhos = dict(Kp=2.0, Ki=60.0, Kd=0.0, Ts=5.0e-3, u_max=24.0, tau_f=0.01, Kaw=1.0)
    pid_bug = DiscretePID(**ganhos)
    pid_ref = DiscretePID(**ganhos)

    with tempfile.TemporaryDirectory(prefix="nexabot_bug_") as tmp:
        lib_bug = _carregar_controlador_com_bug(pid_bug, Path(tmp))

        print("\n--- Cenário 1: satura e depois DESSATURA (anti-windup precisa desenrolar) ---")
        print("  (o bug de sinal só aparece quando a referência volta ao regime linear:")
        print("   durante a saturação, a saída fica travada em u_max nos dois casos --")
        print("   comparar só a fase saturada esconderia o bug.)")
        n_satura, n_linear = 50, 1000
        n = n_satura + n_linear
        # fase 2 com referência ABAIXO da medição (e < 0): é o único jeito de o
        # anti-windup correto realmente zerar o excesso de integral acumulado
        # (com e >= 0 constante, o integrador "deveria" continuar crescendo --
        # não seria um bug, seria controle integral funcionando).
        r_satura = np.concatenate([np.full(n_satura, 500.0), np.full(n_linear, -5.0)])
        y_satura = np.zeros(n)
        u_modelo = np.array([pid_ref.step(r_satura[k], y_satura[k]) for k in range(n)])
        u_bug = _rodar_com_bug(lib_bug, pid_bug, r_satura, y_satura)
        erro_satura = float(np.max(np.abs(u_modelo - u_bug)))
        erro_final = float(abs(u_modelo[-1] - u_bug[-1]))
        print(f"  u modelo no final (deveria ter desenrolado) : {u_modelo[-1]:.4f} V")
        print(f"  u código com bug no final (travado?)        : {u_bug[-1]:.4f} V")
        print(f"  erro máximo com bug (todo o cenário 1)      : {erro_satura:.3e} V")

        print("\n--- Cenário 2: referência pequena, NUNCA satura (anti-windup nunca ativa) ---")
        pid_ref2 = DiscretePID(**ganhos)
        pid_bug2 = DiscretePID(**ganhos)
        lib_bug2 = _carregar_controlador_com_bug(pid_bug2, Path(tmp) / "caso2")
        r_linear = np.full(n, 2.0)
        y_linear = np.zeros(n)
        u_modelo2 = np.array([pid_ref2.step(r_linear[k], y_linear[k]) for k in range(n)])
        u_bug2 = _rodar_com_bug(lib_bug2, pid_bug2, r_linear, y_linear)
        erro_linear = float(np.max(np.abs(u_modelo2 - u_bug2)))
        print(f"  erro máximo com bug (regime linear): {erro_linear:.3e} V")

    print("\n" + linha("-"))
    print("Para comparação, o controlador SEM bug (SILController de produção):")
    correto = SILController(**ganhos)
    u_correto = np.array([correto.step(r_satura[k], y_satura[k]) for k in range(n)])
    pid_ref3 = DiscretePID(**ganhos)
    u_modelo3 = np.array([pid_ref3.step(r_satura[k], y_satura[k]) for k in range(n)])
    erro_correto = float(np.max(np.abs(u_modelo3 - u_correto)))
    print(f"  erro máximo (mesmo cenário 1, sem bug): {erro_correto:.3e} V")

    print("\n" + linha("="))
    print("Conclusão")
    print(linha("="))
    bug_detectado_onde_importa = erro_satura > 1.0e-6
    bug_mascarado_onde_nao_importa = erro_linear < 1.0e-9
    print(f"  bug pego no cenário que satura?      {'sim' if bug_detectado_onde_importa else 'NÃO -- revise'}")
    print(f"  bug mascarado no cenário linear?     {'sim' if bug_mascarado_onde_nao_importa else 'não'}")
    print(f"  código sem bug (mesmo cenário 1)?    erro {erro_correto:.3e} V (deve ser ~0)")
    print("\nLição: um bug de codegen pode ficar INVISÍVEL se a suíte de regressão só")
    print("testar o regime linear. É por isso que 03_regressao.py varia ganhos E")
    print("amplitude de referência com hypothesis, em vez de fixar um único cenário.")

    if not (bug_detectado_onde_importa and bug_mascarado_onde_nao_importa):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
