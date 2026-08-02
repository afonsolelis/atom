# Entrega de Trabalho (PBL) — Distributed Systems Engineering

> **Arquivo-mestre de produção.** A Parte A é a versão do estudante. A Parte B, ao final, é exclusiva do professor tutor e não pode ser incluída no arquivo distribuído aos estudantes. A versão mestra já foi gerada no modelo institucional; antes da distribuição, devem ser exportadas e aprovadas cópias separadas, com a versão estudantil encerrada antes da Parte B.

- **Disciplina:** Distributed Systems Engineering
- **Professor-conteudista:** Afonso Cesar Lelis Brandão
- **Prazo de produção:** 16 de agosto de 2026

> O **caso** existe para que o estudante entenda a aplicabilidade do conteúdo estudado na realidade do mercado de trabalho.

---

# Parte A — Versão do estudante

## 1. Título

**Operação Black Friday: evolução arquitetural da NexaOrder**

---

## 2. Desafio

> **O quê?** A **NexaOrder**, plataforma fictícia de pedidos, pagamentos e expedição utilizada como fio condutor da disciplina, precisa **evoluir sua arquitetura** para suportar a Black Friday sem indisponibilidade, sem cobrança duplicada e sem perda de pedidos, aplicando os fundamentos de comunicação, tempo/falhas, replicação/consistência, consenso, sagas, arquitetura orientada a eventos, contêineres/Kubernetes, segurança e observabilidade estudados nas 4 unidades.
>
> **Quem?** A equipe de engenharia da NexaOrder, uma operação de comércio eletrônico de médio porte que hoje roda como um **monólito modular em uma única região**, com um único banco relacional e sem mensageria. Você foi contratado(a) como **engenheiro(a) de sistemas distribuídos** para liderar o plano de evolução antes do próximo evento.
>
> **Quando?** Restam **90 dias** até a Black Friday. O plano de evolução deve estar implantável dentro desse prazo, em fases.
>
> **Onde?** A operação atual roda em **3 instâncias sem estado** atrás de um balanceador, cada uma sustentando cerca de **200 requisições por segundo**, e em **um único banco de dados relacional**, sem réplicas, na mesma zona de disponibilidade. Não há fila de mensagens: toda comunicação entre os serviços de pedidos, estoque, pagamento e expedição é síncrona, via chamadas HTTP diretas.
>
> **Por quê?** A Black Friday do ano anterior expôs os limites dessa arquitetura. **Indicadores do incidente anterior (diagnóstico)**:
>
> - **Tráfego de pico observado:** picos de **6.000 requisições por segundo** durante 40 minutos, contra uma capacidade sustentada atual de **600 requisições por segundo** (3 instâncias × 200 requisições/s) — um fator de **10×**.
> - **Disponibilidade atual:** 99,5% mês a mês, equivalente a **3h36min de indisponibilidade em uma janela de 30 dias**; meta contratual para o próximo evento: **99,95%**, equivalente a **21min36s na mesma janela**.
> - **Cobrança duplicada:** em picos anteriores, **2% das chamadas ao provedor de pagamento sofreram timeout**; sem idempotência, isso gerou cobrança duplicada em **cerca de 0,3% dos pedidos** do dia — o equivalente a centenas de estornos manuais.
> - **Ponto único de falha de dados:** o banco relacional único não tem réplica; uma falha nele derruba pedidos, estoque, pagamento e expedição simultaneamente.
> - **Sem isolamento de falhas:** quando o provedor de pagamento ficou lento por 8 minutos, as chamadas síncronas represaram threads em todos os serviços a jusante, e o site inteiro ficou inacessível — não apenas o pagamento.
> - **Sem observabilidade distribuída:** não há rastreamento entre serviços; o diagnóstico do incidente levou mais de 3 horas porque a equipe precisou correlacionar registros manualmente.
> - **Orçamento de infraestrutura aprovado para o evento:** até **4× o custo mensal atual de infraestrutura**, não mais que isso. Como o caso não fornece preços unitários nem a composição integral da fatura, o estudante deverá declarar as premissas de custo e apresentar cenários ou limites, sem alegar um valor exato que os dados não permitam calcular.
>
> **Sua missão como engenheiro(a) de sistemas distribuídos:** propor e justificar tecnicamente um **plano de evolução arquitetural completo e defensável** para a NexaOrder suportar a Black Friday, integrando os fundamentos das 4 unidades da disciplina (comunicação/tempo/falhas, dados distribuídos/consenso, serviços/eventos/plataformas nativas de nuvem, operação/observabilidade/resiliência), com diagnóstico, arquitetura-alvo dimensionada numericamente, plano de migração faseado e evidências de que a arquitetura proposta atende às metas.

