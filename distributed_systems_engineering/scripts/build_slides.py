#!/usr/bin/env python3
"""Regera o bloco de slides dos decks HTML da disciplina.

Preserva o `<head>` (CSS + símbolos SVG) e o `<script>` de navegação de cada arquivo:
apenas o bloco `<div class="deck" id="deck">…</div>` é substituído. Os decks continuam
sendo HTML autocontido — este script é uma ferramenta de autoria, não de build.

    python3 scripts/build_slides.py            # regera todos os decks disponíveis
    python3 scripts/build_slides.py 1 2 3      # regera apenas as aulas indicadas
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from slides_kit import RAIZ, escrever  # noqa: E402

DECKS: dict[int, str] = {}

try:
    import slides_intro
    DECKS[0] = slides_intro.A0
except ImportError:
    pass

for modulo, aulas in (
    ("slides_u1", (1, 2, 3, 4)),
    ("slides_u2", (5, 6, 7, 8)),
    ("slides_u3", (9, 10, 11, 12)),
    ("slides_u4", (13, 14, 15, 16)),
):
    try:
        mod = __import__(modulo)
    except ImportError:
        continue
    for aula in aulas:
        corpo = getattr(mod, f"A{aula}", None)
        if corpo:
            DECKS[aula] = corpo


def caminho(aula: int) -> Path:
    unidade = 1 if aula == 0 else (aula - 1) // 4 + 1
    return RAIZ / f"unidade_{unidade}" / "slides" / f"aula{aula}.html"


def main(argv: list[str]) -> int:
    alvos = [int(a) for a in argv] if argv else sorted(DECKS)
    faltando = [a for a in alvos if a not in DECKS]
    if faltando:
        print(f"sem conteúdo definido para: {faltando}", file=sys.stderr)
    for aula in alvos:
        if aula not in DECKS:
            continue
        destino = caminho(aula)
        total = escrever(destino, DECKS[aula])
        print(f"aula{aula:>2} → {destino.relative_to(RAIZ)}  ({total} slides autorais)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
