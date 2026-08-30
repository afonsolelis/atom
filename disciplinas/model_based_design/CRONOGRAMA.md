# Cronograma de produção e validação

Disciplina: *Model-Based Design for Cyber-Physical Systems*
Professor-conteudista: Afonso Cesar Lelis Brandão

> **Prazo institucional:** não informado em nenhum dos três documentos recebidos. A coordenação precisa informá-lo. O cronograma abaixo organiza a produção por dependência técnica, não por data.

## Bloqueios comuns a todas as entregas

Estes itens dependem da coordenação e **não podem ser resolvidos pelo conteudista**:

1. Ratificação da divisão em 4 unidades e 16 videoaulas de 20 minutos — inferida dos quatro blocos da ementa, não informada em documento.
2. Ratificação da substituição ferramental por pilha aberta em Python, mantidos integralmente os conteúdos da ementa (ver `ANALISE_MATERIAIS_RECEBIDOS.md`, seção 4.2).
3. Fornecimento dos modelos institucionais DOCX (unidade, questionário, avaliação final, entrega de trabalho, slides), se existirem, ou confirmação de que a estrutura da variante TECH do Átomo 3.0 é aceita.
4. Confirmação da quantidade e da tipologia das questões (40 por unidade: 20 asserção-razão + 20 interpretação).
5. Confirmação do formato da avaliação final (10 dissertativas).
6. Informação da carga horária e do prazo de entrega.
7. Definição do padrão de slides.

Enquanto esses pontos não forem ratificados, todo o material produzido permanece identificado como **proposta do conteudista**, sem declaração de conformidade institucional.

## Fase 1 — Fundação documental

| Item | Estado |
| --- | --- |
| Verificação de integridade dos três documentos recebidos | Concluído |
| Análise crítica da ementa e registro dos conflitos | Concluído — `ANALISE_MATERIAIS_RECEBIDOS.md` |
| Plano de aprendizagem com 4 unidades e 16 aulas | Concluído — `PLANO_APRENDIZAGEM_PROPOSTO.md` |
| Diretrizes de produção | Concluído — `DIRETRIZES_PRODUCAO.md` |
| Definição e verificação da pilha tecnológica | Concluído — `AMBIENTE_E_STACK.md` |
| Definição do fio condutor (NexaBot) e conferência numérica em código | Concluído |

## Fase 2 — Laboratório executável

O laboratório precede o roteiro: nenhum comando entra em roteiro sem ter sido executado antes.

| Item | Estado |
| --- | --- |
| Pacote base (`params`, `plant`, `controllers`) com números conferidos | Concluído |
| Laboratórios das Aulas 1 a 7 | Ver `projeto_nexabot/aula_01`…`aula_07` |
| FMU FMI 3.0 e co-simulação (Aula 8) | Ver `projeto_nexabot/aula_08` |
| Supervisor, verificação formal e testes gerados (Aulas 9 a 12) | Ver `projeto_nexabot/aula_09`…`aula_12` |
| Geração de código, SIL, HIL e rastreabilidade (Aulas 13 a 16) | Ver `projeto_nexabot/aula_13`…`aula_16` |
| Suíte `pytest` completa | `projeto_nexabot/tests/` |
| Integração contínua | `projeto_nexabot/.github/workflows/` |

## Fase 3 — Material escrito

| Item | Estado |
| --- | --- |
| `unidade_1/unidade_1.md` (Aulas 1 a 4 + quiz + AAI + material complementar) | Concluído e validado |
| `unidade_2/unidade_2.md` (Aulas 5 a 8 + quiz + material complementar) | Concluído e validado |
| `unidade_3/unidade_3.md` (Aulas 9 a 12 + quiz + material complementar) | Concluído e validado |
| `unidade_4/unidade_4.md` (Aulas 13 a 16 + quiz + material complementar) | Concluído e validado |

## Fase 4 — Roteiros de gravação

| Item | Estado |
| --- | --- |
| `roteiro_video_introdutorio.md` (até 2 min) | Concluído — apenas apresentação; campos pessoais em branco para o professor |
| `unidade_1/roteiros_20min.md` (Videoaulas 1 a 4) | Concluído — 2.321 a 2.496 palavras faladas |
| `unidade_2/roteiros_20min.md` (Videoaulas 5 a 8) | Concluído — 2.435 a 2.697 palavras faladas |
| `unidade_3/roteiros_20min.md` (Videoaulas 9 a 12) | Concluído — 2.425 a 2.529 palavras faladas |
| `unidade_4/roteiros_20min.md` (Videoaulas 13 a 16) | Concluído — 2.202 a 2.409 palavras faladas |

## Fase 5 — Avaliação

