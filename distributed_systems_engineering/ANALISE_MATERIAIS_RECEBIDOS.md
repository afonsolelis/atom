# Análise dos materiais recebidos

Data da análise inicial: 30 de julho de 2026

Atualização do inventário: 1º de agosto de 2026

Origem histórica registrada na análise inicial: arquivo externo `a.zip`

## Estado da evidência

O workspace contém em `documentos/` os 34 arquivos descritos na análise inicial:

- 4 modelos de unidade em DOCX;
- 4 modelos de questionário em DOCX;
- 2 modelos de instrumentos avaliativos em DOCX;
- 4 fichas de validação de videoaulas em DOCX;
- 16 modelos de slides em PPTX;
- 4 cópias do guia de produção de vídeos em PDF.

O inventário confirma 14 DOCX, 16 PPTX e 4 PDF. Caminhos e hashes estão em `documentos/MANIFESTO_SHA256.md`, e a verificação dos 34 hashes foi concluída com sucesso. As quatro cópias do guia de vídeo são idênticas, confirmado pelo SHA-256 registrado.

Esses arquivos são **originais institucionais de referência e devem permanecer imutáveis**. O preenchimento deve ocorrer em cópias. A pasta `materiais_recebidos/` continua contendo somente seu README, mas os originais agora estão preservados em `documentos/`.

As saídas preenchidas são mantidas separadamente em `entrega_final/` e permanecem em pré-validação. Os 10 modelos DOCX que originam entregáveis de conteúdo são:

- 4 modelos de unidade;
- 4 modelos de questionário;
- 1 modelo de trabalho PBL;
- 1 modelo de avaliação final dissertativa.

Os outros 4 DOCX são fichas operacionais de validação. As cópias de trabalho podem receber metadados neutros, mas o parecer, a data e o responsável somente podem ser preenchidos pela coordenação e pelo profissional de vídeo depois da gravação; por isso, permanecem marcados como pendentes. Os 16 PPTX são modelos das videoaulas 1 a 16, e os 4 PDF idênticos são guias de gravação.

### Estado das cópias preenchidas

O diretório `entrega_final/` espelha as pastas de `documentos/` e contém 14 DOCX gerados a partir de cópias dos 14 modelos:

- 4 materiais didáticos, com quatro textos-base e quatro roteiros cada;
- 4 questionários, totalizando 160 questões, 800 alternativas, 160 marcações de gabarito e 800 devolutivas;
- trabalho PBL e avaliação final dissertativa em versões mestras com as partes do estudante e do tutor delimitadas;
- 4 fichas de validação preparadas com metadados neutros e todos os pareceres pendentes após a gravação.

O QA automatizado dos oito DOCX de unidades e questionários está registrado em `entrega_final/validacao_docx.json`: todos foram reabertos; os rótulos das aulas e dos roteiros correspondem às Unidades 1 a 4; não foram encontrados instruções internas, marcadores de preenchimento, comentários ou partes `customXML`; e o bloco autorizado da Biblioteca Virtual foi preservado uma vez em cada material didático. A tipografia também passou sem divergências: materiais didáticos em Times New Roman 12 e questionários em Arial 12, ambos com entrelinha 1,15, alinhamento à esquerda e sem espaçamento posterior. Os seis DOCX de instrumentos e validação também foram reabertos pelo gerador. A avaliação foi ajustada para Arial 12, com entrelinha 1,5 nos enunciados e 1,0 com alinhamento justificado nos critérios, e seu checklist técnico de exportação foi excluído. O PBL preserva o texto ABNT e contém cinco hyperlinks HTTP clicáveis.

O modelo defeituoso da Unidade 2 exigiu remapeamento das caixas internamente rotuladas como Aulas 1 a 4 para as Aulas 5 a 8. A cópia gerada está coerente com a Unidade 2, mas essa adaptação continua sujeita à ratificação formal do NEaD.

### Alerta de segurança

Os modelos de unidade incluem dados de acesso institucional nas orientações internas. Os valores não são reproduzidos neste relatório. Por autorização expressa do responsável pelo projeto, o bloco deve ser preservado exatamente nas cópias institucionais preenchidas, sem transcrição para relatórios, mensagens ou materiais públicos. A coordenação deve confirmar seu tratamento antes de qualquer publicação fora do ambiente protegido.

## Ausência do plano de aprendizagem

O plano de aprendizagem de *Distributed Systems Engineering* não está preenchido nos arquivos recebidos.

A inspeção dos modelos confirma que o plano não está preenchido e que aparece apenas o campo:

> Caro coordenador, insira o plano de ensino da disciplina aqui.

Portanto, ainda não temos oficialmente:

- ementa;
- competências;
- resultados de aprendizagem;
- títulos das quatro unidades;
- títulos e conteúdos das 16 aulas;
- bibliografia;
- sequência didática indicada pela coordenação.

