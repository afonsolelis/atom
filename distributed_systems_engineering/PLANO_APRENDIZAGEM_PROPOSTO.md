# Plano de Aprendizagem Proposto

## Identificação

- **Disciplina:** *Distributed Systems Engineering*
- **Professor-conteudista:** Afonso Cesar Lelis Brandão
- **Natureza:** teórico-prática
- **Organização:** 4 unidades, 16 aulas e 16 videoaulas
- **Duração-base das videoaulas:** 20 minutos
- **Situação:** proposta provisória elaborada a partir do título da disciplina; deverá ser confrontada com o plano oficial quando ele for disponibilizado

## Ementa

Fundamentos, modelos e desafios de sistemas distribuídos. Arquiteturas cliente-servidor, em camadas, orientadas a serviços e orientadas a eventos. Comunicação entre processos por HTTP, APIs, RPC, mensageria e transmissão de eventos. Concorrência, tempo físico e lógico, ordenação de eventos e causalidade. Modelos de falha, tolerância a falhas, disponibilidade e particionamentos de rede. Replicação, particionamento de dados, modelos de consistência e teorema CAP. Coordenação distribuída, eleição de líder, consenso, Raft e máquinas de estado replicadas. Transações distribuídas, confirmação em duas fases, sagas, idempotência e consistência eventual. Microsserviços, descoberta de serviços, balanceamento, gateways e comunicação assíncrona. Plataformas de eventos, particionamento, grupos de consumidores e semânticas de entrega. Contêineres, orquestração, Kubernetes e reconciliação de estado. Observabilidade, segurança, resiliência, engenharia do caos e testes de sistemas distribuídos. Processamento distribuído de dados, computação em borda e funções como serviço. Projeto, avaliação e evolução de arquiteturas distribuídas considerando desempenho, escalabilidade, segurança, custo e confiabilidade.

## Justificativa

Aplicações modernas raramente permanecem confinadas a um único processo ou servidor. Comércio eletrônico, serviços financeiros, plataformas de mídia, sistemas industriais, aplicações de mobilidade e serviços em nuvem dependem de componentes que cooperam por meio de redes sujeitas a atraso, perda de mensagens, concorrência e falhas parciais. A disciplina prepara o estudante para raciocinar sobre essas condições, evitando tratar um conjunto de máquinas como se fosse um computador único.

O diferencial profissional está na capacidade de relacionar decisões arquiteturais a garantias verificáveis. O estudante deverá compreender não apenas como utilizar tecnologias, mas por que certas combinações de replicação, consistência, mensageria, consenso e observabilidade se comportam de determinada maneira diante de sobrecarga ou falha.

## Objetivo geral

Projetar, analisar, implementar e avaliar sistemas distribuídos escaláveis, observáveis, seguros e tolerantes a falhas, justificando decisões arquiteturais com base em modelos, algoritmos, requisitos de negócio e evidências operacionais.

## Objetivos específicos

Ao final da disciplina, o estudante deverá ser capaz de:

1. caracterizar um sistema distribuído e explicar seus principais desafios;
2. comparar estilos arquiteturais e mecanismos de comunicação;
3. modelar concorrência, causalidade, ordenação e falhas parciais;
4. selecionar estratégias de replicação, particionamento e consistência;
5. explicar o papel do consenso e de máquinas de estado replicadas;
6. projetar fluxos distribuídos idempotentes e recuperáveis;
7. avaliar transações locais e distribuídas, sagas e compensações;
8. projetar serviços síncronos e assíncronos com contratos explícitos;
9. empregar padrões de resiliência, observabilidade e segurança;
10. planejar testes de carga, falhas e recuperação;
11. analisar compromissos entre latência, disponibilidade, consistência, custo e complexidade;
12. documentar uma arquitetura distribuída e defender tecnicamente suas decisões.

## Competências desenvolvidas

### Competências técnicas

- modelagem de sistemas distribuídos;
- desenho de APIs e contratos de eventos;
- análise de consistência e disponibilidade;
- particionamento e replicação de dados;
- coordenação e consenso;
- tolerância a falhas;
- conteinerização e orquestração;
- observabilidade e resposta a incidentes;
- testes de resiliência e desempenho;
- documentação e decisão arquitetural.

### Competências profissionais

- pensamento sistêmico;
- resolução de problemas complexos;
- comunicação de compromissos técnicos;
- tomada de decisão orientada por evidências;
- colaboração entre desenvolvimento, operações, segurança e produto;
- análise de impacto técnico e de negócio;
- postura ética diante de disponibilidade, integridade e privacidade.

