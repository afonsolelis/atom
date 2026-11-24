# Unidade 3 — Sensores IoT e Redes de Comunicação

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 9 a 12

## Aula 9 — Sensores para obras: inclinômetros, extensômetros, acelerômetros, temperatura, umidade e poeira

> Segunda-feira, 7h, numa obra de três subsolos em área urbana. A cortina de estacas está sendo escavada ao lado de um prédio antigo; uma escora metálica, ao sol da tarde, parece "ganhar" carga; a laje do térreo foi concretada no sábado; a equipe de pintura quer começar a impermeabilização num dia úmido; e a vizinhança reclama da poeira. São cinco perguntas diferentes, e todas têm a mesma resposta: **medir**. Mas medir o quê, com qual sensor e com que cuidado? Nesta aula, você vai conhecer os sensores mais usados no monitoramento de obras — **inclinômetros, extensômetros, acelerômetros e sensores de temperatura, umidade e poeira** — e aprender o que cada um mede, como funciona e onde costuma enganar.

### O que você verá nesta unidade

Na Unidade 2, o drone olhou a obra de cima. Agora o monitoramento desce para dentro do solo, da estrutura e do ar do canteiro. Nesta unidade, você vai seguir o caminho completo de um dado de sensor: na **Aula 9**, os sensores e as grandezas que eles medem; na **Aula 10**, as plataformas embarcadas (Arduino, ESP32 e dataloggers) que condicionam, digitalizam, alimentam e instalam esses sensores em campo; na **Aula 11**, as redes que levam o dado para fora do canteiro — LoRaWAN, Wi-Fi e redes celulares —; e, na **Aula 12**, os protocolos e as plataformas que recebem e guardam as leituras — MQTT, Node-RED e bancos de séries temporais como o InfluxDB. É a "internet das coisas" aplicada ao canteiro, no sentido discutido por Magrani (2018): objetos do dia a dia que passam a coletar e trocar dados sem intervenção humana a cada leitura.

### Do fenômeno ao sensor: escolher pelo mensurando

Todo projeto de instrumentação começa pela **grandeza** e pelo **mensurando** — o valor específico que se quer conhecer: "o deslocamento horizontal da cortina a 3 m de profundidade", e não apenas "o movimento do solo". Com o mensurando definido, o sensor é escolhido por cinco critérios: **faixa** de medição, **resolução**, **incerteza** (resolução não é exatidão: um visor com três casas decimais pode errar por um milímetro inteiro), **estabilidade a longo prazo** (deriva) e **robustez** às condições de campo. E todo sensor precisa de **calibração rastreável**, de **leitura zero** e de **limites e ações** definidos antes de a obra começar.

### Inclinômetros: deslocamento horizontal em profundidade

O **inclinômetro** mede o deslocamento horizontal ao longo da profundidade. Instala-se um **tubo-guia** com quatro ranhuras internas num furo vertical atrás da contenção, com o pé engastado em solo ou rocha que **não se mova**. Uma **sonda** com acelerômetros, que corre pelas ranhuras, é lida a cada $L = 0{,}5\,\mathrm{m}$ e mede a inclinação $\theta$ de cada trecho; o desvio horizontal do trecho é $d = L\,\sin\theta$. O deslocamento é sempre a **diferença em relação à leitura zero**, acumulada **de baixo para cima** a partir do pé fixo, e faz-se uma segunda passada com a sonda girada 180°, que cancela o viés do sensor. Para leitura automática, há os **inclinômetros in-place** (cadeias de sensores MEMS no tubo) e os **clinômetros de parede**, que medem a rotação de pilares e fachadas.

### Extensômetros: da deformação à força

O **extensômetro** mede deformação específica, em **microdeformações** ($1\,\mu\varepsilon = 10^{-6}$). No **extensômetro elétrico de resistência**, uma grade metálica colada à peça muda de resistência com a deformação: $\Delta R/R = GF\,\varepsilon$, com fator do extensômetro $GF \approx 2$. É rápido, mas sofre com umidade e deriva. Para o longo prazo, a obra usa o **extensômetro de corda vibrante**: um fio tensionado entre dois blocos fixados à peça, cuja frequência de vibração $f$ varia com a deformação ($\varepsilon \propto f^2$). É estável por anos e pode ser soldado em escoras ou embutido no concreto.

![Duas mãos amarram, com abraçadeiras plásticas brancas, um extensômetro com fios vermelhos a barras de armadura e cordoalhas de uma viga, antes da concretagem; ao fundo, outras barras verticais da armação. Foto: Federal Highway Administration, Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/6/60/Strain_Gauge_Installation_in_SCC_Beams-2_SC_%288496265082%29.jpg)

No regime elástico, a tensão vem da lei de Hooke, $\sigma = E\,\varepsilon$, e a força, de $N = \sigma\,A$. A armadilha é a **temperatura**: o aço dilata cerca de $12 \times 10^{-6}/^\circ\mathrm{C}$, e 15 °C de variação diária dão cerca de 180 µε, da ordem do sinal. Numa escora travada, parte dessa dilatação é impedida e vira **força térmica real**; outra parte vem da diferença entre fio e peça. Por isso, o extensômetro de corda vibrante traz um **termistor**, e a fórmula do fabricante **separa a parcela térmica** da causada pela escavação.

### Acelerômetros: vibração e assinatura dinâmica

O **acelerômetro** mede aceleração. Os **MEMS** (microssistemas eletromecânicos em chip) são baratos e de baixo consumo, ideais para IoT; os **piezoelétricos** têm mais sensibilidade e faixa de frequência. Eles medem a **vibração** induzida pela obra (cravação, compactação), avaliada nos vizinhos pela velocidade de partícula de pico, em mm/s, e as **frequências naturais** da estrutura. Num modelo de massa e mola, $f = \frac{1}{2\pi}\sqrt{k/m}$: se a rigidez $k$ cai por dano, a frequência cai junto, e $f_2/f_1 = \sqrt{k_2/k_1}$ — 5% a menos na frequência correspondem a cerca de 10% a menos na rigidez. Para registrar vibração, vale o critério de Nyquist: amostrar a mais que o dobro — na prática, de 5 a 10 vezes — a maior frequência de interesse.