Essas informações precisam ser recuperadas do ambiente institucional ou solicitadas à equipe do NEaD antes da redação definitiva. Até lá, `PLANO_APRENDIZAGEM_PROPOSTO.md` e todo conteúdo dele derivado permanecem provisórios.

## Requisitos registrados para os modelos de unidade

### Estrutura geral

Cada unidade deve conter:

- identificação da disciplina e do conteudista;
- plano de ensino da unidade;
- quatro textos-base;
- quatro roteiros sintéticos de videoaula;
- duas questões de quiz não avaliativo;
- materiais complementares.

A Unidade 1 também exige:

- texto sobre a relação da disciplina com a atuação profissional;
- roteiro do vídeo introdutório de até 2 minutos;
- uma atividade verificadora individual dissertativa, com resposta esperada.

Nos modelos analisados, a atividade verificadora aparecia somente na Unidade 1.

### Regras de escrita

- Texto acadêmico, coeso e objetivo;
- linguagem clara, acessível, dialógica e didática;
- explicação de termos técnicos sem perder profundidade;
- palavras estrangeiras em itálico;
- referências conforme ABNT NBR 6023:2018;
- corpo do texto em Times New Roman, tamanho 12, espaçamento entre linhas de 1,15, alinhamento à esquerda e sem recuo adicional após os parágrafos;
- citações diretas entre aspas e citações indiretas por paráfrase;
- similaridade máxima indicada de 3% no CopySpider;
- estrutura e caixas do DOCX não devem ser alteradas na entrega final;
- orientações internas devem ser apagadas após o preenchimento.

Não foi determinada quantidade mínima de páginas ou palavras.

### Recursos visuais

Cada aula deve conter de 3 a 5 imagens, gráficos ou organogramas:

- relevantes para a aprendizagem;
- de domínio público, Creative Commons ou provenientes do Envato;
- com resolução adequada;
- acompanhados de descrição alternativa;
- indicados no ponto exato do texto;
- com link de referência ou arquivo anexado.

Para as 16 aulas, isso representa de 48 a 80 recursos visuais.

### Regras específicas das aulas

- Primeira aula de cada unidade: seção “O que você verá nesta unidade”;
- terceira aula de cada unidade: “Pausa para reflexão” ou “Desafio”;
- quarta aula de cada unidade: transição “O que você verá na próxima unidade”;
- texto escrito: prioriza teoria, conceitos e fundamentos;
- videoaula: prioriza aplicações, exemplos, casos e demonstrações;
- texto e vídeo devem ser complementares, evitando redundância.

Na Aula 16, a orientação sobre “próxima unidade” deve ser interpretada como fechamento da disciplina, pois não existe Unidade 5. Esse ajuste deverá preservar a intenção pedagógica do modelo.

### Quiz

Cada unidade exige duas questões intermediárias:

- verdadeiro ou falso e/ou múltipla escolha;
- devolutiva que explique o conceito;
- respostas sem mensagens simplistas de apenas “certo” ou “errado”.

### Materiais complementares

São obrigatórios e devem indicar a aula de inserção:

1. livro da Biblioteca Virtual, com texto provocativo e capítulo;
2. material gratuito para aprofundamento;
3. podcast, preferencialmente no Spotify, ou vídeo em formato de podcast, com até 45 minutos;
4. artigo científico relacionado diretamente ao conteúdo, com referência ABNT.

Materiais pagos por serviços como Netflix ou Amazon não são permitidos.

## Questionários das unidades

### Requisitos confirmados

- 40 questões por unidade segundo o contrato, o e-mail e os nomes dos quatro arquivos;
- total de 160 questões;
- padrão ENADE;
- cinco alternativas por questão;
- alternativa correta marcada com asterisco;
- devolutiva individual para cada uma das cinco alternativas;
- devolutivas reunidas ao final do documento;
- questões autorais ou questões ENADE adaptadas ao contexto;
- exemplos do modelo devem ser removidos na entrega.

### Inconsistência encontrada

Segundo a análise registrada, os documentos apresentavam conflito:

- Unidade 1: diz “40 questões”, mas especifica 10 de asserção–razão e 10 de interpretação, totalizando apenas 20;
- Unidades 2, 3 e 4: dizem internamente “20 questões”, apesar de o nome do arquivo e o pacote contratado indicarem 40;
- todos os quatro documentos apresentam distribuição de apenas 10 questões de asserção–razão e 10 de interpretação.

### Regra adotada

O pacote contratado prevalece: serão produzidas 40 questões em cada unidade.

Até confirmação da equipe, a distribuição mais coerente é:

- 20 questões de asserção–razão;
- 20 questões de interpretação.

Antes da produção em massa, é recomendável confirmar por e-mail se essa divisão está correta.

## Trabalho

O trabalho deve seguir Problem-Based Learning (PBL) e conter obrigatoriamente:

- título conciso;
- desafio realista e suficientemente complexo;
- narrativa do caso respondendo o quê, quem, quando, onde e por quê;
- problema central;
- aplicação ao mercado de trabalho;
- pelo menos quatro fontes primárias;
- indicação das aulas que ajudam a resolver o desafio;
- formato do entregável;
- distribuição percentual da pontuação;
- solução esperada destinada ao professor tutor;
- roteiro do estudante.

