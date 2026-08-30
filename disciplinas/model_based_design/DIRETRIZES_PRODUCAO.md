# Diretrizes de produção — Model-Based Design for Cyber-Physical Systems

> **Fonte de verdade desta disciplina.** Este arquivo, junto com `PLANO_APRENDIZAGEM_PROPOSTO.md`, precede o `CLAUDE.md` da raiz do repositório em qualquer divergência de layout. Os requisitos aqui consolidados vêm de dois documentos recebidos: a ementa oficial (`MODEL_BASED_DESIGN_FOR_CYBER_PHYSICAL_SYSTEMS.docx`) e as diretrizes de gravação do Núcleo das Engenharias e Tecnologia (`orientacoes_gravacao_EAD.pdf`), complementadas pelo e-mail de encaminhamento (`direcionamentos.md`).

## 1. Requisitos recebidos e como foram atendidos

### Do e-mail de encaminhamento

| # | Requisito informado | Decisão de produção |
| --- | --- | --- |
| 1 | Tempo mínimo de vídeo: 12 a 18 minutos, podendo exceder com aplicação prática | Adotados **20 minutos** por videoaula, conforme determinação posterior do responsável, com narração dimensionada em 2.200 a 2.700 palavras faladas |
| 2 | Não gravar em estúdio; usar OBS Studio, Loom ou similar com captura de tela e câmera | Todo o material foi desenhado para captura de tela: cada aula tem um laboratório executável em `projeto_nexabot/aula_NN/` |
| 3 | Conteúdo 100% conectado ao mercado de 2026 | Pilha aberta atual: Python 3.12, `uv`, `python-control` 0.10, FMI 3.0, Hypothesis, PlatformIO/ESP32, GitHub Actions |
| 4 | Modelo hands-on real: menos teoria solta, mais prática | Toda aula abre com a ferramenta em execução; a teoria entra como explicação do que está na tela |
| 5 | Aula prática desde os primeiros minutos | Bloco 00:00–02:00 sempre com terminal ou editor ativo |
| 6 | Construção do básico ao avançado | Progressão em quatro camadas: modelar (U1), controlar (U2), provar (U3), embarcar (U4) |
| 7 | Ritmo dinâmico e metodologia ativa | Situação-problema por aula, erro real demonstrado e corrigido, desafio ao final |
| 8 | Padrão visual limpo e profissional | Saída de terminal em tabela ASCII, fonte ampliada, sem janelas gráficas obrigatórias |
| 9 | Uso de ferramentas, cases, desafios e aplicações reais | Fio condutor único (NexaBot) e casos automotivo, aeroespacial e de robótica na Aula 16 |

### Das diretrizes de gravação do Núcleo

| Diretriz | Como o material a cumpre |
| --- | --- |
| Analisar criticamente a ementa e propor ajustes | Seção "Adequações propostas à ementa oficial" em `PLANO_APRENDIZAGEM_PROPOSTO.md`, com tabela de correspondência ferramental. Nenhum tópico da ementa foi removido |
| Roteiro claro, objetivo e dinâmico | Roteiros com mapa de tempo por bloco, marcações de troca de tela e narração pronta para leitura |
| Metodologia ativa e foco em atenção | Situação-problema, erro deliberado e correção, pausa para reflexão, desafio final |
| Prática desde o início | Nenhuma aula abre por definição conceitual |
| Progressão do básico ao avançado | Aula 1 instala o ambiente; Aula 16 monta matriz de rastreabilidade e discute certificação |
| Tela limpa, legível, com fonte e contraste ajustados | Checklist de gravação na seção 6 |
| Conteúdo atualizado para 2026 | Versões fixadas e verificadas em `AMBIENTE_E_STACK.md` |
| Prática guiada e desafio final | Todo laboratório termina em `NN_desafio.py`, com enunciado e critério de aceitação |
| Comunicação profissional, direta e segura | Registro de exposição técnica contínua, sem oralidade informal e sem floreio |
| Apresentação pessoal em no máximo 2 minutos | Vídeo introdutório roteirizado separadamente, com limite de 2 minutos |

