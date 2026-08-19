# Roteiros das videoaulas 5 a 8 — Unidade 2 (20 minutos)

Disciplina: Distributed Systems Engineering
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 2: Dados distribuídos, consistência e coordenação
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: aproximadamente 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, indicações de edição e fontes.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas, respiração e construção progressiva dos recursos visuais.

Cada roteiro acompanha, slide a slide, o deck HTML da aula correspondente em `unidade_2/slides/`. As marcações entre colchetes duplos indicam o intervalo de tempo e o slide que deve estar na tela naquele momento. O avanço de slide é o principal marcador de edição: quando a marcação muda, o slide muda.

Plano de tempo de referência, adaptável ao ritmo de cada aula:

- 00:00–01:45 — capa, audiodescrição e sumário;
- 01:45–04:00 — objetivos de aprendizagem e situação-problema;
- 04:00–13:00 — desenvolvimento conceitual;
- 13:00–16:00 — demonstração, exemplos numéricos e estudo de caso;
- 16:00–18:00 — aplicação profissional e pausa para reflexão;
- 18:00–20:00 — pontos-chave, atividade prática e fechamento.

Os quatro roteiros a seguir correspondem às Aulas 5 a 8 da Unidade 2, mantendo a NexaOrder como fio condutor prático. Cada roteiro é um texto de narração pronto para gravação, e não notas de aula. O registro é o de exposição didática contínua, próximo ao de um livro-texto lido em voz alta: frases completas, encadeamento explícito entre as ideias e ausência de recursos de oralidade informal.

---

## Roteiro da Videoaula 5 — “Três cópias, três respostas diferentes — e nenhuma delas mentiu”

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 5 — Replicação e modelos de consistência.

