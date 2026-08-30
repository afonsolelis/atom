#!/usr/bin/env python3
"""Aula 7 — Script 1/5: discretizar G(s) por Euler, Tustin e ZOH — qual erra menos?

O que este script demonstra
----------------------------
A mesma função de transferência contínua do NexaBot, G(s) = W(s)/V(s), é
discretizada no período de amostragem nominal do firmware (Ts = 5 ms, 200 Hz)
pelos três métodos disponíveis em `control.c2d`:

  - `method='euler'` (a.k.a. `forward_diff`): aproxima s por (z-1)/Ts —
    a integração de Euler para frente, a mais simples e a mais barata de
    implementar em C, mas a que introduz mais erro de discretização.
  - `method='tustin'` (a.k.a. `bilinear`): aproxima s por (2/Ts).(z-1)/(z+1)
    — a transformação bilinear, que preserva melhor a resposta em frequência
    perto da origem porque mapeia EXATAMENTE s=0 em z=1 (ganho DC idêntico).
  - `method='zoh'`: resolve a equação de estados exatamente assumindo que a
    entrada é mantida constante entre amostras (sample-and-hold) — é
    precisamente como um DAC/PWM realmente aplica a tensão ao motor.

As três versões discretas recebem um degrau de 12 V e são comparadas com a
resposta CONTÍNUA de referência (`nexabot.plant.simulate`, RK4 de passo
fino) amostrada nos mesmos instantes.

Ponto pedagógico: para uma entrada em DEGRAU, o ZOH não é "só mais um
método" — ele é MATEMATICAMENTE EXATO, porque a hipótese sob a qual ele é
derivado (entrada constante entre amostras) é exatamente o que a simulação
está fazendo. Euler e Tustin são aproximações da dinâmica contínua e por
isso carregam erro de discretização, mesmo que pequeno neste Ts. Os números
abaixo mostram que a comparação Euler-vs-Tustin não é unânime em todas as
métricas (Tustin acerta melhor o valor final porque preserva o ganho DC
exatamente; Euler tem erro RMS de transitório menor neste caso) — o
estudante deve olhar o número, não decorar uma regra geral.

Como rodar
----------
    .venv/bin/python aula_07/01_euler_tustin_zoh.py
"""

from __future__ import annotations

import os
import sys
import warnings

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import control as ct  # noqa: E402
import numpy as np  # noqa: E402
from scipy.signal import BadCoefficients  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import simulate, transfer_function  # noqa: E402

METODOS = [
    ("euler", "Euler p/ frente (forward_diff): s ~ (z-1)/Ts"),
    ("tustin", "Tustin/bilinear: s ~ (2/Ts).(z-1)/(z+1)"),
    ("zoh", "ZOH (zero-order hold): exato p/ entrada mantida entre amostras"),
]


