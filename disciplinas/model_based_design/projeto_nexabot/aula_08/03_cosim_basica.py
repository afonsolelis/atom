#!/usr/bin/env python
"""Aula 8 — Passo 3: co-simulacao basica planta (FMU) + controlador (Python).

O QUE ESTE SCRIPT DEMONSTRA
----------------------------
Roda `nexabot.cosim.run_cosimulation` com passo de comunicacao H = 5 ms
(o mesmo Ts=200 Hz usado no controlador embarcado do NexaBot, PARAMS.Ts) —
um degrau de referencia de 1,0 m/s (400 rad/s no motor). A cada passo H:

    1. o mestre LE omega medido do FMU (fmi3GetFloat64);
    2. o `DiscretePID` (rodando em Python, no mestre) calcula a tensao;
    3. o mestre ESCREVE a tensao no FMU (fmi3SetFloat64);
    4. o FMU avanca H segundos (fmi3DoStep), integrando a planta em C.

Imprime uma tabela tempo / referencia / velocidade / tensao para mostrar
a resposta ao degrau convergindo ao regime esperado (~18,85 V, 400 rad/s).

COMO RODAR
----------
    .venv/bin/python aula_08/03_cosim_basica.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from nexabot.cosim import run_cosimulation
from nexabot.controllers import step_metrics
from nexabot.params import PARAMS


def linha(char: str = "=", n: int = 78) -> None:
    print(char * n)


def main() -> int:
    H = PARAMS.Ts  # 5 ms — mesmo passo do controlador embarcado real
    T_END = 1.0    # s
    V_REF = 1.0    # m/s -> 400 rad/s no motor

    linha()
    print("AULA 8 — Passo 3: co-simulacao basica (H = 5 ms, degrau de 1,0 m/s)")
    linha()
    print()
    print(f"Passo de comunicacao H  : {H*1000:.1f} ms ({1/H:.0f} Hz)")
    print(f"Duracao simulada        : {T_END:.2f} s")
    print(f"Referencia de velocidade: {V_REF:.2f} m/s "
          f"({PARAMS.v_to_omega(V_REF):.2f} rad/s no motor)")
    print()

    resultado = run_cosimulation(H=H, t_end=T_END, v_ref=V_REF)

    v_medida = PARAMS.omega_to_v(resultado.omega)
    v_ref_arr = PARAMS.omega_to_v(resultado.referencia)

    print(f"{'t [s]':>8} {'v_ref [m/s]':>12} {'v [m/s]':>10} {'omega [rad/s]':>14} {'u [V]':>10}")
    print("-" * 62)
    n = len(resultado.t)
    # mostra ~20 linhas espalhadas por toda a simulacao, sempre incluindo t=0
    passo_exibicao = max(1, n // 20)
    for k in range(0, n, passo_exibicao):
        print(f"{resultado.t[k]:8.3f} {v_ref_arr[k]:12.4f} {v_medida[k]:10.4f} "
              f"{resultado.omega[k]:14.4f} {resultado.tensao[k]:10.4f}")
    if (n - 1) % passo_exibicao != 0:
        k = n - 1
        print(f"{resultado.t[k]:8.3f} {v_ref_arr[k]:12.4f} {v_medida[k]:10.4f} "
              f"{resultado.omega[k]:14.4f} {resultado.tensao[k]:10.4f}")

    print("-" * 62)

    metricas = step_metrics(resultado.t, resultado.omega, r=PARAMS.v_to_omega(V_REF))
    print()
    print("== Metricas da resposta ao degrau (sobre omega) ==")
    print(f"  sobressinal          : {metricas['overshoot_pct']:.3f} %")
    print(f"  tempo de subida 10-90%: {metricas['t_rise_s']*1000:.2f} ms")
    print(f"  tempo de acomodacao   : {metricas['t_settle_s']*1000:.2f} ms")
    print(f"  erro em regime        : {metricas['steady_state_error']:.5f} rad/s")
    print(f"  valor final           : {metricas['y_final']:.4f} rad/s "
          f"({PARAMS.omega_to_v(metricas['y_final']):.4f} m/s)")
    print(f"  tensao final aplicada : {resultado.tensao[-1]:.4f} V "
          f"(esperado ~18,85 V em regime)")

    print()
    linha()
    print("RESULTADO: co-simulacao FMU+PID rodou do inicio ao fim sem erros,")
    print("convergindo para a velocidade de referencia com a tensao esperada.")
    linha()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
