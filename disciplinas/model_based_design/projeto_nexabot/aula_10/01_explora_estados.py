#!/usr/bin/env python3
"""Aula 10 — Script 01: rodando o model checker de estados explícitos.

O que este script faz
----------------------
Executa `nexabot.modelcheck.explorar` sobre o supervisor real do NexaBot,
imprime as estatísticas da busca em largura (estados alcançáveis, transições
exploradas, tempo) e verifica todos os requisitos formais aplicáveis
(invariantes, segurança, vivacidade e alcançabilidade).

Como rodar
----------
    .venv/bin/python aula_10/01_explora_estados.py

Saída esperada (resumo)
------------------------
6 estados alcançáveis, 768 transições exploradas, tempo < 5 ms, 0 violações
de invariante e REQ-SAFE-003 (MOVENDO alcançável) confirmado.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.modelcheck import (  # noqa: E402
    formatar_caminho,
    imprimir_estatisticas,
    verificar_tudo,
)
from nexabot.requisitos import REQUISITOS_ALCANCABILIDADE, REQUISITOS_TRANSICAO  # noqa: E402


def main() -> None:
    print("=" * 78)
    print("AULA 10 — Explorando o espaço de estados do supervisor do NexaBot")
    print("=" * 78)

    relatorio = verificar_tudo()
    resultado = relatorio["resultado"]

    print()
    imprimir_estatisticas(resultado)

    print("\nVerificação dos requisitos de transição:")
    print("+--------------+------------------+----------------------------------+")
    print("| REQUISITO    | TIPO             | RESULTADO                        |")
    print("+--------------+------------------+----------------------------------+")
    violados_por_id = {}
    for v in relatorio["violacoes"]:
        violados_por_id.setdefault(v.requisito.id, []).append(v)
    for req in REQUISITOS_TRANSICAO:
        n_viol = len(violados_por_id.get(req.id, []))
        status = "OK (0 violações)" if n_viol == 0 else f"FALHOU ({n_viol} violações)"
        print(f"| {req.id:<12} | {req.tipo:<16} | {status:<34} |")
    print("+--------------+------------------+----------------------------------+")

    print("\nVerificação de alcançabilidade:")
    print("+--------------+------------------+----------------------------------+")
    print("| REQUISITO    | TIPO             | RESULTADO                        |")
    print("+--------------+------------------+----------------------------------+")
    for req in REQUISITOS_ALCANCABILIDADE:
        alcancavel, caminho = relatorio["alcancabilidade"][req.id]
        status = f"ALCANÇÁVEL em {len(caminho)} passo(s)" if alcancavel else "INALCANÇÁVEL"
        print(f"| {req.id:<12} | {req.tipo:<16} | {status:<34} |")
    print("+--------------+------------------+----------------------------------+")

    req003 = REQUISITOS_ALCANCABILIDADE[0]
    _, caminho = relatorio["alcancabilidade"][req003.id]
    print(f"\nTestemunha de {req003.id} (caminho até MOVENDO):")
    print(formatar_caminho(caminho))

    total_violacoes = len(relatorio["violacoes"])
    print(f"\nRESUMO FINAL: {total_violacoes} violações em {resultado.n_transicoes} transições exploradas.")


if __name__ == "__main__":
    main()
