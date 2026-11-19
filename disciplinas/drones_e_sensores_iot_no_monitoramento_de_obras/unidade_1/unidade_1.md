# Unidade 1 — Fundamentos do Monitoramento Digital de Obras

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 1 a 4

## Vídeo introdutório + Relação da disciplina com a atuação profissional

Pense na última obra grande por que você passou: um edifício com três subsolos, um viaduto, um loteamento com quilômetros de terraplenagem. Agora pense na pergunta que o engenheiro responsável faz todas as manhãs: **a obra está como deveria estar?** O prédio vizinho recalcou? O nível d'água na escavação subiu com a chuva da madrugada? Quantos metros cúbicos de aterro foram executados esta semana — e quantos foram medidos? Durante décadas, essas respostas vieram de vistorias a pé, do diário de obra escrito à mão e de levantamentos topográficos feitos de tempos em tempos. Hoje elas podem vir **de um drone que sobrevoa o canteiro em vinte minutos e de sensores que enviam leituras a cada quinze minutos para a nuvem**.

Esta disciplina existe para te preparar para essa transformação. Vamos partir do zero: o que é medir, o que é um sensor, como um dado sai do canteiro e chega à tela de quem decide. Depois vamos estudar os drones — tipos, regulamentação, planejamento de voo, fotogrametria, nuvens de pontos e cálculo de volumes —, os sensores IoT do monitoramento geotécnico e estrutural (inclinômetros, piezômetros, extensômetros, acelerômetros) e, por fim, a integração de tudo isso com BIM, gêmeo digital e inteligência artificial.

O diferencial de mercado é concreto. Construtoras, gerenciadoras, concessionárias de infraestrutura, mineradoras e empresas de instrumentação geotécnica procuram engenheiros que saibam **especificar** um plano de monitoramento, **interpretar** os dados com senso crítico e **transformar** leitura em decisão. Poucos colegas de graduação dominam a combinação de engenharia civil, metrologia, conectividade e regulamentação aeronáutica — e é exatamente essa combinação que você vai construir aqui.

Ao final, você será capaz de desenhar um sistema de monitoramento completo para uma obra real: o que medir, com qual instrumento, com que frequência, com quais limites de alerta e com qual resposta prevista. Isso é engenharia de verdade, não apenas tecnologia.

### Roteiro do vídeo introdutório (até 2 min)

*Acompanha o deck `slides/aula0.html` (13 slides). Cada bloco indica a tela correspondente.*

**Abertura (0:00 – 0:20):**
[TELA: Slide 1 — capa; Slide 2 — audiodescrição; Slide 3 — Sobre o professor]
> "Olá! Eu sou o professor Afonso Brandão. Para quem usa audiodescrição: sou um homem de pele clara, com cabelos castanho-escuros curtos e barba cheia, também escura e bem aparada; tenho olhos castanhos e sobrancelhas grossas, e apareço em plano médio, de frente para a câmera. Seja muito bem-vindo(a) a Drones e Sensores IoT no Monitoramento de Obras."

**Conexão com o mercado (0:20 – 0:55):**
[TELA: Slide 4 — sumário; Slide 5 — foto aérea do canteiro; Slide 6 — canteiro conectado em 3D]
> "Toda obra tem a mesma pergunta diária: está tudo sob controle? O prédio vizinho recalcou? O talude está se movendo? Quanto de terra já movimentamos? Hoje, um drone registra o canteiro inteiro em um voo, e sensores conversam com a nuvem dia e noite. Construtoras, concessionárias e empresas de instrumentação precisam de engenheiros que saibam usar esses dados para decidir."

**Conteúdo e diferencial (0:55 – 1:25):**
[TELA: Slide 7 — o que vamos monitorar; Slide 8 — do diário de obra ao canteiro conectado; Slide 9 — gêmeo digital em 3D; Slide 10 — 16 videoaulas em 4 unidades]
> "Vamos do zero. Primeiro, os fundamentos: medição, sensores, redes IoT e a regulamentação de drones no Brasil. Depois, o drone na prática: planejamento de voo, fotogrametria, volumes, LiDAR e termografia. Em seguida, os sensores do monitoramento geotécnico e estrutural. E, para fechar, BIM, gêmeo digital e inteligência artificial: a obra viva dentro do computador, em malha fechada."

**Benefício para o aluno (1:25 – 1:45):**
[TELA: Slide 11 — onde isso aparece na sua carreira; Slide 12 — como você será avaliado]
> "Ao final, você consegue **projetar** um plano de monitoramento, **interpretar** os dados com senso crítico e **decidir** com base neles. Nas avaliações, a pergunta será sempre a mesma: o que o engenheiro deve fazer com esse dado?"

**Encerramento (1:45 – 2:00):**
[TELA: Slide 13 — encerramento]
> "Bora começar? A obra do futuro já está conectada e precisa de engenheiros que saibam ler o que ela está dizendo. Te espero na Aula 1!"

---

## Aula 1 — Monitoramento de obras na era digital: do diário de obra ao canteiro conectado

> Segunda-feira, 7h. O mestre de obras liga: "Engenheiro, apareceu uma trinca na garagem do prédio vizinho". A escavação do seu subsolo está a 6 metros de profundidade. A trinca é antiga ou nova? Está crescendo? Tem relação com a sua obra? Se a única informação disponível for uma anotação no diário de obra de três semanas atrás, você está decidindo no escuro. Nesta aula, você vai entender **por que** e **como** se monitora uma obra, o que drones e sensores resolvem (e o que não resolvem) e dois conceitos que vão atravessar toda a disciplina: o **gêmeo digital** e a **malha fechada**.

### Por que monitorar uma obra?

Monitorar é **medir de forma sistemática, ao longo do tempo, grandezas que indicam se a obra está se comportando como o projeto previu**. As razões se agrupam em quatro dimensões clássicas da gestão:

