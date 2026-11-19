# Unidade 3 — Sensores IoT no Monitoramento de Obras

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 9 a 12

## Aula 9 — Monitoramento geotécnico: inclinômetros, piezômetros e marcos de recalque

> Na orla de Santos (SP), dezenas de edifícios construídos entre as décadas de 1950 e 1970, com fundações rasas sobre camadas profundas de argila mole, estão visivelmente inclinados. Agora imagine a sua obra: uma escavação de 10 m para três subsolos, num solo parecido, ao lado de um prédio desses. Antes da primeira caçamba de terra sair, você precisa responder: **o que medir, com qual instrumento, onde instalar e com quais limites?** Nesta aula, você vai conhecer os três instrumentos clássicos do monitoramento geotécnico — **inclinômetro, piezômetro e marco de recalque** — e aprender a transformar as leituras deles em milímetros, em distorção angular e em decisão.

### Instrumentar para decidir: o método observacional

Na Unidade 1, você viu que monitorar é fechar a malha entre medição e ação. Na geotecnia, essa ideia tem nome e sobrenome: o **método observacional**, sistematizado por Peck (1969). Como o solo nunca é exatamente o da sondagem, o projetista adota as hipóteses mais prováveis, **prevê** o comportamento da obra, define **de antemão** os limites aceitáveis e um **plano de contingência** para o caso de os limites serem atingidos — e a obra é executada medindo e comparando. Instrumentação sem limites e sem plano de ação não é método observacional; é coleta de curiosidades.

Numa escavação urbana, três perguntas resumem o risco geotécnico, e cada uma tem o seu instrumento:

- **A contenção e o solo estão se deslocando horizontalmente?** → inclinômetro.
- **A água no solo está empurrando mais do que o previsto?** → piezômetro.
- **Os vizinhos estão recalcando?** → marcos de recalque.

Toda essa instrumentação precisa de uma **leitura zero** (de referência), feita **antes** de a escavação começar, de preferência repetida duas ou três vezes para garantir estabilidade. Sem ela, não há com o que comparar.

### Inclinômetro: como funciona

O inclinômetro mede o **deslocamento horizontal ao longo da profundidade**. Instala-se um **tubo-guia** com quatro ranhuras internas, num furo vertical atrás da contenção, com o pé engastado em solo ou rocha que **não se mova** — abaixo da zona de influência da escavação. Uma **sonda** com rodas, que corre pelas ranhuras e carrega acelerômetros (servo ou MEMS), é baixada até o fundo e lida a cada $L = 0{,}5\,\mathrm{m}$, que é a distância entre as rodas. Em cada posição, a sonda mede a inclinação $\theta$ do trecho, e o desvio horizontal desse trecho é $d = L\,\sin\theta$.

Dois cuidados práticos fazem toda a diferença: faz-se uma **segunda passada com a sonda girada 180°**, que cancela o viés do sensor; e o deslocamento é sempre a **diferença em relação à leitura zero**, acumulada **de baixo para cima**, partindo do pé fixo. Hoje, além das campanhas com sonda manual, existem os **inclinômetros in-place**: cadeias de sensores MEMS fixos dentro do tubo, lidos automaticamente por um datalogger — exatamente o tipo de instrumento que a arquitetura IoT da Aula 3 conecta à nuvem.

### Piezômetro: medir a água que empurra

O **piezômetro** mede a **poropressão** $u$, a pressão da água nos vazios do solo, que se converte em carga de água por $u = \gamma_w\,h$. Ele é crítico em escavações com rebaixamento do lençol, em aterros sobre solo mole e em taludes. Os tipos mais comuns são:

- **Casagrande (tubo aberto)** — um tubo com ponta porosa; o nível d'água é lido com um medidor elétrico. Barato e robusto, mas **lento**: em argila, a água precisa entrar ou sair do tubo para o nível se ajustar.
- **Corda vibrante** — um diafragma ligado a um fio tensionado; a frequência de vibração do fio varia com a pressão. Responde em minutos, permite leitura automática e precisa de correção de temperatura (e, se o sensor não for ventilado, da pressão atmosférica).
- **Pneumático** — lido com gás comprimido; ainda comum em barragens.

![Desenho em corte de um piezômetro de corda vibrante: à esquerda, o filtro poroso e o diafragma; no centro, dentro de um invólucro de aço inoxidável, o fio vibrante tensionado e as bobinas que o excitam e leem a sua frequência; à direita, a vedação interna e o cabo de quatro condutores. Figura: U.S. Bureau of Reclamation, Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/d/d1/Vibrating_wire_piezometer_from_USBR_6515-09_Fig._1.png)

Esse **tempo de resposta** importa. Pela formulação clássica de Hvorslev, o tempo básico de resposta de um tubo aberto é $T = A/(F\,k)$, em que $A$ é a área do tubo, $F$ um fator de forma da ponta e $k$ a permeabilidade. Num tubo de 19 mm de diâmetro em argila com $k = 10^{-8}\,\mathrm{m/s}$, $T$ é da ordem de 10 horas; com $k = 10^{-9}\,\mathrm{m/s}$, de alguns dias. Um piezômetro de Casagrande em argila pode, portanto, "mentir" por dias depois de uma chuva — e é por isso que, onde a resposta precisa ser rápida, usa-se corda vibrante.

### Marcos de recalque e a referência que não pode se mexer

O recalque dos vizinhos é medido em **marcos** — pinos metálicos fixados nos pilares ou na base das fachadas — por **nivelamento geométrico de precisão**, a partir de uma **referência de nível (RN) profunda**, ancorada fora da zona de influência da escavação. Se a referência se mexer, todas as leituras mentem juntas.

![Referência de nível de precisão: placa metálica circular numerada cravada no solo, junto a uma tampa metálica de piso, com a ponta de uma mira de nivelamento apoiada sobre ela. Foto: MapStaringEnthusiast, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/7/7f/Precise_Level_Benchmark%2C_Singapore.jpg)

A automação substitui ou complementa o nivelamento manual: **estações totais robóticas** que leem prismas a cada hora, **células de recalque por nível hidrostático** (vasos comunicantes ligados a transdutores de pressão) e **clinômetros de parede** (*tiltmeters*), que medem a rotação de um pilar ou de uma fachada.

### Recalque diferencial e distorção angular

O que fissura um prédio não é tanto o recalque **absoluto**, e sim o **diferencial**: um pilar descendo mais que o vizinho. A medida usada é a **distorção angular** $\beta = \delta/L$, o recalque diferencial $\delta$ entre dois pilares dividido pela distância $L$ entre eles. Bjerrum (1963) propôs uma escala de referência ainda muito usada:

| $\beta$ | Efeito associado |
| --- | --- |
| 1/750 | dificuldades com máquinas sensíveis a recalques |
| 1/600 | perigo para pórticos com diagonais |
| 1/500 | limite de segurança para edifícios em que não se admitem fissuras |
| 1/300 | primeiras fissuras em paredes de alvenaria; dificuldades com pontes rolantes |
| 1/250 | a inclinação de edifícios altos torna-se visível |
| 1/150 | fissuração considerável em paredes; danos estruturais |

A **ABNT NBR 6122** (projeto e execução de fundações) torna obrigatório o monitoramento de recalques em alguns casos — por exemplo, estruturas em que a carga variável é significativa (silos, reservatórios), edificações altas ou esbeltas e fundações não convencionais —, e o plano de monitoramento da obra deve fixar os limites de cada instrumento.

### Exemplo numérico

**(a) Do ângulo ao milímetro.** Numa escavação, a sonda do inclinômetro ($L = 0{,}5\,\mathrm{m}$) registra, em relação à leitura zero, variações de $\sin\theta$ apenas nos seis trechos superiores: $6{,}0$; $5{,}0$; $4{,}0$; $3{,}0$; $1{,}6$ e $0{,}4 \times 10^{-3}$ (do topo para baixo). Os trechos abaixo não variaram — o pé está fixo. O deslocamento no topo é a soma:

$
\delta_{topo} = L \sum \Delta(\sin\theta) = 0{,}5 \times (6{,}0 + 5{,}0 + 4{,}0 + 3{,}0 + 1{,}6 + 0{,}4) \times 10^{-3} = 0{,}5 \times 0{,}020 = 0{,}010\,\mathrm{m} = 10{,}0\,\mathrm{mm}
$

