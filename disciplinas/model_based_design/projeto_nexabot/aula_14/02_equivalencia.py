#!/usr/bin/env python3
"""Aula 14 — Script 2/5: equivalência modelo x código (o ponto central da aula).

O que este script faz
----------------------
Roda `DiscretePID` (o modelo Python, Unidade 2) e `SILController` (o C
gerado na Aula 13, compilado e chamado via ctypes) sobre EXATAMENTE a mesma
sequência de referência/medição, amostra a amostra, e mede o erro absoluto
entre as duas saídas — `nexabot.sil.compare_model_vs_code`.

Isto é o SIL (Software-in-the-Loop) propriamente dito: a evidência de que
"o código gerado implementa o modelo" deixa de ser uma alegação de design e
passa a ser um número medido, reproduzível, e verificável de novo a
qualquer momento (inclusive em CI — ver `04_ci.py`).

Como rodar
----------
    .venv/bin/python aula_14/02_equivalencia.py

Saída esperada (resumo)
------------------------
Erro máximo da variante `double` da ordem do épsilon de máquina (idealmente
exatamente 0.0, já que a tradução para C preserva a ordem de operações do
modelo) e um resumo em tabela ASCII por trecho da simulação.

Rastreabilidade: este script é a evidência de TESTE de REQ-CTRL-001
(rastreamento de velocidade), REQ-CTRL-002 (saturação do atuador),
REQ-CTRL-003 (anti-windup) e REQ-CODEGEN-001 (equivalência numérica código
gerado x modelo) — os quatro requisitos que `pid_step`/`pid_fixed_step`
(código gerado) precisam preservar do modelo `DiscretePID`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

from nexabot.sil import compare_model_vs_code  # noqa: E402

EPS_MAQUINA = np.finfo(float).eps


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def sequencia_de_teste(n: int = 6000, Ts: float = 5.0e-3, seed: int = 7):
    """Referência em degraus variados + medição com ruído de encoder e
    saturações propositais, para exercitar toda a lógica de `pid_step`
    (incluindo a saturação e o anti-windup, não só o regime linear)."""
    rng = np.random.default_rng(seed)
    t = np.arange(n) * Ts
    r = np.select(
        [t < 3.0, t < 7.0, t < 12.0, t < 18.0],
        [80.0, -80.0, 150.0, 0.0],
        default=40.0 * np.sin(2 * np.pi * 0.3 * t),
    )
    y = np.zeros(n)
    estado = 0.0
    alpha = Ts / (0.03 + Ts)
    for k in range(n):
        estado += alpha * (r[k] - estado)
        y[k] = estado + rng.normal(0.0, 0.8)
    return r, y


def main() -> None:
    print(linha("="))
    print("Aula 14 — Equivalência SIL: DiscretePID (Python) x código C gerado")
    print(linha("="))

    r, y = sequencia_de_teste()
    ganhos = dict(Kp=2.0, Ki=40.0, Kd=0.02, Ts=5.0e-3, u_max=24.0, tau_f=0.01, Kaw=1.0)
    print(f"\nSequência de teste: {len(r)} amostras, ganhos = {ganhos}")

    print("\n" + linha("-"))
    print(f"{'variante':<10} | {'n amostras':>10} | {'erro máx [V]':>13} | {'erro médio [V]':>15} | {'erro RMS [V]':>13}")
    print(linha("-"))

    rep_double = compare_model_vs_code(r, y, fixed_point=False, **ganhos)
    print(f"{'double':<10} | {rep_double.n_amostras:>10} | {rep_double.erro_maximo_abs:>13.3e} | "
          f"{rep_double.erro_medio_abs:>15.3e} | {rep_double.erro_rms:>13.3e}")

    rep_fixed = compare_model_vs_code(r, y, fixed_point=True, **ganhos)
    print(f"{'Q16.16':<10} | {rep_fixed.n_amostras:>10} | {rep_fixed.erro_maximo_abs:>13.3e} | "
          f"{rep_fixed.erro_medio_abs:>15.3e} | {rep_fixed.erro_rms:>13.3e}")

    print("\n" + linha("-"))
    print(f"Amostra de pior caso (variante double): k = {rep_double.amostra_pior_caso}")
    k = rep_double.amostra_pior_caso
    print(f"  u_modelo[{k}] = {rep_double.saidas_modelo[k]!r}")
    print(f"  u_codigo[{k}] = {rep_double.saidas_codigo[k]!r}")

    tolerancia_double = 100 * EPS_MAQUINA  # margem folgada acima do épsilon de máquina
    print("\n" + linha("="))
    print(f"Épsilon de máquina (float64): {EPS_MAQUINA:.3e}")
    print(f"Tolerância adotada para a variante double: {tolerancia_double:.3e} (100x épsilon)")
    ok = rep_double.erro_maximo_abs <= tolerancia_double
    print(f"Erro máximo double ({rep_double.erro_maximo_abs:.3e}) <= tolerância? "
          f"{'OK' if ok else 'FALHOU -- há um bug de codegen a corrigir'}")

    if not ok:
        raise SystemExit(1)

    print("\nConclusão: o C gerado pela Aula 13 é numericamente equivalente ao")
    print("modelo DiscretePID dentro do erro de arredondamento de ponto flutuante")
    print("-- não 'parecido', EQUIVALENTE, com número medido para provar.")


if __name__ == "__main__":
    main()
