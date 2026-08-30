#!/usr/bin/env python3
"""Aula 10 — Script 04: desafio — injete o SEU próprio bug e ache o contraexemplo.

O que este script faz
----------------------
Convida o estudante a modificar `transition_com_bug_do_estudante` (uma cópia
da transição correta, com um comentário marcando onde mexer) e rodar o
model checker contra ela. Duas sugestões de bug prontas para descomentar,
mais um espaço para o estudante inventar o próprio.

Como rodar
----------
    .venv/bin/python aula_10/04_desafio.py

Saída esperada (resumo)
------------------------
Com a implementação padrão (sem bug ativado), 0 violações — o script avisa
que nada foi injetado ainda. Ao descomentar uma das sugestões, o script
deve encontrar e imprimir um contraexemplo.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.modelcheck import explorar, formatar_caminho, verificar_invariantes  # noqa: E402
from nexabot.requisitos import REQUISITOS_TRANSICAO  # noqa: E402
from nexabot.supervisor import Entradas, Estado, Saidas  # noqa: E402


def transition_com_bug_do_estudante(estado: Estado, entradas: Entradas) -> tuple[Estado, Saidas]:
    """Copie a lógica de `nexabot.supervisor.transition` aqui e quebre-a de propósito.

    Sugestões de bug (descomente UMA por vez):

      (a) Trocar a prioridade de emergência e falha de encoder — fazer
          `entradas.falha_encoder` ser checado ANTES do bloco absorvente de
          FALHA, quebrando REQ-SAFE-004.

      (b) Em PARADO_OBSTACULO, esquecer de checar `entradas.emergencia` e
          `entradas.falha_encoder` antes de voltar a MOVENDO, quebrando o
          REQ-SAFE-005 já refinado na Aula 9.

      (c) Uma ideia sua.
    """
    from nexabot.supervisor import transition as _correta

    estado_novo, saida = _correta(estado, entradas)

    # --- ESPAÇO DO DESAFIO: descomente uma linha para injetar um bug -----
    # (a) trocar torque_habilitado por True sempre que emergencia estiver ligada
    #     e o estado de origem for MOVENDO (quebra REQ-SAFE-002):
    # if estado is Estado.MOVENDO and entradas.emergencia:
    #     saida = Saidas(torque_habilitado=True, freio_acionado=saida.freio_acionado)

    # (b) "esquecer" de tirar o robô de PARADO_OBSTACULO mesmo com tudo liberado:
    # if estado is Estado.PARADO_OBSTACULO and estado_novo is Estado.MOVENDO:
    #     estado_novo = Estado.PARADO_OBSTACULO

    return estado_novo, saida


def main() -> None:
    print("=" * 78)
    print("AULA 10 — Desafio: injete seu próprio bug")
    print("=" * 78)

    resultado = explorar(transition_fn=transition_com_bug_do_estudante)
    violacoes = verificar_invariantes(resultado, REQUISITOS_TRANSICAO)

    print(f"\nTransições exploradas: {resultado.n_transicoes}")
    print(f"Violações encontradas: {len(violacoes)}")

    if not violacoes:
        print(
            "\nNenhum bug ativo ainda — abra este arquivo e descomente uma das"
            "\nsugestões (a) ou (b) dentro de `transition_com_bug_do_estudante`,"
            "\nou escreva a sua própria, e rode de novo."
        )
    else:
        for v in violacoes[:5]:
            print(f"\n[{v.requisito.id}] {v.requisito.descricao}")
            print(formatar_caminho(v.caminho))


if __name__ == "__main__":
    main()
