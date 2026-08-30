#!/usr/bin/env python3
"""Aula 6 — Script 4/5: efeito do windup e correção por anti-windup (back-calculation).

O que este script demonstra
----------------------------
"Windup" acontece quando o atuador satura (aqui, ±24 V) por tempo prolongado
enquanto o erro continua grande: o termo integral do PID continua acumulando
("carregando") mesmo sem efeito nenhum sobre a planta, porque a tensão já
está no limite. Quando o erro finalmente muda de sinal (ou a referência cai),
o controlador ainda "acha" que precisa de muito mais tensão do que o
necessário — o integrador continua mandando o atuador saturado na direção
errada por um bom tempo, atrasando a correção.

Cenário de demonstração: uma referência de velocidade linear DELIBERADAMENTE
IRREAL de 4,0 m/s — bem acima do limite físico do motor do NexaBot em
V_max=24V contínuos (esse teto físico, `PARAMS.dc_gain * PARAMS.V_max`
convertido para m/s, é de ~1,27 m/s — e também bem acima do limite de
segurança `v_max_safe = 1,20 m/s`) — é aplicada por 0,5 s, forçando o
atuador a ficar saturado o tempo todo (não há tensão possível que atinja
4 m/s). Em seguida a referência cai para um valor seguro e alcançável
(0,5 m/s). O que se mede é: quanto tempo o NexaBot demora para OBEDECER à
nova referência, mais baixa, depois de ter sido mandado acelerar ao
impossível.

Sobre os ganhos usados: o enunciado sugere os ganhos do ZN clássico do
script 2, mas seu Ki=241,72 é tão agressivo que MESMO valores de Kaw bem
acima do sugerido (testamos até 50) não conseguem descarregar o integrador
em poucos segundos — o efeito do anti-windup fica mascarado pela magnitude
do próprio Ki. Por isso usamos aqui o ajuste MANUAL do script 3
(Kp=1,3, Ki=15, Kd=0,01), um Ki "razoável" o bastante para que o mecanismo
de anti-windup mostre seu benefício de forma limpa dentro de poucos segundos
de simulação — o ponto pedagógico (windup existe, back-calculation ajuda) é
o mesmo, só muda o quão rápido ele fica visível na tela.

Roda a MESMA malha fechada duas vezes, mudando apenas `Kaw`:

  1. `Kaw=0.0`  — anti-windup DESLIGADO: o integrador acumula livremente.
  2. `Kaw=2.0`  — anti-windup por back-calculation: o integrador é "puxado
     de volta" proporcionalmente ao quanto o atuador está saturado.

Como rodar
----------
    .venv/bin/python aula_06/04_antiwindup.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import derivative  # noqa: E402
from nexabot.controllers import DiscretePID  # noqa: E402


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None,
                               registrar_integral=False):
    """Simula a malha fechada planta-contínua + PID-discreto (ZOH em Ts).

    Se `registrar_integral=True`, devolve também o histórico do estado
    `pid.integral` amostrado a Ts (só existe nesta variante do script porque
    é o dado central da demonstração de windup).
    """
    if dt_sim is None:
        dt_sim = ts / 10.0
    n_sim = int(round(t_end / dt_sim))
    n_por_ts = max(1, int(round(ts / dt_sim)))
    x = np.zeros(2) if x0 is None else np.array(x0, dtype=float)
    t_hist = np.zeros(n_sim + 1)
    X_hist = np.zeros((n_sim + 1, 2))
    U_hist = np.zeros(n_sim + 1)
    I_hist = np.zeros(n_sim + 1)
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
        I_hist[k + 1] = pid.integral
    if registrar_integral:
        return t_hist, X_hist, U_hist, I_hist
    return t_hist, X_hist, U_hist


def main() -> int:
    print(viz.titulo("NexaBot — Aula 6 — Windup e anti-windup por back-calculation"))

    v_max_fisico = PARAMS.omega_to_v(PARAMS.dc_gain * PARAMS.V_max)
    v_irreal = 4.0
    v_alvo = 0.5
    w_irreal = PARAMS.v_to_omega(v_irreal)
    w_alvo = PARAMS.v_to_omega(v_alvo)
    t_fase1 = 0.5
    t_end = 3.0

    print(f"Velocidade linear máxima FÍSICA do NexaBot em V_max={PARAMS.V_max:.0f} V contínuos: "
          f"{v_max_fisico:.3f} m/s (limite de segurança v_max_safe={PARAMS.v_max_safe:.2f} m/s).")
    print(f"Fase 1 (0 a {t_fase1:.1f} s): referência IRREAL de {v_irreal:.1f} m/s "
          f"({w_irreal:.0f} rad/s) — impossível de atingir, força saturação total.")
    print(f"Fase 2 ({t_fase1:.1f} a {t_end:.1f} s): referência cai para {v_alvo:.1f} m/s "
          f"({w_alvo:.0f} rad/s) — seguro e alcançável.\n")

    def r_of_t(t):
        return w_irreal if t < t_fase1 else w_alvo

    Kp, Ki, Kd = 1.3, 15.0, 0.01
    print(f"Ganhos do PID (ajuste manual do script 3): Kp={Kp}, Ki={Ki}, Kd={Kd}\n")

    banda = 0.02 * w_alvo

    def tempo_de_recuperacao(t, w):
        """Primeiro instante, após a comutação de referência, a partir do qual
        w(t) permanece dentro de 2% do novo alvo até o fim da simulação."""
        pos = t >= t_fase1
        t_pos, w_pos = t[pos], w[pos]
        dentro = np.abs(w_pos - w_alvo) <= banda
        for i in range(len(dentro)):
            if np.all(dentro[i:]):
                return float(t_pos[i] - t_fase1)
        return float("nan")

    resultados = {}
    for label, Kaw in [("SEM anti-windup (Kaw=0.0)", 0.0), ("COM anti-windup (Kaw=2.0)", 2.0)]:
        pid = DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=PARAMS.Ts, Kaw=Kaw)
        t, X, U, I = simular_malha_fechada_pid(pid, r_of_t, t_end, PARAMS.Ts, registrar_integral=True)
        w = X[:, 1]
        idx_switch = int(round(t_fase1 / (PARAMS.Ts / 10.0)))
        overshoot_pos_switch = float(np.max(w[idx_switch:]) - w_alvo) / w_alvo * 100.0
        t_recuperacao = tempo_de_recuperacao(t, w)
        resultados[label] = {
            "t": t, "w": w, "U": U, "I": I,
            "I_na_comutacao": float(I[idx_switch]),
            "I_final": float(I[-1]),
            "overshoot_pos_switch": overshoot_pos_switch,
            "t_recuperacao_s": t_recuperacao,
        }

        print(viz.titulo(label, largura=78))
        viz.plot_ascii(t, w, altura=13, largura=64,
                        titulo_grafico="Velocidade angular w(t)", y_ref=w_alvo, unidade_y="rad/s")
        print()
        viz.plot_ascii(t, U, altura=8, largura=64,
                        titulo_grafico="Tensão de comando u(t) (saturação em ±24V)", unidade_y="V")
        print()

    linhas = []
    for label, r in resultados.items():
        linhas.append([
            label,
            f"{r['I_na_comutacao']:.1f}",
            f"{r['I_final']:.2f}",
            f"{r['overshoot_pos_switch']:.1f}",
            f"{r['t_recuperacao_s'] * 1000:.1f}" if not np.isnan(r["t_recuperacao_s"]) else "não recuperou",
        ])

    viz.tabela(
        ["caso", "integral na comutação", "integral final", "pico pós-comutação [%]",
         "tempo p/ voltar à faixa de 2% [ms]"],
        linhas,
        titulo_tabela="Comparação SEM vs COM anti-windup",
    )

    r_sem = resultados["SEM anti-windup (Kaw=0.0)"]
    r_com = resultados["COM anti-windup (Kaw=2.0)"]
    fator = r_sem["t_recuperacao_s"] / r_com["t_recuperacao_s"] if r_com["t_recuperacao_s"] else float("nan")

    viz.figura_resposta_degrau(
        r_sem["t"], r_sem["w"], y_ref=w_alvo,
        titulo_fig="NexaBot — SEM anti-windup (Kaw=0): recuperação lenta após saturação",
        ylabel="velocidade angular w [rad/s]",
        nome_arquivo="aula06_antiwindup_sem.png",
    )
    viz.figura_resposta_degrau(
        r_com["t"], r_com["w"], y_ref=w_alvo,
        titulo_fig="NexaBot — COM anti-windup (Kaw=2): recuperação rápida após saturação",
        ylabel="velocidade angular w [rad/s]",
        nome_arquivo="aula06_antiwindup_com.png",
    )

    print(viz.negrito("\nPonto pedagógico:"))
    print("  O pico de velocidade após a queda de referência é praticamente o mesmo nos")
    print("  dois casos (~509 rad/s, o teto FÍSICO do motor em V_max) — isso não é efeito")
    print("  do anti-windup, é simplesmente onde a velocidade já estava quando a")
    print("  referência caiu, resultado da fase 1 irrealista. O que o anti-windup muda")
    print("  de verdade é a VELOCIDADE DE RECUPERAÇÃO: sem ele, o integrador continua")
    print(f"  \"carregado\" ({r_sem['I_na_comutacao']:.0f} no instante da comutação) e o NexaBot")
    print(f"  demora {r_sem['t_recuperacao_s']*1000:.0f} ms para obedecer à nova referência; com back-calculation,")
    print(f"  o integrador some muito mais rápido ({r_com['I_na_comutacao']:.0f} na comutação) e a")
    print(f"  recuperação leva só {r_com['t_recuperacao_s']*1000:.0f} ms — cerca de {fator:.1f}x mais rápido.")
    print("  Para um AGV que compartilha corredor com pessoas, esse atraso em obedecer")
    print("  a uma ordem de desaceleração É uma questão de segurança (REQ-SAFE-*), não")
    print("  só de qualidade de controle.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