![Acelerômetro com unidade de sensor sem fio fixado na base de um pendural de uma ponte em arco metálico, junto ao guarda-corpo, com um caminhão passando ao fundo na pista. Foto: Y. Lei, W. A. Shen, Y. Song, Y. Wang, Wikimedia Commons, CC BY 4.0](https://upload.wikimedia.org/wikipedia/commons/7/7e/Accelerometer-with-wireless-sensor-on-a-hanger.jpg)

### Temperatura: o sensor que corrige todos os outros

A temperatura é medida por **termistores** (NTC, baratos e sensíveis), **termorresistências** (Pt100, estáveis e exatas) e **termopares** (ampla faixa, mas exigem compensação da junta fria). Na obra, ela tem três papéis. Primeiro, **corrigir outros sensores** — extensômetros, fissurômetros e piezômetros de corda vibrante. Segundo, controlar a **cura do concreto**: pelo método da maturidade (ASTM C1074), o fator temperatura-tempo de Nurse-Saul, $M = \sum (T - T_0)\,\Delta t$, estima a resistência nas primeiras idades a partir de uma curva calibrada para a mesma mistura, apoiando decisões de desforma — sem substituir o controle por corpos de prova. Terceiro, vigiar o **gradiente térmico** em concreto massa (blocos de fundação), em que a diferença entre o núcleo e a superfície pode fissurar a peça; o limite é fixado no projeto.

### Umidade: do ar, do concreto e do solo

A **umidade relativa do ar** (UR) é medida por sensores **capacitivos** — um polímero cuja constante dielétrica varia com o vapor d'água absorvido —, quase sempre integrados a um sensor de temperatura no mesmo chip. Na obra, UR e temperatura definem o **ponto de orvalho**: se uma superfície estiver abaixo dele, haverá condensação, o que compromete pintura, impermeabilização e colagem de revestimentos. Uma regra comum de especificações de pintura é exigir a superfície pelo menos 3 °C acima do ponto de orvalho. A umidade também é medida **dentro** dos materiais: sondas de UR em furos na laje indicam quando o concreto está seco o bastante para receber piso (método da ASTM F2170, com o limite dado pelo fabricante do revestimento), e sensores capacitivos ou de TDR medem a **umidade do solo** em aterros e taludes, em que a chuva reduz a resistência.

![Placa eletrônica vermelha com o sensor de umidade e temperatura Si7021, um pequeno chip com janela branca, ao lado de quatro furos de conexão marcados para alimentação e comunicação. Foto: SparkFun, Wikimedia Commons, CC BY 2.5](https://upload.wikimedia.org/wikipedia/commons/4/48/SparkFun_Humidity_and_Temperature_Sensor_Breakout_-_Si7021_13763-01a.jpg)

### Poeira: MP10 e MP2,5

A poeira de obra é monitorada como **material particulado** com diâmetro até 10 µm (**MP10**) e até 2,5 µm (**MP2,5**), que penetram no sistema respiratório. Os sensores IoT mais comuns são **óticos de espalhamento de luz**: um ventilador ou um canal de convecção faz o ar passar por um feixe de LED ou laser, e um fotodetector mede a luz espalhada pelas partículas. São baratos e de baixo consumo, mas **superestimam a concentração com umidade alta** (as partículas absorvem água e "incham") e precisam ser **calibrados por colocalização** com uma estação de referência. Os padrões nacionais de qualidade do ar estão na **Resolução CONAMA nº 506/2024**; na etapa em vigor desde 2025, a média de 24 h é de 100 µg/m³ para MP10 e 50 µg/m³ para MP2,5. São padrões de **ar ambiente**, não limites de emissão: o plano da obra fixa gatilhos na divisa e as ações (aspersão, lavagem de rodas).

![Sensor ótico de poeira GP2Y1010AU0F: invólucro metálico com um furo central por onde o ar passa diante do emissor de luz, fixado a uma placa azul e ligado por um conector a fios coloridos. Foto: wdwd, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/f/f2/Dust_sensor_GP2Y1010AU0F.JPG)

![Escavadeira com rompedor demolindo uma estrutura elevada de concreto enquanto um jato de água, lançado de trás de um tapume, molha o ponto de demolição para controlar a poeira. Foto: MassDOT, Wikimedia Commons, domínio público](https://upload.wikimedia.org/wikipedia/commons/e/e8/Dust_control_for_Lechmere_Elevated_demolition%2C_June_2020.jpg)

### Exemplo numérico

**(a) Do ângulo ao milímetro.** A sonda do inclinômetro ($L = 0{,}5\,\mathrm{m}$) registra, em relação à leitura zero, variações de $\sin\theta$ apenas nos seis trechos superiores: $6{,}0$; $5{,}0$; $4{,}0$; $3{,}0$; $1{,}6$ e $0{,}4 \times 10^{-3}$. O deslocamento no topo é

$
\delta_{topo} = L \sum \Delta(\sin\theta) = 0{,}5 \times 0{,}020 = 0{,}010\,\mathrm{m} = 10{,}0\,\mathrm{mm}
$

**(b) Quanto a escora está carregando?** Um extensômetro de corda vibrante numa escora de aço ($E = 200\,\mathrm{GPa}$, $A = 120\,\mathrm{cm^2}$) indica, já corrigido para a temperatura, $\Delta\varepsilon = 250\,\mu\varepsilon$:

$
\sigma = 200.000 \times 250 \times 10^{-6} = 50\,\mathrm{MPa}
\qquad
N = 50\,\mathrm{MPa} \times 0{,}012\,\mathrm{m^2} = 0{,}6\,\mathrm{MN} = 600\,\mathrm{kN}
$

Com carga de projeto de 900 kN (valor ilustrativo), a escora está a 67% dela.

**(c) Pode impermeabilizar?** O sensor registra $T = 20\,^\circ\mathrm{C}$ e $UR = 80\%$. Pela aproximação de Magnus ($a = 17{,}62$; $b = 243{,}12\,^\circ\mathrm{C}$):

$
\gamma = \ln(0{,}80) + \frac{17{,}62 \times 20}{243{,}12 + 20} \approx -0{,}223 + 1{,}339 = 1{,}116
\qquad
T_{orv} = \frac{243{,}12 \times 1{,}116}{17{,}62 - 1{,}116} \approx 16{,}4\,^\circ\mathrm{C}
$

Uma laje a 18 °C está só 1,6 °C acima do ponto de orvalho, abaixo da margem de 3 °C: a aplicação deve esperar.

### Atividade prática

Para a obra do gancho, monte uma tabela com os seis sensores da aula e as colunas: mensurando, local de instalação, princípio de funcionamento, principal fonte de erro, correção ou calibração e decisão que a leitura apoia (reforçar uma escora, liberar uma laje, adiar a pintura, ligar a aspersão).

### Pontos-chave

- Escolha o sensor pelo **mensurando** (faixa, resolução, incerteza, deriva e robustez); todo sensor precisa de calibração, **leitura zero** e limites com ação definida.
- **Inclinômetros** dão deslocamento em profundidade ($d = L\,\sin\theta$, acumulado a partir do pé fixo); **extensômetros** dão deformação, que vira força por $\sigma = E\,\varepsilon$ e $N = \sigma\,A$ depois da correção térmica.
- **Acelerômetros** medem vibração e frequências naturais ($f_2/f_1 = \sqrt{k_2/k_1}$), respeitando Nyquist; a **temperatura** corrige os demais sensores e controla a cura (maturidade).
- **Umidade** define o ponto de orvalho e a secagem de lajes e solos; sensores óticos de **poeira** (MP10, MP2,5) exigem calibração por colocalização e erram com umidade alta.

### Para saber mais

- **MISHRA, M.; LOURENÇO, P. B.; RAMANA, G. V. — *Structural health monitoring of civil engineering structures by using the internet of things: a review* (Journal of Building Engineering, 2022):** https://doi.org/10.1016/j.jobe.2021.103954
- **CARINO, N. J.; LEW, H. S. — *The Maturity Method: From Theory to Application* (NIST, 2001):** https://www.nist.gov/publications/maturity-method-theory-application
- **Wikipedia — Ponto de orvalho:** https://pt.wikipedia.org/wiki/Ponto_de_orvalho
- **Wikipedia — Material particulado:** https://pt.wikipedia.org/wiki/Material_particulado

## Aula 9 — Roteiro da Videoaula 9: "O que a obra sente e ninguém vê: seis sensores que contam tudo"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–4 — capa, sumário, a obra de três subsolos com cinco perguntas e o mapa da unidade.

> "Uma escavação ao lado de um prédio antigo, uma escora no sol, uma laje recém-concretada, a pintura num dia úmido e a poeira na vizinhança. Cinco perguntas, uma resposta: medir. Nesta unidade, você vai seguir o dado do sensor até o banco de dados. E hoje começamos pelo começo: os sensores."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 5–7 — do fenômeno ao sensor, o inclinômetro e o exemplo do ângulo ao milímetro.

> "Sensor se escolhe pelo mensurando: faixa, resolução, incerteza, deriva e robustez. E todo sensor começa com uma leitura zero. O inclinômetro mede o deslocamento em profundidade: L vezes o seno do ângulo, trecho a trecho, de baixo para cima. No exemplo, meio metro vezes 0,020 dá 10 milímetros no topo."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 8–10 — extensômetros, a escora no sol e os acelerômetros.

> "O extensômetro de corda vibrante é o cavalo de batalha da obra. Duzentas e cinquenta microdeformações dão 600 quilonewtons na escora — mas 15 graus de sol valem 180 microdeformações. Sem separar a parcela térmica, a variação do dia é confundida com efeito da escavação. O acelerômetro mede vibração e a assinatura da estrutura: se a rigidez cai, a frequência cai junto."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 11–15 — temperatura e maturidade, umidade e a calculadora do ponto de orvalho, poeira, a tabela dos seis sensores e o laboratório. Slide 15 — laboratório no simulador da obra Torre A: o cenário Escora no sol, com a carga aparente do E-01 passando de 960 kN entre o fim da manhã e o meio da tarde e voltando a cerca de 600 kN com a compensação térmica ligada.

> "A temperatura corrige os outros sensores e diz quando a laje pode ser desformada. A umidade diz se dá para impermeabilizar: 20 graus e 80% dão ponto de orvalho de 16,4 graus; laje a 18 graus, espera. E o sensor de poeira é barato, mas superestima com o ar úmido: calibre ao lado de uma estação de referência."

### 5. Encerramento
**[TELA]** Slides 16–18 — atividade, pontos-chave e encerramento.

> "Você conheceu os seis sensores. Mas um sensor sozinho só dá um sinal elétrico fraquinho. Quem transforma isso em número, guarda e alimenta tudo no meio da obra? As plataformas embarcadas: Arduino, ESP32 e datalogger. Te espero na Aula 10!"

---

## Aula 10 — Plataformas embarcadas e coleta de dados em campo

> Um estagiário montou, num fim de semana, um protótipo com uma placa ESP32, um extensômetro colado numa escora e um rádio. Na segunda-feira, o gráfico mostrava uma linha perfeitamente reta — a escora parecia não carregar nada. Na terça, a bateria acabou. Na quarta, a chuva entrou na caixa. O sensor estava certo; o que falhou foi **tudo o que fica entre o sensor e o número**: o condicionamento do sinal, a conversão analógico-digital, a energia e a instalação. Nesta aula, você vai abrir essa caixa e entender como **plataformas embarcadas** — Arduino, ESP32 e dataloggers — coletam dados confiáveis em campo.

### A cadeia de medição embarcada

Entre a grandeza física e o dado na rede há uma cadeia: **sensor** (responde à grandeza) → **condicionamento** (excita, amplifica, filtra e adapta o sinal) → **conversor analógico-digital** (ADC, transforma tensão em número) → **microcontrolador** (aplica a calibração, carimba o tempo e decide quando ler e transmitir) → **memória local** e **rádio** — tudo alimentado por uma fonte de **energia**. A qualidade do dado é a do elo mais fraco: um sensor excelente ligado a um ADC ruidoso produz uma leitura ruim.

### Condicionamento de sinal

Muitos sensores entregam sinais fracos ou em formatos que o microcontrolador não lê diretamente. Os casos típicos são:

- **Ponte de Wheatstone** — o extensômetro elétrico é montado numa ponte de quatro resistores excitada por uma tensão $V_{ex}$. Com um único extensômetro ativo (um quarto de ponte), a saída é $V_o \approx V_{ex}\,GF\,\varepsilon/4$: microvolts, que exigem **amplificador de instrumentação** antes do ADC.
- **Laço de corrente 4–20 mA** — padrão industrial imune a ruído e à resistência de cabos longos. O "zero vivo" de 4 mA permite distinguir leitura nula de **cabo rompido** (0 mA). Um resistor de carga converte corrente em tensão: com 120 Ω, 4–20 mA viram 0,48–2,40 V, dentro da faixa de medição precisa do ADC do ESP32.
- **Corda vibrante** — o sensor precisa ser excitado e ter a sua **frequência** medida, o que exige uma interface específica, comum em dataloggers profissionais.
- **Filtro anti-aliasing** — um filtro passa-baixas antes do ADC impede que frequências acima da metade da taxa de amostragem apareçam como sinais falsos.

![Diagrama de uma ponte de Wheatstone com quatro extensômetros: R1 e R3 em compressão, R2 e R4 em tração, alimentada pela tensão de excitação V_EX à esquerda, com a tensão de saída V_o medida entre os dois nós centrais. Figura: Daraceleste, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/3/37/Wheatstone_bridge_with_gauges.jpg)

### Conversão analógico-digital

Um ADC de $n$ bits divide a faixa de entrada em $2^n$ níveis; o menor degrau, o **LSB**, vale $V_{ref}/2^n$. O **Arduino Uno** (microcontrolador ATmega328P) tem ADC de 10 bits em 0–5 V: $5/1.024 \approx 4{,}9\,\mathrm{mV}$ por nível. O **ESP32** tem ADC de 12 bits (0 a 4.095), com faixa de medição precisa de cerca de 0,15–2,45 V na atenuação de 11 dB (fora dela, a resposta deixa de ser linear), mas é conhecido por **não linearidade e desvio** de uma placa para outra — por isso, deve ser calibrado ou substituído por um ADC externo: o **ADS1115** (16 bits) para tensões em geral e o **HX711** (24 bits, com ganho interno) para pontes de extensômetros e células de carga. Muitos sensores modernos já entregam o valor **digital**, por barramentos como **I²C** e **SPI** (curta distância, na mesma placa), **UART**, **1-Wire** (termômetros DS18B20), **SDI-12** (sensores ambientais) e **RS-485/Modbus** (equipamentos industriais, centenas de metros de cabo).

### Arduino, ESP32 e o datalogger profissional

O **Arduino** é a porta de entrada: simples, com enorme comunidade, ótimo para aprender e prototipar, mas sem rádio nativo. O **ESP32**, da Espressif, é um microcontrolador de 32 bits com **Wi-Fi e Bluetooth integrados**, modo de sono profundo (*deep sleep*) e preço baixo — a escolha natural para protótipos IoT, programável na própria IDE do Arduino. O **datalogger profissional** é outra categoria: entradas para corda vibrante e pontes, multiplexadores para dezenas de canais, faixa de temperatura estendida, caixa com grau de proteção elevado, relógio estável, memória para meses de leituras e certificado de calibração.

![Placa de desenvolvimento ESP32, com o módulo metálico que integra o processador e o rádio Wi-Fi e Bluetooth, conector micro-USB e duas fileiras de pinos, fixada sobre uma placa acrílica ao lado de uma matriz de contatos (protoboard). Foto: Edwiyanto, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/c/c2/ESP32_Dev_Board.jpg)

![Placa Arduino Uno R3 azul, com o conector USB tipo B, a entrada de alimentação, o microcontrolador e as barras de pinos digitais e analógicos nas bordas. Foto: SparkFun Electronics, Wikimedia Commons, CC BY 2.0](https://upload.wikimedia.org/wikipedia/commons/3/38/Arduino_Uno_-_R3.jpg)

A regra prática: **Arduino e ESP32 são excelentes para protótipos, ensino e monitoramentos de baixa criticidade** (temperatura, umidade, poeira, ocupação). Para monitoramentos que embasam decisões de segurança — uma contenção, um vizinho que recalca —, usam-se instrumentos e dataloggers com calibração rastreável, instalados por equipe qualificada.

### Amostragem, relógio e memória

O microcontrolador decide **quando** ler. A taxa de amostragem segue a velocidade do fenômeno (Nyquist, $f_s > 2\,f_{max}$): um piezômetro pode ser lido a cada 15 minutos; uma vibração de cravação exige centenas de amostras por segundo. Ler várias vezes e tirar a média (**sobreamostragem**) reduz o ruído aleatório pelo fator $\sqrt{N}$. Toda leitura precisa de **carimbo de tempo** confiável, em UTC: um relógio de tempo real (RTC) com bateria própria, sincronizado pela rede (NTP) ou por GNSS. E a leitura deve ficar guardada em **memória local** (cartão SD ou flash) até a confirmação de envio: se a rede cair, nada se perde.

### Energia: o orçamento que define a autonomia

No canteiro, nem sempre há tomada. O consumo médio de um nó é a carga gasta num ciclo dividida pela duração do ciclo, e a autonomia é a capacidade útil da bateria dividida pelo consumo médio. O que governa a conta é o **tempo dormindo**: o chip ESP32 em sono profundo consome da ordem de 10 µA, mas uma **placa de desenvolvimento** comum consome miliamperes dormindo, por causa do regulador de tensão e do conversor USB. Em campo, usam-se placas de baixo consumo, baterias de lítio e, onde a demanda é maior, **painel solar** com controlador de carga e bateria dimensionados para os dias nublados.

![Estação automática de monitoramento em campo: caixa branca de datalogger fixada num mastro metálico, com um painel solar inclinado logo abaixo, cabos enrolados e um sensor de temperatura e umidade com abrigo no alto. Foto: Rory Finneren, Wikimedia Commons, CC BY 2.0](https://upload.wikimedia.org/wikipedia/commons/3/39/Solar_powered_weather_station%2C_Laurel_Airport%2C_Delaware.jpg)

### Instalação em campo

Um bom nó sensor dura a obra inteira se for bem instalado: **caixa com grau de proteção** adequado (IP65 resiste a jatos d'água; IP67, a imersão temporária — ABNT NBR IEC 60529), prensa-cabos e dessecante; **proteção contra surtos** e aterramento, sobretudo em cabos longos e mastros; cabos em eletroduto, longe da circulação de máquinas; antena **fora** da caixa metálica; e acesso seguro para manutenção, sem expor a equipe a riscos. Cada instalação gera uma **ficha**: identificação igual à do banco de dados, número de série, coordenadas, profundidade ou cota, foto, data e hora, fatores de calibração e leitura zero. O **comissionamento** verifica alimentação, comunicação e plausibilidade das primeiras leituras.

![Datalogger IoT compacto para monitoramento de nível, com caixa plástica vedada e etiqueta de identificação, ligado por um cabo enrolado a um transdutor de pressão, ao lado de um pequeno painel solar. Foto: Niau33, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/e/eb/LPMDL-110X_IoT_solar_level_monitoring_data_logger.jpg)

### Exemplo numérico

**(a) Por que a linha ficou reta?** O extensômetro do estagiário ($GF = 2$), em quarto de ponte excitado com $3{,}3\,\mathrm{V}$, sofre $100\,\mu\varepsilon$:

$
V_o \approx \frac{3{,}3 \times 2 \times 100 \times 10^{-6}}{4} = 165\,\mu\mathrm{V}
\qquad
\mathrm{LSB}_{ESP32} \approx \frac{3{,}3}{4.096} \approx 806\,\mu\mathrm{V}
$

O sinal é menor que um degrau do ADC: a leitura não muda. Com um amplificador de ganho 500, a saída vai a $82{,}5\,\mathrm{mV}$, cerca de 100 níveis — aproximadamente $1\,\mu\varepsilon$ por nível (valores ilustrativos).

**(b) Um piezômetro 4–20 mA no ESP32.** O transdutor de 0–200 kPa, com resistor de 120 Ω, fornece 9,6 mA: $V = 9{,}6 \times 10^{-3} \times 120 \approx 1{,}15\,\mathrm{V}$, e a pressão é $p = (9{,}6 - 4) \times 200/16 = 70\,\mathrm{kPa}$. Um nível do ADC equivale a $806\,\mu\mathrm{V}/120\,\Omega \approx 6{,}7\,\mu\mathrm{A}$; como $200/16 = 12{,}5\,\mathrm{kPa/mA}$, isso vale $0{,}0067 \times 12{,}5 \approx 0{,}084\,\mathrm{kPa}$ — cerca de 9 mm de coluna d'água.

**(c) Quanto dura a bateria?** A cada 15 min (900 s), o nó acorda 5 s a 120 mA (leitura, Wi-Fi e envio) e dorme 895 s. Com 7.200 mAh úteis:

$
\bar{I}_{otim} = \frac{5 \times 120 + 895 \times 0{,}15}{900} \approx 0{,}82\,\mathrm{mA} \Rightarrow t \approx \frac{7.200}{0{,}82} \approx 8.800\,\mathrm{h} \approx 1\,\mathrm{ano}
$

$
\bar{I}_{dev} = \frac{5 \times 120 + 895 \times 10}{900} \approx 10{,}6\,\mathrm{mA} \Rightarrow t \approx 680\,\mathrm{h} \approx 28\,\mathrm{dias}
$

A mesma lógica, numa placa de desenvolvimento que consome 10 mA dormindo, dura menos de um mês: é o sono que decide. O protótipo do estagiário era ainda pior: placa de desenvolvimento e uma bateria pequena, de cerca de 500 mAh — $500/10{,}6 \approx 47\,\mathrm{h}$, uns dois dias. Por isso a bateria acabou na terça.

### Atividade prática

No simulador gratuito **Wokwi** (wokwi.com), monte um ESP32 com um sensor de temperatura e umidade (DHT22) e um potenciômetro que represente um transdutor analógico. Programe a leitura a cada 10 s, converta o valor bruto do ADC para unidade de engenharia e imprima cada leitura com carimbo de tempo. Depois, escreva a ficha de instalação desse nó para uma obra real: caixa, grau de proteção, alimentação, autonomia estimada, local e leitura zero.

### Pontos-chave

- A cadeia embarcada vai do **sensor** ao **condicionamento**, ao **ADC**, ao **microcontrolador**, à **memória** e ao **rádio**; o dado tem a qualidade do elo mais fraco.
- Sinais fracos (pontes de extensômetros) exigem amplificação; o **4–20 mA** é robusto e detecta cabo rompido; o **LSB** de um ADC de $n$ bits é $V_{ref}/2^n$.
- **Arduino e ESP32** servem a protótipos e monitoramentos de baixa criticidade; decisões de segurança pedem **dataloggers** e instrumentos calibrados.
- A **autonomia** é governada pelo consumo em sono; a **instalação** exige grau de proteção, proteção contra surtos, ficha, leitura zero e comissionamento.

### Para saber mais

- **Espressif — página do ESP32:** https://www.espressif.com/en/products/socs/esp32
- **Arduino — documentação oficial:** https://docs.arduino.cc/
- **Wokwi — simulador on-line de ESP32 e Arduino:** https://wokwi.com/
- **Wikipedia — Conversor analógico-digital:** https://pt.wikipedia.org/wiki/Conversor_anal%C3%B3gico-digital

## Aula 10 — Roteiro da Videoaula 10: "Por que o protótipo mentiu? O que acontece entre o sensor e o número"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–3 — capa, sumário e o protótipo que mostrava uma linha reta.

> "Segunda: a linha do gráfico, perfeitamente reta. Terça: a bateria acabou. Quarta: a chuva entrou na caixa. O sensor estava certo — o que falhou foi tudo o que fica entre o sensor e o número. Hoje a gente abre essa caixa."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 4–8 — a cadeia de medição, condicionamento e ponte de Wheatstone, o laço 4–20 mA, a simulação dos bits do ADC e o exemplo dos 165 microvolts.

> "Sensor, condicionamento, conversor, microcontrolador, memória e rádio. O extensômetro numa ponte dá 165 microvolts; o degrau do ADC do ESP32 é de 806. O sinal cabe dentro de um degrau: a linha fica reta. Com um amplificador, aparece a carga. E o 4 a 20 miliampères é robusto: se a corrente vai a zero, é cabo rompido, não leitura nula."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 9–11 — Arduino, ESP32 e datalogger, barramentos digitais e amostragem, relógio e memória.

> "Arduino para aprender, ESP32 para prototipar IoT com Wi-Fi integrado, datalogger profissional para o que embasa decisões de segurança. Muitos sensores já falam digital, por I2C, SDI-12 ou Modbus. E toda leitura precisa de hora certa, em UTC, e de memória local: se a rede cair, nada se perde."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 12–15 — a calculadora de autonomia, a instalação em campo, do protótipo à produção e o laboratório. Slide 15 — laboratório no simulador da obra Torre A: três horas sem internet, 258 leituras guardadas nos nós e reenviadas com a hora original da medição, em UTC.

> "Bateria: o mesmo programa dura um ano numa placa de baixo consumo e 28 dias numa placa de desenvolvimento que gasta 10 miliampères dormindo. É o sono que decide. Na instalação: caixa IP67, proteção contra surtos, antena fora da caixa, ficha com leitura zero e comissionamento."

### 5. Encerramento
**[TELA]** Slides 16–18 — atividade no Wokwi, pontos-chave e encerramento.

> "Agora o dado existe e está guardado no nó. Mas ele precisa sair do subsolo e atravessar a cidade. LoRaWAN, Wi-Fi ou rede celular? Te espero na Aula 11!"

---

## Aula 11 — Redes de comunicação: LoRaWAN, Wi-Fi e redes celulares

> A obra instalou piezômetros no terceiro subsolo, inclinômetros atrás da cortina, um sensor de poeira na divisa e câmeras na grua. No primeiro dia, o Wi-Fi do escritório de obra não chegava ao subsolo; o chip 4G do sensor de poeira gastava a bateria em uma semana; e as câmeras congestionavam a rede de todo mundo. Nenhuma rede é a melhor para tudo. Nesta aula, você vai aprender a escolher a tecnologia de comunicação de cada sensor — **LoRaWAN, Wi-Fi ou redes celulares (4G/5G, LTE-M e NB-IoT)** — pelo **alcance**, pela **taxa de dados** e pelo **consumo de energia**, e a verificar com números se o sinal vai chegar.

### Três critérios e um triângulo de compromissos

Toda escolha de rede sem fio equilibra três grandezas que puxam em sentidos opostos: **alcance**, **taxa de dados** e **consumo de energia**. Não é possível maximizar as três ao mesmo tempo: redes de longo alcance e baixo consumo transmitem pouco; redes de alta taxa gastam muita energia ou alcançam pouco. Somam-se a eles **custo**, **cobertura** no local, **latência** e **quem opera** a rede.

### Propagação no canteiro e orçamento de enlace

O sinal de rádio enfraquece com a distância e com os obstáculos. No espaço livre, a perda de percurso (em dB) é

$
FSPL = 20\,\log_{10}(d_{km}) + 20\,\log_{10}(f_{MHz}) + 32{,}44
$

Frequências mais baixas, como as faixas sub-GHz (915 MHz), atravessam obstáculos e chegam mais longe que 2,4 GHz. No canteiro, somam-se perdas por paredes e lajes de concreto, armaduras, terreno, máquinas e, sobretudo, **subsolos** — cada parede de concreto pode atenuar da ordem de 10 dB ou mais, e um subsolo pode bloquear o sinal quase por completo. O **orçamento de enlace** (*link budget*) faz a conta: potência recebida = potência transmitida + ganhos das antenas − perdas; o enlace funciona se a potência recebida superar a **sensibilidade** do receptor com uma **margem** de segurança, tipicamente de 10 dB ou mais. Daí as boas práticas: gateway **no alto** (topo da grua), com visada para os sensores, e antenas **fora** de caixas metálicas.

### LoRaWAN: longe, devagar e com pouca energia

**LoRa** é a modulação de rádio (espalhamento espectral por *chirp*), e **LoRaWAN** é o protocolo de rede da LoRa Alliance. A topologia é em **estrela de estrelas**: os **dispositivos finais** (nós sensores) transmitem para qualquer **gateway** ao alcance; os gateways apenas encaminham os pacotes, pela internet, a um **servidor de rede** (*network server*), que elimina duplicatas, controla a taxa de dados e entrega os dados ao **servidor de aplicação**. As mensagens são cifradas com AES-128.

![Montagem de demonstração LoRaWAN: à esquerda, um dispositivo final numa caixa preta com antena, ligado por cabo a uma sonda de umidade do solo com três hastes; à direita, um gateway LoRaWAN montado sobre um computador de placa única, com antena. Foto: Roujiamo87, Wikimedia Commons, CC0](https://upload.wikimedia.org/wikipedia/commons/0/0c/Representative_LoRaWAN_Deployment_with_Gateway_%2B_End_Device.png)

O parâmetro-chave é o **fator de espalhamento** (*spreading factor*, SF7 a SF12): cada passo de SF aumenta a sensibilidade em cerca de 2,5 dB — mais alcance —, mas praticamente **dobra o tempo no ar** e, portanto, a energia por mensagem. O mecanismo de **taxa de dados adaptativa** (ADR) escolhe o menor SF que garante o enlace. As mensagens são pequenas (dezenas de bytes), o que basta para leituras periódicas. Os dispositivos **classe A**, os mais econômicos, só escutam a rede logo depois de transmitir. No Brasil, a LoRaWAN opera na faixa de 915–928 MHz (planos de frequência AU915 ou LA915), de uso não licenciado, com equipamentos que precisam de **homologação da Anatel**; a obra pode montar uma **rede privada** (gateway próprio) ou usar uma rede de terceiros.

![Topo de uma torre treliçada vermelha e branca contra o céu azul, com antenas verticais e equipamentos de rádio de uma rede LoRaWAN fixados nos braços laterais. Foto: Fabian Horst, Wikimedia Commons, CC BY 4.0](https://upload.wikimedia.org/wikipedia/commons/5/5f/2021-04-24-LoRaWAN-Mast-Sylt.jpg)

### Wi-Fi: muita taxa, pouco alcance, muita energia

O **Wi-Fi** (família IEEE 802.11) opera em 2,4 GHz e 5 GHz (e, nas versões recentes, 6 GHz) e oferece dezenas a centenas de Mbit/s — ideal para **câmeras**, escritório de obra, tablets e equipamentos com energia disponível. O alcance é de dezenas de metros em ambientes internos e algumas centenas ao ar livre, com antenas externas e visada; enlaces **ponto a ponto** direcionais ligam prédios distantes. O preço é o **consumo**: conectar-se e manter a associação gasta muita energia, o que não combina com sensores a bateria lidos a cada poucos minutos. O ESP32 clássico usa só 2,4 GHz. Em canteiros grandes, usam-se redes em **malha** (*mesh*) de pontos de acesso, que acompanham a obra conforme ela cresce, e a rede deve ser protegida com **WPA2/WPA3** e separada da rede administrativa.

![Ponto de acesso Wi-Fi para uso externo, numa caixa cinza fixada num mastro com uma antena vertical longa, sobre o telhado de uma edificação, com antenas de TV ao lado. Foto: Wikimedia Commons, CC BY-SA 3.0](https://upload.wikimedia.org/wikipedia/commons/6/6c/Wireless_ap_outdoor.jpg)

### Redes celulares: 4G, 5G, LTE-M e NB-IoT

As redes celulares usam a infraestrutura das **operadoras**: não exigem gateway próprio, mas têm mensalidade e dependem da cobertura local. O **4G (LTE)** e o **5G** dão alta taxa e servem a gateways, câmeras e envio de imagens de drones. Para sensores, a 3GPP definiu duas versões de baixa potência: o **LTE-M** (Cat-M1), com taxa da ordem de centenas de kbit/s a 1 Mbit/s e suporte a mobilidade — útil em equipamentos que se deslocam —, e o **NB-IoT**, com taxa menor, mas **cobertura profunda** (atravessa melhor paredes e subsolos) e consumo muito baixo. Ambos têm modos de economia de energia (**PSM** e **eDRX**), em que o módulo "dorme" com o registro na rede preservado. Antes de escolher, é preciso **confirmar a cobertura** de LTE-M ou NB-IoT da operadora no endereço da obra — e lembrar que as redes 2G e 3G estão em desligamento gradual.

![Torre de telefonia celular cilíndrica, com antenas de várias operadoras no topo, cercada por um alambrado verde com armários de equipamentos e um quadro elétrico na base, sob céu azul. Foto: Diacius, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/f/fd/Mobile_phone_mast.jpg)

### Comparando as redes

| Tecnologia | Alcance típico | Taxa de dados | Consumo | Infraestrutura | Uso típico no canteiro |
| --- | --- | --- | --- | --- | --- |
| **LoRaWAN** | de 2–5 km (urbano) a mais de 10 km (aberto) | centenas de bit/s a dezenas de kbit/s | muito baixo (anos de bateria) | gateway próprio ou rede de terceiros | piezômetros, inclinômetros, fissurômetros, temperatura |
| **NB-IoT** | cobertura da operadora, com boa penetração | dezenas de kbit/s | muito baixo | operadora (chip) | nós isolados, subsolos, onde não há gateway |
| **LTE-M** | cobertura da operadora | centenas de kbit/s a 1 Mbit/s | baixo | operadora (chip) | equipamentos móveis, rastreadores |
| **4G/5G** | cobertura da operadora | alta | alto | operadora (chip) | gateways, câmeras, imagens e vídeos |
| **Wi-Fi** | dezenas a centenas de metros | alta | alto | pontos de acesso próprios | escritório, câmeras, áreas cobertas com energia |

Regra prática: **leitura lenta a bateria → LoRaWAN ou NB-IoT; muito dado e energia disponível → Wi-Fi ou 4G/5G**. E, qualquer que seja a rede, o nó deve **armazenar e reenviar** (*store-and-forward*): guardar as leituras com o carimbo de tempo da medição e reenviá-las quando a conexão voltar. Para sensores críticos, vale ter **rota alternativa** — dois gateways, ou um gateway com conexão 4G de reserva.

### Exemplo numérico

**(a) O sinal chega do subsolo?** Um nó LoRaWAN no subsolo transmite a 14 dBm, com antena de 2 dBi, para um gateway com antena de 3 dBi, a 1,5 km. As perdas por obstáculos, lajes e cabos somam 35 dB (valor ilustrativo).

$
FSPL = 20\,\log_{10}(1{,}5) + 20\,\log_{10}(915) + 32{,}44 \approx 3{,}5 + 59{,}2 + 32{,}4 = 95{,}2\,\mathrm{dB}
$

$
P_{rx} = 14 + 2 + 3 - 95{,}2 - 35 = -111{,}2\,\mathrm{dBm}
$

Com sensibilidade típica de $-123\,\mathrm{dBm}$ em SF7, a margem é de 11,8 dB; em SF12 ($-137\,\mathrm{dBm}$), de 25,8 dB. Os dois fecham o enlace.

**(b) Quanto custa cada SF?** Para 12 bytes de dados (25 bytes no quadro LoRaWAN, largura de banda de 125 kHz), o tempo no ar é de cerca de 62 ms em SF7 e de 1,48 s em SF12. Transmitindo a 120 mA:

$
Q_{SF7} = 120 \times 0{,}062 \approx 7{,}4\,\mathrm{mA \cdot s}
\qquad
Q_{SF12} = 120 \times 1{,}48 \approx 178\,\mathrm{mA \cdot s}
$

O SF12 gasta cerca de 24 vezes mais energia por mensagem — e ocupa o canal 24 vezes mais. Se o SF7 já dá margem suficiente, o ADR o escolhe. (Alguns planos de frequência limitam o tempo no ar por transmissão, o que pode até impedir os SF mais altos: confira o plano usado e a regulamentação vigente.)

### Pausa para reflexão (Desafio)

A construtora pode montar a **própria rede LoRaWAN** — gateway no topo da grua, servidor de rede contratado — ou usar **chips NB-IoT** de uma operadora. Na primeira opção, a obra controla tudo, não paga mensalidade por sensor e não depende da cobertura de terceiros; mas alguém precisa manter o gateway funcionando às 2h da madrugada, e, quando a grua for desmontada, a rede vai junto. Na segunda, a operadora cuida da infraestrutura, mas a obra depende da cobertura no subsolo, paga por chip e fica sem dados se a operadora tiver uma falha. **Quem deve operar a rede que transporta dados de segurança?** Pense: o que acontece com os sensores que precisam continuar lendo **depois** da entrega da obra? Há rota alternativa se a rede principal cair? Quem é avisado quando um sensor para de transmitir?

### Atividade prática

Para a obra do gancho, escolha a rede de cada grupo de sensores e justifique por alcance, taxa, consumo, custo e cobertura. Desenhe a planta com a posição do gateway ou dos pontos de acesso, faça o orçamento de enlace do sensor mais desfavorável e defina o que acontece com os dados se a conexão cair por 12 horas.

### Pontos-chave

- A rede se escolhe pelo compromisso entre **alcance, taxa de dados e consumo**, somado a custo, cobertura, latência e quem a opera.
- O **orçamento de enlace** compara a potência recebida com a sensibilidade do receptor; subsolos e concreto impõem grandes perdas, e a margem deve ser de 10 dB ou mais.
- **LoRaWAN**: longo alcance, baixíssimo consumo e mensagens pequenas; SF maior = mais alcance, mais tempo no ar e mais energia. **Wi-Fi** e **4G/5G**: alta taxa, alto consumo. **NB-IoT** e **LTE-M**: celulares de baixa potência, com cobertura a confirmar.
- Toda rede falha: o nó deve **armazenar e reenviar**, e sensores críticos merecem rota alternativa.

### Para saber mais

- **LoRa Alliance — *What is LoRaWAN*:** https://lora-alliance.org/about-lorawan/
- **The Things Network — documentação sobre LoRaWAN:** https://www.thethingsnetwork.org/docs/lorawan/
- **Wikipedia — NB-IoT:** https://pt.wikipedia.org/wiki/NB-IoT
- **Anatel — Certificação e homologação de produtos:** https://www.gov.br/anatel/pt-br/regulado/certificacao-de-produtos

## Aula 11 — Roteiro da Videoaula 11: "Por que o sinal some no subsolo? A rede certa para cada sensor"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–4 — capa, sumário, o primeiro dia da rede na obra e o triângulo alcance × taxa × consumo.

> "Primeiro dia: o Wi-Fi não chega ao subsolo, o chip 4G do sensor de poeira acaba com a bateria em uma semana e as câmeras entopem a rede. Nenhuma rede é a melhor para tudo. Alcance, taxa e consumo: escolha dois."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 5–6 — propagação no canteiro e a calculadora do orçamento de enlace.

> "O sinal perde força com a distância e com o concreto. A conta é o orçamento de enlace: potência, mais ganhos, menos perdas. Um nó no subsolo a 1,5 quilômetro chega com menos 111 dBm. Em SF7, a margem é de quase 12 dB: fecha. Gateway no alto e antena fora da caixa metálica."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 7–10 — a arquitetura LoRaWAN, SF × tempo no ar × energia, Wi-Fi e redes celulares.

> "LoRaWAN: nó, gateway, servidor de rede, aplicação. Quilômetros de alcance e anos de bateria, com mensagens pequenas. Cada passo de SF dá mais alcance e dobra o tempo no ar: o SF12 gasta 24 vezes mais energia que o SF7. Wi-Fi é para câmera e escritório; 4G e 5G, para muito dado. Para sensores a bateria, a operadora oferece LTE-M e NB-IoT — confirme a cobertura no endereço da obra."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 11–14 — a tabela comparativa, armazenar e reenviar, a pausa para reflexão e o laboratório. Slide 14 — laboratório no simulador da obra Torre A: o PZ-03 do 3º subsolo sobe de SF7 para SF9 com 70 dB de perdas e sai do ar com 90 dB; sem ADR, a bateria cai de 12,5 para 1,4 ano.

> "Regra prática: leitura lenta a bateria, LoRaWAN ou NB-IoT; muito dado com energia, Wi-Fi ou 4G. Toda rede cai: o nó guarda e reenvia com a hora da medição. E pare para pensar: rede própria ou da operadora? Quem mantém o gateway às duas da manhã — e depois que a grua for embora?"

### 5. Encerramento
**[TELA]** Slides 15–17 — atividade, pontos-chave e encerramento.

> "O dado saiu do canteiro. Mas como ele chega, em ordem e sem se perder, ao banco de dados — e de que forma deve ser guardado? MQTT, Node-RED e séries temporais. Te espero na Aula 12!"

---

## Aula 12 — Protocolos e plataformas IoT: MQTT e armazenamento de séries temporais

> A obra tem 60 sensores de três fornecedores diferentes. Cada um tem o seu portal, a sua senha, o seu formato de arquivo e o seu relógio. Para saber se o recalque do vizinho acompanha a subida da água no solo, o engenheiro baixa três planilhas, acerta os fusos horários à mão e cola tudo numa quarta planilha — toda segunda-feira. Quando um sensor para de transmitir, ninguém percebe por dias. O problema não está nos sensores nem nas redes: falta uma **linguagem comum** para as mensagens e um **lugar comum** para guardá-las. Nesta aula, você vai conhecer o **MQTT**, protocolo de mensagens mais usado em IoT, o **Node-RED**, que integra os fluxos de dados, e os **bancos de séries temporais**, com o modelo de dados do **InfluxDB**.

### Da rede à aplicação: a pilha IoT

Gubbi et al. (2013) descrevem a IoT como a integração de sensores, redes, nuvem e visualização. Na obra, isso vira camadas: **percepção** (sensores e nós, Aulas 9 e 10), **rede** (LoRaWAN, Wi-Fi, celular, Aula 11), **plataforma** (recepção das mensagens, integração e armazenamento — esta aula) e **aplicação** (painéis, alertas e integração com BIM — Unidade 4). Entre a rede e a plataforma, as mensagens precisam de um **protocolo de aplicação**. O **HTTP** funciona, mas é pesado para dispositivos pequenos; o **CoAP** é uma alternativa enxuta sobre UDP; e o **MQTT** tornou-se o padrão de fato da IoT.

### MQTT: publicar e assinar por meio de um broker

O **MQTT** é um protocolo leve de mensagens, padronizado pela OASIS (versões 3.1.1 e 5.0), que funciona sobre TCP/IP. Em vez de os dispositivos conversarem diretamente, todos se conectam a um servidor central, o **broker** (como o Mosquitto, o EMQX ou o HiveMQ). Um cliente **publica** uma mensagem num **tópico**; o broker a entrega a todos os clientes que **assinaram** aquele tópico. Publicador e assinante não se conhecem: o sensor não sabe quem vai usar a leitura, e o painel não precisa saber de onde ela veio. Assim, acrescentar um novo consumidor — um painel, um sistema de alertas — não exige mexer em nenhum sensor. Numa rede LoRaWAN, quem publica no broker normalmente é o servidor de rede, por meio da sua **integração MQTT**; um ESP32 com Wi-Fi ou 4G publica diretamente.

![Diagrama do MQTT: à esquerda, um cliente publicador envia um pacote PUBLISH, com tópico e nível de QoS, a um broker hexagonal no centro; à direita, o broker reenvia o PUBLISH a dois clientes assinantes. Figura: Brivadeneira, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/3/3f/MQTT_publish.png)

### Tópicos, QoS e recursos para o canteiro

Os **tópicos** são hierárquicos, com níveis separados por barra, como `obra/torre-a/escavacao/piezometro/PZ-03/nivel`. Um bom padrão é obra → setor → tipo → sensor → grandeza, sem espaços nem acentos. Os assinantes usam **curingas**: `+` substitui um nível (`obra/torre-a/+/piezometro/+/nivel` recebe o nível de todos os piezômetros de todos os setores) e `#`, usado só no final, substitui todos os níveis abaixo (`obra/torre-a/#`).

A **qualidade de serviço** (QoS) define a garantia de entrega em cada trecho (do publicador ao broker e do broker ao assinante): **QoS 0** — no máximo uma vez, sem confirmação; **QoS 1** — pelo menos uma vez, com confirmação, podendo haver duplicatas; **QoS 2** — exatamente uma vez, com troca de quatro mensagens, mais lenta. Para sensores, QoS 1 costuma ser o equilíbrio: uma duplicata, com o mesmo carimbo de tempo, não cria dado falso. Outros recursos úteis: a **mensagem retida** (*retain*), que o broker guarda e entrega a quem assinar depois — o último estado de cada sensor —; o **último desejo** (*Last Will*), mensagem que o broker publica sozinho se um cliente cair sem se despedir — por exemplo, `offline` no tópico de status do nó —; e o **keep alive**, que detecta conexões mortas. Por segurança, o broker exige **autenticação** e **TLS** (porta 8883, e não a 1883, sem criptografia), e cada dispositivo só acessa os seus tópicos.

### Node-RED: integrar sem escrever um sistema inteiro

O **Node-RED** é uma ferramenta de código aberto, mantida pela OpenJS Foundation, para programar **fluxos** de dados ligando blocos (nós) num editor no navegador. Um fluxo típico de monitoramento tem: um nó **mqtt in**, que assina os tópicos dos sensores; um nó **function** (em JavaScript), que valida a mensagem, aplica a calibração — de miliamperes para quilopascals, por exemplo — e marca a qualidade da leitura; um nó **switch**, que separa leituras de status; e um nó de saída que **grava no banco de séries temporais**. O Node-RED roda num computador da obra, junto ao gateway (processamento **na borda**) ou num servidor em nuvem.

![Exemplo de fluxo no editor do Node-RED: três nós de entrada à esquerda ligados a um nó de função Filter, seguido de um nó de atraso de 10 segundos que alimenta dois nós de saída, Beep e E-Mail. Figura: 1-Byte, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/2/23/Node-RED_Example.png)

### Séries temporais: a anatomia de uma leitura

Uma **série temporal** é uma sequência de valores ordenados no tempo. Cada ponto de uma série de sensor precisa de: **carimbo de tempo** (em UTC, o da medição, não o da chegada); **identificação do sensor**; **valor bruto** (Hz, mA, contagens do ADC); **valor de engenharia** (mm, kPa), obtido com a leitura zero e os fatores de calibração, que devem ser **versionados**; **unidade**; **marca de qualidade**; e dados de **saúde** do nó, como tensão da bateria e intensidade do sinal. Regra de ouro: **nunca sobrescreva o dado bruto**; qualquer correção é uma nova camada, rastreável. Todo dado de campo tem defeitos — picos espúrios, lacunas, deriva, relógios desacertados —, e só o bruto preservado permite tratá-los depois.

### O modelo de dados do InfluxDB

Os **bancos de séries temporais** são otimizados para gravar dados em ordem de chegada, comprimir valores parecidos e consultar por intervalo de tempo. No **InfluxDB**, cada ponto tem quatro partes: a **measurement** (o "tipo" de dado, como `piezometro`); as **tags**, pares chave-valor de texto que descrevem e **indexam** a série (`obra`, `setor`, `sensor`); os **fields**, os valores medidos (`nivel_m`, `bruto_ma`, `bat_v`); e o **timestamp**. Os pontos são escritos no formato texto chamado **line protocol**, por exemplo:

`piezometro,obra=torre-a,sensor=PZ-03 nivel_m=7.14,bruto_ma=9.6,bat_v=3.61 1795064400000000000`

— a measurement, as tags, um espaço, os fields, outro espaço e o instante em nanossegundos desde 1/1/1970, em UTC (aqui, 19/11/2026 às 5h). O separador decimal é o **ponto**. Cada combinação única de measurement e tags forma uma **série**, e o número de séries é a **cardinalidade**: tags devem ter poucos valores possíveis (sensores, setores), e o que varia a cada leitura vai para os fields. Os dados ficam num **bucket** (ou banco), com **período de retenção**; as consultas usam InfluxQL ou Flux (versões 1.x e 2.x) e SQL ou InfluxQL (3.x).

![Corredor de um centro de dados com fileiras de servidores em racks, com luzes azuis e verdes de indicação acesas nos painéis frontais. Foto: Victorgrigas, Wikimedia Commons, CC BY-SA 3.0](https://upload.wikimedia.org/wikipedia/commons/9/94/Wikimedia_Foundation_Servers-8055_13.jpg)

### Volume, retenção e agregação

Sistemas maduros guardam o **dado bruto completo** pelo prazo que o contrato e a responsabilidade técnica exigem, mas mostram **agregados** — médias horárias, máximos diários — nos painéis, gerados por tarefas periódicas de **subamostragem** (*downsampling*). Registros de vibração, de centenas de amostras por segundo, são gravados **por evento**: só as janelas em que um gatilho foi ultrapassado, mais o pico de cada intervalo.

### Exemplo numérico

**(a) Quanto dado a obra produz?** Os 60 sensores, lidos a cada 15 minutos, geram

$
60 \times \frac{24 \times 60}{15} = 60 \times 96 = 5.760\,\mathrm{pontos/dia} \approx 2{,}1 \times 10^6\,\mathrm{pontos/ano}
$

A cerca de 100 bytes por linha de line protocol (valor ilustrativo, antes da compressão), são uns 576 kB por dia — pouco. Agora, um único acelerômetro triaxial gravando continuamente a 500 Hz:

$
3 \times 500 \times 86.400 \approx 1{,}3 \times 10^8\,\mathrm{valores/dia}
$

Um único sensor de vibração contínuo produz mais de 20 mil vezes os valores de todos os outros juntos: daí a gravação por evento.

**(b) A tag errada.** Com as tags `obra` e `sensor`, a measurement `piezometro` de 20 piezômetros tem 20 séries — para sempre. Se alguém puser o **identificador de cada leitura** como tag, cada ponto vira uma série nova: $20 \times 96 = 1.920$ séries novas por dia, cerca de 700 mil por ano. O índice cresce sem parar e as consultas ficam lentas. Identificadores únicos e valores medidos são **fields**, nunca tags.

### Atividade prática

Instale (ou suba em contêineres Docker) o broker **Mosquitto**, o **Node-RED** e o **InfluxDB**. No Wokwi, faça o ESP32 da Aula 10 publicar via MQTT, a cada 10 s, uma leitura em JSON no tópico `obra/sua-obra/teste/umidade/UR-01/leitura`, com mensagem de último desejo no tópico de status. No Node-RED, assine o tópico, converta o valor, marque a qualidade e grave no InfluxDB com tags e fields bem escolhidos. Para testes, há o broker público test.mosquitto.org — nunca para dados reais de obra.

### Pontos-chave

- **MQTT** é publicar/assinar por meio de um **broker**: tópicos hierárquicos, curingas `+` e `#`, QoS 0/1/2, mensagem retida, último desejo e TLS com autenticação.
- O **Node-RED** liga os fluxos: assina tópicos, valida, calibra, marca a qualidade e grava; pode rodar na borda ou na nuvem.
- Uma leitura é um registro completo — tempo UTC, sensor, bruto, engenharia, unidade, qualidade e saúde —, e o **bruto nunca é sobrescrito**.
- No **InfluxDB**, measurement + **tags** (indexadas, poucos valores) + **fields** (valores medidos) + timestamp; tags mal escolhidas explodem a **cardinalidade**; retenção e agregação controlam o volume.

### Para saber mais

- **GUBBI, J. et al. — *Internet of Things (IoT): a vision, architectural elements, and future directions* (Future Generation Computer Systems, 2013):** https://doi.org/10.1016/j.future.2013.01.010
- **MQTT.org — documentação do protocolo MQTT:** https://mqtt.org/
- **Node-RED — documentação:** https://nodered.org/docs/
- **InfluxData — *Line protocol* (InfluxDB v2):** https://docs.influxdata.com/influxdb/v2/reference/syntax/line-protocol/

### O que você verá na próxima unidade

Na **Unidade 4 — Painéis, Integração com BIM e Gestão de Riscos**, os dados que agora chegam organizados ao banco de séries temporais vão virar decisão. Você vai montar **painéis de monitoramento** com **alertas e limites de alarme** (Grafana); **integrar** os dados de drones e sensores ao **BIM** e ao **planejamento e controle** da obra; usar a tecnologia a favor da **segurança do trabalho**, à luz da **NR-18**; e, para fechar a disciplina, tratar de **privacidade, LGPD e cibersegurança** em sistemas IoT de obras — inclusive a segurança dos brokers e dispositivos que você conheceu nesta unidade.

## Aula 12 — Roteiro da Videoaula 12: "Um carteiro chamado MQTT: como milhares de leituras chegam ao banco de dados sem se perder"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–4 — capa, sumário, três fornecedores e três portais e a pilha IoT.

> "Sessenta sensores, três fornecedores, três portais, três relógios e uma planilha montada à mão toda segunda-feira. Falta uma linguagem comum para as mensagens e um lugar comum para guardá-las. Hoje: MQTT, Node-RED e séries temporais."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 5–8 — publicar e assinar, a simulação dos tópicos e curingas, QoS, mensagem retida e último desejo, e segurança do broker.

> "No MQTT, ninguém conversa direto: o sensor publica num tópico, o broker entrega a quem assinou. Tópico é endereço: obra, setor, tipo, sensor, grandeza. Com o curinga mais, eu recebo todos os piezômetros. QoS 1 garante a entrega, com possível duplicata. O último desejo avisa quando um nó cai. E broker de obra tem senha e TLS."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 9–10 — o fluxo no Node-RED e a anatomia de uma leitura.

> "No Node-RED, o fluxo assina, valida, converte miliampère em quilopascal, marca a qualidade e grava. E cada leitura leva hora em UTC, sensor, bruto, engenharia, unidade, qualidade e bateria. O bruto nunca é sobrescrito."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 11–15 — o modelo do InfluxDB, o line protocol, a calculadora de volume e cardinalidade, retenção e agregação e o laboratório. Slide 15 — laboratório no simulador da obra Torre A: curingas na aba MQTT, a assinatura inválida com # no meio e o line protocol do PZ-03, com tags e fields.

> "No InfluxDB: measurement, tags, fields e timestamp. Tag é o que identifica a série; field é o que você mede. Sessenta sensores geram 5.760 pontos por dia; um acelerômetro contínuo gera 130 milhões de valores. E se o identificador da leitura virar tag, nascem 700 mil séries por ano. Grave vibração por evento e agregue para o painel."

### 5. Encerramento
**[TELA]** Slides 16–19 — atividade, pontos-chave, prévia da Unidade 4 e encerramento.

> "Você fechou a unidade: sensor, plataforma, rede e banco de dados. Na Unidade 4, esses dados viram painéis com alertas, entram no BIM e no planejamento, apoiam a segurança do trabalho e enfrentam a LGPD e a cibersegurança. Te espero lá!"

---

## Quiz não avaliativo

### Questão 1

Uma construtora precisa monitorar 12 piezômetros instalados no terceiro subsolo de uma obra, lidos a cada 30 minutos, alimentados a bateria e sem energia elétrica disponível no local. O escritório de obra tem Wi-Fi, e a operadora local oferece NB-IoT no endereço. Com base nos conceitos da aula, assinale a alternativa **correta**:

a) O Wi-Fi do escritório é a melhor escolha, porque oferece a maior taxa de dados e, portanto, o menor consumo de energia por leitura.
b) Câmeras e piezômetros devem usar a mesma rede 4G, pois a taxa de dados é o único critério relevante na escolha da tecnologia.
c) LoRaWAN, com gateway em posição elevada, ou NB-IoT são adequados, desde que o orçamento de enlace (ou a cobertura) seja confirmado no subsolo e os nós armazenem e reenviem as leituras.
d) Qualquer rede serve, porque o fator de espalhamento SF12 garante alcance ilimitado sem aumento do consumo de energia.

**Resposta correta:** c)

**Feedback:** A alternativa (c) está correta: leituras lentas, a bateria e em local de difícil acesso pedem redes de baixa potência e longo alcance (LoRaWAN) ou de cobertura profunda (NB-IoT); como subsolos impõem grandes perdas, é preciso verificar o orçamento de enlace ou a cobertura, e o *store-and-forward* protege contra falhas de conexão. A (a) erra: o Wi-Fi tem alto consumo e alcance curto, sobretudo através de lajes. A (b) ignora o compromisso entre alcance, taxa e consumo. A (d) é falsa: o SF12 aumenta o alcance, mas multiplica o tempo no ar e a energia por mensagem.

### Questão 2

Um engenheiro configura o sistema de monitoramento de uma escavação: os nós publicam via MQTT no tópico `obra/torre-a/escavacao/piezometro/PZ-03/nivel`, e o Node-RED grava as leituras no InfluxDB. Assinale a alternativa **correta**:

a) Para receber o nível de todos os piezômetros de todos os setores, o Node-RED deve assinar `obra/torre-a/#/piezometro/nivel`, pois o curinga `#` pode ficar no meio do tópico.
b) A assinatura `obra/torre-a/+/piezometro/+/nivel` recebe o nível de todos os piezômetros de todos os setores; no InfluxDB, o identificador do sensor deve ser tag, e os valores medidos, fields.
c) O identificador único de cada leitura deve ser gravado como tag no InfluxDB, para que cada ponto tenha a sua própria série e as consultas fiquem mais rápidas.
d) Com QoS 0, o broker garante que cada leitura seja entregue exatamente uma vez, sem necessidade de confirmação.

**Resposta correta:** b)

