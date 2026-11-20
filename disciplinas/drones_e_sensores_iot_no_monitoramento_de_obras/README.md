# Drones e Sensores IoT no Monitoramento de Obras

- **Professor-conteudista:** Afonso Cesar Lelis Brandão
- **Layout:** Átomo 3.0 (mesmo padrão de `disciplinas/portos_aeroportos_e_ferrovias/`)
- **Escopo de commit:** `drones_iot`
- **Status:** disciplina completa e **adequada aos templates da pasta do Google Drive** enviada pelo NEaD (e-mail de Carolina Bastos, 20/11/2026). Plano de aulas validado com o coordenador (Osvaldo). Entrega em **.docx** gerada em `entrega_docx/` a partir dos templates originais; apresentações em **HTML** (`unidade_N/slides/`). Pendente apenas: "Direto da fonte" (livro da Biblioteca Virtual) das 4 unidades.

## Fonte de verdade: pasta do Google Drive (NEaD)

- Pasta da disciplina: `Originais - Átomo 3.0/` → `Unidade 1–4/` (TEMPLATE de unidade + Questões UNI*N* + pasta de videoaulas com o documento de validação) e `Instrumentos Avaliativos/` (Avaliação final 30 + 10 e TEMPLATE ENTREGA DE TRABALHO).
- Os templates foram baixados **sem alteração** para `tools/_templates_pristine/` (mesmos tamanhos em bytes do Drive). O `.docx` final é sempre gerado a partir deles.
- **Pacote contratado:** 4 templates + 80 questões + 1 vídeo introdutório + 16 videoaulas + 1 trabalho + 1 avaliação final (30 objetivas + 10 discursivas).
- **Prazos:** 10/01/2027 — Unidades 1 e 2 (template + 20 questões cada), vídeo introdutório, videoaulas 1–8 e Trabalho; 25/01/2027 — Unidades 3 e 4, videoaulas 9–16 e Avaliação final.
- **Gravação:** obrigatoriamente em estúdio ou laboratório da faculdade (em casa só com autorização e aula-teste aprovada).

### Regras do template do Drive aplicadas (diferenças em relação ao Átomo 3.0 antigo)

- **Sem AAI** — o template atual da unidade não tem a caixa "Atividade Verificadora / AAI" (removida das 4 unidades).
- **3 a 5 imagens por aula**, com direitos que permitam reprodução (Wikimedia Commons/CC), indicadas entre colchetes com link de referência e texto alternativo.
- Aula 1 da unidade abre com **"O que você verá nesta unidade"**; Aula 3 tem **"Pausa para reflexão"**; Aula 4 traz **"O que você verá na próxima unidade"** (na Unidade 4, o encerramento da disciplina).
- Roteiro de videoaula **sintético**, com **título que gere curiosidade**; o texto base fica com a teoria e o vídeo, com a aplicação prática.
- Quiz: 2 questões + resposta com explicação. Material complementar com os campos do template (Nome do livro / Capítulo / Link de acesso; Links; NOME DO PODCAST / NOME DO EPISÓDIO / Link; Link + Referência ABNT) e **"Qual aula o material deverá entrar?"** em cada um.
- Questões: alternativas `a)`–`e)`, correta com `*`, e **feedback para cada alternativa** ao final (`N. Feedback`).
- Avaliação final: 15 AR + 15 interpretação + 10 discursivas (no fim); os feedbacks — inclusive a resposta esperada das discursivas — ficam **ao final**.
- Trabalho (PBL): só as caixas do template — Título, Desafio, Fonte de pesquisa (≥ 4 fontes + aulas), 5. Entregável e distribuição da pontuação, 6. Solução. (O antigo "Roteiro do Estudante" não existe no template e saiu.)
- Formatação no .docx: Times New Roman 12, espaçamento 1,15, alinhado à esquerda, sem recuo.

## Estrutura

