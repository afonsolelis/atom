# Roteiros Estendidos (17–19 minutos) — Unidade 3: Sensores IoT no Monitoramento de Obras

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 9 a 12
- **Formato:** roteiro de narração **integral** — o texto em citação (>) é a fala completa. **Esta é a versão a gravar.** Duração-alvo: **17 a 19 minutos** por aula (cerca de 2.150 a 2.600 palavras faladas, a uns 135 palavras/min, já contando as pausas curtas das demonstrações). Os roteiros curtos de `unidade_3.md` são só um guia da sequência.

> **Como usar:** leia as falas em citação na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`), na mesma ordem dos slides. Quando a fala manda clicar, o efeito descrito aparece na tela em poucos segundos; tabelas e listas dos slides **não** são lidas item a item: a fala comenta o essencial e o aluno lê o resto na tela.

---

## Roteiro da Videoaula 9 — "Monitoramento geotécnico: inclinômetros, piezômetros e marcos de recalque"

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 9 de Drones e Sensores IoT no Monitoramento de Obras. Começamos hoje a Unidade 3, a unidade dos sensores. Na Unidade 1, você aprendeu a linguagem: sensor, transdutor, incerteza, calibração, arquitetura IoT, malha fechada. Na Unidade 2, o drone foi para o ar. Agora a gente desce para o chão — ou melhor, para dentro do chão. Hoje o assunto é monitoramento geotécnico: inclinômetros, piezômetros e marcos de recalque."

**[TELA]** Slide 3 — foto: prédios inclinados da orla de Santos.

> "Olha essa foto. É a orla de Santos, no litoral de São Paulo. Repara no prédio: ele não está reto. E não é ilusão de ótica nem defeito da lente. Dezenas de edifícios construídos ali entre as décadas de 1950 e 1970, com fundações rasas sobre camadas profundas de argila mole, inclinaram ao longo dos anos, à vista de todo mundo. É o recalque diferencial que a cidade inteira enxerga."

> "Agora eu quero que você imagine a sua obra. Uma escavação de 10 metros para três subsolos, num solo parecido, colada num prédio desses. Antes de a primeira caçamba de terra sair, você precisa responder a quatro perguntas: o que medir, com qual instrumento, onde instalar e com quais limites? É isso que a gente vai construir nesta aula."

### 2. O método observacional (1:30 – 3:20)

**[TELA]** Slide 4 — instrumentar para decidir: o método observacional.

> "Na geotecnia, a ideia de malha fechada que você aprendeu na Unidade 1 tem nome e sobrenome: é o método observacional, sistematizado pelo engenheiro Ralph Peck em 1969. Qual é o raciocínio? O solo nunca é exatamente o da sondagem. Entre um furo e outro, a natureza faz o que quer. Então o projetista adota as hipóteses mais prováveis e prevê como a obra vai se comportar: quanto a contenção deve deslocar, quanto o vizinho pode recalcar. E, antes de começar, ele define duas coisas: os limites aceitáveis e um plano de contingência — o que fazer se os limites forem atingidos. Aí a obra é executada medindo e comparando."

> "Repara no 'antes'. Instrumentação sem limites e sem plano de ação não é método observacional. É coleta de curiosidades. Você junta gráficos bonitos e não sabe o que fazer com eles."

> "Numa escavação urbana, três perguntas resumem o risco geotécnico, e cada uma tem o seu instrumento. Primeira: a contenção e o solo estão se deslocando na horizontal? Quem responde é o inclinômetro. Segunda: a água no solo está empurrando mais do que o previsto? Quem responde é o piezômetro. Terceira: os vizinhos estão descendo? Quem responde são os marcos de recalque. E tudo isso começa por uma palavra que eu vou repetir muitas vezes hoje: leitura zero. É a leitura de referência, feita antes de a escavação começar, de preferência repetida duas ou três vezes para garantir que ela é estável. Sem leitura zero, não existe com o que comparar."

### 3. A escavação instrumentada (3:20 – 4:40)

**[TELA]** Slide 5 — cena 3D: a escavação instrumentada. Clique em Escavar a cada fala de etapa.

> "Vamos ver isso funcionando. Na tela, uma escavação em corte, com a cortina de estacas, o prédio vizinho à esquerda e os instrumentos. Atrás da cortina, o tubo do inclinômetro, que desce bem abaixo do fundo da escavação. Os dois piezômetros, no solo. E, no pé do prédio, três marcos de recalque."

> "Eu vou clicar em escavar. Primeira etapa: dois metros e meio. Quase nada acontece. Mais uma: cinco metros. Repara que a cortina começa a fletir para dentro da escavação — o desenho exagera, claro, para você enxergar. Sete e meio. Agora olha o perfil do inclinômetro: ele se curva, maior no topo e zero lá embaixo. E os marcos do prédio vizinho começam a descer e a mudar de cor. Dez metros: o deslocamento no topo chega perto de 10 milímetros, e o marco mais próximo da escavação é o que mais recalca. Esse é o filme que a instrumentação vai contar, em números, ao longo da obra."

### 4. Como funciona o inclinômetro (4:40 – 7:10)

**[TELA]** Slide 6 — como funciona o inclinômetro.

> "Vamos abrir o inclinômetro. Ele mede o deslocamento horizontal ao longo da profundidade. Instala-se um tubo-guia, de plástico ou alumínio, com quatro ranhuras internas, num furo vertical atrás da contenção. O detalhe crucial: o pé do tubo tem que ficar engastado em solo ou rocha que não se mova — abaixo da zona de influência da escavação. Esse pé é o nosso ponto fixo."

> "Para ler, baixa-se uma sonda com rodinhas que correm pelas ranhuras. Dentro da sonda, há acelerômetros, que medem a inclinação em relação à vertical — exatamente como o sensor do seu celular sabe se ele está em pé ou deitado. A sonda vai até o fundo e é puxada de volta, parando a cada meio metro, que é a distância entre as rodas. Em cada parada, ela mede o ângulo theta do trecho, e o desvio horizontal daquele trecho é L vezes o seno de theta."

> "Dois cuidados fazem toda a diferença. Primeiro: faz-se uma segunda passada com a sonda girada 180 graus. Por quê? Porque, girando a sonda, o viés do sensor troca de sinal, e a média das duas passadas o cancela. É a veracidade da Aula 2 em ação. Segundo: o que interessa não é a inclinação absoluta do tubo, que nunca fica perfeitamente vertical. É a diferença em relação à leitura zero, trecho a trecho, acumulada de baixo para cima, a partir do pé fixo."

> "E aqui entra a ponte com a Aula 3. Além da sonda manual, que exige um técnico em campo, existe o inclinômetro in-place: uma cadeia de sensores MEMS fixos dentro do tubo, lidos automaticamente por um datalogger, a cada 15 minutos ou a cada hora. É exatamente o tipo de instrumento que a arquitetura IoT conecta à nuvem: o deslocamento chega ao painel sem ninguém descer ao canteiro."

**[TELA]** Slide 7 — simulação do perfil do inclinômetro. Clique em Referência, depois Há 7 dias e, por fim, Hoje.

> "Na simulação, à esquerda, a sonda descendo de meio em meio metro; à direita, o perfil de deslocamento acumulado, com a linha de atenção em 15 milímetros e a de alerta em 25. Começo na referência: tudo zero, claro, é a leitura zero. Agora, há sete dias: o perfil se curva, e o topo marca 7 milímetros. Hoje: o topo marca 10. Repara no formato: grande em cima e se anulando nos trechos de baixo. Isso é um bom sinal: confirma que o pé está fixo."

### 5. Exemplo numérico: do ângulo ao milímetro (7:10 – 8:50)

**[TELA]** Slide 8 — exemplo numérico: tabela trecho a trecho.

> "Vamos fazer a conta que a simulação fez. A sonda tem meio metro entre as rodas. Em relação à leitura zero, só os seis trechos superiores variaram. As variações do seno de theta, do topo para baixo, foram: 6, 5, 4, 3, 1,6 e 0,4 — tudo vezes dez elevado a menos três. Os trechos de baixo não variaram."

> "Multiplicando cada uma por meio metro, os desvios dos trechos são 3; 2,5; 2; 1,5; 0,8 e 0,2 milímetro. Agora acumula de baixo para cima: 0,2; depois 1; depois 2,5; 4,5; 7; e, no topo, 10 milímetros. Em uma linha só: meio metro vezes a soma, que é 0,020, dá 0,010 metro. Dez milímetros."

> "Mas o número sozinho não basta. Há sete dias, o topo estava em 7. Então a velocidade é 3 milímetros em 7 dias: uns 0,43 milímetro por dia. Com o nível de atenção em 15, mantido esse ritmo, a gente chega lá em cerca de 11,7 dias. Isso é tempo para decidir com calma — desde que a velocidade não aumente. E é por isso que, nos níveis de alerta, a gente vai olhar o valor e também a velocidade. Guarda essa ideia para a Aula 12."

### 6. Piezômetros e o tempo de resposta (8:50 – 11:20)

**[TELA]** Slide 9 — piezômetros: Casagrande, corda vibrante e pneumático.

> "Segundo instrumento: o piezômetro. Ele mede a poropressão, que é a pressão da água nos vazios do solo. Lembra da Aula 2? A poropressão se converte em altura de água por u igual a gama da água vezes h. Ela é crítica em escavações com rebaixamento do lençol, em aterros sobre solo mole e em taludes: água empurrando é empuxo a mais na contenção e resistência a menos no solo."

> "Existem três tipos principais. O de Casagrande, ou de tubo aberto: um tubo com uma ponta porosa lá embaixo; o nível d'água dentro do tubo é lido com um medidor elétrico, aquele de carretel que você viu na Unidade 1. É barato e robusto. O de corda vibrante, que está no desenho da tela: a água empurra um diafragma, que está ligado a um fio tensionado; quando a pressão muda, muda a frequência de vibração do fio, e as bobinas leem essa frequência. E o pneumático, lido com gás comprimido, ainda comum em barragens."

**[TELA]** Slide 10 — simulação do tempo de resposta. Comece em k = 10⁻⁸ m/s e depois mova para 10⁻⁹.

> "Agora, uma diferença que pouca gente percebe. No tubo aberto, para o nível dentro do tubo subir, um volume de água tem que entrar pelo solo. Em areia, isso é rápido. Em argila, é lento. A formulação clássica de Hvorslev diz que o tempo básico de resposta é a área do tubo dividida pelo fator de forma da ponta vezes a permeabilidade. Na tela, a pressão no solo sobe de repente no instante zero. A curva do piezômetro de corda vibrante sobe em minutos. A do Casagrande, com permeabilidade de dez à menos oito metros por segundo, leva da ordem de dez horas. Agora eu baixo a permeabilidade para dez à menos nove: vira dias."

> "Pensa no que isso significa. Choveu forte de madrugada, o nível d'água no solo subiu, e o seu piezômetro de tubo aberto em argila só vai mostrar isso dias depois. Ele 'mente' por atraso. É por isso que, onde a resposta precisa ser rápida — escavação com rebaixamento, aterro sobre argila mole —, a escolha é corda vibrante, que ainda por cima conversa com o datalogger e entra na malha fechada. Só não esqueça: o de corda vibrante precisa de correção de temperatura e, se não for do tipo ventilado, de correção da pressão atmosférica."

### 7. Marcos de recalque e a referência de nível (11:20 – 12:50)

**[TELA]** Slide 11 — marcos de recalque e a referência que não pode se mexer.

> "Terceiro instrumento: os marcos de recalque. São pinos metálicos fixados nos pilares ou na base da fachada do vizinho. Eles são lidos por nivelamento geométrico de precisão, com nível e mira, a partir de uma referência de nível, a RN. Na foto, uma referência de nível de precisão, com a mira apoiada em cima."

> "E aqui está a regra mais importante: a referência não pode se mexer. Ela tem que ser profunda e ficar fora da zona de influência da escavação. Se a RN estiver dentro da área que recalca, ela desce junto com tudo, e as suas leituras mostram 'zero recalque' enquanto o prédio está descendo. Todas as leituras mentem juntas — e ninguém percebe."

> "A automação também chegou aqui. Estações totais robóticas leem prismas fixados no vizinho a cada hora, sozinhas. Células de recalque por nível hidrostático usam o princípio dos vasos comunicantes com transdutores de pressão. E os clinômetros de parede, os tiltmeters, medem a rotação de um pilar ou de uma fachada. Tudo isso pode entrar na mesma rede LoRaWAN da Aula 3."

### 8. Recalque diferencial e distorção angular (12:50 – 15:50)

**[TELA]** Slide 12 — cena 3D: o prédio que recalca. Comece com 18 e 6 mm a 6 m; depois aumente o recalque de P1.

> "Agora a pergunta de ouro: quando o recalque vira dano? Repara no prédio da tela, sobre quatro pilares. Se todos descerem igualzinho, o prédio desce inteiro, como um elevador. Ruim para as ligações de água e esgoto, mas a estrutura não distorce. O que fissura um prédio é o recalque diferencial: um pilar descendo mais que o vizinho."

> "A medida usada é a distorção angular, beta: o recalque diferencial dividido pela distância entre os dois pilares. Na simulação, o pilar P1 recalcou 18 milímetros e o P2, 6, a 6 metros de distância. A diferença é 12 milímetros. Doze sobre seis mil milímetros: 0,002, ou um quinhentos avos. Olha a parede entre os dois pilares: ela já mudou de cor. Agora eu aumento o recalque de P1… Passou de um trezentos avos: aparece a fissura diagonal."

**[TELA]** Slide 13 — a escala de Bjerrum (1963).

> "Esses números vêm de uma escala proposta por Bjerrum em 1963, ainda muito usada como referência. Com um setecentos e cinquenta avos, começam dificuldades com máquinas sensíveis a recalques. Um quinhentos avos é o limite de segurança para edifícios em que não se admitem fissuras. Um trezentos avos: primeiras fissuras em paredes de alvenaria. Um duzentos e cinquenta avos: a inclinação de prédios altos fica visível — lembra de Santos? E um cento e cinquenta avos: fissuração considerável e danos estruturais."

> "E tem a norma. A NBR 6122, de projeto e execução de fundações, torna obrigatório o monitoramento de recalques em alguns casos — por exemplo, estruturas em que a carga variável é significativa, como silos e reservatórios, edifícios altos ou esbeltos e fundações não convencionais. Mas, numa escavação ao lado de um vizinho sensível, ninguém precisa da norma mandar: o plano de monitoramento é que fixa os limites de cada instrumento."

**[TELA]** Slide 14 — calculadora: o vizinho já fissura?

> "Na calculadora, os mesmos números: 18 e 6 milímetros, 6 metros. Recalque diferencial de 12, distorção de um quinhentos avos. Classificação: no limite para edifícios em que não se admitem fissuras. O que fazer? Vistoriar o vizinho, aumentar a frequência de leitura e acionar o plano de contingência que já estava escrito. Teste aí: se os pilares estivessem a 4 metros um do outro, com os mesmos recalques, a distorção iria para um trezentos e trinta e três avos. A distância entre os pilares muda tudo."

### 9. Do manual ao IoT, atividade e encerramento (15:50 – 18:00)

**[TELA]** Slide 15 — do manual ao IoT: quando e como ler.

> "Para fechar o raciocínio: a frequência de leitura muda com a fase da obra. Antes: leitura zero, repetida duas ou três vezes. Durante a escavação: leituras diárias, ou automáticas a cada 15 a 60 minutos nos instrumentos críticos. Depois que estabiliza: semanal, depois mensal. E sempre com redundância: dois instrumentos que contam a mesma história. Se o inclinômetro acusa deslocamento, o marco do vizinho deveria recalcar junto. Se só um deles mexe, desconfie do instrumento antes de desconfiar da obra."

**[TELA]** Slide 16 — atividade prática.

> "Sua missão: para a escavação de 10 metros ao lado do prédio de Santos, desenhe uma planta e um corte. Posicione os inclinômetros, dizendo até onde o pé deve descer; os piezômetros, dizendo de que tipo; os marcos de recalque e a referência de nível. Defina a leitura zero, a frequência de leitura em cada fase, os níveis de atenção e alerta de cada grandeza — incluindo a distorção angular. E diga qual instrumento confirma qual."

**[TELA]** Slide 17 — pontos-chave; Slide 18 — encerramento.

> "Resumindo. Método observacional: prever, fixar limites e plano antes, e medir durante. Inclinômetro: L vezes o seno do ângulo, acumulado de baixo para cima, sempre em relação à leitura zero. Piezômetro: o de tubo aberto é lento em argila; o de corda vibrante responde rápido e entra na malha. Marcos de recalque: só valem com uma referência estável, e o dano depende da distorção angular. Hoje você instrumentou o solo e os vizinhos. Na próxima aula, a gente sobe para a estrutura: extensômetros, acelerômetros, fissurômetros e a maturidade do concreto. Te espero na Aula 10!"

---

## Roteiro da Videoaula 10 — "Monitoramento estrutural: extensômetros, acelerômetros, fissurômetros e maturidade do concreto"

**Duração-alvo:** cerca de 17:40 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Aqui é o professor Afonso Brandão, e esta é a Aula 10. Na aula passada, a gente instrumentou o solo e os vizinhos. Hoje a gente sobe para a estrutura: extensômetros, acelerômetros, fissurômetros e a maturidade do concreto."

**[TELA]** Slide 3 — foto: a laje concretada na quarta.

> "Sexta-feira, cinco da tarde. A laje do décimo segundo pavimento foi concretada na quarta. O empreiteiro chega e diz: 'Engenheiro, preciso tirar o escoramento na segunda para reaproveitar as formas no próximo andar'. Os corpos de prova só vão ser rompidos depois. Dá para liberar? Ao mesmo tempo, na escavação ao lado, alguém percebeu que uma escora metálica parece 'ganhar' carga à tarde, quando o sol bate. E o vizinho reclama de uma fissura que 'abre e fecha'."

> "Três situações diferentes, a mesma resposta: medir o que a estrutura está sentindo. E, nas três, você vai ver que existe um vilão escondido, que engana quem não presta atenção: a temperatura. Vamos nessa."

### 2. Quatro perguntas, quatro sensores (1:30 – 2:50)

**[TELA]** Slide 4 — galeria: quatro perguntas, quatro sensores.

> "O monitoramento estrutural responde a quatro perguntas típicas. Quanto esforço a peça está recebendo? Isso é deformação, e quem mede é o extensômetro. Como a estrutura vibra? Isso é aceleração, e quem mede é o acelerômetro. A fissura está crescendo? Quem responde é o fissurômetro. E o concreto já ganhou resistência? Isso a gente estima com a temperatura ao longo do tempo, com sensores de maturidade embutidos no concreto."

> "E em todas elas vale a lição da Unidade 1: o sensor só tem utilidade com três coisas. Uma leitura zero, limites definidos e uma ação associada a cada limite. Sensor sem isso é enfeite caro."

### 3. Extensômetros e a escora no sol (2:50 – 6:30)

**[TELA]** Slide 5 — extensômetro elétrico × corda vibrante.

> "Comecemos pelo extensômetro. Na Aula 2 você conheceu o elétrico de resistência: uma grade metálica colada na peça que muda de resistência quando a peça deforma — delta R sobre R igual ao fator do extensômetro vezes a deformação. Ele lê fenômenos rápidos, mas em monitoramentos de meses pode sofrer com umidade e deriva."

> "Na obra, para o longo prazo, quem reina é o extensômetro de corda vibrante. É um fio de aço tensionado entre dois blocos presos à peça. Quando a peça deforma, a tensão no fio muda, e muda a frequência com que ele vibra — a deformação é proporcional ao quadrado da frequência. É como uma corda de violão: apertou, o som fica mais agudo. A vantagem é que frequência não se perde no cabo: ele é estável por anos e não liga para a resistência de cem metros de fio. Pode ser soldado numa escora metálica ou amarrado à armadura, para ficar embutido no concreto."

> "E como deformação vira força? No regime elástico, pela lei de Hooke: sigma igual a E vezes épsilon. E a força é sigma vezes a área. A deformação é tão pequena que a gente a mede em microdeformações: um milionésimo. Para você ter uma ideia, uma barra de um metro que alonga um milésimo de milímetro sofreu uma microdeformação. Um extensômetro bom resolve isso com folga."

> "E onde instalar? Na escora metálica, no meio do vão, longe das ligações, de preferência com dois sensores em lados opostos da seção, para separar a compressão da flexão. No concreto, nas regiões em que o projeto prevê os maiores esforços: meio do vão de uma viga de transição, base de um pilar muito carregado, a laje sobre um apoio. Sempre perguntando: que decisão esse número vai apoiar?"

**[TELA]** Slide 6 — simulação da escora instrumentada. Comece com 250 µε e ΔT = 0; depois aumente a temperatura e alterne a compensação.

> "Vamos fazer a conta com a escora da tela. Aço, módulo de 200 gigapascals, área de 120 centímetros quadrados. O extensômetro indica 250 microdeformações desde a leitura zero, já corrigidas para a temperatura. Sigma: 200 mil megapascals vezes 250 milionésimos, 50 megapascals. Força: 50 megapascals vezes 0,012 metro quadrado, 0,6 meganewton. Seiscentos quilonewtons. A carga de projeto é 900: a escora está a 67%."

> "Agora o vilão. Eu aumento a temperatura em 15 graus, como entre a manhã e a tarde de sol. O aço tem coeficiente de dilatação de uns 12 milionésimos por grau. Quinze graus vezes 12: 180 microdeformações. Olha o tamanho disso perto dos 250 do sinal! Sem compensação, o painel mostraria uma escora quase no limite só porque o sol bateu nela. Agora eu ligo a compensação: o sistema usa o termistor que vem dentro do próprio extensômetro e separa a parcela térmica. É por isso que todo extensômetro de corda vibrante sério tem um termistor embutido — e é por isso que a leitura tem que ser corrigida antes de virar força. Detalhe importante: numa escora travada entre duas paredes, parte do efeito térmico pode virar força de verdade. Separar as duas coisas é trabalho do engenheiro, não do software."

**[TELA]** Slide 7 — foto: extensômetros amarrados à armadura antes da concretagem.

> "E uma dica de campo. Extensômetro embutido no concreto tem que ser instalado antes da concretagem: amarrado à armadura, como na foto, com o cabo protegido. A leitura zero é feita logo depois do lançamento. E saiba que é comum perder sensores na concretagem — o vibrador acerta um cabo, um sensor se solta. Por isso a regra é redundância: instale mais do que o mínimo. Depois não tem segunda chance."

### 4. Acelerômetros e frequência natural (6:30 – 9:40)

**[TELA]** Slide 8 — acelerômetros: a estrutura tem uma assinatura.

> "Segundo sensor: o acelerômetro. Existem os MEMS, que são chips baratos e de baixo consumo, ótimos para IoT, e os piezoelétricos, mais sensíveis e com faixa de frequência maior. Na foto, um acelerômetro com nó sem fio, preso ao pendural de uma ponte em arco."

> "Por que medir aceleração numa estrutura? Porque toda estrutura tem frequências naturais — o jeito como ela gosta de vibrar. No modelo mais simples, de massa e mola, a frequência natural é um sobre dois pi vezes a raiz de k sobre m: rigidez sobre massa. Agora repara: se a rigidez cai — por fissuração, por uma ligação danificada —, a frequência cai junto. E cai com a raiz quadrada. Dez por cento de rigidez a menos dá uns cinco por cento de frequência a menos, porque 0,95 ao quadrado é cerca de 0,90. A frequência é a assinatura da rigidez. Esse é o princípio do monitoramento da saúde estrutural, que você vai ver na literatura com a sigla em inglês SHM. E lembre de Nyquist: amostrar a mais do dobro — na prática, cinco a dez vezes — a maior frequência que interessa."

**[TELA]** Slide 9 — cena 3D: o prédio que oscila. Comece em Rigidez original e depois clique em Após dano.

> "Na cena 3D, um prédio esbelto oscilando no primeiro modo, com o acelerômetro amarelo no topo. No canto, o espectro: o pico está em 1,20 hertz — valor ilustrativo. Agora eu clico em 'após dano', com 10% a menos de rigidez. Repara: a oscilação fica um pouco mais lenta, e o pico do espectro anda para a esquerda, para uns 1,14 hertz. Cinco por cento de queda. Na prática, a temperatura, a umidade e até a ocupação mexem nessa frequência, então a mudança tem que ser persistente e explicada — mas é um alerta precioso, que nenhuma inspeção visual daria."

**[TELA]** Slide 10 — foto: a Millennium Bridge, em Londres.

> "E um caso famoso. Essa é a Millennium Bridge, uma passarela sobre o Tâmisa, em Londres. Inaugurada em junho de 2000, ela foi fechada dois dias depois: com a multidão, começou a balançar lateralmente, porque os pedestres, sem perceber, sincronizavam o passo com a oscilação da ponte. Ela só reabriu em 2002, depois da instalação de amortecedores. A lição: medir aceleração e frequências faz parte do projeto e do comissionamento. Não é luxo."

### 5. Fissurômetros: a tendência importa (9:40 – 11:50)

**[TELA]** Slide 11 — fissurômetros: a fissura está crescendo?

> "Terceiro sensor: o fissurômetro. O mais simples é o tell-tale de acrílico: duas placas sobrepostas, uma com uma retícula, fixadas uma de cada lado da fissura. Você lê a olho, com resolução da ordem do milímetro. É barato e ótimo para vistoria. Já o fissurômetro elétrico, com potenciômetro ou LVDT, chega a centésimos de milímetro e manda o dado para o datalogger."

> "E aqui a temperatura volta a atacar. A fissura abre e fecha todo dia — durante o dia o material dilata, à noite contrai — e também ao longo das estações. Aquele vizinho que diz que a fissura 'abre e fecha' está certo! O que interessa não é essa oscilação: é a tendência."

**[TELA]** Slide 12 — simulação da série da fissura. Clique em Separar efeito térmico e depois em Leitura manual semanal.

> "Olha a série de 30 dias. A linha sobe e desce todo dia: é o ciclo térmico. Eu clico em separar o efeito térmico: aparece a média diária, e agora dá para ver que, a partir do dia 15, a fissura começou a abrir um centésimo de milímetro por dia. Isso é sinal estrutural. Um centésimo por dia parece nada, mas são três décimos de milímetro por mês, e a fissura não para sozinha. Agora eu mostro o que um técnico veria com uma leitura manual por semana: quatro pontos. A tendência desaparece no meio da oscilação. Por isso a leitura contínua vale mais. E uma regra de ouro: mapeie e fotografe as fissuras do vizinho antes de a obra começar, numa vistoria cautelar. Sem isso, toda fissura vai ser 'culpa da obra'."

### 6. Maturidade do concreto (11:50 – 14:30)

**[TELA]** Slide 13 — o método da maturidade.

> "Agora, a laje do gancho. A resistência do concreto nas primeiras idades depende da temperatura da cura. No calor, a hidratação do cimento é mais rápida; no frio, mais lenta. O método da maturidade, padronizado na ASTM C1074, traduz o histórico de temperatura num único número."

> "Na função de Nurse-Saul, o fator temperatura-tempo é M igual à soma de T menos T zero, vezes delta t. T é a temperatura média do concreto em cada intervalo; T zero é a temperatura de referência, abaixo da qual se considera que o concreto não ganha resistência. A ASTM recomenda zero grau para cimento tipo I sem aditivos, com cura entre 0 e 40 graus — mas o ideal é determiná-la para a sua mistura. A unidade é grau Celsius vezes hora."

> "Como se usa? Em laboratório, rompem-se corpos de prova da mesma mistura em várias idades, medindo também a maturidade deles, e ajusta-se uma curva de resistência em função de M. Na obra, sensores embutidos na laje registram a temperatura a cada 15 ou 30 minutos e mandam pela rede. Juntou os dois, você estima a resistência em tempo real. E atenção: isso apoia decisões de obra — desforma, retirada de escoramento, protensão. Não substitui o controle tecnológico de aceitação do concreto por corpos de prova."

**[TELA]** Slide 14 — simulação: 72 horas de maturidade. Clique em Caso do exemplo e depois em Inverno.

> "Na simulação, a curva de temperatura, o M acumulado e a resistência estimada pela curva de calibração, com a linha-alvo de 21 megapascals. Caso do exemplo: 28, 32 e 26 graus em blocos de 12 horas. O marcador mostra que o alvo é atingido por volta de 29 horas. Agora o inverno, a 15 graus constantes: o mesmo alvo só chega perto de 56 horas. Mesma laje, mesmo concreto, mais de um dia de diferença. É exatamente esse tipo de informação que o cronograma precisa."

> "E repara num detalhe da curva de temperatura: logo depois da concretagem, ela sobe sozinha, mesmo com o tempo ameno. É o calor de hidratação do cimento. Em peças espessas, o concreto massa, esse calor é tão grande que a diferença entre o núcleo quente e a superfície fria pode fissurar a peça. Os mesmos sensores de temperatura servem para vigiar isso: dois sensores, um no centro e outro perto da face, e um limite para a diferença entre eles. É o sensor de maturidade fazendo dupla função."

**[TELA]** Slide 15 — calculadora: pode liberar a laje?

> "Vamos à conta do texto. A calibração da mistura deu f c igual a 9,2 vezes o logaritmo natural de M, menos 41 — valores ilustrativos. Maturidade: 12 vezes 28 mais 32 mais 26, que dá 12 vezes 86: 1.032 grau-hora. Resistência estimada: 9,2 vezes o logaritmo de 1.032, menos 41, uns 22,8 megapascals. Acima dos 21 exigidos. A maturidade necessária era de uns 845 grau-hora. Decisão: liberar, confirmando com corpos de prova e com o projetista da estrutura."

### 7. Atividade, pontos-chave e encerramento (14:30 – 17:40)

**[TELA]** Slide 16 — atividade prática.

> "Sua missão: um edifício de 15 pavimentos, com escavação escorada e um vizinho que já tem fissuras. Monte uma tabela com a grandeza, o sensor, o local de instalação, o momento da leitura zero, a frequência de leitura, a forma de compensar a temperatura e a decisão que cada sensor apoia — reforçar uma escora, liberar uma laje, chamar o projetista. Inclua pelo menos um extensômetro, um fissurômetro e um sensor de maturidade. Pense em redundância: onde você instalaria dois sensores em vez de um?"

> "E uma pergunta para você levar: se o seu sensor de maturidade fica no meio da laje, e a borda da laje, exposta ao vento, esfria mais rápido, onde está o ponto crítico? A resposta muda a posição do sensor. Instrumentar é sempre escolher onde a pergunta é mais difícil."

**[TELA]** Slide 17 — pontos-chave.

> "Resumindo. Extensômetro dá deformação; força vem de sigma igual a E épsilon e N igual a sigma A — depois de corrigir a temperatura, que pode valer 180 microdeformações numa escora ao sol. Acelerômetro: a frequência natural é a assinatura da rigidez; dez por cento a menos de rigidez, uns cinco por cento a menos de frequência. Fissurômetro: o que importa é a tendência, não a oscilação diária, e as fissuras do vizinho se mapeiam antes da obra. Maturidade: temperatura vezes tempo, com curva calibrada para a mistura, sem dispensar os corpos de prova."

**[TELA]** Slide 18 — encerramento e gancho para a Aula 11.

> "Repara que, nas três histórias de hoje, o vilão foi o mesmo: a temperatura. Na escora, ela fingia carga. Na fissura, ela fingia movimento. Na laje, ela era a própria informação. Saber separar o sinal do efeito térmico é o que distingue quem lê sensor de quem só olha gráfico. Na próxima aula, o monitoramento sai da estrutura e vai para o entorno: vibração nos vizinhos, ruído, poeira e o rastreamento de máquinas e pessoas. Te espero na Aula 11!"

---

## Roteiro da Videoaula 11 — "Segurança, ambiente e produtividade: vibração, ruído, poeira e rastreamento de equipamentos"

**Duração-alvo:** cerca de 17:50 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Aqui é o professor Afonso Brandão, e esta é a Aula 11. Até agora, nesta unidade, a gente olhou para dentro da obra: o solo, a contenção, a estrutura. Hoje a gente olha para fora, para o entorno e para a operação do canteiro: vibração, ruído, poeira e rastreamento de máquinas e pessoas."

**[TELA]** Slide 3 — foto: estacas cravadas ao lado de uma casa.

> "Segunda-feira, oito da manhã. Começa a cravação de estacas-prancha a 15 metros de um casarão tombado — parecido com o da foto, onde o bate-estacas trabalha rente à casa de tijolos. Às nove, o morador liga: 'a casa inteira treme'. Às dez, a vizinhança reclama do barulho e da poeira na prefeitura. Às onze, um caminhão de terra dá ré na rampa e passa a meio metro de um ajudante. Quatro problemas diferentes numa só manhã."

### 2. Três frentes, uma arquitetura (1:40 – 2:50)

**[TELA]** Slide 4 — três frentes, uma só arquitetura.

> "Repara que os quatro problemas se agrupam em três frentes. Segurança: vibração nos vizinhos e colisão entre máquina e pessoa. Ambiente: ruído e poeira. E uma terceira, que muita gente esquece: produtividade — as máquinas estão trabalhando ou só ligadas? A boa notícia é que a arquitetura é a mesma da Aula 3: sensor, rede, plataforma, ação. O que muda é a régua de comparação. Tem norma da ABNT, resolução do CONAMA, a legislação municipal — que costuma regular o ruído e o horário de obra — e a NR-18, que trata da segurança e saúde no trabalho na indústria da construção."

### 3. Vibração: PPV e frequência (2:50 – 6:40)

**[TELA]** Slide 5 — vibração: velocidade de partícula e frequência.

> "Vamos começar pela vibração. Para avaliar risco de dano numa edificação, a grandeza usada é a velocidade de vibração de partícula de pico, em milímetros por segundo — a sigla em inglês é PPV. Quem mede é o sismógrafo de engenharia, com um geofone triaxial apoiado no pé da edificação vizinha. Triaxial porque mede três componentes: vertical, longitudinal e transversal. E a NBR 9653 define a velocidade de pico como o maior dos três picos."

> "Mas o valor não basta. A frequência dominante também importa, e muito. As edificações são mais sensíveis às baixas frequências, que ficam perto das frequências naturais delas — lembra da aula passada? Uma vibração lenta, de poucos hertz, conversa com o prédio; uma vibração rápida, de 50 hertz, ele mal sente. Na foto, um sismógrafo com sensores no tripé, ao lado de uma obra. Ele fica ligado com um gatilho: quando a vibração passa de um limiar, registra o evento inteiro."

**[TELA]** Slide 6 — simulação: PPV × distância e frequência. Comece a 15 m e 10 Hz; depois aproxime a fonte e mude a frequência.

> "Na simulação, à esquerda, a forma de onda: cada golpe do martelo gera uma rajada que se amortece. À direita, a curva-limite da NBR 9653 em função da frequência, com o nosso ponto. A 15 metros e 10 hertz, a PPV é de 12 milímetros por segundo — valores ilustrativos. Eu aproximo a fonte para 8 metros: a PPV sobe bastante, porque a vibração se atenua com a distância. Agora eu volto para 15 e subo a frequência para 30 hertz: a mesma PPV, mas o ponto fica bem mais longe da curva. A frequência mudou a avaliação."

**[TELA]** Slide 7 — a curva da NBR 9653 e os cuidados.

> "Os números da norma. De 4 a 15 hertz, o limite começa em 15 milímetros por segundo e aumenta linearmente até 20. De 15 a 40 hertz, sobe linearmente de 20 até 50. Acima de 40 hertz, 50. E abaixo de 4 hertz, a norma usa outro critério: deslocamento de partícula de pico de no máximo 0,6 milímetro. Ela também limita a pressão acústica de um desmonte a 100 pascals, que são 134 decibéis lineares de pico."

> "Vamos ao exemplo. Doze milímetros por segundo a 10 hertz. O limite a 10 hertz é 15 mais 5 vezes, 10 menos 4, sobre 15 menos 4: uns 17,7. Doze sobre 17,7: 68% do limite. Se fosse a 30 hertz, o limite seria 38."

> "Agora, os dois cuidados que separam o engenheiro do aplicador de tabela. Primeiro: a NBR 9653 foi feita para desmonte de rocha com explosivos, em mineração perto de áreas urbanas. Para cravação de estacas, compactação vibratória e, principalmente, para uma edificação sensível como um casarão tombado, o plano de monitoramento costuma fixar limites próprios, bem mais baixos. Nesse caso, 12 milímetros por segundo provavelmente pediriam ação imediata. Segundo: o incômodo humano aparece muito antes de qualquer dano. O morador sente a casa tremer com valores que não trincam parede nenhuma — e isso também precisa de resposta, com comunicação e horário combinado."

> "E o que fazer quando a vibração passa do limite do plano? As alavancas são conhecidas: reduzir a energia do golpe, aumentar a distância — por exemplo, mudando a sequência de cravação —, fazer pré-furo, trocar estacas cravadas por escavadas ou prensadas, ou, numa compactação, trocar o rolo vibratório por um estático perto do vizinho. E, depois de cada mudança, medir de novo. Malha fechada, sempre. Uma dica de ouro: faça a vistoria cautelar do casarão antes da primeira estaca, com fotos datadas de todas as fissuras existentes. Sem ela, qualquer trinca vai ser atribuída à sua obra."

### 4. Ruído: decibéis não se somam como metros (6:40 – 9:30)

**[TELA]** Slide 8 — ruído e a NBR 10151.

> "Segunda frente: ruído. O nível de pressão sonora se mede em decibéis, uma escala logarítmica. A ponderação A, o dB(A), aproxima a sensibilidade do ouvido humano, que escuta mal os graves. E, como o ruído varia o tempo todo, usa-se o nível equivalente, o L A eq: o nível constante que teria a mesma energia no intervalo. Na foto, um sonômetro marcando 49,3 decibéis."

> "A referência técnica é a NBR 10151, de 2019, que define como medir e avaliar o ruído em áreas habitadas, com limites por tipo de área e período. Por exemplo: 50 decibéis de dia e 45 à noite numa área estritamente residencial urbana ou de hospitais ou de escolas; 55 e 50 numa área mista predominantemente residencial. E a lei municipal pode trazer regras próprias, como os horários permitidos para obra."

**[TELA]** Slide 9 — calculadora: somando três máquinas.

> "Agora o que pega muita gente. Decibel não se soma como metro. Como a escala é logarítmica, a gente soma as energias: dez vezes o logaritmo da soma de dez elevado a L sobre dez. No receptor, um gerador sozinho dá 62, uma escavadeira, 65, e o bate-estacas, 68 decibéis. Total: não é 195! É uns 70,4. Agora a pergunta prática: o que adianta desligar? Eu tiro o gerador, o mais silencioso: cai para 69,8. Seis décimos. Quase nada. Eu trato o bate-estacas, o mais barulhento: cai para 66,8. A lição é simples: ataque a fonte dominante."

> "Duas regrinhas para guardar. Duas fontes iguais somam 3 decibéis: dois compressores de 70 dão 73, não 140. E, para uma fonte pontual ao ar livre, dobrar a distância tira uns 6 decibéis. Oitenta e cinco decibéis a 10 metros viram uns 67 a 80 metros. Mesmo assim, perto de uma referência de 55, ainda sobra excedente — e aí entram barreiras acústicas, enclausuramento, horários restritos e métodos menos ruidosos, como estacas escavadas no lugar das cravadas."

### 5. Poeira: MP10 e MP2,5 (9:30 – 12:00)

**[TELA]** Slide 10 — poeira: MP10 e MP2,5.

> "Terceira frente: poeira. Ela é monitorada como material particulado: MP10, partículas de até 10 micrômetros, e MP2,5, de até 2,5 micrômetros, que entram fundo no sistema respiratório. Os sensores IoT mais comuns são óticos: um feixe de luz, uma câmara, e as partículas espalham a luz. São baratos e gastam pouca energia. Mas têm um defeito conhecido: com umidade alta, as partículas incham de água e o sensor superestima. Por isso eles precisam ser calibrados por colocalização: ficam um tempo ao lado de uma estação de referência, e você corrige a curva. É a calibração da Aula 2 aplicada ao ar."

> "E onde colocar o sensor? Na divisa, do lado de quem você quer proteger — a escola, as casas —, e de preferência com um segundo sensor do lado oposto, para medir a poeira que já chega de fora. Sem esse sensor de fundo, você pode ser culpado pela poeira da avenida. Junto, uma estação meteorológica simples, com direção e velocidade do vento: a mesma terraplenagem pode não incomodar ninguém com vento a favor e encher a escola de pó com vento contrário. A regra de aspersão fica muito mais inteligente quando cruza a poeira com o vento."

> "E a régua? Os padrões nacionais de qualidade do ar estão na Resolução CONAMA número 506, de 2024, que substituiu a 491, de 2018. Ela entra em vigor por etapas; na etapa atual, a PI-2, em vigor desde janeiro de 2025, a média de 24 horas é de 100 microgramas por metro cúbico para MP10 e 50 para MP2,5. Mas atenção, que aqui muita gente erra: esses são padrões de qualidade do ar ambiente, da cidade, não limites de emissão de uma obra. O plano de monitoramento define os gatilhos próprios, medidos na divisa do canteiro, e a ação de cada um. Na foto, uma das ações clássicas: jato d'água sobre a demolição."

**[TELA]** Slide 11 — simulação: MP10 na divisa, com aspersão. Comece em Malha fechada e depois clique em Malha aberta.

> "Na simulação, o MP10 na divisa ao longo de um dia de terraplenagem, com níveis do plano — ilustrativos, não da CONAMA. Em malha fechada, com leitura a cada 15 minutos, cruzou a atenção, a aspersão liga e a curva cai. Em malha aberta, com uma vistoria a cada 6 horas, a poeira passa do alerta antes de alguém ligar o caminhão-pipa. É a mesma lição da Unidade 1, agora no ar que o vizinho respira. E não esqueça o trabalhador: a poeira com sílica cristalina, de corte de concreto e de rocha, é risco ocupacional sério, tratado pelas normas regulamentadoras."

### 6. Rastreamento e produtividade (12:00 – 15:00)

**[TELA]** Slide 12 — rastreamento: máquinas, pessoas e cercas virtuais.

> "Quarta peça: o rastreamento. Nas máquinas, a telemetria com GNSS informa posição, horas de motor, tempo em marcha lenta e consumo. Nas pessoas, sistemas de localização em tempo real, o RTLS, com etiquetas UWB, que localizam com precisão de decímetros, ou BLE, de metros, presas no capacete ou no crachá. Com isso, você cria cercas virtuais: uma zona de exclusão em torno da escavadeira. Entrou, o operador e o trabalhador recebem um alerta sonoro."

**[TELA]** Slide 13 — cena 3D: a cerca virtual. Deixe rodar com a cerca ligada; depois desligue.

> "Na cena, a escavadeira gira, o caminhão vai e volta pela rota e três trabalhadores circulam. O disco vermelho é a zona de exclusão, de oito metros. Repara: um trabalhador entrou na zona — ele e a máquina piscam, e o contador de alertas sobe. Agora eu desligo a cerca virtual. A situação continua acontecendo, mas ninguém é avisado e nada fica registrado. O quase-acidente da rampa do nosso gancho, sem cerca, é só um susto que ninguém conta. Com cerca, vira dado: onde, quando, com qual máquina. É assim que se corrige um layout de canteiro antes do acidente."

> "Pense na pirâmide clássica da segurança do trabalho: para cada acidente grave, existem muitos quase-acidentes que ninguém registrou. A cerca virtual transforma esses quase-acidentes em estatística. Se a mesma rampa gera dez alertas por dia, o problema não é o trabalhador desatento: é a rampa, o fluxo do caminhão, a falta de um sinaleiro. O dado aponta para a correção do processo, que é o que a NR-18 pede quando fala em planejar a circulação de máquinas e pessoas no canteiro."

**[TELA]** Slide 14 — calculadora: a escavadeira trabalha ou só fica ligada?

> "E a mesma telemetria fala de produtividade. Turno de 9 horas. A escavadeira ficou 7,2 horas com o motor ligado, das quais 2,1 em marcha lenta, parada. Tempo produtivo: 5,1 horas. Utilização: 5,1 sobre 9, uns 57%. Ociosidade: 2,1 sobre 7,2, uns 29% do tempo ligado. A 4 litros por hora em marcha lenta, valor ilustrativo, são 8,4 litros de diesel por dia queimados para nada — em 22 dias, quase 185 litros. E o dado não serve para culpar o operador: em geral, a escavadeira espera porque o caminhão não chegou. O gargalo está no ciclo, e é o dado que mostra onde."

### 7. Pausa para reflexão (15:00 – 16:30)

**[TELA]** Slide 15 — Pausa para reflexão: rastrear pessoas é segurança ou vigilância?

> "Agora eu quero que você pause o vídeo e pense comigo. O crachá UWB que evitou o atropelamento na rampa é o mesmo que registra, minuto a minuto, onde cada trabalhador esteve. Pausas, idas ao banheiro, conversas, quanto tempo cada um ficou em cada frente. Rastrear pessoas é segurança ou vigilância?"

> "Considere cinco perguntas. Qual é a finalidade declarada? Dá para minimizar o dado — por exemplo, processar só a proximidade com a máquina, na borda, sem guardar um histórico com nome? Por quanto tempo o dado fica guardado? Quem tem acesso? E os trabalhadores foram informados, com clareza? Uma regra para testar: coletar o mínimo necessário para a finalidade de segurança, informar com transparência e não reutilizar o dado para outra finalidade, como avaliar desempenho individual. Volte ao vídeo quando tiver a sua resposta. Esse tema volta, com a LGPD, na Unidade 4."

### 8. Atividade, pontos-chave e encerramento (16:30 – 17:50)

**[TELA]** Slide 16 — atividade prática.

> "Sua missão: o plano de monitoramento ambiental e de segurança da cravação junto ao casarão. Onde ficam o sismógrafo, o sonômetro e o sensor de MP10? Quais são os níveis de atenção e de alerta do plano para cada grandeza, e qual ação corresponde a cada um — reduzir a energia de cravação, trocar o método, aspergir água, mudar o horário? Qual é a regra da cerca virtual? E o que vai no relatório para o vizinho e para a prefeitura?"

**[TELA]** Slide 17 — pontos-chave; Slide 18 — encerramento.

> "Resumindo. Vibração se avalia por PPV e frequência; a NBR 9653 é a régua do desmonte com explosivos, e edificações sensíveis pedem limites próprios. Ruído se soma em escala logarítmica: duas fontes iguais, mais 3 decibéis; ataque a fonte dominante. Poeira: sensores óticos precisam de calibração, e os padrões do CONAMA são do ar ambiente. Telemetria e RTLS dão segurança e produtividade, mas localização de pessoas é dado pessoal. E agora você tem dezenas de sensores gerando milhares de leituras por dia. Como limpar esses dados, como definir alertas que não enlouqueçam a equipe e como montar um painel que leve à decisão? É a última aula da unidade. Te espero na Aula 12!"

---

## Roteiro da Videoaula 12 — "Dados de sensores: séries temporais, níveis de alerta e dashboards"

**Duração-alvo:** cerca de 17:50 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Aqui é o professor Afonso Brandão, e esta é a Aula 12, a última da Unidade 3. Nas três aulas anteriores, a gente instalou sensores no solo, na estrutura e no entorno da obra. Hoje a pergunta é: o que fazer com tanto dado? Séries temporais, níveis de alerta e dashboards."

**[TELA]** Slide 3 — foto: a sala de monitoramento; 37 alarmes, 35 falsos.

> "Segunda-feira, sete da manhã. A obra tem 60 sensores e gera milhares de leituras por dia. No fim de semana, o painel disparou 37 alarmes. Trinta e cinco eram falsos: um pico de rádio, um sensor com a bateria no fim, o sol batendo numa escora. Na terceira semana assim, a equipe fez o que qualquer ser humano faria: parou de olhar. E um dos alarmes era real."

> "Esse fenômeno tem nome: fadiga de alarmes. É conhecido em hospitais, em aviação, em usinas — e chegou aos canteiros com a IoT. Um sistema que grita o tempo todo é tão perigoso quanto um sistema mudo. Hoje você vai aprender a tratar os dados, a desenhar alertas com um plano de ação e a montar painéis que levam à decisão, e não ao cansaço."

### 2. Anatomia de uma leitura (1:40 – 3:10)

**[TELA]** Slide 4 — anatomia de uma leitura.

> "Primeiro, um ponto de uma série temporal não é só um número. Ele precisa de um carimbo de tempo, de preferência em UTC, o tempo universal, com o fuso declarado. Da identificação do sensor. Do valor bruto — em hertz, miliampères, dígitos. Do valor de engenharia, em milímetros ou quilopascals, calculado com a leitura zero e os fatores de calibração. Da unidade. De marcas de qualidade. E de dados de saúde: bateria e intensidade do sinal."

> "E duas regras de ouro. Os fatores de calibração devem ser versionados: se o sensor foi recalibrado em março, você precisa saber qual fator valia em fevereiro. E nunca, jamais, sobrescreva o dado bruto. A correção é sempre uma nova camada, rastreável. Se um dia alguém perguntar 'de onde veio esse número?', você tem que conseguir refazer o caminho. Esses dados vivem em bancos de séries temporais, feitos para gravar e consultar por intervalo de tempo."

> "E quanto dado é isso? Faça a conta comigo. Um piezômetro lido a cada 15 minutos gera 96 leituras por dia. Sessenta sensores assim: quase 6 mil pontos por dia, mais de 2 milhões por ano. E um sismógrafo, durante um evento de vibração, grava centenas de amostras por segundo. Por isso os sistemas maduros guardam o dado bruto completo, mas mostram no painel agregados: médias horárias, máximos diários. E usam a amostragem adaptativa da Aula 3: leitura lenta no normal, rápida quando a atenção é cruzada. Mais dado não é melhor dado. Melhor dado é a leitura certa, no momento certo, nas mãos de quem decide."

### 3. Os cinco defeitos e a limpeza (3:10 – 6:40)

**[TELA]** Slide 5 — cinco defeitos que todo dado de campo tem.

> "Todo dado de campo tem defeito, e são sempre os mesmos cinco. Picos espúrios: um valor isolado e fisicamente impossível, por interferência ou falha de leitura. Lacunas: horas ou dias sem dado, porque a bateria acabou, o rádio caiu ou alguém passou com a retroescavadeira por cima do cabo. Deriva: o sensor anda devagar sem que a grandeza mude — lembra da Aula 2. Ciclos térmicos: a oscilação diária e sazonal que você viu na escora e na fissura, na Aula 10. E carimbo errado ou duplicado: o relógio do datalogger desacertado, confusão de fuso, horário de verão."

**[TELA]** Slide 6 — simulação: limpeza da série. Ligue, em sequência, a mediana, a média móvel e a compensação térmica.

> "Na simulação, 30 dias de recalque, em cinza, do jeito que chegam: com tendência, ciclo diário, ruído, três picos e uma lacuna de dois dias. Eu ligo o filtro de mediana. A mediana de três leituras pega o valor do meio; um pico isolado nunca é o do meio, então ele some — e a tendência fica no lugar. Olha o contador: três picos removidos. Agora a média móvel de 24 horas: a curva fica lisinha. Mas repara no marcador: ela atrasa. Ao suavizar, a média móvel responde a uma aceleração com atraso — quanto maior a janela, maior o atraso. E a compensação térmica usa a temperatura medida junto ao sensor para tirar a parcela do sol."

> "Uma ferramenta a mais, talvez a mais importante: a taxa de variação, a velocidade em milímetros por dia. Um deslocamento pequeno que acelera preocupa mais do que um grande que estabilizou. E um aviso: toda limpeza tem que ficar registrada. Um pico 'removido' pode ser o primeiro sinal de um problema real. O filtro não decide sozinho: ele sinaliza, e alguém olha."

### 4. Exemplo numérico: oito leituras (6:40 – 8:30)

**[TELA]** Slide 7 — exemplo numérico: oito leituras diárias.

> "Vamos ao exemplo. Um marco de recalque automatizado registrou, em oito dias: 4,0; 4,2; 4,3; 4,5; 10,6; 5,2; 5,9 e 6,8 milímetros. O plano diz: atenção em 10 milímetros, alerta em 15, e velocidade de atenção de 0,5 milímetro por dia."

> "O dia 5 salta 6,1 milímetros e volta no dia seguinte. Prédio não sobe 6 milímetros de um dia para o outro: é espúrio. A mediana dos dias 4, 5 e 6 — 4,5, 10,6 e 5,2 — é 5,2. Esse valor entra na série tratada, com a marca 'corrigido', e o bruto fica guardado. E repara: se o sistema exigisse duas leituras seguidas acima de 10, esse pico nem teria disparado o alarme."

> "Agora a média móvel de três dias no dia 8: 5,2 mais 5,9 mais 6,8, dividido por 3, uns 6,0. Abaixo do último valor, de 6,8: é o atraso da média móvel. E a velocidade recente: 6,8 menos 5,2, em dois dias, 0,8 milímetro por dia. Acima dos 0,5 do plano. O valor está longe da atenção, mas a velocidade dispara o amarelo. Guarda esse número."

### 5. TARP e persistência (8:30 – 11:40)

**[TELA]** Slide 8 — níveis de alerta e o plano de ação (TARP).

> "Os limites não podem ficar soltos. Eles se organizam num plano de ação por gatilhos — em inglês, Trigger Action Response Plan, o TARP. Para cada nível, ele diz o que acontece, quem faz e em quanto tempo. Verde, normal: dentro do esperado, leitura na rotina, responsabilidade da equipe de instrumentação. Amarelo, atenção: o valor ou a velocidade passou do nível de atenção; aumenta-se a frequência, inspeciona-se o local e avisa-se o projetista no mesmo dia; quem responde é o engenheiro da obra. Vermelho, alerta: o nível de alerta foi confirmado; executam-se as medidas de contingência que já estavam previstas — reduzir ou paralisar a frente, reforçar —, com reunião técnica imediata entre o engenheiro responsável e o projetista."

> "Repara em duas palavras: 'ou velocidade' e 'confirmado'. Gatilhos por valor e por velocidade. E confirmação: por uma segunda leitura ou por um segundo instrumento."

**[TELA]** Slide 9 — simulação: persistência × atraso. Varie a persistência de 1 a 4 leituras e ligue o gatilho de velocidade.

> "Na simulação, 40 dias de leituras a cada 6 horas, com ruído e picos aleatórios, e um deslocamento real que começa a crescer no dia 25. Com persistência de uma leitura — qualquer leitura acima do limite dispara —, olha a quantidade de alarmes falsos em vermelho antes do dia 25. Isso é a fadiga de alarmes. Agora eu exijo duas leituras seguidas: os falsos quase somem, e o evento real é detectado seis horas mais tarde. Com quatro leituras: zero falso, mas o atraso cresce. É um compromisso, não existe almoço grátis. E a escolha depende da velocidade do fenômeno: se o deslocamento real leva semanas para ficar perigoso, seis ou doze horas de atraso não fazem diferença, e a persistência compensa. Se o fenômeno é rápido — o nível d'água subindo depois de uma chuva forte, por exemplo —, o atraso pode custar caro, e a saída é ler mais vezes ou confirmar com um segundo instrumento, em vez de esperar a próxima leitura do mesmo sensor. Agora eu ligo o gatilho de velocidade: o evento real é pego mais cedo, porque a curva acelera antes de chegar ao limite. Persistência com gatilho de velocidade é a combinação que funciona."

**[TELA]** Slide 10 — calculadora: quanto tempo até o alerta?

> "De volta ao nosso marco. Leitura atual de 6,8, anterior de 5,2, dois dias entre elas: 0,8 milímetro por dia. Até a atenção, de 10: 3,2 milímetros, divididos por 0,8, são 4 dias. Até o alerta, de 15: uns 10,3 dias. A situação na tela: alerta de velocidade, valor abaixo da atenção, mas acelerando. Isso muda tudo na gestão: você não espera chegar a 10 para agir. Você tem quatro dias para vistoriar, conferir a leitura com nivelamento manual e conversar com o projetista."

**[TELA]** Slide 11 — incerteza nos limiares.

> "E não esqueça a incerteza da Aula 2. Se a leitura mais a incerteza expandida alcança o limite, trate como atenção: o limite pode ter sido atingido. Se a leitura menos a incerteza passa do limite, o alerta está confirmado. No nosso exemplo, 6,8 mais ou menos 1,5 fica abaixo de 10: o valor está seguro. Mas é a tendência que manda agir agora. E, antes de confiar em qualquer número, olhe a saúde do sensor: bateria, sinal e hora da última leitura."

### 6. Dashboards (11:40 – 15:00)

**[TELA]** Slide 12 — o que um bom dashboard mostra (e o que esconde).

> "Agora o painel. Um bom dashboard de monitoramento mostra quatro coisas. Uma planta da obra com cada instrumento colorido pelo seu estado: verde, amarelo, vermelho — num relance, você sabe onde olhar. Séries temporais com os limites desenhados e a velocidade. A saúde dos sensores: bateria, hora da última leitura, sinal. E uma lista de alarmes com reconhecimento: quem viu, quando e o que fez."

> "E ele evita quatro armadilhas. Gráfico sem limite: o número sobe, mas sobe até onde? Eixo cortado, que transforma meio milímetro numa montanha. Excesso de cores, que não diz nada. E, a pior de todas, alarme sem dono. O princípio é: cada alerta tem um responsável, um prazo e uma ação."

> "E pense em quem vai olhar. O engenheiro de plantão, às duas da manhã, precisa de uma tela no celular que diga em cinco segundos: está tudo bem, ou não está, e onde. O projetista precisa de séries longas, com a obra sobreposta — que etapa de escavação estava acontecendo quando a curva acelerou? E o cliente, ou o vizinho, precisa de um relatório periódico, claro, com os limites e a interpretação. Um dashboard só não serve a todos. Projete a tela para a decisão de cada um."

**[TELA]** Slide 13 — simulação: o painel. Clique em Simular evento; quando o alarme entrar no log, clique em Reconhecer.

> "Olha o painel simulado. À esquerda, a planta com seis instrumentos: inclinômetro, piezômetro, marco de recalque, sismógrafo, fissurômetro e o sensor de MP10. À direita, as séries do inclinômetro e do piezômetro, ao vivo, com os limites. Embaixo, o log de alarmes e a saúde dos sensores. Eu clico em simular evento: o inclinômetro INC-01 acelera. O ponto na planta fica amarelo, a série se inclina e um alarme novo entra no log, com hora e nível. Agora o engenheiro de plantão clica em reconhecer: o status muda para 'reconhecido', com o nome de quem viu. Isso é rastreabilidade. Se alguém perguntar amanhã 'quem soube e o que fez?', a resposta está ali."

**[TELA]** Slide 14 — cena 3D: do dashboard ao gêmeo digital.

> "E o próximo passo. O dashboard mostra números. O gêmeo digital, que você vai estudar na Unidade 4, põe esses números dentro do modelo da obra e devolve decisões. Na cena, o prédio real e o gêmeo: o recalque aparece no modelo, a cor muda e, em malha fechada, o comando volta para a obra. É a malha fechada da Unidade 1, agora alimentada por tudo o que você instalou nesta unidade."

> "E é aqui que a disciplina inteira começa a se juntar. O drone da Unidade 2 entrega a geometria: ortomosaico, nuvem de pontos, volumes. Os sensores desta unidade entregam o comportamento: deslocamentos, pressões, deformações, vibrações. O gêmeo digital é o lugar onde a geometria e o comportamento se encontram, no tempo certo, para alguém decidir."

### 7. Atividade, pontos-chave, fechamento da unidade e encerramento (15:00 – 17:50)

**[TELA]** Slide 15 — atividade prática.

> "Sua missão: pegue uma série real — dados abertos de uma estação meteorológica servem — ou simule 30 dias de leituras numa planilha, com tendência, ciclo diário, ruído e alguns picos. Aplique a mediana de três, a média móvel e calcule a velocidade. Depois defina níveis de atenção e de alerta, por valor e por velocidade, monte a tabela TARP e esboce três telas de dashboard: a planta com status, as séries com os limites e a lista de alarmes. Dica: teste a sua regra de persistência contando quantos alarmes falsos ela teria gerado. E escreva, ao lado de cada nível do TARP, o nome — ou pelo menos o cargo — de quem responde e o prazo. Se você não conseguir preencher essa coluna, o seu sistema ainda não fecha a malha."

**[TELA]** Slide 16 — pontos-chave.

> "Resumindo. Uma leitura é um registro completo: tempo em UTC, sensor, bruto, engenharia, unidade, qualidade e saúde — e o bruto nunca é sobrescrito. Mediana remove picos; média móvel suaviza, mas atrasa; a velocidade costuma avisar antes do valor. Os níveis de alerta formam um TARP, com gatilho, ação, responsável e prazo; persistência, redundância e incerteza combatem a fadiga de alarmes. E todo alarme tem dono."

**[TELA]** Slide 17 — fechamento da Unidade 3.

> "E, com isso, fechamos a Unidade 3. Na Aula 9, o solo e os vizinhos: inclinômetros, piezômetros, marcos de recalque e distorção angular. Na Aula 10, a estrutura: extensômetros, acelerômetros, fissurômetros e maturidade — e a temperatura como vilã e como informação. Na Aula 11, o entorno e a operação: vibração, ruído, poeira e rastreamento. E hoje, os dados: séries, alertas e painéis."

**[TELA]** Slide 18 — prévia da Unidade 4; Slide 19 — encerramento.

> "Na Unidade 4, drones e sensores finalmente se encontram. Você vai integrar o monitoramento ao BIM e ao gêmeo digital, com o 4D e a comparação entre o que foi construído e o que foi projetado. Vai usar inteligência artificial e visão computacional para detectar fissuras e medir o avanço físico. Vai tratar da gestão do monitoramento: custo-benefício, LGPD, segurança da informação e contratos. E, para fechar, vai desenvolver o projeto integrado de monitoramento de uma obra. Foi um prazer! Te espero lá."
