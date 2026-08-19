---
name: project-slide-review
description: Structure and known quirks of the 16 Indústria 4.0 HTML slide decks, for content review
metadata:
  type: project
---

Disciplina Indústria 4.0: 16 self-contained HTML decks at `unidade_N/slides/aulaK.html`, K = continuous videoaula number 1–16 (U1: aula1–4, U2: aula5–8, U3: aula9–12, U4: aula13–16).

**Why:** Decks are reviewed for pedagogical content BEFORE videoaula recording. PO reviews, @dev fixes.

**How to apply:**
- Content lives only in `<section class="slide">` bodies; the CSS/SVG boilerplate (~440 lines) is identical across decks — extract text with `awk '/<div class="deck"/{p=1} /<nav class="nav"/{p=0} p'` + strip tags.
- Known intra-deck numbering quirk: U2–U4 divider numbers and footers label aulas as "01–04 / Aula 1–4" *within the unit* while the footer also shows the continuous "Videoaula 5–16". U1 uses continuous 01–04 in dividers. This is by design (videoaula number is the cross-deck key), not necessarily a bug — flag only if it confuses.
- Numeric examples (aula2 IIoT ROI, aula5 rede dimensioning, aula6 bebidas analytics, aula7 edge banda) are all arithmetically consistent — verified 2026-06-07.
- Reference case Metalúrgica Sigma (PBL) is in `instrumentos_avaliativos/`, NOT in slides.
