#!/usr/bin/env python3
"""Exporta o material da disciplina de Markdown para DOCX institucional.

Pipeline: Markdown -> HTML com estilos institucionais -> LibreOffice -> DOCX.

Formatação aplicada, conforme `DIRETRIZES_PRODUCAO.md`:
  - corpo em Times New Roman 12, espaçamento entre linhas 1,15;
  - alinhamento à esquerda, sem recuo adicional após os parágrafos;
  - títulos hierárquicos em Times New Roman;
  - trechos de código em Courier New 10, em bloco sombreado;
  - tabelas com bordas e cabeçalho em negrito.

A matemática em LaTeX é convertida para texto Unicode legível: o DOCX é um
documento de leitura institucional, não um artigo tipografado. A fonte
Markdown continua sendo a versão canônica das fórmulas.

Uso:
    tools/.venv/bin/python tools/build_docx.py              # exporta tudo
    tools/.venv/bin/python tools/build_docx.py unidade_1    # exporta um alvo
    tools/.venv/bin/python tools/build_docx.py --lista      # lista os alvos
"""

from __future__ import annotations

import html
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import markdown as md_lib
except ImportError:  # pragma: no cover
    sys.exit(
        "Falta a dependência 'markdown'. Instale com:\n"
        "  uv pip install --python tools/.venv/bin/python markdown"
    )

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "entrega_docx" / "_apoio_producao"

# --- Alvos de exportação -------------------------------------------------
#
# ATENÇÃO AO ESCOPO DESTE SCRIPT.
#
# A entrega institucional NÃO sai daqui. Os documentos que têm modelo oficial da
# UniFECAF — as quatro unidades, os quatro questionários, a avaliação final e a
# entrega de trabalho — são preenchidos dentro dos próprios modelos Word por:
#
#     tools/preencher_unidades.py
#     tools/preencher_questoes.py
#     tools/preencher_instrumentos.py
#
# Este script cobre apenas os documentos de produção que **não possuem modelo
# institucional** (plano de aprendizagem, diretrizes, análise dos materiais,
# ambiente, cronograma e o roteiro do vídeo introdutório). Eles são material de
# trabalho e de conferência da coordenação, e por isso saem em uma subpasta
# separada, para não se misturarem ao pacote institucional.
#
# (caminho relativo do .md, nome do DOCX gerado, corte antes da Parte B?)
ALVOS: list[tuple[str, str, bool]] = [
    ("PLANO_APRENDIZAGEM_PROPOSTO.md", "00 - Plano de Aprendizagem Proposto", False),
    ("DIRETRIZES_PRODUCAO.md", "00 - Diretrizes de Producao", False),
    ("ANALISE_MATERIAIS_RECEBIDOS.md", "00 - Analise dos Materiais Recebidos", False),
    ("AMBIENTE_E_STACK.md", "00 - Ambiente e Pilha Tecnologica", False),
    ("CRONOGRAMA.md", "00 - Cronograma de Producao e Validacao", False),
    ("roteiro_video_introdutorio.md", "00 - Roteiro do Video Introdutorio", False),
]

# --- Conversão de LaTeX para texto Unicode -------------------------------

SIMBOLOS = {
    r"\\times": "×", r"\\cdot": "·", r"\\approx": "≈", r"\\neq": "≠",
    r"\\leq": "≤", r"\\geq": "≥", r"\\pm": "±", r"\\infty": "∞",
    r"\\alpha": "α", r"\\beta": "β", r"\\gamma": "γ", r"\\delta": "δ",
    r"\\Delta": "Δ", r"\\epsilon": "ε", r"\\varepsilon": "ε", r"\\zeta": "ζ",
    r"\\eta": "η", r"\\theta": "θ", r"\\lambda": "λ", r"\\mu": "μ",
    r"\\pi": "π", r"\\rho": "ρ", r"\\sigma": "σ", r"\\tau": "τ",
    r"\\phi": "φ", r"\\omega": "ω", r"\\Omega": "Ω", r"\\Sigma": "Σ",
    r"\\rightarrow": "→", r"\\to": "→", r"\\Rightarrow": "⇒",
    r"\\leftarrow": "←", r"\\Leftarrow": "⇐", r"\\in": "∈",
    r"\\forall": "∀", r"\\exists": "∃", r"\\wedge": "∧", r"\\vee": "∨",
    r"\\neg": "¬", r"\\land": "∧", r"\\lor": "∨", r"\\int": "∫",
    r"\\partial": "∂", r"\\nabla": "∇", r"\\sum": "Σ", r"\\prod": "Π",
    r"\\dot": "", r"\\ldots": "…", r"\\dots": "…",
    r"\\quad": "  ", r"\\qquad": "    ",
}

