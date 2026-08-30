"""Utilidades de visualização do NexaBot: tabelas e gráficos ASCII no terminal,
mais salvamento de figuras PNG (backend Agg, sem janela) para complementar a
gravação de tela das aulas.

A prioridade é a saída de terminal: toda função aqui produz algo legível
imediatamente no console, sem depender de abrir um visualizador de imagens.
Os PNGs em `figuras/` são o complemento, não o produto principal.

Rastreabilidade: apoio às Aulas 1-7 (Unidades 1 e 2).
"""

from __future__ import annotations

import os
import re

import matplotlib

matplotlib.use("Agg")  # nunca abre janela: essencial para gravação de tela
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402

FIGURAS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "figuras")

# --------------------------------------------------------------------------
# Cores ANSI (verde/vermelho/amarelo) para relatórios de terminal
# --------------------------------------------------------------------------

_ANSI_RE = re.compile(r"\033\[[0-9;]*m")


def _largura_visivel(texto: str) -> int:
    """Comprimento do texto ignorando códigos de escape ANSI (cor/negrito)."""
    return len(_ANSI_RE.sub("", texto))


def _pad(texto: str, largura: int, alinhar: str = "e") -> str:
    """`ljust`/`rjust` cientes de ANSI: o preenchimento usa a largura visível."""
    falta = largura - _largura_visivel(texto)
    if falta <= 0:
        return texto
    return (texto + " " * falta) if alinhar == "e" else (" " * falta + texto)


_RESET = "\033[0m"
_CODIGOS = {
    "verde": "\033[92m",
    "vermelho": "\033[91m",
    "amarelo": "\033[93m",
    "azul": "\033[94m",
    "ciano": "\033[96m",
    "negrito": "\033[1m",
    "cinza": "\033[90m",
}


def _colorir(texto: str, cor: str) -> str:
    return f"{_CODIGOS[cor]}{texto}{_RESET}"


def verde(texto: str) -> str:
    """Colore o texto de verde (usado para itens OK)."""
    return _colorir(texto, "verde")


def vermelho(texto: str) -> str:
    """Colore o texto de vermelho (usado para itens com falha)."""
    return _colorir(texto, "vermelho")


def amarelo(texto: str) -> str:
    """Colore o texto de amarelo (usado para avisos)."""
    return _colorir(texto, "amarelo")


def negrito(texto: str) -> str:
    """Aplica negrito ao texto."""
    return _colorir(texto, "negrito")


def titulo(texto: str, largura: int = 78) -> str:
    """Formata um cabeçalho de seção com linha de destaque."""
    barra = "=" * largura
    return f"\n{barra}\n{negrito(texto)}\n{barra}"


# --------------------------------------------------------------------------
# Tabela ASCII
# --------------------------------------------------------------------------

def tabela(cabecalhos: list[str], linhas: list[list], titulo_tabela: str | None = None,
           alinhamentos: list[str] | None = None) -> str:
    """Monta e imprime uma tabela ASCII com bordas Unicode.

    `alinhamentos` é uma lista opcional de 'e' (esquerda) ou 'd' (direita) por
    coluna; por padrão a primeira coluna é alinhada à esquerda e o resto à
    direita (convém para nome-do-parâmetro | valor).
    """
    linhas_str = [[str(c) for c in linha] for linha in linhas]
    n_col = len(cabecalhos)
    larguras = [_largura_visivel(h) for h in cabecalhos]
    for linha in linhas_str:
        for j in range(n_col):
            larguras[j] = max(larguras[j], _largura_visivel(linha[j]))

    if alinhamentos is None:
        alinhamentos = ["e"] + ["d"] * (n_col - 1)

    def _fmt_linha(campos):
        partes = []
        for j, campo in enumerate(campos):
            alinhar = "d" if alinhamentos[j] == "d" else "e"
            partes.append(_pad(campo, larguras[j], alinhar))
        return "│ " + " │ ".join(partes) + " │"

    topo = "┌─" + "─┬─".join("─" * w for w in larguras) + "─┐"
    meio = "├─" + "─┼─".join("─" * w for w in larguras) + "─┤"
    fundo = "└─" + "─┴─".join("─" * w for w in larguras) + "─┘"

    saida = []
    if titulo_tabela:
        saida.append(negrito(titulo_tabela))
    saida.append(topo)
    saida.append(_fmt_linha(cabecalhos))
    saida.append(meio)
    for linha in linhas_str:
        saida.append(_fmt_linha(linha))
    saida.append(fundo)

    texto = "\n".join(saida)
    print(texto)
    return texto


# --------------------------------------------------------------------------
# Sparkline (mini-gráfico de uma linha)
# --------------------------------------------------------------------------

_BLOCOS = " ▁▂▃▄▅▆▇█"


