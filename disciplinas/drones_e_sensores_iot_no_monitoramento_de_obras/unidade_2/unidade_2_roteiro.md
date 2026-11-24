# Roteiros das videoaulas — Unidade 2 — Aquisição e Processamento de Imagens

Disciplina: Drones e Sensores IoT no Monitoramento de Obras  
Professor: Afonso Cesar Lelis Brandão

> Cópia para a gravação, montada a partir de `roteiros_15min.md` (fala integral, versão a gravar). Os arquivos de origem não foram alterados.

> **Como usar:** leia as falas em citação (>) na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`).

---

## Roteiro da Videoaula 5 — "Como 330 fotos viram um modelo 3D — e por que ele pode estar 18 cm fora do lugar?"

**Aula 5 — Fotogrametria digital: sobreposição, pontos de controle e georreferenciamento**

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 2:00)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à quinta aula — a primeira da Unidade 2. Na Unidade 1, a gente construiu a base: por que e como monitorar uma obra, que drones e que sensores existem, o que a ANAC, o DECEA e a Anatel exigem e, na Aula 4, como planejar uma missão de voo, com GSD, altura, sobreposição e as condições de segurança. O drone pousou, o cartão de memória está cheio. E agora começa a parte que transforma foto em número de engenharia."

**[TELA]** Slide 3 — "O que você verá nesta unidade": fotogrametria, GNSS e exatidão, produtos cartográficos, volumes e projetado × executado.

> "Esta unidade tem quatro aulas. Hoje, a fotogrametria digital: como fotos sobrepostas viram um modelo 3D, o que são pontos de controle e como se georreferencia esse modelo. Na Aula 6, o posicionamento por GNSS — de onde vêm os erros, RTK, PPK — e como provar a exatidão de um produto com RMSE e com o padrão brasileiro, o PEC-PCD. Na Aula 7, os produtos: ortomosaico, modelos digitais de superfície e de terreno, nuvens de pontos e o LiDAR. E na Aula 8, volumes, curvas de nível e a comparação entre o projetado e o executado. O fio condutor é uma pergunta só: quanto eu posso confiar neste produto, e que decisão ele sustenta?"

**[TELA]** Slide 4 — foto do topógrafo com o receptor GNSS: "18 cm de diferença na cota de um marco".

> "Começo com uma cena que acontece muito. As 330 fotos do plano da Aula 4 viraram um modelo 3D lindo. Texturas nítidas, dá para ler a placa da obra, os prédios vizinhos perfeitos. Todo mundo na reunião adorou. Aí o topógrafo vai a campo e confere um marco de concreto no meio do terreno. Diferença na cota: 18 centímetros. O modelo está certo ou errado? Ele é coerente por dentro: as distâncias entre os objetos batem. Mas o conjunto está deslocado e levemente embarrigado. Hoje você vai entender como as fotos viram 3D, por que isso acontece e como evitar."

### 2. O princípio: interseção de raios e colinearidade (2:00 – 4:30)

**[TELA]** Slide 5 — interativo: câmeras no alto e raios até um ponto do terreno.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com "Fotos que veem o ponto" em 4, "Erro na posição das câmeras" em 0 cm e o botão "Erro aleatório" aceso. O chip diz "Sem erro: os raios se cruzam no ponto verdadeiro". Apontar o ponto verde ("ponto verdadeiro") durante o primeiro parágrafo.
2. Na fala "eu coloco erro na posição das câmeras, 60 centímetros", arrastar "Erro na posição das câmeras" até 60 cm, com "Erro aleatório" ainda aceso. O chip passa a "Aleatório: raios não se encontram (até 32 cm), ponto a 117 cm do verdadeiro" e aparece o círculo vermelho ("ponto calculado").
3. Na fala "Agora eu mudo para erro sistemático", clicar em "Erro sistemático (viés)". O chip passa a "Viés: raios se cruzam bem (dispersão 0 cm), mas deslocados 70 cm: preciso, inexato".

> "Fotogrametria é a ciência de obter medidas confiáveis a partir de fotografias. É a definição do livro de Coelho e Brito, Fotogrametria Digital, que é a bibliografia básica desta unidade. E o princípio é muito simples. Cada pixel de uma foto define um raio: uma reta que sai do centro da câmera e passa pelo ponto do terreno que aquele pixel enxerga. Uma foto só não basta, porque o ponto pode estar em qualquer lugar ao longo do raio. Mas se o mesmo ponto aparece em duas, três, quatro fotos, tiradas de posições diferentes, os raios se cruzam no espaço. E o cruzamento é o ponto em 3D."

> "Olha na tela: quatro câmeras ao longo da rota de voo, a 70 metros, e os quatro raios se encontrando no ponto verde, o ponto verdadeiro. Agora eu coloco erro na posição das câmeras, 60 centímetros, com erro aleatório. Os raios já não se encontram num ponto só, e o ponto calculado, o círculo vermelho, foge do verdadeiro. Agora eu mudo para erro sistemático: todas as câmeras deslocadas para o mesmo lado. Olha que interessante: os raios voltam a se cruzar direitinho, só que num lugar errado. Coerente por dentro, errado no mundo. É exatamente o modelo do gancho."

**[TELA]** Slide 6 — as equações de colinearidade e as duas orientações.

> "A matemática que liga o ponto do terreno, o centro da câmera e o pixel são as equações de colinearidade. Não precisa decorar: o que importa é o que entra nelas. Para cada foto, seis números: a posição do centro da câmera, X zero, Y zero e Z zero, e os três ângulos de atitude, ômega, fi e capa. Isso é a orientação exterior. E, para a câmera, a distância focal, o ponto principal e a distorção da lente: a orientação interior, que é a calibração. Guarde esses dois nomes, porque o efeito de domo, daqui a pouco, nasce de um erro na orientação interior."

### 3. Por que tanta sobreposição (4:30 – 7:00)

**[TELA]** Slide 7 — interativo: o mapa de quantas fotos veem cada ponto; comece em 80% e 70% e, quando a fala pedir, baixe para 50% e 40%.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com "Sobreposição frontal sf" em 80% e "Sobreposição lateral sl" em 70%. Apontar no resultado "B = 70 × (1 − 0,80) = 14,0 m" e "Canteiro de 12 ha (400 × 300 m): 330 fotos" (as 330 fotos do gancho).
2. Na fala "Umas 16 fotos", apontar "≈ 1 / [(1 − sf)(1 − sl)] = 16,7"; o mapa conta "em média, em 17 fotos (mínimo 6)".
3. Na fala "baixo para 50 e 40%", arrastar "Sobreposição frontal sf" até 50% e "Sobreposição lateral sl" até 40%. O mapa fica amarelo e laranja; o resultado passa a "em média, em 4 fotos (mínimo 2)", com a fórmula dando 3,3, e o canteiro cai para 78 fotos.
4. Na fala "Volto para 80 e 70", levar os dois controles de volta a 80% e 70%.

> "Na Aula 4, você calculou o espaçamento entre faixas a partir da sobreposição lateral; ao longo da faixa, a distância entre fotos, a base, é o lado da foto no sentido do voo vezes um menos a sobreposição frontal: no nosso voo, 70 vezes 0,2, 14 metros. No canteiro de 12 hectares, isso dá umas 11 faixas de 30 fotos: as 330 fotos do gancho. Agora a fotogrametria explica por que a gente insiste em 75 a 80% de frontal e 65 a 75% de lateral. O primeiro motivo é a multiplicidade. Em média, cada ponto aparece em um sobre o produto das partes que não se repetem: um sobre 0,2 vezes 0,3. Umas 16 fotos. Na tela, cada cor diz em quantas fotos aquele ponto aparece."

> "Agora olha o que acontece se eu economizo: baixo para 50 e 40%. O mapa vira amarelo e laranja, a média cai para umas 3 fotos e há faixas de pontos vistos em apenas duas. Com uma foto, não tem interseção; com duas, qualquer erro passa despercebido, e basta uma foto borrada para abrir um buraco no modelo. Mais raios por ponto é redundância. Volto para 80 e 70."

**[TELA]** Slide 8 — a base efetiva: o mesmo ponto visto pelas fotos 1 e 2 e pelas fotos 1 e 5.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com o botão "Fotos 1 e 2 (B = 14 m)" aceso. Durante o primeiro parágrafo, apontar o chip "H/B = 5,00 · σZ ≈ 5,00 × 1,92 × 0,5 = 4,8 cm" e a região de cruzamento alta e estreita.
2. Na fala "as duas mais distantes estão a quatro bases uma da outra", clicar em "Fotos 1 e 5 (B = 56 m)". O chip passa a "H/B = 1,25 · σZ ≈ 1,25 × 1,92 × 0,5 = 1,2 cm", a cota "B = 56 m" aparece acima das câmeras e a região de cruzamento fica baixa e compacta.

> "O segundo motivo é a geometria. A precisão vertical de um par de fotos depende da razão entre a altura e a base. Raios quase paralelos se cruzam mal: um erro pequeno na imagem vira um erro grande na cota. A aproximação é sigma Z igual a H sobre B, vezes o GSD, vezes a precisão de medição em pixels. Com o nosso voo — 70 metros, base de 14, GSD de 1,92 centímetro e meio pixel de precisão —, um par de fotos vizinhas dá 5 vezes 1,92 vezes 0,5: 4,8 centímetros. Ruim."

> "Mas, com 80% de frontal, cada ponto aparece em umas 5 fotos seguidas da faixa. As duas mais distantes estão a quatro bases uma da outra: 56 metros. H sobre B cai para 1,25, e a precisão vertical vai para 1,2 centímetro. Quatro vezes melhor. Então a sobreposição alta não é desperdício de bateria: é ela que dá base efetiva grande e, com isso, cota boa. E o ajustamento ainda combina todos esses raios ao mesmo tempo. Valores ilustrativos, mas a lógica é exatamente essa."

### 4. Structure from Motion (7:00 – 9:30)

**[TELA]** Slide 9 — os 4 passos do SfM.

> "Na fotogrametria clássica, de avião, a orientação das câmeras era conhecida com instrumentos caros. Nos drones, o processamento usa o Structure from Motion, SfM: 'estrutura a partir do movimento'. Ele resolve ao mesmo tempo onde estavam as câmeras e qual é a forma do terreno. São quatro passos."

> "Primeiro, detectar. Em cada foto, o algoritmo encontra milhares de feições distintivas — cantos, texturas, manchas — e descreve cada uma com uma espécie de assinatura, como no método SIFT. Segundo, corresponder: reconhecer a mesma feição em fotos diferentes. Esses são os pontos homólogos. Terceiro, ajustar: o ajustamento por feixes, o bundle adjustment, um grande ajuste de mínimos quadrados das equações de colinearidade. Ele calcula, de uma vez, a orientação exterior de cada foto, a orientação interior da câmera — é a autocalibração — e as coordenadas dos pontos homólogos. O resultado é a nuvem esparsa. E quarto, densificar: com as câmeras orientadas, o software procura correspondências pixel a pixel e gera a nuvem densa, a matéria-prima de todos os produtos da Aula 7."

**[TELA]** Slide 10 — interativo: as etapas do SfM com duas fotos; clique em cada etapa quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com o botão "1. Detectar" aceso: duas fotos com as feições em azul (chip "Feições detectadas em cada foto"). Se a animação já tiver passado, clicar de novo em "1. Detectar" na fala "Etapa 1".
2. Na fala "Etapa 2", clicar em "2. Corresponder": linhas verdes e as vermelhas tracejadas, descartadas.
3. Na fala "Etapa 3", clicar em "3. Ajustar": câmeras orientadas e nuvem esparsa amarela.
4. Na fala "Etapa 4", clicar em "4. Densificar": nuvem densa colorida. O segundo parágrafo é dito com essa etapa na tela.

> "Vamos ver isso acontecendo. Etapa 1: duas fotos do mesmo galpão e da mesma pilha, e as feições aparecendo em azul. Etapa 2: as linhas verdes ligam as correspondências. Repare nas linhas vermelhas tracejadas: são correspondências erradas, um canto confundido com outro. O algoritmo as descarta, porque não combinam com a geometria das outras. Etapa 3: as câmeras orientadas lá em cima e a nuvem esparsa em amarelo. Etapa 4: a nuvem densa, milhares de pontos com cor."

> "E onde o SfM tropeça? Em superfícies sem textura — água, telhado metálico liso, uma laje novinha e uniforme. Em objetos em movimento: a escavadeira mudou de lugar entre uma foto e outra e vira um fantasma. E em vegetação densa: a câmera só vê a copa. Dica de campo: voe com as máquinas paradas na área que importa e aumente a sobreposição em solo homogêneo."

### 5. Georreferenciamento e o efeito de domo (9:30 – 11:45)

**[TELA]** Slide 11 — georreferenciamento indireto × direto.

> "Agora o ponto central da aula. Só com as fotos, o SfM reconstrói a forma. Mas não sabe onde essa forma está no mundo, nem o tamanho exato dela. O GNSS de navegação do drone ajuda, mas tem exatidão de metros. Para amarrar o modelo ao sistema de referência — no Brasil, o SIRGAS2000 —, existem dois caminhos. O georreferenciamento indireto: medir em campo pontos de controle visíveis nas fotos e colocá-los no ajustamento. E o georreferenciamento direto: conhecer, com exatidão de centímetros, a posição de cada foto, com GNSS RTK ou PPK embarcado no drone. Esse segundo caminho é o assunto da próxima aula."

**[TELA]** Slide 12 — cena 3D: terreno real × modelo; troque o cenário quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. A cena abre com o botão "Sem GCP" aceso e gira sozinha; se quiser, arrastar para girar e rolar para aproximar. Apontar o chip "Desvio no marco central: 18 cm · nos cantos: 8 cm" na fala "no marco central, 18 centímetros; nos cantos, 8".
2. Na fala "Clico em 'Com GCP'", clicar em "Com GCP": aparecem os alvos laranja, a malha desce e o chip passa a "Desvio no marco central: 4 cm · nos cantos: 0 cm": sobra um domo pequeno.
3. Na fala "E em 'GCP mais oblíquas'", clicar em "GCP + oblíquas": o chip passa a "Desvio no marco central: 1 cm · nos cantos: 0 cm" e a curvatura praticamente some.

> "Sem nenhum dos dois, além do deslocamento, aparece o efeito de domo. Pequenos erros na calibração da lente, que o ajustamento não consegue separar da forma do terreno, curvam o modelo como uma tigela virada. É típico de blocos com fotos todas verticais e paralelas — exatamente o voo em faixas que a gente planejou —, e foi bem descrito por James e Robson, num artigo de 2014 que está na lista de leituras."

> "Olha em 3D. A superfície marrom é o terreno real; a malha azul é o modelo fotogramétrico, com os desvios verticais exagerados 60 vezes. Sem pontos de controle, a malha está acima do terreno e curvada no centro: no marco central, 18 centímetros; nos cantos, 8. É o nosso gancho. Clico em 'Com GCP': a malha desce e se aproxima do terreno; sobra um domo pequeno. E em 'GCP mais oblíquas': as fotos inclinadas travam a calibração da lente e o domo praticamente some."

> "Na prática, como colocar fotos oblíquas no voo? Duas formas comuns: uma segunda passada em grade cruzada, com a câmera inclinada uns 20 a 30 graus, ou algumas fotos inclinadas ao redor da área, no fim do voo. Custa alguns minutos de bateria e economiza muita dor de cabeça no processamento."

### 6. Pontos de controle e de verificação (11:45 – 14:00)

**[TELA]** Slide 13 — foto do alvo de controle na Islândia: "Um grupo amarra, o outro prova".

> "Então vamos aos pontos de controle, os GCPs, do inglês ground control points. São alvos bem visíveis nas fotos — placas em xadrez, cruzes pintadas no chão, como esse alvo laranja e branco da foto — cujas coordenadas são medidas em campo com GNSS RTK ou estação total. O alvo precisa ocupar dezenas de pixels: um alvo de 60 centímetros, com o nosso GSD de 1,92, tem uns 31 pixels de lado. Dá para marcar o centro com precisão de fração de pixel."

> "E existe um segundo grupo, que muita gente esquece: os pontos de verificação, os checkpoints. São medidos exatamente do mesmo jeito, mas não entram no processamento. Servem só para conferir. Por quê? Porque, se eu uso os mesmos pontos para ajustar e para verificar, o modelo vai passar direitinho por eles e eu não aprendo nada. É o aluno corrigindo a própria prova."

**[TELA]** Slide 14 — interativo: distribuição dos GCPs e o mapa de erro; troque a distribuição quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com o botão "Só nos 4 cantos" aceso. Na fala "o checkpoint do meio lê quase 19 centímetros", apontar o rótulo "18,8 cm" no checkpoint branco do centro e o chip "Só nos 4 cantos · pior checkpoint: 18,8 cm".
2. Na fala "Concentrados num lado", clicar em "Concentrados num lado": o lado oposto fica vermelho e o chip passa a "Concentrados num lado · pior checkpoint: 15,7 cm".
3. Na fala "Agora, seis pontos no perímetro e no interior", clicar em "6: perímetro + interior": tudo verde, e o chip passa a "6: perímetro + interior · pior checkpoint: 4,7 cm".

> "E onde colocar os GCPs? Olha o mapa de 20 hectares; a cor mostra o erro vertical esperado — o modelo fica bem amarrado perto dos GCPs e solto longe deles. Modelo de erro ilustrativo, só para comparar. Com quatro GCPs só nos cantos, o centro fica vermelho: o checkpoint do meio lê quase 19 centímetros. Concentrados num lado, o lado oposto fica solto. Agora, seis pontos no perímetro e no interior: tudo verde. A regra: GCPs no perímetro e no interior, cobrindo também os pontos altos e baixos, e checkpoints independentes espalhados pela área. Com georreferenciamento direto, os GCPs podem ser poucos. Os checkpoints, nunca zero."

### 7. O processamento no OpenDroneMap e no Metashape (14:00 – 16:15)

**[TELA]** Slide 15 — o fluxo de processamento: importar, alinhar, marcar GCPs, gerar produtos, ler o relatório.

> "Na prática, onde tudo isso acontece? A ementa sugere dois programas. O OpenDroneMap, que é livre, com a interface web chamada WebODM. E o Agisoft Metashape, comercial, muito usado em empresas de topografia. O fluxo é o mesmo. Um: importar as fotos, que já vêm com a posição do GNSS do drone. Dois: alinhar — é o SfM com o ajustamento. Três: marcar os pontos de controle nas fotos. No OpenDroneMap, isso entra por um arquivo de texto com as coordenadas e os pixels onde cada alvo aparece; no Metashape, você clica no centro de cada alvo e reotimiza a câmera. Quatro: gerar nuvem densa, modelo de superfície e ortomosaico. E cinco, a etapa que muita gente pula: ler o relatório de qualidade."

**[TELA]** Slide 16 — o relatório de qualidade: erro de reprojeção, erro nos GCPs e erro nos checkpoints.

> "No relatório, três números merecem atenção. O erro de reprojeção, que em geral fica abaixo de 1 pixel: ele diz se as fotos estão coerentes entre si. O erro nos GCPs: diz se o modelo passou bem pelos alvos que você mandou ele respeitar. E o erro nos checkpoints, que é o único que mede a exatidão de verdade, porque esses pontos não participaram do ajuste. Um modelo pode ter erro de reprojeção de 0,4 pixel, GCPs com 1 centímetro e checkpoints com 9. Isso quer dizer que, entre os alvos, o modelo está solto — talvez pela distribuição, talvez por um domo residual. Se você só olhasse os dois primeiros números, assinaria um levantamento ruim."

### 8. Atividade, síntese e prévia da Aula 6 (16:15 – 18:00)

**[TELA]** Slide 17 — atividade prática e pontos-chave.

> "Sua missão: baixe um conjunto de dados de exemplo do OpenDroneMap que traga arquivo de pontos de controle. Processe duas vezes no WebODM: sem e com os GCPs, reservando dois ou três alvos como checkpoints. Compare os relatórios. O erro de reprojeção mudou muito? E os checkpoints? O modelo sem GCPs é coerente por dentro? Está no lugar certo?"

> "Resumindo: a fotogrametria funciona por interseção de raios, com orientação exterior e interior; a sobreposição alta dá redundância e base efetiva; o SfM detecta, corresponde, ajusta e densifica; sem georreferenciamento, o modelo fica deslocado e com domo; e GCPs amarram, checkpoints provam."

**[TELA]** Slide 18 — encerramento.

> "Ficou uma pergunta no ar. Eu disse que o georreferenciamento direto usa RTK ou PPK, com exatidão de centímetros. Mas de onde vêm os metros de erro do GNSS comum? Como o RTK chega ao centímetro? E como se prova, com números, que um produto atende ao padrão brasileiro? Na próxima aula, a gente abre a caixa-preta do GNSS. Te espero na Aula 6!"

---

## Roteiro da Videoaula 6 — "O drone dizia 'FIX', mas a obra inteira estava 1,5 metro ao lado: o que o GNSS não te conta"

**Aula 6 — Posicionamento por GNSS e precisão dos produtos cartográficos**

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à sexta aula. Na aula passada, a gente viu que o modelo fotogramétrico precisa ser amarrado ao terreno, por pontos de controle ou pela posição exata de cada foto. Em todos os casos, quem mede essas posições é o GNSS: no bastão do topógrafo, na base do canteiro, no próprio drone. Hoje a gente vai entender como ele funciona, de onde vêm os erros e como provar a exatidão de um produto cartográfico. A referência da aula é o livro do professor João Galera Monico, Posicionamento pelo GNSS, da bibliografia da disciplina."

**[TELA]** Slide 3 — ortomosaico perfeito sobre o projeto, deslocado: "FIX o voo inteiro".

> "E começo com uma história. O drone com RTK mostrou FIX o voo inteiro. O ortomosaico ficou impecável; as distâncias medidas nele batiam com a trena. Mas, quando a equipe sobrepôs o projeto, a obra inteira estava um metro e meio ao lado e quase três metros acima do lugar. O que aconteceu? A base GNSS tinha sido instalada num ponto cujas coordenadas vieram do próprio receptor, em modo autônomo. O levantamento era preciso — e inexato. No fim da aula, você vai saber explicar isso e, mais importante, evitar."

### 2. Como o GNSS mede posição (1:40 – 4:00)

**[TELA]** Slide 4 — as constelações: GPS, GLONASS, Galileo e BeiDou; foto da constelação GPS.

> "GNSS é o nome genérico dos sistemas de navegação por satélite. O GPS, americano, é o mais conhecido, mas hoje um receptor de obra usa também o GLONASS, russo, o Galileo, europeu, e o BeiDou, chinês. Mais satélites no céu significam mais chance de boa geometria, o que faz muita diferença num canteiro cheio de obstruções."

**[TELA]** Slide 5 — pseudodistância: ρ = c · Δt e os 4 satélites.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre com "Erro do relógio do receptor δt" em 1,00 µs. Na fala "um erro de um microssegundo", apontar "Erro na distância c · δt: 300 m" e "Em quilômetros: 0,30 km" (a barra "c · δt" mostra 300 m). Não é preciso mexer no controle: o valor inicial já é o da fala.
2. Na fala "pelo menos quatro satélites", apontar a linha "Incógnitas: X, Y, Z e o relógio: 4 satélites, no mínimo".

> "Como o receptor mede posição? Cada satélite transmite a hora de um relógio atômico e a sua órbita. O receptor mede quanto tempo o sinal levou para chegar e multiplica pela velocidade da luz: é a pseudodistância. Pseudo, por quê? Porque o relógio do receptor é barato e não está sincronizado com o dos satélites. E olha o tamanho do problema: um erro de um microssegundo, um milionésimo de segundo, vezes 300 mil quilômetros por segundo, dá 300 metros. Por isso a gente precisa de pelo menos quatro satélites: três incógnitas de posição, X, Y e Z, e uma quarta, o erro do relógio do receptor."

> "E existe uma segunda medida, que é a que leva ao centímetro: a fase da onda portadora. O comprimento de onda do sinal é de uns 19 centímetros, e o receptor geodésico mede a fração de ciclo com resolução de milímetros. O problema é que ele não sabe quantos ciclos inteiros cabem entre o satélite e a antena. Esse número inteiro desconhecido é a ambiguidade. Guarde essa palavra."

### 3. Fontes de erro e geometria (4:00 – 6:45)

**[TELA]** Slide 6 — as fontes de erro: órbita e relógio, ionosfera, troposfera, multicaminho, receptor e antena.

> "No posicionamento autônomo — um receptor sozinho, como o do celular e o de navegação do drone —, vários erros se somam. Erros de órbita e de relógio dos satélites. O atraso na ionosfera, a camada ionizada da atmosfera, que em geral é o maior de todos. O atraso na troposfera, por causa da umidade e da pressão. O multicaminho: o sinal que chega refletido numa parede, numa estrutura metálica, numa máquina ou na água, percorrendo um caminho maior. E o ruído e o centro de fase da antena do receptor."

**[TELA]** Slide 7 — interativo: o céu simulado com satélites e o PDOP; agrupe os satélites quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com o botão "Bem espalhados" aceso e "Erro de cada pseudodistância" em 2,0 m. Na fala "o PDOP fica perto de 2", apontar "PDOP = 2,0".
2. Na fala "Agora eu agrupo os satélites num canto", clicar em "Agrupados (ao lado de um prédio)": os satélites migram para um lado, metade do céu fica cinza ("céu bloqueado pelo prédio") e o resultado passa a "PDOP = 7,8" (σ ≈ 15,6 m).
3. Na fala "Com PDOP 2 e erro de 2 metros", clicar de volta em "Bem espalhados" e apontar "σposição ≈ 2,0 × 2,0 m = 4,0 m". O controle de erro fica em 2,0 m.

> "E a geometria dos satélites multiplica tudo. O desvio da posição é, aproximadamente, o PDOP vezes o erro de cada pseudodistância. PDOP é a diluição da precisão. Olha o céu simulado: com os satélites bem espalhados, o PDOP fica perto de 2. Agora eu agrupo os satélites num canto, como acontece ao lado de um prédio alto: o PDOP passa de 6. Com PDOP 2 e erro de 2 metros por pseudodistância, a posição autônoma erra uns 4 metros. Por isso o GNSS de navegação do drone serve para voar, mas não para medir."

**[TELA]** Slide 8 — dois cuidados brasileiros: a anomalia equatorial e o canteiro como ambiente de multicaminho.

> "E aqui vão dois cuidados bem brasileiros e bem de canteiro. O Brasil fica sob a chamada anomalia equatorial de ionização. Em períodos de alta atividade solar, a cintilação ionosférica, principalmente entre o pôr do sol e a madrugada, faz o receptor perder satélites e perder a solução RTK. Quem já tentou levantar à noite no Nordeste ou no Centro-Oeste conhece. O segundo cuidado: o canteiro é um ambiente de multicaminho e de obstrução — grua, fachada, fôrma metálica, contêiner. Use máscara de elevação, de 10 a 15 graus, para descartar satélites muito baixos, e instale a base longe de superfícies refletoras, com céu aberto."

### 4. Posicionamento relativo: RTK e PPK (6:45 – 9:45)

**[TELA]** Slide 9 — base e rover observando os mesmos satélites; FIX × FLOAT.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre com "Distância do rover à base" em 12 km. O primeiro parágrafo é dito sem mexer no controle.
2. Na fala "8 milímetros mais 1 ppm na horizontal e 15 milímetros mais 1 ppm na vertical", arrastar "Distância do rover à base" até 0 km: "Horizontal: 8 mm + 1 ppm: 8 mm" e "Vertical: 15 mm + 1 ppm: 15 mm".
3. Na fala "A 12 quilômetros da base", arrastar de volta até 12 km: 20 mm na horizontal e 27 mm na vertical, como nas barras "Horizontal" e "Vertical".

> "Agora, a grande sacada. Os erros de órbita, relógio e atmosfera são quase iguais para dois receptores próximos. Então eu coloco uma base em coordenadas conhecidas e um rover — o drone ou o bastão do topógrafo — observando os mesmos satélites. Fazendo as diferenças entre as observações, a maior parte dos erros se cancela. E, com os erros cancelados, o software consegue resolver aquela ambiguidade da fase. Quando resolve, a solução é fixa — o famoso FIX —, de centímetros. Quando não resolve, a solução é flutuante, FLOAT, de decímetros. Levantamento de engenharia se faz com FIX."

> "E a precisão piora com a distância à base, porque os erros vão ficando menos parecidos. As fichas técnicas expressam isso como, por exemplo, 8 milímetros mais 1 ppm na horizontal e 15 milímetros mais 1 ppm na vertical. Um ppm é um milímetro por quilômetro. A 12 quilômetros da base: 8 mais 12, 20 milímetros na horizontal; 15 mais 12, 27 na vertical."

**[TELA]** Slide 10 — RTK × PPK: rádio e NTRIP, RBMC-IP, RBMC e reprocessamento.

> "Existem dois jeitos de usar isso. No RTK, as correções chegam durante o voo, por rádio de uma base local ou pela internet, pelo protocolo NTRIP, de uma rede de estações. O IBGE oferece a RBMC-IP, que transmite dados de estações da Rede Brasileira de Monitoramento Contínuo em tempo real. A vantagem é saber na hora se está tudo certo; a limitação é depender do enlace funcionando o tempo todo."

> "No PPK, o drone só grava os dados brutos, e a correção é calculada depois, no escritório, com os dados de uma base local ou de uma estação da RBMC. Não depende de enlace durante o voo e permite reprocessar se algo der errado. Um cuidado: as estações da RBMC podem estar a dezenas de quilômetros da obra, e o erro cresce com a distância; para drone, uma base no canteiro costuma ser a melhor opção."

**[TELA]** Slide 11 — interativo: o erro da base desloca todo o levantamento; mova a base quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com "Erro na coordenada da base" em 0,0 m: o chip diz "Base em coordenada correta: levantamento sobre o projeto" e "Distância interna: 20,00 m (não muda)".
2. Na fala "Se eu desloco a coordenada da base em um metro e meio", arrastar "Erro na coordenada da base" até 1,5 m. O levantamento inteiro (em azul) sai de cima do projeto, e o chip passa a "Todos os pontos deslocados 1,5 m, na mesma direção".
3. Na fala "as distâncias internas continuam perfeitas", apontar o chip "Distância interna: 20,00 m (não muda)". Deixar em 1,5 m até o fim do slide.

> "E agora a explicação do gancho. No posicionamento relativo, o rover é calculado em relação à base. Olha na tela: a base, os pontos do levantamento e a distância entre eles. Se eu desloco a coordenada da base em um metro e meio, todos os pontos se deslocam junto, um metro e meio. A forma não muda nada, as distâncias internas continuam perfeitas. Por isso o ortomosaico batia com a trena. O erro da base vira erro de todo o levantamento. Então a coordenada da base tem que vir de um vértice conhecido, de pós-processamento com a RBMC ou do IBGE-PPP, o serviço gratuito de posicionamento por ponto preciso do IBGE, que, com algumas horas de rastreio, entrega coordenadas de centímetros. Nunca do modo autônomo."

> "E, no drone, o RTK tem mais dois cuidados, que separam o georreferenciamento direto que funciona do que engana. O primeiro é o sincronismo: a posição tem que ser a do instante exato da foto. Um atraso de 20 milissegundos, a 6 metros por segundo, desloca a foto 12 centímetros — mais de seis vezes o nosso GSD. O segundo é o braço de alavanca: a antena fica em cima do drone e a câmera, embaixo, e essa distância, combinada com a inclinação do drone, precisa ser descontada. Drones de mapeamento fazem isso de fábrica; adaptações caseiras, nem sempre. E é por isso que, mesmo com RTK, os checkpoints continuam obrigatórios."

### 5. Referenciais, projeção e altitudes (9:45 – 12:15)

**[TELA]** Slide 12 — SIRGAS2000, UTM e o fator de escala.

> "Coordenada certa também precisa estar no referencial certo. O sistema geodésico oficial do Brasil é o SIRGAS2000. Para trabalhar em planta, em metros, usa-se em geral a projeção UTM; no Sudeste, por exemplo, o fuso 23 Sul. Um detalhe que pega muito engenheiro: a UTM tem fator de escala de 0,9996 no meridiano central. Um quilômetro medido no terreno aparece como 999,6 metros na planta. Quarenta centímetros por quilômetro! Em obras extensas, como rodovias e loteamentos grandes, usa-se um sistema topográfico local, como o da norma NBR 14166."

**[TELA]** Slide 13 — altura elipsoidal × altitude: o elipsoide, o geoide e a ondulação N; mapa das ondulações do geoide.

> "E a altitude, que é onde mora a maior confusão. O GNSS entrega a altura elipsoidal, h, medida sobre o elipsoide, uma superfície matemática lisa. O projeto usa a altitude ligada ao nível médio do mar, H. A diferença entre as duas é a ondulação geoidal, N: H é aproximadamente h menos N. No mapa, você vê que o geoide sobe e desce dezenas de metros em relação ao elipsoide. No Brasil, a ondulação é obtida dos modelos do IBGE, como o MAPGEO2015 e o hgeoHNOR2020."

> "Um exemplo. Um checkpoint tem altura elipsoidal de 742,35 metros, e a ondulação no local é de menos 5,20 metros — valor ilustrativo. A altitude é 742,35 menos menos 5,20: 747,55 metros. Se alguém comparar a altura elipsoidal com o projeto, vai achar um 'erro' de mais de 5 metros que não existe. E atenção: muitos aplicativos de drone gravam altura elipsoidal ou referida a um modelo global. Confira sempre o referencial vertical antes de comparar com o projeto."

### 6. Precisão, exatidão e RMSE (12:15 – 13:45)

**[TELA]** Slide 14 — precisão × exatidão; RMSE e média dos resíduos.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com "Viés somado a todos os pontos" em 0,0 cm: cinco barras (CP1 a CP5) dentro da faixa verde de ±5 cm, "Média dos Δz: 0,34 cm", "RMSEz: 2,56 cm" e "Especificação RMSEz ≤ 5 cm: atende". O primeiro parágrafo é dito sem mexer no controle.
2. Na fala "Mas não pare no RMSE: calcule também a média dos resíduos", arrastar "Viés somado a todos os pontos" até +5,0 cm. As barras sobem juntas, a linha amarela da média vai a 5,34 cm, o RMSEz a 5,91 cm e a especificação passa a "não atende".
3. Na fala "é a média que denuncia o viés", apontar a linha amarela "média" e mostrar que ela ficou quase do tamanho do RMSE (5,34 × 5,91 cm): é a "assinatura de erro sistemático" da fala. Deixar em +5,0 cm até o fim do slide.

> "Agora, como se diz, com números, que um produto é bom. Primeiro, duas palavras. Precisão é a dispersão de medidas repetidas. Exatidão é a proximidade do valor verdadeiro. O gancho é o caso extremo: dispersão de centímetros, erro de metros. Para avaliar a exatidão, a gente usa pontos de verificação independentes, medidos com um método várias vezes mais exato que o produto."

> "E calcula o RMSE, a raiz do erro médio quadrático: para cada ponto, modelo menos campo, elevo ao quadrado, tiro a média e a raiz. Na horizontal, combino x e y. Mas não pare no RMSE: calcule também a média dos resíduos. O RMSE soma a dispersão e o viés; é a média que denuncia o viés. No gancho, o RMSE seria de quase três metros, e a média, praticamente igual. Isso é assinatura de erro sistemático."

### 7. PEC-PCD e o exemplo dos cinco checkpoints (13:45 – 16:45)

**[TELA]** Slide 15 — PEC-PCD: Decreto 89.817/1984, ET-CQDG, classes A a D, PEC e EP.

> "No Brasil, produtos cartográficos são classificados pelo PEC-PCD, o Padrão de Exatidão Cartográfica dos Produtos Cartográficos Digitais. A base legal é o Decreto 89.817, de 1984, e a especificação técnica de controle de qualidade do Exército, a ET-CQDG. Para cada escala e cada classe, de A a D, há dois limites. Noventa por cento dos pontos devem ter erro até o PEC. E o erro-padrão, que é o RMSE, deve ficar até o EP. Na planimetria, a Classe A tem PEC de 0,28 milímetro e EP de 0,17 milímetro na escala da carta. Na altimetria, PEC de 0,27 e EP de um sexto da equidistância das curvas de nível. O padrão americano, da ASPRS, na edição de 2023, reporta pelo próprio RMSE e pede no mínimo 30 checkpoints para a avaliação completa."

**[TELA]** Slide 16 — tabela dos cinco checkpoints e a classificação.

> "Vamos ao exemplo. O voo da Aula 4, GSD de 1,92 centímetro, com RTK e 6 GCPs, foi conferido em 5 checkpoints independentes. Fazendo as contas, o RMSE em x dá 1,25 centímetro, e em y, 1,13. Na horizontal: raiz de 1,25 ao quadrado mais 1,13 ao quadrado, 1,69 centímetro, cerca de 0,9 GSD. Na vertical, os quadrados somam 32,65; dividido por 5 e tirada a raiz, 2,56 centímetros, cerca de 1,3 GSD. E a média dos resíduos verticais: mais 0,34 centímetro. Praticamente zero. Sem viés."

> "Agora, a classificação. Na escala 1 para 500, a Classe A planimétrica pede EP de 0,17 vezes 500, 85 milímetros, e PEC de 140. Com 1,69 centímetro, atende com folga. Na altimetria, a Classe A exige que o RMSE seja até um sexto da equidistância. Então a equidistância tem que ser pelo menos 6 vezes 2,56: 15,4 centímetros. Arredondando para um valor usual, curvas de nível de 20 centímetros. Com elas, o EP é 3,3 e o PEC, 5,4 centímetros, e todos os resíduos ficam abaixo. Ressalva honesta: cinco pontos são ilustrativos; a classificação formal segue o tamanho de amostra da especificação. E esse número, 20 centímetros, volta na Aula 8, quando a gente gerar as curvas."

### 8. Atividade, síntese e prévia da Aula 7 (16:45 – 18:00)

**[TELA]** Slide 17 — atividade prática e pontos-chave.

> "Sua missão: no portal do IBGE, baixe os dados de um dia de uma estação da RBMC próxima da sua cidade, e submeta uma hora desses dados ao IBGE-PPP. Compare a coordenada que voltar com a coordenada oficial da estação. Depois, consulte a ondulação geoidal no MAPGEO2015 para o mesmo ponto e converta a altura elipsoidal em altitude."

> "Para levar: o GNSS mede pseudodistâncias e fase; os erros, multiplicados pelo PDOP, deixam o modo autônomo em metros; o posicionamento relativo, com RTK ou PPK e solução fixa, chega ao centímetro; o erro da base desloca tudo; altitude não é altura elipsoidal; e a exatidão se prova com RMSE e média nos checkpoints, classificada pelo PEC-PCD."

**[TELA]** Slide 18 — encerramento.

> "Com o modelo no lugar certo e a exatidão provada, chegou a hora de colher os produtos. Na próxima aula: ortomosaico, MDS, MDT, nuvem de pontos e o laser que enxerga o chão debaixo da mata. Te espero na Aula 7!"

---

## Roteiro da Videoaula 7 — "Uma foto aérea não é um mapa: ortomosaico, MDS, MDT e o laser que enxerga o chão sob a mata"

**Aula 7 — Ortomosaicos, modelos digitais de superfície e nuvens de pontos**

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à sétima aula. Nas duas últimas aulas, a gente transformou centenas de fotos num modelo 3D, amarrado ao terreno, com a exatidão provada nos checkpoints. Hoje é o dia de colher os frutos: o que sai do processamento, o que cada produto representa e como abrir e analisar tudo isso num software livre, o QGIS."

**[TELA]** Slide 3 — os três pedidos: área executada, pilha de brita e encosta com mata.

> "Imagina uma segunda-feira na obra. Três pedidos chegam ao mesmo tempo. O planejamento quer a área de laje e de pavimento executada no mês. A área de suprimentos quer o volume da pilha de brita. E a projetista do acesso quer o terreno natural de uma encosta coberta de mata — só que a fotogrametria da semana passada só viu a copa das árvores. Os três dizem a mesma frase: 'me manda o levantamento do drone'. Mas qual produto? No fim da aula, você vai ter a resposta para cada um."

### 2. Os quatro produtos e a nuvem de pontos (1:40 – 4:00)

**[TELA]** Slide 4 — galeria: nuvem de pontos, ortomosaico, MDS e MDT.

> "Da nuvem densa da Aula 5 saem quatro produtos principais: a nuvem de pontos, o ortomosaico, o MDS e o MDT. E eu quero que você guarde uma ideia desde já: cada um responde a uma pergunta diferente. A nuvem responde 'onde está cada coisa, em 3D?'. O ortomosaico responde 'onde está e quanto mede, em planta?'. E o MDS e o MDT respondem 'qual é a cota — e a cota de quê?'. Essa última parte, 'de quê', é a que mais dá problema. Usar o produto errado é a fonte mais comum de erro de medição que eu conheço."

**[TELA]** Slide 5 — nuvem de pontos: X, Y, Z e cor, formato LAS/LAZ e as classes.

> "Começando pela nuvem de pontos. Ela é um conjunto de milhões de pontos, cada um com coordenadas X, Y e Z e, na fotogrametria, com a cor do pixel de onde veio. Quando você gira a nuvem na tela, ela parece uma maquete fotográfica. A densidade típica de uma nuvem fotogramétrica é de centenas de pontos por metro quadrado e depende do GSD que você escolheu no planejamento."

> "O formato-padrão é o LAS, ou o LAZ, compactado. E ele tem um campo importantíssimo: a classe de cada ponto. Classe 2, solo. De 3 a 5, vegetação baixa, média e alta. 6, edificação. 7, ruído. 9, água. É essa classificação que vai permitir separar o terreno de tudo o que está em cima dele. Com a nuvem, você mede distâncias e alturas e extrai perfis e seções transversais."

### 3. Por que a foto não é mapa: o ortomosaico (4:00 – 6:45)

**[TELA]** Slide 6 — simulação: vista lateral e vista de cima do deslocamento devido ao relevo; clique em Ortorretificar quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com "Altura do prédio" em 30 m e "Distância ao centro da foto" em 40 m. Na fala "uns 17 metros no terreno", apontar "Topo projetado 17,1 m para fora da base" e a linha "Δ = x · h / (H − h) = 40 × 30 / (100 − 30)".
2. Na fala "Se eu levo o prédio para o nadir", arrastar "Distância ao centro da foto" até 0 m: "Topo projetado 0,0 m".
3. Na fala "se eu afasto e aumento a altura do prédio", arrastar "Distância ao centro da foto" até 60 m e "Altura do prédio" até 40 m: "Topo projetado 40,0 m".
4. Na fala "Volto para o nosso prédio", voltar "Altura do prédio" a 30 m e "Distância ao centro da foto" a 40 m (17,1 m de novo).
5. Na fala "Agora eu clico em Ortorretificar", clicar em "Ortorretificar": o raio verde desce reto, o resultado cai a "0,0 m" e a linha de baixo acrescenta "ortorretificado: Δ = 0".

> "Agora uma pergunta que parece boba: uma foto aérea vertical é um mapa? Não é. À esquerda, a vista lateral: a câmera a 100 metros de altura e um prédio de 30 metros, a 40 metros do nadir, que é o ponto bem embaixo da câmera. A câmera fotografa em perspectiva central: todos os raios passam pelo centro da lente. O raio azul vai até a base do prédio. O raio vermelho passa pelo topo e, prolongado até o chão, cai mais longe. Na foto, o telhado aparece deslocado para fora. Quanto? A fórmula está na tela: R vezes h, dividido por H menos h. Quarenta vezes 30, dividido por 70: uns 17 metros no terreno. É o deslocamento devido ao relevo."

> "Se eu levo o prédio para o nadir, o deslocamento some: zero. Se eu afasto e aumento a altura do prédio, ele cresce: com 40 metros de altura, a 60 metros do nadir, o topo vai parar 40 metros para fora da base. Volto para o nosso prédio, 30 metros a 40 do nadir. E não é só prédio: morro, talude, pilha, tudo que tem altura sofre esse efeito. Agora eu clico em Ortorretificar. O software usa o modelo de superfície para reprojetar cada ponto como se fosse visto na vertical. O raio verde desce reto, e o telhado volta para cima da base."

**[TELA]** Slide 7 — foto: ortofoto de uma obra ao redor de uma estação ferroviária: "A foto que vira mapa".

> "O ortomosaico é o mosaico das fotos ortorretificadas, costuradas numa imagem só, com escala constante. Nele, você mede distâncias e áreas como mediria numa planta, confere a locação de uma fundação e sobrepõe o projeto em CAD ou BIM. Esta ortofoto é de uma obra ao redor de uma estação ferroviária, na Alemanha: dá para ler as plataformas, os estacionamentos, as áreas de terra em execução. Para medir avanço físico — metros de pavimento, lajes, fachada —, é o produto preferido. Um detalhe: feito sobre o MDS, como nos softwares de drone, ele se aproxima de uma ortofoto verdadeira, mas as bordas de prédios e as copas podem sair borradas, porque ali o modelo de superfície é imperfeito. E repare: ortomosaico é planta. Não dá cota."

### 4. MDS × MDT, em 3D (6:45 – 9:30)

**[TELA]** Slide 8 — MDS × MDT: esquema em perfil com a linha da superfície e a do terreno.

> "Para cota, entram os dois produtos que mais causam confusão. O MDS, modelo digital de superfície, é a cota do primeiro obstáculo visto de cima: telhados, copas, máquinas, pilhas. No esquema, a linha vermelha por cima das casas. O MDT, modelo digital do terreno, é o solo nu, depois de filtrar o que não é terreno: a linha azul, por baixo das casas. MDS menos MDT dá a altura dos objetos, o modelo normalizado. Os dois são rasters, grades de cotas, em geral em GeoTIFF, com resolução de duas a cinco vezes o GSD."

**[TELA]** Slide 9 — cena 3D: o mesmo canteiro como cena real, nuvem, MDS, MDT e MDS − MDT; use os botões na ordem da fala.

Na tela (passo a passo do que clicar, na ordem):
1. A cena abre com o botão "Cena real" aceso (chip "Cena real: terreno, edifício, árvores, pilha e máquina") e gira sozinha. Apontar o edifício, as árvores, a pilha e a máquina na fala da descrição.
2. Na fala "Clico em Nuvem de pontos", clicar em "Nuvem de pontos" (chip "Nuvem de pontos: X, Y, Z + cor (14 mil pontos aqui)"); os rótulos da cena real somem.
3. Na fala "Agora MDS", clicar em "MDS" (chip "MDS: a primeira superfície vista de cima (cor = cota)"): o lençol colorido pela cota cobre prédio, copas e máquina.
4. Na fala "Clico em MDT", clicar em "MDT" (chip "MDT: só o solo, com a pilha"). Na fala "Mas a pilha ficou", arrastar para girar a cena até a pilha ficar de frente.
5. Na fala "E agora MDS menos MDT", clicar em "MDS − MDT" (chip "MDS − MDT: em vermelho, o que viraria volume falso"): prédio, copas e máquina em vermelho.

> "Vamos ver em 3D. Um canteiro ilustrativo de 120 por 120 metros: terreno ondulado, um edifício, um grupo de árvores, uma pilha de material e uma máquina. Clico em Nuvem de pontos: o mesmo canteiro como milhares de pontos coloridos. Agora MDS: um lençol estendido sobre tudo, por cima do prédio, das copas e da máquina. Clico em MDT. Prédio, árvores e máquina sumiram. Mas a pilha ficou. Por quê? Porque a pilha é material — é o que eu quero medir. Filtrar não é apagar tudo o que é alto; é decidir o que é terreno para a pergunta que você está fazendo. O OpenDroneMap faz isso com um filtro morfológico; o Metashape, com uma classificação por ângulo e distância. E sempre vale conferir."

> "E agora MDS menos MDT. Tudo em vermelho é o que viraria volume falso se você usasse o MDS. Imagine uma escavadeira parada em cima do corte no dia do voo: com o MDS, ela vira terra que ninguém escavou. Em terraplenagem com solo exposto, filtrar é fácil. Debaixo de mata densa, é impossível: a câmera simplesmente não vê o chão."

### 5. LiDAR: o chão debaixo da mata (9:30 – 12:45)

**[TELA]** Slide 10 — animação de um pulso: sobre solo exposto e sobre uma árvore. Comece em "Sobre uma árvore"; clique em "Sobre solo exposto" quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com o botão "Sobre uma árvore" aceso. Na fala "Olha a animação", acompanhar o pulso descendo de "drone a 80 m" e apontar os três ecos no gráfico "Intensidade do eco × tempo de ida e volta": "copa" (413 ns → 62 m), "galho" (467 ns → 70 m) e "chão" (533 ns → 80 m).
2. Na fala "Sobre solo exposto, um eco só", clicar em "Sobre solo exposto": um único eco, "chão", e a legenda "1 retorno: R = c·Δt/2 = 3×10⁸ × 533 ns / 2 ≈ 80 m".
3. Na fala "O primeiro retorno descreve a superfície", clicar de volta em "Sobre uma árvore" para mostrar de novo o primeiro e o último eco.

> "E aí entra o LiDAR, que você conheceu como sensor na Aula 2. Lembrando: ele emite pulsos de laser e mede o tempo de ida e volta; a distância é a velocidade da luz vezes o tempo, dividido por dois. Com o GNSS RTK ou PPK e uma unidade inercial de alta qualidade, cada pulso vira um ponto 3D. Agora o detalhe que resolve a encosta. O feixe chega lá embaixo com alguns centímetros de diâmetro. Olha a animação: o pulso desce do drone, a 80 metros, e encontra uma árvore. Parte da energia bate na copa e volta: primeiro eco, a 62 metros. Outra parte passa por um vão entre as folhas e bate num galho: segundo eco. E uma parte chega ao chão: último eco, a 80 metros, em 533 nanossegundos. Um pulso, três retornos. Sobre solo exposto, um eco só."

> "O primeiro retorno descreve a superfície: é o MDS. E o último, quando classificado como solo, permite o MDT debaixo da vegetação. Agora, um cuidado de vocabulário que derruba muita gente em prova: o laser não atravessa as folhas. Ele passa pelos vãos entre elas. Mata muito fechada deixa poucos pontos no chão."

**[TELA]** Slide 11 — cena 3D: a encosta com mata varrida pelo laser; alterne entre último e primeiro retorno.

Na tela (passo a passo do que clicar, na ordem):
1. Ao entrar no slide, clicar em "Recomeçar voo", para os pontos começarem a se acumular do zero durante a fala "os pontos vão se acumulando" (o chip "Pontos" volta perto de zero e sobe). O botão "Último retorno (MDT)" já vem aceso, com o chip "Último retorno: terreno (MDT)".
2. Na fala "No modo último retorno", deixar "Último retorno (MDT)" aceso: copas transparentes e o terreno colorido pela cota. Arrastar para girar até a clareira aparecer.
3. Na fala "Agora, primeiro retorno", clicar em "Primeiro retorno (MDS)": o chip passa a "Primeiro retorno: copa (MDS)", a nuvem desenha a copa em verde e o contador "Pontos" fica maior, porque todo pulso tem um primeiro eco.

> "Em três dimensões: uma encosta coberta de árvores, com uma clareira no meio. O drone emite um leque de feixes, uns 35 graus para cada lado, e os pontos vão se acumulando. No modo último retorno, as árvores ficam transparentes e aparece o terreno natural, colorido pela cota; sob as copas mais fechadas, há menos pontos. Repare no contador de pontos, no canto: no último retorno ele cresce mais devagar, porque só uma parte dos pulsos acha um vão até o chão. Agora, primeiro retorno: a nuvem desenha a copa, em verde. É o que a fotogrametria teria visto. Um mostra a mata; o outro, o chão onde a obra vai passar."

**[TELA]** Slide 12 — calculadora: largura da faixa, densidade e erro na borda; nuvem LiDAR real de edificações.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre já com os valores da fala: "Taxa de pulsos" 240 kHz, "Campo de visão" 70°, "Altura de voo" 80 m, "Velocidade" 8 m/s e "Erro de atitude da IMU" 0,05°. Não mexer nos controles.
2. Na fala "a faixa dá uns 112 metros e a densidade, uns 268 pontos por metro quadrado", apontar "Faixa W = 2H · tan(FOV/2): 112 m" e "Densidade ρ ≈ PRR / (v · W): 268 pontos/m²".
3. Na fala "na borda da faixa, a uns 97,7 metros", apontar "Distância na borda R = H / cos(FOV/2): 97,7 m" e "Erro na borda R · δθ: 8,5 cm", e as barras "Erro no nadir (H · δθ)" (7,0 cm) e "Erro na borda (R · δθ)" (8,5 cm).
4. No segundo parágrafo, apontar a foto da nuvem LiDAR real ao lado.

> "Quantos pontos por metro quadrado? A densidade é a taxa de pulsos dividida pela velocidade vezes a largura da faixa; e a largura é duas vezes a altura vezes a tangente da metade do campo de visão. Com 240 quilohertz, campo de 70 graus, 80 metros e 8 metros por segundo, a faixa dá uns 112 metros e a densidade, uns 268 pontos por metro quadrado, numa passada. E a exatidão depende da trajetória: na borda da faixa, a uns 97,7 metros, um erro de atitude de só cinco centésimos de grau desloca o ponto em 8,5 centímetros. Por isso o LiDAR embarcado exige uma IMU cara. E a conferência é a mesma da Aula 6: checkpoints e RMSE."

> "Depois do voo, a nuvem LiDAR também precisa ser processada. Primeiro, a trajetória é calculada com o GNSS em PPK e a IMU. Depois, as faixas sobrepostas são ajustadas entre si, para que um telhado medido em duas passadas não apareça duplicado, com alguns centímetros de diferença. E, por fim, a classificação: o software separa o solo, a vegetação e as edificações, usando aquelas classes do formato LAS. Debaixo da mata, sempre vale conferir a classificação em alguns perfis, porque um tronco caído ou uma pedra grande pode ser confundido com o chão."

**[TELA]** Slide 13 — tabela LiDAR × fotogrametria.

> "Então LiDAR é sempre melhor? Não. Solo sob vegetação e superfície sem textura: ponto para o LiDAR. Cor e ortomosaico: só a fotogrametria, a menos que o LiDAR tenha uma câmera auxiliar. E o custo do LiDAR é bem mais alto. Para terraplenagem em solo exposto, a fotogrametria costuma bastar. Escolha pelo problema, não pela moda."

### 6. Abrindo os produtos no QGIS (12:45 – 14:45)

**[TELA]** Slide 14 — tela do QGIS com um modelo digital de terreno sombreado.

> "E onde se analisa tudo isso? A ementa sugere o QGIS, que é livre e roda em qualquer computador. Ele abre, no mesmo projeto, o ortomosaico e o MDS ou MDT como camadas raster, e a nuvem LAS ou LAZ como camada de nuvem de pontos, inclusive em 3D. O fluxo básico tem cinco passos. Primeiro, definir o sistema de referência do projeto — por exemplo, SIRGAS 2000, UTM 23 Sul. Segundo, aplicar o sombreamento, o hillshade, ao MDT, para enxergar o relevo como na tela. Terceiro, medir distâncias e áreas sobre o ortomosaico. Quarto, traçar perfis com a ferramenta de perfil de elevação. E quinto, usar a calculadora raster para fazer o MDS menos o MDT."

> "Um aviso prático: ortomosaico é arquivo grande. Os 12 hectares da Aula 4, com GSD de 1,92 centímetro, dão uns 325 milhões de pixels: cerca de 1 gigabyte sem compressão. Use GeoTIFF compactado e crie pirâmides, senão o QGIS vai sofrer."

> "E antes de entregar qualquer produto, faça uma inspeção visual. No ortomosaico, procure as linhas de costura entre fotos que cortam um objeto ao meio, borrões nas bordas de prédios e manchas de reflexo em telhados e na água. No MDS, procure buracos e picos isolados, que são ruído. Na nuvem, gire a vista para o lado e veja se há uma 'camada fantasma' abaixo do terreno, sinal de pontos errados. Cinco minutos de inspeção evitam uma medição inteira contestada. E sobreponha sempre um ou dois checkpoints na tela: ver o alvo exatamente sobre a marca do ponto medido em campo é a confirmação mais simples de que o produto está no lugar."

### 7. Pausa para reflexão (14:45 – 16:45)

**[TELA]** Slide 15 — Pausa para reflexão: os três pedidos, que produto, que sensor e que cuidado.

> "Hora da pausa para reflexão. Volte aos três pedidos do começo. Para cada um, decida qual produto entregar, com que sensor e qual cuidado de processamento é crítico. A área executada sai do ortomosaico — mas a de uma laje alta, na borda da foto, sofre o deslocamento devido ao relevo se a ortorretificação for ruim. O volume da pilha exige um MDT em que a pilha fica e a pá carregadeira sai. E a encosta: vale contratar um LiDAR, mais caro, ou basta a fotogrametria nas clareiras e uma topografia complementar?"

> "Pare o vídeo e responda uma pergunta para cada caso: que erro custaria mais caro? Um erro de área de 2% na medição? Um volume de pilha superestimado por causa de uma máquina? Ou um acesso projetado sobre um terreno que é, na verdade, a copa das árvores, com cortes e aterros completamente errados? Pensar no custo do erro é o que define o produto e o sensor."

### 8. Atividade, síntese e prévia da Aula 8 (16:45 – 18:00)

**[TELA]** Slide 16 — atividade prática e pontos-chave.

> "Sua missão: baixe um conjunto de dados de exemplo já processado do OpenDroneMap — ortomosaico, MDS e nuvem. No QGIS, defina o sistema de referência, meça a área de um telhado no ortomosaico, trace um perfil sobre o MDS e gere o MDS menos MDT com a calculadora raster. Que objetos aparecem no modelo normalizado?"

> "Para levar: nuvem, ortomosaico, MDS e MDT respondem a perguntas diferentes; o ortomosaico corrige o deslocamento devido ao relevo; MDS menos MDT dá a altura dos objetos, e filtrar depende da pergunta; o LiDAR, com múltiplos retornos, dá o MDT sob vegetação; e o QGIS junta tudo."

**[TELA]** Slide 17 — encerramento.

> "Hoje a gente foi das fotos aos produtos. Na próxima aula, esses produtos viram metros cúbicos, curvas de nível e a resposta à pergunta mais cara da obra: o executado bate com o projeto? Te espero na Aula 8!"

---

## Roteiro da Videoaula 8 — "48.200 ou 46.900 m³? Quem tem razão na medição de terraplenagem por drone"

**Aula 8 — Cálculo de volumes, curvas de nível e comparação entre o projetado e o executado**

**Duração-alvo:** cerca de 18:50 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à oitava aula — a que fecha a Unidade 2. Você já sabe transformar fotos num modelo georreferenciado, provar a exatidão com checkpoints e gerar ortomosaico, MDS, MDT e nuvem de pontos. Hoje esses produtos viram decisão: quantos metros cúbicos se escavaram, como é o relevo e se o que foi executado bate com o projeto. É, de longe, o uso mais disputado do drone numa obra — disputado no sentido literal, porque é com esse número que se paga a empreiteira."

**[TELA]** Slide 3 — foto aérea de grandes pilhas de material: "Empreiteira: 48.200 m³. Fiscalização: 46.900 m³. E a plataforma está no greide?"

> "Imagina a cena. Fim do mês numa obra de terraplenagem. A empreiteira voa o drone e mede 48.200 metros cúbicos de corte. A fiscalização, com outro voo, encontra 46.900. São 1.300 metros cúbicos de diferença, algumas dezenas de milhares de reais na medição. E, na mesma reunião, a projetista pergunta se a plataforma do galpão já está no greide, dentro da tolerância. Quem errou? E como responder à projetista com segurança? No fim da aula, você vai ter argumentos de engenheiro para as duas perguntas."

### 2. Volume entre duas superfícies (1:30 – 4:15)

**[TELA]** Slide 4 — volume como soma de prismas e as três superfícies de referência.

> "O cálculo de volume tem uma ideia simples: dividir o terreno numa malha de células e, em cada célula, multiplicar a diferença de cota pela área. Volume é a soma de delta z vezes a área da célula. Na prática, o software faz isso com milhões de células, ou com prismas sobre uma triangulação. Contra o greide de projeto, onde o terreno está acima do greide, delta z é positivo: é corte a executar. Onde está abaixo, é aterro a executar. Contra o levantamento do mês anterior, a lógica se inverte: onde o terreno baixou, houve corte executado; onde subiu, aterro executado. E corte e aterro se calculam separados, porque são serviços diferentes, com preços diferentes."

> "A conta é simples. O que exige engenharia é escolher as duas superfícies. A referência pode ser o greide de projeto, quando você quer saber quanto ainda falta. O levantamento anterior, quando você quer saber quanto se movimentou no mês — a base da medição de pagamento; aí o delta z é anterior menos atual. Ou um plano de base, para o volume de uma pilha."

**[TELA]** Slide 5 — malha interativa de oito células contra o greide.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com "Viés vertical do modelo" em 0 cm: as oito células em vermelho (corte) e azul (aterro), com o perfil de barras sobre a linha "greide de projeto", e o resultado "Corte: 435 m³ · Aterro: 145 m³" e "Variação do volume líquido: +0 m³". Na fala das oito diferenças, apontar as células uma a uma; na fala "435 metros cúbicos" e "145 metros cúbicos", apontar o resultado.
2. Deixar o controle em 0 cm durante todo o slide: o viés é demonstrado no slide 8.

> "Vamos aos números. Uma plataforma comparada ao greide numa malha de células de 10 por 10 metros: 100 metros quadrados cada. Oito células, com as diferenças na tela: mais 1,40, mais 0,90, mais 0,35, menos 0,20, mais 1,10, mais 0,60, menos 0,45 e menos 0,80 metro. Em vermelho, corte; em azul, aterro. O corte é a soma dos positivos: 4,35 metros, vezes 100, 435 metros cúbicos. O aterro: 1,45 vezes 100, 145 metros cúbicos."

> "E o tamanho da célula importa? Importa. Célula grande demais suaviza o terreno e erra nas bordas de taludes e cristas; célula pequena demais só multiplica o processamento sem ganhar exatidão, porque o modelo não é melhor que o GSD e os checkpoints dizem. Na prática, os softwares usam a própria grade do MDT, com células de alguns centímetros, ou prismas sobre uma triangulação, que acompanham melhor as quebras do terreno. Para medição mensal, o que vale é usar sempre o mesmo método, com a mesma resolução, nas duas superfícies."

### 3. Pilhas, os três cuidados e o empolamento (4:15 – 5:55)

**[TELA]** Slide 6 — foto de pilhas num pátio de estocagem; três jeitos de definir a base da pilha.

> "Para uma pilha, a referência é a base, e aqui mora uma armadilha. A base pode ser um plano horizontal pelo ponto mais baixo do pé da pilha, um plano inclinado ajustado aos pontos do pé ou uma superfície triangulada por esses pontos. Num pátio com caimento, cada escolha dá um volume diferente. Por isso a base da pilha também precisa ser combinada."

**[TELA]** Slide 7 — três cuidados: MDT, mesmo referencial e empolamento; calculadora de viagens.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre já com os valores da fala: "Volume de corte (in situ)" 435 m³, "Empolamento" 25% e "Capacidade do caminhão" 12 m³. O primeiro parágrafo é dito apontando a lista dos três cuidados.
2. Na fala "435 vezes 1,25: uns 543,8 metros cúbicos", apontar "Volume solto: 543,8 m³" e as barras "In situ (medido)" e "Solto (no caminhão)".
3. Na fala "E número de viagens se arredonda para cima: 46", apontar "Viagens (para cima): 46 viagens" e a nota "543,8 / 12 = 45,3 → 46 viagens". Não é preciso mexer nos controles.

> "E três cuidados valem para qualquer volume. Primeiro: use o MDT, nunca o MDS — a máquina parada vira terra que ninguém escavou. Segundo: as duas superfícies precisam estar no mesmo referencial, horizontal e vertical. Lembra da Aula 6? Se um levantamento usou altura elipsoidal e o outro altitude, a diferença inteira vira volume. Terceiro: o empolamento. O drone mede o volume no corte, in situ. Escavado, o solo se solta e ocupa mais espaço no caminhão."

> "Se os 435 metros cúbicos de corte forem para o bota-fora, com 25% de empolamento, o volume solto é 435 vezes 1,25: uns 543,8 metros cúbicos. Com caminhões de 12, dá 45,3. E número de viagens se arredonda para cima: 46. Quem orça o transporte pelo volume in situ erra o número de caminhões em quase um quarto."

### 4. Incerteza do volume (5:55 – 6:55)

**[TELA]** Slide 8 — calculadora δV ≈ A · δz; leve o viés a 3 cm na malha de oito células quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre com "Área" em 800 m² (a malha de oito células) e "Viés vertical do modelo δz" em 0 cm. O primeiro parágrafo é dito sem mexer nos controles.
2. Na fala "se eu ponho um viés de 3 centímetros", arrastar "Viés vertical do modelo δz" até 3 cm: "δV ≈ A · δz: 24 m³" e "Na malha de 8 células: 5,5 % do corte de 435 m³".
3. Na fala "Num pátio de 2 hectares", arrastar "Área" até 20.000 m², mantendo o viés em 3 cm: "δV ≈ A · δz: 600 m³" e "Em caminhões de 12 m³: 50 viagens".

> "Agora, a parte mais importante para quem vai assinar uma medição. Os erros aleatórios de cota — uma célula um pouco mais alta, a vizinha um pouco mais baixa — tendem a se compensar numa área grande. Mas um viés, um erro sistemático que afeta o modelo inteiro, não se compensa. Ele vira volume diretamente: delta V é aproximadamente a área vezes o viés."

> "Na nossa malha, se eu ponho um viés de 3 centímetros, o volume líquido muda 800 metros quadrados vezes 0,03: 24 metros cúbicos, uns 5,5% do corte. Num pátio de 2 hectares, os mesmos 3 centímetros dão 600 metros cúbicos — uns 50 caminhões. É por isso que, nos checkpoints, a média dos resíduos importa tanto quanto o RMSE."

### 5. Curvas de nível (6:55 – 9:25)

**[TELA]** Slide 9 — mapa topográfico com curvas de nível; curvas mestras e intermediárias.

> "Agora, o segundo produto da aula: as curvas de nível. Curva de nível é uma linha que une pontos de mesma altitude. Elas são geradas a partir do MDT, com uma equidistância constante entre uma curva e a seguinte. A cada cinco curvas, uma é a mestra, mais grossa e cotada, para facilitar a leitura. E a distância horizontal entre curvas diz a declividade: equidistância dividida pela distância. Curvas próximas, terreno íngreme; afastadas, terreno suave. Duas curvas de meio metro separadas por 4 metros em planta: 0,5 dividido por 4, 12,5% de declividade."

**[TELA]** Slide 10 — interativo: o mesmo MDT com curvas de 0,10 m, 0,20 m e 0,50 m; ative a suavização quando a fala pedir.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com o botão "0,20 m" aceso: o chip diz "Eq = 0,20 m ≥ 15,4 cm: compatível com a Classe A" e "MDT bruto: ruído ≈ 2,6 cm". Apontar na fala "com curvas de 20 centímetros, o relevo aparece limpo".
2. Na fala "Agora eu baixo para 10 centímetros", clicar em "0,10 m": curvas serrilhadas e ilhas; o chip passa a "Eq = 0,10 m < 15,4 cm: desenha ruído".
3. Na fala "Eu ligo a suavização", clicar em "Suavizar MDT" (com "0,10 m" ainda aceso): as curvas ficam contínuas e o chip passa a "MDT suavizado: ruído ≈ 1,6 cm" (era 2,6 cm).
4. No último parágrafo (como se lê uma planta com curvas), clicar em "Suavizar MDT" de novo, para desligar, e em "0,20 m", voltando à leitura limpa.

> "E qual equidistância usar? Aqui a Aula 6 volta com tudo. Na Classe A do PEC-PCD, o RMSE vertical tem que ser no máximo um sexto da equidistância. Com o nosso RMSE de 2,56 centímetros, a equidistância precisa ser de pelo menos 15,4 centímetros: curvas de 20. Olha na tela: com curvas de 20 centímetros, o relevo aparece limpo. Agora eu baixo para 10 centímetros. Repare nas curvas serrilhadas, cheias de pequenas ilhas: isso não é relevo, é ruído do modelo desenhado como se fosse terreno. Curva de nível com equidistância menor que a exatidão é desenhar ruído."

> "E um segundo cuidado: o MDT costuma ser suavizado antes de gerar as curvas. Eu ligo a suavização: as curvas ficam contínuas, sem perder a forma do relevo. Mas suavizar demais apaga feições reais, como a crista de um talude. Mais uma decisão de engenharia."

> "E como se lê uma planta com curvas? Curvas em V apontando para as cotas mais altas indicam um vale, por onde a água escoa; em V apontando para as mais baixas, uma crista. Curvas fechadas e concêntricas são um morro ou uma depressão. Para a obra, a drenagem provisória e o acesso das máquinas saem dessa leitura — e, com o drone, essa planta se atualiza todo mês."

### 6. Projetado × executado (9:25 – 11:35)

**[TELA]** Slide 11 — mapa de desvios: MDT − superfície de projeto, em cores divergentes.

Na tela (passo a passo do que clicar, na ordem):
1. O slide abre com "Tolerância" em 5,0 cm: a plataforma dividida em três trechos pelas linhas tracejadas e o resultado "Dentro: 36% · falta cortar: 64% · falta aterrar: 1%". Na fala "Verde… Vermelho… Azul", apontar uma área de cada cor (o azul é a mancha pequena à esquerda).
2. Não é preciso mexer no controle: a tolerância de 5 cm é a mesma do slide 12.

> "Agora, a pergunta da projetista: a plataforma está no greide? Eu subtraio a superfície de projeto do MDT levantado e obtenho o mapa de desvios, também chamado de mapa de corte e aterro. Verde, dentro da tolerância. Vermelho, acima do greide: ainda falta cortar. Azul, abaixo: falta aterrar. Num relance, a equipe de campo sabe onde a motoniveladora precisa passar de novo."

> "E, para estruturas — um pilar, uma laje, uma parede de contenção —, a comparação é nuvem-modelo: a distância de cada ponto da nuvem à superfície do modelo de projeto, num programa como o CloudCompare, que é livre. Isso é a ponte para a integração com o BIM, que você vai ver na Aula 14."

**[TELA]** Slide 12 — a regra de decisão: conforme, inconclusivo e não conforme; calculadora e tabela dos três trechos da plataforma.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre com "Desvio médio medido" em 7 cm, "Tolerância" em 5 cm e "Incerteza da medição" em 3 cm (é o trecho 2). O primeiro parágrafo é dito apontando a tabela ao lado; "Tolerância" e "Incerteza da medição" não mudam durante o slide.
2. Na fala "Trecho 1, desvio médio de 2 centímetros": arrastar "Desvio médio medido" até 2 cm (passo de 0,5). Aparecem "Desvio − incerteza: -1,0 cm", "Desvio + incerteza: 5,0 cm" e, em destaque, "Decisão: conforme"; a barra "Desvio + U" fica da altura da barra "Tolerância".
3. Na fala "Trecho 2, 7 centímetros": arrastar de volta até 7 cm: 4,0 cm e 10,0 cm, e "Decisão: inconclusivo: medir de novo".
4. Na fala "Trecho 3, 12 centímetros": arrastar até 12 cm: 9,0 cm e 15,0 cm, e "Decisão: não conforme: a máquina volta"; agora até a barra "Desvio − U" passa da "Tolerância".

> "Mas aqui vem o ponto que separa a engenharia do palpite. O desvio medido tem incerteza. Então a regra de decisão defensável tem três saídas. Se o desvio mais a incerteza fica dentro da tolerância, conforme. Se o desvio menos a incerteza passa da tolerância, não conforme. E, no meio, inconclusivo: medir de novo, com método mais exato."

> "Vamos aplicar. Tolerância da plataforma, 5 centímetros; incerteza, 3 — valores ilustrativos, porque a tolerância real vem do projeto, da especificação de serviço ou do contrato. Trecho 1, desvio médio de 2 centímetros: 2 mais 3 dá 5, dentro: conforme. Trecho 2, 7 centímetros: 7 menos 3 dá 4, dentro, mas 7 mais 3 dá 10, fora. Inconclusivo. E a resposta não é aprovar por pouco: é medir de novo, com nivelamento ou estação total. Trecho 3, 12 centímetros: 12 menos 3 dá 9, fora mesmo descontando a incerteza. Não conforme: a máquina volta."

### 7. No QGIS e a medição de pagamento (11:35 – 14:30)

**[TELA]** Slide 13 — o fluxo no QGIS: calculadora raster, Volume de superfície raster, Contorno e perfil de elevação.

> "E tudo isso cabe no QGIS. A calculadora raster faz o delta z: MDT anterior menos MDT atual, para o que se movimentou no mês, ou MDT atual menos a superfície de projeto; com uma rampa de cores divergente, vira o mapa de desvios. O algoritmo Volume de superfície raster calcula corte e aterro em relação a um plano — ou, somando as células do delta z, entre duas superfícies. O algoritmo Contorno, do GDAL, gera as curvas de nível. E o perfil de elevação traça as seções transversais. A superfície de projeto vem do software de projeto viário ou de terraplenagem, exportada como raster ou como triangulação."

> "Três conselhos de quem já apanhou. Primeiro: as duas superfícies no mesmo sistema de referência e com a mesma resolução de célula; o QGIS reprojeta na tela, mas a calculadora raster precisa das grades alinhadas. Segundo: recorte as duas pelo mesmo polígono da frente de serviço, senão uma borda sem dados vira volume. Terceiro: guarde o polígono, as superfícies e os parâmetros junto com o relatório."

**[TELA]** Slide 14 — quem está certo? A diferença das duas medições comparada ao efeito do viés, e o que exigir no contrato.

Na tela (passo a passo do que clicar, na ordem):
1. A calculadora abre com os valores do gancho: "Área da frente" em 4 ha, "Viés vertical plausível" em 3 cm e "Diferença entre as medições" em 1.300 m³. Não é preciso mexer nos controles.
2. Na fala "A diferença é de 1.300 metros cúbicos, 2,8%": apontar "Diferença relativa: 2,8 %".
3. Na fala "ou seja, 1.200 metros cúbicos": apontar o número em destaque "Viés δz em A: 1.200 m³" e as barras "Diferença medida" (1.300 m³) e "Viés em um voo" (1.200 m³).
4. Na fala "uns 1.700 metros cúbicos": apontar "Dois voos (√2 · δV): 1.697 m³", a barra "Dois voos (√2)" e a linha "Leitura: cabe na incerteza: combine o método".
5. No segundo parágrafo, apontar a lista "O que exigir antes da 1ª medição", à esquerda.

> "E agora a briga do começo: 48.200 contra 46.900, numa frente de 4 hectares. A diferença é de 1.300 metros cúbicos, 2,8%. Faça a conta que você aprendeu: um viés de 3 centímetros em 4 hectares vale 40.000 vezes 0,03, ou seja, 1.200 metros cúbicos. Praticamente toda a diferença. E são dois voos, cada um com o seu viés; combinando os dois pela raiz da soma dos quadrados, a diferença pode chegar a uns 1.700 metros cúbicos."

> "Então, quem está certo? Talvez ninguém esteja errado: os dois números podem estar dentro da incerteza. E aí a discussão deixa de ser técnica e vira contratual. O que exigir, antes da primeira medição? A mesma superfície de referência para as duas partes: o primitivo, levantado no início da obra. MDT, e não MDS. Checkpoints independentes, com RMSE vertical e média dos resíduos no relatório. Data e hora do voo. Uma tolerância de volume acordada. E um procedimento de arbitragem para quando a diferença passar dela. Pare o vídeo um minuto e pense: na sua obra, quem faria o voo de referência? Medição sem método combinado é discussão garantida."

### 8. Laboratório: o voo desta semana no simulador da Torre A (14:30 – 16:45)

**[TELA]** Slide 15 — laboratório no simulador da obra Torre A, aberto na aba Drone e BIM (indicadores de avanço, tabela dos voos semanais e barras do avanço por serviço).

Na tela (passo a passo do que clicar, na ordem):
1. O simulador abre reiniciado na aba "Drone e BIM" (não é preciso clicar em "Iniciar": o voo não depende do relógio da obra). Na fala "Antes do voo desta semana", apontar os indicadores "Avanço medido: 38,7%", "Previsto (curva S): 45,0%", "Dito na reunião: 62%" e "IDP = VA/VP: 0,86", e, na tabela "Voos", a linha do topo: "09/11", "2,2 cm/px", "6", "2,9 cm", "44.600 m³", "38,7%" (ao lado do botão, o aviso "Último voo: 09/11.").
2. Na fala "Clico em Voar e processar o voo desta semana": clicar em "Voar e processar o voo desta semana". O simulador passa sozinho para a aba "Canteiro", e o ponto amarelo "drone" varre a planta em oito faixas, em cerca de 4 segundos. Esperar o ponto sumir.
3. Na fala "Volto à aba Drone e BIM": clicar na aba "Drone e BIM". A linha nova fica no topo da tabela: "16/11", "2,1 cm/px", "6", "2,3 cm", "46.900 m³", "40,8%"; o botão fica desabilitado e o aviso passa a "Voo de 16/11 processado: 46.900 m³ escavados (a planilha dizia 48.200)."
4. Na fala "o avanço medido sobe para 40,8%": apontar "Avanço medido: 40,8%", "VP · VA · CR (R$ mi): 9,00 · 8,15 · 8,60", "IDP = VA/VP: 0,91" e "IDC = VA/CR: 0,95"; descer até "Avanço físico ponderado" e mostrar as barras (executado / previsto): Fundações 100% / 100%, Estrutura 50% / 55%, Alvenaria 10% / 15% e Instalações 5% / 10%.

Atenção: o drone só avança enquanto a aba "Canteiro" está aberta; se voltar à aba "Drone e BIM" antes de ele sumir, o aviso fica em "Drone em voo (veja a aba Canteiro)…". O botão funciona uma vez: para repetir, clicar em "Reiniciar" ou sair do slide e voltar (o simulador reinicia sozinho, de novo com o último voo em 09/11).

> "Agora, a mesma conta numa obra que acompanha a disciplina inteira: a Torre A, no simulador. Estou na aba Drone e BIM. Antes do voo desta semana, o último levantamento é o de 9 de novembro: 44.600 metros cúbicos escavados e 38,7% de avanço medido, contra 45% previstos na curva S. IDP de 0,86. E repare no indicador em vermelho: na reunião, alguém disse que a obra estava com 62%."

> "Clico em Voar e processar o voo desta semana. O simulador me leva para a planta do canteiro, e o drone varre a obra em faixas paralelas, como no plano de voo da Aula 4. Volto à aba Drone e BIM. Linha nova no topo da tabela: 16 de novembro, GSD de 2,1 centímetros por pixel, 6 pontos de controle e RMSE de 2,3 centímetros. Volume escavado: 46.900 metros cúbicos. Os mesmos 46.900 do começo da aula; a planilha da obra dizia 48.200."

> "E repare na diferença entre os dois números. Os 46.900 saem de um voo com data, GSD, pontos de controle e erro conhecidos: dá para refazer a conta e auditar. A planilha preenchida de memória não tem nada disso. Com o voo, o avanço medido sobe para 40,8%, o valor agregado vai a 8,15 milhões de reais e o IDP melhora para 0,91. Ainda abaixo de 1: a obra continua atrasada, só que agora a gente sabe quanto, e com que exatidão. Nas barras, cada serviço com o executado contra o previsto: a estrutura está em 50% para 55% previstos. É assim que o número do drone entra no controle da obra."

### 9. Atividade, fechamento da unidade e prévia da Unidade 3 (16:45 – 18:50)

**[TELA]** Slide 16 — atividade prática e pontos-chave.

> "Sua missão: no QGIS, com um MDT de exemplo, gere curvas de nível de 0,5 e de 0,1 metro e decida qual é compatível com a exatidão do levantamento. Depois, crie um plano horizontal como greide de projeto, calcule o mapa de desvios e o volume de corte e aterro, e repita deslocando o plano 5 centímetros. Quanto mudou o volume? Compare com área vezes delta z. Você vai sentir na mão o peso do viés."

**[TELA]** Slide 17 — fechamento da Unidade 2: da foto ao número de engenharia.

> "E com isso fechamos a Unidade 2. Você aprendeu como fotos sobrepostas viram um modelo 3D com a fotogrametria; como o GNSS posiciona esse modelo e como provar a exatidão com RMSE e PEC-PCD; quais produtos saem do processamento, inclusive com o LiDAR; e como transformar esses produtos em volumes, curvas de nível e decisões de conformidade. Em todos os casos, a pergunta foi a mesma: quanto eu posso confiar neste produto, e que decisão ele sustenta?"

**[TELA]** Slide 18 — prévia da Unidade 3: sensores, plataformas embarcadas, redes e MQTT.

> "Na Unidade 3, o foco desce do céu para dentro do solo, da estrutura e do ar do canteiro. Os sensores para obras: inclinômetros, extensômetros, acelerômetros, temperatura, umidade e poeira. As plataformas embarcadas, como Arduino e ESP32, e a coleta de dados em campo. As redes de comunicação: LoRaWAN, Wi-Fi e redes celulares. E os protocolos e plataformas IoT, com o MQTT e o armazenamento de séries temporais. O drone mostra a obra por fora e em campanhas; os sensores contam o que acontece entre um voo e outro."

**[TELA]** Slide 19 — encerramento: "Unidade 2 concluída".

> "Foi um prazer voar com você nesta unidade. Te espero na Unidade 3, na Aula 9. Um abraço!"

---
