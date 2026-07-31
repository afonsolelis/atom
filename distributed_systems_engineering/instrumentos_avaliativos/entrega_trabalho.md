# Entrega de Trabalho (PBL) — Distributed Systems Engineering

> Roteiro para elaboração com **Problem-Based Learning**.

- **Disciplina:** Distributed Systems Engineering
- **Professor-conteudista:** Afonso Cesar Lelis Brandão
- **Prazo de produção:** 16 de agosto de 2026

> O **CASE** existe para que o estudante entenda a aplicabilidade do conteúdo estudado na realidade do mercado de trabalho.

---

## 1. Título

**Operação Black Friday — Plano de Evolução Arquitetural da NexaOrder para Suportar 10× o Tráfego sem Perder Pedidos**

---

## 2. Desafio

> **O quê?** A **NexaOrder**, plataforma fictícia de pedidos, pagamentos e expedição utilizada como fio condutor da disciplina, precisa **evoluir sua arquitetura** para suportar a Black Friday sem indisponibilidade, sem cobrança duplicada e sem perda de pedidos, aplicando os fundamentos de comunicação, tempo/falhas, replicação/consistência, consenso, sagas, arquitetura orientada a eventos, contêineres/Kubernetes, segurança e observabilidade estudados nas 4 unidades.
>
> **Quem?** A equipe de engenharia da NexaOrder, uma operação de e-commerce de médio porte que hoje roda como um **monólito modular em uma única região**, com um único banco relacional e sem mensageria. Você foi contratado(a) como **engenheiro(a) de sistemas distribuídos** para liderar o plano de evolução antes do próximo evento.
>
> **Quando?** Restam **90 dias** até a Black Friday. O plano de evolução deve estar implantável dentro desse prazo, em fases.
>
> **Onde?** A operação atual roda em **3 instâncias sem estado** atrás de um balanceador, cada uma sustentando cerca de **200 requisições por segundo**, e em **um único banco de dados relacional**, sem réplicas, na mesma zona de disponibilidade. Não há fila de mensagens: toda comunicação entre os serviços de pedidos, estoque, pagamento e expedição é síncrona, via chamadas HTTP diretas.
>
> **Por quê?** A Black Friday do ano anterior expôs os limites dessa arquitetura. **Indicadores do incidente anterior (diagnóstico)**:
>
> - **Tráfego de pico observado:** picos de **6.000 requisições por segundo** durante 40 minutos, contra uma capacidade sustentada atual de **600 requisições por segundo** (3 instâncias × 200 req/s) — um fator de **10×**.
> - **Disponibilidade atual:** 99,5% mês a mês, equivalente a **≈ 3h36min de indisponibilidade por mês**; meta contratual para o próximo evento: **99,95%** (≈ 21,9 minutos por mês).
> - **Cobrança duplicada:** em picos anteriores, **2% das chamadas ao provedor de pagamento sofreram timeout**; sem idempotência, isso gerou cobrança duplicada em **cerca de 0,3% dos pedidos** do dia — o equivalente a centenas de estornos manuais.
> - **Ponto único de falha de dados:** o banco relacional único não tem réplica; uma falha nele derruba pedidos, estoque, pagamento e expedição simultaneamente.
> - **Sem isolamento de falhas:** quando o provedor de pagamento ficou lento por 8 minutos, as chamadas síncronas represaram threads em todos os serviços a jusante, e o site inteiro ficou inacessível — não apenas o pagamento.
> - **Sem observabilidade distribuída:** não há tracing entre serviços; o diagnóstico do incidente levou mais de 3 horas porque a equipe precisou correlacionar logs manualmente.
> - **Orçamento de infraestrutura aprovado para o evento:** até **4× o custo mensal atual de infraestrutura**, não mais que isso.
>
> **Sua missão como engenheiro(a) de sistemas distribuídos:** propor e justificar tecnicamente um **plano de evolução arquitetural completo e defensável** para a NexaOrder suportar a Black Friday, integrando os fundamentos das 4 unidades da disciplina (comunicação/tempo/falhas, dados distribuídos/consenso, serviços/eventos/cloud-native, operação/observabilidade/resiliência), com diagnóstico, arquitetura-alvo dimensionada numericamente, plano de migração faseado e evidências de que a arquitetura proposta atende às metas.