---

## 3. Fontes de pesquisa

O estudante deverá pesquisar como a indústria projeta e opera sistemas distribuídos de alta escala:

1. **Material da disciplina** — as 16 aulas, com ênfase na Unidade 1 (comunicação, tempo, modelos de falha), Unidade 2 (replicação, particionamento, CAP, consenso, sagas), Unidade 3 (decomposição em serviços, eventos, Kubernetes, segurança) e Unidade 4 (observabilidade, testes de resiliência, engenharia do caos).
2. KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O’Reilly Media, 2017 — fonte bibliográfica secundária para replicação, particionamento e consistência.
3. APACHE SOFTWARE FOUNDATION. *Apache Kafka documentation*. [S. l.], [s. d.]. Disponível em: <https://kafka.apache.org/documentation/>. Acesso em: 1 ago. 2026 — fonte técnica primária.
4. KUBERNETES AUTHORS. *Kubernetes documentation*. [S. l.], [s. d.]. Disponível em: <https://kubernetes.io/docs/>. Acesso em: 1 ago. 2026 — fonte técnica primária.
5. ONGARO, Diego; OUSTERHOUT, John. In search of an understandable consensus algorithm. In: USENIX ANNUAL TECHNICAL CONFERENCE, 2014, Philadelphia. *Proceedings [...]*. Berkeley: USENIX Association, 2014. p. 305-319. Disponível em: <https://raft.github.io/raft.pdf>. Acesso em: 1 ago. 2026 — artigo primário sobre Raft.
6. BEYER, Betsy; JONES, Chris; PETOFF, Jennifer; MURPHY, Niall Richard (ed.). *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol: O’Reilly Media, 2016. Disponível em: <https://sre.google/sre-book/table-of-contents/>. Acesso em: 1 ago. 2026.
7. OPENTELEMETRY AUTHORS. *OpenTelemetry documentation*. [S. l.], [s. d.]. Disponível em: <https://opentelemetry.io/docs/>. Acesso em: 1 ago. 2026 — fonte técnica primária.
8. **Caso real selecionado pelo estudante** — relato público, identificável e referenciado conforme a ABNT, produzido por uma equipe de engenharia sobre preparação para pico sazonal. Não basta citar genericamente “blogs de empresas”.

As fontes 3, 4, 5 e 7 constituem o conjunto mínimo de quatro fontes técnicas primárias. O estudante pode substituí-las por fontes primárias equivalentes, desde que justifique a escolha e apresente a referência completa.

**Aulas relacionadas:** todas as 16 servem de insumo. Em ordem de relevância: Aula 1 (escalabilidade horizontal, disponibilidade, dimensionamento), Aula 2 (comunicação síncrona/assíncrona, *timeouts*, idempotência), Aula 4 (*circuit breaker*, *bulkhead*), Aulas 5–8 (replicação, CAP, consenso, sagas), Aulas 9–11 (decomposição de serviços, eventos, Kubernetes), Aula 12 (segurança entre serviços), Aulas 13–14 (observabilidade, testes de resiliência e caos).

---

## 4. Componentes avaliativos, submissão e pontuação

A avaliação possui **três componentes obrigatórios**: parte teórica (25%), parte prática com memorial de cálculo (50%) e vídeo de apresentação (25%). Para a submissão, o estudante enviará **um PDF único**, contendo as partes teórica e prática e o memorial como anexo, e **um link para o vídeo** ao final desse PDF.

O objetivo é elaborar um **plano de evolução arquitetural** baseado nos fundamentos das 4 unidades, demonstrando capacidade de diagnosticar os limites da arquitetura atual, propor mecanismos técnicos dimensionados numericamente e construir um plano de migração faseado, dentro do orçamento. Os números devem ser calculados e demonstrados passo a passo, e não estimados sem fundamentação.

### 1. Parte Teórica — (25% da nota)

Desenvolva um **relatório técnico em PDF** contendo:

- Diagnóstico da **arquitetura atual da NexaOrder** e dos seus pontos de falha (capacidade sustentada, ponto único de falha de dados, ausência de isolamento entre serviços, ausência de observabilidade), com dados verificáveis do caso.
- **Modelo de falha** esperado para o evento: quais componentes podem falhar, de que forma (parada, omissão, temporização) e qual o impacto em cascata caso não haja isolamento.
- Fundamentação teórica das soluções propostas, utilizando os conceitos das 4 unidades e as referências pesquisadas.

### 2. Parte Prática — (50% da nota)

Desenvolva uma **proposta técnica completa** para a evolução da NexaOrder contemplando, no mínimo:

- **Dimensionamento de capacidade, com cálculo numérico**: número mínimo de instâncias sem estado necessárias para o pico de 6.000 requisições/s com margem operacional.
- **Estratégia de dados**: replicação (fator de replicação, quóruns de leitura/escrita) e particionamento do catálogo/estoque, com justificativa de consistência (forte, causal ou eventual) por domínio de dado.
- **Coordenação**: onde e por que aplicar consenso (ex.: reserva de estoque, eleição de líder de um serviço crítico), com estimativa de quóruns e tolerância a falhas de nós.
- **Comunicação assíncrona e sagas**: migração do fluxo pedido→estoque→pagamento→expedição de chamadas síncronas para uma saga orientada a eventos, com padrão *outbox*, idempotência e ações compensatórias; dimensionamento do número de partições de tópicos com base na taxa de eventos esperada.
- **Isolamento de falhas e Kubernetes**: aplicação de *circuit breaker* e *bulkhead* nas chamadas ao provedor de pagamento; estratégia de escalonamento automático (HPA) em Kubernetes para absorver o pico dentro do orçamento aprovado.
- **Observabilidade e SLOs**: definição de SLIs/SLOs para o fluxo de finalização da compra, cálculo do orçamento de erro compatível com a meta de 99,95% e plano de rastreamento distribuído.
- **Plano de teste de resiliência**: um experimento de engenharia do caos (hipótese de estado estável, raio de impacto, mecanismo de interrupção) simulando a indisponibilidade do provedor de pagamento antes do evento real.
- **Memorial de cálculo** — **anexo obrigatório do PDF** com os cálculos que sustentam numericamente as decisões do plano, cada um com **fórmula, substituição dos dados do caso, premissas e resultado**, demonstrado passo a passo. No mínimo:
  - **(a) Dimensionamento de instâncias** — aplicar
    $$
    N = \left\lceil \frac{\lambda_{\text{pico}}}{C_{\text{instância}} \times U_{\text{alvo}}} \right\rceil
    $$
    aos 6.000 requisições/s de pico do caso, com a capacidade de 200 requisições/s por instância e a utilização-alvo escolhida (justificar a escolha entre 60% e 80%).
  - **(b) Disponibilidade e orçamento de erro** — usar uma janela de 30 dias para calcular quantos minutos de indisponibilidade as metas de 99,5% e 99,95% permitem; comparar, respectivamente, 216 minutos e 21,6 minutos.
  - **(c) Dimensionamento de partições de tópico** — primeiro estimar a taxa de eventos por meio de
    $$
    \lambda_{\text{eventos}} = \lambda_{\text{HTTP}} \times p_{\text{pedidos}} \times e_{\text{eventos por pedido}},
    $$
    declarando e justificando a proporção de requisições que representa pedidos e o número médio de eventos por pedido. Depois, dividir pela vazão-alvo por partição e acrescentar margem de crescimento. **Não se deve equiparar automaticamente 6.000 requisições HTTP/s a 6.000 eventos/s.**
  - **(d) Cenário de custo** — expressar o custo mensal como soma do custo de base com o custo adicional ponderado pelas horas de pico. Como faltam preços unitários, apresentar as premissas e uma análise de sensibilidade que demonstre em quais condições o teto relativo de 4× é respeitado.
  - **(e) (opcional) Quórum de replicação** — para um fator de replicação escolhido (por exemplo, 3 réplicas), definir W e R que satisfaçam $W + R > N$ no modelo simplificado adotado e justificar as hipóteses, a latência e os limites dessa garantia.

A proposta poderá conter diagramas de arquitetura, fluxogramas da saga, tabelas comparativas antes/depois e demais representações gráficas que auxiliem na comunicação da solução. **Rastreabilidade:** os resultados do memorial devem ser **citados e discutidos** no documento técnico — não basta anexar a conta solta.

