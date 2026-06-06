# Unidade 3 — Aplicações e Digitalização de Processos

- **Disciplina:** Indústria 4.0 e Digitalização de Processos
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 9 a 12

> **Recap da Unidade 2:** vimos as **tecnologias habilitadoras** que dão sustentação à Indústria 4.0 — IIoT (a porta de entrada via sensores), Big Data e Analytics (transformação de dado em insight), Nuvem e Edge (onde processar), e IA/ML (decisão automática). Agora, **descemos ao chão de fábrica** e vemos essas tecnologias em uso real, em aplicações que estão mudando a forma como se produz.

---

## Aula 9 — Manufatura Aditiva (Impressão 3D), Simulação e Digital Twin

A primeira aplicação prática da Indústria 4.0 que vamos explorar é uma das mais visíveis e impactantes: a **manufatura aditiva** (popularmente conhecida como impressão 3D) e seu primo digital, a **simulação** com **digital twin**. Juntas, essas tecnologias estão mudando a forma como engenheiros projetam, produzem e mantêm peças industriais.

### O que é manufatura aditiva

> **Manufatura aditiva** é o processo de **construir uma peça camada por camada**, a partir de um modelo digital, em contraste com a manufatura tradicional (**subtrativa**), em que se parte de um bloco e retira-se material até chegar à peça.

A palavra "aditiva" vem do princípio: você **adiciona** material onde ele precisa estar, em vez de remover de onde ele não precisa estar. Isso muda fundamentalmente a economia da produção: peças complexas, antes proibitivas, ficam viáveis; peças simples em pequena quantidade, antes economicamente inviáveis, agora valem a pena.