# Espaçadores LaTeX. Precisam ser tratados antes dos símbolos nomeados e sem a
# proteção `(?![a-zA-Z])`: em "2{,}92\,ms" o caractere seguinte a `\,` é uma
# letra, e o lookahead impediria a substituição, deixando `\,` literal no DOCX.
ESPACADORES = [
    (r"\\,", " "), (r"\\;", " "), (r"\\:", " "), (r"\\!", ""), (r"\\ ", " "),
]

SOBRESCRITO = str.maketrans("0123456789+-=()n", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿ")
SUBSCRITO = str.maketrans("0123456789+-=()aeioxhklmnpst",
                          "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑᵢₒₓₕₖₗₘₙₚₛₜ")


def latex_para_texto(expr: str) -> str:
    """Converte uma expressão LaTeX simples em texto Unicode legível."""
    s = expr

    # \frac{a}{b} -> (a)/(b), aplicado repetidamente para casos aninhados
    for _ in range(4):
        novo = re.sub(r"\\d?frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", s)
        if novo == s:
            break
        s = novo

    # \sqrt{a} -> √(a)
    s = re.sub(r"\\sqrt\{([^{}]*)\}", r"√(\1)", s)

    # \mathrm{...}, \text{...}, \mathbf{...} -> conteúdo puro
    s = re.sub(r"\\(?:mathrm|text|mathbf|mathit|operatorname)\{([^{}]*)\}", r"\1", s)

    # matrizes: \begin{bmatrix} a & b \\ c & d \end{bmatrix} -> [a b; c d]
    def _matriz(m):
        corpo = m.group(1)
        linhas = [ln.strip() for ln in re.split(r"\\\\", corpo) if ln.strip()]
        return "[" + "; ".join(" ".join(c.strip() for c in ln.split("&")) for ln in linhas) + "]"

    s = re.sub(r"\\begin\{[bp]matrix\}(.*?)\\end\{[bp]matrix\}", _matriz, s, flags=re.S)

    # espaçadores primeiro (ver comentário em ESPACADORES)
    for padrao, sub in ESPACADORES:
        s = re.sub(padrao, sub, s)

    # símbolos nomeados
    for padrao, sub in SIMBOLOS.items():
        s = re.sub(padrao + r"(?![a-zA-Z])", sub, s)

    # expoentes e índices
    s = re.sub(r"\^\{([^{}]*)\}",
               lambda m: m.group(1).translate(SOBRESCRITO)
               if all(c in "0123456789+-=()n" for c in m.group(1)) else f"^({m.group(1)})", s)
    s = re.sub(r"\^(\w)",
               lambda m: m.group(1).translate(SOBRESCRITO)
               if m.group(1) in "0123456789n" else f"^{m.group(1)}", s)
    s = re.sub(r"_\{([^{}]*)\}",
               lambda m: m.group(1).translate(SUBSCRITO)
               if all(c in "0123456789+-=()aeioxhklmnpst" for c in m.group(1))
               else f"_({m.group(1)})", s)
    s = re.sub(r"_(\w)",
               lambda m: m.group(1).translate(SUBSCRITO)
               if m.group(1) in "0123456789aeioxhklmnpst" else f"_{m.group(1)}", s)

    # separador decimal preservado: {,} -> ,
    s = s.replace("{,}", ",")

    # chaves e barras invertidas residuais
    s = s.replace("\\left", "").replace("\\right", "")
    s = re.sub(r"\\[a-zA-Z]+", "", s)
    s = s.replace("{", "").replace("}", "")
    return s.strip()


def converter_matematica(texto: str) -> str:
    """Substitui blocos e trechos LaTeX por texto Unicode, preservando código."""
    partes = re.split(r"(```.*?```|`[^`\n]*`)", texto, flags=re.S)
    for i, parte in enumerate(partes):
        if parte.startswith("```") or parte.startswith("`"):
            continue  # nunca mexer em código

        # bloco: linha contendo apenas $ ... $ delimitando
        linhas = parte.split("\n")
        saida, dentro, buffer = [], False, []
        for linha in linhas:
            if linha.strip() == "$":
                if dentro:
                    expr = latex_para_texto(" ".join(buffer))
                    saida.append(f"<<<EQBLOCO>>>{expr}<<<FIMEQ>>>")
                    buffer, dentro = [], False
                else:
                    dentro = True
                continue
            if dentro:
                buffer.append(linha)
            else:
                saida.append(linha)
        if dentro:  # bloco não fechado: devolve como estava
            saida.append("$")
            saida.extend(buffer)
        parte = "\n".join(saida)

        # inline $...$
        parte = re.sub(r"\$([^$\n]+)\$", lambda m: latex_para_texto(m.group(1)), parte)
        partes[i] = parte
    return "".join(partes)


# --- Montagem do HTML ----------------------------------------------------

CSS = """
@page { size: A4; margin: 2.5cm 2.0cm 2.0cm 3.0cm; }
body { font-family: "Times New Roman", Times, serif; font-size: 12pt;
       line-height: 1.15; text-align: left; color: #000; }
p { margin: 0 0 6pt 0; text-align: left; text-indent: 0; }
h1 { font-family: "Times New Roman", Times, serif; font-size: 16pt;
     font-weight: bold; margin: 18pt 0 10pt 0; }
h2 { font-size: 14pt; font-weight: bold; margin: 16pt 0 8pt 0; }
h3 { font-size: 12pt; font-weight: bold; margin: 14pt 0 6pt 0; }
h4 { font-size: 12pt; font-weight: bold; font-style: italic; margin: 12pt 0 6pt 0; }
ul, ol { margin: 0 0 6pt 0; padding-left: 20pt; }
li { margin: 0 0 3pt 0; }
table { border-collapse: collapse; width: 100%; margin: 8pt 0 10pt 0; font-size: 10pt; }
th, td { border: 0.5pt solid #444; padding: 3pt 5pt; text-align: left;
         vertical-align: top; }
th { font-weight: bold; background-color: #E8E8E8; }
pre { font-family: "Courier New", monospace; font-size: 9pt; background-color: #F2F2F2;
      border: 0.5pt solid #BBB; padding: 6pt; margin: 6pt 0 8pt 0;
      white-space: pre-wrap; line-height: 1.05; }
code { font-family: "Courier New", monospace; font-size: 10pt; }
blockquote { margin: 6pt 0 8pt 16pt; padding-left: 8pt;
             border-left: 2pt solid #888; font-size: 11pt; }
hr { border: none; border-top: 0.5pt solid #888; margin: 12pt 0; }
.eqbloco { font-family: "Times New Roman", Times, serif; font-style: italic;
           text-align: center; margin: 8pt 0 8pt 0; font-size: 12pt; }
.rodape { font-size: 9pt; color: #555; margin-top: 18pt;
          border-top: 0.5pt solid #AAA; padding-top: 6pt; }
"""


def cortar_parte_do_tutor(texto: str) -> str:
    """Corta o documento antes da Parte B (versão exclusiva do tutor)."""
    padrao = re.compile(r"^#{1,2}\s*Parte B\b.*$", re.M | re.I)
    m = padrao.search(texto)
    if not m:
        return texto
    corte = texto[: m.start()].rstrip()
    # remove um separador '---' imediatamente anterior ao corte
    corte = re.sub(r"\n-{3,}\s*$", "", corte)
    # A cópia distribuída não deve parecer um arquivo-mestre nem instruir o
    # estudante sobre o conteúdo reservado ao tutor.
    corte = re.sub(r"^.*(?:Controle de versão:|Arquivo-mestre de produção\.).*$\n?",
                   "", corte, flags=re.M)
    corte = corte.replace("— arquivo-mestre", "— versão do estudante")
    corte = re.sub(r"^# Parte A — Versão do estudante$", "# Versão do estudante",
                   corte, flags=re.M)
    return corte + (
        "\n\n---\n\n*Documento de distribuição ao estudante.*\n"
    )


def md_para_html(caminho_md: Path, titulo: str, cortar: bool) -> str:
    texto = caminho_md.read_text(encoding="utf-8")
    if cortar:
        texto = cortar_parte_do_tutor(texto)
    texto = converter_matematica(texto)

    corpo = md_lib.markdown(
        texto,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"],
        output_format="html5",
    )

    corpo = corpo.replace("&lt;&lt;&lt;EQBLOCO&gt;&gt;&gt;", '<p class="eqbloco">')
    corpo = corpo.replace("&lt;&lt;&lt;FIMEQ&gt;&gt;&gt;", "</p>")
    corpo = corpo.replace("<<<EQBLOCO>>>", '<p class="eqbloco">')
    corpo = corpo.replace("<<<FIMEQ>>>", "</p>")

    return (
        "<!DOCTYPE html>\n<html lang=\"pt-BR\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        f"<title>{html.escape(titulo)}</title>\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n{corpo}\n"
        "<p class=\"rodape\">Model-Based Design for Cyber-Physical Systems — "
        "Professor-conteudista: Afonso Cesar Lelis Brand&atilde;o. "
        f"Documento gerado automaticamente a partir de <code>{html.escape(caminho_md.name)}</code>.</p>\n"
        "</body>\n</html>\n"
    )


def html_para_docx(html_texto: str, destino: Path) -> None:
    """Converte HTML em DOCX com o LibreOffice em modo headless."""
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        raise RuntimeError("LibreOffice não encontrado no PATH (soffice/libreoffice).")

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        origem = tmp_path / (destino.stem + ".html")
        origem.write_text(html_texto, encoding="utf-8")

        proc = subprocess.run(
            [
                soffice, "--headless", "--norestore",
                f"-env:UserInstallation=file://{tmp_path / 'lo-profile'}",
                "--infilter=HTML (StarWriter)",
                "--convert-to", "docx:MS Word 2007 XML",
                "--outdir", str(tmp_path), str(origem),
            ],
            capture_output=True, text=True, timeout=600,
        )
        gerado = tmp_path / (destino.stem + ".docx")
        if not gerado.exists():
            raise RuntimeError(
                f"Conversão falhou para {destino.name}.\n"
                f"stdout: {proc.stdout}\nstderr: {proc.stderr}"
            )
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(gerado), str(destino))


