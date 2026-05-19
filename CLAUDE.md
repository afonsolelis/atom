# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

This is a **content-authoring repo for Brazilian higher-education disciplines** (engenharia civil + IA), not a software project. The "code" is Markdown coursework that gets compiled to PDFs. All content is in **pt-BR**. The author / professor is **Afonso Cesar Lelis Brandão** — that name is the default `professor` field everywhere.

Each top-level directory (other than `base/` and `Originais - Átomo 3.0/`) is one discipline. Disciplines follow one of three layouts:

- **Átomo 3.0** (`industria_4_0_e_digitalizacao_de_processos/`, `sistemas_de_informacao_automacao_e_ia_aplicada_a_producao/`): the current Ânima/Átomo 3.0 template — `unidade_N/unidade_N.md` (texto + roteiros + quiz + AAI + material complementar inline) + `unidade_N/questoes_uniN.md` + a shared `instrumentos_avaliativos/` folder with `avaliacao_final.md` and `entrega_trabalho.md`. **Use this layout for any new discipline.**
- **Unit-based (legacy)** (`Estruturas_de_Concreto_Pilares_e_Solicitacoes_Dinamicas/`, `nova_disciplina/`): older layout — 4 units, each with `unidade_N_conteudo.md` + four `unidade_N_i_aula.md` + `questoes_unidade_N.md`.
- **Aula-based** (`estrutura_pontes/`, `engenharia_de_prompt_a_mentalidade_de_ia_e_o_conhecimento_digital/`): 16 individual `aulaN.md` files in `aulas/` plus parallel `roteiros/`, `questoes/`, `m_complementar/` directories. 16 aulas = 4 units × 4 aulas, but flattened.

The folder `Originais - Átomo 3.0/` holds the **canonical Word templates** from Ânima (TEMPLATE de unidade, Questões UNI1–4, Avaliação final, Entrega de trabalho, slides, guia de vídeo). It is the source of truth for the Átomo 3.0 layout — the markdown files in the new disciplines are 1:1 derivations of those `.docx` templates. Don't edit the `.docx` files; edit the markdown.

**This folder is `.gitignore`d** (174MB of binary institutional templates, kept only locally). The relevant content has already been extracted: textual templates → markdown in the new disciplines; branding images → `assets/originais_atomo_3_0/`.

When asked to author or modify content in legacy disciplines, always check the discipline's `DIRETRIZES_DISCIPLINA.json` / `DIRETRIZES_UNIDADE.json` first — those JSON files are the source of truth for the legacy layouts. The Átomo 3.0 disciplines don't have a DIRETRIZES JSON; the rules live in this file and in the `Originais - Átomo 3.0/` Word templates.

## Authoring rules (read these before writing content)

Rules below apply to all layouts unless marked otherwise. Legacy disciplines additionally follow their `DIRETRIZES_*.json`; Átomo 3.0 disciplines follow the structure of the Word templates in `Originais - Átomo 3.0/`.

- **Per aula**: 700–1200 words, 6–10 subsections, 1–3 images (Wikimedia/Wikipedia, with descriptive alt text), at least one numeric example, a practical activity, 3–5 pontos-chave bullets, and 2–4 supplementary links.
- **Math**: LaTeX only, with `$…$` for inline and `$` on its own line for block. **Never use code fences for math** — `build_pdfs.py` rewrites lone-`$` lines to `$$` for pandoc.
- **Images**: prefer Wikimedia Commons; format `![alt descritivo](URL)`. Local assets live in `<unidade>/assets/` (and `assets/downloads/` for files fetched by `normalize_images.py`).
- **Questões file (legacy)**: exactly 20 MC items, 5 alternatives each (`a.` through `e.`), correct one prefixed with `*` (e.g. `*c. …`), followed by a `## Feedbacks` section with one numbered explanation per question. Distribute the correct letter evenly across a-e (4× each in a 20-question set; see `how_to_create_questions.json`).
- **Questões file (Átomo 3.0)**: 20 questões padrão ENADE — **10 asserção-razão + 10 interpretação**, 5 alternativas cada (a–e), correta com `*`, feedbacks ao final.
- **Avaliação final (legacy)**: 30 questões total — 10 múltipla escolha + 10 asserção-razão + 10 interpretação. Same `*` marker, feedbacks at the bottom. See `template_avaliacao_final.md`.
- **Avaliação final (Átomo 3.0)**: **40 questões** padrão ENADE — **15 asserção-razão + 15 interpretação + 10 discursivas** (discursivas vão ao final). Objetivas com 5 alternativas, correta prefixada por `*`. Feedbacks das objetivas ao final. The 10 discursivas are reflected in the file name `Avaliação final_(30 questões múltipla escolha + 10 discursivas)` — 30 MC = 15 AR + 15 interpretação.
- **Entrega de trabalho (Átomo 3.0)**: PBL case com 5 seções obrigatórias — Título, Desafio, Fontes de pesquisa (≥4), Entregável + distribuição da pontuação, Solução (removida antes de entregar ao aluno) — mais o Roteiro do Estudante.
- **Material complementar**: 4 fixed sections — *Direto da Fonte* (BV / Brightspace livro), *Para Mergulhar* (filme/série/livro/blog), *Podcast* (**must be YouTube**), *Artigo científico* (DOI + ABNT).

