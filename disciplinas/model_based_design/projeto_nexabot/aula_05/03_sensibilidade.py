#!/usr/bin/env python3
"""Aula 5 — Script 3/4: sensibilidade S(s) e sensibilidade complementar T(s).

O que este script demonstra
----------------------------
Para a malha L(s) = C(s).G(s) — o mesmo PID do script 2 (Kp=2, Ki=50,
Kd=0.001), agora na versão contínua equivalente via
`nexabot.controllers.pid_transfer_function` — definem-se duas funções de
transferência de malha fechada:

    S(s) = 1 / (1 + L(s))        sensibilidade
    T(s) = L(s) / (1 + L(s))     sensibilidade complementar

Fisicamente:

  - S(s) é a função de transferência de um DISTÚRBIO NA SAÍDA (ou de um
    distúrbio de carga refletido na saída) para o ERRO de rastreamento.
    Quanto menor |S(jw)|, melhor a malha rejeita distúrbios e ruído de
    baixa frequência naquela faixa — é por isso que o script 2 mostrou o
    erro final praticamente zero sob um distúrbio de carga em regime
    (frequência ~0, onde |S| é minúsculo).
  - T(s) é a função de transferência de REFERÊNCIA para SAÍDA — e também de
    RUÍDO DE MEDIÇÃO (sensor) para a saída. Quanto menor |T(jw)|, melhor a
    malha rejeita ruído de alta frequência do sensor, mas pior ela segue
    referências rápidas naquela faixa.

Como S(s) + T(s) = 1 EXATAMENTE (identidade algébrica: 1/(1+L) + L/(1+L) =
(1+L)/(1+L) = 1) para todo s, não dá para tornar |S| e |T| pequenos ao mesmo
tempo na mesma frequência — essa é a "água-cama da sensibilidade": apertar
num lugar do espectro faz sobrar (|S| ou |T| > 1) em outro. O script
confirma numericamente a identidade S(jw)+T(jw)=1 (como número complexo, não
como soma de magnitudes — |S|+|T| NÃO é 1 em geral) numa faixa de
frequências, e tabula/plota |S(jw)| e |T(jw)| em pontos marcantes: DC, o
pico de sensibilidade, a banda passante (T a -3 dB) e alta frequência.

Como rodar
----------
    .venv/bin/python aula_05/03_sensibilidade.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import control as ct  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import pid_transfer_function  # noqa: E402
from nexabot.plant import transfer_function  # noqa: E402


def main() -> int:
    print(viz.titulo("NexaBot — Aula 5 — Sensibilidade S(s) e sensibilidade complementar T(s)"))

    G = transfer_function()
    Kp, Ki, Kd = 2.0, 50.0, 0.001
    C = pid_transfer_function(Kp=Kp, Ki=Ki, Kd=Kd, N=20.0)
    L = ct.series(C, G)
    S = ct.feedback(1, L)   # 1/(1+L)
    T = ct.feedback(L, 1)   # L/(1+L)

    print(f"Controlador PID contínuo equivalente (Kp={Kp}, Ki={Ki}, Kd={Kd}, N=20):")
    print(f"  C(s) = {Kp} + {Ki}/s + {Kd}.20.s/(s+20)")
    print(f"L(s) = C(s).G(s) tem {L.den[0][0].size - 1}º grau no denominador "
          f"(2 do PID+filtro + 2 da planta).\n")

    # --- Verificação numérica da identidade S(jw) + T(jw) = 1 -------------
    w_verif = np.logspace(-2, 6, 200)
    soma = S(1j * w_verif) + T(1j * w_verif)
    erro_max = float(np.max(np.abs(soma - 1.0)))
    print(f"Verificação S(jw) + T(jw) = 1 (identidade COMPLEXA, não de magnitudes)")
    print(f"  em {len(w_verif)} frequências de {w_verif[0]:.3g} a {w_verif[-1]:.3g} rad/s:")
    print(f"  maior |S(jw)+T(jw) - 1| observado = {erro_max:.3e}")
    identidade_ok = erro_max < 1e-9
    print(f"  -> {viz.verde('CONFIRMADA') if identidade_ok else viz.vermelho('FALHOU')}\n")

    # --- Frequências marcantes ---------------------------------------------
    w_varredura = np.logspace(-2, 6, 4000)
    mag_S = np.abs(S(1j * w_varredura))
    mag_T = np.abs(T(1j * w_varredura))
    mag_L = np.abs(L(1j * w_varredura))

    w_pico_S = float(w_varredura[np.argmax(mag_S)])
    pico_S = float(np.max(mag_S))
    w_cruzamento = float(w_varredura[np.argmin(np.abs(mag_L - 1.0))])
    w_banda = float(w_varredura[np.argmin(np.abs(mag_T - 0.7071))])

    marcos = [
        ("DC (quase-estático, ~0 rad/s)", 1.0e-2),
        ("pico de sensibilidade |S|max", w_pico_S),
        ("banda passante (|T| = -3 dB)", w_banda),
        ("cruzamento |L|=1 (0 dB)", w_cruzamento),
        ("alta frequência (ruído de sensor)", 1.0e5),
    ]

    linhas = []
    for nome, wv in marcos:
        sv = abs(complex(S(1j * wv)))
        tv = abs(complex(T(1j * wv)))
        linhas.append([
            nome, f"{wv:.3g}",
            f"{sv:.4f}", f"{20 * np.log10(sv):.2f}",
            f"{tv:.4f}", f"{20 * np.log10(tv):.2f}",
        ])

    viz.tabela(
        ["frequência marcante", "w [rad/s]", "|S|", "|S| [dB]", "|T|", "|T| [dB]"],
        linhas,
        titulo_tabela="Sensibilidade S(jw) e sensibilidade complementar T(jw)",
    )

    # --- Gráfico ASCII (magnitude em dB vs log10(w)) -----------------------
    log_w = np.log10(w_varredura)
    print()
    viz.plot_ascii(log_w, 20 * np.log10(mag_S), altura=13, largura=64,
                    titulo_grafico="|S(jw)| [dB]  (eixo x = log10(w), w em rad/s)",
                    y_ref=0.0, unidade_x="log10(rad/s)", unidade_y="dB")
    print()
    viz.plot_ascii(log_w, 20 * np.log10(mag_T), altura=13, largura=64,
                    titulo_grafico="|T(jw)| [dB]  (eixo x = log10(w), w em rad/s)",
                    y_ref=0.0, unidade_x="log10(rad/s)", unidade_y="dB")

    # --- Bode de S e T sobrepostos (PNG) ------------------------------------
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    ax.semilogx(w_varredura, 20 * np.log10(mag_S), label="|S(jw)| — sensibilidade",
                color="#1f6feb", linewidth=1.8)
    ax.semilogx(w_varredura, 20 * np.log10(mag_T), label="|T(jw)| — sensibilidade complementar",
                color="#d1242f", linewidth=1.8)
    ax.axhline(0.0, color="#57606a", linestyle=":", linewidth=1.0)
    ax.axvline(w_cruzamento, color="#8250df", linestyle="--", linewidth=1.0,
               label=f"cruzamento |L|=1 ({w_cruzamento:.0f} rad/s)")
    ax.set_xlabel("frequência w [rad/s]")
    ax.set_ylabel("magnitude [dB]")
    ax.set_title("NexaBot — S(jw) e T(jw) da malha PID (água-cama da sensibilidade)")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=8)
    viz.salvar_figura(fig, "aula05_sensibilidade_bode.png")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print(f"  |S| é pequeno (<< 1) em baixa frequência ({20 * np.log10(mag_S[0]):.0f} dB perto de DC) — "
          "é por isso que o")
    print("  script 2 mostrou erro quase nulo sob distúrbio de carga (que atua como um")
    print("  degrau, ou seja, energia concentrada em w->0). |T| é próximo de 1 (0 dB) na")
    print(f"  mesma faixa: a malha segue bem a referência. Mas perto do cruzamento (w~"
          f"{w_cruzamento:.0f} rad/s)")
    print(f"  ambos passam de 1 (|S|max={pico_S:.3f} em w={w_pico_S:.0f} rad/s) — a água-cama: reduzir |S|")
    print("  numa faixa necessariamente eleva |S| (ou |T|) em outra. Em alta frequência")
    print("  |T|->0: a malha filtra ruído de sensor, ao custo de não seguir referências")
    print("  muito rápidas ali (mas isso não importa: nenhuma referência real do NexaBot")
    print("  tem conteúdo espectral em dezenas de kHz).")

    if identidade_ok:
        print(viz.verde(viz.negrito(
            "\nIdentidade S(jw)+T(jw)=1 confirmada numericamente em toda a varredura.")))
        return 0
    print(viz.vermelho(viz.negrito("\nIdentidade S+T=1 NÃO confirmada — revise S e T.")))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