**Deck de apoio:** `unidade_2/slides/aula5.html` — 19 slides (capa, audiodescrição, sumário, 15 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de justificar a replicação a partir de disponibilidade, latência, escala de leitura ou durabilidade, comparar líder-seguidor e multi-líder, explicar leituras obsoletas pelo atraso de réplica, distinguir os quatro modelos de consistência, dimensionar quóruns com a condição W mais R maior que N e escolher a garantia adequada por dado.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 por que replicar · 05:20 líder-seguidor e multi-líder · 07:10 quando a escrita conclui · 08:50 exemplo numérico do atraso de réplica · 10:20 citação · 10:40 quatro modelos de consistência · 12:40 erro comum · 13:50 garantias de sessão · 15:10 exemplo numérico dos quóruns · 16:50 combinações de quórum · 17:50 uma garantia por dado · 19:10 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 5, primeira da Unidade 2, e a pergunta central da disciplina muda de objeto a partir daqui. A Unidade 1 tratou de processos que se comunicam; esta unidade trata de dados e do problema mais persistente da engenharia distribuída: manter cópias do mesmo dado coerentes entre si.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: os slides usam fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo aparece em cartões claros. São cinco recursos visuais: o quadro comparativo entre líder-seguidor e multi-líder, a linha do tempo do atraso de réplica, a tabela dos quatro modelos de consistência, o diagrama de quóruns com interseção destacada e a matriz de garantias por dado da NexaOrder. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo por quatro motivos concretos para replicar dados. Depois comparo os modelos de replicação: líder-seguidor e multi-líder. Em seguida discuto quando uma escrita é considerada concluída — síncrona, assíncrona ou semissíncrona. Trato então do atraso de réplica e das leituras obsoletas. Apresento os quatro modelos de consistência: forte, sequencial, causal e eventual. Falo das garantias centradas no cliente, dimensiono quóruns de leitura e escrita e fecho escolhendo uma garantia diferente para cada dado da NexaOrder.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir justificar a replicação a partir de disponibilidade, latência, escala de leitura ou durabilidade. Deve comparar líder-seguidor e multi-líder quanto à ordenação de escritas e ao risco de conflito. Deve explicar leituras obsoletas pelo atraso de réplica, sem tratá-las como defeito automático. Deve distinguir consistência forte, sequencial, causal e eventual pelas propriedades que cada uma garante. Deve dimensionar quóruns usando a condição W mais R maior que N. E deve escolher a garantia adequada por dado, e não por serviço inteiro.

**[02:20–03:50 · Slide 4 — Situação-problema]**

O incidente que abre a aula é este. Um banco por serviço ainda era ponto único de falha e gargalo de leitura. A NexaOrder passou a manter cópias em vários nós, o que resolveu a disponibilidade — e criou um problema novo.

Durante uma promoção, um cliente consultou o catálogo três vezes e recebeu três preços diferentes, todos apresentados como “atuais”. Uma reserva confirmada em uma réplica não havia chegado a outra. E um segundo cliente conseguiu reservar a mesma unidade do mesmo produto.

A observação decisiva é esta: nenhuma réplica mentiu. Cada uma respondeu com exatidão ao que já havia recebido. Não houve corrupção de dados, não houve bug de leitura. Cada nó deu a resposta certa para o estado que ele conhecia.

O problema não foi a replicação. O problema foi não ter definido, para cada tipo de dado, qual garantia de consistência era necessária e qual mecanismo a sustentaria.

### Desenvolvimento conceitual

**[03:50–05:20 · Slide 5 — Por que replicar dados]**

Replicação é a manutenção de cópias do mesmo dado em nós diferentes. Quatro motivações aparecem com mais frequência.

Disponibilidade: se um nó falhar, outra cópia continua respondendo. É o motivo mais citado e, geralmente, o motivo real.

Redução de latência: servir leituras a partir do nó geograficamente mais próximo do usuário. Um cliente em Recife lê da réplica de Recife, não de um nó na Europa.

Escalabilidade de leitura: distribuir um grande volume de consultas entre várias réplicas, em vez de concentrar tudo em um único nó.

E durabilidade: reduzir a chance de perda definitiva após a falha de um único nó. Uma cópia única permanece uma cópia única — perdida ela, perde-se o dado.

Nenhum desses benefícios, porém, é gratuito. Toda cópia adicional traz a pergunta central da aula: como manter réplicas coerentes o suficiente para o uso pretendido, sem sacrificar justamente o benefício que motivou a replicação? A expressão “o suficiente para o uso pretendido” é decisiva e reaparecerá ao longo de toda a unidade.

**[05:20–07:10 · Slide 6 — Líder-seguidor e multi-líder]**

Existem dois grandes modelos de replicação, e a diferença entre eles é quem pode aceitar escrita.

*[indicação de edição: inserir Recurso visual 16 da Aula 5 — quadro comparativo entre líder-seguidor e multi-líder, revelado linha a linha]*

No modelo primário-réplica, também chamado de líder-seguidor, apenas o líder aceita escrita. A ordenação das escritas fica centralizada em um único ponto, sem disputa. A vantagem principal é justamente essa: na operação normal, não existe conflito de escrita, porque só um nó decide a ordem. O custo é que o líder vira gargalo e exige um processo de recuperação quando falha. E o risco típico é uma promoção mal coordenada gerar split-brain — exatamente o que discutimos na Aula 4.

No modelo multi-líder, mais de um nó aceita escrita, tipicamente em regiões diferentes. As escritas são ordenadas de forma concorrente entre os líderes. A vantagem principal é que a escrita local reduz a latência regional — um usuário na Europa escreve no nó europeu. O custo é a necessidade de uma regra explícita de resolução de conflito. E o risco típico é escritas concorrentes sobre o mesmo dado colidirem.

Um exemplo concreto: se um centro de distribuição registra a saída de uma unidade enquanto outro registra uma correção de inventário do mesmo item, é preciso decidir de antemão qual regra vale — prevalência do último carimbo, mesclagem de campos ou intervenção manual. Sem regra explícita, o comportamento em conflito é imprevisível — e imprevisível, em produção, significa decidido pelo acaso.

**[07:10–08:50 · Slide 7 — Quando a escrita é considerada concluída]**

A segunda decisão importante é: em que momento o sistema informa ao cliente que a escrita terminou?

Na replicação síncrona, o líder só confirma ao cliente depois que uma ou mais réplicas confirmaram ter recebido o dado. O efeito é mais durabilidade e menor risco de perda. Em contrapartida, paga-se mais latência e passa-se a depender da disponibilidade das réplicas para responder.

Na replicação assíncrona, o líder responde imediatamente, sem aguardar confirmação, e a propagação continua em segundo plano. O efeito é menor latência percebida. Existe, contudo, uma janela — pequena, porém real — em que a falha do líder perde uma escrita que nenhuma réplica durável chegou a receber. O cliente viu “confirmado” e o dado desapareceu.

Há também um meio-termo: a replicação semissíncrona, que exige confirmação de apenas parte das réplicas. Não se aguardam todas, mas tampouco se responde isoladamente.

Essa ideia de confirmação parcial reaparece adiante com outro nome: quórum de escrita.

**[08:50–10:20 · Slide 8 — Exemplo numérico: atraso de réplica e leituras obsoletas]**

O fenômeno que explica o incidente do catálogo pode ser quantificado com precisão.

*[indicação de edição: inserir Recurso visual 17 da Aula 5 — linha do tempo do atraso de réplica, com a janela de leitura obsoleta destacada em cor]*

O intervalo entre a confirmação no líder e a aplicação efetiva na réplica é o que chamamos de atraso de réplica. Enquanto esse intervalo existe, uma leitura feita na réplica devolve um valor mais antigo que o já confirmado no líder.

Considere a linha do tempo. No instante t-zero, o líder confirma a escrita — o novo preço do produto. O atraso da réplica é de 150 milissegundos. No instante t-zero mais 150 milissegundos, a réplica aplica essa escrita. O intervalo entre esses dois momentos constitui uma janela de 150 milissegundos de leitura obsoleta.

A conexão com o incidente é imediata. O cliente consultou o catálogo três vezes, e cada consulta pode ter sido atendida por uma réplica diferente, cada uma em um ponto distinto da própria janela de atraso. Daí os três preços, todos corretos do ponto de vista de quem os devolveu.

A conclusão a reter é que o atraso de réplica não é, isoladamente, um defeito. Ele vira problema quando o processo de negócio pressupõe, implicitamente, uma consistência que ninguém garantiu explicitamente.

**[10:20–10:40 · Slide 9 — Citação]**

Esta é a frase que organiza a aula: nenhuma réplica mentiu — cada uma respondeu com exatidão ao que já havia recebido.

### Demonstração, exemplo ou estudo de caso

**[10:40–12:40 · Slide 10 — Quatro modelos de consistência]**

Chegamos ao vocabulário central da unidade. Existem quatro modelos de consistência que é preciso saber nomear e distinguir.

*[indicação de edição: inserir Recurso visual 18 da Aula 5 — tabela dos quatro modelos, revelando uma linha por vez]*

Consistência forte, também chamada de linearizabilidade: o sistema se comporta como se houvesse uma única cópia, e toda leitura reflete a escrita concluída mais recente. O custo típico é mais coordenação, o que pode elevar a latência ou reduzir a disponibilidade sob falha.

Consistência sequencial: todas as réplicas concordam com a mesma ordem de operações. A diferença em relação à consistência forte é sutil — a ordem sobre a qual todos concordam não precisa coincidir com o tempo real entre clientes distintos. Todos observam a mesma sequência, ainda que ela não corresponda ao relógio.

Consistência causal: operações que têm relação de causa e efeito são vistas na mesma ordem por todos. Operações concorrentes, porém, podem ser vistas em ordens diferentes por observadores diferentes. Trata-se de retomada direta da relação happened-before da Aula 3 — o mesmo raciocínio, agora aplicado a réplicas de dados em vez de eventos de processos.

Consistência eventual: cessadas as escritas, as réplicas convergem para o mesmo valor. O que ela não oferece é prazo definido nem qualquer garantia sobre a ordem observada no meio-tempo.

**[12:40–13:50 · Slide 11 — Erro comum: “forte é melhor, eventual é pior”]**

Cabe desfazer aqui uma das confusões mais custosas da área. É comum ler essa lista como uma escala de qualidade, do melhor para o pior. Ela não é isso.

Consistência forte não é melhor em absoluto. Ela costuma exigir mais coordenação, e coordenação tem preço em latência e em disponibilidade sob falha.

Consistência eventual não é pior. Ela pode permitir menos coordenação, o que não garante automaticamente menor custo, porque reconciliar divergências também tem preço.

Tampouco é verdade que a consistência eventual seja sempre mais disponível. O resultado depende do protocolo específico e das falhas consideradas.

O que determina a escolha é o dado: o que ele representa e que risco carrega para o negócio. A pergunta pertinente, portanto, não é qual modelo é o melhor, e sim o que este dado específico não pode tolerar.

**[13:50–15:10 · Slide 12 — Garantias centradas no cliente]**

Existe um caminho intermediário que resolve boa parte dos problemas reais sem exigir linearizabilidade global: as garantias centradas no cliente, ou garantias de sessão.

A observação de partida é esta: boa parte do que o usuário percebe como defeito não exige consistência global. Exige apenas coerência do ponto de vista daquele usuário.

São quatro garantias. Leitura das próprias escritas: o cliente sempre vê as alterações que ele mesmo fez. Se ele mudou o endereço de entrega, ele vê o endereço novo, mesmo que outra pessoa ainda veja o antigo. Leituras monotônicas: uma vez que ele observou um valor, ele nunca verá um valor mais antigo depois — o preço não “volta no tempo”. Escritas monotônicas: as escritas de um mesmo cliente são aplicadas na ordem em que ele as emitiu. E prefixo consistente: se B depende causalmente de A, ninguém observa B sem antes observar A — a resposta nunca aparece antes da pergunta.

Um cuidado conceitual: essas são garantias de sessão, não degraus de uma escala universal. Elas reduzem a inconsistência percebida pelo usuário; o custo real depende do protocolo e da arquitetura adotados para implementá-las.

**[15:10–16:50 · Slide 13 — Exemplo numérico: quóruns de leitura e escrita]**

Chegamos à conta central da aula.

*[indicação de edição: inserir Recurso visual 19 da Aula 5 — diagrama de quóruns, com a interseção entre o conjunto de escrita e o de leitura destacada]*

Com o dado replicado em N nós, a escrita conclui quando confirmada por W réplicas, e a leitura consulta R réplicas, reconciliando as respostas por metadados de versão. A condição clássica de interseção é: W mais R maior que N.

Os números do exemplo são estes. N igual a 5 réplicas do dado. W igual a 3 réplicas confirmam a escrita. R igual a 3 réplicas consultadas na leitura. A soma: 3 mais 3 é 6, e 6 é maior que 5. Logo, há interseção garantida — pelo menos uma das réplicas consultadas na leitura necessariamente participou da escrita.

Duas ressalvas são necessárias para que a conclusão não fique simplificada em excesso. A interseção garante que ao menos uma resposta possa conter a versão confirmada, desde que os quóruns sejam fixos, e não do tipo sloppy, e desde que o sistema compare versões corretamente. A desigualdade, isoladamente, não garante linearizabilidade nem resolve escritas concorrentes; para isso são necessários W maior que N sobre 2, versionamento e reconciliação explícita.

Em síntese: o quórum garante que a informação correta está disponível em algum lugar do conjunto lido. Devolvê-la ao cliente ainda depende da capacidade de comparar versões.

**[16:50–17:50 · Slide 14 — Combinações de quórum e seus compromissos]**

Os casos extremos esclarecem o desenho.

Com W igual a 1 e R igual a N: a escrita é rápida, porque basta um nó confirmar, mas a leitura fica cara e menos disponível, porque depende de todas as réplicas responderem.

Com W igual a N e R igual a 1: o inverso. A leitura é rápida, mas a escrita fica cara e menos disponível, porque depende de todos os nós.

Com W mais R maior que N: configuração equilibrada, com interseção garantida.

E com W mais R menor ou igual a N: prioriza-se a disponibilidade, aceitando conscientemente que não há garantia de sobreposição e que leituras obsoletas ocorrerão.

Há ainda uma fórmula a registrar: N maior ou igual a 2f mais 1 é o número mínimo de réplicas para tolerar f falhas mantendo maioria. Esse princípio de maioria reaparece na Aula 7, no tratamento do consenso.

### Aplicação profissional

**[17:50–19:10 · Slide 15 — Uma garantia diferente para cada dado]**

Chegamos à habilidade central desta unidade: decompor o sistema por dado, e não por serviço inteiro.

*[indicação de edição: inserir Recurso visual 20 da Aula 5 — matriz de garantias por dado da NexaOrder, revelando uma linha por vez]*

Considere a NexaOrder. Para o catálogo, consistência eventual é adequada: um preço levemente desatualizado por alguns segundos não compromete o negócio, e priorizar disponibilidade e latência faz sentido para quem está navegando.

Para o estoque, a exigência é outra. A reserva demanda controle explícito de concorrência para não vender a mesma unidade duas vezes, o que leva a garantias de cliente combinadas com quórum com sobreposição — por exemplo, N igual a 3, W igual a 2 e R igual a 2.

Para o pagamento, o registro da transação se aproxima de consistência forte, por ser o dado com maior risco financeiro e regulatório. Mesmo aqui, contudo, as notificações associadas — o e-mail de confirmação, a atualização do painel — podem permanecer eventuais.

Há um erro a evitar: afirmar apenas “W maior ou igual a 2” não basta. Sem definir N, R e a regra de reconciliação, essa afirmação não descreve um sistema; descreve uma intenção.

### Fechamento

**[19:10–19:40 · Slides 16 e 17 — Pontos-chave e atividade prática]**

Recapitulando. Replicar tem preço: melhora disponibilidade, latência e durabilidade, e introduz o problema de manter cópias coerentes. Líder ordena: o modelo líder-seguidor centraliza a ordenação na operação normal, enquanto o multi-líder reduz latência regional e exige regra de conflito. Quando confirmar: a replicação síncrona reduz a janela de perda com mais coordenação, e a assíncrona responde antes aceitando risco maior. Obsoleto não é errado: o atraso de réplica explica leituras antigas sem que nenhuma réplica esteja incorreta. Não há escala única entre os quatro modelos de consistência. E quórum não basta sozinho: a interseção garante que a versão certa está no conjunto lido, mas devolvê-la ainda exige metadados de versão e reconciliação.

A atividade prática pede uma tabela de três linhas — catálogo, estoque e pagamento — indicando para cada um: o modelo de consistência mais adequado com justificativa de negócio, o modelo de replicação, se a replicação será síncrona, assíncrona ou por quórum, valores plausíveis de N, W e R, um cenário de leitura obsoleta que seria aceitável e um que não seria, com o porquê.

**[19:40–20:00 · Slide 18 — Encerramento]**

Esta aula forma a capacidade de escolher a garantia de consistência adequada a cada dado e de dimensionar quóruns de leitura e escrita. Na próxima aula, o problema muda de natureza: não se trata mais de copiar o mesmo dado, e sim de dividir dados que já não cabem em um único nó.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 5 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com os três sintomas destacados um a um (02:20–03:50).
- Recurso visual 16 — quadro comparativo líder-seguidor versus multi-líder (aproximadamente 05:30).
- Recurso visual 17 — linha do tempo do atraso de réplica, com a janela de 150 ms destacada (aproximadamente 09:00).
- Slide 9 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (10:20).
- Recurso visual 18 — tabela dos quatro modelos de consistência, revelada linha a linha (10:40–12:40).
- Recurso visual 19 — diagrama de quóruns com interseção destacada (aproximadamente 15:20).
- Recurso visual 20 — matriz de garantias por dado da NexaOrder (aproximadamente 18:00).
- Slide 18 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- VOGELS, Werner. Eventually consistent. *Communications of the ACM*, v. 52, n. 1, p. 40-44, 2009. DOI: 10.1145/1435417.1435432 — referência conceitual, sem reprodução de trecho externo.
- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O’Reilly Media, 2017 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, tabelas e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 5 (`unidade_2.md`) e do deck `unidade_2/slides/aula5.html`.

---

## Roteiro da Videoaula 6 — “Quando uma cópia inteira já não cabe em um nó”

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 6 — Particionamento, CAP e escalabilidade de dados.

**Deck de apoio:** `unidade_2/slides/aula6.html` — 19 slides (capa, audiodescrição, sumário, 15 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de diferenciar particionamento de replicação, escolher a estratégia de partição adequada aos padrões de consulta, calcular a fração de chaves redistribuída com hashing consistente, diagnosticar pontos quentes, aplicar o teorema CAP ao comportamento sob partição e usar o PACELC para explicar o custo de consistência fora de cenários de falha.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:40 particionamento horizontal · 05:00 três estratégias · 06:50 exemplo numérico do hashing consistente · 08:40 rebalanceamento e pontos quentes · 10:40 citação · 11:00 particionamento e replicação combinados · 12:20 exemplo numérico do scatter-gather · 14:00 teorema CAP · 15:30 CP e AP · 16:50 PACELC · 18:20 matriz de decisão · 19:10 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 6, dedicada a particionamento, CAP e escalabilidade de dados. A aula anterior tratou de como manter cópias coerentes; nesta, a NexaOrder esbarra em um limite diferente, que copiar não resolve.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o quadro das três estratégias de particionamento, o anel de hashing consistente com nós virtuais, o diagrama de dispersão e coleta entre partições, a tabela comparativa CP versus AP e a matriz PACELC da NexaOrder. Descrevo cada um no momento em que aparecerem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo diferenciando particionamento horizontal de replicação. Examino em seguida as três estratégias — por faixa, por hash e por diretório. Em seguida apresento o hashing consistente e os nós virtuais, discuto rebalanceamento e pontos quentes, mostro como particionamento e replicação se combinam em produção e analiso o custo das consultas que atravessam partições. Fecho com o teorema CAP durante uma partição de rede e com o PACELC, que descreve o compromisso que existe todos os dias, e não só na falha.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir diferenciar particionamento de replicação e reconhecer por que produção combina os dois. Deve escolher a estratégia de partição adequada aos padrões de consulta mais frequentes. Deve calcular a fração de chaves redistribuída ao adicionar um nó com hashing consistente. Deve diagnosticar pontos quentes e propor mitigações distintas para leitura e para escrita. Deve aplicar o teorema CAP ao comportamento do sistema durante uma partição de rede. E deve usar o PACELC para explicar o custo de consistência fora de cenários de falha.

**[02:20–03:40 · Slide 4 — Situação-problema]**

Resolvida a coerência entre réplicas, a NexaOrder encontrou um segundo limite. O catálogo chegou a milhões de produtos, e o histórico de pedidos, a bilhões de registros. Uma cópia inteira simplesmente não cabia mais, com desempenho aceitável, em um único nó.

Era preciso dividir os dados, e não apenas copiá-los. Essa distinção organiza toda a aula.

A primeira tentativa da equipe foi ingênua e, por isso mesmo, instrutiva: produtos de “A” a “M” em um nó, de “N” a “Z” em outro — uma divisão aparentemente equilibrada.

Veio então uma campanha concentrada em produtos iniciados por “S”. Aquele nó sobrecarregou isoladamente, enquanto o outro permaneceu praticamente ocioso.

A lição é que dividir exige estratégia, e não um corte arbitrário. A distribuição real das chaves quase nunca é uniforme.

### Desenvolvimento conceitual

**[03:40–05:00 · Slide 5 — Particionamento horizontal]**

Particionamento horizontal, também chamado de sharding, divide um conjunto de dados em partições menores, cada uma servida por um subconjunto de nós.

A diferença em relação à aula anterior é fundamental e merece enunciado explícito. Replicação copia: mantém cópias completas do mesmo dado em nós diferentes. Particionamento divide: distribui fatias diferentes de um mesmo conjunto.

Copiar melhora disponibilidade e leitura. Dividir permite crescer além do que um nó comporta. São problemas diferentes, com soluções diferentes.

Em produção, os dois se combinam: cada partição é, por sua vez, replicada para garantir disponibilidade. Particionar sem replicar significa perder a partição inteira quando um nó falha; replicar sem particionar significa esbarrar no tamanho do nó.

O objetivo final é deixar que volume de dados e volume de operações cresçam distribuindo trabalho, em vez de exigir tudo de um único nó.

**[05:00–06:50 · Slide 6 — Três estratégias de particionamento]**

Como decidir a que partição cada registro pertence? Existem três estratégias clássicas.

*[indicação de edição: inserir Recurso visual 21 da Aula 6 — quadro das três estratégias, revelando uma linha por vez]*

Particionamento por faixa: definem-se intervalos contíguos da chave — janeiro e fevereiro em uma partição, A a M e N a Z em outra. A vantagem é que consultas por intervalo atingem partições contíguas, o que é eficiente. A limitação é exatamente o que a NexaOrder enfrentou: pontos quentes quando a distribuição real não é uniforme.

Particionamento por hash: aplica-se uma função de espalhamento à chave e usa-se o resultado para escolher a partição. A vantagem é uma distribuição aproximadamente uniforme. A limitação é que a consulta por intervalo perde eficiência — chaves próximas vão parar em partições distantes — e uma chave popular continua concentrando tráfego.

Particionamento por diretório: mantém-se uma tabela explícita mapeando chave para partição. A vantagem é flexibilidade máxima para rebalancear. A limitação é a introdução de um componente adicional, que pode se tornar ponto único de falha.

Um esclarecimento importante: o hash reduz pontos quentes causados por concentração em faixas, mas não resolve o problema de uma única chave muito popular. Se um produto específico recebe metade do tráfego, nenhuma função de espalhamento corrige a situação.

**[06:50–08:40 · Slide 7 — Exemplo numérico: hashing consistente]**

Esta é uma das contas mais elegantes da disciplina.

*[indicação de edição: inserir Recurso visual 22 da Aula 6 — anel de hashing consistente, com o novo nó sendo inserido e apenas o segmento afetado destacado]*

O problema do hash simples é o seguinte: usando-se hash da chave, módulo N, qualquer mudança em N faz quase todas as chaves mudarem de partição. Adicionar um único nó reorganiza o cluster inteiro.

O hashing consistente resolve isso organizando o espaço como um anel. Cada chave vai ao primeiro nó encontrado em sentido horário. Ao se adicionar um nó, apenas as chaves entre esse novo nó e seu vizinho anterior precisam se mover.

A fração redistribuída é aproximadamente 1 dividido por N mais 1. Com 9 nós existentes e 1 nó adicionado, a fração é 1 dividido por 10, ou seja, aproximadamente 10% das chaves se movem. O hash simples moveria aproximadamente 100%. É a diferença entre uma manutenção rotineira e uma migração de grande porte.

Há um refinamento importante: os nós virtuais. Cada nó físico costuma receber 100 ou 200 posições virtuais espalhadas pelo anel. A razão é que, com uma única posição, a carga de cada nó dependeria do acaso de sua colocação no anel — um nó poderia ficar com um segmento extenso e outro com um segmento mínimo. Com muitas posições virtuais, a soma dos segmentos se aproxima da média, o que reduz a variância de carga sem alterar a lógica de atribuição.

**[08:40–10:40 · Slide 8 — Rebalanceamento e pontos quentes]**

Mesmo com hashing consistente, uma única chave pode concentrar tráfego desproporcional. É o caso do produto em promoção relâmpago, que atrai quase todas as leituras de estoque. As mitigações precisam ser separadas, porque leitura e escrita pedem soluções diferentes.

Ponto quente de leitura: resolve-se com cache, réplicas de leitura e visão materializada, observado um cuidado — é preciso definir a invalidação ou uma versão que explicite a defasagem tolerada. Cache sem política de invalidação apenas troca um problema por outro.

Ponto quente de escrita: sufixos aleatórios funcionam para escritas agregáveis, como contadores. Divide-se um contador em dez subcontadores e soma-se na leitura. O fan-out, porém, exige atenção: se toda leitura precisar consultar todas as subchaves, o gargalo se agrava em vez de diminuir.

Há um caso que exige atenção especial: o estoque autoritativo. A reserva não pode ser dividida ingenuamente. Espalhar o saldo em dez subchaves abre a possibilidade de vender dez vezes o disponível. Nesse caso, mantém-se regra única de concorrência, cotas por partição ou decisão serializada por produto. Durante o pico, uma alternativa é isolar temporariamente aquele item e aplicar controle de admissão.

Um último ponto sobre rebalanceamento, com frequência esquecido no planejamento: rebalancear move carga, não apenas dados. Origem e destino processam tráfego normal e transferência ao mesmo tempo. Daí a necessidade de throttling e de janelas de menor tráfego.

**[10:40–11:00 · Slide 9 — Citação]**

Esta frase resume a segunda metade da aula: uma decisão registrada apenas como “usamos hash consistente” está incompleta sem a decisão complementar — sob partição de rede, esse dado prioriza consistência ou disponibilidade?

### Demonstração, exemplo ou estudo de caso

**[11:00–12:20 · Slide 10 — Particionamento e replicação combinados]**

As duas aulas se articulam neste ponto. Uma arquitetura típica particiona os dados em P partições e replica cada partição em R nós. O resultado é um cluster com P vezes R réplicas distribuídas.

A divisão de responsabilidades se torna clara. Dentro de cada partição, valem os conceitos da Aula 5: líder-seguidor ou multi-líder, quóruns de leitura e escrita. Entre as partições, valem os conceitos desta aula: escolha da chave, estratégia e rebalanceamento.

O benefício prático aparece na falha. Se um nó físico cai, ele afeta apenas as partições cujas réplicas ele hospedava, não o sistema inteiro. O raio de impacto fica contido pelo desenho — que é exatamente o princípio de isolamento da Aula 4, aplicado agora aos dados.

Uma condição importante acompanha esse resultado: a escrita só é comprometida se as réplicas restantes não formarem o quórum exigido. Havendo quórum, a partição segue disponível, apenas com menor margem para novas falhas.

**[12:20–14:00 · Slide 11 — Exemplo numérico: scatter-gather e a cauda de latência]**

Há um efeito que costuma passar despercebido no projeto e se manifestar apenas em produção.

*[indicação de edição: inserir Recurso visual 23 da Aula 6 — diagrama de dispersão e coleta, com a partição mais lenta destacada]*

Uma consulta que combina dados de várias partições exige dispersão e coleta: ela vai a todas as partições relevantes e agrega os resultados parciais. O tempo total é determinado pela partição mais lenta a responder, e não pela média.

Considere os números a seguir. São 8 partições atingidas, com resposta média de 20 milissegundos e uma chance de 5% de cada partição apresentar uma resposta na cauda, isto é, muito mais lenta que a média.

A probabilidade de ao menos uma partição ser lenta é 1 menos 0,95 elevado a 8, o que dá aproximadamente 0,34. Ou seja: 34% das consultas.

Esse número merece atenção. Mais de um terço das consultas que tocam oito partições tende a sofrer a cauda de pelo menos uma delas, ainda que cada partição seja lenta apenas 5% das vezes. A raridade individual não se traduz em raridade agregada.

Trata-se de um argumento numérico forte em favor de chaves que evitem consultas dispersas. Cabe a ressalva metodológica: o cálculo assume ocorrências independentes, o que é uma simplificação assumida apenas para este exemplo.

**[14:00–15:30 · Slide 12 — O teorema CAP]**

Chegamos ao teorema mais citado e mais mal interpretado da área.

Durante uma partição de rede — quando nós deixam de se comunicar entre si — um sistema replicado não pode oferecer simultaneamente três coisas.

Consistência, o C: toda leitura reflete a escrita mais recente confirmada. Disponibilidade, o A: toda requisição a um nó ativo recebe resposta, mesmo sem garantia de ser a mais recente. E tolerância a partição, o P: o sistema continua operando apesar da perda de comunicação entre alguns nós.

A leitura correta do teorema, frequentemente distorcida, é a seguinte. Como partições são inevitáveis em sistemas reais — cabos se rompem, roteadores falham, zonas ficam isoladas —, P não é opcional na prática. Não há escolha entre os três. A escolha relevante ocorre entre C e A, e apenas durante o período em que a partição persiste.

Fora da partição, um sistema pode oferecer alta consistência e alta disponibilidade simultaneamente. O CAP não afirma que algo precisa ser sacrificado o tempo todo.

**[15:30–16:50 · Slide 13 — CP e AP: dois comportamentos sob partição]**

Cabe examinar o que cada escolha significa concretamente.

*[indicação de edição: inserir Recurso visual 24 da Aula 6 — tabela comparativa CP versus AP, revelando uma linha por vez]*

Um sistema CP, durante a partição, rejeita ou atrasa respostas no lado que não consegue garantir a versão mais recente. Ele preserva consistência e arrisca indisponibilidade parcial enquanto a partição durar. A vantagem é que, depois da partição, não há nada a reconciliar.

Um sistema AP, durante a partição, continua respondendo em ambos os lados. Ele preserva disponibilidade e arrisca valores divergentes, o que exige reconciliação quando a comunicação é restabelecida.

Na NexaOrder: reserva de estoque e confirmação de pagamento pedem comportamento CP — é melhor recusar a operação do que vender duas vezes o mesmo item. Leitura do catálogo de produtos pede comportamento AP — é melhor mostrar um preço possivelmente desatualizado do que uma página de erro.

**[16:50–18:20 · Slide 14 — PACELC: o compromisso de todos os dias]**

O CAP tem uma limitação séria: descreve apenas o comportamento sob partição, e partições são raras. Isoladamente, portanto, ele deixa de fora quase toda a operação normal do sistema.

O PACELC estende a análise. Sua leitura é: se há partição, o P, escolhe-se entre disponibilidade e consistência; caso contrário — e esse caso contrário é o E, de else —, escolhe-se entre latência e consistência.

Esse deslocamento muda os termos da discussão técnica. Partições são raras, mas o compromisso entre latência e consistência ocorre a cada operação. Exigir confirmação de todas as réplicas antes de responder custa latência sempre, e não apenas na falha. Trata-se de um custo constante, não excepcional.

A formulação também qualifica a conversa com o negócio, ao deixar claro que consistência tem impacto cotidiano — no tempo que o cliente espera a tela carregar — e não apenas em cenários excepcionais raramente observados.

A conclusão de projeto é que “como particionar” e “o que fazer sob partição” são duas decisões distintas, e não uma só.

### Aplicação profissional

**[18:20–19:10 · Slide 15 — Matriz de decisão da NexaOrder]**

As decisões da aula se consolidam em uma matriz.

*[indicação de edição: inserir Recurso visual 25 da Aula 6 — matriz PACELC da NexaOrder, com destaque nas duas linhas de estoque]*

O catálogo é PA barra EL: sob partição, prioriza disponibilidade; fora dela, prioriza latência, com convergência eventual.

O pagamento é PC barra EC: prioriza consistência sempre, mesmo que isso signifique recusar ou atrasar uma resposta.

O estoque aparece duas vezes, e nisso reside o aprendizado mais fino da aula. A leitura informativa do estoque é PA barra EL: um saldo aproximado tolera disponibilidade maior em situações de baixo risco. Já a reserva efetiva é PC: aproxima-se de CP para evitar vender o mesmo item duas vezes.

Vale observar o que ocorreu: o mesmo serviço aparece em duas linhas diferentes, com garantias opostas, porque a decisão se dá por operação sobre o dado, e não por serviço inteiro. É a mesma lição da Aula 5, agora com outro vocabulário.

### Fechamento

**[19:10–19:40 · Slides 16 e 17 — Pontos-chave e atividade prática]**

Recapitulando. Dividir, não só copiar: particionamento distribui fatias de um conjunto e complementa a replicação, em vez de substituí-la. Faixa favorece intervalo, mas a distribuição real das chaves pode criar pontos quentes. Hash espalha chaves distintas ao custo da consulta por intervalo, e não resolve uma chave popular. O anel reduz migração: o hashing consistente move aproximadamente 1 sobre N mais 1 das chaves ao adicionar um nó. O CAP vale na partição: a escolha entre consistência e disponibilidade só se impõe enquanto a comunicação estiver rompida. E o PACELC vale sempre: fora da partição, o compromisso é entre latência e consistência, e ele ocorre a cada operação.

Na atividade prática, você vai escolher as chaves de partição para pedidos e estoque: definir chave e estratégia de cada dado, justificar pelos padrões de consulta mais comuns, simular um produto virando ponto quente durante uma campanha, descrever o efeito esperado sobre a partição, propor uma mitigação concreta distinguindo leitura de escrita e classificar cada dado como CP ou AP, verificando se a escolha se sustenta na lógica do PACELC.

**[19:40–20:00 · Slide 18 — Encerramento]**

Esta aula forma a capacidade de dividir dados sem criar pontos quentes e de explicar, com CAP e PACELC, o comportamento do sistema quando a rede se rompe. A próxima aula retoma o problema deixado em aberto na Aula 4: como um conjunto de nós concorda, sem intervenção externa, sobre quem exerce a liderança.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 6 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com o nó sobrecarregado destacado em vermelho (02:20–03:40).
- Recurso visual 21 — quadro das três estratégias de particionamento (aproximadamente 05:10).
- Recurso visual 22 — anel de hashing consistente com nós virtuais e o segmento migrado em destaque (aproximadamente 07:00).
- Slide 9 — citação em tela cheia (10:40).
- Recurso visual 23 — diagrama de dispersão e coleta, com a partição mais lenta destacada (aproximadamente 12:30).
- Recurso visual 24 — tabela comparativa CP versus AP (aproximadamente 15:40).
- Recurso visual 25 — matriz PACELC da NexaOrder, com as duas linhas de estoque em destaque (aproximadamente 18:30).
- Slide 18 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- BREWER, Eric. CAP twelve years later: how the “rules” have changed. *Computer*, v. 45, n. 2, p. 23-29, 2012. DOI: 10.1109/MC.2012.37 — referência conceitual, sem reprodução de trecho externo.
- ABADI, Daniel. Consistency tradeoffs in modern distributed database system design: CAP is only part of the story. *Computer*, v. 45, n. 2, p. 37-42, 2012. DOI: 10.1109/MC.2012.33 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, anéis, tabelas e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 6 (`unidade_2.md`) e do deck `unidade_2/slides/aula6.html`.

---

## Roteiro da Videoaula 7 — “Quem manda quando o líder some?”

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 7 — Consenso, eleição de líder e Raft.

**Deck de apoio:** `unidade_2/slides/aula7.html` — 21 slides (capa, audiodescrição, sumário, 17 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de enunciar o problema do consenso pelas três propriedades que a decisão precisa satisfazer, calcular quantas falhas um cluster de N nós tolera, explicar por que clusters usam número ímpar de nós, descrever a eleição de líder do Raft, distinguir segurança de progresso e dimensionar o custo de latência de uma confirmação por consenso.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 o problema do consenso · 05:10 exemplo numérico da maioria · 06:50 tamanho do cluster · 08:00 máquina de estados replicada · 09:20 eleição de líder · 11:00 citação · 11:20 termos e log replicado · 12:50 detalhe crítico da confirmação · 14:10 segurança e progresso · 15:20 consenso e CAP · 16:20 exemplo numérico da latência · 17:40 limites e custos · 18:30 pausa para reflexão · 19:15 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 7, dedicada a consenso, eleição de líder e Raft. O ponto de partida é um incidente particularmente instrutivo desta unidade, porque nele o erro não foi de máquina, e sim de processo.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o diagrama do cluster com dois líderes concorrentes, a fórmula da tolerância a falhas, o diagrama da eleição com temporizadores aleatórios, a linha do tempo do log replicado e a ilustração da partição em maioria e minoria. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo enunciando o problema do consenso pelas três propriedades que a decisão precisa satisfazer. Depois trabalho maioria e quórum, calculando quantas falhas um cluster tolera. Apresento a máquina de estados replicada, que é a abstração central. Em seguida detalho a eleição de líder do Raft e os temporizadores aleatórios, os termos, o log replicado e a regra de confirmação. Separo segurança de progresso, conecto consenso com CAP olhando o lado minoritário e fecho com os limites e custos do consenso.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir enunciar o problema do consenso pelas três propriedades que a decisão precisa satisfazer. Deve calcular quantas falhas um cluster de N nós tolera mantendo maioria. Deve explicar por que clusters de consenso usam número ímpar de nós. Deve descrever a eleição de líder do Raft e o papel dos temporizadores aleatórios. Deve distinguir segurança de progresso, reconhecendo que só o progresso depende de maioria ativa. E deve dimensionar o custo de latência de uma confirmação por consenso.

**[02:20–03:50 · Slide 4 — Situação-problema]**

O incidente ocorreu da seguinte forma. O nó líder do estoque, na região sul, ficou inacessível por uma falha de rede. A equipe de plantão precisou promover um seguidor manualmente, e o resultado foi previsível: dois operadores, sem se comunicar entre si, promoveram dois nós diferentes quase ao mesmo tempo.

*[indicação de edição: inserir Recurso visual 26 da Aula 7 — diagrama do cluster com dois nós marcados como líder simultaneamente, em cores conflitantes]*

Por alguns minutos, o sistema teve dois líderes aceitando escritas. Parte das reservas feitas nesse intervalo divergiu entre os dois.

O diagnóstico correto é este. O problema real não era a indisponibilidade do líder, situação esperada e tratável. O problema real era outro: como um conjunto de nós concorda, por conta própria, sobre quem é o líder legítimo, mesmo na presença de falhas?

Convém observar o que ocorreu: resolver consenso manualmente é precisamente o que produz split-brain. Duas decisões concorrentes, tomadas sem coordenação, cada uma correta do ponto de vista de quem a tomou.

### Desenvolvimento conceitual

**[03:50–05:10 · Slide 5 — O problema do consenso]**

O enunciado formal é curto e merece ser memorizado.

Consenso é fazer um conjunto de nós concordar sobre um único valor, mesmo na presença de falhas, de modo que a decisão satisfaça três propriedades.

Primeira, validade: o valor decidido foi de fato proposto por algum nó. Isso impede soluções triviais, como todo mundo sempre decidir zero.

Segunda, uniformidade: todos os nós corretos decidem o mesmo valor. Não pode haver dois grupos com decisões diferentes, que foi exatamente o que ocorreu na NexaOrder.

Terceira, irrevogabilidade: uma vez decidido, o valor não muda. Não há revisão posterior da decisão.

Esse problema aparece sempre que o sistema precisa de uma única fonte de verdade: qual nó é o líder, qual foi a próxima operação aplicada ao log, qual transação foi confirmada. Toda vez que se exige uma resposta única e definitiva, está-se diante de consenso.

**[05:10–06:50 · Slide 6 — Exemplo numérico: maioria e tolerância a falhas]**

Algoritmos como o Raft se apoiam em um princípio simples: uma decisão só vale quando aceita por mais da metade dos nós. É o mesmo quórum da Aula 5, aplicado agora à escolha do líder e às entradas confirmadas do log.

A fórmula da tolerância é: f é igual ao piso de N menos 1, dividido por 2.

Aplicando a fórmula: com N igual a 5 nós no cluster, f é o piso de 4 dividido por 2, o que dá 2. O cluster tolera, portanto, 2 falhas, e 3 nós formam maioria.

Essa fórmula responde a uma pergunta frequente: por que se adota sempre número ímpar de nós?

Refazendo a conta com 6 nós, f é o piso de 5 dividido por 2, que continua sendo 2 — exatamente a mesma tolerância de 5 nós. Acrescentou-se uma máquina, elevou-se o custo e aumentou-se o tráfego de coordenação, sem nenhum ganho de tolerância. Por isso números pares raramente se justificam em um cluster de consenso.

**[06:50–08:00 · Slide 7 — Escolhendo o tamanho do cluster]**

Convém comparar os tamanhos usuais.

Com 3 nós: tolera 1 falha, maioria de 2. É o menor fan-out e o menor custo, mas tolera apenas uma falha, de modo que uma manutenção programada já deixa o cluster sem margem.

Com 5 nós: tolera 2 falhas, maioria de 3. É o equilíbrio mais comum entre tolerância e custo de coordenação.

Com 7 nós: tolera 3 falhas, maioria de 4. Mais tolerância, mas aumenta tráfego, armazenamento e custo operacional.

Uma observação técnica evita um mal-entendido comum: como as mensagens são enviadas em paralelo, a latência não cresce linearmente com N. Ela depende da resposta necessária para completar o quórum e da carga adicional introduzida. Um cluster de 7 nós não é duas vezes mais lento que um de 3.

**[08:00–09:20 · Slide 8 — Máquina de estados replicada]**

Antes do Raft propriamente dito, é necessário apresentar a abstração que torna tudo isso viável: a máquina de estados replicada.

A ideia é a seguinte. Cada nó mantém uma réplica que pode estar temporariamente em um índice diferente do log — ou seja, alguns nós estão mais adiantados que outros.

A garantia é esta: réplicas que partem do mesmo estado e aplicam o mesmo prefixo de operações determinísticas, na mesma ordem, chegam ao mesmo estado. São três as condições — mesmo estado inicial, operações determinísticas e mesma ordem —, e satisfeitas as três, o resultado é idêntico.

Seguidores atrasados convergem naturalmente, à medida que recebem e aplicam esse prefixo.

Nisso reside a transformação elegante do problema: manter réplicas consistentes converte-se em uma questão bem mais restrita — o acordo sobre o prefixo confirmado de um log ordenado. Em vez de sincronizar estado, sincroniza-se uma lista de operações, o que é consideravelmente mais tratável.

**[09:20–11:00 · Slide 9 — Eleição de líder]**

Passemos ao mecanismo. O Raft elege, no máximo, um líder por termo. Esse líder recebe novas operações e as replica para os seguidores.

*[indicação de edição: inserir Recurso visual 27 da Aula 7 — diagrama da eleição, com os temporizadores de cada nó expirando em instantes diferentes]*

A eleição acontece em quatro passos. Primeiro, silêncio: os seguidores deixam de receber sinais válidos do líder. Segundo, expiração dos temporizadores, e aqui está o detalhe decisivo do algoritmo — cada seguidor tem um temporizador aleatório, que vence em um instante diferente dos demais. Terceiro, candidatura: o primeiro a expirar torna-se candidato e solicita votos aos outros. Quarto, eleição por maioria: quem recebe votos da maioria torna-se líder do novo termo.

A opção por temporizadores aleatórios, e não fixos, é deliberada. Se todos disparassem no mesmo instante, todos se tornariam candidatos simultaneamente, dividiriam os votos e nenhum alcançaria maioria; os empates poderiam se repetir, atrasando indefinidamente a formação de um novo líder. A aleatoriedade quebra a simetria — é a mesma ideia do jitter da Aula 2, aplicada a outro problema.

Um detalhe importante completa o mecanismo: um líder antigo que estava isolado, ao retornar, descobre a existência de um termo maior e volta à condição de seguidor.

**[11:00–11:20 · Slide 10 — Citação]**

Esta frase separa duas garantias que costumam ser confundidas: a segurança do Raft vale mesmo durante uma partição de rede; a disponibilidade depende de haver, em algum momento, comunicação suficiente entre a maioria.

### Demonstração, exemplo ou estudo de caso

**[11:20–12:50 · Slide 11 — Termos, log replicado e confirmação]**

O tempo, no Raft, é dividido em termos numerados sequencialmente. Cada termo tem no máximo um líder, e toda mensagem carrega o número do termo. Isso permite rejeitar ordens vindas de um líder antigo, resolvendo por construção exatamente o problema da situação que abriu a aula.

*[indicação de edição: inserir Recurso visual 28 da Aula 7 — linha do tempo do log replicado, com as entradas sendo anexadas e confirmadas]*

O caminho de uma operação tem quatro passos. Primeiro, o líder anexa a nova operação ao seu log, no termo corrente. Segundo, replica aos seguidores por mensagens de append entries. Terceiro, confirma — e este é o ponto crítico — ao armazenar essa entrada do termo corrente em uma maioria. Quarto, aplica à máquina de estados e só então devolve o resultado ao cliente.

A ordem é essencial: o cliente só recebe resposta depois que a operação está durável em uma maioria de nós. É isso que impede que a resposta seja desmentida posteriormente.

**[12:50–14:10 · Slide 12 — Por que uma entrada antiga não se confirma sozinha]**

Há um detalhe sutil do Raft, ponto em que a maioria das implementações próprias falha.

Uma entrada de termo anterior não é confirmada diretamente só porque passou a aparecer em uma maioria de nós. Ela se torna confirmada indiretamente, quando uma entrada posterior do termo corrente é confirmada.

A razão de ser dessa regra é a seguinte: sem ela, uma entrada replicada em maioria ainda poderia ser sobrescrita por um líder futuro, em determinadas sequências de falha. A regra elimina essa possibilidade.

Combinada às restrições de eleição e de consistência do log, ela garante que entradas confirmadas sobrevivam a trocas de líder, que é a propriedade efetivamente desejada.

A consequência prática merece registro: “está na maioria” não é sinônimo de “está confirmado”. São afirmações diferentes, e confundi-las produz perda de dados em cenários raros — precisamente os que se manifestam em produção nos momentos mais inoportunos.

**[14:10–15:20 · Slide 13 — Segurança e progresso]**

Convém separar duas famílias de garantias, distinção que esclarece boa parte das discussões sobre o tema.

Segurança, ou safety, é o que o Raft garante sempre: no máximo um líder por termo; apenas um líder com maioria confirma entradas; e uma entrada confirmada nunca é perdida ou substituída. Mais importante ainda, isso vale mesmo sob partição de rede ou atraso arbitrário de mensagens. Nenhum comportamento da rede quebra essas garantias.

Progresso, ou liveness, é outra coisa: o cluster eventualmente elege um líder e continua processando operações. Isso exige, porém, maioria ativa trocando mensagens com atrasos compatíveis com os timeouts de eleição.

A assimetria entre as duas famílias é o ponto central da aula. Uma maioria apenas conectada, mas submetida indefinidamente a atrasos incompatíveis com os temporizadores, não garante progresso — o cluster pode eleger e reeleger sem avançar. As garantias de segurança, contudo, permanecem intactas. O sistema pode parar, mas não corrompe.

**[15:20–16:20 · Slide 14 — Consenso e CAP: o lado minoritário]**

A conexão com a aula anterior é direta. Considere um cluster de cinco nós que se divide, por uma partição de rede, em um grupo de três e outro de dois.

O grupo de três é maioria: elege líder e continua aceitando escritas normalmente.

O grupo de dois permanece sem líder até a partição ser resolvida. Ele não aceita escrita, mesmo estando perfeitamente saudável do ponto de vista de hardware.

O ponto essencial é que nenhum dos dois grupos está indisponível. Ambos operam, apenas isolados. É a mesma simetria da ilusão discutida na Aula 4.

Trata-se de aplicação direta do CAP: o Raft escolhe consistência, ou seja, comportamento CP, em detrimento da disponibilidade do lado minoritário. Essa escolha é propriedade do algoritmo, e não uma configuração ajustável.

**[16:20–17:40 · Slide 15 — Exemplo numérico: o custo de latência do consenso]**

O preço dessa escolha é concreto e pode ser quantificado.

Cada operação confirmada exige, no mínimo, uma rodada de comunicação entre o líder e seguidores suficientes para formar maioria. Como os envios são paralelos, o que determina o tempo é a resposta que completa o quórum.

Cenário um: três zonas próximas, com tempo de ida e volta de 4 milissegundos. A confirmação mínima é de aproximadamente 4 milissegundos.

Cenário dois: cluster intercontinental, com tempo de ida e volta de 120 milissegundos. A confirmação mínima é de aproximadamente 120 milissegundos.

São 30 vezes a latência mínima, e isso antes de qualquer processamento de negócio.

É por essa razão que clusters de consenso mantêm nós relativamente próximos entre si, ainda que o sistema como um todo seja global. Distribui-se o sistema e concentra-se o consenso.

**[17:40–18:30 · Slide 16 — Limites e custos do consenso]**

Para fechar o desenvolvimento, cabe examinar os limites que precisam ser conhecidos antes de se aplicar consenso indiscriminadamente.

O throughput é limitado pelo líder: é a capacidade dele de processar e replicar que define o teto do grupo inteiro. Adicionar seguidores não aumenta a vazão de escrita.

A escala de escrita vem do particionamento, ou seja, de vários grupos de consenso independentes — e não de múltiplos líderes no mesmo log. Isso conecta diretamente com a Aula 6.

O Raft pressupõe falhas de parada ou de rede: nós que param ou ficam inacessíveis. Ele não trata falhas bizantinas, isto é, nós que enviam informações deliberadamente incorretas. Consenso bizantino existe, e é relevante em redes de blockchain público, mas está fora do escopo desta disciplina.

Por fim, consenso não é gratuito. Aplicá-lo onde uma garantia mais fraca bastaria significa desperdiçar latência em toda operação.

### Aplicação profissional

**[18:30–19:15 · Slide 17 — Pausa para reflexão]**

Pause o vídeo e analise o cenário a seguir.

Um cluster de cinco nós está distribuído em três zonas: duas máquinas na zona A, duas na zona B e uma na zona C. Uma falha isola completamente a zona C e degrada parcialmente a comunicação entre A e B, sem isolá-las por completo.

*[indicação de edição: pausar a narração por 10 segundos com o diagrama das três zonas e o texto “Pense antes de continuar”]*

Considerando apenas o critério de maioria, quais combinações de nós ainda elegeriam um líder? Que diferença faz distribuir cinco nós em três zonas em vez de concentrá-los em duas? Em um cluster de apenas três nós, o que significaria uma manutenção programada que retira um nó? E que evidência operacional — métrica, log ou alerta — revelaria que o cluster está sem maioria?

O objetivo é praticar o raciocínio conjunto sobre maioria, topologia física e disponibilidade, retomando o conceito de zonas independentes de falha apresentado na Unidade 1. A matemática do quórum é simples; a dificuldade está em mapeá-la sobre a geografia real da infraestrutura.

### Fechamento

**[19:15–19:40 · Slides 18 e 19 — Pontos-chave e atividade prática]**

Recapitulando. Três propriedades: a decisão de consenso precisa ser válida, uniforme e irrevogável, mesmo com falhas. Maioria define tudo: um cluster de N nós tolera o piso de N menos 1 sobre 2 falhas, e números pares não aumentam a tolerância. Log em vez de estado: a máquina de estados replicada troca o problema de consistência pelo acordo sobre um log ordenado. Um líder por termo, com temporizadores aleatórios reduzindo empates. Confirmação tem regra: entradas de termos anteriores só se confirmam indiretamente, junto com uma entrada do termo corrente. E CP por construção: sob partição, apenas o lado majoritário progride.

Na atividade prática, você vai simular um cluster Raft de cinco nós, entregando diagrama e descrição de cada etapa: identificar o líder inicial no termo 1, simular a falha do líder e a sequência até a nova eleição, indicar o novo número de termo, simular três operações e sua replicação, indicar o ponto exato em que cada uma é confirmada e descrever como o log do nó que falhou é reconciliado ao voltar.

**[19:40–20:00 · Slide 20 — Encerramento]**

Esta aula estabelece como um conjunto de nós elege um líder e mantém um log replicado sem nenhuma intervenção manual, e a que custo. Na última aula da unidade, o problema muda de escopo: manter uma compra coerente atravessando quatro serviços com quatro bancos independentes.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 7 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Recurso visual 26 — cluster com dois líderes concorrentes, em cores conflitantes (aproximadamente 02:40).
- Slide 6 — fórmula da tolerância a falhas, com os quatro números aparecendo em sequência (aproximadamente 05:20).
- Recurso visual 27 — diagrama da eleição com temporizadores aleatórios expirando em instantes distintos (aproximadamente 09:30).
- Slide 10 — citação em tela cheia (11:00).
- Recurso visual 28 — linha do tempo do log replicado, com a confirmação por maioria destacada (aproximadamente 11:40).
- Slide 14 — partição do cluster em grupo de três e grupo de dois, com o minoritário esmaecido (aproximadamente 15:30).
- Slide 15 — comparação de latência entre cluster regional e intercontinental (aproximadamente 16:40).
- Slide 17 — pausa de reflexão de 10 segundos com o diagrama das três zonas (aproximadamente 18:45).
- Slide 20 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- ONGARO, Diego; OUSTERHOUT, John. In search of an understandable consensus algorithm. In: USENIX ANNUAL TECHNICAL CONFERENCE, 2014, Philadelphia. *Proceedings* [...]. Berkeley: USENIX Association, 2014. p. 305-319 — referência conceitual, sem reprodução de trecho externo.
- LAMPORT, Leslie. The part-time parliament. *ACM Transactions on Computer Systems*, v. 16, n. 2, p. 133-169, 1998. DOI: 10.1145/279227.279229 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, linhas do tempo e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 7 (`unidade_2.md`) e do deck `unidade_2/slides/aula7.html`.

---

## Roteiro da Videoaula 8 — “Uma compra, quatro serviços, nenhuma transação única”

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 8 — Transações distribuídas, sagas e idempotência.

**Deck de apoio:** `unidade_2/slides/aula8.html` — 21 slides (capa, audiodescrição, sumário, 17 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar por que a atomicidade de um banco não se estende a operações entre serviços, descrever as duas fases do 2PC e seu cenário de bloqueio, modelar uma saga com ações compensatórias, escolher entre coreografia e orquestração, aplicar os padrões outbox e inbox e projetar operações idempotentes que sobrevivam a reentregas.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:40 atomicidade local e distribuída · 04:50 confirmação em duas fases · 06:20 o bloqueio do 2PC · 07:40 exemplo numérico dos participantes · 09:10 citação · 09:30 sagas · 10:50 coreografada ou orquestrada · 12:20 ações compensatórias · 13:40 escrita dupla e outbox · 15:10 inbox · 16:40 at-least-once · 18:00 a saga completa · 18:50 transição para a Unidade 3 · 19:20 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a última aula da Unidade 2, dedicada a transações distribuídas, sagas e idempotência. Ela articula o conteúdo anterior, ao tratar do problema que permanece depois que cada serviço já resolveu suas questões internas.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o diagrama das duas fases do 2PC, o quadro comparativo entre saga coreografada e orquestrada, a tabela de ações compensatórias, o diagrama do padrão outbox e o fluxo completo da saga da NexaOrder. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo separando atomicidade local de atomicidade distribuída. Apresento em seguida a confirmação em duas fases e o problema de bloqueio que ela carrega. Trato então de sagas, comparando coreografia e orquestração, e discuto ações compensatórias e o que elas não conseguem desfazer. Passo depois a dois padrões práticos que resolvem problemas concretos: o outbox, contra a escrita dupla, e o inbox, para deduplicação atômica. Fecho com entrega pelo menos uma vez, efeito efetivamente único, e a saga completa da NexaOrder montada peça por peça.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir explicar por que a atomicidade de um banco não se estende a operações entre serviços. Deve descrever as duas fases do 2PC e identificar o cenário de bloqueio do coordenador. Deve modelar uma saga com transações locais e ações compensatórias correspondentes. Deve escolher entre coreografia e orquestração a partir do número de passos e da necessidade de rastreio. Deve aplicar os padrões outbox e inbox para eliminar escrita dupla e efeito duplicado. E deve projetar operações idempotentes que sobrevivam a reentregas do tipo at-least-once.

**[02:20–03:40 · Slide 4 — Situação-problema]**

Com replicação, particionamento e consenso resolvidos dentro de cada serviço, restou o problema que atravessa todos eles. Uma compra na NexaOrder toca pedidos, estoque, pagamento e expedição — e cada um desses serviços tem o seu próprio banco de dados.

Não existe mais uma transação única capaz de garantir que os quatro passos aconteçam todos ou nenhum. Aquela garantia confortável do banco relacional simplesmente não se estende para além do banco.

O que ocorreu em teste de carga foi o seguinte: o pagamento foi autorizado, mas uma falha de rede impediu que a confirmação chegasse a tempo ao serviço de pedidos. O cliente viu a interface travada, tentou novamente, e dois pagamentos foram processados para a mesma compra.

O padrão é o silêncio ambíguo, apresentado na Aula 1. A diferença é que, em vez do diagnóstico, esta aula constrói a solução completa.

### Desenvolvimento conceitual

**[03:40–04:50 · Slide 5 — Atomicidade local e distribuída]**

Convém organizar o problema.

Dentro de um banco, a atomicidade é responsabilidade do próprio sistema de gerenciamento: ele aplica todas as operações ou nenhuma, mesmo em caso de falha no meio do processo. Essa garantia vem pronta.

Entre bancos independentes, nenhuma transação única garante essa propriedade automaticamente. Não existe commit global implícito.

Resta, portanto, um mecanismo explícito de coordenação entre os serviços. A palavra-chave é explícito: alguém precisa projetá-lo, pois ele não decorre da infraestrutura.

A escolha que organiza o restante da aula é entre duas famílias: coordenar bloqueando, que é o 2PC, ou coordenar compensando, que são as sagas.

**[04:50–06:20 · Slide 6 — Confirmação em duas fases (2PC)]**

O primeiro caminho é a confirmação em duas fases, ou two-phase commit.

*[indicação de edição: inserir Recurso visual 29 da Aula 8 — diagrama das duas fases do 2PC, com o coordenador ao centro e os participantes ao redor]*

Um coordenador conduz a transação distribuída em etapas. Primeiro, a preparação: o coordenador pergunta a cada participante se ele está pronto para confirmar a sua parte. Segundo, a resposta: cada participante executa provisoriamente, bloqueia os recursos envolvidos e responde “pronto” ou “abortar”. Terceiro, a confirmação: se todos responderam “pronto”, o coordenador ordena a confirmação definitiva. Quarto, o aborto: se algum respondeu “abortar” ou não respondeu a tempo, o coordenador ordena desfazer em todos.

Cabe reconhecer o mérito do algoritmo: o 2PC de fato garante atomicidade distribuída e cumpre o que promete. O custo é manter recursos bloqueados durante toda a espera pela decisão, e é esse custo que determina a maioria das escolhas de arquitetura.

**[06:20–07:40 · Slide 7 — O bloqueio do 2PC]**

O cenário crítico é este: o coordenador falha depois da fase de preparação e antes de comunicar a decisão final.

Considere o que isso significa para cada participante. Ele já executou provisoriamente, já bloqueou os recursos e já respondeu “pronto”, mas desconhece se deve confirmar ou desfazer. E não pode decidir isoladamente, porque outro participante pode ter respondido “abortar”. Permanece, assim, bloqueado à espera.

A recuperação exige registrar a decisão de forma durável antes da falha e, em geral, um processo que consulte o registro do coordenador assim que ele retornar. É viável, mas constitui infraestrutura adicional que precisa funcionar exatamente no pior momento.

O custo cresce com o número de participantes e com a duração da transação. Por isso o 2PC é pouco usado em operações de negócio longas. Ele é mais comum em transações curtas, dentro do mesmo domínio de infraestrutura, onde o coordenador e os participantes compartilham a mesma operação.

**[07:40–09:10 · Slide 8 — Exemplo numérico: por que mais participantes pioram o risco]**

Um número torna esse argumento consideravelmente mais forte.

Suponha que cada um dos quatro serviços tenha, isoladamente, 1% de chance de estar lento ou indisponível em um dado instante, tratando-se os eventos como independentes — mais uma vez, simplificação assumida apenas para este cálculo.

A chance de pelo menos um atrasar a transação é 1 menos 0,99 elevado a 4, o que dá aproximadamente 3,9%.

O risco agregado é, portanto, quase quatro vezes o risco individual: com 1% em cada serviço, o conjunto se aproxima de 4%.

Quanto mais participantes um coordenador precisa reunir, maior a chance de a transação inteira ficar condicionada ao elo mais lento. E isso vale mesmo quando nenhum serviço falhou efetivamente — basta que esteja lento.

Somado ao risco de bloqueio na falha do coordenador, esse é o argumento decisivo contra o 2PC em fluxos com muitos serviços independentes. O argumento é aritmético, não doutrinário.

**[09:10–09:30 · Slide 9 — Citação]**

Esta frase é a advertência mais importante da segunda metade da aula: uma compensação nem sempre é o inverso perfeito da operação original — estornar um pagamento já processado pode envolver taxas e prazos diferentes de nunca ter cobrado.

### Demonstração, exemplo ou estudo de caso

**[09:30–10:50 · Slide 10 — Sagas: transações locais encadeadas]**

O segundo caminho, dominante em arquiteturas de serviços, é a saga.

Uma saga substitui a transação distribuída única por uma sequência de transações locais, cada uma confinada a um serviço e encadeada por eventos ou comandos. Cada etapa é atômica dentro do próprio banco, garantia já disponível.

As diferenças em relação ao 2PC são três. Primeira: não há desfazer instantâneo. Quando uma etapa falha, a saga não reverte tudo automaticamente como o 2PC faria. Segunda: existe compensação — a saga executa ações que revertem logicamente o efeito das etapas já concluídas. Terceira: não há bloqueio global. Cada transação local confirma e libera seus recursos imediatamente.

Todo ganho tem preço, e o preço aqui é a existência de um intervalo em que o sistema está parcialmente aplicado. O estoque já foi reservado, mas o pagamento ainda não foi autorizado. E isso precisa ser visível — para o cliente, para o suporte, para a operação. Um estado intermediário que ninguém consegue observar é um estado que ninguém consegue diagnosticar.

**[10:50–12:20 · Slide 11 — Coreografada ou orquestrada]**

Existem dois estilos de saga, e a escolha entre eles é uma decisão real de arquitetura.

*[indicação de edição: inserir Recurso visual 30 da Aula 8 — quadro comparativo entre saga coreografada e orquestrada, revelado linha a linha]*

Na saga coreografada, cada serviço publica eventos e os demais reagem, sem coordenação central. O fluxo fica implícito, disperso entre os serviços, o que dificulta saber em que etapa uma saga se encontra. Esse estilo funciona bem para poucos passos e acoplamento mínimo. O cuidado necessário é relevante: o processo de negócio não existe em lugar algum — não há arquivo, diagrama executável ou componente que represente o funcionamento de uma compra. Ele está distribuído pelo sistema.

Na saga orquestrada, um orquestrador central envia comandos explícitos. O fluxo fica concentrado em um componente, o que facilita acompanhamento e auditoria, e é preferível para fluxos longos com muitas compensações. O cuidado aqui é outro: o orquestrador concentra conhecimento. Uma distinção, porém, é fundamental — ao contrário do 2PC, ele não bloqueia recursos. Concentrar coordenação não equivale a bloquear.

**[12:20–13:40 · Slide 12 — Ações compensatórias]**

Como não existe transação global para desfazer, cada etapa que altera estado precisa de uma compensação capaz de revertê-la de forma consistente com o negócio.

Na NexaOrder: reservar estoque tem como compensação liberar a reserva. Autorizar pagamento tem como compensação estornar o valor autorizado. Gerar etiqueta de expedição tem como compensação cancelar a etiqueta antes do despacho.

A relação parece simétrica, mas não é, e nisso reside o ponto mais sutil da aula. A compensação nem sempre é o inverso perfeito da operação. Estornar um pagamento pode envolver taxas de processamento, prazos de devolução ou políticas comerciais inteiramente distintas de nunca ter cobrado. O cliente cobrado e estornado teve experiência diferente do cliente que nunca foi cobrado, ainda que o saldo final coincida.

Algumas ações, ademais, não têm compensação: se a etiqueta já se converteu em despacho e o produto saiu do centro de distribuição, cancelar deixa de ser opção e o caso passa a ser de logística reversa.

Projetar a compensação é, por isso, uma decisão de negócio tanto quanto técnica. E, sempre que possível, a saga deve ser ordenada de modo a deixar as etapas irreversíveis por último.

**[13:40–15:10 · Slide 13 — Escrita dupla e o padrão outbox]**

Há um problema prático presente em toda arquitetura orientada a eventos: a escrita dupla.

O cenário é este: o serviço grava no banco e depois publica o evento. São duas operações separadas, em dois sistemas diferentes. Uma falha entre elas faz com que o evento nunca seja publicado — ou, na ordem inversa, que seja publicado sem que a alteração tenha sido persistida. Em ambos os casos, o sistema fica inconsistente.

*[indicação de edição: inserir Recurso visual 31 da Aula 8 — diagrama do padrão outbox, com a transação única englobando alteração de negócio e tabela de eventos]*

A solução é o padrão outbox, em quatro passos. Primeiro: uma única transação local grava a alteração de negócio e o evento em uma tabela auxiliar. Uma transação, dois registros, atomicidade garantida pelo banco. Segundo: essa tabela outbox vive dentro do banco do próprio serviço — não é um sistema externo. Terceiro: um processo separado lê essa tabela e publica os eventos na mensageria de forma confiável. Quarto: o resultado é que evento e estado ficam consistentes, sem precisar de transação distribuída entre banco e mensageria.

A elegância da solução está em substituir um problema difícil — coordenar dois sistemas — por um problema simples: uma transação local, recurso já dominado.

**[15:10–16:40 · Slide 14 — Inbox: deduplicação que só funciona atômica]**

O inbox complementa o outbox, do lado do consumidor. O detalhe que o torna correto é a fronteira transacional, ponto em que a maioria das implementações falha.

Em uma única transação local, o consumidor insere o identificador da mensagem, com restrição de unicidade, e aplica a alteração de negócio. As duas coisas juntas, na mesma transação.

Se o identificador já existe, a mensagem é duplicata, e o efeito não se repete. Se houver falha antes do commit, tanto o registro do identificador quanto a alteração são revertidos — e a reentrega vai tentar de novo, corretamente.

O erro comum consiste em fazer isso em transações separadas, o que é inseguro. Registrando-se o identificador primeiro e ocorrendo falha antes de aplicar a alteração, a mensagem será descartada na reentrega como já processada, embora o efeito nunca tenha ocorrido. A operação se perde silenciosamente, e o defeito é difícil de localizar precisamente porque não gera erro.

Há ainda uma limitação a registrar: para efeitos externos ao banco local — chamar um provedor de pagamento, por exemplo — o inbox sozinho não basta. Ele precisa ser combinado com outbox, estados intermediários ou idempotência no próprio destino.

**[16:40–18:00 · Slide 15 — At-least-once e efeito efetivamente único]**

Cabe fechar o raciocínio sobre duplicação.

A entrega pelo menos uma vez, at-least-once, é o padrão da mensageria: em caso de dúvida, ela reentrega. Duplicatas são, portanto, esperadas, e não excepcionais. Não constituem falha do sistema de mensageria, e sim seu comportamento correto.

Quanto ao exactly-once anunciado por alguns produtos, ele existe dentro de limites específicos e bem documentados. O efeito de negócio ponta a ponta, contudo, continua dependendo das fronteiras transacionais adotadas. Nenhum produto de mensageria garante que um provedor de pagamento externo deixe de cobrar duas vezes.

O que se constrói, então, é o efeito efetivamente único, combinando três elementos: deduplicação, alteração de estado atômica e operações idempotentes.

Os componentes concretos já foram apresentados na Aula 2. A chave é por operação lógica, criada antes do primeiro envio e reutilizada em todas as retentativas daquela operação. A fronteira precisa ser atômica: verificar e inserir a chave, aplicar a mudança e armazenar o resultado, tudo na mesma transação.

Retomando o incidente que abriu a aula: com esse desenho, as duas tentativas do cliente carregariam a mesma chave. O serviço reconheceria a segunda, devolveria o resultado já registrado e não cobraria novamente.

### Aplicação profissional

**[18:00–18:50 · Slide 16 — A saga completa da NexaOrder]**

Os elementos da aula se reúnem no desenho completo do fluxo.

*[indicação de edição: inserir Recurso visual 32 da Aula 8 — fluxo completo da saga da NexaOrder, com as etapas normais em azul e as compensações em amarelo]*

Uma saga orquestrada para a compra, com as compensações explícitas. Etapa 1: reservar estoque, com compensação liberar a reserva. Etapa 2: autorizar pagamento, com compensação estornar o valor autorizado. Etapa 3: confirmar pedido, com compensação marcar o pedido como cancelado. Etapa 4: solicitar expedição, com compensação cancelar a etiqueta antes do despacho.

Os padrões da aula operam sobre esse fluxo. Cada etapa publica seu evento via outbox. Cada consumidor grava o inbox e o efeito de negócio na mesma transação local. E a chave de idempotência da operação é reutilizada em todas as retentativas.

Dois cenários demonstram o funcionamento. Se a autorização de pagamento falhar, a compensação libera a reserva de estoque, de modo que o cliente não permanece com uma unidade retida. Se a expedição falhar depois do pagamento, o valor é estornado e o pedido é cancelado.

Nada disso é automático. Cada compensação foi escrita por alguém que decidiu, explicitamente, o que significa desfazer aquela etapa.

**[18:50–19:20 · Slide 17 — Transição para a Unidade 3]**

Cabe articular a unidade como um todo. Ela tratou de como os dados da NexaOrder são replicados, particionados, coordenados por consenso e mantidos coerentes por sagas.

A Unidade 3 desloca o foco dos dados para os próprios serviços. Como decompor a NexaOrder em limites de domínio bem definidos? Como uma arquitetura orientada a eventos organiza produtores, consumidores e tópicos? Como contêineres e Kubernetes automatizam implantação e recuperação desses serviços? E como garantir comunicação segura e identidade entre eles?

Há continuidade evidente: o padrão outbox e as sagas estudados nesta aula reaparecem como parte central da arquitetura orientada a eventos da próxima unidade. Nada do que foi visto aqui é descartado.

### Fechamento

**[19:20–19:40 · Slides 18 e 19 — Pontos-chave e atividade prática]**

Recapitulando. Atomicidade não se estende: a garantia de um único banco não cobre operações que atravessam múltiplos serviços. 2PC bloqueia: garante atomicidade distribuída, mas prende recursos e fica vulnerável à falha do coordenador. Saga compensa: substitui a transação única por transações locais encadeadas com ações compensatórias. Coreografia ou orquestração: a primeira dispensa coordenador, a segunda torna o fluxo explícito e rastreável. Outbox e inbox: o outbox elimina a escrita dupla, e o inbox só evita efeito duplicado se identificador e alteração estiverem na mesma transação. E a idempotência fecha a conta: como a entrega é at-least-once, o efeito único depende de a operação ser idempotente.

Na atividade prática, você vai modelar a saga completa pedido, estoque, pagamento e expedição, em um diagrama de fluxo com etapas normais e compensações claramente distinguidas — listando as compensações, escolhendo entre coreografia e orquestração com justificativa, indicando onde aplicar o outbox, definindo onde a chave de idempotência é criada, reutilizada e verificada, mostrando a fronteira transacional do inbox e explicando o que ocorre se houver falha antes do commit.

**[19:40–20:00 · Slide 20 — Encerramento]**

A Unidade 2 se encerra com a capacidade de manter uma operação coerente entre quatro bancos independentes, sem coordenador bloqueante e sem duplicação de efeitos. A Unidade 3 leva essas ideias para o desenho dos serviços e para a plataforma que os executa. Bons estudos.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 8 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com os dois pagamentos duplicados destacados (02:20–03:40).
- Recurso visual 29 — diagrama das duas fases do 2PC, com o coordenador falhando entre as fases (aproximadamente 05:00).
- Slide 8 — cálculo do risco agregado com quatro participantes (aproximadamente 07:50).
- Slide 9 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (09:10).
- Recurso visual 30 — quadro comparativo entre saga coreografada e orquestrada (aproximadamente 11:00).
- Recurso visual 31 — diagrama do padrão outbox, com a transação única em destaque (aproximadamente 13:50).
- Slide 14 — comparação entre inbox atômico e inbox em transações separadas (aproximadamente 15:20).
- Recurso visual 32 — fluxo completo da saga da NexaOrder, com compensações em cor distinta (aproximadamente 18:10).
- Slide 20 — vinheta de encerramento e transição para a Unidade 3 (últimos 15 segundos).

### Fontes e links de mídia

- GARCIA-MOLINA, Hector; SALEM, Kenneth. Sagas. *ACM SIGMOD Record*, v. 16, n. 3, p. 249-259, 1987. DOI: 10.1145/38714.38742 — referência conceitual, sem reprodução de trecho externo.
- RICHARDSON, Chris. *Microservices Patterns: With Examples in Java*. Shelter Island: Manning, 2018 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas, quadros e fluxos devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 8 (`unidade_2.md`) e do deck `unidade_2/slides/aula8.html`.
