# Unidade 4 — Painéis, Integração com BIM e Gestão de Riscos

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas desta unidade:** 13 a 16

## Aula 13 — Painéis de monitoramento, alertas e limites de alarme

### O que você verá nesta unidade

Nas três primeiras unidades, você aprendeu a planejar o voo, a processar as imagens e a instrumentar a obra com sensores que publicam leituras por MQTT num banco de séries temporais. Agora o dado precisa virar **decisão**. Nesta unidade, você vai montar **painéis** com limites e alertas que a equipe realmente leva a sério (Aula 13); integrar drones e sensores ao **BIM** e ao **planejamento e controle** da obra — cronograma, avanço físico e curva S (Aula 14); usar a tecnologia a favor da **segurança do trabalho**, à luz da **NR-18** (Aula 15); e proteger o sistema e as pessoas, com **LGPD** e **cibersegurança** em IoT (Aula 16), fechando a disciplina.

### Do banco de séries ao painel

> Segunda-feira, 7h. A obra tem 60 sensores e gera milhares de leituras por dia. No fim de semana, o painel disparou **37 alarmes**. Trinta e cinco eram falsos: um pico de rádio, um sensor com bateria fraca, o sol batendo numa escora. Na terceira semana assim, a equipe passou a ignorar os alarmes — e um deles era real. Esse fenômeno tem nome: **fadiga de alarmes**.

Na Aula 12, as leituras chegaram por MQTT, passaram pelo Node-RED e foram gravadas no **InfluxDB**. O **Grafana**, software de código aberto, é a camada de visualização: conecta-se ao banco como **fonte de dados** (*data source*), consulta um intervalo de tempo e desenha **painéis** (*panels*) reunidos num **dashboard**. Os tipos mais úteis no monitoramento de obras são:

- **Séries temporais** (*time series*) — a curva de cada instrumento, com os limites desenhados como faixas coloridas (*thresholds*);
- **Valor único e mostrador** (*stat*, *gauge*) — a última leitura, colorida pelo nível;
- **Linha do tempo de estados** (*state timeline*) — quando cada sensor esteve verde, amarelo ou vermelho;
- **Planta ou mapa** (*canvas*, *geomap*) — os instrumentos posicionados sobre a planta da obra ou sobre o ortomosaico do drone.

Variáveis de painel (por exemplo, "sensor" ou "frente de serviço") permitem trocar de instrumento sem duplicar telas, e as consultas devem **agregar** o dado (média horária, máximo diário) para que o painel não arraste milhões de pontos brutos.