def main(argv: list[str]) -> int:
    if "--lista" in argv:
        print("Alvos de exportação:\n")
        for rel, nome, cortar in ALVOS:
            marca = "  [corta Parte B]" if cortar else ""
            print(f"  {rel:52s} -> {nome}.docx{marca}")
        return 0

    filtro = [a for a in argv[1:] if not a.startswith("-")]
    alvos = [a for a in ALVOS if not filtro or any(f in a[0] or f in a[1] for f in filtro)]
    if not alvos:
        print(f"Nenhum alvo corresponde a {filtro}. Use --lista para ver os alvos.")
        return 1

    SAIDA.mkdir(parents=True, exist_ok=True)
    ok, ausentes, falhas = 0, [], []

    for rel, nome, cortar in alvos:
        origem = RAIZ / rel
        if not origem.exists():
            ausentes.append(rel)
            print(f"  [ausente] {rel}")
            continue
        destino = SAIDA / f"{nome}.docx"
        try:
            html_texto = md_para_html(origem, nome, cortar)
            html_para_docx(html_texto, destino)
            tam = destino.stat().st_size
            print(f"  [ok]      {rel}  ->  {destino.name}  ({tam:,} bytes)")
            ok += 1
        except Exception as exc:  # noqa: BLE001
            falhas.append((rel, str(exc)))
            print(f"  [falha]   {rel}: {exc}")

    print(f"\nGerados: {ok} | Ausentes: {len(ausentes)} | Falhas: {len(falhas)}")
    if ausentes:
        print("Fontes ainda não escritas: " + ", ".join(ausentes))
    return 1 if falhas else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