**Feedback:** A alternativa (b) está correta: o curinga `+` substitui exatamente um nível do tópico (aqui, o setor e o sensor), e, no InfluxDB, tags identificam e indexam as séries (sensor, setor), enquanto os fields guardam os valores medidos. A (a) erra porque `#` só pode ser usado no último nível. A (c) descreve a explosão de cardinalidade: cada leitura viraria uma série nova, inchando o índice e deixando as consultas mais lentas. A (d) confunde os níveis: QoS 0 é "no máximo uma vez", sem confirmação; "exatamente uma vez" é o QoS 2.

---

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

> _[PENDENTE — aguardando acesso à Biblioteca Virtual]_ Sugestão a confirmar na BV: MAGRANI, Eduardo. *A internet das coisas*. Rio de Janeiro: FGV Editora, 2018 (bibliografia básica da ementa), capítulo de conceitos e aplicações da IoT. Consultar a fonte original ajuda o aluno a enxergar além da técnica: o livro discute o que muda quando objetos passam a coletar e trocar dados sozinhos, incluindo riscos e responsabilidades que voltam na Unidade 4.

- **Nome do livro:** 
- **Capítulo:** 
- **Link de acesso:** 
- **Qual aula o material deverá entrar?** Aulas 9 e 12

### Para mergulhar no assunto (saiba mais)