## 2. Estrutura de arquivos da disciplina

```
disciplinas/model_based_design/
├── MODEL_BASED_DESIGN_FOR_CYBER_PHYSICAL_SYSTEMS.docx   (recebido, não editar)
├── orientacoes_gravacao_EAD.pdf                          (recebido, não editar)
├── direcionamentos.md                                    (recebido, não editar)
├── PLANO_APRENDIZAGEM_PROPOSTO.md
├── DIRETRIZES_PRODUCAO.md
├── ANALISE_MATERIAIS_RECEBIDOS.md
├── AMBIENTE_E_STACK.md
├── CRONOGRAMA.md
├── roteiro_video_introdutorio.md
├── unidade_1/  unidade_1.md · roteiros_20min.md · questoes_uni1.md
├── unidade_2/  unidade_2.md · roteiros_20min.md · questoes_uni2.md
├── unidade_3/  unidade_3.md · roteiros_20min.md · questoes_uni3.md
├── unidade_4/  unidade_4.md · roteiros_20min.md · questoes_uni4.md
├── instrumentos_avaliativos/
│   ├── avaliacao_dissertativa.md
│   └── entrega_trabalho.md
├── projeto_nexabot/            laboratório executável, um diretório por aula
└── entrega_docx/               exportações institucionais geradas por tools/build_docx.py
```

O layout segue a **variante TECH do Átomo 3.0**, a mesma de `disciplinas/distributed_systems_engineering/`: um arquivo por unidade, roteiros em arquivo irmão, 40 questões por unidade e avaliação final exclusivamente dissertativa.

## 3. Estrutura de cada `unidade_N.md`

1. Cabeçalho: disciplina, unidade, professor-conteudista.
2. Relação da unidade com a atuação profissional.
3. "O que você verá nesta unidade" (apenas na primeira aula de cada unidade, dentro do arquivo da unidade).
4. Quatro aulas completas, cada uma com:
   - situação-problema de abertura;
   - texto base de 700 a 1.200 palavras por aula, em seções curtas;
   - pelo menos um exemplo numérico completo, com os números do NexaBot;
   - laboratório prático correspondente em `projeto_nexabot/aula_NN/`;
   - "Pausa para reflexão" ou desafio na terceira aula da unidade;
   - transição para a unidade seguinte na quarta aula (fechamento da disciplina na Aula 16);
   - síntese da aula com 3 a 6 pontos-chave;
   - referência ao roteiro da videoaula correspondente;
   - referências da aula.
5. Quiz não avaliativo com duas questões e devolutiva conceitual.
6. Atividade Avaliativa Individual (AAI) — **somente na Unidade 1**, com enunciado dissertativo e resposta esperada.
7. Síntese da unidade.
8. Material complementar em quatro seções fixas: *Direto da Fonte*, *Para Mergulhar no Assunto*, *Podcast* (obrigatoriamente YouTube), *Artigo científico* (com DOI e referência ABNT).
9. Referências da unidade, em ABNT NBR 6023:2018.

Recursos visuais aparecem como blocos descritivos para a equipe de edição, no formato:

```
> **Recurso visual N — Título.** Descrição do que deve ser produzido.
> *Texto alternativo:* descrição acessível completa.
```

De 3 a 5 recursos visuais por aula.

## 4. Estrutura de cada `roteiros_20min.md`

Um arquivo por unidade, contendo os quatro roteiros das videoaulas daquela unidade. Cada roteiro contém:

- título da videoaula e vínculo com o plano de aprendizagem;
- objetivo da videoaula;
- mapa de tempo e de telas;
- narração contínua, pronta para leitura, dividida em blocos com marcação `**[mm:ss–mm:ss · Tela N — Descrição]**`;
- comandos exatos a digitar e saída esperada, quando o bloco for de demonstração;
- indicações de edição e recursos visuais;
- fontes e licenças de qualquer mídia externa.

**Dimensionamento:** 2.200 a 2.700 palavras faladas por roteiro, a um ritmo de 115 a 130 palavras por minuto. Títulos, marcações de tempo, comandos, saídas de terminal e indicações de edição não contam nesse total.