- **Prazo** — avanço físico real comparado ao cronograma (volumes escavados, pavimentos concretados, área de fachada executada).
- **Custo** — medição de serviços para pagamento, controle de perdas e de retrabalho.
- **Segurança** — de pessoas (quedas, interferência de equipamentos) e de estruturas (recalques, deslocamentos de contenções, nível d'água em escavações).
- **Qualidade** — conformidade geométrica (prumo, nível, espessuras) e desempenho dos materiais (temperatura e maturidade do concreto, por exemplo).

Monitorar não é luxo: é a forma de transformar **incerteza de projeto** — o solo nunca é exatamente o da sondagem — em **informação de obra**.

### Do diário de obra ao canteiro conectado

O monitoramento tradicional se apoia no **diário de obra**, em vistorias visuais, em fotos de celular e em campanhas periódicas de topografia e instrumentação lidas manualmente. Funciona, mas tem três fragilidades: **baixa frequência** (a leitura é semanal ou mensal), **atraso** (o dado leva dias para virar relatório) e **subjetividade** (cada vistoriador descreve do seu jeito).

![Vista aérea, feita por drone, do canteiro de obras do Pronto-Socorro Central de Itapevi (SP): terreno cercado por tapume, com contêineres e materiais, ao lado do prédio existente, de ruas e do bairro. Foto: Célio Junior / Prefeitura de Itapevi, Wikimedia Commons, CC BY 2.0](https://upload.wikimedia.org/wikipedia/commons/c/cc/%282019.12.09%29_Obras_PS_Central%2C_Drone_%2849204900632%29.jpg)

No **canteiro conectado**, drones produzem ortofotos e modelos 3D do canteiro inteiro em um único voo, e sensores em contenções, fundações e estruturas enviam leituras sozinhos para uma plataforma na nuvem. A frequência sobe de mensal para horária, o atraso cai de dias para minutos e o dado passa a ser **quantitativo e rastreável**.

### O ciclo dado → informação → decisão → ação

Dado sozinho não salva obra nenhuma. O valor aparece quando o dado percorre um ciclo completo:

1. **Dado** — a leitura bruta: "o inclinômetro registrou 18 mm a 4 m de profundidade".
2. **Informação** — o dado comparado a uma referência: "o deslocamento é 60% do limite de projeto e dobrou em uma semana".
3. **Decisão** — o julgamento técnico: "reduzir a escavação na frente norte e instalar mais uma linha de tirantes".
4. **Ação** — a intervenção executada no canteiro.

Toda a tecnologia desta disciplina serve para **encurtar e tornar confiável** esse ciclo.

### Malha aberta × malha fechada

A engenharia de controle oferece uma distinção poderosa. Em **malha aberta**, você mede e arquiva: a leitura vira relatório e ninguém a compara com um limite a tempo de agir — o que acontece em muitas obras.

Em **malha fechada**, a medição **realimenta** a execução: **medir → comparar com a referência ou o limite → decidir → agir na obra → medir de novo** para confirmar o efeito. Se o deslocamento da contenção parou de crescer depois dos tirantes adicionais, o laço confirma a decisão; se não parou, dispara uma nova. Na Aula 3 você verá como uma arquitetura IoT implementa esse laço.

### Gêmeo digital: modelo, sombra e gêmeo

Um termo que você vai ouvir muito é **gêmeo digital** (*digital twin*): um **modelo digital vinculado ao ativo físico por um fluxo de dados contínuo**, que representa o estado atual da obra e permite simular e decidir sobre ela. Kritzinger *et al.* (2018) propuseram uma classificação útil, baseada no grau de integração dos dados:

- **Modelo digital** — não há troca automática de dados entre físico e digital. Um modelo BIM atualizado à mão é um modelo digital.
- **Sombra digital** — o dado flui **automaticamente** do físico para o digital, mas a volta (do digital para o físico) depende de ação manual.
- **Gêmeo digital** — o fluxo é automático **nos dois sentidos**: o estado da obra atualiza o modelo e o modelo devolve comandos ou decisões ao ativo.

Repare na ligação entre os conceitos: um gêmeo digital é, por definição, uma **malha fechada** entre o canteiro e o modelo. Na prática da construção, a maior parte dos sistemas atuais é sombra digital — e tudo bem, desde que o laço seja fechado por um engenheiro que decide.

### O que drones e sensores resolvem — e o que não resolvem

Drones e sensores resolvem **cobertura** (o canteiro inteiro em um voo), **frequência** (leituras contínuas), **acesso** (fachadas, coberturas e taludes sem expor pessoas) e **rastreabilidade** (dado datado e georreferenciado). Mas **não** resolvem: projeto mal feito, ausência de limites de alerta definidos, sensor mal instalado ou nunca calibrado, nem a falta de alguém com autoridade para agir. Um sistema de monitoramento sem plano de resposta é só um gerador de gráficos bonitos.

![Estação total robótica e prisma topográfico montados em tripés amarelos sobre calçada, prontos para um levantamento em área urbana](https://upload.wikimedia.org/wikipedia/commons/1/15/Surveying_prism_and_total_station%2C_for_land_surveying%2C_in_Shibuya-ku.jpg)

A topografia convencional, com estação total e GNSS, continua indispensável: fornece pontos de controle e valida os produtos aéreos.

### Exemplo numérico

Considere um canteiro de terraplenagem com área $A = 12\,\mathrm{ha}$ que precisa de um levantamento planialtimétrico **por mês** para medir volumes. Os valores a seguir são **ilustrativos** — servem para treinar o raciocínio, não como tabela de preços.

**Levantamento convencional** (estação total/GNSS): produtividade de campo $p_c = 3\,\mathrm{ha/dia}$, mais 1 dia de escritório, com custo de equipe de R\$ 2.400 por dia.

$
T_c = \frac{A}{p_c} + t_{esc} = \frac{12}{3} + 1 = 5\,\mathrm{dias}
\qquad
C_c = 5 \times 2.400 = \mathrm{R\$}\,12.000
$

**Levantamento com drone** (1 dia de campo com pontos de controle + 1 dia de processamento), com custo de equipe e equipamento de R\$ 3.000 por dia:

$
T_d = 1 + 1 = 2\,\mathrm{dias}
\qquad
C_d = 2 \times 3.000 = \mathrm{R\$}\,6.000
$

Em 10 medições mensais, a economia é $10 \times (12.000 - 6.000) = \mathrm{R\$}\,60.000$. Mais importante que o dinheiro: o dado chega **3 dias antes** a quem decide, e a densidade de informação muda de escala — o convencional entrega, digamos, 1 ponto a cada $100\,\mathrm{m^2}$ (cerca de 1.200 pontos), enquanto o drone gera uma nuvem com dezenas de pontos por $\mathrm{m^2}$. A ressalva: o drone não enxerga sob vegetação densa nem dentro de galerias, e sua exatidão depende dos pontos de controle medidos em campo.

### Atividade prática

Escolha uma obra que você conhece (pode ser uma obra pública noticiada na sua cidade). Em uma folha:

1. Liste **3 riscos** dessa obra ligados a prazo, custo, segurança ou qualidade.
2. Para cada risco, indique **o que medir** e se a medição seria por drone, por sensor ou por topografia convencional.
3. Descreva, para um dos riscos, a **malha fechada** completa: medição, referência/limite, decisão e ação.
4. Classifique o sistema que você imaginou como modelo digital, sombra digital ou gêmeo digital — e justifique.

### Pontos-chave

- Monitorar é medir sistematicamente, ao longo do tempo, grandezas que indicam se a obra se comporta como o projeto previu — em **prazo, custo, segurança e qualidade**.
- O valor do monitoramento está no ciclo **dado → informação → decisão → ação**; dado arquivado sem comparação é **malha aberta**.
- **Malha fechada**: medir → comparar com o limite → decidir → agir → medir de novo para confirmar.
- **Gêmeo digital** é o modelo vinculado ao ativo por fluxo de dados contínuo e bidirecional; com fluxo só físico → digital, temos uma **sombra digital** (Kritzinger *et al.*, 2018).
- Drones e sensores aumentam cobertura, frequência e rastreabilidade, mas **não substituem** limites de alerta, calibração e um plano de resposta.

### Para saber mais

- **Wikipedia — Gêmeo digital:** https://pt.wikipedia.org/wiki/G%C3%AAmeo_digital
- **KRITZINGER, W. et al. — *Digital Twin in manufacturing: a categorical literature review and classification* (modelo, sombra e gêmeo digital):** https://doi.org/10.1016/j.ifacol.2018.08.474
- **Wikipedia — Sistema de controle (malha aberta e malha fechada):** https://pt.wikipedia.org/wiki/Sistema_de_controle
- **Wikipedia — Estação total:** https://pt.wikipedia.org/wiki/Esta%C3%A7%C3%A3o_total

## Aula 1 — Roteiro da Videoaula 1: "Monitoramento de obras na era digital: do diário de obra ao canteiro conectado"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e a trinca na garagem do vizinho.

> "Segunda-feira, sete da manhã, o mestre de obras liga: apareceu uma trinca na garagem do prédio vizinho. Sua escavação está a seis metros. A trinca é nova? Está crescendo? Se a única informação que você tem é uma anotação de três semanas atrás no diário de obra, você está decidindo no escuro. Hoje a gente vai entender por que e como se monitora uma obra."

### 2. Desenvolvimento — parte 1 (0:30 – 1:10)

**[TELA]** Slides 4–8 — quatro dimensões, as três fragilidades, o canteiro conectado em 3D, a mudança de escala e o ciclo dado → ação.

> "Monitorar é medir de forma sistemática, ao longo do tempo, aquilo que mostra se a obra está se comportando como o projeto previu. E a gente monitora por quatro motivos: prazo, custo, segurança e qualidade. O jeito tradicional — diário de obra, vistoria, foto de celular, topografia de vez em quando — funciona, mas é lento, pouco frequente e subjetivo. O canteiro conectado muda isso: o drone cobre o canteiro inteiro num voo, e os sensores mandam leitura sozinhos para a nuvem. Só que dado sozinho não salva obra. Ele precisa virar informação, a informação vira decisão e a decisão vira ação no canteiro."

### 3. Desenvolvimento — parte 2 (1:10 – 2:00)

**[TELA]** Slides 9–12 — malha aberta × fechada, Kritzinger, o gêmeo digital em 3D e as peças de um gêmeo.

> "Agora, dois conceitos que vão acompanhar a gente na disciplina inteira. O primeiro é malha fechada. Malha aberta é medir e arquivar: o relatório vai para a pasta e ninguém compara com limite nenhum. Malha fechada é medir, comparar com o limite, decidir, agir na obra e medir de novo para confirmar que funcionou. O segundo é gêmeo digital: um modelo digital ligado à obra por um fluxo contínuo de dados. Kritzinger e colegas separam três níveis: modelo digital, sem troca automática; sombra digital, quando o dado vem sozinho do canteiro para o modelo; e gêmeo digital, quando o fluxo é automático nos dois sentidos. Perceberam? Gêmeo digital é, por definição, uma malha fechada."

### 4. Desenvolvimento — parte 3 (2:00 – 2:40)

**[TELA]** Slides 13–16 — o que resolve e o que não resolve, a calculadora de 12 ha, a densidade de informação e a atividade.

> "Vamos fazer uma conta. Um canteiro de 12 hectares, com levantamento mensal. No convencional, a 3 hectares por dia mais um dia de escritório, são 5 dias e uns 12 mil reais. Com drone, 2 dias e uns 6 mil — valores ilustrativos, tá? Em dez meses, 60 mil reais de economia. Mas o principal é outro: o dado chega três dias antes e com uma densidade muito maior. E atenção: o drone não enxerga debaixo de vegetação, e a exatidão dele depende dos pontos de controle medidos pela topografia. Uma tecnologia complementa a outra."

### 5. Encerramento (2:40 – 3:10)

**[TELA]** Slides 17–18 — pontos-chave e encerramento.

> "Hoje você viu por que monitorar, o ciclo do dado até a ação, a diferença entre malha aberta e malha fechada e o que é, de verdade, um gêmeo digital. Mas tem uma pergunta anterior a tudo isso: dá para confiar na leitura do sensor? Qual é a incerteza dela? Esse é o assunto da próxima aula, sobre os fundamentos de sensoriamento. Te espero na Aula 2!"

---

## Aula 2 — Fundamentos de sensoriamento: grandezas, transdutores, incerteza e calibração

> O sistema de monitoramento acusa: o recalque do pilar P12 do prédio vizinho chegou a 9 mm, e o nível de alerta é 10 mm. Você mobiliza a equipe ou espera a próxima leitura? A resposta depende de uma pergunta que muita gente esquece de fazer: **qual é a incerteza desses 9 mm?** Se ela for de ±0,2 mm, você está longe do alerta; se for de ±1,5 mm, o alerta pode já ter sido atingido. Nesta aula, você vai aprender a linguagem da metrologia — grandeza, transdutor, exatidão, precisão, incerteza e calibração — sem a qual nenhum dado de sensor merece confiança.

### Grandezas e mensurandos

Toda medição começa pela **grandeza** que se quer conhecer: deslocamento, recalque, inclinação, pressão de água no solo (poropressão), deformação específica, temperatura, aceleração. O valor específico que se deseja medir — "o recalque do pilar P12 entre 1º e 15 de março" — é o **mensurando**. Definir bem o mensurando é metade do trabalho: recalque em relação a quê? Medido onde? Com que referência?

Nas obras, as grandezas mais comuns são geométricas (deslocamentos e recalques, em mm), hidráulicas (nível d'água e poropressão, em m ou kPa), mecânicas (deformação, em $\mu\varepsilon$; força, em kN; aceleração, em $\mathrm{m/s^2}$, medida por acelerômetro; e velocidade de vibração, em mm/s, medida por sismógrafo de engenharia com geofones ou obtida integrando o sinal do acelerômetro) e térmicas (°C, fundamentais no concreto massa e na correção de outras leituras).

### Sensores, transdutores e o sinal elétrico

O **sensor** é o elemento que responde à grandeza física; o **transdutor** converte essa resposta em um sinal mensurável, quase sempre elétrico. Um **extensômetro elétrico de resistência** (*strain gauge*) é o exemplo clássico: uma grade metálica colada à peça que, ao se deformar, muda de resistência elétrica.

![Extensômetro elétrico de resistência colado sobre uma peça metálica, com a grade metálica em zigue-zague e dois fios de ligação soldados](https://upload.wikimedia.org/wikipedia/commons/9/9c/Strain_gauge_-.jpg)

Na instrumentação de obras, são muito usados: **transdutores de corda vibrante** (a frequência de um fio tensionado varia com a deformação ou a pressão — robustos e estáveis por anos), **piezorresistivos** (pressão), **MEMS** (acelerômetros e inclinômetros em chip) e **potenciômetros/LVDT** (deslocamento). O sinal costuma ser padronizado — por exemplo, **4–20 mA** em corrente — e lido por um **datalogger**, que registra as leituras e as entrega à rede.

### Características estáticas: faixa, resolução, sensibilidade

- **Faixa de medição** — intervalo de valores que o instrumento mede corretamente (ex.: 0 a 200 kPa).
- **Resolução** — a menor variação que o instrumento consegue indicar (ex.: 0,01 mm).
- **Sensibilidade** — razão entre a variação da indicação (saída) e a variação correspondente do mensurando (entrada). Um transdutor 4–20 mA de 0 a 200 kPa tem sensibilidade $16\,\mathrm{mA}/200\,\mathrm{kPa} = 0{,}08\,\mathrm{mA/kPa}$; o inverso, $12{,}5\,\mathrm{kPa/mA}$, é o **fator de escala** usado para converter a leitura.
- **Deriva** (*drift*) — variação lenta da indicação ao longo do tempo sem variação do mensurando; crítica em monitoramentos de meses.
- **Histerese** — diferença de indicação para o mesmo valor, dependendo de a grandeza estar subindo ou descendo.

Cuidado com uma confusão frequente: **resolução não é exatidão**. Um sensor pode exibir três casas decimais e errar por um milímetro inteiro.

### Exatidão × precisão (e incerteza)

O Vocabulário Internacional de Metrologia (VIM) separa três ideias. **Precisão** é a proximidade entre medições repetidas, entre si (erro aleatório pequeno). **Veracidade** é a proximidade entre a **média** de muitas medições e o valor verdadeiro (erro sistemático, o viés, pequeno). **Exatidão** é a proximidade entre **uma** medição e o valor verdadeiro, e por isso exige as duas. Pense em tiros num alvo: agrupados e longe do centro = precisos, mas com viés (veracidade ruim, corrigível por calibração); espalhados em torno do centro = sem viés, mas imprecisos (cada tiro isolado é inexato).

Como o valor verdadeiro nunca é conhecido, a metrologia expressa a qualidade de uma medição pela **incerteza de medição**: um parâmetro que caracteriza a dispersão dos valores que podem ser razoavelmente atribuídos ao mensurando. Quando há várias fontes independentes de incerteza, elas se combinam pela **raiz da soma dos quadrados**, conforme o GUM (*Guia para a Expressão da Incerteza de Medição*):

$
u_c = \sqrt{u_1^2 + u_2^2 + \cdots + u_n^2}
$

e a **incerteza expandida** é $U = k \cdot u_c$, com fator de abrangência $k = 2$ para cerca de 95% de confiança.

### Taxa de amostragem e o critério de Nyquist

Um sensor digital lê a grandeza em instantes discretos. Pelo **teorema de Nyquist–Shannon**, para representar um fenômeno com frequência máxima $f_{max}$, a taxa de amostragem deve ser **maior que o dobro** dela: $f_s > 2\,f_{max}$. Se uma vibração de cravação de estacas tem componentes até 50 Hz, amostrar a 100 Hz ou menos não garante o registro, e abaixo de 100 Hz surge o **aliasing** — a vibração aparece com frequência falsa. Na prática, usa-se de 5 a 10 vezes $f_{max}$. Já um piezômetro em solo argiloso pode ser lido a cada hora sem perder nada: a taxa certa depende da **velocidade do fenômeno**, não da vontade de ter muitos dados.

### Calibração e rastreabilidade

**Calibrar** é comparar as indicações do instrumento com um padrão de referência de incerteza conhecida e estabelecer a relação entre elas — muitas vezes uma reta $y = a + b\,x$. A calibração só tem valor se for **rastreável**: o padrão usado foi calibrado por outro padrão, numa cadeia ininterrupta que chega aos padrões nacionais mantidos pelo **Inmetro**. No Brasil, laboratórios acreditados pelo Inmetro compõem a **Rede Brasileira de Calibração (RBC)**, e o certificado de calibração deve trazer a incerteza e a rastreabilidade.

![Medidor elétrico de nível d'água em carretel preto, com visor digital, montado sobre um pilar de concreto junto ao tubo azul de um poço de observação, com o cabo graduado estendido em diagonal; é usado para a leitura manual de piezômetros](https://upload.wikimedia.org/wikipedia/commons/5/5b/Piezometer_for_groundwater.JPG)

### Exemplo numérico

**(a) Reta de calibração de um piezômetro.** Um transdutor de pressão com saída 4–20 mA foi calibrado com dois pontos: 4 mA ↔ 0 kPa e 20 mA ↔ 200 kPa. O coeficiente angular $b$ (fator de escala, inverso da sensibilidade de 0,08 mA/kPa) e o intercepto $a$ são:

$
b = \frac{200 - 0}{20 - 4} = 12{,}5\,\mathrm{kPa/mA}
\qquad
a = 0 - 12{,}5 \times 4 = -50\,\mathrm{kPa}
$

Para uma leitura de 9,6 mA, a poropressão e a coluna d'água correspondente ($\gamma_w = 9{,}81\,\mathrm{kN/m^3}$) valem:

$
p = -50 + 12{,}5 \times 9{,}6 = 70\,\mathrm{kPa}
\qquad
h = \frac{p}{\gamma_w} = \frac{70}{9{,}81} \approx 7{,}14\,\mathrm{m}
$

**(b) Incerteza combinada de uma leitura de recalque.** Uma leitura por nivelamento geométrico tem quatro fontes independentes: instrumento, $u_1 = 0{,}3\,\mathrm{mm}$; mira e posicionamento, $u_2 = 0{,}4\,\mathrm{mm}$; estabilidade da referência de nível, $u_3 = 0{,}5\,\mathrm{mm}$; efeitos térmicos, $u_4 = 0{,}2\,\mathrm{mm}$.

$
u_c = \sqrt{0{,}3^2 + 0{,}4^2 + 0{,}5^2 + 0{,}2^2} = \sqrt{0{,}54} \approx 0{,}73\,\mathrm{mm}
\qquad
U = 2 \times 0{,}73 \approx 1{,}5\,\mathrm{mm}
$

O recalque de $9{,}0 \pm 1{,}5\,\mathrm{mm}$ pode estar entre 7,5 e 10,5 mm: o intervalo **inclui** o nível de alerta de 10 mm. A decisão tecnicamente defensável é tratar a situação como **atenção** — aumentar a frequência de leitura e preparar a resposta —, e não ignorar o valor por ele estar "abaixo" de 10.

### Atividade prática

Pegue a ficha técnica (*datasheet*) de um sensor real usado em obras — um inclinômetro MEMS, um piezômetro de corda vibrante ou um sismógrafo de vibração. Identifique e anote: faixa, resolução, exatidão (ou incerteza), sensibilidade, deriva térmica e taxa de amostragem máxima. Em seguida, responda: esse sensor serve para detectar uma variação de 2 mm (ou 2 kPa, ou 1 mm/s) com segurança? Justifique usando os conceitos da aula.

### Pontos-chave

- **Sensor** responde à grandeza; **transdutor** a converte em sinal mensurável; o **datalogger** registra e transmite.
- **Resolução não é exatidão**; **precisão** é repetibilidade, **veracidade** é ausência de viés e **exatidão** exige as duas.
- A qualidade de uma medição é expressa pela **incerteza**; fontes independentes combinam-se pela **raiz da soma dos quadrados** ($U = k\,u_c$, com $k = 2$).
- A taxa de amostragem deve satisfazer **Nyquist** ($f_s > 2\,f_{max}$) e acompanhar a velocidade do fenômeno.
- Calibração só vale se for **rastreável** aos padrões nacionais (Inmetro/RBC).

### Para saber mais

- **Inmetro — Vocabulário Internacional de Metrologia (VIM 2012), edição luso-brasileira:** http://www.inmetro.gov.br/inovacao/publicacoes/vim_2012.pdf
- **JCGM/BIPM — GUM: *Evaluation of measurement data — Guide to the expression of uncertainty in measurement*:** https://doi.org/10.59161/JCGM100-2008E
- **Wikipedia — Teorema da amostragem de Nyquist–Shannon:** https://pt.wikipedia.org/wiki/Teorema_da_amostragem_de_Nyquist%E2%80%93Shannon
- **Wikipedia — Extensômetro:** https://pt.wikipedia.org/wiki/Extens%C3%B4metro

## Aula 2 — Roteiro da Videoaula 2: "Fundamentos de sensoriamento: grandezas, transdutores, incerteza e calibração"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e o recalque de 9 mm com alerta em 10 mm.

> "O sistema avisa: o recalque do pilar do vizinho chegou a 9 milímetros, e o alerta é 10. Você relaxa ou mobiliza a equipe? Depende de uma pergunta que quase ninguém faz: qual é a incerteza desses 9 milímetros? Hoje a gente vai aprender a falar a língua da metrologia — porque sem ela nenhum dado de sensor merece confiança."

### 2. Desenvolvimento — parte 1 (0:25 – 1:20)

**[TELA]** Slides 4–9 — grandezas, escavação instrumentada em 3D, galeria de sensores, ponte de Wheatstone, escala e características estáticas.

> "Tudo começa pela grandeza: deslocamento, recalque, poropressão, deformação, temperatura, aceleração. E pelo mensurando, que é exatamente o que eu quero medir, onde e em relação a quê. O sensor responde à grandeza; o transdutor transforma isso num sinal elétrico. O exemplo clássico é o extensômetro: uma grade metálica colada na peça que muda de resistência quando a peça deforma. Na obra, você vai ver muito sensor de corda vibrante, MEMS e saída de 4 a 20 miliampères, tudo lido por um datalogger. E aí entram as características: faixa, resolução, sensibilidade — saída sobre entrada, como 0,08 miliampère por quilopascal —, deriva e histerese. E guarde isso: resolução não é exatidão. O display mostrar três casas decimais não quer dizer que o sensor acerta três casas decimais."

### 3. Desenvolvimento — parte 2 (1:20 – 2:15)

**[TELA]** Slides 10–13 — o alvo (precisão, veracidade e exatidão), Nyquist a 50 Hz, calibração e rastreabilidade.

> "Precisão é repetir o mesmo valor; veracidade é não ter viés, a média perto do valor verdadeiro; e exatidão, cada leitura perto do verdadeiro, exige as duas. Lembra do alvo: tiros agrupados longe do centro são precisos, mas com viés — e isso a calibração corrige. Como a gente nunca conhece o valor verdadeiro, expressa a qualidade da medição pela incerteza, e combina fontes independentes pela raiz da soma dos quadrados, como manda o GUM. Outra regra de ouro é Nyquist: amostrar a mais que o dobro da maior frequência do fenômeno. Vibração de 50 hertz? Mais de 100 amostras por segundo, de preferência 250 a 500; em 60, aparece aliasing. E calibração tem que ser rastreável: uma cadeia de padrões que chega ao Inmetro, através dos laboratórios da Rede Brasileira de Calibração."

### 4. Desenvolvimento — parte 3 (2:15 – 2:55)

**[TELA]** Slides 14–17 — reta de calibração, incerteza combinada, da incerteza à decisão e a atividade.

> "Duas contas rápidas. Um piezômetro de 4 a 20 miliampères calibrado de zero a 200 quilopascals: o fator de escala dá 12,5 quilopascals por miliampère. Leu 9,6 miliampères? São 70 quilopascals, ou uns 7,14 metros de coluna d'água. Agora o recalque: quatro fontes de incerteza, de 0,3, 0,4, 0,5 e 0,2 milímetro. A combinada dá uns 0,73; a expandida, com k igual a 2, quase 1,5 milímetro. Então aqueles 9 milímetros podem ser 10,5. O alerta pode já ter sido atingido! A decisão certa é entrar em atenção e aumentar a frequência de leitura."

### 5. Encerramento (2:55 – 3:25)

**[TELA]** Slides 18–19 — pontos-chave e encerramento.

> "Agora você sabe avaliar se uma leitura merece confiança. Mas como essa leitura sai do sensor enterrado no solo e chega à tela do engenheiro — e, mais do que isso, como ela dispara uma ação na obra? Na próxima aula, a gente monta a arquitetura IoT do canteiro e fecha a malha de verdade. Te espero na Aula 3!"

---

## Aula 3 — Arquiteturas IoT para o canteiro: dispositivos, conectividade e nuvem

> Uma escavação de 9 metros para um subsolo, ao lado de uma rua movimentada. Às 2h da madrugada, depois de uma chuva forte, o nível d'água atrás da cortina de estacas começa a subir. Ninguém está na obra. Em um sistema de malha aberta, o problema seria descoberto às 7h — talvez tarde demais. Em um sistema IoT bem projetado, o piezômetro detecta a subida, o dado atravessa a cidade em segundos, a plataforma compara com o nível de alerta, a bomba de rebaixamento é acionada e o engenheiro de plantão recebe uma mensagem. Nesta aula, você vai entender **as camadas** que tornam isso possível, **as tecnologias de rede** que levam o dado e como desenhar uma **malha fechada** de monitoramento.

### O que é IoT no canteiro

**Internet das Coisas (IoT)** é a conexão de objetos físicos — sensores, máquinas, equipamentos — a redes de dados, de modo que eles enviem informações e recebam comandos sem intervenção humana a cada leitura. No canteiro, as "coisas" são piezômetros, inclinômetros, marcos de recalque automatizados, sensores de vibração, estações meteorológicas e até gruas e caminhões rastreados.

### As quatro camadas de uma arquitetura IoT

Uma forma didática de organizar o sistema é em camadas:

1. **Percepção** — sensores e **datalogger/nó sensor**: medem, digitalizam e guardam a leitura. Funcionam a bateria, às vezes com painel solar.
2. **Rede** — o **gateway** recebe os dados dos nós por rádio e os encaminha para a internet (via 4G/5G, fibra ou satélite).
3. **Plataforma** — servidores na nuvem armazenam as séries temporais, aplicam regras, comparam com limites e geram alertas. É aqui que vive o **gêmeo digital** (ou a sombra digital) da obra: a representação atualizada do estado do canteiro que recebe os dados.
4. **Aplicação** — painéis (*dashboards*), relatórios, alertas por SMS/e-mail e integração com BIM e cronograma.

![Nó sensor LoRaWAN com sonda de umidade do solo e, ao lado, um gateway LoRaWAN montado sobre um computador de placa única, com antenas, dispostos sobre uma mesa](https://upload.wikimedia.org/wikipedia/commons/0/0c/Representative_LoRaWAN_Deployment_with_Gateway_%2B_End_Device.png)

### Conectividade: LoRaWAN, NB-IoT, 4G/5G e Wi-Fi

Não existe rede "melhor" — existe a adequada ao **alcance**, à **taxa de dados** e ao **consumo de energia** exigidos:

| Tecnologia | Alcance típico | Taxa de dados | Consumo | Uso típico no canteiro |
| --- | --- | --- | --- | --- |
| **LoRaWAN** | de 2–5 km (urbano) a mais de 10 km (aberto) | muito baixa (centenas de bit/s a dezenas de kbit/s) | muito baixo (anos de bateria) | piezômetros, inclinômetros, fissurômetros com leituras periódicas |
| **NB-IoT / LTE-M** | cobertura da operadora celular | baixa | baixo | nós isolados onde há cobertura celular, sem gateway próprio |
| **4G/5G** | cobertura da operadora | alta | alto | câmeras, gateways, envio de imagens e vídeos |
| **Wi-Fi** | dezenas a centenas de metros (ao ar livre, com antena externa) | alta | alto | escritório de obra, áreas cobertas, equipamentos com energia |

Como regra: **sensor de leitura lenta e a bateria → LoRaWAN ou NB-IoT; muito dado e energia disponível → 4G/5G ou Wi-Fi**. O **LoRaWAN** opera em faixas de radiofrequência não licenciadas; no Brasil, os equipamentos de radiocomunicação precisam de **homologação da Anatel**.

### Borda (*edge*) × nuvem (*cloud*) e o protocolo MQTT

Processar **na borda** é decidir no próprio datalogger ou gateway, sem depender da internet — útil para respostas rápidas (ligar uma bomba) e se o 4G cair. Processar **na nuvem** permite cruzar muitos sensores, guardar o histórico e rodar modelos pesados. Sistemas robustos fazem os dois: regra crítica na borda; análise e registro na nuvem.

Para levar as mensagens até a plataforma, um protocolo muito usado é o **MQTT**, leve e baseado em **publicação/assinatura**. Numa rede LoRaWAN, o gateway apenas encaminha os pacotes de rádio ao **servidor de rede** (*network server*), que os decodifica e os publica em um **tópico** (por exemplo, `obra/escavacao/PZ-03/nivel`) num servidor chamado **broker**; qualquer aplicação interessada **assina** o tópico e recebe as leituras. O mesmo mecanismo permite enviar comandos no sentido contrário — o que fecha a malha.

### A malha fechada com monitoramento IoT

Voltando à escavação do gancho, a malha fechada fica assim:

1. **Medir** — o piezômetro PZ-03, atrás da cortina, lê o nível d'água a cada 15 minutos.
2. **Transmitir** — o nó envia a leitura por LoRaWAN ao gateway, que a encaminha ao servidor de rede; este a publica via MQTT na plataforma.
3. **Comparar** — a plataforma (o gêmeo digital da escavação) compara o nível com os **limites de projeto**: nível de **atenção** (ex.: 2,0 m abaixo do fundo da escavação) e de **alerta** (1,0 m).
4. **Decidir e agir** — ao cruzar a atenção, aumenta a frequência de leitura e avisa o engenheiro; ao cruzar o alerta, **aciona a bomba do rebaixamento** e recomenda **paralisar a frente** de escavação próxima.
5. **Medir de novo** — as leituras seguintes confirmam (ou não) que o nível voltou a cair. Se não cair, o laço escala a decisão para a equipe de geotecnia.

Note que o laço **não termina na tela**: ele termina numa ação no canteiro e numa nova leitura que verifica a ação.

### Exemplo numérico

Um nó sensor de piezômetro funciona a bateria de lítio de 19.000 mAh, da qual se considera utilizável 80% (efeitos de temperatura e autodescarga). A cada ciclo de 15 min (900 s), ele: lê o sensor por 2 s a 25 mA; transmite por 1 s a 120 mA; e dorme o restante (897 s) a 0,02 mA.

$
Q_{ciclo} = 2 \times 25 + 1 \times 120 + 897 \times 0{,}02 \approx 187{,}9\,\mathrm{mA \cdot s}
$

$
\bar{I} = \frac{Q_{ciclo}}{T_{ciclo}} = \frac{187{,}9}{900} \approx 0{,}2088\,\mathrm{mA}
$

$
t = \frac{0{,}8 \times 19.000}{0{,}2088} \approx 72.800\,\mathrm{h} \approx 3.033\,\mathrm{dias} \approx 8{,}3\,\mathrm{anos}
$

Se, em modo de alerta, o ciclo cair para 60 s (2 s de leitura, 1 s de transmissão, 57 s de sono):

$
\bar{I} = \frac{50 + 120 + 57 \times 0{,}02}{60} \approx 2{,}85\,\mathrm{mA}
\qquad
t = \frac{15.200}{2{,}85} \approx 5.330\,\mathrm{h} \approx 222\,\mathrm{dias}
$

Moral: a **taxa de leitura governa a autonomia**. Por isso, bons sistemas usam **amostragem adaptativa** — leem devagar em condição normal e aceleram só quando a malha entra em atenção.

### Pausa para reflexão (Desafio)

No exemplo da escavação, a plataforma pode ligar a bomba **sozinha**. Mas deveria também **paralisar a escavação sozinha**, travando as máquinas? Pense nos dois lados: a resposta automática é rápida e funciona às 2h da madrugada; mas um sensor com defeito ou uma leitura espúria pode parar uma obra inteira sem motivo — ou, pior, uma ação automática pode criar um risco novo. **Quando a malha deve ser automática e quando deve exigir decisão humana?** Considere: a consequência de agir errado, a consequência de não agir a tempo, a confiabilidade do sensor (há redundância?) e a reversibilidade da ação. Uma regra prática que você pode testar: ações **reversíveis, de baixo risco e urgentes** podem ser automáticas; ações **de alto impacto ou difíceis de reverter** pedem um humano no laço.

### Atividade prática

Desenhe, em uma folha, a arquitetura IoT de monitoramento para um dos casos: (a) recalque de um edifício vizinho a uma escavação; (b) vibração causada por cravação de estacas próxima a um casarão histórico. Indique as quatro camadas, a tecnologia de rede escolhida (justifique por alcance, taxa e consumo), onde roda cada regra (borda ou nuvem) e a malha fechada completa, com níveis de atenção e alerta e a ação associada a cada um.

### Pontos-chave

- Arquitetura IoT em quatro camadas: **percepção** (sensor + datalogger), **rede** (gateway), **plataforma** (nuvem, onde vive o gêmeo digital) e **aplicação** (dashboards e alertas).
- A rede se escolhe por **alcance, taxa de dados e consumo**: LoRaWAN e NB-IoT para leituras lentas a bateria; 4G/5G e Wi-Fi para grandes volumes de dados.
- **Borda** para respostas rápidas e independentes da internet; **nuvem** para histórico, cruzamento de dados e análise.
- A **malha fechada IoT** vai do sensor à ação no canteiro e volta ao sensor para verificar o efeito.
- A **taxa de amostragem** determina a autonomia da bateria; a amostragem adaptativa equilibra vigilância e consumo.

### Para saber mais

- **LoRa Alliance — *What is LoRaWAN*:** https://lora-alliance.org/about-lorawan/
- **MQTT.org — documentação do protocolo MQTT:** https://mqtt.org/
- **Wikipedia — Internet das coisas:** https://pt.wikipedia.org/wiki/Internet_das_coisas
- **Anatel — Certificação e homologação de produtos:** https://www.gov.br/anatel/pt-br/regulado/certificacao-de-produtos

## Aula 3 — Roteiro da Videoaula 3: "Arquiteturas IoT para o canteiro: dispositivos, conectividade e nuvem"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e a escavação às duas da manhã.

> "Duas da manhã, depois de uma chuva forte. Atrás da cortina de estacas de uma escavação de 9 metros, o nível d'água começa a subir. Não tem ninguém na obra. Num sistema de malha aberta, alguém descobre às sete. Num sistema IoT bem feito, a bomba já ligou e o engenheiro de plantão já foi avisado. Hoje a gente vai montar esse sistema, camada por camada."

### 2. Desenvolvimento — parte 1 (0:30 – 1:25)

**[TELA]** Slides 4–9 — IoT no canteiro, as quatro camadas, as camadas em 3D, a tabela de redes, a simulação de alcance e o gateway.

> "IoT é conectar coisas físicas a redes de dados. No canteiro, as coisas são piezômetros, inclinômetros, sensores de vibração, até a grua. E a arquitetura tem quatro camadas. Percepção: o sensor e o datalogger, a bateria. Rede: o gateway, que recebe o rádio dos sensores e encaminha pela internet ao servidor de rede. Plataforma: a nuvem, que guarda, compara com os limites e alerta — e é aqui que mora o gêmeo digital da obra. E aplicação: os dashboards e as mensagens que chegam para você. Para a rede, a escolha depende de alcance, taxa e consumo. LoRaWAN vai longe, gasta pouquíssimo e transmite pouco: perfeito para piezômetro. 4G e 5G transmitem muito, mas gastam muito: bons para câmera. E lembre: equipamento de rádio no Brasil precisa de homologação da Anatel."

### 3. Desenvolvimento — parte 2 (1:25 – 2:25)

**[TELA]** Slides 10–13 — borda × nuvem, MQTT, os cinco passos da malha e a simulação do nível d'água com a bomba.

> "Onde a decisão roda? Na borda, no próprio gateway, ela é rápida e funciona mesmo se a internet cair. Na nuvem, dá para cruzar tudo e guardar o histórico. O ideal é usar os dois. E quem entrega a mensagem à plataforma costuma ser o MQTT: o servidor de rede publica a leitura num tópico, a plataforma assina. Agora, a malha fechada completa: o piezômetro mede a cada 15 minutos, o dado vai por LoRaWAN até o gateway e por MQTT até a plataforma, o gêmeo digital compara com os níveis de atenção e de alerta, passou do alerta, liga a bomba e recomenda parar a frente de escavação. E aí vem a parte que muita gente esquece: medir de novo para ver se o nível baixou. Se não baixou, a decisão sobe para a geotecnia."

### 4. Desenvolvimento — parte 3 (2:25 – 3:10)

**[TELA]** Slides 14–16 — autonomia da bateria, a pausa para reflexão e a atividade.

> "E a bateria aguenta? Vamos à conta. Leitura de 2 segundos a 25 miliampères, transmissão de 1 segundo a 120, e o resto do ciclo de 15 minutos dormindo a 0,02. A corrente média dá uns 0,21 miliampère. Com uma bateria de 19 mil miliampères-hora, usando 80%, são mais de 8 anos. Agora, se eu passo a ler a cada minuto, a autonomia cai para uns 222 dias. Por isso o sistema bom lê devagar no normal e acelera só no alerta. E fica a reflexão: a plataforma pode ligar a bomba sozinha. Mas deveria parar a obra sozinha? Pense em consequência, confiabilidade do sensor e se a ação é reversível."

### 5. Encerramento (3:10 – 3:35)

**[TELA]** Slides 17–18 — pontos-chave e encerramento.

> "Você montou hoje uma arquitetura IoT completa e fechou a malha do sensor até a ação no canteiro. Falta o outro protagonista da disciplina: o drone. Que tipos existem, do que ele é feito, que câmeras e sensores ele carrega e, principalmente, o que a lei brasileira exige para voar numa obra. É a próxima aula. Te espero na Aula 4!"

---

## Aula 4 — Drones (RPA): tipos, componentes, cargas úteis e regulamentação brasileira

> A construtora comprou um drone e quer voar o canteiro toda semana. Qual drone, com qual sensor — e, antes de tudo, **pode voar?** Esta aula, que fecha os fundamentos, trata de tipos, componentes e cargas úteis dos drones e do arcabouço regulatório brasileiro.

### Termos e tipos de drone: multirrotor, asa fixa e VTOL

"Drone" é o nome popular. A regulamentação fala em **aeronave não tripulada (UA)** e em **sistema de aeronave não tripulada (UAS)** — a aeronave mais a estação de pilotagem remota e o enlace de comando. A literatura técnica usa também **RPA** (*remotely piloted aircraft*). Há três famílias:

- **Multirrotor** (quadri, hexa ou octocóptero) — decola na vertical, paira e manobra com precisão. Ideal para **inspeção de fachadas e estruturas** e áreas pequenas; autonomia típica de 20 a 45 minutos.
- **Asa fixa** — voa como um avião; cobre **centenas de hectares** por voo e é o preferido em rodovias, ferrovias e grandes terraplenagens. Precisa de área de pouso e não paira.
- **VTOL** (*vertical take-off and landing*) — decola e pousa na vertical e voa em cruzeiro como asa fixa.

![Drone VTOL de asa fixa laranja, do tipo tail-sitter, pousado na vertical sobre gramado de montanha antes de um voo de mapeamento](https://upload.wikimedia.org/wikipedia/commons/0/0b/WingtraOne_in_use.jpg)

### Componentes de um drone

- **Estrutura (frame)** — em fibra de carbono ou compósitos, leve e rígida.
- **Motores e ESC** — motores elétricos *brushless* acionados por controladores eletrônicos de velocidade (*ESC*).
- **Controladora de voo** — o "cérebro": estabiliza a aeronave e executa missões automáticas.
- **GNSS e RTK** — o receptor de navegação por satélite posiciona o drone; com **RTK** (correção em tempo real), a posição das fotos chega ao nível de centímetros, reduzindo a necessidade de pontos de controle.
- **IMU** — unidade inercial com acelerômetros e giroscópios, que mede atitude e aceleração.
- **Bateria LiPo** (polímero de lítio) — alta densidade de energia, mas exige cuidado com carga, temperatura e armazenamento.
- **Gimbal** — suporte estabilizado que mantém a câmera firme e apontada.
- **Rádio (enlace de comando e de vídeo)** — liga a aeronave à estação de pilotagem remota.

### Cargas úteis (payloads)

- **Câmera RGB** — a mais usada: fotogrametria (ortomosaico, modelo 3D, volumes) e avanço físico.
- **Multiespectral** — bandas além do visível; útil em recuperação vegetal e meio ambiente.
- **Térmica** — diferenças de temperatura: perdas de calor em fachadas, infiltrações, descolamento de revestimentos, painéis elétricos aquecidos.
- **LiDAR** — laser que gera nuvem de pontos e alcança o terreno sob vegetação, onde a fotogrametria falha.

![Drone multirrotor quadricóptero de uso profissional exposto em feira, com braços em fibra de carbono, trem de pouso e gimbal com câmeras de zoom e térmica sob a fuselagem](https://upload.wikimedia.org/wikipedia/commons/5/5c/DJI_M300_Matrice_300_RTK_%28FA39TN4A93%29_%284-12-2024%29.jpg)

### Regulamentação brasileira: ANAC

Por quase uma década, a referência foi o **RBAC-E nº 94** da ANAC (2017), que classificava as aeronaves pelo **peso máximo de decolagem**: **Classe 1** (acima de 150 kg), **Classe 2** (acima de 25 kg até 150 kg) e **Classe 3** (até 25 kg). Essas classes ainda aparecem em contratos e editais.

Em **junho de 2026**, a ANAC aprovou o **RBAC nº 100** (Resolução nº 805, de 15/06/2026), que **substituiu o RBAC-E nº 94** e passou a classificar as **operações pelo risco**, e não mais pelo peso:

- **Categoria aberta** — peso em voo até 25 kg, em linha de visada visual (VLOS) ou estendida, com apoio de observador (EVLOS), até 120 m (400 pés) acima do solo, em **áreas distantes de terceiros**: em nenhuma hipótese a menos de **30 m horizontais de pessoas não envolvidas e não anuentes**, salvo barreira mecânica capaz de protegê-las. Exige avaliação de risco operacional atualizada (facultativa se a operação estiver a mais de 150 m dessas pessoas ou protegida por barreira).
- **Categoria específica** — quando algum critério da aberta não é atendido (voo além da linha de visada, acima de 120 m, acima de 25 kg etc.); o operador demonstra a segurança por avaliação de risco operacional, por método aceito pela ANAC (como o **SORA**, da JARUS, previsto no art. 4º da Resolução nº 805), ou por cenário padrão definido pela ANAC; conforme a complexidade da operação, o operador obtém o **Cadastro de Operador na categoria específica (COE)** (RBAC nº 100, Subparte F).
- **Categoria certificada** — operações de alto risco, como transporte de artigos perigosos, com certificação da aeronave, do operador e do piloto.

Outros requisitos do RBAC nº 100: aeronaves das categorias aberta e específica são **cadastradas no SISANT** (cadastro válido por 24 meses e identificação na aeronave); o piloto remoto deve ser aprovado em **exame de conhecimento teórico da ANAC** (exigível a partir de 2027); e as operações devem ter **seguro com cobertura de danos a terceiros** (o seguro conhecido no setor como RETA), com poucas exceções. Drones de **até 250 g**, operando **até 120 m (400 pés) acima do solo e em VLOS ou EVLOS**, ficam **fora** do RBAC nº 100 (§ 100.1(e)), sob as regras simplificadas da Resolução nº 806/2026, mas continuam sujeitos às regras do DECEA: a ICA 100-40 também se aplica a eles, e o acesso ao espaço aéreo é solicitado pelo SARPAS. Atos emitidos sob o RBAC-E nº 94 seguem válidos até serem revistos pela ANAC, e as operações autorizadas até 15/06/2026 que não se enquadram na categoria aberta têm **2 anos** para obter nova autorização operacional (Resolução nº 805, art. 2º).

### DECEA, Anatel e o voo na prática

O **espaço aéreo** é do **DECEA**, cuja **ICA 100-40** (Portaria DECEA nº 2.094/DNOR8, de 2026) determina que o acesso seja solicitado pelo sistema **SARPAS**, com antecedência que cresce com o risco. Os rádios do drone precisam de **homologação da Anatel**.

Há ainda um ponto que pega muita obra de surpresa: o **aerolevantamento**. Mapear um terreno em **faixas de voo sobrepostas** para gerar ortomosaico, MDT ou planta planialtimétrica é aerolevantamento (Decreto nº 2.278/1997; Portaria GM-MD nº 3.703/2021, art. 8º), executado só por entidade **inscrita no Ministério da Defesa**. Projetos pequenos ficam **pré-autorizados**, com dispensa da autorização específica do Ministério da Defesa, quando a área não ultrapassa um círculo de raio de 2,2 km ou uma área circular inferior a 15 km², **desde que atendidas condições cumulativas** (entre elas, não tocar áreas ou instalações sujeitas a restrição e não ser levantamento geofísico) (Portaria GM-MD nº 3.703/2021, art. 38). A pré-autorização não dispensa a inscrição nem o pedido no SARPAS, com **4 dias corridos** de antecedência (ICA 100-40, art. 57). Foto de inspeção, sem faixas sobrepostas, não é aerolevantamento.

Resumo para a obra: **aeronave cadastrada + piloto aprovado + seguro + autorização no SARPAS + equipamento homologado + avaliação de risco** e, se for mapeamento, **aerolevantamento por empresa inscrita**. E não esqueça a **LGPD**: imagens de trabalhadores e vizinhos são dados pessoais.

### Exemplo numérico

Quanto um drone cobre por voo? A área mapeada é aproximadamente:

$
A_{voo} = v \cdot t_{útil} \cdot d
$

onde $v$ é a velocidade de cruzeiro, $t_{útil}$ o tempo útil de mapeamento e $d$ o espaçamento entre faixas de voo. Com uma faixa imageada no solo de 100 m e sobreposição lateral de 70%, $d = 100 \times (1 - 0{,}7) = 30\,\mathrm{m}$ (o cálculo da faixa você verá na Unidade 2).

**Multirrotor:** autonomia de 30 min, dos quais 70% são úteis (reserva de bateria, decolagem, pouso e curvas): $t_{útil} = 0{,}7 \times 30 = 21\,\mathrm{min} = 1.260\,\mathrm{s}$; $v = 6\,\mathrm{m/s}$.

$
A_{multi} = 6 \times 1.260 \times 30 = 226.800\,\mathrm{m^2} \approx 22{,}7\,\mathrm{ha}
$

**VTOL de asa fixa:** autonomia de 59 min, $t_{útil} = 0{,}7 \times 59 \approx 41{,}3\,\mathrm{min} \approx 2.478\,\mathrm{s}$; $v = 16\,\mathrm{m/s}$.

$
A_{VTOL} = 16 \times 2.478 \times 30 \approx 1.189.000\,\mathrm{m^2} \approx 119\,\mathrm{ha}
$

O canteiro de 12 ha da Aula 1 cabe num voo do multirrotor; 20 km de rodovia com 60 m de faixa de domínio (120 ha) pede o VTOL: $120/119 \approx 1{,}01 \rightarrow$ **2 voos** (arredonda-se sempre para cima), contra 6 do multirrotor. E, longe da decolagem, o VTOL sai da linha de visada: voo **BVLOS** (além da linha de visada visual) é **categoria específica** (pedido no SARPAS 8 dias antes), ou o trecho é dividido em blocos voados em linha de visada. Ou seja: **o tipo de drone segue a geometria da obra**, e a geometria também define a categoria.

### Atividade prática

Escolha uma obra e monte um **checklist de conformidade** para voar sobre ela (categoria no RBAC nº 100, cadastro, piloto, seguro, SARPAS, aerolevantamento, Anatel, distância de terceiros, LGPD). Depois indique o tipo de drone e a carga útil mais adequados, justificando pela geometria e pelo objetivo do levantamento.

### Pontos-chave

- **Multirrotor** paira e inspeciona; **asa fixa** cobre grandes áreas; **VTOL** une decolagem vertical e eficiência de cruzeiro.
- Componentes essenciais: frame, motores/ESC, controladora, **GNSS/RTK**, IMU, bateria LiPo, gimbal e rádio; cargas úteis: **RGB, multiespectral, térmica e LiDAR**.
- O **RBAC nº 100** (2026) substituiu o RBAC-E nº 94 e classifica operações por **risco** (aberta, específica, certificada), não mais por classes de peso.
- Para voar na obra: **SISANT, exame teórico da ANAC, seguro, SARPAS (DECEA, ICA 100-40) e homologação Anatel** — e respeito à LGPD. Mapeamento em faixas sobrepostas é **aerolevantamento** (empresa inscrita no Ministério da Defesa).
- A área por voo é $A = v \cdot t_{útil} \cdot d$: o tipo de drone segue a geometria da obra.

### Para saber mais

- **ANAC — Drones (portal oficial):** https://www.gov.br/anac/pt-br/assuntos/drones
- **ANAC — RBAC nº 100, Emenda 00 (texto integral):** https://pergamum.anac.gov.br/pergamum/vinculos/RBAC100EMD00.pdf
- **DECEA — ICA 100-40 (2026): Aeronaves Não Tripuladas e o Acesso ao Espaço Aéreo Brasileiro (texto oficial; cópia no portal de Aerolevantamento do Ministério da Defesa):** https://www.gov.br/defesa/pt-br/assuntos/aerolevantamento/arquivos/2026/ica-100-40-publicada-port-2094-dnor8-18-03-2026-bca-058-30-03-2026.pdf
- **Wikipedia — Veículo aéreo não tripulado:** https://pt.wikipedia.org/wiki/Ve%C3%ADculo_a%C3%A9reo_n%C3%A3o_tripulado

### O que você verá na próxima unidade

Na **Unidade 2 — Drones: Aquisição e Processamento de Dados**, o drone vai para o ar. Você vai **planejar o voo** (GSD, altura, sobreposição, plano de missão), entender como a **fotogrametria** transforma centenas de fotos em um modelo 3D (*Structure from Motion*, pontos de controle, RTK/PPK), gerar os **produtos cartográficos** — ortomosaico, MDS/MDT, nuvem de pontos e **cálculo de volumes** — e conhecer o **LiDAR embarcado** e a **termografia** na inspeção de estruturas e fachadas. Malha fechada, incerteza e regulamentação vão se aplicar a cada voo.

## Aula 4 — Roteiro da Videoaula 4: "Drones (RPA): tipos, componentes, cargas úteis e regulamentação brasileira"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 17 a 19 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e "pode voar?".

> "A construtora comprou um drone e quer voar o canteiro amanhã. Tira da caixa, carrega a bateria e decola, certo? Errado. Qual drone serve para mapear e qual serve para inspecionar fachada? Que sensor ele carrega? E, antes de tudo: pode voar? Hoje, fechando os fundamentos, você vai conhecer os drones por dentro e as regras do jogo no Brasil."

### 2. Desenvolvimento — parte 1 (0:25 – 1:15)

**[TELA]** Slides 4–8 — as três famílias, o VTOL, o drone em 3D, os componentes reais e as cargas úteis.

> "Drone é o nome popular; a norma fala em aeronave não tripulada e sistema de aeronave não tripulada, e a literatura usa muito RPA. Existem três famílias. O multirrotor paira e manobra, perfeito para fachada e obra urbana, mas voa 20 a 45 minutos. A asa fixa voa como avião e cobre centenas de hectares, ótima para rodovia. E o VTOL decola na vertical e cruza como asa fixa. Por dentro: frame, motores com ESC, controladora de voo, GNSS — com RTK chega a centímetros —, IMU, bateria LiPo, gimbal e rádio. E as cargas úteis: câmera RGB para fotogrametria, multiespectral, térmica para infiltração e descolamento de revestimento, e LiDAR, que chega ao terreno mesmo com vegetação."

### 3. Desenvolvimento — parte 2 (1:15 – 2:40)

**[TELA]** Slides 9–14 — do RBAC-E nº 94 ao RBAC nº 100, as três categorias, a escala em 3D, os números, o DECEA e o checklist.

> "Agora a regulamentação. Durante anos valeu o RBAC-E 94 da ANAC, com classes por peso: Classe 1 acima de 150 quilos, Classe 2 de 25 a 150, Classe 3 até 25. Em junho de 2026, a ANAC aprovou o RBAC 100, que substituiu o 94 e passou a olhar o risco da operação. Na categoria aberta: até 25 quilos, linha de visada, até 120 metros de altura e nunca a menos de 30 metros de pessoas não envolvidas e não anuentes, a não ser que haja uma barreira. Saiu disso, é categoria específica, com avaliação de risco, como o método SORA. Risco alto, categoria certificada. E mais: cadastro no SISANT, prova teórica da ANAC — exigível a partir de 2027 —, seguro contra danos a terceiros. Do lado do DECEA, a ICA 100-40 manda pedir o acesso ao espaço aéreo pelo SARPAS, inclusive para os drones de até 250 gramas, que só ficam fora do RBAC 100 se voarem até 120 metros e em linha de visada. Mapeamento em faixas sobrepostas é aerolevantamento: empresa inscrita no Ministério da Defesa. E o rádio do drone precisa de homologação da Anatel. Sem esquecer a LGPD: imagem de pessoa é dado pessoal."

### 4. Desenvolvimento — parte 3 (2:40 – 3:25)

**[TELA]** Slides 15–17 — área por voo, o canteiro voado em faixas e a atividade com os pontos-chave.

> "Quanto um drone cobre por voo? Velocidade vezes tempo útil vezes espaçamento entre faixas. Um multirrotor a 6 metros por segundo, com 21 minutos úteis e faixas a cada 30 metros, cobre uns 22,7 hectares. Um VTOL a 16 metros por segundo, com uns 41 minutos úteis, cobre perto de 119 hectares. O canteiro de 12 hectares da Aula 1 vai num voo só do multirrotor; vinte quilômetros de rodovia, 120 hectares, pedem 2 voos do VTOL — e, além da linha de visada, o voo BVLOS, categoria específica. O tipo de drone segue a geometria da obra."

### 5. Encerramento (3:25 – 3:45)

**[TELA]** Slides 18–20 — fechamento da unidade, prévia da Unidade 2 e encerramento.

> "Com esta aula, você fechou os fundamentos: por que monitorar, como medir com confiança, como o dado viaja numa arquitetura IoT e o que é preciso para voar legalmente. Na Unidade 2, o drone vai para o ar de verdade: planejamento de voo, fotogrametria, ortomosaico, volumes, LiDAR e termografia. Foi um prazer! Te espero lá."

---

## Quiz não avaliativo

### Questão 1

Uma construtora instalou piezômetros automatizados em uma escavação. As leituras chegam a cada 15 minutos a uma plataforma na nuvem, que exibe gráficos atualizados, mas não há níveis de alerta definidos e os relatórios são lidos apenas na reunião semanal. Com base nos conceitos de **malha fechada** e **gêmeo digital**, assinale a alternativa **correta**:

- [ ] a. O sistema é um gêmeo digital completo, porque os dados dos piezômetros fluem automaticamente do canteiro para a plataforma na nuvem.
- [x] b. O sistema opera em malha aberta: é uma sombra digital, pois falta comparar as leituras com limites e devolver uma ação ao canteiro a tempo.
- [ ] c. O sistema está em malha fechada, porque a frequência de leitura de 15 minutos acompanha os fenômenos geotécnicos da escavação.
- [ ] d. Para virar um gêmeo digital, bastaria trocar os piezômetros por sensores de maior resolução e menor incerteza.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) está correta: os dados fluem automaticamente do físico para o digital, o que caracteriza uma **sombra digital** (Kritzinger *et al.*, 2018), mas, sem níveis de alerta e sem resposta a tempo, a leitura é apenas arquivada — o laço medir → comparar → decidir → agir → medir de novo não se fecha. A (a) erra porque o gêmeo digital exige fluxo automático **nos dois sentidos**, o que não existe aqui. A (c) confunde frequência de leitura com malha fechada: ler a cada 15 minutos não adianta se ninguém compara a leitura com um limite nem age. A (d) é falsa: resolução do sensor não muda a natureza da integração entre físico e digital; o que falta são referências, decisão e ação.

### Questão 2

Um engenheiro planeja voar um multirrotor de 9 kg, em linha de visada, a 80 m de altura, sobre um canteiro urbano, mantendo isolada a área sob o voo. Considerando os fundamentos de sensoriamento e a regulamentação vigente, assinale a alternativa **correta**:

- [ ] a. Como o drone tem menos de 25 kg, a operação fica dispensada do cadastro da aeronave, do seguro contra danos a terceiros e do pedido de acesso ao espaço aéreo.
- [ ] b. A operação deve seguir as classes por peso do RBAC-E nº 94 (Classe 3, até 25 kg), que continua sendo a norma aplicável a todas as novas operações.
- [x] c. Pode caber na categoria aberta do RBAC nº 100, mantidos 30 m de pessoas não anuentes (ou barreira), com SISANT, piloto habilitado, seguro e pedido no SARPAS.
- [ ] d. Se a câmera do drone tiver alta resolução, a exatidão do levantamento estará garantida, e os pontos de controle no terreno passam a ser dispensáveis.

**Resposta correta:** `c`

**Feedback:** A alternativa (c) está correta: 9 kg, linha de visada e 80 m de altura atendem aos critérios da categoria aberta do **RBAC nº 100**, que exige áreas distantes de terceiros (nunca menos de 30 m de pessoas não envolvidas e não anuentes, salvo barreira), cadastro no SISANT, piloto habilitado (o exame teórico da ANAC é exigível a partir de 1º/01/2027), seguro e o acesso ao espaço aéreo via SARPAS (ICA 100-40). Se o voo for um mapeamento em faixas sobrepostas, entra ainda o aerolevantamento. A (a) é falsa: a exclusão do RBAC nº 100 vale para aeronaves de até **250 g** operando até 120 m e em VLOS/EVLOS, não até 25 kg, e mesmo essas continuam pedindo acesso ao espaço aéreo pelo SARPAS. A (b) erra: o RBAC-E nº 94 foi substituído pelo RBAC nº 100 em junho de 2026, que classifica as operações por risco. A (d) confunde **resolução** com **exatidão**: uma câmera de alta resolução não elimina erros sistemáticos de posicionamento, que se controlam com pontos de controle e/ou RTK.

---

## Atividade Verificadora (AAI — Atividade Avaliativa Individual)

**Pergunta:**

> Uma incorporadora vai construir um edifício residencial com **dois subsolos** (escavação de $7\,\mathrm{m}$) em um terreno de $2.400\,\mathrm{m^2}$ em área urbana. A contenção é uma cortina de estacas atirantada. De um lado há um **sobrado antigo com fundação rasa**, a 3 m da divisa; do outro, um **prédio de 8 pavimentos**. O lençol freático está a $4\,\mathrm{m}$ de profundidade e a obra prevê rebaixamento por poços. A construtora quer ainda medir mensalmente o avanço físico e os volumes escavados.
>
> Você foi contratado(a) para propor o **plano de monitoramento**. Estruture sua resposta em quatro partes:
>
> 1. **Grandezas e instrumentos** — o que medir, com quais sensores e onde instalá-los (no mínimo três grandezas), e onde o drone entra.
> 2. **Arquitetura e malha fechada** — descreva a arquitetura IoT (camadas e tecnologia de rede) e a malha fechada para **uma** das grandezas, com nível de atenção, nível de alerta e a ação associada a cada um. Indique o que seria automático e o que exigiria decisão humana.
> 3. **Cálculo** — a leitura de recalque de um pilar do sobrado é de $11{,}2\,\mathrm{mm}$, com incertezas-padrão independentes de $0{,}4\,\mathrm{mm}$ (instrumento), $0{,}6\,\mathrm{mm}$ (referência de nível) e $0{,}3\,\mathrm{mm}$ (efeitos térmicos). O nível de alerta é $12\,\mathrm{mm}$. Calcule a incerteza combinada e a expandida ($k = 2$) e conclua se o alerta pode ter sido atingido. Calcule também a autonomia de um nó sensor com bateria utilizável de $10.000\,\mathrm{mAh}$ e corrente média de $0{,}25\,\mathrm{mA}$.
> 4. **Drone e regulamentação** — indique o tipo de drone e a carga útil para o levantamento mensal e liste os requisitos regulatórios para voar nesse canteiro.

**Resposta esperada:**

> **Parte 1.** Espera-se: **recalques** no sobrado e no prédio vizinho (marcos de recalque lidos por nivelamento ou prismas lidos por estação total robótica); **deslocamento horizontal da contenção** (inclinômetros instalados junto à cortina, e/ou prismas no topo das estacas); **nível d'água/poropressão** (piezômetros atrás da cortina e nos poços de rebaixamento); desejável: **carga nos tirantes** (células de carga), **fissuras** no sobrado (fissurômetros) e **vibração** (sismógrafo de engenharia, em velocidade de vibração, durante a execução das estacas). O drone entra no **levantamento mensal** (ortomosaico e modelo 3D para avanço físico e volume escavado) e em **inspeções visuais** de fachadas e coberturas vizinhas — não substitui os instrumentos de precisão.
>
> **Parte 2.** Arquitetura em quatro camadas: sensores + datalogger (percepção), **LoRaWAN** ou NB-IoT até um gateway com 4G (rede), plataforma na nuvem com séries temporais, limites e alertas — a sombra/gêmeo digital da escavação (plataforma) — e dashboard/alertas por mensagem (aplicação). Exemplo de malha fechada para o nível d'água: piezômetro lê a cada 15 min; **atenção** (ex.: nível d'água a 2,0 m abaixo do fundo da escavação) → aumentar frequência de leitura e avisar o engenheiro; **alerta** (ex.: a 1,0 m abaixo do fundo) → acionar automaticamente a bomba reserva do rebaixamento e recomendar a paralisação da escavação na frente afetada; nova leitura confirma a eficácia. Automático: ações **reversíveis, urgentes e de baixo risco** (ligar bomba, aumentar frequência, notificar). Decisão humana: ações de **alto impacto** (paralisar a obra, evacuar o sobrado, reforçar a contenção). Boa resposta menciona redundância de sensores para evitar alarmes falsos.
>
> **Parte 3.** Incerteza combinada:
>
> $
> u_c = \sqrt{0{,}4^2 + 0{,}6^2 + 0{,}3^2} = \sqrt{0{,}61} \approx 0{,}78\,\mathrm{mm}
> \qquad
> U = 2 \times 0{,}78 \approx 1{,}6\,\mathrm{mm}
> $
>
> O recalque está entre $11{,}2 - 1{,}6 = 9{,}6\,\mathrm{mm}$ e $11{,}2 + 1{,}6 = 12{,}8\,\mathrm{mm}$; como o intervalo **inclui** o nível de alerta de 12 mm, o alerta **pode ter sido atingido** — deve-se tratar como **atenção** (aumentar a frequência de leitura, repetir a leitura e preparar a resposta); se a leitura seguinte confirmar, passa-se ao **alerta**. Autonomia: $t = 10.000 / 0{,}25 = 40.000\,\mathrm{h} \approx 1.667\,\mathrm{dias} \approx 4{,}6\,\mathrm{anos}$, observando que a autonomia cai se a taxa de leitura aumentar em alerta.
>
> **Parte 4.** Terreno pequeno ($2.400\,\mathrm{m^2}$) e urbano → **multirrotor** com **câmera RGB** (e GNSS RTK, ou pontos de controle), eventualmente com câmera térmica para inspeção de fachadas. Requisitos: enquadramento no **RBAC nº 100** (categoria aberta se até 25 kg, em linha de visada, até 120 m e a pelo menos 30 m de pessoas não envolvidas e não anuentes ou com barreira — em área urbana densa, a operação pode exigir a categoria específica, com avaliação de risco por método aceito pela ANAC, como o SORA, e, conforme a complexidade, o COE); **cadastro no SISANT**; piloto aprovado no **exame teórico da ANAC**; **seguro** contra danos a terceiros; **avaliação de risco operacional**; solicitação de acesso ao espaço aéreo no **SARPAS** (DECEA, ICA 100-40); como o levantamento mensal gera ortomosaico e modelo 3D a partir de faixas sobrepostas, é **aerolevantamento** (Portaria GM-MD nº 3.703/2021, art. 8º): deve ser executado por empresa inscrita no Ministério da Defesa, com pedido no SARPAS 4 dias antes; a área pequena tende a ficar pré-autorizada (art. 38), desde que atendidas as condições cumulativas; equipamento **homologado pela Anatel**; e cuidados de **LGPD** com imagens de vizinhos e trabalhadores. Resposta exemplar articula as quatro partes num plano coerente, e não apenas numa lista de equipamentos.

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

> Recomendo o vídeo **"Acompanhamento de obra com DRONE na Prática"**, do canal Continental Drones, no YouTube, que mostra em campo como se faz um acompanhamento de obra com drone — equipamento, planejamento e captação das imagens. Assista com o olhar crítico desta unidade: em que ponto esse levantamento vira informação? Quem compara o resultado com o planejado? A malha está aberta ou fechada? Para conferir as regras de voo, complemente com o portal de drones da ANAC.

- **Link(s):** https://www.youtube.com/watch?v=k4_NHrCXs0U · https://www.gov.br/anac/pt-br/assuntos/drones
- **Aula em que entra:** Aulas 1 e 4

### Podcast (curadoria, até 45 min)

> No episódio #107 do podcast de **André Choma**, voltado à gestão de obras e à construção civil, o tema são os **gêmeos digitais e o uso da tecnologia na construção**. A conversa ajuda a separar o conceito do marketing — exatamente a distinção entre modelo, sombra e gêmeo digital que vimos na Aula 1. O episódio completo tem cerca de 66 minutos; para esta curadoria, ouça os **primeiros 45 minutos**.

- **Nome do podcast/canal:** André Choma (canal no YouTube)
- **Tema recomendado:** Episódio #107 — Gêmeos digitais e o uso da tecnologia na construção
- **Link:** https://www.youtube.com/watch?v=zBGzGt5tt70
- **Aula em que entra:** Aula 1

### Artigo científico

> Artigo de acesso aberto que propõe a **construção com gêmeo digital** (*Digital Twin Construction*). Os autores argumentam que o gêmeo digital não é "BIM com sensores", e sim uma forma de **fechar os laços de controle** da obra: o monitoramento automatizado alimenta o ciclo planejar-executar-verificar-agir (PDCA) em ciclos aninhados — do controle do projeto inteiro à resposta em tempo real sobre segurança e qualidade no canteiro. É a fundamentação acadêmica dos conceitos de gêmeo digital e malha fechada das Aulas 1 e 3.

- **Link:** https://doi.org/10.1017/dce.2020.16
- **Aula em que entra:** Aulas 1 e 3
- **Referência bibliográfica do artigo no formato ABNT:**
  > SACKS, Rafael; BRILAKIS, Ioannis; PIKAS, Ergo; XIE, Haiyan Sally; GIROLAMI, Mark. Construction with digital twin information systems. **Data-Centric Engineering**, v. 1, e14, 2020. DOI: 10.1017/dce.2020.16.
