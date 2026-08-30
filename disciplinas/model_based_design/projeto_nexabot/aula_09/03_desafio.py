#!/usr/bin/env python3
"""Aula 09 — Script 03: formalize uma propriedade redundante adicional.

O que este script faz
----------------------
Propõe um requisito adicional, em texto livre, que o supervisor do NexaBot
JÁ satisfaz (mas que ainda não está formalizado em `nexabot/requisitos.py`):

    "O robô nunca aciona o freio E habilita o torque ao mesmo tempo."

O estudante deve completar a função `req_extra_freio_xor_torque` abaixo e
então rodar este script, que verifica a formalização contra todo o espaço
de estados alcançável do supervisor usando o mesmo model checker da Aula 10
(antecipado aqui só para fechar o ciclo "texto -> predicado -> verificação").

Como rodar
----------
    .venv/bin/python aula_09/03_desafio.py

Saída esperada (resumo)
------------------------
Com a implementação de referência (já preenchida abaixo, comentada), o
script imprime "0 violações em N transições" — ou seja, o requisito extra
é, de fato, uma consequência do desenho atual do supervisor.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.modelcheck import explorar, formatar_caminho, reconstruir_caminho  # noqa: E402
from nexabot.supervisor import Entradas, Estado, Saidas  # noqa: E402


def req_extra_freio_xor_torque(estado: Estado, entradas: Entradas, saida: Saidas, proximo: Estado) -> bool:
    """DESAFIO: complete este predicado.

    Requisito em texto livre: "o robô nunca aciona o freio E habilita o
    torque ao mesmo tempo" — isto é, `torque_habilitado` e `freio_acionado`
    nunca podem ser True simultaneamente na mesma saída.

    Dica: isto não depende do estado nem da entrada, só da saída — é o
    predicado mais simples de todo o módulo de requisitos.
    """
    # --- solução de referência (apague e reescreva como exercício) ---
    return not (saida.torque_habilitado and saida.freio_acionado)


def main() -> None:
    print("=" * 78)
    print("AULA 09 — Desafio: formalize e verifique uma propriedade adicional")
    print("=" * 78)
    print("\nRequisito proposto (texto livre):")
    print('  "O robô nunca aciona o freio E habilita o torque ao mesmo tempo."')

    resultado = explorar()
    violacoes = []
    for t in resultado.transicoes:
        if not req_extra_freio_xor_torque(t.origem, t.entrada, t.saida, t.destino):
            violacoes.append(reconstruir_caminho(resultado, t.origem) + [t])

    print(f"\nTransições exploradas: {resultado.n_transicoes}")
    print(f"Violações encontradas: {len(violacoes)}")
    for caminho in violacoes[:3]:
        print(formatar_caminho(caminho))

    if not violacoes:
        print("\nO requisito extra é uma CONSEQUÊNCIA do desenho atual do supervisor.")
        print("Pergunta para discussão: vale registrar formalmente essa propriedade")
        print("redundante, sem confundi-la com o identificador já reservado ao limite")
        print("contínuo de velocidade? Defesa em profundidade também é uma decisão")
        print("de projeto, mas identificadores de requisitos não podem ser ambíguos.")


if __name__ == "__main__":
    main()
