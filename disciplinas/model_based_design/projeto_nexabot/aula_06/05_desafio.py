#!/usr/bin/env python3
"""Aula 6 — Script 5/5: DESAFIO — ajuste manual de PID sob dois requisitos.

Enunciado
---------
O time de engenharia do NexaBot definiu dois requisitos para o controlador
de velocidade do eixo de tração, para um degrau de referência de
`w_ref = 150 rad/s` (~0,375 m/s) partindo do repouso:

  REQ-A: overshoot máximo de 10% em relação à referência.
  REQ-B: tempo de acomodação (faixa de 2%) de no máximo 250 ms.

Complete `ajustar_pid_manual` para:

1. Escolher valores de `Kp`, `Ki`, `Kd` (por tentativa e erro, ou por algum
   raciocínio de sintonia à sua escolha — não precisa ser Ziegler-Nichols).
2. Montar um `DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=PARAMS.Ts)`.
3. Simular a malha fechada com o loop manual RK4 (`simular_malha_fechada_pid`,
   já implementado abaixo) para `w_ref = 150.0` rad/s por `t_end = 1.0` s,
   partindo do repouso.
4. Calcular as métricas com `nexabot.controllers.step_metrics`.
5. Devolver um dicionário com `Kp`, `Ki`, `Kd`, `overshoot_pct`, `t_settle_s`.

Critério de aceitação
----------------------
Rodando este script (sem argumentos), o estudante deve obter (verificado
rodando uma implementação de referência: Kp=0,5, Ki=2,0, Kd=0,002 — não é a
única solução válida, apenas uma prova de que a faixa é alcançável):

- `overshoot_pct` até 10,0% (a referência obteve ≈0,53%);
- `t_settle_s` até 0,250 s / 250 ms (a referência obteve ≈0,076 s / 76 ms);
- erro em regime (`abs(steady_state_error)`) até 2,0 rad/s (a referência
  obteve ≈0,035 rad/s).

O script IMPRIME o enunciado e, se `ajustar_pid_manual` ainda não tiver sido
implementada, avisa claramente o que falta — mas termina sem lançar exceção,
como convém a um esqueleto de desafio.

Como rodar
----------
    .venv/bin/python aula_06/05_desafio.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import numpy as np  # noqa: E402

from nexabot import viz  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402
from nexabot.plant import derivative  # noqa: E402
from nexabot.controllers import DiscretePID, step_metrics  # noqa: E402

W_REF = 150.0     # rad/s ~= 0,375 m/s
T_END = 1.0       # s
OVERSHOOT_MAX_PCT = 10.0
T_SETTLE_MAX_S = 0.250
ERRO_REGIME_MAX = 2.0


def simular_malha_fechada_pid(pid, r_of_t, t_end, ts, dt_sim=None,
                               tau_load_of_t=None, p=PARAMS, x0=None):
    """Simula a malha fechada planta-contínua + PID-discreto (ZOH em Ts)."""
    if dt_sim is None:
        dt_sim = ts / 10.0
    n_sim = int(round(t_end / dt_sim))
    n_por_ts = max(1, int(round(ts / dt_sim)))
    x = np.zeros(2) if x0 is None else np.array(x0, dtype=float)
    t_hist = np.zeros(n_sim + 1)
    X_hist = np.zeros((n_sim + 1, 2))
    U_hist = np.zeros(n_sim + 1)
    X_hist[0] = x
    u = 0.0
    for k in range(n_sim):
        tk = k * dt_sim
        if k % n_por_ts == 0:
            u = pid.step(r_of_t(tk), x[1])
        tl = tau_load_of_t(tk) if tau_load_of_t else 0.0
        k1 = derivative(x, u, tl, p)
        k2 = derivative(x + 0.5 * dt_sim * k1, u, tl, p)
        k3 = derivative(x + 0.5 * dt_sim * k2, u, tl, p)
        k4 = derivative(x + dt_sim * k3, u, tl, p)
        x = x + (dt_sim / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
        t_hist[k + 1] = tk + dt_sim
        X_hist[k + 1] = x
        U_hist[k + 1] = u
    return t_hist, X_hist, U_hist


def ajustar_pid_manual() -> dict | None:
    """TODO(estudante): escolha Kp, Ki, Kd que satisfaçam REQ-A e REQ-B.

    Veja o enunciado no docstring do módulo para o passo a passo. Devolva
    `None` enquanto não estiver implementado (comportamento atual) ou o
    dicionário {'Kp':..., 'Ki':..., 'Kd':..., 'overshoot_pct':...,
    't_settle_s':...} quando a implementação estiver pronta.
    """
    # TODO: 1. escolha Kp, Ki, Kd (tentativa e erro é válido aqui)
    # TODO: 2. monte pid = DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=PARAMS.Ts)
    # TODO: 3. simule com simular_malha_fechada_pid(pid, lambda t: W_REF, T_END, PARAMS.Ts)
    # TODO: 4. calcule step_metrics(t, w, W_REF) a partir de X_hist[:, 1]
    # TODO: 5. devolva o dicionário com Kp, Ki, Kd, overshoot_pct, t_settle_s
    return None


def main() -> int:
    print(viz.titulo("NexaBot — Aula 6 — DESAFIO: ajuste manual de PID sob dois requisitos"))
    print(__doc__.split("Como rodar")[0].strip())
    print()

    print(f"Executando com w_ref = {W_REF:.0f} rad/s ({PARAMS.omega_to_v(W_REF):.3f} m/s), "
          f"t_end = {T_END:.1f} s...\n")

    resultado = ajustar_pid_manual()

    if resultado is None:
        print(viz.amarelo(viz.negrito(
            "AINDA NÃO IMPLEMENTADO: ajustar_pid_manual() devolveu None.")))
        print("Implemente os 5 passos marcados com TODO na função acima.")
        print("\nCritério de aceitação:")
        viz.tabela(
            ["requisito", "limite", "referência obtida"],
            [
                ["overshoot_pct", f"até {OVERSHOOT_MAX_PCT:.1f} %", "~0.53 %"],
                ["t_settle_s", f"até {T_SETTLE_MAX_S:.3f} s", "~0.076 s"],
                ["abs(erro em regime)", f"até {ERRO_REGIME_MAX:.1f} rad/s", "~0.035 rad/s"],
            ],
        )
        return 0

    linhas = [
        ["Kp", f"{resultado['Kp']:.4f}", "-"],
        ["Ki", f"{resultado['Ki']:.4f}", "-"],
        ["Kd", f"{resultado['Kd']:.5f}", "-"],
        ["overshoot_pct", f"{resultado['overshoot_pct']:.3f}", "%"],
        ["t_settle_s", f"{resultado['t_settle_s']:.4f}", "s"],
    ]
    viz.tabela(["grandeza", "valor", "unidade"], linhas, titulo_tabela="Resultado do estudante")

    dentro_a = resultado["overshoot_pct"] <= OVERSHOOT_MAX_PCT
    dentro_b = resultado["t_settle_s"] <= T_SETTLE_MAX_S

    print()
    print((viz.verde if dentro_a else viz.vermelho)(
        f"REQ-A (overshoot <= {OVERSHOOT_MAX_PCT:.1f}%): "
        f"{'OK' if dentro_a else 'FALHOU'} ({resultado['overshoot_pct']:.2f}%)"))
    print((viz.verde if dentro_b else viz.vermelho)(
        f"REQ-B (t_settle <= {T_SETTLE_MAX_S:.3f} s): "
        f"{'OK' if dentro_b else 'FALHOU'} ({resultado['t_settle_s']:.4f} s)"))

    if dentro_a and dentro_b:
        print(viz.verde(viz.negrito("\nOs dois requisitos foram satisfeitos — desafio resolvido.")))
    else:
        print(viz.vermelho(viz.negrito("\nAo menos um requisito não foi satisfeito — ajuste os ganhos.")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
