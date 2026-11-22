# Unidade 2 — Aquisição e Processamento de Imagens

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 5 a 8

## Aula 5 — Fotogrametria digital: sobreposição, pontos de controle e georreferenciamento

### O que você verá nesta unidade

Na Unidade 1, você aprendeu por que e como monitorar uma obra, conheceu os drones e seus sensores, a regulamentação brasileira e o planejamento de uma missão de voo. Agora o cartão de memória chegou ao escritório, cheio de fotos — e esta unidade trata do caminho **da imagem ao número de engenharia**. Você vai estudar a **fotogrametria digital** (como a sobreposição, os pontos de controle e o georreferenciamento transformam fotos num modelo 3D no lugar certo); o **posicionamento por GNSS** e a forma de **provar a exatidão** dos produtos cartográficos; os **ortomosaicos, modelos digitais de superfície e nuvens de pontos**, inclusive os gerados por LiDAR; e, por fim, o **cálculo de volumes**, as **curvas de nível** e a **comparação entre o projetado e o executado**. O fio condutor é uma pergunta que vale para toda a disciplina: **quanto eu posso confiar neste produto — e que decisão ele sustenta?**

> As cerca de 330 fotos do voo planejado na Aula 4 viraram um modelo 3D lindo: texturas nítidas, prédios vizinhos perfeitos. A topografia confere um marco de concreto no meio do canteiro e encontra **18 cm de diferença na cota**. O modelo está "certo" ou "errado"? Ele é **coerente por dentro** — as distâncias entre os objetos batem —, mas está todo **deslocado e levemente "embarrigado"**. Nesta aula você vai entender como fotos sobrepostas viram 3D, por que os **pontos de controle** existem e como **georreferenciar** o modelo de forma verificável.

### Da foto ao 3D: interseção de raios e colinearidade

**Fotogrametria** é a ciência de obter medidas confiáveis a partir de fotografias (Coelho e Brito, 2007). O princípio é a **interseção de raios**: cada pixel define um raio que sai do centro de perspectiva da câmera e passa pelo ponto do terreno. Uma foto só não basta, porque o ponto pode estar em qualquer lugar ao longo do raio; se o mesmo ponto aparece em duas ou mais fotos tiradas de posições diferentes, os raios se cruzam — e o ponto fica determinado em 3D.

A relação entre o ponto do terreno $(X, Y, Z)$, o centro da câmera $(X_0, Y_0, Z_0)$ e a coordenada $(x, y)$ na imagem são as **equações de colinearidade**:

$
x = -f\,\frac{r_{11}(X - X_0) + r_{12}(Y - Y_0) + r_{13}(Z - Z_0)}{r_{31}(X - X_0) + r_{32}(Y - Y_0) + r_{33}(Z - Z_0)}
\qquad
y = -f\,\frac{r_{21}(X - X_0) + r_{22}(Y - Y_0) + r_{23}(Z - Z_0)}{r_{31}(X - X_0) + r_{32}(Y - Y_0) + r_{33}(Z - Z_0)}
$

em que os $r_{ij}$ formam a matriz de rotação dada pelos ângulos de atitude $\omega$, $\varphi$ e $\kappa$. Os seis parâmetros $(X_0, Y_0, Z_0, \omega, \varphi, \kappa)$ de cada foto são a **orientação exterior**; a distância focal, o ponto principal e a distorção da lente formam a **orientação interior** (a calibração da câmera).

### Por que tanta sobreposição

Na Aula 4 você calculou o espaçamento entre faixas $d = W(1 - s_l)$; ao longo da faixa, a distância entre fotos consecutivas (a **base**) é $B = L(1 - s_f)$, em que $L$ é o lado da foto no sentido do voo. No voo da Aula 4 ($H = 70\,\mathrm{m}$, foto de $105 \times 70\,\mathrm{m}$, 80% frontal e 70% lateral), $B = 70 \times 0{,}2 = 14\,\mathrm{m}$ e $d = 31{,}5\,\mathrm{m}$: no canteiro de 12 ha ($400 \times 300\,\mathrm{m}$), cerca de 11 faixas × 30 fotos ≈ **330 fotos**. A fotogrametria explica **por que** se usam 75–80% de sobreposição frontal e 65–75% lateral. Primeiro, a **multiplicidade**: em média, cada ponto aparece em cerca de

$
n \approx \frac{1}{(1 - s_f)(1 - s_l)}
$

fotos — com 80% e 70%, umas 16. Mais raios por ponto significam **redundância**: uma foto borrada ou um ponto mal reconhecido não abrem buraco no modelo. Segundo, a **geometria de interseção**: a precisão vertical de um par de fotos piora com a razão $H/B$ (raios quase paralelos se cruzam mal). Com sobreposição alta, o mesmo ponto é visto também por fotos **distantes** entre si na faixa, com base efetiva grande — e é isso que dá boa precisão vertical.

