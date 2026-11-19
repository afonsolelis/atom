# Roteiros Estendidos (17–19 minutos) — Unidade 2: Drones: Aquisição e Processamento de Dados

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 5 a 8
- **Formato:** roteiro de narração **integral** — o texto em citação (>) é a fala completa. **Esta é a versão a gravar.** Duração-alvo: **17 a 19 minutos** por aula (cerca de 2.150 a 2.550 palavras faladas, a uns 135 palavras/min, já contando as pausas curtas das demonstrações). Os roteiros curtos de `unidade_2.md` são só um guia da sequência.

> **Como usar:** leia as falas em citação na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`), na mesma ordem dos slides. Quando a fala manda clicar, o efeito descrito aparece na tela em poucos segundos; tabelas e listas dos slides **não** são lidas item a item: a fala comenta o essencial e o aluno lê o resto na tela.

---

## Roteiro da Videoaula 5 — "Planejamento de voo: GSD, sobreposição, altura e plano de missão"

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à quinta aula — a primeira da Unidade 2. Na Unidade 1, a gente construiu os fundamentos: por que monitorar, como medir com confiança, como o dado viaja numa arquitetura IoT e o que é preciso para voar legalmente. Agora o drone vai para o ar de verdade. E a primeira coisa que eu quero te mostrar é que o voo de mapeamento começa muito antes da decolagem: começa numa folha de cálculo. Hoje a gente vai fazer as contas do plano de voo — GSD, altura, área de cada foto, sobreposição, espaçamento entre faixas e intervalo entre fotos. E, de quebra, você vai descobrir de onde veio aquela faixa de 100 metros que eu usei na Aula 4."

**[TELA]** Slide 3 — foto aérea de um grande canteiro: "O piloto subiu a 120 m e voltou com 90 fotos".

> "Começo com uma cena. A gerenciadora pede um levantamento do canteiro de 12 hectares 'com resolução de 2 centímetros'. O piloto pensa: quanto mais alto, mais rápido. Sobe a 120 metros, faz o voo e volta com 90 fotos. No escritório, o software não consegue montar o modelo em metade da área. E onde monta, cada pixel cobre mais de 3 centímetros do terreno. O contrato pedia 2. Ninguém errou o voo: o drone fez exatamente o que mandaram. O que deu errado foi o plano. No fim da aula, a gente volta a esse caso e faz o diagnóstico completo, com números."

### 2. O que é planejar um voo de mapeamento (1:30 – 3:00)

**[TELA]** Slide 4 — faixas paralelas, como um cortador de grama: as quatro escolhas do plano.

> "Primeiro, uma distinção. Existe o voo de inspeção, em que o piloto leva o drone até a fachada, até a trinca, e aponta a câmera para o que quer ver. E existe o voo de mapeamento, que é o assunto de hoje. No mapeamento, a missão é automática: o drone percorre faixas paralelas, indo e voltando, como um cortador de grama, e dispara a câmera em intervalos regulares. O objetivo é que cada ponto do terreno apareça em várias fotos, vistas de posições diferentes. Guarde essa frase, porque ela é a matéria-prima da fotogrametria da próxima aula: sem o mesmo ponto em várias fotos, não existe reconstrução 3D."

> "Planejar é fazer quatro escolhas antes de decolar. A resolução: quanto do terreno cabe num pixel. A altura acima do terreno que entrega essa resolução. As sobreposições, frontal e lateral. E o traçado: o polígono, a direção das faixas, a velocidade e o intervalo de disparo. Todo o resto — quantas fotos, quanto tempo de voo, quantas baterias — é consequência dessas quatro escolhas."

### 3. GSD: o tamanho do pixel no terreno (3:00 – 6:00)

**[TELA]** Slide 5 — interativo: o drone, o cone da câmera e o alvo xadrez de 60 cm. Comece em 70 m; quando a fala pedir, leve a altura a 140 m e depois a 30 m.

> "Vamos à primeira grandeza: o GSD, do inglês ground sample distance, a distância de amostragem no solo. É o tamanho, no terreno, de um pixel da imagem. E a fórmula sai de uma semelhança de triângulos entre o sensor da câmera e o terreno: GSD é igual à altura H vezes o tamanho do pixel no sensor, p, dividido pela distância focal, f."

> "A câmera da aula é uma câmera típica de drone de mapeamento: 20 megapixels, 5.472 por 3.648 pixels, pixel de 2,41 micrômetros e distância focal de 8,8 milímetros — um sensor de uma polegada. A 70 metros, o GSD dá 70 vezes 0,00241 dividido por 8,8: 1,92 centímetro. Do lado direito, um alvo xadrez de 60 centímetros, como os alvos de ponto de controle que você vai ver na Aula 6, aparece com uns 31 pixels de lado. Nítido."

> "Agora eu subo o drone para 140 metros. Olha o cone abrindo: a faixa no chão dobra. E olha o alvo: os pixels ficam duas vezes maiores, e as bordas do xadrez ficam borradas. Dobrar a altura dobra o GSD. Note também a linha tracejada: acima de 120 metros, a gente sai da categoria aberta do RBAC 100. Agora desço para 30 metros: o pixel fica com menos de um centímetro, mas a faixa no chão encolhe para uns 45 metros. Voltando para 70."

**[TELA]** Slide 6 — tabela de altura, GSD e largura da foto, e as três consequências.

> "Esta tabela resume o compromisso central do planejamento. Com essa câmera, a 30 metros, GSD de 0,82 centímetro e uma foto de 45 metros de largura. A 70, 1,92 centímetro e 105 metros. A 120, o teto da categoria aberta, 3,29 centímetros e 180 metros. Voar mais alto cobre mais área por foto, mas com pixel maior. Não existe almoço grátis."

> "E daqui saem três consequências práticas. Primeira: dobrar a altura dobra o GSD. Segunda: a exatidão final do levantamento costuma ficar na ordem de 1 a 3 GSD — então, se você quer medir cota com 3 centímetros de exatidão, não adianta voar com GSD de 5. Terceira: um objeto só é identificável se ocupar vários pixels. Uma fissura de 1 milímetro não aparece num GSD de 2 centímetros, por mais nítida que a foto pareça. Para isso, o voo é outro: de inspeção, perto da estrutura."

### 4. A área de cada foto e as sobreposições (6:00 – 9:00)

**[TELA]** Slide 7 — interativo: fotos de 105 × 70 m em faixas e o mapa de quantas fotos veem cada ponto. Comece em 80% e 70%; quando a fala pedir, baixe as duas para 50% e 40%.

> "Se a imagem tem 5.472 por 3.648 pixels, a área que uma foto cobre no terreno — o footprint — é o número de pixels vezes o GSD. A 70 metros: 5.472 vezes 1,92 centímetro dá uns 105 metros, e 3.648 vezes 1,92 dá uns 70. Em geral, o lado maior, de 105 metros, fica perpendicular à direção de voo: é a largura da faixa imageada."

> "Agora, as sobreposições. A frontal é a porcentagem de uma foto que se repete na seguinte, ao longo da faixa. A lateral, a porcentagem que se repete entre faixas vizinhas. Para fotogrametria de obra, os valores usuais são 75 a 80% de frontal e 65 a 75% de lateral. Terreno homogêneo — solo exposto, gramado — ou relevo forte pedem os valores mais altos, porque o software tem mais dificuldade de achar o mesmo ponto em fotos diferentes."

> "Na tela, cada cor diz em quantas fotos aquele ponto aparece. Com 80 e 70%, cada ponto aparece, em média, em umas 16 fotos — é a conta de um sobre o produto das partes que não se repetem: um sobre 0,2 vezes 0,3. Agora olha o que acontece se eu economizo: baixo para 50% de frontal e 40% de lateral. O mapa vira amarelo e laranja: a média cai para umas 3 fotos, e há faixas inteiras de pontos vistos em apenas duas. Com uma foto, não tem interseção nenhuma; com duas, qualquer erro passa despercebido, e basta uma foto ruim para abrir um buraco. É assim que nascem os buracos do modelo. Volto para 80 e 70."

**[TELA]** Slide 8 — ficha histórica "Overlap photographs", do Arquivo Nacional dos EUA.

> "E esta conta não é novidade. Esta ficha, do início do século passado, já relacionava altura de voo, intervalo entre as fotos e área coberta, para garantir a sobreposição na fotografia aérea feita de avião. Hoje o software do drone faz a conta sozinho, mas a lógica é a mesma. A base, B, que é a distância entre duas fotos consecutivas, é o comprimento L da foto vezes um menos a sobreposição frontal. O espaçamento entre faixas, d, é a largura W vezes um menos a sobreposição lateral — e esse é o mesmo d da fórmula de área por voo da Aula 4. E o intervalo entre disparos é a base dividida pela velocidade. Esse intervalo precisa ser maior que o tempo mínimo que a câmera leva para gravar uma foto; se não for, a câmera perde disparos."

### 5. Altura sobre o terreno, não sobre a decolagem (9:00 – 10:45)

**[TELA]** Slide 9 — cena 3D: o canteiro de 400 × 300 m com um morro de 20 m. Deixe o drone passar sobre o morro (o retângulo da foto fica vermelho) e, quando a fala pedir, clique em Acompanhar relevo.

> "Agora, uma armadilha clássica. O H da fórmula é a altura acima do terreno fotografado, não acima do ponto de decolagem. Olha a cena: o canteiro tem um morro de 20 metros. O drone voa a 70 metros da cota de decolagem. Na parte plana, tudo certo: foto de 70 por 105 metros, sobreposição lateral de 70%. Mas, quando ele passa sobre o morro, ali ele está a 50 metros do chão. O GSD até melhora, mas a foto encolhe para 75 metros de largura. E como as faixas continuam a 31,5 metros umas das outras, a sobreposição lateral cai para um menos 31,5 sobre 75: 58%. Abaixo do recomendado. Repara que o retângulo fica vermelho exatamente em cima do morro — e é exatamente ali que aparecem os buracos no modelo."

> "Solução? Eu clico em Acompanhar relevo. O drone passa a manter 70 metros acima do terreno, usando um modelo de elevação: sobe junto com o morro, e a foto mantém o mesmo tamanho. Isso se chama terrain follow. A alternativa, quando o software não tem essa função, é planejar o espaçamento pela cota mais alta. E, em qualquer caso, respeitando o teto de 120 metros acima do solo."

### 6. Velocidade, obturador e arrasto (10:45 – 12:00)

**[TELA]** Slide 10 — calculadora do arrasto: comece em 6 m/s e 1/1.000 s; depois leve a velocidade a 15 m/s e a exposição a 1/250 s.

> "Mais um detalhe que separa um voo amador de um voo de engenharia. Durante a exposição, o drone anda. O arrasto, o motion blur, é a velocidade vezes o tempo de exposição. Com 6 metros por segundo e exposição de um milésimo de segundo, o drone anda 6 milímetros: uns 0,31 pixel com o GSD de 1,92 centímetro. A regra prática é manter o arrasto abaixo de meio pixel. Agora, se eu acelero para 15 metros por segundo e o dia está nublado, com exposição de 1/250: o arrasto passa de 3 pixels. Foto borrada, modelo ruim."

> "E tem o tipo de obturador. O mecânico, ou global, expõe o quadro inteiro ao mesmo tempo. O eletrônico, o rolling shutter, lê as linhas em sequência; com o drone em movimento, a imagem sai levemente 'torta'. Com esse tipo de câmera, ou se reduz a velocidade, ou o software precisa modelar esse efeito."

### 7. O plano de missão e o aerolevantamento (12:00 – 13:40)

**[TELA]** Slide 11 — tela do Mission Planner, com a imagem de satélite de São Carlos (SP).

> "Juntando tudo, o plano de missão de um mapeamento registra: o polígono da área, com margem além do limite da obra, porque as bordas têm menos sobreposição; a altura e o GSD; as sobreposições; a direção das faixas, em geral paralelas ao lado maior do terreno, para reduzir curvas; a velocidade e o intervalo de disparo; as baterias e os pontos de troca; decolagem e pouso; e as condições meteorológicas aceitáveis — vento, chuva e sol baixo, que gera sombras longas. Na tela, o Mission Planner, um software livre; há também o QGroundControl e os aplicativos dos fabricantes. Eles fazem todas essas contas a partir de poucos parâmetros. Mas quem responde pelo plano é o engenheiro."

**[TELA]** Slide 12 — faixas sobrepostas = aerolevantamento: Ministério da Defesa, SARPAS e RBAC nº 100.

> "E o plano encontra a regulamentação da Aula 4. Voo em faixas sobrepostas para gerar ortomosaico ou modelo do terreno é aerolevantamento: executado por entidade inscrita no Ministério da Defesa, com pedido no SARPAS feito com 4 dias corridos de antecedência. Áreas pequenas podem ficar pré-autorizadas, desde que atendidas as condições cumulativas da portaria. E vale tudo da categoria aberta: até 120 metros, em linha de visada, longe de pessoas não envolvidas e não anuentes. Por isso eu digo que o plano é documento de engenharia: ele justifica o GSD contratado, prova que a altura respeita o teto e entra no pedido de aerolevantamento."

### 8. Exemplo numérico: o canteiro de 12 ha (13:40 – 16:40)

**[TELA]** Slide 13 — calculadora do plano para o canteiro de 400 × 300 m; comece em 70 m, 80%, 70% e 6 m/s; quando a fala pedir, leve a altura a 90 m.

> "Agora, a conta completa. O contrato pede GSD de no máximo 2 centímetros. Qual a altura máxima? Basta inverter a fórmula: altura máxima é GSD vezes f sobre p: 0,02 vezes 8,8 dividido por 0,00241. Dá uns 73 metros. Eu adoto 70, com uma pequena folga para o relevo. GSD: 1,92 centímetro — atende. Footprint: 105 por 70 metros. Com 80% de frontal, a base é 70 vezes 0,2: 14 metros. Com 70% de lateral, o espaçamento entre faixas é 105 vezes 0,3: 31,5 metros. A 6 metros por segundo, uma foto a cada 14 dividido por 6: 2,3 segundos."

> "O canteiro de 12 hectares da Aula 1 tem 400 por 300 metros. Com as faixas ao longo dos 400 metros: 300 dividido por 31,5 dá 9,5; arredonda para 10 e soma uma faixa, para cobrir as duas bordas: 11 faixas. Em cada faixa, 400 dividido por 14 dá 28,6; arredonda para 29 e soma uma: 30 fotos. Total: 11 vezes 30, 330 fotos. O percurso: 11 faixas de 400 metros mais 10 trechos de 31,5 entre elas, 4.715 metros. A 6 metros por segundo, 13,1 minutos. Cabe numa bateria de 21 minutos úteis, com folga."

> "Olha o que acontece se alguém sobe para 90 metros para 'ganhar tempo': o voo cai para uns 11 minutos, mas o GSD passa de 2 centímetros e o contrato deixa de ser atendido. A calculadora mostra na hora."

**[TELA]** Slide 14 — os resultados: 105 m, 31,5 m, 14 m, 330 fotos e 13,1 min; o arrasto e o morro.

> "Repare no primeiro número: 105 metros de largura de foto. É a faixa de cerca de 100 metros que eu usei na Aula 4, quando calculamos a área por voo. Agora você sabe de onde ela veio: de uma câmera de uma polegada voando a uns 70 metros. E a conta da Aula 4 fecha: 6 metros por segundo, vezes 1.260 segundos úteis, vezes 31,5 metros, dá uns 23,8 hectares por bateria. O arrasto, a um milésimo de segundo, é de 0,31 pixel: aceitável. E, no morro de 20 metros, a sobreposição lateral cai para 58%: por isso, nesse canteiro, o voo deve acompanhar o relevo."

**[TELA]** Slide 15 — de volta ao gancho: por que o voo a 120 m falhou.

> "E agora o diagnóstico do gancho. Resolução: a 120 metros, o GSD é 120 vezes 0,00241 dividido por 8,8 — uns 3,29 centímetros. O contrato pedia 2; o limite era 73 metros. Sobreposição: a 120 metros, cada foto cobre 180 por 120 metros. Mesmo assim, com 80 e 70% de sobreposição seriam umas 126 fotos para os 12 hectares. Com 90, a sobreposição foi menor que a necessária — e vieram os buracos. E o plano: sem margem nas bordas, sem conferir o relevo e sem registrar o GSD exigido, não havia como auditar nada. 'Quanto mais alto, mais rápido' não é critério de engenharia. A ordem certa está na tela: GSD exigido, altura máxima, footprint, sobreposições, base e espaçamento, e só então fotos, tempo e baterias."

### 9. Atividade prática, pontos-chave e encerramento (16:40 – 18:00)

**[TELA]** Slide 16 — ortofoto de uma obra ferroviária na Alemanha: "Centenas de fotos bem sobrepostas viram um mapa".

> "Quando o plano é bem feito, o resultado é este: uma ortofoto, uma imagem com escala constante, onde dá para medir. Ela só existe porque cada ponto do terreno foi fotografado várias vezes, de posições diferentes, com GSD controlado."

**[TELA]** Slide 17 — Atividade prática e pontos-chave.

> "Sua missão: escolha a câmera de um drone real — procure a ficha técnica, com o número de pixels, o tamanho do sensor e a distância focal — e uma obra que você conhece. Calcule a altura para GSD de 2 e de 5 centímetros, o footprint, a base e o espaçamento com 80 e 70%, o número de fotos e o tempo de voo a 6 metros por segundo. Depois, desenhe o polígono e as faixas num software gratuito de planejamento e compare com as suas contas. Para levar: GSD é H vezes p sobre f, com H acima do terreno; base e espaçamento saem do footprint e das sobreposições; relevo rouba sobreposição; arrasto abaixo de meio pixel; e o plano é documento de engenharia."

**[TELA]** Slide 18 — encerramento: "Plano pronto, drone no ar".

> "Plano pronto, drone no ar, 330 fotos no cartão de memória. E agora? Como essas fotos viram um modelo 3D? E, mais importante: como provar que esse modelo está no lugar certo, com a exatidão que o contrato exige? Na próxima aula, a gente entra na fotogrametria: Structure from Motion, pontos de controle, RTK, PPK e precisão. Te espero na Aula 6!"

---

## Roteiro da Videoaula 6 — "Fotogrametria com drones: SfM, pontos de controle, RTK/PPK e precisão"

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à sexta aula. Na aula passada, a gente fez o plano de voo do canteiro de 12 hectares: 70 metros de altura, GSD de 1,92 centímetro, 80% de sobreposição frontal, 70% lateral, 11 faixas e umas 330 fotos, tudo numa bateria. O drone pousou, o cartão de memória está cheio. E agora? Como é que 330 fotos viram um modelo 3D em que eu posso medir uma cota, uma distância, um volume? E, principalmente: como eu sei que essas medidas estão certas? É disso que a gente vai falar hoje."

**[TELA]** Slide 3 — foto do topógrafo com o receptor GNSS: "18 cm de diferença na cota de um marco".

> "Começo com uma cena que acontece muito. O modelo 3D do canteiro ficou lindo. Texturas nítidas, dá para ler a placa da obra, os prédios vizinhos perfeitos. Todo mundo na reunião adorou. Aí o topógrafo vai a campo com o receptor GNSS, igual ao da foto, e confere um marco de concreto no meio do terreno. Diferença na cota: 18 centímetros. E a pergunta é: o modelo está certo ou errado? A resposta é a palavra da Aula 2: ele é preciso, mas não é exato. Tudo dentro dele é coerente — as distâncias entre os objetos batem —, mas o conjunto está deslocado e levemente embarrigado. Hoje você vai entender como as fotos viram 3D, por que isso acontece e, o mais importante, como provar com números que um levantamento está bom."

### 2. O princípio: interseção de raios (1:30 – 3:30)

**[TELA]** Slide 4 — interativo: câmeras no alto e raios até um ponto do terreno.

> "Fotogrametria é a ciência de tirar medidas de fotografias. E o princípio é muito simples. Cada pixel de uma foto define um raio: uma reta que sai do centro da câmera e passa pelo ponto do terreno que aquele pixel enxerga. Uma foto só não basta, porque o ponto pode estar em qualquer lugar ao longo do raio. Mas se o mesmo ponto aparece em duas, três, quatro fotos, tiradas de posições diferentes, os raios se cruzam no espaço. E o cruzamento é o ponto em 3D. A matemática que liga o ponto do terreno, o centro da câmera e o pixel na imagem são as equações de colinearidade."

> "Olha na tela: quatro câmeras ao longo da rota de voo, a 70 metros, e os quatro raios se encontrando no ponto verde, o ponto verdadeiro. Agora eu coloco erro na posição das câmeras, 60 centímetros, com erro aleatório. Os raios já não se encontram num ponto só, e o ponto calculado, o círculo vermelho, foge do verdadeiro. Agora eu mudo para erro sistemático: todas as câmeras deslocadas para o mesmo lado. Olha que interessante: os raios voltam a se cruzar direitinho, dispersão zero, só que num lugar errado. Preciso, mas inexato. É exatamente o modelo do gancho."

> "E é por isso que a gente brigou tanto pela sobreposição na aula passada: sem que cada ponto apareça em várias fotos, não existe interseção."

### 3. Structure from Motion (3:30 – 6:00)

**[TELA]** Slide 5 — os 4 passos do SfM.

> "Na fotogrametria clássica, de avião, a posição e a orientação das câmeras eram muito bem conhecidas. Nos drones, o processamento usa uma técnica chamada Structure from Motion, SfM, 'estrutura a partir do movimento'. Ela resolve ao mesmo tempo onde estavam as câmeras e qual é a forma do terreno. São quatro passos."

> "Primeiro, detectar. Em cada foto, o algoritmo encontra milhares de feições distintivas — cantos, texturas, manchas — e descreve cada uma com uma espécie de assinatura, como no método SIFT. Segundo, corresponder: reconhecer a mesma feição em fotos diferentes. Esses são os pontos homólogos. Terceiro, ajustar: um ajustamento por feixes, o bundle adjustment, que é um grande ajuste de mínimos quadrados. Ele calcula, de uma vez, a posição e a orientação de cada foto, os parâmetros da câmera — distância focal, distorção da lente — e as coordenadas dos pontos homólogos. O resultado é a nuvem esparsa. E quarto, densificar: com as câmeras orientadas, o software procura correspondências pixel a pixel e gera a nuvem densa, que é a matéria-prima de todos os produtos da Aula 7."

**[TELA]** Slide 6 — interativo: as etapas do SfM com duas fotos; clique em cada etapa quando a fala pedir.

> "Vamos ver isso acontecendo. Etapa 1: duas fotos do mesmo galpão e da mesma pilha, e as feições aparecendo em azul. Etapa 2: as linhas verdes ligam as correspondências. Repare nas linhas vermelhas tracejadas: são correspondências erradas, um canto confundido com outro. O algoritmo as descarta, porque elas não combinam com a geometria das outras. Etapa 3: as câmeras orientadas lá em cima e a nuvem esparsa em amarelo, já mostrando o galpão e a pilha em corte. Etapa 4: a nuvem densa, milhares de pontos com cor. Na vida real são centenas de fotos e milhares de feições por foto, mas a lógica é essa."

**[TELA]** Slide 7 — onde a correspondência tropeça.

> "E onde o SfM tropeça? Em três situações. Superfícies sem textura: água, telhado metálico liso, uma laje de concreto novinha e uniforme. Não há feição para reconhecer, e o modelo fica com buracos ou ruído. Objetos em movimento: a escavadeira mudou de lugar entre uma foto e outra, e a superfície vira um fantasma. E vegetação densa: a câmera só vê a copa, então o modelo representa a superfície das árvores, e não o chão. A resposta parcial para isso é o LiDAR, da Aula 8. Dica de campo: voe com as máquinas paradas na área que importa e aumente a sobreposição em solo homogêneo."

### 4. Escala, georreferenciamento e o efeito de domo (6:00 – 8:30)

**[TELA]** Slide 8 — o SfM puro reconstrói a forma, mas não sabe onde ela está.

> "Agora vem o ponto central da aula. Só com as fotos, o SfM reconstrói a forma. Mas ele não sabe onde essa forma está no mundo nem qual é o tamanho dela. O GNSS comum do drone ajuda, mas tem exatidão de metros. Resultado: o modelo pode estar deslocado de metros. E pior: pode sofrer o efeito de domo, o doming. Pequenos erros na calibração da lente, que o ajustamento não consegue separar da forma do terreno, fazem o modelo se curvar, como uma tigela virada. Esse efeito é típico de blocos com fotos todas verticais e paralelas, exatamente o voo em faixas que a gente planejou, e foi bem descrito por James e Robson, num artigo de 2014 que está na lista de leituras."

> "Para amarrar o modelo, existem dois caminhos: medir pontos no terreno, ou conhecer com exatidão a posição de cada foto. E, contra o domo, duas armas: pontos de controle bem distribuídos e algumas fotos oblíquas, inclinadas."

**[TELA]** Slide 9 — cena 3D: terreno real × modelo; troque o cenário quando a fala pedir.

> "Olha em 3D. A superfície marrom é o terreno real, medido pela topografia. A malha azul é o modelo fotogramétrico. Os desvios verticais estão exagerados 60 vezes, para a gente enxergar. No cenário sem pontos de controle, a malha está acima do terreno e curvada para cima no centro: no marco central, 18 centímetros, nos cantos, 8. É o nosso gancho. Agora eu clico em 'Com GCP': aparecem os alvos laranja, e a malha desce e se aproxima do terreno; sobra um domo pequeno, de poucos centímetros. E em 'GCP mais oblíquas': as fotos inclinadas travam a calibração da lente e o domo praticamente some. Valores ilustrativos, mas o comportamento é exatamente esse."

### 5. Pontos de controle e de verificação (8:30 – 10:30)

**[TELA]** Slide 10 — foto do alvo de controle na Islândia: "Um grupo amarra, o outro prova".

> "Então vamos aos pontos de controle, os GCPs, do inglês ground control points. São alvos bem visíveis nas fotos — placas em xadrez, cruzes pintadas no chão, como esse alvo laranja e branco da foto — cujas coordenadas são medidas em campo com GNSS RTK ou com estação total. Eles entram no ajustamento e amarram o modelo ao sistema de referência, que no Brasil é o SIRGAS2000."

> "E existe um segundo grupo, que muita gente esquece: os pontos de verificação, os checkpoints. São medidos exatamente do mesmo jeito, mas não entram no processamento. Servem só para conferir. Por quê? Porque se eu uso os mesmos pontos para ajustar e para verificar, o modelo vai passar direitinho por eles, e eu não aprendo nada. É o aluno corrigindo a própria prova."

**[TELA]** Slide 11 — interativo: distribuição dos GCPs e o mapa de erro; troque a distribuição quando a fala pedir.

> "E onde colocar os GCPs? Olha o mapa de 20 hectares. A cor mostra o erro vertical esperado: o modelo fica bem amarrado perto dos GCPs e solto longe deles. Esse modelo de erro é ilustrativo, só para comparar. Com quatro GCPs só nos cantos, o centro fica vermelho: o checkpoint do meio lê quase 19 centímetros. Concentrados num lado, o lado oposto fica solto. Agora, seis pontos no perímetro e no interior: tudo verde, o pior checkpoint abaixo de 5 centímetros. A regra: GCPs no perímetro e no interior, cobrindo também os pontos altos e baixos, e checkpoints independentes, espalhados pela área."

### 6. RTK e PPK (10:30 – 12:45)

**[TELA]** Slide 12 — RTK × PPK.

> "O segundo caminho é saber, com exatidão, onde estava cada foto. Com RTK, o drone recebe durante o voo correções de uma base GNSS — pode ser uma base própria, montada no canteiro, ou uma rede de estações, pela internet, com o protocolo NTRIP. Cada foto sai com posição de poucos centímetros. A limitação: depende do enlace de rádio ou de internet funcionando durante o voo."

> "No PPK, o drone só grava os dados brutos de GNSS, e a correção é feita depois do voo, no escritório, com os dados de uma base. E aqui tem um recurso brasileiro importante: as estações da RBMC, a Rede Brasileira de Monitoramento Contínuo do IBGE. O PPK não depende de enlace nenhum durante o voo. E guarde a frase da tela: RTK e PPK reduzem a necessidade de GCPs. Não dispensam os pontos de verificação. Sempre confira."

**[TELA]** Slide 13 — calculadora: sincronismo da foto e braço de alavanca.

> "Dois cuidados que separam o RTK que funciona do RTK que engana. O primeiro é o sincronismo. A posição do GNSS tem que ser a do instante exato em que a foto foi tirada. Se houver um atraso de 20 milissegundos entre o disparo e o registro, a 6 metros por segundo, a foto fica deslocada 6 vezes 0,020: 0,12 metro, 12 centímetros. Na calculadora, isso dá mais de 6 vezes o nosso GSD. Se eu reduzo o atraso para 2 milissegundos, cai para pouco mais de 1 centímetro. O segundo cuidado é o braço de alavanca: a antena GNSS fica em cima do drone e a câmera, embaixo. Essa distância precisa ser conhecida e considerada no processamento."

### 7. Como se expressa a exatidão (12:45 – 14:15)

**[TELA]** Slide 14 — RMSE, ASPRS e PEC-PCD.

> "E como se diz, com números, que um levantamento é bom? Pelo RMSE, a raiz do erro médio quadrático, calculado nos checkpoints. Para cada ponto, eu faço modelo menos campo, elevo ao quadrado, tiro a média e a raiz. Na horizontal, combino o RMSE em x e em y: raiz de x ao quadrado mais y ao quadrado."

> "Existem padrões para isso. O americano, da ASPRS, na segunda edição, de 2023, passou a reportar a exatidão pelo próprio RMSE, deixando de usar o nível de 95% como medida principal, e exige no mínimo 30 checkpoints para a avaliação completa de um produto. No Brasil, produtos cartográficos são classificados pelo PEC-PCD, o Padrão de Exatidão Cartográfica dos Produtos Cartográficos Digitais, com base num decreto de 1984 e na especificação técnica do Exército. E como ordem de grandeza: um bom levantamento com drone chega a 1 a 2 GSD na horizontal e 1,5 a 3 GSD na vertical. A vertical é sempre a mais difícil."

### 8. Exemplo numérico (14:15 – 16:40)

**[TELA]** Slide 15 — tabela dos cinco checkpoints.

> "Vamos ao exemplo. O voo da Aula 5, GSD de 1,92 centímetro, com RTK e 6 GCPs, foi conferido em 5 checkpoints independentes. Na tabela, os resíduos em centímetros. Em x: mais 1,2; menos 0,9; mais 2,0; menos 1,1; mais 0,6. Os quadrados somam 7,82; dividido por 5 e tirada a raiz, RMSE em x de 1,25 centímetro. Em y, da mesma forma, 1,13. Na horizontal: raiz de 1,25 ao quadrado mais 1,13 ao quadrado, 1,69 centímetro, cerca de 0,9 GSD. Na vertical, os quadrados somam 32,65; dividido por 5, 6,53; raiz: 2,56 centímetros, cerca de 1,3 GSD."

> "E tem um número que pouca gente olha: a média dos resíduos verticais, mais 0,34 centímetro. Praticamente zero. Isso quer dizer que não há viés relevante: os erros vão para cima e para baixo e se compensam. Se a especificação da obra pede RMSE vertical de até 5 centímetros para cálculo de volume, o levantamento atende. Com uma ressalva honesta: 5 checkpoints bastam para o controle de rotina de uma obra pequena, mas são poucos para declarar conformidade com o padrão ASPRS completo, que pede 30."

**[TELA]** Slide 16 — interativo: o que um viés faz com o RMSE; leve o viés a 18 cm quando a fala pedir.

> "Agora olha o que acontece quando existe viés. Na tela, os cinco resíduos verticais e a faixa de mais ou menos 5 centímetros. Eu somo um viés a todos os pontos, como se o modelo inteiro subisse. Com 3 centímetros, a média vai para 3,34 e o RMSE já passa de 4. Agora eu levo o viés a 18 centímetros, o do gancho: todas as barras vermelhas, média de 18,34, RMSE de 18,5 centímetros. Reprovado. E o modelo continua lindo! Guarde isso: o RMSE soma a dispersão e o viés, e é a média dos resíduos que denuncia o viés. Na próxima aula, você vai ver que, para volume, o viés é o pior inimigo."

### 9. Atividade, síntese e prévia da Aula 7 (16:40 – 18:00)

**[TELA]** Slide 17 — atividade prática e pontos-chave.

> "Sua missão: num levantamento de 20 hectares, desenhe onde ficariam 6 GCPs e 5 checkpoints, justificando a distribuição. Depois, com os resíduos verticais de mais 4, mais 5, mais 3, mais 6 e mais 4 centímetros, calcule o RMSE vertical e a média. O que a média revela? E que causa você investigaria primeiro? Uma dica: lembre do sincronismo e da altura da antena."

> "Resumindo: a fotogrametria funciona por interseção de raios; o SfM detecta, corresponde, ajusta e densifica; sem amarração, o modelo pode ser preciso e inexato, com domo; GCPs amarram, checkpoints provam; RTK e PPK reduzem os GCPs, mas não os checkpoints; e a exatidão se expressa pelo RMSE."

**[TELA]** Slide 18 — da nuvem densa aos produtos da obra.

> "Com o modelo amarrado e a exatidão provada, a nuvem densa vira produto de engenharia. Na próxima aula, a gente gera o ortomosaico, os modelos de superfície e de terreno, a nuvem de pontos, e calcula volumes de corte e aterro — e vai ver quanto um viés de poucos centímetros custa numa medição de terraplenagem."

**[TELA]** Slide 19 — encerramento.

> "Modelo bonito não basta: modelo bom é o que tem a exatidão provada nos checkpoints. Te espero na Aula 7!"

---

## Roteiro da Videoaula 7 — "Produtos cartográficos: ortomosaico, MDS/MDT, nuvem de pontos e cálculo de volumes"

**Duração-alvo:** cerca de 18:30 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à sétima aula. Nas duas últimas aulas, a gente planejou o voo e entendeu como a fotogrametria transforma centenas de fotos num modelo 3D, com pontos de controle, RTK e checkpoints para provar a exatidão. Hoje é o dia de colher os frutos: o que sai do processamento, o que cada produto representa e, principalmente, como se calcula volume — que é, de longe, o uso mais disputado do drone numa obra. Disputado no sentido literal: é com esse número que se paga a empreiteira."

**[TELA]** Slide 3 — foto aérea de grandes pilhas de material: "Empreiteira: 48.200 m³. Fiscalização: 46.900 m³. Alguém errou?"

> "Imagina a cena. Fim do mês numa obra de terraplenagem. A empreiteira voa o drone e mede 48.200 metros cúbicos de corte. A fiscalização, com outro voo, encontra 46.900. São 1.300 metros cúbicos de diferença, o que dá algumas dezenas de milhares de reais na medição. Os dois usaram drone, os dois usaram software sério. E agora? Quem errou? A tentação é escolher um lado. Mas, antes de apontar culpados, você precisa saber três coisas: o que cada produto do drone representa, como o volume é calculado e quanta incerteza cabe nesse número. No fim da aula, a gente volta a essa briga — e você vai ter argumentos de engenheiro para resolvê-la."

### 2. Os quatro produtos e a nuvem de pontos (1:40 – 4:00)

**[TELA]** Slide 4 — galeria: nuvem de pontos, ortomosaico, MDS e MDT.

> "Da nuvem densa que a gente gerou na Aula 6 saem quatro produtos principais. A nuvem de pontos, o ortomosaico, o MDS e o MDT. E eu quero que você guarde uma ideia desde já: cada um responde a uma pergunta diferente. A nuvem responde 'onde está cada coisa, em 3D?'. O ortomosaico responde 'quanto mede e onde está, em planta?'. E o MDS e o MDT respondem 'qual é a cota — e a cota de quê?'. Essa última parte, 'de quê', é a que mais dá problema. Usar o produto errado é a fonte mais comum de erro de volume que eu conheço."

**[TELA]** Slide 5 — nuvem de pontos: X, Y, Z e cor, densidade, medições e classificação.

> "Começando pela nuvem de pontos. Ela é um conjunto de milhões de pontos, cada um com coordenadas X, Y e Z e, na fotogrametria, com a cor RGB do pixel de onde ele veio. Por isso, quando você gira a nuvem na tela, ela parece uma maquete fotográfica, como esta da imagem. A densidade típica de uma nuvem fotogramétrica é da ordem de centenas de pontos por metro quadrado, e depende do GSD que você escolheu lá no planejamento: GSD menor, mais pontos."

> "É o produto mais bruto e, ao mesmo tempo, o mais rico. Com a nuvem você mede distâncias e alturas, extrai perfis e seções transversais — aquela seção da estrada a cada 20 metros que o projetista adora. E, muito importante, você pode classificar os pontos: este é solo, este é vegetação, este é edificação, este é máquina. Guarde isso, porque é a classificação que vai permitir, daqui a pouco, separar o terreno de tudo o que está em cima dele."

### 3. Por que a foto não é mapa: o ortomosaico (4:00 – 6:30)

**[TELA]** Slide 6 — simulação: vista lateral e vista de cima do deslocamento devido ao relevo; clique em Ortorretificar quando a fala pedir.

> "Agora uma pergunta que parece boba: uma foto aérea vertical é um mapa? Não é. E a simulação mostra por quê. À esquerda, a vista lateral: a câmera a 100 metros de altura e um prédio de 30 metros, a 40 metros do centro da foto. A câmera fotografa em perspectiva central: todos os raios passam por um único ponto, o centro da lente. O raio azul vai até a base do prédio. O raio vermelho passa pelo topo do prédio e, se você prolongar até o chão, ele cai mais longe. Resultado: na foto, o telhado aparece deslocado para fora em relação à base — aqui, uns 17 metros no terreno. É o deslocamento devido ao relevo. À direita, vista de cima: o tracejado é a base, o quadrado cheio é o telhado, fora do lugar."

> "Se eu levo o prédio para o centro da foto, o deslocamento some; se eu afasto e aumento a altura, ele cresce. E não é só prédio: um morro, um talude, uma pilha, tudo que tem altura sofre esse efeito, e a escala da foto varia com a cota do terreno. Agora eu clico em Ortorretificar."

> "O software usa o modelo de superfície para reprojetar cada ponto como se fosse visto na vertical. O raio verde desce reto, e o telhado volta para cima da base."

**[TELA]** Slide 7 — foto: ortofoto de uma obra ao redor de uma estação ferroviária: "A foto que vira mapa".

> "O ortomosaico é exatamente isso: o mosaico das fotos ortorretificadas, costuradas numa imagem só. O resultado é uma imagem com escala constante. Nela você mede distâncias e áreas como mediria numa planta, confere a locação de um gabarito, de uma fundação, de um meio-fio, e sobrepõe o projeto em CAD ou em BIM para ver o que está fora do lugar. Esta ortofoto é de uma obra ao redor de uma estação ferroviária, na Alemanha: dá para ler as plataformas, os estacionamentos, as áreas de terra em execução. Para medir avanço físico — quantos metros de pavimento, quantas lajes, quanto de fachada —, o ortomosaico é o produto preferido. Mas repare: ele é uma imagem em planta. Ele não te dá cota. Para cota, você precisa dos modelos digitais."

### 4. MDS × MDT, em 3D (6:30 – 9:20)

**[TELA]** Slide 8 — MDS × MDT: esquema em perfil com a linha da superfície e a do terreno.

> "E aqui entram os dois produtos que mais causam confusão. O MDS, modelo digital de superfície, representa a cota do primeiro obstáculo visto de cima. Telhados, copas de árvores, máquinas, pilhas: o que o drone vê primeiro, ele registra. No esquema, é a linha vermelha passando por cima das casas. O MDT, modelo digital do terreno, representa o solo nu, depois de filtrar tudo o que não é terreno. É a linha azul passando por baixo das casas. E a diferença entre os dois, MDS menos MDT, dá a altura dos objetos — o chamado modelo normalizado."

> "Gerar o MDT a partir de fotogrametria exige filtrar os pontos que não são solo. Em terraplenagem, com solo exposto, isso é fácil. Debaixo de mata densa, é impossível: a câmera simplesmente não vê o chão. É aí que entra o LiDAR, que é assunto da próxima aula. E do MDT saem as curvas de nível, os perfis e as seções que o projeto usa."

**[TELA]** Slide 9 — cena 3D: o mesmo canteiro como cena real, nuvem de pontos, MDS, MDT e MDS − MDT; use os botões na ordem da fala.

> "Vamos ver isso em 3D. Este é um canteiro ilustrativo de 120 por 120 metros: um terreno ondulado, um edifício, um grupo de árvores, uma pilha de material e uma máquina. Clico em Nuvem de pontos: o mesmo canteiro como milhares de pontos coloridos. O edifício aparece claro, as árvores em verde, a máquina em amarelo e a pilha em marrom."

> "Agora MDS. Um lençol estendido sobre tudo: passa por cima do prédio, das copas e da máquina. A cor é a cota. Clico em MDT. Prédio, árvores e máquina sumiram. Mas atenção: a pilha ficou. Por quê? Porque a pilha é material, é exatamente o que eu quero medir. Filtrar não é 'apagar tudo o que é alto'; é decidir o que é terreno para a pergunta que você está fazendo."

> "E agora MDS menos MDT. Tudo o que está em vermelho é o que viraria volume falso se você calculasse o volume com o MDS. Imagine uma escavadeira parada em cima do corte no dia do voo: com o MDS, ela vira terra que ninguém escavou."

### 5. Cálculo de volumes e os três cuidados (9:20 – 11:30)

**[TELA]** Slide 10 — volume como soma de prismas e as três superfícies de referência.

> "Agora, o cálculo de volume. A ideia é simples: dividir o terreno em células — uma malha — e, em cada célula, multiplicar a diferença de cota pela área. Volume é a soma de delta z vezes a área da célula. Na prática, o software faz isso com milhões de células, ou com prismas sobre uma triangulação. Onde delta z é positivo, a superfície medida está acima da referência: é corte, há material a tirar. Onde é negativo, está abaixo: é aterro."

> "A conta é simples. O que exige engenharia é escolher as duas superfícies certas. E a referência pode ser três coisas. O greide de projeto, quando você quer saber quanto ainda falta escavar ou aterrar. O levantamento anterior, quando você quer saber quanto se movimentou no mês — essa é a base da medição de pagamento. Ou um plano de base, quando você quer o volume de uma pilha de brita ou de material estocado."

**[TELA]** Slide 11 — três cuidados: usar o MDT, o mesmo referencial e o empolamento.

> "E três cuidados, que são onde o volume costuma dar errado. Primeiro: use o MDT, nunca o MDS. Já vimos por quê. Segundo: as duas superfícies precisam estar no mesmo referencial — o mesmo sistema de coordenadas e de altitudes. Se um levantamento está num referencial e o outro está deslocado verticalmente alguns centímetros, essa diferença inteira vira volume. Terceiro: o empolamento. O volume que o drone mede no corte é in situ, no lugar. Quando o solo é escavado, ele se solta e ocupa mais espaço no caminhão. Na medição de pagamento, esses três cuidados viram cláusulas: qual superfície, qual referencial e em que estado o volume é medido."

### 6. Exemplo numérico: corte, aterro e viagens (11:30 – 14:00)

**[TELA]** Slide 12 — malha interativa de oito células contra o greide; quando a fala pedir, leve o viés a +3 cm.

> "Vamos fazer a conta com números. Uma plataforma foi levantada e comparada ao greide de projeto numa malha de células de 10 por 10 metros: cada célula tem 100 metros quadrados. São oito células, com as diferenças que estão na tela: mais 1,40, mais 0,90, mais 0,35, menos 0,20, mais 1,10, mais 0,60, menos 0,45 e menos 0,80 metro. Em vermelho, corte; em azul, aterro. Embaixo, o mesmo dado como perfil: barras acima e abaixo da linha do greide."

> "O corte é a soma dos positivos: 1,40 mais 0,90 mais 0,35 mais 1,10 mais 0,60 dá 4,35 metros; vezes 100 metros quadrados, 435 metros cúbicos. O aterro: 0,20 mais 0,45 mais 0,80 dá 1,45; vezes 100, 145 metros cúbicos."

> "Agora eu introduzo um viés: o modelo inteiro 3 centímetros mais alto do que deveria. Olha o que acontece: o corte sobe para uns 450, o aterro cai para uns 136, e o volume líquido muda 24 metros cúbicos. Por quê? Porque são 800 metros quadrados vezes 3 centímetros. Isso é cerca de 5,5% do corte. Em área pequena e corte raso, o viés pesa proporcionalmente mais."

**[TELA]** Slide 13 — calculadora de empolamento e viagens de caminhão.

> "E se todo esse corte for para o bota-fora? Entra o empolamento. Considerando 25%, o volume solto é 435 vezes 1,25, aproximadamente 543,8 metros cúbicos. Com caminhões de 12 metros cúbicos, 543,8 dividido por 12 dá 45,3. E número de viagens se arredonda para cima: 46 viagens. Quem orça o transporte pelo volume in situ, sem empolamento, erra o número de caminhões em quase um quarto. E repare que o drone mede o volume no lugar; quem carrega o volume solto é o caminhão."

### 7. Incerteza do volume (14:00 – 15:20)

**[TELA]** Slide 14 — calculadora δV ≈ A · δz.

> "Agora, a parte mais importante da aula para quem vai assinar uma medição. Qual é a incerteza de um volume calculado por drone? Os erros aleatórios de cota — uma célula um pouco mais alta, a vizinha um pouco mais baixa — tendem a se compensar quando a área é grande. Mas um erro sistemático, um viés de altura que afeta o modelo inteiro, não se compensa. Ele vira volume diretamente: delta V é aproximadamente a área vezes o viés."

> "Num pátio de 2 hectares, que são 20.000 metros quadrados, um viés de apenas 3 centímetros dá 600 metros cúbicos. Seiscentos! Uns 50 caminhões. Por um erro de 3 centímetros, que é pouco mais que o RMSE vertical que a gente comemorou na Aula 6. É por isso que, nos checkpoints, a média dos resíduos importa tanto quanto o RMSE: a média é justamente o indicador do viés."

### 8. Pausa para reflexão: quem está certo? (15:20 – 17:20)

**[TELA]** Slide 15 — Pausa para reflexão: a diferença das duas medições comparada ao efeito do viés, e o que exigir no contrato.

> "Hora da pausa para reflexão. Vamos voltar à briga do começo: 48.200 contra 46.900 metros cúbicos, numa frente de 4 hectares. A diferença é de 1.300 metros cúbicos, cerca de 2,8%. Agora faça a conta que você acabou de aprender: um viés de 3 centímetros em 4 hectares vale 40.000 vezes 0,03, ou seja, 1.200 metros cúbicos. Praticamente toda a diferença. E tem mais: são dois voos, cada um com o seu viés. Combinando os dois pela raiz da soma dos quadrados — lembra da Aula 2? —, dá cerca de 1.700 metros cúbicos. Na barra amarela."

> "Então, quem está certo? Talvez ninguém esteja errado. Os dois números podem estar dentro da incerteza. E aí a discussão deixa de ser técnica e vira contratual. Pense no que você exigiria no contrato, antes da primeira medição. A mesma superfície de referência para os dois lados: o primitivo, levantado no início da obra. MDT, e não MDS. Checkpoints independentes, com o RMSE vertical e a média dos resíduos informados no relatório. Data e hora do voo, porque a obra muda de um dia para o outro. Uma tolerância de volume acordada. E um procedimento de arbitragem, caso a diferença passe da tolerância."

> "Pare o vídeo um minuto e responda: na sua obra, quem faria o voo de referência? E qual tolerância você aceitaria? Medição de pagamento sem método combinado é discussão garantida."

### 9. Atividade prática, pontos-chave e encerramento (17:20 – 18:30)

**[TELA]** Slide 16 — Atividade prática e pontos-chave.

> "Sua missão para esta aula: baixe um ortomosaico e um MDS gratuitos — o OpenDroneMap disponibiliza conjuntos de dados de exemplo — e, no QGIS, que é software livre, meça uma área, trace um perfil e calcule o volume de uma pilha com um plano de base. Depois, repita o cálculo deslocando o plano de base 5 centímetros para cima e para baixo. Quanto mudou o volume? Compare com área vezes delta z. Você vai sentir na mão o peso do viés."

> "Para levar: nuvem, ortomosaico, MDS e MDT respondem a perguntas diferentes. O ortomosaico corrige o deslocamento devido ao relevo e tem escala constante. Volume é soma de delta z vezes área, sempre com MDT, no mesmo referencial e considerando o empolamento. Viés de cota vira volume. E medição por drone exige método e tolerância em contrato."

**[TELA]** Slide 17 — encerramento: "Das fotos aos metros cúbicos".

> "Hoje a gente foi das fotos aos metros cúbicos. Mas ficou uma pendência: e debaixo da mata, onde a câmera não vê o chão? E a fachada com revestimento descolando, que nenhuma foto colorida revela? Na próxima aula, você vai conhecer o LiDAR embarcado e a termografia na inspeção de estruturas e fachadas. Te espero na Aula 8!"

---

## Roteiro da Videoaula 8 — "LiDAR embarcado e termografia na inspeção de estruturas e fachadas"

**Duração-alvo:** cerca de 18:20 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à oitava aula — a que fecha a Unidade 2. Até aqui, o nosso drone carregou uma câmera comum, a RGB. Com ela você planejou o voo, fez fotogrametria, gerou ortomosaico, modelo do terreno e calculou volumes. Hoje eu quero te mostrar dois problemas que essa câmera não resolve — e as duas cargas úteis que completam o kit do drone de engenharia: o LiDAR embarcado e a câmera térmica."

**[TELA]** Slide 3 — foto do drone com LiDAR: "Nenhum dos dois se resolve com a câmera RGB".

> "Imagina que chegam dois pedidos no mesmo dia. O primeiro: levantar o terreno natural de uma encosta coberta de mata, por onde vai passar o acesso de uma obra. Só que a equipe já voou essa área na semana passada, com fotogrametria, e o modelo saiu bonito... mas só mostra a copa das árvores. Onde está o chão? Ninguém sabe. O segundo pedido: um condomínio de quinze anos, com fachada em revestimento cerâmico, quer saber onde as placas estão descolando antes que uma caia na calçada. Uma foto comum mostra a placa no lugar, inteira, bonita — o problema está atrás dela. Nenhum dos dois se resolve com a câmera RGB. O da encosta se resolve com o laser que você vê embaixo desse drone, o LiDAR. O da fachada, com a câmera térmica. Vamos a eles."

### 2. LiDAR: medir distância com luz (1:40 – 3:30)

**[TELA]** Slide 4 — o princípio do LiDAR: 80 m, 533 ns, 240 mil pulsos por segundo.

> "LiDAR vem do inglês light detection and ranging: detecção e medição de distância por luz. O princípio é simples. O sensor emite um pulso de laser, o pulso bate no alvo e volta, e o equipamento mede o tempo de ida e volta. A distância é a velocidade da luz vezes esse tempo, dividido por dois. Por que dividido por dois? Porque o pulso vai e volta: o tempo medido é o do caminho dobrado."

> "Vamos sentir a ordem de grandeza. A luz anda a uns 300 mil quilômetros por segundo — três vezes dez à oitava metros por segundo. Um alvo a 80 metros devolve o pulso em cerca de 533 nanossegundos, ou seja, 533 bilionésimos de segundo. E o equipamento faz isso centenas de milhares de vezes por segundo: o do nosso exemplo emite 240 mil pulsos por segundo."

> "Só a distância, porém, não basta. Para cada pulso virar um ponto com coordenadas X, Y e Z, o sistema combina três coisas: o ângulo em que o feixe saiu, a posição do drone naquele instante, dada pelo GNSS com RTK ou PPK, como vimos na Aula 6, e a atitude do drone — se ele estava inclinado, girado —, dada por uma IMU, a unidade inercial, de alta qualidade. E repare numa diferença enorme em relação à fotogrametria: o LiDAR mede a distância diretamente. Ele não precisa de textura para fazer correspondência entre fotos, e não precisa de luz do sol. Pode voar à noite."

### 3. Múltiplos retornos: o chão sob a mata (3:30 – 6:10)

**[TELA]** Slide 5 — animação de um pulso: sobre solo exposto e sobre uma árvore. Comece em "Sobre uma árvore"; clique em "Sobre solo exposto" quando a fala pedir.

> "Agora o detalhe que resolve o problema da encosta. O feixe de laser não é uma linha infinitamente fina: quando chega lá embaixo, ele tem alguns centímetros de diâmetro. Olha a animação. O pulso desce do drone, a 80 metros, e encontra uma árvore. Parte da energia bate na copa e volta: é o primeiro eco, que chega em uns 413 nanossegundos — a copa está a 62 metros do drone. Outra parte passa por um vão entre as folhas e bate num galho: segundo eco, a uns 70 metros. E uma parte ainda chega ao chão: o último eco, a 80 metros, em 533 nanossegundos. Um pulso, três retornos."

> "Agora eu troco para solo exposto. Um eco só, do chão, em 533 nanossegundos. Oitenta metros."

> "Isso é o que a gente chama de múltiplos retornos. O primeiro retorno descreve a primeira coisa que o laser encontra de cima para baixo: copa, telhado, máquina. É o modelo de superfície, o MDS da aula passada. E o último retorno, quando é solo, permite construir o MDT — o modelo do terreno — mesmo debaixo da vegetação. Agora, um cuidado de vocabulário que derruba muita gente em prova: o laser não atravessa as folhas. Ele passa pelos vãos entre elas. Mata muito fechada, sem frestas, deixa poucos pontos no chão. O LiDAR melhora muito a situação, mas não faz milagre."

**[TELA]** Slide 6 — cena 3D: a encosta com mata varrida pelo laser. Deixe acumular pontos em "Último retorno (MDT)"; clique em "Primeiro retorno (MDS)" e depois volte.

> "Vamos ver isso em três dimensões. Aqui está uma encosta coberta de árvores, com uma clareira no meio. O drone percorre a área emitindo um leque de feixes, de mais ou menos 35 graus para cada lado, e os pontos vão se acumulando. Neste modo, o de último retorno, as árvores ficam transparentes e o que aparece é o terreno natural, colorido pela cota. Repare que, sob as copas mais fechadas, há menos pontos: só os pulsos que acharam um vão chegaram ao chão."

> "Agora eu mudo para primeiro retorno. Olha a nuvem: ela desenha a copa das árvores, em verde. É exatamente o que a fotogrametria teria visto. Essa é a diferença entre o modelo da semana passada e o que o cliente precisa: um mostra a mata; o outro, o chão onde a obra vai passar."

**[TELA]** Slide 7 — nuvens LiDAR reais: edificações com pátio arborizado e um trevo rodoviário.

> "E aqui estão nuvens de verdade. À esquerda, uma nuvem aérea colorida pela altura: torres, um pátio arborizado, as ruas do entorno, ponto a ponto. À direita, um trevo rodoviário, com alças, viadutos e a vegetação em volta. Esse é o tipo de produto que alimenta projeto de corredor, de rodovia, de ferrovia."

### 4. Densidade de pontos e exatidão (6:10 – 8:30)

**[TELA]** Slide 8 — calculadora: largura da faixa, densidade e erro na borda. Mova a altura e o erro da IMU quando a fala pedir; volte aos valores do exemplo.

> "Quantos pontos o LiDAR entrega por metro quadrado? Pense assim: o sensor dispara um certo número de pulsos por segundo e, nesse mesmo segundo, o drone varre uma certa área. A densidade é, aproximadamente, a taxa de pulsos dividida pela velocidade vezes a largura da faixa. E a largura da faixa vem da geometria: duas vezes a altura vezes a tangente da metade do campo de visão."

> "O exemplo da aula: taxa de 240 quilohertz, campo de visão de 70 graus, altura de 80 metros e velocidade de 8 metros por segundo. A faixa dá 2 vezes 80 vezes a tangente de 35 graus: uns 112 metros. A densidade: 240 mil dividido por 8 vezes 112, cerca de 268 pontos por metro quadrado. Isso numa única passada e contando um retorno por pulso; a sobreposição entre faixas aumenta esse número. Se eu subo o drone, a faixa alarga e a densidade cai; se eu acelero, a densidade também cai."

> "E a exatidão? Aqui está a parte que explica por que um LiDAR embarcado é caro. Um erro de ângulo na atitude do drone vira um erro de posição no chão que cresce com a distância: aproximadamente a distância vezes o erro angular, em radianos. Na borda da faixa, a distância inclinada é 80 dividido pelo cosseno de 35 graus, uns 97,7 metros. Um erro de atitude de apenas cinco centésimos de grau, que são 8,7 décimos de milésimo de radiano, desloca o ponto em cerca de 8,5 centímetros. Só pela IMU! Repare nas barras: no nadir, bem embaixo do drone, o erro é de 7 centímetros; na borda, 8,5. Se eu aumento o erro da IMU, as duas barras disparam. Por isso o sistema LiDAR exige uma IMU muito melhor que a de um drone de fotografia. E a conferência é exatamente a da Aula 6: pontos de verificação em campo e RMSE."

### 5. LiDAR × fotogrametria (8:30 – 9:55)

**[TELA]** Slide 9 — tabela LiDAR × fotogrametria e onde o LiDAR brilha.

> "Então LiDAR é sempre melhor? Não. Olha a tabela. Solo sob vegetação: a fotogrametria não vê, o LiDAR vê pelas frestas. Superfície sem textura, como um telhado metálico liso: a fotogrametria falha, o LiDAR mede normalmente. Iluminação: a fotogrametria precisa de luz e de sombras curtas; o LiDAR independe. Fios, cabos e estruturas finas: difíceis para a fotogrametria, bons para o LiDAR. Mas cor e textura? Só a fotogrametria entrega o ortomosaico; o LiDAR, sem uma câmera auxiliar, não tem cor. E o custo do equipamento do LiDAR é bem mais alto."

> "Na obra, o LiDAR brilha em terreno natural com vegetação, linhas de transmissão, corredores de rodovia e ferrovia, estruturas metálicas e túneis — esses, com LiDAR terrestre ou móvel. Já para terraplenagem em solo exposto, a fotogrametria costuma bastar, e é mais barata. Escolha pelo problema, não pela moda."

### 6. Termografia: enxergar temperatura (9:55 – 12:35)

**[TELA]** Slide 10 — o princípio da termografia; termogramas de varandas em dia frio e de fachadas com e sem isolamento.

> "Agora o segundo pedido: a fachada. Todo corpo acima do zero absoluto emite radiação infravermelha — você, eu, a parede, o asfalto. A câmera térmica, em geral um sensor chamado microbolômetro, que trabalha na faixa de 8 a 14 micrômetros de comprimento de onda, mede essa radiação e a converte em temperatura aparente, mostrada em cores falsas. A imagem resultante se chama termograma."

> "E por que eu digo temperatura aparente? Porque a conversão depende de várias coisas. Da emissividade do material, que é quanto ele emite em relação a um corpo negro ideal. Da temperatura refletida do entorno. Da distância e da umidade do ar. Superfícies brilhantes, como metal polido e vidro, têm baixa emissividade e refletem o calor de outros objetos — o céu, o prédio da frente, o próprio operador. Ali o termograma pode mentir. No termograma do meio, de uma torre com varandas em balanço num dia frio, as bordas das lajes aparecem quentes: é calor escapando pelas pontes térmicas. No da direita, a fachada com isolamento aparece em azul, e a sem isolamento, em amarelo e vermelho."

**[TELA]** Slide 11 — três aplicações em fachadas: descolamento, umidade e pontes térmicas.

> "Em inspeção predial, o que interessa não é o valor absoluto da temperatura; é a diferença entre regiões. E há três aplicações clássicas. Primeira: descolamento de revestimento. A placa solta tem uma camada de ar atrás, e o ar isola. Então, sob sol, ela aquece mais rápido que a placa aderida, porque o calor não escoa para a parede: aparece mais quente. E à noite ela esfria mais rápido, e aparece mais fria. Segunda: umidade e infiltração. A água evaporando resfria a superfície; manchas frias em lajes, platibandas e paredes indicam umidade. Terceira: pontes térmicas e instalações — perda de calor por vigas, pilares e lajes, e painéis elétricos ou conexões aquecidos."

> "E guarde a frase do rodapé: a termografia de fachada é passiva. Ela depende de fluxo de calor. Num dia nublado, sem vento, com a fachada sem insolação, as temperaturas se igualam — e nada aparece."

### 7. A fachada ao longo do dia e o planejamento (12:35 – 15:05)

**[TELA]** Slide 12 — termograma simulado da fachada cerâmica; comece às 11 h, depois leve a hora a 16 h e a 21 h; por fim, clique em "Revelar defeitos reais".

> "Vamos testar isso numa fachada simulada, de placas cerâmicas, com sol entre sete da manhã e cinco da tarde. São onze horas, fase de aquecimento. Olha as duas manchas claras: placas descoladas, uns 7 graus mais quentes que as aderidas. E embaixo, uma faixa escura, mais fria: umidade."

> "Agora eu levo o relógio para as quatro da tarde. Repare: o contraste das placas descoladas quase some. É a janela cega: a placa solta já está esfriando, a aderida ainda está quente, e as duas se cruzam. Quem voar nesse horário vai relatar 'fachada sem anomalias' — e vai estar errado. Agora, nove da noite: as placas descoladas aparecem mais frias que as aderidas, uns 3 graus. A anomalia inverteu o sinal! Revelo os defeitos reais: lá estão as duas áreas descoladas e a umidade na base. Moral: o horário do voo é parte do método, não um detalhe."

**[TELA]** Slide 13 — foto: termograma noturno de um edifício: "O termograma diz onde olhar".

> "Então, como se planeja uma inspeção termográfica? O horário se define pela orientação da fachada — se você quer pegá-la aquecendo ou resfriando. Evite chuva recente, que molha tudo e iguala as temperaturas, e vento forte, que rouba calor da superfície. Ajuste a emissividade do material na câmera. E aqui vai a regra mais importante: em fachadas, a termografia apoia a inspeção predial da ABNT NBR 16747, mas não substitui o ensaio de percussão — aquele som cavo da placa solta — nem o ensaio de arrancamento nas áreas suspeitas. O termograma diz onde olhar; a confirmação é local."

> "E lembre da Aula 4: inspeção de fachada é voo junto a edifício habitado, com gente na calçada. Os 30 metros de distância de pessoas não envolvidas e não anuentes, ou uma barreira de proteção, definem a categoria da operação. E isso conversa diretamente com a conta que vem agora."

### 8. Exemplo numérico: a que distância voar? (15:05 – 16:45)

**[TELA]** Slide 14 — calculadora do IFOV e do menor defeito; comece em 10 m e leve a distância a 30 m quando a fala pedir.

> "Uma câmera térmica tem poucos pixels: a do exemplo tem 640 por 512, com pixel de 12 micrômetros e distância focal de 13 milímetros. O equivalente do GSD, para ela, é o IFOV, o campo de visão instantâneo: o tamanho do pixel dividido pela distância focal. 12 micrômetros sobre 13 milímetros dá cerca de 0,92 miliradiano."

> "O que isso significa na fachada? A 10 metros de distância, cada pixel cobre 10 vezes 0,92, uns 9,2 milímetros. E existe uma regra prática: para medir um defeito com confiança, ele precisa ocupar pelo menos três por três pixels. Então o menor defeito confiável a 10 metros tem cerca de 2,8 centímetros."

> "Agora eu levo a distância para 30 metros — a distância que talvez você precise manter das pessoas na calçada. Cada pixel passa a cobrir 2,8 centímetros, e o menor defeito confiável sobe para uns 8,3 centímetros. Olha as barras crescendo. Uma placa cerâmica pequena, descolada sozinha, pode simplesmente sumir na imagem. Moral: a distância de voo é uma decisão de engenharia e de segurança ao mesmo tempo. Às vezes, a solução é isolar a calçada para poder chegar mais perto."

### 9. Atividade prática, fechamento da unidade e prévia da Unidade 3 (16:45 – 18:20)

**[TELA]** Slide 15 — Atividade prática e pontos-chave.

> "Sua missão: escolha uma fachada que você conhece e planeje uma inspeção termográfica com drone. Orientação da fachada e horário do voo, distância e menor defeito detectável, condições meteorológicas, segurança para quem está na calçada — e quais ensaios complementares você faria nas áreas suspeitas. Os pontos-chave estão na tela: tempo de voo do pulso, múltiplos retornos, densidade e trajetória; e, na termografia, diferenças, emissividade, fluxo de calor e confirmação local."

**[TELA]** Slide 16 — foto: modelo 3D de Londres gerado por LiDAR: "Do voo planejado ao modelo da cidade".

> "E com isso fechamos a Unidade 2. Você planejou o voo, com GSD, sobreposição e altura; transformou fotos em 3D com SfM, pontos de controle e RTK ou PPK; gerou ortomosaico, MDS, MDT e volumes; e hoje somou o LiDAR e a termografia. Em todos os casos, a pergunta é a mesma da Unidade 1: qual é a incerteza desse produto, e que decisão ele sustenta?"

**[TELA]** Slide 17 — prévia da Unidade 3: geotécnico, estrutural, segurança e ambiente, dados.

> "Na Unidade 3, o foco desce do céu para dentro do solo e da estrutura. Monitoramento geotécnico, com inclinômetros, piezômetros e marcos de recalque. Monitoramento estrutural, com extensômetros, acelerômetros, fissurômetros e a maturidade do concreto. Sensores de segurança, ambiente e produtividade: vibração, ruído, poeira e rastreamento de equipamentos. E, para fechar, como transformar leituras em séries temporais, níveis de alerta e dashboards. O drone mostra a obra por fora e em campanhas; os sensores contam o que acontece entre um voo e outro. É a combinação dos dois que fecha a malha."

**[TELA]** Slide 18 — encerramento: "Unidade 2 concluída".

> "Foi um prazer voar com você nesta unidade. Te espero na Unidade 3, na Aula 9. Um abraço!"

---

---
