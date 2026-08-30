#!/usr/bin/env python3
"""Aula 11 — Script 03: desafio — e se DOIS ciclos puderem ser perdidos?

O que este script faz
----------------------
O autômato temporizado de `nexabot.timed` foi construído para permitir no
máximo 1 ciclo de atuação perdido (`permite_ciclo_perdido`). Este desafio
pede para o estudante generalizar `explorar_caminhos`/`_sucessores` (ou
escrever uma versão própria aqui, sem tocar em `nexabot/timed.py`) para
permitir até `max_ciclos_perdidos` perdidos em sequência, e então responder:
com o atraso de detecção nominal do projeto (2 períodos), quantos ciclos
perdidos consecutivos o REQ-SAFE-006 ainda tolera?

Como rodar
----------
    .venv/bin/python aula_11/03_desafio.py

Saída esperada (resumo)
------------------------
Uma tabela mostrando, para 0 a 6 ciclos perdidos permitidos (com atraso de
detecção fixo em 2 períodos), o pior caso em ms e se o requisito ainda vale
— revelando quantos ciclos perdidos o projeto atual tolera antes de violar
os 150 ms.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.params import PARAMS  # noqa: E402
from nexabot.timed import EstadoTemporizado, LIMITE_PERIODOS, NoTemporizado  # noqa: E402


def _sucessores_generalizado(no: NoTemporizado, atraso_deteccao_max: int, max_ciclos_perdidos: int, ciclos_ja_perdidos: int):
    """Versão generalizada de `nexabot.timed._sucessores` com N ciclos perdidos.

    DESAFIO: esta função já está pronta — o exercício é ENTENDER a mudança
    em relação à original (que só tinha um booleano `ciclo_perdido_usado`,
    aqui virou um contador `ciclos_ja_perdidos` comparado a
    `max_ciclos_perdidos`) e depois usá-la para responder a pergunta do
    script.
    """
    if no.estado is EstadoTemporizado.DETECTANDO:
        sucessores = [(EstadoTemporizado.COMANDANDO, no.clock + 1, ciclos_ja_perdidos)]
        if no.clock < atraso_deteccao_max:
            sucessores.append((EstadoTemporizado.DETECTANDO, no.clock + 1, ciclos_ja_perdidos))
        return sucessores

    if no.estado is EstadoTemporizado.COMANDANDO:
        sucessores = [(EstadoTemporizado.ZERADO, no.clock + 1, ciclos_ja_perdidos)]
        if ciclos_ja_perdidos < max_ciclos_perdidos:
            sucessores.append((EstadoTemporizado.COMANDANDO, no.clock + 1, ciclos_ja_perdidos + 1))
        return sucessores

    return []


def pior_caso_com_n_ciclos_perdidos(atraso_deteccao_max: int, max_ciclos_perdidos: int) -> int:
    """Busca exaustiva (DFS) do pior caso em períodos, com até N ciclos perdidos."""
    pilha = [(NoTemporizado(EstadoTemporizado.DETECTANDO, 0, False), 0)]
    pior = 0
    while pilha:
        no, ciclos_perdidos = pilha.pop()
        if no.estado is EstadoTemporizado.ZERADO:
            pior = max(pior, no.clock)
            continue
        for estado, clock, cp in _sucessores_generalizado(no, atraso_deteccao_max, max_ciclos_perdidos, ciclos_perdidos):
            pilha.append((NoTemporizado(estado, clock, False), cp))
    return pior


def main() -> None:
    print("=" * 78)
    print("AULA 11 — Desafio: quantos ciclos de atuação perdidos o prazo tolera?")
    print("=" * 78)

    atraso_nominal = 2
    print(f"\nAtraso de detecção fixo em {atraso_nominal} períodos (cenário nominal de projeto).")
    print(f"Limite do requisito: {LIMITE_PERIODOS} períodos = {PARAMS.d_stop_max * 1000:.0f} ms.\n")

    print("+---------------------------+------------------+----------------+--------+")
    print("| CICLOS PERDIDOS PERMITIDOS| PIOR CASO (perís)| PIOR CASO (ms) | REQ OK |")
    print("+---------------------------+------------------+----------------+--------+")
    primeiro_que_viola = None
    for n in range(0, 7):
        pior_periodos = pior_caso_com_n_ciclos_perdidos(atraso_nominal, n)
        pior_ms = pior_periodos * PARAMS.Ts * 1000.0
        ok = pior_periodos <= LIMITE_PERIODOS
        if not ok and primeiro_que_viola is None:
            primeiro_que_viola = n
        marca = "SIM" if ok else "NÃO"
        print(f"| {n:>26} | {pior_periodos:>17} | {pior_ms:>14.1f} | {marca:<6} |")
    print("+---------------------------+------------------+----------------+--------+")

    if primeiro_que_viola is not None:
        print(f"\nCom atraso de detecção de {atraso_nominal} períodos, o REQ-SAFE-006 tolera até "
              f"{primeiro_que_viola - 1} ciclo(s) de atuação perdido(s) consecutivos.")
    else:
        print("\nO REQ-SAFE-006 tolera todos os cenários testados (até 6 ciclos perdidos).")


if __name__ == "__main__":
    main()
