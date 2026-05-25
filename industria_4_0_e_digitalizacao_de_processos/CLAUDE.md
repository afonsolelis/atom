# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Scope

This is **one discipline** inside the larger `atom/` content-authoring repo — the cross-cutting rules (Átomo 3.0 layout, authoring conventions, math/image/question formatting, commit scopes, slide template) live in [../CLAUDE.md](../CLAUDE.md). Read that first. This file only covers what is specific to **Indústria 4.0 e Digitalização de Processos**.

## What this discipline is

A pt-BR graduation course for Brazilian engenharia de produção students, authored by **Afonso Cesar Lelis Brandão**, following the **Átomo 3.0** layout. The "code" is Markdown coursework + self-contained HTML slide decks — there is **no build tooling here** (no `tools/`, no `scripts/`); the markdown is the deliverable as-is.

Content is already fully drafted (see commit `e5a64f6 feat(industria_4_0): preenche todo o conteúdo da disciplina`). Most edits from here will be **revisions, not new authoring**.

## Discipline structure

16 videoaulas across 4 units, with the canonical Átomo 3.0 numbering (U1 = 1–4, U2 = 5–8, U3 = 9–12, U4 = 13–16):

- [unidade_1/](unidade_1/) — **Fundamentos e Contexto Histórico** — revoluções industriais (1ª→4ª), 9 pilares, sistemas ciber-físicos (CPS) + digital twin, maturidade digital.
- [unidade_2/](unidade_2/) — **Tecnologias Habilitadoras** — IIoT, Big Data/Analytics, Cloud + Edge, IA/ML no chão de fábrica.
- [unidade_3/](unidade_3/) — **Aplicações e Digitalização de Processos** — manufatura aditiva + simulação, robótica colaborativa (cobots), RA/VR, cibersegurança industrial (OT vs IT).
- [unidade_4/](unidade_4/) — **Implementação, Casos e Futuro** — BPM + digitalização, roadmap de implementação, casos reais BR/mundo, Indústria 5.0.

Each `unidade_N/unidade_N.md` follows the Átomo 3.0 scaffold: vídeo introdutório (U1 only), 4 aulas (texto base + roteiro da videoaula), Quiz não avaliativo, AAI, Material complementar. Sibling `questoes_uniN.md` carries the 20 ENADE questions (10 AR + 10 interpretação).

## Slides

Each aula has a deck at `unidade_N/slides/aulaK.html`, where **K is the continuous videoaula number 1–16** (U1: aula1–aula4, U2: aula5–aula8, U3: aula9–aula12, U4: aula13–aula16) — already created from [../assets/template_apresentacao/index.html](../assets/template_apresentacao/index.html). Decks are single-file HTML (UniFECAF identity: `--azul-fecaf #002057`, `--amarelo #F0CE29`). The professor photo at `unidade_N/slides/assets/foto-professor.jpg` is shared across units.

## Final assessments

- [instrumentos_avaliativos/avaliacao_final.md](instrumentos_avaliativos/avaliacao_final.md) — 40 questões (15 AR + 15 interpretação + **10 discursivas ao final**).
- [instrumentos_avaliativos/entrega_trabalho.md](instrumentos_avaliativos/entrega_trabalho.md) — PBL case da **Metalúrgica Sigma** (Sorocaba-SP, 620 funcionários, R$ 280M faturamento). Cenário: roadmap de transformação digital de 18 meses, orçamento R$ 3M, baseline OEE 67% / paradas não programadas 145h-mês / DPPM 3.800. Mantenha esses números consistentes se editar qualquer parte do case — eles são referenciados ao longo do enunciado.

## Commit scope

Use `industria_4_0` as the conventional-commits scope for changes anywhere under this directory (see [../commit-guidelines.json](../commit-guidelines.json)).
