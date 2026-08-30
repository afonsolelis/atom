#!/usr/bin/env python3
"""Aula 4 — Script 1/5: controlabilidade e observabilidade do NexaBot.

O que este script demonstra
----------------------------
Antes de projetar QUALQUER realimentação de estados (aloção de polos, LQR,
observador) é preciso responder duas perguntas estruturais sobre o modelo:

1. Controlabilidade: existe alguma tensão de armadura V(t) capaz de levar o
   estado [corrente, velocidade] do NexaBot de qualquer ponto inicial a
   qualquer ponto final em tempo finito? Se não, nenhum projeto de ganho K
   consegue posicionar os polos de malha fechada onde quisermos.
2. Observabilidade: dado que o encoder do NexaBot só mede a velocidade
   angular w (não a corrente i diretamente), é possível reconstruir os DOIS
   estados a partir apenas dessa medida, observando sua evolução no tempo?
   Se não, nenhum observador (Aula 4, script 4) converge para o estado real.

O critério clássico (Kalman) usa o POSTO das matrizes de controlabilidade e
observabilidade:

    Wc = [B, A.B]           (n colunas para n estados, m=1 entrada)
    Wo = [C; C.A]           (n linhas para n estados, p=1 saída)

O sistema é totalmente controlável se posto(Wc) = n e totalmente observável
se posto(Wo) = n, com n = 2 (corrente e velocidade) para o NexaBot.

Como rodar
----------
    .venv/bin/python aula_04/01_ctrb_obsv.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402
import control as ct  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import state_space_matrices  # noqa: E402


def formatar_matriz(M: np.ndarray, casas: int = 4) -> list[list[str]]:
    """Formata uma matriz numpy como lista de linhas de strings alinhadas."""
    return [[f"{v:.{casas}g}" for v in linha] for linha in M]


def main() -> int:
    print(viz.titulo("NexaBot — Aula 4 — Controlabilidade e observabilidade"))

    A, B, C, D = state_space_matrices(PARAMS)
    n = A.shape[0]

    print("Matrizes do modelo em espaço de estados x=[corrente, velocidade], u=tensão, y=velocidade:\n")
    viz.tabela(["A", "coluna 1", "coluna 2"],
               [[f"linha {i + 1}"] + formatar_matriz(A)[i] for i in range(n)],
               titulo_tabela="Matriz de estados A")
    print()
    viz.tabela(["B", "coluna 1"],
               [[f"linha {i + 1}"] + formatar_matriz(B)[i] for i in range(n)],
               titulo_tabela="Matriz de entrada B")
    print()
    viz.tabela(["C", "coluna 1", "coluna 2"],
               [["linha 1"] + formatar_matriz(C)[0]],
               titulo_tabela="Matriz de saída C (só mede velocidade w)")

    # --- Controlabilidade ---------------------------------------------------
    Wc = ct.ctrb(A, B)
    posto_c = int(np.linalg.matrix_rank(Wc))

    print()
    viz.tabela(["Wc = [B, A.B]", "coluna 1 (B)", "coluna 2 (A.B)"],
               [[f"linha {i + 1}"] + formatar_matriz(Wc)[i] for i in range(n)],
               titulo_tabela="Matriz de controlabilidade Wc")
    print(f"\n  det(Wc) = {np.linalg.det(Wc):.6g}   |   posto(Wc) = {posto_c} (de n = {n})")

    # --- Observabilidade ------------------------------------------------------
    Wo = ct.obsv(A, C)
    posto_o = int(np.linalg.matrix_rank(Wo))

    print()
    viz.tabela(["Wo = [C; C.A]", "coluna 1", "coluna 2"],
               [[f"linha {i + 1}"] + formatar_matriz(Wo)[i] for i in range(n)],
               titulo_tabela="Matriz de observabilidade Wo")
    print(f"\n  det(Wo) = {np.linalg.det(Wo):.6g}   |   posto(Wo) = {posto_o} (de n = {n})")

    print()
    viz.tabela(
        ["propriedade", "posto obtido", "posto necessário", "resultado"],
        [
            ["controlabilidade (Wc)", str(posto_c), str(n),
             viz.verde("TOTALMENTE CONTROLÁVEL") if posto_c == n else viz.vermelho("NÃO CONTROLÁVEL")],
            ["observabilidade (Wo)", str(posto_o), str(n),
             viz.verde("TOTALMENTE OBSERVÁVEL") if posto_o == n else viz.vermelho("NÃO OBSERVÁVEL")],
        ],
        titulo_tabela="Resumo do critério de posto de Kalman",
    )

    print(viz.negrito("\nO que isso significa fisicamente para o NexaBot:"))
    print("  Controlável (posto 2): a tensão de armadura V(t), sozinha, é capaz de")
    print("  levar o par [corrente, velocidade] de QUALQUER estado inicial a QUALQUER")
    print("  estado final em tempo finito. Fisicamente faz sentido: a corrente responde")
    print("  quase instantaneamente a V (τ_elétrica ≈ 2,92 ms) e arrasta a velocidade")
    print("  atrás dela (τ_mecânica ≈ 148 ms) — não há um modo do motor inacessível a V.")
    print("  Isso é o que permite alocar os polos de malha fechada onde quisermos nos")
    print("  scripts 2 e 3 desta aula (na prática, limitado pela saturação de 24 V).")
    print()
    print("  Observável (posto 2): embora o encoder só meça w (a corrente i NÃO é")
    print("  medida diretamente), a forma como w reage no tempo carrega informação")
    print("  suficiente sobre i para reconstruí-la — porque i afeta dw/dt via Kt.i/J,")
    print("  então observar a EVOLUÇÃO de w (não seu valor instantâneo) revela i.")
    print("  Isso é exatamente o que o observador de Luenberger do script 4 explora:")
    print("  estimar a corrente sem um sensor de corrente, só com o encoder de w.")

    ok = (posto_c == n) and (posto_o == n)
    if ok:
        print(viz.verde(viz.negrito(
            "\nConfirmado: o NexaBot é totalmente controlável e totalmente observável.")))
    else:
        print(viz.vermelho(viz.negrito(
            "\nATENÇÃO: modelo perdeu controlabilidade/observabilidade — revise params.py.")))

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