---

## 3. Fontes de pesquisa

O estudante deverá pesquisar como a indústria projeta e opera sistemas distribuídos de alta escala:

1. **Material da disciplina** — as 16 aulas, com ênfase na Unidade 1 (comunicação, tempo, modelos de falha), Unidade 2 (replicação, particionamento, CAP, consenso, sagas), Unidade 3 (decomposição em serviços, eventos, Kubernetes, segurança) e Unidade 4 (observabilidade, testes de resiliência, engenharia do caos).
2. **KLEPPMANN, M. Designing Data-Intensive Applications.** Sebastopol: O'Reilly Media, 2017 — replicação, particionamento e consistência.
3. **Apache Kafka Documentation** — <https://kafka.apache.org/documentation/> — tópicos, partições, grupos de consumidores e semânticas de entrega.
4. **Kubernetes Documentation** — <https://kubernetes.io/docs/> — Deployments, HPA (Horizontal Pod Autoscaler), reconciliação e escalonamento.
5. **Raft Consensus Algorithm** — <https://raft.github.io/> — eleição de líder e replicação de log para o componente de coordenação.
6. **Google SRE Book** — <https://sre.google/sre-book/table-of-contents/> — SLI, SLO, orçamento de erro e prática de observabilidade.
7. **OpenTelemetry Documentation** — <https://opentelemetry.io/docs/> — instrumentação e tracing distribuído.
8. **Casos reais de picos sazonais** — relatos públicos de engenharia de grandes varejistas e marketplaces sobre preparação para eventos de pico (ex.: postmortems e blogs de engenharia de empresas de e-commerce), usados como referência de ordens de grandeza e práticas de mercado.

**Aulas relacionadas:** todas as 16 servem de insumo. Em ordem de relevância: Aula 1 (escalabilidade horizontal, disponibilidade, dimensionamento), Aula 2 (comunicação síncrona/assíncrona, timeouts, idempotência), Aula 4 (circuit breaker, bulkhead), Aulas 5–8 (replicação, CAP, consenso, sagas), Aulas 9–11 (decomposição de serviços, eventos, Kubernetes), Aula 12 (segurança entre serviços), Aulas 13–14 (observabilidade, testes de resiliência e caos).

---

## 4. Entregável e distribuição da pontuação

Sua entrega final da disciplina **Distributed Systems Engineering** será composta por **3 entregáveis obrigatórios**. O objetivo é elaborar um **plano de evolução arquitetural** baseado nos fundamentos das 4 unidades, demonstrando capacidade de diagnosticar os limites da arquitetura atual, propor mecanismos técnicos dimensionados numericamente e construir um plano de migração faseado, dentro do orçamento — com os **números calculados e demonstrados passo a passo**, e não estimados "no olho".

### 1. Parte Teórica — (25% da nota)

Desenvolva um **relatório técnico em PDF** contendo:

- Diagnóstico da **arquitetura atual da NexaOrder** e dos seus pontos de falha (capacidade sustentada, ponto único de falha de dados, ausência de isolamento entre serviços, ausência de observabilidade), com dados verificáveis do case.
- **Modelo de falha** esperado para o evento: quais componentes podem falhar, de que forma (parada, omissão, temporização) e qual o impacto em cascata caso não haja isolamento.
- Fundamentação teórica das soluções propostas, utilizando os conceitos das 4 unidades e as referências pesquisadas (Kleppmann, documentação de Kafka/Kubernetes, Raft, SRE Book).

### 2. Parte Prática — (50% da nota)

