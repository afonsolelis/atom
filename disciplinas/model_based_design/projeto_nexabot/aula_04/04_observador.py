#!/usr/bin/env python3
"""Aula 4 — Script 4/5: observador de estados (filtro de Luenberger).

O que este script demonstra
----------------------------
Toda a realimentação de estados dos scripts 2 e 3 desta aula assume que o
controlador conhece x(t) = [corrente, velocidade] inteiro. Na prática, o
NexaBot só tem um encoder no eixo — mede w (a velocidade angular), NÃO a
corrente de armadura i. Instalar um sensor de corrente é possível, mas custa
dinheiro, espaço e mais um canal de ruído: o observador de Luenberger propõe
ESTIMAR i a partir só de w e da tensão aplicada, sem sensor de corrente.

A ideia: rodar, em paralelo com a planta real, uma CÓPIA do modelo (A, B)
corrigida pelo erro de saída (y - C.x_hat), ponderado por um ganho L:

    x_hat_dot = A.x_hat + B.u + L.(y - C.x_hat)

O erro de estimação e = x - x_hat obedece e_dot = (A - L.C).e — uma dinâmica
que não depende da entrada u, só dos autovalores de (A - L.C). Como o
NexaBot é observável (script 1 desta aula, posto(Wo) = 2), `control.place`
consegue posicionar esses autovalores onde quisermos: aqui, 3-5x mais
rápidos que a malha fechada de referência (polos moderados do script 2, em
-700 e -20 rad/s), para que o observador convirja bem antes de o controlador
precisar da estimativa.

Este script aplica um degrau de TENSÃO (malha aberta, para isolar o efeito
do observador do efeito do controlador) e mostra a corrente REAL simulada
pela planta lado a lado com a corrente ESTIMADA pelo observador, convergindo
uma para a outra mesmo partindo de estimativas iniciais diferentes.

Como rodar
----------
    .venv/bin/python aula_04/04_observador.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402
import control as ct  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import state_space_matrices, derivative  # noqa: E402


def ganho_observador(A: np.ndarray, C: np.ndarray, polos_observador) -> np.ndarray:
    """Calcula L por alocação de polos do sistema DUAL (A^T, C^T).

    O erro de estimação e_dot = (A - L.C).e tem a mesma estrutura de um
    problema de realimentação de estados no sistema transposto: alocar os
    autovalores de (A - L.C) equivale a alocar os de (A^T - C^T.L^T) via
    `control.place(A^T, C^T, polos)`, e então transpor o resultado.
    """
    return np.asarray(ct.place(A.T, C.T, polos_observador)).T


def simular_planta_e_observador(V_degrau: float, L: np.ndarray, t_end: float,
                                 dt: float = 1.0e-5, x0=None, x0_hat=None,
                                 p: NexaBotParams = PARAMS):
    """Simula a planta real e o observador em paralelo, RK4 manual, entrada = degrau de V.

    Devolve (t, X, X_hat) com X e X_hat de forma (n_amostras, 2).
    """
    A, B, C, D = state_space_matrices(p)
    Bv = B.flatten()
    Lv = L.flatten()

    n = int(round(t_end / dt))
    t = np.linspace(0.0, n * dt, n + 1)
    x = np.zeros(2) if x0 is None else np.array(x0, dtype=float)
    x_hat = np.zeros(2) if x0_hat is None else np.array(x0_hat, dtype=float)
    X = np.zeros((n + 1, 2))
    X_hat = np.zeros((n + 1, 2))
    X[0], X_hat[0] = x, x_hat

    for k in range(n):
        u = V_degrau

        k1 = derivative(x, u, 0.0, p)
        k2 = derivative(x + 0.5 * dt * k1, u, 0.0, p)
        k3 = derivative(x + 0.5 * dt * k2, u, 0.0, p)
        k4 = derivative(x + dt * k3, u, 0.0, p)
        x = x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        y = float((C @ x).item())

        def obs_deriv(xh):
            return A @ xh + Bv * u + Lv * (y - float((C @ xh).item()))

        k1o = obs_deriv(x_hat)
        k2o = obs_deriv(x_hat + 0.5 * dt * k1o)
        k3o = obs_deriv(x_hat + 0.5 * dt * k2o)
        k4o = obs_deriv(x_hat + dt * k3o)
        x_hat = x_hat + (dt / 6.0) * (k1o + 2 * k2o + 2 * k3o + k4o)

        X[k + 1], X_hat[k + 1] = x, x_hat

    return t, X, X_hat


def main() -> int:
    print(viz.titulo("NexaBot — Aula 4 — Observador de estados: estimando a corrente sem sensor"))

    A, B, C, D = state_space_matrices(PARAMS)

    # polos de malha fechada de referência: cenário "moderado" do script 2
    polos_malha_fechada = [-700.0, -20.0]
    # observador 3-5x mais rápido que a malha fechada (fator ~3,6x e ~4x aqui)
    polos_observador = [-2500.0, -80.0]

    L = ganho_observador(A, C, polos_observador)
    autovalores_erro = np.linalg.eigvals(A - L @ C)

    print(f"Polos de malha fechada de referência (script 2, cenário moderado): "
          f"{polos_malha_fechada}")
    print(f"Polos do observador escolhidos (~3,6x e ~4,0x mais rápidos): {polos_observador}\n")

    viz.tabela(
        ["grandeza", "valor"],
        [
            ["L (ganho do observador)", f"[{L[0, 0]:.2f}, {L[1, 0]:.2f}]^T"],
            ["autovalores de (A - L.C)", f"{autovalores_erro[0]:.2f}, {autovalores_erro[1]:.2f}"],
            ["autovalores pedidos", f"{polos_observador[0]:.2f}, {polos_observador[1]:.2f}"],
        ],
        titulo_tabela="Projeto do observador por alocação de polos do erro",
    )

    # --- Simulação: degrau de tensão, observador parte de estimativa ERRADA --
    V_degrau = 12.0
    t_end = 0.15
    dt = 1.0e-5
    x0 = np.array([0.0, 0.0])         # planta real parte do repouso
    x0_hat = np.array([1.0, 30.0])    # observador começa com um "chute" ERRADO de propósito

    t, X, X_hat = simular_planta_e_observador(V_degrau, L, t_end, dt, x0=x0, x0_hat=x0_hat)
    corrente_real = X[:, 0]
    corrente_est = X_hat[:, 0]
    erro = corrente_real - corrente_est

    print(f"\nDegrau de tensão V = {V_degrau:.1f} V aplicado à planta e ao observador em paralelo.\n")

    viz.plot_ascii(t, corrente_real, altura=13, largura=64,
                    titulo_grafico="Corrente REAL simulada  i(t)  [A]", unidade_y="A")
    print()
    viz.plot_ascii(t, corrente_est, altura=13, largura=64,
                    titulo_grafico="Corrente ESTIMADA pelo observador  î(t)  [A]", unidade_y="A")
    print()
    viz.plot_ascii(t, erro, altura=10, largura=64,
                    titulo_grafico="Erro de estimação de corrente  i(t) - î(t)  [A]",
                    y_ref=0.0, unidade_y="A")

    instantes_ms = [0.0, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 40.0, 80.0, 150.0]
    linhas = []
    for tt_ms in instantes_ms:
        idx = min(int(round((tt_ms / 1000.0) / dt)), len(t) - 1)
        linhas.append([
            f"{tt_ms:.2f}",
            f"{corrente_real[idx]:.5f}",
            f"{corrente_est[idx]:.5f}",
            f"{erro[idx]:.6f}",
        ])

    print()
    viz.tabela(
        ["t [ms]", "i real [A]", "î estimada [A]", "erro [A]"],
        linhas,
        titulo_tabela="Convergência da estimativa de corrente ao longo do tempo",
    )

    erro_final = float(erro[-1])
    erro_pico = float(np.max(np.abs(erro)))
    print(f"\nErro de estimação: pico = {erro_pico:.6f} A  |  ao final de {t_end * 1000:.0f} ms = "
          f"{erro_final:.6f} A")

    viz.figura_resposta_degrau(
        t, corrente_real, y_ref=None,
        titulo_fig="NexaBot — corrente real vs. estimada pelo observador de Luenberger",
        ylabel="corrente de armadura [A]",
        nome_arquivo="aula04_observador_corrente_real.png",
    )
    fig_est = viz.figura_resposta_degrau(
        t, corrente_est, y_ref=None,
        titulo_fig="NexaBot — corrente ESTIMADA pelo observador",
        ylabel="corrente estimada î(t) [A]",
        nome_arquivo="aula04_observador_corrente_estimada.png",
    )
    del fig_est

    tau_obs_lento = 1000.0 / abs(polos_observador[1])  # ms, constante de tempo do polo mais lento
    convergiu = abs(erro_final) < 0.01
    print(viz.negrito("\nPonto pedagógico:"))
    print("  O observador NUNCA mede a corrente — ele só vê a tensão aplicada e a")
    print("  velocidade medida pelo encoder. Ele partiu de um CHUTE ERRADO de propósito")
    print(f"  (î0={x0_hat[0]:.1f} A, ŵ0={x0_hat[1]:.1f} rad/s, contra i0=w0=0 reais), e o erro chega a")
    print(f"  {erro_pico:.1f} A no transitório inicial — mas decai com a constante de tempo do polo")
    print(f"  mais lento do observador (-{abs(polos_observador[1]):.0f} rad/s → τ≈{tau_obs_lento:.1f} ms),")
    print(f"  ficando praticamente nulo ({erro_final:.6f} A) ao final de {t_end * 1000:.0f} ms — sem nunca")
    print("  medir i diretamente. Isso só é possível porque o sistema é observável: a forma")
    print("  como i afeta dw/dt (via Kt.i/J) deixa uma \"assinatura\" em w(t) que o observador")
    print("  usa para corrigir sua própria estimativa a cada instante.")

    if convergiu:
        print(viz.verde(viz.negrito("\nErro de estimação convergiu para próximo de zero — observador OK.")))
    else:
        print(viz.vermelho(viz.negrito("\nErro de estimação não convergiu como esperado — revise L.")))

    return 0 if convergiu else 1


if __name__ == "__main__":
    raise SystemExit(main())
