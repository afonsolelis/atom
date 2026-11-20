# Unidade 4 — Integração, Inteligência e Gestão do Monitoramento

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 13 a 16

## Aula 13 — Integração com BIM e gêmeo digital: 4D e comparação as-built × as-designed

> Reunião mensal de obra. A gerenciadora apresenta: "avanço físico de 62%, conforme o cronograma". O drone voou ontem, a nuvem de pontos está pronta e os sensores enviam leituras a cada 15 minutos — mas cada dado mora num sistema diferente, e ninguém consegue responder a duas perguntas simples: **o que foi construído está onde o projeto mandou?** E **o que foi construído é o que deveria estar pronto nesta data?** Nesta aula, você vai ver como o **BIM** costura drones, sensores e cronograma num único modelo, o que são **4D** e **5D**, como se compara **as-built × as-designed** com tolerância e incerteza e em que ponto o modelo passa a ser, de fato, um **gêmeo digital**.

### O que você verá nesta unidade

Nesta unidade final, tudo o que você estudou se junta em um sistema único. Você vai integrar nuvens de pontos e sensores ao BIM, com planejamento 4D e comparação entre o executado e o projetado (Aula 13); conhecer o que a inteligência artificial e a visão computacional já fazem na obra, como detectar fissuras e medir avanço físico (Aula 14); avaliar custo-benefício, LGPD, segurança da informação e contratos do monitoramento (Aula 15); e montar o projeto integrado de monitoramento de uma obra real (Aula 16). O objetivo é que você seja capaz de propor e defender um plano completo — técnica, econômica e juridicamente. Essa é a competência que o mercado procura: não quem apenas opera um equipamento, mas quem desenha o sistema e responde por ele.

### BIM: o modelo é informação, não desenho

**BIM** (*Building Information Modeling*, modelagem da informação da construção) é o processo de criar e gerir um modelo digital em que cada elemento — pilar, laje, estaca, tirante — é um **objeto com geometria, propriedades e relações**: material, fck, data de concretagem, fornecedor, fase da obra. A diferença para o CAD é essa: no CAD, uma linha é uma linha; no BIM, a linha é um "pilar P12, concreto C35, concretado em 14/03".

Para que modelos de softwares diferentes conversem, existe o **openBIM**, baseado no **IFC** (*Industry Foundation Classes*), esquema aberto mantido pela buildingSMART e normalizado como ISO 16739. Cada objeto IFC tem um identificador global único (**GUID**), e há classes até para instrumentos — o `IfcSensor`. É esse GUID que permite pendurar no modelo uma leitura de sensor, uma foto de drone ou uma pendência.

