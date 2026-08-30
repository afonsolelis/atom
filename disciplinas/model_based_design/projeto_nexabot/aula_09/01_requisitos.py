#!/usr/bin/env python3
"""Aula 09 — Script 01: os requisitos formais do NexaBot, um por um.

O que este script faz
----------------------
Lista os sete requisitos de segurança rastreados para o NexaBot
(`nexabot/requisitos.py`), classificados por tipo (invariante, segurança,
alcançabilidade, vivacidade, temporizado), e imprime uma tabela ASCII.

Como rodar
----------
    .venv/bin/python aula_09/01_requisitos.py

Saída esperada (resumo)
------------------------
Uma tabela com 6 linhas (REQ-SAFE-001 a 006), cada uma com tipo e descrição,
seguida de uma contagem de requisitos por tipo.
"""

from __future__ import annotations

import sys
from collections import Counter
from pathlib import Path
from textwrap import wrap

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.requisitos import REQUISITOS  # noqa: E402


def imprimir_tabela_requisitos() -> None:
    largura_id, largura_tipo, largura_desc = 14, 16, 60
    borda = "+" + "-" * largura_id + "+" + "-" * largura_tipo + "+" + "-" * largura_desc + "+"

    print(borda)
    print(f"|{'ID':^{largura_id}}|{'TIPO':^{largura_tipo}}|{'DESCRIÇÃO':^{largura_desc}}|")
    print(borda)
    for r in REQUISITOS:
        linhas_desc = wrap(r.descricao, largura_desc - 2) or [""]
        print(f"|{r.id:^{largura_id}}|{r.tipo:^{largura_tipo}}|{linhas_desc[0]:<{largura_desc - 2}}  |")
        for extra in linhas_desc[1:]:
            print(f"|{'':^{largura_id}}|{'':^{largura_tipo}}|{extra:<{largura_desc - 2}}  |")
        print(borda)


def imprimir_contagem_por_tipo() -> None:
    contagem = Counter(r.tipo for r in REQUISITOS)
    print()
    print("Requisitos por tipo:")
    for tipo, n in sorted(contagem.items()):
        print(f"  {tipo:<16} {n}")
    print(f"  {'TOTAL':<16} {len(REQUISITOS)}")


def main() -> None:
    print("=" * 78)
    print("AULA 09 — Requisitos formais do supervisor de segurança do NexaBot")
    print("=" * 78)
    imprimir_tabela_requisitos()
    imprimir_contagem_por_tipo()


if __name__ == "__main__":
    main()
