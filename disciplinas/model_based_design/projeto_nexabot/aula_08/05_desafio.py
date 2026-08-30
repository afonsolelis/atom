#!/usr/bin/env python
"""Aula 8 — Passo 5: DESAFIO — acoplar um disturbio de torque de carga em rampa.

O QUE ESTE SCRIPT JA FAZ (baseline, funcional)
------------------------------------------------
Roda a co-simulacao FMU+PID de `nexabot.cosim.run_cosimulation` com
`tau_load_of_t` fixo em zero, exatamente como no `03_cosim_basica.py`, para
servir de comparacao "sem disturbio".

O QUE VOCE (estudante) DEVE FAZER
------------------------------------
Implementar `tau_load_rampa(t)` abaixo: um torque de carga [N.m] que sobe
em rampa a partir de um instante `T_INICIO_RAMPA`, simulando o NexaBot
subindo uma rampa fisica de carga (por exemplo, o AGV entrando em uma
inclinacao do piso da fabrica). Depois, comparar a resposta COM disturbio
contra a resposta SEM disturbio (ja pronta) e responder as perguntas ao
final do script.

DICAS
-----
- `tau_load` positivo freia o eixo do motor (ver a docstring de
  `nexabot.plant.derivative`).
- Um torque razoavel para este motor esta na faixa de 0 a ~0.05 N.m
  (compare com o torque nominal Kt*i_max = 0.045*12 = 0.54 N.m — fique bem
  abaixo disso para nao saturar o motor).
- Rodar o MESMO cenario com H pequeno (1 ms) e H grande (50 ms) e comparar
  o quanto o controlador consegue (ou nao) rejeitar o disturbio em cada
  caso e uma extensao natural deste desafio — ligando de volta ao
  `04_erro_de_acoplamento.py`.

COMO RODAR (apos completar o TODO)
------------------------------------
    .venv/bin/python aula_08/05_desafio.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from nexabot.cosim import run_cosimulation
from nexabot.params import PARAMS

H = PARAMS.Ts   # 5 ms
T_END = 1.0     # s
V_REF = 1.0     # m/s

T_INICIO_RAMPA = 0.5    # s — instante em que a rampa fisica comeca
INCLINACAO_RAMPA = 0.08  # N.m/s — taxa de crescimento do torque de carga (AJUSTE LIVRE)
TAU_MAX = 0.04           # N.m — torque de carga maximo (satura a rampa aqui)


def tau_load_zero(t: float) -> float:
    """Baseline sem disturbio: torque de carga sempre nulo."""
    return 0.0


def tau_load_rampa(t: float) -> float:
    """TODO (estudante): torque de carga em rampa a partir de T_INICIO_RAMPA.

    Deve devolver:
      - 0.0                                           para t <  T_INICIO_RAMPA
      - INCLINACAO_RAMPA * (t - T_INICIO_RAMPA)        para T_INICIO_RAMPA <= t
        (saturado em TAU_MAX)

    Substitua a linha abaixo pela sua implementacao.
    """
    raise NotImplementedError(
        "TODO: implemente a rampa de torque de carga (ver docstring acima)."
    )


def linha(char: str = "=", n: int = 78) -> None:
    print(char * n)


def main() -> int:
    linha()
    print("AULA 8 — Passo 5 (DESAFIO): disturbio de torque de carga em rampa")
    linha()
    print()
    print(f"Passo de comunicacao H : {H*1000:.1f} ms")
    print(f"Referencia de velocidade: {V_REF:.2f} m/s")
    print(f"Rampa de torque a partir de t = {T_INICIO_RAMPA:.2f} s, "
          f"inclinacao {INCLINACAO_RAMPA:.3f} N.m/s, limite {TAU_MAX:.3f} N.m")
    print()

    print("Rodando baseline (sem disturbio)...")
    baseline = run_cosimulation(H=H, t_end=T_END, v_ref=V_REF, tau_load_of_t=tau_load_zero)
    print("  OK.")
    print()

    print("Rodando cenario com disturbio (requer TODO implementado)...")
    try:
        com_disturbio = run_cosimulation(
            H=H, t_end=T_END, v_ref=V_REF, tau_load_of_t=tau_load_rampa,
        )
    except NotImplementedError as exc:
        print()
        print(f"  AINDA NAO IMPLEMENTADO: {exc}")
        print()
        linha()
        print("Complete `tau_load_rampa()` neste arquivo e rode novamente.")
        linha()
        return 1

    print("  OK.")
    print()

    v_base = PARAMS.omega_to_v(baseline.omega)
    v_dist = PARAMS.omega_to_v(com_disturbio.omega)

    print(f"{'t [s]':>8} {'v_base [m/s]':>13} {'v_disturbio [m/s]':>18} "
          f"{'tau_load [N.m]':>15} {'u_disturbio [V]':>16}")
    print("-" * 76)
    n = len(baseline.t)
    passo_exibicao = max(1, n // 20)
    for k in range(0, n, passo_exibicao):
        tk = baseline.t[k]
        print(f"{tk:8.3f} {v_base[k]:13.4f} {v_dist[k]:18.4f} "
              f"{tau_load_rampa(tk):15.4f} {com_disturbio.tensao[k]:16.4f}")

    erro_final_base = abs(V_REF - v_base[-1])
    erro_final_dist = abs(V_REF - v_dist[-1])

    print("-" * 76)
    print()
    print("== Comparacao final ==")
    print(f"  erro em regime SEM disturbio: {erro_final_base:.6f} m/s")
    print(f"  erro em regime COM disturbio: {erro_final_dist:.6f} m/s")
    print()

    linha()
    print("PERGUNTAS PARA REFLEXAO (responda no seu relatorio da Aula 8):")
    print("  1. O PID rejeita o disturbio de torque em regime permanente?")
    print("     (compare os dois erros em regime acima — deveriam ser proximos")
    print("     se o ganho integral Ki eliminar o erro de carga.)")
    print("  2. Repita esta comparacao com H = 1 ms e H = 50 ms (edite a")
    print("     constante H no topo do arquivo). O que muda na velocidade de")
    print("     rejeicao do disturbio quando H cresce?")
    print("  3. Existe um H a partir do qual a rejeicao ao disturbio piora")
    print("     visivelmente? Relacione com o `04_erro_de_acoplamento.py`.")
    linha()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
