#!/usr/bin/env python3
"""Aula 15 — Script 4/4: desafio — escolha um Ts_max seguro contra o jitter medido.

O que este script faz
----------------------
A Aula 15 mediu jitter e latência do laço HIL. Este desafio inverte a
pergunta: DADO o jitter medido neste ambiente, qual é o menor Ts (maior
frequência de amostragem) que ainda pode ser considerado seguro?

Critério proposto (comum em projetos de controle digital): o jitter de pior
caso (`atraso_maximo_ms`, ou uma margem de segurança sobre o desvio padrão)
não deve consumir mais que uma fração `margem` do período de amostragem —
senão o controlador roda, no pior caso, com uma cadência efetivamente
diferente da assumida no projeto (Ts usado para discretizar os ganhos).

DESAFIO: complete `ts_minimo_seguro`, que calcula o menor Ts testado (entre
os candidatos fornecidos) cujo jitter de pior caso ainda respeita a margem.

Como rodar
----------
    .venv/bin/python aula_15/04_desafio.py

Saída esperada (resumo)
------------------------
Uma tabela com jitter medido para vários candidatos de Ts e a indicação de
qual é o menor Ts seguro dado o critério.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.hil import LoopbackTarget, run_closed_loop_hil  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402


def linha(char: str = "-", n: int = 90) -> str:
    return char * n


def ts_minimo_seguro(candidatos_ts_s: list[float], jitter_por_ts_ms: dict[float, float],
                      margem: float = 0.2) -> float | None:
    """DESAFIO: devolva o menor Ts em `candidatos_ts_s` cujo jitter de pior
    caso (`jitter_por_ts_ms[Ts]`, em ms) seja <= `margem` * Ts (em ms).

    Devolve `None` se nenhum candidato respeitar o critério.
    """
    # --- solução de referência (apague e reescreva como exercício) ---
    seguros = [
        ts for ts in candidatos_ts_s
        if jitter_por_ts_ms[ts] <= margem * (ts * 1e3)
    ]
    return min(seguros) if seguros else None


def main() -> None:
    print(linha("="))
    print("Aula 15 — Desafio: qual o menor Ts seguro, dado o jitter medido?")
    print(linha("="))

    candidatos_ts_ms = [5.0, 2.0, 1.0, 0.5]
    candidatos_ts_s = [ts / 1e3 for ts in candidatos_ts_ms]
    margem = 0.2  # jitter de pior caso não pode passar de 20% de Ts

    ganhos_base = dict(Kp=2.0, Ki=40.0, Kd=0.02, u_max=PARAMS.V_max, tau_f=0.01, Kaw=1.0)

    jitter_por_ts_ms: dict[float, float] = {}
    print(f"\nMargem de segurança: jitter de pior caso <= {margem:.0%} de Ts\n")
    header = f"{'Ts [ms]':>8} | {'n amostras':>10} | {'jitter σ [ms]':>13} | {'atraso máx [ms]':>15} | {'limite (20% Ts) [ms]':>20}"
    print(header)
    print(linha("-", len(header)))

    for ts_s, ts_ms in zip(candidatos_ts_s, candidatos_ts_ms):
        target = LoopbackTarget(Ts=ts_s, **ganhos_base)
        # amostra por 0.5s em cada Ts -- suficiente para caracterizar o jitter
        # sem tornar o desafio lento de rodar ao vivo.
        resultado = run_closed_loop_hil(target, lambda t: 60.0, t_end=0.5, Ts=ts_s, real_time=True)
        target.close()
        stats = resultado.jitter_stats
        jitter_por_ts_ms[ts_s] = stats["atraso_maximo_ms"]
        limite = margem * ts_ms
        print(f"{ts_ms:>8.2f} | {stats['n_amostras']:>10} | {stats['jitter_desvio_padrao_ms']:>13.4f} | "
              f"{stats['atraso_maximo_ms']:>15.4f} | {limite:>20.4f}")

    escolhido = ts_minimo_seguro(candidatos_ts_s, jitter_por_ts_ms, margem=margem)

    print("\n" + linha("="))
    if escolhido is not None:
        print(f"Menor Ts seguro neste ambiente, com esta margem: {escolhido * 1e3:.2f} ms "
              f"({1.0/escolhido:.0f} Hz)")
    else:
        print("Nenhum candidato respeitou o critério -- nem mesmo Ts=5ms (o Ts de projeto).")
        print("Isso seria um sinal real de alerta: reveja o critério de margem ou o ambiente.")
        raise SystemExit(1)

    print("\nLição: a resposta depende do AMBIENTE de execução, não só do algoritmo --")
    print("o mesmo laço, no mesmo hardware, mas competindo por CPU com outros processos,")
    print("pode empurrar o Ts mínimo seguro para cima. Em um firmware bare-metal/RTOS")
    print("dedicado, o jitter cairia ordens de grandeza e Ts poderia ser bem menor.")


if __name__ == "__main__":
    main()
