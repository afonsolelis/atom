# Diretrizes de produção

> **Status documental:** estas diretrizes consolidam requisitos do pacote institucional preservado em `documentos/` e inventariado em `documentos/MANIFESTO_SHA256.md`. Os 34 originais estão disponíveis, tiveram seus hashes reconferidos e não devem ser editados. As 14 cópias DOCX preenchidas foram geradas separadamente em `entrega_final/`; continuam em pré-validação porque o plano oficial e a aprovação da coordenação ainda não estão disponíveis.

## Requisitos informados por e-mail

1. A disciplina possui quatro unidades.
2. Cada unidade corresponde a um modelo e quatro videoaulas.
3. Cada unidade deve conter 40 questões.
4. Haverá um vídeo introdutório conectando a disciplina ao mercado de trabalho.
5. As 16 videoaulas devem apresentar conteúdo prático e relevante para o cotidiano profissional.
6. Os slides devem orientar a equipe de edição.
7. Os slides podem indicar frases, imagens, tomadas e outros recursos audiovisuais.
8. Quando houver mídia externa, devem ser registrados o endereço, a autoria, a licença e o trecho exato que será utilizado.
9. A avaliação final terá 10 questões dissertativas.
10. Todas as entregas passarão pela validação da coordenação e poderão receber solicitações de ajuste.

## Requisitos verificados nos modelos oficiais

- Cada aula deve conter de 3 a 5 imagens, gráficos ou organogramas.
- Os recursos visuais devem ter licença compatível, origem registrada e descrição alternativa.
- As referências devem seguir a ABNT NBR 6023:2018.
- Nos modelos de unidade, o corpo do texto é especificado em Times New Roman, tamanho 12, espaçamento entre linhas de 1,15, alinhamento à esquerda e sem recuo adicional após os parágrafos.
- Palavras e expressões em língua estrangeira devem ser apresentadas em itálico, exceto siglas, marcas, nomes próprios e trechos de código.
- A similaridade indicada pelo modelo é de, no máximo, 3% no CopySpider.
- A primeira aula de cada unidade deve apresentar “O que você verá nesta unidade”.
- A terceira aula de cada unidade deve conter uma “Pausa para reflexão” ou um “Desafio”.
- A última aula de cada unidade deve realizar a transição para a unidade seguinte; na Aula 16, deve haver o fechamento da disciplina.
- Cada unidade deve conter duas questões de quiz não avaliativo com devolutiva conceitual.
- Os materiais complementares devem ser públicos ou estar disponíveis na Biblioteca Virtual.
- O trabalho deve seguir *Problem-Based Learning* (PBL) e apresentar pelo menos quatro fontes primárias.
- A avaliação final deve conter 10 questões dissertativas, modelos de resposta e critérios de correção.
- A duração adotada para as videoaulas é de **20 minutos**, conforme determinação do responsável pelo projeto. O guia recuperado `Guia - Como Fazer um Bom Vídeo.pdf` indica de 5 a 10 minutos; o conflito está registrado em `ANALISE_MATERIAIS_RECEBIDOS.md` e deve ser ratificado pelo NEaD. Os 16 roteiros estão dimensionados para 20 minutos, com narração mapeada slide a slide, e ainda exigem ensaio cronometrado antes da gravação.
- O vídeo introdutório deve durar até 2 minutos.
- Todas as videoaulas devem possuir slides.
- A estrutura, as caixas e os estilos dos DOCX oficiais não devem ser alterados.
- As instruções internas e os exemplos dos modelos devem ser removidos da versão final.

## Estrutura de cada unidade na fonte de trabalho

Cada arquivo de unidade deve conter ou reservar:

- identificação da disciplina, unidade e conteudista;
- relevância profissional da unidade;
- competências e resultados de aprendizagem;
- quatro aulas completas;
- aplicação ou estudo de caso;
- atividade prática;
- síntese e pontos-chave;
- duas questões de quiz com devolutiva;
- quatro categorias de materiais complementares;
- referências;
- elementos exigidos pelo modelo institucional.

Essa estrutura organiza a redação, mas não substitui o preenchimento dos DOCX oficiais.

## Estrutura das videoaulas

Cada roteiro deve conter:

- título e vínculo com o plano de aprendizagem;
- deck de apoio correspondente e mapa de tempo por slide;
- objetivo da videoaula;
- abertura contextualizada;
- desenvolvimento conceitual;
- demonstração, exemplo ou estudo de caso;
- aplicação profissional;
- fechamento e saudação final;
- indicações de edição e recursos visuais;
- fontes, licenças e trechos de eventual mídia externa.

## Regra de conteúdo e governança

O plano oficial deve determinar ementa, competências, bibliografia e sequência didática. Enquanto ele estiver ausente, `PLANO_APRENDIZAGEM_PROPOSTO.md` e o material dele derivado deverão permanecer identificados como **proposta provisória**, sem declaração de conformidade ou conclusão institucional.

Uma aprovação formal da coordenação poderá tornar a proposta a base definitiva. Se o plano oficial divergir, ele prevalecerá e todo o conteúdo afetado deverá ser revisado.

## Regra das questões

O contrato e o e-mail informam 40 questões por unidade, totalizando 160. Os modelos analisados apresentaram instruções internas conflitantes, registradas em `ANALISE_MATERIAIS_RECEBIDOS.md`.

Até confirmação do NEaD, a fonte de trabalho adota provisoriamente:

- 20 questões de asserção–razão;
- 20 questões de interpretação;
- cinco alternativas em todas as questões;
- devolutiva específica para cada alternativa;
- alternativa correta marcada com asterisco.

Essa distribuição não deve ser tratada como validada até haver confirmação registrada.

## Versões do estudante e do tutor

- A versão do estudante deve conter apenas enunciados, orientações, critérios públicos e formato de entrega.
- A versão do tutor deve conter os mesmos enunciados e, em seção ou documento separado, respostas esperadas, devolutivas e rubricas.
- Respostas esperadas, soluções e chaves de correção nunca devem permanecer na versão distribuída aos estudantes.
- No arquivo-fonte, os limites das duas versões devem ser inequívocos para permitir exportação segura.

## Formatos de trabalho

- Fonte editável durante a produção: Markdown (`.md`).
- Entrega intermediária opcional: HTML preparado para revisão.
- Entrega institucional final informada: DOCX preenchido nos modelos recebidos.
- Slides: formato e modelo a serem confirmados pelo NEaD; os HTMLs atuais são protótipos e não substituem automaticamente os PPTX.

Os 17 protótipos HTML passaram por QA em seis dimensões de viewport, 1.608 estados de slide/aba e 30 estados com reflexões expandidas, sem falhas, erros JavaScript ou *overflow* não rolável. Nenhum PPTX novo foi gerado. A fonte Poppins depende da instalação local, com Montserrat como alternativa, e a impressão/PDF preserva somente a aba interativa que estiver selecionada.

Os DOCX, PPTX e PDF existentes em `documentos/` são originais institucionais de referência. As cópias preenchidas de `entrega_final/` não alteram esse acervo e não devem ser confundidas com aprovação institucional. Na data registrada no README, ainda não há pacote validado pela coordenação.

## Mapa exato dos originais e das saídas esperadas

### Modelos que originaram 10 DOCX de conteúdo preenchidos

1. `documentos/Unidade 1/TEMPLATE - Unidade 1_nome da disciplina.docx` → Unidade 1, incluindo relação com a atuação profissional e roteiro introdutório;
2. `documentos/Unidade 2/TEMPLATE - Unidade 2_nome da disciplina.docx` deveria originar a Unidade 2, mas seu texto interno é idêntico ao modelo da Unidade 1 e contém “Plano de Ensino - Unidade 1”, vídeo introdutório e Aulas 1 a 4. A cópia preenchida remapeou as mesmas caixas para as Aulas 5 a 8, sem alterar o original; deve-se obter ratificação formal dessa adaptação ou substituir a cópia quando o modelo correto for fornecido;
3. `documentos/Unidade 3/TEMPLATE - Unidade 3_nome da disciplina.docx` → Unidade 3;
4. `documentos/Unidade 4/TEMPLATE - Unidade 4_nome da disciplina.docx` → Unidade 4;
5. `documentos/Unidade 1/40 Questões - UNI1_nomedadisciplina.docx` → questionário da Unidade 1;
6. `documentos/Unidade 2/40 Questões - UNI2_nomedadisciplina.docx` → questionário da Unidade 2;
7. `documentos/Unidade 3/40 Questões - UNI3_nomedadisciplina.docx` → questionário da Unidade 3;
8. `documentos/Unidade 4/40 Questões - UNI4_nomedadisciplina.docx` → questionário da Unidade 4;
9. `documentos/Instrumentos Avaliativos/TEMPLATE ENTREGA DE TRABALHO - nomedadisciplina.docx` → versão mestra do trabalho PBL com as partes do estudante e do tutor delimitadas; as cópias de distribuição separadas continuam pendentes;
10. `documentos/Instrumentos Avaliativos/Avaliação final_(10 discursivas)_nomedadisciplina.docx` → versão mestra da avaliação final com respostas ao final; as cópias de distribuição separadas continuam pendentes.

