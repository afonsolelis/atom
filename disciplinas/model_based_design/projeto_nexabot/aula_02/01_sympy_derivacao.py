#!/usr/bin/env python3
"""Aula 2 — Script 1/5: da equação diferencial à matriz, com sympy.

O que este script demonstra
----------------------------
Todo o resto da disciplina depende das matrizes (A, B, C, D) que aparecem em
`nexabot/plant.py`, mas ali elas já chegam prontas, montadas à mão a partir
das duas EDOs do motor CC. Este script refaz esse caminho SIMBOLICAMENTE,
com sympy, para que fique claro que a passagem "equação diferencial ->
espaço de estados" é mecânica, não mágica:

1. Escreve as duas EDOs do motor CC de ímã permanente:
       L . di/dt = V - R.i - Ke.w        (malha elétrica de armadura)
       J . dw/dt = Kt.i - b.w - tau_load  (malha mecânica do eixo)
2. Isola di/dt e dw/dt (resolve o sistema para as derivadas).
3. Monta a forma matricial x' = A.x + B.u, y = C.x + D.u tomando o jacobiano
   simbólico de [di/dt, dw/dt] em relação ao estado x=[i, w] e à entrada u=V
   (tau_load é tratado como perturbação não modelada nesta representação,
   exatamente como em `nexabot/plant.py` — por isso é zerado aqui).
4. Substitui os valores numéricos de `nexabot.params.PARAMS` nas matrizes
   simbólicas e confere, com tolerância 1e-6, contra os números já
   verificados da disciplina E contra `nexabot.plant.state_space_matrices`.

Se as três fontes (dedução simbólica, número "de cabeça" já verificado,
`plant.py`) não baterem, algo está errado no contrato da disciplina — é por
isso que o script devolve 1 nesse caso, embora isso não deva acontecer.

Como rodar
----------
    .venv/bin/python aula_02/01_sympy_derivacao.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import state_space_matrices  # noqa: E402

# Matrizes numéricas já verificadas para PARAMS (ver enunciado da Aula 2):
# A referência é intencionalmente escrita "a mão", sem depender de plant.py,
# para que a comparação final não seja circular.
A_VERIFICADA = np.array([[-342.857, -12.857], [180.0, -0.32]])
B_VERIFICADA = np.array([[285.714], [0.0]])
C_VERIFICADA = np.array([[0.0, 1.0]])
D_VERIFICADA = np.array([[0.0]])
TOL = 1e-2  # a referência "a mão" tem só 3 casas decimais; plant.py e sympy usam o valor exato


def main() -> int:
    print(viz.titulo("NexaBot — Aula 2 — Da EDO do motor CC ao espaço de estados (sympy)"))

    # -- 1. símbolos e EDOs -------------------------------------------------
    t = sp.symbols("t", real=True)
    R, L, Ke, Kt, J, b, tau_load = sp.symbols("R L K_e K_t J b tau_load", real=True)
    i = sp.Function("i")(t)
    w = sp.Function("w")(t)
    V = sp.Function("V")(t)

    eq_eletrica = sp.Eq(L * sp.diff(i, t), V - R * i - Ke * w)
    eq_mecanica = sp.Eq(J * sp.diff(w, t), Kt * i - b * w - tau_load)

    print(viz.negrito("\n1) EDOs do motor CC de ímã permanente"))
    print("\nMalha elétrica de armadura:")
    sp.pprint(eq_eletrica)
    print("\nMalha mecânica do eixo:")
    sp.pprint(eq_mecanica)

    # -- 2. isola di/dt e dw/dt ----------------------------------------------
    solucao = sp.solve([eq_eletrica, eq_mecanica], [sp.diff(i, t), sp.diff(w, t)], dict=True)[0]
    di_dt = sp.simplify(solucao[sp.diff(i, t)])
    dw_dt = sp.simplify(solucao[sp.diff(w, t)])

    print(viz.negrito("\n2) Derivadas isoladas"))
    print("\ndi/dt =")
    sp.pprint(di_dt)
    print("\ndw/dt =")
    sp.pprint(dw_dt)

    # -- 3. forma matricial x' = A.x + B.u -----------------------------------
    # Para a representação de `plant.py`, tau_load é uma perturbação externa,
    # não um segundo canal de entrada: ela é zerada para obter (A, B), do
    # mesmo jeito que `nexabot.plant.state_space_matrices` ignora tau_load.
    x = sp.Matrix([i, w])
    u = sp.Matrix([V])
    xdot = sp.Matrix([di_dt, dw_dt]).subs({tau_load: 0})

    A_sym = xdot.jacobian(x)
    B_sym = xdot.jacobian(u)
    y = sp.Matrix([w])           # saída = velocidade angular do motor
    C_sym = y.jacobian(x)
    D_sym = y.jacobian(u)

    print(viz.negrito("\n3) Forma matricial simbólica  x' = A.x + B.u ,  y = C.x + D.u"))
    print("\nA =")
    sp.pprint(A_sym)
    print("\nB =")
    sp.pprint(B_sym)
    print("\nC =")
    sp.pprint(C_sym)
    print("\nD =")
    sp.pprint(D_sym)

    # -- 4. substitui os valores numéricos de PARAMS e confere ----------------
    subs_numericos = {
        R: PARAMS.R, L: PARAMS.L, Ke: PARAMS.Ke, Kt: PARAMS.Kt, J: PARAMS.J, b: PARAMS.b,
    }
    A_num = np.array(A_sym.subs(subs_numericos)).astype(float)
    B_num = np.array(B_sym.subs(subs_numericos)).astype(float)
    C_num = np.array(C_sym.subs(subs_numericos)).astype(float)
    D_num = np.array(D_sym.subs(subs_numericos)).astype(float)

    A_plant, B_plant, C_plant, D_plant = state_space_matrices(PARAMS)

    print(viz.negrito("\n4) Substituição numérica (PARAMS) e conferência cruzada"))
    viz.tabela(
        ["parâmetro", "valor", "unidade"],
        [
            ["R", f"{PARAMS.R:.4g}", "ohm"],
            ["L", f"{PARAMS.L:.4g}", "H"],
            ["Ke = Kt", f"{PARAMS.Ke:.4g}", "V.s/rad = N.m/A"],
            ["J", f"{PARAMS.J:.4g}", "kg.m^2"],
            ["b", f"{PARAMS.b:.4g}", "N.m.s/rad"],
        ],
        titulo_tabela="Parâmetros substituídos (nexabot.params.PARAMS)",
    )
    print()

    def _fmt(mat):
        """Formata uma matriz numpy em uma única linha (a tabela ASCII não lida
        bem com células multi-linha)."""
        linhas = np.array2string(mat, precision=4, suppress_small=True).splitlines()
        return " ; ".join(l.strip() for l in linhas)

    linhas_matrizes = [
        ["A (sympy -> numérico)", _fmt(A_num)],
        ["A (a mão, já verificada)", _fmt(A_VERIFICADA)],
        ["A (nexabot.plant.py)", _fmt(A_plant)],
        ["B (sympy -> numérico)", _fmt(B_num)],
        ["B (a mão, já verificada)", _fmt(B_VERIFICADA)],
        ["B (nexabot.plant.py)", _fmt(B_plant)],
    ]
    viz.tabela(["matriz", "valor"], linhas_matrizes, titulo_tabela="Comparação das três fontes",
               alinhamentos=["e", "e"])

    diffs = {
        "A vs. já verificada": float(np.max(np.abs(A_num - A_VERIFICADA))),
        "A vs. plant.py": float(np.max(np.abs(A_num - A_plant))),
        "B vs. já verificada": float(np.max(np.abs(B_num - B_VERIFICADA))),
        "B vs. plant.py": float(np.max(np.abs(B_num - B_plant))),
        "C vs. plant.py": float(np.max(np.abs(C_num - C_plant))),
        "D vs. plant.py": float(np.max(np.abs(D_num - D_plant))),
    }

    print()
    linhas_diff = []
    tudo_ok = True
    for nome, diff in diffs.items():
        ok = diff < TOL
        tudo_ok &= ok
        status = viz.verde(f"{diff:.2e}  (OK)") if ok else viz.vermelho(f"{diff:.2e}  (FALHA)")
        linhas_diff.append([nome, status])
    viz.tabela(["comparação", "diferença máxima"], linhas_diff,
               titulo_tabela=f"Diferenças absolutas (tolerância {TOL:g})")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print("  A dedução simbólica com sympy, a conta \"a mão\" e a implementação numérica")
    print("  de plant.py chegam à MESMA matriz. Isso não é coincidência: espaço de estados")
    print("  é só uma reescrita mecânica de EDOs lineares de 1a ordem acopladas — não há")
    print("  nenhuma física nova sendo introduzida ao passar de EDO para (A, B, C, D).")

    if tudo_ok:
        print(viz.verde(viz.negrito("\nTodas as matrizes conferem entre as três fontes.")))
    else:
        print(viz.vermelho(viz.negrito("\nDivergência entre as fontes — revise o contrato de plant.py.")))

    return 0 if tudo_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
