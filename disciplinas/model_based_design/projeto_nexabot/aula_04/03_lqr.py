#!/usr/bin/env python3
"""Aula 4 — Script 3/5: LQR — o compromisso entre desempenho e esforço de controle.

O que este script demonstra
----------------------------
A alocação de polos do script anterior escolhe os polos "no escuro": o
projetista decide um número (-700, -3000...) sem nenhuma medida direta de
quanto esforço de controle aquilo custa. O regulador linear quadrático (LQR)
inverte essa lógica: o projetista escolhe PESOS — Q para o estado, R para o
esforço de controle — e o algoritmo devolve o ganho K que minimiza

    J = integral( x^T.Q.x + u^T.R.u ) dt

Este script varre uma grade de pesos Q = diag([1, q2]) (penaliza o desvio de
velocidade — o segundo estado) e R = [[r]] (penaliza a tensão aplicada), com
q2 em {1, 10, 100, 1000} e r em {0,01, 0,1, 1, 10}. Para cada combinação:

1. Calcula K, S, E via `nexabot.controllers.lqr_gain(Q, R)`.
2. Fecha a malha com pré-compensação Nbar (mesma técnica do script 2) e
   simula (SEM saturar, para isolar o efeito do peso na lei ideal) uma
   referência degrau de 400 rad/s (1,0 m/s).
3. Mede desempenho (`step_metrics`: overshoot, tempo de acomodação) e
   esforço de controle (pico de |u(t)| e a integral de u²(t), proporcional à
   energia elétrica dissipada em comandar o motor).

A tabela final deixa claro o padrão: aumentar q2 (penalizar mais o erro de
velocidade) ou diminuir r (penalizar menos o esforço) sempre torna a
resposta mais rápida — e sempre exige mais tensão/energia para isso. Não há
almoço grátis: desempenho rápido tem um preço em esforço de controle, e
esse preço pode facilmente ultrapassar os 24 V do driver do NexaBot.

Como rodar
----------
    .venv/bin/python aula_04/03_lqr.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import state_space_matrices, derivative  # noqa: E402
from nexabot.controllers import lqr_gain, step_metrics  # noqa: E402


def ganho_pre_compensacao(A: np.ndarray, B: np.ndarray, C: np.ndarray, K: np.ndarray) -> float:
    """Calcula Nbar = 1 / (C.(-(A-B.K))^-1.B) para erro nulo de regime em y=r."""
    A_malha_fechada = A - B @ K
    M = -C @ np.linalg.inv(A_malha_fechada) @ B
    return float(1.0 / M[0, 0])


def simular_malha_fechada_estados(K: np.ndarray, Nbar: float, x_ref: float,
                                   t_end: float, dt: float = 1.0e-4,
                                   p: NexaBotParams = PARAMS):
    """Simula x_dot = A.x + B.u, u = -K.x + Nbar.r, via RK4 manual (sem saturar).

    Devolve (t, X, U). Não satura de propósito: o objetivo aqui é comparar a
    lei de controle IDEAL de cada ponto da grade (Q, R), não o comportamento
    sob limitação do atuador (isso já foi coberto no script 2).
    """
    n = int(round(t_end / dt))
    t = np.linspace(0.0, n * dt, n + 1)
    X = np.zeros((n + 1, 2))
    U = np.zeros(n + 1)
    x = np.zeros(2)

    for k in range(n):
        u = float((-K @ x + Nbar * x_ref).item())
        U[k] = u
        k1 = derivative(x, u, 0.0, p)
        k2 = derivative(x + 0.5 * dt * k1, u, 0.0, p)
        k3 = derivative(x + 0.5 * dt * k2, u, 0.0, p)
        k4 = derivative(x + dt * k3, u, 0.0, p)
        x = x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        X[k + 1] = x

    U[-1] = U[-2]
    return t, X, U


def main() -> int:
    print(viz.titulo("NexaBot — Aula 4 — LQR: desempenho x esforço de controle"))

    A, B, C, D = state_space_matrices(PARAMS)
    x_ref = PARAMS.v_to_omega(1.0)  # 400 rad/s = 1,0 m/s
    t_end = 0.3
    dt = 1.0e-4

    valores_q2 = [1.0, 10.0, 100.0, 1000.0]
    valores_r = [0.01, 0.1, 1.0, 10.0]

    print(f"Referência de velocidade: {x_ref:.0f} rad/s (1,0 m/s)  |  V_max = {PARAMS.V_max:.0f} V")
    print(f"Grade: Q = diag([1, q2]) com q2 em {valores_q2}, R = [[r]] com r em {valores_r}\n")

    linhas = []
    resultados = []
    for q2 in valores_q2:
        for r in valores_r:
            Q = np.diag([1.0, q2])
            R = np.array([[r]])
            K, S, E = lqr_gain(Q, R, PARAMS)
            Nbar = ganho_pre_compensacao(A, B, C, K)

            t, X, U = simular_malha_fechada_estados(K, Nbar, x_ref, t_end, dt, PARAMS)
            met = step_metrics(t, X[:, 1], x_ref)
            u_pico = float(np.max(np.abs(U)))
            u_integral2 = float(np.trapezoid(U ** 2, t))

            resultados.append(dict(q2=q2, r=r, K=K, u_pico=u_pico, u_integral2=u_integral2,
                                    overshoot=met["overshoot_pct"], t_settle=met["t_settle_s"]))
            linhas.append([
                f"{q2:.0f}", f"{r:.2f}",
                f"{K[0, 0]:.2f}", f"{K[0, 1]:.2f}",
                f"{met['overshoot_pct']:.2f}",
                f"{met['t_settle_s'] * 1000:.2f}",
                f"{u_pico:.1f}",
                (viz.vermelho(f"{u_pico:.0f}") if u_pico > PARAMS.V_max else viz.verde(f"{u_pico:.0f}")),
                f"{u_integral2:.2f}",
            ])

    viz.tabela(
        ["q2", "r", "K_i", "K_w", "overshoot%", "t_acom.[ms]", "pico|u|[V]", "vs V_max", "∫u²dt"],
        linhas,
        titulo_tabela="Varredura Q=diag([1,q2]), R=[[r]]  (lei ideal, sem saturar)",
    )

    # --- Destaques: mais suave vs. mais agressivo da grade -------------------
    mais_suave = min(resultados, key=lambda d: d["u_integral2"])
    mais_agressivo = max(resultados, key=lambda d: d["u_integral2"])

    print()
    viz.tabela(
        ["extremo da grade", "q2", "r", "t_acomodação [ms]", "pico |u| [V]", "∫u²dt"],
        [
            ["mais suave (menor ∫u²dt)", f"{mais_suave['q2']:.0f}", f"{mais_suave['r']:.2f}",
             f"{mais_suave['t_settle'] * 1000:.2f}", f"{mais_suave['u_pico']:.1f}",
             f"{mais_suave['u_integral2']:.2f}"],
            ["mais agressivo (maior ∫u²dt)", f"{mais_agressivo['q2']:.0f}", f"{mais_agressivo['r']:.2f}",
             f"{mais_agressivo['t_settle'] * 1000:.2f}", f"{mais_agressivo['u_pico']:.1f}",
             f"{mais_agressivo['u_integral2']:.2f}"],
        ],
        titulo_tabela="Os dois extremos observados na varredura",
    )

    # gráfico ASCII comparando a resposta dos dois extremos
    K_suave, Nbar_suave = mais_suave["K"], ganho_pre_compensacao(A, B, C, mais_suave["K"])
    K_agr, Nbar_agr = mais_agressivo["K"], ganho_pre_compensacao(A, B, C, mais_agressivo["K"])
    t_s, X_s, U_s = simular_malha_fechada_estados(K_suave, Nbar_suave, x_ref, t_end, dt, PARAMS)
    t_a, X_a, U_a = simular_malha_fechada_estados(K_agr, Nbar_agr, x_ref, t_end, dt, PARAMS)

    print()
    viz.plot_ascii(t_s, X_s[:, 1], altura=12, largura=64,
                    titulo_grafico=f"Resposta MAIS SUAVE (q2={mais_suave['q2']:.0f}, r={mais_suave['r']:.2f})",
                    y_ref=x_ref, unidade_y="rad/s")
    print()
    viz.plot_ascii(t_a, X_a[:, 1], altura=12, largura=64,
                    titulo_grafico=f"Resposta MAIS AGRESSIVA (q2={mais_agressivo['q2']:.0f}, "
                                    f"r={mais_agressivo['r']:.2f})",
                    y_ref=x_ref, unidade_y="rad/s")

    viz.figura_resposta_degrau(
        t_a, U_a, y_ref=PARAMS.V_max,
        titulo_fig="NexaBot — tensão de comando no extremo mais agressivo da grade LQR",
        ylabel="tensão de comando u(t) [V]",
        nome_arquivo="aula04_lqr_esforco_agressivo.png",
    )

    print(viz.negrito("\nPonto pedagógico:"))
    print("  Ao longo da grade inteira, aumentar q2 (penalizar mais o erro de velocidade)")
    print("  OU diminuir r (penalizar menos a tensão) sempre reduz o tempo de acomodação —")
    print("  e sempre aumenta o pico de tensão e a energia (∫u²dt) exigidos. O LQR não")
    print("  cria desempenho de graça: ele só torna EXPLÍCITO o compromisso que a alocação")
    print("  de polos do script 2 escondia atrás de números escolhidos às cegas. Qualquer")
    print(f"  combinação com pico de |u| acima de {PARAMS.V_max:.0f} V (destacada em vermelho na")
    print("  tabela) é, na prática, tão ilusória quanto o cenário agressivo do script 2.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
