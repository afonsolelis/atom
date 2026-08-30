#!/usr/bin/env python3
"""Renderiza fórmulas LaTeX em PNG para embutir nos DOCX institucionais.

Cadeia: LaTeX -> MathJax 3 (Node) -> SVG -> cairosvg -> PNG com fundo
transparente. Os PNGs ficam em `tools/_cache_formulas/`, indexados pelo hash da
fórmula, de modo que reexecuções não pagam o custo de renderizar de novo.

Por que esta cadeia e não outra: esta máquina não tem navegador headless
(o rasterizador do pipeline original), nem distribuição LaTeX, e o delegate SVG
do ImageMagick não resolve as referências de glifo do MathJax — testado, produz
imagem em branco. Node e cairosvg cobrem o caso sem exigir instalação
privilegiada.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

import cairosvg

TOOLS = Path(__file__).resolve().parent
CACHE = TOOLS / "_cache_formulas"
NODE_SCRIPT = TOOLS / "render_formulas.js"

# Escala de rasterização: pixels por unidade "ex" do MathJax. 20 px/ex dá cerca
# de 300 dpi para um corpo de texto de 12 pt, resolução suficiente para
# impressão sem inflar o tamanho do DOCX.
PX_POR_EX = 20.0

# 1 ex do MathJax equivale a aproximadamente 0,442 em do corpo do texto. Com
# Times New Roman 12 pt, isso dá cerca de 5,3 pt por ex — usado para dimensionar
# a imagem no documento, de modo que a fórmula fique proporcional à linha.
PT_POR_EX = 5.3


def hash_formula(tex: str, display: bool) -> str:
    chave = f"{'D' if display else 'I'}|{tex.strip()}"
    return hashlib.sha256(chave.encode("utf-8")).hexdigest()[:16]


def coletar_formulas(texto: str) -> list[tuple[str, bool]]:
    """Extrai as fórmulas de um Markdown, ignorando o que estiver em código.

    Devolve pares (latex, display). Blocos são linhas isoladas com `$` ou
    delimitadas por `$$`; o restante é considerado fórmula de linha.
    """
    sem_codigo = re.sub(r"```.*?```", " ", texto, flags=re.S)
    sem_codigo = re.sub(r"`[^`\n]*`", " ", sem_codigo)

    achadas: list[tuple[str, bool]] = []

    # blocos $$ ... $$
    for m in re.finditer(r"\$\$(.+?)\$\$", sem_codigo, flags=re.S):
        achadas.append((m.group(1).strip(), True))
    sem_codigo = re.sub(r"\$\$.+?\$\$", " ", sem_codigo, flags=re.S)

    # blocos delimitados por linhas contendo apenas "$"
    linhas = sem_codigo.split("\n")
    buffer: list[str] = []
    dentro = False
    resto: list[str] = []
    for linha in linhas:
        if linha.strip() == "$":
            if dentro:
                achadas.append((" ".join(buffer).strip(), True))
                buffer, dentro = [], False
            else:
                dentro = True
            continue
        (buffer if dentro else resto).append(linha)
    sem_codigo = "\n".join(resto)

    # fórmulas de linha $...$
    for m in re.finditer(r"(?<!\$)\$([^$\n]+)\$(?!\$)", sem_codigo):
        achadas.append((m.group(1).strip(), False))

    vistas, unicas = set(), []
    for tex, disp in achadas:
        if tex and (tex, disp) not in vistas:
            vistas.add((tex, disp))
            unicas.append((tex, disp))
    return unicas


def _svg_para_png(svg: str, destino: Path) -> None:
    """Converte o SVG do MathJax em PNG, fixando dimensões em pixels.

    O MathJax emite `width`/`height` em `ex`, unidade que o rasterizador não
    interpreta; sem a substituição por pixels a saída sai vazia ou gigante.
    """
    mw = re.search(r'width="([\d.]+)ex"', svg)
    mh = re.search(r'height="([\d.]+)ex"', svg)
    if not (mw and mh):
        raise ValueError("SVG do MathJax sem dimensões em ex")
    w_px = max(1, round(float(mw.group(1)) * PX_POR_EX))
    h_px = max(1, round(float(mh.group(1)) * PX_POR_EX))
    svg = re.sub(r'width="[\d.]+ex"', f'width="{w_px}px"', svg, count=1)
    svg = re.sub(r'height="[\d.]+ex"', f'height="{h_px}px"', svg, count=1)
    if "xmlns=" not in svg:
        svg = svg.replace("<svg", '<svg xmlns="http://www.w3.org/2000/svg"', 1)
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=str(destino))


def renderizar(formulas: list[tuple[str, bool]], verboso: bool = True) -> dict:
    """Renderiza as fórmulas e devolve {(tex, display): {png, largura_pt, altura_pt}}."""
    CACHE.mkdir(parents=True, exist_ok=True)

    indice: dict[tuple[str, bool], dict] = {}
    pendentes = []
    for tex, disp in formulas:
        h = hash_formula(tex, disp)
        png = CACHE / f"{h}.png"
        meta = CACHE / f"{h}.json"
        if png.exists() and meta.exists():
            dados = json.loads(meta.read_text(encoding="utf-8"))
            indice[(tex, disp)] = {
                "png": png,
                "largura_pt": dados["widthEx"] * PT_POR_EX,
                "altura_pt": dados["heightEx"] * PT_POR_EX,
            }
        else:
            pendentes.append({"id": h, "tex": tex, "display": disp})

    if verboso:
        print(f"  fórmulas: {len(formulas)} distintas | "
              f"{len(formulas) - len(pendentes)} em cache | {len(pendentes)} a renderizar")

    if pendentes:
        proc = subprocess.run(
            ["node", str(NODE_SCRIPT)],
            input=json.dumps(pendentes), capture_output=True, text=True,
            cwd=str(TOOLS), timeout=900,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"MathJax (Node) falhou: {proc.stderr[:500]}")
        resultado = json.loads(proc.stdout)

        falhas = 0
        for item in pendentes:
            h = item["id"]
            dados = resultado.get(h) or {}
            if not dados.get("svg") or dados.get("erro"):
                falhas += 1
                if verboso:
                    print(f"    [falha] {item['tex'][:60]!r}: {dados.get('erro')}")
                continue
            png = CACHE / f"{h}.png"
            try:
                _svg_para_png(dados["svg"], png)
            except Exception as exc:  # noqa: BLE001
                falhas += 1
                if verboso:
                    print(f"    [rasterização falhou] {item['tex'][:60]!r}: {exc}")
                continue
            (CACHE / f"{h}.json").write_text(
                json.dumps({"widthEx": dados["widthEx"], "heightEx": dados["heightEx"],
                            "tex": item["tex"], "display": item["display"]}),
                encoding="utf-8")
            indice[(item["tex"], item["display"])] = {
                "png": png,
                "largura_pt": dados["widthEx"] * PT_POR_EX,
                "altura_pt": dados["heightEx"] * PT_POR_EX,
            }
        if verboso and falhas:
            print(f"    {falhas} fórmula(s) não renderizada(s) — entram como texto")

    return indice


if __name__ == "__main__":
    import sys

    alvos = sys.argv[1:] or [
        "unidade_1/unidade_1.md", "unidade_2/unidade_2.md",
        "unidade_3/unidade_3.md", "unidade_4/unidade_4.md",
    ]
    raiz = TOOLS.parent
    todas: list[tuple[str, bool]] = []
    vistas = set()
    for alvo in alvos:
        p = raiz / alvo
        if not p.exists():
            print(f"  [ausente] {alvo}")
            continue
        for f in coletar_formulas(p.read_text(encoding="utf-8")):
            if f not in vistas:
                vistas.add(f)
                todas.append(f)
    print(f"Renderizando {len(todas)} fórmulas distintas de {len(alvos)} arquivo(s)…")
    idx = renderizar(todas)
    print(f"Prontas: {len(idx)} de {len(todas)}")
