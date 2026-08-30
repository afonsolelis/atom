#!/usr/bin/env python3
"""Aula 12 — Script 01: gerando a suíte de testes A PARTIR do modelo.

O que este script faz
----------------------
Usa `nexabot.mbt` para gerar duas suítes de teste diretamente do grafo de
estados do supervisor — nenhum caso é escrito manualmente:

  (a) cobertura de ESTADOS: um caso por estado alcançável;
  (b) cobertura de TRANSIÇÕES: um caso por par (origem, destino) distinto.

Imprime cada caso gerado (sequência de entradas e estados esperados) numa
tabela ASCII.

Como rodar
----------
    .venv/bin/python aula_12/01_gera_testes.py

Saída esperada (resumo)
------------------------
6 casos de cobertura de estados + 25 casos de cobertura de transições, todos
executados com sucesso contra o supervisor real.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.mbt import gerar_casos_cobertura_estados, gerar_casos_cobertura_transicoes  # noqa: E402
from nexabot.modelcheck import formatar_entrada  # noqa: E402


def imprimir_suite(titulo: str, casos) -> None:
    print(f"\n{titulo} ({len(casos)} casos)")
    print("-" * 78)
    for caso in casos:
        print(f"  [{caso.id}]")
        print(f"    {caso.descricao}")
        estados_txt = " -> ".join(e.name for e in caso.estados_esperados)
        print(f"    estados esperados: {estados_txt}")
        if caso.entradas_sequencia:
            entradas_txt = ", ".join(formatar_entrada(e) for e in caso.entradas_sequencia)
            print(f"    entradas aplicadas: {entradas_txt}")
        caso.rodar()
        print("    status: PASSOU")


def main() -> None:
    print("=" * 78)
    print("AULA 12 — Geração de testes a partir do modelo (MBT)")
    print("=" * 78)

    casos_estado = gerar_casos_cobertura_estados()
    casos_transicao = gerar_casos_cobertura_transicoes()

    imprimir_suite("SUÍTE 1 — Cobertura de estados", casos_estado)
    imprimir_suite("SUÍTE 2 — Cobertura de transições", casos_transicao)

    total = len(casos_estado) + len(casos_transicao)
    print("\n" + "=" * 78)
    print(f"RESUMO: {len(casos_estado)} casos (estados) + {len(casos_transicao)} casos (transições) "
          f"= {total} casos, todos gerados do modelo e executados com sucesso.")


if __name__ == "__main__":
    main()