Acumulando de baixo para cima, o perfil passa por 0,2; 1,0; 2,5; 4,5; 7,0 e 10,0 mm. Há 7 dias, o topo estava em 7,0 mm; a velocidade é $(10{,}0 - 7{,}0)/7 \approx 0{,}43\,\mathrm{mm/dia}$. Com nível de atenção em 15 mm, mantido o ritmo, ele seria atingido em $(15 - 10)/0{,}43 \approx 11{,}7$ dias — tempo para decidir com calma, desde que a velocidade não aumente.

**(b) O vizinho já fissura?** Dois pilares do prédio vizinho, a $L = 6{,}0\,\mathrm{m}$ um do outro, recalcaram $18\,\mathrm{mm}$ e $6\,\mathrm{mm}$:

$
\delta = 18 - 6 = 12\,\mathrm{mm}
\qquad
\beta = \frac{\delta}{L} = \frac{12}{6.000} = 0{,}002 = \frac{1}{500}
$

A distorção chegou ao limite de Bjerrum para edifícios em que não se admitem fissuras. É hora de vistoriar o vizinho, aumentar a frequência de leitura e acionar o plano de contingência previsto.

### Atividade prática

Para a escavação de 10 m ao lado do prédio de Santos do gancho, desenhe uma planta e um corte e indique: (1) onde ficam os inclinômetros (quantos, a que profundidade o pé deve chegar), os piezômetros (de que tipo) e os marcos de recalque (em quais pilares), além da referência de nível; (2) a leitura zero e a frequência de leitura antes, durante e depois da escavação; (3) os níveis de atenção e de alerta de cada grandeza, incluindo um limite de distorção angular; (4) qual instrumento confirma qual — por exemplo, se o inclinômetro acusar deslocamento, que outra leitura deveria mudar junto?

### Pontos-chave

- O **método observacional** exige prever o comportamento, definir limites e plano de contingência **antes** de medir; toda instrumentação começa por uma **leitura zero**.
- O **inclinômetro** mede deslocamento horizontal em profundidade: $d = L\,\sin\theta$ por trecho, acumulado de baixo para cima a partir de um pé fixo, sempre em relação à leitura zero.
- O **piezômetro** mede poropressão; o de tubo aberto é lento em argila (tempo de resposta $T = A/(F\,k)$), o de corda vibrante responde em minutos e pode ser automatizado.
- **Marcos de recalque** dependem de uma referência de nível estável; o dano está ligado à **distorção angular** $\beta = \delta/L$ (Bjerrum: 1/500 sem fissuras, 1/300 primeiras fissuras em alvenaria).

### Para saber mais

- **PECK, R. B. — *Advantages and limitations of the observational method in applied soil mechanics* (Géotechnique, 1969):** https://doi.org/10.1680/geot.1969.19.2.171
- **Wikipedia — Piezômetro:** https://pt.wikipedia.org/wiki/Piez%C3%B4metro
- **Wikipedia — Recalque:** https://pt.wikipedia.org/wiki/Recalque
- **Wikipedia (inglês) — Inclinometer:** https://en.wikipedia.org/wiki/Inclinometer

## Aula 9 — Roteiro da Videoaula 9: "Monitoramento geotécnico: inclinômetros, piezômetros e marcos de recalque"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e os prédios inclinados da orla de Santos.

> "Olha esses prédios na orla de Santos: inclinados, à vista de todo mundo. Fundação rasa sobre argila mole. Agora imagina a sua obra: uma escavação de 10 metros ao lado de um prédio desses. Antes da primeira caçamba sair, você precisa saber o que medir, com qual instrumento, onde e com quais limites. É o assunto de hoje."

### 2. Desenvolvimento — parte 1 (0:30 – 1:20)

**[TELA]** Slides 4–8 — método observacional, a escavação instrumentada em 3D, como funciona o inclinômetro, o perfil de deslocamento e o exemplo do ângulo ao milímetro.

> "Peck chamou isso de método observacional: prever o comportamento, fixar os limites e o plano de contingência antes, e medir durante a obra. Três perguntas, três instrumentos: a contenção está andando? Inclinômetro. A água está empurrando? Piezômetro. O vizinho está descendo? Marco de recalque. E tudo começa pela leitura zero. O inclinômetro é um tubo com ranhuras, com o pé fixo em solo que não se move; a sonda lê a inclinação a cada meio metro, e cada trecho desloca L vezes o seno do ângulo. Somando de baixo para cima: no nosso exemplo, 0,5 vezes 0,020 dá 10 milímetros no topo. Há uma semana eram 7: são 0,43 milímetro por dia."

### 3. Desenvolvimento — parte 2 (1:20 – 2:10)

**[TELA]** Slides 9–11 — tipos de piezômetro, o tempo de resposta em argila e os marcos de recalque com a referência de nível.

> "O piezômetro mede a poropressão. O de Casagrande é um tubo aberto: barato, robusto e lento — em argila, o nível pode levar horas ou dias para se ajustar; mexa na permeabilidade e veja. O de corda vibrante responde em minutos e conversa com o datalogger. Já o recalque se mede em marcos nos pilares do vizinho, por nivelamento de precisão, a partir de uma referência de nível profunda, fora da influência da escavação. Se a referência mexer, tudo mente junto."

### 4. Desenvolvimento — parte 3 (2:10 – 3:00)

**[TELA]** Slides 12–15 — o prédio que recalca em 3D, a escala de Bjerrum, a calculadora de distorção angular e do manual ao IoT.

> "Prédio não fissura pelo recalque absoluto, e sim pelo diferencial. A medida é a distorção angular: recalque diferencial dividido pela distância entre os pilares. Dezoito e seis milímetros, a seis metros: 12 sobre 6.000, um quinhentos avos. Pela escala de Bjerrum, é o limite para edifícios em que não se admitem fissuras. Com um trezentos avos, aparecem as primeiras fissuras na alvenaria. E a frequência de leitura muda com a fase da obra: leitura zero, leitura intensa e automática durante a escavação, e espaçada depois que estabiliza."

### 5. Encerramento (3:00 – 3:30)

**[TELA]** Slides 16–18 — atividade, pontos-chave e encerramento.

> "Hoje você instrumentou o solo e os vizinhos. Na próxima aula, a gente sobe para a estrutura: extensômetros, acelerômetros, fissurômetros e a maturidade do concreto. Te espero na Aula 10!"

---

## Aula 10 — Monitoramento estrutural: extensômetros, acelerômetros, fissurômetros e maturidade do concreto

> Sexta-feira, 17h. A laje do 12º pavimento foi concretada na quarta, e o empreiteiro quer retirar o escoramento na segunda para reaproveitar as formas. Os corpos de prova só serão rompidos depois. Na escavação ao lado, uma escora metálica, ao sol da tarde, parece estar "ganhando" carga. E o vizinho reclama de uma fissura que "abre e fecha". Três perguntas, uma mesma resposta: **medir o que a estrutura está sentindo**. Nesta aula, você vai conhecer os sensores do monitoramento estrutural — extensômetros, acelerômetros, fissurômetros e sensores de maturidade — e aprender a separar o sinal estrutural dos efeitos da temperatura.

### Quatro perguntas, quatro sensores

O monitoramento estrutural responde a quatro perguntas típicas: **quanto esforço** a peça está recebendo (deformação → **extensômetro**); **como ela vibra** (aceleração → **acelerômetro**); **a fissura está crescendo** (abertura → **fissurômetro**); e **o concreto já ganhou resistência** (temperatura ao longo do tempo → **sensor de maturidade**). Em todas elas vale a lição da Unidade 1: o sensor só é útil com leitura zero, limites definidos e uma ação associada.

### Extensômetros: da deformação à força

Na Aula 2 você conheceu o **extensômetro elétrico de resistência**, cuja resistência varia com a deformação ($\Delta R/R = GF\,\varepsilon$). Ele lê fenômenos rápidos, mas pode sofrer com umidade e deriva em monitoramentos longos. Em obras, o mais usado para o longo prazo é o **extensômetro de corda vibrante**: um fio tensionado entre dois blocos fixados à peça, cuja frequência de vibração $f$ varia com a deformação ($\varepsilon \propto f^2$). Ele é estável por anos, não é afetado pela resistência do cabo e pode ser **soldado em escoras metálicas** ou **embutido no concreto**, amarrado à armadura antes da concretagem.

