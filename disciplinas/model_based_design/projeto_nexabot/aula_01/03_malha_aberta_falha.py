#!/usr/bin/env python3
"""Aula 1 — Script 3/5: por que malha aberta não atende — erro sob rampa de carga.

O que este script demonstra
----------------------------
O NexaBot é um AGV de armazém: carrega paletes de peso variável. Isso entra
no modelo como `tau_load`, um torque de carga na equação mecânica. Em malha
aberta (tensão fixa, calculada para uma condição de carga), qualquer mudança
na carga desloca a velocidade de regime — sem que ninguém perceba, porque
não há realimentação. Este script aplica uma RAMPA de torque de carga
crescente (carga sendo empilhada) e mostra numericamente o erro de
velocidade crescendo, mesmo com a tensão computada para o ponto de operação
inicial.

Como rodar
----------
    .venv/bin/python aula_01/03_malha_aberta_falha.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import simulate  # noqa: E402


def main() -> int:
    print(viz.titulo("NexaBot — Aula 1 — Malha aberta falha sob carga variável"))

    v_alvo = 1.0  # m/s: velocidade de cruzeiro desejada, vazio
    omega_alvo = PARAMS.v_to_omega(v_alvo)
    V_calculada = omega_alvo / PARAMS.dc_gain  # tensão calculada p/ o ponto de operação SEM carga

    print(f"Objetivo: manter v = {v_alvo:.2f} m/s ({omega_alvo:.1f} rad/s no motor).")
    print(f"Tensão calculada em malha aberta para esse alvo, SEM carga: V = {V_calculada:.3f} V.\n")
    print("Cenário: o NexaBot está transportando um palete e o operador vai empilhando")
    print("mais peso ao longo do trajeto — o torque de carga refletido ao motor cresce")
    print("em rampa de 0 a um valor equivalente a ~30% do torque nominal em 2 s.\n")

    t_end = 2.0
    tau_load_max = 0.35 * PARAMS.Kt * PARAMS.i_max  # ~30-35% do torque nominal a i_max

    def u_of_t(_t):
        return V_calculada  # malha aberta: tensão fixa, nunca é recalculada

    def tau_load_of_t(t):
        return tau_load_max * min(t / t_end, 1.0)

    # Parte já em regime permanente (vazio) no instante t=0, para que a curva
    # mostre só o efeito da carga — não o transiente de partida do motor.
    i0 = PARAMS.b * omega_alvo / PARAMS.Kt
    x0 = np.array([i0, omega_alvo])

    t, X = simulate(u_of_t, t_end=t_end, dt=1.0e-4, x0=x0,
                     tau_load_of_t=tau_load_of_t, p=PARAMS)
    omega = X[:, 1]
    v_linear = PARAMS.omega_to_v(omega)
    erro_v = v_alvo - v_linear
    erro_pct = erro_v / v_alvo * 100.0

    viz.plot_ascii(t, v_linear, altura=14, largura=64,
                    titulo_grafico="Velocidade linear real v(t) sob carga crescente (malha aberta)",
                    y_ref=v_alvo, unidade_y="m/s")
    print()
    viz.plot_ascii(t, erro_pct, altura=10, largura=64,
                    titulo_grafico="Erro percentual de velocidade (t)", unidade_y="%")

    amostras = [0.0, 0.5, 1.0, 1.5, 2.0]
    linhas = []
    for ta in amostras:
        idx = int(round(ta / (t[1] - t[0])))
        idx = min(idx, len(t) - 1)
        linhas.append([
            f"{t[idx]:.2f}",
            f"{tau_load_of_t(t[idx]) * 1000:.2f}",
            f"{v_linear[idx]:.4f}",
            f"{erro_v[idx]:.4f}",
            f"{erro_pct[idx]:.2f}",
        ])

    print()
    viz.tabela(
        ["t [s]", "tau_carga [mN.m]", "v real [m/s]", "erro [m/s]", "erro [%]"],
        linhas,
        titulo_tabela="Degradação do erro de velocidade em malha aberta",
    )

    viz.figura_resposta_degrau(t, v_linear, y_ref=v_alvo,
                                titulo_fig="Malha aberta sob rampa de carga — v(t) se afasta do alvo",
                                ylabel="velocidade linear [m/s]",
                                nome_arquivo="aula01_malha_aberta_falha.png")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print(f"  Sem realimentação, o erro de velocidade cresce até {erro_pct[-1]:.1f}% ao final da rampa de")
    print("  carga — e o controlador não tem como saber disso, porque não está medindo a")
    print("  saída. Isso viola qualquer requisito razoável de precisão de velocidade do")
    print("  NexaBot. A solução (medir e realimentar) começa na Aula 5.")

    if erro_pct[-1] < 1.0:
        print(viz.amarelo("\n  Aviso: o erro ficou pequeno demais para ilustrar bem o ponto — "
                           "aumente tau_load_max."))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
