#!/usr/bin/env python3
"""Aula 7 — Script 4/5: quantização de encoder e de PWM — qual efeito domina?

O que este script demonstra
----------------------------
Nenhum sensor ou atuador digital tem resolução infinita. Este script injeta
DOIS efeitos de quantização, cada um isolado do outro, na mesma malha
fechada PID do NexaBot:

  - ENCODER incremental: a posição angular do motor é acumulada e
    arredondada para CONTAGENS INTEIRAS de pulso (128 ou 2048 pulsos por
    volta do eixo do motor); a velocidade realimentada ao PID é a diferença
    de contagens dividida por Ts — exatamente como um firmware real mede
    velocidade a partir de um encoder incremental (mesma ideia de
    `nexabot.identificacao.gerar_ensaio_degrau`, reimplementada aqui de
    forma simplificada, sem reimportar aquele módulo).
  - PWM: o comando de tensão calculado pelo PID é arredondado para o nível
    mais próximo representável em N bits sobre a faixa +-V_max (passo =
    2.V_max / 2^N), simulando um driver PWM/DAC de resolução finita.

Cada teste ISOLA um efeito de cada vez (quando testamos o encoder, o PWM é
ideal — resolução "infinita" — e vice-versa) para deixar claro qual efeito
domina o desempenho nesta malha específica.

Como rodar
----------
    .venv/bin/python aula_07/04_quantizacao.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import DiscretePID, step_metrics  # noqa: E402
from nexabot.params import PARAMS, NexaBotParams  # noqa: E402
from nexabot.plant import derivative  # noqa: E402

KP_FIXO = 0.5
KI_FIXO = 5.0
KD_FIXO = 0.0005
R_REFERENCIA = 50.0
T_END = 1.5


def simular_malha_com_quantizacao(pid, r: float, t_end: float, ts: float,
                                   contagens_por_volta: float | None = None,
                                   pwm_bits: int | None = None,
                                   dt_sim: float | None = None,
                                   p: NexaBotParams = PARAMS):
    """Malha fechada PID com quantização OPCIONAL de encoder e/ou PWM.

    `contagens_por_volta=None` => velocidade realimentada é a verdadeira
    (encoder "ideal"/resolução infinita). `pwm_bits=None` => tensão de
    comando não é arredondada (PWM "ideal").

    A posição angular é acumulada por integração trapezoidal a cada passo
    fino `dt_sim` (mesma ideia de `identificacao.gerar_ensaio_degrau`); a
    cada `ts`, o número de contagens acumuladas é arredondado para inteiro
    e a velocidade medida é a diferença de contagens dividida por `ts`.
    """
    if dt_sim is None:
        dt_sim = ts / 20.0
    n_sim = int(round(t_end / dt_sim))
    n_por_ts = max(1, int(round(ts / dt_sim)))

    contagens_por_rad = (contagens_por_volta / (2.0 * np.pi)) if contagens_por_volta else None
    passo_pwm = (2.0 * p.V_max / (2 ** pwm_bits)) if pwm_bits else None

    x = np.zeros(2)
    t_hist = np.zeros(n_sim + 1)
    w_hist = np.zeros(n_sim + 1)
    u_hist = np.zeros(n_sim + 1)
    w_medido_hist = np.zeros(n_sim + 1)

    theta_acumulado = 0.0
    contagem_anterior = 0
    w_medido = 0.0
    u = 0.0

    for k in range(n_sim):
        tk = k * dt_sim
        w_antes = x[1]

        if k % n_por_ts == 0:
            if contagens_por_rad is not None:
                contagem_atual = int(round(theta_acumulado * contagens_por_rad))
                w_medido = (contagem_atual - contagem_anterior) / contagens_por_rad / ts
                contagem_anterior = contagem_atual
            else:
                w_medido = x[1]

            u_novo = pid.step(r, w_medido)
            if passo_pwm is not None:
                u_novo = float(np.round(u_novo / passo_pwm) * passo_pwm)
                u_novo = min(max(u_novo, -p.V_max), p.V_max)
            u = u_novo

        k1 = derivative(x, u, 0.0, p)
        k2 = derivative(x + 0.5 * dt_sim * k1, u, 0.0, p)
        k3 = derivative(x + 0.5 * dt_sim * k2, u, 0.0, p)
        k4 = derivative(x + dt_sim * k3, u, 0.0, p)
        x = x + (dt_sim / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        # integração trapezoidal da posição angular verdadeira (para o encoder)
        theta_acumulado += 0.5 * (w_antes + x[1]) * dt_sim

        t_hist[k + 1] = tk + dt_sim
        w_hist[k + 1] = x[1]
        u_hist[k + 1] = u
        w_medido_hist[k + 1] = w_medido

    return t_hist, w_hist, u_hist, w_medido_hist


def linha_resultado(nome, t, w, u):
    m = step_metrics(t, w, R_REFERENCIA)
    metade = len(u) // 2
    chattering_u = float(np.std(u[metade:]))
    ruido_w = float(np.std(w[metade:] - R_REFERENCIA))
    return [
        nome, f"{m['overshoot_pct']:.2f}", f"{m['steady_state_error']:.4f}",
        f"{chattering_u:.4f}", f"{ruido_w:.4f}",
    ]


def main() -> int:
    print(viz.titulo("NexaBot — Aula 7 — Script 4/5: quantização de encoder e de PWM"))

    print(f"PID: Kp={KP_FIXO}, Ki={KI_FIXO}, Kd={KD_FIXO}; Ts = PARAMS.Ts = "
          f"{PARAMS.Ts * 1000:.1f} ms; degrau de referência w_ref = {R_REFERENCIA:.0f} rad/s.\n")

    # --- baseline sem nenhuma quantização (referência de comparação) -------
    pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=PARAMS.Ts)
    t_ideal, w_ideal, u_ideal, _ = simular_malha_com_quantizacao(
        pid, R_REFERENCIA, T_END, PARAMS.Ts)

    linhas_encoder = [linha_resultado("ideal (sem quantização)", t_ideal, w_ideal, u_ideal)]
    linhas_pwm = [linha_resultado("ideal (sem quantização)", t_ideal, w_ideal, u_ideal)]

    print(viz.negrito("Teste 1/2 — ENCODER isolado (PWM ideal, resolução infinita):"))
    resultados_encoder = {}
    for cpv in (128, 2048):
        pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=PARAMS.Ts)
        t, w, u, w_med = simular_malha_com_quantizacao(
            pid, R_REFERENCIA, T_END, PARAMS.Ts, contagens_por_volta=cpv)
        resultados_encoder[cpv] = (t, w, u)
        linhas_encoder.append(linha_resultado(f"{cpv} pulsos/volta", t, w, u))

    viz.tabela(
        ["configuração", "sobressinal [%]", "erro em regime [rad/s]",
         "chattering de u (std) [V]", "ruído de w (std) [rad/s]"],
        linhas_encoder,
        titulo_tabela="Efeito da resolução do ENCODER (PWM ideal)",
    )

    print("\n" + viz.negrito("Teste 2/2 — PWM isolado (encoder ideal, resolução infinita):"))
    resultados_pwm = {}
    for bits in (8, 12):
        pid = DiscretePID(Kp=KP_FIXO, Ki=KI_FIXO, Kd=KD_FIXO, Ts=PARAMS.Ts)
        t, w, u, w_med = simular_malha_com_quantizacao(
            pid, R_REFERENCIA, T_END, PARAMS.Ts, pwm_bits=bits)
        resultados_pwm[bits] = (t, w, u)
        passo = 2.0 * PARAMS.V_max / (2 ** bits)
        linhas_pwm.append(linha_resultado(f"{bits} bits (passo={passo:.4f} V)", t, w, u))

    viz.tabela(
        ["configuração", "sobressinal [%]", "erro em regime [rad/s]",
         "chattering de u (std) [V]", "ruído de w (std) [rad/s]"],
        linhas_pwm,
        titulo_tabela="Efeito da resolução do PWM (encoder ideal)",
    )

    print()
    t128, w128, u128 = resultados_encoder[128]
    t2048, w2048, u2048 = resultados_encoder[2048]
    viz.plot_ascii(t128, w128, altura=12, largura=64,
                    titulo_grafico="Encoder de 128 pulsos/volta — w(t) medido pelo PID",
                    y_ref=R_REFERENCIA, unidade_y="rad/s")
    print()
    viz.plot_ascii(t2048, w2048, altura=12, largura=64,
                    titulo_grafico="Encoder de 2048 pulsos/volta — w(t) medido pelo PID",
                    y_ref=R_REFERENCIA, unidade_y="rad/s")
    print()
    print(viz.negrito("Chattering do comando de tensão u(t) (2a metade da simulação):"))
    print("  128 ppr:  ", end="")
    viz.sparkline(u128[len(u128) // 2:])
    print("  2048 ppr: ", end="")
    viz.sparkline(u2048[len(u2048) // 2:])
    t8, w8, u8 = resultados_pwm[8]
    t12, w12, u12 = resultados_pwm[12]
    print("  PWM  8 b: ", end="")
    viz.sparkline(u8[len(u8) // 2:])
    print("  PWM 12 b: ", end="")
    viz.sparkline(u12[len(u12) // 2:])

    razao_chatter = float(np.std(u128[len(u128) // 2:]) / (np.std(u8[len(u8) // 2:]) + 1e-9))
    print("\n" + viz.negrito("Ponto pedagógico:"))
    print(f"  A resolução do ENCODER domina o desempenho desta malha: o chattering do")
    print(f"  comando de tensão com 128 pulsos/volta é ~{razao_chatter:.0f}x maior que com PWM de")
    print("  8 bits, e o erro em regime com encoder grosseiro (128 ppr) fica na ordem de")
    print("  grandeza de 1 rad/s, contra erro praticamente nulo com PWM grosseiro (8 bits).")
    print("  Faz sentido fisicamente: o ruído de quantização do SENSOR entra direto na")
    print("  malha de realimentação (afeta o termo proporcional E o integral do PID a")
    print("  cada ciclo); o degrau de quantização do ATUADOR é só uma pequena distorção")
    print("  sobre um sinal de comando que já está sendo filtrado pela inércia mecânica")
    print("  da planta (constante de tempo mecânica ~148 ms >> Ts de 5 ms).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