> Para ver os sensores da Aula 9 do ponto de vista de quem projeta e lê a instrumentação, assista ao primeiro bloco do curso **"Instrumentação, Interpretação de Dados e Monitoramento de Estruturas Geotécnicas"**, da Effyía — Escola da Engenharia, no YouTube. Depois, ponha a mão na massa com o vídeo **"Publicando Dados via MQTT e Criando um Dashboard no Node-RED com ESP32 no Simulador Wokwi"**, do canal Clube da Eletrônica: sem comprar nenhum componente, você vê um ESP32 publicar leituras num broker MQTT e o Node-RED recebê-las — exatamente a cadeia das Aulas 10 e 12. Assista com as perguntas da unidade em mente: qual é a leitura zero? Quem garante que a mensagem chegou? Onde o dado bruto fica guardado?

- **Links:** https://www.youtube.com/watch?v=5hwJUP5wIfY · https://www.youtube.com/watch?v=34W3yUgXWTQ
- **Qual aula o material deverá entrar?** Aulas 9, 10 e 12

### Podcast (curadoria | até 45 min)

> Como é a instrumentação de uma obra gigante quando as leituras deixam de ser manuais? No episódio 3 da 2ª temporada do **I&M Geotech Podcast**, canal brasileiro dedicado à instrumentação e ao monitoramento geotécnico, Roberto Collado Bermejo e David José Mendi Fernandez, da Geprode, contam como foi a gestão da instrumentação nas obras da **Linha 6 do Metrô de São Paulo**: sensores automatizados, transmissão e volume de dados — o caminho completo desta unidade, do sensor ao banco de dados. O episódio completo tem cerca de 73 minutos; para esta curadoria, ouça os **primeiros 45 minutos**.