```
unidade_N/unidade_N.md        texto base + roteiros sintéticos + quiz + material complementar
unidade_N/roteiros_15min.md    roteiros estendidos (fala integral, apoio à gravação)
unidade_N/questoes_uniN.md     20 questões (10 AR + 10 interpretação) + feedbacks
unidade_N/slides/aulaN.html    decks UniFECAF (aula0 + aula1–aula16, numeração contínua)
assets/                        deck.css, deck.js, sprite.js (padrão UniFECAF) + obra.css/obra.js (fotos, 3D, simulações) — ver assets/README_DECKS.md
tools/                         gerar_docx.py (preenche os templates do Drive → entrega_docx/), wikimedia.py (fotos), capturar_slides.py (PNG por slide), validar.py N (checagem estrutural)
entrega_docx/                  ENTREGÁVEIS .docx (4 templates de unidade, Questões UNI1–4, Avaliação final, Entrega de trabalho)
instrumentos_avaliativos/      avaliacao_final.md (30 objetivas + 10 discursivas) + entrega_trabalho.md (PBL)
```

## Plano de aulas (validado com a coordenação)

### Unidade 1 — Fundamentos do Monitoramento Digital de Obras

1. Monitoramento de obras na era digital: do diário de obra ao canteiro conectado
2. Fundamentos de sensoriamento: grandezas, transdutores, incerteza e calibração
3. Arquiteturas IoT para o canteiro: dispositivos, conectividade e nuvem
4. Drones (RPA): tipos, componentes, cargas úteis e regulamentação brasileira

### Unidade 2 — Drones: Aquisição e Processamento de Dados

5. Planejamento de voo: GSD, sobreposição, altura e plano de missão
6. Fotogrametria com drones: SfM, pontos de controle, RTK/PPK e precisão
7. Produtos cartográficos: ortomosaico, MDS/MDT, nuvem de pontos e cálculo de volumes
8. LiDAR embarcado e termografia na inspeção de estruturas e fachadas

### Unidade 3 — Sensores IoT no Monitoramento de Obras

9. Monitoramento geotécnico: inclinômetros, piezômetros e marcos de recalque
10. Monitoramento estrutural: extensômetros, acelerômetros, fissurômetros e maturidade do concreto
11. Segurança, ambiente e produtividade: vibração, ruído, poeira e rastreamento de equipamentos
12. Dados de sensores: séries temporais, níveis de alerta e dashboards

### Unidade 4 — Integração, Inteligência e Gestão do Monitoramento

13. Integração com BIM e gêmeo digital: 4D e comparação as-built × as-designed
14. IA e visão computacional: detecção de fissuras e medição de avanço físico
15. Gestão do monitoramento: custo-benefício, LGPD, segurança da informação e contratos
16. Projeto integrado de monitoramento de uma obra (fechamento da disciplina)

## Pendências

- [ ] Seção "Direto da fonte" (livro da Biblioteca Virtual) de cada unidade — escolher o livro e o capítulo na BV (acesso "BV professor", credenciais no próprio template do Drive)
- [ ] Confirmar a gravação (estúdio ou casa) com o NEaD e agendar o estúdio
- [ ] Subir os .docx de `entrega_docx/` na pasta do Drive (só quando autorizado)
- [x] Plano de aulas validado com o coordenador
- [x] Formato confirmado: Átomo 3.0 padrão (20 questões/unidade; avaliação final 30 + 10)
- [x] Prazos (10/01/2027 e 25/01/2027)
- [x] Adequação aos templates do Drive e geração dos .docx
- [x] Decks aula0–aula16 e `index.html` do portal

## Como gerar os .docx

```bash
cd disciplinas/drones_e_sensores_iot_no_monitoramento_de_obras
(cd tools && npm install)        # mathjax-full, para as fórmulas (uma vez)
pip install python-docx pillow cairosvg
python3 tools/gerar_docx.py      # ou: unidades | questoes | avaliacao | trabalho
```

## Referências normativas a considerar (validar na produção)

- ANAC — RBAC nº 100 (Resolução nº 805/2026, substituiu o RBAC-E nº 94; categorias aberta/específica/certificada) e cadastro SISANT
- DECEA — ICA 100-40, edição 2026 (acesso ao espaço aéreo por aeronaves não tripuladas) e sistema SARPAS
- ANATEL — homologação de radiotransmissores (drones e dispositivos IoT)
- ABNT NBR 9653 (vibrações por desmonte de rocha), NBR 16747 (inspeção predial)
- LGPD (Lei 13.709/2018) — imagens e dados de trabalhadores e vizinhança