## Conhecimentos prévios recomendados

- lógica de programação;
- estruturas de dados;
- redes de computadores;
- conceitos básicos de bancos de dados;
- noções de sistemas operacionais;
- leitura de código e uso básico de linha de comando.

Não é necessário domínio prévio de uma plataforma de nuvem específica.

## Fio condutor prático

Durante a disciplina, o estudante acompanhará a evolução da **NexaOrder**, uma plataforma fictícia de pedidos, pagamentos e expedição.

O sistema começa como uma aplicação simples e passa a enfrentar:

- crescimento de tráfego;
- necessidade de múltiplas instâncias;
- falhas de rede;
- duplicação de mensagens;
- concorrência sobre estoque;
- integração com pagamentos;
- replicação de dados;
- eventos fora de ordem;
- indisponibilidade de serviços;
- implantação em múltiplas zonas;
- exigências de auditoria e observabilidade.

Cada unidade acrescentará decisões, mecanismos e evidências à arquitetura. O mesmo caso sustentará exemplos, desafios, videoaulas e o trabalho PBL.

# Organização das unidades

## Unidade 1 — Fundamentos, comunicação, tempo e falhas

### Resultado de aprendizagem da unidade

Analisar os elementos fundamentais de um sistema distribuído, modelar sua comunicação e reconhecer como concorrência, tempo e falhas parciais afetam o comportamento observado.

### Aula 1 — Pensar distribuído: conceitos, propriedades e compromissos

**Tópicos:**

- definição de sistema distribuído;
- distribuição como decisão arquitetural;
- transparência, heterogeneidade, concorrência e autonomia;
- escalabilidade horizontal e vertical;
- latência, throughput, disponibilidade e confiabilidade;
- arquiteturas cliente-servidor, em camadas e peer-to-peer;
- apresentação da NexaOrder e de seus requisitos iniciais.

**Prática da videoaula:** decompor uma aplicação centralizada e identificar quais problemas são criados pela distribuição.

### Aula 2 — Comunicação entre processos: APIs, RPC e mensageria

**Tópicos:**

- comunicação síncrona e assíncrona;
- HTTP e APIs orientadas a recursos;
- RPC e contratos de interface;
- serialização e evolução de esquema;
- filas, publicação-assinatura e eventos;
- timeouts, retries, backoff e jitter;
- idempotência e correlação de requisições.

**Prática da videoaula:** comparar um fluxo de criação de pedido por API síncrona e por mensageria.

### Aula 3 — Concorrência, relógios e ordenação de eventos

**Tópicos:**

- ausência de relógio global;
- relógios físicos, desvio e sincronização;
- relação *happened-before*;
- relógios lógicos de Lamport;
- relógios vetoriais;
- ordem total, ordem parcial e causalidade;
- conflitos concorrentes em estoque e pagamento.

**Prática da videoaula:** construir timestamps lógicos para uma sequência de eventos da NexaOrder.

### Aula 4 — Modelos de falha e desenho para recuperação

**Tópicos:**

- falhas de parada, omissão, temporização e comportamento arbitrário;
- falha parcial e detector de falhas;
- particionamento de rede;
- redundância e isolamento;
- timeout como decisão, não como prova de falha;
- padrões *circuit breaker*, *bulkhead* e degradação graciosa;
- introdução a objetivos de confiabilidade.

**Prática da videoaula:** realizar uma análise de modos de falha do fluxo de pedidos.

## Unidade 2 — Dados distribuídos, consistência e coordenação

### Resultado de aprendizagem da unidade

Projetar estratégias de distribuição e coordenação de estado, avaliando os compromissos entre consistência, disponibilidade, desempenho e tolerância a falhas.

### Aula 5 — Replicação e modelos de consistência

**Tópicos:**

- objetivos da replicação;
- replicação primário-réplica e multi-líder;
- replicação síncrona e assíncrona;
- leituras obsoletas e atraso de réplica;
- consistência forte, sequencial, causal e eventual;
- garantias centradas no cliente;
- quóruns de leitura e escrita.

**Prática da videoaula:** selecionar uma política de replicação para catálogo, estoque e pagamento.

### Aula 6 — Particionamento, CAP e escalabilidade de dados

**Tópicos:**

