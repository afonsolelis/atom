#!/usr/bin/env python3
"""Aula 3 — Script 3/5: resposta em frequência — Bode, margens e banda passante.

O que este script demonstra
----------------------------
A mesma G(s) da planta do NexaBot, agora vista no domínio da frequência:

1. Diagrama de Bode (magnitude em dB e fase em graus) via
   `control.frequency_response`, salvo como PNG (o Bode não cabe bem em
   ASCII — duas décadas de eixo log e fase juntas exigem mais resolução do
   que um terminal oferece).
2. Uma versão ASCII simplificada da curva de MAGNITUDE, com o eixo X em
   log10(frequência), só para não deixar o terminal mudo nesta aula.
3. Margens de ganho e de fase (`control.stability_margins`): a planta é um
   sistema de 2ª ordem estritamente próprio e passa-baixa — a fase nunca
   cruza -180°, então a margem de ganho é infinita (não há frequência de
   cruzamento de fase) e só a margem de fase é um número finito relevante.
4. Banda passante (frequência de -3 dB em relação ao ganho DC).

Como rodar
----------
    .venv/bin/python aula_03/03_bode.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import transfer_function  # noqa: E402


def main() -> int:
    import control as ct

    print(viz.titulo("NexaBot — Aula 3 — Bode, margens de ganho/fase e banda passante"))

    G = transfer_function(PARAMS)
    print(f"G(s) = {G}\n")

    w = np.logspace(-1, 5, 2000)
    resposta = ct.frequency_response(G, w)
    mag = np.abs(resposta.magnitude)
    mag_db = 20.0 * np.log10(mag)
    fase_deg = np.degrees(resposta.phase)
    # `control` devolve a fase "desembrulhada"; para um passa-baixas de 2ª
    # ordem ela é monotonicamente decrescente de 0 a -180°, então basta
    # normalizar o ramo principal caso apareça deslocada por múltiplos de 360°.
    fase_deg = fase_deg - 360.0 * np.round(fase_deg[0] / 360.0)

    dc_gain = float(ct.dcgain(G))
    dc_gain_db = 20.0 * np.log10(dc_gain)
    alvo_3db = dc_gain / np.sqrt(2.0)
    idx_bw = int(np.argmin(np.abs(mag - alvo_3db)))
    banda_passante_rad_s = float(resposta.omega[idx_bw])
    banda_passante_hz = banda_passante_rad_s / (2.0 * np.pi)

    gm, pm, sm, wg, wp, ws = ct.stability_margins(G)

    print(viz.negrito("Curva de magnitude |G(jw)| em ASCII (eixo X = log10(w), w em rad/s):"))
    log_w = np.log10(resposta.omega)
    viz.plot_ascii(log_w, mag_db, altura=15, largura=64,
                    titulo_grafico="Magnitude de G(jw) [dB]  (X = log10(w [rad/s]))",
                    y_ref=dc_gain_db - 3.0, unidade_x="log10(rad/s)", unidade_y="dB")
    print()

    def _fmt_margem(valor, unidade, infinito_ok=True):
        if np.isnan(valor):
            return "não definida (fase nunca cruza -180°)"
        if np.isinf(valor):
            return f"infinita ({'sem cruzamento de fase' if infinito_ok else 'ilimitada'})"
        return f"{valor:.3f} {unidade}"

    linhas_margens = [
        ["margem de ganho (gm)", _fmt_margem(gm, "(abs)")],
        ["freq. de cruzamento de fase (wg)", _fmt_margem(wg, "rad/s")],
        ["margem de fase (pm)", f"{pm:.3f} graus"],
        ["freq. de cruzamento de ganho (wp)", f"{wp:.3f} rad/s ({wp / (2 * np.pi):.3f} Hz)"],
        ["ganho DC", f"{dc_gain:.4f} rad/(s.V)  ({dc_gain_db:.2f} dB)"],
        ["banda passante (-3 dB)", f"{banda_passante_rad_s:.4f} rad/s ({banda_passante_hz:.4f} Hz)"],
    ]
    viz.tabela(["grandeza", "valor"], linhas_margens,
               titulo_tabela="Resposta em frequência de G(s) — resumo")

    print("\n" + viz.negrito("Por que a margem de ganho é infinita:"))
    print("  G(s) é passa-baixa de 2ª ordem sem zeros: a fase parte de 0° e desce")
    print("  monotonicamente até -180° apenas quando w -> infinito (assintoticamente),")
    print("  nunca cruzando -180° em frequência finita. Sem cruzamento de fase, não existe")
    print("  frequência wg onde medir a margem de ganho — por definição, ela é infinita.")
    print("  Isso muda assim que se fecha a malha com um controlador que adicione fase")
    print("  negativa extra (atraso computacional, filtro, zero-order hold — Aula 7).")

    # --- Figura Bode completa (PNG) -----------------------------------------
    fig, (ax_mag, ax_fase) = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    ax_mag.semilogx(resposta.omega, mag_db, color="#1f6feb", linewidth=1.8)
    ax_mag.axhline(dc_gain_db, color="#8b949e", linestyle=":", linewidth=1.0, label="ganho DC")
    ax_mag.axhline(dc_gain_db - 3.0, color="#d1242f", linestyle="--", linewidth=1.2, label="-3 dB")
    ax_mag.axvline(banda_passante_rad_s, color="#d1242f", linestyle="--", linewidth=1.0)
    ax_mag.set_ylabel("Magnitude [dB]")
    ax_mag.set_title("NexaBot — Diagrama de Bode de G(s) = W(s)/V(s)")
    ax_mag.grid(True, which="both", alpha=0.3)
    ax_mag.legend(loc="lower left")

    ax_fase.semilogx(resposta.omega, fase_deg, color="#1f6feb", linewidth=1.8)
    ax_fase.axhline(pm - 180.0, color="#57ab5a", linestyle=":", linewidth=1.0, label="fase em wp")
    ax_fase.axvline(wp, color="#57ab5a", linestyle="--", linewidth=1.0, label=f"wp = {wp:.1f} rad/s")
    ax_fase.set_ylabel("Fase [graus]")
    ax_fase.set_xlabel("Frequência [rad/s]")
    ax_fase.grid(True, which="both", alpha=0.3)
    ax_fase.legend(loc="lower left")

    viz.salvar_figura(fig, "aula03_bode.png")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print(f"  A banda passante ({banda_passante_rad_s:.2f} rad/s) fica muito perto do polo mecânico")
    print("  (~7,22 rad/s) e bem abaixo do polo elétrico (~336 rad/s) — outra forma de ver a")
    print("  mesma separação de escalas do script anterior: é o polo LENTO que limita a")
    print("  velocidade de resposta do sistema em malha aberta, não o rápido.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
