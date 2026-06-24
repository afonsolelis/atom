---
name: revisar-disciplina
description: |
  Revisão e correção de conteúdo de qualquer disciplina deste repo (Átomo 3.0,
  legacy unit-based ou aula-based). Verifica correção técnica/factual, conformidade
  estrutural com o template, LaTeX/matemática, decks HTML (sem MathJax), questões,
  imagens e material complementar. Use quando pedirem para "revisar", "corrigir",
  "validar" ou "conferir" uma unidade, aula, disciplina ou deck de slides.
user-invocable: true
argument-hint: "[caminho da disciplina/unidade/aula a revisar]"
---

# Revisar / Corrigir Disciplina

Skill de revisão de conteúdo didático em pt-BR. O objetivo é encontrar e corrigir
**erros técnicos**, **quebras de formatação** e **desvios do template** em qualquer
disciplina do repo — exatamente a classe de problemas que o commit de melhorias da
disciplina `portos_aeroportos_e_ferrovias` tratou (correção de massa do TR-68,
carga por eixo, LaTeX literal fora de `$...$`, LaTeX em decks sem MathJax, etc.).

A skill **não** é só validação: ela aponta o problema, propõe a correção e (quando
autorizada) aplica a edição no markdown/HTML. Nunca edita os `.docx` em
`Originais - Átomo 3.0/`.

## Passo 0 — Identificar o alvo e o layout

A partir do argumento (caminho de disciplina, unidade, aula ou deck), determine o
**layout** da disciplina — as regras mudam conforme ele:

| Layout | Como reconhecer | Arquivos a revisar |
| --- | --- | --- |
| **Átomo 3.0** | tem `unidade_N/unidade_N.md` + `questoes_uniN.md` + `instrumentos_avaliativos/` | `unidade_N.md`, `questoes_uniN.md`, `slides/aulaN.html`, `avaliacao_final.md`, `entrega_trabalho.md` |
| **Legacy unit-based** | tem `unidade_N_conteudo.md` + `unidade_N_i_aula.md` + `DIRETRIZES_*.json` | os `.md` da unidade + `questoes_unidade_N.md` |
| **Aula-based** | tem `aulas/aulaN.md` + `roteiros/` + `questoes/` + `m_complementar/` | `aulaN.md` e parceiros + `*.svg` |

Para os layouts **legacy/aula-based**, leia primeiro o `DIRETRIZES_DISCIPLINA.json` /
`DIRETRIZES_UNIDADE.json` / `diretrizes_latex.json` / `directions.json` da disciplina —
eles são a fonte de verdade e podem sobrepor as regras gerais abaixo. Para **Átomo 3.0**
não há JSON; as regras vêm do `CLAUDE.md` e dos templates Word em `Originais - Átomo 3.0/`.

Ignore sempre o scaffolding `AIOX` (`.aiox-core/`, `.antigravity/`, `.claude/` dentro
das disciplinas) — não é conteúdo.

## Eixos de revisão

Rode os eixos abaixo. Para cada achado, registre: **arquivo:linha**, **categoria**,
**severidade** (🔴 erro factual / quebra de render · 🟡 desvio de template · 🔵 melhoria)
e a **correção proposta**.

### 1. Correção técnica / factual (🔴 prioridade máxima)

É o eixo mais importante e o que exige leitura atenta, não regex. Procure por:

- **Valores numéricos errados ou improváveis.** Confira grandezas de engenharia
  contra a realidade brasileira/normas. Exemplos reais do commit:
  - massa linear de trilho TR-68 = **67,4 kg/m** (não 33,8); a regra "TR-XX ≈ XX kg/m"
    vale para a nomenclatura brasileira.
  - carga por eixo ferroviária no Brasil = **25 a 32,5 t/eixo** (40 t é atípico).
  - conferir unidades e ordens de grandeza (largura de pista código 4 ≈ 45 m,
    envergadura A380 ≈ 80 m, etc.).
- **Afirmações que se contradizem** entre markdown, tabela, SVG e deck da mesma aula
  (um valor corrigido num arquivo e esquecido em outro). Sempre cheque o mesmo dado
  em **todos** os arquivos da aula (md + slide + svg).
- **Referências normativas plausíveis e específicas** (ASTM, AREMA, UIC/EN, OACI/ICAO
  Anexo, RBAC, ABNT, NBR, DNIT). Quando citar norma, citar o número certo.
- **Exemplo numérico**: refazer a conta. O resultado bate? As unidades fecham?

Quando tiver dúvida factual e a tarefa permitir, **verifique** (WebSearch/WebFetch ou
fontes do material complementar) antes de "corrigir" — não troque um número certo por
um errado. Se não puder verificar, marque como 🟡 "checar" em vez de editar.

### 2. Matemática / LaTeX (🔴 quebra de render)

Regras do `build_pdfs.py` + convenções de `diretrizes_latex.json`:

- Inline com `$…$`; bloco com `$` sozinho na linha. **Nunca** cercar matemática em
  code fences (```).
- **Bug clássico — LaTeX literal fora de `$...$`:** comandos como `\,`, `\mathrm{}`,
  `\geq`, `\leq`, `^{\circ}`, `\times`, `\approx`, frações `7%/300\,\mathrm{m}`
  aparecendo como **texto cru** no corpo. Ou se embrulha em `$...$`, ou se converte
  para texto plano ("7% por 300 m"). Busque por `\mathrm`, `\,`, `\geq`, `\circ`,
  `\times`, `\approx`, `\leq` **fora** de `$...$`.
- Unidades: `\mathrm{}` + espaço fino `\,` (ex.: `15\,\mathrm{kN}`, `1{,}435\,\mathrm{m}`).
- Decimal com vírgula via `{,}` no LaTeX (ex.: `0{,}5`, não `0.5`).
- `$...$` desbalanceado (número ímpar de `$` numa linha/parágrafo) → render quebra.

### 3. Decks HTML — slides (🔴 os decks NÃO têm MathJax)

Este é o eixo mais traiçoeiro. Os `slides/aulaN.html` são single-file e **não
renderizam LaTeX**. Logo:

- **Nenhum comando LaTeX pode aparecer no HTML do slide.** `\mathrm`, `\,`, `m^2`,
  `^{\circ}`, `\geq`, `$...$` viram lixo na tela. Tudo deve estar em **unicode/HTML**:
  `m²`, `°C`, `≥`, `≤`, `×`, `→`, `≈`, `³`, frações com `½`/`⁄` ou texto. (O commit
  converteu ~47 desses spans na U3.) Busque `\` e `$` dentro dos `.html` de `slides/`.
- Os valores técnicos do slide devem **bater com o markdown corrigido** da mesma aula.
- Estrutura UniFECAF: capa com mosaicos, slide **Audiodescrição** após a capa,
  "Sobre o professor", triângulos grandes e esparsos (não o padrão pequeno repetido),
  cartão azul + título verde-claro. Variáveis `--azul-fecaf #002057` e `--amarelo #F0CE29`
  no `:root`. Logo institucional carrega de URL hasheada — se 404, atualizar `href`.

### 4. Estrutura / conformidade com o template (🟡)

**Por aula** (todos os layouts): 700–1200 palavras, 6–10 subseções, 1–3 imagens com
alt descritivo, ≥1 exemplo numérico, 1 atividade prática, 3–5 pontos-chave, 2–4 links
complementares.

**Átomo 3.0** — por unidade: 4 aulas inline (videoaulas 1–16: U1=1–4, U2=5–8, U3=9–12,
U4=13–16), roteiro por videoaula, quiz não avaliativo (2 questões), AAI (1 dissertativa
+ resposta esperada), material complementar (4 seções fixas). U1 abre com vídeo
introdutório; Aula 3 tem "Pausa para Reflexão"/Desafio; Aula 4 das U1–U3 prevê a próxima
unidade; Aula 4 da U4 encerra a disciplina.

**Material complementar** — 4 seções fixas: *Direto da Fonte* (BV/Brightspace),
*Para Mergulhar* (filme/série/livro/blog), *Podcast* (**tem de ser YouTube**),
*Artigo científico* (DOI + ABNT).

**Legacy/aula-based**: validar contra o `validacao_checklist` do `DIRETRIZES_*.json`.

### 5. Questões (🟡/🔴)

- **Átomo 3.0** (`questoes_uniN.md`): 20 questões — **10 asserção-razão + 10
  interpretação**, 5 alternativas (a–e), correta prefixada por `*`, `## Feedbacks` ao final.
- **Avaliação final Átomo 3.0**: 40 questões — 15 AR + 15 interpretação + 10 discursivas
  (discursivas ao final).
- **Legacy** (`questoes_unidade_N.md`): 20 MC, 5 alternativas, `*` na correta, feedbacks;
  **distribuição balanceada** do gabarito (4× cada letra a–e num conjunto de 20 — ver
  `how_to_create_questions.json`).
- Verificar: exatamente uma alternativa marcada com `*` por questão; nº de feedbacks =
  nº de questões; nenhuma alternativa duplicada; enunciado coerente com o gabarito.

### 6. Imagens / assets (🟡)

- Formato `![alt descritivo](URL)`; alt **descritivo** (não "imagem"/"figura").
- Preferir Wikimedia Commons; assets locais em `<unidade>/assets/` (e `assets/downloads/`).
- SVGs cotados devem ter o desenho coerente com o texto (mesma grandeza/valor) e alt
  que descreva o que está cotado.
- Links devem resolver; rodar `normalize_images.py` antes do build se houver links novos.

## Saída

1. **Relatório** agrupado por eixo e severidade, cada item como
   `arquivo:linha — [severidade] categoria: problema → correção`.
2. Se o usuário pediu **correção** (não só revisão), aplique os 🔴 e 🟡 de baixo risco
   via Edit, mantendo o estilo do texto vizinho; deixe os 🔵 e os factuais incertos como
   sugestão para o usuário aprovar.
3. **Não** rode build nem commit a menos que pedido. Se editar, lembre que Átomo 3.0 não
   tem tooling (markdown é o entregável) e que decks exportam PDF via Chrome Print.

## Commit (só se solicitado)

Conventional Commits com escopo de `commit-guidelines.json`. Escopos válidos: `base`,
`unidade_1`–`unidade_4`, `instrumentos_avaliativos`, `estrutura_pontes`, `industria_4_0`,
`sistemas_informacao` (use o escopo da disciplina/unidade). Encerrar a mensagem com a
linha `Co-Authored-By` exigida pelo harness.
