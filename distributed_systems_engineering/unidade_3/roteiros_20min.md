# Roteiros das videoaulas 9 a 12 — Unidade 3 (20 minutos)

Disciplina: Distributed Systems Engineering
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 3: Serviços, eventos e plataformas cloud-native
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: aproximadamente 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, indicações de edição e fontes.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas, respiração e construção progressiva dos recursos visuais.

Cada roteiro acompanha, slide a slide, o deck HTML da aula correspondente em `unidade_3/slides/`. As marcações entre colchetes duplos indicam o intervalo de tempo e o slide que deve estar na tela naquele momento. O avanço de slide é o principal marcador de edição: quando a marcação muda, o slide muda.

Plano de tempo de referência, adaptável ao ritmo de cada aula:

- 00:00–01:45 — capa, audiodescrição e sumário;
- 01:45–04:00 — objetivos de aprendizagem e situação-problema;
- 04:00–13:00 — desenvolvimento conceitual;
- 13:00–16:00 — demonstração, exemplos numéricos e estudo de caso;
- 16:00–18:00 — aplicação profissional e pausa para reflexão;
- 18:00–20:00 — pontos-chave, atividade prática e fechamento.

Os quatro roteiros a seguir correspondem às Aulas 9 a 12 da Unidade 3, mantendo a NexaOrder como fio condutor prático. Cada roteiro é um texto de narração pronto para gravação, e não notas de aula. O registro é o de exposição didática contínua, próximo ao de um livro-texto lido em voz alta: frases completas, encadeamento explícito entre as ideias e ausência de recursos de oralidade informal.

---

## Roteiro da Videoaula 9 — “Dividir não é o mesmo que desacoplar”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 9 — Decomposição em serviços e limites de domínio.