### Demais originais

- Os 16 arquivos `SLIDES - Videoaula N.pptx` são os modelos oficiais para as videoaulas 1 a 16. A Videoaula 1 possui 9 slides; as demais possuem 7. Não há um PPTX específico para o vídeo introdutório, portanto a necessidade de um 17º deck deve ser confirmada.
- Os 4 DOCX de validação são registros operacionais. As cópias geradas contêm somente metadados neutros e status pendente; parecer, data e responsável devem ser preenchidos pela coordenação e pelo profissional de vídeo depois da gravação.
- Os 4 PDF do guia de vídeo são cópias idênticas e servem somente como referência de gravação.

## Segurança dos originais

Os modelos de unidade contêm dados de acesso institucional em suas orientações internas. Por autorização expressa do responsável pelo projeto, esse bloco deve ser preservado exatamente nas cópias institucionais preenchidas. Os valores não podem ser reproduzidos em relatórios, mensagens ou materiais públicos. `documentos/` e os DOCX de `entrega_final/` permanecem ignorados pelo Git, e a coordenação deve confirmar o tratamento e a validade dessas credenciais antes de qualquer publicação fora do fluxo institucional protegido.

## Lista de verificação antes da entrega

- [x] Preservar os 34 arquivos originais e registrar seus hashes em `documentos/MANIFESTO_SHA256.md`.
- [x] Gerar em `entrega_final/` as 10 cópias de conteúdo e as 4 cópias das fichas de validação, preservando os originais.
- [x] Redimensionar os 16 roteiros para a duração de 20 minutos, sincronizados slide a slide com os decks HTML.
- [ ] Obter o plano oficial ou aprovação formal da proposta.
- [ ] Obter o modelo correto da Unidade 2 ou autorização formal para adaptar uma cópia.
- [ ] Confirmar a distribuição das questões e o formato dos slides.
- [x] Preencher as cópias DOCX reaproveitando estrutura, caixas e estilos dos modelos.
- [x] Remover instruções internas, exemplos e marcadores de preenchimento das cópias geradas.
- [x] Confirmar que o bloco institucional de acesso foi preservado sem alteração apenas nas cópias autorizadas e que nenhum valor foi exposto em relatórios ou mensagens.
- [ ] Gerar separadamente as versões do estudante e do tutor.
- [x] Conferir contagens, gabaritos, devolutivas e somas de pontuação.
- [x] Revisar tecnicamente português, estrangeirismos e referências ABNT nas fontes e cópias atuais.
- [x] Verificar de 3 a 5 recursos visuais por aula, licença, origem e texto alternativo nos 17 HTMLs.
- [x] Embutir as 13 figuras autorais da Unidade 1 no material escrito, com legenda, crédito, licença e texto alternativo.
- [ ] Produzir as figuras do material escrito das Unidades 2, 3 e 4, hoje apenas descritas em bloco para a equipe de edição.
- [x] Testar equações e links nos DOCX e acessibilidade responsiva nos HTMLs atuais.
- [ ] Arquivar a autorização formal de uso institucional da fotografia do professor.
- [ ] Repetir o QA de imagens, links e acessibilidade no formato institucional exportado.
- [ ] Confirmar a duração efetiva dos roteiros em ensaio cronometrado.
- [ ] Executar o CopySpider e arquivar o relatório de similaridade.
- [x] Preparar as quatro fichas de validação com metadados neutros e status pendente após gravação.
- [ ] Preencher parecer, data e responsável nas fichas depois da gravação.
- [ ] Registrar a validação da coordenação e eventuais ajustes.
