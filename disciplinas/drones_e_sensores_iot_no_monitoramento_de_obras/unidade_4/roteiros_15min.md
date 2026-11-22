# Roteiros Estendidos (15–19 minutos) — Unidade 4: Painéis, Integração com BIM e Gestão de Riscos

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 13 a 16
- **Formato:** roteiro de narração **integral** — o texto em citação (>) é a fala completa. **Esta é a versão a gravar.** Duração-alvo: **15 a 19 minutos** por aula (cerca de 2.000 a 2.550 palavras faladas, a uns 135 palavras/min, já contando as pausas curtas das demonstrações). Os roteiros curtos de `unidade_4.md` são só um guia da sequência.

> **Como usar:** leia as falas em citação na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`), na mesma ordem dos slides. Quando a fala manda clicar, o efeito descrito aparece na tela em poucos segundos; tabelas e listas dos slides **não** são lidas item a item: a fala comenta o essencial e o aluno lê o resto na tela.

---

## Roteiro da Videoaula 13 — "37 alarmes num fim de semana: por que a equipe parou de ouvir o painel?"

**Aula 13 — Painéis de monitoramento, alertas e limites de alarme**

**Duração-alvo:** cerca de 16:10 (15 a 19 minutos).

### 1. Abertura (0:00 – 2:00)

**[TELA]** Slide 1 — capa; Slide 2 — sumário da aula; Slide 3 — o que você verá nesta unidade.

> "Olá! Eu sou o professor Afonso Brandão, e seja muito bem-vindo, muito bem-vinda à Unidade 4, a última da disciplina Drones e Sensores IoT no Monitoramento de Obras. Até aqui, você planejou o voo, processou as imagens, instalou sensores e fez as leituras chegarem por MQTT a um banco de séries temporais. Agora o dado precisa virar decisão. Nesta unidade, a gente vai montar painéis e alertas, integrar drones e sensores ao BIM e ao planejamento da obra, usar a tecnologia a favor da segurança do trabalho, com a NR-18, e, para fechar, proteger o sistema e as pessoas, com LGPD e cibersegurança. Quatro aulas, um mesmo fio: transformar medição em ação."

**[TELA]** Slide 4 — segunda-feira, 7h: 37 alarmes no fim de semana.

> "E eu começo com uma cena que acontece mais do que se imagina. Segunda-feira, sete da manhã. A obra tem sessenta sensores e gera milhares de leituras por dia. No fim de semana, o painel disparou 37 alarmes. O engenheiro de plantão foi acordado várias vezes. Na segunda, a equipe analisa: 35 eram falsos. Um pico de interferência de rádio, um sensor com bateria fraca mandando lixo, o sol da tarde batendo numa escora metálica e dilatando o aço. Na primeira semana, todo mundo corre. Na segunda semana, corre menos. Na terceira semana, a equipe passa a ignorar o celular à noite. E é exatamente aí que um dos alarmes é real. Esse fenômeno tem nome: fadiga de alarmes. Ele é bem conhecido em hospitais e na indústria de processo, e chega às obras junto com a IoT. Hoje você vai aprender a montar painéis que levam à decisão, e não ao cansaço."

### 2. Do banco de séries ao painel (2:00 – 4:30)

**[TELA]** Slide 5 — a pilha: sensor, MQTT, Node-RED, InfluxDB e Grafana.

> "Vamos lembrar onde paramos na Aula 12. O sensor mede, o datalogger ou o ESP32 publica a leitura por MQTT, o Node-RED trata e encaminha, e o InfluxDB guarda a série temporal. Falta a última camada: a visualização. E a ferramenta mais usada para isso, em obras e em muitos outros setores, é o Grafana. O Grafana é um software de código aberto que se conecta ao banco como uma fonte de dados, em inglês data source, faz a consulta de um intervalo de tempo e desenha painéis. Um conjunto de painéis forma um dashboard. Repare numa coisa importante: o Grafana não guarda o dado. Ele pergunta ao banco toda vez que a tela é atualizada. Por isso, a consulta precisa ser bem feita."

**[TELA]** Slide 6 — captura de um dashboard do Grafana e os quatro tipos de painel.

> "Olha na tela um dashboard típico do Grafana, com fundo escuro, números grandes no alto e gráficos de série temporal embaixo. Para o monitoramento de obras, quatro tipos de painel resolvem quase tudo. Primeiro, a série temporal: a curva de cada instrumento ao longo do tempo, com os limites desenhados como faixas coloridas — no Grafana, os thresholds. Segundo, o valor único ou o mostrador, o stat e o gauge: a última leitura, pintada de verde, amarelo, laranja ou vermelho. Terceiro, a linha do tempo de estados, a state timeline: em que horários cada sensor esteve em cada nível. E quarto, a planta ou o mapa: os instrumentos posicionados sobre a planta da obra, ou até sobre o ortomosaico que o drone gerou na Unidade 2, cada um colorido pelo seu estado."

> "Dois recursos fazem diferença. As variáveis de painel, como sensor ou frente de serviço, deixam você trocar de instrumento num menu, sem duplicar telas. E a agregação: um piezômetro lido a cada 15 minutos gera quase cem pontos por dia. Sessenta sensores, um ano, são milhões de pontos. O painel não precisa desenhar todos: a consulta pede média horária, máximo diário, e o dado bruto continua guardado no banco para quem precisar."

### 3. O que um bom painel mostra (4:30 – 6:20)

**[TELA]** Slide 7 — as três perguntas do painel operacional.

> "Agora, o que faz um painel ser bom? Eu uso um teste simples: em dez segundos, o painel precisa responder a três perguntas. Algo está fora do normal? Onde? E está piorando? Se o engenheiro precisa abrir cinco abas e fazer conta de cabeça para responder, o painel falhou. Para responder às três, ele mostra a planta com o status de cada instrumento, as séries com os limites desenhados e a velocidade — em milímetros por dia, por exemplo —, e uma lista de alertas com reconhecimento: quem viu, quando viu e o que fez."

**[TELA]** Slide 8 — o sensor mudo: saúde dos instrumentos.

> "E tem um item que quase todo painel esquece: a saúde dos sensores. Bateria, intensidade do sinal e, principalmente, a hora da última leitura. Pense no inclinômetro que parou de mandar dados ontem à tarde. Se o painel mostra a última leitura recebida, ele continua verde. Só que ninguém sabe o que está acontecendo com aquela parede. Sensor mudo não é sensor verde. É um estado desconhecido, e precisa de alerta próprio. Às vezes, o sensor parou justamente porque a estrutura se moveu e rompeu o cabo."

> "Um último cuidado sobre o público. O painel operacional, o da equipe de instrumentação, é detalhado e em tempo real. O painel gerencial, da diretoria, resume tendências, pendências e indicadores de avanço — a gente vai ver esses indicadores na próxima aula. E evite os vícios clássicos: gráfico sem limite desenhado, eixo cortado que transforma meio milímetro numa montanha, arco-íris de cores e, o pior de todos, alerta sem dono."

### 4. Limites de atenção, alerta e alarme (6:20 – 8:00)

**[TELA]** Slide 9 — de onde vêm os limites; os três níveis.

> "Vamos falar dos limites. Primeiro, de onde eles vêm. Não é o painel que inventa o limite. Ele vem do projeto: o projetista calculou quanto a cortina pode deslocar, quanto o edifício vizinho pode recalcar, que esforço o tirante aguenta. Vem também de normas, da retroanálise de obras parecidas e da sensibilidade de quem está ao lado — um casarão tombado tolera muito menos que um galpão novo. Com esse valor admissível na mão, a prática é escalonar três níveis acima do normal. Atenção: o comportamento saiu do esperado, mas está longe do limite. Alerta: aproxima-se do admissível, e as medidas preventivas entram em curso. Alarme: chegou ao valor que exige intervenção imediata, ainda com margem em relação ao estado-limite. A ideia é que cada degrau dê tempo para o próximo."

**[TELA]** Slide 10 — foto: os prédios inclinados de Santos.

> "E cada nível se define por valor e por velocidade. Olha essa foto: é um dos prédios inclinados da orla de Santos, no litoral paulista. São edifícios com fundação rasa sobre camadas de argila mole, que recalcaram de forma diferencial ao longo de décadas. O recalque diferencial é lento. Uma leitura isolada não diz quase nada; é a série longa, com limites claros, que mostra a tendência. E repare: um recalque pequeno que está acelerando preocupa mais do que um recalque grande que já estabilizou. Por isso o nível de atenção tem dois gatilhos: um valor, em milímetros, e uma velocidade, em milímetros por dia."

### 5. O plano de ação por gatilhos (8:00 – 9:20)

**[TELA]** Slide 11 — a tabela TARP: nível, gatilho, ação, quem e prazo.

> "Agora a frase mais importante da aula: limite sem ação é enfeite. Os níveis se organizam num plano de ação por gatilhos, em inglês trigger action response plan, o TARP. Ele é um anexo do plano de monitoramento, e diz, para cada nível, o que acontece, quem faz e em quanto tempo. Olha o exemplo na tela, para o topo de uma cortina de contenção, com valores ilustrativos. Verde, abaixo de 10 milímetros e menos de meio milímetro por dia: rotina. Amarelo, atenção, a partir de 10 milímetros ou de meio milímetro por dia: aumentar a frequência de leitura, inspecionar e avisar o projetista, no mesmo dia. Laranja, alerta, a partir de 14 milímetros ou de um milímetro por dia: preparar e iniciar o reforço previsto e restringir a frente, em 24 horas. Vermelho, alarme, 18 milímetros: paralisar a escavação na frente, executar a contingência e isolar a área, imediatamente, sob o responsável técnico."

> "Repare que cada linha tem um nome e um prazo. Quando o alerta chega às três da manhã, ninguém precisa decidir quem liga para quem: está escrito."

### 6. Fadiga de alarmes: persistência, histerese e incerteza (9:20 – 11:40)

**[TELA]** Slide 12 — o princípio da gestão de alarmes: todo alarme exige uma ação.

> "Voltemos aos 37 alarmes. A indústria de processo, as refinarias e as plantas químicas, enfrentou esse problema há décadas e criou normas de gestão de alarmes, como a ANSI/ISA-18.2, equivalente à IEC 62682. O princípio central serve direitinho para a obra: todo alarme deve exigir uma ação. Se não exige, é ruído e deve sair. Com esse princípio, quatro técnicas resolvem a maior parte dos falsos alarmes."

**[TELA]** Slide 13 — simulação: histerese ligada e desligada. Clique em "sem histerese" e depois em "com histerese".

> "A primeira é a persistência: exigir que a condição dure um tempo mínimo, ou duas leituras seguidas, antes de notificar. No Grafana, isso se chama pending period. A segunda é a histerese, e olha a simulação. O inclinômetro oscila em torno de 10 milímetros, com um ruído de uns três décimos: 9,8; 10,1; 9,9; 10,2; 9,9; 10,1. Sem histerese, clico aqui: cada vez que a leitura cruza os 10 para cima, sai uma notificação de alerta, e cada vez que volta para baixo, outra de normalização. Alertas nas leituras 2, 4 e 6; normalizações nas leituras 3 e 5. Três alertas e duas normalizações: cinco notificações em seis leituras. O celular do engenheiro não para. Agora clico em com histerese: o nível entra em 10,0, mas só sai abaixo de 9,5. Olha a diferença: o sensor entra em atenção na leitura de 10,1 e fica em atenção. Uma notificação só. E repare que o limite do projeto não mudou: mudou só a regra de saída."

> "A terceira técnica é a confirmação: antes do alarme máximo, um segundo instrumento ou uma leitura manual confirma. E a quarta é a incerteza, a mesma regra de decisão da Aula 8, aplicada aos sensores da Aula 9. Se a leitura mais a incerteza alcança o limite, trate como atenção; se a leitura menos a incerteza já passou do limite, o nível está confirmado. E não se esqueça da limpeza da série, da Aula 12: um pico espúrio que sobe seis milímetros e volta no dia seguinte não pode acordar ninguém."

### 7. Alertas no Grafana (11:40 – 13:20)

**[TELA]** Slide 14 — anatomia de uma regra de alerta no Grafana.

> "Como isso se configura na prática? No Grafana Alerting, uma regra de alerta tem cinco partes. A consulta: por exemplo, o máximo dos últimos 15 minutos do inclinômetro I-2. A condição: acima de 14 milímetros. O intervalo de avaliação: a cada minuto, digamos. O período pendente: a condição tem de se manter, por exemplo, por 30 minutos. E os rótulos, como severidade igual a alerta e frente igual a cortina norte. São os rótulos que, pelas políticas de notificação, levam a mensagem ao ponto de contato certo: o e-mail da equipe, um aplicativo de mensagens, um SMS, o telefone de plantão. E existe o silenciamento, para manutenção programada — sempre com hora para acabar, senão vira esquecimento."

**[TELA]** Slide 15 — foto: sala de controle do Centro de Operações Rio; a regra crítica na borda.

> "Olha essa sala de controle, do Centro de Operações do Rio, com a parede de telas. É bonito, mas não se iluda: a tela não salva ninguém sozinha. Dois cuidados. Primeiro, a regra crítica — por exemplo, ligar a bomba reserva se o nível d'água subir — roda também na borda, no controlador do canteiro ou no Node-RED junto ao gateway, como você viu nas Aulas 10 e 12. O painel depende da internet; a bomba não pode depender. Segundo, o sistema precisa avisar quando para de receber dados. No Grafana, há tratamento para ausência de dados na regra. Configure isso; é o seu alerta de sensor mudo."

### 8. Exemplo numérico (13:20 – 14:40)

**[TELA]** Slide 16 — calculadora: velocidade e tempo até o próximo nível.

> "Vamos às contas. O inclinômetro I-2 está em 11,5 milímetros e sobe 1,2 milímetro por dia. Pelo valor, ele está em atenção, entre 10 e 14. Pela velocidade, 1,2 é maior que 1: ele já está em alerta. Quanto tempo até o alerta por valor? Quatorze menos 11,5 dá 2,5, dividido por 1,2: uns 2,1 dias. E até o alarme? Dezoito menos 11,5 dá 6,5, dividido por 1,2: 5,4 dias. Conclusão: pela velocidade, o I-2 já está em alerta, e o reforço é preparado agora, e a frequência de leitura passa para a cada seis horas. Mexo aqui na velocidade: se ela cair para 0,3, a previsão se alonga, e o nível volta a ser só atenção. É a velocidade que manda."

> "E a última conta, a dos 37 alarmes. Dois eram verdadeiros. Dois divididos por 37 dá 0,054: 5,4% dos alarmes exigiam ação. Em 19 de cada 20 vezes, o alarme era ruído. É a receita da fadiga. E são exatamente esses 35 que a persistência, a histerese e o alerta de saúde do sensor eliminam."

### 9. Atividade e encerramento (14:40 – 16:00)

**[TELA]** Slide 17 — atividade prática no Grafana.

> "A atividade de hoje é mão na massa. Abra o Grafana, instalado no seu computador ou na demonstração pública, em play.grafana.org. Monte um dashboard com três painéis: uma série temporal de um sensor, que pode ser simulado ou vir do InfluxDB da Aula 12, com as faixas de atenção, alerta e alarme; um painel de valor colorido pelo nível; e um painel com a hora da última leitura. Depois, crie uma regra de alerta com período pendente e escreva a linha do TARP correspondente: gatilho, ação, responsável e prazo."

**[TELA]** Slide 18 — pontos-chave.

> "Recapitulando: o Grafana consulta o banco de séries e mostra séries com limites, valor atual, estados e a planta. Os limites vêm do projeto, em atenção, alerta e alarme, por valor e por velocidade. O TARP dá a cada nível uma ação, um dono e um prazo. Persistência, histerese, confirmação e incerteza combatem a fadiga de alarmes, e sensor mudo também é alarme. E a regra crítica roda na borda."

**[TELA]** Slide 19 — encerramento.

> "Mas o painel mostra o sensor. E o cronograma, o orçamento, o modelo da obra? Na próxima aula, a gente pendura drones e sensores no BIM e no planejamento e controle. Te espero na Aula 14!"

---

## Roteiro da Videoaula 14 — "O drone diz 41%, a planilha diz 62%: quem está certo?"

**Aula 14 — Integração dos dados com BIM e com o planejamento e controle de obras**

**Duração-alvo:** cerca de 15:30 (15 a 19 minutos).

### 1. Abertura (0:00 – 1:20)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e seja bem-vindo, bem-vinda à Aula 14. Na aula passada, o painel transformou leituras em alertas com dono. Hoje a gente sobe um degrau: vai ligar o que os drones e os sensores medem ao modelo da obra e ao planejamento e controle — o cronograma, a medição de avanço, a curva S e o custo."

**[TELA]** Slide 3 — foto: "avanço físico de 62%, conforme o cronograma".

> "A cena é esta. Reunião mensal de obra. A gerenciadora projeta a planilha e anuncia: avanço físico de 62%, conforme o cronograma. Todo mundo concorda com a cabeça. Só que o drone voou ontem, a nuvem de pontos está pronta, e os sensores mandam leitura a cada 15 minutos. O problema é que cada dado mora num sistema diferente: o drone numa pasta, os sensores numa plataforma, o cronograma numa planilha e o projeto num arquivo que ninguém abre na reunião. E ninguém consegue responder a duas perguntas simples. O que foi construído é o que deveria estar pronto nesta data? E quanto isso custou, comparado ao que foi feito? No fim desta aula, você vai mostrar que aquele 62% não para em pé."

### 2. BIM: o modelo é informação (1:20 – 3:00)

**[TELA]** Slide 4 — CAD × BIM; foto de um modelo BIM.

> "Primeiro, desfazer uma confusão. Muita gente acha que BIM é desenho em 3D. Não é. BIM, de Building Information Modeling, é modelagem da informação da construção. A palavra mais importante é informação. No CAD, uma linha é uma linha: o software não sabe que aquilo é um pilar. No BIM, cada elemento é um objeto, com geometria, propriedades e relações. Aquele retângulo é o pilar P12, de concreto C35, concretado em 14 de março, que pertence ao terceiro pavimento e apoia a viga V20. É essa a definição que você encontra no Manual de BIM, de Eastman e colegas, um dos livros da nossa bibliografia. Olha o modelo na tela: telhado, fachadas, estacionamento. Cada peça ali sabe o que é."

**[TELA]** Slide 5 — openBIM, IFC, GUID, IfcSensor e IfcTask.

> "Numa obra real, cada equipe usa um software diferente. Como esses modelos conversam? Pelo openBIM, baseado no IFC, as Industry Foundation Classes. O IFC é um esquema aberto, mantido pela buildingSMART e normalizado como ISO 16739-1. Aberto quer dizer que não pertence a nenhum fabricante. E o detalhe que importa para a nossa disciplina: cada objeto do IFC tem um identificador global único, o GUID. É nesse identificador que a gente pendura tudo o que vem do canteiro. Existe até uma classe para instrumentos, o IfcSensor, e uma para atividades do cronograma, o IfcTask. Ou seja: o sensor e o cronograma cabem dentro do modelo."

### 3. 4D, 5D e a lei (3:00 – 4:40)

**[TELA]** Slide 6 — as dimensões do BIM.

> "Olha o quadro das chamadas dimensões do BIM. O 3D é o modelo com informação. Quando eu ligo cada elemento a uma atividade do cronograma, eu ganho o 4D: o modelo cresce no tempo. Eu arrasto uma data e vejo o que deveria estar pronto naquele dia. Quando eu ligo também quantidades e custos, chego ao 5D: orçamento, medição e fluxo de caixa extraídos do modelo. Depois do 5D, a numeração vira bagunça — cada autor chama o 6D de uma coisa. Não se prenda ao número. Importa o uso."

**[TELA]** Slide 7 — linha do tempo do Decreto nº 10.306/2020 e a ISO 19650.

> "E isso já é lei para muita obra no Brasil. O Decreto 9.983, de 2019, criou a Estratégia BIM BR. O Decreto 10.306, de 2020, tornou o BIM obrigatório, em fases, nas obras federais abrangidas. Desde 2021, nos projetos. Desde 2024 — e é essa a fase que nos interessa —, também na execução: orçamentação, planejamento e controle da obra e atualização do modelo as-built. A partir de 2028, na gestão e manutenção. E a Lei 14.133, de licitações, manda adotar o BIM preferencialmente sempre que adequado ao objeto. Para organizar tanta informação, a série ISO 19650 traz o ambiente comum de dados, o CDE: cada arquivo passa por estados — em elaboração, compartilhado, publicado, arquivado. Leitura de sensor e nuvem de pontos também são informação da obra: precisam de dono, versão e estado."

### 4. Do canteiro ao modelo: os três fluxos (4:40 – 6:20)

**[TELA]** Slide 8 — diagrama: drone, sensores e pendências chegando ao GUID.

> "Agora, a integração propriamente dita. São três fluxos chegando ao modelo. Primeiro fluxo: drone para modelo. A nuvem de pontos, já registrada nas coordenadas do projeto, como você viu na Aula 7, é comparada ao modelo, e a técnica dessa comparação você aprendeu na Aula 8. Aqui, a pergunta é de controle: quais elementos já existem? Cada elemento confirmado recebe uma data de execução. Segundo fluxo: sensores para modelo. O identificador de cada inclinômetro, piezômetro ou extensômetro da Aula 9 é associado ao GUID do elemento onde ele está. A partir daí, o painel da aula passada pinta o próprio modelo: a parede da cortina fica amarela quando o inclinômetro entra em atenção. Terceiro fluxo: pendências. Cada desvio, cada não conformidade, vira um tópico BCF, o BIM Collaboration Format, preso ao elemento, com responsável e prazo."

**[TELA]** Slide 9 — foto: scan-to-BIM de uma casa de máquinas (nuvem em cinza, tubos modelados em azul).

> "Olha essa imagem: a nuvem de pontos de uma casa de máquinas, em cinza, e as tubulações modeladas por cima, em azul. É assim que o capturado e o modelado se encontram. Um cuidado: o vínculo entre sensor e elemento também é informação gerida. Se o inclinômetro I-2 for associado por engano ao trecho errado da cortina, o modelo pinta de amarelo a parede que está bem e deixa verde a que está se mexendo. Esse vínculo tem dono, é conferido em campo e fica registrado no CDE."

### 5. O 4D e a medição de avanço físico (6:20 – 7:50)

**[TELA]** Slide 10 — o BIM 4D em 3D: arraste a semana.

> "Vamos ver o 4D funcionando. Na tela, um edifício. O contorno é o que o cronograma previa até a semana escolhida; o sólido é o que a nuvem confirmou como executado; e o vermelho é o que estava previsto e não foi feito. Arrasto da semana 22 até a 40: olha o vermelho crescendo. Na planilha, o atraso é um número. No 4D, você vê onde está, em que pavimento e desde quando."

**[TELA]** Slide 11 — foto aérea: conjunto residencial em construção; avanço físico ponderado.

> "E como se mede o avanço físico? Olha essa vista de drone de um conjunto residencial: blocos em estágios diferentes. Dá para contar quantos estão com cobertura, quantos só com estrutura. Mas atenção: serviços diferentes não se somam. Não dá para somar metro cúbico de concreto com metro quadrado de alvenaria. Por isso, cada serviço recebe um peso, em geral a sua participação no orçamento, como ensina o Mattos no Planejamento e controle de obras, outro livro da nossa bibliografia. O avanço global é a média ponderada. E aqui está a mudança: o modelo dá as quantidades previstas, e o drone, a nuvem e as câmeras dão as quantidades executadas. A medição sai do campo, não da planilha preenchida de memória."

### 6. Curva S e valor agregado (7:50 – 9:20)

**[TELA]** Slide 12 — curva S prevista e realizada.

> "Na Aula 1, você conheceu a curva S: o avanço acumulado previsto ao longo do tempo, que começa devagar, acelera no meio da obra e desacelera no fim. Com a medição de campo, a gente desenha a curva realizada ao lado da prevista. Se a realizada fica abaixo, a obra está atrasada. Mas atraso em prazo é só metade da história. Falta o custo."

**[TELA]** Slide 13 — valor planejado, valor agregado e custo real; IDP e IDC.

> "Para isso existe o gerenciamento do valor agregado, que compara três grandezas na mesma data. VP, valor planejado: o custo orçado do que deveria estar pronto. VA, valor agregado: o custo orçado do que foi executado de fato — é o avanço físico medido vezes o orçamento. E CR, custo real: o que efetivamente se gastou. Com elas, dois índices. IDP, índice de desempenho de prazo, igual a VA sobre VP. IDC, índice de desempenho de custo, igual a VA sobre CR. Abaixo de 1, o IDP diz que a obra está atrasada; abaixo de 1, o IDC diz que ela está gastando mais do que agrega. E repare onde entra a nossa disciplina: o VA depende do avanço físico. Se o avanço é chutado, o VA é chutado, e os índices também."

### 7. Exemplo numérico (9:20 – 11:00)

**[TELA]** Slide 14 — calculadora de avanço ponderado e valor agregado.

> "Vamos à conta. Obra de 20 milhões de reais. No mês 10, a curva S previa 45%. A medição deu o seguinte. Fundações, peso de 15%, 100% concluídas, conforme o as-built. Estrutura, peso de 45%: a nuvem confirma 2.250 de 4.500 metros cúbicos, ou seja, 50%. Alvenaria, peso de 25%, 10%, medida no ortomosaico. Instalações, peso de 15%, 5%, pela vistoria. Avanço físico: 0,15 vezes 1, mais 0,45 vezes 0,5, mais 0,25 vezes 0,1, mais 0,15 vezes 0,05. Dá 0,4075, uns 40,8%. Arredondando, 41%."

> "Agora o valor agregado. VP: 45% de 20 milhões, 9 milhões. VA: 40,75% de 20 milhões, 8,15 milhões. O custo real apurado foi de 8,6 milhões. IDP: 8,15 sobre 9, cerca de 0,91. A obra agregou 91% do que deveria: está atrasada. IDC: 8,15 sobre 8,6, cerca de 0,95. Está gastando 5% a mais do que agrega. Mantido esse desempenho, o custo final estimado é 20 milhões dividido por 0,95: uns 21,1 milhões. E o 4D mostra onde está o problema: a estrutura atrasada está puxando a alvenaria. Então, quem está certo, a planilha dos 62% ou o drone dos 41%? O drone, com o modelo e a medição rastreável. Mexo aqui no avanço da estrutura: se fosse 70%, o IDP passaria de 1. É o campo que decide."

### 8. A rotina de integração na obra (11:00 – 13:40)

**[TELA]** Slide 15 — a rotina semanal: voo, processamento, comparação, 4D e reunião.

> "Tudo isso parece bonito no slide, mas como vira rotina numa obra de verdade? Eu gosto de pensar numa semana típica. Segunda-feira de manhã, o drone voa a missão de sempre, com o mesmo plano de voo e os mesmos pontos de controle, para que um mês seja comparável com o outro. Segunda à tarde, as imagens são processadas e geram ortomosaico e nuvem de pontos. Terça, a nuvem é registrada nas coordenadas do projeto e comparada ao modelo: os elementos confirmados recebem a data de execução no 4D, e os desvios viram tópicos BCF. Ao mesmo tempo, as leituras dos sensores já estão chegando o tempo todo e pintando o modelo pelo nível de alerta. Quarta, o planejamento atualiza o avanço físico ponderado, o valor agregado e a curva S realizada. E quinta é a reunião de obra, que agora começa pelo painel, e não pela planilha."

> "Repare em três cuidados nessa rotina. Primeiro, a repetibilidade: se cada voo usa altura, sobreposição e pontos de controle diferentes, a comparação de um mês com o outro mistura mudança da obra com mudança do método. Segundo, a rastreabilidade: cada número do relatório precisa apontar para a fonte — qual voo, qual nuvem, qual versão do modelo, qual sensor —, e é o ambiente comum de dados que guarda essa trilha. Terceiro, a responsabilidade: o software sugere que um elemento foi executado, mas quem confirma a medição, que vai virar pagamento, é o engenheiro. Em contrato de obra pública, inclusive, a medição tem efeito financeiro, e o fiscal precisa conseguir refazer a conta."

> "E há uma vantagem que aparece logo nos primeiros meses: a discussão na reunião muda de natureza. Em vez de perguntar se a estrutura está em 60% ou em 50%, a equipe olha o 4D, vê quais pavimentos atrasaram e discute por quê: faltou fôrma? A grua ficou parada por vento? A concretagem esperou o resultado do ensaio? É o planejamento e controle do Mattos funcionando com dado de campo. E, quando o atraso aparece cedo, ainda dá tempo de reprogramar a sequência, reforçar a equipe ou renegociar o fornecimento, antes que ele vire multa contratual."

### 9. Do modelo ao gêmeo digital (13:40 – 14:20)

**[TELA]** Slide 16 — sombra digital e gêmeo digital: fechando a malha.

> "Uma última peça. Quando o modelo é atualizado automaticamente pelo canteiro — a nuvem confirmando elementos, os sensores pintando a cortina —, ele é uma sombra digital: o dado vai sozinho da obra para o modelo. Quando a decisão também volta automaticamente à obra — a plataforma reprograma a frente no 4D e aciona a equipe —, temos um gêmeo digital. Na prática da construção, o mais comum, e muito útil, é a sombra digital com um engenheiro fechando a malha da Aula 1: medir, comparar com o planejado, decidir, agir e medir de novo."

### 10. Atividade e encerramento (14:20 – 15:40)

**[TELA]** Slide 17 — atividade prática.

> "A atividade: pegue o cronograma de uma obra, pode ser acadêmico, com quatro ou cinco serviços e seus pesos. Para uma data, invente as quantidades que o drone e os sensores mediram. Calcule o avanço físico ponderado, o VP, o VA, um custo real plausível, o IDP e o IDC. Desenhe a curva S prevista e a realizada. E escreva o tópico BCF da frente mais atrasada: elemento, problema, responsável e prazo."

**[TELA]** Slide 18 — pontos-chave.

> "Recapitulando: BIM é modelo de informação, e o IFC com o GUID liga sensores, nuvens e pendências a cada elemento. 4D é modelo mais cronograma; 5D, mais custos; e, desde 2024, as obras federais abrangidas usam BIM no planejamento e controle. O avanço físico é ponderado; o modelo dá o previsto, e o campo dá o executado. Curva S e valor agregado transformam medição em decisão."

**[TELA]** Slide 19 — encerramento.

> "Agora, a obra não é só prazo e custo: é gente trabalhando em altura, ao lado de máquinas e sob a lança de uma grua. Na próxima aula, a NR-18 e a tecnologia a favor da segurança. Te espero na Aula 15!"

---

## Roteiro da Videoaula 15 — "Rajada de quase 47 km/h na grua: a tecnologia vê o risco antes do acidente?"

**Aula 15 — Segurança do trabalho, NR-18 e tecnologia para prevenção**

**Duração-alvo:** cerca de 15:20 (15 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e seja bem-vindo, bem-vinda à Aula 15. Até aqui, a gente monitorou a estrutura, o terreno, o prazo e o custo. Hoje o assunto é o mais importante de todos: as pessoas. Vamos falar de segurança do trabalho, da norma regulamentadora da construção, a NR-18, e de como drones, sensores e câmeras podem ajudar a prevenir acidentes — e também de onde estão os limites dessas tecnologias."

**[TELA]** Slide 3 — terça-feira, 10h: três riscos no mesmo canteiro.

> "Começo com uma manhã de terça-feira, dez horas. O anemômetro da grua marca rajadas de 13 metros por segundo. Só que o operador não tem esse número na cabine e continua içando fôrmas. Na rampa da escavação, um caminhão dá ré com o alarme sonoro desligado, porque a vizinhança reclamou do barulho, e passa a meio metro de um ajudante. E, no nono pavimento, falta um trecho de guarda-corpo, que alguém tirou para passar material e não recolocou. Nenhum desses riscos é novo. A NR-18 trata de todos eles. O que mudou é que hoje temos sensores, câmeras e drones capazes de ver o risco antes do acidente. A pergunta da aula é: como ligar a norma à tecnologia, sem achar que a tecnologia substitui a norma?"

### 2. A NR-18 hoje e o PGR (1:30 – 3:20)

**[TELA]** Slide 4 — a estrutura da NR-18 vigente.

> "A NR-18 se chama Segurança e Saúde no Trabalho na Indústria da Construção. Ela foi reformulada pela Portaria 3.733, de 2020, entrou em vigor em 2021 e recebeu alterações depois disso. O texto atual é bem mais enxuto que o antigo e está organizado por temas. Olha na tela: responsabilidades, o Programa de Gerenciamento de Riscos, áreas de vivência, instalações elétricas, etapas de obra, escadas e rampas, proteção contra quedas de altura, no item 18.9, máquinas, equipamentos e ferramentas, no 18.10, movimentação de materiais, andaimes, sinalização, no 18.13, e capacitação. Sempre confira o texto vigente no site do Ministério do Trabalho antes de citar um item, porque a norma continua recebendo ajustes."

**[TELA]** Slide 5 — o PGR do canteiro: itens 18.4.1 a 18.4.3.1.

> "O coração da norma é o PGR, o Programa de Gerenciamento de Riscos, que substituiu o antigo PCMAT. Ele é obrigatório nos canteiros e contempla os riscos ocupacionais e as respectivas medidas de prevenção. É elaborado por profissional legalmente habilitado em segurança do trabalho e implementado sob responsabilidade da organização. Além do que a NR-01 já exige, ele traz documentos como os projetos dos sistemas de proteção coletiva, os projetos dos sistemas de proteção individual contra quedas, quando aplicáveis, e a relação dos EPI. E aqui está o ponto que conversa com a nossa disciplina: o PGR deve estar atualizado de acordo com a etapa em que se encontra o canteiro. A obra muda toda semana. Um sistema de monitoramento é uma ótima forma de saber se o programa acompanha essa mudança."

### 3. Riscos críticos e a hierarquia das medidas (3:20 – 4:50)

**[TELA]** Slide 6 — a hierarquia: eliminar, proteção coletiva, administrativa, EPI.

> "Quais são os riscos mais graves num canteiro? Quedas de altura, soterramento em escavações, choque elétrico, atropelamento e esmagamento por máquinas e queda de materiais. E como se combate um risco? A NR-01 dá a ordem: primeiro, eliminar o risco; depois, adotar proteção coletiva; em seguida, medidas administrativas e de organização do trabalho; e, por último, o equipamento de proteção individual. O EPI é a última barreira, não a primeira."

**[TELA]** Slide 7 — foto: edifício envolvido por andaimes com tela de proteção; o guarda-corpo da NR-18.

> "Olha essa fachada envolvida por andaimes com tela de proteção: ela retém material e reduz a queda de objetos sobre a rua. É proteção coletiva. A NR-18 diz que a proteção coletiva é obrigatória onde houver risco de queda de trabalhadores ou de projeção de materiais, projetada por profissional habilitado. E, na periferia da edificação, desde os serviços da primeira laje. Quando é guarda-corpo, a norma fixa as dimensões: travessão superior a 1,2 metro, intermediário a 0,7 e rodapé de 15 centímetros. E trabalho acima de 2 metros com risco de queda segue também a NR-35. Guarde a frase do dia: a tecnologia entra dentro dessa hierarquia. Um sensor não substitui o guarda-corpo. Mas pode avisar quando ele sumiu."

### 4. A NR-18 já exige sensores (4:50 – 6:20)

**[TELA]** Slide 8 — máquinas: alarme de ré e limitador de carga.

> "E tem uma coisa curiosa: parte do que a norma exige já é sensoriamento. Máquinas autopropelidas, como retroescavadeiras e caminhões, devem ter retrovisores e alarme sonoro acoplado ao câmbio na marcha a ré. Está no item 18.10.1.6. Equipamentos de guindar têm limitador de carga ou de momento com alarme sonoro. Ou seja: o caminhão com alarme de ré desligado da nossa cena não é uma questão de vizinhança — é descumprimento da norma."

**[TELA]** Slide 9 — foto: grua no poço da edificação; o anemômetro e os limites de 42 e 72 km/h.

> "E a grua. Olha essa grua montada no poço de um edifício, com trabalhadores de capacete e colete ao lado. A NR-18 exige que a grua tenha anemômetro e um dispositivo automático com alarme sonoro que indique ventos acima de 42 quilômetros por hora. Acima desse valor, o trabalho tem de ser precedido de análise de risco específica e autorizado por permissão de trabalho. E acima de 72 quilômetros por hora, sob nenhuma condição a grua pode operar. Agora pense na nossa disciplina: esse anemômetro é um sensor. Se ele estiver ligado à plataforma IoT das Aulas 11 e 12, o vento deixa de ser um número só da cabine. Aparece no painel da Aula 13, com histórico, com previsão e com alerta ao encarregado e ao técnico de segurança."

### 5. Sensores vestíveis, gases e cercas virtuais (6:20 – 7:20)

**[TELA]** Slide 10 — simulação 3D: cerca virtual em torno da escavadeira. Clique para mover o trabalhador.

> "Outra frente é a localização em tempo real. Etiquetas UWB, com precisão de decímetros, ou BLE, de alguns metros, vão no capacete ou no crachá. Com elas, a gente cria cercas virtuais. Olha a simulação: em volta da escavadeira há uma zona de exclusão, a área de giro da máquina. Clico e o trabalhador se aproxima. Entrou na zona: o operador recebe um aviso na cabine, e o trabalhador, um alerta vibratório. Ninguém precisa ver o outro para que o aviso chegue. E, em escavações, poços e galerias, os detectores de gases avisam antes da entrada — é a NR-33, de espaços confinados. Somam-se ainda os sensores da Aula 9: inclinação em escoramentos, vibração e poeira. Só um lembrete, que vai ser o tema da próxima aula: localização de pessoa é dado pessoal."

### 6. Visão computacional: EPI e zonas de risco (7:20 – 9:00)

**[TELA]** Slide 11 — foto: caixa de referência e caixa prevista; a IoU.

> "Agora as câmeras. Com detecção de objetos, uma rede neural reconhece capacete, colete de alta visibilidade e pessoas dentro de zonas de risco desenhadas na imagem. O colete, aliás, é exigido pela NR-18 em áreas de movimentação de veículos e cargas. Como se mede se o detector acertou? Olha a imagem: a caixa verde é a referência, desenhada por uma pessoa; a vermelha, a prevista pelo modelo. A qualidade da caixa se mede pela IoU, a interseção sobre a união das duas áreas. Acima de 0,5, costuma contar como acerto."

**[TELA]** Slide 12 — precisão, revocação e o limiar.

> "E o modelo como um todo se avalia por duas métricas. Precisão: dos avisos que o modelo deu, quantos estavam certos? Revocação: das situações de risco que existiam, quantas o modelo encontrou? O modelo devolve uma probabilidade, e o limiar de decisão é escolha do engenheiro. Limiar baixo encontra mais situações de risco, com mais avisos falsos. Limiar alto, o contrário. Em segurança, o erro mais caro é o falso negativo: a pessoa sem capacete que passa despercebida. Por isso, ajusta-se o limiar para revocação alta, e os avisos são conferidos por uma pessoa. E um projeto ético detecta o EPI, não a pessoa. Sem reconhecimento facial, e, de preferência, processando na borda, sem mandar o vídeo inteiro para a nuvem."

### 7. Drones na inspeção de segurança (9:00 – 9:50)

**[TELA]** Slide 13 — foto: viaduto visto do drone durante inspeção.

> "E o drone? Ele inspeciona sem expor ninguém. Bandejas e redes de proteção, guarda-corpos da periferia, coberturas, taludes e escoramentos de escavação, ancoragens de andaimes. Olha essa vista de um viaduto durante uma inspeção: o drone chegou onde uma pessoa precisaria de cesto aéreo e cinto. Um voo semanal com fotos georreferenciadas vira evidência datada para o PGR: o guarda-corpo do nono pavimento estava lá na terça? E valem as regras das Aulas 3 e 4: operação segundo o RBAC 100 da ANAC, acesso ao espaço aéreo pelo DECEA, área de segurança delimitada e nada de sobrevoar trabalhadores sem a devida análise de risco. O drone que inspeciona a segurança não pode virar um risco."

### 8. Segurança no painel e no TARP (9:50 – 12:20)

**[TELA]** Slide 14 — o TARP de segurança: vento na grua, cercas virtuais e proteções inspecionadas.

> "Agora vamos juntar a segurança com o que você aprendeu na Aula 13. Os dados de segurança também entram no painel e também precisam de um plano de ação por gatilhos. Pense no vento da grua. A norma dá dois números: 42 e 72 quilômetros por hora. Mas o plano da obra pode, e deve, criar um degrau antes. Por exemplo, um nível de atenção em 30 quilômetros por hora, valor ilustrativo: o encarregado é avisado, os içamentos de peças de grande área, que pegam muito vento, são reprogramados, e a equipe acompanha a previsão. Em 42, o alerta: só se trabalha com análise de risco e permissão de trabalho. Em 72, o alarme: a grua para, na condição de repouso que o fabricante determina. Cada degrau tem um responsável e um prazo, exatamente como no TARP da cortina."

> "O mesmo raciocínio vale para as cercas virtuais e para as câmeras. Um evento isolado de pessoa na zona de giro da escavadeira gera aviso local, na hora. Mas, se a mesma frente acumula dez eventos por dia, o problema não é o trabalhador: é o layout do canteiro, a rota de pedestres ou o planejamento do serviço. Aí o alerta vai para o técnico de segurança e para o engenheiro, e a resposta é mudar a organização do trabalho. Repare como isso conversa com a hierarquia das medidas: a tecnologia mostra onde a proteção coletiva ou a organização estão falhando."

> "E há uma diferença de indicadores que vale guardar. A taxa de frequência de acidentes, que a gente vai calcular daqui a pouco, é um indicador de resultado: ela olha para trás e só se mexe depois que alguém se machuca. Os dados dos sensores, das câmeras e dos voos de inspeção são indicadores antecipados: quantos guarda-corpos faltando, quantas entradas em zona de risco, quantas horas de vento acima da atenção, quantos quase-acidentes registrados. Uma obra madura acompanha os dois. Os antecipados mostram o risco crescendo; o de resultado confirma se a prevenção funcionou."

### 9. Exemplo numérico (12:20 – 13:50)

**[TELA]** Slide 15 — calculadora: vento, detector e taxa de frequência.

> "Vamos às contas. Primeira: o vento. Rajada de 13 metros por segundo. Para passar para quilômetros por hora, multiplico por 3,6: 46,8, quase 47 quilômetros por hora. Acima de 42: precisa de análise de risco e permissão de trabalho. E o limite de 72 quilômetros por hora, dividido por 3,6, dá 20 metros por segundo: aí, proibido. O alerta da plataforma deve disparar nos 42, não depois."

> "Segunda: o detector de capacete. Em 400 imagens de teste, há 120 pessoas sem capacete. O modelo acertou 102, perdeu 18 e deu 34 avisos falsos. Precisão: 102 sobre 136, 0,75. Revocação: 102 sobre 120, 0,85. F1, perto de 0,80. Leitura: o modelo encontra 85% das situações de risco, e um em cada quatro avisos é falso. Ótimo para chamar o encarregado; nunca para punir alguém automaticamente."

> "Terceira: como medir se a obra está ficando mais segura. A NBR 14280 usa a taxa de frequência: número de acidentes vezes um milhão, dividido pelas horas-homem de exposição. Cento e oitenta trabalhadores, 220 horas por mês, 12 meses: 475.200 horas-homem. Quatro acidentes com afastamento: taxa de frequência de cerca de 8,4. É esse indicador, acompanhado mês a mês, que diz se a tecnologia está fazendo diferença."

### 10. Pausa para reflexão (13:50 – 14:40)

**[TELA]** Slide 16 — pausa para reflexão: prevenção ou vigilância?

> "Agora, pare o vídeo um instante e pense. A construtora quer câmeras com reconhecimento facial em todos os acessos e frentes, para identificar quem está sem capacete e aplicar advertências. O crachá UWB que evita o atropelamento na rampa também registra, minuto a minuto, onde cada trabalhador esteve. O objetivo, segurança, é legítimo. Mas existem alternativas menos invasivas: detectar o capacete sem identificar a pessoa e avisar o encarregado; calcular a proximidade com a máquina na borda, sem guardar o histórico com nome. Onde termina a prevenção e começa a vigilância? Pense na finalidade, na necessidade, na transparência, no prazo de guarda e em quem vai acessar as imagens."

### 11. Atividade e encerramento (14:40 – 15:40)

**[TELA]** Slide 17 — atividade prática.

> "A atividade: para uma obra que você conheça, liste cinco riscos críticos do PGR e, para cada um, indique a proteção coletiva exigida pela NR-18, uma tecnologia que ajude a verificá-la, com o gatilho de alerta, o responsável pela resposta e o cuidado de privacidade necessário."

**[TELA]** Slide 18 — pontos-chave.

> "Recapitulando: a NR-18 exige o PGR, atualizado conforme a etapa. A ordem é eliminar, proteger coletivamente, organizar e, por último, o EPI. A norma já pede sensores, como o alarme de ré e o anemômetro da grua, com 42 e 72 quilômetros por hora. Visão computacional detecta EPI com revocação alta e sem identificar pessoas. E o drone inspeciona sem expor ninguém."

**[TELA]** Slide 19 — encerramento.

> "Só que câmeras, crachás e sensores coletam dados de gente e abrem portas para invasores. Na última aula, LGPD, cibersegurança e o fechamento da disciplina. Te espero na Aula 16!"

---

## Roteiro da Videoaula 16 — "A senha do gateway era 'admin': o elo mais fraco do monitoramento"

**Aula 16 — Privacidade, LGPD e cibersegurança em sistemas IoT de obras (fechamento da disciplina)**

**Duração-alvo:** cerca de 15:40 (15 a 19 minutos).

### 1. Abertura (0:00 – 1:10)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e seja bem-vindo, bem-vinda à Aula 16, a última da disciplina. Hoje a gente fecha dois assuntos que costumam ficar para o fim e que, quando dão problema, param a obra: a proteção de dados pessoais, com a LGPD, e a cibersegurança dos sistemas IoT. E, no final, eu vou costurar com você as dezesseis aulas da disciplina."

**[TELA]** Slide 3 — as duas perguntas da reunião de aprovação.

> "A cena: o sistema de monitoramento está no ar. Sessenta sensores, um gateway LoRaWAN com 4G, câmeras com inteligência artificial nos acessos, voo semanal de drone e o painel no Grafana. Na reunião de aprovação, duas pessoas fazem as perguntas que faltavam. A advogada: podemos filmar os trabalhadores e a casa do vizinho? Por quanto tempo guardamos isso? E o gerente de TI: a senha do gateway ainda é a de fábrica? E se alguém alterar as leituras do inclinômetro? Um monitoramento que expõe pessoas ou aceita dado adulterado não protege ninguém. Vamos responder às duas."

### 2. LGPD: dado pessoal no canteiro (1:10 – 2:10)

**[TELA]** Slide 4 — foto: câmera de vigilância num poste; o que é dado pessoal.

> "A Lei Geral de Proteção de Dados, a Lei 13.709, de 2018, define dado pessoal como informação relacionada a pessoa natural identificada ou identificável. Identificável é a palavra-chave: não precisa ter o nome. No monitoramento de obras, isso inclui o rosto que aparece na foto do drone ou na câmera, a placa do caminhão, o quintal do vizinho, a localização do trabalhador com crachá UWB, o registro de entrada no canteiro e até o registro de quem acessou a plataforma. E há uma categoria especial: os dados sensíveis. Biometria, como o reconhecimento facial, e dados de saúde são sensíveis, com regras mais restritas. Olha essa câmera domo presa ao poste: ela gira, dá zoom e enxerga muito além do canteiro. Tudo o que ela vê, ela trata."

### 3. Bases legais, princípios e o trabalhador (2:10 – 3:20)

**[TELA]** Slide 5 — as bases legais do art. 7º e os princípios do art. 6º.

> "Para tratar dado pessoal, é preciso uma base legal, prevista no artigo 7º. As mais comuns no canteiro são: o cumprimento de obrigação legal — por exemplo, registros exigidos pelas normas de segurança —, a execução de contrato, a proteção da vida e da incolumidade física e o legítimo interesse. E um ponto que pega muita gente: na relação de emprego, o consentimento é frágil. O trabalhador dificilmente se sente livre para dizer não ao patrão. Por isso, o consentimento raramente é a melhor base no canteiro."

> "Além da base legal, todo tratamento respeita os princípios do artigo 6º. Quatro são essenciais aqui. Finalidade: para que serve o dado. Necessidade: o mínimo de dados para essa finalidade. Transparência: avisar quem é filmado e por quê. E segurança: proteger o dado. Um exemplo concreto: a câmera instalada para detectar capacete não pode virar, sem aviso, ferramenta para avaliar a produtividade de cada trabalhador. Mudou a finalidade, mudou tudo."

### 4. Privacidade desde a concepção e governança (3:20 – 5:10)

**[TELA]** Slide 6 — máscara de privacidade, desfoque e retenção. Clique para aplicar a máscara.

> "Na prática, o jeito certo é pensar em privacidade desde a concepção do sistema. Olha a simulação: a câmera enxerga o canteiro e as janelas do prédio vizinho. Clico e aplico a máscara de privacidade: as janelas ficam cobertas na gravação. Clico de novo e ligo o desfoque automático de rostos e placas. Somam-se a isso o enquadramento do voo do drone no canteiro, o prazo de guarda definido — a imagem de segurança fica guardada por um tempo certo e depois é apagada —, o aviso nos acessos e a comunicação prévia aos vizinhos. E o princípio da aula passada: detectar o EPI, não identificar a pessoa."

**[TELA]** Slide 7 — controlador, operador, encarregado, RIPD e a ANPD.

> "E a governança. O controlador é quem decide sobre o tratamento — em geral, a construtora. O operador trata em nome dele — a empresa de monitoramento contratada. O encarregado é o canal com os titulares e com a autoridade. Para tratamentos de risco, faz-se o relatório de impacto, o RIPD. Quem fiscaliza é a ANPD, a Autoridade Nacional de Proteção de Dados. Se houver um incidente de segurança com risco ou dano relevante aos titulares, ele deve ser comunicado à ANPD e aos titulares; pelo regulamento da ANPD, a Resolução 15, de 2024, em regra, em três dias úteis. E as sanções incluem multa de até 2% do faturamento, limitada a 50 milhões de reais por infração. E repare no artigo 46: os agentes de tratamento devem adotar medidas de segurança técnicas e administrativas. É exatamente aqui que a LGPD encontra a cibersegurança."

### 5. Por que um sistema IoT de obra é alvo (5:10 – 6:30)

**[TELA]** Slide 8 — confidencialidade, integridade e disponibilidade.

> "Segurança da informação protege três propriedades. Confidencialidade: só quem deve vê o dado. Integridade: o dado não foi alterado. Disponibilidade: o dado e o sistema estão lá quando a gente precisa. No monitoramento de obras, a mais crítica é a integridade. Pense comigo: uma leitura de inclinômetro adulterada pode esconder um recalque. Um alerta apagado pode atrasar uma evacuação. Na nossa disciplina, segurança da informação é questão de segurança estrutural."

**[TELA]** Slide 9 — foto: gateway LoRaWAN no alto de um mastro; a botnet Mirai.

> "E por que o IoT é alvo fácil? Olha esse gateway LoRaWAN no alto de um mastro, sobre a cidade. Ele fica exposto no campo, roda anos sem ninguém mexer, raramente é atualizado e, muitas vezes, sai de fábrica com usuário e senha padrão. Em 2016, uma rede de dispositivos sequestrados, a botnet Mirai, tomou o controle de centenas de milhares de câmeras e roteadores simplesmente testando senhas de fábrica, e usou esses aparelhos para derrubar grandes serviços da internet. Não à toa, senhas fracas, padrão ou embutidas aparecem em primeiro lugar na lista OWASP IoT Top 10, a referência de vulnerabilidades em internet das coisas."

### 6. Controles mínimos de cibersegurança (6:30 – 8:40)

**[TELA]** Slide 10 — credenciais únicas e o Ato nº 77/2021 da Anatel.

> "Então, quais são os controles mínimos? Primeiro, credenciais. Trocar toda senha de fábrica no comissionamento, uma credencial por dispositivo e autenticação forte na plataforma e no Grafana. Isso é tão importante que a Anatel, no Ato 77, de 2021, passou a exigir de roteadores e modems a troca da senha padrão e atualizações de segurança. Se a agência reguladora exige do roteador da sua casa, o gateway da obra não pode ficar atrás."

**[TELA]** Slide 11 — o caminho do dado: LoRaWAN com AES-128 e MQTT sobre TLS, com ACL por tópico.

> "Segundo, criptografia no caminho. Lembra da Aula 11? O LoRaWAN cifra as mensagens com chaves AES-128 entre o sensor e o servidor de rede. E o MQTT da Aula 12 deve rodar sobre TLS, na porta 8883, e não na 1883, em texto puro. Com TLS, quem intercepta a mensagem não lê nem altera o conteúdo. E mais: cada dispositivo se autentica com usuário e senha ou com certificado próprio, e o broker tem listas de controle de acesso por tópico. O inclinômetro I-2 só pode publicar em obra, barra cortina, barra I-2. Se alguém roubar a credencial dele, não consegue publicar em nome do piezômetro, nem apagar o tópico de alertas."

**[TELA]** Slide 12 — foto: switches num rack; a rede segmentada.

> "Terceiro, segmentação de rede. Olha esses switches no rack: é aqui que a rede se divide. Sensores, gateway e câmeras ficam numa rede separada, uma VLAN, isolada da rede administrativa do escritório da obra e, principalmente, do Wi-Fi dos visitantes. Um firewall libera só o tráfego necessário. Se um notebook infectado entrar no Wi-Fi, ele não alcança o broker. Quarto, firmware: inventário de dispositivos e versões, atualizações assinadas, de preferência remotas, as chamadas atualizações OTA, e substituição do aparelho que não recebe mais correções. E quinto, rastreabilidade: registro de acessos e de alterações, cópia de segurança das séries e conferência de lacunas e saltos estranhos."

### 7. Plano de resposta a incidentes e contrato (8:40 – 11:10)

**[TELA]** Slide 13 — as etapas da resposta a incidentes e as cláusulas do contrato de monitoramento.

> "Nenhum controle é perfeito. Por isso, além de prevenir, a obra precisa saber o que fazer quando algo dá errado. Um plano de resposta a incidentes tem etapas simples. Preparar: saber quem é acionado, ter as cópias de segurança e os contatos prontos. Detectar: perceber o problema, por exemplo, um acesso fora de hora registrado no log ou uma série com um salto impossível. Conter: isolar o gateway, bloquear a credencial, desligar o acesso externo. Erradicar e recuperar: corrigir a causa, trocar todas as senhas, atualizar o firmware, recompor as séries a partir das cópias, registrando cada correção. E, no fim, aprender: o que deixou a porta aberta e como fechá-la de vez. Em paralelo, avalia-se o risco aos titulares e, se for relevante, comunica-se a ANPD e as pessoas afetadas no prazo."

> "E onde isso tudo fica escrito? No contrato. O plano de monitoramento deve ser anexo do contrato, e não um extra. Do lado da proteção de dados, o contrato define quem é controlador e quem é operador, as instruções para o tratamento, a confidencialidade e o dever de avisar imediatamente o controlador sobre qualquer incidente. Do lado da segurança, os requisitos mínimos: troca de credenciais padrão, criptografia, segmentação, atualização de firmware, logs e cópias de segurança. Do lado do serviço, o nível de serviço, o SLA: disponibilidade da plataforma, tempo entre a leitura e o painel e prazo para reparar um sensor quebrado. Um SLA de 99,5% num mês de 30 dias admite 3,6 horas fora do ar; se a escavação é crítica, o contrato pede mais e exige a regra na borda."

> "E não esqueça a propriedade dos dados. As séries, as nuvens e as imagens são da obra, e o contrato deve garantir a entrega em formatos abertos, como CSV e IFC, no fim do serviço, além do prazo de guarda e do descarte do que não for mais necessário. Por fim, a responsabilidade técnica: o monitoramento tem um profissional responsável, com a respectiva ART. É assim que tecnologia, lei e engenharia se encontram num documento só."

### 8. Exemplo numérico (11:10 – 12:40)

**[TELA]** Slide 14 — calculadora de senhas, teto da multa e prazo do incidente.

> "Vamos às contas. Primeira, a senha do gateway. Uma senha numérica de seis dígitos tem um milhão de combinações. A cem tentativas por segundo, que é um ataque online, direto na tela de login do gateway, cai em no máximo dez mil segundos, umas 2,8 horas. Agora, uma senha aleatória de 12 caracteres, escolhidos entre 62 símbolos — maiúsculas, minúsculas e algarismos. São 62 elevado a 12, cerca de 3,2 vezes 10 elevado a 21 combinações. Mesmo num ataque offline, em que o invasor já roubou o arquivo com o hash da senha e testa com placa de vídeo a um bilhão de tentativas por segundo, seriam uns cem mil anos. E a senha de fábrica? Uma tentativa. Ela está no manual, que está na internet."

> "Segunda, o teto da multa. Até 2% do faturamento no Brasil no último exercício, limitada a 50 milhões por infração. Faturamento de 900 milhões: 2% dá 18 milhões. Faturamento de 3,5 bilhões: 2% daria 70 milhões, mas o teto limita a 50. Terceira, o prazo. A construtora descobre na quinta-feira que as imagens das câmeras foram expostas. Três dias úteis, sem feriados: sexta, segunda e terça. A comunicação à ANPD sai até terça-feira. E isso só é possível se o plano de resposta a incidentes já estiver escrito antes."

### 9. Encerramento da disciplina (12:40 – 14:20)

**[TELA]** Slide 15 — a jornada das quatro unidades.

> "E chegamos ao fechamento. Olha a jornada na tela. Na Unidade 1, os fundamentos: os indicadores de controle de avanço e a curva S, os tipos de drones e seus sensores, a regulamentação da ANAC, do DECEA e da Anatel e o planejamento de uma missão segura, com meteorologia e checklists. Na Unidade 2, o drone em ação: fotogrametria com sobreposição e pontos de controle, o GNSS e a precisão dos produtos, os ortomosaicos, os modelos de superfície e as nuvens de pontos, e os volumes e a comparação entre o projetado e o executado. Na Unidade 3, os sensores: inclinômetros, extensômetros, acelerômetros, temperatura, umidade e poeira, as plataformas embarcadas com Arduino e ESP32, as redes LoRaWAN, Wi-Fi e celulares e o MQTT com as séries temporais. E nesta unidade, a gestão: painéis e alertas, BIM e valor agregado, segurança do trabalho e, hoje, proteção de dados e cibersegurança."

**[TELA]** Slide 16 — foto: edifício em construção com grua; a malha fechada.

> "Se eu tivesse de resumir tudo numa ideia, seria a malha fechada. Medir, comparar com um limite, decidir, agir e medir de novo. O drone e o sensor medem. O painel e o BIM comparam. O TARP e o engenheiro decidem e agem. E tudo isso com segurança para quem trabalha e com respeito a quem é medido. Tecnologia nenhuma substitui o engenheiro que conhece o solo, a estrutura e a obra. Mas o engenheiro que domina essa tecnologia decide mais cedo, com mais confiança e com mais gente protegida."

### 10. Atividade e despedida (14:20 – 15:30)

**[TELA]** Slide 17 — atividade; Slide 18 — pontos-chave; Slide 19 — encerramento da disciplina.

> "A última atividade: para o sistema de monitoramento de uma obra que você escolher, monte uma ficha de privacidade e segurança, com o inventário de dados pessoais — o quê, de quem, base legal, finalidade, prazo de guarda e medida de minimização —, a arquitetura da rede com a segmentação e onde há TLS, cinco controles de cibersegurança com responsável e o fluxo de resposta a incidente até a comunicação à ANPD. Recapitulando: imagens, localização e acessos são dados pessoais; biometria é sensível. Todo tratamento precisa de base legal, finalidade, necessidade e transparência. Integridade do dado é segurança estrutural. Troque as credenciais padrão, use MQTT com TLS, segmente a rede e atualize o firmware."

> "Começamos esta disciplina com uma pergunta: a obra está como deveria estar? Hoje você sabe responder com método, com dado e com responsabilidade. Foi um prazer enorme fazer esta jornada com você. Leve isso para a obra — e boa sorte na carreira!"
