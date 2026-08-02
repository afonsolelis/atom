# Distributed Systems Engineering

Produção de conteúdo EAD do NEaD.

- Professor-conteudista: Afonso Cesar Lelis Brandão
- Coordenação indicada no e-mail: Osvaldo
- Acompanhamento da produção: Carolina Bastos
- Contato sobre videoaulas: Maico Pereira Gomes
- Valor informado para o pacote: R$ 6.000,00
- Situação em 1º de agosto de 2026: as fontes de trabalho em Markdown, os 17 decks em HTML, os 16 roteiros de 20 minutos sincronizados slide a slide com os decks, os 34 arquivos institucionais originais e **14 cópias DOCX preenchidas** estão presentes. As cópias ficam em `entrega_final/` e não alteram os originais. O material **ainda não constitui entrega institucional validada**: permanecem pendentes a aprovação do plano e do conteúdo pelo NEaD, a decisão sobre o formato dos slides, os ensaios cronometrados, as versões seguras de distribuição ao estudante, a validação pós-gravação e as gravações.

## Escopo informado

- 4 modelos de unidade;
- 160 questões, sendo 40 por unidade;
- 1 vídeo introdutório;
- 16 videoaulas, sendo 4 por unidade;
- 1 trabalho;
- 1 avaliação final com 10 questões dissertativas.

## Estrutura de arquivos

```text
distributed_systems_engineering/
├── README.md
├── index.html
├── ANALISE_MATERIAIS_RECEBIDOS.md
├── CRONOGRAMA.md
├── DIRETRIZES_PRODUCAO.md
├── PLANO_APRENDIZAGEM_PROPOSTO.md
├── RECURSOS_VISUAIS.md
├── roteiro_video_introdutorio.md
├── assets/fullscreen-button.js
├── documentos/  (34 modelos e guias institucionais de referência)
├── entrega_final/  (pacote preenchido, espelhando as pastas de `documentos/`;
│                    ainda não validado pela coordenação)
├── instrumentos_avaliativos/
│   ├── entrega_trabalho.md
│   └── avaliacao_dissertativa.md
├── materiais_recebidos/
│   └── README.md
├── scripts/  (preenchimento dos modelos DOCX, validação e contagem de palavras)
├── unidade_1/
│   ├── unidade_1.md
│   ├── questoes_uni1.md
│   ├── roteiros_20min.md
│   └── slides/aula0.html–aula4.html
├── unidade_2/  (aula5.html–aula8.html)
├── unidade_3/  (aula9.html–aula12.html)
└── unidade_4/  (aula13.html–aula16.html)
```

Abra `index.html` para acessar o protótipo da apresentação introdutória e das 16 aulas. Os decks funcionam com os arquivos locais do projeto. Eles foram produzidos em HTML com base em uma referência interna de outro projeto; **não há, neste repositório, aprovação do NEaD para substituir os modelos PPTX por HTML**. A autoria, a licença e o inventário declarado dos recursos didáticos estão em `RECURSOS_VISUAIS.md`.

Os 17 HTMLs foram verificados em seis dimensões de viewport: 1.608 estados de slide/aba, além de 30 estados com reflexões expandidas, foram exercitados sem erro JavaScript nem *overflow* não rolável, e as verificações de links, identificadores, ARIA e SVG passaram. Nenhum PPTX novo foi gerado; os 16 PPTX oficiais permanecem imutáveis em `documentos/`. Como limitações, a fonte Poppins depende de disponibilidade local e usa Montserrat como alternativa, e a impressão/PDF registra somente a aba interativa selecionada.

## Saídas DOCX geradas

`entrega_final/` contém 14 cópias preenchidas a partir dos 14 modelos DOCX recebidos, conservando o nome institucional de cada modelo e a mesma árvore de pastas de `documentos/` — `Unidade 1` a `Unidade 4`, cada uma com a subpasta de validação recebida, mais `Instrumentos Avaliativos/`:

- 4 materiais didáticos (`Unidade N/TEMPLATE - Unidade N_…`), um por unidade;
- 4 questionários (`Unidade N/40 Questões - UNIn_…`), cada um com 40 questões, 200 alternativas, 40 gabaritos e 200 devolutivas;
- 1 trabalho PBL e 1 avaliação final dissertativa em `Instrumentos Avaliativos/`, ambos em versão mestra com as partes do estudante e do tutor claramente separadas;
- 4 fichas de validação copiadas sem alteração, com status pendente até a gravação, sem parecer, data ou responsável simulados;
- os 17 decks HTML, em `Unidade N/SLIDES - Videoaulas …/`, com um `index.html` de navegação na raiz do pacote.

O método é o mesmo de `data_engineering_and_pipelines`: o modelo oficial é aberto, cada caixa colorida recebe o conteúdo autoral correspondente, as orientações do modelo são removidas e o resultado é gravado como cópia — capa, cabeçalho, estilos e caixas permanecem intactos. `scripts/validar_entrega.py` reabre os 14 arquivos a cada geração e registra o resultado em `entrega_final/validacao_docx.json`: materiais didáticos em Times New Roman 12 e questionários e avaliações em Arial 12, todos com entrelinha 1,15, alinhamento à esquerda e sem espaçamento posterior; alternativa correta marcada com `*` antes da letra, com distribuição exata de 8 corretas por letra; nenhuma orientação do modelo remanescente e nenhuma sintaxe residual de Markdown ou LaTeX. As cinco URLs do PBL são hyperlinks clicáveis. As versões mestras ainda não substituem os arquivos de distribuição separados do estudante e do tutor nem a aprovação da coordenação.

Para regenerar todo o pacote: `PYTHONPATH=/tmp/dse-docx-libs python3 scripts/montar_entrega.py`. O detalhamento do mapeamento caixa a caixa está em `entrega_final/README.md`.

## Proveniência e limitações

O relatório `ANALISE_MATERIAIS_RECEBIDOS.md` registra uma análise realizada em 30 de julho de 2026 sobre um arquivo externo chamado `a.zip`. O workspace agora contém, em `documentos/`, 34 arquivos nos formatos e quantidades descritos no relatório: 14 DOCX, 16 PPTX e 4 PDF. Eles são modelos e guias de referência, não documentos finais preenchidos. As saídas geradas ficam separadas em `entrega_final/`. `materiais_recebidos/` continua contendo apenas seu README. A integridade da cópia está registrada e validada em `documentos/MANIFESTO_SHA256.md`.

Também não há plano de aprendizagem oficial preenchido. `PLANO_APRENDIZAGEM_PROPOSTO.md` é uma proposta autoral provisória, elaborada a partir do título da disciplina e de inferências pedagógicas. Ela não substitui a aprovação da coordenação.

## Condições para a entrega institucional

1. **concluído no workspace:** manter preservados os 34 modelos e guias de `documentos/`, cujos hashes já foram registrados e reconferidos;
2. **pendente no NEaD:** ratificar a adaptação da cópia da Unidade 2 ou fornecer o modelo correto, pois o arquivo recebido com esse nome repete internamente a Unidade 1;
3. obter o plano oficial ou aprovação formal e registrada da proposta;
4. confirmar a distribuição das 40 questões por unidade;
5. confirmar se os slides devem ser entregues em PPTX/PDF ou se o HTML será aceito;
6. confirmar em ensaio cronometrado que os 16 roteiros entregam os 20 minutos previstos e ratificar essa duração com o NEaD, dado o conflito com o guia recuperado;
7. **concluído no workspace:** revisar tecnicamente conteúdo, referências, links, licenças e acessibilidade dos artefatos atuais, além de executar o QA estrutural e tipográfico dos 14 DOCX;
8. **pendente:** executar o CopySpider, exportar separadamente as versões de distribuição do estudante e do tutor e reauditar os slides no formato aprovado;
9. submeter os documentos à validação da coordenação;
10. definir a modalidade e agendar as gravações.

Os arquivos Markdown são fontes de trabalho. Os DOCX, PPTX e PDF de `documentos/` são referências institucionais imutáveis; as cópias de `entrega_final/` são entregáveis preenchidos em estado de pré-validação. Não existe atualmente um pacote aprovado pela coordenação nem gravações validadas neste repositório.
