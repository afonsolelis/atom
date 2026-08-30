#!/usr/bin/env python3
"""Aula 14 — Script 1/5: compila o SIL e mostra a ponte ctypes por dentro.

O que este script faz
----------------------
Gera o C da Aula 13, compila com `gcc` como biblioteca compartilhada
(`nexabot.sil.compile_shared_library`) e carrega os símbolos com `ctypes`
"na mão" — sem passar pela conveniência de `SILController` — para deixar
visível o mecanismo: um `ctypes.Structure` cujo layout precisa bater
exatamente com a struct C, `argtypes`/`restype` explícitos e uma chamada de
função como qualquer outra chamada Python.

Depois repete a mesma sequência usando `nexabot.sil.SILController` (a
interface de produção, que faz tudo isso internamente) para comparar.

Como rodar
----------
    .venv/bin/python aula_14/01_compila_sil.py

Saída esperada (resumo)
------------------------
Os símbolos exportados pela biblioteca compartilhada, uma chamada manual a
`pid_step` via ctypes e a mesma chamada via `SILController`, com resultados
idênticos.
"""

from __future__ import annotations

import ctypes
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.controllers import DiscretePID  # noqa: E402
from nexabot.codegen.generate import generate_pid_controller  # noqa: E402
from nexabot.sil import SILController, compile_shared_library  # noqa: E402


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


class PidCStructManual(ctypes.Structure):
    """Réplica manual, só para este script, de `pid_controller_t` — o mesmo
    layout usado internamente por `nexabot.sil._PidCStruct`."""

    _fields_ = [
        ("Kp", ctypes.c_double), ("Ki", ctypes.c_double), ("Kd", ctypes.c_double),
        ("Ts", ctypes.c_double), ("u_max", ctypes.c_double), ("tau_f", ctypes.c_double),
        ("Kaw", ctypes.c_double), ("integral", ctypes.c_double),
        ("e_prev", ctypes.c_double), ("d_state", ctypes.c_double),
    ]


def main() -> None:
    print(linha("="))
    print("Aula 14 — SIL: compilando C gerado e carregando via ctypes")
    print(linha("="))

    pid_model = DiscretePID(Kp=2.0, Ki=40.0, Kd=0.02)
    gerado = generate_pid_controller(pid_model)
    print(f"\nC gerado: {gerado.source_path}")

    lib_path = compile_shared_library(gerado.source_path)
    print(f"Biblioteca compartilhada compilada: {lib_path}")

    lib = ctypes.CDLL(str(lib_path))
    print("\nSímbolos usados (definidos explicitamente para segurança de tipos):")
    lib.pid_init.argtypes = [
        ctypes.POINTER(PidCStructManual), ctypes.c_double, ctypes.c_double, ctypes.c_double,
        ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
    ]
    lib.pid_init.restype = None
    lib.pid_step.argtypes = [ctypes.POINTER(PidCStructManual), ctypes.c_double, ctypes.c_double]
    lib.pid_step.restype = ctypes.c_double
    print("  pid_init(pid_controller_t*, double x7) -> void")
    print("  pid_step(pid_controller_t*, double r, double y) -> double")

    estado = PidCStructManual()
    lib.pid_init(ctypes.byref(estado), pid_model.Kp, pid_model.Ki, pid_model.Kd,
                 pid_model.Ts, pid_model.u_max, pid_model.tau_f, pid_model.Kaw)

    print("\n--- Chamada manual via ctypes cru ---")
    for r, y in [(3.0, 0.0), (3.0, 1.0), (3.0, 2.5)]:
        u = lib.pid_step(ctypes.byref(estado), r, y)
        print(f"  pid_step(r={r}, y={y}) = {u:.6f} V")

    print("\n--- Mesma sequência via SILController (interface de produção) ---")
    controlador = SILController(Kp=2.0, Ki=40.0, Kd=0.02)
    for r, y in [(3.0, 0.0), (3.0, 1.0), (3.0, 2.5)]:
        u = controlador.step(r, y)
        print(f"  SILController.step(r={r}, y={y}) = {u:.6f} V")

    print("\n" + linha("="))
    print("As duas sequências de saída são idênticas: SILController só empacota")
    print("exatamente esta mecânica (compilar + ctypes.Structure + argtypes/restype).")


if __name__ == "__main__":
    main()
