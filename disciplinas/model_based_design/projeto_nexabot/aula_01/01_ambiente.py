#!/usr/bin/env python3
"""Aula 1 — Script 1/5: verificação do ambiente de trabalho.

O que este script demonstra
----------------------------
Antes de simular qualquer sistema ciberfísico, precisamos confiar na
ferramentaria: sem numpy/scipy/control funcionando, não existe planta, não
existe controlador, não existe FMU. Este script varre as bibliotecas Python
que a disciplina inteira (Aulas 1 a 16) usa, confere as versões mínimas e
imprime um relatório verde/vermelho de prontidão do ambiente — o tipo de
checagem que qualquer pipeline de MBD roda antes de qualquer coisa.

Também confirma que o pacote `nexabot` (o contrato compartilhado da
disciplina: `params.py`, `plant.py`, `controllers.py`) importa sem erro e
que os números de `params.py` batem com os valores verificados desta aula.

Como rodar
----------
    .venv/bin/python aula_01/01_ambiente.py
"""

from __future__ import annotations

import importlib
import os
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402

# Biblioteca -> versão mínima exigida pela disciplina
BIBLIOTECAS = {
    "numpy": "1.24",
    "scipy": "1.10",
    "control": "0.9",
    "sympy": "1.12",
    "matplotlib": "3.7",
    "jinja2": "3.1",
    "hypothesis": "6.0",
    "pytest": "7.0",
    "coverage": "7.0",
    "fmpy": "0.3",
    "serial": "3.5",  # pacote pyserial, módulo importado como `serial`
}


def _versao_tupla(v: str) -> tuple[int, ...]:
    partes = []
    for p in v.split("."):
        digitos = "".join(c for c in p if c.isdigit())
        partes.append(int(digitos) if digitos else 0)
    return tuple(partes)


def checar_bibliotecas() -> list[tuple[str, bool, str]]:
    """Tenta importar cada biblioteca e compara a versão instalada com a mínima."""
    resultados = []
    for nome, minima in BIBLIOTECAS.items():
        try:
            mod = importlib.import_module(nome)
            versao = getattr(mod, "__version__", "desconhecida")
            ok = versao == "desconhecida" or _versao_tupla(versao) >= _versao_tupla(minima)
            resultados.append((nome, ok, versao))
        except ImportError as exc:
            resultados.append((nome, False, f"AUSENTE ({exc})"))
    return resultados


def checar_ferramentas_externas() -> list[tuple[str, bool, str]]:
    """Confere ferramentas de linha de comando usadas nas unidades 3 e 4 (gcc, pandoc)."""
    resultados = []
    for exe in ("gcc", "python3"):
        caminho = shutil.which(exe)
        if caminho:
            try:
                versao = subprocess.run([exe, "--version"], capture_output=True, text=True, timeout=5)
                primeira_linha = versao.stdout.splitlines()[0] if versao.stdout else "ok"
            except Exception:
                primeira_linha = "ok"
            resultados.append((exe, True, primeira_linha))
        else:
            resultados.append((exe, False, "não encontrado no PATH"))
    return resultados


def checar_contrato_nexabot() -> list[tuple[str, bool, str]]:
    """Confirma que os números de params.py batem com os valores verificados da disciplina."""
    checagens = [
        ("R = 1.2 ohm", PARAMS.R == 1.2),
        ("L = 3.5e-3 H", PARAMS.L == 3.5e-3),
        ("Ke = Kt = 0.045", PARAMS.Ke == 0.045 and PARAMS.Kt == 0.045),
        ("J = 2.5e-4 kg.m^2", PARAMS.J == 2.5e-4),
        ("N_gear = 20", PARAMS.N_gear == 20.0),
        ("V_max = 24 V", PARAMS.V_max == 24.0),
        ("Ts = 5e-3 s (200 Hz)", PARAMS.Ts == 5.0e-3),
        ("ganho DC ~= 21.2164 rad/(s.V)", abs(PARAMS.dc_gain - 21.2164) < 1e-3),
    ]
    return [(nome, ok, "confere" if ok else "DIVERGE de params.py") for nome, ok in checagens]


def main() -> int:
    print(viz.titulo("NexaBot — Aula 1 — Relatório de prontidão do ambiente"))

    secoes = [
        ("Bibliotecas Python", checar_bibliotecas()),
        ("Ferramentas externas", checar_ferramentas_externas()),
        ("Contrato nexabot/params.py", checar_contrato_nexabot()),
    ]

    tudo_ok = True
    for titulo_secao, resultados in secoes:
        linhas = []
        for nome, ok, detalhe in resultados:
            tudo_ok &= ok
            status = viz.verde("OK") if ok else viz.vermelho("FALHA")
            linhas.append([nome, status, detalhe])
        viz.tabela(["item", "status", "detalhe"], linhas, titulo_tabela=titulo_secao)
        print()

    if tudo_ok:
        print(viz.verde(viz.negrito("AMBIENTE PRONTO — pode iniciar a Aula 1.")))
    else:
        print(viz.vermelho(viz.negrito("AMBIENTE COM PENDÊNCIAS — resolva os itens em vermelho antes de continuar.")))

    print(f"\nInterpretador: {sys.executable}")
    print(f"Versão do Python: {sys.version.split()[0]}")
    return 0 if tudo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