![Captura de tela de um dashboard do Grafana com fundo escuro: no alto, três números grandes coloridos; abaixo, gráficos de séries temporais em linhas e áreas empilhadas, um gráfico de barras e legendas com nomes das séries, todos com o eixo do tempo de 07:00 a 09:30](https://thumb.wikimedia.org/wikipedia/commons/thumb/0/04/Grafana_dashboard_%282016%29.png/1280px-Grafana_dashboard_%282016%29.png)

### O que um bom painel mostra (e o que esconde)

Um painel operacional de obra precisa responder, em dez segundos, a três perguntas: **algo está fora do normal? onde? está piorando?** Para isso, mostra: a **planta** com cada instrumento colorido pelo estado; **séries com os limites desenhados** e a **velocidade** (mm/dia); a **saúde dos sensores** — bateria, sinal e hora da última leitura, porque um sensor mudo não é um sensor "verde"; e a **lista de alertas com reconhecimento**: quem viu, quando e o que fez. O painel gerencial é outro: resume tendências, pendências e indicadores de avanço (Aula 14). Evite gráficos sem limites, eixos cortados que exageram variações, cores demais e, sobretudo, **alerta sem dono**.

### Limites de atenção, alerta e alarme

Os limites não são inventados no painel: vêm do **projeto** (deslocamentos e esforços previstos no cálculo), de normas, da retroanálise de obras semelhantes e da sensibilidade do vizinho. É comum escaloná-los em três níveis acima do normal:

- **Atenção** — o comportamento saiu do esperado, mas está longe do limite de projeto;
- **Alerta** — aproxima-se do valor admissível; medidas preventivas entram em curso;
- **Alarme** — atingiu o valor que exige intervenção imediata, ainda com margem em relação ao estado-limite.

Cada nível é definido **por valor e por velocidade**: um recalque pequeno que acelera preocupa mais do que um grande que estabilizou. Os prédios inclinados da orla de Santos (SP), apoiados em fundações rasas sobre argila mole, são o lembrete clássico de que recalque diferencial evolui devagar — e de que só uma série longa, com limites claros, mostra a tendência a tempo.

![Edifício residencial alto e estreito na orla de Santos, visivelmente inclinado em relação à vertical, ao lado de outros prédios e de uma avenida com ciclistas](https://thumb.wikimedia.org/wikipedia/commons/thumb/1/19/SantosTiltedBuildings.JPG/1280px-SantosTiltedBuildings.JPG)

### O plano de ação por gatilhos (TARP)

Limite sem ação é enfeite. Os níveis se organizam num **plano de ação por gatilhos** (*Trigger Action Response Plan*, TARP), anexo ao plano de monitoramento:

| Nível | Gatilho (exemplo ilustrativo: topo de uma cortina) | Ação | Quem / prazo |
| --- | --- | --- | --- |
| **Verde — normal** | abaixo de 10 mm e menos de 0,5 mm/dia | leitura de rotina | equipe de instrumentação |
| **Amarelo — atenção** | 10 mm **ou** 0,5 mm/dia | aumentar a frequência, inspecionar, avisar o projetista | engenheiro da obra, no mesmo dia |
| **Laranja — alerta** | 14 mm **ou** 1,0 mm/dia | preparar e iniciar o reforço previsto, restringir a frente | engenheiro + projetista, em 24 h |
| **Vermelho — alarme** | 18 mm | paralisar a escavação na frente, executar a contingência, isolar a área | responsável técnico, imediato |

### Fadiga de alarmes: persistência, histerese e incerteza

As normas de gestão de alarmes da indústria de processo (ANSI/ISA-18.2, equivalente à IEC 62682) partem de um princípio que vale para a obra: **todo alarme deve exigir uma ação**; se não exige, é ruído e deve sair. Quatro técnicas reduzem os falsos alarmes:

1. **Persistência** — exigir que a condição dure um tempo mínimo ou duas leituras seguidas (no Grafana, o *pending period*);
2. **Histerese** — entrar no nível em 10,0 mm, mas só sair abaixo de 9,5 mm, para que o ruído em torno do limite não faça o alerta "piscar";
3. **Confirmação** — um segundo instrumento ou uma leitura manual confirma antes do alarme máximo;
4. **Incerteza** (Aula 9) — se $x + U$ alcança o limite, trate como atenção; se $x - U$ já passou dele, o nível está confirmado.

E o dado limpo (Aula 12) vem antes: um pico espúrio não pode acionar ninguém às 3h da manhã.

### Alertas no Grafana: regra, avaliação e notificação

No **Grafana Alerting**, uma **regra de alerta** tem uma consulta (por exemplo, o máximo dos últimos 15 min do inclinômetro I-2), uma **condição** (acima de 14 mm), um **intervalo de avaliação** e um **período pendente**. Rótulos como `severidade=alerta` e `frente=cortina-norte` direcionam a notificação, pelas **políticas de notificação**, ao **ponto de contato** certo (e-mail, aplicativo de mensagens, SMS ou plantão). **Silenciamentos** cobrem manutenções programadas — com prazo para acabar. Dois cuidados: a regra crítica (como ligar a bomba reserva) roda também **na borda** (Aula 10), porque o painel depende da internet; e o próprio sistema precisa avisar quando **para de receber dados**.

![Sala de controle panorâmica do Centro de Operações Rio, com uma grande parede de telas exibindo mapas, câmeras e gráficos, e fileiras de estações de trabalho com operadores](https://thumb.wikimedia.org/wikipedia/commons/thumb/a/ae/Sala_de_Controle_do_Centro_de_Opera%C3%A7%C3%B5es_Rio.jpg/1280px-Sala_de_Controle_do_Centro_de_Opera%C3%A7%C3%B5es_Rio.jpg)

### Exemplo numérico

Valores **ilustrativos**, com os limites do TARP acima.

**(a) Histerese.** O inclinômetro I-2 oscila em torno do nível de atenção, com ruído de cerca de ±0,3 mm: 9,8; 10,1; 9,9; 10,2; 9,9; 10,1 mm. Sem histerese, cada cruzamento para cima gera uma notificação: **3 alertas e 3 "normalizações"** em seis leituras. Com histerese de 0,5 mm (entra em 10,0 mm, sai só abaixo de 9,5 mm), o sensor entra em atenção na leitura de 10,1 mm e permanece nela: **1 notificação**, que é o que a situação pede.

**(b) Velocidade e tempo até o próximo nível.** O I-2 está em $11{,}5\,\mathrm{mm}$ e sobe $1{,}2\,\mathrm{mm/dia}$ — a velocidade já é de alerta, embora o valor seja de atenção. Mantida a tendência:

$
t_{alerta} = \frac{14 - 11{,}5}{1{,}2} \approx 2{,}1\,\mathrm{dias}
\qquad
t_{alarme} = \frac{18 - 11{,}5}{1{,}2} \approx 5{,}4\,\mathrm{dias}
$

O reforço é preparado **agora**, e a frequência de leitura passa para a cada 6 h.

**(c) Quanto vale um alarme?** Dos 37 alarmes do fim de semana, 2 eram reais. A fração de alarmes verdadeiros é

$
\frac{2}{37} \approx 0{,}054 = 5{,}4\%
$

Em 19 de cada 20 vezes, o alarme não exigia ação — a receita da fadiga. Persistência e histerese atacam justamente esses 35.

### Atividade prática

No Grafana (instalação local ou a demonstração pública em play.grafana.org), monte um dashboard com: um painel de série temporal de um sensor (use dados simulados ou o InfluxDB da Aula 12) com faixas de atenção, alerta e alarme; um painel *stat* colorido pelo nível; e um painel com a hora da última leitura. Crie uma regra de alerta com período pendente e escreva a linha do TARP correspondente (gatilho, ação, responsável e prazo).

### Pontos-chave

- O **Grafana** consulta o banco de séries (InfluxDB) e organiza painéis: séries com limites, valor atual, linha do tempo de estados e planta com o status dos instrumentos.
- Limites vêm do **projeto**, escalonados em **atenção, alerta e alarme**, definidos por **valor e por velocidade**.
- O **TARP** liga cada nível a uma ação, um responsável e um prazo; alarme sem ação é ruído.
- **Persistência, histerese, confirmação e incerteza** combatem a **fadiga de alarmes**; sensor mudo também é alarme.
- A regra crítica roda também **na borda**: o painel não pode ser o único caminho até a ação.

### Para saber mais

- **Grafana — documentação de alertas (*Grafana Alerting*):** https://grafana.com/docs/grafana/latest/alerting/
- **Grafana — painéis e visualizações:** https://grafana.com/docs/grafana/latest/panels-visualizations/
- **Grafana Play — dashboards de demonstração:** https://play.grafana.org/
- **Wikipedia — Fadiga de alarmes (*alarm fatigue*):** https://en.wikipedia.org/wiki/Alarm_fatigue

## Aula 13 — Roteiro da Videoaula 13: "37 alarmes num fim de semana: por que a equipe parou de ouvir o painel?"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 15 a 18 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, o que você verá nesta unidade e a segunda-feira dos 37 alarmes.

> "Segunda-feira, sete da manhã. O painel disparou 37 alarmes no fim de semana; 35 eram falsos. Na terceira semana assim, a equipe parou de olhar — e um deles era real. Hoje você vai aprender a montar painéis e alertas que a equipe leva a sério."

### 2. Desenvolvimento — parte 1 (0:30 – 1:20)

**[TELA]** Slides 4–7 — do InfluxDB ao Grafana, os tipos de painel, o que um bom painel mostra e o sensor mudo.

> "O Grafana é a vitrine do banco de séries temporais da Aula 12. Série com os limites desenhados, valor atual colorido, linha do tempo de estados e a planta com cada instrumento pintado pelo nível. Um bom painel responde em dez segundos: algo está fora? Onde? Está piorando? E mostra a saúde dos sensores: sensor que não fala não está verde."

### 3. Desenvolvimento — parte 2 (1:20 – 2:20)

**[TELA]** Slides 8–10 — atenção, alerta e alarme; Santos; o TARP.

> "Os limites vêm do projeto e se escalonam em atenção, alerta e alarme, por valor e por velocidade. E cada nível tem uma ação, um responsável e um prazo: é o TARP. Os prédios inclinados de Santos lembram que recalque anda devagar; só a série longa, com limites, mostra a tendência a tempo. O I-2 está em 11,5 milímetros e sobe 1,2 por dia: alerta em uns dois dias. Preparo o reforço agora."

### 4. Desenvolvimento — parte 3 (2:20 – 3:10)

**[TELA]** Slides 11–15 — gestão de alarmes, histerese animada, regra de alerta no Grafana, a regra na borda e a calculadora de velocidade.

> "Olha o sensor oscilando em torno de 10 milímetros: sem histerese, três alertas e três normalizações em seis leituras. Com histerese de meio milímetro, um só. Somo persistência, confirmação e incerteza, e os 35 falsos somem. No Grafana, a regra tem consulta, condição, período pendente, rótulo de severidade e ponto de contato. E a regra crítica roda também na borda."

### 5. Encerramento (3:10 – 3:35)

**[TELA]** Slides 16–17 — pontos-chave e encerramento.

> "Painel bom leva à decisão, não ao cansaço. Mas o painel mostra o sensor; e o cronograma, o orçamento e o modelo da obra? Na próxima aula, a gente pendura drones e sensores no BIM e no planejamento. Te espero na Aula 14!"

---

## Aula 14 — Integração dos dados com BIM e com o planejamento e controle de obras

> Reunião mensal de obra. A gerenciadora apresenta: "avanço físico de 62%, conforme o cronograma". O drone voou ontem, a nuvem de pontos está pronta e os sensores enviam leituras a cada 15 minutos — mas cada dado mora num sistema diferente, e ninguém consegue responder a duas perguntas simples: **o que foi construído é o que deveria estar pronto nesta data?** E **quanto isso custou em relação ao que foi feito?** Nesta aula, você vai ver como o **BIM** costura drones, sensores e cronograma, como medir o **avanço físico** com dados de campo e como levar essa medição à **curva S** e ao **valor agregado** da Aula 1.

### BIM: o modelo é informação, não desenho

**BIM** (*Building Information Modeling*, modelagem da informação da construção) é o processo de criar e gerir um modelo digital em que cada elemento — pilar, laje, estaca, tirante — é um **objeto com geometria, propriedades e relações**: material, fck, data de concretagem, fornecedor, fase da obra (EASTMAN *et al.*, 2014). No CAD, uma linha é uma linha; no BIM, é o "pilar P12, concreto C35, concretado em 14/03".

Para que softwares diferentes conversem, existe o **openBIM**, baseado no **IFC** (*Industry Foundation Classes*), esquema aberto da buildingSMART normalizado como **ISO 16739-1**. Cada objeto IFC tem um identificador global único (**GUID**), e há classes até para instrumentos, como `IfcSensor`, e para atividades do cronograma, como `IfcTask`. É pelo GUID que se pendura no elemento uma leitura de sensor, uma foto de drone ou uma pendência.

![Modelo BIM tridimensional em perspectiva de uma edificação térrea com telhado azul, fachadas com colunas e janelas, estacionamento com carros, árvores e calçadas ao redor](https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d0/Architectural_BIM_3D_Modeling.jpg/1280px-Architectural_BIM_3D_Modeling.jpg)

### 4D, 5D e as "dimensões" do BIM

Ligando cada elemento a uma atividade do cronograma, temos o **BIM 4D**: o modelo "cresce" no tempo, e é possível ver o que deveria estar pronto em cada data. Ligando também quantidades e custos, temos o **BIM 5D** — orçamento, medição e fluxo de caixa extraídos do modelo. Depois do 5D, a numeração varia entre autores (sustentabilidade, operação e manutenção); importa o **uso** do modelo, não o número.

![Quadro colorido com as seis "dimensões" do BIM lado a lado: 1D pesquisa e concepção, 2D desenhos, 3D forma e modelagem, 4D tempo e planejamento, 5D custo e quantitativos e 6D desempenho, cada uma com seus usos listados](https://upload.wikimedia.org/wikipedia/commons/6/68/6_BIM_DIMENSIONS.png)

### BIM na administração pública e a ISO 19650

No Brasil, a **Estratégia BIM BR** (Decreto nº 9.983/2019) organiza a disseminação do BIM, e o **Decreto nº 10.306/2020** tornou seu uso obrigatório, em fases, nas obras federais abrangidas: desde 2021, nos projetos; desde 2024, também na **execução** — orçamentação, **planejamento e controle** da obra e atualização do modelo **as-built**; a partir de 2028, na gestão pós-obra. A Lei nº 14.133/2021 (art. 19, § 3º) manda adotar o BIM preferencialmente nas licitações de obras, quando adequado ao objeto.

A série **ISO 19650** trata da gestão da informação com BIM e tem como conceito central o **ambiente comum de dados** (CDE): cada arquivo passa por estados controlados — em elaboração, compartilhado, publicado e arquivado. Leitura de sensor, ortomosaico e nuvem de pontos também são informação da obra: precisam de dono, versão e estado.

### Do canteiro ao modelo: drone e sensores ligados ao GUID

A integração tem três fluxos:

- **Drone → modelo.** A nuvem de pontos registrada (Aula 7) é comparada ao modelo (Aula 8). Aqui o que interessa é a pergunta de **controle**: quais elementos já existem? Cada elemento confirmado recebe a data de execução.
- **Sensores → modelo.** O ID de cada inclinômetro, piezômetro ou extensômetro (Aula 9) é associado ao GUID do elemento; o painel da Aula 13 passa a pintar o próprio modelo pelo nível de alerta.
- **Pendências → modelo.** Cada desvio ou não conformidade vira um tópico **BCF** (*BIM Collaboration Format*) preso ao elemento, com responsável e prazo.

![Nuvem de pontos em tons de cinza de uma casa de máquinas, obtida por escaneamento a laser, com as tubulações modeladas em BIM sobrepostas em azul-claro, mostrando o alinhamento entre o capturado e o modelado](https://thumb.wikimedia.org/wikipedia/commons/thumb/2/23/Scan-to-BIM_Mechanical_Room.jpg/1280px-Scan-to-BIM_Mechanical_Room.jpg)

### Medição de avanço físico com dados de campo

O **avanço físico** é a porcentagem executada do total, por serviço e para a obra inteira. Como serviços diferentes não se somam em m³ e m², a obra pondera cada um por um **peso** — em geral, sua participação no orçamento (MATTOS, 2010). O modelo dá as **quantidades previstas**; o drone, a nuvem e as câmeras dão as **quantidades executadas**: volume de concreto dos elementos confirmados, área de laje concretada, metros de alvenaria visíveis no ortomosaico. A medição sai do campo, não da planilha preenchida de memória — e fica rastreável no CDE.

![Vista aérea de drone de um conjunto residencial em construção, com cerca de vinte blocos de três pavimentos em diferentes estágios, terreno de terra exposta, vias internas e a mata ao redor](https://thumb.wikimedia.org/wikipedia/commons/thumb/5/5b/Livana_Colts_Neck_Under_Construction%2C_September_2025_%28Aerial%29.jpg/1280px-Livana_Colts_Neck_Under_Construction%2C_September_2025_%28Aerial%29.jpg)

### Curva S e valor agregado: do avanço à decisão

Na Aula 1, você viu a **curva S**: o avanço acumulado previsto ao longo do tempo. Com a medição de campo, desenha-se a curva **realizada** ao lado da prevista, e o **valor agregado** compara três grandezas na mesma data:

- **VP** (valor planejado) — custo orçado do que deveria estar pronto;
- **VA** (valor agregado) — custo orçado do que **foi** executado = avanço físico × orçamento;
- **CR** (custo real) — o que efetivamente se gastou.

Daí saem o **índice de desempenho de prazo**, $IDP = VA/VP$, e o **índice de desempenho de custo**, $IDC = VA/CR$. Abaixo de 1, a obra está atrasada ou gastando mais do que agrega.

### Do modelo ao gêmeo digital: fechando a malha

Modelo atualizado automaticamente pelo canteiro é uma **sombra digital**. Quando a decisão volta à obra — a plataforma reprograma a frente no 4D e aciona a equipe —, temos um **gêmeo digital**. Na prática, o mais comum e útil é a sombra digital com um engenheiro fechando a **malha** da Aula 1: medir, comparar com o planejado, decidir, agir e medir de novo.

### Exemplo numérico

Obra com orçamento de $\mathrm{R\$}\,20{,}0$ milhões; no mês 10, a curva S previa 45% de avanço. Valores **ilustrativos**.

| Serviço | Peso | Executado (fonte) |
| --- | --- | --- |
| Fundações | 15% | 100% (as-built) |
| Estrutura | 45% | 50% — nuvem confirma $2.250$ de $4.500\,\mathrm{m^3}$ |
| Alvenaria | 25% | 10% (ortomosaico) |
| Instalações | 15% | 5% (vistoria) |

$
AF = 0{,}15 \times 1 + 0{,}45 \times 0{,}50 + 0{,}25 \times 0{,}10 + 0{,}15 \times 0{,}05 = 0{,}4075 \approx 40{,}8\%
$

$
VP = 0{,}45 \times 20{,}0 = 9{,}00
\qquad
VA = 0{,}4075 \times 20{,}0 = 8{,}15
\qquad
CR = 8{,}60 \quad (\mathrm{R\$}\ \text{milhões})
$

$
IDP = \frac{8{,}15}{9{,}00} \approx 0{,}91
\qquad
IDC = \frac{8{,}15}{8{,}60} \approx 0{,}95
$

A obra está atrasada (agregou 91% do planejado) e gasta 5% acima do que agrega. Mantido o desempenho, o custo final estimado é $20{,}0/0{,}95 \approx \mathrm{R\$}\,21{,}1$ milhões, e o 4D aponta onde está o atraso: a estrutura, que puxa a alvenaria.

### Atividade prática

Pegue o cronograma de uma obra (pode ser acadêmico) com quatro ou cinco serviços e seus pesos. Para uma data, invente as quantidades medidas pelo drone e pelos sensores, calcule o avanço físico ponderado, o VP, o VA, um CR plausível, o IDP e o IDC, desenhe a curva S prevista e a realizada e escreva o tópico BCF da frente mais atrasada (elemento, problema, responsável e prazo).

### Pontos-chave

- **BIM** é modelo de informação; o **IFC** (ISO 16739-1) e o **GUID** ligam leituras, nuvens e pendências (BCF) a cada elemento.
- **4D** liga o modelo ao cronograma; **5D**, a custos. O Decreto nº 10.306/2020 exige, desde 2024, BIM no planejamento e controle da execução nas obras federais abrangidas.
- O **avanço físico** é ponderado por pesos; o modelo dá o previsto, e drone, nuvem e sensores dão o executado.
- **Curva S** e **valor agregado** ($IDP = VA/VP$, $IDC = VA/CR$) transformam a medição de campo em decisão de prazo e custo.
- Modelo atualizado pelo canteiro é **sombra digital**; com a decisão voltando à obra, **gêmeo digital**.

### Para saber mais

- **Planalto — Decreto nº 10.306/2020 (BIM na administração pública federal):** https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/decreto/D10306.htm
- **MDIC — Estratégia BIM BR:** https://www.gov.br/mdic/pt-br/assuntos/sdic/building-information-modelling-bim
- **buildingSMART — Industry Foundation Classes (IFC):** https://www.buildingsmart.org/standards/bsi-standards/industry-foundation-classes/
- **Wikipedia — Análise de valor agregado:** https://pt.wikipedia.org/wiki/An%C3%A1lise_de_valor_agregado
- **Livros da bibliografia:** EASTMAN, C. *et al.* *Manual de BIM*. Porto Alegre: Bookman, 2014; MATTOS, A. D. *Planejamento e controle de obras*. São Paulo: Pini, 2010.

## Aula 14 — Roteiro da Videoaula 14: "O drone diz 41%, a planilha diz 62%: quem está certo?"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 15 a 18 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e a reunião dos "62%".

> "Reunião de obra: a gerenciadora diz 62%, conforme o cronograma. O drone voou ontem, os sensores mandam leitura a cada 15 minutos, mas cada dado mora num sistema. O que foi construído é o que deveria estar pronto? E quanto custou? Hoje o BIM e o valor agregado respondem."

### 2. Desenvolvimento — parte 1 (0:30 – 1:20)

**[TELA]** Slides 4–7 — BIM é informação, IFC e GUID, as dimensões do BIM e a lei.

> "BIM não é desenho 3D: é modelo de informação. Cada pilar é um objeto com um identificador, o GUID; o IFC, aberto, deixa os softwares conversarem. Ligou ao cronograma, 4D; a custos, 5D. E desde 2024 o Decreto 10.306 exige BIM no planejamento e controle das obras federais abrangidas."

### 3. Desenvolvimento — parte 2 (1:20 – 2:20)

**[TELA]** Slides 8–11 — os três fluxos (drone, sensores, pendências), o 4D em 3D e a medição de avanço.

> "Três fluxos chegam ao modelo: a nuvem do drone confirma o que existe; os sensores, pelo GUID, pintam o elemento pelo nível de alerta; e cada problema vira um tópico BCF. Arrasto a semana no 4D: o fantasma é o planejado, o sólido é o executado. E o avanço físico se pondera por pesos: fundações, estrutura, alvenaria, instalações."

### 4. Desenvolvimento — parte 3 (2:20 – 3:10)

**[TELA]** Slides 12–16 — curva S prevista × realizada, a calculadora de valor agregado, a rotina semanal de integração e a malha fechada.

> "A conta: avanço ponderado de 40,8% contra 45% previstos. Valor planejado, 9 milhões; agregado, 8,15; custo real, 8,6. IDP de 0,91: atrasada. IDC de 0,95: gastando mais do que agrega. Os 62% da reunião não param em pé. Com o modelo atualizado pelo canteiro e o engenheiro decidindo, fechamos a malha."

### 5. Encerramento (3:10 – 3:35)

**[TELA]** Slides 17–18 — atividade, pontos-chave e encerramento.

> "Agora o dado de campo chega ao cronograma e ao custo. Mas a obra não é só prazo e custo: é gente trabalhando em altura, ao lado de máquinas. Na próxima aula, a NR-18 e a tecnologia a favor da segurança. Te espero na Aula 15!"

---

## Aula 15 — Segurança do trabalho, NR-18 e tecnologia para prevenção

> Terça-feira, 10h. O anemômetro da grua marca rajadas de 13 m/s, mas o operador não tem o número na cabine e continua içando fôrmas. Na rampa da escavação, um caminhão dá ré com o alarme sonoro desligado "porque incomodava a vizinhança" e passa a meio metro de um ajudante. No 9º pavimento, falta um trecho de guarda-corpo retirado para passar material. Nenhum desses riscos é novo — a **NR-18** trata de todos eles. O que mudou é que hoje temos sensores, câmeras e drones capazes de **ver o risco antes do acidente**. Nesta aula, você vai ligar a norma à tecnologia, sem esquecer os limites de cada uma.

### A NR-18 hoje: estrutura e o PGR

A **NR-18 — Segurança e Saúde no Trabalho na Indústria da Construção** teve a redação reformulada pela Portaria SEPRT nº 3.733/2020, em vigor desde 2021, com alterações posteriores. O texto vigente é organizado por temas: responsabilidades, **Programa de Gerenciamento de Riscos (PGR)**, áreas de vivência, instalações elétricas, etapas de obra, escadas e rampas, **proteção contra quedas de altura** (18.9), **máquinas, equipamentos e ferramentas** (18.10), movimentação de materiais e pessoas, andaimes, **sinalização** (18.13) e capacitação.

O **PGR** substituiu o antigo PCMAT. É obrigatório nos canteiros, contemplando os riscos ocupacionais e suas medidas de prevenção (item 18.4.1); é elaborado por profissional legalmente habilitado em segurança do trabalho (18.4.2) e, além do exigido pela NR-01, contém os projetos dos sistemas de proteção coletiva e, quando aplicável, dos sistemas de proteção individual contra quedas, e a relação dos EPI (18.4.3). E deve estar **atualizado conforme a etapa** da obra (18.4.3.1) — exatamente o que um sistema de monitoramento ajuda a manter.

### Riscos críticos e a hierarquia das medidas

Quedas de altura, soterramento em escavações, choque elétrico, atropelamento por máquinas e queda de materiais estão entre os riscos mais graves do canteiro. A NR-01 ordena as medidas de prevenção: primeiro **eliminar** o risco; depois, **proteção coletiva**; em seguida, medidas **administrativas** e de organização do trabalho; e, por fim, o **EPI**. Na NR-18, a proteção coletiva é obrigatória onde houver risco de queda de trabalhadores ou de projeção de materiais (18.9.1) e, na periferia da edificação, a partir dos serviços da primeira laje (18.9.4), com guarda-corpo de travessão superior a 1,2 m, intermediário a 0,7 m e rodapé de 0,15 m (18.9.4.2). Trabalho acima de 2 m com risco de queda segue também a NR-35.

A tecnologia entra **dentro** dessa hierarquia: um sensor não substitui o guarda-corpo, mas avisa quando ele sumiu.

![Fachada de um edifício alto em construção inteiramente envolvida por andaimes cobertos com tela verde de proteção, que retém materiais e reduz o risco de queda de objetos sobre a rua](https://thumb.wikimedia.org/wikipedia/commons/thumb/2/22/11_Scaffolding_safety_plastic_net_-_polyethylene_material_nets_at_construction_site_in_Makati_Manila.jpg/1280px-11_Scaffolding_safety_plastic_net_-_polyethylene_material_nets_at_construction_site_in_Makati_Manila.jpg)

### A NR-18 já exige sensores: máquinas e gruas

Parte dos dispositivos que a norma pede já é sensoriamento. Máquinas autopropelidas devem ter retrovisores e **alarme sonoro acoplado ao câmbio** na marcha a ré (18.10.1.6, alínea f). Equipamentos de guindar têm **limitador de carga ou de momento** com alarme sonoro. E a **grua** deve dispor de **anemômetro** e de dispositivo automático com alarme sonoro que indique **ventos acima de 42 km/h** (18.10.1.33, j); acima desse valor, o trabalho exige análise de risco e permissão de trabalho, e **acima de 72 km/h a operação é proibida** (18.10.1.34). Conectados à plataforma IoT (Aulas 11 e 12), esses sinais deixam de ser locais: o anemômetro aparece no painel da Aula 13, com histórico e alerta ao encarregado.

![Mastro alaranjado de uma grua torre montado no poço de uma edificação em construção, visto de baixo, com trabalhadores de capacete e colete de alta visibilidade ao lado](https://thumb.wikimedia.org/wikipedia/commons/thumb/f/f3/Tower_crane_at_a_building_construction_site_in_Taichung_2023-05-13_01.jpg/1280px-Tower_crane_at_a_building_construction_site_in_Taichung_2023-05-13_01.jpg)

### Sensores vestíveis, gases e cercas virtuais

Etiquetas **UWB** (precisão de decímetros) ou **BLE** (metros) em capacetes e crachás formam sistemas de **localização em tempo real** (RTLS) que criam **cercas virtuais**: entrar na zona de giro da escavadeira dispara aviso ao operador e ao trabalhador. **Detectores de gases** em escavações, poços e galerias (espaços confinados, NR-33) avisam antes da entrada. Sensores de inclinação em escoramentos, de vibração e de poeira (Aula 9) completam o quadro. Toda localização de pessoa, porém, é **dado pessoal** (Aula 16).

### Visão computacional: EPI e zonas de risco

Câmeras com **detecção de objetos** reconhecem capacete, colete de alta visibilidade (exigido em áreas de movimentação de veículos, 18.13.2) e pessoas dentro de zonas de risco desenhadas na imagem. A qualidade de cada caixa detectada se mede pela **IoU** (interseção sobre união), e o modelo, por **precisão** ($P = VP/(VP+FP)$) e **revocação** ($R = VP/(VP+FN)$). Em segurança, o falso negativo — a pessoa sem capacete não detectada — custa mais caro; por isso, o limiar é ajustado para revocação alta, com revisão humana. E um projeto ético detecta o **EPI**, não a **pessoa**: sem reconhecimento facial e, de preferência, processando na borda.

![Placa de pare fotografada na rua com duas caixas sobrepostas: em verde, a caixa de referência desenhada por uma pessoa; em vermelho, a caixa prevista por um detector de objetos, quase coincidente](https://upload.wikimedia.org/wikipedia/commons/2/2d/Intersection_over_Union_-_object_detection_bounding_boxes.jpg)

### Drones na inspeção de segurança

O drone inspeciona **sem expor ninguém**: bandejas e redes de proteção, guarda-corpos da periferia, coberturas, taludes e escoramentos de escavação, ancoragens de andaimes. Um voo semanal com fotos georreferenciadas vira **evidência datada** para o PGR. Valem as regras das Aulas 3 e 4: operação segundo o RBAC nº 100 da ANAC, acesso ao espaço aéreo pelo DECEA, área de segurança e nada de sobrevoar trabalhadores sem a devida análise de risco.

![Vista aérea de drone de um viaduto de concreto sobre um vale arborizado, registrada durante uma inspeção, mostrando o tabuleiro e os pilares](https://thumb.wikimedia.org/wikipedia/commons/thumb/2/21/Drone_view_of_a_bridge_during_an_inspection.jpg/1280px-Drone_view_of_a_bridge_during_an_inspection.jpg)

### Pausa para reflexão (Desafio)

A construtora quer instalar câmeras com **reconhecimento facial** em todos os acessos e frentes, para identificar quem está sem capacete e aplicar advertências. O crachá UWB que evita o atropelamento na rampa também registra, minuto a minuto, onde cada trabalhador esteve. O objetivo — segurança — é legítimo. Mas há alternativas menos invasivas: detectar o capacete **sem** identificar a pessoa e alertar o encarregado da frente; processar a proximidade com a máquina na borda, sem guardar o histórico nominal. **Onde termina a prevenção e começa a vigilância?** Considere a finalidade, a necessidade, a transparência, o prazo de guarda e quem terá acesso às imagens.

### Exemplo numérico

Valores **ilustrativos**.

**(a) Vento na grua.** O anemômetro registra rajada de $13\,\mathrm{m/s}$:

$
13 \times 3{,}6 = 46{,}8\,\mathrm{km/h} > 42\,\mathrm{km/h}
\qquad
72\,\mathrm{km/h} \div 3{,}6 = 20\,\mathrm{m/s}
$

Exige análise de risco específica e permissão de trabalho; a 20 m/s, a operação está proibida. O alerta da plataforma deve disparar a 42 km/h, não depois.

**(b) Detector de capacete.** Em 400 imagens de teste há 120 pessoas sem capacete. O modelo acertou $VP = 102$, perdeu $FN = 18$ e deu $FP = 34$ alarmes falsos:

$
P = \frac{102}{136} = 0{,}75
\qquad
R = \frac{102}{120} = 0{,}85
\qquad
F_1 = \frac{2 \times 0{,}75 \times 0{,}85}{0{,}75 + 0{,}85} \approx 0{,}80
$

Encontra 85% das situações de risco; 1 em cada 4 avisos é falso — aceitável para alertar o encarregado, nunca para punir automaticamente.

**(c) Taxa de frequência.** A ABNT NBR 14280 mede a frequência de acidentes por milhão de horas-homem de exposição: $TF = N \times 10^6 / HHT$. Com 180 trabalhadores, 220 h/mês, em 12 meses ($HHT = 475.200\,\mathrm{h}$) e 4 acidentes com afastamento:

$
TF = \frac{4 \times 10^6}{475.200} \approx 8{,}4
$

### Atividade prática

Para uma obra que você conheça, liste cinco riscos críticos do PGR e, para cada um, indique: a medida de proteção coletiva exigida pela NR-18; uma tecnologia que ajude a verificá-la (sensor, câmera ou drone), com o gatilho de alerta; o responsável pela resposta; e o cuidado de privacidade necessário.

### Pontos-chave

- A **NR-18** vigente exige o **PGR** no canteiro, elaborado por profissional habilitado e atualizado conforme a etapa da obra.
- Hierarquia: eliminar, **proteger coletivamente**, organizar e, por fim, o EPI; a tecnologia verifica as medidas, não as substitui.
- A norma já pede sensores: alarme de ré, limitador de carga e **anemômetro da grua** (alarme acima de 42 km/h; operação proibida acima de 72 km/h).
- Visão computacional detecta EPI e zonas de risco; avalie por **revocação e precisão**, detecte o EPI, não a pessoa.
- Drones inspecionam proteções e taludes **sem expor trabalhadores**, gerando evidência datada para o PGR.

### Para saber mais

- **MTE — NR-18 (Segurança e Saúde no Trabalho na Indústria da Construção):** https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/norma-regulamentadora-no-18-nr-18
- **Fundacentro — Segurança do trabalho na indústria da construção:** https://www.gov.br/fundacentro/pt-br
- **Wikipedia — Sistema de localização em tempo real (RTLS):** https://en.wikipedia.org/wiki/Real-time_locating_system

## Aula 15 — Roteiro da Videoaula 15: "Rajada de 46 km/h na grua: a tecnologia vê o risco antes do acidente?"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 15 a 18 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:30)

**[TELA]** Slides 1–3 — capa, sumário e a terça-feira dos três riscos.

> "Rajada de 13 metros por segundo na grua, e o operador sem o número na cabine. Um caminhão de ré com o alarme desligado. Um trecho de guarda-corpo retirado no nono pavimento. A NR-18 trata de todos. Hoje, a tecnologia que ajuda a ver o risco antes do acidente."

### 2. Desenvolvimento — parte 1 (0:30 – 1:20)

**[TELA]** Slides 4–7 — a estrutura da NR-18, o PGR, a hierarquia das medidas e a proteção coletiva.

> "A NR-18 vigente exige o PGR no canteiro, feito por profissional habilitado e atualizado a cada etapa. A ordem das medidas é eliminar, proteger coletivamente, organizar e, por último, o EPI. Guarda-corpo de 1,2 metro desde a primeira laje. A tecnologia não substitui o guarda-corpo: avisa quando ele sumiu."

### 3. Desenvolvimento — parte 2 (1:20 – 2:20)

**[TELA]** Slides 8–10 — a norma que já pede sensores, o anemômetro da grua, as cercas virtuais e os detectores de gases.

> "A norma já pede sensor: alarme de ré, limitador de carga, anemômetro na grua com alarme acima de 42 quilômetros por hora. Treze metros por segundo são 46,8: precisa de análise de risco e permissão de trabalho. Acima de 72, proibido. Ligue isso à plataforma IoT e o encarregado vê no painel. Somo as etiquetas UWB, com cercas virtuais em torno das máquinas, e os detectores de gases."

### 4. Desenvolvimento — parte 3 (2:20 – 3:15)

**[TELA]** Slides 11–16 — o detector de EPI, precisão e revocação, o drone na inspeção, o TARP de segurança, a calculadora e a pausa para reflexão.

> "A câmera detecta capacete e colete e pessoas dentro da zona de risco. Revocação de 85%, precisão de 75%: bom para avisar o encarregado, nunca para punir sozinho. O drone inspeciona bandejas, guarda-corpos e taludes sem expor ninguém. E pense: reconhecimento facial para cobrar capacete é prevenção ou vigilância?"

### 5. Encerramento (3:15 – 3:40)

**[TELA]** Slides 17–18 — atividade, pontos-chave e encerramento.

> "Câmeras, crachás e sensores protegem pessoas, mas também coletam dados delas e abrem portas para invasores. Na última aula, LGPD e cibersegurança em IoT, e o fechamento da disciplina. Te espero na Aula 16!"

---

## Aula 16 — Privacidade, LGPD e cibersegurança em sistemas IoT de obras (fechamento da disciplina)

> O sistema de monitoramento está no ar: 60 sensores, um gateway LoRaWAN com 4G, câmeras com IA nos acessos, voo semanal de drone e o painel no Grafana. Na reunião de aprovação, duas pessoas fazem as perguntas que faltavam. A advogada: **"podemos filmar trabalhadores e a casa do vizinho? Por quanto tempo guardamos isso?"**. O gerente de TI: **"a senha do gateway ainda é a de fábrica? E se alguém alterar as leituras do inclinômetro?"**. Nesta aula final, você vai aprender a responder às duas — porque um monitoramento que expõe pessoas ou aceita dados adulterados não protege ninguém.

### LGPD: dado pessoal no canteiro

A **Lei Geral de Proteção de Dados** (Lei nº 13.709/2018) define dado pessoal como informação relacionada a pessoa natural **identificada ou identificável** (art. 5º, I). No monitoramento, isso inclui rostos em fotos de drone e câmeras, placas de veículos, o quintal do vizinho, a localização de trabalhadores rastreados, registros de acesso ao canteiro e de quem acessou a plataforma. **Biometria** — como o reconhecimento facial — e dados de **saúde** são **dados sensíveis** (art. 5º, II), com regras mais restritas (art. 11).

![Câmera de vigilância do tipo domo, com movimento horizontal, vertical e zoom, presa por um braço curvo a um poste de iluminação pública, contra o céu](https://thumb.wikimedia.org/wikipedia/commons/thumb/3/35/Security_Camera-07-PTZ_mounted_on_light_pole.jpg/1280px-Security_Camera-07-PTZ_mounted_on_light_pole.jpg)

### Bases legais, princípios e o trabalhador

Todo tratamento precisa de uma **base legal** (art. 7º): entre elas, cumprimento de **obrigação legal** (por exemplo, registros exigidos pelas normas de segurança), execução de contrato, proteção da vida e da incolumidade física e **legítimo interesse**. Na relação de emprego, o **consentimento** é frágil — o trabalhador dificilmente se sente livre para recusar —, e por isso raramente é a melhor base. E todo tratamento respeita os **princípios** do art. 6º, sobretudo **finalidade** (para que serve), **necessidade** (o mínimo de dados), **transparência** (avisar quem é filmado) e **segurança**. A câmera instalada para detectar EPI não pode virar, sem aviso, ferramenta de avaliação de desempenho individual.

### Privacidade desde a concepção e governança

- **Minimização**: enquadrar voos e câmeras no canteiro; aplicar **máscara de privacidade** sobre janelas e quintais vizinhos; detectar o EPI, não identificar a pessoa.
- **Desfoque automático** de rostos e placas quando a identificação não é necessária.
- **Retenção definida**: imagens guardadas por prazo certo e depois descartadas.
- **Aviso** nos acessos e comunicação prévia aos vizinhos.
- **Papéis**: o **controlador** decide (em geral, a construtora); o **operador** trata em nome dele (a empresa de monitoramento); o **encarregado** é o canal com titulares e ANPD; e, para tratamentos de risco, o **relatório de impacto** (RIPD).

A fiscalização é da **ANPD**. Incidente de segurança com risco ou dano relevante aos titulares deve ser comunicado à ANPD e aos titulares (art. 48) — pela Resolução CD/ANPD nº 15/2024, em regra em **três dias úteis** —, e as sanções incluem multa de até 2% do faturamento, limitada a R\$ 50 milhões por infração (art. 52). O art. 46 obriga os agentes a adotar medidas de **segurança** técnicas e administrativas: é aqui que a LGPD encontra a cibersegurança.

### Por que um sistema IoT de obra é alvo

Segurança da informação protege **confidencialidade**, **integridade** e **disponibilidade**. No monitoramento, a mais crítica é a **integridade**: uma leitura adulterada pode esconder um recalque, e um alerta apagado pode atrasar uma evacuação. Dispositivos IoT são alvos fáceis: ficam expostos no campo, raramente são atualizados e, muitas vezes, saem de fábrica com **credenciais padrão**. Foi assim que a *botnet* Mirai, em 2016, sequestrou centenas de milhares de câmeras e roteadores apenas testando senhas de fábrica. Senhas fracas, padrão ou embutidas lideram a lista **OWASP IoT Top 10**.

![Gateway LoRaWAN instalado no alto de um mastro, com antena vertical e caixa de equipamentos, sobre a vista de uma cidade portuária com um canal e prédios ao fundo](https://thumb.wikimedia.org/wikipedia/commons/thumb/a/a7/2018-08-31_-_LoRaWan_Gateway_HoernCampus_Kiel.jpg/1280px-2018-08-31_-_LoRaWan_Gateway_HoernCampus_Kiel.jpg)

### Controles mínimos de cibersegurança em IoT

- **Credenciais**: trocar toda senha de fábrica no comissionamento; uma credencial por dispositivo; autenticação forte na plataforma e no Grafana. A Anatel, no Ato nº 77/2021, passou a exigir de roteadores e modems a troca da senha padrão e atualizações de segurança.
- **Criptografia no caminho**: o LoRaWAN cifra as mensagens com chaves AES-128; o **MQTT** deve rodar sobre **TLS** (porta 8883, não a 1883 em texto puro), com usuário e senha ou certificado por dispositivo e **listas de controle de acesso por tópico** — o sensor I-2 só publica em `obra/cortina/I-2`.
- **Segmentação de rede**: sensores, gateway e câmeras numa rede (VLAN) separada da rede administrativa e do Wi-Fi de visitantes, com *firewall* liberando só o necessário.
- **Firmware**: inventário de dispositivos e versões, atualizações assinadas, preferencialmente remotas (OTA), e substituição do que não recebe mais correções.
- **Rastreabilidade**: registro (*log*) de acessos e alterações, cópias de segurança das séries e conferência de lacunas e saltos.

![Três switches de rede empilhados num rack, com cabos conectados e luzes indicando o estado de cada porta](https://thumb.wikimedia.org/wikipedia/commons/thumb/0/04/Network_switches_arranged_in_a_server_rack_with_visible_LED_lights_indicating_connection_status_and_power_levels.jpg/1280px-Network_switches_arranged_in_a_server_rack_with_visible_LED_lights_indicating_connection_status_and_power_levels.jpg)

### Exemplo numérico

Valores **ilustrativos**.

**(a) A senha do gateway.** Uma senha numérica de 6 dígitos tem $10^6$ combinações; a 100 tentativas por segundo, cai em no máximo $10^4\,\mathrm{s} \approx 2{,}8\,\mathrm{h}$. Uma senha aleatória de 12 caracteres entre 62 símbolos (letras maiúsculas, minúsculas e algarismos):

$
62^{12} \approx 3{,}2 \times 10^{21}
\qquad
\frac{3{,}2 \times 10^{21}}{10^{9}\,\mathrm{s^{-1}}} \approx 3{,}2 \times 10^{12}\,\mathrm{s} \approx 100\,000\ \text{anos}
$

E a senha de fábrica? **Uma** tentativa: ela está no manual, na internet.

**(b) Teto da multa.** A multa simples é de até 2% do faturamento no Brasil no último exercício, limitada a R\$ 50 milhões por infração. Para faturamento de R\$ 900 milhões: $0{,}02 \times 900 = 18$ milhões. Para R\$ 3,5 bilhões: $0{,}02 \times 3.500 = 70$ milhões, limitados a **R\$ 50 milhões**.

**(c) Prazo do incidente.** A construtora toma conhecimento, numa quinta-feira, de que as imagens das câmeras foram expostas. Em três dias úteis (sem feriados): sexta, segunda e terça — a comunicação à ANPD deve sair **até terça-feira**.

### Atividade prática

Para o sistema de monitoramento de uma obra que você escolher, monte uma **ficha de privacidade e segurança** com: (1) o inventário de dados pessoais (o quê, de quem, base legal, finalidade, prazo de guarda e medida de minimização); (2) a arquitetura da rede, com a segmentação e onde há TLS; (3) cinco controles de cibersegurança com o responsável por cada um; (4) o fluxo de resposta a incidente, até a comunicação à ANPD.

### Pontos-chave

- Imagens, localização e acessos de obra contêm **dados pessoais**; biometria e saúde são **sensíveis**. Todo tratamento precisa de **base legal**, finalidade, necessidade e transparência.
- **Privacidade desde a concepção**: máscara, desfoque, retenção definida, detectar o EPI e não a pessoa; papéis de controlador, operador e encarregado.
- Em monitoramento, a **integridade** do dado é questão de segurança estrutural.
- Controles mínimos: **trocar credenciais padrão**, **MQTT sobre TLS** com ACL por tópico, **segmentação de rede**, **firmware atualizado** e logs.
- Incidente relevante vai à **ANPD** em três dias úteis; multa de até 2% do faturamento, limitada a R\$ 50 milhões por infração.

### Para saber mais

- **Planalto — Lei nº 13.709/2018 (LGPD):** https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- **ANPD — Autoridade Nacional de Proteção de Dados:** https://www.gov.br/anpd/pt-br
- **OWASP — Internet of Things Project (IoT Top 10):** https://owasp.org/www-project-internet-of-things/
- **HiveMQ — MQTT Security Fundamentals (TLS e autenticação):** https://www.hivemq.com/blog/mqtt-security-fundamentals/

### Encerramento da disciplina

Você começou esta disciplina com uma pergunta: **a obra está como deveria estar?** Ao longo de 16 aulas, aprendeu a responder com método. Na **Unidade 1**, os fundamentos: indicadores de controle de avanço e curva S, tipos de drones e sensores embarcados, a regulamentação de ANAC, DECEA e Anatel e o planejamento de uma missão segura. Na **Unidade 2**, o drone em ação: fotogrametria, GNSS e precisão, ortomosaicos, modelos de superfície e nuvens de pontos, volumes e a comparação entre projetado e executado. Na **Unidade 3**, os sensores: inclinômetros, extensômetros, acelerômetros, temperatura e poeira, plataformas embarcadas, redes LoRaWAN, Wi-Fi e celulares e o MQTT com séries temporais. E nesta unidade, a gestão: painéis e alertas, BIM e valor agregado, segurança do trabalho e proteção de dados.

![Edifício alto em construção, com a estrutura de concreto e as fachadas envidraçadas inacabadas nos últimos pavimentos e uma grua torre amarela e vermelha acima, contra o céu azul](https://thumb.wikimedia.org/wikipedia/commons/thumb/9/95/Edif%C3%ADcio_em_constru%C3%A7%C3%A3o.jpg/1280px-Edif%C3%ADcio_em_constru%C3%A7%C3%A3o.jpg)

O fio que amarra tudo é a **malha fechada**: medir, comparar com um limite, decidir, agir e medir de novo — com segurança para quem trabalha e respeito a quem é medido. Tecnologia nenhuma substitui o engenheiro que conhece o solo, a estrutura e a obra; mas o engenheiro que domina essa tecnologia decide mais cedo, com mais confiança e com mais gente protegida. É esse profissional que o mercado procura, e é esse profissional que você está pronto para ser.

## Aula 16 — Roteiro da Videoaula 16: "A senha do gateway era 'admin': o elo mais fraco do monitoramento"

**Duração: 3 a 4 minutos** (versão-guia resumida, para orientar a sequência dos slides). **A versão a gravar é a fala integral de `roteiros_15min.md`, com 15 a 18 minutos.** As marcações **[TELA]** indicam os slides de `slides/aulaN.html`.

### 1. Abertura (0:00 – 0:25)

**[TELA]** Slides 1–3 — capa, sumário e as duas perguntas da reunião.

> "O sistema está no ar. A advogada pergunta se podemos filmar trabalhadores e a casa do vizinho. O pessoal de TI pergunta se a senha do gateway ainda é a de fábrica. Hoje, as duas respostas — e o fechamento da disciplina."

### 2. Desenvolvimento — parte 1 (0:25 – 1:20)

**[TELA]** Slides 4–7 — dados pessoais no canteiro, bases legais, o trabalhador e a câmera com máscara de privacidade.

> "Rosto, placa, quintal do vizinho, localização do trabalhador: tudo é dado pessoal. Biometria é sensível. Todo tratamento precisa de base legal — obrigação legal, contrato, proteção da vida, legítimo interesse — e de finalidade, necessidade e transparência. Com trabalhador, consentimento é frágil. Na prática: máscara de privacidade, desfoque, prazo de guarda, aviso, e detectar o EPI, não a pessoa."

### 3. Desenvolvimento — parte 2 (1:20 – 2:25)

**[TELA]** Slides 8–12 — confidencialidade, integridade e disponibilidade; a Mirai; a calculadora de senhas; MQTT com TLS; a rede segmentada.

> "Aqui, a propriedade mais crítica é a integridade: leitura adulterada esconde recalque. Em 2016, a Mirai sequestrou centenas de milhares de câmeras testando senhas de fábrica. A senha de fábrica cai na primeira tentativa; uma senha aleatória de 12 caracteres levaria uns cem mil anos. MQTT sobre TLS na porta 8883, ACL por tópico, rede separada e firmware atualizado."

### 4. Desenvolvimento — parte 3 (2:25 – 3:10)

**[TELA]** Slides 13–16 — resposta a incidentes e contrato, a calculadora (senha, multa e prazo), a jornada da disciplina e a malha fechada.

> "Controlador, operador, encarregado e relatório de impacto. Vazou? Três dias úteis para comunicar a ANPD: soube na quinta, comunica até terça. Multa de até 2% do faturamento, com teto de 50 milhões. E olha a jornada: voo, fotogrametria, sensores, redes, painéis, BIM, segurança e dados."

### 5. Encerramento (3:10 – 3:50)

**[TELA]** Slides 17–19 — atividade, pontos-chave e encerramento da disciplina.

> "Começamos com uma pergunta: a obra está como deveria estar? Hoje você sabe responder com método. Medir, comparar, decidir, agir e medir de novo — protegendo quem trabalha e respeitando quem é medido. Foi um prazer fazer esta jornada com você. Leve isso para a obra — e boa sorte na carreira!"

---

## Quiz não avaliativo

### Questão 1

Um inclinômetro tem nível de atenção em $10\,\mathrm{mm}$. Suas leituras oscilam com ruído de cerca de $\pm 0{,}3\,\mathrm{mm}$ em torno desse valor (9,8; 10,1; 9,9; 10,2; 9,9; 10,1 mm), e a equipe recebe uma notificação a cada cruzamento. Assinale a alternativa **correta**:

- [ ] a. A solução é elevar o nível de atenção para 12 mm, pois limites próximos das leituras atuais sempre geram alarmes falsos.
- [ ] b. A solução é desligar as notificações de atenção e manter apenas as de alarme, que são as únicas que exigem ação.
- [x] c. Uma histerese (entrar em 10,0 mm e sair só abaixo de 9,5 mm), somada a um período de persistência, reduz as notificações a uma só, sem alterar o limite de projeto.
- [ ] d. O problema é do Grafana, que não consegue representar limites; é preciso trocar a ferramenta de painel.

**Resposta correta:** `c`

**Feedback:** A alternativa (c) está correta: com histerese de 0,5 mm, o sensor entra em atenção na leitura de 10,1 mm e só sai abaixo de 9,5 mm, de modo que o ruído em torno do limite não faz o alerta "piscar"; a persistência (o *pending period* do Grafana) exige que a condição dure antes de notificar. O limite continua o que o projeto definiu. A (a) muda o critério técnico para esconder um problema de ruído — o limite vem do projeto, não do incômodo. A (b) elimina o nível que serve justamente para agir **antes** do alarme. A (d) está errada: o Grafana representa limites (*thresholds*) e regras de alerta com período pendente; o problema é a configuração da regra.

### Questão 2

Uma construtora quer usar câmeras com **reconhecimento facial** em todas as frentes para identificar quem está sem capacete e aplicar advertências automáticas. Considerando a NR-18 e a LGPD, assinale a alternativa **correta**:

- [ ] a. Como a finalidade é a segurança do trabalho, a LGPD não se aplica às imagens dos trabalhadores dentro do canteiro.
- [x] b. Reconhecimento facial trata dado biométrico, sensível; como existe alternativa menos invasiva — detectar o capacete sem identificar a pessoa e alertar o encarregado —, os princípios da necessidade e da finalidade apontam para ela.
- [ ] c. O uso de câmeras com IA dispensa a proteção coletiva exigida pela NR-18, pois o risco passa a ser controlado pela detecção automática.
- [ ] d. Basta colher o consentimento dos trabalhadores na admissão, que é sempre a base legal mais adequada na relação de emprego.

**Resposta correta:** `b`

**Feedback:** A alternativa (b) está correta: biometria é dado sensível (art. 5º, II, da LGPD), e os princípios da finalidade e da necessidade (art. 6º) pedem o mínimo de dados para o objetivo; detectar o EPI sem identificar a pessoa atinge a finalidade de segurança com muito menos risco. A (a) está errada: a LGPD se aplica a qualquer tratamento de dado pessoal, inclusive no ambiente de trabalho. A (c) inverte a hierarquia das medidas: a NR-01 e a NR-18 põem a proteção coletiva antes, e a tecnologia apenas verifica. A (d) ignora que, na relação de emprego, o consentimento é frágil, pois o trabalhador dificilmente se sente livre para recusar.

---

## Material complementar

### Direto da fonte — livro da Biblioteca Virtual

> _[PENDENTE — aguardando acesso à Biblioteca Virtual]_

- **Nome do livro:** 
- **Capítulo:** 
- **Link de acesso (BV):** 
- **Qual aula o material deverá entrar?** 

### Para mergulhar no assunto

> Recomendo o webinar **"Digitalização BIM da SE Mirueira II: Scan-to-BIM e Gêmeos Digitais"**, do canal do BIM Fórum Brasil, no YouTube. Ele mostra um caso brasileiro real de captura da realidade de uma subestação de energia, da nuvem de pontos ao modelo BIM e ao gêmeo digital. Assista com o olhar da Aula 14: como a nuvem foi registrada? Que informação ficou presa a cada elemento? O resultado é modelo, sombra ou gêmeo digital? Para conferir o enquadramento legal do BIM nas obras públicas, complemente com a página da Estratégia BIM BR, do MDIC.

- **Links:** https://www.youtube.com/watch?v=QFRG0KoirtI · https://www.gov.br/mdic/pt-br/assuntos/sdic/building-information-modelling-bim
- **Qual aula o material deverá entrar?** Aula 14

### Podcast (curadoria, até 45 min)

> No episódio 47 do **Podcast Em Construção**, o professor Fabiano Corrêa (USP) e a professora Tatiana Amaral (UFG) discutem as **aplicações dos gêmeos digitais na construção civil** — desafios e oportunidades para engenheiros, arquitetos e gestores. Retoma a distinção entre modelo, sombra e gêmeo digital à luz da integração de BIM, sensores, painéis e planejamento desta unidade. O episódio tem cerca de 49 minutos; para esta curadoria, ouça os **primeiros 45 minutos**.

- **NOME DO PODCAST:** Podcast Em Construção (canal no YouTube)
- **NOME DO EPISÓDIO:** Episódio 47 — Aplicações dos gêmeos digitais na construção civil, com Fabiano Corrêa
- **Link:** https://www.youtube.com/watch?v=ww_-U1D9NFE
- **Qual aula o material deverá entrar?** Aulas 13 e 14

### Artigo científico

> Artigo de acesso aberto que propõe o **gêmeo digital da construção** como sistema de informação: o modelo do produto e do processo (BIM e cronograma) é alimentado continuamente por dados de monitoramento (drones, sensores, câmeras), e a comparação entre o planejado e o executado orienta o **planejamento e controle** da obra em ciclos fechados. É a fundamentação acadêmica das Aulas 13 e 14 e da ideia de malha fechada que atravessa toda a disciplina.

- **Link:** https://doi.org/10.1017/dce.2020.16
- **Qual aula o material deverá entrar?** Aulas 13 e 14
- **Referência bibliográfica do artigo no formato ABNT:**
  > SACKS, Rafael; BRILAKIS, Ioannis; PIKAS, Ergo; XIE, Haiyan Sally; GIROLAMI, Mark. Construction with digital twin information systems. **Data-Centric Engineering**, v. 1, e14, 2020. DOI: 10.1017/dce.2020.16.
