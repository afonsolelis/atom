# Roteiros Estendidos (15–19 minutos) — Unidade 3: Sensores IoT e Redes de Comunicação

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 9 a 12
- **Formato:** roteiro de narração **integral** — o texto em citação (>) é a fala completa. **Esta é a versão a gravar.** Duração-alvo: **15 a 19 minutos** por aula (cerca de 2.000 a 2.550 palavras faladas, a uns 135 palavras/min, já contando as pausas curtas das demonstrações). Os roteiros curtos de `unidade_3.md` são só um guia da sequência.

> **Como usar:** leia as falas em citação na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`), na mesma ordem dos slides. Quando a fala manda clicar, o efeito descrito aparece na tela em poucos segundos; tabelas e listas dos slides **não** são lidas item a item: a fala comenta o essencial e o aluno lê o resto na tela.

---

## Roteiro da Videoaula 9 — "O que a obra sente e ninguém vê: seis sensores que contam tudo"

**Aula 9 — Sensores para obras: inclinômetros, extensômetros, acelerômetros, temperatura, umidade e poeira**

**Duração-alvo:** cerca de 18:00 (15 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 9 de Drones e Sensores IoT no Monitoramento de Obras. Hoje a gente começa a Unidade 3, a unidade dos sensores e das redes de comunicação. Na Unidade 2, o drone olhou a obra de cima: ortomosaico, modelo de superfície, nuvem de pontos, volumes. Agora o monitoramento muda de ponto de vista. Ele desce para dentro do solo, entra na estrutura e respira o ar do canteiro."

**[TELA]** Slide 3 — a obra de três subsolos e as cinco perguntas.

> "Quero que você imagine uma segunda-feira, sete da manhã, numa obra de três subsolos em área urbana. A cortina de estacas está sendo escavada colada num prédio antigo. Uma escora metálica, ao sol da tarde, parece estar ganhando carga. A laje do térreo foi concretada no sábado, e o empreiteiro já quer desformar. A equipe de pintura quer começar a impermeabilização num dia úmido. E a vizinhança liga reclamando da poeira."

> "Repara: são cinco perguntas completamente diferentes. A contenção está andando? A escora aguenta? A laje já pode ser desformada? Dá para impermeabilizar hoje? A poeira passou do aceitável? E todas elas têm a mesma resposta: medir. Mas medir o quê, com qual sensor, instalado onde, e com que cuidado? É isso que a gente vai construir hoje."

### 2. O mapa da unidade (1:40 – 2:50)

**[TELA]** Slide 4 — o que você verá nesta unidade: do sensor ao banco de dados.

> "Antes de entrar nos sensores, deixa eu te mostrar o mapa da unidade, porque ela conta uma história só: o caminho completo de um dado. Hoje, na Aula 9, os sensores e as grandezas que eles medem. Na Aula 10, as plataformas embarcadas, como o Arduino, o ESP32 e os dataloggers, que transformam o sinal do sensor em número, guardam esse número e alimentam tudo isso no meio da obra. Na Aula 11, as redes que levam o dado para fora do canteiro: LoRaWAN, Wi-Fi e redes celulares. E, na Aula 12, os protocolos e as plataformas que recebem e guardam as leituras: MQTT, Node-RED e o banco de séries temporais InfluxDB."

> "O Eduardo Magrani, no livro A internet das coisas, que é bibliografia da nossa disciplina, descreve justamente isso: objetos do dia a dia que passam a coletar e trocar dados sem que alguém precise intervir a cada leitura. No nosso caso, os objetos são um tubo enterrado, uma escora, uma laje e uma caixinha pendurada no tapume. Vamos a eles."

### 3. Do fenômeno ao sensor (2:50 – 4:30)

**[TELA]** Slide 5 — do fenômeno ao sensor: escolher pelo mensurando.

> "Primeiro princípio: ninguém escolhe sensor pelo catálogo. Escolhe pelo mensurando. Mensurando é o valor específico que eu quero conhecer. Não é o movimento do solo, genericamente. É o deslocamento horizontal da cortina a três metros de profundidade, em relação à leitura de antes da escavação. Quanto mais preciso for o mensurando, mais fácil fica escolher o instrumento."

> "Com o mensurando definido, entram cinco critérios. A faixa de medição: o sensor mede até onde o fenômeno pode chegar? A resolução: qual é a menor variação que ele indica? A incerteza: quanto ele pode errar? E cuidado, porque resolução não é exatidão. Um visor com três casas decimais pode errar por um milímetro inteiro. Depois, a estabilidade a longo prazo, ou seja, a deriva: um monitoramento de obra dura meses, às vezes anos, e o sensor não pode andar sozinho. E, por fim, a robustez: lama, chuva, sol, impacto de máquina, cabo pisado por caminhão."

> "E três regras valem para todos os sensores desta aula. Calibração rastreável. Leitura zero, feita antes de o fenômeno começar. E limites com ação definida antes de a obra começar. Sem essas três coisas, instrumentar vira colecionar curiosidades: gráficos bonitos que ninguém sabe o que fazer com eles."

### 4. Inclinômetros (4:30 – 6:30)

**[TELA]** Slide 6 — o inclinômetro: deslocamento horizontal em profundidade.

> "Vamos ao primeiro sensor: o inclinômetro. Ele responde à pergunta da contenção: o solo e a cortina estão andando na horizontal? Instala-se um tubo-guia, com quatro ranhuras internas, num furo vertical atrás da contenção. O detalhe crucial é o pé do tubo: ele tem que ficar engastado em solo ou rocha que não se mova, abaixo da zona de influência da escavação. Esse pé é o nosso ponto fixo, a nossa referência."

> "Para ler, baixa-se uma sonda que corre pelas ranhuras. Dentro dela há acelerômetros, que medem a inclinação em relação à vertical, do mesmo jeito que o seu celular sabe se está em pé ou deitado. A sonda para a cada meio metro. Em cada parada, mede o ângulo theta daquele trecho, e o desvio horizontal do trecho é o comprimento, meio metro, vezes o seno de theta."

> "Dois cuidados. O que interessa é sempre a diferença em relação à leitura zero, acumulada de baixo para cima, a partir do pé fixo. E faz-se uma segunda passada com a sonda girada cento e oitenta graus, que cancela o viés do próprio sensor. Hoje também existe a versão automática: o inclinômetro in-place, uma cadeia de sensores MEMS fixos dentro do tubo, lidos por um datalogger a cada quinze minutos ou a cada hora. E, para a fachada do vizinho, existe o clinômetro de parede, o tiltmeter, que mede a rotação de um pilar ou de uma parede."

### 5. Exemplo: do ângulo ao milímetro (6:30 – 7:40)

**[TELA]** Slide 7 — exemplo numérico: do ângulo ao milímetro.

> "Vamos fazer a conta. A sonda, com meio metro entre as rodas, registrou variações do seno do ângulo, em relação à leitura zero, só nos seis trechos de cima: seis, cinco, quatro, três, um vírgula seis e zero vírgula quatro, tudo vezes dez elevado a menos três. Abaixo disso, nada mudou. Ótimo sinal: o pé está fixo."

> "Somando as variações, dá vinte vezes dez a menos três, ou seja, zero vírgula zero vinte. Vezes meio metro: zero vírgula zero dez metro. Dez milímetros no topo. Repara como o perfil é grande em cima e vai se anulando para baixo: é exatamente o formato que se espera de uma cortina que flete para dentro da escavação com o pé travado. Se os trechos de baixo também tivessem mexido, a primeira suspeita seria o pé do tubo, e não a cortina."

### 6. Extensômetros (7:40 – 9:00)

**[TELA]** Slide 8 — extensômetros: elétrico de resistência × corda vibrante.

> "Segundo sensor: o extensômetro. Ele mede deformação específica, em microdeformações. Uma microdeformação é um milionésimo: um metro de aço que encolhe um milésimo de milímetro. Existem duas famílias. O extensômetro elétrico de resistência é uma grade metálica colada na peça. Quando a peça deforma, a grade estica ou encurta, e a resistência elétrica muda, na proporção do fator do extensômetro, que é cerca de dois. Ele é rápido, ótimo para ensaios, mas sofre com umidade e com deriva quando fica meses na obra."

> "Para o longo prazo, a obra usa o extensômetro de corda vibrante. É um fio de aço tensionado entre dois blocos presos à peça. Quando a peça deforma, a tensão do fio muda, e a frequência com que ele vibra muda junto: a deformação é proporcional ao quadrado da frequência. Por que a obra gosta tanto dele? Porque ele é estável por anos, e porque a informação está na frequência, não na tensão elétrica. Então o comprimento do cabo e a resistência do fio não atrapalham. Ele pode ser soldado numa escora metálica ou amarrado na armadura antes da concretagem, como nessa foto."

### 7. A escora no sol (9:00 – 10:20)

**[TELA]** Slide 9 — simulação: a escora no sol. Comece com 250 µε e ΔT = 0; depois aumente a temperatura e alterne a correção térmica.

> "Agora a nossa escora. O extensômetro de corda vibrante, já corrigido para a temperatura, indica duzentas e cinquenta microdeformações desde a leitura zero. O aço tem módulo de elasticidade de duzentos gigapascals. Pela lei de Hooke, tensão é módulo vezes deformação: duzentos mil megapascals vezes duzentos e cinquenta milionésimos dá cinquenta megapascals. A área da escora é de cento e vinte centímetros quadrados, ou zero vírgula zero doze metro quadrado. Força é tensão vezes área: seiscentos quilonewtons. Com carga de projeto de novecentos, a escora está a sessenta e sete por cento."

> "Agora eu vou esquentar a escora na simulação. Olha o que acontece com a leitura sem correção. O aço dilata cerca de doze milionésimos por grau. Uma variação de quinze graus, da manhã fria para a tarde de sol, corresponde a cerca de cento e oitenta microdeformações. É da mesma ordem do sinal que a gente quer medir! Numa escora travada entre as paredes, parte dessa dilatação é impedida e vira força térmica de verdade; outra parte é só a diferença entre o fio e a peça. Se ninguém separa a parcela térmica, a variação do dia é confundida com efeito da escavação, e alguém manda reforçar uma escora que estava tranquila, ou pior, ignora um aumento real achando que é só o calor. Por isso, os extensômetros de corda vibrante trazem um termistor embutido, e a fórmula do fabricante separa a parcela térmica da parcela causada pela escavação antes de virar força. Ligo a correção: a curva volta para o que interessa."

### 8. Acelerômetros (10:20 – 11:50)

**[TELA]** Slide 10 — acelerômetros: vibração e assinatura dinâmica.

> "Terceiro sensor: o acelerômetro. Os do tipo MEMS são microssistemas num chip, baratos e de baixo consumo: o mesmo tipo que está no seu celular, perfeito para IoT. Os piezoelétricos são mais sensíveis e alcançam frequências mais altas, para medições mais exigentes. Na foto, um acelerômetro com unidade sem fio, preso no pendural de uma ponte em arco."

> "Na obra, o acelerômetro tem dois usos. O primeiro é medir a vibração que a própria obra provoca: cravação de estacas, compactação vibratória, tráfego de caminhões. Nas edificações vizinhas, essa vibração é avaliada pela velocidade de partícula de pico, em milímetros por segundo. O segundo uso é identificar as frequências naturais da estrutura, que são a assinatura dela. Num modelo de massa e mola, a frequência depende da raiz da rigidez sobre a massa. Se a rigidez cai, por fissuração ou dano numa ligação, a frequência cai junto. Cinco por cento a menos na frequência correspondem a cerca de dez por cento a menos na rigidez."

> "E aqui volta uma regra que você não pode esquecer: Nyquist. Para registrar uma vibração, é preciso amostrar a mais que o dobro da maior frequência de interesse; na prática, de cinco a dez vezes. Se a cravação tem componentes de até cinquenta hertz, eu quero algumas centenas de amostras por segundo. Abaixo disso, a vibração aparece com uma frequência falsa."

### 9. Temperatura (11:50 – 13:00)

**[TELA]** Slide 11 — temperatura: o sensor que corrige todos os outros.

> "Quarto sensor, e talvez o mais subestimado: a temperatura. Termistores NTC são baratos e sensíveis. Termorresistências, como a Pt100, são estáveis e exatas. Termopares cobrem faixas enormes, mas precisam de compensação da junta fria. E a temperatura tem três papéis na obra."

> "Primeiro, corrigir os outros sensores, como você acabou de ver na escora: extensômetros, fissurômetros e piezômetros de corda vibrante dependem dela. Segundo, controlar a cura do concreto. Pelo método da maturidade, a gente soma, ao longo do tempo, a temperatura do concreto menos uma temperatura de referência, multiplicada pelo intervalo. É o fator de Nurse-Saul. Com uma curva calibrada em laboratório para a mesma mistura, esse número estima a resistência nas primeiras idades. Lembra da laje concretada no sábado? O sensor embutido diz se ela já chegou à resistência de desforma, sem substituir os corpos de prova, que continuam sendo o controle de aceitação. Terceiro, em concreto massa, como um bloco de fundação grande, vigiar a diferença entre o núcleo quente e a superfície fria, que pode fissurar a peça. O limite dessa diferença vem do projeto."

### 10. Umidade e ponto de orvalho (13:00 – 14:40)

**[TELA]** Slide 12 — umidade e a calculadora do ponto de orvalho. Comece com 20 °C e 80%; depois mova a temperatura da laje para 18 °C e para 21 °C.

> "Quinto sensor: umidade. A umidade relativa do ar é medida por sensores capacitivos: um polímero cuja propriedade elétrica muda conforme absorve vapor d'água. Quase sempre o chip mede temperatura junto, como essa plaquinha vermelha na foto. E por que a obra se importa? Por causa do ponto de orvalho: a temperatura em que o vapor começa a condensar. Se a superfície estiver abaixo dele, aparece água, e isso compromete pintura, impermeabilização e colagem de revestimento. Muitas especificações de pintura exigem a superfície pelo menos três graus acima do ponto de orvalho."

> "Vamos à calculadora. O sensor marca vinte graus e oitenta por cento de umidade. Pela aproximação de Magnus, o ponto de orvalho dá cerca de dezesseis vírgula quatro graus. A laje está a dezoito graus: só um vírgula seis grau acima. Não atende a margem de três graus. A equipe de impermeabilização espera. Se a laje subir para vinte e um graus, aí a margem passa de quatro graus, e libera. Uma leitura de dois números evita um retrabalho inteiro."

> "E a umidade também se mede dentro dos materiais. Sondas de umidade relativa em furos na laje indicam quando o concreto está seco o bastante para receber piso, pelo método da norma ASTM F2170, com o limite dado pelo fabricante do revestimento. E sensores capacitivos, ou de TDR, medem a umidade do solo em aterros e taludes, onde a chuva reduz a resistência."

### 11. Poeira (14:40 – 15:50)

**[TELA]** Slide 13 — poeira: MP10, MP2,5 e calibração por colocalização.

> "Sexto sensor: poeira. Ela é monitorada como material particulado: MP10, partículas até dez micrômetros, e MP2,5, até dois e meio, que entram fundo no sistema respiratório. Os sensores IoT mais comuns são óticos: o ar passa por um feixe de luz, e um fotodetector mede a luz espalhada pelas partículas. São baratos e consomem pouco, mas têm um defeito sério: com umidade alta, as partículas absorvem água, incham, e o sensor superestima a concentração. Por isso eles precisam ser calibrados por colocalização: fica um tempo ao lado de uma estação de referência, e a gente ajusta a curva."

> "A régua nacional é a Resolução CONAMA quinhentos e seis, de 2024. Na etapa em vigor desde 2025, a média de vinte e quatro horas é de cem microgramas por metro cúbico para MP10 e cinquenta para MP2,5. Mas atenção: são padrões de qualidade do ar ambiente, não limites de emissão de uma obra. O plano de monitoramento fixa gatilhos próprios na divisa e as ações: ligar a aspersão, como nessa foto da demolição, lavar as rodas dos caminhões, cobrir as caçambas."

### 12. Os seis sensores, atividade e encerramento (15:50 – 17:30)

**[TELA]** Slide 14 — tabela: os seis sensores, o que medem e onde enganam.

> "Vamos juntar tudo. Inclinômetro: deslocamento em profundidade, engana se o pé não estiver fixo. Extensômetro: deformação e força, engana com a temperatura. Acelerômetro: vibração e frequência natural, engana se a amostragem for baixa. Temperatura: corrige os outros e controla a cura. Umidade: ponto de orvalho e secagem. Poeira: MP10 e MP2,5, engana com ar úmido e sem calibração. Repara que cada sensor tem a sua armadilha. Conhecer a armadilha é metade do trabalho do engenheiro."

**[TELA]** Slide 15 — atividade prática.

> "Sua atividade: para a obra do gancho, monte uma tabela com os seis sensores e as colunas mensurando, local de instalação, princípio de funcionamento, principal fonte de erro, forma de correção ou calibração e a decisão que a leitura apoia: reforçar a escora, liberar a laje, adiar a pintura, ligar a aspersão."

**[TELA]** Slide 16 — pontos-chave.

> "Recapitulando: sensor se escolhe pelo mensurando, com calibração, leitura zero e limites com ação. Inclinômetro e extensômetro contam como a contenção e a estrutura se comportam; acelerômetro e temperatura, como elas vibram e curam; umidade e poeira, como está o ar e o material."

**[TELA]** Slide 17 — encerramento e gancho para a Aula 10.

> "Mas um sensor sozinho só entrega um sinal elétrico, às vezes de poucos microvolts. Quem transforma isso em número confiável, carimba a hora, guarda na memória e funciona meses a bateria no meio da lama? As plataformas embarcadas: Arduino, ESP32 e datalogger. Te espero na Aula 10!"

---

## Roteiro da Videoaula 10 — "Por que o protótipo mentiu? O que acontece entre o sensor e o número"

**Aula 10 — Plataformas embarcadas e coleta de dados em campo**

**Duração-alvo:** cerca de 17:30 (15 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 10 de Drones e Sensores IoT no Monitoramento de Obras. Na aula passada, você conheceu os seis sensores da obra: inclinômetro, extensômetro, acelerômetro, temperatura, umidade e poeira. Hoje a gente abre a caixinha que fica entre o sensor e o dado: a plataforma embarcada."

**[TELA]** Slide 3 — o protótipo que mostrava uma linha reta.

> "Deixa eu te contar uma história que acontece toda hora. Um estagiário animado montou, num fim de semana, um protótipo: uma placa ESP32, um extensômetro colado numa escora e um rádio. Na segunda-feira, o gráfico mostrava uma linha perfeitamente reta. Pela tela, a escora não carregava absolutamente nada. Na terça, a bateria acabou. Na quarta, choveu e a água entrou na caixa."

> "E o mais curioso: o sensor estava certo. O extensômetro funcionava. O que falhou foi tudo o que fica entre o sensor e o número: o condicionamento do sinal, a conversão analógico-digital, a energia e a instalação. Ao final desta aula, você vai saber explicar cada uma das três falhas, e, principalmente, como evitá-las."

### 2. A cadeia de medição (1:30 – 2:40)

**[TELA]** Slide 4 — a cadeia de medição embarcada.

> "Pensa numa corrente com seis elos. O sensor responde à grandeza física. O condicionamento excita o sensor, amplifica, filtra e adapta o sinal. O conversor analógico-digital, o ADC, transforma tensão em número. O microcontrolador aplica a calibração, carimba a hora e decide quando ler e quando transmitir. A memória local guarda a leitura. E o rádio manda o dado embora. Por baixo de tudo, a energia, alimentando cada elo."

> "Uma corrente arrebenta no elo mais fraco, e com dado é igual. Um sensor excelente, de milhares de reais, ligado a um conversor ruidoso, produz uma leitura ruim. Por isso, quem projeta monitoramento não pode olhar só para o sensor."

### 3. Condicionamento e ponte de Wheatstone (2:40 – 4:10)

**[TELA]** Slide 5 — condicionamento de sinal e a ponte de Wheatstone.

> "Muitos sensores entregam sinais fracos demais, ou em formatos que o microcontrolador não lê direto. O caso clássico é o extensômetro elétrico. A variação de resistência dele é minúscula, então a gente o monta numa ponte de Wheatstone: quatro resistores em losango, alimentados por uma tensão de excitação. Quando a ponte está equilibrada, a saída é zero. Quando o extensômetro deforma, a ponte desequilibra e aparece uma tensão de saída."

> "Com um único extensômetro ativo, o que se chama um quarto de ponte, a saída é aproximadamente a tensão de excitação vezes o fator do extensômetro vezes a deformação, tudo dividido por quatro. Guarde essa conta, porque daqui a pouco ela vai explicar a linha reta do estagiário. Já adianto: o resultado é da ordem de microvolts. E microvolts precisam de um amplificador de instrumentação antes de chegar ao conversor."

> "O condicionamento também inclui o filtro anti-aliasing: um filtro passa-baixas antes do ADC, que impede que frequências acima da metade da taxa de amostragem apareçam como sinais falsos. É o Nyquist, que você viu na aula passada, agora protegido por hardware."

### 4. O laço de corrente 4–20 mA (4:10 – 5:30)

**[TELA]** Slide 6 — o laço de corrente 4–20 mA.

> "Outro padrão que você vai encontrar muito em obra é o laço de corrente de quatro a vinte miliampères. Em vez de mandar o valor como tensão, o transdutor manda como corrente. Por que isso é bom? Porque a corrente é a mesma ao longo de todo o cabo, então cabos longos e ruído elétrico do canteiro atrapalham muito menos."

> "E tem um detalhe genial: o zero vivo. O zero da escala não é zero miliampère, é quatro. Então, se a corrente cair a zero, eu sei que não é uma leitura nula: é cabo rompido ou sensor desligado. O sistema consegue diferenciar 'não tem pressão' de 'perdi o sensor'. Para o microcontrolador ler, um resistor de carga transforma corrente em tensão. Com cento e vinte ohms, quatro a vinte miliampères viram zero vírgula quarenta e oito a dois vírgula quatro volts, dentro da faixa em que o ADC do ESP32 mede com precisão, que vai até uns dois vírgula quatro volts. Na tela, o piezômetro de zero a duzentos quilopascals com setenta quilopascals: a corrente é quatro mais setenta vezes dezesseis sobre duzentos, nove vírgula seis miliampères. E o caminho de volta, que o sistema faz a cada leitura: pressão é a corrente menos quatro, vezes doze vírgula cinco. Nove vírgula seis menos quatro dá cinco vírgula seis; vezes doze vírgula cinco, setenta quilopascals."

> "Os sensores de corda vibrante são um terceiro caso: eles precisam ser excitados e ter a frequência medida, o que exige uma interface específica. É comum em datalogger profissional, e raro em placa de protótipo."

### 5. O ADC e os bits (5:30 – 6:50)

**[TELA]** Slide 7 — simulação: quantos bits tem o seu ADC? Comece com 10 bits e depois passe para 12 e 16.

> "Agora o conversor analógico-digital. Um ADC de n bits divide a faixa de entrada em dois elevado a n degraus. O menor degrau se chama LSB, e vale a tensão de referência dividida por dois elevado a n. Na simulação, eu tenho um sinal suave entrando. Com dez bits, como no Arduino Uno, que tem mil e vinte e quatro níveis em cinco volts, cada degrau vale uns quatro vírgula nove milivolts. Repara na escada no gráfico."

> "Passo para doze bits, como no ESP32: quatro mil e noventa e seis níveis. A escada fica bem mais fina. Mas o ADC do ESP32 tem fama conhecida: não linearidade e desvio de uma placa para outra. Então ele precisa ser calibrado, ou substituído por um ADC externo. Passo para dezesseis bits, como num ADS1115: a escada quase some. E, para pontes de extensômetros e células de carga, existe o HX711, com vinte e quatro bits e ganho interno."

### 6. Exemplo: os 165 microvolts (6:50 – 8:20)

**[TELA]** Slide 8 — exemplo numérico: por que a linha ficou reta?

> "Agora a gente resolve o mistério da linha reta. O extensômetro do estagiário tem fator dois, está num quarto de ponte excitado com três vírgula três volts e sofre cem microdeformações. Três vírgula três vezes dois vezes cem milionésimos, dividido por quatro, dá cento e sessenta e cinco microvolts de saída."

> "E quanto vale um degrau do ADC do ESP32? Três vírgula três volts divididos por quatro mil e noventa e seis: uns oitocentos e seis microvolts. Percebeu? O sinal inteiro, de cento e sessenta e cinco microvolts, cabe dentro de um único degrau. O conversor nunca vê a mudança. A escora carregava, e a tela mostrava uma linha reta. O sensor não mentiu: quem mentiu foi a cadeia."

> "A solução é amplificar. Com um amplificador de ganho quinhentos, a saída vai para oitenta e dois vírgula cinco milivolts: uns cem degraus do ADC. Aí cada degrau equivale a mais ou menos uma microdeformação. Os valores são ilustrativos, mas a lição é real: antes de confiar no gráfico, compare o tamanho do sinal com o tamanho do degrau."

> "E, no caso do piezômetro de quatro a vinte miliampères com o resistor de cento e vinte ohms, um degrau do ADC vale uns seis vírgula sete microampères. Como a escala é de doze vírgula cinco quilopascals por miliampère, isso dá uns zero vírgula zero oitenta e quatro quilopascal: cerca de nove milímetros de coluna d'água. Para nível d'água em escavação, é uma resolução perfeitamente utilizável."

### 7. Arduino, ESP32 e datalogger (8:20 – 9:50)

**[TELA]** Slide 9 — Arduino, ESP32 e o datalogger profissional.

> "Vamos conhecer as plataformas. O Arduino é a porta de entrada: simples, com uma comunidade enorme, ótimo para aprender e prototipar. Mas ele não tem rádio nativo. O ESP32, da Espressif, é um microcontrolador de trinta e dois bits com Wi-Fi e Bluetooth integrados, modo de sono profundo e preço baixo. É a escolha natural para protótipos IoT, e você programa ele na mesma IDE do Arduino."

> "E existe uma terceira categoria: o datalogger profissional. Ele tem entradas para corda vibrante e para pontes, multiplexadores para dezenas de canais, funciona numa faixa larga de temperatura, vem numa caixa com grau de proteção elevado, tem relógio estável, memória para meses e certificado de calibração."

> "A regra prática é esta. Arduino e ESP32 são excelentes para protótipos, para ensino e para monitoramentos de baixa criticidade: temperatura, umidade, poeira, ocupação de áreas. Agora, se a leitura embasa uma decisão de segurança, como uma contenção ou um vizinho que recalca, usam-se instrumentos e dataloggers com calibração rastreável, instalados por equipe qualificada. Não é preconceito com a placa barata; é responsabilidade técnica."

### 8. Barramentos digitais (9:50 – 10:50)

**[TELA]** Slide 10 — sensores que já falam digital: I²C, SPI, UART, 1-Wire, SDI-12 e RS-485.

> "Muitos sensores modernos já entregam o valor pronto, em digital, e aí o problema do ADC fica dentro do próprio sensor. Eles conversam com o microcontrolador por barramentos. I2C e SPI são de curta distância, na mesma placa, como o sensor de umidade da aula passada. UART é a serial clássica, usada por muitos sensores de poeira. 1-Wire é usado por termômetros como o DS18B20. SDI-12 é muito comum em sensores ambientais e dataloggers. E RS-485 com Modbus é o padrão industrial, que aguenta centenas de metros de cabo. Na obra, quando o cabo é longo e o ambiente é hostil, RS-485 e quatro a vinte miliampères são os seus melhores amigos."

### 9. Amostragem, relógio e memória (10:50 – 12:10)

**[TELA]** Slide 11 — amostragem, relógio e memória.

> "O microcontrolador decide quando ler. E a taxa segue a velocidade do fenômeno. Um piezômetro pode ser lido a cada quinze minutos; a vibração de uma cravação exige centenas de amostras por segundo. Um truque barato: ler várias vezes seguidas e tirar a média. Isso se chama sobreamostragem, e reduz o ruído aleatório pela raiz do número de leituras. Dezesseis leituras, ruído quatro vezes menor."

> "Toda leitura precisa de hora confiável, e em UTC, para não brigar com fuso e horário de verão. Para isso, usa-se um relógio de tempo real com bateria própria, sincronizado pela rede ou por GNSS. E a leitura fica guardada em memória local, cartão SD ou flash, até a confirmação de envio. Se a rede cair por um dia, nada se perde: quando ela volta, o nó manda tudo com a hora em que mediu, não a hora em que chegou."

### 10. Energia: a bateria do estagiário (12:10 – 13:50)

**[TELA]** Slide 12 — calculadora de autonomia. Comece com 0,15 mA em sono; depois mude para 10 mA.

> "Agora a segunda falha do estagiário: a bateria. A conta é simples. O consumo médio é a carga gasta num ciclo dividida pela duração do ciclo. E a autonomia é a capacidade útil da bateria dividida pelo consumo médio."

> "Nosso nó acorda a cada quinze minutos, ou seja, a cada novecentos segundos. Fica cinco segundos acordado a cento e vinte miliampères, lendo, conectando ao Wi-Fi e enviando, e dorme oitocentos e noventa e cinco segundos. Numa placa de baixo consumo, dormindo a zero vírgula quinze miliampère, a média dá uns zero vírgula oitenta e dois miliampère. Com sete mil e duzentos miliampères-hora úteis, são umas oito mil e oitocentas horas: cerca de um ano."

> "Agora eu mudo só uma coisa: o consumo dormindo, para dez miliampères. É o que gasta uma placa de desenvolvimento comum, por causa do regulador de tensão e do conversor USB, mesmo com o chip ESP32 dormindo a uns dez microampères. A média sobe para dez vírgula seis miliampères, e a bateria dura umas seiscentas e oitenta horas: vinte e oito dias. Mesmo programa, mesma bateria. Quem decide a autonomia é o sono. E o protótipo do estagiário? Placa de desenvolvimento e uma bateria pequena, de uns quinhentos miliampères-hora: quinhentos dividido por dez vírgula seis dá umas quarenta e sete horas. Dois dias. Por isso a bateria acabou na terça."

> "Onde a demanda é maior, como num gateway ou numa câmera, entra o painel solar, com controlador de carga e uma bateria dimensionada para aguentar os dias nublados."

### 11. Instalação em campo (13:50 – 15:10)

**[TELA]** Slide 13 — instalação em campo: grau de proteção, surtos, ficha e comissionamento.

> "E a terceira falha: a chuva na caixa. Instalação é engenharia, não detalhe. A caixa precisa de grau de proteção adequado, segundo a norma NBR IEC 60529: IP65 aguenta jatos d'água; IP67, imersão temporária. Prensa-cabos de verdade, nada de furo com fita isolante, e um saquinho de dessecante dentro. Proteção contra surtos e aterramento, principalmente com cabos longos e mastros, porque raio em canteiro não é raro. Cabos em eletroduto, longe do trajeto das máquinas. Antena fora da caixa metálica. E um acesso seguro para manutenção, sem expor ninguém a risco."

> "Olha essa foto de uma estação de monitoramento em campo: a caixa do datalogger presa no mastro, o painel solar inclinado logo abaixo, o sensor com abrigo lá no alto, os cabos descendo organizados. Nada disso é enfeite. O mastro tira o equipamento do alcance da lama e das máquinas, o abrigo protege o sensor do sol direto, que falsearia a temperatura, e a caixa fechada guarda a eletrônica da chuva. Agora pensa no canteiro real: retroescavadeira passando, caminhão manobrando, servente lavando a betoneira ao lado. Um cabo solto no chão dura uma semana. Uma caixa sem identificação é arrancada na primeira limpeza da frente de serviço. Por isso, combine com a produção onde cada nó vai ficar, sinalize e inclua a instrumentação no planejamento da obra."

> "Cada instalação gera uma ficha: identificação igual à do banco de dados, número de série, coordenadas, profundidade ou cota, foto, data e hora, fatores de calibração e leitura zero. E, antes de dizer que está pronto, o comissionamento: testar a alimentação, testar a comunicação e verificar se as primeiras leituras fazem sentido físico."

### 12. Do protótipo à produção, atividade e encerramento (15:10 – 17:20)

**[TELA]** Slide 14 — do protótipo à produção.

> "Vamos voltar ao estagiário, agora com tudo o que você aprendeu. Linha reta: sinal de cento e sessenta e cinco microvolts num degrau de oitocentos; faltou amplificar. Bateria de dois dias: placa de desenvolvimento dormindo a miliampères; faltou escolher hardware de baixo consumo. Água na caixa: faltou grau de proteção e prensa-cabos. O protótipo foi útil, sim: ele ensinou onde estão as armadilhas. O passo seguinte é transformar o protótipo em produto de campo, ou reconhecer quando a aplicação pede um datalogger profissional."

**[TELA]** Slide 15 — atividade prática no Wokwi.

> "Sua atividade é no simulador gratuito Wokwi. Monte um ESP32 com um sensor de temperatura e umidade DHT22 e um potenciômetro que faça o papel de um transdutor analógico. Programe a leitura a cada dez segundos, converta o valor bruto do ADC para unidade de engenharia e imprima cada leitura com a hora. Depois, escreva a ficha de instalação desse nó numa obra real: caixa, grau de proteção, alimentação, autonomia estimada, local e leitura zero."

**[TELA]** Slide 16 — pontos-chave.

> "Recapitulando: a cadeia vai do sensor ao condicionamento, ao ADC, ao microcontrolador, à memória e ao rádio, e o dado tem a qualidade do elo mais fraco. Compare sempre o sinal com o degrau do ADC. O quatro a vinte miliampères é robusto e denuncia cabo rompido. Arduino e ESP32 para protótipo e baixa criticidade; datalogger calibrado para decisão de segurança. A autonomia é decidida pelo sono, e a instalação pede proteção, ficha, leitura zero e comissionamento."

**[TELA]** Slide 17 — encerramento e gancho para a Aula 11.

> "Agora o dado existe e está guardado no nó, lá no terceiro subsolo. Mas ele precisa sair dali e atravessar a cidade até o servidor. LoRaWAN, Wi-Fi ou rede celular? E por que o sinal some justamente no subsolo? Te espero na Aula 11!"


---

## Roteiro da Videoaula 11 — "Por que o sinal some no subsolo? A rede certa para cada sensor"

**Aula 11 — Redes de comunicação: LoRaWAN, Wi-Fi e redes celulares**

**Duração-alvo:** cerca de 18:50 (15 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 11 de Drones e Sensores IoT no Monitoramento de Obras. Até aqui, nesta unidade, você conheceu os sensores, na Aula 9, e as plataformas embarcadas que transformam o sinal do sensor em número, na Aula 10. O dado já existe e está guardado na memória do nó. Hoje a pergunta é outra: como esse dado sai do canteiro? Como ele sobe do terceiro subsolo, atravessa a cidade e chega ao servidor? O assunto é redes de comunicação: LoRaWAN, Wi-Fi e redes celulares."

**[TELA]** Slide 3 — o primeiro dia da rede na obra.

> "Deixa eu te contar o primeiro dia de uma obra que eu vou usar como exemplo a aula inteira. A construtora instalou piezômetros no terceiro subsolo, inclinômetros atrás da cortina de estacas, um sensor de poeira na divisa com a vizinhança e câmeras no alto da grua. E aí começaram os problemas. O Wi-Fi do escritório de obra, que funcionava muito bem para os notebooks, não chegava ao subsolo. O sensor de poeira, que alguém resolveu ligar com um chip 4G comum, acabou com a bateria em uma semana. E as câmeras, mandando vídeo o dia inteiro, congestionaram a rede de todo mundo, inclusive a do escritório."

> "Repara que nenhum desses problemas é defeito de equipamento. É escolha errada de rede. Cada tecnologia foi feita para um tipo de uso, e a gente usou a ferramenta certa no lugar errado."

### 2. O triângulo de compromissos (1:30 – 3:00)

**[TELA]** Slide 4 — o triângulo alcance × taxa × consumo.

> "Toda escolha de rede sem fio equilibra três grandezas que puxam em sentidos opostos. A primeira é o alcance: até onde o sinal chega. A segunda é a taxa de dados: quanta informação passa por segundo. A terceira é o consumo de energia: quanto da bateria cada mensagem custa. E aqui vai a regra que eu quero que você leve desta aula: não dá para maximizar as três ao mesmo tempo."

> "Redes de longo alcance e baixo consumo transmitem pouco, mensagens de poucas dezenas de bytes. Redes de alta taxa gastam muita energia ou alcançam pouco. E a esses três critérios se somam outros, bem práticos: o custo, tanto do equipamento quanto da mensalidade; a cobertura disponível naquele endereço; a latência, que é o tempo que a mensagem leva para chegar; e uma pergunta que quase ninguém faz no começo: quem opera essa rede? A própria obra ou uma operadora? Guarde essa pergunta, porque ela volta na pausa para reflexão."

### 3. Propagação e orçamento de enlace (3:00 – 5:50)

**[TELA]** Slide 5 — propagação no canteiro: distância, frequência e obstáculos.

> "Antes de comparar as tecnologias, a gente precisa entender por que o sinal some. Um sinal de rádio enfraquece com a distância, mesmo no espaço livre, sem nenhum obstáculo. Essa perda tem uma fórmula: vinte vezes o logaritmo da distância em quilômetros, mais vinte vezes o logaritmo da frequência em megahertz, mais trinta e dois vírgula quarenta e quatro. O resultado sai em decibéis."

> "Repara que a frequência está na fórmula. Quanto maior a frequência, maior a perda. Por isso as faixas abaixo de um gigahertz, como os 915 megahertz usados pela LoRaWAN no Brasil, chegam mais longe e atravessam melhor os obstáculos do que os 2,4 gigahertz do Wi-Fi. E no canteiro, obstáculo é o que não falta: paredes e lajes de concreto, armaduras, o próprio terreno, máquinas, contêineres. Cada parede de concreto pode tirar dez decibéis ou mais. E o subsolo é o pior caso: cercado de terra e concreto, ele pode bloquear o sinal quase por completo."

**[TELA]** Slide 6 — calculadora do orçamento de enlace. Comece com o nó no subsolo a 1,5 km e em SF7; depois mude para SF12.

> "Para saber se o sinal chega, a gente faz o orçamento de enlace, o link budget. A conta é simples: potência recebida é igual à potência transmitida, mais os ganhos das antenas, menos todas as perdas. O enlace funciona se essa potência recebida for maior que a sensibilidade do receptor, o menor sinal que ele consegue entender, com uma folga, que a gente chama de margem. Na prática, queremos dez decibéis de margem ou mais, porque o canal varia: chove, passa um caminhão, a grua gira."

> "Vamos ao nosso piezômetro no subsolo. O nó transmite com 14 dBm, tem uma antena de 2 dBi, e o gateway, a um quilômetro e meio, tem antena de 3 dBi. A perda no espaço livre, a 915 megahertz e um quilômetro e meio, dá uns 95,2 decibéis. E eu vou somar 35 decibéis de perdas por obstáculos, lajes e cabos. Esse valor é ilustrativo, mas é da ordem de grandeza real de um subsolo. Resultado: catorze, mais dois, mais três, menos 95,2, menos 35: a potência recebida é de menos 111,2 dBm."

> "Agora comparo com a sensibilidade. Em SF7, um rádio LoRa típico ouve até menos 123 dBm. A margem é de 11,8 decibéis: fecha, com folga. Vou mudar para SF12: a sensibilidade vai para menos 137 dBm, e a margem sobe para 25,8. Também fecha, com mais folga ainda. Então por que não usar sempre SF12? Segura essa pergunta, que a resposta vem daqui a pouco. E duas boas práticas que saem dessa conta: gateway e antenas no alto, no topo da grua ou na cobertura do canteiro, com visada para os sensores; e antena sempre fora da caixa metálica. Caixa metálica é uma gaiola de Faraday: ela engole o seu sinal."

### 4. LoRaWAN (5:50 – 9:10)

**[TELA]** Slide 7 — a arquitetura LoRaWAN: nó, gateway, servidor de rede e aplicação.

> "Vamos à primeira tecnologia. Atenção aos nomes: LoRa é a modulação de rádio, uma técnica chamada espalhamento espectral por chirp, em que o sinal varre a frequência como um assobio que sobe. LoRaWAN é o protocolo de rede, mantido pela LoRa Alliance, que organiza quem fala com quem."

> "A topologia é em estrela de estrelas. Na ponta, os dispositivos finais, os nossos nós sensores. Eles transmitem para qualquer gateway que estiver ao alcance, e pode ser mais de um. O gateway é um intermediário bem simples: ele não abre a mensagem, só a encaminha, pela internet, a um servidor de rede. O servidor de rede elimina as cópias repetidas que chegaram por gateways diferentes, controla a taxa de dados de cada nó e entrega a mensagem ao servidor de aplicação, onde ela vai ser usada. E tudo isso vai cifrado, com AES de 128 bits: o gateway encaminha o pacote sem conseguir ler o conteúdo."

> "Na tela, uma montagem de demonstração: à esquerda, um nó numa caixinha preta, ligado a uma sonda de umidade do solo; à direita, um gateway em cima de um computador de placa única. É isso. A infraestrutura de uma rede LoRaWAN privada cabe numa mesa."

**[TELA]** Slide 8 — fator de espalhamento × tempo no ar × energia.

> "Agora a resposta da pergunta que ficou pendente. O parâmetro-chave da LoRa é o fator de espalhamento, o spreading factor, que vai de SF7 a SF12. Cada passo para cima ganha uns dois decibéis e meio de sensibilidade, ou seja, mais alcance. Mas praticamente dobra o tempo que a mensagem fica no ar. E tempo no ar é energia."

> "Vamos às contas do texto. Uma mensagem com 12 bytes de dados, que viram 25 bytes no quadro LoRaWAN, numa largura de banda de 125 quilohertz, fica no ar cerca de 62 milissegundos em SF7. Em SF12, cerca de um segundo e quarenta e oito. Transmitindo a 120 miliampères, a mensagem em SF7 custa uns 7,4 miliampères-segundo; em SF12, uns 178. É cerca de vinte e quatro vezes mais energia por mensagem. E tem mais: enquanto um nó fala em SF12, ele ocupa o canal vinte e quatro vezes mais tempo, e os vizinhos esperam."

> "Por isso existe a taxa de dados adaptativa, o ADR: o servidor de rede observa a qualidade com que cada nó chega e manda o nó usar o menor SF que garanta o enlace. No nosso subsolo, se o SF7 já dá quase 12 decibéis de margem, é ele. E um alerta: alguns planos de frequência limitam o tempo no ar por transmissão, o que pode até impedir os SF mais altos. Confira sempre o plano usado e a regulamentação vigente."

> "Mais três detalhes. As mensagens são pequenas, dezenas de bytes, o que basta para uma leitura de piezômetro, mas não serve para foto. Os dispositivos classe A, os mais econômicos, só escutam a rede logo depois de transmitir: se você quiser mandar um comando para o nó, ele chega na próxima vez que o nó falar. E no Brasil a LoRaWAN opera na faixa de 915 a 928 megahertz, nos planos AU915 ou LA915, de uso não licenciado, mas com equipamentos que precisam de homologação da Anatel. A obra pode montar a própria rede, com gateway próprio, ou usar uma rede de terceiros."

### 5. Wi-Fi (9:10 – 10:40)

**[TELA]** Slide 9 — Wi-Fi: muita taxa, pouco alcance, muita energia.

> "Segunda tecnologia: o Wi-Fi, a família IEEE 802.11, que você conhece de casa. Ele opera em 2,4 e 5 gigahertz e, nas versões mais recentes, em 6 gigahertz. Oferece dezenas a centenas de megabits por segundo. Perfeito para câmeras, para o escritório de obra, para os tablets da fiscalização e para equipamentos que têm tomada por perto."

> "O alcance é de dezenas de metros em ambiente interno e algumas centenas ao ar livre, com antenas externas e visada. Na tela, um ponto de acesso externo num mastro sobre o telhado. Para ligar dois prédios distantes, usam-se enlaces ponto a ponto, com antenas direcionais apontadas uma para a outra."

> "O preço é o consumo. Conectar-se ao ponto de acesso e manter a associação gasta muita energia, e isso não combina com um sensor a bateria lido a cada poucos minutos. Lembra da Aula 10? O nó que acorda, conecta no Wi-Fi e publica gasta uns 120 miliampères durante segundos. E um detalhe prático: o ESP32 clássico só fala em 2,4 gigahertz. Em canteiros grandes, uma boa solução é a rede em malha, o mesh, com vários pontos de acesso que se repetem e acompanham a obra conforme ela cresce. E segurança desde o começo: WPA2 ou WPA3 e a rede dos sensores separada da rede administrativa."

### 6. Redes celulares (10:40 – 12:30)

**[TELA]** Slide 10 — redes celulares: 4G, 5G, LTE-M e NB-IoT.

> "Terceira família: as redes celulares. A grande vantagem é que a infraestrutura é da operadora. Você não monta gateway, não sobe antena na grua: põe um chip no equipamento e pronto. A desvantagem: tem mensalidade por chip e você depende da cobertura naquele endereço."

> "O 4G e o 5G dão alta taxa e servem muito bem para gateways, câmeras e para mandar as imagens do drone. Mas, para sensor a bateria, eles gastam demais: foi o erro do nosso sensor de poeira. Para isso, a 3GPP, que padroniza as redes celulares, criou duas versões de baixa potência. O LTE-M, ou Cat-M1, com taxa de centenas de quilobits até um megabit por segundo e suporte a mobilidade: ótimo para um rastreador num caminhão ou numa máquina que se desloca. E o NB-IoT, com taxa menor, mas com cobertura profunda: ele atravessa melhor paredes e subsolos, e o consumo é muito baixo."

> "Os dois têm modos de economia de energia, o PSM e o eDRX, em que o módulo dorme por longos períodos, mas sem perder o registro na rede. Ele acorda, manda a leitura e volta a dormir, sem refazer todo o processo de conexão. Duas recomendações antes de escolher: confirme com a operadora, por escrito, a cobertura de LTE-M ou NB-IoT no endereço da obra, de preferência com um teste no subsolo. E lembre que as redes 2G e 3G estão em desligamento gradual: não compre equipamento que dependa delas."

### 7. Comparando e se protegendo das falhas (12:30 – 14:00)

**[TELA]** Slide 11 — tabela comparativa das redes.

> "Na tela, a tabela que resume tudo. Não vou ler linha por linha: veja o padrão. LoRaWAN: quilômetros, pouca taxa, anos de bateria, gateway próprio ou de terceiros. NB-IoT: cobertura da operadora com boa penetração, pouca taxa, consumo muito baixo. LTE-M: um pouco mais de taxa e mobilidade. 4G e 5G: alta taxa, alto consumo. Wi-Fi: alta taxa, curto alcance, alto consumo, infraestrutura própria."

> "A regra prática: leitura lenta a bateria, LoRaWAN ou NB-IoT. Muito dado com energia disponível, Wi-Fi ou 4G e 5G. Voltando ao primeiro dia da obra: piezômetros e inclinômetros, LoRaWAN ou NB-IoT. Sensor de poeira, LoRaWAN, ou Wi-Fi se ele estiver junto à tomada do tapume. Câmeras da grua, 4G dedicado ou um enlace Wi-Fi ponto a ponto separado do escritório."

**[TELA]** Slide 12 — armazenar e reenviar, e rota alternativa.

> "E agora uma verdade incômoda: toda rede falha. O gateway reinicia, a operadora tem uma pane, alguém desliga o disjuntor do contêiner. Por isso, qualquer que seja a rede, o nó deve fazer armazenar e reenviar, o store-and-forward. Ele guarda cada leitura, com o carimbo de tempo da medição, não da chegada, e reenvia tudo quando a conexão volta. Assim, uma queda de doze horas vira um atraso de doze horas, e não um buraco de doze horas no gráfico."

> "Para sensores críticos, vale ir além: ter uma rota alternativa. Dois gateways cobrindo a mesma área, ou um gateway com conexão 4G de reserva para o caso de a internet fixa cair. E um alerta que muita obra esquece: alguém precisa ser avisado quando um sensor para de transmitir. Silêncio não é sinal de que está tudo bem."

### 8. Pausa para reflexão (14:00 – 15:20)

**[TELA]** Slide 13 — pausa para reflexão: rede própria ou da operadora?

> "Agora, pare o vídeo se precisar, e pense comigo. A construtora pode montar a própria rede LoRaWAN, com um gateway no topo da grua e um servidor de rede contratado. Ou pode usar chips NB-IoT de uma operadora."

> "Na primeira opção, a obra controla tudo, não paga mensalidade por sensor e não depende da cobertura de terceiros. Mas alguém precisa manter o gateway funcionando às duas da manhã. E repara num detalhe: quando a grua for desmontada, a rede vai junto com ela. Na segunda opção, a operadora cuida da infraestrutura, mas a obra depende da cobertura no subsolo, paga por chip e fica sem dados se a operadora tiver uma falha."

> "Então: quem deve operar a rede que transporta dados de segurança? Pense em três perguntas. O que acontece com os sensores que precisam continuar lendo depois da entrega da obra, por exemplo, o recalque do vizinho nos meses seguintes? Existe rota alternativa se a rede principal cair? E quem é avisado quando um sensor para de transmitir? Não existe resposta única. Mas existe resposta errada: não ter pensado nisso antes de comprar os equipamentos."

### 9. Atividade, pontos-chave e encerramento (15:20 – 17:30)

**[TELA]** Slide 14 — atividade prática.

> "Sua atividade: pegue a obra do nosso exemplo, com piezômetros no terceiro subsolo, inclinômetros atrás da cortina, sensor de poeira na divisa e câmeras na grua. Escolha a rede de cada grupo de sensores e justifique por alcance, taxa, consumo, custo e cobertura. Desenhe a planta com a posição do gateway ou dos pontos de acesso. Faça o orçamento de enlace do sensor mais desfavorável, igual fizemos na calculadora. E defina o que acontece com os dados se a conexão cair por doze horas."

**[TELA]** Slide 15 — pontos-chave.

> "Vamos amarrar. Primeiro: a rede se escolhe pelo compromisso entre alcance, taxa e consumo, somado a custo, cobertura, latência e quem opera. Segundo: o orçamento de enlace compara a potência recebida com a sensibilidade, e subsolo e concreto cobram caro; queira dez decibéis de margem ou mais. Terceiro: LoRaWAN é longo alcance, baixíssimo consumo e mensagens pequenas, e SF maior dá mais alcance ao custo de mais tempo no ar e mais energia. Wi-Fi e 4G e 5G têm alta taxa e alto consumo; NB-IoT e LTE-M são os celulares de baixa potência, com cobertura a confirmar. Quarto: toda rede falha, então o nó armazena e reenvia, e sensor crítico merece rota alternativa."

**[TELA]** Slide 16 — encerramento e gancho para a Aula 12.

> "Hoje o dado saiu do subsolo e atravessou a cidade. Mas, quando ele chega do outro lado, quem recebe? Como mensagens de sessenta sensores, de fornecedores diferentes, chegam em ordem, sem se perder, e onde elas são guardadas para virar gráfico e alerta? Na próxima aula, você vai conhecer um carteiro chamado MQTT, o Node-RED e os bancos de séries temporais. Te espero na Aula 12!"

---

## Roteiro da Videoaula 12 — "Um carteiro chamado MQTT: como milhares de leituras chegam ao banco de dados sem se perder"

**Aula 12 — Protocolos e plataformas IoT: MQTT e armazenamento de séries temporais**

**Duração-alvo:** cerca de 16:50 (15 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 12 de Drones e Sensores IoT no Monitoramento de Obras, a última da Unidade 3. Até aqui, o dado nasceu no sensor, na Aula 9, virou número na plataforma embarcada, na Aula 10, e atravessou a rede, na Aula 11. Hoje ele chega ao destino. O assunto é protocolos e plataformas IoT: o MQTT, o Node-RED e o armazenamento em séries temporais, com o InfluxDB."

**[TELA]** Slide 3 — três fornecedores, três portais, uma planilha.

> "Imagina uma obra com sessenta sensores de três fornecedores diferentes. Cada fornecedor tem o seu portal, a sua senha, o seu formato de arquivo e, pior, o seu relógio: um grava no horário de Brasília, outro em UTC, outro no horário do datalogger, que ninguém acertou. Toda segunda-feira, o engenheiro baixa três planilhas, acerta os fusos à mão e cola tudo numa quarta planilha para ver se o recalque do vizinho acompanha a subida da água no solo. E quando um sensor para de transmitir, ninguém percebe por dias."

> "O problema aqui não é sensor nem rede. Os dados estão chegando. O que falta é uma linguagem comum para as mensagens e um lugar comum para guardá-las. É isso que a gente vai construir hoje."

### 2. A pilha IoT (1:40 – 3:00)

**[TELA]** Slide 4 — a pilha IoT: percepção, rede, plataforma e aplicação.

> "Gubbi e colegas, num artigo de 2013 que está na bibliografia da disciplina, descrevem a Internet das Coisas como a integração de sensores, redes, armazenamento e análise em nuvem, e visualização. Na nossa obra, isso vira quatro camadas. A percepção: sensores e nós, a Aula 10. A rede: LoRaWAN, Wi-Fi, celular, a Aula 11. A plataforma: quem recebe as mensagens, integra e guarda, que é a aula de hoje. E a aplicação: painéis, alertas e integração com o BIM, que é a Unidade 4."

> "Entre a rede e a plataforma, as mensagens precisam de um protocolo de aplicação, um combinado sobre como conversar. O HTTP, o protocolo da web, funciona: o sensor faz uma requisição e o servidor responde. Mas ele é pesado para um dispositivo pequeno, cheio de cabeçalhos. Existe o CoAP, uma versão enxuta sobre UDP. E existe o MQTT, que virou o padrão de fato da IoT. É nele que a gente vai mergulhar."

### 3. MQTT: publicar e assinar (3:00 – 5:00)

**[TELA]** Slide 5 — publicar e assinar por meio de um broker.

> "O MQTT é um protocolo leve de mensagens, padronizado pela OASIS nas versões 3.1.1 e 5.0, e funciona sobre TCP/IP. A grande sacada é que os dispositivos não conversam diretamente entre si. Todos se conectam a um servidor central, o broker. Pense no broker como uma agência dos correios com caixas postais etiquetadas."

> "Um cliente publica uma mensagem num tópico, que é a etiqueta da caixa postal. O broker entrega essa mensagem a todos os clientes que assinaram aquele tópico. Na tela: à esquerda, o publicador; no centro, o broker; à direita, dois assinantes recebendo a mesma mensagem. Os brokers mais conhecidos são o Mosquitto, o EMQX e o HiveMQ."

> "Repara no que isso resolve. O publicador e o assinante não se conhecem. O sensor não sabe quem vai usar a leitura, e o painel não precisa saber de onde ela veio. Se amanhã eu quiser acrescentar um novo consumidor, um painel novo, um registro de auditoria, um sistema de alertas, eu não mexo em nenhum sensor: só faço o novo cliente assinar o tópico. É isso que acaba com as três planilhas da segunda-feira."

> "E de onde vêm as mensagens? Se o nó tem Wi-Fi ou 4G, como o ESP32 da Aula 10, ele publica diretamente no broker. Se a rede é LoRaWAN, quem publica normalmente é o servidor de rede, por meio da sua integração MQTT: o nó manda o pacote de rádio, o servidor decodifica e publica."

### 4. Tópicos e curingas (5:00 – 6:40)

**[TELA]** Slide 6 — simulação dos tópicos e curingas. Digite primeiro a assinatura com mais nos níveis de setor e sensor; depois a assinatura com cerquilha.

> "Os tópicos são hierárquicos, com níveis separados por barra, como um endereço. No nosso exemplo: obra, barra, torre-a, barra, escavação, barra, piezômetro, barra, PZ-03, barra, nível. Um bom padrão segue a lógica obra, setor, tipo, sensor, grandeza. E evite espaços e acentos: escreva escavação sem cedilha e sem til."

> "Agora vem a parte boa: os curingas, que o assinante usa. O sinal de mais substitui exatamente um nível. Vou assinar obra, torre-a, mais, piezômetro, mais, nível. Olha a simulação: chegam os níveis de todos os piezômetros, de todos os setores. O primeiro mais pegou o setor; o segundo, o sensor. Agora vou assinar obra, barra, torre-a, barra, cerquilha. A cerquilha substitui todos os níveis abaixo, e chega tudo da torre A: piezômetros, inclinômetros, poeira, status. Um detalhe que cai em prova: a cerquilha só pode ficar no final do tópico. Não dá para colocá-la no meio."

### 5. QoS, mensagem retida e último desejo (6:40 – 8:40)

**[TELA]** Slide 7 — QoS, mensagem retida e último desejo.

> "Agora, a garantia de entrega. O MQTT tem três níveis de qualidade de serviço, o QoS, e eles valem em cada trecho: do publicador ao broker e do broker ao assinante. QoS zero: no máximo uma vez. A mensagem vai e ninguém confirma; se se perder, perdeu. QoS um: pelo menos uma vez. Há confirmação, e se ela não vier a mensagem é reenviada, então pode chegar duplicada. QoS dois: exatamente uma vez, com uma troca de quatro mensagens. É o mais seguro e o mais lento."

> "Para leitura de sensor, o equilíbrio costuma ser QoS um, com cada leitura identificada pelo carimbo de tempo da medição. Se chegar uma duplicata, ela tem o mesmo instante e o mesmo valor: não cria dado falso, é só descartada ou sobrescrita por ela mesma."

> "Mais três recursos muito úteis no canteiro. A mensagem retida, o retain: o broker guarda a última mensagem do tópico e entrega a quem assinar depois. Um painel que abre às oito da manhã já recebe o último estado de cada sensor, sem esperar a próxima leitura. O último desejo, o Last Will: quando o nó se conecta, ele deixa com o broker uma mensagem de testamento, por exemplo offline no tópico de status. Se o nó cair sem se despedir, o broker publica essa mensagem sozinho. Lembra do sensor que parou e ninguém percebeu por dias? Resolvido. E o keep alive, um sinal periódico que detecta conexões mortas."

**[TELA]** Slide 8 — segurança do broker.

> "E, já que é broker de obra, segurança desde o primeiro dia. O broker deve exigir autenticação, usuário e senha ou certificado para cada dispositivo. Deve usar TLS, a criptografia, na porta 8883, em vez da 1883, que trafega tudo em texto aberto. E cada dispositivo só pode publicar nos seus próprios tópicos. Um sensor de poeira não tem por que publicar no tópico do piezômetro. Esse tema volta com força na Aula 16, de cibersegurança."

### 6. Node-RED (8:40 – 10:20)

**[TELA]** Slide 9 — um fluxo no Node-RED.

> "As mensagens estão chegando ao broker. Quem as pega, confere, converte e guarda? Uma opção muito usada é o Node-RED, uma ferramenta de código aberto, mantida pela OpenJS Foundation, em que você programa fluxos de dados ligando blocos num editor no navegador. Na tela, um exemplo simples do próprio projeto: entradas à esquerda, um filtro no meio, um atraso, e duas saídas, um bipe e um e-mail."

> "No nosso monitoramento, o fluxo típico tem quatro blocos. Um nó mqtt in, que assina os tópicos dos sensores. Um nó function, escrito em JavaScript, que valida a mensagem, aplica a calibração e marca a qualidade da leitura: por exemplo, pega os 9,6 miliampères do piezômetro e transforma em 70 quilopascals, como fizemos na Aula 10. Um nó switch, que separa as leituras das mensagens de status. E um nó de saída que grava tudo no banco de séries temporais. O mesmo fluxo pode avisar a equipe quando um sensor deixa de publicar."

> "E onde o Node-RED roda? Num computador da obra, num Raspberry Pi junto ao gateway, que é o processamento na borda, ou num servidor em nuvem. Na borda, ele continua funcionando mesmo se a internet cair."

### 7. A anatomia de uma leitura (10:20 – 11:40)

**[TELA]** Slide 10 — a anatomia de uma leitura.

> "Antes de guardar, vamos olhar com lupa o que é uma leitura. Uma série temporal é uma sequência de valores ordenados no tempo. E cada ponto de uma série de sensor precisa de sete coisas. O carimbo de tempo, em UTC, o da medição, não o da chegada. A identificação do sensor. O valor bruto: hertz, miliampères, contagens do ADC. O valor de engenharia: milímetros, quilopascals, obtido com a leitura zero e os fatores de calibração, que devem ter versão. A unidade. A marca de qualidade. E a saúde do nó: tensão da bateria, intensidade do sinal."

> "E a regra de ouro: nunca sobrescreva o dado bruto. Se a calibração mudar, se você descobrir que um fator estava errado, a correção é uma nova camada, rastreável. Todo dado de campo tem defeitos: picos espúrios, lacunas, deriva, ciclos térmicos, relógio desacertado. Só com o bruto preservado dá para tratar esses defeitos depois, e defender o seu número num laudo."

### 8. InfluxDB e o line protocol (11:40 – 13:40)

**[TELA]** Slide 11 — o modelo de dados do InfluxDB.

> "Onde guardar? Em bancos de séries temporais, otimizados para gravar dados na ordem em que chegam, comprimir valores parecidos e consultar por intervalo de tempo: me dá o nível do PZ-03 da última semana. O mais conhecido é o InfluxDB. Nele, cada ponto tem quatro partes. A measurement, que é o tipo de dado, por exemplo piezômetro. As tags, pares chave e valor de texto que descrevem e indexam a série: obra, setor, sensor. Os fields, que são os valores medidos: nível em metros, corrente bruta, tensão da bateria. E o timestamp."

> "A frase para guardar: tag é o que identifica a série; field é o que você mede."

**[TELA]** Slide 12 — o line protocol.

> "Os pontos são escritos num formato de texto chamado line protocol. Na tela, a nossa leitura. Primeiro, a measurement: piezômetro. Vírgula, as tags: obra igual a torre-a, sensor igual a PZ-03. Um espaço. Os fields: nível igual a 7.14, corrente bruta igual a 9.6, bateria igual a 3.61. Outro espaço. E o instante, um número enorme: nanossegundos desde primeiro de janeiro de 1970, em UTC. Aqui, dezenove de novembro de 2026, às cinco da manhã em UTC."

> "Dois detalhes. O line protocol usa ponto como separador decimal, não vírgula: cuidado ao converter da planilha brasileira. E os dados ficam num bucket, ou banco de dados, que tem um período de retenção. As consultas usam InfluxQL ou Flux nas versões 1 e 2, e SQL ou InfluxQL na versão 3."

### 9. Volume, cardinalidade e retenção (13:40 – 15:40)

**[TELA]** Slide 13 — calculadora de volume e cardinalidade. Comece com 60 sensores a cada 15 min; depois ative o acelerômetro contínuo; por fim, ative a tag errada.

> "Vamos fazer contas. Sessenta sensores, lidos a cada quinze minutos, são 96 leituras por dia cada um: 5.760 pontos por dia, uns 2,1 milhões por ano. Parece muito? A uns 100 bytes por linha, antes da compressão, são uns 576 quilobytes por dia. Isso cabe em qualquer lugar."

> "Agora vou ligar um único acelerômetro triaxial, gravando continuamente a 500 hertz. Três eixos, vezes 500, vezes 86.400 segundos do dia: cerca de 130 milhões de valores por dia. Um único sensor de vibração contínuo produz mais de vinte mil vezes os valores de todos os outros juntos. É por isso que vibração se grava por evento."

> "E agora o erro clássico. Com as tags obra e sensor, vinte piezômetros formam vinte séries, para sempre. Mas imagine que alguém pôs o identificador de cada leitura como tag. Cada ponto vira uma série nova: vinte vezes 96, 1.920 séries novas por dia, umas 700 mil por ano. Olha o contador disparando. Cada combinação de measurement e tags é uma série, e esse número é a cardinalidade. O índice cresce sem parar e as consultas ficam lentas. Identificador único e valor medido vão para os fields, nunca para as tags."

**[TELA]** Slide 14 — retenção e agregação.

> "Então como os sistemas maduros lidam com o volume? Guardam o dado bruto completo pelo prazo que o contrato e a responsabilidade técnica exigem. Mas os painéis mostram agregados, médias horárias, máximos diários, gerados por tarefas periódicas de subamostragem, o downsampling. Ninguém precisa desenhar dois milhões de pontos num gráfico de celular. E os registros de vibração são gravados por evento: o sensor guarda só as janelas em que um gatilho foi ultrapassado, mais um resumo periódico, como o pico de cada intervalo."

### 10. Atividade, pontos-chave, próxima unidade e encerramento (15:40 – 17:50)

**[TELA]** Slide 15 — atividade prática.

> "Sua atividade fecha a unidade com a mão na massa. Monte num computador, ou com contêineres Docker, um broker Mosquitto, o Node-RED e o InfluxDB. No Wokwi, faça o ESP32 da Aula 10 publicar, a cada dez segundos, uma leitura em JSON num tópico do tipo obra, sua obra, teste, umidade, UR-01, leitura, com mensagem de último desejo no tópico de status. No Node-RED, assine o tópico, converta o valor, marque a qualidade e grave no InfluxDB com tags e fields bem escolhidos. Para testes rápidos, existe o broker público test.mosquitto.org. Mas atenção: nunca use broker público para dado real de obra."

**[TELA]** Slide 16 — pontos-chave.

> "Pontos-chave. Um: MQTT é publicar e assinar por meio de um broker, com tópicos hierárquicos, curingas mais e cerquilha, QoS zero, um e dois, mensagem retida, último desejo e TLS com autenticação. Dois: o Node-RED liga os fluxos, assina, valida, calibra, marca a qualidade e grava, na borda ou na nuvem. Três: uma leitura é um registro completo, e o bruto nunca é sobrescrito. Quatro: no InfluxDB, measurement, tags, fields e timestamp; tag errada explode a cardinalidade, e retenção e agregação controlam o volume."

**[TELA]** Slide 17 — o que você verá na próxima unidade.

> "Com esta aula, você fecha a Unidade 3: o sensor, a plataforma embarcada, a rede e o banco de dados. Os dados agora chegam organizados. Na Unidade 4, Painéis, Integração com BIM e Gestão de Riscos, eles viram decisão. Na Aula 13, painéis de monitoramento com alertas e limites de alarme, no Grafana. Na Aula 14, a integração dos dados de drones e sensores com o BIM e com o planejamento e controle da obra. Na Aula 15, a tecnologia a favor da segurança do trabalho, à luz da NR-18. E, na Aula 16, privacidade, LGPD e cibersegurança, incluindo a segurança dos brokers e dispositivos que você conheceu hoje."

**[TELA]** Slide 18 — encerramento.

> "Foi um prazer acompanhar o seu dado do subsolo até o banco. Revise a atividade, faça o quiz e as questões da unidade, e a gente se vê na Unidade 4. Te espero na Aula 13!"
