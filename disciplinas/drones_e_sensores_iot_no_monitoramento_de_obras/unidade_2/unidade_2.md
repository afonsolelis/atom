# Unidade 2 — Drones: Aquisição e Processamento de Dados

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 5 a 8

## Aula 5 — Planejamento de voo: GSD, sobreposição, altura e plano de missão

> A gerenciadora pediu um levantamento do canteiro de 12 ha "com resolução de 2 cm". O piloto decola, sobe a 120 m — "quanto mais alto, mais rápido" — e volta com 90 fotos. No escritório, o software não consegue montar o modelo em metade da área e, onde monta, cada pixel cobre mais de 3 cm do terreno. Ninguém errou o voo: **errou-se o plano**. Nesta aula você vai aprender a fazer as contas que vêm antes da decolagem — **GSD, altura, área de cada foto, sobreposição, espaçamento entre faixas e intervalo entre fotos** — e vai descobrir de onde veio a faixa de 100 m da Aula 4.

### O que é planejar um voo de mapeamento

Um voo de **mapeamento** (diferente de um voo de inspeção, em que o piloto aponta a câmera para o que quer ver) é uma missão automática em que o drone percorre **faixas paralelas**, como um cortador de grama, tirando fotos em intervalos regulares. O objetivo é que **todo ponto do terreno apareça em várias fotos**, vistas de posições diferentes — é isso que a fotogrametria da Aula 6 vai precisar para reconstruir o 3D.

Planejar é escolher, **antes de decolar**, quatro coisas: a **resolução** desejada no solo, a **altura de voo** que a entrega, as **sobreposições** entre fotos e o **traçado** das faixas. Tudo o resto — número de fotos, tempo de voo, baterias — é consequência.

### GSD: o tamanho do pixel no terreno

O **GSD** (*ground sample distance*, distância de amostragem no solo) é o tamanho, no terreno, de um pixel da imagem. Por semelhança de triângulos entre o sensor e o terreno:

$
GSD = \frac{H \cdot p}{f}
$

onde $H$ é a altura de voo **acima do terreno**, $p$ o tamanho físico do pixel no sensor e $f$ a distância focal. GSD de 2 cm significa que cada pixel "enxerga" um quadrado de 2 × 2 cm. Três consequências práticas: **dobrar a altura dobra o GSD** (imagem mais grosseira); **a exatidão final costuma ficar na ordem de 1 a 3 GSD** (você verá na Aula 6); e um objeto só é identificável se ocupar **vários** pixels — uma fissura de 1 mm não aparece num GSD de 2 cm.