![Ficha de 1918 do Arquivo Nacional dos Estados Unidos, intitulada Overlap photographs: aviões em várias alturas de voo, os cones das fotos sobre o terreno e uma tabela com o intervalo entre exposições, a área coberta e a distância percorrida para garantir a sobreposição, acima de uma faixa de fotos aéreas sobrepostas](https://upload.wikimedia.org/wikipedia/commons/1/15/111-SC-1893_-_Aerial_photography_-_Overlap_photographs_-_NARA_-_55165141.jpg)

### Structure from Motion, passo a passo

Na fotogrametria clássica, de avião, a orientação das câmeras era conhecida com bons instrumentos. Nos drones, o processamento usa o **SfM** (*Structure from Motion*), que resolve ao mesmo tempo a posição das câmeras e a forma do terreno:

1. **Detecção** — em cada foto, o algoritmo encontra milhares de feições distintivas (cantos, texturas), descritas por "assinaturas" como as do método SIFT.
2. **Correspondência** — as mesmas feições são reconhecidas em fotos diferentes (*pontos homólogos*); correspondências incoerentes com a geometria são descartadas.
3. **Ajustamento por feixes** (*bundle adjustment*) — um ajuste por mínimos quadrados das equações de colinearidade calcula, de uma vez, a orientação exterior de cada foto, a orientação interior da câmera (**autocalibração**) e as coordenadas dos pontos homólogos. Sai a **nuvem esparsa**.
4. **Densificação** (*multi-view stereo*) — com as câmeras orientadas, o software busca correspondências pixel a pixel e gera a **nuvem densa**, base dos produtos da Aula 7.

Superfícies **sem textura** (água, telhado metálico liso, laje nova e uniforme), **objetos em movimento** (máquinas, pessoas) e **vegetação densa** confundem a correspondência ou escondem o chão.

![Esquema do Structure from Motion visto de cima: um edifício em cinza e sete posições de câmera numeradas dispostas em arco à sua frente, cada uma fotografando o objeto de um ângulo diferente](https://upload.wikimedia.org/wikipedia/commons/c/ce/Sfm2.jpg)

### Georreferenciamento: indireto, direto e o efeito de domo

Só com as fotos, o SfM reconstrói a **forma**, mas não sabe **onde** ela está nem **qual o seu tamanho exato**. O GNSS de navegação do drone tem exatidão de metros. Há dois caminhos para amarrar o modelo ao sistema de referência (no Brasil, o **SIRGAS2000**):

- **Georreferenciamento indireto** — medir em campo **pontos de controle** visíveis nas fotos e incluí-los no ajustamento.
- **Georreferenciamento direto** — conhecer com exatidão centimétrica a posição de cada foto, por **GNSS RTK ou PPK** embarcado (Aula 6).

Sem nenhum dos dois, além do deslocamento, aparece o **efeito de domo** (*doming*): pequenos erros de calibração da lente, que o ajustamento não consegue separar da forma do terreno, curvam o modelo como uma tigela virada. É típico de blocos com fotos todas verticais e paralelas (James e Robson, 2014). Pontos de controle bem distribuídos e algumas **fotos oblíquas** travam a calibração e reduzem o domo.

### Pontos de controle (GCP) e pontos de verificação

**Pontos de controle** (GCP, *ground control points*) são alvos bem visíveis nas fotos — placas em xadrez, cruzes pintadas — cujas coordenadas são medidas com **GNSS RTK ou estação total**. Na prática, o alvo deve ocupar **dezenas de pixels** (um alvo de 60 cm, com GSD de 2 cm, tem cerca de 30 pixels de lado).

![Ponto de controle no terreno: um alvo quadrado em laranja e branco fixado no chão de cascalho, ao lado de uma estação GNSS com painel solar e de um receptor em tripé, numa paisagem vulcânica da Islândia](https://upload.wikimedia.org/wikipedia/commons/f/f3/Ground_control_point_in_Iceland_%28GCP%29.jpg)

**Pontos de verificação** (*checkpoints*) são medidos da mesma forma, mas **não entram no processamento**: servem só para conferir o resultado. Usar os mesmos pontos para ajustar e para verificar é como o aluno corrigir a própria prova. Boa prática: GCPs no **perímetro e no interior**, cobrindo pontos altos e baixos, e checkpoints independentes espalhados pela área. Com georreferenciamento direto, os GCPs podem ser poucos — os checkpoints, **nunca** zero.

### O processamento no OpenDroneMap e no Metashape

O fluxo é o mesmo nos dois programas mais usados: o **OpenDroneMap** (livre, com a interface WebODM) e o **Agisoft Metashape** (comercial). (1) importar as fotos com suas posições; (2) alinhar — o SfM com ajustamento; (3) marcar os GCPs nas fotos (no ODM, por um arquivo de coordenadas; no Metashape, clicando os alvos) e reotimizar a câmera; (4) gerar nuvem densa, MDS e ortomosaico; (5) ler o **relatório de qualidade**. Três números do relatório merecem atenção: o **erro de reprojeção** (em geral abaixo de 1 pixel), o **erro nos GCPs** e, sobretudo, o **erro nos checkpoints** — que é o único que mede a exatidão de verdade.

### Exemplo numérico

O voo da Aula 4 tem $H = 70\,\mathrm{m}$, GSD de $1{,}92\,\mathrm{cm}$, base $B = 14\,\mathrm{m}$ e sobreposições de 80% e 70%. A multiplicidade média é

$
n \approx \frac{1}{0{,}2 \times 0{,}3} \approx 16{,}7\ \mathrm{fotos\ por\ ponto}
$

Para a precisão vertical de um par, use a aproximação $\sigma_Z \approx (H/B) \cdot GSD \cdot \sigma_{px}$, com precisão de medição de $\sigma_{px} = 0{,}5$ pixel (valor ilustrativo):

$
\sigma_Z^{\,1-2} \approx \frac{70}{14} \times 1{,}92 \times 0{,}5 = 4{,}8\,\mathrm{cm}
$

Com 80% de frontal, cada ponto aparece em cerca de 5 fotos seguidas da faixa; as duas mais distantes estão a $4B = 56\,\mathrm{m}$:

$
\sigma_Z^{\,1-5} \approx \frac{70}{56} \times 1{,}92 \times 0{,}5 = 1{,}2\,\mathrm{cm}
$

A sobreposição alta **quadruplica** a base efetiva e reduz a incerteza vertical a um quarto — e o ajustamento ainda combina todos os raios. Por fim, um alvo de $60\,\mathrm{cm}$ ocupa $60/1{,}92 \approx 31$ pixels de lado: fácil de marcar com precisão de fração de pixel.

### Atividade prática

Baixe um conjunto de dados de exemplo do OpenDroneMap que traga arquivo de GCPs. Processe-o duas vezes no WebODM: **sem** e **com** os GCPs, reservando dois ou três alvos como checkpoints. Compare, nos relatórios, o erro de reprojeção e os resíduos nos checkpoints. O que muda? O modelo sem GCPs é preciso? É exato?

### Pontos-chave

- Fotogrametria determina pontos 3D pela **interseção de raios** (equações de colinearidade); cada foto tem orientação **exterior** (posição e atitude) e a câmera, orientação **interior** (calibração).
- A sobreposição alta dá **redundância** (cerca de 16 fotos por ponto com 80/70%) e **base efetiva grande**, que melhora a precisão vertical.
- O **SfM** detecta feições, faz a correspondência, o **ajustamento por feixes** (com autocalibração) e a densificação.
- Georreferenciamento **indireto** (GCPs) ou **direto** (RTK/PPK); sem eles, o modelo fica deslocado e com **efeito de domo**.
- **GCPs** amarram; **checkpoints** independentes provam — e o erro nos checkpoints é o número que importa no relatório.

### Para saber mais

- **COELHO, L.; BRITO, J. N. *Fotogrametria digital*. 2. ed. Rio de Janeiro: EdUERJ, 2007** — capítulos de orientação interior e exterior, colinearidade e fototriangulação (bibliografia básica da disciplina).
- **Wikipedia — Structure from motion:** https://en.wikipedia.org/wiki/Structure_from_motion
- **JAMES, M. R.; ROBSON, S. — *Mitigating systematic error in topographic models derived from UAV and ground-based image networks* (efeito de domo; acesso aberto):** https://doi.org/10.1002/esp.3609
- **OpenDroneMap — documentação (processamento, GCPs e conjuntos de dados de exemplo):** https://docs.opendronemap.org/
- **Agisoft — manuais do Metashape:** https://www.agisoft.com/downloads/user-manuals/

## Aula 5 — Roteiro da Videoaula 5: "Como 330 fotos viram um modelo 3D — e por que ele pode estar 18 cm fora do lugar?"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–4 — capa, sumário, "o que você verá nesta unidade" e os 18 cm na cota de um marco.

> "As 330 fotos do plano da Aula 4 viraram um modelo 3D lindo. Aí a topografia confere um marco no meio do canteiro: 18 centímetros de diferença na cota. O modelo está certo ou errado? Hoje a gente vai entender como fotos sobrepostas viram 3D e como amarrar esse modelo ao terreno de um jeito que dá para provar."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 5–8 — interseção de raios, colinearidade, multiplicidade e a base efetiva.

> "O princípio é a interseção de raios: cada pixel define um raio, e o mesmo ponto visto em várias fotos fica onde os raios se cruzam. A matemática são as equações de colinearidade, com a orientação exterior de cada foto e a calibração da câmera. E é aqui que a sobreposição da Aula 4 se justifica: com 80 e 70%, cada ponto aparece em umas 16 fotos. Com um par vizinho, a precisão vertical seria de uns 4,8 centímetros; com as fotos mais distantes da faixa, cai para 1,2."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 9–12 — os 4 passos do SfM, onde ele tropeça, georreferenciamento indireto × direto e o efeito de domo em 3D.

> "O Structure from Motion detecta feições, encontra os pontos homólogos, faz o ajustamento por feixes — que calcula câmeras, calibração e a nuvem esparsa — e densifica. Mas só com as fotos ele não sabe onde o modelo está, e ainda pode embarrigar: é o efeito de domo. Para amarrar, dois caminhos: pontos de controle no terreno, o georreferenciamento indireto, ou a posição exata de cada foto por RTK ou PPK, o direto."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 13–16 — GCP × checkpoint, a distribuição dos alvos, o fluxo no OpenDroneMap e no Metashape e o relatório de qualidade.

> "Os GCPs são alvos medidos em campo que entram no ajustamento; os checkpoints são medidos igual, mas não entram: servem para provar. Usar os mesmos pontos é corrigir a própria prova. No OpenDroneMap ou no Metashape, o fluxo é importar, alinhar, marcar os alvos, gerar os produtos e ler o relatório. E no relatório, o número que manda é o erro nos checkpoints, não o erro de reprojeção."

### 5. Encerramento
**[TELA]** Slides 17–18 — atividade e pontos-chave, e encerramento.

> "Processe um conjunto de exemplo com e sem pontos de controle e compare os checkpoints. Na próxima aula, a gente abre a caixa-preta do GNSS: de onde vêm os erros, RTK ou PPK, e como provar, com RMSE e PEC-PCD, a exatidão de um produto. Te espero na Aula 6!"

---

## Aula 6 — Posicionamento por GNSS e precisão dos produtos cartográficos

> O drone com RTK mostrou "FIX" o voo inteiro. O ortomosaico ficou impecável, as distâncias internas batiam com a trena. Mas, ao sobrepor o projeto, **a obra inteira estava 1,5 m ao lado e 2,8 m acima** do lugar. A base GNSS tinha sido instalada sobre um ponto cujas coordenadas vieram do próprio receptor, em modo autônomo. O levantamento era **preciso** — e **inexato**. Nesta aula você vai entender como o GNSS mede posição, de onde vêm os erros, a diferença entre **RTK e PPK**, o que é altitude no Brasil e como se prova, com **RMSE** e **PEC-PCD**, a exatidão de um produto cartográfico.

### Como o GNSS mede posição

**GNSS** (*Global Navigation Satellite System*) é o nome genérico das constelações de navegação por satélite: o **GPS** (EUA), o **GLONASS** (Rússia), o **Galileo** (União Europeia) e o **BeiDou** (China). Cada satélite transmite sinais com a hora de um relógio atômico e sua órbita. O receptor mede o tempo de propagação e calcula a **pseudodistância** $\rho = c \cdot \Delta t$ — "pseudo" porque o relógio do receptor, barato, não está sincronizado: um erro de 1 µs vale $3 \times 10^8 \times 10^{-6} = 300\,\mathrm{m}$. Por isso são necessários **pelo menos 4 satélites**: três incógnitas de posição e uma de relógio. Receptores geodésicos medem também a **fase da onda portadora**, com resolução milimétrica — mas com um número inteiro de ciclos desconhecido, a **ambiguidade** (Monico, 2008).

![Representação tridimensional da constelação GPS: a Terra no centro, cercada pelos planos orbitais inclinados com os satélites distribuídos ao longo deles](https://upload.wikimedia.org/wikipedia/commons/e/e2/GPS-constellation-3D-NOAA.jpg)

### Fontes de erro e geometria (DOP)

No posicionamento **autônomo** (um receptor sozinho, como o do drone e do celular), somam-se: erros de **órbita e relógio** dos satélites; o atraso na **ionosfera**, em geral o maior deles; o atraso na **troposfera**; o **multicaminho** (sinal refletido em paredes, estruturas metálicas, máquinas e água); e o ruído e o centro de fase da antena do receptor. A geometria dos satélites multiplica tudo: $\sigma_{pos} \approx PDOP \cdot \sigma_{UERE}$, em que o **PDOP** (diluição da precisão) cresce quando os satélites estão agrupados num canto do céu. Resultado típico: **erro de metros**.

Dois cuidados bem brasileiros e bem de canteiro: o Brasil fica sob a **anomalia equatorial de ionização**, e em períodos de alta atividade solar a **cintilação ionosférica**, sobretudo do pôr do sol à madrugada, derruba sinais e soluções RTK; e o canteiro é um ambiente de **multicaminho e obstrução** — gruas, fachadas, formas metálicas. Use máscara de elevação (10° a 15°) e instale a base longe de superfícies refletoras.

### Posicionamento relativo: RTK e PPK

Erros de órbita, relógio e atmosfera são quase iguais para dois receptores próximos. No **posicionamento relativo**, uma **base** em coordenadas conhecidas e um **rover** (o drone ou o bastão do topógrafo) observam os mesmos satélites; as diferenças cancelam a maior parte dos erros e permitem resolver a ambiguidade da fase. Com a ambiguidade resolvida, a solução é **fixa** (*FIX*, centímetros); sem ela, **flutuante** (*FLOAT*, decímetros). A precisão degrada com a distância à base — fichas técnicas expressam isso como, por exemplo, $8\,\mathrm{mm} + 1\,\mathrm{ppm}$ na horizontal.

- **RTK** (*real time kinematic*) — as correções chegam **durante** o voo, por rádio de uma base local ou pela internet (protocolo **NTRIP**), de uma rede de estações — como a **RBMC-IP**, do IBGE.
- **PPK** (*post-processed kinematic*) — o drone grava os dados brutos e a correção é calculada **depois**, com os dados de uma base local ou de uma estação da **RBMC** (Rede Brasileira de Monitoramento Contínuo). Não depende de enlace durante o voo e permite reprocessar.

![Topógrafo de colete refletivo segura um bastão com receptor GNSS no topo e consulta a coletora de dados, sobre um pavimento, medindo a coordenada de um ponto com correção RTK](https://upload.wikimedia.org/wikipedia/commons/b/be/Surveyor_Using_GNSS_Receiver_with_RTK_Solution.jpg)

**O erro da base vira erro de todo o levantamento.** No posicionamento relativo, o rover é calculado *em relação* à base; se a coordenada da base estiver errada, tudo se desloca junto — foi o caso do gancho. A coordenada da base deve vir de um vértice conhecido, de pós-processamento com a RBMC ou do serviço **IBGE-PPP** (posicionamento por ponto preciso, com algumas horas de rastreio). No drone, há ainda o **sincronismo** (um atraso de 20 ms a 6 m/s desloca a foto 12 cm) e o **braço de alavanca** entre a antena e a câmera — razões a mais para nunca dispensar os checkpoints.

### Referenciais, projeção e altitudes

O sistema geodésico oficial do Brasil é o **SIRGAS2000**. Para trabalhar em planta, usa-se em geral a projeção **UTM** (no Sudeste, por exemplo, o fuso 23S, EPSG:31983). Atenção: a UTM tem fator de escala de 0,9996 no meridiano central, ou seja, 1 km medido no terreno pode aparecer como 999,6 m na planta; obras extensas usam sistemas topográficos locais (ABNT NBR 14166).

E a altitude. O GNSS entrega a **altura elipsoidal** $h$, medida sobre o elipsoide, uma superfície matemática. Projetos usam a **altitude** ligada ao nível médio do mar (ortométrica ou normal), $H$. A diferença é a **ondulação geoidal** $N$:

$
H \approx h - N
$

No Brasil, $N$ chega a dezenas de metros e é obtido dos modelos do IBGE (o MAPGEO2015 e o hgeoHNOR2020). Muitos aplicativos de drone gravam altura elipsoidal ou referida a um modelo global: confira **sempre** o referencial vertical antes de comparar com o projeto.

![Estação de referência GNSS de operação contínua: uma antena geodésica sob cúpula no topo de um pilar alto, sobre um gramado com céu aberto, ao lado de uma edificação baixa — o tipo de estação que compõe redes como a RBMC](https://upload.wikimedia.org/wikipedia/commons/b/bb/SDFE_GNSS_reference_station_Esbjerg%2C_2020-09-12.jpg)

### Precisão, exatidão e RMSE

**Precisão** é a dispersão de medidas repetidas; **exatidão** é a proximidade do valor verdadeiro. O gancho é o caso extremo: dispersão de centímetros, erro de metros. A exatidão de um produto é avaliada em **pontos de verificação** independentes, medidos com método pelo menos várias vezes mais exato, pelo **RMSE** e pela **média** dos resíduos (que denuncia o viés):

$
RMSE_z = \sqrt{\frac{1}{n}\sum_{i=1}^{n} \left(z_{modelo,i} - z_{campo,i}\right)^2}
\qquad
RMSE_r = \sqrt{RMSE_x^2 + RMSE_y^2}
$

### Padrões de exatidão: PEC-PCD e ASPRS

No Brasil, os produtos são classificados pelo **PEC-PCD** (Padrão de Exatidão Cartográfica dos Produtos Cartográficos Digitais), com base no **Decreto nº 89.817/1984** e na especificação técnica de controle de qualidade da Diretoria de Serviço Geográfico do Exército (ET-CQDG). Para cada escala e classe (A, B, C, D), há dois limites: **90% dos pontos** devem ter erro até o **PEC** e o **erro-padrão** (o RMSE) deve ficar até o **EP**. Na planimetria, a Classe A tem $PEC = 0{,}28\,\mathrm{mm}$ e $EP = 0{,}17\,\mathrm{mm}$ na escala da carta; na altimetria, $PEC = 0{,}27$ e $EP = 1/6$ da **equidistância das curvas de nível**. O padrão americano **ASPRS** (2ª edição, 2023) reporta a exatidão pelo próprio RMSE e pede no mínimo **30 checkpoints** para a avaliação completa. Como ordem de grandeza, um bom levantamento com drone atinge **1 a 2 GSD na horizontal e 1,5 a 3 GSD na vertical**.

### Exemplo numérico

**(a) Do metro ao centímetro.** No modo autônomo, com $PDOP = 2$ e $\sigma_{UERE} = 2\,\mathrm{m}$ (ilustrativos), $\sigma_{pos} \approx 4\,\mathrm{m}$. Em RTK com ficha de $8\,\mathrm{mm} + 1\,\mathrm{ppm}$ (H) e $15\,\mathrm{mm} + 1\,\mathrm{ppm}$ (V), a $12\,\mathrm{km}$ da base: $8 + 12 = 20\,\mathrm{mm}$ na horizontal e $15 + 12 = 27\,\mathrm{mm}$ na vertical.

**(b) Altitude.** Um checkpoint tem $h = 742{,}35\,\mathrm{m}$ e $N = -5{,}20\,\mathrm{m}$ (ilustrativo): $H = 742{,}35 - (-5{,}20) = 747{,}55\,\mathrm{m}$. Confundir $h$ com $H$ geraria um "erro" de 5,20 m.

**(c) Classificação.** O voo da Aula 4 (GSD de 1,92 cm), com RTK e 6 GCPs, foi conferido em 5 checkpoints. Resíduos (modelo − campo), em cm:

| Ponto | $\Delta x$ | $\Delta y$ | $\Delta z$ |
| --- | --- | --- | --- |
| CP1 | +1,2 | −0,8 | +2,1 |
| CP2 | −0,9 | +1,5 | −3,0 |
| CP3 | +2,0 | +0,4 | +1,8 |
| CP4 | −1,1 | −1,6 | −2,4 |
| CP5 | +0,6 | +0,9 | +3,2 |

$
RMSE_r = \sqrt{1{,}25^2 + 1{,}13^2} \approx 1{,}69\,\mathrm{cm} \approx 0{,}9\,GSD
\qquad
RMSE_z = \sqrt{\frac{32{,}65}{5}} \approx 2{,}56\,\mathrm{cm} \approx 1{,}3\,GSD
$

A média de $\Delta z$ é $+0{,}34\,\mathrm{cm}$: sem viés relevante. Na escala 1:500, a Classe A planimétrica pede $EP = 0{,}17 \times 500 = 85\,\mathrm{mm}$ e $PEC = 140\,\mathrm{mm}$: atende com folga. Na altimetria, a Classe A exige $Eq \ge 6 \times RMSE_z \approx 15{,}4\,\mathrm{cm}$: **curvas de 0,20 m** ($EP = 3{,}3\,\mathrm{cm}$; $PEC = 5{,}4\,\mathrm{cm}$, e todos os resíduos ficam abaixo). Ressalva: 5 pontos são ilustrativos; a classificação formal segue o tamanho de amostra da especificação.

### Atividade prática

Baixe, no portal do IBGE, os dados de um dia de uma estação da RBMC próxima da sua cidade e submeta uma hora de dados ao **IBGE-PPP**. Compare a coordenada obtida com a coordenada oficial da estação. Depois, consulte a ondulação geoidal no MAPGEO2015 para o mesmo ponto e converta a altura elipsoidal em altitude.

### Pontos-chave

- O GNSS mede **pseudodistâncias** (e a fase da portadora); são necessários **4 satélites** por causa do relógio do receptor.
- Erros de órbita, relógio, **ionosfera** (crítica no Brasil), troposfera e **multicaminho**, multiplicados pelo **DOP**, deixam o modo autônomo em metros.
- **RTK** (tempo real, rádio ou NTRIP) e **PPK** (pós-processado, base local ou RBMC) chegam ao centímetro com solução **fixa**; o **erro da base** desloca todo o levantamento.
- SIRGAS2000, UTM e **altitude**: $H \approx h - N$, com $N$ dos modelos do IBGE.
- A exatidão se prova em **checkpoints**, com **RMSE e média**; no Brasil, classifica-se pelo **PEC-PCD** (90% até o PEC e RMSE até o EP).

### Para saber mais

- **MONICO, J. F. G. *Posicionamento pelo GNSS: descrição, fundamentos e aplicações*. 2. ed. São Paulo: Editora UNESP, 2008** — fundamentos, erros e métodos de posicionamento (bibliografia complementar da disciplina).
- **IBGE — Serviço on-line de pós-processamento de dados GNSS (IBGE-PPP):** https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16334-servico-online-para-pos-processamento-de-dados-gnss-ibge-ppp.html
- **Wikipedia — Real-time kinematic positioning:** https://en.wikipedia.org/wiki/Real-time_kinematic_positioning
- **LiDAR Magazine — *The ASPRS Positional Accuracy Standards, Edition 2* (resumo das mudanças de 2023):** https://lidarmag.com/2023/10/06/the-asprs-positional-accuracy-standards-edition-2/

## Aula 6 — Roteiro da Videoaula 6: "O drone dizia 'FIX', mas a obra inteira estava 1,5 metro ao lado: o que o GNSS não te conta"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–3 — capa, sumário e o ortomosaico perfeito, 1,5 m ao lado e 2,8 m acima do projeto.

> "O drone mostrou FIX o voo inteiro, o ortomosaico ficou impecável e as distâncias batiam com a trena. Mas a obra inteira estava um metro e meio ao lado e quase três metros acima. Hoje a gente abre a caixa-preta do GNSS e aprende a provar, com números, que um produto está no lugar certo."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 4–7 — as quatro constelações, a pseudodistância e os 4 satélites, as fontes de erro e o PDOP no céu simulado.

> "O receptor mede pseudodistâncias: tempo de propagação vezes a velocidade da luz. Um microssegundo de erro no relógio são 300 metros — por isso, quatro satélites. Somam-se órbitas, relógios, ionosfera, troposfera e multicaminho, multiplicados pela geometria, o PDOP. Resultado: metros."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 8–11 — a ionosfera equatorial e o multicaminho no canteiro, posicionamento relativo (FIX × FLOAT), RTK × PPK (NTRIP, RBMC) e o erro da base que desloca tudo.

> "No Brasil a ionosfera pesa mais, por causa da anomalia equatorial; no canteiro, grua e fachada geram multicaminho. No posicionamento relativo, base e rover veem os mesmos satélites e os erros comuns se cancelam. Resolvida a ambiguidade da fase, a solução é fixa, de centímetros. O RTK corrige em tempo real, por rádio ou NTRIP; o PPK corrige depois, com uma base local ou a RBMC. Mas o rover é calculado em relação à base: base errada, levantamento inteiro errado. Foi o gancho."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 12–16 — SIRGAS2000 e UTM, altura elipsoidal × altitude, RMSE e média, PEC-PCD e a tabela dos 5 checkpoints.

> "O referencial é o SIRGAS2000; a altitude do projeto não é a altura elipsoidal do GNSS: a diferença é a ondulação geoidal, que no Brasil chega a dezenas de metros. A exatidão se prova nos checkpoints, com RMSE e média. No exemplo, 1,69 centímetro na horizontal e 2,56 na vertical, sem viés: Classe A do PEC-PCD na escala 1:500 e curvas de nível de 20 centímetros."

### 5. Encerramento
**[TELA]** Slides 17–18 — atividade e pontos-chave, e encerramento.

> "Submeta dados da RBMC ao IBGE-PPP e converta uma altura elipsoidal em altitude. Na próxima aula, com o modelo no lugar certo, a gente gera ortomosaico, MDS, MDT e nuvem de pontos — e vê o laser que enxerga o chão debaixo da mata. Te espero na Aula 7!"

---

## Aula 7 — Ortomosaicos, modelos digitais de superfície e nuvens de pontos

> Três pedidos chegam na segunda-feira. O planejamento quer **a área de laje e de pavimento executada** no mês. A suprimentos quer o **volume da pilha de brita**. E a projetista do acesso quer **o terreno natural de uma encosta coberta de mata** — e a fotogrametria da semana passada só "viu" a copa das árvores. Todos dizem "me manda o levantamento do drone". Mas **qual produto**? Nesta aula você vai conhecer o que sai do processamento — **nuvem de pontos, ortomosaico, MDS e MDT** —, o papel do **LiDAR** e como abrir e analisar tudo isso no **QGIS**.

### Os produtos de um levantamento

Da nuvem densa (Aula 5) saem quatro produtos principais: a **nuvem de pontos**, o **ortomosaico**, o **MDS** e o **MDT**. Cada um responde a uma pergunta diferente: a nuvem, "onde está cada coisa em 3D?"; o ortomosaico, "onde está e quanto mede em planta?"; o MDS e o MDT, "qual a cota — e a cota **de quê**?". Usar o produto errado é a fonte mais comum de erro de medição.

### Nuvem de pontos

A **nuvem de pontos** é um conjunto de milhões de pontos com coordenadas $X, Y, Z$ e, na fotogrametria, a cor RGB de cada um. É o produto mais rico: permite medir distâncias e alturas, extrair perfis e seções e **classificar** os pontos. O formato-padrão é o **LAS** (ou o compactado **LAZ**), cujas classes incluem solo (2), vegetação baixa, média e alta (3 a 5), edificação (6), ruído (7) e água (9). A densidade de uma nuvem fotogramétrica é da ordem de centenas de pontos por metro quadrado e depende do GSD.

![Modelo 3D georreferenciado, com textura fotográfica, de uma área de rochas avermelhadas, estradas de terra e vegetação rasteira, gerado a partir de imagens aéreas de drone](https://upload.wikimedia.org/wikipedia/commons/9/9e/Geo-Referenced_Point_Cloud.JPG)

### Ortomosaico: a foto que vira mapa

Uma foto aérea **não é um mapa**. Na perspectiva central, um objeto com altura $h$, com a base a uma distância radial $R$ do nadir (medida no terreno), tem o topo projetado para fora da base (**deslocamento devido ao relevo**):

$
\delta = \frac{R \cdot h}{H - h}
$

e a escala da foto varia com a cota do terreno. A **ortorretificação** reprojeta cada pixel sobre o modelo de superfície, como se cada ponto fosse visto na vertical; o **ortomosaico** é o mosaico dessas fotos. Resultado: **escala constante**, em que se medem distâncias e áreas e se sobrepõe o projeto em CAD ou BIM — o produto preferido para **avanço físico** e conferência de locação. Feito sobre o MDS, como nos softwares de drone, ele se aproxima de uma **ortofoto verdadeira**; bordas de prédios e copas podem mostrar "borrões", porque o MDS ali é imperfeito.

![Ortofoto feita por drone de um trecho em obras ao redor de uma estação ferroviária em Eggolsheim, Alemanha: linhas férreas e plataformas no centro, edifício com telhado laranja e painéis solares, estacionamentos, ruas e áreas de terra em execução](https://upload.wikimedia.org/wikipedia/commons/2/2e/Eggolsheim_Bahnhof_Baustelle_Orthophoto-20240428-RM-165210.jpg)

### MDS e MDT: superfície × terreno

O **MDS** (modelo digital de superfície) representa a cota do **primeiro obstáculo** visto de cima: telhados, copas, máquinas, pilhas. O **MDT** (modelo digital do terreno) representa o **solo nu**, depois de filtrar o que não é terreno. A diferença **MDS − MDT** é a altura dos objetos (o **modelo normalizado**). Os dois são **rasters** (grades de cotas, em geral em GeoTIFF), com resolução de 2 a 5 vezes o GSD.

![Esquema em perfil comparando os dois modelos: a linha vermelha do modelo digital de superfície passa por cima dos telhados das casas e acompanha o morro, enquanto a linha azul do modelo digital do terreno passa por baixo das casas, seguindo apenas o solo](https://upload.wikimedia.org/wikipedia/commons/2/2c/DTM_DSM.png)

Gerar o MDT exige **classificar** o solo (o OpenDroneMap usa um filtro morfológico; o Metashape, uma classificação automática por parâmetros de ângulo e distância). "Filtrar" não é apagar tudo o que é alto: é decidir o que é terreno **para a pergunta**. Para o volume de uma pilha, a pilha **fica**. Em terraplenagem com solo exposto, é fácil; sob vegetação densa, a câmera simplesmente não vê o chão.

### LiDAR: o chão debaixo da mata

O **LiDAR** embarcado (Aula 2) mede a distância pelo tempo de ida e volta do pulso, $R = c\,\Delta t / 2$, e, com GNSS RTK/PPK e uma **IMU** de alta qualidade, transforma cada pulso num ponto 3D. Como o feixe tem alguns centímetros de diâmetro, parte da energia volta da copa, parte de galhos e parte **do chão**, passando pelos vãos: são os **múltiplos retornos**. O primeiro retorno descreve a superfície (MDS); o último, classificado como solo, permite o **MDT sob vegetação**. O laser **não atravessa** folhas — passa pelas frestas. A densidade de uma passada é

$
\rho \approx \frac{PRR}{v \cdot W}
\qquad
W = 2\,H\,\tan\left(\frac{FOV}{2}\right)
$

e a exatidão depende sobretudo da **trajetória**: um erro de atitude $\delta\theta$ desloca o ponto em cerca de $R \cdot \delta\theta$.

![Nuvem de pontos LiDAR aérea colorida por altura, mostrando quatro torres em forma de L ao redor de um grande pátio retangular arborizado, com edifícios e ruas do entorno](https://upload.wikimedia.org/wikipedia/commons/8/8d/BNF_Lidar_HD.png)

| Critério | Fotogrametria (RGB) | LiDAR embarcado |
| --- | --- | --- |
| Solo sob vegetação | não vê (só MDS) | vê pelas frestas (MDT) |
| Superfície sem textura | falha | mede normalmente |
| Cor e ortomosaico | sim | não, sem câmera auxiliar |
| Custo do equipamento | baixo a médio | alto |

### Abrindo os produtos no QGIS

O **QGIS** (livre) abre tudo isso no mesmo projeto: o ortomosaico e o MDS/MDT como camadas raster, a nuvem LAS/LAZ como camada de nuvem de pontos (com visualização 3D). Fluxo básico: definir o **SRC** do projeto (por exemplo, SIRGAS 2000 / UTM 23S); aplicar **sombreamento** (*hillshade*) ao MDT para enxergar o relevo; medir distâncias e áreas sobre o ortomosaico; traçar **perfis** com a ferramenta de perfil de elevação; e usar a **calculadora raster** para gerar o MDS − MDT. Ortomosaicos são grandes: use GeoTIFF compactado e pirâmides.

![Tela do QGIS com um modelo digital do terreno de 1 m de resolução exibido em tons de cinza (mais claro, mais alto), a legenda de cotas na lista de camadas e, ao lado, o arquivo de texto com as coordenadas X, Y e Z que deram origem à grade](https://upload.wikimedia.org/wikipedia/commons/a/a8/20230705_19_28_34-QGIS%2C_Anwendungsbeispiel_Digitales_Gel%C3%A4ndemodell_1m.png)

### Exemplo numérico

**(a) Deslocamento devido ao relevo.** Foto a $H = 100\,\mathrm{m}$; um prédio de $h = 30\,\mathrm{m}$ a $R = 40\,\mathrm{m}$ do nadir:

$
\delta = \frac{40 \times 30}{100 - 30} \approx 17{,}1\,\mathrm{m}
$

Medir a locação desse prédio na foto crua seria errar em 17 m; no ortomosaico, o topo volta para cima da base.

**(b) LiDAR na encosta.** $PRR = 240\,\mathrm{kHz}$, $FOV = 70°$, $H = 80\,\mathrm{m}$ e $v = 8\,\mathrm{m/s}$:

$
W = 2 \times 80 \times \tan 35° \approx 112\,\mathrm{m}
\qquad
\rho \approx \frac{240.000}{8 \times 112} \approx 268\,\mathrm{pontos/m^2}
$

Na borda da faixa, a distância é $80/\cos 35° \approx 97{,}7\,\mathrm{m}$; um erro de atitude de $0{,}05°$ ($8{,}7 \times 10^{-4}\,\mathrm{rad}$) desloca o ponto em cerca de **8,5 cm**.

**(c) Tamanho do arquivo.** O ortomosaico RGB de 12 ha com GSD de 1,92 cm tem $120.000/0{,}0192^2 \approx 325$ milhões de pixels — cerca de **1 GB** sem compressão.

### Pausa para reflexão (Desafio)

Volte aos três pedidos do início. Para cada um, decida **qual produto** entregar, **com que sensor** e **qual cuidado** de processamento é crítico. A área executada sai do ortomosaico, mas a de uma laje alta, na borda da foto, sofre o deslocamento devido ao relevo se a ortorretificação for ruim. O volume da pilha exige um MDT em que a pilha **fica** e a pá carregadeira **sai**. E a encosta: vale contratar um LiDAR, mais caro, ou basta a fotogrametria nas clareiras? **Que erro custaria mais caro em cada caso?** Escreva sua resposta antes de seguir para a Aula 8.

### Atividade prática

Baixe um conjunto de dados de exemplo do OpenDroneMap já processado (ortomosaico, MDS e nuvem). No QGIS, defina o SRC, meça a área de um telhado no ortomosaico, trace um perfil sobre o MDS e gere o MDS − MDT com a calculadora raster. Que objetos aparecem no modelo normalizado?

### Pontos-chave

- **Nuvem** (XYZ + cor, LAS/LAZ com classes), **ortomosaico** (escala constante), **MDS** (primeira superfície) e **MDT** (solo nu) respondem a perguntas diferentes.
- A foto crua sofre **deslocamento devido ao relevo**, $\delta = Rh/(H - h)$; o ortomosaico o corrige e serve para áreas, locação e avanço físico.
- **MDS − MDT** dá a altura dos objetos; filtrar o terreno depende da pergunta.
- **LiDAR**: múltiplos retornos dão o **MDT sob vegetação** (pelos vãos), densidade $\rho \approx PRR/(v \cdot W)$ e exatidão ditada pela trajetória.
- O **QGIS** integra ortomosaico, modelos e nuvens: SRC, sombreamento, perfis e calculadora raster.

### Para saber mais

- **Wikipedia — Ortofoto:** https://pt.wikipedia.org/wiki/Ortofoto
- **Wikipedia — Digital elevation model (MDS × MDT):** https://en.wikipedia.org/wiki/Digital_elevation_model
- **Wikipedia — Lidar:** https://pt.wikipedia.org/wiki/Lidar
- **QGIS — Manual do usuário (em português):** https://docs.qgis.org/latest/pt_BR/docs/user_manual/

## Aula 7 — Roteiro da Videoaula 7: "Uma foto aérea não é um mapa: ortomosaico, MDS, MDT e o laser que enxerga o chão sob a mata"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–3 — capa, sumário e os três pedidos: área executada, pilha de brita e encosta com mata.

> "Três pedidos na segunda-feira: a área executada no mês, o volume da pilha de brita e o terreno de uma encosta coberta de mata. Todos dizem 'me manda o levantamento do drone'. Mas qual produto? Hoje você vai aprender o que sai do processamento e o que cada produto responde."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 4–7 — os quatro produtos, a nuvem e suas classes, o deslocamento devido ao relevo e o ortomosaico.

> "Da nuvem densa saem quatro produtos. A nuvem de pontos, com classes como solo, vegetação e edificação. O ortomosaico: uma foto crua não é mapa, porque o topo de um prédio de 30 metros, a 40 do nadir, sai 17 metros deslocado. Ortorretificada, a imagem ganha escala constante — é o produto do avanço físico."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 8–11 — MDS × MDT, o canteiro em 3D com a pilha que fica e a máquina que sai, o pulso com múltiplos retornos e a encosta com mata varrida pelo laser em 3D.

> "O MDS é a primeira superfície; o MDT, o solo nu. MDS menos MDT é a altura dos objetos. Filtrar não é apagar o que é alto: a pilha fica, a máquina sai. E debaixo da mata a câmera não vê o chão: o LiDAR, com múltiplos retornos, passa pelas frestas."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 12–15 — o exemplo numérico do LiDAR embarcado (faixa, densidade e erro na borda), LiDAR × fotogrametria, os produtos no QGIS e a pausa para reflexão.

> "A 80 metros, 240 quilohertz e 8 metros por segundo, a faixa tem uns 112 metros e a densidade, uns 268 pontos por metro quadrado; na borda, um erro de atitude de 0,05 grau desloca o ponto em 8,5 centímetros. Mas LiDAR não é sempre melhor: não tem cor e custa mais. No QGIS, tudo no mesmo projeto: SRC, sombreamento, perfil e calculadora raster. E a pausa para reflexão: para os três pedidos, que produto, que sensor e que erro custaria mais caro?"

### 5. Encerramento
**[TELA]** Slides 16–17 — atividade e pontos-chave, e encerramento.

> "Abra um conjunto de exemplo no QGIS e gere o seu primeiro MDS menos MDT. Na próxima aula, esses modelos viram metros cúbicos, curvas de nível e a resposta à pergunta mais cara da obra: o executado bate com o projeto? Te espero na Aula 8!"

---

## Aula 8 — Cálculo de volumes, curvas de nível e comparação entre o projetado e o executado

> Fim do mês na terraplenagem. A empreiteira mede, com drone, **48.200 m³** de corte; a fiscalização, com outro voo, encontra **46.900 m³**. São 1.300 m³ de diferença — algumas dezenas de milhares de reais na medição. E, na mesma reunião, a projetista pergunta se a plataforma do galpão **já está no greide**, dentro da tolerância. Alguém errou? Nesta aula você vai calcular **volumes**, gerar **curvas de nível** e **comparar o projetado com o executado** — sempre com a incerteza no mesmo quadro.

### Volume entre duas superfícies

O volume é calculado por **malha** (ou por prismas sobre uma triangulação): o terreno é dividido em células de área $A_c$ e, em cada uma, calcula-se a diferença de cota $\Delta z_i$ entre a superfície medida e a de referência:

$
V = \sum_{i} \Delta z_i \cdot A_c
$

Corte e aterro se calculam **separados**: são serviços diferentes. A referência pode ser o **greide de projeto** (quanto falta), o **levantamento anterior** (quanto se movimentou no mês — a base da medição) ou um **plano de base** (pilhas), e o sinal de $\Delta z$ depende dela. Contra o **greide de projeto**, com $\Delta z = z_{terreno} - z_{greide}$: $\Delta z > 0$ é **corte a executar** (material acima do greide) e $\Delta z < 0$, **aterro a executar**. Contra o **levantamento anterior**, com $\Delta z = z_{anterior} - z_{atual}$: $\Delta z > 0$ é **corte executado** no período e $\Delta z < 0$, **aterro executado**. Contra um plano de base, a pilha é o material acima do plano.

![Foto aérea de drone com duas grandes pilhas de material — uma escura, de rejeito, à esquerda, e outra cinza, de cascalho, à direita — separadas por uma rodovia, um pátio de veículos e faixas de vegetação](https://upload.wikimedia.org/wikipedia/commons/8/86/Wimmelburg_stockpiles_2020_germany.jpg)

### Pilhas e os três cuidados

Para uma pilha, a base é um plano ou uma superfície triangulada pelos pontos do **pé da pilha** — e escolher essa base muda o resultado. Três cuidados valem para qualquer volume: usar o **MDT** (máquinas e vegetação no MDS viram "volume" falso); garantir que as duas superfícies estejam no **mesmo referencial** horizontal e vertical (Aula 6); e lembrar do **empolamento** — o volume medido no corte (*in situ*) cresce ao ser escavado e transportado.

### Incerteza do volume

Erros **aleatórios** de cota tendem a se compensar numa área grande. Um erro **sistemático** — um viés de altura em todo o modelo — não se compensa e vira volume diretamente:

$
\delta V \approx A \cdot \delta z
$

Num pátio de 2 ha, um viés de 3 cm vale $20.000 \times 0{,}03 = 600\,\mathrm{m^3}$. Por isso a **média** dos resíduos nos checkpoints (Aula 6) é tão importante: volume é o produto mais sensível ao viés vertical.

### Curvas de nível

**Curvas de nível** são linhas que unem pontos de mesma altitude, geradas a partir do **MDT** com uma **equidistância** constante ($Eq$) entre curvas; a cada cinco, uma **curva mestra**, mais destacada. A distância horizontal entre curvas dá a **declividade**: $i = Eq / D$. Curvas próximas indicam terreno íngreme; afastadas, terreno suave. Duas regras práticas: a equidistância deve ser **compatível com a exatidão vertical** (na Classe A do PEC-PCD, $RMSE_z \le Eq/6$); e o MDT costuma ser **suavizado** antes, senão o ruído de centímetros vira curvas "serrilhadas" sem significado.

![Trecho de carta topográfica do Serviço Geológico dos Estados Unidos com curvas de nível marrons, mais densas nas encostas íngremes e afastadas nos vales, além de rio, estradas, a cidade de Stowe e cotas de morros](https://upload.wikimedia.org/wikipedia/commons/7/79/Topographic_map_example.png)

### Projetado × executado: mapa de desvios

Subtraindo a superfície de projeto do MDT levantado ($\Delta z = z_{exec} - z_{proj}$), obtém-se o **mapa de desvios** (ou de corte e aterro), em cores: verde dentro da tolerância, vermelho acima do greide, azul abaixo. Para estruturas, a comparação é **nuvem-modelo**, com a distância de cada ponto à superfície do modelo (em programas como o CloudCompare) — a ponte para o BIM da Aula 14. A **tolerância** vem do projeto, da especificação de serviço ou do contrato; e o desvio medido tem **incerteza** $U$. A regra de decisão defensável é:

- $|\Delta z| + U \le T$ → **conforme**;
- $|\Delta z| - U > T$ → **não conforme**;
- caso contrário → **inconclusivo**: medir de novo, com método mais exato.

![Nuvem de pontos colorida da fachada de um edifício histórico de dois pavimentos com colunata, gerada por escaneamento a laser, base para a comparação entre o executado e o modelo de projeto](https://upload.wikimedia.org/wikipedia/commons/7/7e/Point_cloud_data_of_the_David_W._Dyer_Federal_Building_and_United_States_Courthouse_in_Florida.jpg)

### Tudo isso no QGIS

No QGIS: **calculadora raster** para $\Delta z$ (MDT anterior − MDT atual, para o movimentado no mês, ou MDT atual − superfície de projeto), com uma rampa de cores divergente para o mapa de desvios; o algoritmo **Volume de superfície raster** (*Raster surface volume*) para corte e aterro em relação a um plano ou, somando as células do $\Delta z$, entre duas superfícies; **Contorno** (GDAL) para as curvas de nível; e o **perfil de elevação** para seções transversais. A superfície de projeto vem do software de projeto viário ou de terraplenagem, exportada como raster ou triangulação.

### Medição de pagamento: quem está certo?

Volte ao gancho: 48.200 × 46.900 m³ numa frente de 4 ha, diferença de 2,8%. Um viés de 3 cm em 4 ha vale $40.000 \times 0{,}03 = 1.200\,\mathrm{m^3}$; se **cada** voo tiver um viés independente dessa ordem, a diferença entre eles pode chegar a $\sqrt{2} \times 1.200 \approx 1.700\,\mathrm{m^3}$. Talvez ninguém esteja "errado": os dois números podem estar **dentro da incerteza**. A discussão deixa de ser técnica e vira contratual. Antes da primeira medição, o contrato deve fixar: a **mesma superfície de referência** para as duas partes (o primitivo, levantado no início da obra); o uso do **MDT**; **checkpoints independentes**, com $RMSE_z$ e média dos resíduos no relatório; **data e hora** do voo; uma **tolerância de volume** acordada; e um **procedimento de arbitragem** quando a diferença passar dela. Medição sem método combinado é discussão garantida.

### Exemplo numérico

**(a) Corte e aterro.** Plataforma comparada ao greide em células de $10 \times 10\,\mathrm{m}$ ($A_c = 100\,\mathrm{m^2}$), com $\Delta z$ (m): $+1{,}40$; $+0{,}90$; $+0{,}35$; $-0{,}20$; $+1{,}10$; $+0{,}60$; $-0{,}45$; $-0{,}80$.

$
V_{corte} = (1{,}40 + 0{,}90 + 0{,}35 + 1{,}10 + 0{,}60) \times 100 = 435\,\mathrm{m^3}
\qquad
V_{aterro} = (0{,}20 + 0{,}45 + 0{,}80) \times 100 = 145\,\mathrm{m^3}
$

Com empolamento de 25% e caminhões de $12\,\mathrm{m^3}$: $435 \times 1{,}25 \approx 543{,}8\,\mathrm{m^3}$ soltos e $\lceil 543{,}8/12 \rceil = 46$ viagens. Um viés de 3 cm nas 8 células vale $800 \times 0{,}03 = 24\,\mathrm{m^3}$ (5,5% do corte).

**(b) Curvas.** Com o $RMSE_z = 2{,}56\,\mathrm{cm}$ da Aula 6, a equidistância compatível com a Classe A é $Eq \ge 6 \times 2{,}56 \approx 15{,}4\,\mathrm{cm}$: curvas de **0,20 m**. Duas curvas de 0,50 m separadas por 4 m em planta indicam $i = 0{,}50/4 = 12{,}5\%$.

**(c) Conformidade.** Tolerância da plataforma $T = 5\,\mathrm{cm}$; incerteza $U = 3\,\mathrm{cm}$ (ilustrativos). Desvios médios de três trechos: $+2$, $+7$ e $+12\,\mathrm{cm}$. Trecho 1: $2 + 3 = 5 \le 5$ → conforme. Trecho 2: $7 - 3 = 4 \le 5$, mas $7 + 3 = 10 > 5$ → inconclusivo. Trecho 3: $12 - 3 = 9 > 5$ → não conforme. No trecho 2, a decisão não é "aprovar por pouco": é **medir de novo**, com nivelamento ou estação total.

### Atividade prática

No QGIS, com um MDT de exemplo, gere curvas de nível de 0,5 m e de 0,1 m e compare: qual delas é compatível com a exatidão do levantamento? Depois, crie um plano horizontal como "greide de projeto", calcule o mapa de desvios e o volume de corte e aterro, e repita deslocando o plano 5 cm. Quanto mudou o volume? Compare com $\delta V \approx A \cdot \delta z$.

### Pontos-chave

- Volume por malha: $V = \sum \Delta z_i \cdot A_c$, **corte e aterro separados**, sempre com **MDT**, no **mesmo referencial** e considerando o **empolamento**.
- Viés de cota vira volume: $\delta V \approx A \cdot \delta z$; a média dos resíduos nos checkpoints é o indicador do viés.
- **Curvas de nível** saem do MDT; a equidistância deve ser compatível com a exatidão ($RMSE_z \le Eq/6$ na Classe A) e a declividade é $Eq/D$.
- **Projetado × executado**: mapa de desvios e regra de decisão com **tolerância e incerteza** (conforme, não conforme ou inconclusivo).
- Medição de pagamento por drone exige **método e tolerância definidos em contrato**.

### Para saber mais

- **Wikipedia — Curva de nível:** https://pt.wikipedia.org/wiki/Curva_de_n%C3%ADvel
- **QGIS — algoritmos de análise raster (inclui *Raster surface volume*):** https://docs.qgis.org/latest/en/docs/user_manual/processing_algs/qgis/rasteranalysis.html
- **CloudCompare — software livre de comparação de nuvens e malhas:** https://www.cloudcompare.org/
- **SIEBERT, S.; TEIZER, J. — *Mobile 3D mapping for surveying earthwork projects using an Unmanned Aerial Vehicle (UAV) system* (2014):** https://doi.org/10.1016/j.autcon.2014.01.004

### O que você verá na próxima unidade

Na **Unidade 3 — Sensores IoT e Redes de Comunicação**, o foco desce do céu para dentro do solo, da estrutura e do ar do canteiro. Você vai estudar os **sensores para obras** — inclinômetros, extensômetros, acelerômetros e sensores de temperatura, umidade e poeira —; as **plataformas embarcadas** (Arduino, ESP32, dataloggers) e a coleta de dados em campo; as **redes de comunicação** LoRaWAN, Wi-Fi e celulares; e os **protocolos e plataformas IoT**, com o MQTT e o armazenamento de séries temporais. O drone mostra a obra por fora e em campanhas; os sensores contam o que acontece **entre um voo e outro**.

## Aula 8 — Roteiro da Videoaula 8: "48.200 ou 46.900 m³? Quem tem razão na medição de terraplenagem por drone"

Roteiro sintético da videoaula, em tópicos e falas-guia, com foco na aplicação prática (o texto base traz a fundamentação teórica). As marcações **[TELA]** indicam os slides da apresentação da aula.

### 1. Abertura
**[TELA]** Slides 1–3 — capa, sumário e as pilhas: 48.200 × 46.900 m³ e a plataforma no greide?

> "A empreiteira mede 48.200 metros cúbicos com drone; a fiscalização, 46.900. E a projetista quer saber se a plataforma já está no greide. Hoje a gente calcula volume, gera curvas de nível e compara o projetado com o executado — sempre com a incerteza na mesma tela."

### 2. Desenvolvimento — parte 1
**[TELA]** Slides 4–7 — volume como soma de prismas, as oito células contra o greide, a pilha e o empolamento.

> "Volume é a soma de delta z vezes a área de cada célula, contra uma referência: o greide, o levantamento anterior ou um plano de base. Corte e aterro separados. Oito células de 100 metros quadrados: 435 de corte e 145 de aterro. Com 25% de empolamento, 543,8 soltos, ou 46 viagens de caminhão."

### 3. Desenvolvimento — parte 2
**[TELA]** Slides 8–11 — δV ≈ A · δz, curvas de nível, equidistância × exatidão e o mapa de desvios.

> "Erro aleatório se compensa; viés vira volume: 3 centímetros em 2 hectares são 600 metros cúbicos. As curvas de nível saem do MDT, e a equidistância tem que caber na exatidão: com RMSE de 2,56 centímetros, curvas de 20. Curvas de 10 centímetros seriam desenhar ruído. E o mapa de desvios é o MDT menos o projeto, em cores."

### 4. Desenvolvimento — parte 3
**[TELA]** Slides 12–14 — a regra conforme/inconclusivo/não conforme, o fluxo no QGIS e quem está certo na medição.

> "Com tolerância de 5 e incerteza de 3 centímetros: desvio de 2, conforme; de 7, inconclusivo; de 12, não conforme. E a briga do começo: 3 centímetros em 4 hectares são 1.200 metros cúbicos. Talvez ninguém esteja errado. Resolve o contrato: mesma referência, MDT, checkpoints, tolerância e arbitragem."

### 5. Encerramento
**[TELA]** Slides 15–18 — atividade e pontos-chave (15), fechamento da Unidade 2 (16), prévia da Unidade 3 (17) e encerramento (18).

> "Com isso, você fecha a Unidade 2: da foto ao modelo georreferenciado, à exatidão provada, aos produtos e aos metros cúbicos. Na Unidade 3, os sensores IoT e as redes que trazem os dados do canteiro. Te espero na Aula 9!"

---

## Quiz não avaliativo

### Questão 1

Num levantamento com drone RTK, todos os cinco checkpoints apresentaram resíduos (modelo − campo) muito parecidos: cerca de $+1{,}5\,\mathrm{m}$ em $X$ e $+2{,}8\,\mathrm{m}$ em $Z$, com variação de apenas 2 cm entre eles. O drone registrou solução fixa o voo inteiro, e a base foi instalada sobre um ponto cujas coordenadas vieram do próprio receptor, em modo autônomo. Assinale a alternativa **correta**:

a) O levantamento é impreciso, porque a solução RTK fixa não alcança exatidão melhor que alguns metros.
b) Como a dispersão entre os checkpoints é de só 2 cm, o levantamento é exato e pode ser usado sem correção.
c) O levantamento é preciso, mas tem viés: o erro da coordenada da base se transmitiu a todo o levantamento, e a base deve ser recalculada (por exemplo, com IBGE-PPP ou RBMC).
d) O problema é o multicaminho no drone, que só se resolve aumentando o número de pontos de controle no processamento.

**Resposta correta:** c)

**Feedback:** A alternativa (c) está correta: no posicionamento relativo, o rover é calculado **em relação à base**; se a base estiver numa coordenada autônoma, com erro de metros, todo o levantamento se desloca do mesmo valor — os resíduos são grandes, mas quase iguais entre si: **preciso, mas com viés**. A solução é obter a coordenada correta da base (vértice conhecido, pós-processamento com a RBMC ou IBGE-PPP) e reprocessar. A (a) erra: a solução fixa dá centímetros **em relação à base**. A (b) confunde precisão (dispersão) com exatidão (proximidade do valor verdadeiro). A (d) é falsa: o multicaminho gera erros variáveis, não um deslocamento idêntico em todos os pontos, e a causa aqui é a coordenada da base.

### Questão 2

Numa terraplenagem, o volume mensal escavado é obtido comparando o MDT do mês com o do mês anterior. Os checkpoints do levantamento atual mostram resíduos verticais (modelo − campo) de $+3$ a $+4\,\mathrm{cm}$, todos positivos, com média de $+3{,}2\,\mathrm{cm}$, numa frente de 3 ha. Assinale a alternativa **correta**:

a) Como o $RMSE_z$ fica abaixo de 5 cm, o levantamento é exato e o volume pode ser usado sem qualquer correção.
b) Erros de cota sempre se compensam em áreas grandes, de modo que o efeito sobre o volume é desprezível.
c) O problema se resolve trocando o MDT pelo MDS, que tem mais pontos e representa melhor a superfície do terreno.
d) Há um viés vertical: em 3 ha, 3,2 cm equivalem a cerca de 960 m³, e a causa (GCPs, base RTK, altura de antena, referencial de altitude) deve ser investigada.

**Resposta correta:** d)

**Feedback:** A alternativa (d) está correta: resíduos todos de mesmo sinal, com média próxima do próprio RMSE, revelam **erro sistemático**, que não se compensa e vira volume diretamente: $\delta V \approx A \cdot \delta z = 30.000 \times 0{,}032 = 960\,\mathrm{m^3}$. A (a) confunde atender a um limite de RMSE com ausência de viés. A (b) só vale para erros **aleatórios**. A (c) piora o problema: o MDS inclui máquinas e vegetação, que viram volume falso.

---

## Material complementar

### Direto da fonte (livro da Biblioteca Virtual)

> _[PENDENTE — aguardando acesso à Biblioteca Virtual]_ Sugestão: verificar na BV a disponibilidade de COELHO e BRITO, *Fotogrametria digital* (EdUERJ), ou de MONICO, *Posicionamento pelo GNSS* (Editora UNESP), bibliografia da ementa para esta unidade.

- **Nome do livro:** 
- **Capítulo:** 
- **Link de acesso:** 
- **Qual aula o material deverá entrar?** Aulas 5 e 6

### Para mergulhar no assunto (saiba mais)

> Recomendo a **"Aula 1 — Fotogrametria e drones em geociências"**, do canal do SPAMLab (Instituto de Astronomia, Geofísica e Ciências Atmosféricas da USP), no YouTube: a primeira aula, gravada em português, de uma disciplina de pós-graduação sobre fotogrametria e drones aplicados às geociências. É uma aula longa (cerca de 1h20): assista acompanhando as Aulas 5 e 7 e anote onde aparecem sobreposição, pontos de controle, georreferenciamento e os produtos do processamento. Para praticar, use a documentação do OpenDroneMap, software livre de processamento sugerido na ementa, que traz conjuntos de dados de exemplo.

- **Links:** https://www.youtube.com/watch?v=_YEmntlFf7E · https://docs.opendronemap.org/
- **Qual aula o material deverá entrar?** Aulas 5 e 7

### Podcast (curadoria | até 45 min)

> No episódio #2 do **Nuvem Cast**, do canal Nuvem UAV, a pergunta é direta: **"Topografia com drones realmente funciona?"**. Os convidados são os professores Antonio Tommaselli e João Francisco Galera Monico — este último, autor do livro *Posicionamento pelo GNSS*, da bibliografia desta unidade. Ouça com o olhar crítico das Aulas 5 e 6: em que condições a topografia com drone entrega exatidão de engenharia? Que papel têm os pontos de controle, o GNSS e a verificação independente? O episódio completo tem cerca de 1h14; para esta curadoria, ouça os **primeiros 45 minutos**.

- **NOME DO PODCAST:** Nuvem Cast (canal Nuvem UAV, no YouTube)
- **NOME DO EPISÓDIO:** #2 — Topografia com drones realmente funciona?
- **Link:** https://www.youtube.com/watch?v=xBgA7UZqNy8
- **Qual aula o material deverá entrar?** Aulas 5 e 6

### Artigo científico

> Artigo de referência sobre o uso de drones no **levantamento de terraplenagem**. Os autores avaliam um sistema com drone construído para adquirir, de forma rápida e autônoma, dados de mapeamento 3D em grandes obras de movimentação de terra: descrevem o equipamento, o **planejamento dos voos fotogramétricos** e a geração de **nuvens de pontos**, e propõem um **modelo para estimar o erro de posição**, testado em canteiros reais de escavação e terraplenagem. É a ponte entre a fotogrametria da Aula 5, os produtos da Aula 7 e os volumes da Aula 8. Leia perguntando: o erro estimado pelos autores seria aceitável para a medição de pagamento da sua obra?

- **Link:** https://doi.org/10.1016/j.autcon.2014.01.004
- **Qual aula o material deverá entrar?** Aulas 5, 7 e 8
- **Referência bibliográfica do artigo no formato ABNT:** SIEBERT, Sebastian; TEIZER, Jochen. Mobile 3D mapping for surveying earthwork projects using an Unmanned Aerial Vehicle (UAV) system. **Automation in Construction**, Amsterdam, v. 41, p. 1-14, maio 2014. DOI: 10.1016/j.autcon.2014.01.004.