![Impressora 3D FDM em operação depositando filamento plástico camada a camada — princípio básico da manufatura aditiva](https://commons.wikimedia.org/wiki/Special:FilePath/MakerBot_Replicator.jpg?width=800)

### As principais tecnologias aditivas

| Tecnologia | Material | Aplicação típica |
| --- | --- | --- |
| **FDM** (Fused Deposition Modeling) | Filamento plástico (PLA, ABS) | Protótipos, peças não-estruturais |
| **SLA / DLP** (Estereolitografia) | Resina líquida + luz UV | Modelos de alta precisão, próteses dentárias |
| **SLS** (Selective Laser Sintering) | Pó de polímero | Peças funcionais, lotes pequenos |
| **DMLS / SLM** (Direct Metal Laser Sintering) | Pó metálico | Peças aeroespaciais, implantes médicos |
| **Binder Jetting** | Areia, metal em pó, gesso | Moldes para fundição, peças cerâmicas |

A **DMLS/SLM** é a fronteira da indústria pesada — permite produzir peças metálicas funcionais que **não poderiam existir** pela manufatura tradicional, com canais internos otimizados, estruturas reticuladas leves e propriedades mecânicas precisas.

### Onde a manufatura aditiva é game-changer

1. **Prototipagem rápida** — antes, um protótipo levava semanas e custava milhares. Hoje, horas e centenas.
2. **Peças de reposição sob demanda** — a Mercedes-Benz já imprime peças raras de caminhões antigos, em vez de manter estoque. Senai-MG fez o mesmo para peças do agronegócio.
3. **Lotes pequenos personalizados** — implantes médicos sob medida do paciente, calçados sob medida do atleta, equipamentos sob medida da fábrica.
4. **Peças com geometria impossível** — turbinas com canais de resfriamento internos otimizados que **só** podem ser impressas em metal.

### O que é simulação industrial

> **Simulação** é a criação de um **modelo virtual** de um sistema (uma peça, uma linha de produção, uma fábrica inteira) para testar comportamentos **antes** de construir no mundo real.

Tipos comuns na indústria:

- **CAE / FEM** (Elementos Finitos) — simula tensões mecânicas, deformação, temperatura em uma peça.
- **CFD** (Dinâmica de Fluidos Computacional) — simula escoamento de gás ou líquido (refrigeração, ventilação, aerodinâmica).
- **Simulação de processos** — simula linhas de produção (gargalos, filas, OEE).
- **Simulação de logística** — armazéns, frotas, rotas.

A **simulação economiza tempo e dinheiro** porque permite **falhar virtualmente** — descobrir que um projeto não funciona **antes** de gastar com protótipo, ferramentaria ou retrabalho.

### Digital twin — quando simulação encontra IIoT

Vimos digital twin na Unidade 1, conceitualmente. Agora podemos dar a definição completa:

> **Digital twin** é uma **simulação que recebe dados do equipamento físico em tempo real**, permitindo:
> - **Espelhar** o estado atual do físico;
> - **Diagnosticar** problemas que estão acontecendo;
> - **Prever** falhas futuras;
> - **Otimizar** parâmetros operacionais.

O digital twin é o **filho** da simulação com a IIoT. Sem IIoT, é só simulação (estática). Sem simulação, é só dashboard (não consegue prever).

### A pirâmide do digital twin

Existem **três níveis** de maturidade do digital twin:

1. **Digital twin de produto** — modelo digital de **uma peça** (uma turbina, um motor, uma cadeira de avião).
2. **Digital twin de sistema** — modelo digital de **um conjunto** (uma linha de produção, um andar de hospital).
3. **Digital twin de processo** — modelo digital de **toda a operação** (uma fábrica inteira, uma cidade inteligente).

Empresas como **Siemens** e **Dassault Systèmes** vendem plataformas completas para construir digital twins nos três níveis.

### Exemplo numérico: manufatura aditiva vs convencional

Suponha que você precise produzir **20 peças prototípicas** de uma nova carcaça plástica:

| Modelo | Custo unitário | Tempo total |
| --- | --- | --- |
| Convencional (molde de injeção) | R\$ 800 (rateio de R\$ 15.000 de ferramentaria) | 4 semanas |
| Aditiva (impressora SLA) | R\$ 80 (matéria + máquina) | 3 dias |
| Economia | **10× mais barato** | **9× mais rápido** |

Para lote pequeno, aditiva ganha. Para lote grande (~10.000 peças), o molde de injeção volta a ser muito mais barato por unidade. **A escolha depende do volume.**

### Caso brasileiro: a Embraer e o digital twin de linha

A **Embraer**, em São José dos Campos (SP), implementou um digital twin de sua linha de montagem de aeronaves. O sistema simula impacto de qualquer mudança — mover uma estação, trocar um fluxo, adicionar um equipamento — **antes** de qualquer obra física. Resultado: economia de **mais de R\$ 10 milhões** em uma única reformulação de linha, evitando erros que seriam descobertos só durante a obra.

### Atividade prática

Pense em um **processo produtivo** que você conhece:

1. Que **peça ou componente** seria interessante imprimir em 3D? Por quê?
2. Que **sistema** (linha, máquina, processo) se beneficiaria de um digital twin?
3. Que **dados** seriam necessários para alimentar esse digital twin?
4. Que **decisões** poderiam ser tomadas a partir dele?

### Pontos-chave

- **Manufatura aditiva** constrói peças camada a camada, viabilizando geometrias e lotes que a manufatura tradicional não atende bem.
- Tecnologias variam por material: **FDM, SLA, SLS, DMLS, Binder Jetting**.
- **Simulação** permite **falhar virtualmente** — testar projetos sem custo de protótipo físico.
- **Digital twin = simulação + IIoT em tempo real**, com três níveis (produto, sistema, processo).
- A escolha entre aditiva e convencional depende **fundamentalmente do volume** e da complexidade.

### Para saber mais

- **Gibson, I.; Rosen, D.; Stucker, B.** *Additive Manufacturing Technologies*. Springer.
- **Senai Lab Fabricação Digital:** https://www.sp.senai.br/
- **Vídeo (Real Engineering, YouTube):** "How 3D printing is changing aerospace"
- **Site Siemens Digital Twin:** https://www.plm.automation.siemens.com/global/en/our-story/glossary/digital-twin/24465

---

## Aula 9 — Roteiro da Videoaula 9: "Imprimir uma peça em metal e simular a linha inteira — bem-vindo à fábrica do futuro"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Imagina conseguir imprimir uma peça de motor de avião em titânio. Imagina simular uma fábrica inteira sem mover um parafuso. Isso não é coisa de filme — é o que a gente vai ver hoje na prática."

### 2. Manufatura aditiva (0:40 – 4:00)

- Diferença aditiva vs subtrativa (sempre repetir essa metáfora).
- Tipos principais: FDM, SLA, SLS, DMLS.
- Quando faz sentido (lote pequeno, complexidade, sob demanda).

### 3. Simulação industrial (4:00 – 6:30)

- "Falhar virtualmente" é o conceito-chave.
- Tipos: FEM, CFD, simulação de processos.
- Custo evitado vs custo de retrabalho.

### 4. Digital twin (6:30 – 9:00)

- Definição: simulação + IIoT em tempo real.
- Três níveis: produto, sistema, processo.
- Caso Embraer (10 milhões economizados).

### 5. Encerramento (9:00 – 11:00)

> "Próxima aula a gente entra em outra fronteira: **robótica colaborativa**. Os cobots — robôs que trabalham **ao lado** do humano, não no lugar dele. Te espero!"

---

## Aula 10 — Robótica colaborativa e automação avançada

Se você imagina robô industrial como aquele braço enorme atrás de uma grade, isolado dos humanos, esta aula vai mudar sua cabeça. A nova geração de robôs — chamados **cobots** (collaborative robots) — foi projetada para **trabalhar lado a lado com o operador**, com segurança garantida por sensores. E isso muda completamente a economia da automação.

### Robô industrial tradicional vs cobot

| Aspecto | Robô tradicional | Cobot |
| --- | --- | --- |
| **Localização** | Atrás de grade, isolado | Lado a lado com humano |
| **Velocidade** | Muito alta (perigoso) | Reduzida quando humano se aproxima |
| **Carga útil** | 50–500 kg | 3–20 kg (típico) |
| **Tempo de programação** | Dias / semanas (técnico especializado) | Horas (operador comum) |
| **Custo típico** | R\$ 300 mil – 1 milhão | R\$ 80–250 mil |
| **Reconfiguração** | Difícil — projeto fixo | Fácil — reposicionável |

O cobot **não substitui** o robô tradicional — eles têm aplicações diferentes. Para soldar carroceria, robô tradicional. Para colocar parafuso ao lado de um operador, cobot.

### As marcas que dominam o mercado

- **Universal Robots (Dinamarca)** — referência em cobots, criou o conceito.
- **FANUC, KUKA, ABB, Yaskawa** — gigantes em robôs industriais com linha cobot crescente.
- **Doosan, Techman, AUBO** — competidores em ascensão.

No Brasil, **Pollux, Astrein** e a **WEG** distribuem essas marcas e prestam serviço de integração.

![Cobot operando em linha de montagem ao lado de operador humano — exemplo de robótica colaborativa industrial](https://commons.wikimedia.org/wiki/Special:FilePath/Cobot.jpg?width=800)

### Como funciona a segurança do cobot

Cobots possuem **três camadas de segurança**:

1. **Limitação de força e torque** — se encostar em alguém, para imediatamente (joelho ou cotovelo não machucam).
2. **Sensores de proximidade** — diminui velocidade quando detecta humano próximo.
3. **Modo "monitorado por velocidade"** — opera rápido quando humano sai da área.

Esses três mecanismos são certificados pela norma **ISO/TS 15066** (Robots and robotic devices — Collaborative robots), que define limites biomecânicos aceitáveis.

### Aplicações típicas de cobots

1. **Pick & place** — pegar peça de uma esteira, colocar em outra.
2. **Inspeção visual** — segurar peça e câmera inspeciona.
3. **Aparafusamento e parafusos** — montagem de produtos eletrônicos, automotivos.
4. **Empacotamento (packaging)** — bens de consumo e alimentação.
5. **Polimento e acabamento** — peças metálicas, plásticas.
6. **Cola e selagem** — automotivo e eletroeletrônico.
7. **Atendimento a CNCs** — alimentar máquina-ferramenta automaticamente.

### Automação avançada além do braço robótico

A robótica é o aspecto mais visível, mas a "automação avançada" da Indústria 4.0 inclui também:

- **AGVs / AMRs** (Veículos Guiados Automaticamente / Robôs Móveis Autônomos) — substituem empilhadeiras humanas em armazéns.
- **Cobotic gripping** — garras adaptativas que se ajustam ao formato da peça.
- **Visão computacional integrada ao robô** — robô vê e decide onde pegar (não precisa de gabarito).
- **Robôs colaborativos com IA** — aprendem com demonstração humana (em vez de programação).

### Exemplo numérico: ROI de um cobot em pick & place

Cenário: aparafusamento manual em uma linha de eletrônicos.

- **Antes:** 1 operador faz 60 unidades/hora. Salário + encargos: R\$ 4.500/mês.
- **Depois:** 1 cobot com operador supervisor (1 supervisor cobre 3 cobots). 100 unidades/hora.
- **Investimento:** R\$ 180.000 (cobot + integração).
- **Economia mensal:** R\$ 4.500 × 2 (3 cobots eliminam 3 operadores; mantém 1 supervisor) = R\$ 13.500/mês por cobot.
- **Payback:** 180.000 / 13.500 ≈ **13 meses**.
- **Ganho de produtividade:** +67% de unidades.

### Caso brasileiro: cobot na Embraco

A **Embraco** (Joinville-SC), fabricante de compressores, instalou cobots da Universal Robots em linha de montagem. Resultado: **40% de ganho** de produtividade na estação onde foram instalados, **zero acidentes** envolvendo o cobot, e tempo de reprogramação para um novo produto reduzido de **3 dias para 4 horas**.

### Cobots e o futuro do trabalho

Há um medo comum: "cobot vai roubar meu emprego". A realidade é mais matizada:

- **Tarefas repetitivas e fisicamente desgastantes** são absorvidas pelo cobot.
- **Tarefas que exigem decisão, criatividade, contexto** permanecem com o humano.
- **Novas funções surgem** — operadores se tornam **integradores e supervisores** de cobot.
- **Postos de produção tradicionais diminuem; postos qualificados aumentam.**

Estudos da OIT mostram que a automação **muda** o emprego mais do que **destrói** — mas exige requalificação contínua.

### Atividade prática

Identifique **três tarefas** do seu dia a dia (no trabalho, estágio ou em uma empresa que conhece) que poderiam ser candidatas a cobot:

1. Que **gesto físico repetitivo** é feito?
2. Quanto **tempo por dia** é gasto nessa tarefa?
3. Que **carga** é manipulada (peso, dimensão)?
4. Há **risco de acidente** com humano? Em que grau?
5. Faria sentido um cobot? Por quê?

### Pontos-chave

- **Cobots** trabalham ao lado de humanos, com segurança certificada (ISO/TS 15066).
- Diferem de robôs tradicionais em **carga, velocidade, custo e flexibilidade**.
- Mercado dominado por **Universal Robots, FANUC, KUKA, ABB**.
- 7 aplicações típicas — pick & place, inspeção, parafuso, empacotamento, polimento, cola, atendimento a CNCs.
- Automação avançada vai além do braço — inclui **AGVs/AMRs, visão computacional, robôs com IA**.
- Cobots **mudam** o emprego industrial — não simplesmente o destroem.

### Para saber mais

- **Universal Robots:** https://www.universal-robots.com/pt/
- **Senai Indústria 4.0:** https://www.sp.senai.br/cobot
- **Vídeo (UR no YouTube):** "Como funciona um cobot"
- **Norma ISO/TS 15066:** disponível em https://www.iso.org/

---

## Aula 10 — Roteiro da Videoaula 10: "Cobots: o robô que trabalha do seu lado"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Esquece aquele robô gigante atrás da grade. Hoje a gente vai conhecer os cobots — robôs colaborativos, que trabalham **ao seu lado**, com segurança. E que estão tomando conta do chão de fábrica de um jeito que ninguém previa."

### 2. Robô tradicional vs cobot (0:40 – 3:30)

- Mostrar a tabela comparativa.
- Reforçar: cobot **não substitui** robô tradicional — atendem casos diferentes.

### 3. Segurança do cobot (3:30 – 5:30)

- Três camadas: limitação de força, sensores de proximidade, modo monitorado.
- Norma ISO/TS 15066.

### 4. Aplicações + caso brasileiro (5:30 – 8:30)

- Listar as 7 aplicações com exemplo curto.
- Caso Embraco: +40% produtividade, zero acidentes, reprogramação 3 dias → 4h.

### 5. Encerramento + gancho (8:30 – 11:00)

> "Próxima aula: como o operador da fábrica está usando **realidade aumentada e virtual** para treinar, montar e fazer manutenção em equipamentos complexos. Te espero!"

---

## Aula 11 — Realidade Aumentada e Virtual na manufatura

> **Pausa para reflexão:** você já usou Google Maps com aquele "modo de realidade aumentada" que mostra setas flutuando na rua à sua frente? Se sim, você já experimentou no pequeno o que a indústria está adotando no grande. Pense nisso enquanto avançamos.

A **Realidade Aumentada (RA)** e a **Realidade Virtual (VR)** deixaram de ser brinquedo de videogame e viraram ferramentas reais de fábrica. Esta aula mostra como — e por que — engenheiros de produção devem entender essas tecnologias.

### RA vs VR: a diferença em uma frase

- **Realidade Aumentada (RA / AR):** sobrepõe **informação digital** ao mundo real, vista por óculos, tablet ou celular. **Você continua vendo o mundo real**, mas com dados extras flutuando nele.
- **Realidade Virtual (VR):** **substitui** o mundo real por um ambiente totalmente digital, vista por óculos imersivos. **Você está dentro de outro lugar**, virtualmente.

Pense assim: RA é uma camada por cima da realidade; VR é uma realidade nova.

### Mixed Reality (MR) — o meio do caminho

Existe ainda a **Realidade Mista (MR)**, que sobrepõe objetos digitais que se comportam como reais (você pode "pegar", "girar", "encaixar"). Os óculos **Microsoft HoloLens** e **Apple Vision Pro** são exemplos.

Para nossos fins industriais, RA e MR são tratadas juntas — interessam pela mesma razão (assistir o operador na fábrica).

![Óculos inteligentes de realidade aumentada — categoria de dispositivos usados na indústria para montagem assistida e manutenção remota (HoloLens, Google Glass, RealWear)](https://commons.wikimedia.org/wiki/Special:FilePath/Google_Glass_Front.jpg?width=800)

### Aplicações industriais

#### Realidade Aumentada (RA)

1. **Assistência à montagem** — óculos mostram setas, instruções e parafusos certos. Boeing reduziu erros de montagem em 90% com RA em cabeamento de aviões.
2. **Manutenção remota** — técnico júnior na fábrica + sênior remoto via RA. O sênior vê o que o júnior vê e desenha indicações na tela.
3. **Inspeção de qualidade** — operador olha a peça e a RA destaca pontos suspeitos automaticamente.
4. **Picking em armazém** — óculos mostram qual prateleira, qual quantidade, qual destino.
5. **Treinamento on-the-job** — RA orienta novato em tempo real, com avaliação automática.

#### Realidade Virtual (VR)

1. **Treinamento de operadores** — simular sala de controle de usina, cabine de guindaste, linha de produção — antes de exposição real.
2. **Simulação de processos perigosos** — soldagem, química, alta tensão.
3. **Reuniões de projeto** — equipes globais "entram" num protótipo 3D da fábrica antes de construir.
4. **Treinamento de emergência** — incêndio, evacuação, vazamento.

### Dispositivos e plataformas

- **Microsoft HoloLens 2** — referência industrial, ~U\$ 3.500.
- **Magic Leap 2** — concorrente, focado em uso médico e industrial.
- **Meta Quest 3** — mais barato, ~U\$ 500, para VR/AR misto.
- **Smartphones e tablets** — RA acessível via apps (Vuforia, ARKit, ARCore).

A indústria usa, na maior parte, **HoloLens** e **smartphones**. Custo importa: óculos premium para tarefas críticas; tablet para tarefas comuns.

### Exemplo numérico: economia em treinamento com VR

Uma siderúrgica treina **100 operadores/ano** em operação de pontes rolantes. Treinamento tradicional:

- 80 horas/operador em sala teórica + 40h supervisionada na ponte real.
- Custo: instrutor + ponte parada para treinamento + risco de acidente = **R\$ 12.000/operador**.

Com VR:

- 60 horas em simulador VR + 20h supervisionada na ponte real.
- Custo: licença simulador + amortização + supervisão = **R\$ 4.500/operador**.
- **Economia:** R\$ 7.500/operador.
- **Anual (100 operadores):** R\$ 750.000.

Não é incomum o investimento em simulador VR (~R\$ 800 mil) se pagar em **menos de 1 ano**.

### Caso brasileiro: VR no treinamento da Petrobras

A **Petrobras** opera plataformas offshore — ambiente caro, perigoso, de difícil acesso. Implementou simuladores VR para treinar operadores em procedimentos críticos: parada de emergência, combate a vazamento, evacuação. Resultado: **redução de 40% no tempo de qualificação** e **simulações de cenários** que seriam impossíveis na plataforma real (não dá pra simular um vazamento de gás de verdade).

### Limitações e desafios

Nem tudo é maravilha. RA/VR industrial enfrenta:

- **Conforto** — óculos pesados causam fadiga em uso prolongado.
- **Latência** — quaisquer milissegundos a mais geram náusea (cybersickness).
- **Custo de conteúdo** — produzir conteúdo VR de qualidade custa caro.
- **Aceitação** — operadores experientes costumam resistir a tecnologia nova.
- **Cibersegurança** — óculos conectados são novos vetores de ataque.

Por isso, RA/VR é hoje **complementar**, não substituto, do treinamento e da operação tradicionais.

### Atividade prática

Pegue um **processo da empresa que você conhece** que envolva treinamento ou montagem:

1. RA ou VR faria sentido? Qual dos dois?
2. Que **tarefa específica** seria assistida?
3. Que **informação digital** deveria aparecer (setas, números, alertas)?
4. Qual seria o **ganho esperado** (tempo, segurança, qualidade)?

### Pontos-chave

- **RA** sobrepõe digital ao real; **VR** substitui o real; **MR** combina os dois.
- **5 aplicações de RA**: montagem assistida, manutenção remota, inspeção, picking, treinamento.
- **4 aplicações de VR**: treinamento, simulação de risco, reuniões 3D, emergência.
- O **conforto, latência e custo de conteúdo** ainda são limitações reais.
- ROI em **treinamento** tende a ser o mais rápido (caso Petrobras, siderúrgicas).

### Para saber mais

- **Boeing — AR Wiring:** https://www.boeing.com/innovation/augmented-reality.page
- **Microsoft HoloLens 2 Industrial:** https://www.microsoft.com/en-us/hololens
- **Vídeo (Microsoft, YouTube):** "HoloLens in Manufacturing"
- **Senai-PR Centro de RA/VR:** https://www.sistemafiep.org.br/

---

## Aula 11 — Roteiro da Videoaula 11: "Óculos que ensinam: RA, VR e treinamento da nova geração"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Imagina aprender a operar uma ponte rolante sem nunca ter subido em uma. Imagina montar um motor seguindo setas que aparecem flutuando no ar. Hoje a gente entra no mundo da **realidade aumentada e virtual** aplicada à indústria."

### 2. RA vs VR vs MR (0:40 – 2:30)

- Definir cada um em uma frase + exemplo.
- "Google Maps em modo AR" como gancho cotidiano.

### 3. Aplicações na indústria (2:30 – 6:30)

- 5 de RA (montagem, manutenção remota, inspeção, picking, treinamento).
- 4 de VR (treinamento, risco, reuniões, emergência).
- Caso Boeing: -90% erros em cabeamento.

### 4. ROI e caso brasileiro (6:30 – 9:00)

- Caso siderúrgica: R\$ 7.500/operador economizados.
- Caso Petrobras: -40% tempo de qualificação.

### 5. Encerramento (9:00 – 11:00)

> "Última aula da unidade: nossa fábrica conectada virou um campo de batalha digital. Quem protege tudo isso? É hora de falar de **cibersegurança industrial**. Te espero!"

---

## Aula 12 — Cibersegurança industrial (OT vs IT)

A fábrica conectada da Indústria 4.0 trouxe ganhos enormes. Mas também trouxe um problema sério: ela virou **alvo**. Esta aula é sobre o pilar **menos glamuroso e mais crítico** da 4.0 — a cibersegurança industrial. Sem ela, todos os outros pilares ruem.

### Por que a fábrica virou alvo

Antes de 2010, fábricas eram redes isoladas — sem internet, sem nuvem, sem invasor. Mas:

- A 4.0 conectou tudo à internet.
- Cibercriminosos perceberam que **parar uma fábrica vale milhões** — alvo perfeito para ransomware.
- Estados-nação descobriram que **sabotar indústria inimiga** é arma de guerra.

Resultado: incidentes industriais explodiram.

![Sala de controle de planta industrial OT — ambiente típico exposto a ataques cibernéticos em fábricas conectadas](https://commons.wikimedia.org/wiki/Special:FilePath/Power_plant_control_room.jpg?width=800)

### Casos famosos

| Ano | Alvo | Tipo | Impacto |
| --- | --- | --- | --- |
| 2010 | Centrífugas de urânio (Irã) | Stuxnet (ataque dirigido) | Atrasou programa nuclear iraniano em anos |
| 2017 | Maersk | NotPetya (ransomware) | U\$ 300 milhões em prejuízo |
| 2020 | Honda | Ransomware | Paralisou plantas em vários países |
| 2021 | Colonial Pipeline (EUA) | Ransomware | Cortou abastecimento de combustível na costa leste |
| 2023 | JBS Brasil | Ransomware | Pagou U\$ 11 milhões em resgate |

A pergunta deixou de ser "se" e passou a ser "**quando**". Toda empresa industrial precisa estar preparada.

### OT vs IT: o cerne da questão

A confusão começa porque a fábrica tem **dois mundos** que precisam se conectar mas têm filosofias opostas:

| Aspecto | TI (IT) — escritório | TA (OT) — chão de fábrica |
| --- | --- | --- |
| **Prioridade #1** | Confidencialidade do dado | Disponibilidade do processo |
| **Aceita atualizar agora?** | Sim, com janela de manutenção | Não — parar para atualizar custa $$$ |
| **Vida útil** | 3 a 5 anos | 15 a 30 anos |
| **Sistema operacional** | Atualizado | Frequentemente antigo (XP, Win 7) |
| **Quem opera** | Equipe de TI | Operadores de chão |
| **Reinicializa?** | Sim, sem grande impacto | Não — pode parar produção |

Essa diferença gera tensão: TI quer reiniciar o servidor para aplicar patch; OT diz "se reiniciar, a linha para por 4 horas — custa R\$ 48.000".

A cibersegurança industrial **precisa equilibrar essas filosofias** — proteger sem parar.

### A pirâmide de defesa (modelo Purdue)

O modelo **Purdue Enterprise Reference Architecture** organiza a fábrica em **5 níveis** de rede:

| Nível | Camada | O que tem | Exposição |
| --- | --- | --- | --- |
| 5 | Internet / nuvem | Acesso externo | Alta |
| 4 | TI corporativa | ERP, e-mail, web | Alta |
| 3 | TI de manufatura | MES, historian | Média |
| 2 | Controle de processo | SCADA, HMI | Média |
| 1 | Controle de equipamentos | CLP, DCS | Baixa |
| 0 | Equipamentos | Sensores, atuadores | Mínima |

A defesa funciona por **segmentação**: cada nível só conversa com o adjacente, com **firewalls** ou **diodos** (dispositivos que só deixam dados passarem em **uma direção**) controlando o tráfego. Internet **nunca** fala diretamente com CLP — passa por todas as camadas no caminho.

### As 5 ações fundamentais de cibersegurança industrial

1. **Inventário de ativos** — você não protege o que não sabe que existe. Mapear cada CLP, IHM, switch, sensor.
2. **Segmentação de rede** — separar OT de IT, separar áreas críticas das comuns.
3. **Patch management responsável** — atualizar quando possível, com janela planejada e validação.
4. **Detecção de anomalias** — IDS/IPS industrial que reconhece tráfego estranho (ex.: CLP "falando" com IP externo desconhecido).
5. **Plano de resposta a incidentes** — quem faz o quê em caso de ataque, em quanto tempo, como comunicar.

Normas de referência: **IEC 62443** (mais usada em OT), **NIST SP 800-82**, **NIST Cybersecurity Framework**.

### Exemplo numérico: custo de um ataque

Cenário hipotético — fábrica de autopeças atingida por ransomware:

- **Paralisação:** 5 dias.
- **Receita perdida:** R\$ 800.000/dia × 5 = **R\$ 4 milhões**.
- **Resgate pago (não recomendado):** U\$ 250.000 ≈ R\$ 1,25 milhão.
- **Custos de resposta:** consultoria forense, advogados, comunicação = R\$ 600.000.
- **Multa LGPD (vazamento associado):** até R\$ 50 milhões.
- **Reputação:** difícil de mensurar — clientes podem migrar.

Total realista: **acima de R\$ 5 milhões** em incidente médio, sem considerar dano de longo prazo.

Compare com o investimento em segurança industrial robusta: R\$ 500 mil a R\$ 2 milhões para empresa média. **Prevenção é dezenas de vezes mais barata que reação.**

### Caso brasileiro: a JBS

Em maio de 2021, a **JBS** sofreu ataque de ransomware que afetou plantas no Brasil, EUA e Austrália. Conseguiu retomar operações em poucos dias, mas optou por **pagar U\$ 11 milhões** em resgate. Esse caso virou estudo obrigatório: mostrou que mesmo gigantes da indústria brasileira são alvos e que **plano de continuidade** é tão importante quanto prevenção.

### O futuro: cibersegurança como pré-requisito

Hoje, grandes contratos industriais já **exigem certificação IEC 62443** do fornecedor. Em alguns setores (energia, saúde, financeiro), há **regulamentação** específica. Tendência: cibersegurança vai virar **pré-requisito de mercado**, não diferencial.

### Atividade prática

Para a empresa que você vem analisando ao longo da disciplina:

1. Ela tem **inventário** de seus ativos de OT? Quanto cobre?
2. Há **segmentação** entre TI e OT? Como?
3. Existe **plano** de resposta a incidente? Quem é responsável?
4. Em escala 1–5, quão preparada está para um ransomware?
5. Que **uma ação** de baixo custo geraria mais impacto na próxima semana?

### O que você verá na próxima unidade

Na **Unidade 4**, fechamos a disciplina com a parte **mais aplicada**: como **mapear e digitalizar** processos existentes (BPM + I4.0, Aula 13), como construir um **roadmap realista** de transformação (Aula 14), o que aprender com **casos reais brasileiros e mundiais** (Aula 15) e para onde aponta a **Indústria 5.0** (Aula 16) — fechando seu repertório como engenheiro(a) de produção formado(a) nesse novo paradigma.

### Pontos-chave

- A fábrica conectada virou **alvo** — incidentes industriais explodiram desde 2010.
- A tensão **OT vs IT** é o cerne do problema — prioridades diferentes, vida útil diferente.
- O **modelo Purdue** organiza a defesa em **5 camadas**, com segmentação por firewall/diodo.
- 5 ações fundamentais: **inventário, segmentação, patch, detecção, plano de resposta**.
- Norma principal: **IEC 62443**.
- **Prevenção é dezenas de vezes mais barata que reação.**

### Para saber mais

- **Norma IEC 62443:** https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series
- **NIST Cybersecurity Framework:** https://www.nist.gov/cyberframework
- **Vídeo (TI Inside, YouTube):** "Cibersegurança industrial — o que você precisa saber"
- **Relatório CNI sobre segurança industrial:** https://www.portaldaindustria.com.br/

---

## Aula 12 — Roteiro da Videoaula 12: "OT vs IT: a fábrica conectada virou alvo"

**Duração:** 9 a 11 minutos.

### 1. Abertura (0:00 – 0:40)

> "Em 2021, a JBS pagou U\$ 11 milhões em resgate para hackers. Em 2017, a Maersk perdeu U\$ 300 milhões em um único ataque. A fábrica conectada virou campo de batalha. Hoje a gente entende por quê — e como defender."

### 2. Por que indústria virou alvo (0:40 – 2:30)

- Antes era isolada; hoje conectada.
- Casos famosos rápidos (Stuxnet, Maersk, Honda, Colonial, JBS).

### 3. OT vs IT (2:30 – 5:30)

- Tabela comparativa.
- Reforçar a tensão: TI quer atualizar; OT diz "não, vai parar a linha".

### 4. Modelo Purdue + 5 ações (5:30 – 8:30)

- Pirâmide de 5 níveis (animação simples).
- 5 ações fundamentais.
- Norma IEC 62443.

### 5. Encerramento (8:30 – 11:00)

> "Próxima unidade a gente sai da teoria e entra no campo. Como **transformar** uma fábrica real em 4.0, com roadmap, casos brasileiros, e olhada no que vem depois — a Indústria 5.0. Te espero!"

---

## Quiz não avaliativo

### Questão 1

A diferença fundamental entre **manufatura aditiva** e **manufatura subtrativa** é:

- [ ] a. Manufatura aditiva só funciona para peças plásticas; subtrativa, para metais.
- [ ] b. Manufatura aditiva é sempre mais barata, independentemente do volume produzido.
- [ ] c. Manufatura subtrativa é mais lenta que aditiva em qualquer cenário.
- [x] d. Manufatura aditiva constrói peças **camada por camada** adicionando material; subtrativa parte de um bloco e remove material. A escolha entre ambas depende fundamentalmente do volume, da geometria e do material.

**Resposta correta:** `d`

**Feedback:** A definição correta é a (d). A escolha entre aditiva e subtrativa **não é absoluta** — depende de volume (aditiva ganha em lotes pequenos; subtrativa, em produção em massa), geometria (aditiva permite formas impossíveis para subtrativa) e material (DMLS e SLM imprimem metal funcional). A (a) é falsa: aditiva imprime metais (DMLS, SLM). A (b) e (c) são generalizações incorretas — a comparação depende do contexto.

### Questão 2

Sobre o **modelo Purdue** de arquitetura de segurança industrial, assinale a alternativa **correta**:

- [ ] a. O modelo Purdue defende que todos os equipamentos industriais devem estar diretamente conectados à internet pública para máxima eficiência.
- [ ] b. O modelo Purdue elimina a necessidade de firewalls entre OT e IT.
- [ ] c. O modelo Purdue tem 2 níveis: corporativo e operacional.
- [x] d. O modelo Purdue organiza a fábrica em camadas hierárquicas (do equipamento físico até a internet) com segmentação por firewalls e diodos entre níveis, de modo que a internet nunca fale diretamente com CLPs ou sensores.

**Resposta correta:** `d`

**Feedback:** A (d) descreve corretamente o modelo. A estratégia é **defesa em profundidade** — várias camadas, cada uma só conversa com a adjacente, dificultando muito o caminho de um invasor da internet até equipamentos críticos. A (a) é o oposto do que o modelo recomenda. A (b) é falsa: firewalls são parte essencial. A (c) é falsa: o modelo tem **5 níveis** (0 a 5 ou 1 a 5, dependendo da versão).

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Considere uma fábrica brasileira de **médio porte** (300 a 800 funcionários) que decidiu investir em transformação digital. A diretoria pediu sua opinião sobre **qual das quatro aplicações** vistas nesta unidade (manufatura aditiva / digital twin / robótica colaborativa / RA-VR / cibersegurança) deveria ser **prioridade** no primeiro ano.
>
> Elabore uma resposta dissertativa estruturada em três partes:
>
> 1. **Recomendação** — qual aplicação você prioriza? Justifique tecnicamente.
> 2. **Plano de implementação** — descreva os passos do primeiro ano em 4-6 etapas, com estimativa de investimento e prazo realistas.
> 3. **Riscos e mitigações** — quais os 3 principais riscos do seu plano? Como mitigaria cada um?
>
> **Importante:** a "resposta correta" não existe — qualquer das aplicações pode ser defensável dependendo do contexto. O que vamos avaliar é a **consistência do raciocínio**.

**Resposta esperada:**

> Resposta exemplar começa por **estabelecer o contexto** da fábrica imaginada (setor, produto, dores principais) — sem isso, qualquer recomendação fica abstrata. A recomendação deve ser **coerente** com o porte (investimento entre R\$ 200 mil e R\$ 1 milhão é realista para o primeiro ano) e com o setor (ex.: cibersegurança em fábrica que sofreu ataque recente; cobots em montagem com tarefas repetitivas e seguras; digital twin em planta com muitos sensores já instalados). O plano deve ter etapas claras (diagnóstico → piloto → escala) e prazos (piloto 3 meses, expansão 6 meses, consolidação 3 meses). Os riscos devem ser **realistas** — não só "falta de capital", mas coisas como resistência cultural, dependência de fornecedor único, dificuldade de medir ROI. A resposta de qualidade demonstra **pensamento sistêmico** (tecnologia + processo + pessoas) e **conhecimento de números reais** (custos, payback, KPIs).

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> Dois títulos da Biblioteca Virtual aprofundam os temas desta unidade. O primeiro fundamenta a **cibersegurança industrial** (capítulo de Segurança da Informação); o segundo conecta a transformação digital à **inteligência artificial** aplicada à produção. Ambos têm linguagem acessível e foco em decisão de engenharia.

**Livro 1 — fundamentos e segurança da informação**

- **Nome do livro:** *Indústria 4.0: Conceitos e Fundamentos* (mesmo livro da Unidade 2)
- **Capítulo:** Segurança da Informação (a partir da p. 122)
- **Autor:** Edson Pinheiro de Lima *et al.*
- **Editora:** Blucher
- **Link de acesso:** Biblioteca Virtual — https://plataforma.bvirtual.com.br/Acervo/Publicacao/164117
- **Aula em que entra:** Aula 12 (Cibersegurança industrial)

**Livro 2 — transformação digital e inteligência artificial**

- **Nome do livro:** *Transformação Digital e Indústria 4.0: Produção e Sociedade*
- **Capítulo:** Capítulo 4 — Inteligência Artificial (a partir da p. 73)
- **Organizadores:** Márcia Terra da Silva, Rodrigo Franco Gonçalves, Sílvia Helena Bonilla e José Benedito Sacomano
- **Editora:** Blucher (1ª ed., 2023)
- **Link de acesso:** Biblioteca Virtual — https://plataforma.bvirtual.com.br/Acervo/Publicacao/230218
- **Aula em que entra:** Aulas 9 a 12

### Para mergulhar no assunto

> Recomendo a série documental **"How It's Made: Industrial Edition"** (Discovery Channel), disponível em trechos no YouTube. Episódios curtos mostram fábricas modernas com cobots, impressoras 3D industriais e digital twins em operação.

- **Link(s):** https://www.youtube.com/results?search_query=how+it%27s+made+industrial
- **Aula em que entra:** Aula 9 ou Aula 10

### Podcast (curadoria, até 45 min)

> O podcast **"Manufatura Avançada"**, produzido por engenheiros brasileiros, tem episódios sobre cada uma das tecnologias da Unidade 3. O episódio recomendado discute cobots na prática, com entrevista de gerente de produção que implementou.

- **Nome do podcast:** Manufatura Avançada
- **Nome do episódio:** "Cobots na linha — como começar"
- **Link:** https://www.youtube.com/@manufaturaavancada
- **Aula em que entra:** Aula 10

### Artigo científico

> Este artigo discute como digital twin está sendo aplicado em fábricas reais com foco em manutenção preditiva, com revisão de 80 casos publicados.

- **Link:** https://doi.org/10.1016/j.jmsy.2020.06.017
- **Aula em que entra:** Aula 9
- **Referência bibliográfica do artigo no formato ABNT:**
  > TAO, Fei *et al*. **Digital twin-driven product design framework**. *Journal of Manufacturing Systems*, v. 58, p. 3-21, jan. 2021.
