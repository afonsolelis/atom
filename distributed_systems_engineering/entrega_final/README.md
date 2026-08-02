# Pacote de entrega — Distributed Systems Engineering

Data da consolidação: 1º de agosto de 2026

Este diretório reúne as cópias preenchidas dos modelos institucionais. Os originais recebidos permanecem imutáveis em `documentos/`; as apresentações solicitadas estão em HTML, dentro das pastas de cada unidade, e podem ser abertas pelo `index.html` deste diretório.

As pastas espelham a árvore dos originais recebidos em `documentos/`, inclusive os nomes irregulares das subpastas de validação, para que a coordenação receba o material na mesma organização em que o enviou.

```text
entrega_final/
├── index.html                        navegação dos 17 decks do pacote
├── assets/fullscreen-button.js       script carregado pelos decks
├── Instrumentos Avaliativos/
│   ├── Avaliação final_(10 discursivas)_Distributed Systems Engineering.docx
│   └── TEMPLATE ENTREGA DE TRABALHO - Distributed Systems Engineering.docx
├── Unidade 1/
│   ├── TEMPLATE - Unidade 1_Distributed Systems Engineering.docx
│   ├── 40 Questões - UNI1_Distributed Systems Engineering.docx
│   ├── SLIDES - Videoaulas Introdutória + 1 a 4/   aula0.html–aula4.html + assets/
│   └── Videoaula_ Introdutória + 1 a 4/
│       └── Videoaulas Introdutória + 1 a 4 - Validação - Distributed Systems Engineering.docx
├── Unidade 2/   … SLIDES - Videoaulas 5 a 8/ · Videoaulas 5 a 8/
├── Unidade 3/   … SLIDES - Videoaulas 9 a 12/ · Videoaula 9 a 12/
├── Unidade 4/   … SLIDES - Videoaulas 13 a 16/ · Videoaula 13 a 16/
├── MANIFESTO_SHA256.md
├── README.md
└── validacao_docx.json
```

O preenchimento segue o mesmo método adotado em `data_engineering_and_pipelines`: o modelo oficial em DOCX é aberto, cada caixa colorida recebe o conteúdo autoral correspondente, as orientações do modelo são removidas e o resultado é gravado como cópia. Nenhum arquivo de `documentos/` é alterado, e a estrutura, as caixas, a capa, o cabeçalho e os estilos institucionais são preservados.

## Inventário (14 DOCX + 17 decks + 1 relatório)

| Arquivo | Origem do conteúdo |
| --- | --- |
| `Unidade N/TEMPLATE - Unidade N_Distributed Systems Engineering.docx` (4) | `unidade_N/unidade_N.md` + `unidade_N/roteiros_20min.md` |
| `Unidade N/40 Questões - UNIn_Distributed Systems Engineering.docx` (4) | `unidade_N/questoes_uniN.md` |
| `Instrumentos Avaliativos/Avaliação final_(10 discursivas)_….docx` | `instrumentos_avaliativos/avaliacao_dissertativa.md` |
| `Instrumentos Avaliativos/TEMPLATE ENTREGA DE TRABALHO - ….docx` | `instrumentos_avaliativos/entrega_trabalho.md` |
| `Unidade N/<subpasta de validação>/Videoaulas … - Validação - ….docx` (4) | cópia sem alteração do modelo recebido |
| `Unidade N/SLIDES - Videoaulas …/aulaN.html` (17) | cópia dos decks de `unidade_N/slides/` |
| `validacao_docx.json` | relatório automatizado de `scripts/validar_entrega.py` |
| `MANIFESTO_SHA256.md` | hashes dos 14 DOCX e do relatório |

## Mapeamento das caixas dos modelos de unidade

| Caixa do modelo | Conteúdo inserido |
| --- | --- |
| Plano de Ensino - Unidade N | nota de governança: o plano oficial não integrava o pacote recebido |
| Relação da disciplina + Roteiro do vídeo introdutório | apenas na Unidade 1: relevância profissional + `roteiro_video_introdutorio.md` |
| TEXTO BASE AULA n | texto-base da aula; a primeira caixa de cada unidade abre com "O que você verá nesta unidade" e a última encerra com a "Síntese da unidade" |
| ROTEIRO VIDEOAULA n | roteiro falado completo; o cabeçalho da caixa recebe o título real do vídeo |
| QUIZ Não Avaliativo | linha 1 com as duas questões e alternativas; linha 2 com as devolutivas |
| AAI – Atividade avaliativa individual | apenas na Unidade 1, conforme o contrato; a caixa é removida nas demais |
| Direto da Fonte / Para Mergulhar / Podcast / Artigo científico | texto provocativo na primeira linha; referência, link, trecho obrigatório e aula indicada na segunda; referência ABNT na terceira, no artigo |