def sparkline(y, largura: int | None = None) -> str:
    """Gera uma sparkline Unicode de uma linha a partir da série `y`.

    Reamostra para `largura` pontos (padrão: min(len(y), 60)) e mapeia cada
    valor para um dos 8 blocos de altura Unicode.
    """
    y = np.asarray(y, dtype=float)
    if largura is None:
        largura = min(len(y), 60)
    if len(y) > largura:
        idx = np.linspace(0, len(y) - 1, largura).astype(int)
        y = y[idx]

    y_min, y_max = float(np.min(y)), float(np.max(y))
    faixa = y_max - y_min
    if faixa < 1e-12:
        niveis = np.full(len(y), len(_BLOCOS) // 2, dtype=int)
    else:
        niveis = np.round((y - y_min) / faixa * (len(_BLOCOS) - 1)).astype(int)

    linha = "".join(_BLOCOS[n] for n in niveis)
    print(f"{linha}  [{y_min:.4g} .. {y_max:.4g}]")
    return linha


# --------------------------------------------------------------------------
# Gráfico ASCII (eixos + curva)
# --------------------------------------------------------------------------

def plot_ascii(t, y, altura: int = 15, largura: int = 60, titulo_grafico: str | None = None,
               y_ref: float | None = None, unidade_x: str = "s", unidade_y: str = "") -> str:
    """Desenha um gráfico ASCII de `y(t)` em uma grade `altura` x `largura`.

    Usa '*' para a curva e, se `y_ref` for informado, uma linha pontilhada
    ':' marcando a referência (útil para respostas ao degrau). Devolve o
    texto desenhado (também impresso no terminal).
    """
    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)

    if len(t) > largura:
        idx = np.linspace(0, len(t) - 1, largura).astype(int)
        t_plot = t[idx]
        y_plot = y[idx]
    else:
        t_plot, y_plot = t, y

    y_min = float(np.min(y_plot))
    y_max = float(np.max(y_plot))
    if y_ref is not None:
        y_min = min(y_min, y_ref)
        y_max = max(y_max, y_ref)
    faixa = y_max - y_min
    if faixa < 1e-12:
        faixa = 1.0

    grade = [[" " for _ in range(len(y_plot))] for _ in range(altura)]

    def _linha_de(valor):
        frac = (valor - y_min) / faixa
        linha = int(round(frac * (altura - 1)))
        return altura - 1 - linha

    if y_ref is not None:
        lr = _linha_de(y_ref)
        if 0 <= lr < altura:
            for c in range(len(y_plot)):
                grade[lr][c] = "·"

    linhas_coluna = [min(max(_linha_de(v), 0), altura - 1) for v in y_plot]
    for c, lc in enumerate(linhas_coluna):
        grade[lc][c] = "*"
        # preenche o vão vertical entre colunas consecutivas (evita "buracos"
        # em trechos de subida/descida íngreme, comuns na resposta ao degrau)
        if c > 0:
            l_ant = linhas_coluna[c - 1]
            passo = 1 if lc > l_ant else -1
            for l in range(l_ant + passo, lc, passo):
                if grade[l][c - 1] == " ":
                    grade[l][c - 1] = "¦"

    saida = []
    if titulo_grafico:
        saida.append(negrito(titulo_grafico))
    rotulo_w = 11
    for i, linha in enumerate(grade):
        valor_eixo = y_max - (y_max - y_min) * i / (altura - 1)
        rotulo = f"{valor_eixo:>9.3g} │"
        saida.append(rotulo + "".join(linha))
    saida.append(" " * rotulo_w + "└" + "─" * len(y_plot))
    saida.append(
        " " * rotulo_w
        + f" t: 0 .. {t_plot[-1]:.4g} {unidade_x}"
        + (f"   y [{unidade_y}]" if unidade_y else "")
    )
    if y_ref is not None:
        saida.append(" " * rotulo_w + f" referência (·): {y_ref:.4g} {unidade_y}")

    texto = "\n".join(saida)
    print(texto)
    return texto


# --------------------------------------------------------------------------
# Figuras PNG (complemento)
# --------------------------------------------------------------------------

def garantir_diretorio_figuras() -> str:
    """Garante que `figuras/` exista e devolve o caminho absoluto."""
    os.makedirs(FIGURAS_DIR, exist_ok=True)
    return FIGURAS_DIR


def salvar_figura(fig, nome_arquivo: str) -> str:
    """Salva `fig` como PNG em `figuras/<nome_arquivo>` e fecha a figura."""
    garantir_diretorio_figuras()
    caminho = os.path.join(FIGURAS_DIR, nome_arquivo)
    fig.savefig(caminho, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  (figura salva em {caminho})")
    return caminho


def figura_resposta_degrau(t, y, y_ref=None, titulo_fig: str = "Resposta ao degrau",
                            ylabel: str = "y(t)", nome_arquivo: str = "resposta_degrau.png") -> str:
    """Gera e salva um PNG padrão de resposta ao degrau (curva + referência)."""
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t, y, label="resposta", color="#1f6feb", linewidth=1.8)
    if y_ref is not None:
        ax.axhline(y_ref, color="#d1242f", linestyle="--", linewidth=1.2, label="referência")
    ax.set_xlabel("tempo [s]")
    ax.set_ylabel(ylabel)
    ax.set_title(titulo_fig)
    ax.grid(True, alpha=0.3)
    ax.legend()
    return salvar_figura(fig, nome_arquivo)