![Duas mãos amarram, com abraçadeiras plásticas brancas, um extensômetro com fios vermelhos a barras de armadura e cordoalhas de uma viga, antes da concretagem; ao fundo, outras barras verticais da armação. Foto: Federal Highway Administration, Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/6/60/Strain_Gauge_Installation_in_SCC_Beams-2_SC_%288496265082%29.jpg)

No regime elástico, a tensão vem da **lei de Hooke**, $\sigma = E\,\varepsilon$, e a força, de $N = \sigma\,A$. A deformação é medida em **microdeformações** ($1\,\mu\varepsilon = 10^{-6}$). E aqui mora a armadilha: a **temperatura**. Uma escora de aço tem coeficiente de dilatação de cerca de $12 \times 10^{-6}/^\circ\mathrm{C}$; uma variação de 15 °C entre a manhã e a tarde equivale a 180 µε de dilatação livre — da mesma ordem do sinal que se quer medir. Por isso os extensômetros de corda vibrante trazem um **termistor** embutido, e a leitura deve ser **corrigida para a temperatura** antes de virar força.

### Acelerômetros: a assinatura dinâmica da estrutura

Os **acelerômetros** medem a vibração. Os **MEMS** são baratos e de baixo consumo, ideais para IoT; os **piezoelétricos** têm mais sensibilidade e faixa de frequência. Toda estrutura tem **frequências naturais**: num modelo simples de massa e mola, $f = \frac{1}{2\pi}\sqrt{k/m}$. Se a rigidez $k$ cai — por fissuração, por dano numa ligação —, a frequência cai junto: $f_2/f_1 = \sqrt{k_2/k_1}$. Uma queda de 5% na frequência corresponde a cerca de 10% de perda de rigidez ($0{,}95^2 \approx 0{,}90$). Esse é o princípio do **monitoramento da saúde estrutural** (*structural health monitoring*, SHM) por identificação modal. Lembre-se de Nyquist (Aula 2): amostrar acima do dobro — na prática, de 5 a 10 vezes — a maior frequência de interesse.

O caso clássico é o da **Millennium Bridge**, em Londres: inaugurada em junho de 2000, foi fechada dois dias depois por oscilações laterais provocadas pelo caminhar sincronizado dos pedestres e só reabriu em 2002, após a instalação de amortecedores. Medir aceleração e frequências faz parte do projeto e do comissionamento — não é luxo.

### Fissurômetros: a fissura está crescendo?

O **fissurômetro** mede a abertura de uma fissura. O mais simples é o *tell-tale* de acrílico: duas placas sobrepostas, uma com retícula, fixadas uma de cada lado da fissura e lidas a olho, com resolução da ordem do milímetro. Os **fissurômetros elétricos** (potenciométricos ou com LVDT) chegam a centésimos de milímetro e se ligam ao datalogger.