## Verificações automatizadas

Executadas por `scripts/validar_entrega.py` a cada geração; o resultado completo fica em `validacao_docx.json`.

- 14/14 DOCX reabertos com `python-docx` e aprovados no teste de integridade ZIP;
- quatro materiais didáticos com as Aulas 1–4, 5–8, 9–12 e 13–16 corretamente identificadas, sem caixa ausente nem caixa vazia;
- corpo dos materiais em Times New Roman 12, entrelinha 1,15, alinhamento à esquerda e sem espaçamento posterior; questionários e avaliações em Arial 12;
- quatro questionários com 40 questões, 200 alternativas, 40 gabaritos e 200 devolutivas cada, alternativa correta marcada com `*` imediatamente antes da letra e distribuição exata de 8 corretas por letra;
- avaliação final com 10 questões discursivas, respostas esperadas ao final e rubrica de 10 pontos por questão, sem nenhuma questão objetiva;
- trabalho PBL com as cinco caixas obrigatórias preenchidas, roteiro do estudante e fontes de pesquisa com link;
- nenhuma orientação, exemplo ou marcador de preenchimento do modelo remanescente;
- nenhuma sintaxe residual de Markdown ou LaTeX: as fórmulas foram convertidas para notação legível no Word;
- fichas de validação copiadas sem parecer, data ou responsável preenchidos — elas só podem ser assinadas após a gravação.

## Conteúdo verificado nas fontes

- 16 roteiros de videoaula entre 2.288 e 2.698 palavras faladas (aproximadamente 18 a 21 minutos), dentro da faixa de 2.200 a 2.700 palavras adotada para os 20 minutos, conferidos por `scripts/contar_palavras.py`;
- roteiro do vídeo introdutório com 225 palavras faladas, dentro do limite de 2 minutos;
- 16 textos-base entre 1.925 e 2.936 palavras, com 3 a 4 recursos visuais cada — numerados de forma contínua dentro de cada unidade, com descrição acessível;
- 17 decks HTML: vídeo introdutório e videoaulas 1 a 16, distribuídos nas pastas de slides de cada unidade e navegáveis pelo `index.html` do próprio pacote; as 52 referências locais dos decks foram conferidas após a cópia.

## Exceções e validações externas

- O modelo recebido da Unidade 2 repete internamente a Unidade 1. A cópia final preserva o desenho institucional e remapeia as caixas para as Aulas 5 a 8, corrigindo os rótulos "TEXTO BASE AULA 1–4" e "Plano de Ensino - Unidade 1". A coordenação deve ratificar a adaptação ou fornecer o modelo corrigido.
- O plano de aprendizagem oficial não veio no pacote. O conteúdo usa `PLANO_APRENDIZAGEM_PROPOSTO.md` como base provisória e ainda requer aprovação da coordenação.
- Os HTMLs seguem a identidade e a estrutura dos PPTX recebidos, mas a aceitação de HTML como formato institucional ainda deve ser confirmada. Nenhum PPTX original foi alterado.
- As versões mestras do trabalho e da avaliação contêm a parte do tutor. Antes de disponibilizá-las aos estudantes, devem ser exportadas cópias sem respostas, soluções ou rubricas internas.
- A duração efetiva das videoaulas deve ser confirmada em ensaio cronometrado; as gravações e a validação pós-gravação não fazem parte deste pacote.
- O teste institucional de similaridade no CopySpider e a aprovação formal do NEaD permanecem externos ao workspace.

## Regeneração do pacote

Com `python-docx` disponível, execute a partir da raiz da disciplina:

```bash
PYTHONPATH=/tmp/dse-docx-libs python3 scripts/montar_entrega.py
```

O comando recria a árvore de pastas, preenche os quatro modelos de unidade, os quatro questionários, a avaliação final e o trabalho PBL, copia as fichas de validação e os 17 decks, escreve o `index.html`, roda a validação estrutural e reescreve o manifesto. Etapas isoladas:

```bash
python3 scripts/preencher_docx.py 2           # só a Unidade 2
python3 scripts/preencher_instrumentos.py questoes
python3 scripts/validar_entrega.py
python3 scripts/contar_palavras.py            # palavras dos roteiros e das aulas
python3 scripts/inspecionar_docx.py <arquivo> # caixas de um DOCX, em ordem
```

Os geradores anteriores, que reconstruíam o corpo do documento em vez de preencher as caixas do modelo, estão preservados em `scripts/legado/` e não fazem mais parte do fluxo.
