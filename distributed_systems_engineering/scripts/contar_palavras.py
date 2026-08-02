#!/usr/bin/env python3
"""Conta palavras faladas de cada roteiro e palavras de texto-base de cada aula.

Uso:
    python3 scripts/contar_palavras.py            # relatório completo
    python3 scripts/contar_palavras.py roteiros   # só os 16 roteiros
    python3 scripts/contar_palavras.py aulas      # só os textos-base

Palavra falada = texto de narração das seções narrativas do roteiro, excluindo
títulos, blocos de vínculo/objetivo, marcações de edição entre colchetes e as
seções "Indicações de edição e recursos visuais" e "Fontes e links de mídia".
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Faixa adotada: videoaulas de 20 minutos; narração de 2.200 a 2.700 palavras.
ROTEIRO_MIN, ROTEIRO_MAX = 2200, 2700
PALAVRAS_POR_MINUTO = 125

SECOES_NAO_FALADAS = {
    "Indicações de edição e recursos visuais",
    "Fontes e links de mídia",
    "Fontes",
}


def palavras_faladas(bloco: str) -> int:
    faladas: list[str] = []
    secao = None
    for linha in bloco.split("\n"):
        texto = linha.strip()
        cabecalho = re.match(r"^#{2,6}\s+(.*)$", texto)
        if cabecalho:
            secao = cabecalho.group(1)
            continue
        if not texto or secao in SECOES_NAO_FALADAS:
            continue
        if texto.startswith(("*[", "**", "-", "|", ">", "```")):
            continue
        faladas.append(texto)
    return len(" ".join(faladas).split())


def relatorio_roteiros() -> int:
    problemas = 0
    for unidade in range(1, 5):
        caminho = ROOT / f"unidade_{unidade}" / "roteiros_20min.md"
        blocos = re.split(r"^##\s+", caminho.read_text(encoding="utf-8"), flags=re.M)[1:]
        print(f"--- Unidade {unidade} — {len(blocos)} roteiros ---")
        for bloco in blocos:
            titulo = bloco.split("\n")[0]
            total = palavras_faladas(bloco)
            dentro = ROTEIRO_MIN <= total <= ROTEIRO_MAX
            problemas += 0 if dentro else 1
            marca = "ok " if dentro else "FORA"
            print(
                f"  [{marca}] {titulo[:56]:56s} {total:5d} palavras "
                f"(~{total / PALAVRAS_POR_MINUTO:.1f} min)"
            )
    return problemas


def relatorio_aulas() -> int:
    total_geral = 0
    aulas = 0
    for unidade in range(1, 5):
        caminho = ROOT / f"unidade_{unidade}" / f"unidade_{unidade}.md"
        texto = caminho.read_text(encoding="utf-8")
        print(f"--- Unidade {unidade} ---")
        for bloco in re.split(r"^##\s+", texto, flags=re.M)[1:]:
            titulo = bloco.split("\n")[0]
            if not titulo.startswith("Aula"):
                continue
            corpo = re.split(r"^###\s+Roteiro da Videoaula", bloco, flags=re.M)[0]
            total = len(corpo.split())
            recursos = len(re.findall(r"\*\*Recurso visual \d+", bloco))
            total_geral += total
            aulas += 1
            print(f"  {titulo[:56]:56s} {total:5d} palavras | {recursos} recursos visuais")
    print(f"\ntexto-base das {aulas} aulas: {total_geral} palavras (média {total_geral // aulas})")
    return 0


def main() -> int:
    alvo = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    fora = 0
    if alvo in ("tudo", "roteiros"):
        fora += relatorio_roteiros()
    if alvo in ("tudo", "aulas"):
        if alvo == "tudo":
            print()
        relatorio_aulas()
    if fora:
        print(f"\n{fora} roteiro(s) fora da faixa de {ROTEIRO_MIN} a {ROTEIRO_MAX} palavras faladas.")
    return 1 if fora else 0


if __name__ == "__main__":
    raise SystemExit(main())