![Fissurômetro de acrílico transparente com retícula graduada, fixado com quatro parafusos sobre uma trinca que atravessa uma parede de tijolos e argamassa. Foto: Smial, Wikimedia Commons, CC BY-SA 2.0 DE](https://upload.wikimedia.org/wikipedia/commons/9/9c/Crackmeter_imgp7707.jpg)

A abertura **oscila com a temperatura** — abre e fecha ao longo do dia e das estações. O que interessa é a **tendência**, e não a oscilação diária; por isso a leitura contínua, que permite separar os dois efeitos, vale mais do que uma leitura manual semanal. E toda fissura do vizinho deve ser mapeada e fotografada **antes** do início da obra, numa vistoria cautelar.

### Maturidade do concreto: temperatura × tempo vira resistência

A resistência do concreto nas primeiras idades depende da **temperatura** da cura: no calor, a hidratação é mais rápida; no frio, mais lenta. O **método da maturidade** (ASTM C1074) traduz o histórico térmico num índice. Na função de **Nurse-Saul**, o fator temperatura-tempo é

$
M = \sum (T - T_0)\,\Delta t
$

em °C·h, em que $T$ é a temperatura média do concreto em cada intervalo $\Delta t$ e $T_0$ é a temperatura de referência (*datum*). A ASTM C1074 recomenda $T_0 = 0\,^\circ\mathrm{C}$ para cimento tipo I sem aditivos, com cura entre 0 e 40 °C; o ideal é determiná-la para a mistura. Em laboratório, rompem-se corpos de prova **da mesma mistura** em várias idades e ajusta-se a curva resistência × maturidade; na obra, **sensores embutidos** registram a temperatura a cada 15 ou 30 minutos e enviam os dados pela rede. O método apoia decisões como desforma, retirada de escoramento e protensão, mas **não substitui** o controle tecnológico de aceitação do concreto por corpos de prova.

### Exemplo numérico

**(a) Quanto a escora está carregando?** Um extensômetro de corda vibrante numa escora de aço ($E = 200\,\mathrm{GPa}$, área $A = 120\,\mathrm{cm^2}$) indica, já corrigido para a temperatura, $\Delta\varepsilon = 250\,\mu\varepsilon$ desde a leitura zero:

$
\sigma = E\,\varepsilon = 200.000\,\mathrm{MPa} \times 250 \times 10^{-6} = 50\,\mathrm{MPa}
\qquad
N = \sigma\,A = 50\,\mathrm{MPa} \times 0{,}012\,\mathrm{m^2} = 0{,}6\,\mathrm{MN} = 600\,\mathrm{kN}
$

Com carga de projeto de 900 kN, a escora está a 67% dela. Sem a correção térmica, os 180 µε de uma variação de 15 °C poderiam ser confundidos com carga.

**(b) Pode liberar a laje?** A calibração (ilustrativa) da mistura em laboratório deu $f_c = 9{,}2\,\ln M - 41$ (MPa, com $M$ em °C·h), e a retirada do escoramento exige $f_c \ge 21\,\mathrm{MPa}$. O sensor da laje registrou temperaturas médias de 28, 32 e 26 °C em três blocos de 12 h. Com $T_0 = 0\,^\circ\mathrm{C}$:

$
M = 12 \times (28 + 32 + 26) = 1.032\,^\circ\mathrm{C \cdot h}
\qquad
f_c = 9{,}2 \times \ln 1.032 - 41 \approx 22{,}8\,\mathrm{MPa}
$

A maturidade necessária é $M = e^{(21 + 41)/9{,}2} \approx 845\,^\circ\mathrm{C \cdot h}$, atingida por volta de 29 h. No inverno, com o concreto a 15 °C, os mesmos 845 °C·h levariam $845/15 \approx 56\,\mathrm{h}$. A decisão: liberar, **confirmando** com corpos de prova e com o projetista da estrutura.

### Atividade prática

Para um edifício de 15 pavimentos com escavação escorada e um vizinho que já tem fissuras, monte uma tabela com: grandeza, sensor, local de instalação, momento da leitura zero, frequência de leitura, forma de compensar a temperatura e decisão que cada sensor apoia (por exemplo: reforçar uma escora, liberar uma laje, chamar o projetista). Inclua ao menos um extensômetro, um fissurômetro e um sensor de maturidade.

### Pontos-chave

- Extensômetros dão deformação; a força vem de $\sigma = E\,\varepsilon$ e $N = \sigma\,A$ — **depois** de corrigir o efeito da temperatura.
- A **frequência natural** é a assinatura da rigidez: $f_2/f_1 = \sqrt{k_2/k_1}$; 5% a menos na frequência ≈ 10% a menos na rigidez.
- No fissurômetro, o que importa é a **tendência**, não a oscilação térmica diária; mapeie as fissuras **antes** da obra.
- A **maturidade** $M = \sum (T - T_0)\,\Delta t$ estima a resistência nas primeiras idades a partir de uma curva calibrada para a mesma mistura, sem substituir o controle por corpos de prova.

### Para saber mais

- **CARINO, N. J.; LEW, H. S. — *The Maturity Method: From Theory to Application* (NIST, 2001):** https://www.nist.gov/publications/maturity-method-theory-application
- **Wikipedia — Acelerômetro:** https://pt.wikipedia.org/wiki/Aceler%C3%B4metro
- **Wikipedia — Frequência natural:** https://pt.wikipedia.org/wiki/Frequ%C3%AAncia_natural

## Aula 10 — Roteiro da Videoaula 10: "Monitoramento estrutural: extensômetros, acelerômetros, fissurômetros e maturidade do concreto"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e a laje concretada na quarta.

> "Sexta, cinco da tarde. A laje foi concretada na quarta e o empreiteiro quer tirar o escoramento na segunda. Os corpos de prova ainda não foram rompidos. Ao lado, uma escora metálica parece ganhar carga no sol da tarde. Hoje a gente mede o que a estrutura está sentindo."

### 2. Desenvolvimento — parte 1 (0:30 – 1:30)

**[TELA]** Slides 4–7 — quatro perguntas e quatro sensores, extensômetro elétrico × corda vibrante, a escora instrumentada e a instalação antes da concretagem.

> "Deformação, vibração, fissura e maturidade: quatro perguntas, quatro sensores. O extensômetro de corda vibrante é o cavalo de batalha da obra: estável por anos, soldado na escora ou amarrado na armadura. Duzentos e cinquenta microdeformações vezes 200 gigapascals dão 50 megapascals; vezes 120 centímetros quadrados, 600 quilonewtons — 67% da carga de projeto. Mas cuidado: 15 graus de sol valem 180 microdeformações. Sem compensar a temperatura, o sol vira carga no seu relatório."

### 3. Desenvolvimento — parte 2 (1:30 – 2:20)

**[TELA]** Slides 8–12 — acelerômetros e frequência natural, o prédio que oscila em 3D, a Millennium Bridge, fissurômetros e a série da fissura.

> "Toda estrutura tem uma assinatura: a frequência natural. Se a rigidez cai, a frequência cai junto — 10% de rigidez a menos, uns 5% de frequência a menos. Foi medindo aceleração que se entendeu o balanço da Millennium Bridge, em Londres. E no fissurômetro, a fissura abre e fecha com o sol todo dia; o que importa é a tendência, que só aparece com leitura contínua."

### 4. Desenvolvimento — parte 3 (2:20 – 3:10)

**[TELA]** Slides 13–15 — o método da maturidade, a curva de 72 h e a calculadora da laje.

> "Agora a laje. Maturidade é temperatura vezes tempo: soma de T menos T zero vezes delta t. Vinte e oito, 32 e 26 graus em blocos de 12 horas dão 1.032 grau-hora; pela curva calibrada da mistura, uns 22,8 megapascals. O alvo de 21 foi atingido por volta de 29 horas. No inverno, a 15 graus, seriam 56 horas. Libera — confirmando com corpo de prova e com o projetista."

### 5. Encerramento (3:10 – 3:35)

**[TELA]** Slides 16–18 — atividade, pontos-chave e encerramento.

> "Você instrumentou a estrutura. Na próxima aula, o monitoramento sai para o entorno: vibração nos vizinhos, ruído, poeira e o rastreamento de máquinas e pessoas. Te espero na Aula 11!"

---

## Aula 11 — Segurança, ambiente e produtividade: vibração, ruído, poeira e rastreamento de equipamentos

> Segunda-feira, 8h. A cravação de estacas-prancha começou a 15 m de um casarão tombado. Às 9h, o morador liga dizendo que "a casa inteira treme". Às 10h, a vizinhança reclama do barulho e da poeira na prefeitura. Às 11h, um caminhão de terra dá ré na rampa e passa a meio metro de um ajudante. São quatro problemas diferentes — **vibração, ruído, poeira e interferência entre máquinas e pessoas** — e todos podem ser monitorados com a mesma arquitetura IoT da Aula 3. Nesta aula, você vai aprender as grandezas, os sensores e as referências normativas de cada um, e a usar os dados também a favor da **produtividade**.

### Três frentes, uma só arquitetura

O monitoramento do entorno e da operação do canteiro atende a três frentes: **segurança** (vibração em edificações vizinhas, colisões entre máquinas e pessoas), **ambiente** (ruído e poeira) e **produtividade** (uso real dos equipamentos). A pilha é a mesma: sensor → rede → plataforma → ação. O que muda é a régua de comparação: normas da ABNT, resoluções do CONAMA, a legislação municipal (que costuma regular ruído e horário de obra) e a **NR-18**, que trata da segurança e saúde no trabalho na indústria da construção.

![Bate-estacas cravando estacas-prancha metálicas para um poço de esgoto numa rua residencial, rente a uma casa de tijolos aparentes com porta vermelha; ao lado, entulho e um poste de iluminação. Foto: Stephen Craven, Wikimedia Commons, CC BY-SA 2.0](https://upload.wikimedia.org/wikipedia/commons/d/dd/Pile_driving_for_a_sewer_shaft_-_geograph.org.uk_-_1120180.jpg)

### Vibração: velocidade de partícula e frequência

Para avaliar dano em edificações, a grandeza usada é a **velocidade de vibração de partícula de pico** (PPV, em mm/s), registrada por um **sismógrafo de engenharia** com geofone triaxial apoiado no pé da edificação vizinha. A ABNT NBR 9653 define a velocidade de partícula de pico como o maior dos três valores de pico das componentes (vertical, longitudinal e transversal). A **frequência dominante** também importa: as edificações são mais sensíveis às baixas frequências, próximas das suas frequências naturais.

![Sismógrafo de engenharia em campo, junto a um canteiro de obras: sensores montados num tripé sobre o piso, ligados por cabos a uma maleta de registro azul, ao lado do tronco de uma árvore. Foto: Wilson, Ihrig & Associates, Inc., Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/f/f4/Seismograph_recording_vibrations.jpg)

A **NBR 9653**, que trata dos efeitos do uso de explosivos em mineração em áreas urbanas, fixa limites de PPV que crescem com a frequência: de 4 a 15 Hz, iniciando em 15 mm/s e aumentando linearmente até 20 mm/s; de 15 a 40 Hz, de 20 mm/s aumentando linearmente até 50 mm/s; acima de 40 Hz, 50 mm/s; abaixo de 4 Hz, vale um critério de deslocamento de partícula de pico de no máximo 0,6 mm. Ela também limita a pressão acústica do desmonte a 100 Pa (134 dBL pico). Dois cuidados: a norma foi feita para **desmonte com explosivos**; para cravação de estacas, compactação vibratória e, sobretudo, para **edificações sensíveis** (como um casarão tombado), o plano de monitoramento costuma fixar limites próprios, mais baixos. E o **incômodo humano** aparece bem antes de qualquer dano.

### Ruído: decibéis não se somam como metros

O nível de pressão sonora é medido em **decibéis**, uma escala logarítmica; a ponderação **A**, dB(A), aproxima a sensibilidade do ouvido, e o $L_{Aeq}$ é o nível equivalente de energia num intervalo. A **ABNT NBR 10151:2019** define como medir e avaliar o ruído em áreas habitadas e traz limites de nível para ambientes externos, por tipo de área e período: por exemplo, 50 dB diurno e 45 dB noturno em área estritamente residencial urbana ou de hospitais ou de escolas, e 55/50 dB em área mista predominantemente residencial. Como a escala é logarítmica, níveis se somam por

$
L_{total} = 10\,\log_{10}\left(\sum 10^{L_i/10}\right)
$

Duas fontes iguais dão **+3 dB**; e, para uma fonte pontual ao ar livre, dobrar a distância reduz cerca de **6 dB** ($L_2 = L_1 - 20\,\log_{10}(r_2/r_1)$).

### Poeira: MP10 e MP2,5

A poeira de obra é monitorada como **material particulado** com diâmetro até 10 µm (**MP10**) e até 2,5 µm (**MP2,5**), que penetram no sistema respiratório. Os sensores IoT mais comuns são **óticos de espalhamento de luz**: baratos e de baixo consumo, mas tendem a superestimar com umidade alta e precisam ser **calibrados por colocalização** com uma estação de referência. Os padrões nacionais de qualidade do ar estão na **Resolução CONAMA nº 506/2024**, que substituiu a 491/2018; na etapa PI-2, em vigor desde janeiro de 2025, a média de 24 h é de 100 µg/m³ para MP10 e 50 µg/m³ para MP2,5. Atenção: são padrões de **qualidade do ar ambiente**, não limites de emissão de uma obra — o plano de monitoramento define gatilhos próprios na divisa e as ações associadas (aspersão de água, lavagem de rodas, cobertura de caçambas, barreiras).

![Escavadeira com rompedor demolindo uma estrutura elevada de concreto enquanto um jato de água, lançado de trás de um tapume, molha o ponto de demolição para controlar a poeira. Foto: MassDOT, Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/e/e8/Dust_control_for_Lechmere_Elevated_demolition%2C_June_2020.jpg)

### Rastreamento: máquinas, pessoas e cercas virtuais

A **telemetria GNSS** nas máquinas informa posição, horas de motor, tempo em marcha lenta e consumo. Sistemas de **localização em tempo real** (RTLS), com etiquetas **UWB** (precisão de decímetros) ou **BLE** (metros) em capacetes e crachás, permitem criar **cercas virtuais** (*geofencing*): uma zona de exclusão em torno da escavadeira que dispara alerta sonoro para o operador e para o trabalhador que entra nela. Mas atenção: localização de pessoas é **dado pessoal** — tema de LGPD que voltará na Unidade 4.

### Exemplo numérico

**(a) Vibração.** O sismógrafo no casarão registra PPV de 12 mm/s com frequência dominante de 10 Hz. Na faixa de 4 a 15 Hz, o limite da NBR 9653 é interpolado:

$
V_{lim} = 15 + (20 - 15)\,\frac{10 - 4}{15 - 4} \approx 17{,}7\,\mathrm{mm/s}
\qquad
\frac{12}{17{,}7} \approx 68\%
$

Se a frequência fosse 30 Hz, o limite seria $20 + 30 \times (30 - 15)/25 = 38\,\mathrm{mm/s}$: a mesma PPV pesa mais em baixa frequência. Num casarão tombado, o plano provavelmente terá um limite próprio bem menor — e 12 mm/s pediriam ação.

**(b) Ruído.** No receptor, um gerador, uma escavadeira e o bate-estacas produzem, isoladamente, 62, 65 e 68 dB(A):

$
L_{total} = 10\,\log_{10}\left(10^{6{,}2} + 10^{6{,}5} + 10^{6{,}8}\right) \approx 70{,}4\,\mathrm{dB(A)}
$

Desligar o gerador (o mais silencioso) só reduz para 69,8 dB(A); tratar o bate-estacas (o mais barulhento) leva a 66,8 dB(A). **Ataque a fonte dominante.** Para uma referência de 55 dB, ainda haveria excedente — daí barreiras acústicas, horários restritos e métodos menos ruidosos.

**(c) Produtividade.** Num turno de 9 h, a telemetria de uma escavadeira mostra 7,2 h de motor ligado, das quais 2,1 h em marcha lenta. Tempo produtivo: $7{,}2 - 2{,}1 = 5{,}1\,\mathrm{h}$; utilização: $5{,}1/9 \approx 57\%$; ociosidade: $2{,}1/7{,}2 \approx 29\%$ do tempo ligado. A 4 L/h em marcha lenta (valor ilustrativo), são 8,4 L de diesel por dia sem produzir nada.

### Pausa para reflexão (Desafio)

O crachá UWB que evita o atropelamento na rampa é o **mesmo** que registra, minuto a minuto, onde cada trabalhador esteve: pausas, idas ao banheiro, conversas, produtividade individual. **Rastrear pessoas é segurança ou vigilância?** Pense: qual é a **finalidade** declarada? É possível **minimizar** o dado — por exemplo, processar só a proximidade com a máquina, na borda, sem guardar o histórico nominal? Por quanto tempo o dado fica guardado e **quem** tem acesso? Os trabalhadores foram **informados**? Uma regra para testar: coletar o mínimo necessário para a finalidade de segurança, informar com transparência e **não reutilizar** o dado para outra finalidade, como avaliar desempenho individual.

### Atividade prática

Monte o plano de monitoramento ambiental e de segurança da cravação junto ao casarão: posição do sismógrafo, do sonômetro e do sensor de MP10; níveis de atenção e de alerta do plano para cada grandeza, com a ação correspondente (reduzir energia de cravação, trocar o método, aspergir água, mudar horário); a regra da cerca virtual em torno das máquinas; e o que será enviado ao vizinho e à prefeitura em cada relatório.

### Pontos-chave

- **Vibração** se avalia por **PPV e frequência**: na NBR 9653 (desmonte com explosivos), o limite vai de 15 mm/s em 4 Hz a 50 mm/s acima de 40 Hz; edificações sensíveis pedem limites próprios do plano.
- **Ruído** em dB(A) se soma logaritmicamente: duas fontes iguais = +3 dB; reduza primeiro a **fonte dominante**. A NBR 10151:2019 é a referência de avaliação em áreas habitadas.
- **Poeira** (MP10, MP2,5): sensores óticos precisam de calibração; os padrões da CONAMA 506/2024 são de qualidade do ar ambiente, e o plano define gatilhos na divisa.
- **Telemetria e RTLS** aumentam segurança (cercas virtuais) e produtividade (utilização × ociosidade), mas localização de pessoas é dado pessoal: finalidade, minimização e transparência.

### Para saber mais

- **CONAMA — Conselho Nacional do Meio Ambiente (resoluções, incluindo a nº 506/2024, qualidade do ar):** https://conama.mma.gov.br/
- **Ministério do Trabalho e Emprego — NR-18 (segurança e saúde no trabalho na indústria da construção):** https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-18-nr-18
- **Wikipedia — Decibel:** https://pt.wikipedia.org/wiki/Decibel
- **Wikipedia — Material particulado:** https://pt.wikipedia.org/wiki/Material_particulado

## Aula 11 — Roteiro da Videoaula 11: "Segurança, ambiente e produtividade: vibração, ruído, poeira e rastreamento de equipamentos"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–4 — capa, sumário, as estacas junto ao casarão e as três frentes.

> "Segunda, oito da manhã: estacas a 15 metros de um casarão tombado. Às nove, a casa treme; às dez, a reclamação de barulho e poeira; às onze, um caminhão passa a meio metro de um ajudante. Quatro problemas, uma mesma arquitetura IoT."

### 2. Desenvolvimento — parte 1 (0:30 – 1:20)

**[TELA]** Slides 5–7 — vibração e sismógrafo, a simulação de PPV × frequência e a curva da NBR 9653.

> "Vibração se mede em velocidade de partícula de pico, em milímetros por segundo, com um sismógrafo no pé da edificação. E a frequência importa: a NBR 9653 parte de 15 milímetros por segundo em 4 hertz e chega a 50 acima de 40. Doze milímetros por segundo a 10 hertz é 68% do limite. Mas a norma é de desmonte com explosivos: para um casarão tombado, o plano fixa limites próprios, mais baixos."

### 3. Desenvolvimento — parte 2 (1:20 – 2:20)

**[TELA]** Slides 8–11 — ruído e NBR 10151, a soma de decibéis, MP10 e MP2,5 e a simulação da poeira com aspersão.

> "Decibel não se soma como metro. Sessenta e dois, 65 e 68 dão 70,4; desligar o gerador quase não muda nada; tratar o bate-estacas, sim. A NBR 10151 é a régua do ruído em área habitada. Poeira: MP10 e MP2,5, com sensores óticos que precisam de calibração. Os padrões da CONAMA 506 são de ar ambiente; na divisa da obra, o plano define o gatilho para ligar a aspersão."

### 4. Desenvolvimento — parte 3 (2:20 – 3:10)

**[TELA]** Slides 12–15 — rastreamento, a cerca virtual em 3D, a calculadora de utilização e a pausa para reflexão.

> "Telemetria na máquina e etiquetas UWB nas pessoas permitem cercas virtuais: entrou na zona da escavadeira, os dois são avisados. E os mesmos dados mostram produtividade: 7,2 horas ligada, 2,1 em marcha lenta, utilização de 57%. Mas pare e pense: rastrear pessoas é segurança ou vigilância? Finalidade, mínimo necessário e transparência."

### 5. Encerramento (3:10 – 3:35)

**[TELA]** Slides 16–18 — atividade, pontos-chave e encerramento.

> "São muitos sensores gerando muitos dados. Como limpar, definir alertas que não enlouqueçam a equipe e montar um dashboard que leve à decisão? É a última aula da unidade. Te espero na Aula 12!"

---

## Aula 12 — Dados de sensores: séries temporais, níveis de alerta e dashboards

> Segunda-feira, 7h. A obra tem 60 sensores e gera milhares de leituras por dia. No fim de semana, o painel disparou **37 alarmes**. Trinta e cinco eram falsos: um pico de rádio, um sensor com bateria fraca, o sol batendo numa escora. Na terceira semana assim, a equipe passou a ignorar os alarmes — e um deles era real. Esse fenômeno tem nome: **fadiga de alarmes**. Nesta aula, você vai aprender a tratar **séries temporais** de sensores, a desenhar **níveis de alerta** com um plano de ação e a montar **dashboards** que levam à decisão, e não ao cansaço.

### Anatomia de uma leitura

Cada ponto de uma série temporal é mais do que um número. Ele precisa de: **carimbo de tempo** (de preferência em UTC, com o fuso declarado); **identificação do sensor**; **valor bruto** (Hz, mA, dígitos); **valor de engenharia** (mm, kPa), obtido com a leitura zero e os fatores de calibração — que devem ser **versionados**; **unidade**; **marcas de qualidade**; e dados de saúde, como **bateria e intensidade do sinal**. Regra de ouro: **nunca sobrescreva o dado bruto**; a correção é sempre uma nova camada, rastreável. Esses dados vivem em **bancos de séries temporais**, otimizados para gravar e consultar por intervalo de tempo.

### Cinco defeitos que todo dado de campo tem

1. **Picos espúrios** — um valor isolado e fisicamente impossível (interferência, falha de leitura).
2. **Lacunas** — horas ou dias sem dado (bateria, rádio, sensor danificado).
3. **Deriva** — o sensor "anda" devagar sem que o mensurando mude (Aula 2).
4. **Ciclos térmicos** — oscilações diárias e sazonais que não são estruturais (Aula 10).
5. **Carimbo errado ou duplicado** — relógio do datalogger desacertado, fuso ou horário de verão.

### Limpeza e filtragem

Três ferramentas resolvem boa parte dos problemas. O **filtro de mediana** (por exemplo, a mediana de três leituras consecutivas) elimina picos isolados sem deslocar a tendência. A **média móvel** suaviza o ruído, mas **atrasa** a curva: uma média de 3 dias responde a uma aceleração com cerca de um dia de atraso. A **compensação térmica** usa a temperatura medida junto ao sensor para remover a parcela térmica. A **taxa de variação** (velocidade, em mm/dia) é muitas vezes mais reveladora que o valor absoluto: um deslocamento pequeno que acelera preocupa mais do que um grande que estabilizou. Toda limpeza deve ficar registrada: um pico "removido" pode ser o primeiro sinal de um problema real.

### Quanto dado e com que frequência?

A frequência de leitura define o volume de dados, a autonomia da bateria (Aula 3) e a capacidade de ver o fenômeno (Nyquist, Aula 2). Um piezômetro lido a cada 15 minutos gera 96 leituras por dia; 60 sensores assim produzem quase 6.000 pontos por dia e mais de 2 milhões por ano — sem contar os registros de vibração, que chegam a centenas de amostras por segundo durante um evento. Por isso, sistemas maduros guardam o **dado bruto completo**, mas exibem **agregados** (médias horárias, máximos diários) nos painéis, e usam **amostragem adaptativa**: leitura lenta na condição normal, rápida quando um nível de atenção é cruzado. Mais dado não é melhor dado: o que importa é ter a leitura certa, no momento certo, nas mãos de quem decide.

### Níveis de alerta e o plano de ação (TARP)

Os limites se organizam num **plano de ação por gatilhos** — em inglês, *Trigger Action Response Plan* (TARP) —, que para cada nível diz **o que acontece, quem faz e em quanto tempo**:

| Nível | Gatilho | Ação | Responsável |
| --- | --- | --- | --- |
| **Verde — normal** | dentro do esperado | leitura na frequência de rotina | equipe de instrumentação |
| **Amarelo — atenção** | valor **ou velocidade** acima do nível de atenção | aumentar a frequência, inspecionar, avisar o projetista (no mesmo dia) | engenheiro da obra |
| **Vermelho — alerta** | nível de alerta confirmado | executar as medidas de contingência previstas (reduzir ou paralisar a frente, reforçar), reunião técnica imediata | engenheiro responsável + projetista |

Três boas práticas reduzem a fadiga de alarmes: gatilhos por **valor e por velocidade**; **persistência** (exigir duas ou mais leituras consecutivas acima do limite, ou a confirmação por um segundo instrumento); e a **incerteza** da Aula 2 — se $x + U$ alcança o limite, trate como atenção; se $x - U$ passa do limite, o alerta está confirmado.

![Sala de controle com uma parede de monitores exibindo mapas e painéis de rastreamento em tempo real; um grupo de pessoas observa as telas, e à esquerda uma tela mostra dados de um dispositivo. Foto: UrusHyby, Wikimedia Commons, CC0](https://upload.wikimedia.org/wikipedia/commons/0/0d/Real-time_bus_tracking_control_room_in_Lebanon.jpg)

### Dashboards que levam à decisão

Um bom painel mostra: uma **planta da obra** com cada instrumento colorido pelo seu estado; **séries temporais com os limites desenhados** e a velocidade; a **saúde dos sensores** (bateria, hora da última leitura, sinal); e uma **lista de alarmes com reconhecimento** — quem viu, quando e o que fez. E evita: gráficos sem limites, eixos cortados que exageram variações, excesso de cores e, principalmente, **alarme sem dono**. Cada alerta precisa de um responsável, de um prazo e de uma ação.

### Exemplo numérico

Um marco de recalque automatizado registrou, em oito dias consecutivos (mm): 4,0; 4,2; 4,3; 4,5; **10,6**; 5,2; 5,9; 6,8. Os níveis do plano são: atenção em 10 mm, alerta em 15 mm e velocidade de atenção em 0,5 mm/dia.

**Pico espúrio.** O dia 5 salta 6,1 mm e volta no dia seguinte — fisicamente implausível. A mediana dos dias 4 a 6 é $\mathrm{med}(4{,}5;\,10{,}6;\,5{,}2) = 5{,}2\,\mathrm{mm}$, que substitui o valor (marcado como "corrigido"). Com regra de persistência de duas leituras, esse pico não teria disparado o alarme de atenção.

**Média móvel e velocidade.** A média móvel de 3 dias no dia 8 é $(5{,}2 + 5{,}9 + 6{,}8)/3 \approx 6{,}0\,\mathrm{mm}$ — abaixo do último valor, efeito do atraso. A taxa recente é

$
v = \frac{6{,}8 - 5{,}2}{2} = 0{,}8\,\mathrm{mm/dia} > 0{,}5\,\mathrm{mm/dia}
$

O valor absoluto ainda está longe da atenção, mas **a velocidade dispara o nível amarelo**. Mantido o ritmo, a atenção seria atingida em $(10 - 6{,}8)/0{,}8 = 4{,}0$ dias e o alerta em $(15 - 6{,}8)/0{,}8 \approx 10{,}3$ dias. Com a incerteza de $\pm 1{,}5\,\mathrm{mm}$ da Aula 2, a leitura de $6{,}8\,\mathrm{mm}$ está segura em valor ($6{,}8 + 1{,}5 < 10$) — mas é a tendência que manda agir agora.

### Atividade prática

Pegue uma série real (por exemplo, dados abertos de uma estação meteorológica) ou simule 30 dias de leituras numa planilha, com tendência, ciclo diário, ruído e alguns picos. Aplique a mediana de 3, a média móvel e calcule a velocidade. Depois, defina níveis de atenção e alerta por valor e por velocidade, monte a tabela TARP e esboce três telas de dashboard: planta com status, séries com limites e lista de alarmes.

### Pontos-chave

- Uma leitura é um registro completo: tempo (UTC), sensor, bruto, engenharia, unidade, qualidade e saúde; **nunca sobrescreva o bruto**.
- **Mediana** remove picos; **média móvel** suaviza, mas atrasa; a **velocidade** costuma avisar antes do valor absoluto.
- Níveis de alerta formam um **TARP**: gatilho, ação, responsável e prazo; persistência, redundância e incerteza reduzem a **fadiga de alarmes**.
- Um bom **dashboard** mostra status, limites, velocidade e saúde dos sensores — e todo alarme tem **dono**.

### Para saber mais

- **Wikipedia — Série temporal:** https://pt.wikipedia.org/wiki/S%C3%A9rie_temporal
- **Wikipedia — Média móvel:** https://pt.wikipedia.org/wiki/M%C3%A9dia_m%C3%B3vel
- **Grafana — documentação de alertas (*Grafana Alerting*):** https://grafana.com/docs/grafana/latest/alerting/

### O que você verá na próxima unidade

Na **Unidade 4 — Integração, Inteligência e Gestão do Monitoramento**, os dados dos drones e dos sensores vão se juntar. Você vai integrar o monitoramento ao **BIM** e ao **gêmeo digital** (4D e comparação *as-built* × *as-designed*), usar **inteligência artificial e visão computacional** para detectar fissuras e medir avanço físico, tratar da **gestão** do monitoramento — custo-benefício, **LGPD**, segurança da informação e contratos — e, para fechar, desenvolver o **projeto integrado** de monitoramento de uma obra.

## Aula 12 — Roteiro da Videoaula 12: "Dados de sensores: séries temporais, níveis de alerta e dashboards"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e os 37 alarmes do fim de semana.

> "Trinta e sete alarmes no fim de semana; trinta e cinco falsos. Na terceira semana, ninguém olhava mais o painel — e um dos alarmes era real. Hoje: como transformar séries de sensores em decisões confiáveis."

### 2. Desenvolvimento — parte 1 (0:25 – 1:20)

**[TELA]** Slides 4–7 — anatomia de uma leitura, os cinco defeitos, a simulação de limpeza e as oito leituras do exemplo.

> "Cada leitura tem tempo em UTC, sensor, valor bruto, valor de engenharia, qualidade e saúde — e o bruto nunca é sobrescrito. Todo dado de campo tem picos, lacunas, deriva, ciclo térmico e relógio errado. A mediana tira o pico; a média móvel suaviza, mas atrasa. No exemplo, o 10,6 do quinto dia vira 5,2 pela mediana, e a taxa recente é de 0,8 milímetro por dia."

### 3. Desenvolvimento — parte 2 (1:20 – 2:15)

**[TELA]** Slides 8–11 — o TARP, a simulação de persistência, a calculadora de tempo até o alerta e a incerteza nos limiares.

> "Os níveis viram um plano de ação: verde, amarelo, vermelho, cada um com ação, responsável e prazo. Gatilho por valor e por velocidade. Exigir duas leituras seguidas corta os alarmes falsos, mas atrasa a detecção do evento real — é um compromisso. No exemplo, 6,8 milímetros estão longe da atenção, mas a 0,8 por dia ela chega em 4 dias. A velocidade manda agir agora."

### 4. Desenvolvimento — parte 3 (2:15 – 3:00)

**[TELA]** Slides 12–14 — o que um bom dashboard mostra, o painel simulado e a ponte para o gêmeo digital.

> "Um bom dashboard mostra a planta com status, as séries com os limites desenhados, a velocidade e a saúde dos sensores — e uma lista de alarmes com dono. Vamos simular um evento: o inclinômetro acelera, fica amarelo, entra no log, o engenheiro de plantão reconhece. E o próximo passo é levar esses números para dentro do modelo da obra: o gêmeo digital."

### 5. Encerramento (3:00 – 3:40)

**[TELA]** Slides 15–19 — atividade, pontos-chave, fechamento da unidade, prévia da Unidade 4 e encerramento.

> "Com esta aula, você fecha a unidade dos sensores: geotecnia, estrutura, entorno e dados. Na Unidade 4, drones e sensores se encontram no BIM e no gêmeo digital, com inteligência artificial, LGPD, contratos e um projeto integrado. Foi um prazer! Te espero lá."

---

## Quiz não avaliativo

### Questão 1

Um inclinômetro instalado atrás de uma cortina de estacas, com o pé previsto em solo indeslocável, apresenta, em relação à leitura zero, deslocamento de 10 mm no topo e deslocamentos que diminuem gradualmente até zero a cerca de 3 m de profundidade, sem variação nos trechos inferiores. Há 7 dias, o topo indicava 7 mm. Com base nos conceitos da aula, assinale a alternativa **correta**:

- [ ] a. O deslocamento no topo é obtido multiplicando-se o ângulo medido no trecho superior pela profundidade total do tubo, sem necessidade de leitura zero.
- [x] b. O perfil é coerente com o pé fixo, e a velocidade de cerca de 0,43 mm/dia deve ser comparada aos limites do plano, além do valor absoluto.
- [ ] c. Como o deslocamento é nulo nos trechos inferiores, o instrumento está com defeito e as leituras devem ser descartadas.
- [ ] d. A segunda passada com a sonda girada 180° serve apenas para dobrar a resolução, e pode ser dispensada em campanhas rotineiras.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) está correta: o deslocamento acumula-se de baixo para cima a partir do pé fixo, de modo que trechos inferiores sem variação são exatamente o esperado; e a velocidade, $(10 - 7)/7 \approx 0{,}43\,\mathrm{mm/dia}$, é informação tão importante quanto o valor absoluto para os níveis de alerta. A (a) erra duas vezes: o deslocamento é a soma de $L\,\sin\theta$ trecho a trecho, e sempre em relação à leitura zero. A (c) inverte a lógica: deslocamento nulo no fundo confirma a premissa de pé indeslocável. A (d) é falsa: a passada a 180° cancela o viés do sensor, o que é essencial para a exatidão.

### Questão 2

O painel de monitoramento de uma escavação disparou dezenas de alarmes de atenção no último mês, quase todos causados por picos isolados de leitura, e a equipe começou a ignorá-los. O engenheiro quer reduzir os falsos alarmes **sem** perder a capacidade de detectar um deslocamento real que esteja acelerando. Assinale a alternativa **correta**:

- [ ] a. Elevar o nível de atenção para o valor do nível de alerta, de modo que só eventos graves gerem mensagens.
- [ ] b. Substituir as leituras por uma média móvel de 7 dias, que elimina os picos e não altera o momento de detecção de uma tendência.
- [ ] c. Desligar os alarmes automáticos e passar a analisar os gráficos na reunião semanal, onde o contexto é discutido com calma.
- [x] d. Aplicar filtro de mediana e regra de persistência (ou confirmação por outro instrumento) e incluir um gatilho por velocidade.

**Resposta correta:** `d`

**Feedback:** A alternativa (d) está correta: a mediana remove picos isolados sem deslocar a tendência; a persistência (duas ou mais leituras consecutivas) ou a confirmação por um segundo instrumento evita disparos por uma única leitura espúria; e o gatilho por velocidade detecta a aceleração antes de o valor absoluto atingir o limite. A (a) elimina o nível de atenção, perdendo o tempo de reação. A (b) erra ao dizer que a média móvel não atrasa a detecção: quanto maior a janela, maior o atraso. A (c) volta à malha aberta da Unidade 1, com leitura que não é comparada a tempo.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma construtora executa uma escavação de $10\,\mathrm{m}$ para três subsolos, contida por cortina de estacas atirantada, em área urbana. De um lado há um **edifício residencial de 6 pavimentos com fundação rasa**; do outro, um **casarão tombado** de alvenaria, a 15 m da linha de estacas-prancha que estão sendo cravadas para uma rampa. O plano de monitoramento já instalou inclinômetros, piezômetros de corda vibrante, marcos de recalque automatizados, um sismógrafo de engenharia no casarão e uma plataforma IoT com dashboard. Os níveis do plano (valores ilustrativos) são: inclinômetro — atenção 12 mm, alerta 20 mm; recalque — atenção 12 mm, alerta 20 mm, velocidade de atenção 0,5 mm/dia; distorção angular — alerta em 1/500; vibração no casarão — atenção 3 mm/s, alerta 5 mm/s.
>
> Responda em quatro partes:
>
> 1. **Instrumentação** — justifique a posição e a função de cada instrumento citado e indique a leitura zero e a frequência de leitura durante a escavação. Que instrumento você acrescentaria e por quê?
> 2. **Cálculos** — (a) o inclinômetro ($L = 0{,}5\,\mathrm{m}$) registra variações de $\sin\theta$ de $8{,}0$; $6{,}0$; $4{,}0$; $2{,}0$ e $1{,}0 \times 10^{-3}$ nos cinco trechos superiores, sem variação abaixo: calcule o deslocamento no topo. (b) Os pilares P1 e P2 do edifício, a $4{,}0\,\mathrm{m}$ um do outro, recalcaram $17\,\mathrm{mm}$ e $5\,\mathrm{mm}$: calcule a distorção angular e classifique-a pela escala de Bjerrum. (c) O sismógrafo do casarão registrou PPV de $9\,\mathrm{mm/s}$ a $8\,\mathrm{Hz}$: compare com a NBR 9653 e com os limites do plano. (d) As três últimas leituras diárias do recalque de P1 foram $15{,}2$; $16{,}1$ e $17{,}0\,\mathrm{mm}$: calcule a velocidade e em quantos dias, mantido o ritmo, o nível de alerta seria atingido.
> 3. **Níveis e dashboard** — classifique cada grandeza (verde, amarelo ou vermelho) e descreva o que o dashboard deve mostrar e quem deve ser avisado, com que prazo.
> 4. **Decisão** — com base nos resultados, que ações você toma agora? O que pode ser automático e o que exige decisão humana?

**Resposta esperada:**

> **Parte 1.** Inclinômetros atrás da cortina, com o pé abaixo da zona de influência da escavação (deslocamento horizontal da contenção e do solo); piezômetros de corda vibrante atrás da cortina e junto aos poços de rebaixamento (poropressão, resposta rápida e leitura automática); marcos de recalque nos pilares do edifício e no casarão, referidos a uma referência de nível profunda fora da zona de influência (recalques e distorção angular); sismógrafo com geofone triaxial no pé do casarão (PPV e frequência durante a cravação). Leitura zero antes da escavação (repetida duas ou três vezes); durante a escavação, leituras automáticas de 15 a 60 min nos instrumentos críticos e eventos de vibração registrados por gatilho. Acréscimos pertinentes: **células de carga nos tirantes**, **fissurômetros** nas fissuras pré-existentes do casarão (mapeadas em vistoria cautelar), **clinômetros de parede**, sonômetro e sensor de MP10 na divisa.
>
> **Parte 2.**
>
> (a) $\delta_{topo} = 0{,}5 \times (8{,}0 + 6{,}0 + 4{,}0 + 2{,}0 + 1{,}0) \times 10^{-3} = 0{,}5 \times 0{,}021 = 0{,}0105\,\mathrm{m} = 10{,}5\,\mathrm{mm}$ → abaixo da atenção (12 mm).
>
> (b) $\delta = 17 - 5 = 12\,\mathrm{mm}$; $\beta = 12/4.000 = 0{,}003 = 1/333$ → entre 1/500 (limite para edifícios em que não se admitem fissuras) e 1/300 (primeiras fissuras em alvenaria): **acima do alerta do plano** (1/500).
>
> (c) Limite da NBR 9653 a 8 Hz: $15 + 5 \times (8 - 4)/11 \approx 16{,}8\,\mathrm{mm/s}$; $9/16{,}8 \approx 54\%$. Pela norma de desmonte, não haveria problema; mas o plano do casarão tombado fixou alerta em 5 mm/s, e **9 mm/s está acima do alerta do plano**. A boa resposta destaca que a NBR 9653 trata de explosivos e que edificações sensíveis pedem limites próprios.
>
> (d) $v = (17{,}0 - 15{,}2)/2 = 0{,}9\,\mathrm{mm/dia}$ (acima da velocidade de atenção de 0,5 mm/dia); dias até o alerta de 20 mm: $(20 - 17{,}0)/0{,}9 \approx 3{,}3$ dias. O valor absoluto (17 mm) já está acima da atenção (12 mm).
>
> **Parte 3.** Inclinômetro: **verde** (10,5 < 12 mm), mas deve-se acompanhar a velocidade. Recalque de P1: **amarelo** por valor e por velocidade, com projeção de alerta em cerca de 3 dias. Distorção angular: **vermelho** (1/333 > 1/500). Vibração no casarão: **vermelho** (9 > 5 mm/s). O dashboard deve mostrar a planta com os instrumentos coloridos por estado, as séries com os limites e a velocidade, a saúde dos sensores (bateria, última leitura) e a lista de alarmes com reconhecimento. Avisar de imediato o engenheiro responsável e o projetista (níveis vermelhos), com reunião técnica no mesmo dia; o nível amarelo dispara aumento de frequência e inspeção do edifício.
>
> **Parte 4.** Ações: **interromper ou reduzir a energia da cravação** junto ao casarão e avaliar métodos alternativos (estacas escavadas ou prensadas, pré-furo), confirmando o efeito com novas leituras do sismógrafo; **vistoriar o edifício** e o casarão (fissuras novas?), confirmar a leitura de recalque com nivelamento manual ou segundo instrumento; acionar as medidas de contingência previstas para o recalque (por exemplo, reduzir a frente de escavação próxima a P1, antecipar tirantes, reavaliar o rebaixamento, se os piezômetros indicarem relação). Automático: aumentar a frequência de leitura, notificar a equipe, registrar o evento, eventualmente sinalizar ao operador da cravação para parar. Decisão humana: paralisar frentes, alterar o método executivo, reforçar a contenção, evacuar ou interditar áreas. Resposta exemplar articula as quatro partes, usa as unidades corretamente, distingue norma de referência e limite de projeto e fecha a malha: ação seguida de nova medição para verificar o efeito.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> _[PENDENTE — aguardando acesso à Biblioteca Virtual]_

- **Nome do livro:** 
- **Capítulo:** 
- **Organizador:** 
- **Editora:** 
- **Link de acesso (BV):** 
- **Aula em que entra:** 

### Para mergulhar no assunto

> Para ver a instrumentação geotécnica do ponto de vista de quem projeta e lê os instrumentos, assista à primeira aula do curso **"Instrumentação, Interpretação de Dados e Monitoramento de Estruturas Geotécnicas"**, da Effyía — Escola da Engenharia, no YouTube (cerca de 31 minutos). Para a maturidade do concreto, a palestra **"Método da maturidade do concreto"**, do canal Engenharia Civil Mackenzie (cerca de 57 minutos), mostra a calibração da curva e o uso de sensores embutidos em obra. Assista com as perguntas desta unidade em mente: qual é a leitura zero? Quais são os limites? Que ação cada leitura dispara?

- **Link(s):** https://www.youtube.com/watch?v=5hwJUP5wIfY · https://www.youtube.com/watch?v=hmVx4cm7deM
- **Aula em que entra:** Aulas 9 e 10

### Podcast (curadoria, até 45 min)

> No episódio 3 da 2ª temporada do **I&M Geotech Podcast**, canal brasileiro dedicado à instrumentação e ao monitoramento geotécnico, os convidados Roberto Collado Bermejo e David José Mendi Fernandez, da Geprode, falam da gestão da instrumentação nas obras da **Linha 6 do Metrô de São Paulo**: automação das leituras, volume de dados e resposta a alertas — tudo o que vimos nas Aulas 9 e 12. O episódio completo tem cerca de 73 minutos; para esta curadoria, ouça os **primeiros 45 minutos**.

- **Nome do podcast/canal:** I&M Geotech: Instrumentação e Monitoramento Geotécnico (canal no YouTube)
- **Tema recomendado:** T02 | EP03 — Instrumentação da Linha 6 do Metrô de São Paulo (Roberto Collado Bermejo e David José Mendi Fernandez)
- **Link:** https://www.youtube.com/watch?v=jQpQFHHl_Zo
- **Aula em que entra:** Aulas 9 e 12

### Artigo científico

> Revisão sobre o uso de **sistemas IoT sem fio no monitoramento da saúde estrutural** (SHM) de obras civis. Os autores reúnem estudos de caso em estruturas reais e investigações de laboratório, com aplicações como **controle de vibração e da qualidade da cura do concreto**, **detecção de fissuras** em edificações, avaliação da qualidade construtiva, diagnóstico de corrosão e avaliação de vulnerabilidade sísmica, e concluem que o SHM baseado em IoT pode aumentar a segurança das estruturas. É a fundamentação acadêmica da Aula 10 e conversa com o tratamento de dados da Aula 12 e com a arquitetura IoT da Aula 3.

- **Link:** https://doi.org/10.1016/j.jobe.2021.103954
- **Aula em que entra:** Aulas 10 e 12
- **Referência bibliográfica do artigo no formato ABNT:**
  > MISHRA, Mayank; LOURENÇO, Paulo B.; RAMANA, G. V. Structural health monitoring of civil engineering structures by using the internet of things: a review. **Journal of Building Engineering**, v. 48, 103954, 2022. DOI: 10.1016/j.jobe.2021.103954.
