# Unidade 1 — Fundamentos da Infraestrutura de Transportes

- **Disciplina:** Portos, Aeroportos e Ferrovias
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 1 a 4

## Vídeo introdutório + Relação da disciplina com a atuação profissional

Você já reparou que **tudo o que existe na sua casa um dia foi transportado**? O celular que você está usando provavelmente desembarcou em um porto, foi distribuído por ferrovia ou rodovia e talvez tenha cruzado o país em um avião de carga. A soja que move a balança comercial brasileira sai de Mato Grosso e percorre milhares de quilômetros até um terminal portuário. **Nada na economia moderna acontece sem infraestrutura de transportes** — e construir essa infraestrutura é, em essência, trabalho de engenharia civil.

Esta disciplina existe para te transformar em um(a) profissional capaz de entender, projetar e dialogar sobre as três grandes infraestruturas que movem o país: **portos, aeroportos e ferrovias**. E o melhor: vamos partir do zero. Você não precisa saber nada de transportes para começar. Vamos construir juntos, desde os conceitos de matriz de transportes e modal, passando por planejamento, geometria, terraplenagem e pavimentos, até chegar ao projeto de cais, pistas de pouso e linhas férreas.

O diferencial de mercado é enorme. O Brasil tem uma das matrizes de transporte mais desbalanceadas do mundo — dependemos excessivamente do caminhão — e o país precisa investir centenas de bilhões de reais em ferrovias, portos e aeroportos nas próximas décadas. Quem domina esse tema participa das grandes obras: concessões rodoviárias, arrendamentos portuários, novas ferrovias como a Fiol e a Ferrogrão, ampliação de aeroportos. Órgãos como **DNIT, ANTT, ANTAQ e ANAC**, além de grandes empreiteiras e concessionárias, buscam engenheiros que entendam infraestrutura de transportes.

Ao final desta disciplina, você saberá diagnosticar gargalos logísticos, ler e interpretar projetos de infraestrutura, dimensionar estruturas básicas e defender tecnicamente suas decisões. É um conhecimento que poucos colegas de graduação têm — e que vai te diferenciar logo na entrada do mercado.

### Roteiro do vídeo introdutório (até 2 min)

**Abertura (0:00 – 0:20):**
> "Olá! Eu sou o professor Afonso Brandão. Seja muito bem-vindo(a) à disciplina de Portos, Aeroportos e Ferrovias. Se você quer entender como pessoas e mercadorias se movem pelo Brasil — e como o engenheiro civil constrói as estruturas que tornam isso possível —, está no lugar certo."

**Conexão com o mercado (0:20 – 0:55):**
> "O Brasil é refém do caminhão: mais de 60% de tudo que produzimos roda sobre rodovias, quando deveria ir por trilho ou navio. Corrigir isso exige bilhões em obras de ferrovia, porto e aeroporto. O engenheiro que entende essas três infraestruturas participa das maiores obras do país."

**Conteúdo e diferencial (0:55 – 1:25):**
> "Vamos do zero. Primeiro os fundamentos comuns: matriz de transportes, planejamento, terraplenagem, pavimentos. Depois mergulhamos em portos e hidrovias, em ferrovias e, por fim, em aeroportos. Você vai sair sabendo conversar com DNIT, ANTT, ANTAQ e ANAC de igual para igual."

**Benefício para o aluno (1:25 – 1:45):**
> "Ao final, você consegue **diagnosticar** um gargalo logístico, **ler** um projeto de infraestrutura e **defender** tecnicamente cada solução. É diferencial real para quem está saindo da graduação em Engenharia Civil."

**Encerramento (1:45 – 2:00):**
> "Bora começar! Portos, aeroportos e ferrovias são as artérias da economia. Vem comigo entender como elas são construídas. Te espero na Aula 1!"

---

## Aula 1 — Sistemas de transporte e a matriz de transportes brasileira

> Imagine que você precisa enviar 50 mil toneladas de soja de Sorriso (MT) até o Porto de Santos. Vai de caminhão? De trem? Quanto custa cada opção? Essa pergunta aparentemente simples revela tudo o que está por trás de um **sistema de transporte** — e por que a forma como o Brasil escolheu transportar suas mercadorias custa caro à economia. Nesta aula, você vai entender o que é a matriz de transportes, conhecer os modais e descobrir por que custo logístico é assunto de engenheiro.

### O papel da infraestrutura de transportes

A infraestrutura de transportes é o conjunto de obras físicas — rodovias, ferrovias, portos, aeroportos, hidrovias e dutos — que permite o deslocamento de **pessoas** e **cargas** no território. Ela é a base sobre a qual a economia funciona: sem estradas e portos, não há comércio; sem aeroportos, não há integração de longas distâncias; sem ferrovias, não há transporte eficiente de grandes volumes.

Para o engenheiro civil, essa infraestrutura representa algumas das maiores e mais desafiadoras obras da profissão — cais que avançam mar adentro, pistas que precisam suportar aeronaves de 400 toneladas, ferrovias que cortam serras com túneis e viadutos. Entender o **sistema** como um todo é o primeiro passo antes de projetar qualquer peça.