Desenvolva uma **proposta técnica completa** para a evolução da NexaOrder contemplando, no mínimo:

- **Dimensionamento de capacidade, com cálculo numérico**: número mínimo de instâncias sem estado necessárias para o pico de 6.000 req/s com margem operacional.
- **Estratégia de dados**: replicação (fator de replicação, quóruns de leitura/escrita) e particionamento do catálogo/estoque, com justificativa de consistência (forte, causal ou eventual) por domínio de dado.
- **Coordenação**: onde e por que aplicar consenso (ex.: reserva de estoque, eleição de líder de um serviço crítico), com estimativa de quóruns e tolerância a falhas de nós.
- **Comunicação assíncrona e sagas**: migração do fluxo pedido→estoque→pagamento→expedição de chamadas síncronas para uma saga orientada a eventos, com padrão outbox, idempotência e ações compensatórias; dimensionamento do número de partições de tópicos com base na taxa de eventos esperada.
- **Isolamento de falhas e Kubernetes**: aplicação de circuit breaker/bulkhead nas chamadas ao provedor de pagamento; estratégia de autoscaling (HPA) em Kubernetes para absorver o pico dentro do orçamento aprovado.
- **Observabilidade e SLOs**: definição de SLIs/SLOs para o fluxo de checkout, cálculo do orçamento de erro compatível com a meta de 99,95%, e plano de tracing distribuído.
- **Plano de teste de resiliência**: um experimento de engenharia do caos (hipótese de estado estável, raio de impacto, mecanismo de interrupção) simulando a indisponibilidade do provedor de pagamento antes do evento real.
- **Memorial de cálculo** — **anexo obrigatório** com os cálculos que **sustentam** numericamente as decisões do plano, cada um com **fórmula, substituição dos dados do case e resultado**, demonstrado passo a passo. No mínimo:
  - **(a) Dimensionamento de instâncias** — aplicar
    $$
    N = \left\lceil \frac{\lambda_{\text{pico}}}{C_{\text{instância}} \times U_{\text{alvo}}} \right\rceil
    $$
    aos 6.000 req/s de pico do case, com a capacidade de 200 req/s por instância e a utilização-alvo escolhida (justificar a escolha entre 60% e 80%).
  - **(b) Disponibilidade e orçamento de erro** — calcular quantos minutos de indisponibilidade a meta de 99,95% permite por mês e comparar com os ≈ 3h36min observados na arquitetura atual (99,5%).
  - **(c) Dimensionamento de partições de tópico** — estimar o número mínimo de partições do tópico de eventos de pedido a partir da taxa de eventos de pico e de uma vazão-alvo por partição (definida e justificada pelo estudante), com margem de crescimento.
  - **(d) (opcional) Quórum de replicação** — para um fator de replicação escolhido (ex.: 3 réplicas), definir W e R que garantam leitura consistente ($W + R > N$) e justificar o compromisso de latência versus consistência resultante.

A proposta poderá conter diagramas de arquitetura, fluxogramas da saga, tabelas comparativas antes/depois e demais representações gráficas que auxiliem na comunicação da solução. **Rastreabilidade:** os resultados do memorial devem ser **citados e discutidos** no documento técnico — não basta anexar a conta solta.

### 3. Vídeo Pitch — (25% da nota)

Grave um **vídeo de até 5 minutos**, simulando uma apresentação técnica para a diretoria da NexaOrder, defendendo o plano desenvolvido. O vídeo deverá apresentar:

- Contextualização do problema (incidente do ano anterior: indisponibilidade, cobrança duplicada, ponto único de falha).
- Justificativa das **prioridades** do plano (o que muda primeiro e por quê) e do faseamento em 90 dias.
- Explicação das principais soluções (replicação/consenso, sagas orientadas a eventos, isolamento de falhas, observabilidade) e dos **números calculados** (instâncias necessárias, orçamento de erro, partições de tópico).
- Demonstração dos ganhos esperados (capacidade, disponibilidade, eliminação de cobrança duplicada, tempo de diagnóstico).
- Reflexão sobre riscos residuais e o que será monitorado durante o evento.