![Modelo BIM tridimensional de uma edificação térrea em perspectiva isométrica, com cobertura, fachadas, estacionamento, calçadas, árvores e acesso viário modelados como objetos. Imagem: Archdraw, Wikimedia Commons, CC BY-SA 4.0](https://upload.wikimedia.org/wikipedia/commons/d/d0/Architectural_BIM_3D_Modeling.jpg)

### 4D, 5D e as "dimensões" do BIM

Quando cada elemento do modelo é ligado a uma atividade do cronograma, temos o **BIM 4D**: o modelo "cresce" no tempo, e é possível comparar o planejado com o executado. Ligando também quantidades e custos, temos o **BIM 5D** — orçamento, medição e fluxo de caixa extraídos do modelo.

![Quadro colorido com as seis "dimensões" do BIM lado a lado: 1D pesquisa e concepção, 2D desenhos, 3D forma e modelagem, 4D tempo e planejamento, 5D custo e quantitativos e 6D desempenho, cada uma com seus usos listados](https://upload.wikimedia.org/wikipedia/commons/6/68/6_BIM_DIMENSIONS.png)

Cuidado com a numeração além do 5D: 6D e 7D aparecem na literatura ora como sustentabilidade, ora como operação e manutenção. O que importa é o **uso** que se faz do modelo, não o número.

### BIM na administração pública e a ISO 19650

No Brasil, a **Estratégia BIM BR** (Decreto nº 9.983/2019) organiza a disseminação do BIM, e o **Decreto nº 10.306/2020** tornou seu uso obrigatório, em fases, nas obras da administração pública federal abrangidas: desde 2021, nos projetos (modelos das disciplinas, detecção de interferências, quantitativos); desde 2024, também na **execução** — orçamentação, planejamento e controle da obra e **atualização do modelo as-built**; a partir de 2028, também na gestão e manutenção pós-obra. A Lei nº 14.133/2021 (art. 19, § 3º) manda adotar o BIM **preferencialmente** nas licitações de obras e serviços de engenharia, sempre que adequado ao objeto.

A série internacional **ISO 19650** trata da **gestão da informação** com BIM. Seu conceito central é o **ambiente comum de dados** (CDE, *common data environment*): um repositório único em que cada arquivo passa por estados controlados — **em elaboração, compartilhado, publicado e arquivado**. Para o monitoramento, a lição é direta: leitura de sensor e nuvem de pontos também são informação da obra e precisam de dono, versão e estado.

### Realidade capturada: scan-to-BIM e scan-vs-BIM

O drone (fotogrametria ou LiDAR, Unidade 2) e o laser scanner terrestre geram **nuvens de pontos** do que foi construído. Há dois usos bem diferentes:

- **Scan-to-BIM** — modelar a partir da nuvem: criar o **as-built** de uma estrutura existente ou recém-executada.
- **Scan-vs-BIM** — comparar a nuvem com o modelo de projeto (**as-designed**) para responder "está no lugar certo?" e "já foi executado?".

![Nuvem de pontos colorida da fachada de um edifício histórico de dois pavimentos com colunata, gerada por escaneamento a laser, em que cada ponto registra a posição e a cor da superfície](https://upload.wikimedia.org/wikipedia/commons/7/7e/Point_cloud_data_of_the_David_W._Dyer_Federal_Building_and_United_States_Courthouse_in_Florida.jpg)

Antes de comparar, a nuvem precisa estar **registrada** (alinhada) no mesmo sistema de coordenadas do modelo, com pontos de controle. Um erro de registro de 2 cm transforma toda a obra em "fora de posição".

### Comparação as-built × as-designed: desvio, tolerância e incerteza

Na comparação **nuvem-modelo** (*cloud-to-model*), calcula-se a distância de cada ponto à superfície correspondente do modelo e pinta-se o resultado num **mapa de calor**: verde dentro da tolerância, amarelo e vermelho fora dela. A **tolerância** é um valor de projeto, de norma ou de contrato (por exemplo, ±10 mm na posição de um pilar). E aqui volta a Aula 2: o desvio medido tem **incerteza**. A regra de decisão defensável é:

- desvio **+ U** abaixo da tolerância → **conforme**;
- desvio **− U** acima da tolerância → **não conforme**;
- tolerância dentro do intervalo → **inconclusivo**: medir de novo, com método mais exato.

Cada não conformidade vira uma pendência rastreável, presa ao GUID do elemento — no openBIM, isso se faz com o **BCF** (*BIM Collaboration Format*).

### Do modelo ao gêmeo digital

Ligue ao modelo os sensores da Unidade 3: o ID de cada inclinômetro ou piezômetro associado ao GUID do elemento, as leituras chegando pela plataforma IoT e os elementos coloridos pelo nível de alerta. O modelo passa a ser uma **sombra digital**. Quando a decisão volta automaticamente à obra — por exemplo, a plataforma reprograma a frente de escavação no 4D e aciona a equipe —, temos o **gêmeo digital** de Kritzinger *et al.* (2018), da Aula 1. Na prática, o mais comum e útil é a sombra digital com um engenheiro fechando a malha.

### Exemplo numérico

**(a) Posição de um pilar.** A comparação nuvem-modelo do pilar P7 deu desvios de $\Delta x = 12\,\mathrm{mm}$ e $\Delta y = -9\,\mathrm{mm}$ em relação ao eixo de projeto. A incerteza expandida do levantamento (registro + nuvem) é $U = 3\,\mathrm{mm}$ e a tolerância contratual é $10\,\mathrm{mm}$.

$
d = \sqrt{\Delta x^2 + \Delta y^2} = \sqrt{12^2 + (-9)^2} = \sqrt{225} = 15\,\mathrm{mm}
\qquad
d - U = 15 - 3 = 12\,\mathrm{mm} > 10\,\mathrm{mm}
$

Mesmo descontando a incerteza, o desvio supera a tolerância: o pilar está **não conforme**, e a pendência vai para o projetista estrutural avaliar a excentricidade adicional.

**(b) Laje inteira.** Da nuvem de uma laje, $48.000$ pontos foram comparados com o modelo, e $45.600$ ficaram dentro de $\pm 10\,\mathrm{mm}$: $45.600/48.000 = 0{,}95$, ou seja, 95% da superfície conforme. O mapa de calor mostra **onde** estão os 5% restantes.

**(c) Avanço no 4D.** Até a data do voo, o 4D previa $420\,\mathrm{m^3}$ de concreto executado; a nuvem confirma os elementos que somam $378\,\mathrm{m^3}$:

$
I = \frac{378}{420} = 0{,}90
$

O avanço físico medido é 90% do planejado — e o "62% conforme o cronograma" da reunião precisa ser revisto.

### Atividade prática

Pegue a planta de formas de um pavimento-tipo (pode ser de um projeto acadêmico). Escolha 6 pilares e invente, para cada um, desvios $\Delta x$ e $\Delta y$ de uma comparação nuvem-modelo. Com tolerância de 10 mm e $U = 3\,\mathrm{mm}$, classifique cada pilar como conforme, não conforme ou inconclusivo e redija a pendência (formato BCF: elemento, problema, responsável, prazo) do pior caso.

### Pontos-chave

- **BIM** é modelo de **informação**: objetos com geometria, propriedades e relações; o **IFC** (openBIM) e o **GUID** permitem ligar sensores, fotos e pendências a cada elemento.
- **4D** liga o modelo ao cronograma; **5D**, a custos e quantidades. O Decreto nº 10.306/2020 exige, desde 2024, o uso na execução e a atualização **as-built** nas obras federais abrangidas.
- **Scan-to-BIM** modela o existente; **scan-vs-BIM** compara a nuvem registrada com o projeto e mede desvios num mapa de calor.
- Conformidade se decide com **desvio, tolerância e incerteza** juntos; resultado inconclusivo pede nova medição.
- Modelo com dados automáticos do canteiro é **sombra digital**; vira **gêmeo** quando a decisão volta à obra.

### Para saber mais

- **Wikipedia — BIM:** https://pt.wikipedia.org/wiki/BIM
- **Planalto — Decreto nº 10.306/2020 (BIM na administração pública federal):** https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/decreto/D10306.htm
- **MDIC — Estratégia BIM BR:** https://www.gov.br/mdic/pt-br/assuntos/sdic/building-information-modelling-bim
- **Wikipedia — Industry Foundation Classes (IFC):** https://en.wikipedia.org/wiki/Industry_Foundation_Classes

## Aula 13 — Roteiro da Videoaula 13: "A obra real bate com o modelo? BIM, 4D e gêmeo digital"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–3 — capa, sumário e a reunião de obra dos "62%".

> "Reunião de obra: a gerenciadora diz que estamos com 62% de avanço, conforme o cronograma. O drone voou ontem, os sensores mandam leitura a cada 15 minutos, mas cada dado mora num sistema diferente. O que foi construído está onde o projeto mandou? E é o que deveria estar pronto hoje? Hoje o BIM vai costurar tudo isso."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 4–7 — BIM é informação, as dimensões do BIM, BIM na lei e a ISO 19650.

> "BIM não é desenho 3D: é um modelo de informação. Cada pilar é um objeto, com material, data de concretagem e um identificador único, o GUID. O IFC, formato aberto, deixa softwares diferentes conversarem. Ligou o modelo ao cronograma? É 4D. Ligou a custos? 5D. E isso já é lei: o Decreto 10.306 exige, desde 2024, BIM na execução das obras federais abrangidas, inclusive o as-built. A ISO 19650 completa: toda informação mora num ambiente comum de dados, com estados controlados."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 8–12 — o 4D em 3D, a realidade capturada, scan-to-BIM × scan-vs-BIM, o mapa de desvios e o fluxo até a pendência.

> "Olha o 4D: arrasto a semana e o prédio planejado aparece em fantasma, o executado em sólido. Para saber o que foi executado, entra a realidade capturada: a nuvem de pontos do drone ou do laser scanner. Scan-to-BIM é modelar a partir da nuvem; scan-vs-BIM é comparar a nuvem com o projeto. Cada ponto ganha uma distância até o modelo, e o mapa de calor mostra onde está fora da tolerância. Mas lembra da Aula 2: o desvio tem incerteza. Desvio mais incerteza abaixo da tolerância, conforme; desvio menos incerteza acima, não conforme; no meio, inconclusivo."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 13–15 — a calculadora do pilar P7, o gêmeo com sensores e a atividade.

> "O pilar P7: 12 milímetros num eixo, menos 9 no outro. Pitágoras dá 15. Tirando a incerteza de 3, ainda sobram 12, acima da tolerância de 10: não conforme. E o avanço: 378 metros cúbicos medidos contra 420 planejados, 90%. Agora pendure os sensores da Unidade 3 no modelo, pelo GUID, e as leituras pintam os elementos: é a sombra digital. Quando a decisão volta sozinha à obra, é gêmeo."

### 5. Encerramento
**[TELA]** Slides 16–17 — pontos-chave e encerramento.

> "Você viu como o BIM integra cronograma, drone e sensores e como decidir conformidade com tolerância e incerteza. Mas quem vai olhar as 3 mil fotos de fachada que o drone tirou? Na próxima aula, a inteligência artificial entra em campo. Te espero na Aula 14!"

---

## Aula 14 — IA e visão computacional: detecção de fissuras e medição de avanço físico

> O drone inspecionou as quatro fachadas e a estrutura do estacionamento: **3.200 fotos** em alta resolução. Em algum lugar delas há fissuras — algumas inofensivas, outras não. Um inspetor experiente leva dias para revisar tudo, e, cansado, deixa passar coisas na foto 2.800. Um modelo de **inteligência artificial** revisa as 3.200 em minutos. Mas quanto ele erra? Que tipo de erro? E dá para **medir** a largura da fissura na foto? Nesta aula, você vai entender como funciona a visão computacional aplicada à obra, como avaliar um modelo com **precisão, revocação e F1** e onde estão os limites físicos e éticos da técnica.

### Visão computacional: três tarefas

**Visão computacional** é o ramo da IA que extrai informação de imagens. Em obra, três tarefas aparecem o tempo todo:

- **Classificação** — a imagem inteira recebe um rótulo: "tem fissura" ou "não tem".
- **Detecção** — o modelo desenha uma **caixa** em volta de cada objeto: um capacete, um caminhão, uma armadura exposta.
- **Segmentação** — cada **pixel** é rotulado: este pixel é fissura, aquele é concreto. É a tarefa que permite medir comprimento e largura.

![Placa de pare fotografada na rua com duas caixas sobrepostas: em verde, a caixa de referência desenhada por uma pessoa; em vermelho, a caixa prevista por um detector de objetos, quase coincidente](https://upload.wikimedia.org/wikipedia/commons/2/2d/Intersection_over_Union_-_object_detection_bounding_boxes.jpg)

Na detecção, a qualidade de cada caixa se mede pela **IoU** (*Intersection over Union*): a área da interseção entre a caixa prevista e a de referência dividida pela área da união. IoU acima de 0,5 costuma contar como acerto.

### Redes neurais convolucionais (CNN)

O motor dessas tarefas é a **rede neural convolucional** (CNN). Ela aplica, em camadas, pequenos **filtros** que percorrem a imagem: as primeiras camadas respondem a bordas e contrastes; as seguintes, a texturas; as últimas, a padrões como "fissura ramificada". Ninguém programa esses filtros à mão: eles são **aprendidos** a partir de exemplos rotulados — é o **aprendizado supervisionado**. Para segmentação, arquiteturas do tipo codificador-decodificador (como a U-Net) devolvem um mapa do tamanho da imagem com a probabilidade de cada pixel ser fissura.

![Diagrama de uma rede neural convolucional: a imagem de entrada passa por camadas de convolução e agrupamento, que extraem características, é vetorizada e segue para camadas totalmente conectadas, que dão como saída a probabilidade de cada classe. Imagem: Irisbox, Wikimedia Commons, CC BY 4.0](https://upload.wikimedia.org/wikipedia/commons/8/88/Convolutional_Neural_Network.png)

### Treinar um modelo: dados antes de algoritmo

A qualidade do modelo depende sobretudo dos **dados**. O fluxo típico é: coletar imagens representativas (concretos, iluminações, sujeiras e manchas diferentes); **rotular** com especialistas; separar em **treino, validação e teste** — o teste nunca é visto no treino; e aplicar **aumento de dados** (*data augmentation*: girar, espelhar, mudar brilho e contraste) para que o modelo não decore o conjunto. Um modelo que acerta tudo no treino e falha em fotos novas sofreu **sobreajuste** (*overfitting*). É comum partir de uma rede já treinada em milhões de imagens e ajustá-la ao problema (**transferência de aprendizado**). Existem bases públicas, como a de 40.000 recortes de concreto com e sem fissura de Özgenel (2019).

### Avaliar: matriz de confusão, precisão, revocação e F1

Num conjunto de teste, cada imagem cai numa de quatro caixas: **verdadeiro positivo** (VP, fissura detectada), **falso positivo** (FP, mancha tomada por fissura), **falso negativo** (FN, fissura perdida) e **verdadeiro negativo** (VN). Daí saem:

$
P = \frac{VP}{VP + FP}
\qquad
R = \frac{VP}{VP + FN}
\qquad
F_1 = \frac{2\,P\,R}{P + R}
$

**Precisão** ($P$) responde "dos alarmes, quantos eram fissura?"; **revocação** ($R$, *recall*) responde "das fissuras, quantas o modelo achou?". O **F1** é a média harmônica das duas. A **acurácia** engana quando as fissuras são raras, como você verá no exemplo.

O modelo devolve uma probabilidade, e o **limiar** de decisão é escolha do engenheiro: limiar baixo aumenta a revocação e os falsos positivos; limiar alto, o contrário. Em segurança estrutural, **falso negativo custa mais caro** — prefere-se revocação alta e revisão humana dos alarmes.

### Da fissura ao milímetro: o GSD manda

Detectar não é medir. A largura de uma fissura só pode ser medida se ela ocupar **alguns pixels** — na prática, pelo menos 2. O tamanho do pixel no objeto é o **GSD** da Unidade 2:

$
GSD = \frac{S_w \cdot D}{f \cdot W}
$

com $S_w$ a largura do sensor, $D$ a distância ao objeto, $f$ a distância focal e $W$ a largura da imagem em pixels. Os limites de abertura de fissuras da ABNT NBR 6118 para concreto armado vão de 0,2 a 0,4 mm, conforme a classe de agressividade ambiental: medir isso exige GSD submilimétrico. Fissuras finas podem até **aparecer** na foto pelo contraste da sombra, mas sua largura não é confiável — e o fissurômetro da Unidade 3 continua sendo o instrumento de acompanhamento.

### Avanço físico com visão computacional

A mesma técnica mede **avanço**: detectores e segmentadores aplicados ao ortomosaico ou a câmeras fixas reconhecem formas, armaduras, lajes concretadas e alvenaria. Cruzando o resultado com o **BIM 4D** da Aula 13, obtém-se o percentual executado por elemento, sem planilha preenchida à mão. Câmeras com IA também detectam ausência de capacete ou pessoas em área de risco — e aí entram questões de privacidade que a Aula 15 vai tratar.

![Trinca vertical irregular atravessando um muro de contenção de blocos de concreto, do topo até a base, junto à calçada](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Detail_of_vertical_crack_in_concrete_retaining_wall_at_Medway_Park_Sports_Centre%2C_Gillingham%2C_Kent%2C_England.jpg/1280px-Detail_of_vertical_crack_in_concrete_retaining_wall_at_Medway_Park_Sports_Centre%2C_Gillingham%2C_Kent%2C_England.jpg)

A IA faz a **triagem**; a classificação da causa (retração, recalque, corrosão) e a decisão continuam com o engenheiro, que é o responsável técnico.

### Exemplo numérico

**(a) Avaliar o modelo.** Num teste com $1.000$ fotos de fachada, $80$ têm fissura. O modelo acertou $VP = 72$, perdeu $FN = 8$, deu $FP = 48$ alarmes falsos e $VN = 872$.

$
P = \frac{72}{72 + 48} = 0{,}60
\qquad
R = \frac{72}{72 + 8} = 0{,}90
\qquad
F_1 = \frac{2 \times 0{,}60 \times 0{,}90}{0{,}60 + 0{,}90} = 0{,}72
$

A acurácia é $(72 + 872)/1.000 = 0{,}944$ — parece ótima, mas um "modelo" que sempre responde "sem fissura" teria $920/1.000 = 0{,}92$ sem achar nenhuma. A leitura correta: o modelo encontra 90% das fissuras, e 4 em cada 10 alarmes são falsos — aceitável para triagem com revisão humana.

**(b) Dá para medir?** Câmera com $S_w = 13{,}2\,\mathrm{mm}$, $f = 8{,}8\,\mathrm{mm}$ e $W = 5.472\,\mathrm{px}$, a $D = 5\,\mathrm{m}$ da fachada:

$
GSD = \frac{13{,}2 \times 5.000}{8{,}8 \times 5.472} \approx 1{,}37\,\mathrm{mm/px}
$

Uma fissura de $0{,}3\,\mathrm{mm}$ ocupa $0{,}3/1{,}37 \approx 0{,}22$ pixel: impossível medir. Para 2 pixels, seria preciso $GSD \le 0{,}15\,\mathrm{mm/px}$, ou seja, voar a $D = 0{,}15 \times 8{,}8 \times 5.472/13{,}2 \approx 0{,}55\,\mathrm{m}$ — inviável com segurança — ou usar zoom com $f \approx 13{,}2 \times 5.000/(0{,}15 \times 5.472) \approx 80\,\mathrm{mm}$ a 5 m.

### Atividade prática

Uma inspeção com IA em 2.000 fotos de um viaduto tem duas opções de limiar. Limiar 0,5: $VP = 120$, $FP = 30$, $FN = 30$. Limiar 0,3: $VP = 141$, $FP = 94$, $FN = 9$. Calcule $P$, $R$ e $F_1$ das duas, decida qual usar numa inspeção de segurança e estime quantas fotos a equipe terá de revisar em cada caso.

### Pontos-chave

- Visão computacional na obra: **classificação**, **detecção** (caixas, IoU) e **segmentação** (pixel a pixel, permite medir).
- CNNs aprendem filtros a partir de **dados rotulados**; separar treino/validação/teste, usar *data augmentation* e evitar *overfitting*.
- Avalie com **precisão, revocação e F1**, não com acurácia; o **limiar** troca falsos positivos por falsos negativos, e em segurança o falso negativo custa mais.
- Medir largura exige ≥ 2 pixels sobre a fissura: o **GSD** decide se a foto mede ou só detecta.
- IA faz **triagem** e mede avanço junto com o BIM 4D; a decisão e a responsabilidade técnica continuam com o engenheiro.

### Para saber mais

- **Wikipedia — Rede neural convolucional:** https://pt.wikipedia.org/wiki/Rede_neural_convolucional
- **Wikipedia — Precisão e revocação:** https://pt.wikipedia.org/wiki/Precis%C3%A3o_e_revoca%C3%A7%C3%A3o
- **ÖZGENEL, Ç. F. — *Concrete Crack Images for Classification* (Mendeley Data, 40.000 imagens):** https://doi.org/10.17632/5y9wdsg2zt.2
- **CHA, Y.-J. et al. — *Deep Learning-Based Crack Damage Detection Using Convolutional Neural Networks* (2017):** https://doi.org/10.1111/mice.12263

## Aula 14 — Roteiro da Videoaula 14: "Uma câmera que acha fissuras sozinha: até onde vai a IA na obra"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–3 — capa, sumário e as 3.200 fotos de fachada.

> "O drone voltou com 3.200 fotos das fachadas. Em algum lugar delas há fissuras. Um inspetor leva dias, e na foto 2.800 já está cansado. A inteligência artificial revisa tudo em minutos. Mas quanto ela erra, que tipo de erro comete e dá para medir a fissura na foto? É o assunto de hoje."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 4–7 — as três tarefas, a convolução animada, o fluxo de treino e a galeria de inspeção.

> "Visão computacional tem três tarefas: classificar a foto inteira, detectar objetos com uma caixa — e medir a caixa pela IoU — e segmentar pixel a pixel, que é o que permite medir. O motor é a rede neural convolucional: filtros que varrem a imagem e respondem a bordas, texturas e padrões. Ninguém programa os filtros: a rede aprende com fotos rotuladas. Por isso, dado vem antes de algoritmo: coletar, rotular, separar treino, validação e teste, aumentar os dados e vigiar o sobreajuste."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 8–10 — a matriz de confusão, o limiar interativo e falso positivo × falso negativo.

> "Mil fotos, oitenta com fissura. O modelo acertou 72, perdeu 8 e deu 48 alarmes falsos. Precisão: 72 sobre 120, 0,60. Revocação: 72 sobre 80, 0,90. F1, 0,72. E a acurácia de 94% engana: dizer sempre 'sem fissura' daria 92%. Agora mexo no limiar: baixo, acho quase todas as fissuras, com mais alarmes; alto, o contrário. Em segurança, perder uma fissura custa mais caro do que revisar um alarme."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 11–16 — a calculadora de GSD, os limites da NBR 6118, a obra vista do alto, o avanço físico medido pela IA, o humano no laço e a atividade.

> "Detectar não é medir. A 5 metros, essa câmera tem pixel de 1,37 milímetro: uma fissura de 0,3 ocupa um quinto de pixel. Para medir, pelo menos 2 pixels: 0,15 milímetro por pixel, o que pede voar a meio metro ou usar zoom de uns 80 milímetros. A mesma IA mede avanço: reconhece laje, alvenaria, fachada e cruza com o 4D. Mas a IA faz triagem; quem classifica a causa e decide é o engenheiro."

### 5. Encerramento
**[TELA]** Slides 17–18 — pontos-chave e encerramento.

> "Hoje você aprendeu a avaliar uma IA como engenheiro: precisão, revocação, limiar e GSD. Só que tudo isso custa dinheiro, filma pessoas e trafega dados pela internet. Vale a pena? Pode filmar? Está seguro? Quem é dono dos dados? Na próxima aula, a gestão do monitoramento. Te espero na Aula 15!"

---

## Aula 15 — Gestão do monitoramento: custo-benefício, LGPD, segurança da informação e contratos

> O plano de monitoramento está pronto: inclinômetros, piezômetros, voo mensal de drone, câmeras com IA e uma plataforma na nuvem. Na reunião de aprovação, quatro pessoas fazem quatro perguntas. O diretor financeiro: **"vale o que custa?"**. A advogada: **"podemos filmar trabalhadores e a casa do vizinho?"**. O gerente de TI: **"e se alguém invadir o gateway e apagar as leituras?"**. O cliente: **"de quem são esses dados e quem responde se o alerta tocar às 3h?"**. Nesta aula, você vai aprender a responder às quatro — porque um sistema tecnicamente perfeito que não passa por essa reunião não sai do papel.

### Quanto custa monitorar

O custo de um sistema de monitoramento tem duas partes. O **CAPEX** (investimento inicial): instrumentos, instalação, dataloggers, gateway, licenças e o drone. O **OPEX** (custo mensal): conectividade, plataforma, voos e processamento, manutenção e recalibração de sensores e — o item mais esquecido — as **horas de engenheiro** para analisar dados e responder alertas. Um sistema sem orçamento para análise é a malha aberta da Aula 1 com conta de luz.

### Custo-benefício: o valor esperado da perda evitada

O benefício principal do monitoramento é **evitar perdas** — dano ao vizinho, colapso parcial, paralisação, retrabalho. Como elas são incertas, usa-se o **valor esperado**: probabilidade vezes consequência, $VE = p \cdot C$. O monitoramento atua nos dois fatores: reduz a **probabilidade** (o problema é corrigido no início) e a **consequência** (o dano é menor quando detectado cedo). O benefício é a diferença entre o $VE$ sem e com monitoramento, somada a ganhos diretos (medições por drone, menos retrabalho). Os números de probabilidade são estimativas — use faixas e teste a sensibilidade. E há o que não se monetiza: vidas, reputação e a responsabilidade técnica.

### LGPD: dado pessoal no canteiro

A **Lei Geral de Proteção de Dados** (Lei nº 13.709/2018) define dado pessoal como informação relacionada a pessoa natural **identificada ou identificável**. No monitoramento, isso inclui rostos em fotos de drone e câmeras, placas de veículos, o quintal do vizinho, a localização de trabalhadores rastreados e o registro de quem acessou o sistema. **Biometria** (como reconhecimento facial) é **dado sensível** (art. 5º, II), com regras mais restritas (art. 11).

Todo tratamento precisa de uma **base legal** (art. 7º): entre elas, cumprimento de obrigação legal, execução de contrato, proteção da vida e da incolumidade física e **legítimo interesse**. E precisa respeitar os **princípios** do art. 6º, sobretudo **finalidade** (para que serve), **necessidade** (o mínimo de dados) e **transparência** (avisar quem é filmado).

![Placa de aviso amarela e branca presa a um poste, com o desenho de uma câmera e os dizeres em inglês CCTV in operation, isto é, circuito fechado de TV em funcionamento, informando quem passa de que está sendo filmado. Foto: Gerald England, Wikimedia Commons, CC BY-SA 2.0](https://upload.wikimedia.org/wikipedia/commons/6/6f/CCTV_warning_sign_-_geograph.org.uk_-_7528603.jpg)

### Medidas práticas de privacidade

- **Minimização**: enquadrar o voo e as câmeras no canteiro; aplicar **máscara de privacidade** sobre janelas e quintais vizinhos.
- **Desfoque automático** de rostos e placas quando a identificação não é necessária.
- **Retenção definida**: fotos de segurança guardadas por prazo certo e depois descartadas.
- **Aviso** nos acessos e comunicação prévia aos vizinhos.
- Para tratamentos de risco, **relatório de impacto** (RIPD); indicação do **encarregado**; e contrato que defina quem é **controlador** (decide) e quem é **operador** (trata em nome dele).

A fiscalização é da **ANPD**. Incidentes de segurança com risco relevante aos titulares devem ser comunicados à ANPD — o regulamento da autoridade (Resolução CD/ANPD nº 15/2024) fixa, como regra, **três dias úteis** — e as sanções incluem multa de até 2% do faturamento, limitada a R$ 50 milhões por infração (art. 52).

![Câmera de vigilância do tipo domo, com movimento horizontal, vertical e zoom, presa por um braço curvo a um poste de iluminação pública, contra o céu](https://thumb.wikimedia.org/wikipedia/commons/thumb/3/35/Security_Camera-07-PTZ_mounted_on_light_pole.jpg/1280px-Security_Camera-07-PTZ_mounted_on_light_pole.jpg)

### Segurança da informação: o dado de monitoramento também é estrutural

Segurança da informação protege três propriedades: **confidencialidade**, **integridade** e **disponibilidade**. No monitoramento, a mais crítica é a **integridade**: uma leitura adulterada pode esconder um recalque. A referência de gestão é a **ISO/IEC 27001** (sistema de gestão de segurança da informação). Em IoT, os erros clássicos estão na lista do OWASP, que traz em primeiro lugar as **senhas fracas, padrão ou embutidas**. Boas práticas mínimas:

- trocar **credenciais padrão** e usar autenticação forte no gateway e na plataforma;
- **criptografar** o caminho do dado: o LoRaWAN cifra as mensagens com chaves AES-128; o MQTT deve rodar sobre **TLS**;
- **segmentar** a rede do canteiro e dar a cada usuário só o acesso necessário;
- **atualizar firmware**, manter **registro (log)** de acessos e **cópias de segurança** das séries;
- conferir a **integridade** das séries (lacunas, saltos e alterações registradas).

![Corredor de um data center com fileiras de racks de servidores, iluminados por luz azul; é em instalações assim que ficam a plataforma na nuvem e as cópias de segurança das séries de monitoramento. Foto: BalticServers.com, Wikimedia Commons, CC BY-SA 3.0](https://upload.wikimedia.org/wikipedia/commons/5/5d/BalticServers_data_center.jpg)

### Contratos: o monitoramento como obrigação

O plano de monitoramento deve ser **anexo do contrato**, e não um "extra". Cláusulas essenciais: **escopo** (grandezas, instrumentos, posições, frequências); **níveis de alerta e plano de resposta** — quem faz o quê, em quanto tempo, em cada nível (o TARP, *trigger-action-response plan*); **SLA** (*service level agreement*): disponibilidade da plataforma, tempo entre leitura e painel, prazo de reparo de sensor; **propriedade e acesso aos dados**, com entrega em **formatos abertos** (CSV, IFC) no fim da obra; **confidencialidade e LGPD**; e **responsabilidade técnica**, com ART do profissional responsável pelo monitoramento.

### Exemplo numérico

**(a) Custo-benefício.** Monitoramento de uma escavação ao lado de um prédio antigo, por 14 meses: CAPEX de R\$ 180.000 e OPEX de R\$ 12.000/mês.

$
C = 180.000 + 14 \times 12.000 = \mathrm{R\$}\,348.000
$

Sem monitoramento, estima-se probabilidade de dano relevante ao vizinho de 8%, com consequência de R\$ 5,0 milhões; com monitoramento, 2%, e o dano detectado cedo custaria R\$ 2,0 milhões.

$
VE_{sem} = 0{,}08 \times 5.000.000 = \mathrm{R\$}\,400.000
\qquad
VE_{com} = 0{,}02 \times 2.000.000 = \mathrm{R\$}\,40.000
$

Perda evitada: R\$ 360.000. Somando R\$ 90.000 de ganhos diretos (medições por drone, menos retrabalho), o benefício é $B = \mathrm{R\$}\,450.000$ e

$
ROI = \frac{B - C}{C} = \frac{450.000 - 348.000}{348.000} \approx 0{,}293 = 29{,}3\%
$

Valores **ilustrativos**: o método é o que importa, e as probabilidades devem ser testadas em faixas.

**(b) SLA.** Disponibilidade de 99,5% num mês de 30 dias admite $30 \times 24 \times 0{,}005 = 3{,}6\,\mathrm{h}$ fora do ar. Se a escavação crítica exige alerta a qualquer hora, o contrato deve pedir mais disponibilidade **e** uma regra de borda que funcione sem a nuvem (Aula 3).

### Pausa para reflexão (Desafio)

A construtora quer instalar câmeras com **reconhecimento facial** em todos os acessos e com IA que identifica, pelo rosto, quem está sem capacete, para aplicar advertências. O argumento é a segurança do trabalho — legítimo. Mas reconhecimento facial trata **dado biométrico, sensível**; há alternativas menos invasivas (crachá com RFID no acesso, detecção de capacete **sem** identificar a pessoa, com alerta ao encarregado da frente); e trabalhadores podem se sentir vigiados, o que afeta a confiança. **Onde termina a segurança e começa a vigilância?** Considere: a finalidade, a necessidade (dá para atingir o objetivo com menos dados?), a transparência, o prazo de guarda e quem terá acesso às imagens.

### Atividade prática

Para a obra da Aula 16 (ou outra que você escolher), monte uma **ficha de gestão do monitoramento** com: (1) CAPEX e OPEX estimados e o cálculo do valor esperado da perda evitada; (2) inventário de dados pessoais tratados, com base legal e medida de minimização para cada um; (3) cinco controles de segurança da informação; (4) as cláusulas contratuais do monitoramento, com um SLA numérico.

### Pontos-chave

- Custo = **CAPEX + OPEX**, incluindo as horas de análise; benefício = **perda evitada** ($VE = p \cdot C$, sem × com) + ganhos diretos.
- Imagens de obra contêm **dados pessoais**; todo tratamento precisa de **base legal**, finalidade e minimização; biometria é **dado sensível**.
- Em monitoramento, a **integridade** do dado é questão de segurança estrutural: credenciais padrão trocadas, criptografia (TLS, AES-128 no LoRaWAN), segmentação e logs.
- O plano de monitoramento é **anexo contratual**: escopo, níveis e plano de resposta, **SLA**, propriedade dos dados em formato aberto e ART.

### Para saber mais

- **Planalto — Lei nº 13.709/2018 (LGPD):** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **ANPD — Autoridade Nacional de Proteção de Dados:** https://www.gov.br/anpd/pt-br
- **OWASP — Internet of Things Project (IoT Top 10):** https://owasp.org/www-project-internet-of-things/
- **Wikipedia — ISO/IEC 27001:** https://pt.wikipedia.org/wiki/ISO/IEC_27001

## Aula 15 — Roteiro da Videoaula 15: "Vale o investimento? Custos, LGPD e contratos do monitoramento"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–3 — capa, sumário e as quatro perguntas da reunião.

> "O plano de monitoramento está pronto e vai para a reunião de aprovação. O financeiro pergunta se vale o que custa. A advogada, se pode filmar. O pessoal de TI, se alguém pode invadir o gateway. E o cliente, de quem são os dados e quem atende o alerta às 3 da manhã. Hoje você vai aprender a responder às quatro."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 4–6 — CAPEX e OPEX, a calculadora do valor esperado e o que não se monetiza.

> "Custo tem investimento inicial, o CAPEX, e custo mensal, o OPEX — e nele entram as horas de engenheiro para analisar. O benefício é a perda evitada, pelo valor esperado: probabilidade vezes consequência. Sem monitoramento, 8% de chance de um dano de 5 milhões: 400 mil. Com monitoramento, 2% de um dano menor, de 2 milhões: 40 mil. Evitei 360 mil; com 90 mil de ganhos diretos, 450 mil contra 348 mil de custo: retorno de uns 29%. Números ilustrativos — o método é o que vale."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 7–10 — dados pessoais no canteiro, bases legais e princípios, a câmera com máscara de privacidade e a governança.

> "Rosto, placa, quintal do vizinho, localização de trabalhador: tudo isso é dado pessoal. Biometria é dado sensível. Todo tratamento precisa de base legal — obrigação legal, contrato, proteção da vida, legítimo interesse — e de finalidade, necessidade e transparência. Na prática: máscara de privacidade, desfoque de rostos, prazo de guarda e aviso. E governança: controlador, operador, encarregado, relatório de impacto, incidente comunicado à ANPD, em regra, em três dias úteis."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 11–17 — confidencialidade, integridade e disponibilidade; a cadeia IoT com controles; o checklist mínimo; as cláusulas do contrato; a calculadora de SLA; os níveis de resposta e a pausa para reflexão.

> "Na segurança da informação, a propriedade mais crítica aqui é a integridade: leitura adulterada esconde recalque. Troque a senha padrão, criptografe com TLS, segmente a rede, atualize firmware, guarde logs. E o contrato: plano de monitoramento como anexo, níveis de resposta com responsáveis e prazos, SLA, dados em formato aberto e ART. Um SLA de 99,5% admite 3,6 horas fora do ar por mês. E pense: reconhecimento facial para cobrar capacete é segurança ou vigilância?"

### 5. Encerramento
**[TELA]** Slides 18–19 — atividade, pontos-chave e encerramento.

> "Agora você sabe defender o monitoramento na reunião: custo, privacidade, segurança e contrato. Na próxima aula, a última da disciplina, a gente junta tudo num projeto integrado de uma obra real, do primeiro sensor ao último contrato. Te espero na Aula 16!"

---

## Aula 16 — Projeto integrado de monitoramento de uma obra (fechamento da disciplina)

> Lembra do edifício da atividade da Unidade 1? **Dois subsolos**, escavação de 7 m, terreno de 2.400 m², cortina de estacas atirantada, um **sobrado antigo com fundação rasa** a 3 m da divisa, um **prédio de 8 pavimentos** do outro lado, lençol freático a 4 m e rebaixamento por poços. Naquela época, você tinha os fundamentos. Agora tem o drone, os sensores, o BIM, a IA e a gestão. Nesta aula final, vamos projetar o monitoramento do **Residencial Ipê** (nome fictício) de ponta a ponta — e, ao fazer isso, revisar a disciplina inteira.

### Etapa 1 — Riscos e grandezas

Todo plano começa pelos **riscos**, não pelos equipamentos. No Residencial Ipê: recalque e fissuração do sobrado; deslocamento excessivo da cortina; subida do nível d'água e ruptura de fundo; perda de carga em tirantes; vibração durante a execução das estacas; e, do lado da gestão, desvio de prazo e de volumes. Cada risco vira uma **grandeza**: recalque (mm), deslocamento horizontal (mm), nível d'água (m), carga (kN), velocidade de vibração (mm/s), abertura de fissura (mm), volume (m³).

Repare que nem todo risco pede sensor: o desvio de volume se mede com drone; o recalque do sobrado, com topografia de precisão e marcos; a fissura existente, com vistoria e fissurômetro. A pergunta de projeto é sempre a mesma da Aula 1: **o que, se não for medido a tempo, causa dano?** Riscos de consequência alta e evolução rápida pedem leitura automática e plano de resposta; riscos lentos ou de baixa consequência admitem campanhas manuais periódicas.

![Vista do alto de uma grande escavação urbana em Amsterdã, junto à linha férrea da estação central: fundo da cava em terra, contenção por estacas-prancha metálicas, gruas torre e, ao lado, trens, edifícios e o rio. Foto: Fons Heijnsbroek, Wikimedia Commons, CC0](https://upload.wikimedia.org/wikipedia/commons/8/83/2005.04_-_Amsterdam_photo_of_a_overview_of_a_building_pit_Oosterdok_in_Amsterdam%2C_2005%3B_view_over_the_construction_site_near_Central_StationDutch_city_photo_%2B_geotag%2C_Fons_Heijnsbroek%2C_The_Netherlands_%2827440032866%29.jpg)

### Etapa 2 — Plano de instrumentação

| Grandeza | Instrumento | Onde | Frequência normal → em atenção |
| --- | --- | --- | --- |
| Recalque | marcos de recalque + prismas (estação total robótica) | pilares do sobrado e do prédio | diária → a cada 2 h |
| Deslocamento da cortina | inclinômetros + prismas no topo | 4 verticais junto à cortina | diária → a cada 6 h |
| Nível d'água | piezômetros (corda vibrante) | atrás da cortina e entre poços | 15 min → 5 min |
| Carga em tirantes | células de carga | 10% dos tirantes, por nível | horária |
| Vibração | sismógrafo de engenharia | fundação do sobrado | contínua na execução das estacas |
| Fissuras | fissurômetros + vistoria cautelar | trincas existentes do sobrado | diária |

A **vistoria cautelar** dos vizinhos, com fotos datadas, antes de qualquer serviço, é o marco zero de toda discussão futura sobre danos.

### Etapa 3 — Drone

Um voo **mensal** de multirrotor com câmera RGB, a 60 m de altura, gera ortomosaico, MDS e nuvem de pontos para medir **volume escavado** e **avanço**, com pontos de controle ou RTK (Unidade 2). Voos extras inspecionam fachadas e coberturas vizinhas (com térmica, se houver suspeita de infiltração). Regulamentação: RBAC nº 100, SISANT, SARPAS e — por ser mapeamento em faixas sobrepostas — **aerolevantamento** (Unidade 1). Imagens dos vizinhos: máscara de privacidade (Aula 15).

![Edifício alto em construção, com a estrutura de concreto e as fachadas envidraçadas inacabadas nos últimos pavimentos e uma grua torre amarela e vermelha acima, contra o céu azul](https://thumb.wikimedia.org/wikipedia/commons/thumb/9/95/Edif%C3%ADcio_em_constru%C3%A7%C3%A3o.jpg/1280px-Edif%C3%ADcio_em_constru%C3%A7%C3%A3o.jpg)

### Etapa 4 — Arquitetura IoT e plano de resposta

Sensores e dataloggers a bateria enviam por **LoRaWAN** a um gateway com 4G e conexão de reserva; a plataforma na nuvem guarda as séries, aplica filtros e regras e alimenta os painéis (Unidades 1 e 3). A regra crítica do nível d'água roda também **na borda**, para ligar a bomba reserva mesmo sem internet. Os limites viram um **plano de resposta** por cores:

| Nível | Exemplo (topo da cortina) | Resposta | Quem / prazo |
| --- | --- | --- | --- |
| Verde | abaixo de 10 mm | rotina | equipe de monitoramento |
| Amarelo (atenção) | 10 a 14 mm | aumentar frequência, inspecionar, preparar reforço | engenheiro da obra, em 24 h |
| Vermelho (alerta) | acima de 14 mm | parar a escavação na frente, executar reforço | projetista + responsável técnico, imediato |

O dashboard mostra **valor, velocidade e tendência**, não só o último número (Unidade 3).

### Etapa 5 — BIM e gêmeo

O modelo BIM recebe a **posição de cada instrumento** (associada ao GUID dos elementos), o **4D** da escavação e das contenções e, a cada voo, a nuvem de pontos para comparar **as-built × as-designed** (Aula 13). Os elementos são coloridos pelo nível de alerta: é a **sombra digital** da obra, com o engenheiro fechando a malha.

![Nuvem de pontos em tons de cinza de uma casa de máquinas, obtida por escaneamento a laser, com as tubulações modeladas em BIM sobrepostas em azul-turquesa, comparando o modelo com a geometria real. Imagem: Oregon State University, Wikimedia Commons, CC BY-SA 2.0](https://upload.wikimedia.org/wikipedia/commons/2/23/Scan-to-BIM_Mechanical_Room.jpg)

### Etapa 6 — IA

Nas fotos periódicas das fachadas do sobrado, um modelo de visão computacional faz a **triagem** de fissuras novas, regulado para **revocação alta**; o que ele marca, um engenheiro revisa, e as trincas relevantes ganham fissurômetro. No ortomosaico, a IA mede o avanço de escavação e estrutura e alimenta o 4D (Aula 14).

### Etapa 7 — Gestão

Orçamento com CAPEX, OPEX e horas de análise; justificativa por **valor esperado da perda evitada**; inventário de dados pessoais e medidas de minimização; credenciais, criptografia e logs; e o plano de monitoramento como **anexo contratual**, com TARP, SLA, entrega dos dados em formato aberto e ART (Aula 15).

### Exemplo numérico

**(a) Velocidade importa.** O inclinômetro I-2 mostra deslocamento no topo da cortina de $11{,}5\,\mathrm{mm}$ (já em amarelo), subindo $1{,}2\,\mathrm{mm/dia}$. Mantida a tendência, o alerta de $14\,\mathrm{mm}$ chega em

$
t = \frac{14 - 11{,}5}{1{,}2} \approx 2{,}1\,\mathrm{dias}
$

A frequência de leitura passa a cada 6 h e o reforço é preparado **agora**, não quando o vermelho acender.

**(b) Avanço pelo drone.** O voo do mês mediu $3.150\,\mathrm{m^3}$ escavados, contra $3.500\,\mathrm{m^3}$ planejados no 4D: $3.150/3.500 = 0{,}90$, ou seja, 90% do previsto para o mês.

**(c) GSD do voo.** Com a câmera da Aula 14 ($S_w = 13{,}2\,\mathrm{mm}$, $f = 8{,}8\,\mathrm{mm}$, $W = 5.472\,\mathrm{px}$) a 60 m:

$
GSD = \frac{13{,}2 \times 60.000}{8{,}8 \times 5.472} \approx 16{,}4\,\mathrm{mm/px} \approx 1{,}6\,\mathrm{cm/px}
$

Ótimo para volumes; inútil para medir fissura — que fica com o fissurômetro.

**(d) Custo relativo.** Monitoramento de R\$ 420 mil numa obra de R\$ 38 milhões: $420/38.000 \approx 1{,}1\%$ do custo da obra.

### Atividade prática

Escolha uma obra real ou fictícia — uma escavação urbana, um viaduto, uma barragem de rejeitos, um retrofit hospitalar — e entregue um **plano integrado de monitoramento** em até 5 páginas, com as sete etapas desta aula: riscos e grandezas; tabela de instrumentação; plano de voo; arquitetura e plano de resposta por cores; integração BIM; uso de IA com métrica de avaliação; e ficha de gestão (custo, LGPD, segurança, contrato).

### Pontos-chave

- Um plano de monitoramento começa pelos **riscos** e termina numa **resposta**: grandeza → instrumento → frequência → limite → ação → responsável.
- Drone dá **cobertura** (volumes, avanço, inspeção); sensores dão **frequência** (recalque, deslocamento, NA); topografia dá a **referência**.
- **Valor, velocidade e tendência** decidem juntos; o plano de resposta por cores define quem faz o quê e em quanto tempo.
- BIM 4D, nuvem de pontos e IA formam a **sombra digital** da obra; o engenheiro fecha a malha.
- Custo, LGPD, segurança e contrato fazem parte do projeto, e não de um anexo esquecido.

### Para saber mais

- **SACKS, R. et al. — *Construction with digital twin information systems* (2020):** https://doi.org/10.1017/dce.2020.16
- **ANAC — Drones:** https://www.gov.br/anac/pt-br/assuntos/drones
- **SPENCER, B. F. et al. — *Advances in computer vision-based civil infrastructure inspection and monitoring* (2019):** https://doi.org/10.1016/j.eng.2018.11.030

### Encerramento da disciplina

Você começou esta disciplina com uma trinca na garagem do vizinho e uma pergunta: **a obra está como deveria estar?** Ao longo de 16 aulas, aprendeu a responder com método. Na Unidade 1, os fundamentos: por que monitorar, malha fechada, gêmeo digital, incerteza, IoT e regulamentação de drones. Na Unidade 2, o drone em ação: planejamento de voo, fotogrametria, volumes, LiDAR e termografia. Na Unidade 3, os sensores: geotécnicos, estruturais e ambientais, séries temporais e alertas. E nesta unidade, a integração: BIM, IA e gestão.

O fio que amarra tudo é a **malha fechada**: medir, comparar com um limite, decidir, agir e medir de novo. Tecnologia nenhuma substitui o engenheiro que conhece o solo, a estrutura e a obra — mas o engenheiro que domina essa tecnologia decide mais cedo, com mais confiança e com mais gente protegida. É esse profissional que o mercado procura, e é esse profissional que você está pronto para ser.

## Aula 16 — Roteiro da Videoaula 16: "Mão na massa: o plano de monitoramento de uma obra de verdade"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–4 — capa, sumário, o edifício em obra e o caso do Residencial Ipê.

> "Lembra da atividade da Unidade 1? Dois subsolos, escavação de 7 metros, sobrado antigo a 3 metros da divisa, prédio de 8 pavimentos do outro lado, lençol a 4 metros. Naquela época você tinha os fundamentos. Hoje tem tudo. Vamos projetar o monitoramento do Residencial Ipê de ponta a ponta."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 5–8 — o canteiro em 3D, riscos e instrumentos, o voo de drone e a arquitetura em camadas.

> "Primeiro os riscos, depois os equipamentos. Recalque do sobrado, deslocamento da cortina, nível d'água, carga nos tirantes, vibração, prazo. Cada risco vira grandeza e instrumento: marcos e prismas, inclinômetros, piezômetros, células de carga, sismógrafo, fissurômetros — e a vistoria cautelar como marco zero. O drone voa todo mês a 60 metros para volume e avanço, com aerolevantamento em dia. E tudo sobe por LoRaWAN até a nuvem, com a regra crítica também na borda."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 9–12 — a malha da cortina, o plano de resposta por cores, BIM e IA, e o painel integrado.

> "A cortina tem atenção em 10 milímetros e alerta em 14. Em malha fechada, o reforço vem a tempo. O plano de resposta diz quem faz o quê: amarelo, engenheiro da obra em 24 horas; vermelho, para a escavação na frente e reforça. O BIM recebe sensores, 4D e nuvem de pontos; a IA faz a triagem de fissuras do sobrado e mede avanço. E o painel junta tudo, com valor, velocidade e tendência."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 13–15 — a calculadora integrada, a gestão e a jornada da disciplina.

> "Os números: o inclinômetro está em 11,5 e sobe 1,2 por dia, o alerta chega em uns 2 dias — preparar o reforço agora. O drone mediu 90% do volume previsto. A 60 metros, o pixel tem 1,6 centímetro: ótimo para volume, inútil para fissura. E o monitoramento custa cerca de 1,1% da obra, com LGPD, segurança e contrato no pacote."

### 5. Encerramento
**[TELA]** Slides 16–18 — atividade, pontos-chave e encerramento da disciplina.

> "Começamos com uma trinca na garagem do vizinho e uma pergunta: a obra está como deveria estar? Hoje você sabe responder com método. Medir, comparar, decidir, agir e medir de novo. Foi um prazer enorme fazer esta jornada com você. Leve isso para a obra — e boa sorte na carreira!"

---

## Quiz não avaliativo

### Questão 1

Na comparação nuvem-modelo de um pilar, o desvio de posição em relação ao projeto foi de $11\,\mathrm{mm}$, a incerteza expandida do levantamento é $U = 3\,\mathrm{mm}$ e a tolerância contratual é $10\,\mathrm{mm}$. Com base na regra de decisão estudada, assinale a alternativa **correta**:

a) O pilar é não conforme, porque o desvio medido de 11 mm é maior que a tolerância de 10 mm, e a incerteza não altera a decisão.
b) O pilar é conforme, porque, descontada a incerteza, o desvio pode ser de apenas 8 mm, abaixo da tolerância.
c) O resultado é inconclusivo: o intervalo de 8 a 14 mm contém a tolerância, e é preciso medir de novo com método mais exato.
d) O pilar é conforme se o modelo BIM tiver sido exportado em IFC, pois o GUID garante a posição correta do elemento.

**Resposta correta:** c)

**Feedback:** A alternativa (c) está correta: com $d = 11 \pm 3\,\mathrm{mm}$, o desvio pode estar entre 8 e 14 mm. Como $d - U = 8 < 10$, não se pode afirmar a não conformidade; como $d + U = 14 > 10$, também não se pode afirmar a conformidade — o resultado é **inconclusivo** e pede nova medição (por exemplo, com estação total). A (a) ignora a incerteza de medição, que é parte da decisão. A (b) erra ao usar só o limite inferior do intervalo: conformidade exige que **desvio + U** fique abaixo da tolerância. A (d) confunde interoperabilidade (IFC, GUID) com exatidão geométrica: o identificador liga a informação ao elemento, mas não diz nada sobre a posição executada.

### Questão 2

Um modelo de IA para triagem de fissuras em fotos de fachada foi testado em 500 imagens, 50 delas com fissura. Ele acertou 45 fissuras, perdeu 5 e gerou 30 alarmes falsos. Considerando que a triagem será revisada por um engenheiro, assinale a alternativa **correta**:

a) A precisão é 0,90 e a revocação é 0,60; o modelo deve ser descartado porque erra mais da metade dos alarmes.
b) A revocação é 0,90 e a precisão é 0,60; o modelo é adequado para triagem, pois encontra 90% das fissuras e os alarmes falsos são revisados.
c) A acurácia de 93% basta para concluir que o modelo é adequado, e as métricas de precisão e revocação são dispensáveis.
d) O modelo deve usar limiar mais alto para zerar os falsos positivos, já que em segurança estrutural o alarme falso é o erro mais grave.

**Resposta correta:** b)

**Feedback:** A alternativa (b) está correta: $R = 45/(45 + 5) = 0{,}90$ e $P = 45/(45 + 30) = 0{,}60$. Para triagem com revisão humana, a revocação alta é o que importa: perder fissuras (falso negativo) é o erro mais grave, e os 30 alarmes falsos custam apenas tempo de revisão. A (a) inverte as duas métricas. A (c) se apoia na acurácia, $(45 + 420)/500 = 0{,}93$, que engana quando a classe é rara: dizer sempre "sem fissura" já daria 0,90. A (d) inverte a lógica: elevar o limiar reduz os falsos positivos às custas de mais **falsos negativos**, justamente o erro que mais pesa em segurança.

---

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

> _[PENDENTE — aguardando acesso à Biblioteca Virtual]_

- **Nome do livro:** 
- **Capítulo:** 
- **Link de acesso:** 
- **Qual aula o material deverá entrar?** 

### Para mergulhar no assunto (saiba mais)

> Recomendo o webinar **"Digitalização BIM da SE Mirueira II: Scan-to-BIM e Gêmeos Digitais"**, do canal do BIM Fórum Brasil, no YouTube. Ele mostra um caso brasileiro real de captura da realidade de uma subestação de energia, da nuvem de pontos ao modelo BIM e ao gêmeo digital. Assista com o olhar da Aula 13: como a nuvem foi registrada? Que tolerância foi adotada? O modelo resultante é modelo, sombra ou gêmeo digital? Para conferir o enquadramento legal do BIM nas obras públicas, complemente com a página da Estratégia BIM BR, do MDIC.

- **Links:** https://www.youtube.com/watch?v=QFRG0KoirtI · https://www.gov.br/mdic/pt-br/assuntos/sdic/building-information-modelling-bim
- **Qual aula o material deverá entrar?** Aulas 13 e 16

### Podcast (curadoria | até 45 min)

> No episódio 47 do **Podcast Em Construção**, o professor Fabiano Corrêa (USP) e a professora Tatiana Amaral (UFG) discutem as **aplicações dos gêmeos digitais na construção civil** — desafios e oportunidades para engenheiros, arquitetos e gestores. É o fechamento ideal da disciplina: retoma a distinção entre modelo, sombra e gêmeo digital da Aula 1 à luz da integração com BIM, sensores e dados desta unidade. O episódio tem cerca de 49 minutos; para esta curadoria, ouça os **primeiros 45 minutos**.

- **NOME DO PODCAST:** Podcast Em Construção (canal no YouTube)
- **NOME DO EPISÓDIO:** Episódio 47 — Aplicações dos gêmeos digitais na construção civil, com Fabiano Corrêa
- **Link:** https://www.youtube.com/watch?v=ww_-U1D9NFE
- **Qual aula o material deverá entrar?** Aulas 13 e 16

### Artigo científico

> Artigo de revisão, de acesso aberto, sobre **visão computacional na inspeção e no monitoramento de infraestrutura civil**. Os autores organizam o campo em duas frentes — a **inspeção** (identificar componentes e detectar danos como fissuras, com classificação, detecção e segmentação por redes neurais) e o **monitoramento** (medir deslocamentos e deformações a partir de imagens) — e discutem os desafios de dados rotulados, de generalização e de integração com modelos da estrutura. É a fundamentação acadêmica da Aula 14 e da integração de dados da Aula 16.

- **Link:** https://doi.org/10.1016/j.eng.2018.11.030
- **Qual aula o material deverá entrar?** Aulas 14 e 16
- **Referência bibliográfica do artigo no formato ABNT:** SPENCER JR., Billie F.; HOSKERE, Vedhus; NARAZAKI, Yasutaka. Advances in computer vision-based civil infrastructure inspection and monitoring. **Engineering**, v. 5, n. 2, p. 199-222, 2019. DOI: 10.1016/j.eng.2018.11.030.
