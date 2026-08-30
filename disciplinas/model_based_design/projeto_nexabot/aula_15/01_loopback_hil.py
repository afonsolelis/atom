#!/usr/bin/env python3
"""Aula 15 — Script 1/4: HIL de verdade, com o alvo rodando em subprocesso.

O que este script faz
----------------------
Fecha a malha de controle do NexaBot com a planta em Python (RK4 de passo
fixo, `nexabot.plant`) e o CONTROLADOR RODANDO FORA DO PROCESSO HOST: um
executável C (`nexabot/firmware/main_loopback.c`), compilado com o mesmo
PID gerado na Aula 13, recebendo `(r, y)` e devolvendo `u` por um protocolo
de linha em stdin/stdout — `nexabot.hil.LoopbackTarget`.

Isto RODA de verdade neste ambiente sem hardware conectado: é o back-end
usado para a gravação da Aula 15. `nexabot.hil.SerialTarget` fala o mesmo
protocolo sobre uma UART real (ESP32/Arduino) e é usado sem alterar
`run_closed_loop_hil` — só trocando o objeto `target`.

Como rodar
----------
    .venv/bin/python aula_15/01_loopback_hil.py

Saída esperada (resumo)
------------------------
Uma tabela com a trajetória de referência/saída/comando amostrada, mais um
resumo de erro de regime permanente — a resposta ao degrau do NexaBot
controlado por um processo separado, exatamente como seria com um alvo
embarcado real.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np  # noqa: E402

from nexabot.hil import LoopbackTarget, run_closed_loop_hil  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def main() -> None:
    print(linha("="))
    print("Aula 15 — HIL: planta em Python + PID rodando em processo separado (C)")
    print(linha("="))

    ganhos = dict(Kp=2.0, Ki=40.0, Kd=0.02, Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=0.01, Kaw=1.0)
    print(f"\nGanhos do alvo: {ganhos}")

    target = LoopbackTarget(**ganhos)
    print(f"Alvo compilado e rodando como subprocesso: {target.exe_path}")

    referencia_rad_s = 100.0  # degrau de velocidade angular do motor [rad/s]

    def r_of_t(t: float) -> float:
        return referencia_rad_s if t >= 0.0 else 0.0

    t_end = 1.0  # 200 amostras a Ts=5ms
    print(f"\nRodando malha fechada por {t_end}s (Ts={ganhos['Ts']*1e3:.1f} ms, "
          f"{int(round(t_end/ganhos['Ts']))} amostras), referência em degrau de "
          f"{referencia_rad_s} rad/s...")

    resultado = run_closed_loop_hil(target, r_of_t, t_end=t_end, Ts=ganhos["Ts"], real_time=True)
    target.close()

    print("\n" + linha("-"))
    header = f"{'t [s]':>8} | {'r [rad/s]':>10} | {'y [rad/s]':>10} | {'u [V]':>8}"
    print(header)
    print(linha("-", len(header)))
    indices = np.linspace(0, len(resultado.t) - 1, 12, dtype=int)
    for k in indices:
        print(f"{resultado.t[k]:>8.3f} | {resultado.r[k]:>10.3f} | {resultado.y[k]:>10.3f} | {resultado.u[k]:>8.3f}")

    y_final = float(np.mean(resultado.y[-10:]))
    erro_regime = referencia_rad_s - y_final
    print("\n" + linha("-"))
    print(f"Velocidade final (média das últimas 10 amostras): {y_final:.3f} rad/s")
    print(f"Erro de regime permanente: {erro_regime:.3f} rad/s "
          f"({100 * erro_regime / referencia_rad_s:.2f}% da referência)")

    print("\n" + linha("=" ))
    print("Estatísticas de tempo real (jitter/latência) -- ver aula_15/02_jitter.py")
    print(linha("-"))
    for chave, valor in resultado.jitter_stats.items():
        print(f"  {chave:<24}: {valor:.4f}" if isinstance(valor, float) else f"  {chave:<24}: {valor}")


if __name__ == "__main__":
    main()
