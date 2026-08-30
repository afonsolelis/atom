#!/usr/bin/env python3
"""Aula 13 — Double vs. ponto fixo Q16.16 (script 3/4).

Roda a variante em `double` e a variante em ponto fixo Q16.16 do C gerado
(ambas no mesmo arquivo `pid_controller.c`, ver Aula 13 script 2) sobre a
mesma sequência de referência/medição e tabula o erro de quantização —
quanto a aritmética de 32 bits sem FPU se afasta da referência em double.

Por que isso importa: um microcontrolador barato sem unidade de ponto
flutuante (a maioria dos Cortex-M0/M0+, e mesmo alguns 8 bits ainda em uso
industrial) roda ponto fixo com desempenho previsível; a Q16.16 gasta 32
bits para 16 bits de parte inteira e 16 de fração, resolução
1/65536 ~= 1{,}5e-5 por operação — mas os erros de arredondamento de cada
multiplicação/divisão se acumulam ao longo de milhares de amostras.

Rodar:
    .venv/bin/python aula_13/03_ponto_fixo.py

Saída esperada (resumo): uma tabela ASCII com o erro amostra a amostra em
alguns pontos da simulação e um resumo com erro máximo/médio/RMS.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot.sil import compare_model_vs_code  # noqa: E402


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def cenario_entradas(n: int = 4000, Ts: float = 5.0e-3) -> tuple[np.ndarray, np.ndarray]:
    """Referência em degraus + rampa de velocidade e uma medição ruidosa
    plausível de encoder, para exercitar o PID em regimes variados."""
    rng = np.random.default_rng(42)
    t = np.arange(n) * Ts
    r = np.piecewise(
        t,
        [t < 2.0, (t >= 2.0) & (t < 5.0), t >= 5.0],
        [50.0, 120.0, lambda tt: 80.0 + 40.0 * np.sin(2 * np.pi * 0.2 * tt)],
    )
    ruido = rng.normal(0.0, 0.5, size=n)
    y = r * 0.0
    # y segue r com atraso simples de primeira ordem simulado + ruído de encoder,
    # só para gerar uma sequência de erro realista (não é a planta completa —
    # o ponto aqui é comparar double x fixo, não validar a malha fechada).
    alpha = Ts / (0.05 + Ts)
    estado = 0.0
    for k in range(n):
        estado += alpha * (r[k] - estado)
        y[k] = estado + ruido[k]
    return r, y


def main() -> None:
    print(linha("="))
    print("Aula 13 — Erro de quantização: double vs. ponto fixo Q16.16")
    print(linha("="))

    r, y = cenario_entradas()
    Kp, Ki, Kd = 2.0, 40.0, 0.02

    rep_double = compare_model_vs_code(r, y, Kp=Kp, Ki=Ki, Kd=Kd, fixed_point=False)
    rep_fixed = compare_model_vs_code(r, y, Kp=Kp, Ki=Ki, Kd=Kd, fixed_point=True)

    print(f"\nSequência de {rep_double.n_amostras} amostras, Kp={Kp}, Ki={Ki}, Kd={Kd}")

    print("\n" + linha("-"))
    print(f"{'variante':<12} | {'erro máximo [V]':>16} | {'erro médio [V]':>15} | {'erro RMS [V]':>13}")
    print(linha("-"))
    print(f"{'double':<12} | {rep_double.erro_maximo_abs:>16.3e} | "
          f"{rep_double.erro_medio_abs:>15.3e} | {rep_double.erro_rms:>13.3e}")
    print(f"{'Q16.16':<12} | {rep_fixed.erro_maximo_abs:>16.3e} | "
          f"{rep_fixed.erro_medio_abs:>15.3e} | {rep_fixed.erro_rms:>13.3e}")

    print("\n" + linha("-"))
    print("Amostras espaçadas (u do modelo vs. u de cada variante em C):")
    print(linha("-"))
    header = f"{'k':>6} | {'u modelo [V]':>13} | {'u double [V]':>13} | {'u Q16.16 [V]':>13} | {'|erro fixo| [V]':>15}"
    print(header)
    print(linha("-", len(header)))
    indices = np.linspace(0, rep_double.n_amostras - 1, 12, dtype=int)
    for k in indices:
        erro_fixo_k = abs(rep_double.saidas_modelo[k] - rep_fixed.saidas_codigo[k])
        print(f"{k:>6} | {rep_double.saidas_modelo[k]:>13.6f} | {rep_double.saidas_codigo[k]:>13.6f} | "
              f"{rep_fixed.saidas_codigo[k]:>13.6f} | {erro_fixo_k:>15.3e}")

    resolucao_q16_16 = 1.0 / 65536.0
    print("\n" + linha("-"))
    print(f"Resolução nominal de Q16.16: 1/65536 ~= {resolucao_q16_16:.3e}")
    print(f"Erro RMS medido (ponto fixo): {rep_fixed.erro_rms:.3e} "
          f"(~{rep_fixed.erro_rms / resolucao_q16_16:.1f}x a resolução nominal, "
          "devido ao acúmulo de arredondamento nas 4 multiplicações/1 divisão por passo)")

    print(linha("="))
    print("Conclusão:")
    print(f"  - double : erro {'de ordem do épsilon de máquina' if rep_double.erro_maximo_abs < 1e-9 else 'ACIMA do esperado -- investigar bug de codegen'} "
          f"(máx = {rep_double.erro_maximo_abs:.3e} V) -> o C reproduz o modelo bit a bit.")
    print(f"  - Q16.16 : erro máximo de {rep_fixed.erro_maximo_abs:.3e} V "
          f"(~{100 * rep_fixed.erro_maximo_abs / max(1e-9, np.max(np.abs(rep_double.saidas_modelo))):.3f}% "
          "da maior tensão de comando) -- aceitável para um driver de motor "
          "com resolução de PWM tipicamente >= 10 bits, mas deve ser validado "
          "contra a margem de estabilidade do laço fechado, não só contra a "
          "resolução nominal.")

    if rep_double.erro_maximo_abs >= 1e-9:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
