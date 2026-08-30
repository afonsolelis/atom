#!/usr/bin/env python3
"""Aula 4 — Script 2/5: alocação de polos por realimentação de estados.

O que este script demonstra
----------------------------
Como o NexaBot é totalmente controlável (script 1 desta aula), `control.place`
consegue calcular um ganho K tal que os autovalores de (A - B.K) caiam
EXATAMENTE onde pedirmos. A lei de controle usada é

    u(t) = -K.x(t) + Nbar.r

com pré-compensação de ganho estático Nbar = 1 / (C.(-(A-B.K))^-1.B), que
garante erro nulo em regime para uma referência degrau r (sem precisar de
ação integral) — desde que a tensão calculada não sature.

Dois cenários são comparados para uma referência de 400 rad/s (1,0 m/s):

  (a) polos MODERADOS — cerca de 2-3x mais rápidos que os polos de malha
      aberta (-335,96 e -7,22 rad/s): polos em -700 e -20.
  (b) polos AGRESSIVOS — de ~10x (no polo dominante) a mais de 400x (no polo
      lento) mais rápidos: polos em -3000 e -3500.

Para cada cenário simulamos DUAS versões da mesma lei de controle:

  - "ideal": u(t) sem qualquer limite (o que a matemática de alocação de
    polos pede, sem levar em conta o mundo físico);
  - "real": u(t) saturado em ±V_max = ±24 V (`np.clip`), que é o que o
    driver do NexaBot de fato consegue entregar.

O ponto pedagógico: alocar polos MUITO mais rápidos parece "melhor" no papel
(resposta linear ideal muitíssimo mais rápida), mas exige um pico de tensão
gigantesco e ILUSÓRIO — o atuador real satura em 24 V, e a resposta real
passa a ser ditada pela saturação, não pela alocação de polos escolhida.

Como rodar
----------
    .venv/bin/python aula_04/02_alocacao_polos.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import state_space_matrices, derivative  # noqa: E402
from nexabot.controllers import state_feedback_gain, step_metrics  # noqa: E402


def ganho_pre_compensacao(A: np.ndarray, B: np.ndarray, C: np.ndarray, K: np.ndarray) -> float:
    """Calcula Nbar = 1 / (C.(-(A-B.K))^-1.B) para erro nulo de regime em y=r."""
    A_malha_fechada = A - B @ K
    M = -C @ np.linalg.inv(A_malha_fechada) @ B
    return float(1.0 / M[0, 0])


def simular_malha_fechada_estados(K: np.ndarray, Nbar: float, x_ref: float,
                                   t_end: float, dt: float = 1.0e-5,
                                   saturar: bool = True, p: NexaBotParams = PARAMS):
    """Simula x_dot = A.x + B.u, u = -K.x + Nbar.r, via RK4 manual.

    Devolve (t, X, U) com X[:, 1] a velocidade angular e U a tensão de
    comando efetivamente aplicada (já saturada, se `saturar=True`).
    """
    n = int(round(t_end / dt))
    t = np.linspace(0.0, n * dt, n + 1)
    X = np.zeros((n + 1, 2))
    U = np.zeros(n + 1)
    x = np.zeros(2)

    for k in range(n):
        u_ideal = float((-K @ x + Nbar * x_ref).item())
        u = float(np.clip(u_ideal, -p.V_max, p.V_max)) if saturar else u_ideal
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
    print(viz.titulo("NexaBot — Aula 4 — Alocação de polos: o preço da agressividade"))

    A, B, C, D = state_space_matrices(PARAMS)
    polos_malha_aberta = np.linalg.eigvals(A)
    print("Polos de malha aberta:", ", ".join(f"{p:.3f}" for p in polos_malha_aberta.real))

    x_ref = PARAMS.v_to_omega(1.0)  # 400 rad/s = 1,0 m/s
    t_end = 0.3
    dt = 1.0e-5

    cenarios = [
        ("moderado", [-700.0, -20.0]),
        ("agressivo", [-3000.0, -3500.0]),
    ]

    # ordena por magnitude para comparar polo lento-com-lento e rápido-com-rápido
    # (a alocação de polos não preserva a "identidade" elétrica/mecânica de cada
    # polo, então a comparação de razão só faz sentido pareando por magnitude)
    ol_ordenado = sorted(polos_malha_aberta.real, key=abs)

    linhas_resumo = []
    for nome, polos in cenarios:
        K = state_feedback_gain(polos, PARAMS)
        Nbar = ganho_pre_compensacao(A, B, C, K)
        polos_ordenados = sorted(polos, key=abs)
        razoes = [polos_ordenados[i] / ol_ordenado[i] for i in range(2)]

        t_id, X_id, U_id = simular_malha_fechada_estados(K, Nbar, x_ref, t_end, dt, saturar=False)
        t_rl, X_rl, U_rl = simular_malha_fechada_estados(K, Nbar, x_ref, t_end, dt, saturar=True)

        u_pico_ideal = float(np.max(np.abs(U_id)))
        met_ideal = step_metrics(t_id, X_id[:, 1], x_ref)
        met_real = step_metrics(t_rl, X_rl[:, 1], x_ref)
        satura = u_pico_ideal > PARAMS.V_max

        print(viz.titulo(
            f"Cenário {nome.upper()}  —  polos em {polos[0]:.0f} e {polos[1]:.0f} rad/s "
            f"({razoes[0]:.1f}x e {razoes[1]:.1f}x mais rápidos que os polos de malha aberta "
            f"pareados por magnitude)", largura=78))
        print(f"K = [{K[0, 0]:.4f}, {K[0, 1]:.4f}]   |   Nbar = {Nbar:.4f}\n")

        viz.plot_ascii(t_id, U_id, altura=12, largura=64,
                        titulo_grafico=f"[{nome}] Tensão de comando IDEAL u(t) — sem saturar",
                        y_ref=PARAMS.V_max, unidade_y="V")
        print()
        viz.plot_ascii(t_rl, X_rl[:, 1], altura=12, largura=64,
                        titulo_grafico=f"[{nome}] Velocidade angular w(t) — lei REAL (saturada em ±24V)",
                        y_ref=x_ref, unidade_y="rad/s")
        print()

        viz.tabela(
            ["grandeza", "lei ideal (sem sat.)", "lei real (sat. ±24V)"],
            [
                ["pico de |u(t)| [V]", f"{u_pico_ideal:.2f}", f"{float(np.max(np.abs(U_rl))):.2f}"],
                ["excede V_max=24V?",
                 viz.vermelho("SIM") if satura else viz.verde("não"), "— (sempre ≤24V por construção)"],
                ["overshoot [%]", f"{met_ideal['overshoot_pct']:.3f}", f"{met_real['overshoot_pct']:.3f}"],
                ["tempo de acomodação [ms]", f"{met_ideal['t_settle_s'] * 1000:.2f}",
                 f"{met_real['t_settle_s'] * 1000:.2f}"],
                ["erro de regime [rad/s]", f"{met_ideal['steady_state_error']:.4f}",
                 f"{met_real['steady_state_error']:.4f}"],
                ["velocidade final [rad/s]", f"{met_ideal['y_final']:.2f}", f"{met_real['y_final']:.2f}"],
            ],
            titulo_tabela=f"Cenário {nome}: ideal vs. real (referência = {x_ref:.0f} rad/s)",
        )
        print()

        viz.figura_resposta_degrau(
            t_rl, X_rl[:, 1], y_ref=x_ref,
            titulo_fig=f"NexaBot — alocação de polos {nome} (polos {polos[0]:.0f}, {polos[1]:.0f}) — saturado",
            ylabel="velocidade angular w [rad/s]",
            nome_arquivo=f"aula04_alocacao_{nome}.png",
        )

        linhas_resumo.append([
            nome, f"{polos[0]:.0f}, {polos[1]:.0f}", f"{u_pico_ideal:.1f}",
            viz.vermelho("SATURA") if satura else viz.verde("não satura"),
            f"{met_real['t_settle_s'] * 1000:.1f}",
        ])

    print(viz.titulo("Resumo comparativo dos dois cenários", largura=78))
    viz.tabela(
        ["cenário", "polos [rad/s]", "pico u ideal [V]", "saturação?", "t. acomodação real [ms]"],
        linhas_resumo,
        titulo_tabela=f"Referência de velocidade: {x_ref:.0f} rad/s (1,0 m/s)  |  V_max = {PARAMS.V_max:.0f} V",
    )

    print(viz.negrito("\nPonto pedagógico:"))
    print("  O cenário AGRESSIVO promete, na matemática linear ideal, uma resposta de")
    print("  poucos milissegundos — mas para isso exige um pico de tensão de dezenas de")
    print("  MILHARES de volts, fisicamente impossível (o driver entrega no máximo 24 V).")
    print("  Quando a saturação é respeitada, a resposta REAL do cenário agressivo deixa")
    print("  de ser ditada pelos polos escolhidos e passa a ser ditada pelo limite do")
    print("  atuador: o controlador vira, na prática, um comando liga/desliga em ±24 V.")
    print("  Alocar polos sem checar a tensão exigida é ILUSÓRIO: o projeto só é válido")
    print("  se a lei de controle respeitar V_max em toda a faixa de operação esperada.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
