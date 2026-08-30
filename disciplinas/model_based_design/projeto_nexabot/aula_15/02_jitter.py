#!/usr/bin/env python3
"""Aula 15 — Script 2/4: mede e tabula jitter e latência do laço HIL.

O que este script faz
----------------------
Roda `run_closed_loop_hil` três vezes, com durações crescentes, sobre o
mesmo `LoopbackTarget`, e tabula as duas métricas que decidem se um laço de
controle discreto é confiável em um alvo real:

- **Latência**: tempo de ida-e-volta de cada `target.step()` (escrever no
  pipe, o alvo processar, ler a resposta) -- o "quanto demora para saber
  quanto tempo sobrou" dentro do período de amostragem Ts.
- **Jitter**: variação do PERÍODO real do laço host em torno de Ts nominal
  -- o "quão irregular" é o relógio do laço, o que interessa mais para a
  malha fechada do que a latência isolada (um atraso constante pode ser
  compensado no projeto do controlador; um atraso IRREGULAR, não).

Como rodar
----------
    .venv/bin/python aula_15/02_jitter.py

Saída esperada (resumo)
------------------------
Uma tabela ASCII com latência/jitter para diferentes durações de execução,
e uma checagem de que o jitter medido é pequeno frente a Ts (o laço em
Python + subprocesso local consegue, de fato, respeitar 5 ms com boa
regularidade neste ambiente).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.hil import LoopbackTarget, run_closed_loop_hil  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402


def linha(char: str = "-", n: int = 100) -> str:
    return char * n


def main() -> None:
    print(linha("="))
    print("Aula 15 — Jitter e latência do laço HIL (LoopbackTarget)")
    print(linha("="))

    ganhos = dict(Kp=2.0, Ki=40.0, Kd=0.02, Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=0.01, Kaw=1.0)
    duracoes_s = [0.5, 1.0, 2.0]

    linhas_tabela = []
    for t_end in duracoes_s:
        target = LoopbackTarget(**ganhos)
        resultado = run_closed_loop_hil(target, lambda t: 80.0, t_end=t_end, Ts=ganhos["Ts"], real_time=True)
        target.close()
        stats = resultado.jitter_stats
        linhas_tabela.append((t_end, stats))

    header = (f"{'duração [s]':>11} | {'n':>5} | {'Ts nom. [ms]':>12} | {'período méd. [ms]':>17} | "
              f"{'jitter σ [ms]':>13} | {'jitter p-p [ms]':>15} | {'latência méd. [ms]':>18} | "
              f"{'latência p95 [ms]':>17} | {'latência máx [ms]':>17}")
    print("\n" + header)
    print(linha("-", len(header)))
    for t_end, stats in linhas_tabela:
        print(f"{t_end:>11.1f} | {stats['n_amostras']:>5} | {stats['Ts_nominal_ms']:>12.3f} | "
              f"{stats['periodo_medio_ms']:>17.4f} | {stats['jitter_desvio_padrao_ms']:>13.4f} | "
              f"{stats['jitter_pico_a_pico_ms']:>15.4f} | {stats['latencia_media_ms']:>18.4f} | "
              f"{stats['latencia_p95_ms']:>17.4f} | {stats['latencia_maxima_ms']:>17.4f}")

    print("\n" + linha("="))
    print("Critério de aceitação adotado nesta aula:")
    ts_ms = ganhos["Ts"] * 1e3
    limite_jitter_pct = 10.0  # jitter (desvio padrão) até 10% de Ts é considerado saudável
    print(f"  jitter (desvio padrão) <= {limite_jitter_pct:.0f}% de Ts = {ts_ms * limite_jitter_pct / 100:.4f} ms")

    todas_ok = True
    for t_end, stats in linhas_tabela:
        limite_ms = ts_ms * limite_jitter_pct / 100
        ok = stats["jitter_desvio_padrao_ms"] <= limite_ms
        todas_ok = todas_ok and ok
        print(f"  duração {t_end:>4.1f}s: jitter {stats['jitter_desvio_padrao_ms']:.4f} ms "
              f"{'<=' if ok else '>'} {limite_ms:.4f} ms -> {'OK' if ok else 'FORA DO CRITÉRIO'}")

    print("\nInterpretação: este é o jitter de um laço de controle em PYTHON de usuário")
    print("(sem prioridade de tempo real, sem RTOS) se comunicando com um subprocesso")
    print("local por pipe -- não o jitter de um firmware real em um microcontrolador")
    print("dedicado, que tipicamente é ORDENS DE GRANDEZA menor (microssegundos, não")
    print("dezenas/centenas de microssegundos). Serve para ensinar o CONCEITO e o")
    print("método de medição; não é uma alegação de determinismo de tempo real.")

    if not todas_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
