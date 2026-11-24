# Roteiros das videoaulas — Unidade 3 — Sensores IoT e Redes de Comunicação

Disciplina: Drones e Sensores IoT no Monitoramento de Obras  
Professor: Afonso Cesar Lelis Brandão

> Cópia para a gravação, montada a partir de `roteiros_15min.md` (fala integral, versão a gravar). Os arquivos de origem não foram alterados.

> **Como usar:** leia as falas em citação (>) na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`).

---

## Roteiro da Videoaula 9 — "O que a obra sente e ninguém vê: seis sensores que contam tudo"

**Aula 9 — Sensores para obras: inclinômetros, extensômetros, acelerômetros, temperatura, umidade e poeira**

**Duração-alvo:** cerca de 18:40 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 9 de Drones e Sensores IoT no Monitoramento de Obras. Hoje começa a Unidade 3, dos sensores e das redes de comunicação. Na Unidade 2, o drone olhou a obra de cima. Agora o monitoramento muda de ponto de vista. Ele desce para dentro do solo, entra na estrutura e respira o ar do canteiro."

**[TELA]** Slide 3 — a obra de três subsolos e as cinco perguntas.

> "Quero que você imagine uma segunda-feira, sete da manhã, numa obra de três subsolos em área urbana. A cortina de estacas está sendo escavada colada num prédio antigo. Uma escora metálica, ao sol da tarde, parece estar ganhando carga. A laje do térreo foi concretada no sábado, e o empreiteiro já quer desformar. A equipe de pintura quer começar a impermeabilização num dia úmido. E a vizinhança liga reclamando da poeira."

> "Repara: são cinco perguntas completamente diferentes. A contenção está andando? A escora aguenta? A laje já pode ser desformada? Dá para impermeabilizar hoje? A poeira passou do aceitável? E todas elas têm a mesma resposta: medir. Mas medir o quê, com qual sensor, instalado onde? É isso que a gente vai construir hoje."

### 2. O mapa da unidade (1:30 – 2:30)

**[TELA]** Slide 4 — o que você verá nesta unidade: do sensor ao banco de dados.

> "Antes de entrar nos sensores, deixa eu te mostrar o mapa da unidade, porque ela conta uma história só: o caminho completo de um dado. Hoje, na Aula 9, os sensores e as grandezas que eles medem. Na Aula 10, as plataformas embarcadas, como o Arduino, o ESP32 e os dataloggers, que transformam o sinal em número e o guardam. Na Aula 11, as redes que levam o dado para fora do canteiro: LoRaWAN, Wi-Fi e redes celulares. E, na Aula 12, os protocolos e as plataformas que recebem e guardam as leituras: MQTT, Node-RED e o banco de séries temporais InfluxDB."

> "O Eduardo Magrani, no livro A internet das coisas, da nossa bibliografia, descreve justamente isso: objetos que coletam e trocam dados sem alguém intervir a cada leitura. No nosso caso, um tubo enterrado, uma escora, uma laje e uma caixinha no tapume. Vamos a eles."

### 3. Do fenômeno ao sensor (2:30 – 4:00)

**[TELA]** Slide 5 — do fenômeno ao sensor: escolher pelo mensurando.

> "Primeiro princípio: ninguém escolhe sensor pelo catálogo. Escolhe pelo mensurando. Mensurando é o valor específico que eu quero conhecer: não o movimento do solo, genericamente, mas o deslocamento horizontal da cortina a três metros de profundidade, em relação à leitura de antes da escavação. Quanto mais preciso for o mensurando, mais fácil fica escolher o instrumento."

> "Com o mensurando definido, entram cinco critérios. A faixa de medição: o sensor mede até onde o fenômeno pode chegar? A resolução: qual é a menor variação que ele indica? A incerteza: quanto ele pode errar? E cuidado, porque resolução não é exatidão. Um visor com três casas decimais pode errar por um milímetro inteiro. Depois, a deriva: o monitoramento dura meses, e o sensor não pode andar sozinho. E, por fim, a robustez: lama, chuva, sol, impacto de máquina, cabo pisado por caminhão."

> "E três regras valem para todos os sensores desta aula. Calibração rastreável. Leitura zero, feita antes de o fenômeno começar. E limites com ação definida antes de a obra começar. Sem essas três coisas, instrumentar vira colecionar curiosidades: gráficos bonitos que ninguém sabe o que fazer com eles."

### 4. Inclinômetros (4:00 – 5:30)

**[TELA]** Slide 6 — o inclinômetro: deslocamento horizontal em profundidade.

> "Vamos ao primeiro sensor: o inclinômetro. Ele responde à pergunta da contenção: o solo e a cortina estão andando na horizontal? Instala-se um tubo-guia, com quatro ranhuras internas, num furo vertical atrás da contenção. O detalhe crucial é o pé do tubo: engastado em solo ou rocha que não se mova, abaixo da zona de influência da escavação. É o nosso ponto fixo."

> "Para ler, baixa-se uma sonda que corre pelas ranhuras. Dentro dela há acelerômetros, que medem a inclinação em relação à vertical, do mesmo jeito que o seu celular sabe se está em pé ou deitado. A sonda para a cada meio metro. Em cada parada, mede o ângulo theta daquele trecho, e o desvio horizontal do trecho é o comprimento, meio metro, vezes o seno de theta."

> "Dois cuidados. O que interessa é sempre a diferença em relação à leitura zero, acumulada de baixo para cima, a partir do pé fixo. E faz-se uma segunda passada com a sonda girada cento e oitenta graus, que cancela o viés do próprio sensor. Existe também a versão automática, o inclinômetro in-place: sensores MEMS fixos dentro do tubo, lidos por um datalogger a cada quinze minutos. E, para a fachada do vizinho, o clinômetro de parede, que mede a rotação de um pilar."

### 5. Exemplo: do ângulo ao milímetro (5:30 – 6:30)

**[TELA]** Slide 7 — exemplo numérico: do ângulo ao milímetro.

Na tela (passo a passo do que clicar, na ordem):
1. A simulação abre com o botão "Hoje" aceso: a sonda amarela desce pelo tubo parando a cada meio metro ("parada a … m"), o perfil azul mostra "10,0 mm no topo" e os indicadores marcam "Topo: 10,0 mm" e "Fundo: 0,0 mm".
2. Na fala "em relação à leitura zero": clicar em "Leitura zero". O perfil fica reto sobre a linha tracejada do zero e o indicador vai a "Topo: 0,0 mm".
3. Na fala "Somando as variações": clicar em "Hoje". O perfil volta a abrir para cima até "10,0 mm no topo", com o aviso "abaixo de 3 m, nada mudou" e "pé fixo" sob o tubo.
4. Na fala "Se os trechos de baixo também tivessem mexido": clicar em "E se o pé tivesse andado?". O perfil fica laranja e todo deslocado: "Topo: 14,0 mm", "Fundo: 4,0 mm", o aviso "o fundo também "andou" 4,0 mm: suspeite do pé do tubo" e, sob o tubo, "pé: móvel?". Clicar em "Hoje" antes de passar de slide.

> "Vamos fazer a conta. A sonda, com meio metro entre as rodas, registrou variações do seno do ângulo, em relação à leitura zero, só nos seis trechos de cima: seis, cinco, quatro, três, um vírgula seis e zero vírgula quatro, tudo vezes dez elevado a menos três. Abaixo disso, nada mudou. Ótimo sinal: o pé está fixo."

> "Somando as variações, dá vinte vezes dez a menos três, ou seja, zero vírgula zero vinte. Vezes meio metro: zero vírgula zero dez metro. Dez milímetros no topo. Repara como o perfil é grande em cima e vai se anulando para baixo: é exatamente o formato que se espera de uma cortina que flete para dentro da escavação com o pé travado. Se os trechos de baixo também tivessem mexido, a primeira suspeita seria o pé do tubo, e não a cortina."

### 6. Extensômetros (6:30 – 7:50)

**[TELA]** Slide 8 — extensômetros: elétrico de resistência × corda vibrante.

> "Segundo sensor: o extensômetro. Ele mede deformação específica, em microdeformações. Uma microdeformação é um milionésimo: um metro de aço que encolhe um milésimo de milímetro. Existem duas famílias. O extensômetro elétrico de resistência é uma grade metálica colada na peça. Quando a peça deforma, a grade estica ou encurta, e a resistência elétrica muda, na proporção do fator do extensômetro, que é cerca de dois. Ele é rápido, ótimo para ensaios, mas sofre com umidade e com deriva quando fica meses na obra."

> "Para o longo prazo, a obra usa o extensômetro de corda vibrante. É um fio de aço tensionado entre dois blocos presos à peça. Quando a peça deforma, a tensão do fio muda, e a frequência com que ele vibra muda junto: a deformação é proporcional ao quadrado da frequência. A obra gosta dele porque é estável por anos e porque a informação está na frequência, não na tensão: o comprimento do cabo não atrapalha. Ele pode ser soldado numa escora metálica ou amarrado na armadura antes da concretagem, como nessa foto."

### 7. A escora no sol (7:50 – 9:30)

**[TELA]** Slide 9 — simulação: a escora no sol. Comece com 250 µε e ΔT = 0; depois aumente a temperatura e alterne a correção térmica.

Na tela (passo a passo do que clicar, na ordem):
1. Não mexer nos controles no primeiro parágrafo: eles abrem com "Deformação (já sem a parcela térmica)" em 250 µε, "ΔT desde a leitura zero" em 0 °C e a caixa "Correção térmica (termistor)" marcada. Na fala da lei de Hooke, apontar "σ = 200 GPa × 250 µε = 50 MPa" e "N = σ · A = 600 kN · 67% do projeto", e a barra "utilização: 67%" antes da marca "atenção 70%".
2. Na fala "Agora eu vou esquentar a escora": arrastar "ΔT desde a leitura zero" até 15 °C. Aparece o sol com "+15 °C" e a linha "Leitura bruta: 430 µε (térmica +180 µε)"; como a correção está ligada, a força continua em 600 kN.
3. Na fala "Olha o que acontece com a leitura sem correção": desmarcar "Correção térmica (termistor)". O resultado vai a "σ = 200 GPa × 430 µε = 86 MPa" e "N = σ · A = 1.032 kN · 115% do projeto", com o aviso "Sem separar a parcela térmica, o calor do dia parece efeito da escavação."; a escora fica vermelha e a barra passa de "alerta 90%" e de "100% = 900 kN".
4. Na fala "Ligo a correção": marcar de novo "Correção térmica (termistor)". A força volta a 600 kN e 67%.

> "Agora a nossa escora. O extensômetro de corda vibrante, já corrigido para a temperatura, indica duzentas e cinquenta microdeformações desde a leitura zero. O aço tem módulo de elasticidade de duzentos gigapascals. Pela lei de Hooke, tensão é módulo vezes deformação: duzentos mil megapascals vezes duzentos e cinquenta milionésimos dá cinquenta megapascals. A área da escora é de cento e vinte centímetros quadrados, ou zero vírgula zero doze metro quadrado. Força é tensão vezes área: seiscentos quilonewtons. Com carga de projeto de novecentos, a escora está a sessenta e sete por cento."

> "Agora eu vou esquentar a escora em quinze graus, da manhã fria para a tarde de sol. O aço dilata cerca de doze milionésimos por grau: quinze graus correspondem a cerca de cento e oitenta microdeformações, e a leitura bruta vai a quatrocentas e trinta. É da mesma ordem do sinal que a gente quer medir! Olha o que acontece com a leitura sem correção: a força aparente passa de mil quilonewtons, 115% do projeto. Se ninguém separa a parcela térmica, o calor do dia parece efeito da escavação, e alguém manda reforçar uma escora tranquila, ou ignora um aumento real achando que é só o calor. Por isso, o extensômetro de corda vibrante traz um termistor embutido. Ligo a correção: seiscentos quilonewtons de novo."

### 8. Acelerômetros (9:30 – 11:00)

**[TELA]** Slide 10 — acelerômetros: vibração e assinatura dinâmica.

> "Terceiro sensor: o acelerômetro. Os do tipo MEMS são microssistemas num chip, baratos e de baixo consumo, como o do seu celular. Os piezoelétricos são mais sensíveis e alcançam frequências mais altas. Na foto, um acelerômetro sem fio no pendural de uma ponte em arco."

> "Na obra, o acelerômetro tem dois usos. O primeiro é medir a vibração que a obra provoca, como a cravação de estacas: no vizinho, ela é avaliada pela velocidade de partícula de pico, em milímetros por segundo. O segundo é identificar as frequências naturais da estrutura, a assinatura dela. Num modelo de massa e mola, a frequência depende da raiz da rigidez sobre a massa. Se a rigidez cai, por fissuração ou dano numa ligação, a frequência cai junto. Cinco por cento a menos na frequência correspondem a cerca de dez por cento a menos na rigidez."

> "E aqui volta uma regra que você não pode esquecer: Nyquist. Para registrar uma vibração, é preciso amostrar a mais que o dobro da maior frequência de interesse; na prática, de cinco a dez vezes. Se a cravação tem componentes de até cinquenta hertz, eu quero algumas centenas de amostras por segundo. Abaixo disso, a vibração aparece com uma frequência falsa."

### 9. Temperatura (11:00 – 12:10)

**[TELA]** Slide 11 — temperatura: o sensor que corrige todos os outros.

> "Quarto sensor, e talvez o mais subestimado: a temperatura. Termistores NTC são baratos e sensíveis. Termorresistências, como a Pt100, são estáveis e exatas. Termopares cobrem faixas enormes, mas precisam de compensação da junta fria. E a temperatura tem três papéis na obra."

> "Primeiro, corrigir os outros sensores, como você acabou de ver na escora: extensômetros, fissurômetros e piezômetros de corda vibrante dependem dela. Segundo, controlar a cura do concreto. Pelo método da maturidade, soma-se a temperatura do concreto menos uma referência, vezes o intervalo: é o fator de Nurse-Saul, que, com uma curva calibrada para a mesma mistura, estima a resistência nas primeiras idades. Lembra da laje concretada no sábado? O sensor embutido diz se ela já chegou à resistência de desforma, sem substituir os corpos de prova, que continuam sendo o controle de aceitação. Terceiro, em concreto massa, como um bloco de fundação grande, vigiar a diferença entre o núcleo quente e a superfície fria, que pode fissurar a peça. O limite dessa diferença vem do projeto."

### 10. Umidade e ponto de orvalho (12:10 – 13:50)

**[TELA]** Slide 12 — umidade e a calculadora do ponto de orvalho. Comece com 20 °C e 80%; depois mova a temperatura da laje para 18 °C e para 21 °C.

Na tela (passo a passo do que clicar, na ordem):
1. Os controles abrem com "Temperatura do ar" em 20,0 °C, "Umidade relativa" em 80 % e "Temperatura da laje" em 18,0 °C. No gráfico, a linha laranja do ar, a linha tracejada azul "ponto de orvalho: 16,4 °C" e a faixa vermelha "risco: até orvalho + 3 °C".
2. Na fala "Vamos à calculadora": apontar o resultado "Ponto de orvalho: 16,4 °C", "Margem da laje: 1,6 °C (exigido ≥ 3 °C)" e "esperar"; o bloco da laje fica vermelho, dentro da faixa de risco, pingando gotas.
3. Na fala "Se a laje subir para vinte e um graus": arrastar "Temperatura da laje" até 21,0 °C. O resultado vai a "Margem da laje: 4,6 °C" e "pode aplicar", e o bloco da laje fica verde, acima da faixa vermelha.

> "Quinto sensor: umidade. A umidade relativa do ar é medida por sensores capacitivos: um polímero cuja propriedade elétrica muda conforme absorve vapor d'água. Quase sempre o chip mede temperatura junto, como essa plaquinha vermelha. E por que a obra se importa? Por causa do ponto de orvalho: a temperatura em que o vapor começa a condensar. Se a superfície estiver abaixo dele, aparece água, e isso compromete pintura, impermeabilização e colagem de revestimento. Muitas especificações de pintura exigem a superfície pelo menos três graus acima do ponto de orvalho."

> "Vamos à calculadora. O sensor marca vinte graus e oitenta por cento de umidade. Pela aproximação de Magnus, o ponto de orvalho dá cerca de dezesseis vírgula quatro graus. A laje está a dezoito graus: só um vírgula seis grau acima. Não atende a margem de três graus. A equipe de impermeabilização espera. Se a laje subir para vinte e um graus, aí a margem passa de quatro graus, e libera. Uma leitura de dois números evita um retrabalho inteiro."

> "E a umidade também se mede dentro dos materiais: sondas em furos na laje dizem quando o concreto está seco para receber piso, pela norma ASTM F2170, e sensores capacitivos medem a umidade do solo em taludes, onde a chuva reduz a resistência."

### 11. Poeira (13:50 – 15:10)

**[TELA]** Slide 13 — poeira: MP10, MP2,5 e calibração por colocalização.

> "Sexto sensor: poeira. Ela é monitorada como material particulado: MP10, partículas até dez micrômetros, e MP2,5, até dois e meio, que entram fundo no sistema respiratório. Os sensores IoT mais comuns são óticos: o ar passa por um feixe de luz, e um fotodetector mede a luz espalhada pelas partículas. São baratos e consomem pouco, mas têm um defeito sério: com umidade alta, as partículas absorvem água, incham, e o sensor superestima a concentração. Por isso eles precisam ser calibrados por colocalização: fica um tempo ao lado de uma estação de referência, e a gente ajusta a curva."

> "A régua nacional é a Resolução CONAMA quinhentos e seis, de 2024. Na etapa em vigor desde 2025, a média de vinte e quatro horas é de cem microgramas por metro cúbico para MP10 e cinquenta para MP2,5. Mas atenção: são padrões de qualidade do ar ambiente, não limites de emissão de uma obra. O plano de monitoramento fixa gatilhos próprios na divisa e as ações: aspersão, como nessa foto da demolição, lavar rodas, cobrir caçambas."

### 12. Os seis sensores (15:10 – 15:40)

**[TELA]** Slide 14 — tabela: os seis sensores, o que medem e onde enganam.

> "Vamos juntar tudo. Inclinômetro: deslocamento em profundidade, engana se o pé não estiver fixo. Extensômetro: deformação e força, engana com a temperatura. Acelerômetro: vibração e frequência natural, engana se a amostragem for baixa. Temperatura: corrige os outros e controla a cura. Umidade: ponto de orvalho e secagem. Poeira: MP10 e MP2,5, engana com ar úmido e sem calibração. Repara que cada sensor tem a sua armadilha. Conhecer a armadilha é metade do trabalho do engenheiro."

### 13. Laboratório: a escora no sol no simulador da Torre A (15:40 – 17:40)

**[TELA]** Slide 15 — laboratório no simulador da obra Torre A, aberto na aba Cenários (os cartões das sete situações de obra), com a compensação térmica da escora desligada.

Na tela (passo a passo do que clicar, na ordem):
1. O simulador abre reiniciado na aba "Cenários", com o relógio em "07:00" e a regra de compensação térmica desligada pelo próprio slide. Na fala "Clico em Iniciar cenário": no cartão "Escora no sol", clicar em "Iniciar cenário". A velocidade passa sozinha a "1 s = 15 min", o relógio começa a andar e aparece, no alto, a "Linha do tempo" com os passos do cenário.
2. Na fala "Abro Séries temporais": clicar na aba "Séries temporais" e, no seletor "Sensor", escolher "Extensômetro E-01 (escora)". A curva sai de cerca de 600 kN, cruza as linhas "atenção 780", "alerta 840" e "alarme 960" no fim da manhã e chega perto de 1.030 kN por volta das 13:00 do relógio (cerca de 24 s depois do início); depois começa a descer, sai do alarme perto das 15:15 e, à noite, volta a cerca de 600 kN.
3. Na fala "Na aba Alarmes": clicar na aba "Alarmes" e apontar, em "Notificações", as linhas do E-01 com os níveis "atenção", "alerta" e "alarme", o motivo "valor … kN" e a ação "Inspecionar a escora e o encunhamento; avisar o projetista.". Em "Regras", ligar a chave "Compensação térmica da escora".
4. Na fala "Repito o cenário": clicar na aba "Cenários" e, embaixo da linha do tempo, em "Repetir este cenário". Voltar a "Séries temporais" (o E-01 continua escolhido): agora a curva fica em torno de 600 kN o dia inteiro, sem cruzar a linha de atenção.
5. Na fala "A leitura bruta continua subindo": clicar na aba "Leituras", escolher "E-01" no filtro "Sensor" e apontar a coluna "Bruto" (perto de 430 µε no começo da tarde) ao lado da coluna "Engenharia" (perto de 600 kN, com a nota "compensada (−… µε)").

Atenção: o cenário dura dois dias simulados (cerca de 3 minutos reais); não é preciso esperar o fim. Ligue a compensação só no passo 3: o slide abre com ela desligada de propósito.

> "Agora vamos ver a mesma escora numa obra: a Torre A, a obra fictícia do simulador da disciplina. Lá, o extensômetro E-01 está na escora EM-03, do primeiro nível, e o sistema converte a deformação em carga: dois vírgula quatro quilonewtons por microdeformação. Com as duzentas e cinquenta de sempre, seiscentos quilonewtons. Os limites do projeto são 780 de atenção, 840 de alerta e 960 de alarme. Clico em Iniciar cenário, no cartão Escora no sol. É um dia de sol forte, e o relógio anda quinze minutos por segundo."

> "Abro Séries temporais e escolho o E-01. Olha a curva: sai de seiscentos, cruza a atenção, o alerta e, no fim da manhã, o alarme. Por volta da uma da tarde, passa de mil quilonewtons. À tarde ela desce, e à noite está de novo em seiscentos. Nenhuma escavação aconteceu: foi o sol."

> "Na aba Alarmes, o celular do engenheiro já recebeu atenção, alerta e alarme, cada um mandando inspecionar a escora. Imagine isso em todo dia de sol: em uma semana, ninguém mais acredita no painel. Ligo a Compensação térmica da escora. Repito o cenário: a mesma manhã de sol, e a carga corrigida fica perto dos seiscentos quilonewtons o dia inteiro."

> "A leitura bruta continua subindo: perto de quatrocentas e trinta microdeformações no começo da tarde, porque o aço esquentou de verdade. O que mudou é que a temperatura medida separou a parcela térmica antes de a leitura virar carga. Cento e oitenta microdeformações de sol viravam um alarme falso. É a lição desta aula: o sensor de temperatura corrige os outros sensores."

### 14. Atividade, pontos-chave e encerramento (17:40 – 18:40)

**[TELA]** Slide 16 — atividade prática.

> "Sua atividade: para a obra do gancho, monte uma tabela com os seis sensores e as colunas mensurando, local de instalação, princípio de funcionamento, principal fonte de erro, forma de correção ou calibração e a decisão que a leitura apoia: reforçar a escora, liberar a laje, adiar a pintura, ligar a aspersão."

**[TELA]** Slide 17 — pontos-chave.

> "Recapitulando: sensor se escolhe pelo mensurando, com calibração, leitura zero e limites com ação. Inclinômetro e extensômetro contam como a contenção e a estrutura se comportam; acelerômetro e temperatura, como elas vibram e curam; umidade e poeira, como está o ar e o material."

**[TELA]** Slide 18 — encerramento e gancho para a Aula 10.

> "Mas um sensor sozinho só entrega um sinal elétrico, às vezes de poucos microvolts. Quem transforma isso em número confiável, carimba a hora, guarda na memória e funciona meses a bateria no meio da lama? As plataformas embarcadas: Arduino, ESP32 e datalogger. Te espero na Aula 10!"

---

## Roteiro da Videoaula 10 — "Por que o protótipo mentiu? O que acontece entre o sensor e o número"

**Aula 10 — Plataformas embarcadas e coleta de dados em campo**

**Duração-alvo:** cerca de 18:50 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:10)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 10 de Drones e Sensores IoT no Monitoramento de Obras. Na aula passada, você conheceu os seis sensores da obra: inclinômetro, extensômetro, acelerômetro, temperatura, umidade e poeira. Hoje a gente abre a caixinha que fica entre o sensor e o dado: a plataforma embarcada."

**[TELA]** Slide 3 — o protótipo que mostrava uma linha reta.

> "Deixa eu te contar uma história que acontece toda hora. Um estagiário animado montou, num fim de semana, um protótipo: uma placa ESP32, um extensômetro colado numa escora e um rádio. Na segunda-feira, o gráfico mostrava uma linha perfeitamente reta: pela tela, a escora não carregava nada. Na terça, a bateria acabou. Na quarta, choveu e a água entrou na caixa."

> "E o mais curioso: o sensor estava certo. O que falhou foi tudo o que fica entre o sensor e o número: o condicionamento do sinal, a conversão analógico-digital, a energia e a instalação. Ao final desta aula, você vai saber explicar as três falhas e como evitá-las."

### 2. A cadeia de medição (1:10 – 2:00)

**[TELA]** Slide 4 — a cadeia de medição embarcada.

> "Pensa numa corrente com seis elos. O sensor responde à grandeza física. O condicionamento excita o sensor, amplifica, filtra e adapta o sinal. O conversor analógico-digital, o ADC, transforma tensão em número. O microcontrolador aplica a calibração, carimba a hora e decide quando ler e quando transmitir. A memória local guarda a leitura. E o rádio manda o dado embora. Por baixo de tudo, a energia, alimentando cada elo."

> "Uma corrente arrebenta no elo mais fraco, e com dado é igual. Um sensor excelente, de milhares de reais, ligado a um conversor ruidoso, produz uma leitura ruim. Por isso, quem projeta monitoramento não pode olhar só para o sensor."

### 3. Condicionamento e ponte de Wheatstone (2:00 – 3:20)

**[TELA]** Slide 5 — condicionamento de sinal e a ponte de Wheatstone.

Na tela (passo a passo do que clicar, na ordem):
1. A animação abre com o controle "Deformação ε" em 100 µε: a viga flete sob a carga, a grade do extensômetro se alonga e o resultado mostra "Vo = 3,3 × 2 × 100 × 10⁻⁶ / 4 = 165 µV".
2. Na fala "Já adianto: o resultado é da ordem de microvolts": arrastar "Deformação ε" até 1.000 µε (o máximo). A viga flete mais e a saída vai a "1.650 µV": nem 2 milivolts. Voltar para 100 µε (165 µV) antes de passar de slide.

> "Muitos sensores entregam sinais fracos demais, ou em formatos que o microcontrolador não lê direto. O caso clássico é o extensômetro elétrico. A variação de resistência dele é minúscula, então a gente o monta numa ponte de Wheatstone: quatro resistores em losango, alimentados por uma tensão de excitação. Quando a ponte está equilibrada, a saída é zero. Quando o extensômetro deforma, a ponte desequilibra e aparece uma tensão de saída."

> "Com um único extensômetro ativo, o que se chama um quarto de ponte, a saída é aproximadamente a tensão de excitação vezes o fator do extensômetro vezes a deformação, tudo dividido por quatro. Guarde essa conta, porque daqui a pouco ela vai explicar a linha reta do estagiário. Já adianto: o resultado é da ordem de microvolts. E microvolts precisam de um amplificador de instrumentação antes de chegar ao conversor."

> "O condicionamento também inclui o filtro anti-aliasing: um filtro passa-baixas antes do ADC, que impede que frequências acima da metade da taxa de amostragem apareçam como sinais falsos. É o Nyquist, que você viu na aula passada, agora protegido por hardware."

### 4. O laço de corrente 4–20 mA (3:20 – 5:20)

**[TELA]** Slide 6 — o laço de corrente 4–20 mA.

Na tela (passo a passo do que clicar, na ordem):
1. A animação abre com "Pressão no piezômetro" em 70 kPa e a corrente circulando no laço: "I = 4 + p × 16 / 200 = 9,60 mA", "V = I × 120 Ω = 1,15 V" e "p = (I − 4) × 12,5 = 70 kPa".
2. Na fala "O zero da escala não é zero miliampère, é quatro": arrastar "Pressão no piezômetro" até 0 kPa. O resultado vai a "4,00 mA" e "0,48 V": pressão nula ainda tem corrente.
3. Na fala "se a corrente cair a zero": marcar "Romper o cabo". A corrente para e o resultado mostra "I = 0 mA < 4 mA" e "cabo rompido". Desmarcar "Romper o cabo".
4. Na fala "quatro a vinte miliampères viram zero vírgula quarenta e oito a dois vírgula quatro volts": arrastar a pressão até 200 kPa ("20,00 mA", "2,40 V").
5. Na fala "Na tela, o piezômetro de zero a duzentos": voltar a pressão para 70 kPa ("9,60 mA", "1,15 V", "70 kPa").

> "Outro padrão que você vai encontrar muito em obra é o laço de corrente de quatro a vinte miliampères. Em vez de mandar o valor como tensão, o transdutor manda como corrente. A vantagem: a corrente é a mesma em todo o cabo, então cabo longo e ruído do canteiro atrapalham muito menos."

> "E tem um detalhe genial: o zero vivo. O zero da escala não é zero miliampère, é quatro. Então, se a corrente cair a zero, eu sei que não é uma leitura nula: é cabo rompido ou sensor desligado. O sistema consegue diferenciar 'não tem pressão' de 'perdi o sensor'. Para o microcontrolador ler, um resistor de carga transforma corrente em tensão. Com cento e vinte ohms, quatro a vinte miliampères viram zero vírgula quarenta e oito a dois vírgula quatro volts, dentro da faixa em que o ADC do ESP32 mede com precisão, que vai até uns dois vírgula quatro volts. Na tela, o piezômetro de zero a duzentos quilopascals com setenta quilopascals: a corrente é quatro mais setenta vezes dezesseis sobre duzentos, nove vírgula seis miliampères. E o caminho de volta, que o sistema faz a cada leitura: pressão é a corrente menos quatro, vezes doze vírgula cinco. Nove vírgula seis menos quatro dá cinco vírgula seis; vezes doze vírgula cinco, setenta quilopascals."

> "Os sensores de corda vibrante são um terceiro caso: eles precisam ser excitados e ter a frequência medida, o que exige uma interface específica. É comum em datalogger profissional, e raro em placa de protótipo."

### 5. O ADC e os bits (5:20 – 6:30)

**[TELA]** Slide 7 — simulação: quantos bits tem o seu ADC? Comece com 10 bits e depois passe para 12 e 16.

Na tela (passo a passo do que clicar, na ordem):
1. A simulação abre com o botão "10 bits · Arduino Uno" aceso: o sinal suave e a escada grossa, com os indicadores "1 LSB = 4,9 mV" e "Níveis: 1.024 em 5 V".
2. Na fala "Passo para doze bits": clicar em "12 bits · ESP32". A escada afina: "1 LSB = 806 µV" e "Níveis: 4.096 em 3,3 V".
3. Na fala "Passo para dezesseis bits": clicar em "16 bits · ADS1115". A escada quase some: "1 LSB = 63 µV" e "Níveis: 65.536 em 4,096 V".

> "Agora o conversor analógico-digital. Um ADC de n bits divide a faixa de entrada em dois elevado a n degraus. O menor degrau se chama LSB, e vale a tensão de referência dividida por dois elevado a n. Na simulação, eu tenho um sinal suave entrando. Com dez bits, como no Arduino Uno, que tem mil e vinte e quatro níveis em cinco volts, cada degrau vale uns quatro vírgula nove milivolts. Repara na escada no gráfico."

> "Passo para doze bits, como no ESP32: quatro mil e noventa e seis níveis. A escada fica bem mais fina. Mas o ADC do ESP32 tem fama conhecida: não linearidade e desvio de uma placa para outra. Então ele precisa ser calibrado, ou substituído por um ADC externo. Passo para dezesseis bits, como num ADS1115: a escada quase some. E, para pontes de extensômetros e células de carga, existe o HX711, com vinte e quatro bits e ganho interno."

### 6. Exemplo: os 165 microvolts (6:30 – 8:10)

**[TELA]** Slide 8 — exemplo numérico: por que a linha ficou reta?

Na tela (passo a passo do que clicar, na ordem):
1. A simulação abre com o botão "Sem amplificador" aceso e "Deformação máxima da escora" em 100 µε (não mexer): em cima, a deformação real sobe; embaixo, a leitura do ADC fica em zero, uma linha reta. Indicadores: "Sinal no ADC: 165 µV · 1 LSB: 806 µV" e "Degraus: 0".
2. Na fala "A solução é amplificar": clicar em "Ganho 500". A leitura de baixo passa a subir em escada, acompanhando a deformação: "Sinal no ADC: 82,5 mV" e "Degraus: 102".

> "Agora a gente resolve o mistério da linha reta. O extensômetro do estagiário tem fator dois, está num quarto de ponte excitado com três vírgula três volts e sofre cem microdeformações. Três vírgula três vezes dois vezes cem milionésimos, dividido por quatro, dá cento e sessenta e cinco microvolts de saída."

> "E quanto vale um degrau do ADC do ESP32? Três vírgula três volts divididos por quatro mil e noventa e seis: uns oitocentos e seis microvolts. Percebeu? O sinal inteiro, de cento e sessenta e cinco microvolts, cabe dentro de um único degrau. O conversor nunca vê a mudança. A escora carregava, e a tela mostrava uma linha reta. O sensor não mentiu: quem mentiu foi a cadeia."

> "A solução é amplificar. Com um amplificador de ganho quinhentos, a saída vai para oitenta e dois vírgula cinco milivolts: uns cem degraus do ADC. Aí cada degrau equivale a mais ou menos uma microdeformação. Os valores são ilustrativos, mas a lição é real: antes de confiar no gráfico, compare o tamanho do sinal com o tamanho do degrau."

> "E no piezômetro de quatro a vinte miliampères, com o resistor de cento e vinte ohms, um degrau do ADC vale uns seis vírgula sete microampères: cerca de nove milímetros de coluna d'água. Para nível d'água em escavação, resolução perfeitamente utilizável."

### 7. Arduino, ESP32 e datalogger (8:10 – 9:20)

**[TELA]** Slide 9 — Arduino, ESP32 e o datalogger profissional.

> "Vamos conhecer as plataformas. O Arduino é a porta de entrada: simples, com uma comunidade enorme, ótimo para aprender e prototipar. Mas ele não tem rádio nativo. O ESP32, da Espressif, é um microcontrolador de trinta e dois bits com Wi-Fi e Bluetooth integrados, modo de sono profundo e preço baixo. É a escolha natural para protótipos IoT, e você programa ele na mesma IDE do Arduino."

> "E existe uma terceira categoria: o datalogger profissional. Ele tem entradas para corda vibrante e para pontes, multiplexadores para dezenas de canais, funciona numa faixa larga de temperatura, vem numa caixa com grau de proteção elevado, tem relógio estável, memória para meses e certificado de calibração."

> "A regra prática é esta. Arduino e ESP32 são excelentes para protótipos, para ensino e para monitoramentos de baixa criticidade: temperatura, umidade, poeira, ocupação de áreas. Agora, se a leitura embasa uma decisão de segurança, como uma contenção ou um vizinho que recalca, usam-se instrumentos e dataloggers com calibração rastreável, instalados por equipe qualificada. Não é preconceito com a placa barata; é responsabilidade técnica."

### 8. Barramentos digitais (9:20 – 10:10)

**[TELA]** Slide 10 — sensores que já falam digital: I²C, SPI, UART, 1-Wire, SDI-12 e RS-485.

> "Muitos sensores modernos já entregam o valor pronto, em digital, e aí o problema do ADC fica dentro do próprio sensor. Eles conversam com o microcontrolador por barramentos. I2C e SPI são de curta distância, na mesma placa. UART é a serial clássica dos sensores de poeira. 1-Wire, dos termômetros como o DS18B20. SDI-12 é muito comum em sensores ambientais e dataloggers. E RS-485 com Modbus é o padrão industrial, que aguenta centenas de metros de cabo. Na obra, quando o cabo é longo e o ambiente é hostil, RS-485 e quatro a vinte miliampères são os seus melhores amigos."

### 9. Amostragem, relógio e memória (10:10 – 11:20)

**[TELA]** Slide 11 — amostragem, relógio e memória.

> "O microcontrolador decide quando ler. E a taxa segue a velocidade do fenômeno. Um piezômetro pode ser lido a cada quinze minutos; a vibração de uma cravação exige centenas de amostras por segundo. Um truque barato: ler várias vezes seguidas e tirar a média. Isso se chama sobreamostragem, e reduz o ruído aleatório pela raiz do número de leituras. Dezesseis leituras, ruído quatro vezes menor."

> "Toda leitura precisa de hora confiável, e em UTC, para não brigar com fuso e horário de verão. Para isso, usa-se um relógio de tempo real com bateria própria, sincronizado pela rede ou por GNSS. E a leitura fica guardada em memória local, cartão SD ou flash, até a confirmação de envio. Se a rede cair por um dia, nada se perde: quando ela volta, o nó manda tudo com a hora em que mediu, não a hora em que chegou."

### 10. Energia: a bateria do estagiário (11:20 – 13:00)

**[TELA]** Slide 12 — calculadora de autonomia. Comece com 0,15 mA em sono; depois mude para 10 mA.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre com os valores do exemplo: "Consumo dormindo" 0,15 mA, "Consumo acordado (ler, Wi-Fi, enviar)" 120 mA, "Tempo acordado por ciclo" 5 s, "Intervalo entre leituras" 15 min e "Capacidade útil da bateria" 7.200 mAh.
2. Na fala "a média dá uns zero vírgula oitenta e dois miliampère": apontar "Consumo médio: 0,82 mA", "Autonomia em horas: 8.825 h" e, em destaque, "Autonomia em dias: 368 dias"; nas barras, "Acordado (mA·s/ciclo)" com 600 mA·s contra "Dormindo (mA·s/ciclo)" com 134 mA·s.
3. Na fala "Agora eu mudo só uma coisa: o consumo dormindo": arrastar "Consumo dormindo" até 10,00 mA (passo de 0,05; as setas do teclado ajudam no ajuste fino). O resultado vai a "Consumo médio: 10,61 mA", "Autonomia em horas: 679 h" e "Autonomia em dias: 28 dias"; a barra "Dormindo" sobe para 8.950 mA·s e passa a do "Acordado".
4. Na fala "E o protótipo do estagiário?": arrastar "Capacidade útil da bateria" de 7.200 até 500 mAh (passo de 100), com o consumo dormindo ainda em 10,00 mA. A autonomia cai para cerca de 47 h (2 dias), a mesma conta da nota abaixo do resultado.

> "Agora a segunda falha do estagiário: a bateria. A conta é simples. O consumo médio é a carga gasta num ciclo dividida pela duração do ciclo. E a autonomia é a capacidade útil da bateria dividida pelo consumo médio."

> "Nosso nó acorda a cada quinze minutos, ou seja, a cada novecentos segundos. Fica cinco segundos acordado a cento e vinte miliampères, lendo, conectando ao Wi-Fi e enviando, e dorme oitocentos e noventa e cinco segundos. Numa placa de baixo consumo, dormindo a zero vírgula quinze miliampère, a média dá uns zero vírgula oitenta e dois miliampère. Com sete mil e duzentos miliampères-hora úteis, são umas oito mil e oitocentas horas: cerca de um ano."

> "Agora eu mudo só uma coisa: o consumo dormindo, para dez miliampères. É o que gasta uma placa de desenvolvimento comum, por causa do regulador e do conversor USB, mesmo com o chip dormindo. A média sobe para dez vírgula seis miliampères, e a bateria dura umas seiscentas e oitenta horas: vinte e oito dias. Mesmo programa, mesma bateria. Quem decide a autonomia é o sono. E o protótipo do estagiário? Placa de desenvolvimento e uma bateria pequena, de uns quinhentos miliampères-hora: quinhentos dividido por dez vírgula seis dá umas quarenta e sete horas. Dois dias. Por isso a bateria acabou na terça."

> "Num gateway ou numa câmera, entra o painel solar, com uma bateria para os dias nublados."

### 11. Instalação em campo (13:00 – 14:50)

**[TELA]** Slide 13 — instalação em campo: grau de proteção, surtos, ficha e comissionamento.

> "E a terceira falha: a chuva na caixa. Instalação é engenharia, não detalhe. A caixa precisa de grau de proteção adequado, segundo a norma NBR IEC 60529: IP65 aguenta jatos d'água; IP67, imersão temporária. Prensa-cabos de verdade, nada de furo com fita isolante, e um saquinho de dessecante dentro. Proteção contra surtos e aterramento, principalmente com cabos longos e mastros, porque raio em canteiro não é raro. Cabos em eletroduto, longe do trajeto das máquinas. Antena fora da caixa metálica. E um acesso seguro para manutenção, sem expor ninguém a risco."

> "Olha essa foto de uma estação de monitoramento em campo: a caixa do datalogger presa no mastro, o painel solar inclinado logo abaixo, o sensor com abrigo lá no alto, os cabos descendo organizados. Nada disso é enfeite: o mastro tira o equipamento do alcance da lama e das máquinas, e o abrigo protege o sensor do sol direto. No canteiro real, um cabo solto no chão dura uma semana, e uma caixa sem identificação é arrancada na primeira limpeza. Combine com a produção onde cada nó vai ficar, sinalize e inclua a instrumentação no planejamento."

> "Cada instalação gera uma ficha: identificação igual à do banco de dados, número de série, coordenadas, profundidade ou cota, foto, data e hora, fatores de calibração e leitura zero. E, antes de dizer que está pronto, o comissionamento: testar a alimentação, testar a comunicação e verificar se as primeiras leituras fazem sentido físico."

### 12. Do protótipo à produção (14:50 – 15:30)

**[TELA]** Slide 14 — do protótipo à produção.

> "Vamos voltar ao estagiário, agora com tudo o que você aprendeu. Linha reta: sinal de cento e sessenta e cinco microvolts num degrau de oitocentos; faltou amplificar. Bateria de dois dias: placa de desenvolvimento dormindo a miliampères; faltou escolher hardware de baixo consumo. Água na caixa: faltou grau de proteção e prensa-cabos. O protótipo foi útil, sim: ele ensinou onde estão as armadilhas. O passo seguinte é transformar o protótipo em produto de campo, ou reconhecer quando a aplicação pede um datalogger profissional."

### 13. Laboratório: três horas sem internet na Torre A (15:30 – 17:20)

**[TELA]** Slide 15 — laboratório no simulador da obra Torre A, aberto na aba Leituras, com o cenário "Três horas sem internet no canteiro" já em andamento.

Na tela (passo a passo do que clicar, na ordem):
1. Ao entrar no slide, o simulador reinicia e o cenário "Três horas sem internet no canteiro" começa sozinho na aba "Leituras", com o relógio em "07:00" e a velocidade em "1 s = 5 min" (não mudar). Apontar os indicadores "Leituras recebidas" (subindo), "Reenviadas (guardadas no nó)" (0), "Na fila dos nós" (0) e "Sensores mudos" (0), e as colunas "Medição (UTC)", "Bruto", "Engenharia", "Bateria" e "Rede" da tabela "Leituras recebidas".
2. Na fala "Às oito horas, a fibra do escritório de obra cai": quando o relógio passar de "08:00" (cerca de 12 s depois de entrar no slide), apontar "Leituras recebidas" parado em 86 e "Na fila dos nós" subindo (o mesmo número aparece no rótulo da aba "Leituras"): cerca de 86 às 09:00, 172 às 10:00 e 253 perto das 11:00. "Sensores mudos" vai a 11.
3. Na fala "Às onze, a fibra volta": quando o relógio passar de "11:00" (cerca de 48 s depois de entrar), apontar "Na fila dos nós" voltando a 0 e "Reenviadas (guardadas no nó)" em 258. Marcar a caixa "só com problema (nível, qualidade ou reenvio)": ficam as linhas roxas, com a etiqueta "reenviada" na coluna "Rede".
4. Na fala "Agora olha a coluna Medição": apontar, nas linhas roxas, horários de medição entre "11-16 11:00Z" e "11-16 14:00Z" e comparar com o relógio do topo, que está no horário de Brasília (3 horas a menos que o UTC).

Atenção: o cenário dura 6 horas simuladas (cerca de 72 s) e para sozinho no fim. Se o tempo se perder, sair do slide e voltar a ele reinicia o cenário do começo.

> "Agora vamos ver isso numa obra: a Torre A, do simulador da disciplina. O cenário se chama Três horas sem internet no canteiro, e já começou: são sete da manhã, e o relógio anda cinco minutos por segundo. Na aba Leituras, cada linha é uma mensagem de um dos onze sensores, com o valor bruto, o valor em engenharia, a bateria e o sinal de rádio."

> "Às oito horas, a fibra do escritório de obra cai, e o gateway no topo da grua fica sem saída para a internet. Repara: as leituras recebidas param em oitenta e seis, e o indicador Na fila dos nós começa a subir. Os sensores continuam medindo, e cada nó guarda a leitura na memória, com a hora certa. Às nove, são umas oitenta e seis leituras guardadas; perto das onze, mais de duzentas e cinquenta."

> "Às onze, a fibra volta. A fila zera de uma vez, e as reenviadas marcam duzentas e cinquenta e oito. Marco só com problema: as linhas roxas são as reenviadas. Agora olha a coluna Medição, em UTC. Essas leituras chegaram às onze, mas trazem a hora em que foram medidas: entre onze e catorze horas UTC, ou seja, entre oito e onze da manhã em Brasília. O relógio do topo está no horário local; o banco guarda em UTC, três horas à frente."

> "Nenhuma leitura se perdeu: o gráfico não ganha um buraco, ganha um atraso. Relógio certo, em UTC, e memória no nó: é isso que separa uma lacuna de uma série completa."

### 14. Atividade, pontos-chave e encerramento (17:20 – 18:50)

**[TELA]** Slide 16 — atividade prática no Wokwi.

> "Sua atividade é no simulador gratuito Wokwi. Monte um ESP32 com um sensor de temperatura e umidade DHT22 e um potenciômetro que faça o papel de um transdutor analógico. Programe a leitura a cada dez segundos, converta o valor bruto do ADC para unidade de engenharia e imprima cada leitura com a hora. Depois, escreva a ficha de instalação desse nó numa obra real: caixa, grau de proteção, alimentação, autonomia estimada, local e leitura zero."

**[TELA]** Slide 17 — pontos-chave.

> "Recapitulando: a cadeia vai do sensor ao condicionamento, ao ADC, ao microcontrolador, à memória e ao rádio, e o dado tem a qualidade do elo mais fraco. Compare sempre o sinal com o degrau do ADC. O quatro a vinte miliampères é robusto e denuncia cabo rompido. Arduino e ESP32 para protótipo e baixa criticidade; datalogger calibrado para decisão de segurança. A autonomia é decidida pelo sono, e a instalação pede proteção, ficha, leitura zero e comissionamento."

**[TELA]** Slide 18 — encerramento e gancho para a Aula 11.

> "Agora o dado existe e está guardado no nó, lá no terceiro subsolo. Mas ele precisa sair dali e atravessar a cidade até o servidor. LoRaWAN, Wi-Fi ou rede celular? E por que o sinal some justamente no subsolo? Te espero na Aula 11!"


---

## Roteiro da Videoaula 11 — "Por que o sinal some no subsolo? A rede certa para cada sensor"

**Aula 11 — Redes de comunicação: LoRaWAN, Wi-Fi e redes celulares**

**Duração-alvo:** cerca de 18:40 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 11 de Drones e Sensores IoT no Monitoramento de Obras. Você já conhece os sensores e as plataformas embarcadas: o dado existe e está guardado no nó. Hoje a pergunta é outra: como ele sobe do terceiro subsolo, atravessa a cidade e chega ao servidor? O assunto é redes de comunicação: LoRaWAN, Wi-Fi e redes celulares."

**[TELA]** Slide 3 — o primeiro dia da rede na obra.

> "Deixa eu te contar o primeiro dia de uma obra que eu vou usar como exemplo a aula inteira. A construtora instalou piezômetros no terceiro subsolo, inclinômetros atrás da cortina de estacas, um sensor de poeira na divisa com a vizinhança e câmeras no alto da grua. E aí começaram os problemas. O Wi-Fi do escritório, ótimo para os notebooks, não chegava ao subsolo. O sensor de poeira, que alguém resolveu ligar com um chip 4G comum, acabou com a bateria em uma semana. E as câmeras, mandando vídeo o dia inteiro, congestionaram a rede de todo mundo, inclusive a do escritório."

> "Repara que nenhum desses problemas é defeito de equipamento. É escolha errada de rede. Cada tecnologia foi feita para um tipo de uso, e a gente usou a ferramenta certa no lugar errado."

### 2. O triângulo de compromissos (1:30 – 2:30)

**[TELA]** Slide 4 — o triângulo alcance × taxa × consumo.

Na tela (passo a passo do que clicar, na ordem):
1. O triângulo abre trocando sozinho de tecnologia a cada 3 segundos; o indicador mostra a nota de cada uma, por exemplo "LoRaWAN · alcance alto · taxa muito baixa · economia de energia alta".
2. Na fala "Redes de longo alcance e baixo consumo transmitem pouco": clicar em "LoRaWAN" (a troca automática para) e depois em "NB-IoT" ("alcance alto · taxa muito baixa · economia de energia alta").
3. Na fala "Redes de alta taxa gastam muita energia ou alcançam pouco": clicar em "4G/5G" ("alcance médio · taxa alta · economia de energia muito baixa") e em "Wi-Fi" ("alcance muito baixo · taxa alta · economia de energia muito baixa"). Nenhum polígono alcança os três vértices.

> "Toda escolha de rede sem fio equilibra três grandezas que puxam em sentidos opostos. O alcance, até onde o sinal chega; a taxa de dados, quanta informação passa por segundo; e o consumo, quanto da bateria cada mensagem custa. E a regra desta aula: não dá para maximizar as três ao mesmo tempo."

> "Redes de longo alcance e baixo consumo transmitem pouco, mensagens de poucas dezenas de bytes. Redes de alta taxa gastam muita energia ou alcançam pouco. E a esses três critérios se somam outros, bem práticos: o custo do equipamento e da mensalidade; a cobertura naquele endereço; a latência; e uma pergunta que quase ninguém faz no começo: quem opera essa rede? A própria obra ou uma operadora? Guarde essa pergunta, porque ela volta na pausa para reflexão."

### 3. Propagação e orçamento de enlace (2:30 – 5:30)

**[TELA]** Slide 5 — propagação no canteiro: distância, frequência e obstáculos.

Na tela (passo a passo do que clicar, na ordem):
1. O mapa de 4 km abre com o botão "LoRaWAN" aceso: o círculo de alcance cobre os sete sensores e o indicador mostra "LoRaWAN · alcance ~3 km (urbano; em área aberta passa de 10 km) · conectados: 7/7".
2. Na fala "do que os 2,4 gigahertz do Wi-Fi": clicar em "Wi-Fi". O círculo encolhe para "alcance ~200 m (ao ar livre, antena externa)" e só os dois sensores do canteiro ficam ligados: "conectados: 2/7".
3. Clicar de novo em "LoRaWAN" antes da fala sobre os obstáculos.

> "Antes de comparar as tecnologias, a gente precisa entender por que o sinal some. Um sinal de rádio enfraquece com a distância, mesmo no espaço livre, sem nenhum obstáculo. Essa perda tem uma fórmula: vinte vezes o logaritmo da distância em quilômetros, mais vinte vezes o logaritmo da frequência em megahertz, mais trinta e dois vírgula quarenta e quatro. O resultado sai em decibéis."

> "Repara que a frequência está na fórmula. Quanto maior a frequência, maior a perda. Por isso as faixas abaixo de um gigahertz, como os 915 megahertz usados pela LoRaWAN no Brasil, chegam mais longe e atravessam melhor os obstáculos do que os 2,4 gigahertz do Wi-Fi. E no canteiro, obstáculo é o que não falta: cada parede ou laje de concreto pode tirar dez decibéis ou mais. E o subsolo é o pior caso: cercado de terra e concreto, ele pode bloquear o sinal quase por completo."

**[TELA]** Slide 6 — calculadora do orçamento de enlace. Comece com o nó no subsolo a 1,5 km e em SF7; depois mude para SF12.

Na tela (passo a passo do que clicar, na ordem):
1. Não mexer nos controles: "Distância ao gateway" abre em 1,5 km, "Perdas por obstáculos, lajes e cabos" em 35 dB e o botão "SF7" aceso. A cascata desce da potência do nó até a barra "recebida".
2. Na fala "a potência recebida é de menos 111,2 dBm": apontar "FSPL (915 MHz) = 95,2 dB" e "Prx = 14 + 2 + 3 − 95,2 − 35 = -111,2 dBm".
3. Na fala "Em SF7, um rádio LoRa típico ouve até menos 123 dBm": apontar "Sensibilidade SF7: -123,0 dBm → margem 11,8 dB" e "Fecha com folga.".
4. Na fala "Vou mudar para SF12": clicar em "SF12". A linha da sensibilidade desce: "Sensibilidade SF12: -137,0 dBm → margem 25,8 dB".

> "Para saber se o sinal chega, a gente faz o orçamento de enlace, o link budget. A conta é simples: potência recebida é igual à potência transmitida, mais os ganhos das antenas, menos todas as perdas. O enlace funciona se ela superar a sensibilidade do receptor, o menor sinal que ele entende, com uma folga, a margem. Queremos dez decibéis ou mais, porque o canal varia: chove, passa um caminhão, a grua gira."

> "Vamos ao nosso piezômetro no subsolo. O nó transmite com 14 dBm, tem uma antena de 2 dBi, e o gateway, a um quilômetro e meio, tem antena de 3 dBi. A perda no espaço livre, a 915 megahertz e um quilômetro e meio, dá uns 95,2 decibéis. E somo 35 decibéis de perdas por obstáculos, lajes e cabos, um valor ilustrativo, mas realista para um subsolo. Resultado: catorze, mais dois, mais três, menos 95,2, menos 35: a potência recebida é de menos 111,2 dBm."

> "Agora comparo com a sensibilidade. Em SF7, um rádio LoRa típico ouve até menos 123 dBm. A margem é de 11,8 decibéis: fecha, com folga. Vou mudar para SF12: a sensibilidade vai para menos 137 dBm, e a margem sobe para 25,8. Também fecha, com mais folga ainda. Então por que não usar sempre SF12? A resposta vem daqui a pouco. E duas boas práticas: gateway no alto, no topo da grua, com visada para os sensores; e antena fora da caixa metálica, que é uma gaiola de Faraday."

### 4. LoRaWAN (5:30 – 8:40)

**[TELA]** Slide 7 — a arquitetura LoRaWAN: nó, gateway, servidor de rede e aplicação.

> "Vamos à primeira tecnologia. Atenção aos nomes: LoRa é a modulação de rádio, uma técnica chamada espalhamento espectral por chirp, em que o sinal varre a frequência como um assobio que sobe. LoRaWAN é o protocolo de rede, mantido pela LoRa Alliance, que organiza quem fala com quem."

> "A topologia é em estrela de estrelas. Os nós sensores transmitem para qualquer gateway ao alcance, e pode ser mais de um. O gateway não abre a mensagem: só a encaminha, pela internet, a um servidor de rede. O servidor de rede elimina as cópias repetidas que chegaram por gateways diferentes, controla a taxa de dados de cada nó e entrega a mensagem ao servidor de aplicação, onde ela vai ser usada. E tudo isso vai cifrado, com AES de 128 bits: o gateway encaminha o pacote sem conseguir ler o conteúdo."

> "Na tela, um nó numa caixinha preta, com uma sonda de umidade do solo, e um gateway sobre um computador de placa única: a infraestrutura de uma rede LoRaWAN privada cabe numa mesa."

**[TELA]** Slide 8 — fator de espalhamento × tempo no ar × energia.

Na tela (passo a passo do que clicar, na ordem):
1. As barras abrem com o botão "SF7" aceso e os indicadores "Tempo no ar: 62 ms", "Carga a 120 mA: 7,4 mA·s (1,0 × SF7)" e "Sensibilidade: -123,0 dBm"; embaixo, a faixa do canal com pacotes curtos.
2. Na fala "Em SF12, cerca de um segundo e quarenta e oito": clicar em "SF12". Os indicadores vão a "Tempo no ar: 1,48 s", "Carga a 120 mA: 177,9 mA·s (24,0 × SF7)" e "Sensibilidade: -137,0 dBm", e a faixa do canal fica quase toda ocupada.
3. Na fala "o menor SF que garanta o enlace": clicar de novo em "SF7".

> "Agora a resposta da pergunta que ficou pendente. O parâmetro-chave da LoRa é o fator de espalhamento, o spreading factor, que vai de SF7 a SF12. Cada passo para cima ganha uns dois decibéis e meio de sensibilidade, ou seja, mais alcance. Mas praticamente dobra o tempo que a mensagem fica no ar. E tempo no ar é energia."

> "Uma mensagem com 12 bytes de dados, 25 bytes no quadro LoRaWAN, a 125 quilohertz, fica no ar cerca de 62 milissegundos em SF7. Em SF12, cerca de um segundo e quarenta e oito. Transmitindo a 120 miliampères, a mensagem em SF7 custa uns 7,4 miliampères-segundo; em SF12, uns 178. É cerca de vinte e quatro vezes mais energia por mensagem. E tem mais: enquanto um nó fala em SF12, ele ocupa o canal vinte e quatro vezes mais tempo, e os vizinhos esperam."

> "Por isso existe a taxa de dados adaptativa, o ADR: o servidor de rede observa a qualidade com que cada nó chega e manda o nó usar o menor SF que garanta o enlace. No nosso subsolo, se o SF7 já dá quase 12 decibéis de margem, é ele. E alguns planos de frequência limitam o tempo no ar por transmissão: confira o plano e a regulamentação vigente."

> "Mais três detalhes. As mensagens têm dezenas de bytes: basta para um piezômetro, não para uma foto. Os dispositivos classe A só escutam a rede logo depois de transmitir. E no Brasil a LoRaWAN opera de 915 a 928 megahertz, nos planos AU915 ou LA915, sem licença, mas com equipamento homologado pela Anatel."

### 5. Wi-Fi (8:40 – 10:10)

**[TELA]** Slide 9 — Wi-Fi: muita taxa, pouco alcance, muita energia.

> "Segunda tecnologia: o Wi-Fi, a família IEEE 802.11, que você conhece de casa. Ele opera em 2,4 e 5 gigahertz e, nas versões mais recentes, em 6 gigahertz. Oferece dezenas a centenas de megabits por segundo. Perfeito para câmeras, para o escritório de obra, para os tablets da fiscalização e para equipamentos que têm tomada por perto."

> "O alcance é de dezenas de metros em ambiente interno e algumas centenas ao ar livre, com antena externa, como esse ponto de acesso no mastro. Para ligar dois prédios distantes, usam-se enlaces ponto a ponto, com antenas direcionais."

> "O preço é o consumo. Conectar-se ao ponto de acesso e manter a associação gasta muita energia, e isso não combina com um sensor a bateria lido a cada poucos minutos. Lembra da Aula 10: uns 120 miliampères durante segundos a cada envio. E o ESP32 clássico só fala em 2,4 gigahertz. Em canteiros grandes, uma boa solução é a rede em malha, o mesh, com vários pontos de acesso que se repetem e acompanham a obra conforme ela cresce. E segurança desde o começo: WPA2 ou WPA3 e a rede dos sensores separada da rede administrativa."

### 6. Redes celulares (10:10 – 11:50)

**[TELA]** Slide 10 — redes celulares: 4G, 5G, LTE-M e NB-IoT.

> "Terceira família: as redes celulares. A vantagem: a infraestrutura é da operadora; você põe um chip no equipamento e pronto. A desvantagem: mensalidade por chip e dependência da cobertura naquele endereço."

> "O 4G e o 5G dão alta taxa e servem muito bem para gateways, câmeras e para mandar as imagens do drone. Mas, para sensor a bateria, eles gastam demais: foi o erro do nosso sensor de poeira. Para isso, a 3GPP, que padroniza as redes celulares, criou duas versões de baixa potência. O LTE-M, ou Cat-M1, com taxa de centenas de quilobits até um megabit por segundo e suporte a mobilidade: ótimo para um rastreador num caminhão ou numa máquina que se desloca. E o NB-IoT, com taxa menor, mas com cobertura profunda: ele atravessa melhor paredes e subsolos, e o consumo é muito baixo."

> "Os dois têm modos de economia de energia, o PSM e o eDRX, em que o módulo dorme por longos períodos sem perder o registro na rede. Duas recomendações antes de escolher: confirme com a operadora, por escrito, a cobertura de LTE-M ou NB-IoT no endereço da obra, de preferência com um teste no subsolo. E lembre que as redes 2G e 3G estão em desligamento gradual: não compre equipamento que dependa delas."

### 7. Comparando e se protegendo das falhas (11:50 – 13:40)

**[TELA]** Slide 11 — tabela comparativa das redes.

> "Na tela, a tabela que resume tudo. Veja o padrão: LoRaWAN e NB-IoT, longo alcance, pouca taxa e anos de bateria; LTE-M, um pouco mais de taxa e mobilidade; 4G, 5G e Wi-Fi, alta taxa e alto consumo, e o Wi-Fi com curto alcance."

> "A regra prática: leitura lenta a bateria, LoRaWAN ou NB-IoT. Muito dado com energia disponível, Wi-Fi ou 4G e 5G. Voltando ao primeiro dia da obra: piezômetros e inclinômetros, LoRaWAN ou NB-IoT. Sensor de poeira, LoRaWAN, ou Wi-Fi se ele estiver junto à tomada do tapume. Câmeras da grua, 4G dedicado ou um enlace Wi-Fi ponto a ponto separado do escritório."

**[TELA]** Slide 12 — armazenar e reenviar, e rota alternativa.

Na tela (passo a passo do que clicar, na ordem):
1. A linha do tempo abre com o botão "Sem armazenar e reenviar" aceso e o relógio de 24 h correndo (cerca de 11 s): das 6h às 18h a rede cai e as leituras somem. No fim, "Agora: 24h · no servidor: 48 leituras" e "Perdidas: 48".
2. Na fala "o nó deve fazer armazenar e reenviar": clicar em "Com armazenar e reenviar". O relógio recomeça; das 6h às 18h o indicador "Guardadas no nó" sobe até 48 e, às 18h, todas chegam ao servidor com a hora da medição: no fim, "no servidor: 96 leituras".

> "E agora uma verdade incômoda: toda rede falha. O gateway reinicia, a operadora tem uma pane, alguém desliga o disjuntor do contêiner. Por isso, qualquer que seja a rede, o nó deve fazer armazenar e reenviar, o store-and-forward. Ele guarda cada leitura, com o carimbo de tempo da medição, não da chegada, e reenvia tudo quando a conexão volta. Assim, uma queda de doze horas vira um atraso, e não um buraco no gráfico."

> "Para sensores críticos, vale ir além: ter uma rota alternativa. Dois gateways cobrindo a mesma área, ou um gateway com conexão 4G de reserva para o caso de a internet fixa cair. E um alerta que muita obra esquece: alguém precisa ser avisado quando um sensor para de transmitir. Silêncio não é sinal de que está tudo bem."

### 8. Pausa para reflexão (13:40 – 15:00)

**[TELA]** Slide 13 — pausa para reflexão: rede própria ou da operadora?

> "Agora, pare o vídeo se precisar, e pense comigo. A construtora pode montar a própria rede LoRaWAN, com gateway no topo da grua, ou usar chips NB-IoT de uma operadora."

> "Na primeira opção, a obra controla tudo, não paga mensalidade por sensor e não depende da cobertura de terceiros. Mas alguém precisa manter o gateway funcionando às duas da manhã. E repara num detalhe: quando a grua for desmontada, a rede vai junto com ela. Na segunda opção, a operadora cuida da infraestrutura, mas a obra depende da cobertura no subsolo, paga por chip e fica sem dados se a operadora tiver uma falha."

> "Então: quem deve operar a rede que transporta dados de segurança? Pense em três perguntas. O que acontece com os sensores que precisam continuar lendo depois da entrega da obra, por exemplo, o recalque do vizinho nos meses seguintes? Existe rota alternativa se a rede principal cair? E quem é avisado quando um sensor para de transmitir? Não existe resposta única. Mas existe resposta errada: não ter pensado nisso antes de comprar os equipamentos."

### 9. Laboratório: o sinal sai do 3º subsolo da Torre A? (15:00 – 17:00)

**[TELA]** Slide 14 — laboratório no simulador da obra Torre A, aberto na aba Rede LoRaWAN, com o ADR ligado e 35 dB de perdas no 3º subsolo.

Na tela (passo a passo do que clicar, na ordem):
1. O simulador abre reiniciado na aba "Rede LoRaWAN", parado em "07:00". Apontar os indicadores "Gateway GW-01" ("ligado"), "Saída para a internet" ("fibra"), "Pior margem" ("PZ-03 · 40,5 dB") e "Leituras na fila" (0) e, na tabela "Enlace de cada sensor", a linha do PZ-03: "55 m", "35 dB", "-82,5 dBm", "SF7", margem "40,5 dB", "62 ms" e "12,5 anos". Os "Controles" ficam abaixo da tabela: rolar o simulador até eles.
2. Na fala "Clico em Iniciar": clicar em "Iniciar", no topo (velocidade "1 s = 5 min"), para o relógio andar e as leituras saírem.
3. Na fala "arrasto as perdas do terceiro subsolo para 70": arrastar "Perdas extras no 3º subsolo (PZ-03)" de 35 até 70 dB. A linha do PZ-03 passa a "-117,5 dBm", "SF9", margem "11,5 dB", "206 ms" e "6,9 anos"; a nota abaixo dos controles diz "PZ-03 em SF9 com margem de 11,5 dB".
4. Na fala "Agora noventa": arrastar até 90 dB. O PZ-03 fica em "-137,5 dBm", "SF12" e margem "-0,5 dB" (linha vermelha), a nota passa a "PZ-03 fora do ar: recebe -137,5 dBm, abaixo da sensibilidade até do SF12" e, com o relógio andando, a coluna "Fila no nó" do PZ-03 e o indicador "Leituras na fila" sobem uma leitura a cada 3 s, mais ou menos.
5. Na fala "Volto para 35": arrastar de volta a 35 dB. A fila se descarrega e volta a 0; o PZ-03 volta a SF7 com 40,5 dB.
6. Na fala "Agora desligo o ADR": desmarcar "ADR (taxa adaptativa)". Todos os sensores vão para "SF12" e "1.483 ms"; o PZ-03 cai para "1,4 anos" de bateria (PO-01 e ACC-01, que falam a cada 5 min, para "0,5 anos"), e a nota avisa "Sem ADR, todos transmitem em SF12".
7. Na fala "Por fim, ligo o Gateway com 4G de reserva": marcar "Gateway com 4G de reserva". A tabela não muda e "Saída para a internet" continua "fibra". Clicar em "Pausar" antes de passar de slide.

Atenção: sem clicar em "Iniciar", a fila não cresce no passo 4, porque o relógio está parado. Ao sair e voltar ao slide, o simulador reinicia com ADR ligado e 35 dB.

> "Agora o orçamento de enlace na Torre A, a obra do simulador da disciplina. Na aba Rede LoRaWAN, cada linha é um sensor, com a distância ao gateway GW-01, no topo da grua, as perdas, a potência recebida, o SF, a margem, o tempo no ar e a bateria estimada. O caso difícil é o PZ-03, o piezômetro do terceiro subsolo. Ele está a só cinquenta e cinco metros da grua, mas com trinta e cinco decibéis de lajes e paredes no caminho. Mesmo assim, recebe menos 82,5 dBm e fecha em SF7 com 40,5 decibéis de margem. Distância curta perdoa muito."

> "Clico em Iniciar e arrasto as perdas do terceiro subsolo para 70 decibéis. O ADR sobe o PZ-03 para SF9, com 11,5 de margem, e a bateria estimada cai de 12,5 para 6,9 anos. Agora noventa: menos 137,5 dBm, abaixo da sensibilidade até do SF12. O enlace não fecha, e a fila no nó começa a crescer: o nó guarda as leituras e espera. Volto para 35, e a fila é entregue na hora."

> "Agora desligo o ADR. Todos os sensores vão para SF12: um segundo e meio no ar por mensagem, e a bateria do PZ-03 cai de 12,5 para 1,4 ano. Margem sobrando, energia jogada fora. Por fim, ligo o Gateway com 4G de reserva. Nada muda na tabela, e é isso mesmo: a reserva só trabalha quando a fibra cai, como no cenário da Aula 10. Margem de dez decibéis, o menor SF que fecha o enlace e uma rota alternativa: é assim que se projeta a rede da obra."

### 10. Atividade, pontos-chave e encerramento (17:00 – 18:40)

**[TELA]** Slide 15 — atividade prática.

> "Sua atividade: pegue a obra do nosso exemplo, com piezômetros no terceiro subsolo, inclinômetros atrás da cortina, sensor de poeira na divisa e câmeras na grua. Escolha a rede de cada grupo de sensores e justifique por alcance, taxa, consumo, custo e cobertura. Desenhe a planta com a posição do gateway. Faça o orçamento de enlace do sensor mais desfavorável. E defina o que acontece com os dados se a conexão cair por doze horas."

**[TELA]** Slide 16 — pontos-chave.

> "Vamos amarrar. Primeiro: a rede se escolhe pelo compromisso entre alcance, taxa e consumo, somado a custo, cobertura, latência e quem opera. Segundo: o orçamento de enlace compara a potência recebida com a sensibilidade; queira dez decibéis de margem ou mais. Terceiro: na LoRaWAN, SF maior dá alcance ao custo de tempo no ar e energia; NB-IoT e LTE-M são os celulares de baixa potência, com cobertura a confirmar. Quarto: toda rede falha, então o nó armazena e reenvia, e sensor crítico merece rota alternativa."

**[TELA]** Slide 17 — encerramento e gancho para a Aula 12.

> "Hoje o dado saiu do subsolo e atravessou a cidade. Mas, quando ele chega do outro lado, quem recebe? Como mensagens de sessenta sensores, de fornecedores diferentes, chegam em ordem, sem se perder, e onde elas são guardadas para virar gráfico e alerta? Na próxima aula, você vai conhecer um carteiro chamado MQTT, o Node-RED e os bancos de séries temporais. Te espero na Aula 12!"

---

## Roteiro da Videoaula 12 — "Um carteiro chamado MQTT: como milhares de leituras chegam ao banco de dados sem se perder"

**Aula 12 — Protocolos e plataformas IoT: MQTT e armazenamento de séries temporais**

**Duração-alvo:** cerca de 18:50 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 12 de Drones e Sensores IoT no Monitoramento de Obras, a última da Unidade 3. Até aqui, o dado nasceu no sensor, na Aula 9, virou número na plataforma embarcada, na Aula 10, e atravessou a rede, na Aula 11. Hoje ele chega ao destino. O assunto é protocolos e plataformas IoT: o MQTT, o Node-RED e o armazenamento em séries temporais, com o InfluxDB."

**[TELA]** Slide 3 — três fornecedores, três portais, uma planilha.

> "Imagina uma obra com sessenta sensores de três fornecedores diferentes. Cada fornecedor tem o seu portal, a sua senha, o seu formato de arquivo e, pior, o seu relógio: um grava no horário de Brasília, outro em UTC, outro no horário do datalogger, que ninguém acertou. Toda segunda-feira, o engenheiro baixa três planilhas, acerta os fusos à mão e cola tudo numa quarta planilha para ver se o recalque do vizinho acompanha a subida da água no solo. E quando um sensor para de transmitir, ninguém percebe por dias."

> "O problema aqui não é sensor nem rede. Os dados estão chegando. O que falta é uma linguagem comum para as mensagens e um lugar comum para guardá-las. É isso que a gente vai construir hoje."

### 2. A pilha IoT (1:30 – 2:40)

**[TELA]** Slide 4 — a pilha IoT: percepção, rede, plataforma e aplicação.

> "Gubbi e colegas, num artigo de 2013 que está na bibliografia da disciplina, descrevem a Internet das Coisas como a integração de sensores, redes, armazenamento e análise em nuvem, e visualização. Na nossa obra, isso vira quatro camadas. A percepção: sensores e nós, a Aula 10. A rede: LoRaWAN, Wi-Fi, celular, a Aula 11. A plataforma: quem recebe as mensagens, integra e guarda, que é a aula de hoje. E a aplicação: painéis, alertas e integração com o BIM, que é a Unidade 4."

> "Entre a rede e a plataforma, as mensagens precisam de um protocolo de aplicação, um combinado sobre como conversar. O HTTP, o protocolo da web, funciona: o sensor faz uma requisição e o servidor responde. Mas ele é pesado para um dispositivo pequeno, cheio de cabeçalhos. Existe o CoAP, uma versão enxuta sobre UDP. E existe o MQTT, que virou o padrão de fato da IoT. É nele que a gente vai mergulhar."

### 3. MQTT: publicar e assinar (2:40 – 4:30)

**[TELA]** Slide 5 — publicar e assinar por meio de um broker.

> "O MQTT é um protocolo leve de mensagens, padronizado pela OASIS nas versões 3.1.1 e 5.0, e funciona sobre TCP/IP. A grande sacada é que os dispositivos não conversam diretamente entre si. Todos se conectam a um servidor central, o broker. Pense no broker como uma agência dos correios com caixas postais etiquetadas."

> "Um cliente publica uma mensagem num tópico, que é a etiqueta da caixa postal. O broker entrega essa mensagem a todos os clientes que assinaram aquele tópico. Na tela: à esquerda, o publicador; no centro, o broker; à direita, dois assinantes recebendo a mesma mensagem. Os brokers mais conhecidos são o Mosquitto, o EMQX e o HiveMQ."

> "Repara no que isso resolve. O publicador e o assinante não se conhecem. O sensor não sabe quem vai usar a leitura, e o painel não precisa saber de onde ela veio. Se amanhã eu quiser acrescentar um novo consumidor, um painel novo, um registro de auditoria, um sistema de alertas, eu não mexo em nenhum sensor: só faço o novo cliente assinar o tópico. É isso que acaba com as três planilhas da segunda-feira."

> "E de onde vêm as mensagens? Se o nó tem Wi-Fi ou 4G, como o ESP32 da Aula 10, ele publica diretamente no broker. Se a rede é LoRaWAN, quem publica normalmente é o servidor de rede, por meio da sua integração MQTT: o nó manda o pacote de rádio, o servidor decodifica e publica."

### 4. Tópicos e curingas (4:30 – 5:40)

**[TELA]** Slide 6 — simulação dos tópicos e curingas. Use primeiro a assinatura com mais nos níveis de setor e sensor; depois a assinatura com cerquilha e, por fim, a cerquilha no meio.

Na tela (passo a passo do que clicar, na ordem):
1. A simulação abre com o botão "+ setor, + sensor" aceso e o campo "Filtro do assinante (digite ou escolha):" com obra/torre-a/+/piezometro/+/nivel. As mensagens saem dos oito tópicos da lista, passam pelo broker e só as que casam chegam ao assinante.
2. Na fala "Olha a simulação: chegam os níveis de todos os piezômetros": apontar o indicador "Casam com o filtro: 3 de 8 tópicos" (PZ-01 e PZ-03 da escavação e PZ-07 da divisa); a bateria do PZ-03 e a torre B ficam de fora.
3. Na fala "Agora vou assinar obra, barra, torre-a, barra, cerquilha": clicar em "# torre A". O indicador vai a "Casam com o filtro: 7 de 8 tópicos": só o tópico da torre B não chega.
4. Na fala "a cerquilha só pode ficar no final do tópico": clicar em "# no meio" (obra/#/nivel). A borda do campo fica vermelha e o indicador mostra "Filtro inválido: nada chega".

> "Os tópicos são hierárquicos, com níveis separados por barra, como um endereço. No nosso exemplo: obra, barra, torre-a, barra, escavação, barra, piezômetro, barra, PZ-03, barra, nível. Um bom padrão segue a lógica obra, setor, tipo, sensor, grandeza. E evite espaços e acentos: escreva escavação sem cedilha e sem til."

> "Agora vem a parte boa: os curingas, que o assinante usa. O sinal de mais substitui exatamente um nível. Vou assinar obra, torre-a, mais, piezômetro, mais, nível. Olha a simulação: chegam os níveis de todos os piezômetros, de todos os setores. O primeiro mais pegou o setor; o segundo, o sensor. Agora vou assinar obra, barra, torre-a, barra, cerquilha. A cerquilha substitui todos os níveis abaixo, e chega tudo da torre A: piezômetros, inclinômetros, poeira, status. Um detalhe que cai em prova: a cerquilha só pode ficar no final do tópico. Não dá para colocá-la no meio."

### 5. QoS, mensagem retida e último desejo (5:40 – 7:50)

**[TELA]** Slide 7 — QoS, mensagem retida e último desejo.

> "Agora, a garantia de entrega. O MQTT tem três níveis de qualidade de serviço, o QoS, e eles valem em cada trecho: do publicador ao broker e do broker ao assinante. QoS zero: no máximo uma vez. A mensagem vai e ninguém confirma; se se perder, perdeu. QoS um: pelo menos uma vez. Há confirmação, e se ela não vier a mensagem é reenviada, então pode chegar duplicada. QoS dois: exatamente uma vez, com uma troca de quatro mensagens. É o mais seguro e o mais lento."

> "Para leitura de sensor, o equilíbrio costuma ser QoS um, com cada leitura identificada pelo carimbo de tempo da medição. Uma duplicata tem o mesmo instante e o mesmo valor: não cria dado falso."

> "Mais três recursos muito úteis no canteiro. A mensagem retida, o retain: o broker guarda a última mensagem do tópico e entrega a quem assinar depois. Um painel aberto às oito da manhã já recebe o último estado de cada sensor. O último desejo, o Last Will: quando o nó se conecta, ele deixa com o broker uma mensagem de testamento, por exemplo offline no tópico de status. Se o nó cair sem se despedir, o broker publica essa mensagem sozinho. Lembra do sensor que parou e ninguém percebeu por dias? Resolvido."

**[TELA]** Slide 8 — segurança do broker.

> "E, já que é broker de obra, segurança desde o primeiro dia. O broker deve exigir autenticação, usuário e senha ou certificado para cada dispositivo. Deve usar TLS, a criptografia, na porta 8883, em vez da 1883, que trafega tudo em texto aberto. E cada dispositivo só pode publicar nos seus próprios tópicos. Um sensor de poeira não tem por que publicar no tópico do piezômetro. Esse tema volta com força na Aula 16, de cibersegurança."

### 6. Node-RED (7:50 – 9:20)

**[TELA]** Slide 9 — um fluxo no Node-RED.

> "As mensagens estão chegando ao broker. Quem as pega, confere, converte e guarda? Uma opção muito usada é o Node-RED, uma ferramenta de código aberto, mantida pela OpenJS Foundation, em que você programa fluxos de dados ligando blocos num editor no navegador. Na tela, um exemplo simples do próprio projeto: entradas à esquerda, um filtro no meio, um atraso, e duas saídas, um bipe e um e-mail."

> "No nosso monitoramento, o fluxo típico tem quatro blocos. Um nó mqtt in, que assina os tópicos dos sensores. Um nó function, escrito em JavaScript, que valida a mensagem, aplica a calibração e marca a qualidade da leitura: por exemplo, pega os 9,6 miliampères do piezômetro e transforma em 70 quilopascals, como fizemos na Aula 10. Um nó switch, que separa as leituras das mensagens de status. E um nó de saída que grava tudo no banco de séries temporais. O mesmo fluxo pode avisar a equipe quando um sensor deixa de publicar."

> "E onde o Node-RED roda? Num computador da obra, num Raspberry Pi junto ao gateway, que é o processamento na borda, ou num servidor em nuvem. Na borda, ele continua funcionando mesmo se a internet cair."

### 7. A anatomia de uma leitura (9:20 – 10:30)

**[TELA]** Slide 10 — a anatomia de uma leitura.

> "Antes de guardar, vamos olhar com lupa o que é uma leitura. Uma série temporal é uma sequência de valores ordenados no tempo. E cada ponto de uma série de sensor precisa de sete coisas. O carimbo de tempo, em UTC, o da medição, não o da chegada. A identificação do sensor. O valor bruto: hertz, miliampères, contagens do ADC. O valor de engenharia: milímetros, quilopascals, obtido com a leitura zero e os fatores de calibração, que devem ter versão. A unidade. A marca de qualidade. E a saúde do nó: tensão da bateria, intensidade do sinal."

> "E a regra de ouro: nunca sobrescreva o dado bruto. Se a calibração mudar, se você descobrir que um fator estava errado, a correção é uma nova camada, rastreável. Todo dado de campo tem defeitos: picos espúrios, lacunas, deriva, ciclos térmicos, relógio desacertado. Só com o bruto preservado dá para tratar esses defeitos depois, e defender o seu número num laudo."

### 8. InfluxDB e o line protocol (10:30 – 12:10)

**[TELA]** Slide 11 — o modelo de dados do InfluxDB.

> "Onde guardar? Em bancos de séries temporais, otimizados para gravar dados na ordem em que chegam, comprimir valores parecidos e consultar por intervalo de tempo: me dá o nível do PZ-03 da última semana. O mais conhecido é o InfluxDB. Nele, cada ponto tem quatro partes. A measurement, que é o tipo de dado, por exemplo piezômetro. As tags, pares chave e valor de texto que descrevem e indexam a série: obra, setor, sensor. Os fields, que são os valores medidos: nível em metros, corrente bruta, tensão da bateria. E o timestamp."

> "A frase para guardar: tag é o que identifica a série; field é o que você mede."

**[TELA]** Slide 12 — o line protocol.

> "Os pontos são escritos num formato de texto chamado line protocol. Na tela, a nossa leitura. Primeiro, a measurement: piezômetro. Vírgula, as tags: obra igual a torre-a, sensor igual a PZ-03. Um espaço. Os fields: nível igual a 7.14, corrente bruta igual a 9.6, bateria igual a 3.61. Outro espaço. E o instante, um número enorme: nanossegundos desde primeiro de janeiro de 1970, em UTC. Aqui, dezenove de novembro de 2026, às cinco da manhã em UTC."

> "Dois detalhes. O line protocol usa ponto como separador decimal, não vírgula: cuidado ao converter da planilha brasileira. E os dados ficam num bucket, ou banco de dados, que tem um período de retenção. As consultas usam InfluxQL ou Flux nas versões 1 e 2, e SQL ou InfluxQL na versão 3."

### 9. Volume, cardinalidade e retenção (12:10 – 14:20)

**[TELA]** Slide 13 — calculadora de volume e cardinalidade. Comece com 60 sensores a cada 15 min; depois ative o acelerômetro contínuo; por fim, ative a tag errada.

Na tela (passo a passo do que clicar, na ordem):
1. Não mexer nos controles: "Sensores" abre em 60 e "Intervalo entre leituras" em 15 min. Na fala "Sessenta sensores, lidos a cada quinze minutos": apontar "Pontos por dia: 5.760" e, embaixo das barras, "≈ 2,1 mi por ano · ≈ 576 kB por dia"; a barra "acelerômetro" está "desligado" e o painel da direita mostra "Séries no índice: 20" ("tags obra e sensor: 20 séries, para sempre").
2. Na fala "Agora vou ligar um único acelerômetro": clicar em "Acelerômetro contínuo 500 Hz". O indicador vai a "Pontos por dia: 129,6 mi", a barra laranja sobe na escala logarítmica e aparece "um só sensor: 23 mil × todos os outros".
3. Na fala "imagine que alguém pôs o identificador de cada leitura como tag": clicar em "Tag errada (ID da leitura)". O contador "Séries no índice" dispara (um dia simulado a cada 2 s), a grade de séries enche e a legenda passa a "+1.920 por dia · ≈ 700 mil por ano".
4. Clicar de novo nos dois botões para desligá-los antes de passar de slide.

> "Vamos fazer contas. Sessenta sensores, lidos a cada quinze minutos, são 96 leituras por dia cada um: 5.760 pontos por dia, uns 2,1 milhões por ano. Parece muito? A uns 100 bytes por linha, antes da compressão, são uns 576 quilobytes por dia. Isso cabe em qualquer lugar."

> "Agora vou ligar um único acelerômetro triaxial, gravando continuamente a 500 hertz. Três eixos, vezes 500, vezes 86.400 segundos do dia: cerca de 130 milhões de valores por dia. Um único sensor de vibração contínuo produz mais de vinte mil vezes os valores de todos os outros juntos. É por isso que vibração se grava por evento."

> "E agora o erro clássico. Com as tags obra e sensor, vinte piezômetros formam vinte séries, para sempre. Mas imagine que alguém pôs o identificador de cada leitura como tag. Cada ponto vira uma série nova: vinte vezes 96, 1.920 séries novas por dia, umas 700 mil por ano. Olha o contador disparando. Cada combinação de measurement e tags é uma série, e esse número é a cardinalidade. O índice cresce sem parar e as consultas ficam lentas. Identificador único e valor medido vão para os fields, nunca para as tags."

**[TELA]** Slide 14 — retenção e agregação.

> "Então como os sistemas maduros lidam com o volume? Guardam o dado bruto completo pelo prazo que o contrato e a responsabilidade técnica exigem. Mas os painéis mostram agregados, médias horárias, máximos diários, gerados por tarefas periódicas de subamostragem, o downsampling. Ninguém precisa desenhar dois milhões de pontos num gráfico de celular. E os registros de vibração são gravados por evento: o sensor guarda só as janelas em que um gatilho foi ultrapassado, mais um resumo periódico, como o pico de cada intervalo."

### 10. Laboratório: assine o tópico certo na Torre A (14:20 – 16:20)

**[TELA]** Slide 15 — laboratório no simulador da obra Torre A, aberto na aba MQTT, com o relógio já andando.

Na tela (passo a passo do que clicar, na ordem):
1. O simulador abre reiniciado na aba "MQTT" e já rodando (o botão do topo mostra "Pausar"; velocidade "1 s = 5 min"). No campo de assinatura está obra/torre-a/#, com a mensagem "Assinatura válida. O broker entrega as mensagens dos tópicos que casam com ela."; a tabela "Mensagens entregues a esta assinatura" mostra "Hora", "Tópico", "QoS" (1) e "Payload" em JSON (por exemplo {"ts":"2026-11-16T10:28:08Z","bruto":8.6847,"valor":5.856,"un":"m","q":"ok","bat":3.67}).
2. Na fala "Clico em todos os piezômetros": clicar no botão "todos os piezômetros". O campo passa a obra/torre-a/+/piezometro/+/nivel e só chegam mensagens de PZ-01, PZ-02 e PZ-03 (o contador ao lado do título conta "… mensagem(ns)").
3. Na fala "Clico em cerquilha barra nível": clicar em "#/nivel (inválido)". Aparece, em vermelho, "Assinatura inválida: o # só pode ser o último nível (e o + ocupa um nível inteiro). O broker recusa." e a tabela fica vazia ("0 mensagem(ns)").
4. Na fala "Agora digito": apagar o campo e digitar obra/torre-a/+/+/I-2/#. A assinatura volta a ser válida e só chegam as mensagens de obra/torre-a/cortina/inclinometro/I-2/desloc, com "valor" perto de 8,6 mm. Na tabela "Tópicos no broker", apontar o I-2 e a linha obra/torre-a/status/GW-01 com "online".
5. Na fala "Agora abro Séries temporais": clicar na aba "Séries temporais" e, no seletor "Sensor", escolher "Piezômetro PZ-03". Apontar o quadro "Line protocol" (leitura,obra=torre-a,setor=escavacao,tipo=piezometro,sensor=PZ-03 valor=…,bruto=…,bat=…,q="ok" e o carimbo em nanossegundos) e os comentários de tags, fields e timestamp; depois, em "Volume de dados", os indicadores "Séries (sensores)" 11, "Pontos por dia" 2.064 e "Pontos por ano" 753.360.

> "Agora a mão na massa na Torre A, a obra do simulador da disciplina, aberta na aba MQTT. Cada leitura dos onze sensores vira uma mensagem num tópico do tipo obra, torre-a, setor, tipo, sensor e grandeza. A assinatura que vem pronta é obra, torre-a, cerquilha: chega tudo da obra. Repara no payload: um JSON com o carimbo de tempo em UTC, o bruto, o valor, a unidade, a qualidade e a bateria. Quase a anatomia inteira de uma leitura."

> "Clico em todos os piezômetros: obra, torre-a, mais, piezômetro, mais, nível. Agora só chegam PZ-01, PZ-02 e PZ-03. Clico em cerquilha barra nível: o simulador avisa, assinatura inválida, e o broker recusa. Agora digito: obra, torre-a, mais, mais, I-2, cerquilha. O primeiro mais pega o setor, o segundo pega o tipo, e a cerquilha, no final, pega qualquer grandeza do I-2. Só chegam as leituras do inclinômetro junto ao prédio antigo, perto de 8,6 milímetros. E, nos tópicos do broker, o status do gateway aparece como online, retido: se ele cair, o último desejo troca para offline."

> "Agora abro Séries temporais e escolho o PZ-03. Embaixo, o line protocol de verdade. A measurement se chama leitura; as tags são obra, setor, tipo e sensor; os fields são valor, bruto, bateria e qualidade; e o timestamp, em nanossegundos UTC, é a hora da medição. Nível perto de 5,9 metros, bruto perto de 8,7 miliampères. E o volume: onze sensores dão 2.064 pontos por dia, uns 753 mil por ano. Tópico bem desenhado e tag bem escolhida: é isso que deixa assinar, consultar e agregar."

### 11. Atividade, pontos-chave, próxima unidade e encerramento (16:20 – 18:50)

**[TELA]** Slide 16 — atividade prática.

> "Sua atividade fecha a unidade com a mão na massa. Monte num computador, ou com contêineres Docker, um broker Mosquitto, o Node-RED e o InfluxDB. No Wokwi, faça o ESP32 da Aula 10 publicar, a cada dez segundos, uma leitura em JSON num tópico do tipo obra, sua obra, teste, umidade, UR-01, leitura, com mensagem de último desejo no tópico de status. No Node-RED, assine o tópico, converta o valor, marque a qualidade e grave no InfluxDB com tags e fields bem escolhidos. Para testes, existe o broker público test.mosquitto.org; nunca o use para dado real de obra."

**[TELA]** Slide 17 — pontos-chave.

> "Pontos-chave. Um: MQTT é publicar e assinar por meio de um broker, com tópicos hierárquicos, curingas, QoS, mensagem retida, último desejo e TLS. Dois: o Node-RED liga os fluxos, assina, valida, calibra, marca a qualidade e grava, na borda ou na nuvem. Três: uma leitura é um registro completo, e o bruto nunca é sobrescrito. Quatro: no InfluxDB, measurement, tags, fields e timestamp; tag errada explode a cardinalidade, e retenção e agregação controlam o volume."

**[TELA]** Slide 18 — o que você verá na próxima unidade.

> "Com esta aula, você fecha a Unidade 3: o sensor, a plataforma embarcada, a rede e o banco de dados. Os dados agora chegam organizados. Na Unidade 4, Painéis, Integração com BIM e Gestão de Riscos, eles viram decisão. Na Aula 13, painéis de monitoramento com alertas e limites de alarme, no Grafana. Na Aula 14, a integração dos dados de drones e sensores com o BIM e com o planejamento e controle da obra. Na Aula 15, a tecnologia a favor da segurança do trabalho, à luz da NR-18. E, na Aula 16, privacidade, LGPD e cibersegurança, incluindo a segurança dos brokers e dispositivos que você conheceu hoje."

**[TELA]** Slide 19 — encerramento.

> "Foi um prazer acompanhar o seu dado do subsolo até o banco. Revise a atividade, faça o quiz e as questões da unidade, e a gente se vê na Unidade 4. Te espero na Aula 13!"