| Item | Estado |
| --- | --- |
| `unidade_N/questoes_uniN.md` — 40 questões por unidade, 160 no total | Concluído — 8 respostas corretas por letra e 800 devolutivas |
| `instrumentos_avaliativos/avaliacao_dissertativa.md` — 10 dissertativas | Concluído — rubricas de 10 pontos por questão |
| `instrumentos_avaliativos/entrega_trabalho.md` — PBL | Concluído — versões estudante e tutor separadas na exportação |

## Fase 6 — Exportação no modelo institucional

A entrega sai **dentro dos modelos Word oficiais da UniFECAF** (Núcleo das Engenharias e Tecnologia), preservados em `tools/_templates_pristine/`. Os modelos são reaproveitados da disciplina irmã `data_engineering_and_pipelines`, do mesmo Núcleo e da mesma variante — inclusive a avaliação final de 10 discursivas, que coincide com o formato desta disciplina. Cada execução parte da cópia pristina, de modo que os scripts são reexecutáveis sem acumular resíduo.

| Item | Estado |
| --- | --- |
| `tools/preencher_unidades.py` — 4 unidades no modelo oficial | Concluído — caixas TEXTO BASE, ROTEIRO VIDEOAULA, QUIZ, AAI e material complementar preenchidas |
| `tools/preencher_questoes.py` — 4 questionários no modelo oficial | Concluído — 40 questões e 200 devolutivas por unidade |
| `tools/preencher_instrumentos.py` — avaliação final e trabalho PBL | Concluído — versões mestre e estudante |
| `tools/formulas.py` + `tools/render_formulas.js` — fórmulas como imagem | Concluído — 458 fórmulas renderizadas, nenhuma em branco |
| `tools/build_docx.py` — apenas documentos sem modelo institucional | Reduzido de escopo; saída isolada em `entrega_docx/_apoio_producao/` |

**Pacote institucional em `entrega_docx/` — 12 arquivos:** 4 unidades, 4 questionários, avaliação final (mestre e estudante) e entrega de trabalho (mestre e estudante).

**Apoio de produção em `entrega_docx/_apoio_producao/` — 10 arquivos:** plano de aprendizagem, diretrizes, análise dos materiais, ambiente, cronograma, roteiro do vídeo introdutório e os quatro cadernos de roteiros para leitura durante a gravação. Não possuem modelo institucional e por isso ficam separados, para não serem confundidos com a entrega.

### Escopo do vídeo introdutório

O vídeo introdutório e o deck `aula0` são **apenas apresentação**: quem é o professor e o que é a disciplina. Não há demonstração técnica, terminal, código nem simulação — a prática começa na Aula 1, que abre já com o ambiente na tela.

A gravação é integralmente em câmera cheia, sem captura de tela. O deck tem seis slides: capa, audiodescrição, "Sobre o professor", "O que é esta disciplina", o percurso das quatro unidades e o encerramento. A narração soma 225 palavras faladas, o que dá de 1 min 44 s a 1 min 57 s no ritmo de referência, deixando folga para as frases pessoais que o professor acrescentar nos campos em branco.

## Fase 7 — Decks de slides

Dezessete decks HTML autocontidos: `aula0` (vídeo introdutório) e `aula1` a `aula16`, com numeração contínua entre unidades, conforme a convenção do repositório.

| Item | Estado |
| --- | --- |
| `unidade_N/slides/aulaN.html` — 17 decks | Concluído |
| Padrão visual UniFECAF preservado (variáveis de `:root` intactas) | Conferido por comparação de hash entre os decks |
| Autocontenção (sem CDN, sem MathJax, sem recurso externo) | Conferido |
| Referências relativas resolvem no disco | Conferido arquivo a arquivo |
| `tools/validar_slides.py` | Concluído — 17 aprovados, 0 falhas |

**Correções aplicadas na revisão final:**

- Onze decks apontavam para `../../../assets/`, três níveis acima, quando a pasta `assets/` da raiz exige quatro. Todos os caminhos foram padronizados e verificados por resolução no sistema de arquivos.
- Dez arquivos intermediários de montagem (`_head13.html`, `_body14.html` e semelhantes) ficaram na pasta da Unidade 4 e foram removidos.
- Os decks das Unidades 1 e 2 tinham 10 slides e não traziam Sumário nem Objetivos de aprendizagem, ao contrário dos das Unidades 3 e 4. Foram nivelados para 15 a 18 slides.
- O deck `aula0`, do vídeo introdutório, não existia e foi criado.
- **O deck `aula5` continha o conteúdo do `aula9`** — título, tema de verificação formal e rodapé de outra unidade —, com apenas a tag `<title>` correta. Foi reescrito a partir do roteiro da Aula 5. Nenhuma checagem estrutural pegaria esse erro, então `validar_slides.py` passou a conferir se cada deck contém o título da própria videoaula e se o rodapé aponta para a unidade e a aula certas.
- O slide "Sobre o professor" aparecia em sete decks, em cinco deles sem os marcadores `[preencher: …]`. A convenção do repositório, conferida nas três disciplinas já migradas, é de um deck em dezessete: apenas o `aula0`. O slide foi concentrado ali, e é o único ponto de todo o material que contém informação pessoal — deixada em branco, para o professor preencher.

