#!/usr/bin/env python3
"""Aula 2 — Script 2/5: espaço de estados e função de transferência são o mesmo sistema.

O que este script demonstra
----------------------------
`nexabot/plant.py` oferece DUAS representações do mesmo motor CC:
`state_space(p)` (matrizes A, B, C, D) e `transfer_function(p)` (a fração de
polinômios W(s)/V(s)). Um erro comum de quem está aprendendo é tratá-las como
dois modelos diferentes que "por acaso" concordam. Este script mostra que são
a MESMA descrição matemática, só que escritas de duas formas:

1. Converte a state-space (`nexabot.plant.state_space`) para função de
   transferência com `control.tf(...)` e compara os polos e o ganho DC com
   os obtidos diretamente de `nexabot.plant.transfer_function`.
2. Aplica um degrau de tensão nos dois modelos — uma vez via
   `control.step_response` na função de transferência, outra vez via
   `nexabot.plant.simulate` (o integrador RK4 manual usado no resto da
   disciplina) — e mostra que as respostas coincidem a menos de erro
   numérico de integração.

Como rodar
----------
    .venv/bin/python aula_02/02_estado_vs_transferencia.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import control as ct  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import simulate, state_space, transfer_function  # noqa: E402

TOL_POLOS = 1e-6
TOL_GANHO = 1e-6
TOL_RESPOSTA = 1e-3  # rad/s: erro numérico esperado entre integrador RK4 e o solver do `control`


def main() -> int:
    print(viz.titulo("NexaBot — Aula 2 — Espaço de estados x função de transferência: o mesmo sistema"))

    # -- 1. converte SS -> TF e compara com a TF direta ----------------------
    ss = state_space(PARAMS)
    tf_via_ss = ct.tf(ss)
    tf_direta = transfer_function(PARAMS)

    print(viz.negrito("\n1) Duas formas de chegar na função de transferência"))
    print("\nA partir do espaço de estados (control.tf(state_space(PARAMS))):")
    print(tf_via_ss)
    print("A partir da fórmula fechada (nexabot.plant.transfer_function(PARAMS)):")
    print(tf_direta)

    polos_ss = np.sort_complex(ct.poles(tf_via_ss))
    polos_direta = np.sort_complex(ct.poles(tf_direta))
    ganho_ss = float(ct.dcgain(tf_via_ss))
    ganho_direta = float(ct.dcgain(tf_direta))

    diff_polos = float(np.max(np.abs(polos_ss - polos_direta)))
    diff_ganho = abs(ganho_ss - ganho_direta)

    viz.tabela(
        ["grandeza", "via espaço de estados", "via fórmula direta", "já verificado"],
        [
            ["polo 1 [1/s]", f"{polos_ss[1].real:.4f}", f"{polos_direta[1].real:.4f}", "-7.215"],
            ["polo 2 [1/s]", f"{polos_ss[0].real:.4f}", f"{polos_direta[0].real:.4f}", "-335.962"],
            ["ganho DC [rad/(s.V)]", f"{ganho_ss:.4f}", f"{ganho_direta:.4f}", "21.2164"],
        ],
        titulo_tabela="Polos e ganho DC: espaço de estados vs. fórmula fechada",
    )

    print()
    status_polos = viz.verde(f"{diff_polos:.2e}  (idênticos)") if diff_polos < TOL_POLOS \
        else viz.vermelho(f"{diff_polos:.2e}  (DIVERGEM)")
    status_ganho = viz.verde(f"{diff_ganho:.2e}  (idênticos)") if diff_ganho < TOL_GANHO \
        else viz.vermelho(f"{diff_ganho:.2e}  (DIVERGEM)")
    viz.tabela(
        ["comparação", "diferença máxima"],
        [["polos (SS vs. direta)", status_polos], ["ganho DC (SS vs. direta)", status_ganho]],
        titulo_tabela="Diferenças absolutas",
    )

    # -- 2. degrau de tensão nos dois "mundos": TF (control) x integrador RK4 -
    V_degrau = 12.0
    t_end = 0.8
    t_grade = np.linspace(0.0, t_end, 4000)

    print(viz.negrito("\n2) Mesmo degrau de tensão, dois caminhos de simulação"))
    print(f"\nDegrau de V = {V_degrau:.1f} V por {t_end:.1f} s.")
    print("  Caminho A: control.step_response(transfer_function * V_degrau)")
    print("  Caminho B: nexabot.plant.simulate(...)  (integrador RK4 manual, mesmo de plant.py)")

    t_tf, w_tf = ct.step_response(tf_direta * V_degrau, T=t_grade)

    def u_of_t(t):
        return V_degrau if t >= 0 else 0.0

    t_rk4, X_rk4 = simulate(u_of_t, t_end=t_end, dt=1.0e-4, p=PARAMS)
    w_rk4_na_grade_tf = np.interp(t_tf, t_rk4, X_rk4[:, 1])

    erro = w_tf - w_rk4_na_grade_tf
    erro_max = float(np.max(np.abs(erro)))
    erro_max_pct = erro_max / float(np.max(np.abs(w_tf))) * 100.0

    viz.plot_ascii(t_tf, w_tf, altura=14, largura=64,
                    titulo_grafico="w(t) via função de transferência (control.step_response)  [rad/s]",
                    unidade_y="rad/s")
    print()
    viz.plot_ascii(t_rk4, X_rk4[:, 1], altura=14, largura=64,
                    titulo_grafico="w(t) via integrador RK4 (nexabot.plant.simulate)  [rad/s]",
                    unidade_y="rad/s")
    print()
    viz.plot_ascii(t_tf, erro, altura=8, largura=64,
                    titulo_grafico="Erro entre os dois caminhos: TF - RK4  [rad/s]", unidade_y="rad/s")

    print()
    viz.tabela(
        ["métrica", "valor"],
        [
            ["erro absoluto máximo", f"{erro_max:.3e} rad/s"],
            ["erro relativo máximo (% do pico)", f"{erro_max_pct:.4f} %"],
            ["amostras comparadas", f"{len(t_tf)}"],
        ],
        titulo_tabela="Erro entre função de transferência e integrador RK4",
    )

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(7, 6), sharex=True)
    ax1.plot(t_tf, w_tf, label="função de transferência (control)", color="#1f6feb", linewidth=2.2)
    ax1.plot(t_rk4, X_rk4[:, 1], label="integrador RK4 (plant.simulate)", color="#d1242f",
             linestyle="--", linewidth=1.4)
    ax1.set_ylabel("w(t) [rad/s]")
    ax1.set_title(f"NexaBot — degrau de {V_degrau:.0f} V: espaço de estados x função de transferência")
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax2.plot(t_tf, erro, color="#8250df", linewidth=1.2)
    ax2.set_xlabel("tempo [s]")
    ax2.set_ylabel("erro TF - RK4 [rad/s]")
    ax2.grid(True, alpha=0.3)
    viz.salvar_figura(fig, "aula02_estado_vs_transferencia.png")

    status = viz.verde(viz.negrito("Respostas idênticas a menos de erro numérico de integração.")) \
        if erro_max_pct < 1.0 \
        else viz.vermelho(viz.negrito("Erro maior que o esperado — revise o passo de integração."))

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print("  Espaço de estados e função de transferência descrevem a MESMA dinâmica linear:")
    print("  a conversão control.tf(state_space(...)) não perde nem inventa informação, e o")
    print("  pequeno erro remanescente vem só do método numérico (RK4 de passo fixo vs. o")
    print("  solver de EDO usado internamente por control.step_response), não da física.")
    print()
    print(status)

    tudo_ok = (diff_polos < TOL_POLOS) and (diff_ganho < TOL_GANHO) and (erro_max_pct < 1.0)
    return 0 if tudo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
