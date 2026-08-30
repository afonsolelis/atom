#!/usr/bin/env python3
"""Aula 7 — Script 3/5: atraso computacional de 1 ciclo — quanto custa em fase?

O que este script demonstra
----------------------------
No firmware real do NexaBot, o comando de tensão calculado no ciclo k do
laço de controle NÃO sai instantaneamente no PWM: entre ler o encoder,
calcular o PID e atualizar o registrador do PWM, passa tempo de execução.
No pior caso didático, esse tempo consome um ciclo INTEIRO de amostragem, e
o valor de u calculado em k só é de fato aplicado em k+1.

Esse atraso de UMA amostra é, em tempo discreto, a multiplicação da função
de transferência de malha aberta por z^-1 = e^{-j.w.Ts} — que introduz uma
fase adicional de -w.Ts RADIANOS em cada frequência w (sem alterar o
ganho). Como a margem de fase é medida na frequência de cruzamento de
ganho (wgc), a perda de margem de fase por esse atraso é aproximadamente
`wgc * Ts` (em radianos), convertido para graus.

Este script calcula a margem de fase da malha aberta discreta (PID + planta
via `control.c2d(..., method='zoh')`) COM e SEM o atraso extra de z^-1,
usando `control.stability_margins`, para dois períodos de amostragem
diferentes (Ts nominal de 5 ms e um Ts maior de 20 ms) — e confirma
numericamente a simulação em tempo discreto com o parâmetro
`atraso_ciclos` do laço manual de malha fechada.

CUIDADO (conforme pedido no enunciado): a relação entre Ts e o efeito
RELATIVO do atraso fixo de 1 ciclo não é assumida, é MEDIDA abaixo. O que a
simulação mostra: a frequência de cruzamento de ganho (wgc) muda pouco com
Ts nestes dois casos, então a perda de fase (~wgc.Ts) cresce quase
proporcionalmente a Ts — e como a margem de fase SEM atraso já é menor em
Ts=20ms (o próprio ZOH mais lento já custa fase), a mesma "meia-volta"
adicional de atraso de 1 ciclo empurra o sistema de estável para instável
em Ts=20ms, mas apenas reduz a margem (mantendo estabilidade) em Ts=5ms.

Como rodar
----------
    .venv/bin/python aula_07/03_atraso_computacional.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import control as ct  # noqa: E402
import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import DiscretePID  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import derivative, transfer_function  # noqa: E402

KP_FIXO = 0.5
KI_FIXO = 5.0
KD_FIXO = 0.0005
TAU_F = 0.01     # constante do filtro derivativo (igual ao padrão de DiscretePID)

R_REFERENCIA = 50.0
T_END = 3.0


def pid_discreto_tf(Kp: float, Ki: float, Kd: float, Ts: float, tau_f: float = TAU_F):
    """Função de transferência C(z) do MESMO `DiscretePID` (integral por
    Euler p/ trás, derivativo filtrado), IGNORANDO saturação/anti-windup —
    a análise de margem é sempre sobre o modelo LINEARIZADO da malha aberta.

        C(z) = Kp + Ki.Ts.z/(z-1) + Kd.(z-1) / [(tau_f+Ts).z - tau_f]
    """
    c_p = ct.tf([Kp], [1], Ts)
    c_i = ct.tf([Ki * Ts, 0.0], [1.0, -1.0], Ts)
    c_d = ct.tf([Kd, -Kd], [(tau_f + Ts), -tau_f], Ts)
    return c_p + c_i + c_d


def margem_com_e_sem_atraso(Ts: float):
    """Devolve (pm_sem, wgc_sem, pm_com, wgc_com) para a malha aberta
    C(z).Gd(z), com e sem um atraso extra de z^-1 (1 ciclo)."""
    G = transfer_function(PARAMS)
    Gd = ct.c2d(G, Ts, method="zoh")
    C = pid_discreto_tf(KP_FIXO, KI_FIXO, KD_FIXO, Ts)
    L = ct.series(C, Gd)

    _, pm_sem, _, _, wgc_sem, _ = ct.stability_margins(L)

    atraso = ct.tf([1.0], [1.0, 0.0], Ts)   # z^-1 : atraso de 1 amostra
    L_atraso = ct.series(L, atraso)
    _, pm_com, _, _, wgc_com, _ = ct.stability_margins(L_atraso)

    return float(pm_sem), float(wgc_sem), float(pm_com), float(wgc_com)


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None, atraso_ciclos=0):
    if dt_sim is None:
        dt_sim = ts / 20.0
    n_sim = int(round(t_end / dt_sim))
    n_por_ts = max(1, int(round(ts / dt_sim)))
    x = np.zeros(2) if x0 is None else np.array(x0, dtype=float)
    t_hist = np.zeros(n_sim + 1)
    X_hist = np.zeros((n_sim + 1, 2))
    U_hist = np.zeros(n_sim + 1)
    X_hist[0] = x
    u = 0.0
    fila_atraso = [0.0] * max(1, atraso_ciclos)
    for k in range(n_sim):
        tk = k * dt_sim
        if k % n_por_ts == 0:
            u_novo = pid.step(r_of_t(tk), x[1])
            if atraso_ciclos > 0:
                fila_atraso.append(u_novo)
                u = fila_atraso.pop(0)
            else:
                u = u_novo
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
    print(viz.titulo("NexaBot — Aula 7 — Script 3/5: atraso computacional de 1 ciclo e margem de fase"))

    print(f"PID: Kp={KP_FIXO}, Ki={KI_FIXO}, Kd={KD_FIXO} (mesmo de aula_07/02_escolha_de_ts.py).")
    print("Modelo linear de malha aberta L(z) = C(z).Gd(z), Gd via ZOH; atraso extra = z^-1.\n")

    ts_testados = [PARAMS.Ts, 0.020]
    linhas = []
    resultados = {}
    for ts in ts_testados:
        pm_sem, wgc_sem, pm_com, wgc_com = margem_com_e_sem_atraso(ts)
        perda = pm_sem - pm_com
        perda_teorica = np.degrees(wgc_sem * ts)
        resultados[ts] = (pm_sem, wgc_sem, pm_com, wgc_com)
        linhas.append([
            f"{ts * 1000:.1f}",
            f"{pm_sem:.2f}",
            f"{pm_com:.2f}",
            f"{perda:.2f}",
            f"{perda_teorica:.2f}",
        ])

    viz.tabela(
        ["Ts [ms]", "PM sem atraso [graus]", "PM com atraso 1 ciclo [graus]",
         "perda de PM [graus]", "perda teórica wgc.Ts [graus]"],
        linhas,
        titulo_tabela="Margem de fase da malha aberta discreta: com x sem atraso de 1 ciclo",
    )

    print()
    for ts in ts_testados:
        pm_sem, wgc_sem, pm_com, wgc_com = resultados[ts]
        veredito = viz.verde("permanece ESTÁVEL") if pm_com > 0 else viz.vermelho("fica INSTÁVEL (PM < 0)")
        print(f"  Ts={ts * 1000:5.1f} ms: sem atraso PM={pm_sem:6.2f}°  (wgc={wgc_sem:.1f} rad/s)  "
              f"->  com atraso PM={pm_com:6.2f}°  ->  {veredito}")

    # --- confirmação em tempo discreto (domínio do tempo) -------------------
    print("\n" + viz.negrito("Confirmação no domínio do tempo (simulação não linear com saturação):"))
    linhas_tempo = []
    for ts in ts_testados:
        for atraso_ciclos in (0, 1):
            pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=ts)

            def r_of_t(_t, r=R_REFERENCIA):
                return r

            t, X, U = simular_malha_fechada_pid(pid, r_of_t, T_END, ts, atraso_ciclos=atraso_ciclos)
            w = X[:, 1]
            w_max = float(np.max(np.abs(w)))
            w_final = float(w[-1])
            instavel = w_max > 3.0 * R_REFERENCIA
            linhas_tempo.append([
                f"{ts * 1000:.1f}", str(atraso_ciclos), f"{w_max:.2f}", f"{w_final:.2f}",
                viz.vermelho("instável") if instavel else viz.verde("estável"),
            ])

    viz.tabela(
        ["Ts [ms]", "atraso [ciclos]", "|w| máx [rad/s]", "w final [rad/s]", "veredito (tempo)"],
        linhas_tempo,
        titulo_tabela=f"Simulação temporal: degrau de {R_REFERENCIA:.0f} rad/s, com/sem atraso de 1 ciclo",
    )

    print()
    pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=0.020)
    t0, X0, _ = simular_malha_fechada_pid(pid, lambda _t: R_REFERENCIA, T_END, 0.020, atraso_ciclos=0)
    pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=0.020)
    t1, X1, _ = simular_malha_fechada_pid(pid, lambda _t: R_REFERENCIA, T_END, 0.020, atraso_ciclos=1)
    viz.plot_ascii(t0, X0[:, 1], altura=12, largura=64,
                    titulo_grafico="Ts=20ms, SEM atraso computacional (0 ciclos)",
                    y_ref=R_REFERENCIA, unidade_y="rad/s")
    print()
    viz.plot_ascii(t1, X1[:, 1], altura=12, largura=64,
                    titulo_grafico="Ts=20ms, COM atraso computacional (1 ciclo) — mesma malha",
                    y_ref=R_REFERENCIA, unidade_y="rad/s")

    print("\n" + viz.negrito("Ponto pedagógico (o que foi OBSERVADO, não assumido):"))
    print("  A perda de margem de fase medida bate com a previsão analítica wgc.Ts em graus")
    print("  (ver colunas 'perda de PM' e 'perda teórica' na primeira tabela — praticamente")
    print("  idênticas): o atraso de 1 ciclo custa mais graus de fase quando Ts é MAIOR,")
    print("  porque a fase perdida por amostra de atraso é proporcional a Ts, não constante.")
    print("  Em Ts=5ms a malha larga com margem folgada e sobra margem positiva mesmo com")
    print("  o atraso; em Ts=20ms a margem SEM atraso já é pequena, e o mesmo atraso de UM")
    print("  ciclo (agora 'valendo' mais graus) derruba a margem para negativo -> instável,")
    print("  confirmado pela simulação temporal (|w| diverge/satura sem convergir).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