### 3. Vídeo de apresentação — (25% da nota)

Grave um **vídeo de até 5 minutos**, simulando uma apresentação técnica para a diretoria da NexaOrder e defendendo o plano desenvolvido. O vídeo deverá apresentar:

- Contextualização do problema (incidente do ano anterior: indisponibilidade, cobrança duplicada, ponto único de falha).
- Justificativa das **prioridades** do plano (o que muda primeiro e por quê) e do faseamento em 90 dias.
- Explicação das principais soluções (replicação/consenso, sagas orientadas a eventos, isolamento de falhas, observabilidade) e dos **números calculados** (instâncias necessárias, orçamento de erro, partições de tópico).
- Demonstração dos ganhos esperados (capacidade, disponibilidade, eliminação de cobrança duplicada, tempo de diagnóstico).
- Reflexão sobre riscos residuais e o que será monitorado durante o evento.

O vídeo deverá ser publicado no **YouTube (modo não listado)** ou em outra plataforma de hospedagem, e o **link deverá ser inserido ao final do PDF**. Antes da submissão, verifique se o link está correto e acessível para a correção.

**Critérios qualitativos transversais:** **clareza** e organização do texto e dos diagramas; **profundidade técnica** (não generalidades sobre “usar microsserviços”); **realismo** dos números (capacidade, orçamento de infraestrutura, disponibilidade); **coerência interna** (diagnóstico → arquitetura-alvo → migração → evidências alinhados); **rastreabilidade** (os cálculos do memorial devem usar os dados e as premissas declaradas e ser citados no documento); e **integração** dos conceitos das 4 unidades.

---

## Roteiro do estudante

### 1. Leia o desafio

Sua primeira tarefa é entender o desafio proposto. Leia o cenário da **Operação Black Friday da NexaOrder** com atenção:

- **Quem** é a NexaOrder e qual é a arquitetura atual (monólito modular, 3 instâncias, banco único, comunicação síncrona)?
- **Qual** é a dor mais clara do incidente anterior (fator 10× de tráfego, cobrança duplicada, indisponibilidade em cascata)?
- **Quais** restrições foram colocadas (90 dias, orçamento de até 4× o custo mensal, meta de 99,95% de disponibilidade)?
- **Onde** estão os gargalos hoje (capacidade de 600 requisições/s, ponto único de falha no banco, ausência de isolamento e de observabilidade)?

Tome **notas estruturadas** dos indicadores atuais (600 requisições/s contra 6.000 requisições/s de pico, 99,5% contra 99,95% de disponibilidade, 2% de *timeouts* de pagamento e 0,3% de cobrança duplicada). Esses números são sua **base argumentativa**. Separe dados fornecidos pelo caso de premissas que você precisar adotar.

### 2. Fontes de pesquisa

Antes de propor a solução, reúna referências e ancore seus números:

- **Releia** as Unidades 1 a 4 — todas são insumo direto (comunicação e falhas, replicação e consenso, serviços e eventos, observabilidade e resiliência).
- **Aprofunde** os conceitos que vai aplicar: fórmula de dimensionamento de instâncias, cálculo de disponibilidade e orçamento de erro, quóruns de replicação ($W + R > N$), dimensionamento de partições de tópico, padrão saga com *outbox* e idempotência, *circuit breaker*, *bulkhead*, SLI/SLO e engenharia do caos — todos demonstrados **passo a passo** no memorial de cálculo.
- **Consulte** a documentação oficial de Kafka e Kubernetes, o algoritmo Raft e o Google SRE Book para embasar as escolhas técnicas.
- **Pesquise** ordens de grandeza de mercado para eventos de pico sazonal em relatos públicos de equipes de engenharia de comércio eletrônico e fundamente suas premissas de infraestrutura.

Não esqueça de trazer um **exemplo concreto** de como outra empresa se preparou para um pico de tráfego sazonal semelhante.

### 3. Entrega

Como orientação editorial desta atividade, estruture o **documento técnico em PDF, com 14 a 20 páginas antes dos anexos**, assim:

1. **Capa e sumário executivo** (1 página) — 5 linhas com a recomendação central.
2. **Diagnóstico da arquitetura atual e do incidente anterior** (2 a 3 páginas) — números do caso, pontos de falha, causa-raiz da cobrança duplicada.
3. **Arquitetura-alvo** (4 a 6 páginas) — replicação e consenso, saga orientada a eventos, isolamento de falhas (*circuit breaker* e *bulkhead*), Kubernetes, escalonamento automático, observabilidade e SLOs, com dimensionamento numérico.
4. **Plano de migração em 90 dias** (2 páginas) — fases, dependências entre fases, marcos de validação.
5. **Plano de teste de resiliência** (1 a 2 páginas) — experimento de engenharia do caos antes do evento.
6. **Riscos residuais e monitoramento durante o evento** (1 a 2 páginas).
7. **Referências** — fontes consultadas, ABNT.

Inclua no mesmo PDF, como anexo, o **memorial de cálculo** que sustenta os seus números. Reúna nele, no mínimo: (a) o dimensionamento de instâncias para o pico de 6.000 requisições/s; (b) o cálculo de disponibilidade e orçamento de erro; (c) o dimensionamento de partições a partir de uma taxa de eventos derivada e justificada; e (d) o cenário de custo. Cada cálculo deve apresentar fórmula, dados, premissas, substituição e resultado. Os resultados precisam aparecer e ser discutidos no corpo do documento.

Para o **vídeo de apresentação (até 5 minutos)**:

- Abra com **a recomendação central** e o problema (fator 10× de tráfego, cobrança duplicada, indisponibilidade em cascata).
- Mostre o diagnóstico e as prioridades do plano com 2–3 números fortes.
- Apresente as soluções e os **principais cálculos do memorial** (instâncias, orçamento de erro, partições) em alto nível.
- Feche com o **plano de 90 dias**, a viabilidade orçamentária sob as premissas declaradas e os riscos residuais.
- Publique no **YouTube (modo não listado)** e cole o **link ao final do PDF** — confira se está acessível.

**Dica final:** capriche na **defesa numérica**. Uma diretoria não aprova ideia bonita — aprova plano com **números defensáveis**. Cada decisão (número de instâncias, fator de replicação, quórum, número de partições) deve estar ancorada em cálculo ou referência técnica, não em opinião — e o **memorial de cálculo** é a sua prova de que o número foi de fato calculado, não chutado.

Esse projeto é seu **portfólio final** — o tipo de plano que se apresenta a lideranças técnicas para defender decisões de arquitetura de sistemas distribuídos. **Capriche**.

Boa entrega!

---

# Parte B — Versão exclusiva do professor tutor

> **NÃO DISTRIBUIR AOS ESTUDANTES.** Esta parte contém a solução esperada e a orientação de correção. Ao gerar a versão do estudante, encerrar o documento em “Boa entrega!”. Ao gerar a versão do tutor, incluir as Partes A e B e aplicar o modelo institucional.

## Solução esperada e critérios de correção

**Diagnóstico esperado:** a arquitetura atual sustenta 600 requisições/s e enfrenta pico de 6.000 requisições/s, portanto está subdimensionada por um fator de 10 antes mesmo da margem operacional. Também apresenta ponto único de falha no banco, acoplamento síncrono sem isolamento e ausência de observabilidade distribuída.

**Dimensionamento de capacidade esperado:** aplicando

$$
N = \left\lceil \frac{\lambda_{\text{pico}}}{C_{\text{instância}} \times U_{\text{alvo}}} \right\rceil
$$

com $\lambda_{\text{pico}} = 6.000$, $C_{\text{instância}} = 200$ e $U_{\text{alvo}} = 0{,}70$:

$$
N = \left\lceil \frac{6.000}{200 \times 0{,}70} \right\rceil
  = \left\lceil 42{,}86 \right\rceil
  = 43 \text{ instâncias}.
$$

O resultado corresponde ao pico simultâneo sob as premissas simplificadas de capacidade homogênea e distribuição uniforme da carga. Ele não comprova, sozinho, que o teto de custo de 4× será atendido. A resposta deve separar capacidade de pico de custo mensal e explicitar limitações como composição do tráfego, gargalos de banco e dependências externas.

**Disponibilidade e orçamento de erro esperados:** em uma janela de 30 dias, há 43.200 minutos. Assim:

- 99,5% permite $43.200 \times 0{,}005 = 216$ minutos, ou 3h36min;
- 99,95% permite $43.200 \times 0{,}0005 = 21{,}6$ minutos, ou 21min36s.

A resposta deve usar a mesma janela para as duas metas e relacionar a redução do orçamento de erro à remoção de pontos únicos de falha, à recuperação automática e ao isolamento de dependências.

