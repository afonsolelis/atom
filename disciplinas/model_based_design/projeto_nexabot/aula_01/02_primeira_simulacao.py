#!/usr/bin/env python3
"""Aula 1 — Script 2/5: do zero à primeira resposta ao degrau do NexaBot.

O que este script demonstra
----------------------------
Em poucas linhas de código: carregar os parâmetros identificados do NexaBot,
aplicar um degrau de tensão ao motor e observar a velocidade angular subir
até o regime permanente. É a primeira simulação da disciplina inteira — o
"hello world" de Model-Based Design: antes de qualquer controlador, é
preciso ver a planta em malha aberta respondendo a uma entrada conhecida.

O ponto pedagógico principal aparece no console: em malha aberta, aplicar
um degrau de tensão NÃO leva a velocidade a um valor de referência
desejado — leva ao ganho estático vezes a tensão, e só. Se você quer 1,0
m/s de verdade, ou calcula a tensão exata (o que a Aula 5 mostra ser frágil)
ou fecha a malha (Aula 5 em diante).

Como rodar
----------
    .venv/bin/python aula_01/02_primeira_simulacao.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import simulate  # noqa: E402


def main() -> int:
    print(viz.titulo("NexaBot — Aula 1 — Primeira simulação: degrau de tensão em malha aberta"))

    V_degrau = 12.0  # metade da tensão máxima do driver
    t_end = 0.8

    print(f"Aplicando um degrau de V = {V_degrau:.1f} V (V_max = {PARAMS.V_max:.0f} V) "
          f"por {t_end:.1f} s, partindo do repouso...\n")

    def u_of_t(t):
        return V_degrau if t >= 0 else 0.0

    t, X = simulate(u_of_t, t_end=t_end, dt=1.0e-4, p=PARAMS)
    corrente = X[:, 0]
    omega = X[:, 1]
    v_linear = PARAMS.omega_to_v(omega)

    omega_regime = V_degrau * PARAMS.dc_gain
    v_regime = PARAMS.omega_to_v(omega_regime)

    viz.plot_ascii(t, omega, altura=14, largura=64,
                    titulo_grafico="Velocidade angular do motor  w(t)  [rad/s]",
                    y_ref=omega_regime, unidade_y="rad/s")
    print()
    viz.plot_ascii(t, corrente, altura=10, largura=64,
                    titulo_grafico="Corrente de armadura  i(t)  [A]", unidade_y="A")
    print()

    viz.tabela(
        ["grandeza", "valor", "unidade"],
        [
            ["tensão aplicada (degrau)", f"{V_degrau:.2f}", "V"],
            ["ganho DC do motor", f"{PARAMS.dc_gain:.4f}", "rad/(s.V)"],
            ["velocidade angular em regime", f"{omega_regime:.2f}", "rad/s"],
            ["velocidade linear em regime", f"{v_regime:.4f}", "m/s"],
            ["corrente de pico", f"{corrente.max():.3f}", "A"],
            ["corrente em regime", f"{corrente[-1]:.3f}", "A"],
            ["constante de tempo elétrica (L/R)", f"{PARAMS.tau_elec * 1000:.3f}", "ms"],
            ["constante de tempo mecânica (J.R/(Kt.Ke))", f"{PARAMS.tau_mech * 1000:.2f}", "ms"],
        ],
        titulo_tabela="Resumo numérico da primeira simulação",
    )

    viz.figura_resposta_degrau(t, v_linear, y_ref=v_regime,
                                titulo_fig=f"NexaBot — degrau de {V_degrau:.0f} V em malha aberta",
                                ylabel="velocidade linear [m/s]",
                                nome_arquivo="aula01_primeira_simulacao.png")

    v_exigido = PARAMS.v_to_omega(1.0) / PARAMS.dc_gain
    print("\n" + viz.negrito("Ponto pedagógico:"))
    print("  Em malha aberta, a velocidade de regime é IMPOSTA pelo ganho DC do motor,")
    print("  não escolhida livremente. Para andar a 1,0 m/s de verdade seria preciso")
    print(f"  aplicar V = {v_exigido:.2f} V EXATAMENTE — e isso muda se a carga, a bateria")
    print("  ou o atrito mudarem (ver aula_01/03_malha_aberta_falha.py).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
