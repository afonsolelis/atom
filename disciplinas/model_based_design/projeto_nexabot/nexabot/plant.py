"""Modelo da planta do NexaBot em espaço de estados e função de transferência.

Equações do motor CC (Aula 2):

    L . di/dt = V - R.i - Ke.w
    J . dw/dt = Kt.i - b.w - tau_load

Com x = [i, w]^T, u = V e y = w:

    A = [[-R/L, -Ke/L],
         [ Kt/J, -b/J ]]
    B = [[1/L], [0]]
    C = [[0, 1]]
    D = [[0]]

Rastreabilidade: REQ-PLANT-001.
"""

from __future__ import annotations

import numpy as np

from .params import PARAMS, NexaBotParams


def state_space_matrices(p: NexaBotParams = PARAMS):
    """Devolve as matrizes (A, B, C, D) do modelo contínuo do NexaBot."""
    A = np.array(
        [
            [-p.R / p.L, -p.Ke / p.L],
            [p.Kt / p.J, -p.b / p.J],
        ]
    )
    B = np.array([[1.0 / p.L], [0.0]])
    C = np.array([[0.0, 1.0]])
    D = np.array([[0.0]])
    return A, B, C, D


def state_space(p: NexaBotParams = PARAMS):
    """Modelo contínuo como objeto `control.StateSpace`."""
    import control as ct

    A, B, C, D = state_space_matrices(p)
    return ct.ss(A, B, C, D, name="NexaBot")


def transfer_function(p: NexaBotParams = PARAMS):
    """Função de transferência W(s)/V(s) do NexaBot.

        W(s)/V(s) = Kt / (L.J.s^2 + (R.J + L.b).s + (R.b + Kt.Ke))
    """
    import control as ct

    num = [p.Kt]
    den = [p.L * p.J, p.R * p.J + p.L * p.b, p.R * p.b + p.Kt * p.Ke]
    return ct.tf(num, den, name="NexaBot")


def derivative(x: np.ndarray, u: float, tau_load: float = 0.0,
               p: NexaBotParams = PARAMS) -> np.ndarray:
    """Derivada do estado dx/dt para integração numérica manual.

    `x` é [corrente, velocidade angular do motor]; `u` é a tensão aplicada em
    volts; `tau_load` é o torque de carga em N.m (positivo = frena o eixo).
    """
    i, w = float(x[0]), float(x[1])
    di = (u - p.R * i - p.Ke * w) / p.L
    dw = (p.Kt * i - p.b * w - tau_load) / p.J
    return np.array([di, dw])


def simulate(u_of_t, t_end: float, dt: float = 1.0e-4,
             x0: np.ndarray | None = None, tau_load_of_t=None,
             p: NexaBotParams = PARAMS):
    """Integra a planta por Runge-Kutta de 4a ordem com passo fixo.

    Este integrador existe para que o estudante veja a planta rodando sem
    depender de nenhuma biblioteca de simulação: é o mesmo laço que, na
    Unidade 4, passa a viver dentro do FMU em C.

    Devolve (t, X) com X de forma (n_amostras, 2).
    """
    if x0 is None:
        x0 = np.zeros(2)
    n = int(round(t_end / dt))
    t = np.linspace(0.0, n * dt, n + 1)
    X = np.zeros((n + 1, 2))
    X[0] = x0
    x = np.array(x0, dtype=float)

    for k in range(n):
        tk = t[k]
        u = float(u_of_t(tk)) if callable(u_of_t) else float(u_of_t)
        u = float(np.clip(u, -p.V_max, p.V_max))
        tl = float(tau_load_of_t(tk)) if callable(tau_load_of_t) else float(tau_load_of_t or 0.0)

        k1 = derivative(x, u, tl, p)
        k2 = derivative(x + 0.5 * dt * k1, u, tl, p)
        k3 = derivative(x + 0.5 * dt * k2, u, tl, p)
        k4 = derivative(x + dt * k3, u, tl, p)
        x = x + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        X[k + 1] = x

    return t, X
