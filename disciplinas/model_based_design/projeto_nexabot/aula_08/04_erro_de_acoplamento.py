#!/usr/bin/env python
"""Aula 8 — Passo 4: como o erro de acoplamento cresce com o passo H.

ESTE E O PONTO PEDAGOGICO CENTRAL DA AULA.

O QUE ESTE SCRIPT DEMONSTRA
----------------------------
Em co-simulacao, planta e controlador so trocam informacao a cada passo de
comunicacao H: durante todo o intervalo [t, t+H), a tensao que o
controlador calculou em t fica congelada (retentor de ordem zero — ZOH) na
entrada da planta, e o controlador so volta a "enxergar" a planta em
t+H. Quanto maior H:

    1. mais desatualizada fica a tensao aplicada em relacao ao que o
       controlador aplicaria se pudesse reagir continuamente;
    2. mais grosseira fica a propria amostragem do controlador digital
       (o `DiscretePID` roda com Ts = H).

Este script varre H em {1, 5, 10, 20, 50} ms para o MESMO cenario (degrau
de 1,0 m/s) e mede, contra uma referencia "quase-continua" (H = 0,5 ms), o
quanto a trajetoria de cada co-simulacao se afasta dela — mostrando
numericamente que o erro de acoplamento CRESCE com H.

COMO RODAR
----------
    .venv/bin/python aula_08/04_erro_de_acoplamento.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from nexabot.cosim import run_cosimulation
from nexabot.controllers import step_metrics
from nexabot.params import PARAMS

T_END = 1.0
V_REF = 1.0
H_REFERENCIA = 0.5e-3          # 0,5 ms — trajetoria de referencia "quase-continua"
VALORES_H = [1e-3, 5e-3, 10e-3, 20e-3, 50e-3]  # ms pedidos pelo enunciado


def linha(char: str = "=", n: int = 78) -> None:
    print(char * n)


def erro_contra_referencia(t_ref, omega_ref, t_h, omega_h):
    """Interpola a trajetoria fina na grade grossa e mede o erro relativo."""
    omega_ref_na_grade = np.interp(t_h, t_ref, omega_ref)
    escala = max(np.max(np.abs(omega_ref_na_grade)), 1e-9)
    erro_abs = np.abs(omega_h - omega_ref_na_grade)
    erro_rms_pct = float(np.sqrt(np.mean(erro_abs**2))) / escala * 100.0
    erro_max_pct = float(np.max(erro_abs)) / escala * 100.0
    return erro_rms_pct, erro_max_pct


def main() -> int:
    linha()
    print("AULA 8 — Passo 4: crescimento do erro de acoplamento com H")
    linha()
    print()
    print(f"Cenario: degrau de {V_REF:.2f} m/s ({PARAMS.v_to_omega(V_REF):.1f} rad/s), "
          f"duracao {T_END:.2f} s")
    print(f"Referencia 'quase-continua': H = {H_REFERENCIA*1000:.2f} ms")
    print()

    print("Rodando referencia quase-continua...")
    ref = run_cosimulation(H=H_REFERENCIA, t_end=T_END, v_ref=V_REF)
    print(f"  OK — {len(ref.t)} passos de comunicacao.")
    print()

    omega_ref_final = PARAMS.v_to_omega(V_REF)

    linhas_tabela = []
    for H in VALORES_H:
        res = run_cosimulation(H=H, t_end=T_END, v_ref=V_REF)
        erro_rms, erro_max = erro_contra_referencia(ref.t, ref.omega, res.t, res.omega)
        metr = step_metrics(res.t, res.omega, r=omega_ref_final)
        # ripple de tensao em regime: desvio pico-a-pico na ultima metade da simulacao
        metade = len(res.tensao) // 2
        ripple_v = float(np.max(res.tensao[metade:]) - np.min(res.tensao[metade:]))
        linhas_tabela.append((H, erro_rms, erro_max, metr["overshoot_pct"],
                               metr["t_settle_s"], ripple_v))
        print(f"H = {H*1000:5.1f} ms  ->  erro_rms = {erro_rms:8.4f} %   "
              f"erro_max = {erro_max:8.4f} %   ({len(res.t)} passos)")

    print()
    linha("-")
    print("== Resumo: erro de acoplamento cresce com H ==")
    linha("-")
    print(f"{'H [ms]':>8} {'erro_rms [%]':>13} {'erro_max [%]':>13} "
          f"{'sobressinal [%]':>16} {'t_acomod [ms]':>14} {'ripple_V [V]':>13}")
    print("-" * 82)
    for H, erro_rms, erro_max, overshoot, t_settle, ripple_v in linhas_tabela:
        print(f"{H*1000:8.1f} {erro_rms:13.4f} {erro_max:13.4f} "
              f"{overshoot:16.4f} {t_settle*1000:14.2f} {ripple_v:13.5f}")

    print()
    erros_rms = [r for _, r, *_ in linhas_tabela]
    crescente = all(a <= b + 1e-9 for a, b in zip(erros_rms, erros_rms[1:]))
    linha()
    if crescente:
        print("RESULTADO: o erro RMS cresce monotonicamente com H, confirmando")
        print("que passos de comunicacao maiores degradam a fidelidade da")
        print("co-simulacao — o controlador reage cada vez mais tarde e com")
        print("uma tensao cada vez mais 'congelada' em relacao a planta real.")
    else:
        print("RESULTADO: o erro nao cresceu estritamente em todos os passos —")
        print("normal em malha fechada (o PID pode compensar parcialmente um H")
        print("moderado); ainda assim, compare o extremo H=1ms com H=50ms acima:")
        print(f"  H=1ms   -> erro_rms={erros_rms[0]:.4f}%")
        print(f"  H=50ms  -> erro_rms={erros_rms[-1]:.4f}%")
    linha()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