`estrutura_pontes/diretrizes_latex.json` adds discipline-specific conventions: use `\mathrm{}` + thin space (`\,`) for units (`15\,\mathrm{kN}`), vírgula decimal (`{,}` in LaTeX), and standard sign conventions (`+` tração, `+` sagging). It also expects an `aulaN_ponte.svg` per aula. `engenharia_de_prompt/.../directions.json` removes "Objetivos"/time markers and expects an `aulaN_prompt_flow.svg` diagram instead.

## Common commands

All commands assume you `cd` into the discipline first.

```powershell
# Build PDFs for every unidade_*/*.md in a unit-based discipline
cd Estruturas_de_Concreto_Pilares_e_Solicitacoes_Dinamicas
python tools/build_pdfs.py                # outputs to pdfs/unidade_N/*.pdf

# Download remote images locally and convert SVG/GIF/WebP → PNG so pandoc finds them
python tools/normalize_images.py          # run before build_pdfs.py if links are new

# Upload assets to Cloudinary and rewrite markdown links (estrutura_pontes only)
cd estrutura_pontes
python scripts/cloudinary_upload_and_replace.py   # needs CLOUDINARY_* env vars
```

`build_pdfs.py` requires **pandoc + xelatex** with the DejaVu Serif font (falls back to default if missing). It looks for assets via a resource-path that includes `<md_dir>` and `<md_dir>/assets`, so keep images relative to the markdown file. `normalize_images.py` shells out to `curl` and ImageMagick `convert`.

## Commit conventions

This repo uses Conventional Commits with a custom scope list defined in `commit-guidelines.json`:

- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.
- Scopes: `base`, `unidade_1`–`unidade_4`, `instrumentos_avaliativos`, `estrutura_pontes`, `industria_4_0`, `sistemas_informacao`.
- Format: `^(\w+)(\(\w+\))?: (\w+.*)$` — e.g. `feat(unidade_1): add new exercise about bridge calculations`.

Existing commits on `main` are short (`"ok"`, `"docs: adicionar materiais complementares (unidades 1–4)"`) — don't be afraid of terse messages, but stick to the format for anything non-trivial.

## When asked to "create a new unit" or "create a new aula"

### Legacy layout (Estruturas_de_Concreto, nova_disciplina)

The workflow in `DIRETRIZES_UNIDADE.json` is canonical. Summarized:

1. Collect the 4 aula titles for the unit.
2. Create `<disciplina>/unidade_N/` and write `unidade_N_conteudo.md` first (header, texto-base inicial, all 4 aulas inline, avaliações, material complementar).
3. Copy each aula's section into its own `unidade_N_i_aula.md` (i = 1..4).
4. Write `questoes_unidade_N.md` (20 questions + feedbacks).
5. Validate against `validacao_checklist` in the diretrizes JSON.

Use `unidade_2/unidade_2_1_aula.md` of `Estruturas_de_Concreto_Pilares_e_Solicitacoes_Dinamicas/` as the reference for depth and pacing — the diretrizes explicitly name it as the model.

### Átomo 3.0 layout (industria_4_0, sistemas_de_informacao)

Single file per unit; 4 aulas inline. Each unit's `unidade_N.md` already has scaffolding with placeholders — fill in:

1. Header (disciplina name is already set; conteudista defaults to Afonso Cesar Lelis Brandão).
2. **Unit 1 only**: "Vídeo introdutório + Relação da disciplina com a atuação profissional" + roteiro.
3. For each aula (4 per unit, videoaulas numbered 1–16 across the discipline): texto base (700–1200 words) + roteiro da videoaula. Aulas have specificities — Aula 1 of each unit opens the unit, Aula 3 has a "Pausa para Reflexão"/Desafio, Aula 4 of units 1–3 previews the next unit, Aula 4 of unit 4 closes the discipline.
4. Quiz não avaliativo (2 questões) + AAI (1 questão dissertativa + resposta esperada).
5. Material complementar — 4 fixed sections.
6. Sibling `questoes_uniN.md` — 20 questões (10 AR + 10 interpretação) + feedbacks.
7. After all 4 units, fill `instrumentos_avaliativos/avaliacao_final.md` (40 questões) and `entrega_trabalho.md` (PBL case).

Videoaula numbering: U1 = 1–4, U2 = 5–8, U3 = 9–12, U4 = 13–16.

## Templates

- `Originais - Átomo 3.0/` — **canonical Word templates** from Ânima (current Átomo 3.0 layout). Source of truth for the new disciplines.
- `template_unidade.json` — legacy schema for a full unit (use as a checklist of fields).
- `template_avaliacao_final.md` — example of the 30-question (legacy) final exam format (delete the sample items before writing real ones).
- `how_to_create_questions.json` — question-formatting rules including the balanced-letter-distribution requirement.
