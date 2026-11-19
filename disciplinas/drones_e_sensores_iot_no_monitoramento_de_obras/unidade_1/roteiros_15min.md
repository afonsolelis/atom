# Roteiros Estendidos (17–19 minutos) — Unidade 1: Fundamentos do Monitoramento Digital de Obras

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 1 a 4
- **Formato:** roteiro de narração **integral** — o texto em citação (>) é a fala completa. **Esta é a versão a gravar.** Duração-alvo: **17 a 19 minutos** por aula (cerca de 2.150 a 2.550 palavras faladas, a uns 135 palavras/min, já contando as pausas curtas das demonstrações). Os roteiros curtos de `unidade_1.md` são só um guia da sequência.

> **Como usar:** leia as falas em citação na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`), na mesma ordem dos slides. Quando a fala manda clicar, o efeito descrito aparece na tela em poucos segundos; tabelas e listas dos slides **não** são lidas item a item: a fala comenta o essencial e o aluno lê o resto na tela.

---

## Roteiro da Videoaula 1 — "Monitoramento de obras na era digital: do diário de obra ao canteiro conectado"

**Duração-alvo:** cerca de 18:05 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:45)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e seja muito bem-vindo, muito bem-vinda à primeira aula da disciplina Drones e Sensores IoT no Monitoramento de Obras. IoT é a sigla em inglês para Internet das Coisas: objetos que medem e conversam com a rede sozinhos. Eu quero começar com uma cena que todo engenheiro de obra já viveu, ou vai viver. Segunda-feira, sete da manhã. Você ainda está no trânsito e o telefone toca. É o mestre de obras: 'Engenheiro, apareceu uma trinca na garagem do prédio vizinho'. A sua escavação para o subsolo está com seis metros de profundidade. E aí começam as perguntas: essa trinca é nova ou é antiga? Está crescendo? Tem alguma relação com a sua obra, ou o prédio já tinha esse problema antes de você chegar?"

**[TELA]** Slide 3 — foto: "Engenheiro, apareceu uma trinca na garagem do prédio vizinho."

> "Agora imagina que a única informação que você tem é uma anotação no diário de obra, de três semanas atrás, dizendo 'vistoria no vizinho, sem novidades'. Sem foto datada, sem medida, sem nada. Você está decidindo no escuro. Pode parar a escavação à toa e perder dias de cronograma — ou pode continuar escavando enquanto o prédio ao lado está se mexendo. Nesta aula, a gente vai entender por que e como se monitora uma obra, o que drones e sensores resolvem — e o que eles não resolvem — e dois conceitos que vão atravessar a disciplina inteira: a malha fechada e o gêmeo digital. Vamos nessa."

### 2. Por que monitorar uma obra? (1:45 – 3:40)

**[TELA]** Slide 4 — Por que monitorar: as quatro dimensões (prazo, custo, segurança, qualidade).

> "Primeiro, uma definição que eu quero que você leve para a vida profissional. Monitorar é medir de forma sistemática, ao longo do tempo, grandezas que indicam se a obra está se comportando como o projeto previu. Repara nas três ideias dentro dessa frase. 'Sistemática' quer dizer que tem método: sempre no mesmo ponto, do mesmo jeito, com o mesmo instrumento. 'Ao longo do tempo' quer dizer que uma leitura isolada vale pouco — o que conta é a tendência. E 'como o projeto previu' quer dizer que existe uma referência para comparar. Sem referência, você tem um número, não tem uma informação."

> "E por que a gente monitora? As razões cabem em quatro dimensões clássicas da gestão. Prazo: o avanço físico real comparado ao cronograma — quantos metros cúbicos foram escavados, quantos pavimentos foram concretados, quanto de fachada já foi executado. Custo: a medição de serviços para pagamento, o controle de perdas e de retrabalho. Segurança: das pessoas — quedas, interferência entre equipamentos — e das estruturas — recalques, deslocamento de contenções, nível d'água em escavações. E qualidade: conformidade geométrica, como prumo, nível e espessura, e desempenho dos materiais, como a temperatura do concreto nas primeiras horas."

> "Monitorar não é luxo: é a forma de transformar incerteza de projeto em informação de obra. O projeto de fundação partiu de alguns furos de sondagem, e o solo entre um furo e outro nunca é exatamente igual. O monitoramento é a obra respondendo ao projeto: a hipótese estava certa — ou não."

### 3. Do diário de obra ao canteiro conectado (3:40 – 5:35)

**[TELA]** Slide 5 — foto aérea das obras das estações Campo Belo do Metrô de São Paulo: as três fragilidades do jeito tradicional.

> "Como isso é feito tradicionalmente? Com o diário de obra, com vistorias visuais, com fotos de celular e com campanhas periódicas de topografia e de instrumentação lidas manualmente. Um técnico vai lá uma vez por semana, ou uma vez por mês, lê o instrumento, anota na planilha, e o dado vira relatório alguns dias depois. Isso funciona — muita obra boa foi feita assim. Mas tem três fragilidades. A primeira é a baixa frequência: a leitura é semanal ou mensal, e muita coisa pode acontecer entre duas leituras. A segunda é o atraso: o dado leva dias para virar relatório e chegar a quem decide. E a terceira é a subjetividade: cada vistoriador descreve do seu jeito. 'Fissura pequena' para um é 'trinca preocupante' para outro."

**[TELA]** Slide 6 — o canteiro conectado em 3D (gire a cena).

> "Agora olha a cena 3D na tela. Esse é o canteiro conectado. Repara na pessoa de 1,75 metro e no caminhão, perto da borda: eles dão a escala do canteiro. O drone sobrevoa o canteiro inteiro e, em um único voo, produz uma ortofoto — que é uma imagem aérea sem distorção, na escala certa — e um modelo 3D do terreno. Ao mesmo tempo, sensores instalados na contenção, nas fundações e na estrutura enviam as leituras sozinhos para uma plataforma na nuvem."

**[TELA]** Slide 7 — A mudança de escala: frequência, atraso e dado numérico.

> "Repara no que muda. A frequência sobe de mensal para horária, ou até mais. O atraso cai de dias para minutos. E o dado passa a ser quantitativo e rastreável: cada leitura tem data, hora, posição e instrumento de origem. Ninguém precisa interpretar o adjetivo do vistoriador — o número está lá."

### 4. O ciclo dado → informação → decisão → ação (5:35 – 7:05)

**[TELA]** Slide 8 — o ciclo dado → informação → decisão → ação, revelado passo a passo.

> "Só que aqui vem o primeiro alerta da disciplina: dado sozinho não salva obra nenhuma. Tem obra com dezenas de sensores em que, mesmo assim, o problema foi descoberto tarde. O valor não está no dado. Está no ciclo que o dado percorre. São quatro etapas."

> "Primeira: dado. A leitura bruta. 'O inclinômetro registrou 18 milímetros a 4 metros de profundidade.' Isso, sozinho, não diz se é bom ou ruim. Segunda: informação. É o dado comparado a uma referência. 'Esse deslocamento corresponde a 60% do limite de projeto e dobrou em uma semana.' Agora sim, eu entendo a situação: estou abaixo do limite, mas a velocidade preocupa. Terceira: decisão. É o julgamento técnico, feito por quem tem conhecimento e autoridade. 'Vamos reduzir a escavação na frente norte e instalar mais uma linha de tirantes.' E quarta: ação. A intervenção executada de fato no canteiro."

> "Guarda isso: toda a tecnologia desta disciplina — drone, sensor, rede, nuvem, inteligência artificial — serve para duas coisas. Encurtar esse ciclo, para que a ação aconteça a tempo. E torná-lo confiável, para que a decisão seja tomada com base em números em que dá para acreditar. Se a tecnologia não melhora nenhuma das duas coisas, ela é enfeite."

### 5. Malha aberta × malha fechada (7:05 – 9:25)

**[TELA]** Slide 9 — simulação malha aberta × malha fechada: deslocamento da contenção em 20 dias, atenção em 18 mm e alerta em 30 mm. A simulação já começa em Malha fechada; deixe rodar uns 15 segundos e só então clique em Malha aberta.

> "Agora vamos pegar emprestado um conceito da engenharia de controle, que é muito poderoso para pensar monitoramento. Existem dois jeitos de operar um sistema: em malha aberta e em malha fechada."

> "Em malha aberta, você mede e arquiva. A leitura vira relatório, o relatório vai para uma pasta, e ninguém compara aquele número com um limite a tempo de agir. O sensor está lá, mas o laço não fecha. Em malha fechada, a medição realimenta a execução. O ciclo é: medir, comparar com a referência ou com o limite, decidir, agir na obra — e medir de novo para confirmar o efeito."

> "A analogia clássica é o ar-condicionado. Um ventilador ligado no máximo é malha aberta: ele sopra do mesmo jeito, esteja a sala fria ou quente. Já o ar-condicionado com termostato mede a temperatura, compara com os 23 graus que você escolheu, decide se liga ou desliga o compressor, age — e mede de novo. É malha fechada."

> "Olha a simulação na tela. É o deslocamento da contenção ao longo de 20 dias, com o nível de atenção em 18 milímetros, que é 60% do limite, e o de alerta em 30. Ela começa em malha fechada: a leitura é automática; quando o deslocamento cruza a atenção, a equipe é avisada, decide-se pelos tirantes adicionais, os tirantes são executados — e repara no detalhe — as leituras seguintes mostram que a curva parou de subir e ficou na horizontal. Agora eu clico em malha aberta: a leitura manual é semanal, o número vai para o relatório, e quando alguém age a curva já passou do alerta. Esse último passo é o que muita gente esquece. Medir de novo é o que confirma a decisão. Se o deslocamento parou, o laço confirma. Se não parou, o laço dispara uma nova decisão. Na Aula 3, você vai ver como uma arquitetura IoT implementa esse laço de ponta a ponta."

### 6. Gêmeo digital: modelo, sombra e gêmeo (9:25 – 12:30)

**[TELA]** Slide 10 — Kritzinger et al. (2018): modelo, sombra ou gêmeo digital? A animação abre no primeiro nível, Modelo digital.

> "O segundo grande conceito é o gêmeo digital — em inglês, digital twin. O termo é muito usado de um jeito exagerado, como sinônimo de qualquer modelo 3D bonito. Então vamos à definição séria. Gêmeo digital é um modelo digital vinculado ao ativo físico por um fluxo de dados contínuo, que representa o estado atual da obra e permite simular e decidir sobre ela."

**[TELA]** Slide 10 — a animação já está em Modelo digital; clique em Sombra digital e depois em Gêmeo digital à medida que narra cada nível.

> "Para separar conceito de marketing, eu gosto muito de uma classificação proposta por Kritzinger e colegas, em 2018. Eles olham para uma coisa só: o grau de integração dos dados entre o físico e o digital. E chegam a três níveis."

> "Nível um: modelo digital. Não existe troca automática de dados entre o físico e o digital. Um modelo BIM — a modelagem da informação da construção — que alguém atualiza à mão, uma vez por semana, olhando as fotos da obra, é um modelo digital. Útil, mas desconectado. Nível dois: sombra digital. Aqui o dado flui automaticamente do físico para o digital — os sensores atualizam o modelo sozinhos —, mas a volta, do digital para o físico, depende de ação manual. E a palavra 'sombra' é perfeita: a sua sombra acompanha cada movimento seu, fielmente, mas ela não consegue fazer nada com você. Nível três: gêmeo digital. O fluxo é automático nos dois sentidos. O estado da obra atualiza o modelo, e o modelo devolve comandos ou decisões ao ativo."

**[TELA]** Slide 11 — gêmeo digital em 3D: clique em Simular recalque.

> "Agora repara na ligação entre os dois conceitos da aula. Um gêmeo digital, pela definição de Kritzinger, é uma malha fechada entre o canteiro e o modelo. Mede, compara, decide, age, mede de novo — só que de forma automática nos dois sentidos. Clico em simular recalque: o recalque aparece no modelo e o modelo devolve a ação à obra."

**[TELA]** Slide 12 — as peças de um gêmeo no mundo real: modelo BIM, nuvem de pontos, sensores embutidos e o painel de um centro de operações.

> "E quais são as peças de um gêmeo de verdade? Olha a tela: o modelo BIM, que sozinho é só modelo digital; a realidade capturada, a nuvem de pontos que vira modelo; os sensores embutidos antes da concretagem; e o painel, onde o dado vira informação, como neste centro de operações da cidade do Rio de Janeiro."

> "Uma dose de realismo: a maior parte dos sistemas de obra hoje é sombra digital. Os sensores alimentam a plataforma sozinhos, mas quem fecha o laço é um engenheiro, que lê o alerta e decide. Isso não é defeito; o problema é a sombra digital sem ninguém para fechar o laço — aí você volta à malha aberta, só que com gráficos mais caros."

### 7. O que drones e sensores resolvem — e o que não resolvem (12:30 – 13:50)

**[TELA]** Slide 13 — o que drones e sensores resolvem e o que não resolvem, com a foto da estação total robótica e do prisma.

> "Então vamos ser honestos sobre a tecnologia. Na tela estão as quatro coisas que drones e sensores resolvem; eu destaco duas. Acesso: fachadas e taludes inspecionados sem expor ninguém a altura ou a desmoronamento. E rastreabilidade: o dado datado e georreferenciado, que serve até como prova num conflito com o vizinho."

> "Mas eles não resolvem projeto mal feito. Não resolvem a ausência de limites de alerta definidos — se ninguém disse qual deslocamento é aceitável, o sensor não tem com o que comparar. Não resolvem sensor mal instalado ou nunca calibrado. E não resolvem a falta de alguém com autoridade para agir. Eu gosto de dizer assim: um sistema de monitoramento sem plano de resposta é só um gerador de gráficos bonitos."

> "E um recado sobre a topografia. Essa foto é de uma estação total com prisma. Ela não vai desaparecer por causa do drone. A topografia convencional, com estação total e GNSS — o posicionamento por satélite —, continua indispensável: é ela que fornece os pontos de controle e valida os produtos aéreos. Uma tecnologia complementa a outra."

### 8. Exemplo numérico: drone × levantamento convencional (13:50 – 15:55)

**[TELA]** Slide 14 — calculadora: levantamento mensal, convencional × drone (área inicial de 12 ha).

> "Vamos colocar números nisso, com valores ilustrativos — servem para treinar o raciocínio, não são tabela de preços. O cenário: um canteiro de terraplenagem com 12 hectares, que precisa de um levantamento planialtimétrico por mês para medir volumes."

> "Primeiro, o levantamento convencional, com estação total e GNSS. A produtividade de campo é de 3 hectares por dia, mais 1 dia de escritório para processar. O tempo é 12 dividido por 3, que dá 4 dias de campo, mais 1 de escritório: 5 dias. Com um custo de equipe de 2.400 reais por dia, são 5 vezes 2.400: 12 mil reais por levantamento."

> "Agora com drone: 1 dia de campo, incluindo a medição dos pontos de controle, mais 1 dia de processamento. São 2 dias. O custo diário de equipe e equipamento é maior, digamos 3.000 reais. Então 2 vezes 3.000: 6 mil reais por levantamento."

> "A economia é de 6 mil reais por medição; em 10 medições mensais, 60 mil reais. Mas o dinheiro não é o mais importante. Primeiro: o dado chega 3 dias antes a quem decide — e encurtar o ciclo é justamente o objetivo."

**[TELA]** Slide 15 — a densidade de informação muda de escala.

> "Segundo: a densidade da informação. O convencional entrega, digamos, 1 ponto a cada 100 metros quadrados — nos 12 hectares, cerca de 1.200 pontos. O drone gera uma nuvem com dezenas de pontos por metro quadrado. É a diferença entre desenhar o terreno com uma dúzia de traços e fotografá-lo."

> "E as ressalvas, que um bom engenheiro sempre faz. O drone não enxerga debaixo de vegetação densa, nem dentro de galerias. E a exatidão do levantamento com drone depende dos pontos de controle medidos em campo pela topografia. Por isso o convencional não morre: ele muda de papel."

### 9. Atividade prática + encerramento (15:55 – 18:05)

**[TELA]** Slide 16 — Atividade prática.

> "Sua missão até a próxima aula. Escolha uma obra que você conhece — pode ser uma obra pública noticiada na sua cidade, uma ponte, uma escola, um viaduto. Em uma folha, faça quatro coisas. Primeiro, liste três riscos dessa obra ligados a prazo, custo, segurança ou qualidade. Segundo, para cada risco, indique o que medir e se a medição seria por drone, por sensor ou por topografia convencional. Terceiro, para um dos riscos, descreva a malha fechada completa: o que se mede, qual é a referência ou o limite, qual decisão se toma e qual ação se executa. E quarto: classifique o sistema que você imaginou como modelo digital, sombra digital ou gêmeo digital, e justifique."

**[TELA]** Slide 17 — Pontos-chave; Slide 18 — encerramento e gancho para a Aula 2.

> "Vamos amarrar. Hoje você viu que monitorar é medir de forma sistemática, ao longo do tempo, para comparar a obra com o projeto, em prazo, custo, segurança e qualidade. Viu que o valor está no ciclo dado, informação, decisão e ação. Viu a diferença entre malha aberta, que mede e arquiva, e malha fechada, que mede, compara, decide, age e mede de novo. E viu que gêmeo digital, no sentido sério, é um fluxo automático nos dois sentidos — e que a maior parte do que existe hoje é sombra digital com um engenheiro fechando o laço."

> "Mas tem uma pergunta que vem antes de tudo isso. Lembra do inclinômetro com 18 milímetros? Dá para confiar nessa leitura? Qual é a incerteza dela? Se o limite é 30 e a leitura é 18, tudo bem — mas e se o limite fosse 19? É disso que a gente vai tratar na próxima aula: os fundamentos de sensoriamento, a metrologia que separa um dado confiável de um número qualquer. Te espero na Aula 2. Um abraço!"

---

## Roteiro da Videoaula 2 — "Fundamentos de sensoriamento: grandezas, transdutores, incerteza e calibração"

**Duração-alvo:** cerca de 18:40 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:25)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda de volta. Na aula passada, a gente viu que o valor do monitoramento está no ciclo que leva o dado até a ação. Hoje a gente vai olhar com lupa para o primeiro elo desse ciclo — o dado — e fazer a pergunta mais incômoda que existe em instrumentação: dá para confiar nele?"

**[TELA]** Slide 3 — foto do nível topográfico com o número em destaque: recalque de 9 mm no pilar P12, alerta em 10 mm.

> "Começo com uma situação. O sistema de monitoramento da sua obra acusa: o recalque do pilar P12 do prédio vizinho chegou a 9 milímetros. O nível de alerta, definido no projeto, é 10 milímetros. Você mobiliza a equipe ou espera a próxima leitura? Muita gente responderia: está abaixo de 10, tudo bem. Mas a resposta depende de uma pergunta que quase ninguém faz: qual é a incerteza desses 9 milímetros? Se a incerteza for de 0,2 milímetro para mais ou para menos, você está tranquilo, longe do alerta. Se for de 1,5 milímetro, o alerta pode já ter sido atingido. Mesmo número no painel, decisões completamente diferentes. Hoje a gente vai aprender a língua da metrologia — grandeza, transdutor, exatidão, precisão, incerteza e calibração. Sem essa língua, nenhum dado de sensor merece a sua confiança."

### 2. Grandezas e mensurandos (1:25 – 3:30)

**[TELA]** Slide 4 — tabela das quatro famílias de grandezas, com unidades e instrumentos, e o quadro do mensurando.

> "Toda medição começa pela grandeza que você quer conhecer. Na tela, as grandezas de obra estão em quatro famílias: geométricas, hidráulicas, mecânicas e térmicas, com as unidades e os instrumentos de cada uma. Dois destaques. Poropressão é a pressão da água nos poros do solo. E, na vibração, não confunda: o acelerômetro mede aceleração, em metros por segundo ao quadrado; a velocidade de vibração, em milímetros por segundo, que é o que as normas usam para avaliar danos em edificações, vem de um sismógrafo de engenharia, com geofones, ou da integração do sinal do acelerômetro."

> "Mas a grandeza ainda é genérica. O que você mede, de fato, é o mensurando: o valor específico que se deseja conhecer. Não é 'o recalque'. É 'o recalque do pilar P12 entre 1º e 15 de março'. E definir bem o mensurando é metade do trabalho. Recalque em relação a quê? A uma referência de nível que está fora da zona de influência da escavação — ou a uma que também está afundando junto? Medido onde? No pilar, na laje, no piso da garagem? Muita briga entre construtora e vizinho é só isso: cada lado medindo um mensurando diferente com o mesmo nome."

**[TELA]** Slide 5 — escavação instrumentada em 3D: clique nos botões para destacar cada instrumento.

> "Agora olha essa escavação em 3D, cortada ao meio. Cada instrumento mede uma grandeza diferente. No prédio vizinho, o marco de recalque, em milímetros, e o sismógrafo, que registra a velocidade de vibração em milímetros por segundo. No solo, atrás da contenção, o inclinômetro e o piezômetro. Na escora, o extensômetro, em microdeformações. Na laje de fundo, o termopar. E tudo chega ao datalogger. Repara: uma escavação, seis grandezas, seis mensurandos que precisam ser bem definidos."

### 3. Sensores, transdutores e o sinal elétrico (3:30 – 6:50)

**[TELA]** Slide 6 — galeria: extensômetro elétrico, corda vibrante, piezômetro de corda vibrante, roseta, MEMS e datalogger.

> "Agora, como a grandeza física vira número? Dois papéis aqui. O sensor é o elemento que responde à grandeza física. O transdutor converte essa resposta em um sinal mensurável, quase sempre elétrico. O exemplo clássico é este da foto: o extensômetro elétrico de resistência, o strain gauge. É uma grade metálica fininha, em zigue-zague, colada na peça. Quando a peça se deforma, a grade estica ou encurta junto, e a resistência elétrica dela muda. Medindo a resistência, eu sei a deformação."

> "Na instrumentação de obras, você vai encontrar muito quatro famílias. A primeira são os transdutores de corda vibrante. Pensa numa corda de violão: se você aperta a tarraxa, a nota fica mais aguda. No sensor é igual: um fio tensionado vibra numa frequência que muda com a deformação ou com a pressão. Lendo a frequência, eu leio a grandeza. São robustos e estáveis por anos — por isso são tão usados em piezômetros e em barragens. A segunda são os piezorresistivos, muito usados para pressão. A terceira são os MEMS, os microssistemas eletromecânicos: acelerômetros e inclinômetros dentro de um chip, os mesmos princípios do sensor que gira a tela do seu celular. E a quarta são os potenciômetros e os LVDT — transformadores diferenciais lineares, em que um núcleo metálico desliza dentro de bobinas —, para medir deslocamento."

> "O sinal costuma ser padronizado. Um padrão muito comum é o de 4 a 20 miliampères, em corrente. E tem um detalhe esperto nesse padrão: o zero da escala é 4 miliampères, não zero. Por quê? Porque se o cabo romper, a corrente vai a zero — e o sistema sabe que aquilo é falha, e não uma leitura legítima de zero. Esse sinal é lido por um datalogger, que é o equipamento que registra as leituras e as entrega à rede. Sensor responde, transdutor converte, datalogger registra e transmite."

**[TELA]** Slide 7 — por dentro do transdutor: a viga deforma, o extensômetro alonga e a ponte de Wheatstone mede (leve o controle de deformação até 1.000 με).

> "Voltando ao extensômetro: como uma variação minúscula de resistência vira número? Olha a animação; eu aumento a deformação. A viga flete, a grade colada na face de baixo se alonga e a resistência sobe um pouquinho. Essa variação é tão pequena que ninguém mede direto: o extensômetro entra numa ponte de Wheatstone, quatro resistores equilibrados. Quando um deles muda, a ponte desequilibra e aparece uma tensão de saída de alguns milivolts. É esse sinal que o datalogger lê."

**[TELA]** Slide 8 — escala: unidade inercial sobre uma moeda, viga de ponte de dezenas de metros e os números da proporção.

> "E para ter dimensão: a grade de um extensômetro tem uns 6 milímetros e vai numa viga de 6 metros, uma proporção de 1 para 1.000. Com 500 microdeformações, ela alonga só 3 micrômetros, umas vinte e poucas vezes menos que a espessura de um fio de cabelo, como mostra a conta no slide. É com sensores desse tamanho que a gente vigia estruturas de dezenas de metros."

### 4. Características estáticas: faixa, resolução, sensibilidade (6:50 – 8:00)

**[TELA]** Slide 9 — as características estáticas, com um exemplo em cada uma (sensibilidade: 0,08 mA/kPa).

> "Toda ficha técnica de sensor traz as características da tela, cada uma com um exemplo. Eu comento três. Sensibilidade: a razão entre a variação da saída e a da entrada. No piezômetro de 4 a 20 miliampères, para 0 a 200 quilopascals, são 16 miliampères para 200 quilopascals: 0,08 miliampère por quilopascal; o inverso, 12,5 quilopascals por miliampère, é o fator de escala que converte a leitura em pressão. Deriva, o drift: a variação lenta da indicação ao longo do tempo, sem que o mensurando mude — crítica em monitoramento de meses, porque pode parecer um recalque que não existe. E histerese: indicações diferentes para o mesmo valor, conforme a grandeza esteja subindo ou descendo."

> "E aqui está a confusão mais frequente da disciplina: resolução não é exatidão. Resolução é a menor variação que o display indica; exatidão é a proximidade do valor verdadeiro. Um sensor pode exibir três casas decimais e errar por um milímetro inteiro."

### 5. Exatidão × precisão e incerteza (8:00 – 11:10)

**[TELA]** Slide 10 — alvo interativo (a mosca tem ±2 mm). Ajuste os dois controles para cada caso, na ordem da fala: viés 6 e dispersão 0,4; viés 0 e dispersão 4; viés 0 e dispersão 0,4; viés 6 e dispersão 4.

> "Agora três conceitos que no dia a dia a gente usa como sinônimos, mas que na metrologia, no Vocabulário Internacional de Metrologia, o VIM, são bem diferentes. Precisão é a proximidade entre medições repetidas, entre si. Veracidade é a proximidade entre a média de muitas medições e o valor verdadeiro: é a ausência de viés. E exatidão é a proximidade entre uma medição e o valor verdadeiro, que exige as duas coisas."

> "Olha o alvo na tela. Primeiro caso, com viés de 6 milímetros e dispersão pequena: tiros agrupados, bem juntinhos, mas longe do centro. Isso é preciso, mas com viés: a veracidade é ruim. Há um erro sistemático — sempre para o mesmo lado. E a boa notícia é que erro sistemático é corrigível por calibração: descobriu o desvio, desconta. Segundo caso, sem viés e com dispersão grande: tiros espalhados em torno do centro. Na média, acertam; um por um, erram. Isso é sem viés, mas impreciso: erro aleatório, e cada leitura isolada é inexata. Para reduzir, você repete medições e trabalha com a média. Terceiro caso, o ideal, sem viés e com dispersão pequena: agrupados e no centro, precisos e sem viés: cada leitura é exata. E o quarto, o pior, com viés e dispersão grandes: espalhados e longe do centro."

> "Só que tem um problema filosófico aqui: na vida real, eu nunca conheço o valor verdadeiro. Se eu conhecesse, não precisaria medir. Então como expressar a qualidade de uma medição? A metrologia responde com o conceito de incerteza de medição: um parâmetro que caracteriza a dispersão dos valores que podem ser razoavelmente atribuídos ao mensurando. Em português de canteiro: é a faixa dentro da qual o valor real provavelmente está."

**[TELA]** Slide 10 (continua no ar) — o alvo; a combinação das incertezas (raiz da soma dos quadrados) será aplicada no Slide 15.

> "E quando há várias fontes de incerteza independentes — o instrumento, a mira, a referência, a temperatura —, como elas se combinam? Não é somando direto. Elas se combinam pela raiz da soma dos quadrados, conforme o GUM — sigla em inglês do Guia para a Expressão da Incerteza de Medição. Eleva cada uma ao quadrado, soma, tira a raiz. Isso dá a incerteza combinada. E para comunicar um resultado com um nível de confiança conhecido, multiplica-se a combinada por um fator de abrangência k. Com k igual a 2, você tem cerca de 95% de confiança. Essa é a incerteza expandida, a que vai no relatório."

> "Por que não somar direto? Porque fontes independentes raramente erram todas para o mesmo lado ao mesmo tempo; somar seria supor sempre o pior caso. Mas isso só vale se as fontes forem mesmo independentes."

### 6. Taxa de amostragem e o critério de Nyquist (11:10 – 13:20)

**[TELA]** Slide 11 — simulação de Nyquist: senoide de 50 Hz, com o controle começando em 400 Hz.

> "Mudando de assunto, mas não muito. Um sensor digital não lê a grandeza o tempo todo. Ele lê em instantes discretos — tira 'fotografias' do fenômeno. E aí surge a pergunta: quantas fotos por segundo eu preciso?"

> "Sabe a roda da carroça que, no filme, parece girar para trás? A câmera tira poucos quadros por segundo para a velocidade da roda, e aparece um movimento falso. Isso tem nome: aliasing. E a regra para evitar é o teorema de Nyquist–Shannon: para representar um fenômeno com uma frequência máxima, a taxa de amostragem tem que ser maior que o dobro dessa frequência."

> "Olha a simulação. A onda azul é uma vibração de cravação de estacas, de 50 hertz. A 400 amostras por segundo, os pontos amarelos desenham a onda direitinho. Agora eu desço para 100 hertz, exatamente o dobro: é o limite, e o resultado depende de onde as amostras caem — não dá para confiar. Desço mais, para 60 hertz: olha o que aparece, uma onda lenta, de uns 10 hertz, com frequência falsa, que não existe na realidade. Se eu fosse avaliar o risco ao prédio vizinho com esse registro, ia avaliar o fenômeno errado. Por isso a regra é maior que o dobro, e não igual. E na prática, usa-se de 5 a 10 vezes a frequência máxima — no nosso caso, entre 250 e 500 hertz — para ter uma forma de onda bem definida."

> "Mas cuidado com o exagero oposto. Um piezômetro num solo argiloso pode ser lido a cada hora sem perder nada, porque a poropressão ali muda devagar. A taxa certa depende da velocidade do fenômeno, não da vontade de ter muitos dados. E guarda isso para a Aula 3: ler demais custa bateria, e bateria no canteiro é ouro."

### 7. Calibração e rastreabilidade (13:20 – 14:40)

**[TELA]** Slide 12 — foto do medidor de nível em carretel: "A água no solo vira número, mas só se a reta estiver certa".

> "Último conceito teórico: calibração. Calibrar é comparar as indicações do instrumento com um padrão de referência, de incerteza conhecida, e estabelecer a relação entre elas. Muitas vezes, essa relação é uma reta: o valor da grandeza é igual a um intercepto mais um coeficiente vezes a leitura. Na foto, um medidor de nível em carretel, lido à mão num poço de observação; um piezômetro elétrico faz o mesmo sozinho, com saída de 4 a 20 miliampères — desde que a reta dele esteja certa."

**[TELA]** Slide 13 — a cadeia de rastreabilidade: instrumento de campo → laboratório acreditado → Inmetro.

> "Mas calibração só tem valor se for rastreável. O que isso significa? O padrão que calibrou o seu sensor foi, por sua vez, calibrado por outro padrão, melhor, e esse por outro, numa cadeia ininterrupta que chega aos padrões nacionais, mantidos pelo Inmetro. No Brasil, laboratórios acreditados pelo Inmetro formam a Rede Brasileira de Calibração, a RBC. E o certificado de calibração tem que trazer a incerteza e a rastreabilidade. Quando chegar um sensor na sua obra, peça o certificado. Se ele não informar a incerteza, ele não está te dizendo a coisa mais importante."

### 8. Exemplo numérico: a reta do piezômetro e a incerteza do recalque (14:40 – 17:05)

**[TELA]** Slide 14 — reta de calibração do piezômetro 4–20 mA (mova o controle até 9,6 mA).

> "Hora das contas. São duas, e as duas aparecem em prova e na vida. Primeira: um transdutor de pressão, saída de 4 a 20 miliampères, calibrado com dois pontos. 4 miliampères correspondem a 0 quilopascal; 20 miliampères correspondem a 200 quilopascals. O coeficiente b, o fator de escala, é a variação de pressão dividida pela variação de corrente: 200 menos 0, dividido por 20 menos 4. Dá 200 sobre 16, que é 12,5 quilopascals por miliampère — o inverso da sensibilidade de 0,08 miliampère por quilopascal. E o intercepto: 0 menos 12,5 vezes 4, que dá menos 50 quilopascals. A reta é: pressão igual a menos 50 mais 12,5 vezes a corrente."

> "O datalogger leu 9,6 miliampères. A pressão é menos 50 mais 12,5 vezes 9,6. 12,5 vezes 9,6 dá 120; menos 50, sobram 70 quilopascals. E quanto é isso em coluna d'água? Divide pelo peso específico da água, 9,81 quilonewtons por metro cúbico: 70 sobre 9,81 dá aproximadamente 7,14 metros. Ou seja, há cerca de 7 metros de água acima do sensor."

**[TELA]** Slide 15 — calculadora da incerteza combinada e expandida (GUM).

> "Segunda conta, voltando ao pilar P12. A leitura de recalque é feita por nivelamento geométrico e tem quatro fontes independentes de incerteza. Instrumento: 0,3 milímetro. Mira e posicionamento: 0,4. Estabilidade da referência de nível: 0,5. Efeitos térmicos: 0,2. Raiz da soma dos quadrados: 0,09, mais 0,16, mais 0,25, mais 0,04, dá 0,54. A raiz de 0,54 é aproximadamente 0,73 milímetro. Essa é a incerteza combinada. A expandida, com k igual a 2: aproximadamente 1,5 milímetro."

**[TELA]** Slide 16 — da incerteza à decisão: 9,0 ± 1,5 mm contra o alerta de 10 mm.

> "Agora a leitura de engenheiro. O recalque é 9,0 mais ou menos 1,5 milímetro. Ou seja, o valor real pode estar entre 7,5 e 10,5 milímetros. Esse intervalo inclui o nível de alerta de 10. A decisão tecnicamente defensável não é 'está abaixo de 10, segue o jogo'. É tratar a situação como atenção: aumentar a frequência de leitura e preparar a resposta. Repara que a incerteza não é um detalhe acadêmico — ela mudou a decisão."

### 9. Atividade prática + encerramento (17:05 – 18:40)

**[TELA]** Slide 17 — Atividade prática.

> "Sua missão: pegue a ficha técnica, o datasheet, de um sensor real usado em obras — um inclinômetro MEMS, um piezômetro de corda vibrante ou um sismógrafo de vibração. Anote as características que estão na tela. E depois responda: esse sensor serve para detectar com segurança uma variação de 2 milímetros, ou 2 quilopascals, ou 1 milímetro por segundo, conforme o caso? Justifique com os conceitos de hoje — e eu aposto que, em algum datasheet, você vai pegar a resolução sendo vendida como se fosse exatidão."

**[TELA]** Slide 18 — Pontos-chave; Slide 19 — encerramento e gancho para a Aula 3.

> "Fechando. Sensor responde, transdutor converte, datalogger registra e transmite. Resolução não é exatidão. Precisão é repetir; veracidade é não ter viés; exatidão exige as duas. A qualidade da medição se expressa pela incerteza, e fontes independentes se combinam pela raiz da soma dos quadrados. A amostragem respeita Nyquist e acompanha a velocidade do fenômeno. E calibração só vale se for rastreável ao Inmetro."

> "Agora, você já sabe avaliar se uma leitura merece confiança. Mas como ela sai daquele piezômetro enterrado atrás da cortina de estacas e chega à tela do engenheiro, às duas da manhã? E, mais do que chegar, como ela dispara uma ação no canteiro? Na próxima aula, a gente monta a arquitetura IoT do canteiro, camada por camada, e fecha a malha de verdade. Te espero na Aula 3!"

---

## Roteiro da Videoaula 3 — "Arquiteturas IoT para o canteiro: dispositivos, conectividade e nuvem"

**Duração-alvo:** cerca de 18:30 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:25)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à Aula 3. Até aqui, você aprendeu por que monitorar e como avaliar se uma leitura é confiável. Hoje a gente vai construir o caminho que essa leitura percorre — do sensor até a ação no canteiro."

**[TELA]** Slide 3 — foto: canteiro urbano à noite, "Duas da manhã, depois de uma chuva forte".

> "Imagina a cena. Uma escavação de 9 metros para um subsolo, ao lado de uma rua movimentada. A contenção é uma cortina de estacas. São duas da madrugada, e acabou de cair uma chuva forte. Atrás da cortina, o nível d'água começa a subir. Não tem ninguém na obra — o vigia está na portaria, longe dali. Num sistema de malha aberta, o problema vai ser descoberto às sete da manhã, quando a equipe chegar. Talvez tarde demais. Agora, num sistema IoT bem projetado, a história é outra: o piezômetro detecta a subida, o dado atravessa a cidade em segundos, a plataforma compara com o nível de alerta, a bomba do rebaixamento é acionada e o engenheiro de plantão recebe uma mensagem no celular. Tudo antes que alguém acorde. Nesta aula, você vai entender as camadas que tornam isso possível, as tecnologias de rede que levam o dado e como desenhar uma malha fechada de monitoramento."

### 2. O que é IoT no canteiro (1:25 – 2:25)

**[TELA]** Slide 4 — IoT no canteiro: a lista das "coisas", com a foto da escavação escorada e a do medidor em carretel.

> "IoT, como vimos, é a Internet das Coisas: a conexão de objetos físicos — sensores, máquinas, equipamentos — a redes de dados, de modo que eles enviem informações e recebam comandos sem intervenção humana a cada leitura. Ninguém precisa ir até o piezômetro com uma prancheta. As 'coisas' do canteiro estão listadas na tela. E a foto é de uma obra real de São Paulo: a escavação escorada da Estação Brooklin do metrô — o tipo de obra que vamos vigiar."

> "O que muda com IoT não é o instrumento — muitas vezes é o mesmo piezômetro de corda vibrante. É que ele ganha um datalogger com rádio e passa a falar sozinho. IoT, no canteiro, é menos sobre sensor novo e mais sobre o caminho que o dado percorre."

### 3. As quatro camadas de uma arquitetura IoT (2:25 – 4:55)

**[TELA]** Slide 5 — as quatro camadas, com uma foto para cada uma.

> "Para organizar o sistema, a gente usa uma divisão didática em quatro camadas. E eu vou usar uma analogia com os Correios, que ajuda muito. Camada um: percepção. São os sensores e o datalogger, ou nó sensor: medem, digitalizam e guardam a leitura. Funcionam a bateria, às vezes com um painel solar pequeno. Na analogia, é quem escreve a carta."

> "Camada dois: rede. Aqui o personagem principal é o gateway. Ele recebe os dados dos nós por rádio e os encaminha para a internet — pela rede celular 4G ou 5G, por fibra ou até por satélite, se a obra for remota. Na analogia, é a agência dos Correios: recebe as cartas do bairro e despacha para o centro de distribuição."

> "Camada três: plataforma. São servidores na nuvem que armazenam as séries temporais — as leituras com data e hora —, aplicam regras, comparam com os limites e geram alertas. É o centro de triagem, que lê o endereço e decide para onde cada coisa vai. E é aqui, nesta camada, que vive o gêmeo digital da obra — ou, como vimos na Aula 1, mais frequentemente a sombra digital: a representação atualizada do estado do canteiro, que recebe os dados e onde as decisões são calculadas."

> "Camada quatro: aplicação. Os painéis, os dashboards, os relatórios, os alertas por mensagem de texto ou e-mail, e a integração com o BIM e com o cronograma. É o destinatário abrindo a carta. E é a camada que você, engenheiro, vai efetivamente ver. Mas não se engane: se uma das camadas de baixo falhar, a tela continua bonita, só que mostrando dado velho."

**[TELA]** Slide 6 — as camadas funcionando no canteiro 3D.

> "Olha as camadas funcionando no canteiro. Os pontos amarelos saem dos sensores, na escavação e no prédio, e vão até o gateway: é a percepção falando com a rede. Do gateway, os pontos azuis sobem para a nuvem, onde vive o gêmeo digital: é a plataforma. E a aplicação é a tela em que você acompanha tudo isso. A pessoa e o caminhão no canto dão a escala."

### 4. Conectividade: LoRaWAN, NB-IoT, 4G/5G e Wi-Fi (4:55 – 8:20)

**[TELA]** Slide 7 — tabela de conectividade: alcance, taxa de dados, consumo e uso típico (deixe a tabela no ar; a fala comenta só o contraste principal).

> "Agora a pergunta que todo projeto IoT enfrenta: qual rede usar? E a resposta honesta é: não existe rede melhor. Existe a rede adequada a três critérios: alcance, taxa de dados e consumo de energia. Vamos olhar a tabela."

> "Na tela estão as quatro opções; eu não vou ler a tabela, vou ao contraste que importa. De um lado, o LoRaWAN — de Long Range, longo alcance, numa rede de área ampla. Quilômetros de alcance, taxa de dados muito baixa e anos de bateria: é um mensageiro que grita poucas palavras, mas é ouvido muito longe e quase não se cansa. Perfeito para piezômetros e inclinômetros com leituras periódicas."

> "Do outro lado, o 4G e o 5G da operadora: taxa alta, consumo alto. É a rede das câmeras e dos próprios gateways. No meio, o NB-IoT e o LTE-M — Internet das Coisas em banda estreita e a versão do 4G para máquinas: usam a torre da operadora, com taxa e consumo baixos, sem gateway próprio, mas só onde há cobertura. E o Wi-Fi tem taxa alta e alcance curto, de dezenas a poucas centenas de metros: serve dentro do canteiro, perto da energia."

> "A regra prática que eu quero que você guarde: sensor de leitura lenta e a bateria, vá de LoRaWAN ou NB-IoT. Muito dado e energia disponível, vá de 4G, 5G ou Wi-Fi. E um detalhe regulatório: o LoRaWAN opera em faixas de radiofrequência não licenciadas, o que quer dizer que você não paga licença de espectro. Mas, no Brasil, os equipamentos de radiocomunicação precisam de homologação da Anatel. Comprou um nó sensor barato no exterior, sem homologação? Ele não deveria estar operando no seu canteiro."

**[TELA]** Slide 8 — simulação "Quem alcança quem?": clique em Wi-Fi, depois LoRaWAN, depois NB-IoT.

> "Olha a simulação. Clico em Wi-Fi: só os dois sensores dentro do canteiro ficam verdes, o piezômetro e o extensômetro; o resto fica vermelho. Clico em LoRaWAN: um gateway no canteiro, com uns 3 quilômetros de alcance urbano, alcança todos os sensores do mapa. Clico em NB-IoT: quem alcança agora é a torre da operadora. Vamos aplicar isso na nossa escavação. Os piezômetros e inclinômetros leem a cada 15 minutos e mandam poucos bytes: LoRaWAN resolve, com o gateway num ponto alto, ligado na tomada e mandando tudo para a nuvem por 4G. E a câmera da frente de escavação, que gera vídeo, vai direto no 4G ou no Wi-Fi do escritório. Um mesmo canteiro usa várias redes, cada uma na sua vocação."

**[TELA]** Slide 9 — foto do gateway LoRaWAN no alto de um mastro.

> "E esse é o gateway, a ponte entre o rádio e a internet. Por padrão, ele não decide nada: recebe o rádio dos nós e encaminha ao servidor de rede LoRaWAN, que entrega as mensagens à plataforma. Mas ele pode rodar regras simples ali mesmo, na borda. E isso leva à próxima decisão de projeto."

### 5. Borda × nuvem e o protocolo MQTT (8:20 – 10:45)

**[TELA]** Slide 10 — borda (edge) × nuvem (cloud).

> "Próxima decisão de projeto: onde o processamento acontece? Processar na borda — o edge — é decidir no próprio datalogger ou no gateway, sem depender da internet. Processar na nuvem — o cloud — permite cruzar muitos sensores, guardar todo o histórico e rodar modelos pesados."

> "Pensa no seu corpo: você puxa a mão da panela quente antes de sentir a dor — um reflexo resolvido na medula, sem consultar o cérebro. Isso é a borda. Decidir se vale trocar de panela é o cérebro, com calma e histórico: a nuvem. Sistemas robustos fazem os dois: a regra crítica fica na borda — ligar a bomba, por exemplo, continua funcionando mesmo se o 4G cair às duas da manhã. A análise e o registro ficam na nuvem."

**[TELA]** Slide 11 — simulação MQTT: publicar e assinar. Clique em Chuva forte quando a fala pedir; em cerca de 6 segundos o nível cruza o alerta e o comando LIGAR chega à bomba.

> "E como a mensagem chega à plataforma? Numa rede LoRaWAN, o gateway só encaminha os pacotes; quem os decodifica e entrega é o servidor de rede, e um protocolo muito usado nessa entrega é o MQTT — sigla em inglês de transporte de telemetria por filas de mensagens. Ele é leve, feito para dispositivos simples, e funciona no modelo de publicação e assinatura. Pensa num grupo de mensagens temático. A leitura de cada sensor é publicada num tópico — por exemplo, obra, barra, escavação, barra, PZ-03, barra, nível — num servidor central chamado broker. E qualquer aplicação interessada assina aquele tópico e recebe as leituras. Quem publica não precisa saber quem vai ler. E o mais importante para nós: o mesmo mecanismo funciona no sentido contrário. A plataforma pode publicar um comando num tópico que a bomba assina, pelo mesmo caminho de rede — 'liga a bomba'. Clico em chuva forte. Olha a régua do nível d'água descendo para perto do fundo; a cada leitura, o pacote passa pelo broker e chega ao gêmeo digital. Cruzou a atenção, sai o aviso; cruzou o alerta, sai o comando LIGAR, que passa pelo broker e chega à bomba. É isso que fecha a malha."

### 6. A malha fechada com monitoramento IoT (10:45 – 13:25)

**[TELA]** Slide 12 — a malha fechada em cinco passos, do piezômetro à bomba.

> "Agora vamos juntar tudo e voltar às duas da madrugada. A malha fechada da escavação tem cinco passos, que estão na tela."

> "Passo um: medir. O piezômetro PZ-03, instalado atrás da cortina, lê o nível d'água a cada 15 minutos. Passo dois: transmitir. O nó envia a leitura por LoRaWAN ao gateway, que a encaminha ao servidor de rede, e este a publica via MQTT na plataforma. Passo três: comparar. A plataforma — aqui funcionando como o gêmeo digital da escavação — compara o nível com os limites de projeto. Há um nível de atenção, por exemplo, o nível d'água a 2 metros abaixo do fundo da escavação. E um nível de alerta, por exemplo, a 1 metro abaixo do fundo."

**[TELA]** Slide 13 — simulação: o nível d'água do PZ-03 sobe 0,5 m/h depois da chuva; leitura a cada 15 min. Ela já começa em Malha fechada; espere a bomba ligar (uns 15 segundos) e então clique em Malha aberta.

> "Passo quatro: decidir e agir. Olha a curva subindo. Cruzou a atenção: o sistema aumenta a frequência de leitura e avisa o engenheiro. Cruzou o alerta: aciona a bomba do rebaixamento e recomenda paralisar a frente de escavação mais próxima. E passo cinco, o que separa engenharia de alarme: medir de novo. As leituras seguintes confirmam — ou não — que o nível voltou a cair. Olha na simulação: a bomba ligou e a curva dobrou para baixo. Laço confirmado. Agora eu clico em malha aberta: com vistoria a cada 6 horas, a água chega ao fundo da escavação, na sétima hora, antes de a bomba ser ligada, na oitava. E se não tivesse caído? Aí o laço escala a decisão para a equipe de geotecnia, porque o problema é maior do que a bomba resolve."

> "Repara numa coisa: esse laço não termina na tela. Ele termina numa ação no canteiro e numa nova leitura que verifica a ação. Se o seu sistema termina num gráfico, ele ainda é malha aberta, por mais moderno que seja."

> "E revisita a classificação de Kritzinger. No laço da bomba, o dado vai e o comando volta automaticamente: para essa malha, a plataforma é gêmeo digital de verdade. Na recomendação de paralisar a frente, a volta depende de um engenheiro: sombra digital com um humano fechando o laço. Um mesmo sistema pode ter as duas coisas — e isso é decisão de projeto."

### 7. Exemplo numérico: quanto dura a bateria? (13:25 – 15:20)

**[TELA]** Slide 14 — calculadora da autonomia do nó sensor: ciclo de 15 min × ciclo de 60 s.

> "Agora a pergunta que todo cliente faz: e a bateria, aguenta quanto tempo? Vamos calcular. O nó sensor do piezômetro tem uma bateria de lítio de 19.000 miliampères-hora. Mas a gente não usa tudo: considera utilizável 80%, por causa de efeitos de temperatura e de autodescarga. A cada ciclo de 15 minutos, que são 900 segundos, ele faz três coisas. Lê o sensor por 2 segundos, a 25 miliampères. Transmite por 1 segundo, a 120 miliampères. E dorme o resto, 897 segundos, a 0,02 miliampère."

> "Carga por ciclo: 2 vezes 25, que dá 50. Mais 1 vezes 120, que dá 120. Mais 897 vezes 0,02, que dá quase 18. Total: aproximadamente 187,9 miliampères-segundo. Dividindo pelos 900 segundos do ciclo, a corrente média é de uns 0,21 miliampère. E a autonomia: 80% de 19.000, que dá 15.200 miliampères-hora, dividido por 0,2088. Dá cerca de 72.800 horas — uns 3.033 dias, ou aproximadamente 8,3 anos. Mais tempo que a obra inteira."

> "Agora vem a pegadinha. Em modo de alerta, o sistema passa a ler a cada 60 segundos: 2 de leitura, 1 de transmissão e 57 dormindo. A corrente média sobe para uns 2,85 miliampères. E a autonomia despenca para cerca de 5.330 horas — uns 222 dias. Saímos de 8 anos para 7 meses só mudando a taxa de leitura. A moral: a taxa de leitura governa a autonomia. Lembra da Aula 2, quando eu disse que bateria no canteiro é ouro? Por isso os bons sistemas usam amostragem adaptativa: leem devagar na condição normal e só aceleram quando a malha entra em atenção."

### 8. Pausa para reflexão: automática ou humana? (15:20 – 17:00)

**[TELA]** Slide 15 — Pausa para reflexão: "A malha deve agir sozinha ou chamar um humano?", com a calculadora dos quatro critérios.

> "Agora eu quero que você pause o vídeo por um minuto e pense comigo. No nosso exemplo, a plataforma liga a bomba sozinha. Ótimo. Mas ela deveria também paralisar a escavação sozinha, travando as máquinas?"

> "Olha os dois lados. A favor da resposta automática: ela é rápida e funciona às duas da manhã, quando ninguém está acordado. Contra: um sensor com defeito ou uma leitura espúria — uma descarga elétrica, um cabo mordido — pode parar a obra inteira sem motivo. Ou, pior, uma ação automática pode criar um risco novo: imagina travar uma escavadeira no meio de uma manobra, com caminhão posicionado ao lado."

> "Para decidir, considere quatro critérios. A consequência de agir errado. A consequência de não agir a tempo. A confiabilidade do sensor — existe redundância, dois instrumentos que confirmam um ao outro? E a reversibilidade da ação. Uma regra prática que você pode testar: ações reversíveis, de baixo risco e urgentes podem ser automáticas — ligar uma bomba, aumentar a frequência de leitura, mandar uma notificação. Ações de alto impacto ou difíceis de reverter pedem um humano no laço — paralisar a obra, evacuar um imóvel, mudar o projeto da contenção. Use a calculadora da tela para testar dois casos: ligar a bomba e paralisar a escavação. Volte ao vídeo quando tiver a sua resposta."

### 9. Atividade prática + encerramento (17:00 – 18:30)

**[TELA]** Slide 16 — Atividade prática.

> "Sua missão: desenhe numa folha a arquitetura IoT de monitoramento para um destes casos. Caso A: recalque de um edifício vizinho a uma escavação. Caso B: vibração causada por cravação de estacas perto de um casarão histórico. Indique as quatro camadas; a tecnologia de rede, justificando por alcance, taxa e consumo; onde roda cada regra, na borda ou na nuvem; e a malha fechada completa, com níveis de atenção e alerta e a ação de cada um. Dica para o caso B: lembre-se de Nyquist antes de escolher a rede."

**[TELA]** Slide 17 — Pontos-chave; Slide 18 — encerramento e gancho para a Aula 4.

> "Fechando. Arquitetura IoT em quatro camadas: percepção, rede, plataforma — onde vive o gêmeo ou a sombra digital — e aplicação. A rede se escolhe por alcance, taxa e consumo. Borda para o reflexo, nuvem para o raciocínio. A malha fechada vai do sensor à ação e volta ao sensor. E a taxa de amostragem governa a bateria."

> "Hoje a gente montou o sistema dos sensores. Mas falta o outro protagonista da disciplina: o drone. Que tipos existem, do que ele é feito por dentro, que câmeras e sensores ele carrega — e, principalmente, o que a lei brasileira exige para voar sobre uma obra. É a próxima aula. Te espero na Aula 4!"

---

## Roteiro da Videoaula 4 — "Drones (RPA): tipos, componentes, cargas úteis e regulamentação brasileira"

**Duração-alvo:** cerca de 18:50 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:10)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à quarta aula — a que fecha os fundamentos da disciplina. Começo com uma cena muito comum. A construtora comprou um drone. Chegou a caixa no escritório da obra, e o gerente fala: 'A partir de amanhã, quero o canteiro voado toda semana'. Tira da caixa, carrega a bateria e decola, certo?"

**[TELA]** Slide 3 — foto do piloto remoto com o controle na mão: "Antes de tudo: pode voar?"

> "Errado. Antes de decolar, tem uma lista de perguntas. Qual drone serve para mapear 12 hectares — e qual serve para inspecionar a fachada? Não é o mesmo. Que sensor ele precisa carregar: uma câmera comum, uma térmica, um LiDAR? E, antes de tudo, a pergunta que pode custar caro: pode voar? A aeronave está cadastrada? O piloto está habilitado? O voo foi solicitado ao controle do espaço aéreo? Tem seguro? Nesta aula, você vai conhecer os tipos de drone, os componentes, as cargas úteis e o arcabouço regulatório brasileiro — que acabou de mudar, e isso é importante."

### 2. RPA, UAS e drone: os termos (1:10 – 1:50)

**[TELA]** Slide 3 (continua no ar) — o texto com os termos UA, UAS e RPA.

> "Primeiro, os nomes. 'Drone' é o nome popular — o que a gente fala no canteiro. A regulamentação fala em aeronave não tripulada, a UA, e em sistema de aeronave não tripulada, o UAS. E por que 'sistema'? Porque o UAS é a aeronave mais a estação de pilotagem remota e o enlace de comando entre elas. Se o rádio falha, o sistema falha, mesmo que a aeronave esteja perfeita. A literatura técnica também usa muito RPA, a aeronave remotamente pilotada. Aeromodelos recreativos têm regras próprias; drone sobre obra, para uma construtora, é uso profissional."

### 3. Tipos de drone: multirrotor, asa fixa e VTOL (1:50 – 3:15)

**[TELA]** Slide 4 — as três famílias: multirrotor, asa fixa e VTOL.

> "Existem três grandes famílias. A primeira é o multirrotor — quadricóptero, hexacóptero, octocóptero, conforme o número de hélices. Ele decola na vertical, paira parado no ar e manobra com precisão. Isso faz dele o ideal para inspeção de fachadas e de estruturas, e para áreas pequenas. A limitação é a autonomia: tipicamente de 20 a 45 minutos. Gastar energia para ficar parado no ar é caro."

> "A segunda é a asa fixa. Voa como um avião: a asa gera sustentação, e o motor só empurra para frente. Isso é muito mais eficiente, então ela cobre centenas de hectares por voo. É a preferida em rodovias, ferrovias e grandes terraplenagens. Mas precisa de área para pousar e não paira em frente a uma trinca."

**[TELA]** Slide 5 — foto do VTOL tail-sitter pousado na vertical.

> "E a terceira é o VTOL, da sigla em inglês para decolagem e pouso vertical. É um híbrido: decola e pousa na vertical, como o multirrotor, e voa em cruzeiro como asa fixa. A foto na tela é um VTOL do tipo tail-sitter, que fica 'sentado' na cauda antes de decolar. Junta o melhor dos dois mundos para mapeamento de grandes áreas sem pista."

### 4. Componentes de um drone (3:15 – 5:20)

**[TELA]** Slide 6 — drone em 3D, montado, com as hélices girando. Clique em Vista explodida quando a fala pedir; as peças se separam em cerca de 2 segundos.

> "Agora vamos abrir o drone. Clico em vista explodida, e as peças se separam. Começando pela estrutura, o frame: fibra de carbono ou compósitos, leve e rígida. Motores e ESC: os motores são elétricos do tipo brushless, sem escovas, e cada um é acionado por um controlador eletrônico de velocidade, o ESC — sigla em inglês de electronic speed controller. É ele que varia a rotação de cada hélice centenas de vezes por segundo para manter o drone estável."

> "No centro, a controladora de voo: o cérebro. Ela estabiliza a aeronave e executa as missões automáticas — aquele voo em linhas paralelas que você vai planejar na Unidade 2. Para saber onde está, ela usa o receptor GNSS, de navegação por satélite. E aqui tem um detalhe que importa muito para a engenharia: com RTK — de real time kinematic, a correção cinemática em tempo real —, a posição de cada foto chega ao nível de centímetros, o que reduz a necessidade de pontos de controle em campo. Reduz — não elimina. Lembra da Aula 2: a gente sempre quer verificar."

> "Para saber como está inclinado, a controladora usa a IMU, a unidade de medição inercial, com acelerômetros e giroscópios — os mesmos MEMS que vimos na aula de sensoriamento. A energia vem da bateria LiPo, de polímero de lítio: alta densidade de energia, mas exige cuidado com carga, temperatura e armazenamento. O gimbal é o suporte estabilizado que mantém a câmera firme mesmo com vento. E o rádio faz o enlace de comando e de vídeo com a estação de pilotagem remota."

**[TELA]** Slide 7 — os componentes de verdade: motor brushless, bateria LiPo e plataforma profissional com RTK.

> "E aqui estão esses componentes de verdade: o motor sem escovas, a bateria LiPo e uma plataforma profissional com receptor RTK."

### 5. Cargas úteis (5:20 – 7:10)

**[TELA]** Slide 8 — as quatro cargas úteis: RGB, térmica, LiDAR e multiespectral.

> "A carga útil — o payload — é o que o drone leva para trabalhar. São quatro principais. A câmera RGB — de red, green e blue, a câmera comum — é de longe a mais usada: com ela se faz fotogrametria, que gera o ortomosaico, o modelo 3D e o cálculo de volumes, além do acompanhamento do avanço físico. A câmera multiespectral capta bandas além do visível; o mapa colorido da tela é um índice de vegetação, que mostra onde ela está mais vigorosa — útil para acompanhar se a hidrossemeadura de um talude pegou. A câmera térmica mostra diferenças de temperatura: infiltrações, descolamento de revestimentos de fachada, painéis elétricos aquecidos. No termograma da tela, uma fachada com isolamento aparece em azul e outra sem isolamento, perdendo calor, em amarelo e vermelho. E o LiDAR — de light detection and ranging, detecção e medição de distância por luz — é um laser que gera diretamente uma nuvem de pontos e, como os pulsos passam pelas frestas da vegetação, alcança o terreno onde a fotogrametria falha. Lembra da ressalva da Aula 1, de que o drone não enxerga sob vegetação densa? O LiDAR é a resposta parcial a ela."

> "Como escolher? Pelo objetivo. Volume escavado e avanço físico do mês? RGB. Infiltração numa laje ou revestimento descolando numa fachada antiga do litoral? Térmica. Terreno natural de uma encosta coberta de mata? LiDAR. E, como vimos na Aula 2, câmera de alta resolução não garante exatidão."

### 6. Regulamentação brasileira: do RBAC-E nº 94 ao RBAC nº 100 (7:10 – 12:00)

**[TELA]** Slide 9 — do RBAC-E nº 94 (classes por peso) ao RBAC nº 100 (categorias por risco).

> "Agora a parte que mais muda a vida de quem opera drone no Brasil. Por quase uma década, a referência foi o RBAC-E número 94 da ANAC, de 2017. Ele classificava as aeronaves pelo peso máximo de decolagem, em três classes, com o limite de 25 quilos separando a Classe 3 das demais. Você ainda vai encontrar essas classes em contratos e editais."

> "Em junho de 2026, a ANAC aprovou o RBAC número 100, pela Resolução número 805, de 15 de junho de 2026. Ele substituiu o RBAC-E 94 — e quem já tinha autorização que não cabe na categoria aberta tem 2 anos para obter uma nova. A mudança de filosofia é grande: em vez de classificar a aeronave pelo peso, passa a classificar a operação pelo risco. Um drone de 5 quilos sobre uma multidão é mais perigoso que um de 20 sobre um descampado."

**[TELA]** Slide 10 — as três categorias de operação: aberta, específica e certificada.

> "São três categorias. A categoria aberta: peso em voo até 25 quilos, em linha de visada visual — o VLOS, com o piloto vendo o drone — ou estendida, o EVLOS, com a ajuda de um observador; até 120 metros — 400 pés — acima do solo, em áreas distantes de terceiros. E aqui vem o número que você precisa decorar: em nenhuma hipótese a menos de 30 metros horizontais de pessoas não envolvidas e não anuentes, a não ser que exista uma barreira mecânica capaz de protegê-las. E ela também exige uma avaliação de risco operacional atualizada."

> "A categoria específica entra quando algum critério da aberta não é atendido: voo além da linha de visada — o BVLOS —, acima de 120 metros, aeronave acima de 25 quilos. Aí o operador demonstra a segurança por uma avaliação de risco, num método aceito pela ANAC, como o SORA — a avaliação de risco de operações específicas, criada pelo grupo internacional de autoridades JARUS —, ou por um cenário padrão; conforme a complexidade, ele ainda obtém o COE, o Cadastro de Operador na categoria específica. E a categoria certificada é para operações de alto risco, como transporte de artigos perigosos, com certificação da aeronave, do operador e do piloto."

**[TELA]** Slide 11 — escala real em 3D: o prédio de 40 pavimentos (120 m), o círculo de 30 m e o de 150 m.

> "Olha a cena em escala real: um prédio de 40 pavimentos de 3 metros é o teto da categoria aberta. Eu levo o drone até o limite e aproximo das pessoas até o círculo vermelho de 30 metros; com a barreira ligada, a regra muda. No canteiro urbano, pessoas não envolvidas e não anuentes são o pedestre, o vizinho, o motorista; os seus operários, informados e de acordo, são outra situação. Num terreno pequeno, cercado de prédios, cumprir os 30 metros pode não ser trivial — e aí a operação pode cair na categoria específica."

> "Um caso: multirrotor de 9 quilos, em linha de visada, a 80 metros, sobre um canteiro urbano, com a área sob o voo isolada e os 30 metros respeitados. Cabe na categoria aberta. Mas 'categoria aberta' não quer dizer 'liberado': faltam os requisitos que vêm agora."

**[TELA]** Slide 12 — os números do RBAC nº 100 (120 m, 30 m, 25 kg, 24 meses, 250 g) e os cartões SISANT, Piloto e Seguro.

> "Além das categorias, o RBAC 100 traz outros requisitos. As aeronaves das categorias aberta e específica são cadastradas no SISANT, o Sistema de Aeronaves não Tripuladas da ANAC, com cadastro válido por 24 meses e identificação na própria aeronave. O piloto remoto precisa ser aprovado em exame de conhecimento teórico da ANAC — e aqui tem uma transição: a própria resolução dispensou essa exigência até 31 de dezembro de 2026, então o exame passa a ser exigível a partir de 1º de janeiro de 2027. E as operações devem ter seguro com cobertura de danos a terceiros — o seguro de responsabilidade aeronáutica, que o setor chama de RETA —, com poucas exceções. Os drones de até 250 gramas ficam fora do RBAC 100, com as regras simplificadas da Resolução 806 — desde que voem até 120 metros e em linha de visada, VLOS ou EVLOS; e continuam passando pelo DECEA e pelo SARPAS. Atenção: 250 gramas, não 25 quilos."

### 7. DECEA, Anatel, LGPD e o voo na prática (12:00 – 14:15)

**[TELA]** Slide 13 — foto (placa de zona proibida nos EUA): "O espaço aéreo tem dono".

> "Só que a ANAC não é a única porta. A ANAC cuida da aeronave e do operador. Mas o espaço aéreo é do DECEA, o Departamento de Controle do Espaço Aéreo. A ICA 100-40 — a instrução do Comando da Aeronáutica para aeronaves não tripuladas —, na edição de 2026, determina que o acesso ao espaço aéreo seja solicitado pelo SARPAS, o sistema de solicitação de acesso de aeronaves remotamente pilotadas. Não importa se o drone é pequeno e o voo é baixo: o pedido passa pelo SARPAS, com uma antecedência que cresce com o risco — minutos na categoria aberta, dias num voo além da linha de visada. E os rádios do drone precisam de homologação da Anatel, como os nós sensores da Aula 3."

> "E tem um ponto que pega muita obra de surpresa: o aerolevantamento. Se você voa em faixas sobrepostas para gerar ortomosaico ou modelo do terreno, isso é aerolevantamento, pelo artigo 8º da Portaria 3.703 do Ministério da Defesa. Só pode ser executado por entidade inscrita no ministério, e o pedido no SARPAS sai com 4 dias corridos de antecedência. Pelo artigo 38, áreas pequenas — um círculo de até 2,2 quilômetros de raio, ou menos de 15 quilômetros quadrados — ficam pré-autorizadas, desde que atendidas condições cumulativas, como não tocar áreas sujeitas a restrição. Isso não dispensa a inscrição nem o DECEA. Já a foto de inspeção ou o vídeo de avanço, sem faixas sobrepostas, não é aerolevantamento."

**[TELA]** Slide 14 — checklist interativo com nove itens; marque-os enquanto fala, sem ler cada um.

> "Tudo isso cabe num checklist de nove itens, que está na tela. Três deles pegam mais gente: o pedido no SARPAS, o aerolevantamento quando é mapeamento e a LGPD — a Lei Geral de Proteção de Dados —, porque a imagem de trabalhadores e vizinhos é dado pessoal. Imprime a lista e cola na tampa da maleta do drone."

### 8. Exemplo numérico: quanto um drone cobre por voo? (14:15 – 17:05)

**[TELA]** Slide 15 — calculadora de área por voo: multirrotor × VTOL.

> "Vamos às contas, porque é a geometria da obra que vai escolher o drone para você. A área mapeada por voo é, aproximadamente, a velocidade de cruzeiro vezes o tempo útil de mapeamento vezes o espaçamento entre as faixas de voo. Como um cortador de grama: velocidade, vezes tempo, vezes a largura que avança a cada passada."

> "O espaçamento: com faixa imageada de 100 metros e sobreposição lateral de 70%, cada faixa nova avança 30% da largura, 30 metros."

> "Multirrotor: autonomia de 30 minutos. Mas nem tudo é útil: tem reserva de bateria, decolagem, pouso e curvas. Considerando 70% úteis, são 21 minutos, ou 1.260 segundos. Velocidade de 6 metros por segundo. A área: 6 vezes 1.260 vezes 30, que dá 226.800 metros quadrados, aproximadamente 22,7 hectares."

> "VTOL de asa fixa: autonomia de 59 minutos. Com 70% úteis, cerca de 41,3 minutos, uns 2.478 segundos. Velocidade de 16 metros por segundo. A área: 16 vezes 2.478 vezes 30, que dá cerca de 1.189.000 metros quadrados, aproximadamente 119 hectares. Mais de cinco vezes o multirrotor."

> "E a leitura de engenheiro. O canteiro de 12 hectares da Aula 1 cabe com folga num único voo do multirrotor. Já 20 quilômetros de rodovia, com 60 metros de faixa de domínio, são 120 hectares: pede o VTOL. Quantos voos? 120 dividido por 119 dá 1,01, e número de voos se arredonda para cima: 2 voos do VTOL, contra 6 do multirrotor. E a 10 quilômetros da decolagem ninguém enxerga o drone: voo BVLOS, além da linha de visada, é categoria específica, com pedido no SARPAS 8 dias antes; a alternativa é dividir o trecho em blocos voados em linha de visada. Ou seja, o tipo de drone segue a geometria da obra — e a geometria também define a categoria. Para inspecionar fachada, a conta nem é de área: é pairar perto. Aí volta o multirrotor."

**[TELA]** Slide 16 — simulação: o canteiro de 12 ha da Aula 1 voado em faixas; quando a fala pedir, leve o tempo útil a 10 min (o voo recomeça; a segunda cor aparece no fim da varredura, em uns 5 segundos).

> "Olha o canteiro de 12 hectares sendo voado em faixas de ida e volta. Cada cor é uma bateria. Com 6 metros por segundo, 21 minutos úteis e 30 metros entre faixas, cabe tudo numa cor só: um voo. Agora eu reduzo o tempo útil para 10 minutos, como numa bateria cansada ou num dia de vento: o voo recomeça e, no fim da varredura, aparece a segunda cor. A margem de hoje pode sumir amanhã."

### 9. Atividade prática, síntese da unidade e prévia da Unidade 2 (17:05 – 18:50)

**[TELA]** Slide 17 — Atividade prática e pontos-chave.

> "Sua missão: escolha uma obra e monte um checklist de conformidade para voar sobre ela. Enquadramento no RBAC 100 — aberta ou específica? —, cadastro, piloto, seguro, SARPAS, aerolevantamento, Anatel, distância de terceiros e LGPD. Depois indique o tipo de drone e a carga útil mais adequados, justificando pela geometria da obra e pelo objetivo do levantamento."

**[TELA]** Slide 18 — foto aérea das obras do Rodoanel Norte, em São Paulo: "Uma foto assim é só o começo".

> "E com isso fechamos a Unidade 1: por que monitorar e fechar a malha, como medir com confiança, como o dado viaja numa arquitetura IoT e, hoje, o que é um drone por dentro e o que é preciso para voar legalmente."

**[TELA]** Slide 19 — prévia da Unidade 2: planejar o voo, fotogrametria, produtos, LiDAR e térmica.

> "Na Unidade 2, o drone vai para o ar de verdade. Você vai planejar o voo: o tamanho do pixel no solo, a altura, a sobreposição, o plano de missão — e vai descobrir de onde veio aquela faixa de 100 metros. Vai entender como a fotogrametria transforma centenas de fotos num modelo 3D, com pontos de controle e correção de posição. Vai gerar o ortomosaico, os modelos do terreno e a nuvem de pontos, e calcular volumes de corte e aterro. E vai conhecer o LiDAR embarcado e a termografia na inspeção de estruturas e fachadas. Tudo o que vimos aqui — malha fechada, incerteza, regulamentação — vai se aplicar a cada voo. "

**[TELA]** Slide 20 — encerramento: "Fundamentos concluídos".

> "Foi um prazer construir esses fundamentos com você. Te espero na Unidade 2. Um abraço!"

---
