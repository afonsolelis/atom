#!/usr/bin/env python3
"""Primitivas de desenho para as figuras autorais das unidades.

As figuras são escritas em SVG (fonte editável, versionada junto do texto) e
rasterizadas em PNG para embutir nos DOCX institucionais, que não aceitam SVG.
A paleta reproduz a identidade UniFECAF já usada nos decks HTML.

Não há navegador nem Inkscape neste ambiente: a rasterização usa CairoSVG, que
renderiza apenas SVG estático. Por isso o desenho evita CSS, `<marker>` e
recursos dependentes de layout de texto — as pontas de seta são polígonos
calculados em Python e cada linha de texto recebe posição explícita.
"""

from __future__ import annotations

import math
from pathlib import Path

# ============================================================ identidade visual
AZUL = "#002156"
AZUL_MEDIO = "#254AB9"
AZUL_CLARO = "#00B1D2"
AMARELO = "#F2CB0A"
VERDE = "#11A360"
VERDE_CLARO = "#95DE68"
MAGENTA = "#FF2B5F"
MAGENTA_TXT = "#C2185B"
CINZA_BG = "#F2F4F8"
CINZA_TXT = "#1A1A1A"
MUTE = "#5A6175"
BRANCO = "#FFFFFF"
BORDA = "#C7CEDB"

FONTE = "Liberation Sans, Arial, Helvetica, sans-serif"

# Largura média de caractere, em fração do corpo da fonte, medida para
# Liberation Sans. Serve só para quebrar linhas automaticamente.
RAZAO_CARACTERE = 0.53