O vídeo deverá ser publicado no **YouTube (modo não listado)** ou em outra plataforma de hospedagem, e o **link deverá ser inserido ao final do PDF**. Antes da submissão, verifique se o link está correto e acessível para a correção.

**Critérios qualitativos transversais:** **clareza** e organização do texto e dos diagramas; **profundidade técnica** (não generalidades sobre "usar microsserviços"); **realismo** dos números (capacidade, orçamento de infraestrutura, disponibilidade); **coerência interna** (diagnóstico → arquitetura-alvo → migração → evidências alinhados); **rastreabilidade** (os cálculos do memorial devem usar os números do case e ser citados no documento); e **integração** dos conceitos das 4 unidades (não tratar replicação, eventos, Kubernetes e observabilidade como tópicos isolados).

---

## 5. Solução

> **Atenção:** este tópico será removido antes do case ser disponibilizado ao aluno — é apenas para o professor tutor que corrigirá.

**Diagnóstico esperado:** arquitetura atual subdimensionada para o pico (600 req/s de capacidade contra 6.000 req/s de pico — fator 10×), com ponto único de falha no banco de dados, acoplamento síncrono sem isolamento (a lentidão do pagamento derruba todo o site) e ausência de observabilidade distribuída, exatamente os problemas discutidos nas Unidades 1, 2 e 4.

**Dimensionamento de capacidade esperado:** aplicando
$$
N = \left\lceil \frac{\lambda_{\text{pico}}}{C_{\text{instância}} \times U_{\text{alvo}}} \right\rceil
$$
com $\lambda_{\text{pico}} = 6.000$, $C_{\text{instância}} = 200$ e $U_{\text{alvo}} = 0{,}70$:
$$
N = \left\lceil \frac{6.000}{200 \times 0{,}70} \right\rceil = \left\lceil 42{,}86 \right\rceil = 43 \text{ instâncias}
$$
— cerca de **14× a capacidade atual** de 3 instâncias, o que é compatível com um autoscaling agressivo em Kubernetes durante a janela de pico e retorno ao patamar normal depois. O plano deve deixar claro que 43 é o **pico simultâneo**, não o custo médio do mês — o orçamento de 4× o custo atual deve ser calculado sobre o custo médio ponderado pelas horas de pico, não pelo pico constante.

**Disponibilidade e orçamento de erro esperados:** 99,5% permite ≈ 3h36min de indisponibilidade por mês, exatamente o que a NexaOrder vinha tolerando; 99,95% reduz essa margem para ≈ 21,9 minutos por mês. Isso exige eliminar o ponto único de falha do banco (via replicação com failover automático) e isolar falhas do provedor de pagamento (circuit breaker), pois qualquer indisponibilidade não planejada consome rapidamente o orçamento de erro do mês.

**Estratégia de dados esperada (U2):** réplicas do banco (ex.: fator de replicação 3, uma réplica em outra zona de disponibilidade), com leitura majoritária para o catálogo (tolerante a consistência eventual) e escrita/leitura com quórum mais forte para estoque e pagamento (onde a leitura obsoleta causa overselling). Para $N=3$, um quórum como $W=2, R=2$ garante $W+R>N$ e leitura consistente com tolerância a 1 réplica fora do ar.

**Coordenação esperada (U2):** uso de consenso (ex.: um serviço de reserva de estoque baseado em máquina de estados replicada) para evitar duas vendas simultâneas do último item — a NexaOrder já viu esse problema na Aula 1 da Unidade 1. Eleição de líder garante que apenas um nó decide reservas em um dado momento.

