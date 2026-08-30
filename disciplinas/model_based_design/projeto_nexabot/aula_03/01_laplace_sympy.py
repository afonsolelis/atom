#!/usr/bin/env python3
"""Aula 3 — Script 1/5: da EDO à função de transferência via Laplace (SymPy).

O que este script demonstra
----------------------------
As duas equações diferenciais do motor CC do NexaBot (Aula 2) são levadas ao
domínio de Laplace SIMBOLICAMENTE, com condições iniciais nulas:

    L . di/dt = V - R.i - Ke.w      --Laplace-->      L.s.I(s) = V(s) - R.I(s) - Ke.W(s)
    J . dw/dt = Kt.i - b.w          --Laplace-->      J.s.W(s) = Kt.I(s) - b.W(s)

(a derivada no tempo vira multiplicação por `s` porque i(0)=w(0)=0: não há
termo de condição inicial a carregar.) O SymPy resolve o sistema linear em
I(s) e W(s), isola a razão G(s) = W(s)/V(s) e o script confere que o
polinômio do denominador é exatamente

    G(s) = Kt / (L.J.s^2 + (R.J + L.b).s + (R.b + Kt.Ke))

Depois os valores numéricos de `nexabot.params.PARAMS` são substituídos na
expressão simbólica e comparados, coeficiente a coeficiente, com o que
`nexabot.plant.transfer_function(PARAMS)` (via `control`) devolve — as duas
fontes (álgebra simbólica e a biblioteca usada no resto da disciplina)
precisam bater exatamente.

Como rodar
----------
    .venv/bin/python aula_03/01_laplace_sympy.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sympy as sp  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import transfer_function  # noqa: E402


def derivar_funcao_transferencia_simbolica():
    """Deriva G(s) = W(s)/V(s) simbolicamente a partir das duas EDOs do motor.

    Devolve (G_simbolico, coeficientes_denominador, s) onde `coeficientes`
    é a lista [L.J, R.J+L.b, R.b+Kt.Ke] na ordem de `sympy.Poly.all_coeffs`.
    """
    s, R, L, Ke, Kt, J, b = sp.symbols("s R L Ke Kt J b", positive=True)
    I, W, V = sp.symbols("I W V")  # I(s), W(s), V(s) — condições iniciais nulas

    eq_eletrica = sp.Eq(L * s * I, V - R * I - Ke * W)
    eq_mecanica = sp.Eq(J * s * W, Kt * I - b * W)

    solucao = sp.solve([eq_eletrica, eq_mecanica], [I, W], dict=True)[0]
    G = sp.simplify(solucao[W] / V)

    numerador, denominador = sp.fraction(sp.together(G))
    poly_den = sp.Poly(sp.expand(denominador), s)
    coeficientes = poly_den.all_coeffs()  # [s^2, s^1, s^0]

    return G, sp.expand(numerador), coeficientes, (s, R, L, Ke, Kt, J, b)


def main() -> int:
    print(viz.titulo("NexaBot — Aula 3 — Laplace simbólico: da EDO a G(s)"))

    print("Equações do motor no domínio do tempo (Aula 2):")
    print("  L . di/dt = V - R.i - Ke.w")
    print("  J . dw/dt = Kt.i - b.w\n")
    print("Aplicando a Transformada de Laplace com condições iniciais nulas")
    print("(i(0) = w(0) = 0, logo L{dx/dt} = s.X(s), sem termo -x(0)):")
    print("  L.s.I(s) = V(s) - R.I(s) - Ke.W(s)")
    print("  J.s.W(s) = Kt.I(s) - b.W(s)\n")

    G_sym, num_sym, coefs_sym, simbolos = derivar_funcao_transferencia_simbolica()
    s, R, L, Ke, Kt, J, b = simbolos

    print(viz.negrito("Resolvendo o sistema linear (SymPy) para W(s)/V(s):"))
    print(f"  G(s) = W(s)/V(s) = {sp.nsimplify(num_sym)} / ("
          f"{sp.expand(sp.Poly(coefs_sym, s).as_expr())})")
    print()
    print("Forma canônica esperada:")
    print("  G(s) = Kt / (L.J.s^2 + (R.J + L.b).s + (R.b + Kt.Ke))\n")

    coef_s2, coef_s1, coef_s0 = coefs_sym
    print(viz.negrito("Coeficientes simbólicos do denominador (ordem s^2, s^1, s^0):"))
    print(f"  s^2 : {coef_s2}")
    print(f"  s^1 : {coef_s1}")
    print(f"  s^0 : {coef_s0}")

    conferencias = [
        ("s^2 == L.J", sp.simplify(coef_s2 - L * J) == 0),
        ("s^1 == R.J + L.b", sp.simplify(coef_s1 - (R * J + L * b)) == 0),
        ("s^0 == R.b + Kt.Ke", sp.simplify(coef_s0 - (R * b + Kt * Ke)) == 0),
    ]
    linhas_forma = []
    for descricao, ok in conferencias:
        status = viz.verde("OK") if ok else viz.vermelho("FALHOU")
        linhas_forma.append([descricao, status])
    print()
    viz.tabela(["identidade algébrica", "resultado"], linhas_forma,
               titulo_tabela="Conferência da forma canônica (álgebra simbólica pura)")

    # --- Substituição numérica dos parâmetros identificados -----------------
    subs_map = {R: PARAMS.R, L: PARAMS.L, Ke: PARAMS.Ke, Kt: PARAMS.Kt,
                J: PARAMS.J, b: PARAMS.b}
    num_num = float(num_sym.subs(subs_map))
    den_num = [float(c.subs(subs_map)) for c in coefs_sym]

    G_lib = transfer_function(PARAMS)
    num_lib = float(G_lib.num[0][0][0])
    den_lib = [float(c) for c in G_lib.den[0][0]]

    print(viz.titulo("Comparação: substituição numérica no simbólico vs nexabot.plant", largura=78))
    linhas_cmp = [
        ["numerador (Kt)", f"{num_num:.6g}", f"{num_lib:.6g}", f"{abs(num_num - num_lib):.2e}"],
        ["den. s^2 (L.J)", f"{den_num[0]:.6g}", f"{den_lib[0]:.6g}", f"{abs(den_num[0] - den_lib[0]):.2e}"],
        ["den. s^1 (R.J+L.b)", f"{den_num[1]:.6g}", f"{den_lib[1]:.6g}", f"{abs(den_num[1] - den_lib[1]):.2e}"],
        ["den. s^0 (R.b+Kt.Ke)", f"{den_num[2]:.6g}", f"{den_lib[2]:.6g}", f"{abs(den_num[2] - den_lib[2]):.2e}"],
    ]
    viz.tabela(
        ["coeficiente", "SymPy (simbólico -> numérico)", "control (nexabot.plant)", "|diferença|"],
        linhas_cmp,
        titulo_tabela="G(s) = 0.045 / (8.75e-7 s^2 + 3.0028e-4 s + <s^0>)",
    )

    # --- Checagem específica do coeficiente s^0 do enunciado ---------------
    dc_gain_formula = PARAMS.Kt / (PARAMS.R * PARAMS.b + PARAMS.Kt * PARAMS.Ke)
    erro_dc = abs(dc_gain_formula - PARAMS.dc_gain)
    print("\n" + viz.negrito("Checagem do coeficiente s^0 = R.b + Kt.Ke (ponto de atenção do enunciado):"))
    print(f"  R.b + Kt.Ke  = {PARAMS.R * PARAMS.b:.6g} + {PARAMS.Kt * PARAMS.Ke:.6g}"
          f" = {den_num[2]:.6g}  (valor citado no enunciado: 2.121e-3)")
    print(f"  Ganho DC = Kt / (R.b + Kt.Ke) = {dc_gain_formula:.6f} rad/(s.V)")
    print(f"  PARAMS.dc_gain (propriedade)   = {PARAMS.dc_gain:.6f} rad/(s.V)  "
          f"(diferença: {erro_dc:.2e})")

    todas_ok = all(ok for _, ok in conferencias) and erro_dc < 1e-9 and \
        max(abs(num_num - num_lib), *[abs(a - b_) for a, b_ in zip(den_num, den_lib)]) < 1e-9

    print()
    if todas_ok:
        print(viz.verde(viz.negrito(
            "Nenhum erro de digitação encontrado: 2.121e-3 é o valor correto de R.b + Kt.Ke, "
            "e bate com o ganho DC de 21.2164 rad/(s.V) citado no enunciado.")))
    else:
        print(viz.vermelho(viz.negrito("Divergência encontrada — revise os parâmetros ou a álgebra.")))

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print("  A Transformada de Laplace troca uma EDO acoplada de 2ª ordem por uma equação")
    print("  algébrica em s — o que antes exigia resolver duas equações diferenciais")
    print("  simultâneas vira dividir dois polinômios. É essa função de transferência que")
    print("  os scripts seguintes desta aula (polos/zeros, Bode, margens) vão explorar.")

    return 0 if todas_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
