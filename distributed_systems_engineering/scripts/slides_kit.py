"""Kit de composição dos decks HTML da disciplina Distributed Systems Engineering.

Os decks continuam sendo arquivos HTML autocontidos (a entrega é o `.html`). Este kit
apenas gera o bloco `<div class="deck">…</div>`, preservando intactos o `<head>`
(CSS + símbolos SVG) e o `<script>` de navegação já existentes em cada arquivo.

Uso: `python3 scripts/build_slides.py` na raiz da disciplina.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DISCIPLINA = "Distributed Systems Engineering"
PROFESSOR = "Afonso Cesar Lelis Brandão"

FONTE_PROPRIA = (
    'data-source="Elaboração própria: Afonso Cesar Lelis Brandão, 2026" '
    'data-license="CC BY 4.0"'
)

# ---------------------------------------------------------------- decorações

MOSAICO = (
    '    <div class="mosaico-bg" aria-hidden="true">\n'
    '      <svg preserveAspectRatio="none"><use href="#mosaico-frame"/></svg>\n'
    '    </div>\n'
)


def _rodape(aula: int) -> str:
    if aula < 1:
        return (
            f'    <div class="slide-footer"><span>{DISCIPLINA}</span>'
            f'<span>Apresentação da disciplina</span></div>\n'
        )
    unidade = (aula - 1) // 4 + 1
    return (
        f'    <div class="slide-footer"><span>{DISCIPLINA} · Unidade {unidade}</span>'
        f'<span>Aula {aula} — Videoaula {aula}</span></div>\n'
    )


def _itens(itens: list[str]) -> str:
    return "\n".join(f"          <li>{i}</li>" for i in itens)


# ------------------------------------------------------------------- slides


def capa(aula: int, titulo: str, subtitulo: str) -> str:
    rotulo = f"Aula {aula} — {titulo}" if aula >= 1 else titulo
    return f"""  <section class="slide slide-capa active">
    <div class="capa-canto capa-tl" aria-hidden="true"><svg viewBox="0 0 300 300"><use href="#capa-canto-1"/></svg></div>
    <div class="capa-canto capa-tr" aria-hidden="true"><svg viewBox="0 0 300 300"><use href="#capa-canto-2"/></svg></div>
    <div class="capa-canto capa-bl" aria-hidden="true"><svg viewBox="0 0 300 300"><use href="#capa-canto-3"/></svg></div>
    <div class="capa-canto capa-br" aria-hidden="true"><svg viewBox="0 0 300 300"><use href="#capa-canto-4"/></svg></div>
    <div class="slide-content">
      <div class="logo-marca">
        <svg width="340" height="84" viewBox="0 0 271 67" role="img" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
      </div>
      <h1>{rotulo}</h1>
      <div class="subtitulo">{subtitulo}</div>
      <div class="docente">Prof. {PROFESSOR}</div>
    </div>
  </section>
"""


def audiodescricao(texto: str) -> str:
    return f"""  <section class="slide slide-audio">
    <div class="audio-canto-tl" aria-hidden="true"><svg viewBox="0 0 150 130"><use href="#audio-canto-tl"/></svg></div>
    <div class="audio-canto-br" aria-hidden="true"><svg viewBox="0 0 360 250"><use href="#audio-canto-br"/></svg></div>
    <div class="slide-content">
      <div class="audio-logo">
        <svg width="180" height="44" viewBox="0 0 271 67" role="img" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
      </div>
      <h1>Audiodescrição</h1>
      <p class="audio-texto">{texto}</p>
    </div>
  </section>
