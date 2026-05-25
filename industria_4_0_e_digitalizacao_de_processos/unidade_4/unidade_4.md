# Unidade 4 — Implementação, Casos e Futuro

- **Disciplina:** Indústria 4.0 e Digitalização de Processos
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 13 a 16

> **Recap das unidades anteriores:** vimos o contexto histórico (U1), as tecnologias habilitadoras (U2) e as aplicações no chão de fábrica (U3). Agora chegamos à parte **mais aplicada** da disciplina: **como fazer acontecer**. Vamos sair da teoria e olhar para implementação, casos reais e o que vem depois da 4.0.

---

## Aula 13 — Mapeamento e digitalização de processos (BPM + Indústria 4.0)

Antes de digitalizar um processo, você precisa **entender** esse processo. Soa óbvio, mas é o passo que mais se pula em projetos de transformação digital — e por isso tantos falham. Esta aula é sobre **BPM (Business Process Management)** — a disciplina clássica de mapeamento e gestão de processos — e como ela se combina com a Indústria 4.0 para gerar resultado real.

![Diagrama BPMN simples com atividades, gateways e fluxo de eventos — a notação universal para mapear processos](https://commons.wikimedia.org/wiki/Special:FilePath/BPMN-AProcessWithNormalFlow.svg?width=800)

### O que é BPM (e por que ainda importa)

> **BPM (Business Process Management)** é a disciplina de **mapear, analisar, otimizar e monitorar** os processos de uma organização, com o objetivo de tornar a operação mais eficiente, padronizada e mensurável.

O BPM é dos anos 1990 — surge antes da Indústria 4.0. Mas é **pré-requisito** para qualquer transformação digital séria. A razão é simples: você só digitaliza bem o que você já entende bem. Tentar digitalizar processo bagunçado é multiplicar a bagunça com tecnologia.

### O ciclo BPM clássico

O BPM funciona em **6 etapas cíclicas**:

1. **Planejar** — definir objetivos, escopo, indicadores.
2. **Modelar (AS-IS)** — mapear o processo **como ele realmente é hoje** (não como deveria ser).
3. **Analisar** — encontrar gargalos, desperdícios, retrabalhos.
4. **Redesenhar (TO-BE)** — projetar o processo **como deveria ser**.
5. **Implementar** — executar a mudança (treinamento, sistemas, comunicação).
6. **Monitorar** — medir resultado e voltar ao passo 1.

A maioria dos engenheiros confunde o passo 2 (AS-IS) com o passo 4 (TO-BE). Esse é o erro mais comum: descrever o processo idealizado em vez do real. Resultado: as melhorias propostas miram em um processo que não existe.

### A notação BPMN

A linguagem universal para desenhar processos é o **BPMN (Business Process Model and Notation)** — padrão da OMG (Object Management Group). Em BPMN, você usa:

- **Atividades** (retângulos com cantos arredondados) — "o que é feito".
- **Eventos** (círculos) — início, fim, eventos intermediários.
- **Gateways** (losangos) — decisões, paralelismos.
- **Setas** — fluxo do processo.
- **Pools / Lanes** (raias) — quem executa cada parte.

Ferramentas como **Bizagi, Camunda, Lucidchart, Draw.io, Heflo** desenham BPMN. Algumas (Camunda) executam diretamente o diagrama como software.

### Onde BPM e Indústria 4.0 se encontram

A 4.0 trouxe três mudanças que reorganizam a forma de fazer BPM:

1. **Process mining** — em vez de **entrevistar** gente para mapear o AS-IS, você **extrai automaticamente** o processo dos logs dos sistemas (ERP, MES, CRM). Ferramentas: Celonis, UiPath Process Mining, Disco.
2. **Process automation (RPA)** — robôs de software (não físicos) executam tarefas administrativas repetitivas: copiar dado entre sistemas, gerar relatórios, conferir notas fiscais.
3. **Process intelligence** — usa IA para identificar padrões e sugerir melhorias automaticamente.

Esse trio — process mining + RPA + process intelligence — virou o **estado da arte** em digitalização de processos. Empresas como Magazine Luiza, Vale e Itaú usam intensivamente.

### Diferença entre BPM, RPA e workflow

Confusão comum. Vamos separar:

- **BPM** — disciplina ampla de gestão de processos (todo o ciclo).
- **RPA (Robotic Process Automation)** — automação de tarefas repetitivas via "robô" de software que interage com sistemas existentes.
- **Workflow** — automação de **fluxo de aprovação** (formulário → aprovador → próximo passo). Subcategoria do BPM.

BPM contém workflow; RPA pode ser parte da implementação do BPM. Não são sinônimos, mas se complementam.

### Exemplo numérico: ROI de digitalização de um processo administrativo

Cenário: emissão de pedido de compra em uma fábrica média (~5.000 pedidos/mês).

- **Antes (manual):** 2 funcionários gastam 4 horas/dia preenchendo planilha → enviando e-mail → conferindo. Custo: 2 × 8h × R\$ 30/h × 20 dias = R\$ 9.600/mês.
- **Depois (RPA + workflow):** 0,5 funcionário supervisiona o sistema (1h/dia). Custo: R\$ 600/mês.
- **Investimento:** R\$ 70.000 (licença RPA + integração + treinamento).
- **Economia mensal:** R\$ 9.000.
- **Payback:** ~8 meses.
- **Bônus:** redução de erros de digitação em ~95%.

### Caso brasileiro: process mining no Itaú

O **Itaú Unibanco** usa **Celonis** para monitorar mais de 100 processos em tempo real — desde abertura de conta até processamento de empréstimo. O sistema identifica desvios automaticamente: por exemplo, descobriu que 12% das aberturas de conta passavam por uma etapa desnecessária que adicionava 2 dias ao tempo médio. Eliminada a etapa, ganho mensurável em satisfação do cliente.

### Atividade prática

Pegue um **processo administrativo** ou **operacional** do seu dia a dia (na empresa, na faculdade, na vida pessoal):

1. Desenhe o processo **AS-IS** em BPMN simples (caixinhas, setas, losangos).
2. Identifique **2 gargalos** ou **2 desperdícios**.
3. Proponha um **TO-BE** que remova esses problemas.
4. Que **tecnologia** (RPA, IIoT, IA) ajudaria no TO-BE?

### Pontos-chave

- **BPM** é pré-requisito para transformação digital — você só digitaliza bem o que entende bem.
- O ciclo BPM tem **6 etapas**: planejar, AS-IS, analisar, TO-BE, implementar, monitorar.
- **BPMN** é a notação universal — atividades, eventos, gateways, lanes.
- A 4.0 trouxe **process mining, RPA e process intelligence** — trio que mudou a forma de fazer BPM.
- Não confunda **BPM, RPA e workflow**: são complementares, não sinônimos.

### Para saber mais

- **ABPMP — Associação Brasileira de BPM:** https://www.abpmp-br.org/
- **Celonis Academy:** https://www.celonis.com/academy/ (cursos gratuitos)
- **Bizagi Modeler (ferramenta gratuita):** https://www.bizagi.com/pt/produtos/bpm-suite/modeler
- **Vídeo (UiPath Brasil, YouTube):** "RPA na prática"

---

## Aula 13 — Roteiro da Videoaula 13: "Mapeie antes de digitalizar — a regra que ninguém respeita"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Tem um erro que aprendi na pele em 15 anos de projeto: digitalizar processo bagunçado é multiplicar a bagunça. Hoje a gente vai falar de **BPM** — a disciplina chata, mas indispensável, de mapear e arrumar o processo **antes** de comprar tecnologia."

### 2. O que é BPM e o ciclo (0:40 – 3:30)

- Definir BPM em uma frase.
- Mostrar o ciclo de 6 etapas.
- Reforçar a confusão AS-IS vs TO-BE.

### 3. BPMN (3:30 – 5:30)

- Mostrar 4 elementos básicos: atividade, evento, gateway, lane.
- Ferramentas (Bizagi, Camunda, Draw.io).

### 4. BPM + 4.0 (5:30 – 8:30)

- Trio: process mining + RPA + process intelligence.
- Caso Itaú (Celonis, -2 dias em abertura de conta).
- ROI: R\$ 9 mil/mês com R\$ 70 mil investido = 8 meses.

### 5. Encerramento (8:30 – 11:00)

> "Próxima aula: já que mapear é o pré-requisito, **como** se constrói um **roadmap real** de transformação? É o que vamos ver. Te espero!"

---

## Aula 14 — Roadmap de implementação da Indústria 4.0

> **Pausa para reflexão:** se um diretor da sua empresa pedisse, agora, "me dá um plano de 18 meses para a gente virar 4.0", você teria por onde começar? Pense nisso enquanto avançamos.

Existe um abismo entre **entender** as tecnologias da 4.0 e **construir um plano realista** de adoção. Esta aula é sobre o segundo desafio — talvez o mais importante para você como engenheiro(a) de produção.

![Aeronave Embraer E190 — produto da fabricante brasileira referência em roadmap de transformação digital de longo prazo](https://commons.wikimedia.org/wiki/Special:FilePath/Embraer_E190.jpg?width=800)

### Por que a maioria dos projetos 4.0 falha

Estudos da McKinsey e BCG mostram que **70% das iniciativas de transformação digital industriais falham** em entregar o ROI esperado. As causas mais comuns:

1. **Começar pela tecnologia** ("vamos colocar IA") em vez do problema de negócio.
2. **Falta de patrocínio executivo** — CEO topou na reunião, mas não acompanha.
3. **Equipe errada** — só TI ou só chão de fábrica; deveria ter ambos.
4. **Escolher problema errado** — atacar algo de baixo impacto ou alta complexidade.
5. **Querer revolução, não evolução** — querer fazer tudo de uma vez, em vez de pequenos passos.
6. **Subestimar a mudança cultural** — comprar tecnologia é fácil; mudar comportamento é difícil.

O roadmap certo combate cada um desses fatores.

### A estrutura de um roadmap realista

Um roadmap maduro de I4.0 tem **5 fases**:

#### Fase 1 — Diagnóstico (1 a 3 meses)

- Avaliar **maturidade digital** (visto na Aula 4).
- Mapear **processos críticos** (visto na Aula 13).
- Identificar **dores prioritárias** (qual problema custa mais à empresa hoje?).
- Levantar **dados existentes** (o que já se coleta? em que qualidade?).
- Mobilizar **patrocinador executivo**.

#### Fase 2 — Prova de Conceito / Piloto (3 a 6 meses)

- Escolher **um único problema** com retorno claro e mensurável.
- Definir **KPI de sucesso** antes de começar.
- Aplicar **uma tecnologia** (IIoT, IA, RA — não duas).
- Manter equipe **pequena e multidisciplinar** (TI + operação + finanças).
- **Comemorar** o resultado para gerar tração.

#### Fase 3 — Expansão para Linha-Piloto (6 a 12 meses)

- Replicar a solução em outras linhas, máquinas ou unidades.
- **Padronizar** processo, plataforma e dados.
- Treinar equipes locais — não pode depender só do time central.
- Criar **governança** mínima de dados e segurança.

#### Fase 4 — Escala (12 a 24 meses)

- Adotar **plataforma corporativa** (não solução por planta).
- Estruturar **time interno** (data engineer, data scientist, integrador IIoT).
- Criar **centro de excelência** que apoia outras áreas.
- Integrar com **ERP, MES e sistemas legados**.

#### Fase 5 — Inovação contínua (24+ meses)

- Adotar tecnologias emergentes (digital twin avançado, IA generativa, Indústria 5.0).
- Cultura de **experimentação** — pilotos pequenos contínuos.
- Métricas de **velocidade de inovação**, não só ROI direto.

### Quanto custa cada fase?

Como referência (fábrica de médio porte, 300–800 funcionários):

| Fase | Investimento típico | Prazo |
| --- | --- | --- |
| Diagnóstico | R\$ 50–150 mil | 1–3 meses |
| Piloto | R\$ 150–500 mil | 3–6 meses |
| Expansão | R\$ 500 mil–2 milhões | 6–12 meses |
| Escala | R\$ 2–10 milhões | 12–24 meses |
| Inovação contínua | R\$ 5–20 milhões/ano | Contínuo |

**Total de transformação séria nos primeiros 2 anos:** R\$ 3–15 milhões para uma fábrica média. Parece muito? Compare com o ROI esperado: **30–60% de redução em custo operacional** em alguns processos críticos.

### KPIs típicos de um roadmap 4.0

Não dá para gerenciar o que não se mede. KPIs comuns:

- **Disponibilidade de equipamento (OEE)** — alvo: subir de 70% para 85%+.
- **Tempo médio entre falhas (MTBF)** — alvo: dobrar.
- **Tempo de parada não programada** — alvo: -30%.
- **Defeitos por milhão (DPPM)** — alvo: redução de 50%+.
- **Lead time de produção** — alvo: -25%.
- **Custo por unidade produzida** — alvo: -10% a -20%.
- **Tempo de resposta a anomalia** — alvo: <1 minuto.
- **Maturidade digital (Acatech)** — alvo: subir 2 níveis em 24 meses.

Não escolha **todos**. Escolha **3 a 5** que sejam **medíveis hoje** e ataquem suas **dores prioritárias**.

### Caso brasileiro: roadmap da Embraer

A Embraer publicou seu roadmap 2017–2027 em relatório institucional. Os marcos:

- **2017–2019**: digitalização de processos administrativos, ERP unificado, primeiro piloto de digital twin.
- **2019–2022**: linha-piloto totalmente conectada (sensoriamento + analytics + dashboards).
- **2022–2025**: expansão para outras fábricas, IA preditiva em manutenção, RA na linha.
- **2025–2027**: digital twin de toda a operação, indústria 5.0 com colaboração humano-IA.

Investimento total estimado: **mais de R\$ 500 milhões** em 10 anos. Resultado já mensurado: produtividade +25%, defeitos -40%, lead time -35%.

### Atividade prática

Tomando como base a empresa que você analisou ao longo da disciplina:

1. Em **qual fase** do roadmap ela está hoje?
2. Que **2 ações** específicas faltam para passar de fase?
3. Que **investimento** seria realista para os próximos 12 meses?
4. Que **3 KPIs** você acompanharia para medir progresso?

### Pontos-chave

- **70% das iniciativas 4.0 falham** — quase sempre por **não começar pelo problema certo**.
- Um roadmap maduro tem **5 fases**: diagnóstico, piloto, expansão, escala, inovação contínua.
- Cada fase tem **investimento e prazo realistas** — não tente atalhos.
- **Patrocínio executivo + equipe multidisciplinar + KPIs claros** são pré-requisitos.
- Mensure com **3 a 5 KPIs específicos** ligados às dores prioritárias da empresa.

### Para saber mais

- **McKinsey — "Industry 4.0: Reimagining manufacturing operations after COVID-19":** https://www.mckinsey.com/
- **BCG — "Industry 4.0 Beyond the Hype":** https://www.bcg.com/
- **Embraer Sustainability Report:** https://ri.embraer.com.br/
- **Vídeo (Endeavor Brasil, YouTube):** "Como construir um roadmap digital"

---

## Aula 14 — Roteiro da Videoaula 14: "70% dos projetos 4.0 falham — como ser dos 30% que dão certo"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "A estatística é dura: 70% dos projetos de Indústria 4.0 falham em entregar o que prometem. Hoje a gente vai ver por que falham — e como construir um plano que dê certo."

### 2. Por que falham (0:40 – 3:00)

- Listar as 6 causas comuns.
- Reforçar: **começar pela tecnologia** é o erro mais frequente.

### 3. As 5 fases do roadmap (3:00 – 7:00)

- Diagnóstico → Piloto → Expansão → Escala → Inovação contínua.
- Investimento e prazo realistas por fase.

### 4. Caso Embraer + KPIs (7:00 – 9:30)

- Mostrar o roadmap 2017-2027 da Embraer.
- Listar os KPIs mais usados.

### 5. Encerramento (9:30 – 11:00)

> "Próxima aula: vou te mostrar **casos reais** — brasileiros e mundiais — para você ver o que está funcionando hoje, na prática. Te espero!"

---

## Aula 15 — Casos reais brasileiros e mundiais

A teoria sem caso é abstração. Esta aula é dedicada a **casos reais documentados** de aplicação da Indústria 4.0 — no Brasil e no mundo. O objetivo é dar a você **vocabulário concreto** para defender argumentos: "olha, a Klabin fez X e ganhou Y" é muito mais convincente que "tecnologia ABC pode trazer benefícios".


### Caso 1 — Siemens Amberg (Alemanha): a fábrica de referência

A planta da **Siemens em Amberg** é considerada uma das mais avançadas do mundo em I4.0. Produz CLPs e componentes de automação. Características:

- **75% das atividades** são automatizadas (robôs + cobots).
- **99,99885%** de taxa de qualidade (12 defeitos por milhão).
- **Capacidade dobrada** sem aumentar o tamanho da planta nos últimos 25 anos.
- **Digital twin** de toda a operação.
- **50 milhões de processos** rastreados por dia.

Lição: a transformação é **incremental e contínua**. Amberg não virou referência em 1 ano — foram 30 anos de evolução.

### Caso 2 — Klabin (Brasil): IIoT na celulose

A **Klabin**, em Telêmaco Borba (PR), implementou IIoT massivo em sua unidade de celulose. Mais de **1.500 sensores** alimentando um digital twin operacional. Resultados:

- **+8% de produtividade** em 24 meses.
- **-22% de paradas não programadas**.
- **-15% de consumo de químicos** (otimização por IA).
- ROI: **R\$ 80 milhões em ganhos anuais** vs R\$ 35 milhões investidos.

Lição: o setor de celulose, tradicionalmente conservador, é hoje líder em I4.0 no Brasil. **Setor antigo + tecnologia nova = ROI excelente**.

### Caso 3 — WEG (Brasil): motor como serviço

A **WEG**, de Jaraguá do Sul (SC), transformou motor elétrico em **produto + serviço**. Motores embarcam sensores que enviam dados de operação em tempo real para a nuvem da WEG. A empresa monitora performance, identifica padrões anormais e oferece manutenção preditiva ao cliente.

- Cliente paga **mensalidade** por monitoramento.
- WEG ganha **dados em escala global** para melhorar futuros produtos.
- Cliente ganha **previsibilidade** e **menos paradas**.

Lição: a I4.0 viabiliza **novos modelos de negócio** — não só eficiência interna. A WEG não vende mais "só motor"; vende **operação garantida**.

### Caso 4 — Embraco (Brasil): cobots em compressor

A **Embraco**, fabricante de compressores em Joinville-SC, instalou cobots da Universal Robots em linha de montagem.

- **+40% de produtividade** na estação onde foi instalado.
- **Zero acidentes** com o cobot em 4 anos.
- Tempo de **reprogramação** para novo produto: de 3 dias para 4 horas.

Lição: cobots ganham em **flexibilidade**, não só produtividade. Reprogramação rápida é o segredo para fábricas com **portfólio amplo**.

### Caso 5 — Tetra Pak (Suíça): digital twin de embalagem

A **Tetra Pak** usa digital twin para projetar embalagens. Antes, criar uma nova embalagem exigia 6–12 meses de prototipagem física. Com digital twin:

- **Time de prototipagem reduzido em 50%**.
- **Custo de protótipos reduzido em 70%**.
- **Mais variantes testadas** por projeto.

Lição: digital twin acelera **inovação de produto**, não só operação.

### Caso 6 — JBS (Brasil): o ataque que virou estudo

Em 2021, a JBS sofreu o ataque de ransomware mais conhecido do agronegócio brasileiro. A empresa parou plantas no Brasil, EUA e Austrália por dias.

- Pagou **U\$ 11 milhões** em resgate (decisão controversa).
- Reconstruiu sistemas em poucos dias graças a backups.
- Resultado: investimento maciço em cibersegurança industrial nos anos seguintes.

Lição: cibersegurança é **agora ou depois**. JBS está hoje muito mais protegida — porque sofreu. Não espere sofrer para investir.

### Caso 7 — Tesla (EUA): a fábrica que aprende

A **Tesla** opera fábricas que se aproximam do conceito de **adaptive manufacturing** — máquinas com IA que ajustam parâmetros sozinhas com base em dados de qualidade. Mais polêmico do que comprovado em alguns aspectos, mas o ponto inovador é claro: a Tesla **não vê a fábrica como projeto fixo**; vê como **organismo que aprende**.

Lição: olhe para a fronteira, mesmo que não vá implementar amanhã. Inspiração é parte da estratégia.

### Caso 8 — Vale (Brasil): operações autônomas em mineração

A **Vale**, no Pará, opera **caminhões autônomos** em sua mina de Carajás. Mais de 30 caminhões sem motorista, dirigindo 24 horas por dia, controlados por sistemas centrais e IA.

- **+15% de produtividade** vs operação manual.
- **-30% de combustível** (rotas otimizadas).
- **Redução drástica de acidentes** (zero acidente humano com os caminhões autônomos).

Lição: ambientes **extremos** (calor, poeira, distância) são candidatos naturais a automação 4.0.

### Síntese: padrões que aparecem em todos os casos

Olhando os 8 casos juntos, surgem **5 padrões**:

1. **Começam por uma dor real** — não por tecnologia.
2. **Crescem por iteração** — pilotos pequenos viram grandes.
3. **Combinam tecnologias** — IIoT + IA + Cloud, raramente uma só.
4. **Mudam o modelo de negócio**, não só a operação (WEG).
5. **Investem em pessoas** — automação não substitui requalificação.

### Atividade prática

Escolha **um dos 8 casos** que mais te impactou. Reflita:

1. Por que **esse caso** ressoou em você?
2. Qual elemento dele você poderia **trazer** para uma empresa que conhece?
3. Que tecnologias **da Unidade 2** estão presentes nesse caso?
4. Que riscos você antecipa em uma replicação?

### Pontos-chave

- Casos reais dão **vocabulário concreto** — fortalecem argumentos.
- A Siemens Amberg ilustra **evolução incremental de longo prazo**.
- Klabin, WEG, Embraco, Vale mostram que **Brasil está no jogo**.
- Casos como JBS são lembrete de que **cibersegurança é pré-requisito**.
- Cinco padrões comuns: **dor real, iteração, combinação de tecnologias, novo modelo de negócio, investimento em pessoas**.

### Para saber mais

- **World Economic Forum — Lighthouse Network:** https://www.weforum.org/projects/global-lighthouse-network
- **Portal CNI Indústria 4.0:** https://www.portaldaindustria.com.br/industria-4-0/
- **Vídeo (DW Brasil, YouTube):** "A fábrica do futuro" (sobre Siemens Amberg)
- **Caso JBS — análise (G1, ABRAS):** https://g1.globo.com/economia/

---

## Aula 15 — Roteiro da Videoaula 15: "Casos que provam — Brasil e mundo em I4.0"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "Teoria é teoria. Caso real é argumento. Hoje você vai sair com **8 casos concretos** — quem fez, como fez, quanto ganhou — para defender qualquer ideia de I4.0 com base sólida."

### 2. Casos internacionais (0:30 – 4:00)

- Siemens Amberg: referência mundial, evolução de 30 anos.
- Tetra Pak: digital twin em produto.
- Tesla: fábrica que aprende.

### 3. Casos brasileiros (4:00 – 8:00)

- Klabin: R\$ 80 milhões em ganhos.
- WEG: motor como serviço.
- Embraco: cobot +40% produtividade.
- Vale: caminhões autônomos.
- JBS: ataque que virou estudo.

### 4. Os 5 padrões comuns (8:00 – 9:30)

- Dor real, iteração, combinação, novo modelo de negócio, pessoas.

### 5. Encerramento (9:30 – 11:00)

> "Última aula da disciplina: o que vem **depois** da 4.0? Vamos falar da **Indústria 5.0** — humano + máquina, sustentabilidade — e fechar o ciclo. Te espero!"

---

## Aula 16 — Indústria 5.0: humano + máquina, sustentabilidade e o futuro próximo

Chegamos à última aula. Você já entendeu a 4.0 — agora vamos olhar para o que vem a seguir. A **Indústria 5.0** não é uma ruptura como a 4.0 foi; é uma **correção de rota**, uma maturação. Esta aula fecha a disciplina e abre o horizonte da sua carreira.

![Operador humano colaborando com um cobot em estação de montagem — síntese visual da Indústria 5.0 com centralidade humana](https://commons.wikimedia.org/wiki/Special:FilePath/Cobot.jpg?width=800)

### O que é a Indústria 5.0

> **Indústria 5.0** é um conceito emergente que reposiciona a transformação digital industrial em torno de **três valores** centrais: **centralidade humana**, **sustentabilidade** e **resiliência**.

O termo foi proposto pela **Comissão Europeia em 2021** como evolução do conceito de I4.0. A motivação: a 4.0, em alguns lugares, virou sinônimo de "automatizar tudo e reduzir gente". A 5.0 reabilita o humano e adiciona dimensões éticas e ambientais.

### Os três pilares da Indústria 5.0

#### 1. Centralidade humana (human-centric)

- **Cobots e automação adaptativa** que apoiam o trabalhador, não o substituem.
- **Personalização em massa** — produtos sob medida em escala.
- **Treinamento e requalificação** contínuos.
- **Bem-estar do trabalhador** como KPI (não só produtividade).
- **Inclusão** — adaptar postos para pessoas com deficiência, idosos, etc.

#### 2. Sustentabilidade

- **Economia circular** — produzir, usar, recuperar, reusar.
- **Eficiência energética** — IA otimizando consumo.
- **Materiais reciclados e biodegradáveis**.
- **Pegada de carbono mensurada por unidade produzida**.
- **Manufatura local** (em vez de globalização extrema).

#### 3. Resiliência

- **Cadeia de suprimentos diversificada** — não depender de um único fornecedor ou país.
- **Capacidade de reconfiguração rápida** (visto na pandemia COVID-19).
- **Cibersegurança industrial** robusta.
- **Estoque inteligente** — equilíbrio entre lean e segurança.

### Como I5.0 difere da I4.0

| Aspecto | I4.0 | I5.0 |
| --- | --- | --- |
| **Foco** | Eficiência, automação | Centralidade humana, sustentabilidade, resiliência |
| **Tecnologia** | Habilita transformação | É **meio**, não fim |
| **Trabalhador** | Pode ser substituído | É **central**; potencializado por tecnologia |
| **Meio ambiente** | Mencionado, não central | **Central** |
| **Modelo econômico** | Crescimento, eficiência | **Equilíbrio** entre lucro, planeta e pessoas |

A I5.0 **não substitui** a 4.0. Você **precisa** da 4.0 para fazer a 5.0. A 5.0 é a 4.0 **com propósito**.

### Tendências tecnológicas dos próximos 5–10 anos

Tecnologias que serão cada vez mais relevantes:

1. **IA generativa industrial** — modelos como ChatGPT especializados em manuais técnicos, suporte a operador, design de processo.
2. **Computação quântica** — otimização de problemas combinatórios complexos (roteirização, escalonamento).
3. **5G e 6G privados** — latência ultra-baixa para automação crítica.
4. **Robótica avançada** — robôs humanoides para tarefas variadas (Tesla Optimus, Figure 01).
5. **Materiais inteligentes** — capazes de mudar propriedade conforme estímulo.
6. **Bioprodução** — bactérias e fungos produzindo materiais industriais.
7. **Hidrogênio verde** como combustível e matéria-prima.
8. **Captura de carbono industrial** — IA otimizando processos de captura de CO₂.

Você não precisa dominar todas. Mas precisa saber que **existem** e ter capacidade de **aprender rapidamente** quando uma delas se tornar relevante para sua empresa.

### O papel do(a) engenheiro(a) de produção na I5.0

A função clássica do engenheiro de produção — **gerenciar fluxos** — ganha novas dimensões na 5.0:

- **Fluxo de materiais** continua sendo central, mas agora com critérios de circularidade.
- **Fluxo de informação** passa a depender de cibersegurança e governança de dados.
- **Fluxo de pessoas** ganha foco em qualidade de vida, requalificação e diversidade.
- **Fluxo de carbono** entra como nova dimensão a gerenciar.

O profissional formado para a 5.0 é **híbrido**: domina técnicas tradicionais de engenharia + competências de gestão de dados + visão estratégica de sustentabilidade.

### Caso emergente: a fábrica da BMW iFactory

A **BMW** em sua iFactory (Hungria, 2025) propõe a primeira fábrica I5.0 em escala. Características:

- **100% energia renovável**.
- **Carbono neutro** em toda a operação.
- **Cobots e robôs humanoides** trabalhando lado a lado com 1.500 funcionários.
- **Digital twin completo** com gêmeo da cadeia de fornecedores.
- **Hidrogênio verde** como vetor energético.
- **Capacidade de reconfiguração** em horas (não semanas).

É **modelo aspiracional**, não realidade massiva. Mas indica direção.

### Você vai sair daqui sabendo:

Recapitulando a disciplina inteira em uma frase:

> Você sabe **o que é** Indústria 4.0 (U1), **como funciona** por dentro (U2), **onde é aplicada** (U3) e **como implementar** com método (U4) — em uma empresa real, com investimentos realistas, KPIs claros e visão de futuro.

Isso é **conteúdo de gerente de manufatura digital**. Você sai dessa disciplina **acima do nível de muitos profissionais com 5+ anos de experiência industrial**, simplesmente porque a I4.0 está mudando rápido demais para a maioria acompanhar.

### Atividade prática (encerramento da disciplina)

Reflita por escrito (será o ponto de partida do seu projeto integrador):

1. **O que você sabia sobre I4.0 quando começou a disciplina?**
2. **O que você sabe agora?**
3. **Qual aula te impactou mais? Por quê?**
4. **Que tecnologia você quer aprofundar mais?**
5. **Como você imagina aplicar isso na sua carreira nos próximos 3 anos?**

Esse texto é só para você — mas guarde. Daqui a 1 ano, leia de novo. Você vai se surpreender com o quanto evoluiu.

### Pontos-chave

- **Indústria 5.0** não substitui a 4.0 — é a 4.0 **com propósito** humano e ambiental.
- Três pilares: **centralidade humana, sustentabilidade, resiliência**.
- Tendências dos próximos 10 anos: **IA generativa industrial, 5G/6G privado, robótica avançada, materiais inteligentes, bioprodução, hidrogênio verde**.
- O(a) engenheiro(a) de produção da 5.0 gerencia também **fluxo de carbono** e **fluxo de pessoas** com novos critérios.
- Você sai desta disciplina com conteúdo de **gerente de manufatura digital** — use isso na sua carreira.

### Para saber mais (encerramento da disciplina)

- **Comissão Europeia — Indústria 5.0:** https://research-and-innovation.ec.europa.eu/research-area/industrial-research-and-innovation/industry-50_en
- **BMW iFactory:** https://www.bmwgroup.com/
- **Tesla Optimus:** https://www.tesla.com/AI
- **Vídeo (Veritasium, YouTube):** "The Future of Industry"
- **Livro recomendado:** SCHWAB, K. *Moldando a Quarta Revolução Industrial*. Edipro, 2018.

### Encerramento

Parabéns por chegar até aqui. Você terminou uma disciplina densa, prática e atualizada — em um campo que muda mais rápido que qualquer livro consegue acompanhar. Você sai com **vocabulário**, **ferramentas mentais** e **casos reais** para liderar transformação onde for trabalhar. Aproveite cada oportunidade de aplicar — porque a indústria precisa de engenheiros que saibam o **como**, não só o **o quê**.

Boa carreira. E que você seja um(a) dos profissionais que **fazem a 4.0 (e a 5.0) acontecer no Brasil**.

---

## Aula 16 — Roteiro da Videoaula 16: "Indústria 5.0 e o seu papel no futuro"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:30)

> "Última aula da disciplina. Hoje a gente olha para o futuro: o que vem **depois** da Indústria 4.0? E como você se prepara para ele?"

### 2. O que é Indústria 5.0 (0:30 – 3:00)

- Definição (Comissão Europeia, 2021).
- 3 pilares: humano, sustentável, resiliente.
- Tabela I4.0 vs I5.0.

### 3. Tendências dos próximos 10 anos (3:00 – 6:00)

- IA generativa industrial, 5G/6G, robôs humanoides, materiais inteligentes, hidrogênio verde.
- Citar BMW iFactory como caso aspiracional.

### 4. O papel do engenheiro de produção (6:00 – 8:30)

- Gerenciar fluxos clássicos + carbono + pessoas.
- Profissional híbrido.

### 5. Encerramento da disciplina (8:30 – 11:00)

> "Você sai daqui sabendo do que muitos profissionais com 5+ anos de experiência ainda nem ouviram falar. Use isso. A indústria brasileira precisa de gente como você. Obrigado, e boa carreira!"

---

## Quiz não avaliativo

### Questão 1

Sobre o ciclo BPM (Business Process Management), assinale a alternativa **correta**:

- [ ] a. O ciclo BPM começa pela definição do TO-BE (processo ideal); o AS-IS é tratado apenas como referência histórica.
- [x] b. O ciclo BPM tem 6 etapas (planejar → modelar AS-IS → analisar → redesenhar TO-BE → implementar → monitorar), formando um ciclo contínuo de melhoria.
- [ ] c. O ciclo BPM se limita à automação por RPA, sem necessidade de mapear processos antes.
- [ ] d. O ciclo BPM tem apenas 2 fases: tecnologia e treinamento.

**Resposta correta:** `b`

**Feedback:** A (b) descreve corretamente o ciclo BPM clássico — sempre iniciado pelo planejamento e mapeamento da realidade (AS-IS), antes de propor o ideal (TO-BE). A (a) inverte o que é universalmente recomendado: mapear o real **antes** de projetar o ideal evita melhorias que miram em processos que não existem. A (c) confunde BPM com RPA — RPA é uma técnica de automação que pode (ou não) ser usada na etapa de implementação do BPM. A (d) é simplista demais.

### Questão 2

Sobre os pilares da **Indústria 5.0**, assinale a alternativa **correta**:

- [ ] a. A I5.0 elimina completamente a Indústria 4.0, substituindo todas as suas tecnologias.
- [ ] b. A I5.0 prioriza apenas a sustentabilidade, ignorando os demais aspectos.
- [ ] c. A I5.0 retorna ao modelo industrial anterior à 4.0, sem uso de IA, IoT ou digital twin.
- [x] d. A I5.0 mantém as tecnologias da I4.0 mas as orienta para **três pilares**: centralidade humana, sustentabilidade e resiliência — sendo uma evolução, não substituição.

**Resposta correta:** `d`

**Feedback:** A (d) descreve corretamente a Indústria 5.0 — proposta pela Comissão Europeia em 2021 como **maturação** da 4.0, mantendo suas tecnologias mas reorientando-as para propósitos humanos, ambientais e de resiliência. A (a) é falsa: 5.0 **depende** da 4.0. A (b) é incompleta: sustentabilidade é apenas um dos três pilares. A (c) é o oposto: 5.0 **avança** sobre 4.0, não retrocede.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Encerramento da disciplina — esta AAI integra tudo o que você aprendeu. Elabore um **roadmap completo** de transformação digital para uma empresa real (a mesma que você analisou ao longo da disciplina), seguindo a estrutura aprendida.
>
> Estruture sua resposta em **6 seções**:
>
> 1. **Diagnóstico** — em que nível de maturidade (Acatech) a empresa está hoje? Justifique com fatos.
> 2. **Dor prioritária** — qual é o problema #1 que vale a pena atacar primeiro? Por que esse?
> 3. **Solução proposta** — qual(is) tecnologia(s) das Unidades 2 e 3 aplicar? Justifique.
> 4. **Plano em 18 meses** — 5 fases com prazos, investimento estimado e KPIs.
> 5. **Riscos e mitigações** — 3 principais riscos e como mitigá-los.
> 6. **Visão de longo prazo (I5.0)** — em 5 anos, onde essa empresa deveria estar do ponto de vista da I5.0?
>
> **Importante:** este é seu **projeto final**. Capricha. Demonstre tudo o que aprendeu nas 16 aulas. Resposta esperada: **3 a 6 páginas** de texto técnico, com **números e fontes** quando possível.

**Resposta esperada:**

> Resposta exemplar é um **roadmap defensável**, não um wishlist. O diagnóstico precisa apontar **3 a 5 fatos verificáveis** sobre a empresa (ex.: "não há sensor em motor crítico", "decisão de manutenção é por intuição do supervisor"). A dor prioritária deve ter **número de impacto** (R\$, horas, %). A solução combina, idealmente, **uma tecnologia habilitadora (U2) + uma aplicação (U3)** — não tenta tudo. O plano de 18 meses respeita as **5 fases** (diagnóstico → piloto → expansão → escala → ...) sem pular etapas. KPIs precisam ser **medíveis hoje** (3 a 5 deles). Riscos incluem cultura, fornecedor único, sub-orçamento — não só "falta de dinheiro". A visão I5.0 fecha com **humano-tecnologia-sustentabilidade**, conectando os 16 aulas em uma narrativa coerente. Textos genéricos perdem nota; textos com fatos da empresa real ganham. Avaliação dos professores avalia: clareza, profundidade técnica, realismo, integração de conceitos de toda a disciplina.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> O livro consolida tudo o que vimos na disciplina — com foco em **como implementar**, não só em teoria. É a referência ideal para revisar antes da avaliação final e para guardar como manual de cabeceira na carreira.

- **Nome do livro:** *Indústria 4.0: Implementação Estratégica*
- **Capítulo:** Capítulos 7 (roadmap), 8 (casos brasileiros), 10 (futuro)
- **Editora:** Atlas / FGV
- **Link de acesso:** BV UniFECAF — https://fecaf.brightspace.com/d2l/home (BV Professor)
- **Aula em que entra:** Aulas 14 e 16

### Para mergulhar no assunto

> Recomendo o documentário **"The Smart Factory" (DW Documentary)**, disponível gratuitamente no YouTube. Visita Siemens Amberg, BMW, e outras referências da Indústria 4.0 e 5.0 no mundo. Imagens fortes — você vai ver com seus próprios olhos o que estudou nas 16 aulas.

- **Link(s):** https://www.youtube.com/@DWDocumentary
- **Aula em que entra:** Aula 15 ou Aula 16

### Podcast (curadoria, até 45 min)

> O podcast **"Visão Indústria 4.0"** entrevista executivos e engenheiros que estão liderando a transformação digital industrial no Brasil. O episódio recomendado discute roadmap real de implementação, com dores reais e ganhos mensurados.

- **Nome do podcast:** Visão Indústria 4.0
- **Nome do episódio:** "Roadmap de transformação digital — sem mitos"
- **Link:** https://www.youtube.com/@visaoindustria40
- **Aula em que entra:** Aula 14

### Artigo científico

> Este artigo discute a transição da Indústria 4.0 para a 5.0 e o que **precisa** mudar — não apenas tecnologicamente, mas em modelos organizacionais, formação e regulação. É leitura essencial para quem quer estar à frente.

- **Link:** https://doi.org/10.1016/j.jmsy.2022.07.010
- **Aula em que entra:** Aula 16
- **Referência bibliográfica do artigo no formato ABNT:**
  > XU, Xun *et al*. **Industry 4.0 and Industry 5.0 — Inception, conception and perception**. *Journal of Manufacturing Systems*, v. 61, p. 530-535, out. 2021.
