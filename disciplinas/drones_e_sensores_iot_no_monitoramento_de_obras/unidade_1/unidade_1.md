# Unidade 1 — Fundamentos, Regulamentação e Planejamento de Voo

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 1 a 4

## Vídeo introdutório + Relação da disciplina com a atuação profissional

Pense na última obra grande por que você passou: um edifício com três subsolos, um viaduto, um loteamento com quilômetros de terraplenagem. Agora pense na pergunta que o engenheiro responsável faz todas as manhãs: **a obra está como deveria estar?** O cronograma está em dia? O prédio vizinho recalcou? Quantos metros cúbicos de aterro foram executados esta semana — e quantos foram medidos? Durante décadas, essas respostas vieram de vistorias a pé, do diário de obra escrito à mão e de levantamentos topográficos feitos de tempos em tempos. Hoje elas podem vir **de um drone que sobrevoa o canteiro em vinte minutos e de sensores que enviam leituras a cada quinze minutos para a nuvem**.

Esta disciplina existe para te preparar para essa transformação, em quatro etapas. Na **Unidade 1 — Fundamentos, Regulamentação e Planejamento de Voo**, você vai entender o que é monitorar uma obra e como se mede o avanço (curva S, valor agregado), conhecer os tipos de drone e os sensores que eles carregam, aprender o que ANAC, DECEA e Anatel exigem e planejar uma missão com segurança. Na **Unidade 2 — Aquisição e Processamento de Imagens**, as fotos viram produto: fotogrametria, GNSS, ortomosaicos, modelos digitais de superfície, nuvens de pontos e cálculo de volumes, comparando o projetado com o executado. Na **Unidade 3 — Sensores IoT e Redes de Comunicação**, o foco desce para dentro do solo e da estrutura: inclinômetros, extensômetros, acelerômetros, sensores ambientais, plataformas como o ESP32, redes LoRaWAN e celulares, MQTT e séries temporais. Na **Unidade 4 — Painéis, Integração com BIM e Gestão de Riscos**, tudo se junta: painéis e alarmes, BIM e planejamento, segurança do trabalho com a NR-18 e a proteção de dados com a LGPD.

O diferencial de mercado é concreto. Construtoras, gerenciadoras, concessionárias de infraestrutura, mineradoras e empresas de instrumentação procuram engenheiros que saibam **especificar** um plano de monitoramento, **interpretar** os dados com senso crítico e **transformar** leitura em decisão. Poucos profissionais dominam a combinação de engenharia civil, controle de obras, regulamentação aeronáutica e conectividade — e é exatamente essa combinação que você vai construir aqui.

Ao final, você será capaz de planejar e executar o monitoramento de uma obra real com drones e sensores IoT: o que medir, com qual equipamento, com que frequência, dentro de quais regras e com qual resposta prevista quando o dado indicar um problema.

### Roteiro do vídeo introdutório (até 2 min)

*Acompanha o deck `slides/aula0.html`. Cada bloco indica a tela correspondente.*

**Abertura (0:00 – 0:20):**
[TELA: Slide 1 — capa; Slide 2 — audiodescrição; Slide 3 — Sobre o professor]
> "Olá! Eu sou o professor Afonso Brandão. Para quem usa audiodescrição: sou um homem de pele clara, com cabelos castanho-escuros curtos e barba cheia, também escura e bem aparada; tenho olhos castanhos e sobrancelhas grossas, e apareço em plano médio, de frente para a câmera. Seja muito bem-vindo(a) a Drones e Sensores IoT no Monitoramento de Obras."

**Conexão com o mercado (0:20 – 0:50):**
[TELA: Slide 4 — sumário; Slide 5 — foto aérea do canteiro; Slide 6 — canteiro conectado em 3D]
> "Toda obra tem a mesma pergunta diária: está tudo sob controle? O cronograma está em dia? O talude está se movendo? Quanto de terra já movimentamos? Hoje, um drone registra o canteiro inteiro em um voo, e sensores conversam com a nuvem dia e noite. Construtoras, concessionárias e empresas de instrumentação precisam de engenheiros que saibam usar esses dados para decidir."

**Conteúdo e diferencial (0:50 – 1:25):**
[TELA: Slide 7 — o que vamos monitorar; Slide 8 — do diário de obra ao canteiro conectado; Slide 9 — gêmeo digital em 3D; Slide 10 — 16 videoaulas em 4 unidades]
> "São quatro unidades. Primeiro, os fundamentos: indicadores de avanço da obra, tipos de drone e sensores, as regras de ANAC, DECEA e Anatel e o planejamento de um voo seguro. Depois, as imagens: fotogrametria, GNSS, ortomosaicos, nuvens de pontos e volumes. Em seguida, os sensores IoT e as redes que levam o dado do canteiro à nuvem. E, para fechar, painéis de alerta, integração com BIM, segurança do trabalho e proteção de dados."

**Benefício para o aluno (1:25 – 1:45):**
[TELA: Slide 11 — onde isso aparece na sua carreira; Slide 12 — como você será avaliado]
> "Ao final, você consegue **planejar** o monitoramento, **interpretar** os dados com senso crítico e **decidir** com base neles. Nas avaliações, a pergunta será sempre a mesma: o que o engenheiro deve fazer com esse dado?"

**Encerramento (1:45 – 2:00):**
[TELA: Slide 13 — encerramento]
> "Bora começar? A obra do futuro já está conectada e precisa de engenheiros que saibam ler o que ela está dizendo. Te espero na Aula 1!"

---

## Aula 1 — Monitoramento de obras e indicadores de controle de avanço

> Reunião mensal com o cliente. O cronograma diz que a obra deveria estar com 37,5% executados. O mestre de obras acha que "está mais ou menos em dia". O financeiro informa que já foram gastos 1,45 milhão de reais. E o cliente pergunta, olhando para você: **"Afinal, estamos atrasados? Estamos gastando mais do que deveríamos?"** Sem medição confiável do que foi executado, ninguém consegue responder. Nesta aula, você vai entender **por que e como se monitora uma obra**, como medir o **avanço físico** e como dois índices simples — o **IDP** e o **IDC** — transformam medição em diagnóstico de prazo e custo.

### O que você verá nesta unidade

A Unidade 1 constrói a base de tudo o que vem depois. Na **Aula 1**, você vai entender o que é monitorar uma obra e como se controla o avanço com a **curva S** e o **valor agregado**. Na **Aula 2**, vai conhecer os **tipos de drone** (multirrotor, asa fixa e VTOL), seus componentes e os **sensores embarcados**: câmera RGB, multiespectral, térmica e LiDAR. Na **Aula 3**, vai estudar a **regulamentação brasileira** — ANAC, DECEA e Anatel —, que define quando, onde e como se pode voar. E, na **Aula 4**, vai **planejar uma missão** completa: parâmetros de voo, aplicativos como o DJI Pilot e o Pix4Dcapture, condições meteorológicas e procedimentos de segurança.

### Por que monitorar uma obra?

Monitorar é **medir de forma sistemática, ao longo do tempo, grandezas que indicam se a obra está se comportando como o projeto e o planejamento previram**. As razões se agrupam em quatro dimensões clássicas da gestão:

- **Prazo** — avanço físico real comparado ao cronograma (volumes escavados, pavimentos concretados, área de fachada executada).
- **Custo** — medição de serviços para pagamento, controle de perdas e de retrabalho.
- **Segurança** — de pessoas (quedas, interferência de equipamentos) e de estruturas (recalques, deslocamentos de contenções, nível d'água em escavações).
- **Qualidade** — conformidade geométrica (prumo, nível, espessuras) e desempenho dos materiais.

Monitorar não é luxo: é a forma de transformar **incerteza** — o solo nunca é exatamente o da sondagem, a produtividade nunca é exatamente a do orçamento — em **informação de obra**.

### Do diário de obra ao canteiro conectado

O monitoramento tradicional se apoia no **diário de obra**, em vistorias visuais, em fotos de celular e em campanhas periódicas de topografia. Funciona, mas tem três fragilidades: **baixa frequência** (a medição é mensal), **atraso** (o dado leva dias para virar relatório) e **subjetividade** (cada vistoriador descreve do seu jeito).

![Vista aérea, feita por drone, do canteiro de obras do Pronto-Socorro Central de Itapevi (SP): terreno cercado por tapume, com contêineres e materiais, ao lado do prédio existente, de ruas e do bairro. Foto: Prefeitura de Itapevi, Wikimedia Commons, CC BY 2.0](https://upload.wikimedia.org/wikipedia/commons/c/cc/%282019.12.09%29_Obras_PS_Central%2C_Drone_%2849204900632%29.jpg)

No **canteiro conectado**, drones produzem ortofotos e modelos 3D do canteiro inteiro em um único voo, e sensores em contenções e estruturas enviam leituras sozinhos para uma plataforma na nuvem. A frequência sobe, o atraso cai de dias para horas e o dado passa a ser **quantitativo, datado e rastreável** — exatamente o que os indicadores de controle precisam.

### O ciclo do controle: medir, comparar, decidir, agir

Dado sozinho não salva obra nenhuma. O valor aparece quando o dado percorre um ciclo: **dado** (a leitura bruta: "foram escavados 39.000 m³"), **informação** (o dado comparado a uma referência: "o previsto era 45.000 m³"), **decisão** ("mobilizar mais uma escavadeira na frente norte") e **ação** no canteiro. Em **malha aberta**, a medição vira relatório e ninguém a compara com uma referência a tempo de agir. Em **malha fechada**, a medição **realimenta** a execução: medir → comparar → decidir → agir → **medir de novo** para confirmar o efeito. É o mesmo ciclo **PDCA** (planejar, executar, verificar, agir) que Mattos (2010) coloca no centro do controle de obras. Quando esse laço passa a ser automático e contínuo entre o canteiro e um modelo digital, fala-se em **gêmeo digital** — tema que você retomará na Unidade 4.

### Avanço físico e curva S

O **avanço físico** é a fração da obra efetivamente executada. Como os serviços têm unidades diferentes (m³ de escavação, m de estaca, m² de forma), eles são **ponderados pelo peso de cada serviço no orçamento**:

$
\%AF = \sum_i w_i \cdot p_i \qquad w_i = \frac{C_i}{\sum C_i}
$

onde $p_i$ é a porcentagem executada do serviço $i$ e $w_i$ o seu peso (custo do serviço sobre o custo total).

![Vista aérea das obras do Trecho Norte do Rodoanel Mário Covas, em São Paulo: um viaduto em construção atravessa a mata da serra, com a cidade ao fundo. Foto: Governo do Estado de São Paulo, Wikimedia Commons, CC BY 2.0](https://upload.wikimedia.org/wikipedia/commons/d/d9/Obras_do_Rodoanel_Norte.jpg)

Acumulando o avanço previsto período a período, obtém-se a **curva S**: ela começa suave (mobilização), fica íngreme na fase de produção plena e volta a se achatar no acabamento e na desmobilização. A curva S **física** (em %) ou **físico-financeira** (em reais) é a linha de base; a curva do **realizado**, desenhada sobre ela a cada medição, mostra de imediato se a obra está adiantada ou atrasada.

### Valor agregado: IDP e IDC

A **análise de valor agregado** junta prazo e custo em três grandezas, todas em reais e acumuladas até a data de controle:

- **VP — Valor Planejado:** quanto do orçamento deveria ter sido executado até a data, segundo o cronograma.
- **VA — Valor Agregado:** quanto do orçamento corresponde ao que **foi de fato executado** ($VA = \%AF \cdot ONT$, com ONT o orçamento no término).
- **CR — Custo Real:** quanto efetivamente se gastou para executar o que foi executado.

Com elas, os índices:

$
IDP = \frac{VA}{VP} \qquad IDC = \frac{VA}{CR} \qquad ENT \approx \frac{ONT}{IDC}
$

**IDP < 1** indica atraso; **IDC < 1** indica que se gasta mais do que se agrega. A **ENT** (estimativa no término) projeta o custo final caso o desempenho de custo se mantenha. Repare: o VA depende inteiramente da **medição do executado** — e é aí que entram o drone (volumes, áreas, pavimentos) e os sensores.

### O que drones e sensores resolvem — e o que não resolvem

Drones e sensores resolvem **cobertura** (o canteiro inteiro em um voo), **frequência** (medições semanais ou contínuas), **acesso** (fachadas, coberturas e taludes sem expor pessoas) e **rastreabilidade** (dado datado e georreferenciado, útil inclusive em disputas contratuais). Mas **não** resolvem: cronograma mal feito, orçamento sem estrutura analítica, ausência de limites e de responsáveis pela decisão, nem sensor mal instalado.

![Vista aérea, feita por drone, de um centro de eventos em construção em Votuporanga (SP): prédio branco com janelas redondas sobre terreno de terra vermelha terraplenado. Foto: ASCOM Prefeitura de Votuporanga, Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/c/ce/Obras_Centro_de_Eventos_drone_Rodrigo_Pessoa_%286%29_%2850776013991%29.jpg)

A topografia convencional, com estação total e GNSS, continua indispensável: fornece os pontos de controle e valida os produtos aéreos.

![Estação total robótica e prisma topográfico montados em tripés amarelos sobre calçada, prontos para um levantamento em área urbana. Foto: Syced, Wikimedia Commons, CC0](https://upload.wikimedia.org/wikipedia/commons/1/15/Surveying_prism_and_total_station%2C_for_land_surveying%2C_in_Shibuya-ku.jpg)

### Exemplo numérico

Uma obra industrial tem orçamento $ONT = 4.000.000$ reais, distribuído em quatro serviços. Na medição do mês 5, o **drone mediu 39.000 m³** escavados de um total de 60.000 m³ de terraplenagem; os demais avanços vêm da medição de campo. Os valores são **ilustrativos**.

| Serviço | Custo $C_i$ (reais) | Peso $w_i$ | Executado $p_i$ |
| --- | --- | --- | --- |
| Terraplenagem | 1.200.000 | 0,30 | $39.000/60.000 = 65\%$ |
| Contenção | 800.000 | 0,20 | 40% |
| Fundações | 1.000.000 | 0,25 | 20% |
| Estrutura | 1.000.000 | 0,25 | 0% |

$
\%AF = 0{,}30 \times 0{,}65 + 0{,}20 \times 0{,}40 + 0{,}25 \times 0{,}20 + 0{,}25 \times 0 = 0{,}325 = 32{,}5\%
$

$
VA = 0{,}325 \times 4.000.000 = 1.300.000\,\mathrm{reais}
$

O cronograma previa 37,5% ($VP = 1.500.000$ reais) e o custo real é $CR = 1.450.000$ reais:

$
IDP = \frac{1.300.000}{1.500.000} \approx 0{,}87 \qquad IDC = \frac{1.300.000}{1.450.000} \approx 0{,}90 \qquad ENT \approx \frac{4.000.000}{0{,}90} \approx 4{,}46\,\mathrm{milhões\ de\ reais}
$

Resposta ao cliente: a obra está **atrasada** (agregou 87% do previsto) e **acima do custo** (cada real gasto agrega 90 centavos). Mantido o desempenho, o custo final ficaria cerca de 460 mil reais acima do orçamento. Note a sensibilidade: se a medição de volume tivesse erro de 3.000 m³ (5% do total), o avanço da terraplenagem mudaria 5 pontos e o VA, 60 mil reais — por isso a **exatidão do levantamento** (Unidade 2) importa para o controle.

### Atividade prática

Escolha uma obra que você conhece (pode ser uma obra pública noticiada na sua cidade). Em uma folha:

1. Liste **4 serviços principais** e atribua a cada um um custo estimado e um avanço executado.
2. Calcule o **avanço físico ponderado** e o **VA**.
3. Arbitre um VP e um CR plausíveis, calcule o **IDP** e o **IDC** e escreva o diagnóstico em duas frases.
4. Indique quais desses avanços poderiam ser medidos **por drone**, quais **por sensor** e quais exigem **medição convencional**.

### Pontos-chave

- Monitorar é medir sistematicamente, ao longo do tempo, se a obra se comporta como previsto em **prazo, custo, segurança e qualidade**.
- O valor está no ciclo **medir → comparar → decidir → agir → medir de novo** (malha fechada, PDCA); dado arquivado sem comparação é **malha aberta**.
- O **avanço físico** pondera cada serviço pelo seu peso no orçamento; acumulado no tempo, forma a **curva S**.
- **IDP = VA/VP** mede prazo e **IDC = VA/CR** mede custo; valores abaixo de 1 indicam atraso e estouro de custo.
- Drones e sensores tornam a medição do executado **frequente, rastreável e quantitativa**, mas não substituem planejamento, topografia de controle e decisão.

### Para saber mais

- **MATTOS, Aldo Dórea. *Planejamento e controle de obras*. São Paulo: Pini, 2010** (bibliografia básica — capítulos sobre curva S, controle de avanço físico e valor agregado).
- **Wikipedia — Análise de valor agregado:** https://pt.wikipedia.org/wiki/An%C3%A1lise_de_valor_agregado
- **Wikipedia — Earned value management (exemplos de curvas e índices):** https://en.wikipedia.org/wiki/Earned_value_management
- **Wikipedia — Gráfico de Gantt:** https://pt.wikipedia.org/wiki/Gr%C3%A1fico_de_Gantt
- **Wikipedia — Estação total:** https://pt.wikipedia.org/wiki/Esta%C3%A7%C3%A3o_total

## Aula 1 — Roteiro da Videoaula 1: "A obra está atrasada? Como o drone transforma medição em resposta"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e a reunião com o cliente: "Estamos atrasados?".

> "Reunião mensal com o cliente. O cronograma diz 37 e meio por cento. O mestre acha que está mais ou menos em dia. O financeiro diz que já foi 1 milhão e 450 mil. E o cliente pergunta: afinal, estamos atrasados? Estamos gastando demais? Hoje você vai aprender a responder isso com números — e a ver onde o drone entra nessa conta."

### 2. Desenvolvimento — parte 1 (0:30 – 1:10)

**[TELA]** Slides 4–7 — as quatro dimensões, as fragilidades do jeito tradicional, o canteiro conectado e o ciclo medir → agir.

> "Monitorar é medir de forma sistemática, ao longo do tempo, se a obra está se comportando como o previsto: em prazo, custo, segurança e qualidade. O jeito tradicional — diário de obra, vistoria, foto de celular — é lento, pouco frequente e subjetivo. O drone cobre o canteiro inteiro num voo e entrega volumes e áreas medidos. Mas dado sozinho não salva obra: ele precisa ser comparado com uma referência, virar decisão e virar ação. E depois, medir de novo. Isso é malha fechada — é o PDCA do Mattos."

### 3. Desenvolvimento — parte 2 (1:10 – 2:00)

**[TELA]** Slides 8–11 — avanço físico ponderado, curva S previsto × realizado, VP, VA e CR, e os índices IDP e IDC.

> "Como medir o avanço de uma obra com serviços tão diferentes? Pesando cada serviço pelo custo dele no orçamento. Acumulando o previsto no tempo, nasce a curva S: suave no começo, íngreme no meio, suave no fim. E o valor agregado junta prazo e custo: valor planejado, o que deveria estar feito; valor agregado, o que foi feito, em reais do orçamento; custo real, o que se gastou. IDP é VA sobre VP; IDC é VA sobre CR. Abaixo de 1, problema."

### 4. Desenvolvimento — parte 3 (2:00 – 2:50)

**[TELA]** Slides 12–15 — a calculadora do exemplo, a sensibilidade ao erro de volume e a atividade.

> "Vamos à conta. O drone mediu 39 mil metros cúbicos de 60 mil: 65% da terraplenagem. Somando os pesos, o avanço físico dá 32,5%, e o VA, 1,3 milhão. O previsto era 1,5: IDP de 0,87, obra atrasada. Gastou-se 1,45: IDC de 0,90, cada real agrega 90 centavos. Projeção: uns 460 mil acima do orçamento. E repare: um erro de 3 mil metros cúbicos no volume muda o VA em 60 mil reais. A exatidão do drone é dinheiro."

### 5. Encerramento (2:50 – 3:20)

**[TELA]** Slides 16–17 — pontos-chave e encerramento.

> "Hoje você viu por que monitorar, o ciclo do controle, a curva S e o valor agregado. Mas qual drone faz essa medição — e com qual sensor? Uma câmera comum basta, ou eu preciso de térmica, LiDAR, multiespectral? É o assunto da próxima aula. Te espero na Aula 2!"

---

## Aula 2 — Tipos de drones e sensores embarcados

> Dois pedidos chegam no mesmo dia. A gerência quer o volume escavado de um loteamento de 120 ha; o síndico de um condomínio quer saber **onde as placas cerâmicas da fachada estão descolando**, antes que uma caia na calçada. A construtora tem um único drone, pequeno, com câmera comum. Ele serve para os dois? Não. Nesta aula, você vai conhecer **as famílias de drones**, **o que existe dentro deles** e **os sensores embarcados** — e aprender a escolher a combinação certa para cada pergunta da obra.

### Termos: drone, UA, UAS e RPA

"Drone" é o nome popular. A regulamentação fala em **aeronave não tripulada (UA)** e em **sistema de aeronave não tripulada (UAS)** — a aeronave mais a **estação de pilotagem remota** e o **enlace de comando** entre elas. Se o enlace falha, o sistema falha, mesmo com a aeronave perfeita. A literatura técnica usa também **RPA** (*remotely piloted aircraft*). Drone sobre obra, para uma construtora, é uso **profissional** e segue as regras que você verá na Aula 3.

### As três famílias: multirrotor, asa fixa e VTOL

- **Multirrotor** (quadri, hexa ou octocóptero) — decola na vertical, paira e manobra com precisão. Ideal para **inspeção de fachadas e estruturas** e para áreas pequenas; autonomia típica de 20 a 45 minutos, porque ficar parado no ar custa muita energia.
- **Asa fixa** — voa como um avião: a asa gera sustentação e o motor só empurra. Cobre **centenas de hectares** por voo; é a preferida em rodovias, ferrovias e grandes terraplenagens. Precisa de área de pouso e não paira.
- **VTOL** (*vertical take-off and landing*) — decola e pousa na vertical e voa em cruzeiro como asa fixa: grandes áreas sem pista.

![Drone VTOL de asa fixa laranja, do tipo tail-sitter, pousado na vertical sobre gramado de montanha antes de um voo de mapeamento. Foto: Adyasha Dash, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/0/0b/WingtraOne_in_use.jpg)

### Componentes de um drone

- **Estrutura (frame)** — fibra de carbono ou compósitos, leve e rígida.
- **Motores e ESC** — motores elétricos *brushless* acionados por controladores eletrônicos de velocidade, que variam a rotação centenas de vezes por segundo.
- **Controladora de voo** — o "cérebro": estabiliza a aeronave e executa missões automáticas.
- **GNSS e RTK** — o receptor de navegação por satélite posiciona o drone; com **RTK** (correção em tempo real), a posição das fotos chega a centímetros, o que reduz — mas não elimina — os pontos de controle (Unidade 2).
- **IMU e bússola** — acelerômetros, giroscópios e magnetômetro medem atitude e rumo.
- **Bateria LiPo** — alta densidade de energia, mas sensível a temperatura, carga e armazenamento (Aula 4).
- **Gimbal** — suporte estabilizado que mantém o sensor firme e apontado.
- **Rádio** — enlace de comando e de vídeo com a estação de pilotagem remota, homologado pela Anatel.

![Drone multirrotor quadricóptero de uso profissional exposto em feira, com braços em fibra de carbono, trem de pouso e gimbal com câmeras de zoom e térmica sob a fuselagem. Foto: ZLEA, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/5/5c/DJI_M300_Matrice_300_RTK_%28FA39TN4A93%29_%284-12-2024%29.jpg)

### Câmera RGB: a carga útil da fotogrametria

A **câmera RGB** (a câmera "comum") é de longe a mais usada: com ela se faz a **fotogrametria**, que gera ortomosaico, modelo 3D e volumes, além do registro do avanço físico. Três características importam mais que os megapixels: o **tamanho do sensor** (sensores maiores captam mais luz e têm pixels maiores), a **distância focal** (que, com a altura, define o tamanho do pixel no terreno — o GSD da Aula 4) e o **obturador**. Com obturador **mecânico (global)**, o quadro inteiro é exposto ao mesmo tempo; com obturador **eletrônico (rolling shutter)**, as linhas são lidas em sequência e a imagem sai levemente distorcida em movimento.

### Multiespectral e térmica

A **câmera multiespectral** registra bandas estreitas, inclusive o **infravermelho próximo**, com as quais se calculam índices como o **NDVI**, que mostra o vigor da vegetação — útil para verificar se a hidrossemeadura de um talude ou a recuperação de uma área degradada "pegou".

![Mapa NDVI de uma área agrícola gerado com imagens multiespectrais de drone, em cores falsas do roxo ao verde, com escala de 0,28 a 0,60. Imagem: Stoermerjp, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/7/77/DroneMapper_Processed_NDVI_4cm_GSD.png)

A **câmera térmica** (em geral um microbolômetro na faixa de 8 a 14 µm) mede a radiação infravermelha emitida e a converte em **temperatura aparente**, exibida em cores falsas no **termograma**. A conversão depende da **emissividade** do material e da temperatura refletida do entorno: superfícies brilhantes, como metal polido e vidro, refletem calor de outros objetos e "enganam" a câmera. Em obra, o que interessa é a **diferença** de temperatura: revestimento descolado (a camada de ar atrás da placa isola), umidade e infiltração (a evaporação resfria a superfície), pontes térmicas e painéis elétricos aquecidos.

![Termograma de uma torre residencial com varandas de formas onduladas, feito em dia frio: as bordas das lajes das varandas aparecem em amarelo e laranja, indicando perda de calor pelas pontes térmicas, contra o fundo roxo e azul mais frio. Imagem: Jim D'Aloisio, Wikimedia Commons, CC0](https://upload.wikimedia.org/wikipedia/commons/8/8c/Aqua_Tower_thermal_imaging.jpg)

### LiDAR embarcado

O **LiDAR** (*light detection and ranging*) emite pulsos de laser e mede o tempo de ida e volta: $R = c\,\Delta t / 2$. Combinando a distância com a posição (GNSS) e a atitude (IMU) do drone, cada pulso vira um ponto 3D. Numa árvore, parte do pulso volta da copa e parte **do chão, pelas frestas** — os **múltiplos retornos** —, e por isso o LiDAR alcança o terreno sob vegetação, onde a fotogrametria só "vê" as copas. Também mede superfícies sem textura e funciona sem luz. O custo é bem maior; os produtos do LiDAR serão aprofundados na Aula 7.

![Drone quadricóptero cinza pousado sobre cascalho, com um sensor LiDAR cilíndrico e uma unidade de controle montados sob a fuselagem, com vegetação ao fundo. Foto: Jonte, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/f/fa/Drone_with_Lidar.jpg)

### Como escolher a combinação aeronave + sensor

| Pergunta da obra | Aeronave | Sensor |
| --- | --- | --- |
| Volume e avanço de um canteiro urbano | multirrotor | RGB (com RTK ou pontos de controle) |
| Terraplenagem ou rodovia de centenas de hectares | asa fixa ou VTOL | RGB |
| Terreno natural sob mata | multirrotor ou VTOL | LiDAR |
| Descolamento e infiltração em fachada | multirrotor | térmica (+ RGB de zoom) |
| Recuperação vegetal de taludes | multirrotor ou VTOL | multiespectral |

A regra: **a pergunta define o sensor; a geometria da obra define a aeronave**.

### Exemplo numérico

**(a) LiDAR.** Um alvo no solo está a $R = 80\,\mathrm{m}$ do sensor. O tempo de ida e volta do pulso é:

$
\Delta t = \frac{2R}{c} = \frac{2 \times 80}{3 \times 10^8} \approx 5{,}3 \times 10^{-7}\,\mathrm{s} = 533\,\mathrm{ns}
$

Um erro de apenas $1\,\mathrm{ns}$ na medição do tempo corresponde a $c \times 10^{-9} / 2 = 0{,}15\,\mathrm{m}$ de erro na distância: o LiDAR exige eletrônica de altíssima precisão.

**(b) Térmica.** Uma câmera térmica de $640 \times 512$ pixels tem pixel $p = 12\,\mathrm{\mu m}$ e $f = 13\,\mathrm{mm}$. O campo de visão instantâneo de um pixel é:

$
IFOV = \frac{p}{f} = \frac{12 \times 10^{-6}}{13 \times 10^{-3}} \approx 0{,}92\,\mathrm{mrad}
$

A 10 m da fachada, cada pixel cobre $10 \times 0{,}92 \approx 9{,}2\,\mathrm{mm}$; pela regra prática de que um defeito deve ocupar ao menos $3 \times 3$ pixels, o menor defeito confiável tem cerca de **2,8 cm**. A 30 m, cada pixel cobre 2,8 cm e o menor defeito passa a cerca de **8,3 cm**. A distância de voo — que a Aula 3 vai limitar por segurança de terceiros — é também uma decisão de resolução.

### Atividade prática

Escolha duas obras bem diferentes (por exemplo, a reforma de fachada de um edifício e a duplicação de uma rodovia). Para cada uma, defina **a pergunta** que o levantamento deve responder, a **aeronave** e o **sensor**, justificando pela geometria e pelo objetivo. Depois, procure a ficha técnica de um drone comercial e identifique: autonomia, tipo de obturador, tamanho do sensor, presença de RTK e grau de proteção contra água e poeira.

### Pontos-chave

- **Multirrotor** paira e inspeciona; **asa fixa** cobre grandes áreas; **VTOL** une decolagem vertical e eficiência de cruzeiro.
- Componentes essenciais: frame, motores/ESC, controladora, **GNSS/RTK**, IMU, bateria LiPo, gimbal e rádio.
- Sensores embarcados: **RGB** (fotogrametria), **multiespectral** (vegetação), **térmica** (diferenças de temperatura) e **LiDAR** (terreno sob vegetação).
- Na térmica, emissividade e reflexos condicionam a leitura; na RGB, sensor, focal e obturador valem mais que megapixels.
- **A pergunta define o sensor; a geometria da obra define a aeronave.**

### Para saber mais

- **Wikipedia — Veículo aéreo não tripulado:** https://pt.wikipedia.org/wiki/Ve%C3%ADculo_a%C3%A9reo_n%C3%A3o_tripulado
- **Wikipedia — Lidar:** https://pt.wikipedia.org/wiki/Lidar
- **Wikipedia — Termografia:** https://pt.wikipedia.org/wiki/Termografia
- **Wikipedia — Normalized difference vegetation index (NDVI):** https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index

## Aula 2 — Roteiro da Videoaula 2: "Um drone serve para tudo? O sensor certo para cada pergunta da obra"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e os dois pedidos: loteamento de 120 ha e fachada descolando.

> "Dois pedidos no mesmo dia: o volume de um loteamento de 120 hectares e as placas descolando numa fachada. A construtora tem um drone pequeno com câmera comum. Serve para os dois? Não. Hoje você vai conhecer os drones por dentro e, principalmente, os sensores que eles carregam."

### 2. Desenvolvimento — parte 1 (0:25 – 1:15)

**[TELA]** Slides 4–7 — UA, UAS e RPA; as três famílias; o VTOL; o drone em 3D com vista explodida.

> "Drone é o nome popular; a norma fala em aeronave não tripulada e em sistema — porque o enlace de comando faz parte. São três famílias: o multirrotor paira, ótimo para fachada; a asa fixa voa como avião e cobre centenas de hectares; e o VTOL decola na vertical e cruza como asa fixa. Por dentro: frame, motores com ESC, controladora, GNSS — com RTK chega a centímetros —, IMU, bateria LiPo, gimbal e rádio."

### 3. Desenvolvimento — parte 2 (1:15 – 2:20)

**[TELA]** Slides 8–12 — câmera RGB e obturador; NDVI; termograma; LiDAR e múltiplos retornos; a tabela de escolha.

> "Agora, os sensores. A câmera RGB faz a fotogrametria: ortomosaico, modelo 3D e volumes — e aqui vale mais o tamanho do sensor e o obturador do que os megapixels. A multiespectral calcula índices de vegetação, como o NDVI. A térmica mostra diferenças de temperatura: placa descolada, infiltração, painel aquecido — mas cuidado com a emissividade e os reflexos. E o LiDAR mede distância com laser e, pelos múltiplos retornos, enxerga o chão debaixo da mata. A regra: a pergunta define o sensor, a geometria define a aeronave."

### 4. Desenvolvimento — parte 3 (2:20 – 3:00)

**[TELA]** Slides 13–15 — tempo de voo do pulso LiDAR, o pixel térmico na fachada e a atividade.

> "Duas contas. Um alvo a 80 metros devolve o pulso do LiDAR em 533 nanossegundos — e 1 nanossegundo de erro já são 15 centímetros. Na térmica, com pixel de 12 micrômetros e focal de 13 milímetros, a 10 metros cada pixel cobre 9 milímetros, e o menor defeito confiável tem uns 2,8 centímetros. A 30 metros, passa de 8 centímetros. A distância de voo é decisão de engenharia."

### 5. Encerramento (3:00 – 3:25)

**[TELA]** Slides 16–17 — pontos-chave e encerramento.

> "Você já sabe escolher a aeronave e o sensor. Mas pode voar? Quem autoriza, quem cadastra, quem homologa? Na próxima aula, as regras do jogo: ANAC, DECEA e Anatel. Te espero na Aula 3!"

---

## Aula 3 — Regulamentação brasileira de aeronaves não tripuladas: ANAC, DECEA e ANATEL

> A construtora comprou um drone e quer voar o canteiro amanhã cedo. O drone está na caixa, a bateria carregada, o piloto animado. Mas o drone está cadastrado? O piloto está habilitado? Há seguro? O voo foi solicitado ao controle do espaço aéreo? O rádio do equipamento é homologado? E o levantamento que vai gerar o ortomosaico — precisa de autorização do Ministério da Defesa? Nesta aula, você vai conhecer **quem regula o quê** no Brasil e montar o **checklist regulatório** de uma operação em obra.

### Três órgãos, três perguntas

Cada pergunta tem um "dono":

- **A aeronave, o operador e o piloto podem voar?** — **ANAC** (Agência Nacional de Aviação Civil): cadastro, categorias de operação, habilitação, seguro.
- **O espaço aéreo pode ser usado ali, naquela hora?** — **DECEA** (Departamento de Controle do Espaço Aéreo, do Comando da Aeronáutica): solicitação de acesso pelo **SARPAS**.
- **O rádio do equipamento pode transmitir?** — **Anatel**: homologação dos transmissores.

A elas somam-se o **Ministério da Defesa**, quando o voo é **aerolevantamento**, e a **LGPD**, porque imagens de pessoas são dados pessoais.

### ANAC: do RBAC-E nº 94 ao RBAC nº 100

Por quase uma década, a referência foi o **RBAC-E nº 94** da ANAC (2017), citado na bibliografia desta disciplina, que classificava as aeronaves pelo **peso máximo de decolagem**: **Classe 1** (acima de 150 kg), **Classe 2** (acima de 25 kg até 150 kg) e **Classe 3** (até 25 kg). Essas classes ainda aparecem em contratos e editais.

Em **junho de 2026**, a ANAC aprovou o **RBAC nº 100** (Resolução nº 805, de 15/06/2026), que **substituiu o RBAC-E nº 94** e passou a classificar as **operações pelo risco**, e não mais pelo peso — afinal, um drone de 5 kg sobre uma multidão é mais perigoso que um de 20 kg sobre um descampado:

- **Categoria aberta** — peso em voo até 25 kg, em linha de visada visual (VLOS) ou estendida, com apoio de observador (EVLOS), até 120 m (400 pés) acima do solo, em **áreas distantes de terceiros**: em nenhuma hipótese a menos de **30 m horizontais de pessoas não envolvidas e não anuentes**, salvo barreira mecânica capaz de protegê-las. Exige avaliação de risco operacional atualizada (facultativa se a operação estiver a mais de 150 m dessas pessoas ou protegida por barreira).
- **Categoria específica** — quando algum critério da aberta não é atendido (voo além da linha de visada, acima de 120 m, acima de 25 kg etc.); o operador demonstra a segurança por avaliação de risco operacional, por método aceito pela ANAC (como o **SORA**, da JARUS, previsto no art. 4º da Resolução nº 805), ou por cenário padrão definido pela ANAC; conforme a complexidade da operação, obtém o **Cadastro de Operador na categoria específica (COE)** (RBAC nº 100, Subparte F).
- **Categoria certificada** — operações de alto risco, como transporte de artigos perigosos, com certificação da aeronave, do operador e do piloto.

![Piloto remoto de colete refletivo, sobre uma laje, segura o controle de um drone com tela acoplada e observa a aeronave, com telhados de uma cidade ao fundo. Foto: Amuzujoe, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/1/18/Drone_Pilot.jpg)

### ANAC: cadastro, piloto e seguro

Outros requisitos do RBAC nº 100: aeronaves das categorias aberta e específica são **cadastradas no SISANT** (cadastro válido por 24 meses e identificação na aeronave); o piloto remoto deve ser aprovado em **exame de conhecimento teórico da ANAC** (exigível a partir de 1º/01/2027); e as operações devem ter **seguro com cobertura de danos a terceiros** (o seguro conhecido no setor como RETA), com poucas exceções. Drones de **até 250 g**, operando **até 120 m (400 pés) acima do solo e em VLOS ou EVLOS**, ficam **fora** do RBAC nº 100 (§ 100.1(e)), sob as regras simplificadas da Resolução nº 806/2026, mas continuam sujeitos às regras do DECEA. Atos emitidos sob o RBAC-E nº 94 seguem válidos até serem revistos pela ANAC, e as operações autorizadas até 15/06/2026 que não se enquadram na categoria aberta têm **2 anos** para obter nova autorização (Resolução nº 805, art. 2º).

### DECEA: o espaço aéreo tem dono

A ANAC cuida da aeronave e do operador, mas o **espaço aéreo** é do **DECEA**, cuja **ICA 100-40** (Portaria DECEA nº 2.094/DNOR8, de 2026) determina que o acesso seja solicitado pelo sistema **SARPAS**, com antecedência que cresce com o risco da operação — inclusive para os drones de até 250 g. Voos além da linha de visada (**BVLOS**) pedem a solicitação com **8 dias** de antecedência. Proximidade de aeródromos, helipontos, áreas restritas ou proibidas exige análise específica: muitas obras urbanas estão sob rotas de aproximação de aeroportos e heliportos.

![Placa vermelha de zona proibida para drones, com o desenho de um drone riscado, ao lado de um painel informativo, em área natural com rochas avermelhadas e céu azul. Foto: Coconino National Forest, Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/3/35/Sedona_No_Drone_Zone_%2832311452360%29.jpg)

### Aerolevantamento: quando o voo vira mapeamento

Mapear um terreno em **faixas de voo sobrepostas** para gerar ortomosaico, MDT ou planta planialtimétrica é **aerolevantamento** (Decreto nº 2.278/1997; Portaria GM-MD nº 3.703/2021, art. 8º), executado só por entidade **inscrita no Ministério da Defesa**. Projetos pequenos ficam **pré-autorizados**, com dispensa da autorização específica, quando a área não ultrapassa um círculo de raio de 2,2 km ou uma área circular inferior a 15 km², **desde que atendidas condições cumulativas** (entre elas, não tocar áreas ou instalações sujeitas a restrição e não ser levantamento geofísico) (art. 38). A pré-autorização não dispensa a inscrição nem o pedido no SARPAS, com **4 dias corridos** de antecedência (ICA 100-40, art. 57). Foto de inspeção ou vídeo de avanço, sem faixas sobrepostas, **não** é aerolevantamento.

![Foto aérea feita por drone de um viaduto de concreto sobre um vale com vegetação, durante uma inspeção. Foto: FedericaGaspari, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/2/21/Drone_view_of_a_bridge_during_an_inspection.jpg)

### Anatel: homologação dos rádios

O drone transmite: enlace de comando, vídeo e, às vezes, correções RTK por rede celular. Todo transmissor comercializado e usado no Brasil precisa ser **homologado pela Anatel**, que verifica se o equipamento opera nas faixas e potências permitidas (os drones costumam usar as faixas de 2,4 GHz e 5,8 GHz). Na prática: confira o **selo e o código de homologação Anatel** no equipamento ou na embalagem e desconfie de importados "sem selo". A mesma exigência vale para os módulos de rádio dos sensores IoT da Unidade 3 (LoRaWAN, Wi-Fi, celular).

### LGPD e responsabilidade

Imagens que identificam trabalhadores e vizinhos são **dados pessoais** (Lei nº 13.709/2018): defina finalidade, minimize a captura e controle o acesso (Aula 16). O cumprimento das regras é responsabilidade do **operador e do piloto remoto**; voo irregular gera sanções e pode invalidar o seguro.

![Dois operadores com equipamento de proteção preparam um drone VTOL laranja de asa fixa, pousado na vertical sobre o capim seco. Foto: Emily Loosli, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/d/de/WingtraOne_and_operators.jpg)

### Exemplo numérico

Um canteiro urbano retangular mede $80 \times 50\,\mathrm{m}$ ($4.000\,\mathrm{m^2}$). Ao longo do lado de 80 m há uma calçada movimentada; nos outros lados, muros de lotes vazios. A construtora quer voar em **categoria aberta**, sem barreira mecânica, a $60\,\mathrm{m}$ de altura. Valores **ilustrativos**.

Para manter **30 m horizontais** dos pedestres, a área de voo fica limitada à faixa do terreno distante mais de 30 m da calçada:

$
A_{voável} = 80 \times (50 - 30) = 1.600\,\mathrm{m^2}
\qquad
\frac{1.600}{4.000} = 40\%
$

Só 40% do canteiro pode ser sobrevoado diretamente. O mapeamento completo exige outra solução: interdição da calçada autorizada pela prefeitura, barreira capaz de proteger as pessoas ou a **categoria específica**, com avaliação de risco. E, como é um mapeamento em faixas sobrepostas (**aerolevantamento**), o pedido no SARPAS deve sair com **4 dias corridos** de antecedência: para voar na sexta-feira, dia 20, a solicitação deve ser feita até a segunda-feira, dia 16.

### Pausa para reflexão (Desafio)

Quinta-feira, 17h. O gerente do contrato liga: "Preciso do ortomosaico do canteiro amanhã às 9h para a reunião com o cliente. É um voo de 15 minutos, ninguém vai notar". O pedido no SARPAS para aerolevantamento exige 4 dias, a calçada estará cheia de pedestres às 8h e o piloto ainda não fez o exame teórico. O que você faz? Pese o custo de chegar à reunião sem o produto contra o de um acidente com um pedestre, de um seguro que não cobre voo irregular e de uma autuação. **Existe uma alternativa legal que atenda parcialmente ao cliente** — fotos de inspeção sem faixas sobrepostas, dentro da área voável, ou o último ortomosaico regular com a medição de campo da semana? Como você comunicaria isso ao gerente? Segurança em primeiro lugar não é slogan: é uma decisão que o engenheiro toma — e assina.

### Atividade prática

Escolha uma obra da sua cidade e monte o **checklist regulatório** para voar sobre ela: categoria no RBAC nº 100 (verificando os 30 m), SISANT, piloto, seguro, avaliação de risco, SARPAS (com a antecedência), aerolevantamento (sim ou não, e por quê), Anatel e LGPD. Verifique, num mapa, se há aeródromo ou heliponto por perto.

### Pontos-chave

- **ANAC** regula aeronave, operador e piloto; **DECEA** regula o espaço aéreo (ICA 100-40, SARPAS); **Anatel** homologa os rádios.
- O **RBAC nº 100** (2026) substituiu o **RBAC-E nº 94** (2017) e classifica operações por **risco** (aberta, específica, certificada), não mais por classes de peso.
- Categoria aberta: até 25 kg, VLOS/EVLOS, até 120 m e **nunca a menos de 30 m** de pessoas não envolvidas e não anuentes (salvo barreira); SISANT, exame teórico e seguro.
- Mapeamento em faixas sobrepostas é **aerolevantamento**: entidade inscrita no Ministério da Defesa e SARPAS com 4 dias corridos.
- Imagens de pessoas são **dados pessoais** (LGPD); o voo regular é responsabilidade do operador e do piloto.

### Para saber mais

- **AGÊNCIA NACIONAL DE AVIAÇÃO CIVIL (ANAC). *RBAC-E nº 94: requisitos gerais para aeronaves não tripuladas de uso civil*. Brasília: ANAC, 2017** (bibliografia complementar — referência histórica, substituída pelo RBAC nº 100).
- **ANAC — Drones (portal oficial):** https://www.gov.br/anac/pt-br/assuntos/drones
- **ANAC — RBAC nº 100, Emenda 00 (texto integral):** https://pergamum.anac.gov.br/pergamum/vinculos/RBAC100EMD00.pdf
- **DECEA — ICA 100-40 (2026), cópia no portal de Aerolevantamento do Ministério da Defesa:** https://www.gov.br/defesa/pt-br/assuntos/aerolevantamento/arquivos/2026/ica-100-40-publicada-port-2094-dnor8-18-03-2026-bca-058-30-03-2026.pdf
- **Anatel — Certificação e homologação de produtos:** https://www.gov.br/anatel/pt-br/regulado/certificacao-de-produtos

## Aula 3 — Roteiro da Videoaula 3: "Pode voar aqui? O que ANAC, DECEA e Anatel exigem antes da decolagem"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e "Antes de tudo: pode voar?".

> "A construtora comprou um drone e quer voar amanhã cedo. Tira da caixa, carrega a bateria e decola? Não. Cadastro, piloto habilitado, seguro, autorização do espaço aéreo, rádio homologado — e, se for mapeamento, Ministério da Defesa. Hoje você vai aprender quem manda em quê."

### 2. Desenvolvimento — parte 1 (0:25 – 1:30)

**[TELA]** Slides 4–8 — os três órgãos; do RBAC-E 94 ao RBAC 100; as três categorias; a escala dos 120 m e dos 30 m em 3D; SISANT, exame e seguro.

> "Três perguntas, três donos: a ANAC cuida da aeronave, do operador e do piloto; o DECEA, do espaço aéreo; a Anatel, do rádio. Na ANAC, durante anos valeu o RBAC-E 94, com classes por peso. Em junho de 2026, o RBAC 100 substituiu o 94 e passou a olhar o risco. Categoria aberta: até 25 quilos, linha de visada, até 120 metros e nunca a menos de 30 metros de pessoas não envolvidas e não anuentes, salvo barreira. Saiu disso, categoria específica, com avaliação de risco. Risco alto, certificada. E mais: SISANT, exame teórico a partir de 2027 e seguro contra terceiros."

### 3. Desenvolvimento — parte 2 (1:30 – 2:30)

**[TELA]** Slides 9–12 — SARPAS e ICA 100-40; aerolevantamento; selo Anatel; LGPD.

> "O espaço aéreo é do DECEA: pela ICA 100-40, todo voo passa pelo SARPAS — até o de 250 gramas. Além da linha de visada, 8 dias de antecedência. Mapeamento em faixas sobrepostas é aerolevantamento: empresa inscrita no Ministério da Defesa e pedido com 4 dias corridos; foto de inspeção não é. O rádio precisa de homologação da Anatel: procure o selo. E imagem de pessoa é dado pessoal: LGPD."

### 4. Desenvolvimento — parte 3 (2:30 – 3:20)

**[TELA]** Slides 13–15 — o canteiro de 80 × 50 m com a faixa de 30 m; o calendário do SARPAS; a pausa para reflexão.

> "Um canteiro de 80 por 50 metros com calçada movimentada num lado. Mantendo 30 metros dos pedestres, sobra uma faixa de 80 por 20: só 40% do terreno. Para mapear tudo, voo sem pedestres, barreira ou categoria específica. E, para voar na sexta, o pedido sai até segunda. Agora, a reflexão: o gerente quer o ortomosaico amanhã e diz que ninguém vai notar. O que você faz?"

### 5. Encerramento (3:20 – 3:40)

**[TELA]** Slides 16–17 — pontos-chave e encerramento.

> "Você já sabe se pode voar. Falta saber como voar: altura, sobreposição, aplicativo de missão, vento, bateria e checklist. É a próxima aula, que fecha a unidade. Te espero na Aula 4!"

---

## Aula 4 — Planejamento de missão, condições meteorológicas e procedimentos de segurança

> O levantamento do canteiro de 12 ha está autorizado e o pedido no SARPAS foi aceito. Às 7h, o piloto decola com vento "fraco" no chão. A 70 m, o drone luta contra rajadas, gasta bateria na volta contra o vento e pousa com 8% de carga, a 200 m do ponto previsto. Metade das fotos saiu tremida e o modelo tem buracos. Ninguém quebrou regra nenhuma: **faltou planejamento**. Nesta aula, que fecha a Unidade 1, você vai aprender a **planejar a missão**, a **ler o tempo** antes de decolar e a seguir os **procedimentos de segurança** que separam um voo profissional de uma aposta.

### Tipos de missão

O tipo de missão segue o objetivo:

- **Mapeamento em área (grade)** — faixas paralelas, como um cortador de grama, com a câmera apontada para baixo: ortomosaico, modelo de terreno e volumes.
- **Grade dupla e oblíqua** — faixas cruzadas e câmera inclinada: modelos 3D de edificações, com fachadas.
- **Corredor (linear)** — faixas ao longo de um eixo: rodovias, ferrovias, adutoras, linhas de transmissão.
- **Órbita e pontos de passagem (waypoints)** — voo ao redor de uma estrutura ou por pontos definidos: inspeção, registro periódico do avanço do mesmo ângulo.
- **Voo manual** — inspeção de detalhes, sempre com o piloto em linha de visada.

### Os parâmetros do plano: GSD, altura e sobreposição

O **GSD** (*ground sample distance*) é o tamanho, no terreno, de um pixel da imagem:

$
GSD = \frac{H \cdot p}{f}
$

com $H$ a altura **acima do terreno**, $p$ o tamanho do pixel no sensor e $f$ a distância focal. Dobrar a altura dobra o GSD. A largura da faixa imageada é $W = N_x \cdot GSD$ ($N_x$ pixels no sentido transversal ao voo), e o **espaçamento entre faixas** depende da **sobreposição lateral** $s_l$:

$
d = W\,(1 - s_l)
$

Para fotogrametria de obra, usam-se em geral **75–80% de sobreposição frontal e 65–75% lateral** — a razão dessas porcentagens você verá na Aula 5. A área coberta por um voo é aproximadamente $A = v \cdot t_{útil} \cdot d$: velocidade, vezes tempo útil, vezes a largura que se avança a cada passada. Também entram no plano a **velocidade** (que deve manter o arrasto da imagem abaixo de meio pixel), a direção das faixas, a margem além do limite da obra e o ponto de decolagem.

### Aplicativos de missão: DJI Pilot e Pix4Dcapture

Os aplicativos de planejamento transformam esses parâmetros em uma rota automática. No **DJI Pilot** (aplicativo das aeronaves corporativas da DJI), escolhe-se o tipo de missão (mapeamento de área, oblíqua, linear ou waypoints), desenha-se o polígono sobre o mapa e definem-se GSD ou altura, sobreposições, velocidade e ação ao fim da missão. O **Pix4Dcapture** (hoje PIX4Dcapture Pro) faz o mesmo para drones de vários fabricantes, com grades simples, duplas e órbitas, e envia as fotos diretamente ao processamento. Há ainda opções abertas, como o **Mission Planner** e o QGroundControl. Em todos, o aplicativo **calcula** — mas quem responde pelo plano é o engenheiro: conferir altura sobre o terreno, obstáculos (gruas, torres, fios), o polígono autorizado no SARPAS e a **altura de retorno automático (RTH)**.

![Tela do software livre Mission Planner, usado para planejar missões automáticas de drones: à esquerda, o painel de instrumentos com altitude e velocidade; à direita, a imagem de satélite da cidade de São Carlos (SP), onde o plano de voo é desenhado. Imagem: Jesimar da Silva Arantes, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/e/ee/Mission_Planner.png)

### Condições meteorológicas: vento, chuva e visibilidade

O **vento** é o principal limitador. Três cuidados: o vento **aumenta com a altura** — o que se sente no chão subestima o que o drone enfrenta a 70 m; as **rajadas** importam mais que a média; e o voo contra o vento consome mais bateria na volta. Respeite o limite de resistência ao vento do fabricante com folga (uma regra prática é não passar de cerca de dois terços dele). **Chuva e umidade** danificam motores e eletrônica: mesmo aeronaves com grau de proteção IP toleram chuva leve, não temporal. **Visibilidade** e **teto de nuvens** condicionam a linha de visada. Para fotogrametria, prefira sol alto (sombras curtas) ou céu uniformemente nublado; evite manhã cedo e fim de tarde. Consulte **METAR e TAF** dos aeródromos próximos na **REDEMET** (DECEA), a previsão do **INMET** e meça o vento no local com anemômetro.

![Biruta listrada de laranja e branco quase totalmente inflada pelo vento, presa a um mastro metálico, contra céu azul limpo em um aeródromo. Foto: Olaf Oliviero Riemer, Wikimedia Commons, CC BY-SA 3.0](https://upload.wikimedia.org/wikipedia/commons/f/f8/Windsock_Hodenhagen_Aerodrome_2013.jpg)

![Anemômetro digital portátil de hélice, de corpo preto, com visor de cristal líquido e botões de liga/desliga, unidade, máximo/mínimo e média. Foto: Tpdwkouaa, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/7/74/Digital_Handheld_Anemometer.jpg)

### Temperatura, bateria e clima espacial

A bateria **LiPo** entrega menos energia no **frio** (a resistência interna aumenta e a tensão cai sob carga) e se degrada no **calor**: em dias acima de 35 °C, comuns no verão brasileiro, motores, eletrônica e bateria aquecem, e o ar menos denso exige mais potência. Consulte a faixa de operação do fabricante, aqueça as baterias antes do voo em dias frios e reduza o tempo útil planejado. O **clima espacial** também conta: o **índice Kp** (de 0 a 9) mede a atividade geomagnética, e valores a partir de 5 (tempestade geomagnética) podem degradar o GNSS. No Brasil, próximo ao equador magnético, a **cintilação ionosférica** após o pôr do sol, em períodos de alta atividade solar, pode prejudicar o RTK mesmo com Kp baixo.

![Bateria de voo branca de um drone, apoiada sobre uma superfície de madeira. Foto: A.Savin, Wikimedia Commons, FAL](https://upload.wikimedia.org/wikipedia/commons/6/68/DJI_Phantom_4Pro_04-2017_img2_flight_battery.jpg)

### Procedimentos de segurança: antes, durante e depois

- **Antes do voo** — documentos (SISANT, habilitação, seguro, autorização no SARPAS, avaliação de risco); meteorologia e Kp; inspeção da aeronave (hélices, braços, baterias carregadas e equilibradas, firmware); calibração de bússola e IMU quando o aplicativo pedir; **altura de RTH** acima do maior obstáculo; definição da **área de segurança** (decolagem e pouso isolados, sem circulação de pessoas) e briefing com o observador.
- **Durante o voo** — manter linha de visada; monitorar bateria, sinal e GNSS; **reserva de bateria** para retorno com vento contrário; interromper se pessoas não anuentes entrarem na área.
- **Emergências** — perda de enlace (o RTH deve estar configurado e testado); perda de GNSS (o drone passa a modo de atitude e deriva com o vento: assumir manualmente); bateria crítica (pousar no local seguro mais próximo); aeronave tripulada à vista (descer e se afastar — ela tem prioridade).
- **Depois do voo** — registrar o voo (data, local, duração, ocorrências), inspecionar a aeronave, conferir as fotos ainda em campo e armazenar as baterias com **carga de armazenamento**, nunca totalmente cheias por semanas.

### Exemplo numérico

**(a) Altura e faixa.** Uma câmera de 20 MP tem $5.472 \times 3.648$ pixels, pixel $p = 2{,}41\,\mathrm{\mu m}$ e $f = 8{,}8\,\mathrm{mm}$. O contrato pede GSD de no máximo 2 cm:

$
H_{máx} = \frac{GSD \cdot f}{p} = \frac{0{,}02 \times 8{,}8}{0{,}00241} \approx 73\,\mathrm{m}
$

Adotando $H = 70\,\mathrm{m}$: $GSD = 70 \times 0{,}00241 / 8{,}8 \approx 1{,}92\,\mathrm{cm}$, $W \approx 5.472 \times 0{,}0192 \approx 105\,\mathrm{m}$ e, com 70% de sobreposição lateral, $d = 105 \times 0{,}3 \approx 31{,}5\,\mathrm{m}$.

**(b) Cobertura por voo.** Multirrotor com 30 min de autonomia, 70% úteis ($t_{útil} = 1.260\,\mathrm{s}$), a $v = 6\,\mathrm{m/s}$:

$
A = 6 \times 1.260 \times 31{,}5 \approx 238.000\,\mathrm{m^2} \approx 23{,}8\,\mathrm{ha}
$

O canteiro de 12 ha da Aula 1 cabe num voo. Um VTOL a $16\,\mathrm{m/s}$ com 41 min úteis cobriria $16 \times 2.460 \times 31{,}5 \approx 124\,\mathrm{ha}$ — a escolha da Aula 2 para rodovias.

**(c) Vento na altura de voo.** O anemômetro mede $v_{10} = 6\,\mathrm{m/s}$ a 10 m. Pela lei de potência do perfil de vento, com expoente ilustrativo $\alpha = 0{,}2$ (terreno com obstáculos):

$
v_{70} = v_{10} \left(\frac{70}{10}\right)^{\alpha} = 6 \times 7^{0{,}2} \approx 6 \times 1{,}48 \approx 8{,}9\,\mathrm{m/s}
$

Se o fabricante indica resistência ao vento de 12 m/s, o limite prático de dois terços é $8\,\mathrm{m/s}$: **o voo deve ser adiado** (ou feito mais baixo, com GSD melhor e mais faixas). O vento "fraco" do chão era forte na altura de voo — exatamente o que aconteceu no caso do início da aula.

### Atividade prática

Instale um aplicativo de planejamento (DJI Pilot, Pix4Dcapture ou o Mission Planner, que é gratuito) — ou use as fórmulas da aula, se não tiver drone. Para uma obra de sua escolha: desenhe o polígono, defina GSD, altura, sobreposições e velocidade, e anote o número de faixas, de fotos e o tempo de voo. Em seguida, consulte a REDEMET ou o INMET e o índice Kp do dia e escreva a decisão **voa / não voa** com a justificativa. Por fim, redija o seu **checklist pré-voo** em uma página.

### Pontos-chave

- O tipo de missão (grade, oblíqua, corredor, órbita) segue o objetivo do levantamento.
- $GSD = H \cdot p / f$, faixa $W = N_x \cdot GSD$, espaçamento $d = W(1 - s_l)$ e área por voo $A = v \cdot t_{útil} \cdot d$.
- DJI Pilot e Pix4Dcapture calculam a rota, mas **o engenheiro responde pelo plano**: relevo, obstáculos, polígono autorizado e altura de RTH.
- Vento cresce com a altura e as rajadas mandam; frio e calor reduzem a bateria; Kp alto e cintilação ionosférica degradam o GNSS.
- Segurança é procedimento: checklist antes, vigilância durante, resposta a emergências e registro depois.

### Para saber mais

- **DJI — DJI Pilot (aplicativo de missões):** https://www.dji.com/downloads/djiapp/dji-pilot
- **Pix4D — PIX4Dcapture:** https://www.pix4d.com/product/pix4dcapture/
- **DECEA — REDEMET (METAR, TAF e imagens meteorológicas):** https://redemet.decea.mil.br/
- **NOAA SWPC — Índice Kp planetário:** https://www.swpc.noaa.gov/products/planetary-k-index

### O que você verá na próxima unidade

Na **Unidade 2 — Aquisição e Processamento de Imagens**, as fotos do voo que você planejou viram produtos de engenharia. Você vai estudar a **fotogrametria digital** — por que as sobreposições são necessárias, o papel dos **pontos de controle** e do **georreferenciamento** —, o **posicionamento por GNSS** (RTK e PPK) e como se mede a **precisão** de um produto cartográfico, a geração de **ortomosaicos, modelos digitais de superfície e nuvens de pontos** em softwares como OpenDroneMap e Agisoft Metashape e, por fim, o **cálculo de volumes**, as **curvas de nível** e a **comparação entre o projetado e o executado** no QGIS — o que alimenta diretamente o avanço físico e o valor agregado da Aula 1.

## Aula 4 — Roteiro da Videoaula 4: "Vento fraco no chão, rajada a 70 metros: o voo seguro começa antes da decolagem"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e o voo que voltou com 8% de bateria.

> "Voo autorizado, SARPAS aceito. Vento fraco no chão. A 70 metros, rajadas; o drone volta com 8% de bateria, metade das fotos tremidas. Ninguém quebrou regra: faltou planejamento. Hoje, fechando a unidade, a gente planeja a missão, lê o tempo e segue o checklist."

### 2. Desenvolvimento — parte 1 (0:25 – 1:20)

**[TELA]** Slides 4–8 — tipos de missão; GSD e faixa; sobreposição; área por voo; DJI Pilot e Pix4Dcapture.

> "Primeiro, o tipo de missão: grade para ortomosaico, oblíqua para fachada, corredor para rodovia, órbita para inspeção. Depois, os parâmetros: GSD é altura vezes pixel sobre focal; a faixa é o número de pixels vezes o GSD; o espaçamento entre faixas desconta a sobreposição lateral. No DJI Pilot ou no Pix4Dcapture, você desenha o polígono e o aplicativo calcula a rota. Mas quem responde é você: relevo, grua, polígono autorizado e altura de retorno."

### 3. Desenvolvimento — parte 2 (1:20 – 2:20)

**[TELA]** Slides 9–12 — vento e rajadas; biruta e anemômetro; bateria e temperatura; Kp e cintilação.

> "Agora o tempo. O vento cresce com a altura, e a rajada manda mais que a média. Use no máximo uns dois terços do limite do fabricante. Chuva estraga motor e eletrônica. Frio derruba a bateria; calor de verão brasileiro esquenta tudo. E olhe para o céu de cima: índice Kp a partir de 5 e a cintilação ionosférica do começo da noite podem bagunçar o GNSS e o RTK. Consulte REDEMET, INMET e meça o vento no local."

### 4. Desenvolvimento — parte 3 (2:20 – 3:15)

**[TELA]** Slides 13–16 — checklist antes, durante e depois; emergências; a calculadora de altura, cobertura e vento; a atividade.

> "Segurança é procedimento: documentos, aeronave, área de segurança, altura de retorno acima do maior obstáculo. Durante, linha de visada e reserva de bateria. Perdeu o link? Retorno automático. Perdeu o GNSS? Assuma manual. Avião à vista? Desça. As contas: GSD de 2 centímetros pede no máximo 73 metros; a 70, a faixa tem 105 metros e um multirrotor cobre uns 24 hectares por voo. E o vento de 6 metros por segundo no chão vira quase 9 a 70 metros: acima do limite prático de 8. Não voa."

### 5. Encerramento (3:15 – 3:45)

**[TELA]** Slides 17–19 — pontos-chave, prévia da Unidade 2 e encerramento.

> "Você fechou a Unidade 1: sabe por que e como medir o avanço da obra, qual drone e sensor usar, o que a lei exige e como planejar um voo seguro. Na Unidade 2, essas fotos viram ortomosaico, nuvem de pontos e volume — e o volume volta para a curva S. Te espero lá!"

---

## Quiz não avaliativo

### Questão 1

Na medição do mês 6 de uma obra, a equipe obteve, com apoio de levantamento por drone: valor planejado $VP = 2{,}0$ milhões de reais, valor agregado $VA = 2{,}2$ milhões de reais e custo real $CR = 2{,}5$ milhões de reais. Com base na análise de valor agregado, assinale a alternativa **correta**:

- [ ] a. A obra está atrasada e abaixo do custo, pois o custo real supera o valor planejado.
- [x] b. A obra está adiantada ($IDP = 1{,}10$), mas acima do custo ($IDC = 0{,}88$): agregou mais do que o previsto, gastando mais do que agregou.
- [ ] c. A obra está em dia e dentro do custo, pois o valor agregado está entre o valor planejado e o custo real.
- [ ] d. Não é possível avaliar o prazo, porque o IDP só pode ser calculado ao final da obra, com o custo total conhecido.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) está correta: $IDP = VA/VP = 2{,}2/2{,}0 = 1{,}10 > 1$ indica que se executou mais do que o cronograma previa até a data (adiantamento), e $IDC = VA/CR = 2{,}2/2{,}5 = 0{,}88 < 1$ indica que cada real gasto agregou 88 centavos (estouro de custo). A (a) erra porque o prazo se avalia comparando VA com VP, e não CR com VP; e IDC < 1 significa custo acima, não abaixo. A (c) não tem fundamento: a posição relativa dos três valores não substitui o cálculo dos índices. A (d) é falsa: IDP e IDC são calculados a cada medição, justamente para corrigir o rumo durante a obra.

### Questão 2

Um engenheiro planeja voar um multirrotor de 9 kg, em linha de visada, a 80 m de altura, sobre um canteiro urbano, mantendo a área sob o voo isolada e a pelo menos 30 m dos pedestres. O voo é um mapeamento em faixas sobrepostas para gerar ortomosaico. Considerando a regulamentação vigente, assinale a alternativa **correta**:

- [ ] a. Como o drone tem menos de 25 kg, a operação fica dispensada do cadastro da aeronave, do seguro contra danos a terceiros e do pedido de acesso ao espaço aéreo.
- [ ] b. A operação deve seguir as classes por peso do RBAC-E nº 94 (Classe 3, até 25 kg), que continua sendo a norma aplicável a todas as novas operações.
- [x] c. Pode caber na categoria aberta do RBAC nº 100, com SISANT, piloto habilitado e seguro; por ser aerolevantamento, exige entidade inscrita no Ministério da Defesa e pedido no SARPAS com 4 dias corridos.
- [ ] d. Por ser um voo dentro do canteiro da própria construtora, a autorização do DECEA é dispensada, bastando o aviso aos vizinhos.

**Resposta correta:** `c`

**Feedback:** A alternativa (c) está correta: 9 kg, linha de visada, 80 m de altura e 30 m de distância de pessoas não envolvidas e não anuentes atendem aos critérios da categoria aberta do **RBAC nº 100**, que exige cadastro no SISANT, piloto habilitado (exame teórico exigível a partir de 1º/01/2027) e seguro; como o voo gera ortomosaico a partir de faixas sobrepostas, é **aerolevantamento** (Portaria GM-MD nº 3.703/2021, art. 8º), executado por entidade inscrita no Ministério da Defesa, com pedido no SARPAS 4 dias corridos antes (ICA 100-40). A (a) é falsa: a exclusão do RBAC nº 100 vale para aeronaves de até **250 g** (até 120 m, em VLOS/EVLOS), não até 25 kg — e mesmo essas pedem acesso ao espaço aéreo. A (b) erra: o RBAC-E nº 94 foi substituído pelo RBAC nº 100 em junho de 2026. A (d) é falsa: o espaço aéreo sobre o canteiro não pertence à construtora; o acesso é sempre solicitado ao DECEA pelo SARPAS.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> _[PENDENTE — aguardando acesso à Biblioteca Virtual. Sugestão a confirmar na BV: um livro de planejamento e controle de obras (curva S e valor agregado, Aula 1) ou de topografia/aerofotogrametria com drones (Aula 4).]_

- **Nome do livro:** 
- **Capítulo:** 
- **Link de acesso:** 
- **Qual aula o material deverá entrar?** 

### Para mergulhar no assunto

> Recomendo o vídeo **"Acompanhamento de obra com DRONE na Prática"**, do canal Continental Drones, no YouTube, que mostra em campo como se faz um acompanhamento de obra com drone — equipamento, planejamento e captação das imagens. Assista com o olhar crítico desta unidade: o voo segue um plano de missão? Que cuidados de segurança aparecem? Em que ponto o levantamento vira medição de avanço — e quem compara o resultado com o planejado? Para conferir as regras de voo, complemente com o portal de drones da ANAC.

- **Links:** https://www.youtube.com/watch?v=k4_NHrCXs0U · https://www.gov.br/anac/pt-br/assuntos/drones
- **Qual aula o material deverá entrar?** Aulas 1, 3 e 4

### Podcast (curadoria, até 45 min)

> No episódio #107 do podcast de **André Choma**, voltado à gestão de obras e à construção civil, o tema são os **gêmeos digitais e o uso da tecnologia na construção**. A conversa ajuda a separar o conceito do marketing e a enxergar a tecnologia como apoio ao **controle da obra** — o ciclo medir, comparar, decidir e agir da Aula 1 —, antecipando o que você verá na Unidade 4. O episódio completo tem cerca de 66 minutos; para esta curadoria, ouça os **primeiros 45 minutos**.

- **NOME DO PODCAST:** André Choma (canal no YouTube)
- **NOME DO EPISÓDIO:** Episódio #107 — Gêmeos digitais e o uso da tecnologia na construção
- **Link:** https://www.youtube.com/watch?v=zBGzGt5tt70
- **Qual aula o material deverá entrar?** Aula 1

### Artigo científico

> Artigo de acesso aberto que propõe a **construção com gêmeo digital** (*Digital Twin Construction*). Os autores argumentam que o monitoramento automatizado do canteiro serve para **fechar os laços de controle** da obra: os dados medidos alimentam o ciclo planejar-executar-verificar-agir (PDCA) em ciclos aninhados — do controle de prazo e custo do projeto inteiro à resposta diária sobre produção, qualidade e segurança. É a fundamentação acadêmica do ciclo de controle e da medição do avanço discutidos na Aula 1.

- **Link:** https://doi.org/10.1017/dce.2020.16
- **Qual aula o material deverá entrar?** Aula 1
- **Referência bibliográfica do artigo no formato ABNT:**
  > SACKS, Rafael; BRILAKIS, Ioannis; PIKAS, Ergo; XIE, Haiyan Sally; GIROLAMI, Mark. Construction with digital twin information systems. **Data-Centric Engineering**, v. 1, e14, 2020. DOI: 10.1017/dce.2020.16.
