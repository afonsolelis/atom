#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Preenche o template institucional Word (UniFECAF / Núcleo das Engenharias e
Tecnologia) da AVALIAÇÃO FINAL no padrão Átomo 3.0 — "30 questões múltipla
escolha + 10 discursivas" — a partir de
instrumentos_avaliativos/avaliacao_final.md.

Este é o mesmo padrão adotado em `disciplinas/portos_aeroportos_e_ferrovias/`:
40 questões no total, sendo 15 de asserção-razão (1–15), 15 de interpretação
(16–30) e 10 discursivas (31–40, ao final), com feedback para cada uma das 5
alternativas das 30 objetivas, inseridos ao final do documento — exatamente
como o texto de orientação do próprio modelo determina.

- Preserva a tabela do coordenador (INTOCÁVEL).
- Preenche Disciplina / Professor-conteudista.
- Remove as orientações e os exemplos do modelo (tudo após a linha
  "Professor-conteudista:"), conforme a instrução "Exclusão de Exemplos".
- A alternativa correta é marcada com asterisco imediatamente antes da letra
  (`*a. …`), como o modelo institucional exige textualmente.
- Documento único, como o modelo prevê: as respostas esperadas das discursivas
  e os feedbacks das objetivas vão ao final.

Sempre parte do backup pristine em tools/_templates_pristine/ e escreve em
entrega_docx/, sobrescrevendo a cada execução.

Uso:
    tools/.venv/bin/python tools/preencher_avaliacao_final.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from docx import Document

sys.path.insert(0, str(Path(__file__).resolve().parent))
import docx_comum as dc

SECOES = [
    "Questões objetivas (1–30) e discursivas (31–40)",
    "Questões discursivas (31–40)",
    "Feedbacks (questões objetivas 1–30)",
]


def fill() -> dict:
    template_name = (
        f"Avaliação final_(30 questões múltipla escolha + 10 discursivas)_"
        f"{dc.DISCIPLINA_ARQUIVO}.docx"
    )
    pristine = dc.PRISTINE / template_name
    md_path = dc.DISC / "instrumentos_avaliativos" / "avaliacao_final.md"
    out_path = dc.SAIDA / template_name

    if not pristine.exists():
        print(f"  ! template não encontrado: {pristine}")
        return {}
    if not md_path.exists():
        print(f"  ! markdown não encontrado: {md_path}")
        return {}

    md_text = md_path.read_text(encoding="utf-8")
    print("  renderizando fórmulas da avaliação final...")
    formula_index = dc.build_formula_index(md_text)
    stats = dc.new_stats()

    doc = Document(pristine)

    dc.set_placeholder(doc, ("disciplina:",), dc.DISCIPLINA)
    dc.set_placeholder(doc, ("professor-conteudista:",), dc.CONTEUDISTA)

    removed = dc.cut_body_after(
        doc, lambda t: t.strip().lower().startswith("professor-conteudista"),
        keep_matched=True,
    )

    secoes = dc.sections_dict(md_text)
    faltando = [s for s in SECOES if secoes.get(s) is None]
    if faltando:
        print(f"  ! seções não encontradas no markdown: {faltando}")
        return {}

    for titulo in SECOES:
        p = dc.new_para(doc)
        dc.style_run(p.add_run(titulo), bold=True)
        dc.render_blocks(doc, secoes[titulo], formula_index, stats,
                         first=False, alts=True)

    dc.unlock_rows_and_breaks(doc)
    dc.SAIDA.mkdir(parents=True, exist_ok=True)
    doc.save(out_path)

    corpo = md_text.split("## Feedbacks")[0]
    n_obj = len(re.findall(r"(?m)^### Questão \d+ \((?:Asserção-Razão|Interpretação)\)", corpo))
    n_dis = len(re.findall(r"(?m)^### Questão \d+ \(Discursiva\)", corpo))
    n_fb = len(re.findall(r"(?m)^- \*\*[a-e]\.\*\*", md_text.split("## Feedbacks")[1]))

    print(f"  OK -> {out_path.name}  (par. orientação/exemplo removidos: {removed}; "
          f"objetivas: {n_obj}; discursivas: {n_dis}; feedbacks: {n_fb}; "
          f"fórmulas: {dc.stats_total_imagens(stats)} ok / {len(stats['faltantes'])} faltantes)")
    if stats["faltantes"]:
        print("     fórmulas ausentes do índice (entraram como texto):",
              stats["faltantes"][:5], "..." if len(stats["faltantes"]) > 5 else "")

    return {"path": out_path, "pristine": pristine, "n_obj": n_obj,
            "n_dis": n_dis, "n_fb": n_fb, "stats": stats}


def main():
    print("AVALIAÇÃO FINAL (30 objetivas + 10 discursivas):", dc.DISCIPLINA)
    print("-" * 60)
    r = fill()
    print("-" * 60)
    print("Pronto.")
    return r


if __name__ == "__main__":
    main()
