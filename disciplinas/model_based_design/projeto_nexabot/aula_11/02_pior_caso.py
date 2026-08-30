#!/usr/bin/env python3
"""Aula 11 — Script 02: varrendo o atraso de detecção até violar o prazo de 150 ms.

O que este script faz
----------------------
Varre o parâmetro `atraso_deteccao_max` (pior atraso admitido do sensor de
obstáculo, em períodos de Ts=5 ms) de 0 até um valor bem acima do limite do
requisito, chamando `nexabot.timed.verificar_req_safe_006` para cada valor.
Mostra a tabela completa e aponta exatamente o valor de atraso em que o
REQ-SAFE-006 deixa de valer — a fronteira entre um projeto de sensor seguro
e um inseguro.

Como rodar
----------
    .venv/bin/python aula_11/02_pior_caso.py

Saída esperada (resumo)
------------------------
Tabela com atraso de 0 a 32 períodos; REQ-SAFE-006 vale até atraso=27
períodos (pior caso = 30 períodos = 150,0 ms, exatamente no limite) e passa
a violar a partir de atraso=28 (pior caso = 31 períodos = 155,0 ms).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.params import PARAMS  # noqa: E402
from nexabot.timed import LIMITE_PERIODOS, verificar_req_safe_006  # noqa: E402


def main() -> None:
    print("=" * 78)
    print("AULA 11 — Varredura do atraso de detecção: onde o prazo é violado?")
    print("=" * 78)
    print(f"\nLimite do REQ-SAFE-006: {LIMITE_PERIODOS} períodos (150 ms).\n")

    print("+-------------------------+------------------+---------------+--------+")
    print("| ATRASO DETECÇÃO (perís) | PIOR CASO (perís)| PIOR CASO (ms)| REQ OK |")
    print("+-------------------------+------------------+---------------+--------+")

    atraso_de_violacao = None
    for atraso in range(0, 33):
        resultado = verificar_req_safe_006(atraso_deteccao_max=atraso, permite_ciclo_perdido=True)
        marca = "SIM" if resultado.ok else "NÃO"
        destaque = " <-- primeira violação" if (not resultado.ok and atraso_de_violacao is None) else ""
        if not resultado.ok and atraso_de_violacao is None:
            atraso_de_violacao = atraso
        print(
            f"| {atraso:>23} | {resultado.pior_caso_periodos:>17} "
            f"| {resultado.pior_caso_ms:>13.1f} | {marca:<6} |{destaque}"
        )
    print("+-------------------------+------------------+---------------+--------+")

    atraso_ms = atraso_de_violacao * PARAMS.Ts * 1000.0
    print(f"\nFronteira de violação: atraso_deteccao_max = {atraso_de_violacao} períodos "
          f"({atraso_ms:.0f} ms) é o primeiro valor em que o prazo de 150 ms é ultrapassado.")
    print(
        "\nConclusão de engenharia: o filtro/debounce do sensor de obstáculo do"
        "\nNexaBot precisa garantir um atraso de detecção estritamente menor que"
        f"\n{atraso_de_violacao} períodos ({atraso_ms:.0f} ms) para manter a margem de"
        "\nsegurança do REQ-SAFE-006, considerando também 1 ciclo de atuação"
        "\nperdido no pior caso."
    )


if __name__ == "__main__":
    main()