- particionamento horizontal;
- estratégias por faixa, hash e diretório;
- hashing consistente;
- rebalanceamento e pontos quentes;
- consultas entre partições;
- teorema CAP e comportamento durante partições;
- PACELC como extensão de análise de latência e consistência.

**Prática da videoaula:** escolher chaves de partição e simular crescimento desigual.

### Aula 7 — Consenso, eleição de líder e Raft

**Tópicos:**

- problema do consenso;
- maioria e quórum;
- máquina de estados replicada;
- eleição de líder;
- termos, log replicado e confirmação;
- segurança e disponibilidade no Raft;
- limites e custos do consenso.

**Prática da videoaula:** simular eleição, replicação e falha de líder em um cluster de cinco nós.

### Aula 8 — Transações distribuídas, sagas e idempotência

**Tópicos:**

- atomicidade local e distribuída;
- confirmação em duas fases;
- bloqueios, coordenador e recuperação;
- sagas coreografadas e orquestradas;
- ações compensatórias;
- padrões *outbox* e *inbox*;
- deduplicação e processamento efetivamente único.

**Prática da videoaula:** modelar a saga pedido–estoque–pagamento–expedição.

## Unidade 3 — Serviços, eventos e plataformas cloud-native

### Resultado de aprendizagem da unidade

Construir arquiteturas de serviços e eventos com contratos explícitos, mecanismos de descoberta e implantação automatizada, reconhecendo os custos operacionais da distribuição.

### Aula 9 — Decomposição em serviços e limites de domínio

**Tópicos:**

- monólito modular e microsserviços;
- coesão, acoplamento e autonomia;
- contexto delimitado e capacidade de negócio;
- dados por serviço;
- API Gateway e composição;
- comunicação entre serviços;
- riscos do monólito distribuído.

**Prática da videoaula:** definir os limites dos serviços da NexaOrder.

### Aula 10 — Arquitetura orientada a eventos

**Tópicos:**

- evento de domínio, comando e notificação;
- produtores, consumidores, tópicos e partições;
- ordenação por partição;
- grupos de consumidores;
- retenção e reprocessamento;
- semânticas *at-most-once*, *at-least-once* e *exactly-once*;
- evolução de esquemas e compatibilidade.

**Prática da videoaula:** desenhar tópicos, chaves e grupos de consumidores para o ciclo do pedido.

### Aula 11 — Contêineres, Kubernetes e reconciliação

**Tópicos:**

- imagem, contêiner e imutabilidade;
- cluster, nó, Pod, Deployment e Service;
- estado desejado e estado observado;
- controladores e laço de reconciliação;
- descoberta e balanceamento;
- configuração, segredos e armazenamento;
- escalonamento e atualizações graduais.

**Prática da videoaula:** interpretar manifestos e acompanhar a recuperação automática de uma instância.

### Aula 12 — Segurança e comunicação confiável entre serviços

**Tópicos:**

- identidade de serviço e confiança zero;
- autenticação, autorização e menor privilégio;
- TLS e proteção em trânsito;
- gestão de segredos;
- gateway, proxy lateral e *service mesh*;
- limitação de taxa e proteção contra sobrecarga;
- ameaças específicas de sistemas distribuídos.

**Prática da videoaula:** elaborar um fluxo autenticado e autorizado entre pedido e pagamento.

## Unidade 4 — Operação, validação e evolução

### Resultado de aprendizagem da unidade

Validar e operar sistemas distribuídos por meio de telemetria, testes, experimentos de falha e avaliação arquitetural baseada em requisitos e indicadores.

### Aula 13 — Observabilidade e diagnóstico distribuído

**Tópicos:**

- diferença entre monitoramento e observabilidade;
- métricas, logs e traces;
- contexto e correlação distribuída;
- instrumentação e OpenTelemetry;
- indicadores de nível de serviço;
- SLI, SLO e orçamento de erro;
- diagnóstico de latência e dependências.

**Prática da videoaula:** seguir um pedido por múltiplos serviços usando um trace distribuído.

### Aula 14 — Resiliência, testes distribuídos e engenharia do caos

**Tópicos:**

- pirâmide e escopo de testes;
- testes de contrato, integração e ponta a ponta;
- testes de carga, estresse e duração;
- injeção de latência, erro e indisponibilidade;
- hipótese de estado estável;
- raio de impacto e mecanismos de interrupção;
- recuperação e aprendizagem operacional.

**Prática da videoaula:** planejar um experimento controlado de indisponibilidade do serviço de pagamento.

### Aula 15 — Processamento distribuído, edge e serverless

**Tópicos:**