### Conferência executada sobre os 12 documentos institucionais

- Pacote ZIP íntegro e abertura sem erro em todos.
- Tabelas de uso exclusivo do coordenador idênticas às dos modelos pristinos.
- Caixa "Plano de Ensino" preservada com a instrução dirigida ao coordenador.
- Nenhum texto de orientação ao conteudista remanescente; nenhum campo `XXXX`.
- Nas versões do estudante, nenhuma resposta esperada, rubrica ou critério de correção; a caixa SOLUÇÃO do trabalho PBL é removida por inteiro, não apenas esvaziada.
- Sem asterisco de gabarito nas alternativas dos questionários; a resposta correta consta somente da seção de devolutivas.
- Paginação conferida por conversão a PDF, sem quebra indevida de caixa.

### Defeito no modelo da Unidade 2 e correção aplicada

O modelo `TEMPLATE - Unidade 2` recebido é uma **cópia do modelo da Unidade 1**, não um modelo próprio. Ele traz:

- o cabeçalho "Plano de Ensino - **Unidade 1**";
- as caixas rotuladas "TEXTO BASE AULA **1** a **4**" e "ROTEIRO VIDEOAULA **1** a **4**", quando a Unidade 2 cobre as Aulas 5 a 8;
- a caixa "Relação da disciplina com atuação profissional **+ Roteiro do vídeo introdutório**", sendo que o vídeo introdutório é único e pertence à Unidade 1.

Que a numeração contínua é a convenção pretendida fica provado pelos próprios modelos das Unidades 3 e 4, que trazem "AULA 9" a "AULA 12" e "AULA 13" a "AULA 16".

**Correção aplicada, apenas na cópia gerada:** os rótulos foram renumerados para AULA 5 a 8 e VIDEOAULA 5 a 8, o cabeçalho passou a "Plano de Ensino - Unidade 2", e a caixa de abertura passou a "Relação da unidade com atuação profissional". O modelo pristino permanece intacto em `tools/_templates_pristine/`. Sem essa correção, a Aula 5 sairia sob o rótulo "AULA 1", induzindo a coordenação e a equipe de edição ao erro.

A renumeração é **posicional**, e não textual: a k-ésima caixa de aula recebe o número correto. Substituição por texto corromperia as Unidades 3 e 4, porque "AULA 1" é prefixo de "AULA 10", "AULA 11" e "AULA 12".

**Pendência:** ratificar a correção dos rótulos, ou fornecer o modelo correto da Unidade 2.

### Inconsistência interna do modelo de questionário, sem impacto na entrega

O modelo de questionário determina, em seu texto de abertura, que "a pessoa conteudista deve elaborar **40 questões**". Logo abaixo, ao detalhar a distribuição, ele lista "10 questões do tipo asserção-razão" e "10 de interpretação", que somam 20 — inconsistência do próprio modelo, herdada de uma versão anterior.

A entrega segue o número principal do modelo, que coincide com o contrato desta disciplina: **40 questões por unidade, 20 de asserção-razão e 20 de interpretação**. As duas linhas inconsistentes foram removidas junto com o restante das orientações, como o próprio modelo determina, de modo que nenhum texto do documento final contradiz o conteúdo entregue. Não há decisão pendente de coordenação neste ponto.

## Checklist operacional antes de cada gravação

- [ ] Executar o ensaio cronometrado de cada um dos 16 roteiros e ajustar o que exceder 20 minutos.
- [x] Executar uma vez todos os scripts da disciplina, conferindo a saída (realizado na revisão final; repetir apenas os da aula antes da tomada).
- [ ] Executar o CopySpider e arquivar o relatório de similaridade (limite institucional de 3%).
- [x] Decks sem fotografia pessoal; não há autorização de imagem pendente.

## Critério de conclusão

O pacote de conteúdo está concluído quando as Fases 1 a 6 passam em `tools/validar.py`, a suíte de código passa e os 22 DOCX passam em `tools/validar_docx.py`. Ensaio com a voz real, CopySpider e ratificação institucional continuam sendo controles externos à autoria do material e devem ser registrados antes da publicação definitiva.