**Sagas e eventos esperados (U2 + U3):** o fluxo pedido→estoque→pagamento→expedição migra de chamadas HTTP síncronas em cadeia para uma **saga orquestrada ou coreografada** publicando eventos em tópicos particionados por `pedido_id` (garantindo ordenação por pedido); padrão **outbox** no serviço de pedidos evita perda de eventos; **idempotência** por identificador de operação elimina a cobrança duplicada observada (2% de timeouts não devem mais gerar 0,3% de cobranças duplicadas, pois reenvios passam a ser deduplicados). Dimensionamento de partições: para 6.000 eventos/s de pico e uma vazão-alvo de, por exemplo, 1.000 eventos/s por partição, o mínimo é 6 partições; com margem de crescimento, 8 a 12 partições é uma escolha defensável.

**Isolamento e Kubernetes esperados (U3):** circuit breaker nas chamadas ao provedor de pagamento evita que a lentidão dele derrube os demais serviços; bulkhead separa os pools de conexão por dependência; HPA em Kubernetes escala os serviços sem estado a partir de métricas de fila/latência, respeitando o teto orçamentário de 4× o custo mensal médio.

**Observabilidade e teste de resiliência esperados (U4):** SLI de latência (p95 do checkout) e de taxa de erro, com SLO alinhado a 99,95% e orçamento de erro correspondente; tracing distribuído (OpenTelemetry) correlacionando pedido→estoque→pagamento→expedição, reduzindo o tempo de diagnóstico de 3 horas para minutos; um experimento de caos controlado — injetar indisponibilidade simulada no provedor de pagamento em ambiente de teste, com hipótese de estado estável ("o restante do site continua respondendo") e raio de impacto limitado — deve ser executado **antes** do evento real, não durante.

**Plano de migração esperado (90 dias):** faseamento típico — Fase 1 (semanas 1–3): observabilidade e SLOs, para medir o ponto de partida; Fase 2 (semanas 3–7): réplicas de dados e quórum, saga com outbox e idempotência; Fase 3 (semanas 6–10): circuit breaker/bulkhead, HPA e ajuste de capacidade; Fase 4 (semanas 10–13): teste de carga e experimento de caos controlado antes do evento.

**Resposta de alta qualidade** demonstra: números realistas e calculados (instâncias, orçamento de erro, partições); coerência entre diagnóstico, arquitetura-alvo, migração e evidências; integração efetiva das 4 unidades (a saga depende da replicação, que depende da observabilidade para ser validada); tratamento sério de riscos residuais; e plano de migração compatível com o prazo e o orçamento do case.

**Resposta de baixa qualidade** comumente apresenta: "trocar tudo para microsserviços" sem dimensionamento numérico; ignorar o orçamento de infraestrutura de 4×; propor consistência forte em tudo sem discutir o custo de latência; esquecer idempotência (não resolvendo o problema real de cobrança duplicada do case); e não conectar observabilidade/testes de caos ao restante do plano.

---

## Roteiro do Estudante

### 1. Leia o desafio

Sua primeira tarefa é entender o desafio proposto. Leia o cenário da **Operação Black Friday da NexaOrder** com atenção:

- **Quem** é a NexaOrder e qual é a arquitetura atual (monólito modular, 3 instâncias, banco único, comunicação síncrona)?
- **Qual** é a dor mais clara do incidente anterior (fator 10× de tráfego, cobrança duplicada, indisponibilidade em cascata)?
- **Quais** restrições foram colocadas (90 dias, orçamento de até 4× o custo mensal, meta de 99,95% de disponibilidade)?
- **Onde** estão os gargalos hoje (capacidade de 600 req/s, ponto único de falha no banco, ausência de isolamento e de observabilidade)?

Tome **notas estruturadas** dos indicadores atuais (600 req/s vs. 6.000 req/s de pico, 99,5% vs. 99,95% de disponibilidade, 2% de timeouts de pagamento, 0,3% de cobrança duplicada). Esses números são sua **base argumentativa**.

