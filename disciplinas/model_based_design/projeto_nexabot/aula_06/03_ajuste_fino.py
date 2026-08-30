#!/usr/bin/env python3
"""Aula 6 — Script 3/5: comparação de sintonias e ajuste fino manual.

O que este script demonstra
----------------------------
Compara três sintonias de PID para o MESMO degrau de referência de
velocidade (400 rad/s, partindo do repouso, o mesmo cenário do script 2):

  (a) Ziegler-Nichols clássico ("classic_pid")   — agressiva por construção;
  (b) Ziegler-Nichols "no overshoot"              — Ki/Kp bem maior, pensada
      para reduzir o overshoot em processos com atraso dominante;
  (c) um ajuste manual (Kp=1.3, Ki=15, Kd=0.01)   — ver raciocínio abaixo.

Achado importante (e honesto) deste experimento: para um degrau desta
magnitude, `Kp . erro_inicial` já excede `V_max = 24 V` para QUALQUER ganho
proporcional razoável (Kp=2.21 => 2.21x400=884 V; mesmo Kp=0.74 => 296 V).
Ou seja, o atuador satura em ±24 V logo no início e permanece saturado por
boa parte da subida — a rampa inicial de w(t) é, na prática, limitada pela
física do motor em tensão máxima, não pelos ganhos do PID. É por isso que o
tempo de subida sai praticamente IDÊNTICO nas três sintonias (~159 ms) e o
overshoot das sintonias de ZN (que diferem só em Kp/Ki, não em como tratam a
saturação) fica na mesma faixa (~24,8%).

O ajuste manual (c) ataca exatamente esse ponto: ele reduz Ki drasticamente
em relação ao ZN clássico (de 241,7 para 15 — a integral clássica "carrega"
muito torque residual durante a saturação, e é esse torque acumulado que
sustenta o overshoot depois que a velocidade já passou da referência) e
acrescenta um Kd modesto para amortecer a aproximação final. O resultado:
overshoot menor E menor ISE, ao custo de um tempo de acomodação um pouco
maior. Foi encontrado por tentativa e erro, testando várias combinações de
Kp/Ki/Kd e comparando overshoot x ISE x tempo de acomodação.

Como rodar
----------
    .venv/bin/python aula_06/03_ajuste_fino.py
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

# Ku e Tu encontrados em aula_06/01_ganho_critico.py (mesma origem do script 2).
KU_ENCONTRADO = 3.6911
TU_ENCONTRADO_S = 0.018324


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
    print(viz.titulo("NexaBot — Aula 6 — Ajuste fino: comparação de três sintonias de PID"))

    w_ref = 400.0  # rad/s ~= 1,0 m/s, mesmo degrau do script 2
    t_end = 1.2

    def r_of_t(t):
        return w_ref

    sintonias = {
        "ZN classic_pid": ziegler_nichols(KU_ENCONTRADO, TU_ENCONTRADO_S, kind="classic_pid"),
        "ZN no_overshoot": ziegler_nichols(KU_ENCONTRADO, TU_ENCONTRADO_S, kind="no_overshoot"),
        "Manual (Kp=1.3,Ki=15,Kd=0.01)": (1.3, 15.0, 0.01),
    }

    linhas = []
    curvas = {}
    for nome, (Kp, Ki, Kd) in sintonias.items():
        pid = DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=PARAMS.Ts)
        t, X, U = simular_malha_fechada_pid(pid, r_of_t, t_end, PARAMS.Ts)
        w = X[:, 1]
        m = step_metrics(t, w, w_ref)
        erro = w_ref - w
        # numpy >= 2.0 renomeou trapz para trapezoid (mesma integral trapezoidal)
        ise = float(np.trapezoid(erro ** 2, t))
        curvas[nome] = (t, w, U)
        linhas.append([
            nome,
            f"{Kp:.3f}/{Ki:.2f}/{Kd:.4f}",
            f"{m['overshoot_pct']:.2f}",
            f"{m['t_rise_s'] * 1000:.1f}",
            f"{m['t_settle_s'] * 1000:.1f}",
            f"{m['steady_state_error']:.4f}",
            f"{ise:.1f}",
        ])

    viz.tabela(
        ["sintonia", "Kp/Ki/Kd", "overshoot [%]", "t_subida [ms]",
         "t_acomod. [ms]", "erro regime [rad/s]", "ISE"],
        linhas,
        titulo_tabela=f"Comparação de sintonias — degrau de {w_ref:.0f} rad/s ({PARAMS.omega_to_v(w_ref):.2f} m/s)",
    )

    print(viz.negrito("\nGráficos de w(t) das três sintonias:\n"))
    for nome, (t, w, U) in curvas.items():
        viz.plot_ascii(t, w, altura=12, largura=60,
                        titulo_grafico=f"w(t) — {nome}", y_ref=w_ref, unidade_y="rad/s")
        print()

    print(viz.negrito("Recomendação para o NexaBot:"))
    print("  As duas sintonias de Ziegler-Nichols saturam o atuador em ±24 V logo no")
    print("  início do degrau (Kp.erro inicial >> V_max em ambas), o que faz o tempo de")
    print("  subida ficar praticamente igual (~159 ms) e o overshoot ficar preso na")
    print("  mesma faixa (~24,8%) nas duas — a física do motor em tensão máxima, e não")
    print("  os ganhos, domina a subida.")
    print("  A sintonia MANUAL reduz Ki (menos torque integral acumulado durante a")
    print("  saturação) e adiciona um Kd modesto: o overshoot cai para ~22,8% E o ISE")
    print("  cai para o menor dos três (~9470, contra ~9930 do ZN), ao custo de um")
    print("  tempo de acomodação um pouco maior (~669 ms vs ~587-634 ms).")
    print("  Recomendação: a sintonia MANUAL é a mais adequada para o NexaBot — um AGV")
    print("  que carrega paletes tem mais a perder com overshoot de velocidade (risco de")
    print("  a carga escorregar) do que com uma acomodação ~40-80 ms mais lenta.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