def escapar(texto: str) -> str:
    return (
        texto.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def quebrar(texto: str, largura: float, corpo: float) -> list[str]:
    """Quebra `texto` em linhas que caibam em `largura` pixels."""
    limite = max(1, int(largura / (corpo * RAZAO_CARACTERE)))
    linhas: list[str] = []
    atual = ""
    for palavra in texto.split():
        candidato = f"{atual} {palavra}".strip()
        if len(candidato) <= limite or not atual:
            atual = candidato
        else:
            linhas.append(atual)
            atual = palavra
    if atual:
        linhas.append(atual)
    return linhas


class Figura:
    """Acumula elementos SVG e grava SVG + PNG."""

    def __init__(self, largura: int, altura: int, titulo: str, descricao: str):
        self.largura = largura
        self.altura = altura
        self.titulo = titulo
        self.descricao = descricao
        self.partes: list[str] = []

    # -------------------------------------------------------------- primitivas
    def bruto(self, elemento: str) -> None:
        self.partes.append(elemento)

    def retangulo(
        self,
        x: float,
        y: float,
        largura: float,
        altura: float,
        preenchimento: str = BRANCO,
        traco: str = BORDA,
        espessura: float = 2,
        raio: float = 10,
        tracejado: str | None = None,
        opacidade: float = 1.0,
    ) -> None:
        dash = f' stroke-dasharray="{tracejado}"' if tracejado else ""
        self.bruto(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{largura:.1f}" '
            f'height="{altura:.1f}" rx="{raio}" ry="{raio}" '
            f'fill="{preenchimento}" fill-opacity="{opacidade}" '
            f'stroke="{traco}" stroke-width="{espessura}"{dash}/>'
        )

    def linha(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        cor: str = MUTE,
        espessura: float = 2,
        tracejado: str | None = None,
    ) -> None:
        dash = f' stroke-dasharray="{tracejado}"' if tracejado else ""
        self.bruto(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="{cor}" stroke-width="{espessura}" '
            f'stroke-linecap="round"{dash}/>'
        )

    def circulo(
        self,
        cx: float,
        cy: float,
        raio: float,
        preenchimento: str,
        traco: str = "none",
        espessura: float = 2,
    ) -> None:
        self.bruto(
            f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{raio:.1f}" '
            f'fill="{preenchimento}" stroke="{traco}" stroke-width="{espessura}"/>'
        )

    def poligono(self, pontos: list[tuple[float, float]], preenchimento: str) -> None:
        corpo = " ".join(f"{x:.1f},{y:.1f}" for x, y in pontos)
        self.bruto(f'<polygon points="{corpo}" fill="{preenchimento}"/>')

    def caminho(
        self,
        d: str,
        traco: str = MUTE,
        espessura: float = 2,
        preenchimento: str = "none",
        tracejado: str | None = None,
    ) -> None:
        dash = f' stroke-dasharray="{tracejado}"' if tracejado else ""
        self.bruto(
            f'<path d="{d}" fill="{preenchimento}" stroke="{traco}" '
            f'stroke-width="{espessura}" stroke-linecap="round" '
            f'stroke-linejoin="round"{dash}/>'
        )

    def texto(
        self,
        x: float,
        y: float,
        conteudo: str,
        corpo: float = 18,
        cor: str = CINZA_TXT,
        ancora: str = "middle",
        peso: str = "400",
        italico: bool = False,
    ) -> None:
        estilo = ' font-style="italic"' if italico else ""
        self.bruto(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONTE}" '
            f'font-size="{corpo}" font-weight="{peso}" fill="{cor}" '
            f'text-anchor="{ancora}"{estilo}>{escapar(conteudo)}</text>'
        )

    def texto_multilinha(
        self,
        x: float,
        y: float,
        linhas: list[str],
        corpo: float = 18,
        cor: str = CINZA_TXT,
        ancora: str = "middle",
        peso: str = "400",
        entrelinha: float = 1.32,
    ) -> float:
        """Escreve as linhas a partir de `y` e devolve o `y` da última linha."""
        atual = y
        for linha in linhas:
            self.texto(x, atual, linha, corpo, cor, ancora, peso)
            atual += corpo * entrelinha
        return atual - corpo * entrelinha

    def formula(
        self,
        x: float,
        y: float,
        partes: list[tuple[str, str]],
        corpo: float = 18,
        cor: str = CINZA_TXT,
        peso: str = "400",
        ancora: str = "start",
    ) -> None:
        """Texto com subscritos.

        `partes` é uma lista de pares (conteúdo, tipo), com tipo em
        {"base", "sub"} — por exemplo
        [("C ← max(C", "base"), ("local", "sub"), (", C", "base"), ...].
        Tudo sai em um único elemento <text> para que o CairoSVG mantenha o
        avanço horizontal entre os trechos.
        """
        corpo_sub = corpo * 0.7
        deslocamento = corpo * 0.24
        tspans = []
        pendente = 0.0
        for conteudo, tipo in partes:
            if tipo == "sub":
                dy = deslocamento - pendente
                pendente = deslocamento
                tamanho = corpo_sub
            else:
                dy = -pendente
                pendente = 0.0
                tamanho = corpo
            tspans.append(
                f'<tspan font-size="{tamanho:.1f}" dy="{dy:.1f}">'
                f"{escapar(conteudo)}</tspan>"
            )
        self.bruto(
            f'<text x="{x:.1f}" y="{y:.1f}" font-family="{FONTE}" '
            f'font-size="{corpo}" font-weight="{peso}" fill="{cor}" '
            f'text-anchor="{ancora}">{"".join(tspans)}</text>'
        )

    # ---------------------------------------------------------------- compostos
    def seta(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        cor: str = AZUL,
        espessura: float = 2.4,
        tracejado: str | None = None,
        cabeca: float = 11,
    ) -> None:
        angulo = math.atan2(y2 - y1, x2 - x1)
        # a linha para antes da ponta para não engrossar o bico
        fim_x = x2 - math.cos(angulo) * cabeca * 0.85
        fim_y = y2 - math.sin(angulo) * cabeca * 0.85
        self.linha(x1, y1, fim_x, fim_y, cor, espessura, tracejado)
        self.poligono(
            [
                (x2, y2),
                (
                    x2 - math.cos(angulo - 0.42) * cabeca * 1.5,
                    y2 - math.sin(angulo - 0.42) * cabeca * 1.5,
                ),
                (
                    x2 - math.cos(angulo + 0.42) * cabeca * 1.5,
                    y2 - math.sin(angulo + 0.42) * cabeca * 1.5,
                ),
            ],
            cor,
        )

    def caixa(
        self,
        x: float,
        y: float,
        largura: float,
        altura: float,
        titulo: str,
        subtitulo: str | None = None,
        preenchimento: str = BRANCO,
        traco: str = AZUL,
        cor_titulo: str = AZUL,
        cor_subtitulo: str = MUTE,
        corpo: float = 19,
        corpo_sub: float = 15,
        raio: float = 12,
        espessura: float = 2.2,
        tracejado: str | None = None,
    ) -> None:
        self.retangulo(
            x, y, largura, altura, preenchimento, traco, espessura, raio, tracejado
        )
        linhas = quebrar(titulo, largura - 22, corpo)
        sub_linhas = quebrar(subtitulo, largura - 22, corpo_sub) if subtitulo else []
        altura_titulo = len(linhas) * corpo * 1.24
        altura_sub = len(sub_linhas) * corpo_sub * 1.3
        topo = y + (altura - altura_titulo - altura_sub) / 2 + corpo * 0.82
        fim = self.texto_multilinha(
            x + largura / 2, topo, linhas, corpo, cor_titulo, "middle", "700", 1.24
        )
        if sub_linhas:
            self.texto_multilinha(
                x + largura / 2,
                fim + corpo_sub * 1.5,
                sub_linhas,
                corpo_sub,
                cor_subtitulo,
                "middle",
                "400",
                1.3,
            )

    def etiqueta(
        self,
        x: float,
        y: float,
        conteudo: str,
        cor: str = MUTE,
        corpo: float = 15,
        fundo: str = BRANCO,
        ancora: str = "middle",
        peso: str = "400",
    ) -> None:
        """Texto sobre uma tarja opaca, para cruzar linhas sem perder leitura."""
        largura = len(conteudo) * corpo * RAZAO_CARACTERE + 14
        origem = {
            "middle": x - largura / 2,
            "start": x - 7,
            "end": x - largura + 7,
        }[ancora]
        self.retangulo(
            origem, y - corpo * 0.92, largura, corpo * 1.5, fundo, "none", 0, 5
        )
        self.texto(x, y, conteudo, corpo, cor, ancora, peso)

    def faixa(
        self,
        x: float,
        y: float,
        largura: float,
        altura: float,
        conteudo: str,
        cor_fundo: str = CINZA_BG,
        cor_texto: str = AZUL,
        corpo: float = 17,
        traco: str = "none",
    ) -> None:
        self.retangulo(x, y, largura, altura, cor_fundo, traco, 2, 10)
        linhas = quebrar(conteudo, largura - 30, corpo)
        topo = y + (altura - len(linhas) * corpo * 1.3) / 2 + corpo * 0.82
        self.texto_multilinha(
            x + largura / 2, topo, linhas, corpo, cor_texto, "middle", "600", 1.3
        )

    def rotulo_secao(self, x: float, y: float, conteudo: str, cor: str = AZUL) -> None:
        self.texto(x, y, conteudo.upper(), 15, cor, "start", "700")

    # ------------------------------------------------------------------ escrita
    def svg(self) -> str:
        corpo = "\n  ".join(self.partes)
        return (
            f'<svg xmlns="http://www.w3.org/2000/svg" '
            f'width="{self.largura}" height="{self.altura}" '
            f'viewBox="0 0 {self.largura} {self.altura}" role="img">\n'
            f"  <title>{escapar(self.titulo)}</title>\n"
            f"  <desc>{escapar(self.descricao)}</desc>\n"
            f'  <rect width="{self.largura}" height="{self.altura}" fill="{BRANCO}"/>\n'
            f"  {corpo}\n"
            f"</svg>\n"
        )

    def gravar(self, destino: Path, escala: float = 2.0) -> tuple[Path, Path]:
        import cairosvg

        destino.parent.mkdir(parents=True, exist_ok=True)
        caminho_svg = destino.with_suffix(".svg")
        caminho_png = destino.with_suffix(".png")
        caminho_svg.write_text(self.svg(), encoding="utf-8")
        cairosvg.svg2png(
            bytestring=self.svg().encode("utf-8"),
            write_to=str(caminho_png),
            scale=escala,
            background_color=BRANCO,
        )
        return caminho_svg, caminho_png