**Estratégia de dados esperada:** uma proposta defensável pode adotar fator de replicação 3 distribuído entre zonas, comutação automática testada e políticas diferentes por domínio. Catálogo descritivo pode tolerar consistência eventual; estoque e registro interno de pagamentos exigem garantias mais fortes. No modelo simplificado de quórum, $N=3$, $W=2$ e $R=2$ satisfazem $W+R>N$. O estudante deve declarar que essa desigualdade pressupõe conjuntos de réplicas sobrepostos e não substitui a análise do protocolo real.

**Coordenação, pagamento e idempotência:** consenso pode ser justificado para uma máquina de estados replicada ou para eleição de líder em uma função crítica. Consistência do estado interno não impede, por si só, cobrança duplicada em um provedor externo. A solução deve combinar chave de idempotência, consulta/reconciliação do estado do pagamento e consumo idempotente de eventos.

**Sagas e eventos:** o fluxo pedido→estoque→pagamento→expedição pode migrar para uma saga orquestrada ou coreografada. O padrão *outbox* evita a gravação do estado sem o registro transacional do evento; uma chave como `pedido_id` preserva a ordenação por pedido dentro de uma partição.

A taxa de eventos deve ser derivada, e não copiada da taxa HTTP. Exemplo meramente ilustrativo: se 20% das 6.000 requisições/s iniciarem pedidos e cada pedido produzir, em média, quatro eventos principais, então

$$
\lambda_{\text{eventos}} = 6.000 \times 0{,}20 \times 4 = 4.800 \text{ eventos/s}.
$$

Com vazão-alvo de 1.000 eventos/s por partição, o mínimo matemático seria 5 partições; 8 poderia ser escolhido como margem operacional. Outros resultados são aceitáveis quando as premissas e a fonte da vazão forem justificadas.

**Custo esperado:** como o caso não fornece preços, a resposta deve trabalhar com cenários. Uma forma aceitável é modelar

$$
C_{\text{mês}}
= C_{\text{fixo}}
+ \sum_j N_j \times h_j \times c_{\text{instância-hora}}
+ C_{\text{dados}}
+ C_{\text{mensageria}},
$$

variar os custos desconhecidos e demonstrar em quais cenários $C_{\text{mês}} \leq 4 \times C_{\text{atual}}$. Não se deve conceder pontuação integral a uma afirmação de compatibilidade orçamentária sem premissas.

**Isolamento e Kubernetes:** *circuit breaker* reduz tentativas contra uma dependência degradada; *bulkhead* isola os recursos usados para cada dependência; HPA ajusta o número desejado de réplicas com métricas e limites. A resposta deve considerar também a capacidade do *cluster*, o banco, a mensageria e os limites orçamentários, pois HPA não cria capacidade física ilimitada.

**Observabilidade:** são aceitas formulações distintas, desde que SLI e SLO sejam mensuráveis e coerentes. Exemplos: (a) SLI de proporção de finalizações bem-sucedidas em até 3 segundos, com SLO de 99% em 30 dias; ou (b) SLI de latência p95, com SLO de p95 inferior a 3 segundos. Não misturar percentil e proporção na mesma definição. O rastreamento distribuído deve correlacionar o pedido entre serviços.

**Teste de resiliência:** o experimento deve começar em ambiente controlado, definir hipótese de estado estável, raio de impacto, métricas e mecanismo de interrupção. Uma boa proposta injeta indisponibilidade ou latência no pagamento e verifica se navegação, carrinho e consulta de pedidos permanecem dentro de seus SLOs.

**Plano de migração esperado:** um faseamento defensável pode iniciar por instrumentação e SLOs; seguir para replicação, idempotência e *outbox*; depois introduzir isolamento e escalonamento; e terminar com testes de carga, recuperação e caos antes do evento. Fases podem se sobrepor se dependências e critérios de saída forem claros.

**Resposta de alta qualidade:** apresenta premissas rastreáveis, cálculos reproduzíveis, coerência entre diagnóstico, arquitetura, migração e evidências, além de riscos residuais e limites das soluções.

**Resposta de baixa qualidade:** recomenda “migrar tudo para microsserviços” sem dimensionamento; confunde tráfego HTTP com taxa de eventos; declara que o orçamento será respeitado sem premissas; propõe consistência forte em tudo sem discutir latência; ou trata consenso como substituto da idempotência de pagamentos.
