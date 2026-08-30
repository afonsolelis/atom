#!/usr/bin/env python3
"""Audita os 17 decks HTML da disciplina.

Confere a convenção do repositório (aula0 + aula1..aula16, numeração contínua
entre unidades), a estrutura mínima de cada deck, a autocontenção e a
integridade das referências relativas.

Uso:
    tools/.venv/bin/python tools/validar_slides.py
    tools/.venv/bin/python tools/validar_slides.py --detalhe
"""

from __future__ import annotations

import html
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

FALHAS: list[str] = []
AVISOS: list[str] = []
OKS: list[str] = []

VAZIOS = {"br", "img", "hr", "meta", "link", "input", "source", "use", "path",
          "circle", "rect", "polygon", "line", "ellipse", "stop", "col"}


class Balanco(HTMLParser):
    """Detecta tag aberta e não fechada — um deck malformado quebra no navegador."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pilha: list[str] = []
        self.erros: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag not in VAZIOS:
            self.pilha.append(tag)

    def handle_endtag(self, tag):
        if tag in VAZIOS:
            return
        if tag in self.pilha:
            while self.pilha and self.pilha.pop() != tag:
                pass
        else:
            self.erros.append(f"fechamento sem abertura: </{tag}>")


def texto_visivel(fonte: str) -> str:
    s = re.sub(r"<style.*?</style>", " ", fonte, flags=re.S)
    s = re.sub(r"<script.*?</script>", " ", s, flags=re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", s))


def titulos_dos_roteiros() -> dict[int, str]:
    """Título de cada videoaula, lido dos roteiros — a fonte de verdade."""
    titulos: dict[int, str] = {}
    for u in (1, 2, 3, 4):
        f = RAIZ / f"unidade_{u}" / "roteiros_20min.md"
        if not f.exists():
            continue
        for n, tit in re.findall(r'^## Roteiro da Videoaula (\d+) — [""](.+?)[""]',
                                 f.read_text(encoding="utf-8"), re.M):
            titulos[int(n)] = tit
    return titulos


TITULOS = titulos_dos_roteiros()


def validar_deck(caminho: Path, unidade: int, numero: int) -> None:
    nome = f"unidade_{unidade}/slides/{caminho.name}"
    fonte = caminho.read_text(encoding="utf-8")
    txt = texto_visivel(fonte)

    # --- estrutura
    n_slides = len(re.findall(r'<section class="slide', fonte))
    alvo = (6, 9) if numero == 0 else (14, 20)
    if not alvo[0] <= n_slides <= alvo[1]:
        falha = FALHAS.append
        falha(f"{nome}: {n_slides} slides (alvo {alvo[0]} a {alvo[1]})")
    else:
        OKS.append(f"{nome}: {n_slides} slides")

    if 'class="slide slide-capa' not in fonte and "slide-capa" not in fonte:
        FALHAS.append(f"{nome}: sem slide de capa")
    if "audiodescri" not in txt.lower():
        FALHAS.append(f"{nome}: sem slide de audiodescrição (acessibilidade)")
    if "slide-fim" not in fonte:
        FALHAS.append(f"{nome}: sem slide de encerramento")

    if numero > 0:
        for obrig, rotulo in (("sumário", "Sumário"), ("objetivos", "Objetivos de aprendizagem")):
            if obrig not in txt.lower():
                FALHAS.append(f"{nome}: sem slide de {rotulo}")

    # a terceira aula de cada unidade exige pausa para reflexão
    if numero > 0 and (numero - 1) % 4 == 2:
        if "pausa para reflex" not in txt.lower():
            FALHAS.append(f"{nome}: terceira aula da unidade exige 'Pausa para reflexão'")

    # "Sobre o professor" só no primeiro deck da disciplina.
    # A checagem precisa casar a SEÇÃO, não a string: `slide-prof` também
    # aparece como classe na folha de estilo de todos os decks.
    tem_prof = bool(re.search(r'<section class="[^"]*slide-prof', fonte))
    # Convenção verificada nas três disciplinas já migradas do repositório
    # (data_engineering, industria_4_0, portos): o slide "Sobre o professor"
    # aparece em 1 de 17 decks, sempre o aula0.
    if numero != 0 and tem_prof:
        FALHAS.append(f"{nome}: traz 'Sobre o professor', que pela convenção do "
                      "repositório aparece apenas no aula0")
    if numero == 0 and not tem_prof:
        FALHAS.append(f"{nome}: deck de abertura sem o slide 'Sobre o professor'")

    # nenhuma biografia inventada
    if tem_prof and "[preencher" not in txt:
        FALHAS.append(f"{nome}: slide do professor sem marcador '[preencher: …]' — "
                      "verifique se alguma informação biográfica foi presumida")

    # --- o deck fala da SUA aula?
    #
    # Verificação criada depois de um caso real: o deck da Aula 5 era uma cópia
    # do conteúdo da Aula 9 — título, tema e rodapé de outra unidade —, com
    # apenas a tag <title> correta. Nenhuma checagem estrutural pegaria isso.
    if numero > 0:
        titulo = TITULOS.get(numero)
        if titulo and titulo[:28].lower() not in txt.lower():
            FALHAS.append(f"{nome}: não contém o título da própria videoaula "
                          f"({titulo[:40]!r}) — conteúdo pode ser de outra aula")

        rodapes = " ".join(re.findall(r'slide-footer.*?</div>', fonte, re.S))
        u_rod = set(re.findall(r"Unidade (\d)", rodapes))
        a_rod = set(re.findall(r"Aula (\d+)", rodapes))
        if u_rod and u_rod != {str(unidade)}:
            FALHAS.append(f"{nome}: rodapé aponta para Unidade {sorted(u_rod)}, "
                          f"esperado {unidade}")
        if a_rod and a_rod != {str(numero)}:
            FALHAS.append(f"{nome}: rodapé aponta para Aula {sorted(a_rod)}, "
                          f"esperado {numero}")

    # --- autocontenção
    externos = re.findall(r'(?:src|href)="(https?://[^"]+)"', fonte)
    if externos:
        FALHAS.append(f"{nome}: recurso externo: {externos[:2]}")
    if "mathjax" in fonte.lower():
        FALHAS.append(f"{nome}: carrega MathJax — os decks devem ser autocontidos")

    # --- referências relativas resolvem no disco
    for ref in sorted(set(re.findall(r'(?:src|href)="(\.\.[^"]+)"', fonte))):
        if not (caminho.parent / ref).exists():
            FALHAS.append(f"{nome}: referência quebrada -> {ref}")

    # --- HTML bem formado
    b = Balanco()
    b.feed(fonte)
    if b.erros:
        FALHAS.append(f"{nome}: HTML malformado ({b.erros[0]})")
    elif b.pilha:
        FALHAS.append(f"{nome}: tags não fechadas: {b.pilha[-3:]}")

    # --- navegação preservada
    if "getElementById" not in fonte or "keydown" not in fonte:
        FALHAS.append(f"{nome}: JavaScript de navegação ausente ou incompleto")


def main(argv: list[str]) -> int:
    detalhe = "--detalhe" in argv

    esperados = [(1, 0)] + [(u, a) for u in (1, 2, 3, 4)
                            for a in range((u - 1) * 4 + 1, (u - 1) * 4 + 5)]
    for unidade, numero in esperados:
        p = RAIZ / f"unidade_{unidade}" / "slides" / f"aula{numero}.html"
        if not p.exists():
            FALHAS.append(f"unidade_{unidade}/slides/aula{numero}.html: ausente")
            continue
        validar_deck(p, unidade, numero)

    # nenhum arquivo estranho na pasta de slides
    for unidade in (1, 2, 3, 4):
        d = RAIZ / f"unidade_{unidade}" / "slides"
        if not d.exists():
            continue
        for p in sorted(d.glob("*.html")):
            if not re.fullmatch(r"aula\d+\.html", p.name):
                FALHAS.append(f"unidade_{unidade}/slides/{p.name}: arquivo estranho "
                              "(artefato de montagem?)")

    print("=" * 78)
    print("AUDITORIA DOS DECKS HTML")
    print("=" * 78)
    if detalhe:
        print(f"\nAPROVADOS ({len(OKS)}):")
        for m in OKS:
            print(f"  [ok]     {m}")
    if AVISOS:
        print(f"\nAVISOS ({len(AVISOS)}):")
        for m in AVISOS:
            print(f"  [aviso]  {m}")
    if FALHAS:
        print(f"\nFALHAS ({len(FALHAS)}):")
        for m in FALHAS:
            print(f"  [FALHA]  {m}")
    print("\n" + "-" * 78)
    print(f"Aprovados: {len(OKS)}  |  Avisos: {len(AVISOS)}  |  Falhas: {len(FALHAS)}")
    print("-" * 78)
    return 1 if FALHAS else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