![Rodovia Anhanguera, uma das principais vias do sistema rodoviário de São Paulo, ilustrando o modal predominante na matriz brasileira](https://commons.wikimedia.org/wiki/Special:FilePath/Rodovia%20Anhanguera.jpg)

### A matriz de transportes brasileira

**Matriz de transportes** é a distribuição percentual de cargas (ou passageiros) entre os diferentes modais. No Brasil, essa distribuição é fortemente desequilibrada:

| Modal | Participação aproximada (carga) |
| --- | --- |
| Rodoviário | ~61% |
| Ferroviário | ~21% |
| Aquaviário (cabotagem + hidrovias) | ~14% |
| Dutoviário | ~4% |
| Aéreo | <1% |

![Gráfico de barras da matriz de transporte de cargas do Brasil: rodoviário ~61%, ferroviário ~21%, aquaviário ~14%, dutoviário ~4% e aéreo <1%](assets/matriz_modal.svg)

Compare com os Estados Unidos, onde ferrovias respondem por cerca de 43% das cargas, ou a Rússia, onde o trilho domina. O Brasil, um país de dimensões continentais, deveria privilegiar modais de **alta capacidade** (ferrovia e hidrovia) para longas distâncias. A herança rodoviarista — construída a partir dos anos 1950 com o programa JK e a instalação das montadoras — deixou o país dependente do caminhão, encarecendo a logística e reduzindo a competitividade dos nossos produtos no exterior.

O **Plano Nacional de Logística (PNL)**, coordenado pela EPL (Empresa de Planejamento e Logística), é o documento estratégico do governo federal que orienta investimentos para reequilibrar essa matriz. O PNL 2035 prevê aumento da participação ferroviária para 30% e da aquaviária para 29% — metas que dependem de dezenas de projetos de infraestrutura, todos carentes de engenheiros qualificados.

### Os modais e suas características

Cada modal tem vocação para um tipo de transporte:

- **Rodoviário** — flexível, porta a porta, ideal para curtas distâncias e cargas fracionadas. Alto custo por tonelada-quilômetro. No Brasil, a malha pavimentada federal tem cerca de 76 mil km, gerida pelo DNIT e por concessionárias privadas.
- **Ferroviário** — alta capacidade, baixo custo por tonelada-quilômetro, ideal para grandes volumes e longas distâncias (granéis: soja, minério, açúcar). A malha brasileira tem cerca de 30 mil km em operação, regulada pela ANTT.
- **Aquaviário** — o mais barato por unidade transportada, ideal para grandes massas e longas distâncias (comércio exterior, cabotagem). O Brasil tem 16 portos públicos de grande porte e mais de 130 terminais de uso privado, fiscalizados pela ANTAQ.
- **Aéreo** — o mais rápido e o mais caro; usado para cargas de alto valor agregado e baixo peso. A ANAC regula os aeroportos brasileiros, que somam mais de 2.400 unidades (públicos e privados).
- **Dutoviário** — contínuo e seguro, restrito a líquidos e gases (petróleo, combustíveis, gás natural). A Petrobras opera a maior parte da malha dutoviária nacional.

A regra de ouro: **quanto maior o volume e a distância, mais barato deveria ser o modal escolhido** — e é aí que ferrovia e hidrovia ganham do caminhão.

### Custos logísticos e competitividade

O **custo logístico** brasileiro representa cerca de 12% a 13% do PIB, contra 8% nos países desenvolvidos. Essa diferença, chamada de "Custo Brasil", corrói a competitividade. O excesso de transporte rodoviário é o principal vilão: caminhão consome mais combustível, emite mais CO₂ e movimenta menos carga por viagem do que um trem ou navio.

Para o engenheiro, isso significa oportunidade: cada nova ferrovia ou terminal portuário que tira carga da estrada gera economia mensurável para o país. Planejar e construir essa transição é trabalho de Engenharia de Transportes. A **Ferrogrão** (ligando Sinop-MT a Miritituba-PA) e a **FIOL** (Ferrovia de Integração Oeste-Leste, conectando Figueirópolis-TO a Ilhéus-BA) são exemplos de projetos em fase de implementação que ilustram essa transformação.

### Intermodalidade e multimodalidade

Raramente uma carga viaja em um único modal. Os conceitos-chave são:

- **Intermodalidade** — uso de mais de um modal na mesma viagem, com **documentos de transporte separados** para cada trecho (caminhão até o terminal, ferrovia até o porto, navio até o destino).
- **Multimodalidade** — a mesma viagem com **um único documento** e um único responsável (o Operador de Transporte Multimodal — OTM), que coordena toda a cadeia.

O ponto onde os modais se conectam é o **terminal intermodal** (ou pátio de transbordo). Projetar terminais eficientes — reduzindo o tempo e o custo da transferência de carga — é um dos grandes desafios da infraestrutura moderna.

### A moldura da engenharia digital: a nova fronteira dos transportes

Construir o cais, a pista e o trilho é a metade clássica da engenharia de transportes. A outra metade, cada vez mais decisiva, é **digital** — e ela vai reaparecer em cada modal ao longo desta disciplina. Quatro tecnologias formam essa moldura:

- **Gêmeos digitais (Digital Twins)** — uma réplica virtual e dinâmica de um ativo físico (um terminal, um cais, um aeroporto), atualizada em **tempo real** a partir de sensores. O engenheiro simula no gêmeo o que aconteceria na realidade — fluxo de guindastes, posicionamento de navios, ocupação de pista — **antes** de gastar dinheiro ou interromper a operação.
- **IoT (Internet das Coisas)** — sensores embarcados em estruturas, equipamentos e veículos que enviam dados continuamente (temperatura, vibração, posição, carga). É a "fonte de verdade" que alimenta o gêmeo digital e os modelos de IA.
- **Smart Ports / infraestrutura inteligente** — terminais e aeroportos que integram automação, redes 5G, IoT e IA para otimizar operações. O **Porto de Santos**, por exemplo, vem implantando redes 5G e gêmeo digital com a meta de se tornar referência como *smart port* no hemisfério sul.
- **Inteligência Artificial (IA)** — algoritmos que aprendem com os dados para **prever** (demanda, falhas, congestionamentos) e **otimizar** (rotas, escalas, manutenção).

Guarde estes quatro nomes: eles são as **novas fronteiras** do setor. Em Portos veremos o gêmeo digital e o AGV; em Aeroportos, o A-CDM e a previsão de fluxo; em Ferrovias, a defectoscopia automatizada e o ETCS/ERTMS. A infraestrutura física continua sendo a base — mas quem domina a camada digital projeta sistemas mais baratos, seguros e resilientes.

### Sistemas inteligentes de monitoramento climático e resiliência

Eventos climáticos extremos — chuvas intensas, ondas de calor, ventos fortes — são hoje a principal causa de **interrupções operacionais** e danos a portos, aeroportos e ferrovias. A resposta da engenharia moderna é a **gestão de resiliência** apoiada em dados.

A combinação de **sensores IoT** (umidade do solo em taludes, nível de rios, vibração em trilhos, vento em pistas) com **modelos de IA** permite o **monitoramento contínuo** da infraestrutura e a emissão de **alertas precoces**. Em vez de descobrir o problema depois do acidente, o sistema prevê a tempestade, identifica a encosta que está saturando ou o trecho de via sob risco e dispara a ação preventiva — reduzir velocidade, desviar a operação, mobilizar equipes — **em tempo real**, mitigando danos e tempo de parada.

É a engenharia mudando de uma postura **reativa** (consertar depois) para uma postura **preditiva** (antecipar e prevenir). Essa capacidade de manter a operação de pé diante de eventos climáticos é o que se chama de **resiliência** — e ela atravessa todos os modais que estudaremos.

### Exemplo numérico: custo por tonelada-quilômetro

Vamos comparar o custo de transportar a soja de Sorriso (MT) a Santos (SP), distância de aproximadamente $2.000\,\mathrm{km}$, para um volume de $1.000\,\mathrm{t}$.

Considere os custos médios por tonelada-quilômetro (R\$/t·km):

- Rodoviário: $0{,}18\,\mathrm{R\$/t \cdot km}$
- Ferroviário: $0{,}06\,\mathrm{R\$/t \cdot km}$

O custo total é dado por:

$$
C = c \times d \times m
$$

onde $c$ é o custo unitário, $d$ a distância e $m$ a massa transportada.

Para o rodoviário:

$$
C_{\text{rod}} = 0{,}18 \times 2.000 \times 1.000 = 360.000\,\mathrm{R\$}
$$

Para o ferroviário:

$$
C_{\text{fer}} = 0{,}06 \times 2.000 \times 1.000 = 120.000\,\mathrm{R\$}
$$

A economia ao usar ferrovia é de $360.000 - 120.000 = 240.000\,\mathrm{R\$}$, ou **66,7% menos** que o caminhão. Multiplique isso pelos milhões de toneladas de grãos exportados por ano e você entende por que o Brasil precisa de mais ferrovias.

### Atividade prática

Escolha um produto que você consome no dia a dia (café, eletrônico, combustível, etc.) e pesquise sua **origem provável** e o **destino até você**. Em seguida:

1. Identifique quais **modais** essa carga provavelmente percorreu.
2. Aponte onde houve **transbordo** (intermodalidade).
3. Estime, com os custos médios da aula, qual seria a economia se um trecho rodoviário longo fosse substituído por ferrovia.

Anote suas conclusões — vamos retomar esse raciocínio na Aula 2, quando falarmos de planejamento.

### Pontos-chave

- A **matriz de transportes** brasileira é desbalanceada: ~61% rodoviário, contra ~21% ferroviário e ~14% aquaviário.
- Cada **modal** tem vocação: rodovia para curtas distâncias, ferrovia e hidrovia para grandes volumes e longas distâncias.
- O **custo logístico** brasileiro (~12-13% do PIB) é alto justamente pelo excesso de transporte rodoviário.
- **Intermodalidade** usa vários modais com documentos separados; **multimodalidade** usa um único documento e operador.
- Substituir rodovia por ferrovia em longas distâncias pode reduzir o custo de transporte em mais de 60%.
- A **engenharia digital** — gêmeos digitais, IoT, *smart ports* e IA — é a nova fronteira que perpassa todos os modais da disciplina.
- Sistemas de **monitoramento climático com IoT + IA** dão **alertas precoces** e levam a infraestrutura de uma postura reativa a uma postura **preditiva** (resiliência).

### Para saber mais

- **DNIT — Departamento Nacional de Infraestrutura de Transportes:** https://www.gov.br/dnit/
- **EPL/Ministério dos Transportes — Plano Nacional de Logística (PNL):** https://www.gov.br/transportes/pt-br
- **Wikipedia — Transporte no Brasil:** https://pt.wikipedia.org/wiki/Transporte_no_Brasil
- **CNT — Confederação Nacional do Transporte (boletins e pesquisas):** https://www.cnt.org.br/
- **Porto de Santos rumo a *smart port* — redes 5G e Gêmeo Digital (Ministério de Portos e Aeroportos):** https://www.gov.br/portos-e-aeroportos/pt-br/assuntos/noticias/2026/01/porto-de-santos-avanca-para-se-tornar-referencia-global-em-logistica-verde-e-conectada
- **IA em monitoramento ambiental e prevenção de desastres (Jornal da USP):** https://jornal.usp.br/radio-usp/o-uso-da-ia-em-sistemas-de-monitoramento-ambiental-pode-auxiliar-na-prevencao-de-desastres-ambientais/

## Aula 1 — Roteiro da Videoaula 1: "Sistemas de transporte e a matriz de transportes brasileira"

**Duração: 7 a 10 minutos**

### 1. Abertura (0:00 – 0:35)

> "Tudo o que existe na sua casa um dia foi transportado. Mas você já parou pra pensar como? E quanto custa isso? Hoje a gente vai entender o que é um sistema de transporte, conhecer a matriz brasileira e descobrir por que o Brasil paga caro por transportar tudo de caminhão."

### 2. Desenvolvimento — parte 1 (0:35 – 3:30)

> "Vamos começar pela matriz de transportes — a divisão da carga entre os modais. No Brasil, mais de 60% vai por rodovia. Compare com os Estados Unidos, onde a ferrovia leva quase metade. Para um país continental como o nosso, isso é um erro histórico que vem dos anos 50, do rodoviarismo do JK. O Plano Nacional de Logística quer mudar isso. Vou mostrar a tabela completa e por que cada modal tem sua vocação: caminhão para curtas distâncias, trem e navio para grandes volumes. DNIT cuida de rodovias, ANTT regula ferrovias, ANTAQ os portos e ANAC os aeroportos."

### 3. Desenvolvimento — parte 2 (3:30 – 6:30)

> "Agora os custos. O custo logístico brasileiro é de 12 a 13% do PIB — quatro pontos acima dos países desenvolvidos. O culpado? O excesso de caminhão. Projetos como a Ferrogrão e a FIOL mostram que o Brasil está tentando mudar isso. E falo de intermodalidade e multimodalidade: carga quase nunca viaja num modal só. O terminal de transbordo é onde a engenharia faz a diferença."

### 4. Desenvolvimento — parte 3 (6:30 – 8:30)

> "Vamos fazer a conta. Soja de Mato Grosso até Santos, 2.000 km, mil toneladas. De caminhão: 360 mil reais. De trem: 120 mil reais. Economia de 66%! Multiplique pelos milhões de toneladas exportadas por ano — o impacto é bilionário. É por isso que cada nova ferrovia muda a competitividade do agronegócio brasileiro."

### 4b. A nova fronteira digital (8:30 – 9:15)

> "Mas tem uma camada nova que vai aparecer em toda a disciplina: a engenharia digital. Guardem quatro nomes. Gêmeo digital: uma cópia virtual do porto ou do aeroporto, atualizada por sensores em tempo real, onde a gente simula antes de mexer no real. IoT: os sensores que alimentam tudo. Smart port: o terminal inteligente, como Santos virando referência com 5G e gêmeo digital. E IA, que prevê e otimiza. Some a isso o monitoramento climático com IA: sensores e modelos que dão alerta precoce de chuva, vento ou encosta saturando — a infraestrutura deixa de ser reativa e passa a ser preditiva. Isso é resiliência."

### 5. Encerramento (9:15 – 10:00)

> "Você viu por que a infraestrutura de transportes importa tanto, como o engenheiro civil é peça-chave e qual é a nova fronteira digital do setor. Na próxima aula, vamos um passo atrás: antes de construir, é preciso planejar. Como se estuda demanda? Como se prova que uma obra vale a pena? Te espero na Aula 2!"

---

## Aula 2 — Planejamento de transportes e estudo de demanda

> Antes de qualquer obra de infraestrutura nascer, alguém precisa responder a uma pergunta de bilhões de reais: **vale a pena construir?** Uma ferrovia mal planejada vira "ferrovia fantasma"; um aeroporto superdimensionado vira "elefante branco". Nesta aula, você vai conhecer o ferramental que evita esses erros: o planejamento de transportes, o modelo de quatro etapas, os estudos de viabilidade e o licenciamento ambiental.

### Planejamento de infraestrutura de transportes

Planejar transportes é decidir **o que construir, onde, quando e com que recursos**, alinhando a oferta de infraestrutura à demanda futura de deslocamentos. Esse planejamento acontece em camadas: o **estratégico** (políticas e planos nacionais, como o PNL), o **tático** (programas regionais) e o **operacional** (projetos específicos).

![Congestionamento de tráfego em rodovia — a demanda de transporte é o ponto de partida do planejamento de infraestrutura](https://commons.wikimedia.org/wiki/Special:FilePath/Traffic%20jam.jpg)

No Brasil, o planejamento federal é coordenado pelo **Ministério dos Transportes** e pela **EPL (Empresa de Planejamento e Logística S.A.)**, materializado no **Plano Nacional de Logística (PNL)**. A EPL publica regularmente matrizes de transporte inter-regional de carga, que mostram, modal a modal, quanto e o quê o Brasil movimenta entre as regiões. Para o engenheiro, planejar bem significa garantir que a obra atenderá à demanda por toda a sua vida útil — tipicamente de 20 a 50 anos.

O Programa de Parcerias de Investimentos (PPI), vinculado à Casa Civil, organiza as concessões federais de rodovias, ferrovias, portos e aeroportos. Quando um projeto entra no PPI, significa que passou por uma análise de demanda, viabilidade e modelagem de concessão — o engenheiro precisa entender esse processo para atuar tanto no setor público quanto junto a concessionárias.

### O modelo de quatro etapas

O método clássico de previsão de demanda de transportes é o **modelo de quatro etapas** (four-step model), usado mundialmente:

1. **Geração de viagens** — quantas viagens são produzidas e atraídas por cada zona (depende de população, empregos, atividade econômica).
2. **Distribuição de viagens** — para onde vão essas viagens, normalmente calculada pelo **modelo gravitacional** (zonas próximas e grandes atraem mais).
3. **Divisão modal** — qual modal cada viagem usará (carro, ônibus, trem), conforme custo, tempo e conforto.
4. **Alocação de tráfego** — por quais rotas/vias as viagens se distribuem na rede.

![Fluxo do modelo de quatro etapas: geração, distribuição, divisão modal e alocação de tráfego, transformando dados socioeconômicos em fluxos previstos](assets/modelo_4_etapas.svg)

Esse modelo transforma dados socioeconômicos em **fluxos previstos** — a base de todo dimensionamento de capacidade.

### Estudo de demanda e de tráfego

O estudo de demanda quantifica **quantos** vão usar a infraestrutura e **como esse número cresce** no tempo. Para rodovias, o indicador central é o **VDM (Volume Diário Médio)**; para portos, a movimentação anual em toneladas ou TEUs; para aeroportos, o número de passageiros e movimentos de aeronaves por ano.

A projeção costuma usar taxas de crescimento ancoradas no PIB e na população. Um erro comum é projetar crescimento linear quando o fenômeno é **exponencial** — ou vice-versa. Subdimensionar gera congestionamento precoce; superdimensionar desperdiça capital.

No Brasil, a ANTT publica contagens de tráfego nas rodovias federais e ferrovias concedidas; a ANTAQ divulga estatísticas portuárias anuais; e a ANAC disponibiliza dados de movimentação aeroportuária — todas fontes primárias para estudos de demanda.

### Viabilidade técnica e econômica

Definida a demanda, avalia-se a **viabilidade**. Os principais indicadores são:

- **VPL (Valor Presente Líquido)** — soma dos benefícios menos custos, trazidos a valor presente. Se VPL > 0, o projeto cria valor.
- **TIR (Taxa Interna de Retorno)** — taxa que zera o VPL; comparada à taxa mínima de atratividade.
- **Relação Benefício/Custo (B/C)** — benefícios divididos por custos; viável se B/C > 1.

A análise considera benefícios como economia de tempo, redução de custo operacional e de acidentes, e externalidades (emissões, ruído). É a etapa que separa obra útil de desperdício de dinheiro público.

### O EVTEA: o estudo que decide o que se constrói

No Brasil, todos esses indicadores são consolidados em um documento formal: o **EVTEA — Estudo de Viabilidade Técnica, Econômica e Ambiental**. Ele é a peça que **prioriza** quais obras entram na carteira de investimentos. Por lei, **obras de infraestrutura de transporte de grande porte (acima de R\$ 20 milhões) devem ser precedidas de EVTEA**, que por sua vez antecede os estudos ambientais e os projetos de engenharia.

O EVTEA reúne três análises integradas, desenvolvidas em etapas:

1. **Estudos preliminares** — coleta e tratamento de dados disponíveis (tráfego, socioeconômicos, ambientais).
2. **Diagnóstico e alternativas** — análise dos dados, identificação dos problemas e proposição de soluções de traçado/projeto.
3. **Análise técnica** — define as obras de adequação/construção necessárias e estima os custos.
4. **Avaliação ambiental** — identifica os impactos de cada alternativa (insumo para o licenciamento posterior).
5. **Análise econômica e socioeconômica** — consolida tudo e calcula os indicadores **TIR, VPL e B/C** que decidem a viabilidade.

Na prática, é o EVTEA que responde à pergunta de abertura desta aula — "vale a pena construir?" — com números defensáveis. Órgãos como o **DNIT** e a antiga **VALEC** publicam EVTEA de rodovias e ferrovias; sem ele, uma obra federal de grande porte simplesmente não avança.

### Marcos regulatórios: quem regula o quê

Saber a quem o projeto se reporta é parte do planejamento. Quatro instituições estruturam o setor — e cada uma reaparecerá nos modais desta disciplina:

- **DNIT (Departamento Nacional de Infraestrutura de Transportes)** — **executa e gere** a infraestrutura federal **não concedida** (rodovias, ferrovias e hidrovias sob gestão direta); publica EVTEA, normas e manuais. É órgão de execução, não agência reguladora.
- **ANTT (Agência Nacional de Transportes Terrestres)** — **regula** o transporte **terrestre**: ferrovias e rodovias concedidas, transporte interestadual de passageiros e cargas perigosas.
- **ANTAQ (Agência Nacional de Transportes Aquaviários)** — **regula** o transporte **aquaviário**: portos organizados, terminais, cabotagem, navegação interior e de longo curso.
- **ANAC (Agência Nacional de Aviação Civil)** — **regula** a **aviação civil** e a infraestrutura aeroportuária (criada pela Lei nº 11.182/2005).

A regra mnemônica: **DNIT constrói e gere; as agências (ANTT, ANTAQ, ANAC) regulam serviços e concessões.** As concessões federais ainda passam pelo **PPI** (Programa de Parcerias de Investimentos), já citado.

### Descarbonização e ESG na decisão de projetos

A viabilidade de uma obra deixou de ser só técnica e econômica — passou a ser também **ambiental e social**. Metas de **descarbonização** (redução de emissões de CO₂, alinhadas a compromissos climáticos do país) hoje **pesam na priorização**: projetos que tiram carga do caminhão e a colocam no trilho ou na hidrovia ganham pontos justamente por emitirem menos por tonelada transportada.

Esse olhar se sistematiza na sigla **ESG** (*Environmental, Social, Governance* — ambiental, social e governança). Cada vez mais, financiadores e órgãos exigem que o projeto demonstre **desempenho ambiental** (emissões, biodiversidade), **impacto social** (comunidades, segurança, empregos) e **governança** (transparência, controle). Para o engenheiro, isso significa que o EVTEA e a análise de viabilidade já incorporam critérios de descarbonização e ESG — uma obra que ignora esses fatores tem cada vez menos chance de receber financiamento e licença.

### Licenciamento ambiental

Nenhuma grande obra de infraestrutura sai do papel sem **licenciamento ambiental**, conduzido por órgãos como o **IBAMA** (federal) ou órgãos estaduais (como a CETESB em São Paulo). O processo tem três licenças sequenciais:

- **LP (Licença Prévia)** — aprova a viabilidade ambiental e a localização; exige o **EIA/RIMA** (Estudo e Relatório de Impacto Ambiental) para grandes obras.
- **LI (Licença de Instalação)** — autoriza o início da construção.
- **LO (Licença de Operação)** — autoriza o funcionamento.

![Sequência do licenciamento ambiental: Licença Prévia (LP), de Instalação (LI) e de Operação (LO), ao longo do tempo](assets/licenciamento.svg)

O licenciamento frequentemente é o **maior gargalo** de prazo em obras de ferrovia e porto, podendo levar anos. A própria FIOL (Ferrovia de Integração Oeste-Leste) levou mais de uma década entre o projeto e o início das obras, em parte por conta do licenciamento ambiental no bioma Cerrado e na Mata Atlântica. Ignorar esse prazo no cronograma é receita para atraso e judicialização.

### Exemplo numérico: projeção de demanda

Suponha um aeroporto regional que movimentou $800.000$ passageiros em 2025, com crescimento anual estimado em $5\%$. Qual a demanda projetada para 2035 (10 anos depois)?

Usamos a fórmula de crescimento composto:

$$
D_n = D_0 \times (1 + i)^n
$$

onde $D_0 = 800.000$, $i = 0{,}05$ e $n = 10$:

$$
D_{10} = 800.000 \times (1{,}05)^{10}
$$

Como $(1{,}05)^{10} \approx 1{,}629$:

$$
D_{10} \approx 800.000 \times 1{,}629 = 1.303.000 \text{ passageiros}
$$

Ou seja, em 10 anos a demanda saltaria de $800$ mil para cerca de $1{,}3$ milhão de passageiros — um crescimento de **63%**. Esse número é o que define se o terminal atual aguenta ou se será preciso ampliá-lo. Se o engenheiro projetar apenas para a demanda de hoje, o aeroporto estará saturado antes mesmo de a obra ser inaugurada.

### Atividade prática

Escolha uma cidade média da sua região e imagine um novo terminal rodoviário interestadual. Em uma folha:

1. Liste **3 variáveis socioeconômicas** que você usaria para estimar a geração de viagens (população, renda, turismo, etc.).
2. Projete a demanda para 15 anos supondo um crescimento anual de $4\%$ a partir de um valor inicial que você arbitrar.
3. Aponte **um benefício** e **um impacto ambiental** que apareceriam no estudo de viabilidade e licenciamento.

### Pontos-chave

- Planejamento de transportes alinha **oferta de infraestrutura** à **demanda futura**, em horizontes de 20 a 50 anos.
- O **modelo de quatro etapas** (geração, distribuição, divisão modal, alocação) é o método clássico de previsão de demanda.
- Indicadores de viabilidade: **VPL**, **TIR** e **relação Benefício/Custo** — eles separam obra útil de "elefante branco".
- O **EVTEA** (Estudo de Viabilidade Técnica, Econômica e Ambiental) é obrigatório para obras acima de R\$ 20 milhões e **prioriza** o que se constrói, antecedendo estudos ambientais e projetos.
- Marcos regulatórios: **DNIT** executa/gere a infraestrutura não concedida; **ANTT**, **ANTAQ** e **ANAC** regulam, respectivamente, o terrestre, o aquaviário e a aviação civil.
- **Descarbonização** e critérios **ESG** (ambiental, social, governança) hoje pesam na priorização e no financiamento dos projetos.
- O **licenciamento ambiental** (LP, LI, LO) é etapa obrigatória e costuma ser o maior gargalo de prazo.
- Projetar para a demanda de hoje é erro: deve-se usar **crescimento composto** para dimensionar a vida útil da obra.

### Para saber mais

- **ANTT — Agência Nacional de Transportes Terrestres:** https://www.gov.br/antt/
- **IBAMA — Licenciamento Ambiental Federal:** https://www.gov.br/ibama/pt-br
- **Wikipedia — Modelo de quatro etapas (Trip distribution / Transportation forecasting):** https://en.wikipedia.org/wiki/Transportation_forecasting
- **EPL — Plano Nacional de Logística:** https://www.gov.br/transportes/pt-br
- **DNIT — Estudo de Viabilidade Técnica, Econômica e Ambiental (EVTEA):** https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/planejamento/covide-estudos-de-viabilidade/estudo-de-viabilidade-tecnica-economica-e-ambiental-evtea
- **Lei nº 10.233/2001 — cria ANTT, ANTAQ e DNIT (marco regulatório dos transportes):** https://www.planalto.gov.br/ccivil_03/leis/leis_2001/l10233.htm
- **ANTAQ — Agência Nacional de Transportes Aquaviários (regulação portuária e descarbonização do setor):** https://www.gov.br/antaq/pt-br

## Aula 2 — Roteiro da Videoaula 2: "Planejamento de transportes e estudo de demanda"

**Duração: 7 a 10 minutos**

### 1. Abertura (0:00 – 0:35)

> "Antes de qualquer obra nascer, alguém precisa responder: vale a pena construir? Uma ferrovia mal planejada vira ferrovia fantasma; um aeroporto grande demais vira elefante branco. Hoje você vai aprender o ferramental que evita esses erros bilionários."

### 2. Desenvolvimento — parte 1 (0:35 – 3:30)

> "Planejamento acontece em camadas: estratégico, tático e operacional. No Brasil, a EPL e o Ministério dos Transportes coordenam o PNL, que orienta os investimentos. No centro do método está o modelo de quatro etapas — geração, distribuição, divisão modal e alocação. Vou explicar cada uma: quantas viagens nascem, para onde vão, em qual modal e por qual rota. Dados da ANTT, ANTAQ e ANAC alimentam essas projeções."

### 3. Desenvolvimento — parte 2 (3:30 – 6:30)

> "Com a demanda estimada, vem a viabilidade. Três indicadores mandam: VPL, TIR e relação benefício-custo. No Brasil, tudo isso é consolidado no EVTEA — o Estudo de Viabilidade Técnica, Econômica e Ambiental. Obra de transporte acima de 20 milhões de reais exige EVTEA, que vem antes dos estudos ambientais e do projeto. E é bom saber quem regula o quê: o DNIT executa e gere a infraestrutura não concedida; a ANTT cuida do terrestre, a ANTAQ do aquaviário, a ANAC da aviação. Hoje entra também a descarbonização e o ESG: tirar carga do caminhão emite menos CO₂, e isso pesa na priorização e no financiamento. E não esqueça do licenciamento ambiental — LP, LI e LO. Esse processo, conduzido pelo IBAMA, costuma ser o maior gargalo de prazo. A FIOL levou mais de uma década até o início das obras por conta disso."

### 4. Desenvolvimento — parte 3 (6:30 – 8:30)

> "Vamos à conta. Um aeroporto com 800 mil passageiros, crescendo 5% ao ano. Em 10 anos? Aplicando o crescimento composto, chegamos a 1,3 milhão — 63% a mais! Se o engenheiro projetar só para hoje, o terminal satura antes de inaugurar. Por isso projetamos para a demanda futura, não a atual."

### 5. Encerramento (8:30 – 10:00)

> "Agora você sabe planejar e provar que uma obra vale a pena. Na próxima aula, descemos para o terreno literalmente: geometria, terraplenagem e geotecnia. Como se molda o relevo para uma estrada ou ferrovia passar? Te espero na Aula 3!"

---

## Aula 3 — Geometria, terraplenagem e geotecnia aplicada

> Toda estrada, ferrovia ou pista de aeroporto precisa de uma coisa em comum: um terreno **plano e firme** para se apoiar. Mas a natureza raramente oferece isso de graça — há morros para cortar, vales para aterrar e solos fracos para reforçar. Nesta aula, você vai entender como o engenheiro molda o relevo (terraplenagem), equilibra os volumes de terra e garante que o solo aguente as cargas. É a engenharia que acontece **antes** do pavimento.

### Topografia e traçado

Tudo começa com a **topografia**: o levantamento do relevo do terreno por onde a infraestrutura vai passar. A partir dela, o engenheiro define o **traçado** — a linha que a estrada ou ferrovia seguirá, em planta (vista de cima) e em perfil (vista lateral).

![Corte em rocha em obra rodoviária, resultado de operações de terraplenagem](https://commons.wikimedia.org/wiki/Special:FilePath/Road%20cut.jpg)

O bom traçado equilibra três objetivos: **segurança** (curvas e rampas suaves), **economia** (menor volume de terra movimentada) e **respeito ao meio ambiente**. Em ferrovias, a restrição é dura: as **rampas** raramente passam de $1\%$ a $2\%$ e as curvas têm raios mínimos generosos, porque o trem não sobe ladeira nem faz curva fechada como o caminhão.

O DNIT estabelece as normas de projeto geométrico para rodovias federais (como a DNIT 006/2004 para alinhamento horizontal), enquanto a ABNT e os manuais ferroviários — também publicados pelo DNIT — regulam os projetos de via permanente. Qualquer projeto de infraestrutura linear no Brasil parte dessas normas.

### Terraplenagem: corte e aterro

**Terraplenagem** é o conjunto de operações que adapta o terreno natural ao greide (perfil) de projeto. Há duas operações fundamentais:

- **Corte (escavação)** — remoção de material onde o terreno está **acima** do greide (um morro).
- **Aterro** — adição de material compactado onde o terreno está **abaixo** do greide (um vale).

O ideal é que o material retirado nos cortes seja reaproveitado nos aterros, minimizando empréstimos (terra trazida de fora) e bota-foras (terra descartada). Cada metro cúbico movimentado custa dinheiro, então **equilibrar corte e aterro** é objetivo central do projeto.

Em obras como a duplicação da BR-163 (Mato Grosso–Pará) e a construção do trecho norte da FIOL, os volumes de terraplenagem chegam a dezenas de milhões de metros cúbicos, evidenciando a escala e a importância dessa etapa.

### Compensação de volumes (diagrama de massas)

A ferramenta para equilibrar terra é o **diagrama de massas** (ou curva de Bruckner). Ele acumula, ao longo do traçado, o volume de corte (positivo) e de aterro (negativo). Lendo o diagrama, o engenheiro identifica:

- Trechos onde sobra material (corte) e trechos onde falta (aterro).
- A **distância média de transporte** da terra (o quanto e por quanto tempo o caminhão precisa carregar material).
- A necessidade de **empréstimos** (jazidas externas) ou **bota-foras** (áreas de descarte).

Um diagrama bem trabalhado pode reduzir drasticamente o custo da obra, porque transporte de terra é um dos itens mais caros da terraplenagem.

![Diagrama de massas (curva de Bruckner): perfil com cortes e aterros acima e a curva de volume acumulado abaixo, que sobe nos cortes e desce nos aterros](assets/diagrama_massas.svg)

### Drenagem

Água é a maior inimiga da infraestrutura. Solo encharcado perde resistência; pavimento com água por baixo se desfaz. Por isso, todo projeto inclui **drenagem**:

- **Superficial** — sarjetas, valetas, bueiros e canaletas que coletam a água da chuva e a afastam da plataforma.
- **Profunda (subterrânea)** — drenos que rebaixam o lençol freático e mantêm o subleito seco.

O dimensionamento da drenagem parte do estudo hidrológico (chuvas da região) e calcula a vazão que cada dispositivo precisa escoar. Negligenciar a drenagem é a causa número um de patologias precoces em estradas brasileiras — basta lembrar das erosões que comprometem rodovias após a temporada de chuvas no Centro-Oeste e no Norte do país.

### Solos e fundações

O solo onde tudo se apoia precisa ser **caracterizado** geotecnicamente. Os ensaios clássicos incluem:

- **Granulometria** — distribuição dos tamanhos das partículas.
- **Limites de Atterberg** — limites de liquidez (LL) e plasticidade (LP), que indicam o comportamento de solos finos.
- **Compactação (Proctor)** — define a umidade ótima e a densidade máxima.
- **CBR (Índice de Suporte Califórnia)** — mede a capacidade do solo de resistir à penetração; é a principal entrada para o dimensionamento do pavimento.

Solos fracos (argilas moles, turfas) exigem soluções de **reforço**: troca de material, estabilização com cal/cimento, geossintéticos ou fundações profundas. Conhecer o solo é o que separa um aterro estável de um deslizamento.

### Exemplo numérico: volume de terraplenagem

Vamos calcular o volume de um aterro com seção trapezoidal. A plataforma tem **base superior** $b = 12\,\mathrm{m}$, **altura** $h = 4\,\mathrm{m}$ e **taludes** com inclinação $1{:}1{,}5$ (1 vertical para 1,5 horizontal), aplicados nos dois lados, ao longo de um trecho de $L = 200\,\mathrm{m}$.

Primeiro, a base inferior (maior), que soma a projeção horizontal dos dois taludes:

$$
B = b + 2 \times (1{,}5 \times h) = 12 + 2 \times (1{,}5 \times 4) = 12 + 12 = 24\,\mathrm{m}
$$

A área da seção transversal trapezoidal é:

$$
A = \frac{(b + B)}{2} \times h = \frac{(12 + 24)}{2} \times 4 = 18 \times 4 = 72\,\mathrm{m^2}
$$

O volume do aterro no trecho é a área multiplicada pelo comprimento:

$$
V = A \times L = 72 \times 200 = 14.400\,\mathrm{m^3}
$$

![Seção transversal do aterro trapezoidal cotado: plataforma b = 12 m, base B = 24 m, altura h = 4 m e taludes 1:1,5, com A = 72 m² e V = 14.400 m³](assets/secao_terraplenagem.svg)

Se cada metro cúbico de aterro custa cerca de $25\,\mathrm{R\$}$ (escavação, transporte e compactação), o custo desse trecho seria $14.400 \times 25 = 360.000\,\mathrm{R\$}$. É o tipo de conta que mostra por que compensar corte e aterro economiza fortunas.

### Pausa para reflexão (Desafio)

Imagine que você é o engenheiro responsável por uma ferrovia que precisa cruzar uma serra. Você tem duas opções de traçado: **(A)** contornar a serra, dobrando a distância mas com rampas suaves e pouca terraplenagem; ou **(B)** atravessar a serra em linha reta, com túneis, cortes profundos e rampas no limite. A opção A é mais barata de construir, mas mais cara de operar para sempre (mais combustível, mais tempo). A opção B é cara de construir, mas barata de operar.

**Como você decidiria?** Quais variáveis pesariam na sua análise — custo de construção, custo operacional ao longo de 50 anos, impacto ambiental, prazo? Reflita: na engenharia de transportes, a decisão "correta" quase nunca é a mais barata hoje, mas a que minimiza o **custo total ao longo da vida útil**.

### Atividade prática

Pegue um trecho de estrada que você conhece (pode ser no Google Earth) com um corte ou aterro visível. Em uma folha:

1. Identifique visualmente onde há **corte** e onde há **aterro**.
2. Estime a **altura** aproximada do aterro ou corte mais alto.
3. Aponte os dispositivos de **drenagem** visíveis (sarjetas, bueiros).
4. Discuta: o traçado parece priorizar economia de terra ou suavidade de curvas/rampas?

### Pontos-chave

- O **traçado** equilibra segurança, economia e meio ambiente; ferrovias exigem rampas suaves (≤1-2%) e curvas amplas.
- **Terraplenagem** é cortar onde sobra e aterrar onde falta, idealmente reaproveitando a terra.
- O **diagrama de massas** equilibra volumes e minimiza o transporte de terra — um dos custos mais altos da obra.
- **Drenagem** (superficial e profunda) protege a infraestrutura; água mal escoada é a principal causa de patologias.
- O **CBR** e os ensaios geotécnicos caracterizam o solo e alimentam o dimensionamento do pavimento.

### Para saber mais

- **DNIT — Manual de Implantação Básica de Rodovia / Normas de Terraplenagem:** https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/ipr/normas-e-manuais
- **PONTES FILHO, Glauco.** *Estradas de Rodagem: Projeto Geométrico*. (livro consagrado de geometria de vias)
- **Wikipedia — Terraplenagem (Earthworks):** https://en.wikipedia.org/wiki/Earthworks_(engineering)
- **ABGE — Associação Brasileira de Geologia de Engenharia e Ambiental:** https://www.abge.org.br/

## Aula 3 — Roteiro da Videoaula 3: "Geometria, terraplenagem e geotecnia aplicada"

**Duração: 7 a 10 minutos**

### 1. Abertura (0:00 – 0:35)

> "Toda estrada, ferrovia ou pista de avião precisa de um terreno plano e firme. Mas a natureza não dá isso de graça: tem morro para cortar, vale para aterrar, solo fraco para reforçar. Hoje você vai aprender como o engenheiro molda o relevo — a obra que acontece antes do pavimento."

### 2. Desenvolvimento — parte 1 (0:35 – 3:30)

> "Tudo começa na topografia e no traçado. O engenheiro define a linha em planta e perfil, seguindo normas do DNIT, equilibrando segurança, economia e meio ambiente. Em ferrovia, a regra é dura: rampas de no máximo 1 a 2%, curvas amplas, porque o trem não sobe ladeira. Depois vem a terraplenagem: corte onde o terreno está acima do greide, aterro onde está abaixo. Obras como a BR-163 e a FIOL mostram o que é isso em escala real."

### 3. Desenvolvimento — parte 2 (3:30 – 6:30)

> "Como equilibrar a terra que sobra com a que falta? Com o diagrama de massas, a curva de Bruckner. Ele mostra onde há excesso, onde há falta e quanto a terra precisa ser transportada. E nunca esqueça a água: drenagem superficial e profunda. Solo encharcado perde resistência — é a causa número um de buraco em estrada brasileira. Basta ver as rodovias no Norte após a chuva."

### 4. Desenvolvimento — parte 3 (6:30 – 8:30)

> "O solo precisa ser caracterizado: granulometria, limites de Atterberg, Proctor e o famoso CBR, que mede a capacidade de suporte. Vamos calcular um aterro: plataforma de 12 metros, 4 de altura, taludes 1 para 1,5, num trecho de 200 metros. A seção dá 72 metros quadrados, o volume dá 14.400 metros cúbicos — e cerca de 360 mil reais. Olha o tamanho da economia de equilibrar corte e aterro!"

### 5. Encerramento (8:30 – 10:00)

> "Você viu como se prepara o terreno e por que conhecer o solo é vital. Mas o que vai por cima dessa plataforma? Pavimentos, materiais, estruturas que aguentam cargas pesadíssimas. É o tema da próxima aula, que fecha os fundamentos comuns às três infraestruturas. Te espero na Aula 4!"

---

## Aula 4 — Materiais e pavimentos: fundamentos comuns às três infraestruturas

> Um caminhão carregado, um trem de minério e um Boeing pousando têm algo em comum: todos transmitem cargas enormes para uma estrutura que precisa não afundar, não trincar e durar décadas. Essa estrutura é o **pavimento**. Nesta aula, que fecha a unidade de fundamentos, você vai entender os materiais da infraestrutura, a diferença entre pavimento flexível e rígido, como as cargas atuam e por que manutenção é tão importante quanto construção.

### Materiais de construção em infraestrutura

A infraestrutura de transportes usa um conjunto recorrente de materiais, cada um com função clara:

- **Solos e agregados** (brita, areia, cascalho) — formam as camadas inferiores (sub-base e base) e dão suporte estrutural.
- **Ligantes asfálticos (CAP)** — o cimento asfáltico de petróleo, que une os agregados no revestimento flexível. No Brasil, a Petrobras é o principal fornecedor de CAP, e os graus de penetração e viscosidade seguem normas da ABNT.
- **Concreto de cimento Portland** — usado em pavimentos rígidos, cais, lajes e estruturas.
- **Aço** — em armaduras de concreto, trilhos ferroviários e estruturas metálicas.
- **Geossintéticos** — geotêxteis e geogrelhas que reforçam, separam e drenam solos.

![Camadas de um pavimento asfáltico durante a construção de uma rodovia](https://commons.wikimedia.org/wiki/Special:FilePath/Asphalt%20paving.jpg)

A escolha do material depende da carga, do clima e do custo — e o engenheiro precisa conhecer as propriedades de cada um para especificar corretamente.

### Pavimentos flexíveis e rígidos

Existem duas grandes famílias de pavimento:

- **Pavimento flexível** — revestimento em **concreto asfáltico**, apoiado em camadas de base e sub-base granulares. "Flexível" porque se deforma com a carga e distribui o esforço gradualmente para as camadas inferiores. É o mais comum em rodovias brasileiras: mais barato de construir, mas exige manutenção frequente.
- **Pavimento rígido** — placa de **concreto de cimento Portland**, que trabalha à flexão e distribui a carga em grande área. Mais caro de construir, porém muito durável e com baixa manutenção. Usado em pátios de aeroporto, corredores de ônibus e trechos de alto tráfego.

Em aeroportos, ambos coexistem: pistas longas costumam ser flexíveis (ou rígidas), e os pátios de estacionamento de aeronaves, onde a carga é estática e concentrada, costumam ser rígidos. O Aeroporto Internacional de Guarulhos (GRU) é um bom exemplo: pistas em concreto asfáltico modificado e pátios parcialmente em placa de concreto.

### Cargas e solicitações

As cargas variam enormemente entre os três modais:

| Infraestrutura | Carga típica de referência |
| --- | --- |
| Rodovia | Eixo padrão de $8{,}2\,\mathrm{t}$ (80 kN) |
| Ferrovia | Carga por eixo de $25$ a $32{,}5\,\mathrm{t}$ |
| Aeroporto | Trem de pouso com centenas de toneladas distribuídas |

![Cargas de referência por modal: eixo rodoviário padrão de 8,2 t (80 kN), eixo ferroviário de 25 a 32,5 t e trem de pouso de aeronave com centenas de toneladas distribuídas](assets/cargas_eixo.svg)

A solicitação do pavimento não depende só do peso, mas da **repetição**. Por isso usa-se o conceito de **número N**: o número equivalente de passagens do eixo padrão ao longo da vida útil. Quanto maior o N, mais robusto precisa ser o pavimento. Um trem de minério, com eixos de 30 toneladas passando milhares de vezes, impõe solicitações muito superiores às de uma rodovia comum.

### Estruturas de concreto e de aço

Além do pavimento, a infraestrutura de transportes é repleta de **estruturas**: pontes e viadutos rodoviários e ferroviários, cais portuários, edifícios de terminais aeroportuários, torres de controle. O **concreto armado e protendido** domina as grandes obras pela durabilidade e custo; o **aço** aparece em pontes de grandes vãos e estruturas metálicas leves.

Cada estrutura é dimensionada para as cargas que receberá: peso próprio, cargas móveis (veículos, trens, aeronaves), vento, e, em portos, esforços de atracação e ondas. As normas da **ABNT** (como a NBR 6118, de concreto) e os manuais do DNIT regem esse dimensionamento.

### Manutenção e vida útil

Construir é metade do trabalho; manter é a outra metade. Todo pavimento e estrutura têm **vida útil de projeto** (tipicamente 10 anos para revestimento asfáltico, 20+ para rígido, 50-100 para pontes). A manutenção pode ser:

- **Preventiva** — feita antes da falha (selagem de trincas, microrrevestimento). Barata.
- **Corretiva** — feita após a falha (tapa-buraco, recapeamento). Cara.
- **Reabilitação/reconstrução** — quando a estrutura chega ao fim da vida útil.

A "curva de degradação" mostra que **adiar manutenção preventiva multiplica o custo futuro** — cada R\$ 1 economizado em prevenção pode custar R\$ 4 a R\$ 5 em correção. Gestão de pavimentos é, no fundo, gestão de dinheiro público. No Brasil, a CNT publica anualmente a Pesquisa CNT de Rodovias, que avalia o estado de conservação das rodovias federais — um termômetro nacional do estado da manutenção rodoviária.

### Exemplo numérico: dimensionamento simplificado

Vamos estimar a **vida útil em repetições de carga** de um pavimento usando a relação simplificada de fadiga. Suponha que o pavimento suporte um número $N = 5 \times 10^6$ repetições do eixo padrão antes de falhar, e que a via receba $V = 1.200$ veículos pesados por dia, cada um equivalente a $1{,}5$ eixo padrão (fator de equivalência).

As repetições por dia são:

$$
N_{\text{dia}} = V \times f = 1.200 \times 1{,}5 = 1.800 \text{ eixos-padrão/dia}
$$

As repetições por ano (365 dias):

$$
N_{\text{ano}} = 1.800 \times 365 = 657.000 \text{ eixos-padrão/ano}
$$

A vida útil em anos é o total suportado dividido pela solicitação anual:

$$
t = \frac{N}{N_{\text{ano}}} = \frac{5 \times 10^6}{657.000} \approx 7{,}6 \text{ anos}
$$

Ou seja, esse pavimento atingiria o fim da vida estrutural em cerca de **7 anos e meio** sem intervenções. Se o projeto exigir 10 anos, o engenheiro precisa **reforçar as camadas** (aumentar a espessura) ou usar materiais mais resistentes. É exatamente assim que se calibra a espessura de um pavimento na prática.

### Atividade prática

Observe um trecho de rua ou rodovia próximo de você e classifique:

1. O pavimento é **flexível** (asfalto) ou **rígido** (concreto)?
2. Identifique **2 patologias** visíveis (trincas, buracos, afundamentos, remendos).
3. Classifique a manutenção necessária como **preventiva** ou **corretiva**.
4. Estime o **tráfego de veículos pesados** (alto/médio/baixo) e relacione com o estado do pavimento.

### Pontos-chave

- A infraestrutura usa materiais recorrentes: **solos/agregados, asfalto (CAP), concreto, aço e geossintéticos**.
- **Pavimento flexível** (asfalto) é mais barato e deformável; **pavimento rígido** (concreto) é mais durável e caro.
- As cargas variam por modal; o **número N** mede a repetição de carga e dimensiona a robustez do pavimento.
- Estruturas (pontes, cais, terminais) são dimensionadas por normas **ABNT/DNIT** para todas as cargas que receberão.
- **Manutenção preventiva** custa muito menos que a corretiva — adiar manutenção multiplica o custo futuro.

### Para saber mais

- **BERNUCCI, L. B. et al.** *Pavimentação Asfáltica: Formação Básica para Engenheiros*. (livro de referência, Petrobras/Abeda)
- **DNIT — Manual de Pavimentação:** https://www.gov.br/dnit/pt-br/assuntos/planejamento-e-pesquisa/ipr/normas-e-manuais
- **Wikipedia — Pavimento (Road surface):** https://en.wikipedia.org/wiki/Road_surface
- **ABCP — Associação Brasileira de Cimento Portland (pavimento de concreto):** https://abcp.org.br/

### O que você verá na próxima unidade

Na **Unidade 2 — Portos e Hidrovias**, vamos sair em direção à água. Você vai entender o que torna um porto eficiente, como funcionam terminais de contêineres e granéis, o que é cabotagem e por que as hidrovias brasileiras (como a do Tietê-Paraná e a do Madeira) são tão estratégicas. Vamos estudar a engenharia do cais, os esforços de atracação, a dragagem dos canais e como o transporte aquaviário pode reequilibrar a nossa matriz. Tudo o que você aprendeu aqui — matriz, planejamento, terraplenagem, pavimentos — vai se aplicar agora ao ambiente portuário e hidroviário.

## Aula 4 — Roteiro da Videoaula 4: "Materiais e pavimentos: fundamentos comuns às três infraestruturas"

**Duração: 7 a 10 minutos**

### 1. Abertura (0:00 – 0:35)

> "Um caminhão carregado, um trem de minério e um Boeing pousando têm uma coisa em comum: todos jogam cargas enormes numa estrutura que não pode afundar nem trincar. Essa estrutura é o pavimento. Hoje, fechando os fundamentos, você vai entender materiais, pavimentos, cargas e por que manutenção é tão importante quanto construir."

### 2. Desenvolvimento — parte 1 (0:35 – 3:30)

> "Primeiro os materiais: solos e agregados nas camadas de base, asfalto CAP no revestimento flexível — fornecido principalmente pela Petrobras seguindo normas ABNT —, concreto Portland no rígido, aço nas armaduras e trilhos, geossintéticos no reforço. Depois as duas famílias de pavimento: o flexível, de asfalto, mais barato mas que pede manutenção; e o rígido, de concreto, caro mas durável. No aeroporto de Guarulhos, por exemplo, os dois convivem."

### 3. Desenvolvimento — parte 2 (3:30 – 6:30)

> "As cargas variam muito: eixo de 8,2 toneladas na rodovia, até cerca de 32 na ferrovia, centenas de toneladas num avião. Mas o que destrói o pavimento não é só o peso, é a repetição — o número N. E há também as estruturas: pontes, cais, terminais, dimensionados pelas normas da ABNT e do DNIT para cada carga que vão receber. A NBR 6118 rege o concreto armado nessas estruturas."

### 4. Desenvolvimento — parte 3 (6:30 – 8:30)

> "Vamos dimensionar. Um pavimento que aguenta 5 milhões de repetições, numa via com 1.200 pesados por dia. A conta dá cerca de 657 mil eixos-padrão por ano, e uma vida útil de 7 anos e meio. Se o projeto pede 10 anos, é preciso reforçar a espessura. E lembre da manutenção: a Pesquisa CNT de Rodovias mostra que mais de 50% das rodovias brasileiras têm algum problema — cada real economizado em prevenção custa de 4 a 5 reais em correção depois."

### 5. Encerramento (8:30 – 10:00)

> "Com esta aula, você fechou os fundamentos comuns a portos, aeroportos e ferrovias: matriz, planejamento, terraplenagem e pavimentos. Agora vamos aplicar tudo isso ao primeiro grande tema: portos e hidrovias, o assunto da Unidade 2. Foi um prazer! Te espero lá."

---

## Quiz não avaliativo

### Questão 1

Sobre a **matriz de transportes brasileira**, assinale a alternativa **correta**:

- [ ] a. A matriz brasileira é equilibrada, com participação semelhante entre rodovias, ferrovias e hidrovias.
- [x] b. A matriz é fortemente concentrada no modal rodoviário (~61%), em desacordo com a vocação de um país continental, que privilegiaria ferrovia e hidrovia para grandes volumes e longas distâncias.
- [ ] c. O modal aéreo é o principal responsável pelo transporte de cargas no Brasil, por sua alta capacidade e baixo custo.
- [ ] d. O modal ferroviário responde por mais de 60% do transporte de cargas no país, superando a rodovia.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) descreve corretamente o desequilíbrio histórico da matriz brasileira — cerca de 61% rodoviário, contra ~21% ferroviário e ~14% aquaviário —, herança do rodoviarismo dos anos 1950. A (a) é falsa: a matriz é desequilibrada. A (c) confunde o papel do modal aéreo, que responde por menos de 1% da carga e é caro. A (d) inverte os números: é a rodovia, não a ferrovia, que ultrapassa 60%.

### Questão 2

No contexto de **terraplenagem e geotecnia**, assinale a alternativa **correta**:

- [ ] a. O diagrama de massas serve apenas para calcular a drenagem superficial da via.
- [ ] b. Aterro é a operação de remover material onde o terreno está acima do greide de projeto.
- [x] c. O objetivo de equilibrar corte e aterro é reaproveitar o material escavado, minimizando empréstimos e bota-foras e reduzindo o custo do transporte de terra.
- [ ] d. O ensaio CBR não tem relação com o dimensionamento de pavimentos, servindo só para classificar rochas.

**Resposta correta:** `c`

**Feedback:** A alternativa (c) está correta: compensar corte e aterro reaproveita a terra escavada, reduzindo empréstimos, bota-foras e o caro transporte de material. A (a) erra: o diagrama de massas (curva de Bruckner) equilibra volumes de terra, não drenagem. A (b) inverte os conceitos — remover material é corte, não aterro. A (d) é falsa: o CBR (Índice de Suporte Califórnia) mede a capacidade de suporte do solo e é entrada fundamental do dimensionamento do pavimento.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma cooperativa agrícola do interior de Goiás produz $600.000\,\mathrm{t}$ de grãos por ano e hoje transporta toda essa produção por **caminhão** até o Porto de Santos, a $900\,\mathrm{km}$ de distância. Surge a possibilidade de construir um **ramal ferroviário** que ligaria a região a uma ferrovia existente, permitindo levar a carga por trilho.
>
> Você foi convidado(a) a elaborar uma **análise técnica preliminar** dessa proposta. Estruture sua resposta em três partes:
>
> 1. **Comparação de custos** — usando custos médios de $0{,}18\,\mathrm{R\$/t \cdot km}$ (rodovia) e $0{,}06\,\mathrm{R\$/t \cdot km}$ (ferrovia), calcule e compare o custo anual de transporte em cada modal e a economia potencial.
> 2. **Fatores de planejamento** — quais estudos e etapas (demanda, viabilidade, licenciamento, geotecnia/terraplenagem) seriam necessários antes da decisão de construir? Justifique.
> 3. **Riscos e recomendação** — aponte 2 riscos do projeto e dê uma recomendação final fundamentada.

**Resposta esperada:**

> Na parte 1, espera-se o cálculo correto. Custo rodoviário anual: $C_{\text{rod}} = 0{,}18 \times 900 \times 600.000 = 97.200.000\,\mathrm{R\$}$ (R\$ 97,2 milhões/ano). Custo ferroviário: $C_{\text{fer}} = 0{,}06 \times 900 \times 600.000 = 32.400.000\,\mathrm{R\$}$ (R\$ 32,4 milhões/ano). A economia anual é de R\$ 64,8 milhões — uma redução de aproximadamente **66,7%**. A resposta de qualidade observa que essa economia precisa ser confrontada com o **custo de construção** do ramal e seu prazo de retorno (payback). Na parte 2, espera-se a menção ao **estudo de demanda** (confirmar volume estável a longo prazo), à **análise de viabilidade** (VPL, TIR, B/C, comparando economia com investimento), ao **licenciamento ambiental** (LP, LI, LO — possível gargalo de prazo) e aos **estudos geotécnicos e de terraplenagem** (topografia, traçado, CBR do solo, equilíbrio corte/aterro, drenagem). Na parte 3, riscos plausíveis incluem: variação de demanda/safra, sobrecusto e atraso de obra, dependência da capacidade da ferrovia existente, e questões fundiárias/ambientais. A recomendação deve ser fundamentada e demonstrar que a economia operacional, embora expressiva, só justifica o investimento se a viabilidade econômica e o licenciamento forem favoráveis. Resposta exemplar evita concluir "vale a pena" só pela economia anual, sem considerar investimento e prazo.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Esta obra trata exatamente do tema que abre a disciplina: a infraestrutura de transportes e o projeto geométrico de vias. Os capítulos iniciais consolidam os conceitos de traçado, geometria e os fundamentos que sustentam rodovias e ferrovias — a mesma base que construímos na Unidade 1. Leitura essencial para fixar a fundamentação técnica e dialogar com autoridade sobre projeto de vias.

- **Nome do livro:** *Estradas de Rodagem: Projeto Geométrico*
- **Capítulo:** Capítulos iniciais — *Fundamentos e geometria de traçado*
- **Organizador:** Glauco Pontes Filho
- **Editora:** (edição do autor / EESC-USP)
- **Link de acesso (BV):** https://plataforma.bvirtual.com.br/
- **Aula em que entra:** Aulas 1 a 4

### Para mergulhar no assunto

> Recomendo o vídeo **"A Construção da Maior Ferrovia Brasileira que Mudou o país para Sempre"**, disponível no YouTube, que mostra em escala real os desafios de engenharia de uma grande obra ferroviária brasileira — terraplenagem, fundações, obras de arte e estruturas de grande porte. Ver essas etapas em ação ajuda a dimensionar a grandiosidade e a responsabilidade do trabalho do engenheiro de infraestrutura.

- **Link(s):** https://www.youtube.com/watch?v=ef9uq4GMzQs
- **Aula em que entra:** Aulas 1 a 4

### Podcast (curadoria, até 45 min)

> O canal oficial da **CNT (Confederação Nacional do Transporte)** no YouTube reúne vídeos, debates e episódios sobre logística, infraestrutura, matriz de transportes e os gargalos do "Custo Brasil", sempre com dados e casos do mercado nacional. Curadoria ideal para conectar a teoria da aula com a realidade do setor.

- **Nome do podcast/canal:** CNT — Confederação Nacional do Transporte (canal oficial no YouTube)
- **Tema recomendado:** Matriz de transportes brasileira e Custo Brasil
- **Link:** https://www.youtube.com/transportecnt
- **Aula em que entra:** Aula 1

### Artigo científico

> Artigo que analisa como a logística de Estado e a logística corporativa atuam sobre o território brasileiro, discutindo o papel da infraestrutura de transportes na reconfiguração espacial e na competitividade econômica do país. Excelente leitura para fundamentar, com base em pesquisa acadêmica publicada no SciELO, os pontos discutidos na Aula 1.

- **Link:** https://doi.org/10.4215/rm2018.e17008
- **Aula em que entra:** Aula 1
- **Referência bibliográfica do artigo no formato ABNT:**
  > SILVEIRA, Marcio Rogerio. **Transportes e a logística frente à reestruturação econômica no Brasil**. *Mercator (Fortaleza)*, v. 17, e17008, 2018. DOI: 10.4215/rm2018.e17008.