"""


def professor(descricao: str) -> str:
    """Slide 'Sobre o professor' — usado apenas na abertura da disciplina (aula 0)."""
    return f"""  <section class="slide slide-prof">
    <div class="prof-grid">
      <div class="prof-lado-claro">
        <div class="prof-logo-claro">
          <svg width="200" height="49" viewBox="0 0 271 67" role="img" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
        </div>
        <div class="prof-foto" role="figure" aria-label="Retrato do professor {PROFESSOR}" data-source="Acervo pessoal de {PROFESSOR}" data-license="Uso autorizado neste material didático">
          <img src="assets/foto-professor.jpg" alt="Professor {PROFESSOR}, responsável pela disciplina" />
        </div>
      </div>
      <div class="prof-lado-escuro">
        <div class="prof-canto-topo" aria-hidden="true"><svg width="110" height="110"><use href="#prof-canto-amarelo"/></svg></div>
        <div class="prof-triangulos-boundary" aria-hidden="true">
          <svg width="200" height="100%" viewBox="0 0 200 400" preserveAspectRatio="xMidYMid meet"><use href="#prof-cluster"/></svg>
        </div>
        <div class="prof-canto-rodape" aria-hidden="true"><svg width="90" height="60" viewBox="0 0 120 80"><use href="#prof-mini-cluster"/></svg></div>
        <h2 class="prof-nome">{PROFESSOR}</h2>
        <p class="prof-cargo">Professor e conteudista · UniFECAF</p>
        <p class="prof-descricao">{descricao}</p>
      </div>
    </div>
  </section>
"""


def sumario(titulo: str, itens: list[str]) -> str:
    return f"""  <section class="slide slide-sumario">
    <div class="sumario-grid">
      <div class="sumario-lado-claro">
        <div class="sumario-logo">
          <svg width="180" height="44" viewBox="0 0 271 67" role="img" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
        </div>
        <h1 class="sumario-titulo">{titulo}</h1>
      </div>
      <div class="sumario-lado-escuro">
        <div class="prof-canto-topo" aria-hidden="true">
          <svg width="110" height="110"><use href="#prof-canto-amarelo"/></svg>
        </div>
        <div class="prof-triangulos-boundary" aria-hidden="true">
          <svg width="200" height="100%" viewBox="0 0 200 400" preserveAspectRatio="xMidYMid meet"><use href="#prof-cluster"/></svg>
        </div>
        <h2>Sumário</h2>
        <ul>
{_itens(itens)}
        </ul>
        <div class="sumario-canto-rodape" aria-hidden="true">
          <svg width="110" height="110"><use href="#prof-canto-amarelo"/></svg>
        </div>
      </div>
    </div>
  </section>
"""


def slide(aula: int, kicker: str, titulo: str, corpo: str, visual: str | None = None,
          classe: str = "") -> str:
    """Slide de conteúdo padrão: moldura de mosaico + cartão.

    `visual` liga o tratamento gráfico do cartão (map, compare, flow, timeline,
    metric, cycle, triangle, pyramid). `corpo` é o HTML interno do cartão.
    """
    if visual:
        box = (
            f'<div class="slide-content-box visual-diagram" '
            f'data-visual-type="{visual}" {FONTE_PROPRIA}>'
        )
    else:
        box = '<div class="slide-content-box">'
    secao = f'  <section class="slide {classe}">'.replace(" >", ">").rstrip()
    if not classe:
        secao = '  <section class="slide">'
    return f"""{secao}
{MOSAICO}    <div class="slide-content">
      <p class="kicker">{kicker}</p>
      <h2>{titulo}</h2>
      {box}
{corpo}
      </div>
    </div>
{_rodape(aula)}  </section>
"""


def citacao(texto: str, autoria: str) -> str:
    return f"""  <section class="slide slide-quote">
    <div class="quote-logo">
      <svg width="200" height="49" viewBox="0 0 271 67" role="img" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
    </div>
    <div class="quote-shapes" aria-hidden="true">
      <svg viewBox="0 0 1200 90" preserveAspectRatio="none"><use href="#faixa-mosaico"/></svg>
    </div>
    <div class="quote-card">
      <blockquote>{texto}</blockquote>
      <cite>{autoria}</cite>
    </div>
  </section>
