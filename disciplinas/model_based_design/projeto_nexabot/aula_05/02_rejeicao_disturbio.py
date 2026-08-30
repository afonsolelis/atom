#!/usr/bin/env python3
"""Aula 5 — Script 2/4: rejeição a distúrbio — malha aberta vs malha fechada.

O que este script demonstra
----------------------------
O NexaBot cruzando a 1,0 m/s (400 rad/s no motor) recebe, no meio do
trajeto, um DEGRAU de torque de carga equivalente a 30% do torque nominal
(ex.: o operador acabou de empilhar mais um palete). O mesmo evento é
simulado em dois cenários, a partir da mesma condição inicial de regime:

  - MALHA ABERTA: a tensão fica fixa no valor calculado para o ponto de
    operação sem carga (`V_regime`). Ninguém mede a velocidade, então
    ninguém corrige nada quando o torque aumenta.
  - MALHA FECHADA: um PID discreto (`DiscretePID`, `Ts = PARAMS.Ts`) mede a
    velocidade angular a cada período de amostragem e ajusta a tensão para
    manter a referência.

O laço de malha fechada é um integrador RK4 manual chamando
`nexabot.plant.derivative` a cada passo fino e `DiscretePID.step` a cada
`Ts` — o mesmo padrão que, na Unidade 4, passa a rodar dentro do FMU em C.

O ponto pedagógico: a malha aberta se estabiliza em uma velocidade NOVA e
errada (o distúrbio simplesmente desloca o ponto de operação, e ninguém
percebe); a malha fechada volta à referência porque mede o erro e o corrige.

Como rodar
----------
    .venv/bin/python aula_05/02_rejeicao_disturbio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import DiscretePID  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import derivative, simulate  # noqa: E402


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None):
    """Integra a planta em malha fechada com um `DiscretePID` amostrado a `ts`.

    RK4 de passo fixo `dt_sim` (padrão `ts/10`) para a planta contínua;
    `pid.step` só é chamado a cada `ts` (amostragem do controlador
    embarcado), como convém a um sistema de controle digital real.
    """
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


def tempo_recuperacao(t, omega, omega_alvo, t_disturbio, banda=0.02):
    """Tempo, a partir de `t_disturbio`, até `omega` voltar e PERMANECER

    dentro de `banda` (fração) do alvo. Devolve `0.0` se nunca chegou a sair
    da faixa e `None` se nunca volta a entrar (dentro da janela simulada).
    """
    mask = t >= t_disturbio
    tt = t[mask]
    erro_rel = np.abs(omega[mask] - omega_alvo) / omega_alvo
    fora = np.where(erro_rel > banda)[0]
    if len(fora) == 0:
        return 0.0
    ultimo_fora = fora[-1]
    if ultimo_fora + 1 >= len(tt):
        return None
    return float(tt[ultimo_fora + 1] - t_disturbio)


def main() -> int:
    print(viz.titulo("NexaBot — Aula 5 — Rejeição a distúrbio: malha aberta vs malha fechada"))

    p = PARAMS
    v_alvo = 1.0  # m/s
    omega_alvo = p.v_to_omega(v_alvo)
    V_regime = omega_alvo / p.dc_gain  # tensão de regime SEM carga
    tau_load_max = 0.30 * p.Kt * p.i_max  # degrau de 30% do torque nominal

    t_disturbio = 0.10
    t_end = 0.60

    print(f"Alvo de cruzeiro: v = {v_alvo:.2f} m/s ({omega_alvo:.1f} rad/s no motor).")
    print(f"Tensão de regime sem carga: V_regime = {V_regime:.3f} V.")
    print(f"Em t = {t_disturbio:.2f} s aplica-se um DEGRAU de torque de carga "
          f"tau_load = {tau_load_max * 1000:.1f} mN.m (30% do torque nominal a i_max).\n")

    # Condição inicial: já em regime permanente (sem carga) no instante t=0,
    # igual ao padrão de aula_01/03_malha_aberta_falha.py.
    i0 = p.b * omega_alvo / p.Kt
    x0 = np.array([i0, omega_alvo])

    def tau_load_of_t(t):
        return tau_load_max if t >= t_disturbio else 0.0

    # --- Malha aberta: tensão fixa, nunca recalculada ----------------------
    def u_of_t(_t):
        return V_regime

    t_ol, X_ol = simulate(u_of_t, t_end=t_end, dt=1.0e-4, x0=x0,
                           tau_load_of_t=tau_load_of_t, p=p)
    omega_ol = X_ol[:, 1]
    v_ol = p.omega_to_v(omega_ol)

    # --- Malha fechada: PID discreto, Ts = PARAMS.Ts -----------------------
    Kp, Ki, Kd = 2.0, 50.0, 0.001
    pid = DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=p.Ts, u_max=p.V_max)
    # O robô já está de cruzeiro há tempo suficiente para o integrador do PID
    # estar "no ponto": inicializa-se o estado interno no valor de regime
    # (mesmo raciocínio de aula_01/03 ao partir x0 já em regime permanente).
    pid.integral = V_regime

    def r_of_t(_t):
        return omega_alvo

    t_cl, X_cl, U_cl = simular_malha_fechada_pid(
        pid, r_of_t, t_end, p.Ts, tau_load_of_t=tau_load_of_t, p=p, x0=x0)
    omega_cl = X_cl[:, 1]
    v_cl = p.omega_to_v(omega_cl)

    erro_final_ol = v_alvo - v_ol[-1]
    erro_final_cl = v_alvo - v_cl[-1]
    rec_ol = tempo_recuperacao(t_ol, omega_ol, omega_alvo, t_disturbio, banda=0.02)
    rec_cl = tempo_recuperacao(t_cl, omega_cl, omega_alvo, t_disturbio, banda=0.02)

    viz.plot_ascii(t_ol, v_ol, altura=13, largura=64,
                    titulo_grafico="Malha ABERTA — v(t) sob degrau de torque de carga",
                    y_ref=v_alvo, unidade_y="m/s")
    print()
    viz.plot_ascii(t_cl, v_cl, altura=13, largura=64,
                    titulo_grafico="Malha FECHADA (PID) — v(t) sob o mesmo degrau de torque",
                    y_ref=v_alvo, unidade_y="m/s")

    def fmt_rec(rec):
        if rec is None:
            return "não recupera"
        return f"{rec * 1000:.2f} ms" if rec > 0 else "nunca saiu da faixa ±2%"

    print()
    viz.tabela(
        ["grandeza", "malha aberta", "malha fechada (PID)"],
        [
            ["velocidade final", f"{v_ol[-1]:.4f} m/s", f"{v_cl[-1]:.4f} m/s"],
            ["erro final", f"{erro_final_ol:.4f} m/s ({erro_final_ol / v_alvo * 100:.1f} %)",
             f"{erro_final_cl:.6f} m/s ({erro_final_cl / v_alvo * 100:.3f} %)"],
            ["tempo de recuperação (±2%)", fmt_rec(rec_ol), fmt_rec(rec_cl)],
            ["tensão final aplicada", f"{V_regime:.2f} V (fixa)", f"{U_cl[-1]:.2f} V"],
            ["tensão de pico pós-distúrbio", "—", f"{U_cl[int(len(U_cl) * t_disturbio / t_end):].max():.2f} V"],
        ],
        titulo_tabela="Comparação de rejeição ao distúrbio de carga",
    )

    viz.figura_resposta_degrau(
        t_ol, v_ol, y_ref=v_alvo,
        titulo_fig="NexaBot — malha aberta sob degrau de torque de carga",
        ylabel="velocidade linear [m/s]",
        nome_arquivo="aula05_rejeicao_malha_aberta.png")
    viz.figura_resposta_degrau(
        t_cl, v_cl, y_ref=v_alvo,
        titulo_fig="NexaBot — malha fechada (PID) sob o mesmo degrau de torque",
        ylabel="velocidade linear [m/s]",
        nome_arquivo="aula05_rejeicao_malha_fechada.png")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print(f"  O mesmo degrau de carga desloca a malha aberta para um NOVO regime, "
          f"{erro_final_ol / v_alvo * 100:.1f}% abaixo")
    print("  do alvo, e ela fica lá — ninguém está medindo a velocidade para saber que")
    print("  algo mudou. A malha fechada mede o erro a cada Ts e realimenta: o erro")
    print(f"  final cai para {abs(erro_final_cl) / v_alvo * 100:.3f}%, essencialmente zero. Isso É rejeição a")
    print("  distúrbio — o assunto do script 3 (sensibilidade) em termos de frequência.")

    if abs(erro_final_cl) < abs(erro_final_ol) * 0.1:
        print(viz.verde(viz.negrito(
            "\nMalha fechada rejeitou o distúrbio (erro final <10% do erro em malha aberta).")))
        return 0
    print(viz.vermelho(viz.negrito("\nMalha fechada não rejeitou bem o distúrbio — recalibre o PID.")))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
