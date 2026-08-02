#!/usr/bin/env python3
"""Lista, em ordem de documento, as caixas e os títulos de um DOCX gerado.

Percorre também as tabelas embrulhadas em content controls (`w:sdt`), usadas
pelos modelos das Unidades 3 e 4 — elas não aparecem em `body.iterchildren()`.

Uso:
    PYTHONPATH=/tmp/dse-docx-libs python3 scripts/inspecionar_docx.py <arquivo.docx>
"""

from __future__ import annotations

import sys
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph


def percorrer(documento):
    corpo = documento.element.body
    vistos: set[int] = set()
    for elemento in corpo.iter():
        if elemento.tag == qn("w:tbl"):
            # ignora tabelas aninhadas dentro de outra tabela já listada
            ancestral = elemento.getparent()
            aninhada = False
            while ancestral is not None and ancestral is not corpo:
                if ancestral.tag == qn("w:tbl") and id(ancestral) in vistos:
                    aninhada = True
                    break
                ancestral = ancestral.getparent()
            if aninhada:
                continue
            vistos.add(id(elemento))
            yield "tbl", Table(elemento, documento)
        elif elemento.tag == qn("w:p"):
            ancestral = elemento.getparent()
            dentro_de_tabela = False
            while ancestral is not None and ancestral is not corpo:
                if ancestral.tag == qn("w:tbl"):
                    dentro_de_tabela = True
                    break
                ancestral = ancestral.getparent()
            if dentro_de_tabela:
                continue
            yield "p", Paragraph(elemento, documento)


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    caminho = Path(sys.argv[1])
    documento = Document(caminho)
    print(f"### {caminho.name}")
    for tipo, item in percorrer(documento):
        if tipo == "tbl":
            cabecalho = item.rows[0].cells[0].text.strip().replace("\n", " ")
            palavras = sum(len(linha.cells[0].text.split()) for linha in item.rows[1:])
            print(f"  [CAIXA {len(item.rows)}r {palavras:5d} pal] {cabecalho[:78]}")
        else:
            texto = item.text.strip()
            if texto:
                print(f"  P({item.style.name}) {texto[:88]}")
    for secao in documento.sections:
        cab = " | ".join(p.text.strip() for p in secao.header.paragraphs if p.text.strip())
        if cab:
            print(f"  [CABEÇALHO] {cab[:90]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