"""


def pontos_chave(aula: int, pontos: list[tuple[str, str]]) -> str:
    cartoes = "\n".join(
        f'          <div class="ponto"><h3>{t}</h3><p>{d}</p></div>'
        for t, d in pontos
    )
    return f"""  <section class="slide">
{MOSAICO}    <div class="slide-content">
      <p class="kicker">Recapitulando</p>
      <h2>Pontos-chave</h2>
      <div class="slide-content-box">
        <div class="pontos-chave">
{cartoes}
        </div>
      </div>
    </div>
{_rodape(aula)}  </section>
"""


def encerramento(texto: str, proxima: str) -> str:
    return f"""  <section class="slide slide-fim">
    <div class="fim-logo">
      <svg width="220" height="54" viewBox="0 0 271 67" role="img" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
    </div>
    <div class="fim-cluster-topo" aria-hidden="true">
      <svg viewBox="0 0 600 200" preserveAspectRatio="xMaxYMax meet"><use href="#cluster-fim"/></svg>
    </div>
    <div class="fim-cluster-base" aria-hidden="true">
      <svg viewBox="0 0 600 200" preserveAspectRatio="xMidYMax meet"><use href="#cluster-fim"/></svg>
    </div>
    <div class="slide-content">
      <h1>Encerramento</h1>
      <p class="fim-texto">{texto}</p>
      <p class="fim-proxima">{proxima}</p>
      <p class="fim-prof">Prof. {PROFESSOR}</p>
    </div>
  </section>
"""


# ------------------------------------------------------- blocos de conteúdo


def ul(itens: list[str]) -> str:
    linhas = "\n".join(f"          <li>{i}</li>" for i in itens)
    return f"        <ul>\n{linhas}\n        </ul>"


def p(texto: str) -> str:
    return f"        <p>{texto}</p>"


def tabela(cabecalho: list[str], linhas: list[list[str]]) -> str:
    th = "".join(f"<th>{c}</th>" for c in cabecalho)
    trs = "\n".join(
        "            <tr>" + "".join(f"<td>{c}</td>" for c in linha) + "</tr>"
        for linha in linhas
    )
    return (
        '        <table class="tabela-industrial">\n'
        f"          <thead><tr>{th}</tr></thead>\n"
        f"          <tbody>\n{trs}\n          </tbody>\n"
        "        </table>"
    )


def numeros(cartoes: list[tuple[str, str]]) -> str:
    itens = "\n".join(
        f'          <div class="stat-card"><span class="numero-grande">{n}</span>'
        f'<span class="legenda">{leg}</span></div>'
        for n, leg in cartoes
    )
    return f'        <div class="stat-grid">\n{itens}\n        </div>'


def destaque(texto: str) -> str:
    return f'        <div class="callout-azul"><p>{texto}</p></div>'


def formula(expressao: str) -> str:
    return f'        <div class="callout-azul formula"><p>{expressao}</p></div>'


def codigo(fonte: str, legenda: str = "") -> str:
    corpo = html.escape(fonte.strip("\n"))
    rotulo = f'<figcaption>{legenda}</figcaption>' if legenda else ""
    return f'        <figure class="bloco-codigo">{rotulo}<pre><code>{corpo}</code></pre></figure>'


# ------------------------------------------------------------- montagem/IO


ABERTURA = '<div class="deck" id="deck">\n\n'
FECHAMENTO = '</div>\n'


def montar(secoes: list[str]) -> str:
    return ABERTURA + "\n".join(secoes) + "\n" + FECHAMENTO


def escrever(caminho: Path, corpo: str) -> int:
    """Substitui apenas o bloco do deck, preservando head e script do arquivo."""
    original = caminho.read_text(encoding="utf-8")
    padrao = re.compile(
        r'<div class="deck" id="deck">.*?\n</div>\n', re.DOTALL
    )
    if not padrao.search(original):
        raise SystemExit(f"bloco .deck não encontrado em {caminho}")
    novo = padrao.sub(lambda _: corpo, original, count=1)
    caminho.write_text(novo, encoding="utf-8")
    return novo.count('<section class="slide')
