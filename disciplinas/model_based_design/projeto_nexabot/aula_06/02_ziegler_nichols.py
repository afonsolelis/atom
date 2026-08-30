#!/usr/bin/env python3
"""Aula 6 — Script 2/5: sintonia de Ziegler-Nichols a partir de Ku e Tu.

O que este script demonstra
----------------------------
De posse do ganho crítico e do período de oscilação sustentada encontrados
no script anterior (`01_ganho_critico.py`), este script aplica a receita
clássica de Ziegler-Nichols (`nexabot.controllers.ziegler_nichols`, tabela
"classic_pid": Kp=0.60.Ku, Ki=1.20.Ku/Tu, Kd=0.075.Ku.Tu) para obter os três
ganhos do PID, monta um `DiscretePID` real com eles e simula a resposta a um
degrau de referência de velocidade — 400 rad/s, equivalente a 1,0 m/s no
NexaBot — partindo do repouso, na malha planta-contínua + PID-discreto a
Ts = 5 ms (o mesmo loop manual RK4 do script 1).

As métricas de `step_metrics` (overshoot, tempo de subida, tempo de
acomodação, erro em regime) mostram o traço característico do ZN clássico:
resposta rápida, mas com overshoot considerável — o preço de uma sintonia
"agressiva por construção". O script 3 compara essa sintonia com alternativas
mais conservadoras.

Ku e Tu usados abaixo (hardcoded, com a origem documentada no comentário):
foram os valores ENCONTRADOS ao rodar `aula_06/01_ganho_critico.py` nesta
mesma máquina, não valores inventados — Ku ~= 3.6911, Tu ~= 18.324 ms.

Como rodar
----------
    .venv/bin/python aula_06/02_ziegler_nichols.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import derivative  # noqa: E402
from nexabot.controllers import DiscretePID, ziegler_nichols, step_metrics  # noqa: E402

# Valores encontrados em aula_06/01_ganho_critico.py (busca por bisseção na
# malha discreta a Ts=5ms) — NÃO recalculados aqui de propósito, para deixar
# explícito que a sintonia de ZN parte de um experimento já realizado.
KU_ENCONTRADO = 3.6911
TU_ENCONTRADO_S = 0.018324  # 18.324 ms


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None):
    """Simula a malha fechada planta-contínua + PID-discreto (ZOH em Ts)."""
    if dt_sim is None:
        dt_sim = ts / 10.0
    n_sim = int(round(t_end / dt_sim))
    n_por_ts = max(1, int(round(ts / dt_sim)))
    x = np.zeros(2) if x0 is None else np.array(x0, dtype=float)
    t_hist = np.zeros(n_sim + 1)
    X_hist = np.zeros((n_sim + 1, 2))
    U_hist = np.zeros(n_sim + 1)
    X_hist[0] = x
    u = 0.0
    for k in range(n_sim):
        tk = k * dt_sim
        if k % n_por_ts == 0:
            u = pid.step(r_of_t(tk), x[1])
        tl = tau_load_of_t(tk) if tau_load_of_t else 0.0
        k1 = derivative(x, u, tl, p)
        k2 = derivative(x + 0.5 * dt_sim * k1, u, tl, p)
        k3 = derivative(x + 0.5 * dt_sim * k2, u, tl, p)
        k4 = derivative(x + dt_sim * k3, u, tl, p)
        x = x + (dt_sim / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t_hist[k + 1] = tk + dt_sim
        X_hist[k + 1] = x
        U_hist[k + 1] = u
    return t_hist, X_hist, U_hist


def main() -> int:
    print(viz.titulo("NexaBot — Aula 6 — Sintonia de Ziegler-Nichols (ganho crítico)"))

    print(f"Ku = {KU_ENCONTRADO:.4f}  e  Tu = {TU_ENCONTRADO_S * 1000:.3f} ms")
    print("(valores obtidos rodando aula_06/01_ganho_critico.py nesta mesma máquina)\n")

    Kp, Ki, Kd = ziegler_nichols(KU_ENCONTRADO, TU_ENCONTRADO_S, kind="classic_pid")

    viz.tabela(
        ["ganho", "fórmula (classic_pid)", "valor"],
        [
            ["Kp", "0.60 . Ku", f"{Kp:.4f}"],
            ["Ki", "1.20 . Ku / Tu", f"{Ki:.4f}"],
            ["Kd", "0.075 . Ku . Tu", f"{Kd:.6f}"],
        ],
        titulo_tabela="Ganhos de Ziegler-Nichols clássico",
    )

    pid = DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=PARAMS.Ts)

    w_ref = 400.0  # rad/s ~= 1,0 m/s de velocidade linear no NexaBot
    v_ref = PARAMS.omega_to_v(w_ref)
    t_end = 1.2

    def r_of_t(t):
        return w_ref

    print(f"\nDegrau de referência: w_ref = {w_ref:.0f} rad/s ({v_ref:.3f} m/s), partindo do repouso.\n")

    t, X, U = simular_malha_fechada_pid(pid, r_of_t, t_end, PARAMS.Ts)
    w = X[:, 1]

    viz.plot_ascii(t, w, altura=14, largura=64,
                    titulo_grafico="Velocidade angular w(t) — resposta ao degrau (ZN clássico)",
                    y_ref=w_ref, unidade_y="rad/s")
    print()
    viz.plot_ascii(t, U, altura=10, largura=64,
                    titulo_grafico="Tensão de comando u(t)", unidade_y="V")

    metricas = step_metrics(t, w, w_ref)

    viz.tabela(
        ["métrica", "valor", "unidade"],
        [
            ["overshoot", f"{metricas['overshoot_pct']:.2f}", "%"],
            ["tempo de subida (10-90%)", f"{metricas['t_rise_s'] * 1000:.1f}", "ms"],
            ["tempo de acomodação (faixa 2%)", f"{metricas['t_settle_s'] * 1000:.1f}", "ms"],
            ["erro em regime", f"{metricas['steady_state_error']:.4f}", "rad/s"],
            ["valor final", f"{metricas['y_final']:.2f}", "rad/s"],
            ["tensão de comando de pico", f"{np.max(np.abs(U)):.2f}", "V"],
        ],
        titulo_tabela="Métricas da resposta ao degrau — Ziegler-Nichols clássico",
    )

    viz.figura_resposta_degrau(
        t, w, y_ref=w_ref,
        titulo_fig="NexaBot — degrau de 400 rad/s, PID Ziegler-Nichols clássico",
        ylabel="velocidade angular w [rad/s]",
        nome_arquivo="aula06_ziegler_nichols.png",
    )

    print(viz.negrito("\nPonto pedagógico:"))
    print("  A sintonia de ZN clássico é deliberadamente agressiva: ela entrega")
    print(f"  resposta rápida (subida em {metricas['t_rise_s']*1000:.0f} ms) à custa de um overshoot de")
    print(f"  {metricas['overshoot_pct']:.1f}% e de saturar o atuador em ±{PARAMS.V_max:.0f} V durante o transitório.")
    print("  Para o NexaBot — um AGV com carga sobre a plataforma — esse overshoot pode")
    print("  ser inaceitável. O script 3 compara esta sintonia com alternativas.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