def discretizar_sem_aviso(G, Ts: float, metodo: str):
    """Aplica `control.c2d` e converte para espaço de estados suprimindo o
    aviso benigno `BadCoefficients` que o Euler dispara (coeficientes do
    numerador discretizado ficam mal-condicionados numericamente, mas o
    resultado da simulação permanece correto — é só a checagem interna do
    scipy sendo conservadora)."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=BadCoefficients)
        Gd = ct.c2d(G, Ts, method=metodo)
        Gd_ss = ct.tf2ss(Gd)
    return Gd, Gd_ss


def main() -> int:
    print(viz.titulo("NexaBot — Aula 7 — Script 1/5: Euler x Tustin x ZOH na discretização de G(s)"))

    G = transfer_function(PARAMS)
    Ts = PARAMS.Ts
    V_degrau = 12.0
    t_end = 0.8

    print(f"G(s) contínua do NexaBot, Ts nominal do firmware = {Ts * 1000:.1f} ms ({1 / Ts:.0f} Hz).")
    print(f"Degrau de V = {V_degrau:.1f} V, comparação até t = {t_end:.1f} s.\n")

    # --- referência contínua (gabarito de verdade) -------------------------
    def u_of_t(t):
        return V_degrau if t >= 0 else 0.0

    t_c, X_c = simulate(u_of_t, t_end=t_end, dt=1.0e-4, p=PARAMS)
    w_c = X_c[:, 1]

    n = int(round(t_end / Ts))
    t_d = np.arange(n + 1) * Ts
    u_d = np.full(n + 1, V_degrau)
    w_c_interp = np.interp(t_d, t_c, w_c)

    respostas = {}
    linhas_tabela = []
    for metodo, descricao in METODOS:
        Gd, Gd_ss = discretizar_sem_aviso(G, Ts, metodo)
        resp = ct.forced_response(Gd_ss, T=t_d, U=u_d)
        w_d = resp.outputs
        respostas[metodo] = w_d

        erro = w_d - w_c_interp
        rms = float(np.sqrt(np.mean(erro ** 2)))
        erro_final = float(erro[-1])
        erro_final_pct = abs(erro_final) / w_c_interp[-1] * 100.0
        erro_pico = float(np.max(np.abs(erro)))

        def _fmt(v: float) -> str:
            return f"{v:.2e}" if abs(v) < 1.0e-6 else f"{v:.4f}"

        linhas_tabela.append([
            metodo, _fmt(rms), _fmt(erro_final),
            f"{erro_final_pct:.2e}" if erro_final_pct < 1.0e-6 else f"{erro_final_pct:.4f}",
            _fmt(erro_pico),
        ])
        print(f"  {metodo:8s} — {descricao}")

    print()
    viz.tabela(
        ["método", "erro RMS [rad/s]", "erro final [rad/s]", "erro final [%]", "erro de pico [rad/s]"],
        linhas_tabela,
        titulo_tabela="Erro de cada discretização em relação à resposta contínua (Ts = 5 ms)",
    )

    print()
    viz.plot_ascii(t_d, w_c_interp, altura=14, largura=64,
                    titulo_grafico="Referência contínua amostrada  w(t)  [rad/s]",
                    unidade_y="rad/s")
    print()
    viz.plot_ascii(t_d, respostas["euler"], altura=14, largura=64,
                    titulo_grafico="Discretização EULER  w[k]  [rad/s]",
                    y_ref=w_c_interp[-1], unidade_y="rad/s")
    print()
    viz.plot_ascii(t_d, respostas["zoh"], altura=14, largura=64,
                    titulo_grafico="Discretização ZOH  w[k]  [rad/s]  (coincide com a referência)",
                    y_ref=w_c_interp[-1], unidade_y="rad/s")

    # --- PNG comparativo ----------------------------------------------------
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(t_c, w_c, label="contínua (RK4, gabarito)", color="#57606a", linewidth=2.5, alpha=0.6)
    cores = {"euler": "#d1242f", "tustin": "#9a6700", "zoh": "#1f6feb"}
    marcadores = {"euler": "o", "tustin": "s", "zoh": "x"}
    for metodo, _ in METODOS:
        ax.plot(t_d, respostas[metodo], marcadores[metodo], label=metodo, color=cores[metodo],
                 markersize=4, linestyle="-", linewidth=0.8)
    ax.set_xlabel("tempo [s]")
    ax.set_ylabel("velocidade angular w [rad/s]")
    ax.set_title(f"NexaBot — discretização de G(s) em Ts={Ts * 1000:.0f} ms: Euler x Tustin x ZOH")
    ax.grid(True, alpha=0.3)
    ax.legend()
    viz.salvar_figura(fig, "aula07_euler_tustin_zoh.png")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print(viz.verde("  ZOH é EXATO aqui (erro RMS e de pico na casa de 1e-8..1e-9 rad/s, ruído"))
    print(viz.verde("  numérico) porque a hipótese do ZOH — tensão mantida constante entre"))
    print("  amostras — é literalmente como o driver do NexaBot aplica a tensão: é o")
    print("  'gabarito' correto para comparar discretizações neste tipo de entrada.")
    print("  Euler e Tustin aproximam a dinâmica contínua e por isso erram, mas de")
    print("  formas diferentes: Tustin acerta quase perfeitamente o valor final")
    print(f"  (erro final ~{abs(float((respostas['tustin'][-1] - w_c_interp[-1]) / w_c_interp[-1] * 100)):.3f}% "
          f"contra ~{abs(float((respostas['euler'][-1] - w_c_interp[-1]) / w_c_interp[-1] * 100)):.3f}% do Euler)")
    print("  porque a transformação bilinear preserva o ganho DC exatamente (s=0 -> z=1);")
    print("  já o erro RMS do TRANSITÓRIO inteiro é um pouco MENOR no Euler que no Tustin")
    print("  neste caso — a lição não é 'Tustin sempre vence', é 'meça a métrica que")
    print("  importa para o seu problema'.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
