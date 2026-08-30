"""Derivação simbólica (SymPy) das equações de diferenças do PID discreto.

Objetivo desta Unidade 4: provar que o C gerado na Aula 13 não é digitado à
mão, e sim derivado da forma contínua do controlador — a mesma
`pid_transfer_function` de `nexabot.controllers` — por um mapeamento de
discretização explícito (Euler para trás / *backward Euler*), e que o
resultado dessa derivação coincide, termo a termo, com o contrato numérico
documentado em `DiscretePID.step` (REQ-CTRL-001, REQ-CTRL-002, REQ-CTRL-003).

O caminho é:

    C(s) = Kp + Ki/s + Kd.s/(1 + tau_f.s)      <- forma contínua (Aula 5/6)
             |  substitui s = (1 - z^-1)/Ts     <- Euler para trás
             v
    C(z) = Kp + Gi(z) + Gd(z)                  <- forma discreta racional
             |  polinômio em z^-1, resolvido para a amostra atual
             v
    I[k] = I[k-1] + Ki.Ts.e[k]
    D[k] = (Kd.(e[k]-e[k-1]) + tau_f.D[k-1]) / (tau_f + Ts)

Nenhuma dessas duas equações é escrita "de memória": ambas saem de
`difference_equation(...)`, uma função genérica que converte qualquer
H(z) = Y(z)/E(z) racional em uma equação de diferenças causal.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

# Símbolos do domínio Z e do domínio contínuo, compartilhados pelo módulo.
s, z, z_inv = sp.symbols("s z z_inv")
Ts, Kp, Ki, Kd, tau_f = sp.symbols("Ts Kp Ki Kd tau_f", positive=True)


def backward_euler_map() -> sp.Expr:
    """Mapeamento de discretização s -> (1 - z^-1)/Ts (Euler para trás).

    É a mesma escolha de discretização descrita no docstring de
    `DiscretePID`: integral por Euler para trás, derivada por diferença
    para trás. Escolhida (em vez de Tustin) porque é a forma mais comum em
    código embarcado de baixo custo computacional — sem pré-distorção de
    frequência, um multiply-add por termo.
    """
    return (1 - z_inv) / Ts


def continuous_pid(kind: str) -> sp.Expr:
    """Devolve o termo contínuo do PID pedido (`'integral'` ou `'derivative'`).

    Usa a mesma estrutura de `nexabot.controllers.pid_transfer_function`
    (Kp + Ki/s + Kd.N.s/(s+N), com N = 1/tau_f), isolando cada termo.
    """
    if kind == "integral":
        return Ki / s
    if kind == "derivative":
        n = 1 / tau_f
        return Kd * n * s / (s + n)
    raise ValueError(f"termo desconhecido: {kind!r}")


def difference_equation(H: sp.Expr, delay_var: sp.Symbol = z_inv):
    """Converte H(z) = Y(z)/E(z) racional em coeficientes de uma equação de
    diferenças causal.

    Devolve `(den_coeffs, num_coeffs)` tais que, com y[k] a saída e e[k] a
    entrada:

        sum_i den_coeffs[i] * y[k-i]  ==  sum_i num_coeffs[i] * e[k-i]

    normalizados para `den_coeffs[0] == 1`. É uma conversão puramente
    algébrica (extração de coeficientes de polinômios em z^-1), a mesma
    operação que um livro-texto de controle digital faz manualmente — aqui
    feita por SymPy para eliminar erro de transcrição.
    """
    H = sp.together(H)
    num, den = sp.fraction(H)
    num_poly = sp.Poly(sp.expand(num), delay_var)
    den_poly = sp.Poly(sp.expand(den), delay_var)

    degree = max(num_poly.degree(), den_poly.degree())

    def _coeffs(poly: sp.Poly) -> list[sp.Expr]:
        return [poly.coeff_monomial(delay_var**i) for i in range(degree + 1)]

    num_coeffs = _coeffs(num_poly)
    den_coeffs = _coeffs(den_poly)

    lead = den_coeffs[0]
    num_coeffs = [sp.simplify(c / lead) for c in num_coeffs]
    den_coeffs = [sp.simplify(c / lead) for c in den_coeffs]
    return den_coeffs, num_coeffs


@dataclass(frozen=True)
class DerivedRecurrence:
    """Uma equação de diferenças derivada, com sua forma simbólica e textual."""

    nome: str
    expressao: sp.Expr
    equacao_str: str


def derive_integral_recurrence() -> DerivedRecurrence:
    """Deriva I[k] a partir de Gi(s) = Ki/s pela substituição de Euler p/ trás."""
    Gi_s = continuous_pid("integral")
    Gi_z = sp.simplify(Gi_s.subs(s, backward_euler_map()))
    den_coeffs, num_coeffs = difference_equation(Gi_z)

    # den_coeffs = [1, -1]  ->  I[k] - I[k-1] = num_coeffs[0]*e[k]
    assert den_coeffs == [1, sp.Integer(-1)], den_coeffs
    I_km1, e_k = sp.symbols("I_km1 e_k")
    I_k = sp.simplify(I_km1 + num_coeffs[0] * e_k)
    return DerivedRecurrence(
        nome="integral",
        expressao=I_k,
        equacao_str=f"I[k] = I[k-1] + {sp.nsimplify(num_coeffs[0])}*e[k]",
    )


def derive_derivative_recurrence() -> DerivedRecurrence:
    """Deriva D[k] a partir de Gd(s) = Kd.s/(1+tau_f.s) por Euler p/ trás."""
    Gd_s = continuous_pid("derivative")
    Gd_z = sp.simplify(Gd_s.subs(s, backward_euler_map()))
    den_coeffs, num_coeffs = difference_equation(Gd_z)

    # den_coeffs = [1, -tau_f/(tau_f+Ts)], num_coeffs = [Kd/(tau_f+Ts), -Kd/(tau_f+Ts)]
    D_km1, e_k, e_km1 = sp.symbols("D_km1 e_k e_km1")
    a1 = den_coeffs[1]
    b0, b1 = num_coeffs[0], num_coeffs[1]
    D_k = sp.simplify(-a1 * D_km1 + b0 * e_k + b1 * e_km1)

    # Reescreve na forma do contrato de DiscretePID: (Kd.(e-e_prev)+tau_f.D_prev)/(tau_f+Ts)
    contrato = (Kd * (e_k - e_km1) + tau_f * D_km1) / (tau_f + Ts)
    diff = sp.simplify(D_k - contrato)
    if diff != 0:
        raise AssertionError(
            "derivação simbólica diverge do contrato de DiscretePID.step: "
            f"resíduo = {diff}"
        )

    return DerivedRecurrence(
        nome="derivada filtrada",
        expressao=contrato,
        equacao_str="D[k] = (Kd*(e[k]-e[k-1]) + tau_f*D[k-1]) / (tau_f + Ts)",
    )


def derive_all() -> dict[str, DerivedRecurrence]:
    """Deriva as duas recorrências (integral e derivativa) do PID discreto."""
    return {
        "integral": derive_integral_recurrence(),
        "derivada": derive_derivative_recurrence(),
    }
