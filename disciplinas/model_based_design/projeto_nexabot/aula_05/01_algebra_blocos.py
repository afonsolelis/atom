#!/usr/bin/env python3
"""Aula 5 — Script 1/4: álgebra de blocos — série, paralelo e realimentação.

O que este script demonstra
----------------------------
Toda malha de controle "profissional" (biblioteca `control`, Simulink, etc.)
esconde, por trás de `ct.series`/`ct.parallel`/`ct.feedback`, a mesmíssima
álgebra de funções de transferência que se faz à mão: multiplicar frações
(série), somar frações (paralelo) e resolver G/(1+G.H) (realimentação).

Este script monta um controlador PD simples a partir de dois blocos
elementares — um ganho proporcional Kp e um ganho derivativo puro Kd.s — e
combina isso com a planta G(s) do NexaBot em quatro passos:

  1. SÉRIE:          um bloco de ganho Kp em série com G(s).
  2. PARALELO:        Kp e Kd.s em paralelo formam o controlador C(s) = Kp + Kd.s.
  3. SÉRIE (de novo):  C(s) em série com G(s) dá o caminho direto L(s) = C(s).G(s).
  4. REALIMENTAÇÃO:    realimentação unitária negativa fecha a malha:
                        T(s) = L(s) / (1 + L(s)).

Para CADA um dos quatro passos, o resultado do `control` é refeito à mão com
`sympy` (as mesmas frações racionais, substituindo os coeficientes numéricos
de G(s)) e os coeficientes de numerador/denominador dos dois resultados são
comparados numericamente — se não baterem, o script termina com erro. Isso é
a prova de que `ct.series/parallel/feedback` não fazem mágica: são a mesma
álgebra de segundo grau que se aprende no papel.

Como rodar
----------
    .venv/bin/python aula_05/01_algebra_blocos.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import control as ct  # noqa: E402
import numpy as np  # noqa: E402
import sympy as sp  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.controllers import step_metrics  # noqa: E402
from nexabot.plant import transfer_function  # noqa: E402

s_sym = sp.symbols("s")


# --------------------------------------------------------------------------
# Utilidades de conversão control <-> sympy e comparação de polinômios
# --------------------------------------------------------------------------

def ct_para_sympy(tf: "ct.TransferFunction"):
    """Converte uma `control.TransferFunction` SISO em fração racional sympy.

    Os coeficientes são convertidos com `sp.Rational` (não `sp.Float`) porque
    `sympy.cancel` só cancela fatores comuns de forma exata quando os
    coeficientes vivem num corpo exato — com `Float` o cancelamento de
    numerador/denominador fica incompleto por causa de erros de arredondamento
    binário, e os graus dos polinômios "não fecham" na comparação final.
    """
    num = [sp.Rational(c) for c in tf.num[0][0]]
    den = [sp.Rational(c) for c in tf.den[0][0]]
    ns = sum(c * s_sym ** (len(num) - 1 - i) for i, c in enumerate(num))
    ds = sum(c * s_sym ** (len(den) - 1 - i) for i, c in enumerate(den))
    return ns / ds


def normalizar_coeficientes(expr) -> tuple[list[float], list[float]]:
    """Extrai (coef. do numerador, coef. do denominador) normalizados.

    `sp.cancel` faz o MDC exato entre numerador e denominador (equivalente a
    simplificar a fração à mão); o denominador é normalizado para ter
    coeficiente líder 1, para que a comparação entre duas frações
    matematicamente iguais não dependa de um fator de escala comum.
    """
    expr = sp.cancel(sp.together(expr))
    numer, denom = sp.fraction(expr)
    coef_num = [float(c) for c in sp.Poly(sp.expand(numer), s_sym).all_coeffs()]
    coef_den = [float(c) for c in sp.Poly(sp.expand(denom), s_sym).all_coeffs()]
    lider = coef_den[0]
    return [c / lider for c in coef_num], [c / lider for c in coef_den]


def _com_zeros_a_esquerda(a: list[float], b: list[float]):
    """Preenche o polinômio de grau menor com zeros à esquerda para comparar."""
    n = max(len(a), len(b))
    return [0.0] * (n - len(a)) + list(a), [0.0] * (n - len(b)) + list(b)


def comparar_tf(nome: str, expr_sympy, tf_control: "ct.TransferFunction",
                 tol: float = 1e-6) -> bool:
    """Compara a fração racional sympy com a `control.TransferFunction`.

    Imprime uma tabela com os coeficientes dos dois lados e devolve `True`
    se baterem dentro da tolerância relativa `tol`.
    """
    cn_sym, cd_sym = normalizar_coeficientes(expr_sympy)
    cn_ctl, cd_ctl = normalizar_coeficientes(ct_para_sympy(tf_control))

    cn_sym, cn_ctl = _com_zeros_a_esquerda(cn_sym, cn_ctl)
    cd_sym, cd_ctl = _com_zeros_a_esquerda(cd_sym, cd_ctl)

    ok_num = np.allclose(cn_sym, cn_ctl, rtol=tol, atol=1e-9)
    ok_den = np.allclose(cd_sym, cd_ctl, rtol=tol, atol=1e-9)
    ok = ok_num and ok_den

    linhas = []
    for i, (a, b) in enumerate(zip(cn_sym, cn_ctl)):
        grau = len(cn_sym) - 1 - i
        linhas.append([f"num s^{grau}", f"{a:.6g}", f"{b:.6g}"])
    for i, (a, b) in enumerate(zip(cd_sym, cd_ctl)):
        grau = len(cd_sym) - 1 - i
        linhas.append([f"den s^{grau}", f"{a:.6g}", f"{b:.6g}"])

    viz.tabela(
        ["coeficiente", "sympy (à mão)", "control (biblioteca)"],
        linhas,
        titulo_tabela=f"{nome} — comparação sympy vs control",
    )
    status = viz.verde("BATEU") if ok else viz.vermelho("NÃO BATEU")
    print(f"  -> {status} (tolerância relativa {tol:.0e})\n")
    return ok


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------

def main() -> int:
    print(viz.titulo("NexaBot — Aula 5 — Álgebra de blocos: série, paralelo, realimentação"))

    G = transfer_function()
    G_sym = ct_para_sympy(G)
    print("Planta G(s) (função de transferência V -> velocidade angular do motor):")
    print(f"  {G}")

    Kp = 6.0
    Kd = 0.01
    print(f"Controlador PD elementar: bloco proporcional Kp = {Kp:.2f} e bloco "
          f"derivativo puro Kd.s com Kd = {Kd:.3f}.\n")

    # --- Passo 1: SÉRIE — Kp em série com G(s) ----------------------------
    print(viz.negrito("Passo 1 — SÉRIE: Kp em série com a planta G(s)"))
    Kp_bloco = ct.tf([Kp], [1])
    KpG_ctl = ct.series(Kp_bloco, G)
    KpG_sym = sp.Rational(Kp) * G_sym
    ok1 = comparar_tf("Kp . G(s)  [ct.series(Kp, G)]", KpG_sym, KpG_ctl)

    # --- Passo 2: PARALELO — Kp e Kd.s formam o controlador C(s) ----------
    print(viz.negrito("Passo 2 — PARALELO: Kp em paralelo com Kd.s forma o controlador C(s)"))
    Kd_bloco = ct.tf([Kd, 0], [1])
    C_ctl = ct.parallel(Kp_bloco, Kd_bloco)
    # Coeficientes como sp.Rational (não float puro): mantém a álgebra exata
    # nos passos seguintes, que somam frações e por isso exigem cancelamento
    # de fatores comuns — com Float o cancelamento fica incompleto por
    # arredondamento binário e os graus dos polinômios não "fecham".
    C_sym = sp.Rational(Kp) + sp.Rational(Kd) * s_sym
    ok2 = comparar_tf("C(s) = Kp + Kd.s  [ct.parallel(Kp, Kd.s)]", C_sym, C_ctl)

    # --- Passo 3: SÉRIE — C(s) em série com G(s) dá o caminho direto L(s) -
    print(viz.negrito("Passo 3 — SÉRIE: C(s) em série com G(s) dá o caminho direto L(s)"))
    L_ctl = ct.series(C_ctl, G)
    L_sym = sp.cancel(C_sym * G_sym)
    ok3 = comparar_tf("L(s) = C(s) . G(s)  [ct.series(C, G)]", L_sym, L_ctl)

    # --- Passo 4: REALIMENTAÇÃO — malha fechada unitária negativa ---------
    print(viz.negrito("Passo 4 — REALIMENTAÇÃO: malha fechada com realimentação unitária negativa"))
    T_ctl = ct.feedback(L_ctl, 1, sign=-1)
    T_sym = sp.cancel(L_sym / (1 + L_sym))
    ok4 = comparar_tf("T(s) = L(s) / (1 + L(s))  [ct.feedback(L, 1, sign=-1)]", T_sym, T_ctl)

    todos_ok = ok1 and ok2 and ok3 and ok4

    # --- Resposta ao degrau da malha fechada resultante -------------------
    t, y = ct.step_response(T_ctl, T=np.linspace(0.0, 0.05, 2000))
    m = step_metrics(t, y, r=1.0)

    viz.plot_ascii(t, y, altura=14, largura=64,
                    titulo_grafico="Resposta ao degrau unitário de T(s) = L/(1+L)",
                    y_ref=1.0, unidade_x="s")

    print()
    viz.tabela(
        ["grandeza", "valor"],
        [
            ["polos de T(s)", ", ".join(f"{p:.2f}" for p in T_ctl.poles())],
            ["ganho DC de T(s)", f"{float(ct.dcgain(T_ctl)):.4f}"],
            ["sobressinal", f"{m['overshoot_pct']:.2f} %"],
            ["tempo de subida (10-90%)", f"{m['t_rise_s'] * 1000:.3f} ms"],
            ["tempo de acomodação (±2%)", f"{m['t_settle_s'] * 1000:.3f} ms"],
            ["erro em regime (referência=1)", f"{m['steady_state_error']:.4f}"],
        ],
        titulo_tabela="Malha fechada T(s) resultante da álgebra de blocos",
    )

    fig_path = "aula05_algebra_blocos_step.png"
    viz.figura_resposta_degrau(t, y, y_ref=1.0,
                                titulo_fig="NexaBot — malha fechada T(s) montada por álgebra de blocos",
                                ylabel="saída (normalizada)",
                                nome_arquivo=fig_path)

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print("  ct.series, ct.parallel e ct.feedback não fazem nada que não se faça à mão:")
    print("  multiplicar frações, somar frações e resolver G/(1+G.H). A vantagem da")
    print("  biblioteca é evitar erro de álgebra em graus altos — mas o resultado é")
    print("  sempre auditável, e é isso que os quatro cheques acima confirmaram.")

    if todos_ok:
        print(viz.verde(viz.negrito(
            "\nTodos os 4 passos de álgebra de blocos bateram entre control e sympy.")))
        return 0
    print(viz.vermelho(viz.negrito(
        "\nPelo menos um passo NÃO bateu entre control e sympy — revise a álgebra.")))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
