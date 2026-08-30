#!/usr/bin/env python3
"""Aula 13 — Do modelo ao C (script 1/4).

Deriva simbolicamente, com SymPy, as duas equações de diferenças do PID
discreto do NexaBot — a integral e a derivada filtrada — a partir da forma
CONTÍNUA do controlador (`nexabot.controllers.pid_transfer_function`), por
discretização de Euler para trás. Mostra o caminho passo a passo e verifica,
por igualdade simbólica, que o resultado bate com o contrato numérico
documentado em `DiscretePID.step` (nexabot/controllers.py).

Este é o ponto central da aula: o C gerado na Aula 13 não vem de digitar a
fórmula do PID de memória — vem de uma cadeia de transformação algébrica
auditável, do contínuo ao discreto.

Rodar:
    .venv/bin/python aula_13/01_do_modelo_ao_c.py

Saída esperada (resumo): as formas contínuas Gi(s) e Gd(s), o mapeamento de
discretização usado, as equações de diferenças derivadas e a confirmação
"OK" de que coincidem com o contrato de DiscretePID.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sympy as sp  # noqa: E402

from nexabot.codegen import derive  # noqa: E402


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def main() -> None:
    print(linha("="))
    print("Aula 13 — Do modelo (contínuo) ao código (C), passo a passo")
    print(linha("="))

    print("\n1) Forma contínua do PID (nexabot.controllers.pid_transfer_function):")
    print("   C(s) = Kp + Ki/s + Kd.s/(1 + tau_f.s)")
    print("   (equivalente a Kp + Ki/s + Kd.N.s/(s+N), com N = 1/tau_f)")

    print("\n2) Mapeamento de discretização (Euler para trás):")
    mapeamento = derive.backward_euler_map()
    print(f"   s -> {mapeamento}")
    print("   Escolhido por ser a discretização padrão em código embarcado:")
    print("   sem pré-distorção de frequência, um multiply-add por termo,")
    print("   estado cabendo em uma única variável por termo (I, D).")

    print("\n3) Termo integral: Gi(s) = Ki/s")
    Gi_s = derive.continuous_pid("integral")
    Gi_z = sp.simplify(Gi_s.subs(derive.s, mapeamento))
    print(f"   Gi(s)            = {Gi_s}")
    print(f"   Gi(z) = Gi(s)|s=(1-z^-1)/Ts = {Gi_z}")
    den_i, num_i = derive.difference_equation(Gi_z)
    print(f"   coeficientes do denominador (em z^-1): {den_i}")
    print(f"   coeficientes do numerador   (em z^-1): {num_i}")
    rec_integral = derive.derive_integral_recurrence()
    print(f"   => {rec_integral.equacao_str}")

    print("\n4) Termo derivativo filtrado: Gd(s) = Kd.s/(1 + tau_f.s)")
    Gd_s = derive.continuous_pid("derivative")
    Gd_z = sp.simplify(Gd_s.subs(derive.s, mapeamento))
    print(f"   Gd(s)            = {sp.simplify(Gd_s)}")
    print(f"   Gd(z) = Gd(s)|s=(1-z^-1)/Ts = {Gd_z}")
    den_d, num_d = derive.difference_equation(Gd_z)
    print(f"   coeficientes do denominador (em z^-1): {den_d}")
    print(f"   coeficientes do numerador   (em z^-1): {num_d}")
    rec_derivada = derive.derive_derivative_recurrence()
    print(f"   => {rec_derivada.equacao_str}")

    print("\n5) Verificação contra o contrato de DiscretePID.step:")
    e_k, e_km1, D_km1 = sp.symbols("e_k e_km1 D_km1")
    Kd, tau_f, Ts = derive.Kd, derive.tau_f, derive.Ts
    contrato_D = (Kd * (e_k - e_km1) + tau_f * D_km1) / (tau_f + Ts)
    residuo = sp.simplify(rec_derivada.expressao - contrato_D)
    print(f"   D[k] derivado - D[k] do contrato (docstring) = {residuo}")
    ok = residuo == 0
    print(f"   {'OK' if ok else 'DIVERGIU'}: derivação simbólica {'==' if ok else '!='}"
          " contrato de DiscretePID.step")
    if not ok:
        raise SystemExit(1)

    print("\n" + linha("="))
    print("Conclusão: I[k] e D[k] gerados pela Aula 13 em C vêm desta derivação,")
    print("não de uma fórmula copiada — ver nexabot/codegen/derive.py e generate.py.")
    print(linha("="))


if __name__ == "__main__":
    main()
