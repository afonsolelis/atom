#!/usr/bin/env python3
"""Constrói os notebooks passo a passo das dezesseis aulas.

Cada aula tem um arquivo-fonte em `tools/notebooks/aula_NN.py` que declara as
células como uma lista de `md(...)` e `code(...)`. Este módulo transforma essa
lista num `.ipynb` válido em `notebooks/`.

Por que gerar em vez de editar o `.ipynb` direto: JSON de notebook é ilegível
em diff, e o conteúdo destes notebooks é sobretudo texto didático, que precisa
ser revisado como texto. O arquivo-fonte é o que se revisa; o `.ipynb` é o
artefato.

Uso:
    python3 tools/nbkit.py            # constrói todos
    python3 tools/nbkit.py 1 2        # constrói só as aulas 1 e 2
    python3 tools/nbkit.py --check    # valida sem escrever
"""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FONTES = RAIZ / "tools" / "notebooks"


def _destino(n: int) -> Path:
    """O notebook mora na pasta da unidade a que a aula pertence.

    A convenção é a mesma dos slides: `unidade_N/slides/aulaN.html` e
    `unidade_N/notebooks/aula_NN_*.ipynb`. As aulas se distribuem 1-4 na
    Unidade 1, 5-8 na 2, 9-12 na 3 e 13-16 na 4.
    """
    unidade = (n - 1) // 4 + 1
    return RAIZ / f"unidade_{unidade}" / "notebooks"


# --------------------------------------------------------------- células

def md(texto: str) -> dict:
    """Célula de texto. Recebe Markdown já escrito em português."""
    return {"tipo": "markdown", "fonte": texto}


def code(fonte: str) -> dict:
    """Célula de código Python."""
    return {"tipo": "code", "fonte": fonte}


# ------------------------------------------------------------ construção

def _linhas(texto: str) -> list[str]:
    """Quebra o texto no formato que o `.ipynb` espera: uma string por linha,
    com `\\n` no fim de todas menos a última."""
    texto = texto.strip("\n")
    partes = texto.split("\n")
    return [p + "\n" for p in partes[:-1]] + [partes[-1]]


def montar(celulas: list[dict], titulo: str) -> dict:
    saida = []
    for c in celulas:
        if c["tipo"] == "markdown":
            saida.append({
                "cell_type": "markdown",
                "metadata": {},
                "source": _linhas(c["fonte"]),
            })
        else:
            saida.append({
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": _linhas(c["fonte"]),
            })
    return {
        "cells": saida,
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (NexaBot)",
                "language": "python",
                "name": "python3",
            },
            "language_info": {"name": "python", "version": "3.12"},
            "title": titulo,
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def carregar_fonte(n: int):
    caminho = FONTES / f"aula_{n:02d}.py"
    if not caminho.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"aula_{n:02d}", caminho)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


# ------------------------------------------------------------- validação

def validar(nb: dict, rotulo: str) -> list[str]:
    """Confere o que quebra o notebook antes de o aluno abrir."""
    erros = []
    celulas = nb["cells"]

    if not celulas or celulas[0]["cell_type"] != "markdown":
        erros.append(f"{rotulo}: primeira célula precisa ser de texto")

    # todo código precisa compilar
    for i, c in enumerate(celulas):
        if c["cell_type"] != "code":
            continue
        fonte = "".join(c["source"])
        try:
            compile(fonte, f"{rotulo}[célula {i + 1}]", "exec")
        except SyntaxError as e:
            erros.append(f"{rotulo}: célula {i + 1} não compila — {e.msg} (linha {e.lineno})")

    # o padrão pedagógico exige as seções fixas
    texto = "\n".join("".join(c["source"]) for c in celulas if c["cell_type"] == "markdown")
    for marca, rotulo_secao in (
        ("## O que você vai fazer aqui", "O que você vai fazer aqui"),
        ("## Antes de começar", "Antes de começar"),
        ("## Mexa aqui", "Mexa aqui"),
        ("## Se deu erro", "Se deu erro"),
    ):
        if marca not in texto:
            erros.append(f"{rotulo}: falta a seção '{rotulo_secao}'")

    # toda célula de código precisa de texto explicando antes
    for i, c in enumerate(celulas):
        if c["cell_type"] == "code" and i > 0 and celulas[i - 1]["cell_type"] == "code":
            fonte_ant = "".join(celulas[i - 1]["source"]).strip()
            # duas células de código seguidas só passam se a anterior for curta
            # (import ou continuação óbvia)
            if len(fonte_ant.splitlines()) > 3:
                erros.append(
                    f"{rotulo}: célula {i + 1} vem depois de outra célula de código "
                    "sem texto explicando — o padrão exige explicação antes de rodar"
                )
    return erros


# ------------------------------------------------------------------ main

def main(argv: list[str]) -> int:
    apenas_checar = "--check" in argv
    pedidas = [int(a) for a in argv if a.isdigit()]
    alvos = pedidas or list(range(1, 17))

    erros: list[str] = []
    feitos = 0
    ausentes = []

    for n in alvos:
        mod = carregar_fonte(n)
        if mod is None:
            ausentes.append(n)
            continue
        nb = montar(mod.CELULAS, mod.TITULO)
        rotulo = f"aula_{n:02d}"
        erros += validar(nb, rotulo)
        pasta = _destino(n)
        pasta.mkdir(parents=True, exist_ok=True)
        destino = pasta / f"{rotulo}_{mod.SLUG}.ipynb"
        if not apenas_checar:
            destino.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + "\n",
                               encoding="utf-8")
        n_code = sum(1 for c in nb["cells"] if c["cell_type"] == "code")
        rel = destino.relative_to(RAIZ)
        print(f"  {rel}: {len(nb['cells'])} células ({n_code} de código)")
        feitos += 1

    print()
    if ausentes:
        print(f"Ainda sem fonte: aulas {', '.join(str(a) for a in ausentes)}")
    if erros:
        print("FALHAS:")
        for e in erros:
            print(f"  [FALHA] {e}")
        return 1
    print(f"{feitos} notebook(s) construído(s), sem falhas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
