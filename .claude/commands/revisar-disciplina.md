---
description: Revisa e corrige conteúdo de qualquer disciplina (técnica, LaTeX, decks, questões, template)
argument-hint: "[caminho da disciplina/unidade/aula] [--apenas-revisar | --corrigir]"
---

Revise e corrija o conteúdo em `$ARGUMENTS` usando a skill **revisar-disciplina**.

Se nenhum caminho for passado, revise as alterações ainda não commitadas
(`git status` / `git diff`). Se vier `--apenas-revisar`, só produza o relatório de
achados sem editar; se vier `--corrigir` (ou nada), aplique as correções de severidade
🔴 e 🟡-baixo-risco e deixe o resto como sugestão.

Siga os seis eixos da skill, **nesta ordem de prioridade**:

1. **Correção técnica/factual** — valores numéricos, unidades, normas, exemplos
   refeitos, e coerência do mesmo dado entre markdown + slide + SVG da aula. Não troque
   um número certo por um errado: se não puder verificar, marque "checar" em vez de editar.
2. **LaTeX/matemática** — comandos (`\mathrm`, `\,`, `\geq`, `^{\circ}`, `\times`...)
   vazando fora de `$...$`; code fences em volta de math; `$` desbalanceado; vírgula
   decimal `{,}`; unidades com `\mathrm{}`+`\,`.
3. **Decks HTML** (`slides/aulaN.html`) — **não têm MathJax**: nenhum LaTeX ou `$` pode
   sobrar; tudo em unicode/HTML (`m²`, `°C`, `≥`, `×`, `→`). Valores devem bater com o
   markdown corrigido.
4. **Estrutura/template** — contagens (700–1200 palavras, 6–10 subseções, pontos-chave,
   links), seções obrigatórias, material complementar (4 seções, podcast = YouTube),
   numeração de videoaulas. Para legacy/aula-based, leia o `DIRETRIZES_*.json` antes.
5. **Questões** — contagem e tipos por layout, marcador `*` único por questão,
   nº feedbacks = nº questões, distribuição balanceada do gabarito (legacy).
6. **Imagens/assets** — alt descritivo, Wikimedia/local em `assets/`, links resolvem.

Comece detectando o **layout** da disciplina (Átomo 3.0 / legacy / aula-based) — as
regras mudam conforme ele. Nunca edite os `.docx` de `Originais - Átomo 3.0/` nem o
scaffolding AIOX (`.aiox-core/`, `.claude/` dentro das disciplinas).

Entregue um **relatório agrupado por eixo e severidade** (`arquivo:linha — [sev]
categoria: problema → correção`) e, ao final, um resumo do que foi corrigido vs. o que
ficou pendente de decisão do usuário. Não rode build nem commit a menos que eu peça.