![Tela do software livre Mission Planner, usado para planejar missões automáticas de drones: à esquerda, o painel de instrumentos com altitude e velocidade; à direita, a imagem de satélite da cidade de São Carlos (SP), onde o plano de voo é desenhado](https://upload.wikimedia.org/wikipedia/commons/e/ee/Mission_Planner.png)

### A área de cada foto (footprint)

Se a imagem tem $N_x \times N_y$ pixels, a área coberta por uma foto no terreno (o *footprint*) é:

$
W = N_x \cdot GSD \qquad L = N_y \cdot GSD
$

Em geral, o lado maior ($W$) fica **perpendicular** à direção de voo: é a **largura da faixa imageada**. Note que $W$ cresce com a altura: voar mais alto cobre mais área por foto, mas com GSD pior. **É o compromisso central do planejamento.**

### Sobreposição frontal e lateral

A **sobreposição frontal** é a porcentagem de uma foto repetida na seguinte, ao longo da faixa; a **lateral**, a porcentagem repetida entre faixas vizinhas. Para fotogrametria de obra, valores usuais são **75–80% frontal e 65–75% lateral**; terrenos homogêneos (solo exposto, gramado) ou com relevo forte pedem os valores mais altos. A partir delas:

$
B = L\,(1 - s_f) \qquad d = W\,(1 - s_l)
$

$B$ é a **base** (distância entre fotos consecutivas) e $d$ é o **espaçamento entre faixas** — o mesmo $d$ da fórmula $A = v \cdot t_{útil} \cdot d$ da Aula 4. O intervalo entre disparos é $\Delta t = B / v$, que precisa ser maior que o tempo mínimo que a câmera leva para gravar uma foto.

### Altura sobre o terreno, não sobre a decolagem

O $H$ da fórmula é a altura **acima do terreno fotografado**. Se o drone voa a 70 m acima do ponto de decolagem e passa sobre um morro 20 m mais alto, ali ele está a 50 m: o GSD melhora, mas o *footprint* encolhe e **a sobreposição cai** — e é exatamente onde aparecem os "buracos" no modelo. Em terrenos acidentados, usa-se o **voo acompanhando o relevo** (*terrain follow*, com base num modelo de elevação) ou um planejamento pela cota mais alta. Lembre também do teto da categoria aberta do RBAC nº 100: **120 m acima do solo**.

### Velocidade, obturador e arrasto

Durante a exposição, o drone anda. O **arrasto** (*motion blur*) é $v \cdot t_{exp}$; a regra prática é mantê-lo **abaixo de meio pixel**. Câmeras com **obturador mecânico (global)** expõem o quadro inteiro ao mesmo tempo; com **obturador eletrônico (rolling shutter)**, as linhas são lidas em sequência e a imagem sai levemente "torta" em movimento — por isso, ou se reduz a velocidade, ou o software precisa modelar esse efeito.

![Ortofoto feita por drone de um trecho em obras ao redor de uma estação ferroviária em Eggolsheim, Alemanha: linhas férreas e plataformas no centro, edifício com telhado laranja e painéis solares, estacionamentos, ruas e áreas de terra em execução](https://upload.wikimedia.org/wikipedia/commons/2/2e/Eggolsheim_Bahnhof_Baustelle_Orthophoto-20240428-RM-165210.jpg)

### O plano de missão completo

Um plano de missão de mapeamento registra: **polígono da área** (com margem além do limite da obra, porque as bordas têm menos sobreposição); **altura** e **GSD**; **sobreposições**; **direção das faixas** (em geral paralelas ao lado maior do terreno, para reduzir curvas); **velocidade** e **intervalo de disparo**; **baterias** e **pontos de troca**; **ponto de decolagem e pouso**; e as **condições meteorológicas** aceitáveis (vento, chuva, sol baixo, que gera sombras longas). Softwares como o Mission Planner, o QGroundControl e os aplicativos dos fabricantes calculam tudo isso a partir de poucos parâmetros — mas **quem responde pelo plano é o engenheiro**.

E o plano encontra a regulamentação da Aula 4: um voo em **faixas sobrepostas** para gerar ortomosaico ou modelo do terreno é **aerolevantamento** — executado por entidade inscrita no Ministério da Defesa, com pedido no **SARPAS** feito com **4 dias corridos** de antecedência.

### Exemplo numérico

Uma câmera de 20 MP tem $5.472 \times 3.648$ pixels, pixel $p = 2{,}41\,\mathrm{\mu m}$ e $f = 8{,}8\,\mathrm{mm}$ (sensor de 1", com $13{,}2 \times 8{,}8\,\mathrm{mm}$). O contrato pede **GSD de no máximo 2 cm**. A altura máxima é:

$
H_{máx} = \frac{GSD \cdot f}{p} = \frac{0{,}02 \times 8{,}8}{0{,}00241} \approx 73\,\mathrm{m}
$

Adotando $H = 70\,\mathrm{m}$ (folga para o relevo):

$
GSD = \frac{70 \times 0{,}00241}{8{,}8} \approx 0{,}0192\,\mathrm{m} = 1{,}92\,\mathrm{cm}
\qquad
W \approx 5.472 \times 0{,}0192 \approx 105\,\mathrm{m}
\qquad
L \approx 3.648 \times 0{,}0192 \approx 70\,\mathrm{m}
$

É a **faixa de cerca de 100 m** que usamos na Aula 4. Com sobreposições de 80% (frontal) e 70% (lateral):

$
B = 70 \times (1 - 0{,}8) = 14\,\mathrm{m}
\qquad
d = 105 \times (1 - 0{,}7) = 31{,}5\,\mathrm{m}
\qquad
\Delta t = \frac{14}{6} \approx 2{,}3\,\mathrm{s}
$

Para o canteiro de 12 ha da Aula 1 ($400 \times 300\,\mathrm{m}$), com faixas ao longo dos 400 m: $\lceil 300/31{,}5 \rceil + 1 = 11$ faixas e $\lceil 400/14 \rceil + 1 = 30$ fotos por faixa, ou cerca de **330 fotos**. O percurso tem $11 \times 400 + 10 \times 31{,}5 = 4.715\,\mathrm{m}$; a $6\,\mathrm{m/s}$, são cerca de **13,1 min** — cabe numa bateria com 21 min úteis. O arrasto com exposição de 1/1.000 s é $6 \times 0{,}001 = 6\,\mathrm{mm} \approx 0{,}31$ pixel: aceitável.

Agora o morro: onde o terreno está 20 m mais alto, $H = 50\,\mathrm{m}$, $W = 75\,\mathrm{m}$ e a sobreposição lateral cai para $1 - 31{,}5/75 = 58\%$ — abaixo do recomendado. Solução: voo acompanhando o relevo ou espaçamento planejado pelo ponto mais alto.

### Atividade prática

Escolha a câmera de um drone real (procure a ficha técnica: pixels, tamanho do sensor e distância focal). Para uma obra de sua escolha, calcule: a altura para GSD de 2 cm e de 5 cm; o *footprint*; a base e o espaçamento entre faixas com 80/70% de sobreposição; o número aproximado de fotos e o tempo de voo a 6 m/s. Depois, desenhe o polígono e as faixas num software de planejamento gratuito e compare com suas contas.

### Pontos-chave

- $GSD = H \cdot p / f$: a altura **acima do terreno** define a resolução; dobrar a altura dobra o GSD.
- O *footprint* ($W = N_x \cdot GSD$) e as sobreposições definem a base $B = L(1 - s_f)$ e o espaçamento entre faixas $d = W(1 - s_l)$.
- Sobreposições usuais em obra: **75–80% frontal e 65–75% lateral**; relevo e superfícies homogêneas pedem mais.
- Relevo reduz a altura efetiva e a sobreposição: use **voo acompanhando o terreno** ou planeje pelo ponto mais alto; controle o **arrasto** (menos de meio pixel).
- O plano de missão é documento de engenharia — e mapeamento em faixas sobrepostas é **aerolevantamento**.

### Para saber mais

- **Wikipedia — Ground sample distance:** https://en.wikipedia.org/wiki/Ground_sample_distance
- **Pix4D — calculadora de GSD (explica a fórmula e as variáveis):** https://support.pix4d.com/hc/en-us/articles/202560249
- **OpenDroneMap — boas práticas de voo para mapeamento:** https://docs.opendronemap.org/flying/
- **ArduPilot — documentação do Mission Planner:** https://ardupilot.org/planner/

## Aula 5 — Roteiro da Videoaula 5: "Planejamento de voo: GSD, sobreposição, altura e plano de missão"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e o voo a 120 m que voltou com 90 fotos.

> "A gerenciadora pediu resolução de 2 centímetros. O piloto subiu a 120 metros, porque mais alto é mais rápido, e voltou com 90 fotos. O software não montou metade do modelo e, onde montou, cada pixel cobre mais de 3 centímetros. Ninguém errou o voo: errou-se o plano. Hoje a gente faz as contas que vêm antes da decolagem."

### 2. Desenvolvimento — parte 1 (0:30 – 1:20)

**[TELA]** Slides 4–6 — as quatro escolhas do plano, o GSD interativo e a tabela de altura × GSD.

> "No voo de mapeamento, o drone percorre faixas paralelas e dispara em intervalos regulares, para que cada ponto do terreno apareça em várias fotos. Planejar é escolher resolução, altura, sobreposições e traçado. A resolução é o GSD, o tamanho do pixel no terreno: altura vezes o pixel do sensor, dividido pela distância focal. Com a nossa câmera de 20 megapixels, a 70 metros, dá 1,92 centímetro. Dobrou a altura, dobrou o GSD. A 120 metros, o teto da categoria aberta, são 3,29 centímetros."

### 3. Desenvolvimento — parte 2 (1:20 – 2:15)

**[TELA]** Slides 7–10 — o mapa de sobreposição, a ficha histórica, o morro em 3D e a calculadora de arrasto.

> "Cada foto cobre o número de pixels vezes o GSD: a 70 metros, 105 por 70 metros. Com 80% de sobreposição frontal e 70% de lateral, cada ponto aparece em umas 16 fotos; a base entre fotos é 14 metros e o espaçamento entre faixas, 31,5. Economizou na sobreposição? Aparecem os buracos. E atenção: a altura é sobre o terreno. Num morro de 20 metros, o drone fica a 50 metros do chão e a sobreposição lateral cai para 58%. Solução: acompanhar o relevo. E o arrasto: a 6 metros por segundo e um milésimo de segundo, 0,31 pixel; tem que ficar abaixo de meio."

### 4. Desenvolvimento — parte 3 (2:15 – 3:15)

**[TELA]** Slides 11–15 — o plano de missão, o aerolevantamento, a calculadora do canteiro de 12 ha, os resultados e o diagnóstico do gancho.

> "O plano de missão registra polígono com margem, altura, GSD, sobreposições, direção das faixas, velocidade, baterias e meteorologia. E voo em faixas sobrepostas é aerolevantamento: empresa inscrita no Ministério da Defesa e SARPAS com 4 dias de antecedência. A conta completa: GSD de 2 centímetros exige no máximo 73 metros; a 70, são 11 faixas, 330 fotos, 4.715 metros e 13,1 minutos: uma bateria. E aqueles 105 metros de faixa são a faixa da Aula 4. O voo do gancho? Acima de 73 metros, não atendia ao contrato; e com 90 fotos, sobreposição de menos."

### 5. Encerramento (3:15 – 3:40)

**[TELA]** Slides 16–18 — a ortofoto, atividade e pontos-chave, e encerramento.

> "Plano bem feito vira mapa. Agora calcule o plano para uma câmera real e compare com um software de planejamento. Na próxima aula, a gente descobre como 330 fotos viram um modelo 3D — e como provar que ele está no lugar certo. Te espero na Aula 6!"

---

## Aula 6 — Fotogrametria com drones: SfM, pontos de controle, RTK/PPK e precisão

> O modelo 3D do canteiro ficou lindo: texturas nítidas, prédios vizinhos perfeitos. A topografia confere um marco de concreto no meio do terreno e encontra uma diferença de **18 cm na cota**. O modelo está "certo" ou "errado"? Ele é **preciso** — tudo está coerente entre si —, mas **não é exato**: está todo deslocado e levemente "embarrigado". Nesta aula você vai entender como centenas de fotos viram um modelo 3D (*Structure from Motion*), por que os **pontos de controle** e o **RTK/PPK** existem e como **provar**, com números, a exatidão de um levantamento.

### Da foto ao 3D: o princípio da fotogrametria

**Fotogrametria** é a ciência de obter medidas a partir de fotografias. O princípio é a **interseção de raios**: cada pixel define um raio que sai do centro da câmera e passa pelo ponto do terreno. Se o mesmo ponto aparece em duas ou mais fotos tiradas de posições conhecidas, os raios se cruzam no espaço — e o ponto fica determinado em 3D. A relação matemática entre ponto no terreno, centro da câmera e pixel na imagem são as **equações de colinearidade**. Daí a necessidade das sobreposições da Aula 5: sem que cada ponto apareça em várias fotos, não há interseção.

### Structure from Motion (SfM), passo a passo

Nos drones, o processamento usa o **SfM** (*Structure from Motion*), que resolve ao mesmo tempo a posição das câmeras e a forma do terreno:

1. **Detecção de pontos característicos** — em cada foto, o algoritmo encontra milhares de feições distintivas (cantos, texturas), descritas por "assinaturas" como as do método SIFT.
2. **Correspondência** — as mesmas feições são reconhecidas em fotos diferentes (*pontos homólogos*).
3. **Ajustamento por feixes** (*bundle adjustment*) — um ajuste de mínimos quadrados calcula, de uma vez, a posição e a orientação de cada foto, os parâmetros internos da câmera (distância focal, distorção da lente) e as coordenadas dos pontos homólogos. Sai uma **nuvem esparsa**.
4. **Densificação** (*multi-view stereo*) — com as câmeras já orientadas, o software busca correspondências pixel a pixel e gera a **nuvem densa**, base dos produtos da Aula 7.

Superfícies **sem textura** (água, telhado metálico liso, concreto novo e uniforme) e **objetos em movimento** (máquinas, pessoas) confundem a correspondência — e ficam com buracos ou ruído.

### Escala e georreferenciamento: o problema do SfM puro

Só com as fotos, o SfM reconstrói a **forma**, mas não sabe **onde** ela está no mundo nem **qual o seu tamanho**. Para georreferenciar, há dois caminhos: medir **pontos no terreno** ou conhecer com exatidão **a posição de cada foto**. Sem nenhum deles (só com o GNSS comum do drone, de exatidão métrica), o modelo pode estar deslocado de metros e sofrer o **efeito de "domo"** (*doming*): uma curvatura sistemática causada por pequenos erros na calibração da lente, típica de blocos de fotos todas verticais e paralelas (James e Robson, 2014). Fotos **oblíquas** adicionais e pontos de controle bem distribuídos reduzem esse efeito.

### Pontos de controle (GCP) e pontos de verificação

**Pontos de controle** (GCP, *ground control points*) são alvos bem visíveis nas fotos — placas em xadrez, cruzes pintadas — cujas coordenadas são medidas em campo com **GNSS RTK ou estação total**. Eles entram no ajustamento e "amarram" o modelo ao sistema de referência (no Brasil, o **SIRGAS2000**).

![Ponto de controle no terreno: um alvo quadrado em laranja e branco fixado no chão de cascalho, ao lado de uma estação GNSS com painel solar e de um receptor em tripé, numa paisagem vulcânica da Islândia](https://upload.wikimedia.org/wikipedia/commons/f/f3/Ground_control_point_in_Iceland_%28GCP%29.jpg)

**Pontos de verificação** (*checkpoints*) são medidos da mesma forma, mas **não entram no processamento**: servem só para conferir o resultado. Usar os mesmos pontos para ajustar e para verificar é como o aluno corrigir a própria prova. Boa prática: GCPs no **perímetro e no interior** da área, cobrindo também os pontos altos e baixos, e checkpoints independentes espalhados.

### RTK e PPK: posição exata de cada foto

Com **RTK** (*real time kinematic*), o drone recebe, durante o voo, correções de uma **base GNSS** (própria ou de uma rede via internet, por NTRIP) e registra a posição de cada foto com exatidão de poucos centímetros. No **PPK** (*post-processed kinematic*), o drone grava os dados brutos de GNSS e a correção é feita **depois do voo**, com os dados de uma base — por exemplo, uma estação da Rede Brasileira de Monitoramento Contínuo (RBMC) do IBGE. O PPK não depende do enlace de rádio ou de internet durante o voo.

![Topógrafo de colete refletivo segura um bastão com receptor GNSS no topo e consulta a coletora de dados, sobre um pavimento, medindo a coordenada de um ponto com correção RTK](https://upload.wikimedia.org/wikipedia/commons/b/be/Surveyor_Using_GNSS_Receiver_with_RTK_Solution.jpg)

Dois cuidados: o **instante** de cada foto precisa estar sincronizado com o GNSS (um atraso de 20 ms a 6 m/s desloca a foto 12 cm), e a distância entre a antena e o centro da câmera (**braço de alavanca**) precisa ser conhecida. RTK/PPK **reduz** a necessidade de GCPs — **não dispensa** os pontos de verificação.

### Como se expressa a exatidão: RMSE e padrões

A exatidão é avaliada nos checkpoints pela **raiz do erro médio quadrático** (RMSE):

$
RMSE_z = \sqrt{\frac{1}{n}\sum_{i=1}^{n} \left(z_{modelo,i} - z_{campo,i}\right)^2}
\qquad
RMSE_r = \sqrt{RMSE_x^2 + RMSE_y^2}
$

O padrão americano **ASPRS** (*Positional Accuracy Standards for Digital Geospatial Data*), na **2ª edição (2023)**, passou a reportar a exatidão pelo próprio **RMSE** (deixando de usar o nível de 95% como medida principal) e exige no mínimo **30 checkpoints** para a avaliação completa de um produto. No Brasil, produtos cartográficos são classificados pelo **PEC-PCD** (Padrão de Exatidão Cartográfica dos Produtos Cartográficos Digitais), com base no Decreto nº 89.817/1984 e na especificação técnica da Diretoria de Serviço Geográfico do Exército. Como ordem de grandeza, um bom levantamento com drone atinge **1 a 2 GSD na horizontal e 1,5 a 3 GSD na vertical**.

### Exemplo numérico

O voo da Aula 5 (GSD de 1,92 cm), com RTK e 6 GCPs, foi conferido em 5 checkpoints independentes. Os resíduos (modelo − campo), em cm, foram:

| Ponto | $\Delta x$ | $\Delta y$ | $\Delta z$ |
| --- | --- | --- | --- |
| CP1 | +1,2 | −0,8 | +2,1 |
| CP2 | −0,9 | +1,5 | −3,0 |
| CP3 | +2,0 | +0,4 | +1,8 |
| CP4 | −1,1 | −1,6 | −2,4 |
| CP5 | +0,6 | +0,9 | +3,2 |

$
RMSE_x = \sqrt{\frac{1{,}44 + 0{,}81 + 4{,}00 + 1{,}21 + 0{,}36}{5}} \approx 1{,}25\,\mathrm{cm}
\qquad
RMSE_y \approx 1{,}13\,\mathrm{cm}
$

$
RMSE_r = \sqrt{1{,}25^2 + 1{,}13^2} \approx 1{,}69\,\mathrm{cm} \approx 0{,}9\,GSD
\qquad
RMSE_z = \sqrt{\frac{4{,}41 + 9{,}00 + 3{,}24 + 5{,}76 + 10{,}24}{5}} \approx 2{,}56\,\mathrm{cm} \approx 1{,}3\,GSD
$

A média de $\Delta z$ é $+0{,}34\,\mathrm{cm}$: **não há viés relevante**. Se a especificação da obra pede $RMSE_z \le 5\,\mathrm{cm}$ para cálculo de volumes, o levantamento atende. Ressalva honesta: 5 checkpoints bastam para o controle de rotina de uma obra pequena, mas são poucos para declarar conformidade com o padrão ASPRS completo, que pede 30.

### Atividade prática

Num levantamento de 20 ha, desenhe (em papel quadriculado ou num mapa) onde você colocaria **6 GCPs** e **5 checkpoints**, justificando a distribuição. Depois, para os resíduos verticais $+4$, $+5$, $+3$, $+6$ e $+4\,\mathrm{cm}$, calcule o $RMSE_z$ e a média. O que a média revela? Que causa você investigaria primeiro?

### Pontos-chave

- Fotogrametria determina pontos 3D pela **interseção de raios** de várias fotos; o **SfM** detecta feições, faz a correspondência, o **ajustamento por feixes** e a densificação.
- Sem georreferenciamento confiável, o modelo pode ser **preciso e inexato**: deslocado e com **efeito de domo**.
- **GCPs** amarram o modelo ao terreno; **checkpoints** independentes provam a exatidão — nunca use os mesmos pontos para as duas coisas.
- **RTK** (tempo real) e **PPK** (pós-processado) dão a posição de cada foto em centímetros e reduzem os GCPs, mas não os checkpoints.
- A exatidão se expressa pelo **RMSE** nos checkpoints (ASPRS 2023: no mínimo 30 para conformidade plena; no Brasil, PEC-PCD); ordem de grandeza: 1–2 GSD na horizontal e 1,5–3 GSD na vertical.

### Para saber mais

- **Wikipedia — Structure from motion:** https://en.wikipedia.org/wiki/Structure_from_motion
- **JAMES, M. R.; ROBSON, S. — *Mitigating systematic error in topographic models derived from UAV and ground-based image networks* (efeito de domo; acesso aberto):** https://doi.org/10.1002/esp.3609
- **LiDAR Magazine — *The ASPRS Positional Accuracy Standards, Edition 2* (resumo das mudanças de 2023):** https://lidarmag.com/2023/10/06/the-asprs-positional-accuracy-standards-edition-2/
- **IBGE — Serviço on-line de pós-processamento de dados GNSS (IBGE-PPP):** https://www.ibge.gov.br/geociencias/informacoes-sobre-posicionamento-geodesico/servicos-para-posicionamento-geodesico/16334-servico-online-para-pos-processamento-de-dados-gnss-ibge-ppp.html

## Aula 6 — Roteiro da Videoaula 6: "Fotogrametria com drones: SfM, pontos de controle, RTK/PPK e precisão"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e os 18 cm na cota de um marco.

> "As 330 fotos do plano da aula passada viraram um modelo 3D lindo. Aí a topografia confere um marco no meio do canteiro: 18 centímetros de diferença na cota. O modelo está certo ou errado? Ele é preciso, mas não é exato. Hoje a gente vai entender como as fotos viram 3D e como provar, com números, que um levantamento está bom."

### 2. Desenvolvimento — parte 1 (0:30 – 1:20)

**[TELA]** Slides 4–7 — interseção de raios, os 4 passos do SfM, o SfM animado e onde a correspondência tropeça.

> "O princípio é a interseção de raios: cada pixel define um raio, e o mesmo ponto visto em várias fotos fica onde os raios se cruzam. Com erro aleatório nas câmeras, os raios não se encontram; com erro sistemático, se cruzam bem, mas no lugar errado. O Structure from Motion faz isso em quatro passos: detecta feições, encontra os pontos homólogos, faz o ajustamento por feixes, que dá as câmeras e a nuvem esparsa, e densifica. E tropeça em superfície sem textura, em máquina se movendo e sob vegetação."

### 3. Desenvolvimento — parte 2 (1:20 – 2:15)

**[TELA]** Slides 8–11 — escala e georreferenciamento, o efeito de domo em 3D, GCP × checkpoint e a distribuição dos pontos de controle.

> "Só com fotos, o SfM sabe a forma, mas não sabe onde ela está, e ainda pode embarrigar: é o efeito de domo, de James e Robson. A cena 3D mostra o modelo 18 centímetros acima do marco sem pontos de controle, e o domo sumindo com GCPs e fotos oblíquas. Os GCPs são alvos medidos em campo que entram no ajustamento; os checkpoints são medidos igual, mas não entram: servem para provar. Usar os mesmos pontos é corrigir a própria prova. E a distribuição importa: perímetro mais interior."

### 4. Desenvolvimento — parte 3 (2:15 – 3:15)

**[TELA]** Slides 12–16 — RTK × PPK, sincronismo e braço de alavanca, RMSE/ASPRS/PEC-PCD, a tabela dos 5 checkpoints e o viés no RMSE.

> "O outro caminho é saber onde estava cada foto: RTK corrige em tempo real, por uma base ou rede NTRIP; PPK corrige depois do voo, por exemplo com a RBMC do IBGE. Reduzem os GCPs, não os checkpoints. Cuidado com o sincronismo: 20 milissegundos a 6 metros por segundo são 12 centímetros. A exatidão se prova pelo RMSE nos checkpoints; a ASPRS, desde 2023, pede no mínimo 30 para a avaliação completa, e no Brasil vale o PEC-PCD. No exemplo, RMSE horizontal de 1,69 centímetro, uns 0,9 GSD, e vertical de 2,56, uns 1,3 GSD, com média de 0,34: sem viés, atende aos 5 centímetros. Somando um viés de 18 centímetros, o RMSE vai a 18,5: reprovado."

### 5. Encerramento (3:15 – 3:40)

**[TELA]** Slides 17–19 — atividade e pontos-chave, da nuvem densa aos produtos e encerramento.

> "Modelo bonito não basta: modelo bom é o que tem a exatidão provada nos checkpoints. Na próxima aula, a nuvem densa vira ortomosaico, MDS, MDT e cálculo de volumes — e você vai ver quanto custa um viés de poucos centímetros. Te espero na Aula 7!"

---

## Aula 7 — Produtos cartográficos: ortomosaico, MDS/MDT, nuvem de pontos e cálculo de volumes

> Fim do mês na terraplenagem. A empreiteira mede, com drone, **48.200 m³** de corte; a fiscalização, com outro voo, encontra **46.900 m³**. São 1.300 m³ de diferença — algumas dezenas de milhares de reais na medição. Alguém errou? Antes de responder, você precisa saber **o que cada produto do drone representa**, como o volume é calculado e **quanta incerteza** cabe nesse número. É o assunto desta aula.

### Os produtos de um levantamento

Da nuvem densa da Aula 6 saem quatro produtos principais: a **nuvem de pontos**, o **ortomosaico**, o **MDS** e o **MDT**. Cada um responde a uma pergunta diferente — e usar o produto errado é a fonte mais comum de erro de volume.

### Nuvem de pontos

A **nuvem de pontos** é um conjunto de milhões de pontos com coordenadas $X, Y, Z$ e, na fotogrametria, a cor RGB de cada um. É o produto mais "bruto" e mais rico: permite medir distâncias e alturas, extrair perfis e seções, e **classificar** os pontos (solo, vegetação, edificação, máquinas). A densidade típica de uma nuvem fotogramétrica é da ordem de centenas de pontos por metro quadrado, dependendo do GSD.

![Modelo 3D georreferenciado, com textura fotográfica, de uma área de rochas avermelhadas, estradas de terra e vegetação rasteira, gerado a partir de imagens aéreas de drone](https://upload.wikimedia.org/wikipedia/commons/9/9e/Geo-Referenced_Point_Cloud.JPG)

### Ortomosaico: a foto que vira mapa

Uma foto aérea comum **não é um mapa**: por causa da perspectiva central, o topo de um prédio aparece deslocado em relação à base (**deslocamento devido ao relevo**), e a escala varia com a altura do terreno. O **ortomosaico** é o mosaico das fotos **ortorretificadas** — reprojetadas sobre o modelo de superfície como se cada ponto fosse visto na vertical. Resultado: uma imagem com **escala constante**, na qual se medem distâncias e áreas e sobre a qual se sobrepõe o projeto em CAD ou BIM. É o produto preferido para **avanço físico** e conferência de locação.

### MDS e MDT: superfície × terreno

O **MDS** (modelo digital de superfície, *DSM*) representa a cota do **primeiro obstáculo** visto de cima: telhados, árvores, máquinas, pilhas. O **MDT** (modelo digital do terreno, *DTM*) representa o **solo nu**, depois de remover tudo o que não é terreno. A diferença MDS − MDT é a **altura dos objetos** (o chamado modelo normalizado).

![Esquema em perfil comparando os dois modelos: a linha vermelha do modelo digital de superfície passa por cima dos telhados das casas e acompanha o morro, enquanto a linha azul do modelo digital do terreno passa por baixo das casas, seguindo apenas o solo](https://upload.wikimedia.org/wikipedia/commons/2/2c/DTM_DSM.png)

Gerar o MDT a partir de fotogrametria exige **filtrar** os pontos que não são solo — fácil em terraplenagem com solo exposto, difícil sob vegetação densa, onde a câmera simplesmente não vê o chão (é aí que entra o LiDAR da Aula 8). Do MDT saem as **curvas de nível**, os perfis e as seções transversais.

### Cálculo de volumes

O volume entre duas superfícies é calculado, na prática, por **malha** (ou por prismas sobre uma triangulação): o terreno é dividido em células de área $A_c$, e em cada uma se calcula a diferença de cota $\Delta z_i$ entre a superfície medida e a de referência:

$
V = \sum_{i} \Delta z_i \cdot A_c
$

Células com $\Delta z > 0$ somam **corte** (há material acima da referência); com $\Delta z < 0$, **aterro**. A superfície de referência pode ser o **greide de projeto** (quanto falta escavar), o **levantamento anterior** (quanto se escavou no mês) ou um **plano de base** (volume de uma pilha de agregado). Três cuidados: usar **MDT** (máquinas e vegetação no MDS viram "volume" falso); garantir que as duas superfícies estejam no **mesmo referencial**; e lembrar do **empolamento** — o volume medido no corte (*in situ*) cresce ao ser escavado e transportado.

### Incerteza do volume

Erros **aleatórios** de cota, de célula para célula, tendem a se compensar numa área grande. Um erro **sistemático** — um viés de altura em todo o modelo — não se compensa: ele vira volume diretamente,

$
\delta V \approx A \cdot \delta z
$

Num pátio de 2 ha, um viés de apenas 3 cm equivale a $20.000 \times 0{,}03 = 600\,\mathrm{m^3}$. É por isso que os checkpoints da Aula 6 e a **média** dos resíduos importam tanto: volume é o produto mais sensível ao viés vertical.

### Exemplo numérico

Uma plataforma foi levantada e comparada ao greide de projeto numa malha de células de $10 \times 10\,\mathrm{m}$ ($A_c = 100\,\mathrm{m^2}$). As diferenças $\Delta z = z_{levantado} - z_{projeto}$, em metros, foram: $+1{,}40$; $+0{,}90$; $+0{,}35$; $-0{,}20$; $+1{,}10$; $+0{,}60$; $-0{,}45$; $-0{,}80$.

$
V_{corte} = (1{,}40 + 0{,}90 + 0{,}35 + 1{,}10 + 0{,}60) \times 100 = 435\,\mathrm{m^3}
\qquad
V_{aterro} = (0{,}20 + 0{,}45 + 0{,}80) \times 100 = 145\,\mathrm{m^3}
$

Se o corte for todo levado a bota-fora, com empolamento de 25% e caminhões de $12\,\mathrm{m^3}$:

$
V_{solto} = 435 \times 1{,}25 \approx 543{,}8\,\mathrm{m^3}
\qquad
n = \left\lceil \frac{543{,}8}{12} \right\rceil = 46\,\mathrm{viagens}
$

E a incerteza: se o modelo tivesse um viés de 3 cm, nas 8 células ($800\,\mathrm{m^2}$) o erro seria $800 \times 0{,}03 = 24\,\mathrm{m^3}$ — cerca de 5,5% do corte. Em áreas pequenas e cortes rasos, o **viés pesa proporcionalmente mais**.

### Pausa para reflexão (Desafio)

Volte ao gancho: 48.200 m³ (empreiteira) × 46.900 m³ (fiscalização), numa frente de 4 ha. A diferença é de 1.300 m³, cerca de 2,8%. Um viés de 3 cm em 4 ha vale $40.000 \times 0{,}03 = 1.200\,\mathrm{m^3}$ — praticamente toda a diferença; e, se **cada** levantamento tiver um viés independente dessa ordem, a diferença entre eles pode chegar a $\sqrt{2} \times 1.200 \approx 1.700\,\mathrm{m^3}$. **Quem está certo?** Talvez ninguém esteja "errado": os dois números podem estar dentro da incerteza. Pense no que você exigiria **no contrato**, antes da primeira medição: a mesma superfície de referência (o primitivo levantado no início da obra); MDT, e não MDS; checkpoints independentes com $RMSE_z$ e média dos resíduos informados; data e hora do voo; tolerância de volume acordada; e um procedimento de arbitragem. **Medição de pagamento sem método combinado é discussão garantida.**

### Atividade prática

Pegue um ortomosaico e um MDS gratuitos (por exemplo, um conjunto de dados de exemplo do OpenDroneMap) e, num software livre como o QGIS, meça uma área, trace um perfil e calcule o volume de uma pilha com um plano de base. Repita o cálculo deslocando o plano de base 5 cm para cima e para baixo: quanto muda o volume? Relacione com $\delta V \approx A \cdot \delta z$.

### Pontos-chave

- **Nuvem de pontos** (XYZ + cor), **ortomosaico** (foto ortorretificada, escala constante), **MDS** (primeira superfície) e **MDT** (solo nu) respondem a perguntas diferentes.
- O ortomosaico corrige o **deslocamento devido ao relevo**: é o produto para medir áreas, locação e avanço físico.
- Volume por malha: $V = \sum \Delta z_i \cdot A_c$, separando corte e aterro, sempre com **MDT** e no **mesmo referencial**; considere o **empolamento** no transporte.
- Erro sistemático de cota vira volume: $\delta V \approx A \cdot \delta z$ — por isso o viés vertical é crítico.
- Medição de pagamento por drone exige **método e tolerância definidos em contrato**.

### Para saber mais

- **Wikipedia — Ortofoto:** https://pt.wikipedia.org/wiki/Ortofoto
- **Wikipedia — Digital elevation model (MDS × MDT):** https://en.wikipedia.org/wiki/Digital_elevation_model
- **Wikipedia — Nuvem de pontos:** https://pt.wikipedia.org/wiki/Nuvem_de_pontos
- **OpenDroneMap — documentação (software livre de processamento, com conjuntos de dados de exemplo):** https://docs.opendronemap.org/

## Aula 7 — Roteiro da Videoaula 7: "Produtos cartográficos: ortomosaico, MDS/MDT, nuvem de pontos e cálculo de volumes"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e as pilhas: 48.200 × 46.900 m³.

> "Fim do mês na terraplenagem. A empreiteira mede 48.200 metros cúbicos com drone; a fiscalização, com outro voo, 46.900. São 1.300 metros cúbicos de diferença. Alguém errou? Antes de responder, você precisa saber o que cada produto do drone representa, como se calcula volume e quanta incerteza cabe nesse número."

### 2. Desenvolvimento — parte 1 (0:25 – 1:20)

**[TELA]** Slides 4–9 — os quatro produtos, a nuvem de pontos, o deslocamento devido ao relevo, o ortomosaico, MDS × MDT e o canteiro em 3D.

> "Da nuvem densa saem quatro produtos. A nuvem de pontos: milhões de pontos X, Y, Z com cor, que dá para medir e classificar. O ortomosaico: as fotos ortorretificadas, sem o deslocamento devido ao relevo, com escala constante — o produto do avanço físico. O MDS, que é a primeira superfície vista de cima, com telhados, copas e máquinas. E o MDT, o solo nu. No 3D, o MDT apaga o prédio, as árvores e a máquina, mas mantém a pilha, porque ela é o que eu quero medir. MDS menos MDT mostra o que viraria volume falso."

### 3. Desenvolvimento — parte 2 (1:20 – 2:20)

**[TELA]** Slides 10–13 — volume como soma de prismas, os três cuidados, as oito células contra o greide e o empolamento.

> "Volume é a soma de delta z vezes a área de cada célula, contra uma referência: o greide, o levantamento anterior ou um plano de base. Três cuidados: usar o MDT, o mesmo referencial e lembrar do empolamento. Oito células de 100 metros quadrados: 435 metros cúbicos de corte e 145 de aterro. Mandando o corte para o bota-fora com 25% de empolamento, são uns 543,8 metros cúbicos soltos, ou 46 viagens de caminhão de 12."

### 4. Desenvolvimento — parte 3 (2:20 – 3:10)

**[TELA]** Slides 14–15 — δV ≈ A · δz e a pausa para reflexão: quem está certo na medição?

> "Erro aleatório se compensa; viés vira volume. Em 2 hectares, 3 centímetros de viés são 600 metros cúbicos. E a pausa para reflexão: em 4 hectares, 3 centímetros são 1.200 metros cúbicos — quase toda a diferença entre empreiteira e fiscalização. Talvez ninguém esteja errado. O que resolve é o contrato: mesma superfície de referência, MDT, checkpoints com RMSE e média dos resíduos, data do voo, tolerância e arbitragem."

### 5. Encerramento (3:10 – 3:35)

**[TELA]** Slides 16–17 — atividade, pontos-chave e encerramento.

> "Sua missão: calcular no QGIS o volume de uma pilha e ver quanto ele muda com 5 centímetros de viés. Hoje fomos das fotos aos metros cúbicos. Mas e debaixo da mata, onde a câmera não vê o chão? E a fachada descolando? Na próxima aula, LiDAR embarcado e termografia. Te espero na Aula 8!"

---

## Aula 8 — LiDAR embarcado e termografia na inspeção de estruturas e fachadas

> Dois pedidos chegam no mesmo dia. O primeiro: levantar o terreno natural de uma encosta coberta de mata, onde vai passar o acesso de uma obra — e a fotogrametria da semana passada só "viu" a copa das árvores. O segundo: um condomínio de 15 anos com fachada em revestimento cerâmico quer saber **onde as placas estão descolando** antes que uma caia na calçada. Nenhum dos dois se resolve com a câmera RGB. Nesta aula você vai conhecer as duas cargas úteis que completam o kit do drone de engenharia: o **LiDAR embarcado** e a **câmera térmica**.

### LiDAR: medir distância com luz

O **LiDAR** (*light detection and ranging*) emite pulsos de laser e mede o **tempo de ida e volta** de cada um. A distância é

$
R = \frac{c \cdot \Delta t}{2}
$

com $c \approx 3 \times 10^8\,\mathrm{m/s}$. Um alvo a 80 m devolve o pulso em cerca de 533 nanossegundos. Combinando a distância com o **ângulo** do feixe e com a **posição e a atitude** do drone — dadas por **GNSS RTK/PPK** e por uma **IMU** de alta qualidade —, cada pulso vira um ponto $X, Y, Z$. Ao contrário da fotogrametria, o LiDAR **não precisa de textura nem de luz** (voa à noite) e mede a distância diretamente.

### Múltiplos retornos: o chão sob a vegetação

O feixe tem alguns centímetros de diâmetro ao chegar ao alvo. Numa árvore, parte da energia volta da copa, parte de galhos e parte **do chão**, passando pelas frestas: são os **múltiplos retornos**. Classificando o **último retorno**, obtém-se o MDT mesmo sob vegetação — onde a fotogrametria só entrega o MDS. Atenção: o laser **não atravessa** folhas; ele passa **pelos vãos**. Mata muito fechada ainda pode deixar poucos pontos no solo.

![Nuvem de pontos LiDAR aérea colorida por altura, mostrando quatro torres em forma de L ao redor de um grande pátio retangular arborizado, com edifícios e ruas do entorno](https://upload.wikimedia.org/wikipedia/commons/8/8d/BNF_Lidar_HD.png)

### Densidade de pontos e exatidão

A **densidade** de uma faixa é aproximadamente a taxa de pulsos dividida pela área varrida por segundo:

$
\rho \approx \frac{PRR}{v \cdot W}
\qquad
W = 2\,H\,\tan\left(\frac{FOV}{2}\right)
$

onde $PRR$ é a taxa de repetição de pulsos, $v$ a velocidade e $W$ a largura da faixa. A exatidão depende sobretudo da **trajetória**: um erro angular de atitude $\delta\theta$ desloca o ponto em cerca de $R \cdot \delta\theta$ — por isso o LiDAR embarcado cobra uma IMU muito melhor que a de um drone de fotografia, e por isso o sistema é caro. A conferência é a mesma da Aula 6: **checkpoints e RMSE**.

### LiDAR × fotogrametria

| Critério | Fotogrametria (RGB) | LiDAR embarcado |
| --- | --- | --- |
| Solo sob vegetação | não vê (só MDS) | vê pelas frestas (MDT) |
| Superfície sem textura | falha | mede normalmente |
| Iluminação | precisa de luz e sombras curtas | independe |
| Cor e textura | sim (ortomosaico) | não, sem câmera auxiliar |
| Fios, cabos, estruturas finas | difícil | bom |
| Custo do equipamento | baixo a médio | alto |

Na obra, o LiDAR brilha em **terreno natural com vegetação**, **linhas de transmissão**, **corredores** de rodovia e ferrovia, **estruturas metálicas** e **túneis** (com LiDAR terrestre ou móvel). Para terraplenagem em solo exposto, a fotogrametria costuma ser suficiente — e mais barata.

### Termografia: enxergar temperatura

Todo corpo acima do zero absoluto emite radiação infravermelha; a **câmera térmica** (em geral um microbolômetro na faixa de 8 a 14 µm) mede essa radiação e a converte em temperatura aparente, exibida em **cores falsas** no **termograma**. A conversão depende da **emissividade** do material (quanto ele emite em relação a um corpo negro ideal), da **temperatura refletida** do entorno, da distância e da umidade do ar. Superfícies brilhantes — metal polido, vidro — têm baixa emissividade e **refletem** o calor de outros objetos: o termograma pode "mentir".

![Termograma de uma torre residencial com varandas de formas onduladas, feito em dia frio: as bordas das lajes das varandas aparecem em amarelo e laranja, indicando perda de calor pelas pontes térmicas, contra o fundo roxo e azul mais frio](https://upload.wikimedia.org/wikipedia/commons/8/8c/Aqua_Tower_thermal_imaging.jpg)

### Termografia em fachadas e estruturas

Em inspeções prediais, o que interessa é a **diferença** de temperatura entre regiões, não o valor absoluto. Três aplicações clássicas:

- **Descolamento de revestimento** — a placa solta tem uma camada de ar atrás, que isola. Sob sol, ela **aquece mais rápido** que a placa aderida (fica mais quente no termograma); à noite, **esfria mais rápido**.
- **Umidade e infiltração** — a água evaporando **resfria** a superfície; manchas frias em lajes, platibandas e paredes indicam umidade.
- **Pontes térmicas e instalações** — perdas de calor em vigas, pilares e lajes; painéis elétricos e conexões aquecidos.

A termografia é **passiva** e depende de **fluxo de calor**: sem diferença de temperatura (dia nublado e sem vento, fachada sem insolação), nada aparece. Planeje o horário pela **orientação da fachada** (aquecimento ou resfriamento), evite chuva recente e vento forte, e ajuste a emissividade. Em fachadas, a técnica apoia a inspeção predial da **ABNT NBR 16747** — mas **não substitui** o ensaio de percussão e o de arrancamento nas áreas suspeitas: o termograma diz **onde** olhar.

E lembre da Aula 4: inspeção de fachada é voo próximo a edifício habitado — a distância de **30 m** de pessoas não envolvidas e não anuentes, ou a barreira, define a categoria da operação.

### Exemplo numérico

**(a) LiDAR.** Um LiDAR com $PRR = 240\,\mathrm{kHz}$ e campo de visão de $70°$ voa a $H = 80\,\mathrm{m}$ e $v = 8\,\mathrm{m/s}$:

$
W = 2 \times 80 \times \tan 35° \approx 112\,\mathrm{m}
\qquad
\rho \approx \frac{240.000}{8 \times 112} \approx 268\,\mathrm{pontos/m^2}
$

(densidade de uma única passada e de um retorno por pulso; a sobreposição entre faixas a aumenta). Na borda da faixa, a distância inclinada é $80/\cos 35° \approx 97{,}7\,\mathrm{m}$; um erro de atitude de $0{,}05°$ ($8{,}7 \times 10^{-4}\,\mathrm{rad}$) desloca o ponto em $97{,}7 \times 8{,}7 \times 10^{-4} \approx 0{,}085\,\mathrm{m}$ — **8,5 cm só pela IMU**.

**(b) Termografia.** Uma câmera térmica de $640 \times 512$ pixels, pixel de $12\,\mathrm{\mu m}$ e $f = 13\,\mathrm{mm}$ tem **campo de visão instantâneo** (IFOV, o "GSD angular"):

$
IFOV = \frac{p}{f} = \frac{12 \times 10^{-6}}{13 \times 10^{-3}} \approx 0{,}92\,\mathrm{mrad}
$

A 10 m da fachada, cada pixel cobre $10 \times 0{,}92 \approx 9{,}2\,\mathrm{mm}$; pela regra prática de que um defeito deve ocupar ao menos $3 \times 3$ pixels para ser medido com confiança, o menor defeito é cerca de **2,8 cm**. A 30 m (distância que talvez você precise manter de pessoas na calçada), cada pixel cobre 2,8 cm e o menor defeito confiável passa a cerca de **8,3 cm**. Moral: **a distância de voo é uma decisão de engenharia e de segurança ao mesmo tempo**.

### Atividade prática

Escolha uma fachada que você conhece. Planeje uma inspeção termográfica com drone: orientação da fachada e horário do voo (aquecimento ou resfriamento), distância à fachada e menor defeito detectável (com a câmera do exemplo), condições meteorológicas exigidas e restrições de segurança para pessoas na calçada. Indique quais ensaios complementares você faria nas áreas suspeitas.

### Pontos-chave

- **LiDAR** mede distância pelo tempo de voo do pulso ($R = c\,\Delta t / 2$); com GNSS e IMU, cada pulso vira um ponto 3D.
- **Múltiplos retornos** permitem obter o **MDT sob vegetação** — o laser passa pelas frestas, não pelas folhas.
- Densidade $\rho \approx PRR/(v \cdot W)$; a exatidão depende sobretudo da **trajetória** (GNSS + IMU) e se confere por checkpoints.
- **Termografia** mede **diferenças** de temperatura aparente; depende de emissividade, reflexos e de haver fluxo de calor — planeje horário e clima.
- Em fachadas, o termograma **localiza** suspeitas (descolamento, umidade, pontes térmicas); a confirmação é por ensaio local, no contexto da **NBR 16747**.

### Para saber mais

- **Wikipedia — Lidar:** https://pt.wikipedia.org/wiki/Lidar
- **Wikipedia — Termografia:** https://pt.wikipedia.org/wiki/Termografia
- **Wikipedia — Thermography (aplicações em edificações):** https://en.wikipedia.org/wiki/Thermography

### O que você verá na próxima unidade

Na **Unidade 3 — Sensores IoT no Monitoramento de Obras**, o foco desce do céu para dentro do solo e da estrutura. Você vai estudar o **monitoramento geotécnico** (inclinômetros, piezômetros e marcos de recalque), o **monitoramento estrutural** (extensômetros, acelerômetros, fissurômetros e maturidade do concreto), os sensores de **segurança, ambiente e produtividade** (vibração, ruído, poeira e rastreamento de equipamentos) e, por fim, como transformar leituras em **séries temporais, níveis de alerta e dashboards**. O drone mostra a obra por fora e em campanhas; os sensores contam o que acontece **entre um voo e outro** — e é a combinação dos dois que fecha a malha.

## Aula 8 — Roteiro da Videoaula 8: "LiDAR embarcado e termografia na inspeção de estruturas e fachadas"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e os dois pedidos: a encosta com mata e a fachada cerâmica.

> "Dois pedidos no mesmo dia: levantar o terreno de uma encosta coberta de mata, onde a fotogrametria só viu a copa das árvores, e descobrir onde as placas de uma fachada cerâmica estão descolando. Nenhum dos dois se resolve com a câmera RGB. Hoje, fechando a Unidade 2, você vai conhecer o LiDAR embarcado e a câmera térmica."

### 2. Desenvolvimento — parte 1 (0:25 – 1:30)

**[TELA]** Slides 4–7 — o princípio do LiDAR, um pulso com vários retornos, a encosta em 3D e nuvens de pontos reais.

> "O LiDAR emite pulsos de laser e mede o tempo de ida e volta: a distância é a velocidade da luz vezes o tempo, dividido por dois. A 80 metros, são uns 533 nanossegundos. Com o GNSS e a IMU, cada pulso vira um ponto 3D, e ele não precisa de luz nem de textura. Numa árvore, o mesmo pulso devolve vários ecos: da copa, de um galho e do chão. O primeiro retorno dá o MDS; o último, quando é solo, dá o MDT sob a vegetação. Atenção: o laser não atravessa as folhas — passa pelos vãos entre elas."

### 3. Desenvolvimento — parte 2 (1:30 – 2:20)

**[TELA]** Slides 8–9 — densidade e exatidão e a comparação LiDAR × fotogrametria.

> "A densidade é a taxa de pulsos dividida pela velocidade vezes a largura da faixa. Com 240 quilohertz, 80 metros, campo de visão de 70 graus e 8 metros por segundo, a faixa tem uns 112 metros e a densidade fica perto de 268 pontos por metro quadrado. E um erro de atitude de só 0,05 grau desloca o ponto da borda em uns 8,5 centímetros: a exatidão depende da trajetória. LiDAR brilha sob vegetação, em fios e em corredores; para terraplenagem em solo exposto, a fotogrametria costuma bastar e é mais barata."

### 4. Desenvolvimento — parte 3 (2:20 – 3:20)

**[TELA]** Slides 10–14 — termografia, as três aplicações em fachadas, a fachada simulada ao longo do dia, o planejamento da inspeção e a calculadora do IFOV.

> "A câmera térmica mede infravermelho e mostra temperatura aparente, que depende da emissividade e dos reflexos. Em fachada, o que importa é a diferença: a placa descolada aquece mais rápido sob sol e esfria mais rápido à noite; a umidade aparece fria. Sem fluxo de calor, nada aparece — então o horário do voo é parte do método. O termograma diz onde olhar, mas não substitui a percussão e o arrancamento da NBR 16747. E a distância importa: com IFOV de 0,92 miliradiano, a 10 metros o menor defeito confiável tem uns 2,8 centímetros; a 30 metros, uns 8,3."

### 5. Encerramento (3:20 – 3:50)

**[TELA]** Slides 15–18 — atividade e pontos-chave, fechamento da Unidade 2, prévia da Unidade 3 e encerramento.

> "Com isso, você fecha a Unidade 2: do voo planejado ao modelo 3D, aos volumes, ao LiDAR e à termografia. Na Unidade 3, o foco desce para dentro do solo e da estrutura: sensores geotécnicos e estruturais, segurança e ambiente, e as séries de dados com alertas e dashboards. Te espero na Aula 9!"

---

## Quiz não avaliativo

### Questão 1

Um drone com câmera de pixel $p = 2{,}41\,\mathrm{\mu m}$ e distância focal $f = 8{,}8\,\mathrm{mm}$ mapeia um canteiro a $70\,\mathrm{m}$ acima do ponto de decolagem, com sobreposição lateral planejada de 70%. Parte do terreno é um morro 20 m mais alto que o ponto de decolagem. Sobre o que acontece sobre o morro, assinale a alternativa **correta**:

- [ ] a. O GSD piora (aumenta), porque o drone fica mais longe do terreno, e a sobreposição lateral aumenta.
- [x] b. A altura efetiva cai para 50 m: o GSD melhora (diminui), mas o *footprint* encolhe e a sobreposição lateral cai abaixo do planejado.
- [ ] c. Nada muda, porque o GSD depende da altura em relação ao ponto de decolagem, que é a referência do plano de voo.
- [ ] d. A sobreposição lateral não muda, porque o espaçamento entre faixas é proporcional à altura de voo em qualquer ponto.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) está correta: o $H$ da fórmula $GSD = H \cdot p / f$ é a altura **acima do terreno fotografado**. Sobre o morro, $H = 50\,\mathrm{m}$, o GSD cai de 1,92 para cerca de 1,37 cm, mas a largura da foto cai de 105 para 75 m; como o espaçamento entre faixas foi fixado em 31,5 m, a sobreposição lateral cai para $1 - 31{,}5/75 = 58\%$ — e aparecem falhas no modelo. A (a) inverte o efeito: mais perto do terreno, o GSD diminui. A (c) erra a referência da altura. A (d) é falsa: o espaçamento $d$ é fixo no plano; o que varia com o relevo é o *footprint*. A solução é o voo acompanhando o relevo ou o planejamento pelo ponto mais alto.

### Questão 2

Numa terraplenagem, o volume mensal escavado é obtido comparando o MDT do mês com o do mês anterior. Os checkpoints do levantamento atual mostram resíduos verticais (modelo − campo) de $+3$ a $+4\,\mathrm{cm}$, todos positivos, com média de $+3{,}2\,\mathrm{cm}$, numa frente de 3 ha. Assinale a alternativa **correta**:

- [ ] a. Como o $RMSE_z$ fica abaixo de 5 cm, o levantamento é exato e o volume pode ser usado sem qualquer correção.
- [ ] b. Erros de cota sempre se compensam em áreas grandes, de modo que o efeito sobre o volume é desprezível.
- [ ] c. O problema se resolve trocando o MDT pelo MDS, que tem mais pontos e representa melhor a superfície do terreno.
- [x] d. Há um viés vertical: em 3 ha, 3,2 cm equivalem a cerca de 960 m³, e a causa (GCPs, base RTK, altura de antena) deve ser investigada.

**Resposta correta:** `d`

**Feedback:** A alternativa (d) está correta: resíduos todos de mesmo sinal, com média próxima do próprio RMSE, revelam **erro sistemático**, que não se compensa e vira volume diretamente: $\delta V \approx A \cdot \delta z = 30.000 \times 0{,}032 = 960\,\mathrm{m^3}$. A (a) confunde atender a um limite de RMSE com ausência de viés: o modelo é **preciso, mas com viés**. A (b) só vale para erros **aleatórios**. A (c) piora o problema: o MDS inclui máquinas e vegetação, que viram volume falso.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma construtora executa a terraplenagem de um loteamento de $600 \times 300\,\mathrm{m}$ (18 ha), com uma **frente de corte de 3 ha** e, no extremo sul, uma **encosta de 2 ha coberta por mata**, onde será aberto um acesso. A gerenciadora exige **levantamento mensal** com GSD de no máximo $2{,}5\,\mathrm{cm}$ e $RMSE_z \le 5\,\mathrm{cm}$ nos checkpoints. O drone disponível é um multirrotor com RTK, câmera de $5.472 \times 3.648$ pixels, $p = 2{,}41\,\mathrm{\mu m}$ e $f = 8{,}8\,\mathrm{mm}$, voando a $8\,\mathrm{m/s}$, com 20 min úteis por bateria.
>
> Estruture sua resposta em quatro partes:
>
> 1. **Planejamento de voo** — calcule a altura máxima para o GSD exigido e adote $H = 90\,\mathrm{m}$. Para esse $H$, calcule o GSD, o *footprint*, a base e o espaçamento entre faixas (sobreposições de 80% frontal e 70% lateral), o intervalo entre fotos, o número aproximado de faixas e de fotos (faixas ao longo dos 600 m) e o tempo de voo. Cabe numa bateria? Que cuidado regulatório o voo exige por ser um mapeamento em faixas sobrepostas?
> 2. **Controle e exatidão** — proponha a quantidade e a distribuição de GCPs e de checkpoints. No levantamento deste mês, os resíduos verticais dos 5 checkpoints foram $+3{,}1$; $+2{,}4$; $+4{,}0$; $+2{,}8$ e $+3{,}7\,\mathrm{cm}$. Calcule a média e o $RMSE_z$. O levantamento atende à especificação? Ele é preciso? É exato? O que você investigaria?
> 3. **Volume** — o volume escavado no mês (MDT anterior − MDT atual) na frente de 3 ha resultou em $21.600\,\mathrm{m^3}$. Sabendo que o levantamento anterior foi validado sem viés, estime o efeito do viés do item 2 sobre esse volume e o volume corrigido. Explique por que se usa o MDT, e não o MDS.
> 4. **Encosta com mata** — o drone com câmera RGB consegue gerar o MDT da encosta? Proponha o sensor adequado e estime a densidade de pontos de um LiDAR com $PRR = 240\,\mathrm{kHz}$ e campo de visão de $70°$, voando a $80\,\mathrm{m}$ e $8\,\mathrm{m/s}$. Como você verificaria a exatidão desse levantamento?

**Resposta esperada:**

> **Parte 1.** Altura máxima: $H_{máx} = GSD \cdot f / p = 0{,}025 \times 8{,}8 / 0{,}00241 \approx 91{,}3\,\mathrm{m}$. Com $H = 90\,\mathrm{m}$ (abaixo do teto de 120 m da categoria aberta):
>
> $
> GSD = \frac{90 \times 0{,}00241}{8{,}8} \approx 2{,}46\,\mathrm{cm}
> \qquad
> W \approx 5.472 \times 0{,}0246 \approx 135\,\mathrm{m}
> \qquad
> L \approx 3.648 \times 0{,}0246 \approx 90\,\mathrm{m}
> $
>
> $
> B = 90 \times 0{,}2 = 18\,\mathrm{m}
> \qquad
> d = 135 \times 0{,}3 = 40{,}5\,\mathrm{m}
> \qquad
> \Delta t = 18/8 = 2{,}25\,\mathrm{s}
> $
>
> Faixas: $\lceil 300/40{,}5 \rceil + 1 = 9$; fotos por faixa: $\lceil 600/18 \rceil + 1 = 35$; total de cerca de **315 fotos**. Percurso: $9 \times 600 + 8 \times 40{,}5 = 5.724\,\mathrm{m}$, ou $5.724/8 \approx 716\,\mathrm{s} \approx 11{,}9\,\mathrm{min}$ — **cabe numa bateria** (a capacidade por bateria é $A = 8 \times 1.200 \times 40{,}5 \approx 38{,}9\,\mathrm{ha}$). Boa resposta comenta o relevo (a encosta reduz a altura efetiva e a sobreposição; usar voo acompanhando o terreno) e o arrasto. Regulação: mapeamento em faixas sobrepostas é **aerolevantamento** — empresa inscrita no Ministério da Defesa e pedido no **SARPAS com 4 dias corridos** de antecedência —, além do enquadramento no RBAC nº 100, SISANT, piloto, seguro e LGPD.
>
> **Parte 2.** Espera-se algo como **5 a 8 GCPs** no perímetro e no interior (incluindo pontos altos e baixos) e **checkpoints independentes** (ao menos 5 para o controle de rotina; o padrão ASPRS 2023 pede 30 para conformidade plena), medidos com GNSS RTK ou estação total, sem uso no processamento. Cálculo:
>
> $
> \bar{\Delta z} = \frac{3{,}1 + 2{,}4 + 4{,}0 + 2{,}8 + 3{,}7}{5} = 3{,}2\,\mathrm{cm}
> \qquad
> RMSE_z = \sqrt{\frac{9{,}61 + 5{,}76 + 16{,}00 + 7{,}84 + 13{,}69}{5}} \approx 3{,}25\,\mathrm{cm}
> $
>
> Numericamente, $3{,}25 \le 5\,\mathrm{cm}$: **atende** à especificação. Mas todos os resíduos são positivos e a média é quase igual ao RMSE: a dispersão em torno da média é só $\sqrt{3{,}25^2 - 3{,}2^2} \approx 0{,}6\,\mathrm{cm}$. O modelo é **preciso, mas tem viés** — não é exato no sentido de veracidade (Aula 2). Investigar: altura da antena nos GCPs ou na base, coordenadas da base RTK, sistema de altitudes, calibração da câmera.
>
> **Parte 3.** O MDT atual está, em média, 3,2 cm **acima** do real; como o volume escavado é MDT anterior − MDT atual, o volume está **subestimado** em $\delta V \approx A \cdot \delta z = 30.000 \times 0{,}032 = 960\,\mathrm{m^3}$. Volume corrigido: $21.600 + 960 = 22.560\,\mathrm{m^3}$ (diferença de cerca de 4,3%). O ideal é corrigir a causa e reprocessar, não apenas somar o valor. Usa-se o **MDT** porque o MDS inclui máquinas, caminhões, vegetação e pilhas temporárias, que viram volume falso.
>
> **Parte 4.** Não: sob mata, a câmera vê a copa, e a fotogrametria gera só o MDS. O sensor adequado é o **LiDAR embarcado**, cujos **múltiplos retornos** passam pelas frestas da vegetação; com o último retorno classificado como solo, obtém-se o MDT. Densidade:
>
> $
> W = 2 \times 80 \times \tan 35° \approx 112\,\mathrm{m}
> \qquad
> \rho \approx \frac{240.000}{8 \times 112} \approx 268\,\mathrm{pontos/m^2}
> $
>
> (uma passada; sob a mata, só uma fração desses pontos chega ao solo). A exatidão se verifica com **checkpoints em clareiras e em áreas abertas** e com o RMSE, como na fotogrametria; a qualidade depende da trajetória (GNSS RTK/PPK + IMU). Resposta exemplar integra as quatro partes num procedimento mensal coerente, com método e tolerância definidos em contrato para a medição.

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

> Recomendo a **"Aula 1 — Fotogrametria e drones em geociências"**, do canal do SPAMLab (Instituto de Astronomia, Geofísica e Ciências Atmosféricas da USP), no YouTube: a primeira aula, gravada em português, de uma disciplina de pós-graduação sobre fotogrametria e drones aplicados às geociências. É uma aula longa (cerca de 1h20): assista acompanhando as Aulas 5 e 6 e anote onde aparecem GSD, sobreposição, pontos de controle e exatidão. Para praticar, use a documentação do OpenDroneMap, software livre de processamento, que traz boas práticas de voo e conjuntos de dados de exemplo.

- **Link(s):** https://www.youtube.com/watch?v=_YEmntlFf7E · https://docs.opendronemap.org/
- **Aula em que entra:** Aulas 5 e 6

### Podcast (curadoria, até 45 min)

> No episódio #2 do **Nuvem Cast**, do canal Nuvem UAV, a pergunta é direta: **"Topografia com drones realmente funciona?"**. Os convidados são os professores Antonio Tommaselli e João Galera, referências brasileiras em fotogrametria e geodésia. Ouça com o olhar crítico desta unidade: em que condições a topografia com drone entrega exatidão de engenharia? Que papel têm os pontos de controle, o GNSS e a verificação independente? É o centro das Aulas 6 e 7. O episódio completo tem cerca de 1h14; para esta curadoria, ouça os **primeiros 45 minutos**.

- **Nome do podcast/canal:** Nuvem Cast (canal Nuvem UAV, no YouTube)
- **Tema recomendado:** Episódio #2 — Topografia com drones realmente funciona?
- **Link:** https://www.youtube.com/watch?v=xBgA7UZqNy8
- **Aula em que entra:** Aulas 6 e 7

### Artigo científico

> Artigo de referência sobre o uso de drones no **levantamento de terraplenagem**. Os autores avaliam o desempenho de um sistema com drone construído para adquirir, de forma rápida e autônoma, dados de mapeamento 3D em grandes obras de movimentação de terra: descrevem o equipamento, o **planejamento dos voos fotogramétricos** e a geração de **nuvens de pontos**, e propõem um **modelo para estimar o erro de posição**, testado em canteiros reais de escavação e terraplenagem. É a ponte entre o planejamento da Aula 5, a exatidão da Aula 6 e os volumes da Aula 7.

- **Link:** https://doi.org/10.1016/j.autcon.2014.01.004
- **Aula em que entra:** Aulas 5, 6 e 7
- **Referência bibliográfica do artigo no formato ABNT:**
  > SIEBERT, Sebastian; TEIZER, Jochen. Mobile 3D mapping for surveying earthwork projects using an Unmanned Aerial Vehicle (UAV) system. **Automation in Construction**, v. 41, p. 1-14, 2014. DOI: 10.1016/j.autcon.2014.01.004.
