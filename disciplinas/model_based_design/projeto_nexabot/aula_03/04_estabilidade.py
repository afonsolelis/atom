#!/usr/bin/env python3
"""Aula 3 — Script 4/5: ganho proporcional, margem de fase e o limite (que não vem).

O que este script demonstra
----------------------------
Fecha a malha de velocidade do NexaBot com um controlador puramente
proporcional CONTÍNUO, Kp, em realimentação unitária:

    C(s) = Kp        malha fechada: T(s) = Kp.G(s) / (1 + Kp.G(s))

e varre Kp de 0,5 a 50 observando margem de fase, sobressinal e tempo de
acomodação. O ponto pedagógico central: como G(s) é de 2ª ordem estritamente
própria, o denominador de malha fechada é

    L.J.s^2 + (R.J + L.b).s + (R.b + Kt.Ke + Kp.Kt)

Os três coeficientes são positivos para QUALQUER Kp > 0 (o termo extra
Kp.Kt só soma ao coeficiente independente, que já era positivo) — logo
Routh-Hurwitz de 2ª ordem (todos os coeficientes positivos) é satisfeito
sempre. O sistema JAMAIS desestabiliza por realimentação proporcional
contínua, não importa quão grande seja Kp: a margem de fase tende a zero
assintoticamente e o sobressinal tende a 100%, mas nunca há instabilidade de
verdade nesta malha contínua.

Isso é diferente do que acontece quando a malha é DISCRETA (amostrada a
Ts = 5 ms, como o controlador embarcado do NexaBot): o atraso de fase
introduzido pelo segurador de ordem zero (ZOH) e pelo próprio período de
amostragem FAZ a malha desestabilizar para um Kp finito. Esse resultado é o
assunto da Aula 7 (discretização) — aqui fica só o gancho.

Como rodar
----------
    .venv/bin/python aula_03/04_estabilidade.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import step_metrics  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import transfer_function  # noqa: E402


def main() -> int:
    import control as ct

    print(viz.titulo("NexaBot — Aula 3 — Kp crescente: margem de fase, sobressinal e o limite que não vem"))

    G = transfer_function(PARAMS)
    valores_kp = [0.5, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0, 50.0]

    t = np.linspace(0.0, 1.0, 20000)
    linhas = []
    fases = []
    sobressinais = []
    for Kp in valores_kp:
        _, pm, _, _, wp, _ = ct.stability_margins(Kp * G)
        malha_fechada = ct.feedback(Kp * G, 1)
        dc_gain_mf = float(ct.dcgain(malha_fechada))
        _, y = ct.step_response(malha_fechada, T=t)
        metrica = step_metrics(t, y, r=dc_gain_mf)
        # overshoot negativo (ruído numérico de ponto flutuante em respostas sem
        # sobressinal real) é clampado a 0.00% só para exibição.
        overshoot_exibicao = max(0.0, metrica["overshoot_pct"])

        fases.append(pm)
        sobressinais.append(overshoot_exibicao)
        linhas.append([
            f"{Kp:.1f}",
            f"{pm:.2f}",
            f"{wp:.1f}",
            f"{overshoot_exibicao:.2f}",
            f"{metrica['t_settle_s'] * 1000:.2f}",
            f"{dc_gain_mf:.4f}",
        ])

    viz.tabela(
        ["Kp", "margem de fase [graus]", "wp [rad/s]", "sobressinal [%]",
         "t_acomod. (2%) [ms]", "ganho DC malha fechada"],
        linhas,
        titulo_tabela="Varredura de Kp em malha fechada unitária (controlador proporcional contínuo)",
    )

    print()
    viz.plot_ascii(valores_kp, fases, altura=13, largura=60,
                    titulo_grafico="Margem de fase x Kp — tende a zero, nunca fica negativa",
                    unidade_x="Kp", unidade_y="graus")
    print()
    viz.plot_ascii(valores_kp, sobressinais, altura=13, largura=60,
                    titulo_grafico="Sobressinal x Kp — tende a 100%, malha nunca instabiliza",
                    unidade_x="Kp", unidade_y="%")

    menor_pm = min(fases)
    maior_overshoot = max(sobressinais)
    print(f"\nNa faixa varrida (Kp de {valores_kp[0]} a {valores_kp[-1]}): margem de fase mínima "
          f"observada = {menor_pm:.2f}° (Kp={valores_kp[int(np.argmin(fases))]:.1f}), sempre > 0.")
    print(f"Sobressinal máximo observado = {maior_overshoot:.2f}% (Kp={valores_kp[int(np.argmax(sobressinais))]:.1f}), sempre < 100%.")

    # --- Confirmação simbólica de Routh-Hurwitz (2a ordem, sempre estável p/ Kp>0)
    a0 = PARAMS.L * PARAMS.J
    a1 = PARAMS.R * PARAMS.J + PARAMS.L * PARAMS.b
    a2_base = PARAMS.R * PARAMS.b + PARAMS.Kt * PARAMS.Ke
    print("\n" + viz.negrito("Por que nunca desestabiliza (Routh-Hurwitz, malha contínua):"))
    print(f"  Denominador de malha fechada: {a0:.4g}.s^2 + {a1:.4g}.s + ({a2_base:.4g} + Kp.{PARAMS.Kt})")
    print("  2ª ordem: estável <=> todos os coeficientes > 0. a0 e a1 não dependem de Kp e já são")
    print("  positivos; o termo com Kp só SOMA ao coeficiente independente (que já era positivo).")
    print("  Logo, para todo Kp > 0, os três coeficientes permanecem positivos: sempre estável.")

    print("\n" + viz.negrito("Gancho para a Aula 7:"))
    print("  Essa garantia é exclusiva da malha CONTÍNUA. O controlador do NexaBot roda")
    print(f"  amostrado a Ts = {PARAMS.Ts * 1000:.0f} ms com um segurador de ordem zero (ZOH) na saída —")
    print("  esse atraso extra de fase, ausente aqui, FAZ a malha discreta desestabilizar para")
    print("  um Kp finito. A Aula 7 mostra o ganho crítico exato dessa malha discreta.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
