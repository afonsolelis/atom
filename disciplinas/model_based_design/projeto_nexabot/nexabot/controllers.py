"""Controladores do NexaBot: PID contínuo, PID discreto e realimentação de estados.

O `DiscretePID` desta classe é o modelo de referência da Unidade 4: o código C
gerado na Aula 13 precisa reproduzir exatamente esta aritmética, e a Aula 14
compara as duas implementações amostra a amostra.

Rastreabilidade: REQ-CTRL-001 (rastreamento de velocidade), REQ-CTRL-002
(saturação do atuador), REQ-CTRL-003 (anti-windup).
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .params import PARAMS, NexaBotParams


def pid_transfer_function(Kp: float, Ki: float, Kd: float, N: float = 20.0):
    """PID contínuo com derivativo filtrado: Kp + Ki/s + Kd.N.s/(s+N)."""
    import control as ct

    s = ct.tf("s")
    return Kp + Ki / s + Kd * N * s / (s + N)


@dataclass
class DiscretePID:
    """PID discreto de posição, com filtro derivativo, saturação e anti-windup.

    Discretização: integral por Euler para trás (backward Euler) e derivada
    por diferença para trás com filtro de primeira ordem. Essa é a forma
    adotada em código embarcado porque não exige histórico longo: o estado
    cabe em duas variáveis (`integral` e `d_state`).

    Contrato numérico (o C gerado deve reproduzi-lo):

        e[k]   = r[k] - y[k]
        I[k]   = I[k-1] + Ki.Ts.e[k]
        D[k]   = (Kd.(e[k]-e[k-1]) + tau_f.D[k-1]) / (tau_f + Ts)
        u_ns   = Kp.e[k] + I[k] + D[k]
        u[k]   = sat(u_ns, -u_max, +u_max)
        se u[k] != u_ns:  I[k] <- I[k] + Kaw.(u[k] - u_ns).Ts   (anti-windup)
    """

    Kp: float
    Ki: float
    Kd: float = 0.0
    Ts: float = PARAMS.Ts
    u_max: float = PARAMS.V_max
    tau_f: float = 0.01          # constante do filtro derivativo [s]
    Kaw: float = 1.0             # ganho de anti-windup (back-calculation)

    integral: float = field(default=0.0, init=False)
    e_prev: float = field(default=0.0, init=False)
    d_state: float = field(default=0.0, init=False)

    def reset(self) -> None:
        """Zera o estado interno. Obrigatório ao sair de FAULT (REQ-SAFE-004)."""
        self.integral = 0.0
        self.e_prev = 0.0
        self.d_state = 0.0

    def step(self, r: float, y: float) -> float:
        """Executa um passo do controlador e devolve a tensão de comando [V]."""
        e = r - y

        self.integral += self.Ki * self.Ts * e

        d = (self.Kd * (e - self.e_prev) + self.tau_f * self.d_state) / (self.tau_f + self.Ts)

        u_unsat = self.Kp * e + self.integral + d
        u = min(max(u_unsat, -self.u_max), self.u_max)

        if u != u_unsat:
            self.integral += self.Kaw * (u - u_unsat) * self.Ts

        self.e_prev = e
        self.d_state = d
        return u


def ziegler_nichols(Ku: float, Tu: float, kind: str = "classic_pid") -> tuple[float, float, float]:
    """Sintonia de Ziegler-Nichols pelo método do ganho crítico.

    `Ku` é o ganho crítico e `Tu` o período de oscilação sustentada, ambos
    obtidos experimentalmente na Aula 6.
    """
    tables = {
        "p": (0.50 * Ku, 0.0, 0.0),
        "pi": (0.45 * Ku, 0.54 * Ku / Tu, 0.0),
        "classic_pid": (0.60 * Ku, 1.20 * Ku / Tu, 0.075 * Ku * Tu),
        "no_overshoot": (0.20 * Ku, 0.40 * Ku / Tu, 0.066 * Ku * Tu),
    }
    if kind not in tables:
        raise ValueError(f"sintonia desconhecida: {kind!r}; use {sorted(tables)}")
    return tables[kind]


def state_feedback_gain(poles, p: NexaBotParams = PARAMS) -> np.ndarray:
    """Calcula K por alocação de polos para u = -K.x (Aula 4)."""
    import control as ct

    from .plant import state_space_matrices

    A, B, _, _ = state_space_matrices(p)
    return np.asarray(ct.place(A, B, poles))


def lqr_gain(Q=None, R=None, p: NexaBotParams = PARAMS):
    """Calcula o ganho ótimo K do regulador linear quadrático (Aula 4)."""
    import control as ct

    from .plant import state_space_matrices

    A, B, _, _ = state_space_matrices(p)
    if Q is None:
        Q = np.diag([1.0, 10.0])
    if R is None:
        R = np.array([[0.1]])
    K, S, E = ct.lqr(A, B, Q, R)
    return np.asarray(K), np.asarray(S), np.asarray(E)


def step_metrics(t: np.ndarray, y: np.ndarray, r: float, band: float = 0.02) -> dict:
    """Métricas da resposta ao degrau usadas como critério de aceitação.

    Devolve sobressinal percentual, tempo de subida 10-90%, tempo de
    acomodação dentro da faixa `band` e erro em regime permanente.
    """
    y = np.asarray(y, dtype=float)
    t = np.asarray(t, dtype=float)
    y_final = float(np.mean(y[-max(1, len(y) // 50):]))

    overshoot = (float(np.max(y)) - r) / r * 100.0 if r != 0 else float("nan")

    def _cross(level):
        idx = np.argmax(y >= level)
        return float(t[idx]) if np.any(y >= level) else float("nan")

    t_rise = _cross(0.9 * r) - _cross(0.1 * r)

    outside = np.where(np.abs(y - r) > band * abs(r))[0]
    t_settle = float(t[outside[-1] + 1]) if len(outside) and outside[-1] + 1 < len(t) else 0.0

    return {
        "overshoot_pct": overshoot,
        "t_rise_s": t_rise,
        "t_settle_s": t_settle,
        "steady_state_error": r - y_final,
        "y_final": y_final,
    }