- **NOME DO PODCAST:** I&M Geotech: Instrumentação e Monitoramento Geotécnico (canal no YouTube)
- **NOME DO EPISÓDIO:** T02 | EP03 — Roberto Collado Bermejo e David José Mendi Fernandez (instrumentação da Linha 6 do Metrô de São Paulo)
- **Link:** https://www.youtube.com/watch?v=jQpQFHHl_Zo
- **Qual aula o material deverá entrar?** Aulas 9 e 12

### Artigo científico

> Sensores, redes, nuvem e visualização: será que a IoT é só a soma dessas peças? Neste artigo muito citado (bibliografia complementar da disciplina), Gubbi, Buyya, Marusic e Palaniswami apresentam uma visão da Internet das Coisas centrada na integração entre **redes de sensores sem fio**, **computação em nuvem** e **visualização**, discutem os elementos de arquitetura — identificação, sensoriamento, comunicação, armazenamento e análise — e apontam desafios ainda atuais, como interoperabilidade, energia, segurança e privacidade. Leia pensando no canteiro: onde estão, na sua obra, cada um desses elementos? É a fundamentação acadêmica das Aulas 11 e 12 e uma ponte para a cibersegurança da Unidade 4.

- **Link:** https://doi.org/10.1016/j.future.2013.01.010
- **Qual aula o material deverá entrar?** Aulas 11 e 12
- **Referência bibliográfica do artigo no formato ABNT:** GUBBI, Jayavardhana; BUYYA, Rajkumar; MARUSIC, Slaven; PALANISWAMI, Marimuthu. Internet of Things (IoT): a vision, architectural elements, and future directions. **Future Generation Computer Systems**, Amsterdam, v. 29, n. 7, p. 1645-1660, set. 2013. DOI: 10.1016/j.future.2013.01.010.