- processamento em lote e em fluxo;
- MapReduce e DAGs;
- particionamento, embaralhamento e tolerância a falhas;
- tempo de evento e janelas;
- funções como serviço;
- computação de borda;
- localização de dados e compromisso custo-latência.

**Prática da videoaula:** comparar alternativas para detectar fraude em tempo quase real.

### Aula 16 — Projeto integrado e avaliação arquitetural

**Tópicos:**

- requisitos funcionais e atributos de qualidade;
- estimativa de carga e capacidade;
- decisões e registros arquiteturais;
- análise de pontos únicos de falha;
- plano de consistência e recuperação;
- segurança e observabilidade desde o projeto;
- custo, sustentabilidade e evolução;
- revisão integral da NexaOrder.

**Prática da videoaula:** defender uma arquitetura final diante de cenários de carga e falha.

## Metodologia

A disciplina combinará:

- textos-base acadêmicos e dialógicos;
- videoaulas práticas de 20 minutos;
- estudos de caso;
- demonstrações e simulações;
- pausas para reflexão;
- diagramas arquiteturais;
- exercícios de decisão;
- questionários no padrão ENADE;
- projeto PBL;
- leitura de documentação técnica e artigos científicos.

## Estratégia de avaliação

### Avaliação formativa

- dois itens de quiz não avaliativo por unidade;
- desafios e pausas para reflexão;
- exercícios práticos nas videoaulas;
- atividade verificadora individual prevista no template da Unidade 1.

### Questionários

- 40 questões por unidade;
- 160 questões no total;
- padrão ENADE;
- distribuição provisória de 20 questões de asserção–razão e 20 de interpretação;
- cinco alternativas;
- feedback por alternativa.

### Trabalho PBL

Projeto arquitetural da NexaOrder ou de sistema equivalente, contendo:

- requisitos e estimativas;
- decomposição de componentes;
- decisões de comunicação;
- distribuição e consistência de dados;
- mecanismos de resiliência;
- segurança;
- observabilidade;
- estratégia de testes;
- análise de compromissos;
- diagrama e registros de decisão.

### Avaliação final

- 10 questões dissertativas;
- distribuição equilibrada entre as quatro unidades;
- situações-problema;
- modelo de resposta e critérios de correção.

## Critérios internos de produção

Os templates não determinam limite de palavras ou caracteres. Para assegurar robustez e previsibilidade, serão utilizados os seguintes alvos internos:

- relação com a atuação profissional: 300 a 500 palavras;
- texto-base de cada aula: 2.000 a 3.000 palavras;
- roteiro de videoaula: conteúdo planejado para 20 minutos, com cerca de 2.200 a 2.700 palavras faladas, ajustado pela presença de demonstrações;
- roteiro introdutório: até 2 minutos, aproximadamente 220 a 280 palavras;
- 3 a 5 recursos visuais por aula;
- 2 questões de quiz por unidade;
- 1 atividade verificadora na Unidade 1;
- 4 categorias de material complementar por unidade.

Esses números são metas de produção, não limites institucionais. Se o plano oficial trouxer outras medidas, ele prevalecerá.

## Bibliografia básica proposta

- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.
- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O’Reilly Media, 2017.
- TANENBAUM, Andrew S.; VAN STEEN, Maarten. *Distributed Systems*. 4. ed. [S. l.]: distributed-systems.net, 2023.

## Bibliografia complementar proposta

- BURNS, Brendan. *Designing Distributed Systems*. 2. ed. Sebastopol: O’Reilly Media, 2024.
- NEWMAN, Sam. *Building Microservices*. 2. ed. Sebastopol: O’Reilly Media, 2021.
- O’REILLY, Tim et al. *Site Reliability Engineering*. Sebastopol: O’Reilly Media, 2016.
- ONGARO, Diego; OUSTERHOUT, John. In search of an understandable consensus algorithm. In: USENIX ANNUAL TECHNICAL CONFERENCE, 2014, Philadelphia. *Proceedings [...]*. Berkeley: USENIX Association, 2014.
- RICHARDSON, Chris. *Microservices Patterns*. Shelter Island: Manning, 2018.

## Fontes técnicas de referência

- Apache Kafka Documentation: <https://kafka.apache.org/documentation/>
- Kubernetes Documentation: <https://kubernetes.io/docs/>
- OpenTelemetry Documentation: <https://opentelemetry.io/docs/>
- Raft Consensus Algorithm: <https://raft.github.io/>