**Deck de apoio:** `unidade_3/slides/aula9.html` — 18 slides (capa, audiodescrição, sumário, 14 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de comparar monólito, monólito modular e microsserviços sem tratá-los como escala de qualidade, aplicar coesão e acoplamento como critérios de fronteira, calcular a instabilidade de um serviço, identificar contextos delimitados, diagnosticar um monólito distribuído pelos sintomas operacionais e registrar uma decisão de fronteira.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 três formas de organizar · 05:40 coesão e acoplamento · 07:10 exemplo numérico da instabilidade · 09:00 contexto delimitado · 10:50 dados por serviço · 12:30 citação · 12:50 API Gateway · 14:20 comunicação conversacional · 15:50 seis sinais · 17:30 decisão de fronteira · 19:00 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 9, primeira da Unidade 3, e o foco da disciplina se desloca novamente. A Unidade 1 tratou de processos; a Unidade 2, de dados. Esta unidade trata dos serviços em si, e do lugar onde se traçam as linhas que separam um serviço do outro.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: os slides usam fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo aparece em cartões claros. São cinco recursos visuais: o quadro comparativo entre as três formas de organizar um sistema, a fórmula da instabilidade, o diagrama de dois contextos delimitados sobre o mesmo termo, o diagrama do API Gateway compondo respostas e a lista dos seis sinais de monólito distribuído. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo comparando monólito, monólito modular e microsserviços. Trato depois de coesão e acoplamento como critérios explícitos de desenho, incluindo uma métrica numérica de instabilidade. Apresento em seguida contexto delimitado e capacidade de negócio, oriundos do Domain-Driven Design, e o princípio de dados por serviço. Examino o API Gateway e da composição de respostas, discuto a comunicação conversacional como sintoma e fecho com os seis sinais do monólito distribuído e com a decisão de fronteira registrada.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir comparar monólito, monólito modular e microsserviços sem tratá-los como uma escala de qualidade. Deve aplicar coesão e acoplamento como critérios explícitos de desenho de fronteira. Deve calcular a instabilidade de um serviço a partir de suas dependências. Deve identificar contextos delimitados a partir de termos que mudam de significado. Deve diagnosticar um monólito distribuído pelos seus sintomas operacionais. E deve registrar uma decisão de fronteira com requisito, decisão, compromisso e evidência.

**[02:20–03:50 · Slide 4 — Situação-problema]**

A NexaOrder já opera com quatro serviços aparentemente independentes. Cada um tem seu repositório, seu pipeline e seu time responsável. No diagrama, a arquitetura parece correta. A equipe, porém, convive com sintomas persistentes.

Alterar o formato do pedido exige mudar o estoque junto, porque os dois compartilham a mesma tabela de itens. Liberar o pagamento sem atualizar pedidos no mesmo dia quebra o checkout. E qualquer incidente exige praticamente todo o time disponível, porque ninguém consegue diagnosticar sua parte isoladamente.

O diagnóstico é este: a separação foi feita por conveniência técnica, e não por limites de negócio.

O resultado tem nome, já mencionado em aulas anteriores: monólito distribuído. Paga-se todo o custo operacional da distribuição — rede, serialização, falhas parciais, complexidade de depuração — sem colher o benefício principal, que é a autonomia de evolução dos times.

Trata-se do pior arranjo possível, e também de um dos mais frequentes.

### Desenvolvimento conceitual

**[03:50–05:40 · Slide 5 — Três formas de organizar um sistema]**

Convém examinar as três opções com rigor.

*[indicação de edição: inserir Recurso visual 33 da Aula 9 — quadro comparativo das três formas, revelado linha a linha]*

O monólito: uma única unidade executável, com banco geralmente compartilhado. Adequa-se a times pequenos e a domínios ainda em descoberta — enquanto não se sabe onde as fronteiras deveriam estar, não há razão para fixá-las.

O monólito modular: também uma única unidade de implantação, mas com fronteiras internas rígidas e esquemas segregados dentro do mesmo banco. Cabe uma ênfase: trata-se de arquitetura legítima, e não apenas de etapa de transição rumo a microsserviços. Para muitas equipes, é o ponto de chegada adequado.

Os microsserviços: cada serviço implanta e escala de forma independente, com armazenamento próprio. Adequam-se quando escala e autonomia organizacional justificam o custo operacional, que é real e elevado.

A conclusão que atravessa a aula é que nenhuma dessas formas é universalmente superior. Um monólito modular bem projetado pode ser mais barato de operar do que dezenas de microsserviços mal delimitados. É exatamente o mesmo raciocínio de custo, benefício e evidência que estabelecemos na Aula 1.

**[05:40–07:10 · Slide 6 — Coesão, acoplamento e autonomia]**

Se a forma não é o critério, qual é? São dois conceitos antigos da engenharia de software, que ganham significado novo aqui.

Coesão é o grau em que os elementos internos de um componente se relacionam e mudam juntos. A expressão “mudam juntos” é operacional, não estética: se dois elementos sempre se alteram na mesma tarefa, provavelmente pertencem ao mesmo lugar.

Acoplamento é o grau em que um componente depende de detalhes internos de outro. A expressão “detalhes internos” é decisiva: depender de um contrato público é uma coisa; depender da estrutura interna de uma tabela alheia é outra inteiramente distinta.

O bom limite, portanto, é aquele que maximiza a coesão interna e minimiza o acoplamento externo. A autonomia é consequência: com a fronteira correta, o time implanta sem coordenação com os demais.

O teste prático é objetivo. Fronteira não é questão de preferência; ela se manifesta em duas medidas — quantas implantações precisam ser coordenadas e quantas pessoas precisam estar presentes em um incidente. Se esses dois números são altos, a fronteira está incorreta, independentemente da elegância do diagrama.

**[07:10–09:00 · Slide 7 — Exemplo numérico: instabilidade]**

Parte disso pode ser expressa numericamente. Existe uma heurística de Robert C. Martin, originalmente proposta para pacotes, adaptável com cautela ao nível de serviços.

*[indicação de edição: inserir a fórmula da instabilidade, com os dois termos do denominador destacados]*

Sejam C-a o acoplamento aferente — quantos componentes dependem deste — e C-e o acoplamento eferente — de quantos este depende. A instabilidade é: I igual a C-e dividido pela soma de C-a mais C-e.

Tomemos o caso do estoque da NexaOrder. Três serviços consomem o estoque, então C-a é igual a 3. O estoque depende de um único serviço, então C-e é igual a 1. A conta: 1 dividido por 3 mais 1, ou seja, 1 dividido por 4, que dá 0,25.

A interpretação é a seguinte. A escala vai de 0 a 1, de estável a instável. Um valor baixo, como esse 0,25, indica um serviço estável: muito pressionado por consumidores e pouco dependente de outros. Isso significa que ele precisa de contratos muito bem cuidados, porque mudanças nele se propagam para três lugares. Uma instabilidade alta indica o oposto: menos pressão externa, porém maior sujeição a mudanças alheias.

Cabe uma ressalva metodológica importante: essa métrica não substitui julgamento de negócio nem mede criticidade. Um serviço com instabilidade 0,9 pode ser o mais crítico do sistema. O que ela oferece é tornar parte do acoplamento discutível, convertendo uma percepção difusa em um número que a equipe pode debater.

**[09:00–10:50 · Slide 8 — Contexto delimitado e capacidade de negócio]**

Chegamos ao instrumento mais poderoso desta aula, proveniente do Domain-Driven Design.

São dois conceitos. Contexto delimitado é a fronteira dentro da qual um modelo de domínio e sua linguagem têm significado consistente. Capacidade de negócio é algo que a organização faz para gerar valor — “gerenciar estoque”, “processar pagamentos” — independentemente de como isso é implementado.

*[indicação de edição: inserir Recurso visual 34 da Aula 9 — o mesmo termo “item” representado de duas formas diferentes, no catálogo e no estoque]*

Um exemplo esclarece o conceito de modo duradouro. Considere a palavra “item” dentro da NexaOrder.

Para o catálogo, um “item” é uma descrição comercial: preço, imagens, categorias, texto de marketing. Para o estoque, o mesmo “item” é quantidade física em um depósito, com número de série e localização na prateleira.

São duas entidades distintas designadas pela mesma palavra. O erro clássico consiste em tratar essas duas visões como um mesmo modelo de dados compartilhado, o que constitui fonte comum de acoplamento acidental — uma mudança no significado de “item” para o catálogo pode comprometer silenciosamente o controle de estoque.

Daí decorre uma heurística de trabalho: onde um mesmo termo muda de significado conforme quem fala, provavelmente existem dois contextos delimitados diferentes. O vocabulário empregado nas reuniões revela fronteiras com mais precisão do que qualquer diagrama.

**[10:50–12:30 · Slide 9 — Dados por serviço]**

Consequência direta de contextos bem definidos: cada serviço possui e controla seu próprio armazenamento, e nenhum outro serviço o acessa diretamente. Nem por leitura.

A restrição merece ênfase, por ser o ponto em que as equipes costumam abrir exceções: nem por leitura. A consulta aparentemente inofensiva ao banco alheio é a origem de boa parte do acoplamento acidental observado em produção.

Toda interação passa por contrato explícito: uma API, uma mensagem ou um evento publicado.

O custo aparente é a perda da conveniência de um JOIN entre tabelas de serviços diferentes. Consultas antes triviais passam a exigir composição de chamadas ou réplicas de leitura.

Esse custo, contudo, é deliberado. Sem ele, qualquer alteração de esquema compromete quem lê a tabela diretamente, e nem sempre se sabe quem são esses consumidores. Sem ele, a fronteira não existe de fato, ainda que existam repositório de código, pipeline e time separados.

Foi exatamente esse o erro da NexaOrder: permitir que pedidos e pagamento lessem a mesma tabela de itens do estoque. Três serviços no diagrama, um único banco na prática.

**[12:30–12:50 · Slide 10 — Citação]**

Esta frase enuncia a tese da aula: a divisão física em repositórios ou processos não produz, por si só, autonomia real.

### Demonstração, exemplo ou estudo de caso

**[12:50–14:20 · Slide 11 — API Gateway e composição]**

Se cada serviço tem seu contrato, como o mundo externo fala com o sistema?

Expor todos os serviços diretamente traz dois problemas. Primeiro, acopla a topologia interna aos consumidores externos — dividir um serviço em dois passa a comprometer o aplicativo do cliente. Segundo, multiplica autenticação e limitação de taxa em cada serviço.

*[indicação de edição: inserir Recurso visual 35 da Aula 9 — API Gateway compondo uma resposta a partir de três serviços]*

O API Gateway resolve isso com quatro funções. Rotear a requisição para o serviço correto. Compor respostas de múltiplos serviços em uma única resposta. Aplicar autenticação e limitação de taxa em um só lugar. E ocultar a decomposição interna dos consumidores externos.

Um exemplo concreto: a tela de detalhes do pedido precisa de dados de pedidos, estoque e expedição. O gateway consulta os três e devolve uma resposta única, sem que o aplicativo tenha conhecimento dos três serviços subjacentes.

Um alerta importante acompanha esse padrão: o gateway não deve acumular regras de negócio. Quando isso ocorre, ele se converte em um novo monólito oculto atrás de uma fachada de microsserviços. Toda mudança de regra passa a exigir alteração no gateway, o que recria o gargalo que se pretendia eliminar, agora em posição mais crítica.

**[14:20–15:50 · Slide 12 — Comunicação entre serviços e o sintoma conversacional]**

O vocabulário sobre como os serviços se comunicam foi estabelecido na Aula 2. Comunicação síncrona, com HTTP ou RPC, oferece simplicidade e resposta imediata, mas propaga indisponibilidade pela cadeia. Comunicação assíncrona, com eventos, reduz o acoplamento temporal ao custo de um raciocínio mais complexo sobre consistência.

O que cabe acrescentar aqui é um sintoma de diagnóstico: a comunicação conversacional, situação em que um único caso de uso dispara dezenas de chamadas remotas entre serviços — busca o pedido, busca o item, busca o preço, busca o estoque, busca a promoção, e assim sucessivamente.

Esse sintoma revela que a fronteira foi traçada no lugar errado. Responsabilidades fortemente relacionadas — que mudam juntas e são consultadas juntas — foram separadas sem necessidade.

Uma prática simples é particularmente útil em revisões de arquitetura: contar quantas chamadas remotas um caso de uso exige está entre os diagnósticos mais baratos e mais reveladores de fronteira mal desenhada. Não é necessária ferramenta alguma — basta tomar o caso de uso mais frequente do sistema e contar os saltos de rede.

**[15:50–17:30 · Slide 13 — Seis sinais de monólito distribuído]**

O diagnóstico se consolida em uma lista utilizável como roteiro de autoavaliação.

*[indicação de edição: inserir Recurso visual 36 da Aula 9 — lista dos seis sinais, revelada item a item, com marcadores de verificação]*

Sinal um: implantações de serviços diferentes precisam ser coordenadas no mesmo horário.

Sinal dois: qualquer mudança de esquema em um serviço quebra outros serviços.

Sinal três: um incidente em um serviço exige a presença de praticamente todo o time.

Sinal quatro: serviços compartilham tabelas, filas ou segredos sem contrato explícito.

Sinal cinco: a topologia de chamadas de um único caso de uso é profunda e conversacional.

Sinal seis: times não conseguem testar ou implantar sem depender de outros no mesmo instante.

Uma ressalva sobre o uso dessa lista: nenhum sintoma isolado é definitivo. Uma implantação coordenada pontual ocorre em qualquer arquitetura. Vários sinais simultâneos, porém, indicam que a divisão física não produziu autonomia. A lista serve como roteiro de autodiagnóstico em uma retrospectiva de arquitetura, e sua utilidade depende de respostas honestas — o custo de ignorar os sinais é elevado.

### Aplicação profissional

**[17:30–19:00 · Slide 14 — Do diagnóstico à decisão de fronteira]**

Diagnosticar é a parte simples; a decisão exige mais. Como na Aula 1, ela precisa explicitar quatro elementos.

Para a NexaOrder, o registro ficaria assim.

Requisito: eliminar a necessidade de coordenar implantações entre pedidos e estoque. O requisito é operacional e mensurável, não estético.

Decisão: separar “item de catálogo” de “unidade em estoque”, cada um com armazenamento próprio, com comunicação por eventos de reserva e liberação.

Compromisso, elemento que confere honestidade à decisão: consultas que hoje usam um JOIN local passam a exigir composição no gateway ou réplicas de leitura assíncronas, com atraso de propagação. Paga-se em latência e em consistência aquilo que se ganha em autonomia, e esse custo precisa estar registrado por escrito.

Evidência: o número de implantações que exigiram coordenação simultânea, antes e depois, medido ao longo de um trimestre. Se esse número não diminuir, a mudança não entregou o que prometia, e isso também precisa ser declarado.

O padrão é o mesmo: requisito, decisão, compromisso e evidência — a estrutura da Aula 1, aplicada agora a fronteiras de serviço. Ela se aplica a qualquer decisão arquitetural.

### Fechamento

**[19:00–19:40 · Slides 15 e 16 — Pontos-chave e atividade prática]**

Recapitulando. Três opções válidas: monólito, monólito modular e microsserviços são escolhas arquiteturais, e a decisão depende de requisitos, não de tendência. Coesão dentro, acoplamento fora: um bom limite agrupa o que muda junto e isola o que não deveria mudar junto. Termos revelam fronteiras: onde um mesmo termo muda de significado, provavelmente há dois contextos delimitados. Dados por serviço: acesso direto ao armazenamento alheio anula a fronteira, mesmo com repositórios separados. Gateway sem negócio: ele concentra composição e políticas transversais, e regras de domínio ali criam um monólito escondido. E os sintomas se somam: implantações coordenadas e chamadas conversacionais são evidências práticas de fronteira mal traçada.

Na atividade prática, você vai definir os limites de serviço da NexaOrder, entregando diagrama e tabela de justificativas: listar as capacidades de negócio, identificar o contexto delimitado de cada uma, registrar onde o significado de um termo comum muda entre contextos, propor a divisão indicando qual serviço possui qual armazenamento, calcular a instabilidade aproximada de dois serviços e listar três sintomas que a nova divisão elimina mais um novo risco que ela introduz.

**[19:40–20:00 · Slide 17 — Encerramento]**

Esta aula forma a capacidade de desenhar fronteiras que desacoplam times, dados e ciclos de implantação, e de diagnosticar quando isso não ocorreu. A próxima aula substitui a cadeia de chamadas síncronas por uma arquitetura orientada a eventos.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 9 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com os três sintomas destacados um a um (02:20–03:50).
- Recurso visual 33 — quadro comparativo das três formas de organizar um sistema (aproximadamente 04:00).
- Slide 7 — fórmula da instabilidade, com o cálculo aparecendo passo a passo (aproximadamente 07:20).
- Recurso visual 34 — o termo “item” em dois contextos delimitados distintos (aproximadamente 09:20).
- Slide 10 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (12:30).
- Recurso visual 35 — API Gateway compondo resposta de três serviços (aproximadamente 13:00).
- Recurso visual 36 — lista dos seis sinais de monólito distribuído, revelada item a item (15:50–17:30).
- Slide 17 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- EVANS, Eric. *Domain-Driven Design: Tackling Complexity in the Heart of Software*. Boston: Addison-Wesley, 2003 — referência conceitual, sem reprodução de trecho externo.
- NEWMAN, Sam. *Building Microservices*. 2. ed. Sebastopol: O’Reilly Media, 2021 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, quadros e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 9 (`unidade_3.md`) e do deck `unidade_3/slides/aula9.html`.

---

## Roteiro da Videoaula 10 — “Reagir a fatos, em vez de esperar respostas”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 10 — Arquitetura orientada a eventos.

**Deck de apoio:** `unidade_3/slides/aula10.html` — 18 slides (capa, audiodescrição, sumário, 14 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de distinguir comando, evento de domínio e notificação, escolher a chave de particionamento que preserva a ordem necessária, dimensionar o número mínimo de partições, explicar o efeito de um rebalanceamento, comparar as três semânticas de entrega e evoluir esquemas de evento preservando compatibilidade.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:40 comando, evento e notificação · 05:30 tópicos e partições · 07:10 ordenação por partição · 08:40 grupos de consumidores · 10:20 exemplo numérico das partições · 11:50 citação · 12:10 retenção e reprocessamento · 13:50 três semânticas de entrega · 15:40 evolução de esquemas · 17:20 o ciclo do pedido reorganizado · 19:00 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 10, dedicada à arquitetura orientada a eventos. A aula anterior tratou das fronteiras entre os serviços; esta trata do modo como eles se comunicam, mudança cujas consequências são profundas.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o quadro dos três tipos de mensagem, o diagrama de tópico com partições e deslocamentos, o diagrama de grupos de consumidores compartilhando partições, a tabela de políticas de retenção e o fluxo do ciclo do pedido reorganizado por eventos. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo separando comando, evento de domínio e notificação. Apresento depois a infraestrutura: produtores, consumidores, tópicos e partições. Trato em seguida da ordenação, garantida dentro da partição e não entre partições, e dos grupos de consumidores e do paralelismo que permitem. Examino retenção e reprocessamento, comparo as três semânticas de entrega — at-most-once, at-least-once e exactly-once — e discuto evolução de esquemas. Fecho reorganizando o ciclo completo do pedido em torno de eventos.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir distinguir comando, evento de domínio e notificação pelo acoplamento que cada um cria. Deve escolher a chave de particionamento que preserva a ordem necessária ao negócio. Deve dimensionar o número mínimo de partições a partir da taxa de pico e da capacidade do consumidor. Deve explicar o que acontece com a carga quando um grupo de consumidores rebalanceia. Deve comparar as três semânticas de entrega quanto a perda e duplicação. E deve evoluir esquemas de evento preservando compatibilidade retroativa e prospectiva.

**[02:20–03:40 · Slide 4 — Situação-problema]**

Com fronteiras mais claras, um problema persiste na NexaOrder. O checkout chama pedidos, que chama de forma síncrona o estoque, que chama pagamento, que chama expedição.

As consequências são previsíveis a partir do que a Unidade 1 estabeleceu. Se qualquer serviço estiver lento, a cadeia inteira fica lenta. Se qualquer um estiver indisponível, o pedido falha por completo.

O aspecto mais problemático desse desenho é que isso vale mesmo quando a etapa afetada não é urgente. A notificação de expedição pode falhar e comprometer uma compra já paga, resultado desproporcional à natureza da etapa.

A saída é reorganizar a comunicação em torno de fatos já ocorridos. Em vez de solicitar uma ação e aguardar resposta, o serviço registra que algo aconteceu, e os interessados reagem. Eventos permitem que outros serviços observem e reajam no próprio ritmo, sem bloquear quem os publicou.

### Desenvolvimento conceitual

**[03:40–05:30 · Slide 5 — Comando, evento de domínio e notificação]**

Antes da infraestrutura, o vocabulário. São três tipos de mensagem, e a diferença entre eles é o acoplamento que cada um cria.

*[indicação de edição: inserir Recurso visual 37 da Aula 10 — quadro dos três tipos de mensagem, revelado linha a linha]*

Comando: expressa uma solicitação para que algo aconteça. Tem destinatário específico, que pode aceitar ou recusar. O acoplamento é direto — quem envia sabe quem recebe e espera uma aceitação.

Evento de domínio: é o registro de um fato que já ocorreu. Não tem destinatário em particular. O acoplamento é baixo — quem publica não sabe, nem precisa saber, quem consome.

Notificação: é um aviso leve de que algo aconteceu. Vai para os interessados, tem acoplamento baixo, e normalmente não carrega dados completos — ela convida o interessado a buscar mais informação.

O tempo verbal é a pista mais confiável para distingui-los. O comando está no imperativo: “reserve o estoque”. O evento está no passado: “estoque reservado”. Essa diferença gramatical carrega uma diferença arquitetural considerável.

Na NexaOrder, passamos a tratar pedido criado, estoque reservado, pagamento aprovado e pedido expedido como eventos de domínio, publicados por seus respectivos serviços.

**[05:30–07:10 · Slide 6 — Tópicos, partições e deslocamento]**

Passemos à infraestrutura, com quatro termos de uso permanente.

*[indicação de edição: inserir Recurso visual 38 da Aula 10 — tópico dividido em partições, com os deslocamentos crescentes visíveis]*

Tópico é um canal nomeado, organizado por tipo de evento ou por agregado de negócio. Produtores publicam eventos em um tópico e consumidores os leem. A diferença crucial em relação a uma fila tradicional está aqui: ler não remove a mensagem para os demais, de modo que vários serviços processam o mesmo evento de forma independente.

Partição é uma sequência ordenada e imutável de eventos, identificada por um deslocamento, o offset, que apenas cresce. A imagem adequada é a de um registro em que só se escreve na última linha, e cada linha recebe um número.

Chave é o que determina a partição de destino. Normalmente é o identificador do agregado — o número do pedido, por exemplo.

O efeito da chave é o ponto central: todos os eventos daquele pedido caem na mesma partição. A seção seguinte depende inteiramente dessa escolha.

**[07:10–08:40 · Slide 7 — Ordenação: uma garantia por partição]**

Esta é a regra que mais gera confusão em produção, e por isso merece enunciado explícito.

A plataforma garante ordem dentro de uma partição. Ela não garante ordem entre partições diferentes.

Com chave estável, o comportamento é o desejado: os eventos do pedido 4021 caem todos na mesma partição e são lidos exatamente na ordem publicada — criado, reservado, aprovado, expedido.

Entre pedidos diferentes, a ordem relativa pode variar. O pedido 4022 pode ser processado antes do 4021, o que em geral não representa problema, por se tratar de agregados distintos, sem relação causal entre si.

A chave inadequada, porém, compromete essa garantia. Particionando-se por tipo de evento — todos os “pedido criado” em uma partição, todos os “pagamento aprovado” em outra —, os eventos do mesmo pedido se espalham entre partições, e o consumidor pode observar “pagamento aprovado” antes de “pedido criado”.

Considere a situação do ponto de vista de quem consome: chega a aprovação de um pagamento referente a um pedido que, para ele, ainda não existe. É preciso decidir entre descartar, armazenar ou aguardar. Uma escolha de chave inadequada criou um problema de tratamento complexo.

**[08:40–10:20 · Slide 8 — Grupos de consumidores]**

Resta examinar como escalar o consumo.

*[indicação de edição: inserir Recurso visual 39 da Aula 10 — dois grupos de consumidores lendo o mesmo tópico, com as partições atribuídas em cores distintas]*

Um grupo de consumidores é um conjunto de instâncias que divide entre si as partições de um tópico, segundo uma regra simples: cada partição é atribuída a exatamente uma instância do grupo por vez.

Disso resulta escala horizontal. Em um tópico com 6 partições e um grupo de 3 consumidores, cada instância processa aproximadamente 2 partições.

Os grupos são independentes entre si. O painel operacional e o disparo de e-mails leem o mesmo tópico, cada um em seu próprio ritmo e com seu próprio deslocamento, de modo que o atraso de um não afeta o outro.

Quando uma instância falha, ocorre o rebalanceamento: suas partições são redistribuídas entre as remanescentes, e o sistema se recupera sem intervenção.

O custo do rebalanceamento, contudo, costuma passar despercebido no planejamento de capacidade. Passando-se de 3 instâncias para 2, com as mesmas 8 partições, a carga por instância aumenta, e a capacidade total pode inclusive cair até que uma nova réplica entre e o grupo rebalanceie novamente. A falha de um consumidor não degrada apenas a parte que lhe cabia: ela pressiona os remanescentes.

**[10:20–11:50 · Slide 9 — Exemplo numérico: quantas partições sustentam o pico?]**

O dimensionamento segue uma fórmula muito próxima à da Aula 1, o que não é coincidência.

O número mínimo de partições é o teto da divisão entre a taxa de eventos no pico e a capacidade de um consumidor.

Números da NexaOrder: 1200 eventos por segundo no pico; 150 eventos por segundo por consumidor. A conta: 1200 dividido por 150 dá exatamente 8. Portanto, 8 partições no mínimo.

Há uma consequência frequentemente negligenciada: esse número 8 é também o teto de paralelismo útil. Acrescentar um nono consumidor ao grupo não aumentaria o throughput, pois não haveria uma nona partição a lhe atribuir, e a instância permaneceria ociosa, consumindo recursos sem produzir trabalho.

O número de partições constitui, portanto, um limite estrutural de paralelismo. E, como aumentar partições posteriormente é operação delicada — pode alterar o mapeamento de chaves e a ordenação —, esse número deve ser definido com folga em relação à carga de pico esperada. Trata-se de um parâmetro barato de acertar no início e caro de corrigir depois.

**[11:50–12:10 · Slide 10 — Citação]**

Esta frase resume a mudança de perspectiva proposta pela aula: quem publica um evento não sabe, e não precisa saber, quem o consome.

### Demonstração, exemplo ou estudo de caso

**[12:10–13:50 · Slide 11 — Retenção e reprocessamento]**

Há uma diferença fundamental em relação a uma fila tradicional. Em uma fila, a mensagem desaparece após o consumo. Em uma plataforma de eventos, a mensagem é retida por um período configurável, independentemente de ter sido lida.

Isso viabiliza um recurso de grande valor: o reprocessamento.

*[indicação de edição: inserir Recurso visual 40 da Aula 10 — tabela de políticas de retenção, revelada linha a linha]*

Três políticas merecem comparação. Retenção de poucas horas: permite recuperação de falhas imediatas, mas praticamente elimina a possibilidade de correção retroativa. Retenção de sete dias: permite corrigir na segunda-feira um defeito reprocessando a semana anterior, a custo moderado de armazenamento. Retenção indefinida: oferece registro histórico completo, útil para auditoria, ao custo de armazenamento crescente no tempo.

O valor prático do caso de sete dias é evidente. Descobre-se na segunda-feira que o cálculo de frete estava incorreto desde quarta. Com retenção, corrige-se o código e reprocessam-se os eventos daquele período. Sem retenção, a reconstrução dos dados é manual.

Um ponto conceitual importante acompanha essa discussão. O log de eventos só pode ser tratado como fonte de verdade quando deliberadamente projetado para esse fim: com retenção suficiente, eventos completos e imutáveis, versionamento e garantias de durabilidade. Retenção longa, isoladamente, não transforma um tópico em banco de dados. É uma decisão de projeto, não um efeito colateral de configuração.

**[13:50–15:40 · Slide 12 — Três semânticas de entrega]**

O tema a seguir reaparece com nome novo, embora já tenha sido tratado na Unidade 2.

At-most-once: zero ou uma entrega. Nunca duplica, mas pode perder. Ocorre quando o consumidor confirma o recebimento antes de concluir o processamento — interrompido no meio, a mensagem consta como confirmada e o trabalho não foi realizado.

At-least-once: uma ou mais entregas. A duplicação é possível e esperada. Ocorre com publicação durável, retenção vigente e retentativas disponíveis. É a configuração comum na prática.

Exactly-once: um efeito observável por evento, dentro de uma fronteira declarada. O modo como se obtém esse resultado é decisivo: pela combinação de at-least-once com deduplicação ou idempotência no consumidor. Não se trata de propriedade automática da infraestrutura.

Segue a ressalva mais importante da aula, por ser fonte de erros custosos. O exactly-once não elimina duplicações na transmissão e não se estende automaticamente a efeitos fora da fronteira transacional. Ao chamar um provedor de pagamento externo, é necessária idempotência ponta a ponta, exatamente o que foi construído na Aula 8. Nenhuma configuração de plataforma impede que um provedor externo cobre duas vezes.

**[15:40–17:20 · Slide 13 — Evolução de esquemas e compatibilidade]**

Eventos publicados hoje podem ser lidos por serviços implantados semanas depois. Simultaneamente, um consumidor antigo pode continuar em produção enquanto o produtor já foi atualizado. As duas direções precisam funcionar.

Daí os dois tipos de compatibilidade. Compatibilidade retroativa, ou backward: o consumidor novo lê eventos publicados no esquema antigo. Compatibilidade prospectiva, ou forward: o consumidor antigo lê eventos do esquema novo, ignorando campos que não conhece.

A mudança segura é aditiva. Adicionar canal de venda como campo opcional não quebra ninguém: consumidores novos usam, consumidores antigos ignoram.

A mudança perigosa é renomear. Trocar valor total por valor líquido, sem transição, quebra a compatibilidade — o consumidor antigo procura um campo que não existe mais e recebe nulo, ou zero, ou uma exceção.

A regra prática é a seguinte: remover, renomear ou mudar o tipo de um campo exige estratégia explícita de migração. A mais comum consiste em publicar temporariamente nos dois formatos, migrar os consumidores um a um e só então remover o campo antigo. O procedimento é trabalhoso, e esse é o preço de manter consumidores que não estão sob o controle de quem publica.

### Aplicação profissional

**[17:20–19:00 · Slide 14 — O ciclo do pedido reorganizado]**

Os elementos da aula se reúnem no desenho completo do ciclo.

*[indicação de edição: inserir Recurso visual 41 da Aula 10 — fluxo do ciclo do pedido reorganizado por eventos, com os tópicos e as reações destacados]*

Nenhum serviço chama o seguinte de forma síncrona e bloqueante. Cada um reage a fatos publicados, no seu próprio ritmo.

Pedidos recebe um comando síncrono do cliente — e aqui a comunicação síncrona se justifica, pois o cliente precisa saber se o pedido foi aceito —, valida e publica o evento pedido criado.

Estoque consome esse evento, tenta reservar e publica estoque reservado ou estoque indisponível.

Pagamento consome estoque reservado e publica pagamento aprovado ou pagamento recusado.

Expedição consome pagamento aprovado e publica pedido expedido.

A comparação com a cadeia síncrona da abertura é elucidativa. Com a expedição indisponível por dez minutos, o pedido é criado, o estoque é reservado e o pagamento é aprovado; a expedição processa quando retornar. O cliente não perde a compra em razão de um serviço que sequer participa da decisão de vender.

Quanto às chaves, adota-se o identificador do pedido, de modo que todos os eventos de um mesmo pedido mantenham a ordem. E as pré-condições de negócio permanecem válidas, conforme discutido na Aula 2: desacoplamento não autoriza expedir antes de cobrar.

### Fechamento

**[19:00–19:40 · Slides 15 e 16 — Pontos-chave e atividade prática]**

Recapitulando. Três tipos de mensagem: comando acopla ao destinatário, evento de domínio registra um fato sem destinatário e notificação apenas avisa. A ordem é por partição: só existe garantia dentro de uma partição, e a chave decide o que permanece ordenado. Partições limitam a escala: o paralelismo útil de um grupo nunca ultrapassa o número de partições do tópico. Retenção habilita correção: reter eventos permite reprocessar e reconstruir estado, com custo de armazenamento proporcional. Duplicata é o normal: at-least-once é a configuração comum, e o efeito único é responsabilidade do desenho do consumidor. E esquema evolui aditivamente: campos opcionais preservam compatibilidade, enquanto remover ou renomear exige migração explícita.

Na atividade prática, você vai desenhar tópicos, chaves e grupos de consumidores para o ciclo de vida do pedido: listar no mínimo quatro eventos de domínio, definir tópico e chave de particionamento de cada um, justificar a chave em termos da ordenação necessária, definir dois grupos de consumidores distintos lendo o mesmo tópico com finalidades diferentes, calcular o número mínimo de partições para uma taxa de pico hipotética e indicar a semântica de entrega que cada consumidor deveria adotar.

**[19:40–20:00 · Slide 17 — Encerramento]**

Esta aula forma a capacidade de desacoplar o ciclo do pedido com eventos, chaves e grupos de consumidores, e de dimensionar o paralelismo daí decorrente. A próxima aula desce uma camada: como esses serviços são executados, escalados e recuperados automaticamente.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 10 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com a cadeia síncrona quebrando em um elo (02:20–03:40).
- Recurso visual 37 — quadro dos três tipos de mensagem (aproximadamente 03:50).
- Recurso visual 38 — tópico dividido em partições, com deslocamentos crescentes (aproximadamente 05:40).
- Slide 7 — comparação entre chave por pedido e chave por tipo de evento (aproximadamente 07:20).
- Recurso visual 39 — dois grupos de consumidores lendo o mesmo tópico (aproximadamente 08:50).
- Slide 9 — cálculo do número mínimo de partições, com o consumidor ocioso destacado (aproximadamente 10:30).
- Slide 10 — citação em tela cheia (11:50).
- Recurso visual 40 — tabela de políticas de retenção (aproximadamente 12:20).
- Recurso visual 41 — ciclo do pedido reorganizado por eventos (aproximadamente 17:30).
- Slide 17 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- KREPS, Jay. *I heart logs: event data, stream processing, and data integration*. Sebastopol: O’Reilly Media, 2014 — referência conceitual, sem reprodução de trecho externo.
- HOHPE, Gregor; WOOLF, Bobby. *Enterprise Integration Patterns*. Boston: Addison-Wesley, 2003 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, tabelas e fluxos devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 10 (`unidade_3.md`) e do deck `unidade_3/slides/aula10.html`.

---

## Roteiro da Videoaula 11 — “A instância que se recupera sozinha (e a que não deveria)”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 11 — Contêineres, Kubernetes e reconciliação.

**Deck de apoio:** `unidade_3/slides/aula11.html` — 19 slides (capa, audiodescrição, sumário, 15 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar o que a imutabilidade de imagens garante e o que não garante, distinguir os papéis de Pod, Deployment e Service, descrever o laço de reconciliação, diferenciar sonda de vivacidade de sonda de prontidão, calcular o número de réplicas de um escalonamento automático e reconhecer quando a recuperação automática está mascarando um defeito determinístico.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:40 imagem e contêiner · 05:10 objetos do Kubernetes · 06:50 estado desejado e observado · 08:20 laço de reconciliação · 09:50 limite da automação · 11:10 sondas · 12:40 citação · 13:00 descoberta e configuração · 14:20 exemplo numérico do autoescalonamento · 15:40 atualização gradual · 17:20 pausa para reflexão · 19:00 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 11, dedicada a contêineres, Kubernetes e reconciliação. A aula se abre com um episódio aparentemente favorável que, examinado de perto, revela um problema relevante.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o diagrama de imagem e contêineres em execução, a tabela dos objetos centrais do Kubernetes, o manifesto declarativo em bloco de código, o diagrama do laço de reconciliação em três passos e a linha do tempo da atualização gradual. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo por imagem, contêiner e imutabilidade. Apresento depois os objetos centrais do Kubernetes — cluster, nó, Pod, Deployment e Service. Chego então ao núcleo da aula: estado desejado e estado observado, e o laço de reconciliação que os aproxima. Trato das sondas de vivacidade, prontidão e inicialização, de descoberta, balanceamento e configuração, e fecho com escalonamento automático horizontal e atualizações graduais sem perder capacidade.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir explicar o que a imutabilidade de imagens garante — e, igualmente importante, o que ela não garante. Deve distinguir os papéis de Pod, Deployment e Service em uma mesma aplicação. Deve descrever o laço de reconciliação entre estado desejado e observado. Deve diferenciar sonda de vivacidade de sonda de prontidão pelo efeito de cada falha. Deve calcular o número de réplicas resultante de um escalonamento automático horizontal. E deve reconhecer quando a recuperação automática está mascarando um defeito determinístico.

**[02:20–03:40 · Slide 4 — Situação-problema]**

O episódio é o seguinte. Em uma madrugada de alta demanda, uma instância do serviço de pagamento trava e deixa de responder. Minutos depois, sem qualquer intervenção humana, uma nova instância surge, assume o tráfego, e o incidente quase passa despercebido.

O resultado parece inteiramente positivo, e em parte é. Três perguntas, porém, se impõem.

Primeira: quem decidiu recriar a instância? Segunda: como o sistema sabia que ela deveria existir? Terceira, e a mais relevante: e se a causa do travamento for um defeito que se repete a cada reinício?

A recuperação não é automática por natureza. Ela resulta de um laço de reconciliação em execução contínua. Compreender esse laço é o que permite diferenciar uma recuperação saudável de um sintoma mascarado.

### Desenvolvimento conceitual

**[03:40–05:10 · Slide 5 — Imagem, contêiner e imutabilidade]**

Comecemos pelos fundamentos.

Imagem é um pacote autocontido, com código, dependências e instruções de execução, construído em camadas imutáveis. Contêiner é uma instância em execução dessa imagem, isolada em processos, sistema de arquivos e, em geral, rede.

A diferença em relação a uma máquina virtual está em que o contêiner compartilha o núcleo do sistema operacional do hospedeiro. Ele não carrega um sistema operacional inteiro, e por isso é mais leve e inicia em segundos.

A imutabilidade tem consequência operacional direta: em vez de corrigir uma instância em execução, publica-se uma nova imagem e substituem-se os contêineres. Não se acessa a máquina para consertá-la; substitui-se a máquina.

Cabe, porém, uma qualificação frequentemente omitida no material de divulgação. A imutabilidade reduz a divergência do artefato de aplicação entre ambientes — o binário que executa em produção é o mesmo que executou em teste. Ela não elimina diferenças de configuração, de infraestrutura, de dados, de arquitetura do host ou de serviços externos. Essas variáveis permanecem e continuam exigindo controle e teste.

A discrepância entre ambientes torna-se menos provável, portanto, mas não desaparece.

**[05:10–06:50 · Slide 6 — Os objetos centrais do Kubernetes]**

Cinco objetos respondem por praticamente toda a execução, e cada um será apresentado com o exemplo correspondente na NexaOrder.

*[indicação de edição: inserir Recurso visual 42 da Aula 11 — tabela dos objetos centrais, revelada linha a linha]*

Cluster: o conjunto de máquinas gerenciadas como uma unidade. Na NexaOrder, é o ambiente inteiro da plataforma.

Nó: a máquina física ou virtual que executa contêineres. Cada servidor do cluster.

Pod: a menor unidade implantável — um ou mais contêineres que compartilham rede e armazenamento local. Na NexaOrder, um Pod é uma instância do serviço de pagamento.

Deployment: declara quantas réplicas devem existir e como atualizá-las. Na NexaOrder, quatro réplicas de pagamento.

Service: expõe um conjunto de Pods sob um endereço de rede estável. É o endereço que o estoque usa para alcançar o pagamento — e que não muda quando os Pods são substituídos.

Essa última distinção é fonte frequente de confusão e merece registro: o Deployment cuida de quantos e de qual versão; o Service cuida de como ser encontrado.

**[06:50–08:20 · Slide 7 — Estado desejado e estado observado]**

Chegamos ao conceito que reorganiza a forma de pensar a operação.

O usuário não instrui passo a passo. Ele declara o resultado desejado e delega ao sistema a tarefa de alcançá-lo e mantê-lo. Esse é o modelo declarativo, oposto ao modelo imperativo, em que se determina criar uma máquina, instalar componentes e iniciar processos em sequência.

*[indicação de edição: exibir o manifesto do Deployment em bloco de código, destacando a linha “replicas: 4” conforme a narração]*

O manifesto exibido na tela declara: tipo Deployment, nome pagamento, réplicas quatro, imagem nexaorder barra pagamento, versão 1.7.0. Trata-se de uma declaração de intenção, e não de uma sequência de comandos.

O ponto central é o seguinte. Se, por qualquer motivo, restarem três dos quatro Pods, há divergência entre o estado desejado — quatro — e o estado observado — três. É essa divergência que aciona a reconciliação.

Não é necessário que alguém perceba a diferença e atue. A discrepância entre o declarado e o real é, por si só, o gatilho.

**[08:20–09:50 · Slide 8 — Controladores e o laço de reconciliação]**

Esse trabalho cabe ao controlador. Um controlador observa o estado atual, compara-o com o desejado e age para reduzir a diferença.

O detalhe fundamental é que o laço não executa uma única vez: ele executa indefinidamente, em ciclos curtos.

*[indicação de edição: inserir Recurso visual 43 da Aula 11 — diagrama circular do laço de reconciliação, com os três passos animados em sequência]*

São três passos, em círculo. Primeiro, observar: qual é a condição real do cluster neste momento? Segundo, comparar: em que ela diverge do que foi declarado? Terceiro, agir: executar o que reduz essa diferença. E o ciclo recomeça, continuamente.

A situação-problema comporta dois casos concretos. Se um Pod é removido, o controlador observa três dos quatro e cria outro. Se o processo travou dentro de um Pod que permanece ativo, e a sonda de vivacidade está falhando, o kubelet reinicia o contêiner dentro do mesmo Pod.

Ambos produzem recuperação automática, mas atuam em níveis diferentes: um recria o Pod, o outro reinicia o contêiner. Identificar qual dos dois ocorreu é essencial para diagnosticar um incidente.

**[09:50–11:10 · Slide 9 — O limite da automação]**

Chegamos à parte crítica da aula.

O que o laço restaura é a quantidade e o estado de execução declarados. Ele garante que existam quatro Pods em execução.

O que ele não resolve é a causa raiz de uma falha recorrente. O laço não identifica por que o Pod travou, e essa informação não integra seu escopo.

Considere o cenário do reinício em ciclo. Se o Pod trava por um defeito de código que se manifesta sob determinada carga, o Kubernetes o recriará indefinidamente: trava, recria, trava, recria.

O risco principal não é a indisponibilidade, e sim o mascaramento. O problema permanece oculto precisamente porque a disponibilidade aparenta estar preservada. Os indicadores permanecem normais, nenhum alerta é acionado, e o defeito segue em produção por meses.

A conclusão a fixar é esta: reconciliação automática é um mecanismo de disponibilidade, não uma prova de correção. Vale aqui o mesmo raciocínio aplicado aos timeouts na Aula 4 — um mecanismo que responde ao sintoma não é um mecanismo que diagnostica a causa.

**[11:10–12:40 · Slide 10 — Como o cluster percebe que algo não vai bem]**

As sondas são o meio pelo qual o cluster avalia a saúde de um Pod. São três, e confundi-las provoca incidentes concretos.

Sonda de vivacidade, ou liveness: verifica se o contêiner ainda consegue progredir. Quando ela falha, o kubelet reinicia o contêiner, conforme a política do Pod. É uma ação drástica.

Sonda de prontidão, ou readiness: verifica se o Pod está apto a receber tráfego. Quando ela falha, o Pod segue executando normalmente, mas sai dos destinos prontos do Service. Ele para de receber requisições, mas não é reiniciado. É uma ação suave.

Sonda de inicialização, ou startup: verifica se uma aplicação lenta ainda está subindo. Ela protege a partida, evitando que a sonda de vivacidade dispare reinícios prematuros em uma aplicação que só demora a inicializar.

Um alerta de projeto merece destaque: as sondas devem verificar sinais úteis, sem converter uma dependência externa instável em reinícios em cascata por todo o cluster. Uma sonda de vivacidade que consulta o banco de dados faz com que uma lentidão no banco reinicie todos os Pods simultaneamente, transformando uma degradação em colapso. É o mesmo raciocínio de isolamento da Aula 4.

**[12:40–13:00 · Slide 11 — Citação]**

Esta frase constitui o eixo da aula: reconciliação automática é um mecanismo de disponibilidade, não uma prova de correção.

### Demonstração, exemplo ou estudo de caso

**[13:00–14:20 · Slide 12 — Descoberta, balanceamento, configuração e dados]**

Alguns elementos complementares resolvem problemas práticos recorrentes.

Pods são voláteis: recebem endereços internos que mudam a cada substituição. Por isso o endereço de um Pod nunca deve ser armazenado.

O Service resolve isso: ele associa um nome estável e um endereço fixo aos Pods selecionados por rótulos, distribuindo tráfego entre os saudáveis. É a camada de indireção que torna a volatilidade dos Pods invisível para quem chama.

Para configuração, existem os ConfigMaps: configuração não sensível, injetada em tempo de execução. E os Secrets, para dados sensíveis.

Um detalhe operacional costuma passar despercebido: variáveis de ambiente não se alteram em um processo já iniciado. Alterado um Secret exposto como variável de ambiente, o Pod permanece com o valor antigo até ser reiniciado de forma controlada. Volumes projetados, por sua vez, recebem atualização eventual, mas a aplicação precisa reler o arquivo para percebê-la. Alterar o valor, portanto, não significa que a aplicação passou a utilizá-lo.

E, para dados, o armazenamento persistente vincula um volume ao ciclo de vida da aplicação, e não ao do Pod — cujo disco local é efêmero e desaparece com ele.

**[14:20–15:40 · Slide 13 — Exemplo numérico: escalonamento automático horizontal]**

Passemos à primeira conta.

O escalonador automático horizontal calcula o número desejado de réplicas assim: o teto do produto entre o número atual de réplicas e a razão da utilização observada pela utilização-alvo.

Números da NexaOrder: 4 réplicas atuais, CPU observada em 85%, CPU alvo de 60%.

A conta: 4 vezes 85 dividido por 60, que dá 5,67. Arredondando para cima: 6 réplicas desejadas.

Vale observar como os mecanismos se articulam. O autoescalonador não cria Pods; apenas ajusta o campo de réplicas no Deployment, de 4 para 6. A partir daí, o laço de reconciliação identifica a divergência — desejado 6, observado 4 — e se encarrega de criar os dois novos Pods.

São dois mecanismos independentes, cada um operando em seu nível, que compõem um comportamento aparentemente único. Nisso reside a elegância do modelo declarativo.

**[15:40–17:20 · Slide 14 — Atualização gradual sem perder capacidade]**

A segunda conta trata de implantação.

*[indicação de edição: inserir Recurso visual 44 da Aula 11 — linha do tempo da atualização gradual, com a contagem de Pods variando entre 5 e 7]*

Considere um Deployment de 6 réplicas, configurado para no máximo 1 indisponível e 1 excedente durante a transição.

O processo é o seguinte. Primeiro, cria-se 1 Pod com a versão nova, totalizando 7 Pods, sendo 6 antigos e 1 novo. Segundo, aguarda-se que o Pod novo seja aprovado na sonda de prontidão. Terceiro, remove-se 1 Pod antigo, retornando a 6 no total. Quarto, repete-se o ciclo até que todas as réplicas estejam na versão nova.

O efeito é que a capacidade saudável nunca cai abaixo de 5 nem ultrapassa 7. A versão inteira do serviço é substituída sem impacto perceptível para o cliente.

Se o Pod novo falhar repetidamente na sonda de prontidão, o avanço é interrompido: a atualização cessa, preservando os Pods antigos em funcionamento, o que constitui comportamento desejável.

Um detalhe, contudo, é frequentemente presumido de forma incorreta: o Deployment não realiza rollback automático por padrão. A implantação fica interrompida, mas não retorna à versão anterior por conta própria. A equipe, ou uma automação externa, precisa observar a condição de progresso e decidir entre pausar e reverter. Sem esse acompanhamento, a implantação permanece parcialmente concluída por tempo indeterminado.

### Aplicação profissional

**[17:20–19:00 · Slide 15 — Pausa para reflexão: robustez ou mascaramento?]**

A aula se encerra com uma reflexão. Pause o vídeo antes de prosseguir.

O reinício em ciclo de um Pod é, simultaneamente, evidência da robustez do laço de reconciliação e risco de ocultar defeitos. As duas leituras são verdadeiras.

*[indicação de edição: pausar a narração por 10 segundos com o texto “Robustez ou mascaramento?” na tela]*

Quatro perguntas orientam a análise: além da constatação de que o serviço está no ar, que sinais revelariam que um Pod está sendo recriado repetidamente? Um Pod que trava sob alta carga e é recriado com sucesso está, do ponto de vista de negócio, resolvido? Qual é a diferença entre tolerar falhas transitórias e, sem percebê-lo, ocultar um defeito determinístico? E como alertas de reinício, o parâmetro de prazo de progresso e automação externa interromperiam uma implantação defeituosa?

Um dado técnico fundamenta a resposta: um Deployment não oferece número máximo de reinícios, como os Jobs oferecem por meio do limite de tentativas. A interrupção depende de política operacional declarada pela equipe. Sem a configuração do alerta correspondente, nenhuma notificação será emitida.

A prática profissional a reter é a seguinte: a contagem de reinícios deve ser monitorada como sinal de primeira classe, no mesmo nível de latência e taxa de erro. Um serviço que reinicia trinta vezes por dia e mantém 99,9% de disponibilidade não está saudável; está sendo sustentado pela plataforma.

### Fechamento

**[19:00–19:40 · Slides 16 e 17 — Pontos-chave e atividade prática]**

Recapitulando. Imutável, mas não igual: a imagem reduz a divergência do artefato, enquanto configuração, dados e dependências externas ainda variam. Cinco objetos bastam: cluster, nó, Pod, Deployment e Service organizam praticamente toda a execução. Declare o resultado: o laço de reconciliação compara desejado e observado e age continuamente para aproximá-los. Disponibilidade não é correção: a recuperação automática restaura quantidade e execução, nunca a causa raiz. Sondas decidem o destino: vivacidade reinicia o contêiner, prontidão apenas retira o Pod do tráfego. E capacidade preservada: escalonamento e atualização gradual ajustam réplicas e versão sem derrubar o serviço.

Na atividade prática, você vai interpretar manifestos e cenários de recuperação: descrever o que ocorre se dois Pods terminarem, descrever separadamente o que ocorre se dois Pods apenas falharem na prontidão, calcular réplicas de um autoescalonador para seis réplicas com 92% observados e 65% de alvo, descrever um cenário plausível de reinício em loop para o estoque, propor um sinal de observabilidade que revelaria o problema antes de afetar clientes e explicar a diferença entre o papel do Deployment e o do Service.

**[19:40–20:00 · Slide 18 — Encerramento]**

Esta aula estabelece como o cluster mantém suas instâncias em funcionamento e quando essa automação está ocultando um defeito. A última aula da unidade trata do tráfego entre esses serviços: identidade, criptografia e autorização.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 11 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com a instância travando e sendo substituída (02:20–03:40).
- Recurso visual 42 — tabela dos objetos centrais do Kubernetes (aproximadamente 05:20).
- Slide 7 — manifesto declarativo em bloco de código, com “replicas: 4” em destaque (aproximadamente 07:00).
- Recurso visual 43 — diagrama circular do laço de reconciliação, com os três passos animados (aproximadamente 08:30).
- Slide 11 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (12:40).
- Slide 13 — cálculo do escalonamento automático, com os quatro números em sequência (aproximadamente 14:30).
- Recurso visual 44 — linha do tempo da atualização gradual, mostrando a contagem entre 5 e 7 Pods (aproximadamente 15:50).
- Slide 15 — pausa de reflexão de 10 segundos (aproximadamente 17:40).
- Slide 18 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- BURNS, Brendan; BEDA, Joe; HIGHTOWER, Kelsey. *Kubernetes: Up and Running*. 3. ed. Sebastopol: O’Reilly Media, 2022 — referência conceitual, sem reprodução de trecho externo.
- BEYER, Betsy et al. (org.). *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol: O’Reilly Media, 2016 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, manifestos e linhas do tempo devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 11 (`unidade_3.md`) e do deck `unidade_3/slides/aula11.html`.

---

## Roteiro da Videoaula 12 — “Qualquer serviço pode falar com qualquer serviço?”

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 12 — Segurança e comunicação confiável entre serviços.

**Deck de apoio:** `unidade_3/slides/aula12.html` — 18 slides (capa, audiodescrição, sumário, 14 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de contrapor segurança de perímetro e confiança zero, separar autenticação de autorização aplicando menor privilégio, explicar o que o TLS mútuo garante e o que não garante, justificar a gestão externa de segredos pelo tempo de resposta a incidente, dimensionar um limitador por balde de fichas e reconhecer ameaças que exploram propriedades já estudadas.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 perímetro e confiança zero · 05:30 autenticação e autorização · 07:00 TLS e TLS mútuo · 08:40 gestão de segredos · 10:20 citação · 10:40 gateway, proxy lateral e mesh · 12:30 exemplo numérico do balde de fichas · 14:20 quatro ameaças · 16:20 fluxo autenticado · 17:40 transição para a Unidade 4 · 19:00 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a última aula da Unidade 3, dedicada à segurança e à comunicação confiável entre serviços. A pergunta que dá título à aula é aparentemente elementar, mas revela um problema estrutural presente em muitas arquiteturas reais.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o contraste entre perímetro e confiança zero, o diagrama do TLS mútuo com dois certificados, a tabela de tempo de contenção de segredos, o diagrama do proxy lateral interceptando tráfego e o quadro das quatro ameaças com suas mitigações. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo contrapondo segurança de perímetro e confiança zero. Separo depois autenticação de autorização e apresento o princípio do menor privilégio. Trato em seguida de TLS e TLS mútuo na comunicação interna, e da gestão e rotação de segredos. Examino gateway, proxy lateral e service mesh, dimensiono um limitador de taxa por balde de fichas, apresento quatro ameaças específicas de sistemas distribuídos e fecho montando um fluxo autenticado de ponta a ponta.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir contrapor segurança de perímetro e confiança zero em uma arquitetura de serviços. Deve separar autenticação de autorização e aplicar o princípio do menor privilégio. Deve explicar o que o TLS mútuo garante e o que ele deliberadamente não garante. Deve justificar a gestão externa de segredos pelo tempo de resposta a um incidente. Deve dimensionar um limitador de taxa por balde de fichas, distinguindo pico de regime permanente. E deve reconhecer ameaças que exploram propriedades já estudadas de comunicação e de falha.

**[02:20–03:50 · Slide 4 — Situação-problema]**

Uma revisão de segurança na NexaOrder revela um risco que estava à vista o tempo todo.

Nada impede que a expedição chame o serviço de pagamento e solicite um reembolso, operação jamais prevista para ela. Não se trata de permissão excessivamente ampla: não existe verificação alguma. Conhecido o endereço, a chamada se realiza.

A comunicação interna ocorre em texto claro dentro do cluster. Não há verificação de identidade além do endereço de rede, e endereço de rede não é identidade, e sim localização. As credenciais do provedor de pagamento, por sua vez, estão em um arquivo de configuração versionado, ou seja, no histórico do repositório, acessível a qualquer pessoa com acesso ao código.

Confiabilidade, neste contexto, é noção mais ampla do que disponibilidade. É confiar que a mensagem vem de quem diz vir, que ela não foi alterada no caminho, que cada serviço só faz o que lhe é explicitamente permitido e que segredos não ficam expostos por conveniência operacional.

### Desenvolvimento conceitual

**[03:50–05:30 · Slide 5 — Perímetro e confiança zero]**

O primeiro deslocamento conceitual da aula é o seguinte.

O modelo de perímetro parte da premissa de que tudo dentro da rede interna é relativamente confiável, e concentra a proteção na borda. É o modelo da fortificação: quem ultrapassou o portão está dentro.

Esse modelo falha em uma arquitetura de serviços porque, com dezenas de serviços e múltiplos times, um único componente comprometido obtém acesso amplo. Basta uma vulnerabilidade em um serviço periférico — o de recomendações, por exemplo — para que o atacante alcance o de pagamento.

A alternativa é a confiança zero. O princípio é: nenhuma requisição é confiável apenas por vir de dentro da rede.

Isso se concretiza em duas exigências. Primeira: identidade verificável — cada serviço tem certificado ou token criptográfico associado a ele, e não ao seu endereço de rede. A identidade viaja com o serviço, não com o IP. Segunda: toda comunicação é autenticada, mesmo entre serviços do mesmo cluster, como se cada chamada cruzasse uma fronteira não confiável.

A referência formal do tema é a publicação especial do NIST sobre arquitetura de confiança zero, leitura recomendada para quem for implementá-la profissionalmente.

**[05:30–07:00 · Slide 6 — Autenticação, autorização e menor privilégio]**

Duas perguntas são frequentemente confundidas, e nenhuma delas substitui a outra.

Autenticação responde: quem está fazendo esta requisição? Autorização responde: o que essa identidade tem permissão para fazer?

São perguntas independentes, articuladas pelo princípio do menor privilégio: cada identidade recebe apenas as permissões estritamente necessárias.

Na NexaOrder, a expedição autentica-se como “expedição” e é autorizada apenas a consultar status e confirmar envio.

O ponto que resolve a situação-problema é este: um serviço pode estar corretamente autenticado e ainda assim não ter autorização para uma operação específica. O reembolso continua fora do alcance da expedição, mesmo que a rede permita a chamada, mesmo que o certificado seja válido, mesmo que ela esteja dentro do cluster.

Autenticação sem autorização equivale a conferir a identidade de quem entra no prédio e, em seguida, permitir o acesso irrestrito a todos os andares.

**[07:00–08:40 · Slide 7 — TLS e TLS mútuo]**

Passemos à criptografia em trânsito.

*[indicação de edição: inserir Recurso visual 45 da Aula 12 — comparação entre TLS tradicional, com um certificado, e TLS mútuo, com dois]*

TLS protege dados em trânsito contra leitura e alteração por terceiros, com criptografia entre as duas pontas. É o mecanismo já empregado em qualquer acesso a um site com conexão segura.

No TLS tradicional da web, apenas o servidor apresenta certificado. O navegador verifica a identidade do banco; o banco não verifica a identidade do usuário por certificado.

No TLS mútuo, o mTLS, ambas as partes apresentam certificados e verificam a identidade uma da outra. É essa reciprocidade que se aplica adequadamente à comunicação entre serviços.

O que o mTLS resolve: o serviço de pagamento passa a autenticar criptograficamente a identidade de quem o chamou. A verificação deixa de basear-se na origem de rede e passa a fundar-se no certificado apresentado.

O que ele não resolve — e esta é a distinção mais importante da aula — é a permissão: uma política de autorização separada decide se aquela identidade pode executar a operação. O certificado prova quem é; não determina o que pode.

A conclusão é dupla: estar na mesma rede não basta, e possuir certificado válido tampouco concede, por si só, permissão de reembolso.

**[08:40–10:20 · Slide 8 — Gestão de segredos: por que o cofre importa]**

Credenciais, chaves de API e certificados não devem permanecer em imagens, arquivos versionados ou variáveis definidas manualmente. O consenso quanto a esse princípio é amplo em tese; o argumento decisivo, porém, aparece no momento do incidente.

*[indicação de edição: inserir Recurso visual 46 da Aula 12 — tabela comparando o tempo até a contenção nos dois cenários]*

Cenário um: o segredo está embutido na imagem e constata-se seu vazamento. Para substituí-lo, é preciso publicar uma nova imagem, testar e reimplantar todos os Pods afetados. Tempo até a contenção: horas. Durante esse período, a credencial exposta permanece válida e utilizável pelo atacante.

Cenário dois: o segredo está em um gestor de segredos com rotação. Para substituí-lo, basta rotacionar o valor, e o Pod consulta o segredo atual quando necessário. Tempo até a contenção: segundos, sem qualquer nova publicação de imagem.

Além da velocidade, um gestor de segredos controla acesso, registra auditoria de uso e permite rotação periódica preventiva.

É essa diferença de velocidade de resposta que costuma determinar se um incidente fica contido ou se prolonga por dias. A pergunta pertinente a uma equipe não é se os segredos estão seguros, e sim em quanto tempo é possível invalidar uma credencial comprometida.

**[10:20–10:40 · Slide 9 — Citação]**

Esta frase separa identidade de permissão: estar na mesma rede não basta; possuir um certificado válido também não concede, por si só, permissão para reembolsar ou cobrar.

### Demonstração, exemplo ou estudo de caso

**[10:40–12:30 · Slide 10 — Gateway, proxy lateral e service mesh]**

Há um problema prático a resolver: implementar autenticação, criptografia, limitação de taxa e autorização dentro do código de cada serviço é custoso e propenso a inconsistências. Cada time adota uma abordagem própria, e uma correção de segurança passa a exigir alterações em dezenas de repositórios.

*[indicação de edição: inserir Recurso visual 47 da Aula 12 — Pod com aplicação e proxy lateral, com todo o tráfego passando pelo proxy]*

A solução estrutural é o proxy lateral, o sidecar: um processo auxiliar que roda junto a cada instância, no mesmo Pod, e intercepta todo o tráfego de entrada e de saída.

O ganho é direto: as políticas se aplicam de forma uniforme, sem que a aplicação precise implementá-las. O código do serviço de pagamento não contém referência alguma a certificados.

O service mesh constitui o passo seguinte: proxies laterais coordenados por um plano de controle que distribui configuração, certificados e políticas a todos eles.

Os papéis se complementam. O gateway protege a borda voltada a clientes externos; o proxy lateral protege a comunicação interna. Não são concorrentes, e atuam em posições distintas.

O resultado prático para a NexaOrder é que aplicar mTLS entre todos os serviços não exige alterar o código de pedidos, estoque, pagamento e expedição. Adicionalmente, o mesh produz métricas uniformes de comunicação entre todos os serviços, tema retomado na primeira aula da Unidade 4.

**[12:30–14:20 · Slide 11 — Exemplo numérico: balde de fichas]**

A conta desta aula trata da proteção contra sobrecarga.

O algoritmo do balde de fichas funciona assim: um balde de capacidade C é reabastecido a uma taxa r de fichas por segundo. Cada requisição consome uma ficha, e requisições que chegam sem ficha disponível são recusadas ou colocadas em espera.

A leitura do modelo é direta: a taxa sustentável de longo prazo é r, e o pico instantâneo absorvido é C. Um parâmetro controla o regime permanente; o outro controla a rajada.

Os números do exemplo são estes. Capacidade do balde: 50 fichas. Taxa de reposição: 20 fichas por segundo. Chegam 90 requisições em 1 segundo.

O balde absorve as primeiras 50 imediatamente, por estarem acumuladas. As 40 restantes são recusadas ou atrasadas até que novas fichas sejam repostas, o que ocorre à taxa de 20 por segundo.

O objetivo do mecanismo não é penalizar o cliente responsável pela rajada, e sim proteger o serviço de uma sobrecarga que comprometeria a disponibilidade para todos os chamadores, e não apenas para a origem da rajada. Sem limitação, uma única origem descontrolada indisponibiliza o serviço para todos — efeito, aliás, que um atacante busca deliberadamente.

**[14:20–16:20 · Slide 12 — Quatro ameaças que exploram a distribuição]**

Quatro ameaças são específicas de sistemas distribuídos, e todas retomam conceitos já estudados.

*[indicação de edição: inserir Recurso visual 48 da Aula 12 — quadro das quatro ameaças com suas mitigações, revelado linha a linha]*

Repetição, ou replay: uma mensagem legítima é capturada e reenviada para produzir efeito indevido. Uma cobrança válida, reenviada dez vezes. A mitigação combina identificador único persistido, janela de validade, verificação de integridade e rejeição atômica de identificadores já consumidos.

Movimento lateral: um serviço de baixo privilégio é comprometido e usado para alcançar serviços sensíveis. É exatamente a falha do modelo de perímetro. A mitigação é autenticação mútua e menor privilégio entre todos os serviços, e não só na borda.

Amplificação por retry: repetição agressiva transforma uma indisponibilidade parcial em sobrecarga generalizada. A mitigação é backoff, jitter e orçamento de tentativas, conforme apresentado na Aula 2.

Exposição de segredos: segredos em imagens, logs ou repositórios tornam-se acessíveis muito além do escopo pretendido. A mitigação é o gestor de segredos com rotação e auditoria.

Um padrão atravessa as quatro ameaças: todas reinterpretam, sob ótica adversarial, conceitos já estudados. O replay explora a mesma ausência de identificação de operação que motivou a idempotência. A amplificação reproduz, com intenção maliciosa, o mesmo efeito manada tratado antes como problema acidental. Segurança, neste contexto, não constitui assunto à parte: é a mesma engenharia, com um adversário incluído no modelo.

### Aplicação profissional

**[16:20–17:40 · Slide 13 — Um fluxo autenticado: pedidos para pagamento]**

Os elementos da aula se reúnem no desenho de um fluxo completo.

Uma chamada do serviço de pedidos ao de pagamento deveria atravessar, no mínimo, quatro verificações.

Primeira, TLS mútuo: ambos os lados apresentam certificados válidos, emitidos por uma autoridade confiável do cluster. Essa camada responde à questão da identidade.

Segunda, autorização: a identidade “pedidos” pode solicitar autorizações de pagamento, mas não reembolsos. Essa camada responde à questão da permissão.

Terceira, limitação de taxa: aplicada pelo proxy lateral do serviço de pagamento, protegendo-o de sobrecarga, inclusive da sobrecarga acidental provocada por um defeito no próprio serviço de pedidos.

Quarta, identificador único: anexado à requisição, permite rejeitar repetições indevidas. É a idempotência da Aula 2, cumprindo agora também um papel de segurança.

As quatro camadas são independentes e cumulativas. A falha em qualquer uma delas deixa uma via de acesso desprotegida, e nenhuma compensa a ausência das demais.

**[17:40–19:00 · Slide 14 — Transição para a Unidade 4]**

Cabe articular a unidade e o conjunto da disciplina.

Com serviços delimitados, comunicação orientada a eventos, execução orquestrada e comunicação segura, a arquitetura da NexaOrder está estruturalmente completa.

A Unidade 4 desloca a pergunta de como construir para como verificar que o sistema funciona.

Como enxergar o sistema por dentro, com logs, métricas e rastreamento distribuído? Como provar que a resiliência que desenhamos na Unidade 1 realmente funciona, com testes e engenharia do caos? Como processar grandes volumes em lote e em fluxo? E como avaliar e evoluir a arquitetura a partir de requisitos e indicadores?

Há aqui uma mudança de posição: até este ponto, o papel exercido foi o de quem constrói. Na Unidade 4, soma-se a ele o papel de quem opera, mede e questiona o que foi construído.

### Fechamento

**[19:00–19:40 · Slides 15 e 16 — Pontos-chave e atividade prática]**

Recapitulando. Perímetro não basta: confiança zero trata cada requisição interna como se cruzasse uma fronteira não confiável. Duas perguntas distintas: autenticação identifica quem chama, autorização decide o que essa identidade pode fazer. mTLS autentica, não autoriza: certificado válido prova identidade, e a permissão vem de uma política separada. Segredo fora do artefato: rotação em segundos versus horas é o que separa um incidente contido de um incidente prolongado. Política sem tocar no código: o service mesh aplica mTLS, autorização e limitação de taxa de forma uniforme via proxies laterais. E ameaças reciclam conceitos: replay, movimento lateral e amplificação exploram, com intenção maliciosa, propriedades que já estudamos.

Na atividade prática, você vai elaborar o fluxo de segurança entre pedidos e pagamento: descrever as identidades e o mecanismo de autenticação mútua, definir as permissões da identidade “pedidos” aplicando menor privilégio, indicar explicitamente quais operações ela não pode executar, especificar onde os segredos ficam e com que política de rotação, dimensionar um balde de fichas justificando capacidade e taxa, e explicar como o desenho impede um ataque de repetição da requisição de cobrança.

**[19:40–20:00 · Slide 17 — Encerramento]**

A Unidade 3 se encerra com uma arquitetura estruturalmente completa: serviços delimitados, comunicação por eventos, execução orquestrada e tráfego autenticado. A Unidade 4 examina essa arquitetura por dentro e trata de medir, testar e evoluir o que foi construído. Bons estudos.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 12 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com os quatro riscos destacados um a um (02:20–03:50).
- Slide 5 — contraste visual entre modelo de perímetro e confiança zero (aproximadamente 04:00).
- Recurso visual 45 — comparação entre TLS tradicional e TLS mútuo (aproximadamente 07:10).
- Recurso visual 46 — tabela de tempo até a contenção de um segredo comprometido (aproximadamente 08:50).
- Slide 9 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (10:20).
- Recurso visual 47 — Pod com proxy lateral interceptando todo o tráfego (aproximadamente 10:50).
- Slide 11 — cálculo do balde de fichas, com as 50 absorvidas e as 40 recusadas em destaque (aproximadamente 12:40).
- Recurso visual 48 — quadro das quatro ameaças e suas mitigações (14:20–16:20).
- Slide 17 — vinheta de encerramento e transição para a Unidade 4 (últimos 15 segundos).

### Fontes e links de mídia

- ROSE, Scott et al. *Zero trust architecture*. Gaithersburg: NIST, 2020. (NIST Special Publication 800-207). DOI: 10.6028/NIST.SP.800-207 — referência conceitual, sem reprodução de trecho externo.
- RESCORLA, Eric. *The Transport Layer Security (TLS) Protocol Version 1.3*. [S. l.]: IETF, 2018. (RFC 8446). DOI: 10.17487/RFC8446 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, tabelas e quadros devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 12 (`unidade_3.md`) e do deck `unidade_3/slides/aula12.html`.
