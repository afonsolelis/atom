#!/usr/bin/env python3
"""Aula 13 — Script 4/4: desafio — por que Euler para trás, e não Tustin?

O que este script faz
----------------------
`nexabot.codegen.derive` discretiza o termo integral do PID por Euler para
trás (`s -> (1-z^-1)/Ts`), chegando em `I[k] = I[k-1] + Ki.Ts.e[k]` — um
único estado (`integral`), sem precisar guardar `e[k-1]` para esse termo.

DESAFIO: complete `mapeamento_tustin` com a transformação bilinear (Tustin)
`s -> (2/Ts).(1-z^-1)/(1+z^-1)` e descubra, RODANDO o script, quantos termos
de estado a integral discretizada por Tustin exigiria — e por que isso
importa para código embarcado.

Como rodar
----------
    .venv/bin/python aula_13/04_desafio.py

Saída esperada (resumo)
------------------------
Duas equações de diferenças para o mesmo Gi(s)=Ki/s (uma por Euler para
trás, outra por Tustin) e uma conclusão sobre por que o gerador da Aula 13
usa Euler para trás.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import sympy as sp  # noqa: E402

from nexabot.codegen import derive  # noqa: E402


def mapeamento_tustin() -> sp.Expr:
    """DESAFIO: mapeamento de Tustin (transformação bilinear).

    s -> (2/Ts) . (1 - z^-1) / (1 + z^-1)

    É a discretização que preserva melhor a resposta em frequência (usada,
    por exemplo, quando se quer casar o ganho em uma frequência específica
    via pré-distorção) — mas isso tem um custo em estado, como este script
    mostra.
    """
    # --- solução de referência (apague e reescreva como exercício) ---
    return (2 / derive.Ts) * (1 - derive.z_inv) / (1 + derive.z_inv)


def main() -> None:
    print("=" * 78)
    print("AULA 13 — Desafio: Euler para trás vs. Tustin no termo integral")
    print("=" * 78)

    Gi_s = derive.continuous_pid("integral")
    print(f"\nGi(s) = Ki/s = {Gi_s}")

    print("\n--- Euler para trás (o que o gerador de código usa) ---")
    Gi_z_euler = sp.simplify(Gi_s.subs(derive.s, derive.backward_euler_map()))
    den_euler, num_euler = derive.difference_equation(Gi_z_euler)
    n_estados_euler = sum(1 for c in den_euler[1:] if c != 0) + sum(1 for c in num_euler[1:] if c != 0)
    print(f"  Gi(z)       = {Gi_z_euler}")
    print(f"  denominador = {den_euler}  (coefs. de z^-1, do grau 0 em diante)")
    print(f"  numerador   = {num_euler}")
    print(f"  => I[k] = I[k-1] + Ki.Ts.e[k]   (precisa de e[k-1]? "
          f"{'sim' if num_euler[1:] and any(c != 0 for c in num_euler[1:]) else 'não'})")

    print("\n--- Tustin / bilinear (desafio) ---")
    Gi_z_tustin = sp.simplify(Gi_s.subs(derive.s, mapeamento_tustin()))
    den_tustin, num_tustin = derive.difference_equation(Gi_z_tustin)
    print(f"  Gi(z)       = {Gi_z_tustin}")
    print(f"  denominador = {den_tustin}")
    print(f"  numerador   = {num_tustin}")
    precisa_e_km1 = len(num_tustin) > 1 and num_tustin[1] != 0
    print(f"  => precisa de e[k-1] além de I[k-1]? {'sim' if precisa_e_km1 else 'não'}")

    print("\n" + "=" * 78)
    print("Conclusão")
    print("=" * 78)
    if precisa_e_km1:
        print("Tustin faz a integral virar uma regra trapezoidal: I[k] depende de")
        print("I[k-1] E de (e[k]+e[k-1]) -- exige guardar e[k-1] SÓ para a integral")
        print("(o termo derivativo já guarda e_prev, mas por um motivo diferente).")
        print("Euler para trás evita essa variável extra: em um firmware com RAM")
        print("contada em bytes, cada `double` de estado a menos importa. É por")
        print("isso que nexabot/codegen/derive.py usa Euler para trás, não Tustin")
        print("-- a escolha de discretização é uma decisão de engenharia, não um")
        print("detalhe arbitrário.")
    else:
        print("Resultado inesperado -- revise mapeamento_tustin().")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