**Diferença em relação a uma disciplina expositiva:** esta é uma disciplina de captura de tela. Cada roteiro alterna entre blocos de **[SLIDE]** e blocos de **[TELA: terminal]** ou **[TELA: editor]**, e todo bloco de tela traz o comando literal e um resumo da saída que aparecerá. O professor não improvisa o que digita.

## 5. Estrutura dos questionários

- 40 questões por unidade: 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
- Cinco alternativas por questão, de `a.` a `e.`, com a correta prefixada por `*`.
- Distribuição equilibrada da letra correta: 8 questões por letra no conjunto de 40.
- Devolutiva para **todas** as alternativas, não apenas para a correta.
- As questões de interpretação devem apresentar cenário, dado numérico ou trecho de código do NexaBot e exigir análise, não memorização.

## 6. Checklist de gravação (por aula)

- [ ] Terminal em fonte grande, tema de alto contraste, prompt curto, diretório da aula já aberto.
- [ ] Ambiente virtual ativado e verificado com `aula_01/01_ambiente.py`.
- [ ] Scripts da aula executados uma vez antes de gravar, para conferir a saída.
- [ ] Saída longa filtrada; nada de rolagem ilegível.
- [ ] Nenhuma credencial, caminho pessoal ou aba particular na tela.
- [ ] Câmera enquadrada, iluminação sem contraluz.
- [ ] Marcação de erro deliberado ensaiada: o erro precisa aparecer e ser corrigido na mesma tomada, quando previsto no roteiro.
- [ ] Duração cronometrada em ensaio antes da gravação definitiva.

## 7. Regras de conteúdo

- Português do Brasil em todo o material, incluindo comentários e saídas dos scripts.
- Estrangeirismos em itálico, exceto siglas, marcas, nomes próprios e trechos de código.
- Matemática em LaTeX: `$…$` para linha e `$` isolado para bloco. Nunca dentro de cerca de código.
- Referências em ABNT NBR 6023:2018.
- Todo número citado no material escrito e nos roteiros deve ser reproduzível por um script de `projeto_nexabot/`. Número que não roda não entra.
- Honestidade técnica é requisito: o pipeline aberto **produz evidências**, não certifica. Confiança e eventual qualificação de ferramentas dependem do uso, do impacto de erro e da capacidade de detecção posterior — não da licença aberta ou comercial.

## 8. Versões do estudante e do tutor

- A avaliação final dissertativa e o trabalho PBL são arquivos-mestres, com Parte A (estudante) e Parte B (tutor).
- Respostas esperadas, soluções e rubricas nunca podem permanecer no arquivo distribuído ao estudante.
- A exportação para distribuição deve cortar o arquivo antes do início da Parte B.

## 9. Formatos

- Fonte editável de produção: Markdown.
- Entrega institucional: DOCX gerado por `tools/build_docx.py`, com corpo em Times New Roman 12, espaçamento 1,15, alinhamento à esquerda.
- Laboratórios: código Python e C versionado em `projeto_nexabot/`.

## 10. Lista de verificação antes da entrega

- [x] Ementa oficial analisada criticamente e adequações registradas e justificadas.
- [x] Plano de aprendizagem com 4 unidades e 16 aulas de 20 minutos.
- [x] Fio condutor prático único, com parâmetros numéricos verificados em código.
- [x] Quatro arquivos de unidade completos.
- [x] Dezesseis roteiros de 20 minutos dimensionados e com comandos literais.
- [x] Roteiro do vídeo introdutório de até 2 minutos.
- [x] Cento e sessenta questões, com devolutiva para todas as alternativas.
- [x] Avaliação final com 10 dissertativas, respostas esperadas e critérios.
- [x] Trabalho PBL com Parte A e Parte B delimitadas.
- [x] Laboratório executável de todas as 16 aulas, com saída conferida.
- [x] Exportação DOCX gerada e conferida.
- [ ] Ensaio cronometrado de cada roteiro.
- [ ] Relatório de similaridade (CopySpider) arquivado.
- [ ] Validação da coordenação registrada.