## Avaliação final

O instrumento exige:

- 10 questões dissertativas;
- aderência ao plano de aprendizagem e ao conteúdo desenvolvido;
- devolutivas ao final;
- modelo de resposta esperado para cada questão;
- exclusão dos exemplos do modelo;
- manutenção rigorosa da formatação institucional.

## Videoaulas e slides

### Duração e abordagem

- 1 vídeo introdutório de até 2 minutos;
- 16 videoaulas;
- cada videoaula tem **20 minutos** nesta produção, por determinação do responsável pelo projeto; o PDF `Guia - Como Fazer um Bom Vídeo.pdf` indica de 5 a 10 minutos (conflito registrado abaixo);
- todas as videoaulas devem ter slides;
- roteiros devem ser planejados para evitar repetição do texto escrito;
- conteúdo deve ser prático, organizado e diretamente relacionado à carreira.

**Conflito de duração — registro.** O guia recuperado indica de 5 a 10 minutos por videoaula; os DOCX de unidade não mencionam duração. O responsável pelo projeto determinou 20 minutos por videoaula, e é essa a duração adotada na fonte de trabalho: os 16 roteiros estão em `roteiros_20min.md`, um arquivo por unidade, com narração de 2.200 a 2.700 palavras faladas mapeada slide a slide aos decks HTML. O conflito permanece aberto e deve ser ratificado pelo NEaD; se a coordenação confirmar a faixa do guia, os roteiros precisarão ser condensados e os decks, reduzidos. O tempo efetivo de cada fala ainda deve ser confirmado em ensaio cronometrado antes da gravação.

### Slides verificados

- Videoaula 1: 9 slides, incluindo audiodescrição, minibiografia, sumário e encerramento;
- Videoaulas 2 a 16: 7 slides por arquivo;
- os arquivos são modelos visuais ainda sem conteúdo da disciplina;
- os slides permitem imagem, frase, lista curta, take e indicação de mídia;
- textos longos devem ser evitados;
- links externos devem indicar o trecho exato a ser utilizado.

Separadamente, o workspace contém 17 protótipos navegáveis em HTML: introdução com 7 telas, Videoaula 1 com 9 e Videoaulas 2 a 16 com 7 cada. O QA final em Chromium percorreu seis dimensões de viewport, 1.608 estados de slide/aba e 30 estados com reflexões expandidas, sem falhas, erros JavaScript ou *overflow* não rolável; links, identificadores, ARIA e SVG também passaram. Esses protótipos não são conversões dos PPTX. Nenhum PPTX novo foi gerado, a fonte Poppins usa Montserrat como alternativa quando indisponível, e a impressão/PDF captura apenas a aba interativa selecionada.

### Gravação

A inspeção do guia confirma as seguintes orientações:

- gravação horizontal;
- preferência por Full HD, 1920 × 1080;
- formatos MP4, AVI, MOV ou MPEG;
- áudio em ambiente silencioso;
- roupa lisa, sem marcas destacadas;
- iluminação frontal;
- olhar para a lente;
- pausas de dois segundos antes e depois da fala;
- comunicação no singular, dirigindo-se ao estudante;
- saudação e encerramento em todas as aulas.

## Erros de reaproveitamento registrados nos modelos

Algumas instruções não foram atualizadas corretamente:

- o arquivo chamado `TEMPLATE - Unidade 2_nome da disciplina.docx` possui texto interno idêntico ao modelo da Unidade 1: identifica “Plano de Ensino - Unidade 1”, repete o vídeo introdutório e solicita as Aulas 1 a 4; não há nele seções para as Aulas 5 a 8;
- o modelo da Unidade 3 chamava a Videoaula 9 de “Videoaula 5” em uma orientação;
- o modelo da Unidade 4 chamava a Aula 13 de “Aula 9” e a Videoaula 13 de “Videoaula 5” em orientações;
- a Aula 16 solicita anúncio da “próxima unidade”, embora seja a última aula;
- a quantidade de questões diverge do pacote contratado.

Esses erros não devem ser reproduzidos no conteúdo final.

## Conclusão

Os 34 modelos e guias originais estão preservados e seus requisitos estruturais podem ser auditados. Cópias DOCX preenchidas são geradas em `entrega_final/`, mas ainda não equivalem a uma entrega aprovada. Continuam pendentes o plano de aprendizagem oficial ou a aprovação formal da proposta, a validação da coordenação e as etapas posteriores à gravação.

As próximas providências indispensáveis são obter da coordenação o plano oficial ou a aprovação formal da proposta; preservar e repetir o QA após eventuais ajustes; manter restrito o bloco institucional expressamente autorizado; exportar versões seguras de estudante e tutor; validar o formato final dos slides; cronometrar os roteiros; executar o CopySpider; e registrar a aprovação institucional.