### 2. Fontes de Pesquisa

Antes de propor a solução, reúna referências e ancore seus números:

- **Releia** as Unidades 1 a 4 — todas são insumo direto (comunicação e falhas, replicação e consenso, serviços e eventos, observabilidade e resiliência).
- **Aprofunde** os conceitos que vai aplicar: fórmula de dimensionamento de instâncias, cálculo de disponibilidade e orçamento de erro, quóruns de replicação ($W + R > N$), dimensionamento de partições de tópico, padrão saga com outbox e idempotência, circuit breaker/bulkhead, SLI/SLO e engenharia do caos — todos demonstrados **passo a passo** no memorial de cálculo.
- **Consulte** a documentação oficial de Kafka e Kubernetes, o algoritmo Raft e o Google SRE Book para embasar as escolhas técnicas.
- **Pesquise** ordens de grandeza de mercado para eventos de pico sazonal (relatos públicos de engenharia de e-commerce) e ancore seu orçamento de infraestrutura.

Não esqueça de trazer um **exemplo concreto** de como outra empresa se preparou para um pico de tráfego sazonal semelhante.

### 3. Entrega

Estruture o **documento técnico (PDF, 14-20 páginas)** assim:

1. **Capa e sumário executivo** (1 página) — 5 linhas com a recomendação central.
2. **Diagnóstico da arquitetura atual e do incidente anterior** (2-3 páginas) — números do case, pontos de falha, causa-raiz da cobrança duplicada.
3. **Arquitetura-alvo** (4-6 páginas) — replicação e consenso, saga orientada a eventos, isolamento de falhas (circuit breaker/bulkhead), Kubernetes/autoscaling, observabilidade e SLOs, com dimensionamento numérico.
4. **Plano de migração em 90 dias** (2 páginas) — fases, dependências entre fases, marcos de validação.
5. **Plano de teste de resiliência** (1-2 páginas) — experimento de engenharia do caos antes do evento.
6. **Riscos residuais e monitoramento durante o evento** (1-2 páginas).
7. **Referências** — fontes consultadas, ABNT.

Além do PDF e do vídeo pitch, entregue o **memorial de cálculo** que sustenta os seus números. Reúna nele, no mínimo: (a) o **dimensionamento de instâncias** para o pico de 6.000 req/s; (b) o **cálculo de disponibilidade e orçamento de erro** para a meta de 99,95%; e (c) o **dimensionamento de partições** do tópico de eventos de pedido. Regras: cada cálculo com **fórmula, substituição dos dados do case e resultado**, organizado de forma legível; os resultados precisam aparecer e ser discutidos no documento técnico (não basta anexar a conta solta). Lembre: a matemática vai escrita de forma clara, **passo a passo**.

Para o **vídeo pitch (até 5 minutos)**:

- Abra com **a recomendação central** e o problema (fator 10× de tráfego, cobrança duplicada, indisponibilidade em cascata).
- Mostre o diagnóstico e as prioridades do plano com 2–3 números fortes.
- Apresente as soluções e os **principais cálculos do memorial** (instâncias, orçamento de erro, partições) em alto nível.
- Feche com o **plano de 90 dias**, o orçamento respeitado e os riscos residuais.
- Publique no **YouTube (modo não listado)** e cole o **link ao final do PDF** — confira se está acessível.

**Dica final:** capriche na **defesa numérica**. Uma diretoria não aprova ideia bonita — aprova plano com **números defensáveis**. Cada decisão (número de instâncias, fator de replicação, quórum, número de partições) deve estar ancorada em cálculo ou referência técnica, não em opinião — e o **memorial de cálculo** é a sua prova de que o número foi de fato calculado, não chutado.

Esse projeto é seu **portfólio final** — o tipo de plano que se apresenta a lideranças técnicas para defender decisões de arquitetura de sistemas distribuídos. **Capricha**.

Boa entrega!
