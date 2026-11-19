# Roteiros Estendidos (17–19 minutos) — Unidade 4: Integração, Inteligência e Gestão do Monitoramento

- **Disciplina:** Drones e Sensores IoT no Monitoramento de Obras
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 13 a 16
- **Formato:** roteiro de narração **integral** — o texto em citação (>) é a fala completa. **Esta é a versão a gravar.** Duração-alvo: **17 a 19 minutos** por aula (cerca de 2.150 a 2.600 palavras faladas, a uns 135 palavras/min, já contando as pausas curtas das demonstrações). Os roteiros curtos de `unidade_4.md` são só um guia da sequência.

> **Como usar:** leia as falas em citação na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`), na mesma ordem dos slides. Quando a fala manda clicar, o efeito descrito aparece na tela em poucos segundos; tabelas e listas dos slides **não** são lidas item a item: a fala comenta o essencial e o aluno lê o resto na tela.

---

## Roteiro da Videoaula 13 — "Integração com BIM e gêmeo digital: 4D e comparação as-built × as-designed"

**Duração-alvo:** cerca de 17:50 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e seja muito bem-vindo, muito bem-vinda à Unidade 4, a última da disciplina Drones e Sensores IoT no Monitoramento de Obras. Até aqui, você aprendeu os fundamentos, colocou o drone no ar e instrumentou a obra com sensores. Agora chegou a hora de juntar tudo. Nesta unidade, a gente fala de integração, de inteligência e de gestão. E a primeira peça dessa integração é o BIM."

**[TELA]** Slide 3 — foto: "Avanço físico de 62%, conforme o cronograma."

> "Começo com uma cena muito comum. Reunião mensal de obra. A gerenciadora projeta a planilha e anuncia: avanço físico de 62%, conforme o cronograma. Todo mundo concorda com a cabeça. Só que o drone voou ontem, a nuvem de pontos está pronta, e os sensores mandam leitura a cada 15 minutos. O problema é que cada um desses dados mora num sistema diferente: o drone numa pasta, os sensores numa plataforma, o cronograma numa planilha e o projeto num arquivo que ninguém abre na reunião. E aí ninguém consegue responder a duas perguntas muito simples. Primeira: o que foi construído está onde o projeto mandou? Segunda: o que foi construído é o que deveria estar pronto nesta data? Hoje a gente vai ver como o BIM costura esses dados, o que são o 4D e o 5D, como se compara o que foi construído com o que foi projetado — usando tolerância e incerteza — e em que momento o modelo vira, de verdade, um gêmeo digital."

### 2. BIM: o modelo é informação (1:40 – 3:50)

**[TELA]** Slide 4 — CAD × BIM: objetos com informação, IFC e GUID.

> "Vamos começar desfazendo uma confusão. Muita gente acha que BIM é desenho em 3D. Não é. BIM, de Building Information Modeling, é modelagem da informação da construção. A palavra mais importante é informação. No CAD, uma linha é uma linha: o software não sabe que aquilo é um pilar. Se o projeto muda, cada planta, cada corte e cada vista é corrigido à mão. No BIM, cada elemento é um objeto, com geometria, com propriedades e com relações. Aquele retângulo não é um retângulo: é o pilar P12, de concreto C35, concretado em 14 de março, que pertence ao terceiro pavimento e apoia a viga V20."

> "Agora, numa obra real, cada equipe usa um software diferente. A arquitetura num, a estrutura noutro, as instalações num terceiro. Como esses modelos conversam? Pelo openBIM, baseado no IFC, as Industry Foundation Classes. O IFC é um esquema aberto, mantido pela buildingSMART e normalizado como ISO 16739. Aberto quer dizer que não pertence a nenhum fabricante. E tem um detalhe que importa muito para a nossa disciplina: cada objeto do IFC tem um identificador global único, o GUID. É nesse identificador que a gente vai pendurar tudo o que vem do canteiro — a leitura de um sensor, a foto do drone, uma pendência de qualidade. Existe até uma classe IFC específica para instrumentos, o IfcSensor. Ou seja: o monitoramento cabe dentro do modelo."

### 3. 4D, 5D e as dimensões do BIM (3:50 – 5:10)

**[TELA]** Slide 5 — quadro das dimensões do BIM, de 1D a 6D.

> "Olha esse quadro na tela, com as chamadas dimensões do BIM. O 3D é o modelo geométrico com informação. Quando eu ligo cada elemento do modelo a uma atividade do cronograma, eu ganho o 4D: o modelo passa a crescer no tempo. Eu arrasto uma data e vejo o que deveria estar pronto naquele dia — e posso comparar com o que foi executado. Quando eu ligo também quantidades e custos, eu chego ao 5D: orçamento, medição de serviços e fluxo de caixa extraídos direto do modelo."

> "Um cuidado: depois do 5D, a numeração vira bagunça. Tem autor que chama o 6D de sustentabilidade, outro de desempenho, outro de operação e manutenção. Não se prenda ao número. O que importa é o uso que você faz do modelo. E, para a nossa disciplina, os usos que interessam são dois: o 4D, que responde 'está em dia?', e a comparação geométrica, que responde 'está no lugar?'."

### 4. BIM na lei e a ISO 19650 (5:10 – 7:20)

**[TELA]** Slide 6 — linha do tempo: Decreto nº 9.983/2019, Decreto nº 10.306/2020 e as três fases.

> "E isso não é moda: já é lei para muita obra no Brasil. Em 2019, o Decreto 9.983 instituiu a Estratégia BIM BR, para disseminar o BIM no país. Em 2020, o Decreto 10.306 tornou o uso obrigatório, de forma gradual, nas obras e serviços de engenharia da administração pública federal abrangidos pelo decreto. Repare nas três fases. Desde 2021, a primeira fase: projeto — modelos das disciplinas, detecção de interferências, extração de quantitativos e geração de pranchas. Desde 2024, a segunda fase, que é a que mais interessa a nós: o BIM entra na execução da obra, com orçamentação, planejamento e controle, e com a atualização do modelo as-built, ou seja, o modelo do que foi efetivamente construído. E, a partir de 2028, a terceira fase: gestão e manutenção depois da obra. Além disso, a Lei 14.133, a nova lei de licitações, manda adotar o BIM preferencialmente nas licitações de obras e serviços de engenharia, sempre que for adequado ao objeto. Percebe a conexão? O monitoramento desta disciplina é exatamente o que alimenta a fase dois: controle da execução e as-built."

**[TELA]** Slide 7 — ISO 19650: o ambiente comum de dados e seus quatro estados.

> "Para organizar toda essa informação existe a série internacional ISO 19650, que trata da gestão da informação com BIM. O conceito central dela é o ambiente comum de dados, em inglês common data environment, o CDE. É um repositório único em que cada arquivo passa por estados controlados. Em elaboração: a equipe ainda está produzindo. Compartilhado: liberado para as outras equipes coordenarem e verificarem. Publicado: aprovado para uso — é com ele que se constrói, mede e paga. E arquivado: o histórico, para saber quem mudou o quê, quando e por quê. A lição para quem monitora é direta: leitura de sensor e nuvem de pontos também são informação da obra. Precisam de dono, de versão e de estado. Um gráfico solto num e-mail não é informação gerida."

### 5. O 4D na prática (7:20 – 8:40)

**[TELA]** Slide 8 — o BIM 4D em 3D: arraste a semana. Comece na semana 22 e arraste até a 40.

> "Vamos ver o 4D funcionando. Na tela, um edifício de 12 pavimentos. O contorno azul é o que o cronograma previa até a semana escolhida. O sólido é o que a nuvem de pontos confirmou como executado. E o vermelho é o que estava previsto e não foi feito. Estamos na semana 22: repare que o planejado está um pouco acima do executado, e o índice de avanço aparece no alto. Agora eu arrasto até a semana 40. Olha como o vermelho cresce: a obra vai perdendo um pouco de ritmo a cada laje, e o atraso se acumula. Na planilha da reunião, isso é um número. No 4D, você vê onde está o atraso, em que pavimento e desde quando."

> "E o 4D não serve só para olhar para trás. Ele serve para planejar. Com o modelo no tempo, eu consigo ver, antes de acontecer, que na semana 30 a grua vai precisar içar fôrmas para dois pavimentos ao mesmo tempo, ou que a escavação de uma frente vai coincidir com a concretagem da laje vizinha. É a logística da obra desenhada no modelo. E, quando o drone confirma o executado, o planejamento se ajusta: a obra real corrige o plano, e o plano orienta a obra real. Isso também é malha fechada, só que aplicada ao prazo."

### 6. Realidade capturada: scan-to-BIM e scan-vs-BIM (8:40 – 10:50)

**[TELA]** Slide 9 — galeria: laser scanner terrestre, nuvem de pontos e scan-to-BIM.

> "Mas como eu sei o que foi construído? Pela realidade capturada. Na tela, à esquerda, um laser scanner terrestre: ele gira sobre o tripé e mede milhões de pontos com exatidão milimétrica, de perto. No meio, uma nuvem de pontos de uma fachada histórica: cada ponto tem posição e cor. E, à direita, um caso de scan-to-BIM: a nuvem em cinza e, sobre ela, a tubulação modelada. E não esqueça o drone da Unidade 2: fotogrametria ou LiDAR embarcado geram a mesma nuvem, só que do canteiro inteiro, num único voo."

**[TELA]** Slide 10 — scan-to-BIM × scan-vs-BIM e o registro da nuvem.

> "E aqui tem uma distinção que muita gente confunde. Scan-to-BIM é modelar a partir da nuvem: você usa os pontos para criar o modelo as-built de uma estrutura existente ou recém-executada. Por exemplo: modelar o sobrado vizinho antes da escavação. Scan-vs-BIM é outra coisa: é comparar a nuvem com o modelo de projeto, o as-designed. Aí eu respondo duas perguntas: está no lugar certo? E já foi executado? Só que, antes de qualquer comparação, vem um passo que não pode ser esquecido: o registro. A nuvem precisa estar alinhada no mesmo sistema de coordenadas do modelo, com pontos de controle. Se o registro tiver um erro de 2 centímetros, a obra inteira vai aparecer 2 centímetros fora de posição — e o problema não está na obra, está no alinhamento."

### 7. Comparação as-built × as-designed (10:50 – 13:40)

**[TELA]** Slide 11 — mapa de calor dos desvios de uma laje: mexa na tolerância e na incerteza.

> "Agora a comparação propriamente dita. Na comparação nuvem-modelo, em inglês cloud-to-model, o software calcula, para cada ponto, a distância até a superfície correspondente do modelo. E pinta o resultado num mapa de calor. Olha a tela: é a planta de uma laje de 30 por 20 metros, com os pilares em contorno branco. Os pontos verdes estão dentro da tolerância. E repare em duas regiões: no meio do vão, uma flecha, e na borda direita, um trecho executado fora de posição. Com tolerância de 10 milímetros e incerteza de 3, os contadores no alto mostram quanto da laje está conforme, quanto está inconclusivo e quanto está fora. Agora eu diminuo a tolerância para 6 milímetros: olha o amarelo e o vermelho se espalhando. Volto para 10 e aumento a incerteza para 6: a faixa amarela, a do inconclusivo, cresce. Ou seja: uma medição ruim não diz nem que está bom, nem que está ruim."

**[TELA]** Slide 12 — conforme, não conforme ou inconclusivo; o fluxo até a pendência no BCF.

> "E isso nos leva à regra de decisão, que você já conhece da Aula 2. O desvio medido tem incerteza. Então: se o desvio mais a incerteza ficar abaixo da tolerância, o elemento é conforme — mesmo no pior caso, ele está dentro. Se o desvio menos a incerteza ficar acima da tolerância, é não conforme — mesmo no melhor caso, ele está fora. E se a tolerância cair dentro do intervalo, é inconclusivo: a medição não decide, e é preciso medir de novo com um método mais exato. O fluxo completo é este: nuvem, registro, distância de cada ponto ao modelo, mapa de calor e, para cada não conformidade, uma pendência presa ao GUID do elemento. No openBIM, essa pendência tem formato próprio, o BCF, BIM Collaboration Format: elemento, problema, responsável e prazo. A decisão sai daí."

### 8. Exemplo numérico (13:40 – 15:20)

**[TELA]** Slide 13 — calculadora: o pilar P7 e o avanço medido no 4D.

> "Vamos fazer as contas. A comparação nuvem-modelo do pilar P7 deu um desvio de 12 milímetros em x e de menos 9 em y. Desvio de posição é a distância entre o eixo executado e o de projeto, então eu uso Pitágoras: raiz de 12 ao quadrado mais 9 ao quadrado. 144 mais 81 dá 225. Raiz de 225: 15 milímetros. A incerteza expandida do levantamento, somando registro e nuvem, é de 3 milímetros, e a tolerância contratual é 10. Desvio menos incerteza: 15 menos 3, 12 milímetros. Doze é maior que dez. Então, mesmo descontando a incerteza, o pilar está fora: não conforme. A pendência vai para o projetista estrutural avaliar a excentricidade adicional. Olha as barras: o d menos U, o d, o d mais U e a tolerância lá embaixo."

> "Agora mexo no controle: se o desvio em x fosse 8 e em y fosse 6, o desvio daria 10, e o intervalo iria de 7 a 13. A tolerância está dentro: inconclusivo. E o avanço: o 4D previa 420 metros cúbicos de concreto até a data do voo; a nuvem confirmou elementos que somam 378. 378 dividido por 420 dá 0,90. Noventa por cento do previsto. Aquele '62% conforme o cronograma' da reunião precisa ser revisto. E, no texto da aula, tem ainda um terceiro cálculo: de 48 mil pontos da laje, 45.600 ficaram dentro da tolerância, ou seja, 95% da superfície conforme."

### 9. Do modelo ao gêmeo digital (15:20 – 16:40)

**[TELA]** Slide 14 — gêmeo digital em 3D: clique em Simular recalque.

> "Agora a última peça. Pegue os sensores da Unidade 3 — inclinômetros, piezômetros, marcos de recalque — e associe o identificador de cada um ao GUID do elemento do modelo. As leituras chegam pela plataforma IoT e pintam o modelo pelo nível de alerta: verde, amarelo, vermelho. Nesse ponto, pela classificação de Kritzinger que você viu na Aula 1, o modelo virou uma sombra digital: o dado vai sozinho do canteiro para o modelo. Clico em simular recalque: o prédio real inclina, e o modelo acompanha e muda de cor. Quando a decisão também volta automaticamente para a obra — a plataforma reprograma a frente de escavação no 4D e aciona a equipe —, aí sim temos um gêmeo digital. E repare: na prática da construção, o mais comum, e muito útil, é a sombra digital com um engenheiro fechando a malha."

> "Um cuidado final: o modelo só merece confiança se o vínculo entre sensor e elemento estiver certo. Se o inclinômetro I-2 estiver associado, por engano, ao trecho errado da cortina, o modelo vai pintar de vermelho a parede que está bem e deixar verde a que está se mexendo. Por isso, a associação entre sensor e GUID também é informação gerida: tem dono, é conferida em campo e fica registrada no ambiente comum de dados."

### 10. Atividade e encerramento (16:40 – 17:50)

**[TELA]** Slide 15 — atividade prática: classifique seis pilares.

> "A atividade de hoje: pegue a planta de formas de um pavimento-tipo — pode ser de um projeto acadêmico. Escolha seis pilares e invente desvios em x e em y de uma comparação nuvem-modelo. Com tolerância de 10 milímetros e incerteza de 3, classifique cada um: conforme, não conforme ou inconclusivo. E redija a pendência do pior caso, no formato do BCF: elemento, problema, responsável e prazo."

**[TELA]** Slide 16 — pontos-chave; Slide 17 — encerramento.

> "Recapitulando: BIM é modelo de informação, e o IFC com o GUID liga sensores, fotos e pendências a cada elemento. 4D é modelo mais cronograma; 5D, mais custos. Desde 2024, as obras federais abrangidas usam BIM na execução e no as-built. Scan-to-BIM modela o existente; scan-vs-BIM compara com o projeto. Conformidade se decide com desvio, tolerância e incerteza. E dado automático no modelo é sombra digital; quando a decisão volta à obra, é gêmeo. Mas fica uma pergunta: o drone voltou com 3.200 fotos de fachada. Quem vai olhar todas? Na próxima aula, a inteligência artificial entra em campo. Te espero na Aula 14!"

---

## Roteiro da Videoaula 14 — "IA e visão computacional: detecção de fissuras e medição de avanço físico"

**Duração-alvo:** cerca de 17:40 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e seja bem-vindo, bem-vinda à Aula 14. Na aula passada, o BIM juntou cronograma, nuvem de pontos e sensores num modelo só. Hoje vamos falar de um assunto que está em toda manchete: inteligência artificial. Mas a gente vai olhar para ela como engenheiro, e não como torcedor. Que tarefa ela faz, como aprende, quanto erra e onde estão os limites."

**[TELA]** Slide 3 — foto: 3.200 fotos de fachada.

> "A situação é esta. O drone inspecionou as quatro fachadas do edifício e a estrutura do estacionamento e voltou com 3.200 fotos em alta resolução. Em algum lugar delas há fissuras. Algumas inofensivas, outras não. Um inspetor experiente leva dias para revisar tudo isso. E, sendo humano, lá pela foto 2.800 já está cansado e deixa passar alguma coisa. Um modelo de inteligência artificial revisa as 3.200 fotos em minutos. Ótimo. Mas aí vêm as perguntas de engenheiro: quanto ele erra? Que tipo de erro ele comete? E dá para medir a largura da fissura na foto? Essas são as três perguntas desta aula."

### 2. Três tarefas da visão computacional (1:40 – 3:30)

**[TELA]** Slide 4 — classificação, detecção e segmentação; a IoU.

> "Visão computacional é o ramo da inteligência artificial que extrai informação de imagens. Na obra, três tarefas aparecem o tempo todo. A primeira é a classificação: a foto inteira recebe um rótulo. Tem fissura, não tem fissura. A segunda é a detecção: o modelo desenha uma caixa em volta de cada objeto que encontra — um capacete, um caminhão, uma armadura exposta. E a terceira é a segmentação: cada pixel da imagem recebe um rótulo. Este pixel é fissura, aquele é concreto. A segmentação é a mais trabalhosa, mas é a única que permite medir comprimento e largura."

> "Olha a imagem à direita. A caixa verde é a referência, desenhada por uma pessoa. A caixa vermelha é a previsão do detector. Como eu sei se a detecção foi boa? Pela IoU, intersection over union: a área em que as duas caixas se sobrepõem dividida pela área total que as duas ocupam juntas. Se as caixas coincidem perfeitamente, a IoU é 1. Na prática, uma IoU acima de 0,5 costuma contar como acerto."

> "E qual tarefa usar? Depende da pergunta. Se a pergunta é 'em quais destas 3.200 fotos eu preciso olhar?', classificação basta. Se é 'quantos trabalhadores estão sem capacete na frente norte?', é detecção. E se é 'qual o comprimento e a largura desta fissura, e ela cresceu desde o mês passado?', só a segmentação responde. Quanto mais fina a tarefa, mais caro é rotular os dados: marcar pixel a pixel uma fissura leva muito mais tempo do que dizer 'tem' ou 'não tem'."

### 3. Redes neurais convolucionais (3:30 – 5:10)

**[TELA]** Slide 5 — animação de convolução: troque o filtro.

> "E qual é o motor por trás disso? A rede neural convolucional, a CNN. Olha a animação. À esquerda, um recorte de concreto com uma fissura escura. Um pequeno filtro, de 3 por 3 pixels — o quadrado azul —, percorre a imagem, e, a cada posição, faz uma conta com os pixels embaixo dele. O resultado vai formando, à direita, o mapa de ativação: ele acende onde o filtro encontrou o padrão que procura. Com o filtro de linha escura, o mapa acende ao longo da fissura. Agora eu troco para borda vertical: acendem os trechos em que a fissura corre na vertical. Borda horizontal: acende a ramificação."

> "Numa CNN de verdade, há dezenas de camadas com centenas desses filtros. As primeiras respondem a bordas e contrastes; as do meio, a texturas; as últimas, a padrões complexos, como 'fissura ramificada'. E o ponto central: ninguém programa esses filtros à mão. Eles são aprendidos a partir de milhares de exemplos rotulados. É o chamado aprendizado supervisionado. Para segmentação, usam-se arquiteturas do tipo codificador-decodificador, como a U-Net, que devolvem um mapa do tamanho da imagem com a probabilidade de cada pixel ser fissura."

> "E como a rede aprende? De um jeito parecido com a calibração da Aula 2. Ela recebe uma foto rotulada, faz uma previsão, compara com o rótulo e mede o erro. Depois ajusta um pouquinho os números dos filtros na direção que diminui esse erro. E repete isso milhares, às vezes milhões de vezes, com milhares de fotos. No começo, os filtros são aleatórios e a rede chuta. No fim, os filtros viraram detectores de bordas, de texturas e de fissuras. Não tem mágica: tem muito exemplo, muita repetição e uma medida de erro bem definida."

### 4. Treinar: dados antes de algoritmo (5:10 – 6:50)

**[TELA]** Slide 6 — coletar, rotular, separar, aumentar e testar.

> "Se a rede aprende com exemplos, a qualidade do modelo depende, antes de tudo, dos dados. O fluxo tem cinco passos. Coletar imagens representativas: concretos claros e escuros, sol e sombra, fachada molhada, manchas, sujeira, juntas. Rotular, com especialistas marcando o que é fissura e o que só parece fissura. Separar em três conjuntos: treino, validação e teste — e o teste nunca, nunca é visto no treino. Aumentar os dados, o data augmentation: girar, espelhar, mudar brilho e contraste das imagens de treino para o modelo não decorar o conjunto. E, por fim, testar com fotos novas."

> "Dois termos para guardar. Sobreajuste, ou overfitting: o modelo acerta tudo no treino e falha em fotos novas, porque decorou em vez de aprender. E transferência de aprendizado: em vez de começar do zero, parte-se de uma rede já treinada em milhões de imagens e ajusta-se a rede ao problema. E existem bases públicas para começar, como a de 40 mil recortes de concreto, com e sem fissura, publicada por Özgenel em 2019."

**[TELA]** Slide 7 — galeria: fissura em muro, ponte vista por drone e inspeção com caminhão e drone.

> "Olha a galeria. À esquerda, uma fissura num muro de contenção: fácil para nós, difícil de padronizar para uma máquina. No meio, uma ponte vista por drone: uma inspeção dessas gera milhares de fotos. E, à direita, o drone complementando o caminhão com braço articulado numa inspeção de ponte. É nesse volume de imagens que a IA faz diferença."

### 5. Avaliar: matriz de confusão (6:50 – 9:00)

**[TELA]** Slide 8 — matriz de confusão: 1.000 fotos, 80 com fissura.

> "Agora a pergunta mais importante: quanto o modelo erra? Para responder, a gente testa o modelo num conjunto de mil fotos, 80 delas com fissura, e monta a matriz de confusão. São quatro caixas. Verdadeiro positivo: tinha fissura e o modelo achou — 72. Falso negativo: tinha fissura e o modelo não achou — 8. Falso positivo: não tinha fissura, mas o modelo deu alarme, uma mancha tomada por fissura — 48. E verdadeiro negativo: concreto são, corretamente ignorado — 872."

> "Daí saem as métricas. Precisão responde 'dos alarmes, quantos eram fissura de verdade?': 72 dividido por 72 mais 48, ou seja, 72 sobre 120, 0,60. Revocação, o recall, responde 'das fissuras que existiam, quantas o modelo achou?': 72 sobre 80, 0,90. E o F1, a média harmônica das duas: 2 vezes 0,60 vezes 0,90, dividido por 1,50, dá 0,72. Agora, a armadilha. A acurácia — acertos sobre o total — dá 72 mais 872, sobre mil: 94,4%. Parece ótima. Mas um 'modelo' que responde sempre 'sem fissura', sem olhar a foto, acertaria 920 de mil: 92%. E não acharia nenhuma fissura! Quando a classe que interessa é rara, a acurácia engana. Olhe sempre precisão e revocação."

### 6. O limiar e o custo de cada erro (9:00 – 11:10)

**[TELA]** Slide 9 — histogramas das notas e o limiar ajustável. Comece em 0,50, desça para 0,30 e suba para 0,75.

> "O modelo não responde sim ou não: ele dá uma nota, uma probabilidade de haver fissura. Quem decide a partir de que nota a foto vira alarme é o engenheiro, escolhendo o limiar. Olha a tela. Em verde, as notas das fotos sem fissura, concentradas à esquerda. Em vermelho, as das fotos com fissura, concentradas à direita. E elas se sobrepõem no meio. A linha amarela é o limiar, em 0,50. Agora eu desço para 0,30: repare que quase todas as fissuras ficam à direita da linha — a revocação sobe —, mas muitas fotos verdes também passam, e os falsos positivos aumentam. Subo para 0,75: os alarmes falsos quase somem, mas começo a perder fissuras. Não existe limiar que zere os dois erros. Existe a escolha."

> "E onde essa escolha é feita? No conjunto de validação, nunca no de teste. A equipe testa vários limiares nas fotos de validação, olha a revocação e o número de fotos a revisar em cada um e escolhe o ponto que atende ao objetivo da inspeção. Só depois roda o teste, uma vez, para ter a medida honesta do desempenho. Se você ajusta o limiar olhando o teste, está se enganando: o número fica bonito no relatório e piora na obra."

**[TELA]** Slide 10 — falso positivo × falso negativo.

> "E como escolher? Pelo custo de cada erro. Um falso positivo é uma mancha, uma junta, uma sombra marcada como fissura. Custa alguns minutos de revisão do engenheiro. Se forem alarmes demais, cansa a equipe — então não pode ser absurdo. Já um falso negativo é uma fissura real que passou despercebida. Custa um dano que evolui sem resposta. Em segurança estrutural, o falso negativo é o erro mais caro. A regra prática é: limiar que dê revocação alta, mais revisão humana de tudo o que a IA marcar."

### 7. Da fissura ao milímetro (11:10 – 13:40)

**[TELA]** Slide 11 — calculadora: quantos pixels cabem sobre a fissura?

> "Segunda grande pergunta: dá para medir a fissura na foto? Detectar não é medir. Para medir a largura, a fissura precisa ocupar alguns pixels — na prática, pelo menos 2. E o tamanho do pixel no objeto é o nosso velho conhecido da Unidade 2, o GSD: largura do sensor vezes distância, dividido por distância focal vezes largura da imagem em pixels. Vamos com uma câmera de sensor de 13,2 milímetros, distância focal de 8,8 e imagem de 5.472 pixels, a 5 metros da fachada. 13,2 vezes 5.000, dividido por 8,8 vezes 5.472: dá cerca de 1,37 milímetro por pixel. Uma fissura de 0,3 milímetro ocupa 0,3 dividido por 1,37: 0,22 pixel. Um quinto de pixel. Impossível medir."

> "Para ter 2 pixels, eu preciso de GSD de 0,15 milímetro por pixel. Mexo na distância: seria preciso fotografar a uns 55 centímetros da fachada. Com drone, junto à parede, isso é inviável com segurança. A alternativa é a lente: volto para 5 metros e aumento a distância focal para uns 80 milímetros — um zoom. Olha a barra: agora a fissura cabe em 2 pixels, e a calculadora diz que mede a largura."

**[TELA]** Slide 12 — limites de abertura de fissuras da ABNT NBR 6118.

> "E por que meio milímetro importa tanto? Porque a ABNT NBR 6118 limita a abertura característica das fissuras no concreto armado em 0,4 milímetro na classe de agressividade ambiental I, 0,3 nas classes II e III e 0,2 na classe IV. Na terceira coluna, o GSD necessário para medir com 2 pixels: de 0,20 a 0,10 milímetro por pixel. É submilimétrico. Um detalhe: fissuras finas às vezes aparecem na foto mesmo menores que um pixel, pelo contraste da sombra. Mas aparecer não é medir. A IA faz a triagem; o fissurômetro da Unidade 3 continua acompanhando a abertura."

### 8. Avanço físico e humano no laço (13:40 – 16:30)

**[TELA]** Slide 13 — foto aérea de um condomínio em construção.

> "A mesma técnica tem um segundo uso enorme: medir avanço. Olha essa foto aérea: um condomínio em que cada prédio está num estágio diferente — uns com cobertura, outros só com estrutura. No ortomosaico do drone ou em câmeras fixas, detectores e segmentadores reconhecem fôrmas, armaduras, lajes concretadas, alvenaria, cobertura. E, cruzando com o BIM 4D da aula passada, o percentual executado sai por elemento, sem planilha preenchida à mão."

> "Tem também a versão com câmeras fixas: uma câmera no alto da grua ou num poste tira uma foto a cada hora, e a IA conta quantas betoneiras chegaram, quanto tempo a bomba de concreto ficou parada, quantas lajes foram concretadas na semana. Isso é produtividade medida, e não estimada. Mas atenção: essa mesma câmera filma pessoas, e por isso a finalidade e o enquadramento precisam ser pensados desde o início."

**[TELA]** Slide 14 — a IA classifica 12 trechos de laje; compare com o 4D, semana a semana.

> "Na tela, um pavimento dividido em 12 trechos de laje. A varredura da IA classifica cada trecho: fôrma, armação ou concretado, com a confiança da classificação. Cada estágio tem um peso: fôrma 30%, armação 60%, concretado 100%. O avanço é a média ponderada, e o painel compara com o previsto no 4D. Repare no trecho com borda vermelha: confiança abaixo de 70%. Esse vai para revisão humana. Clico na semana 11 e na 12: o avanço medido cresce, e dá para ver se está acompanhando o planejado."

**[TELA]** Slide 15 — limites da IA: dados enviesados, causa e gravidade, pessoas na imagem.

> "E os limites. Primeiro, dados enviesados: um modelo treinado só com concreto claro e sol erra em fachada escura, molhada ou suja. O conjunto de teste precisa parecer a sua obra. Segundo, causa e gravidade: a IA diz 'aqui tem fissura'. Se é retração, recalque ou corrosão, se está ativa ou estabilizada, isso é diagnóstico de engenharia, com responsabilidade técnica. E terceiro: câmeras com IA que detectam capacete também filmam trabalhadores. Isso tem implicações de privacidade, que é assunto da próxima aula. Resumo: a IA faz a triagem; o engenheiro decide."

### 9. Atividade e encerramento (16:30 – 17:40)

**[TELA]** Slide 16 — atividade prática: qual limiar usar na inspeção do viaduto?

> "Atividade. Uma inspeção com IA em 2 mil fotos de um viaduto tem duas opções de limiar. Com 0,5: 120 verdadeiros positivos, 30 falsos positivos e 30 falsos negativos. Com 0,3: 141 verdadeiros positivos, 94 falsos positivos e só 9 falsos negativos. Calcule precisão, revocação e F1 das duas opções, decida qual usar numa inspeção de segurança e estime quantas fotos a equipe vai revisar em cada caso."

**[TELA]** Slide 17 — pontos-chave; Slide 18 — encerramento.

> "Recapitulando: três tarefas — classificação, detecção e segmentação. CNNs aprendem filtros com dados rotulados, e dado vem antes de algoritmo. Avalie com precisão, revocação e F1, nunca só com acurácia; em segurança, o falso negativo custa mais. Para medir largura, pelo menos 2 pixels sobre a fissura: o GSD decide. E a IA faz triagem e mede avanço com o 4D, mas a decisão é do engenheiro. Só que tudo isso custa dinheiro, filma pessoas e trafega dados pela internet. Vale a pena? Pode filmar? Está seguro? De quem são os dados? Na próxima aula, a gestão do monitoramento. Te espero na Aula 15!"

---

## Roteiro da Videoaula 15 — "Gestão do monitoramento: custo-benefício, LGPD, segurança da informação e contratos"

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 15. Até aqui, a disciplina foi muito técnica: sensores, drones, BIM, inteligência artificial. Hoje a conversa muda de sala. Sai do canteiro e vai para a sala de reunião. Porque um sistema de monitoramento tecnicamente perfeito, se não for aprovado, contratado e operado com responsabilidade, não sai do papel."

**[TELA]** Slide 3 — foto: as quatro perguntas da reunião de aprovação.

> "O plano de monitoramento está pronto: inclinômetros, piezômetros, voo mensal de drone, câmeras com IA e uma plataforma na nuvem. Na reunião de aprovação, quatro pessoas fazem quatro perguntas. O diretor financeiro: vale o que custa? A advogada: podemos filmar os trabalhadores e a casa do vizinho? O gerente de TI: e se alguém invadir o gateway e apagar as leituras? E o cliente: de quem são esses dados e quem atende o alerta às 3 da manhã? Hoje você vai aprender a responder às quatro."

### 2. Quanto custa e quanto vale (1:30 – 5:40)

**[TELA]** Slide 4 — CAPEX + OPEX.

> "Primeira pergunta: quanto custa. O custo tem duas partes. O CAPEX é o investimento inicial: instrumentos, instalação, dataloggers, gateway, licenças, o drone e as câmeras. O OPEX é o custo mensal: conectividade, plataforma, voos e processamento, manutenção, recalibração de sensores, troca de baterias. E tem um item que quase todo orçamento esquece: as horas de engenheiro para analisar os dados e responder aos alertas. Um sistema sem orçamento para análise é exatamente a malha aberta da Aula 1 — só que agora com conta de luz."

**[TELA]** Slide 5 — calculadora: valor esperado e retorno.

> "E quanto vale? O benefício principal do monitoramento é evitar perdas: dano ao vizinho, colapso parcial, paralisação, retrabalho. Como essas perdas são incertas, a gente usa o valor esperado: probabilidade vezes consequência. E o monitoramento atua nos dois fatores. Reduz a probabilidade, porque o problema é corrigido no começo. E reduz a consequência, porque o dano detectado cedo é menor."

> "Vamos ao exemplo. Monitoramento de uma escavação ao lado de um prédio antigo, por 14 meses. CAPEX de 180 mil reais e OPEX de 12 mil por mês. Custo total: 180 mil mais 14 vezes 12 mil, ou seja, 348 mil reais. Sem monitoramento, a equipe estima 8% de probabilidade de um dano relevante ao vizinho, com consequência de 5 milhões. Valor esperado: 0,08 vezes 5 milhões, 400 mil. Com monitoramento, a probabilidade cai para 2%, e o dano, detectado cedo, custaria 2 milhões: 0,02 vezes 2 milhões, 40 mil. A perda evitada é a diferença: 360 mil. Somo 90 mil de ganhos diretos — medições por drone, menos retrabalho — e o benefício vai a 450 mil. O retorno é 450 menos 348, dividido por 348: cerca de 29%."

> "Agora o mais importante: esses números são ilustrativos. Probabilidade de dano é estimativa. Então mexa nos controles. Se a probabilidade sem monitoramento for 5% em vez de 8%, olha o retorno cair. É isso que se chama análise de sensibilidade: descobrir a partir de que probabilidade o sistema deixa de se pagar."

> "Vamos fazer essa conta juntos. Mantendo os outros números, o benefício é a probabilidade sem monitoramento vezes 5 milhões, menos os 40 mil do cenário com monitoramento, mais os 90 mil de ganhos diretos. Para empatar com os 348 mil de custo, a probabilidade sem monitoramento precisa ser de cerca de 6%. Ou seja: se a equipe acredita que o risco de dano ao vizinho está acima de 6%, o sistema se paga só com dinheiro. Abaixo disso, a decisão passa a depender do que não se monetiza. É esse tipo de frase que convence um diretor financeiro: não um número mágico, mas um limite claro para discutir."

**[TELA]** Slide 6 — o que a planilha não mostra.

> "E leia a conta com senso crítico. Tem o que não se monetiza: vidas, reputação, a relação com a vizinhança e a responsabilidade técnica de quem assina a obra. Tem a incerteza das probabilidades, que pede faixas e sensibilidade. E tem os custos esquecidos: horas de análise, recalibração, baterias, plantão para alerta fora do expediente. Quem leva só a planilha bonita para a reunião perde a discussão na primeira pergunta difícil."

### 3. LGPD: dado pessoal no canteiro (5:40 – 9:50)

**[TELA]** Slide 7 — dado pessoal: rostos, placas, vizinhança, localização e acessos.

> "Segunda pergunta: pode filmar? Aqui entra a Lei Geral de Proteção de Dados, a LGPD, Lei 13.709 de 2018. Ela define dado pessoal como informação relacionada a pessoa natural identificada ou identificável. Pense no monitoramento: rostos de trabalhadores e vizinhos nas fotos de drone e nas câmeras. Placas de veículos. O quintal, a piscina e a janela da casa ao lado. A localização de trabalhadores rastreados. E até o registro de quem acessou a plataforma. Tudo isso é dado pessoal. E tem uma categoria mais delicada: biometria, como o reconhecimento facial, é dado pessoal sensível, com regras mais restritas."

**[TELA]** Slide 8 — bases legais e princípios.

> "Todo tratamento de dado pessoal precisa de uma base legal, listada no artigo 7º. Consentimento é uma delas, mas não a única — e, numa obra, raramente a melhor. Olha a tabela: cumprimento de obrigação legal, para os registros exigidos pelas normas de segurança do trabalho; execução de contrato, para o controle de acesso dos trabalhadores contratados; proteção da vida e da incolumidade física, para o alerta de pessoa em área de risco; e legítimo interesse, por exemplo, para as fotos de drone que medem o avanço, desde que com minimização e avaliação de impacto. E, além da base legal, os princípios do artigo 6º. Três pesam muito aqui: finalidade — para que serve o dado; necessidade — usar o mínimo possível; e transparência — avisar quem está sendo filmado."

> "Repare num detalhe do legítimo interesse. Ele não é um cheque em branco. Para usá-lo, a empresa precisa ponderar: o meu interesse — medir o avanço da obra — é legítimo? Dá para atingi-lo com menos dados? E o que o titular razoavelmente espera? A vizinha não espera que o drone da obra fotografe a piscina dela toda semana. Então, se o voo precisa passar sobre o lote vizinho, a resposta não é desistir do voo: é enquadrar, mascarar e descartar o que não interessa à engenharia."

**[TELA]** Slide 9 — a cena da câmera: ligue máscara, desfoque e retenção.

> "Na prática, como fica? Olha a cena: a câmera do canteiro vê a casa vizinha, com uma pessoa na janela e outra na piscina, os trabalhadores na escavação e um carro com a placa visível na rua. O contador mostra os dados pessoais expostos. Ligo a máscara de privacidade: o lote vizinho fica preto. Ligo o desfoque de rostos e placas: os rostos viram mosaico, a placa some. E ligo a retenção de 30 dias: as imagens guardadas param de crescer sem fim e caem para o prazo definido. Repare que o que interessa à engenharia — a escavação, o capacete, o avanço — continua visível. A gente perdeu dado pessoal, não perdeu informação de obra."

**[TELA]** Slide 10 — governança: papéis, relatório de impacto, incidentes e sanções.

> "E a governança. Dois papéis definidos em contrato: o controlador, que decide sobre o tratamento, e o operador, que trata em nome dele — muitas vezes, a empresa de monitoramento. Para tratamentos de risco, um relatório de impacto, o RIPD, e um encarregado indicado. Se houver um incidente de segurança com risco relevante aos titulares, ele precisa ser comunicado à ANPD, a Autoridade Nacional de Proteção de Dados; o regulamento da ANPD fixa, como regra, 3 dias úteis. E as sanções incluem multa de até 2% do faturamento, limitada a 50 milhões de reais por infração."

### 4. Segurança da informação (9:50 – 12:50)

**[TELA]** Slide 11 — foto do data center: confidencialidade, integridade e disponibilidade.

> "Terceira pergunta: e se alguém invadir? A segurança da informação protege três propriedades. Confidencialidade: só quem pode, vê. Integridade: o dado não foi alterado. Disponibilidade: o dado está lá quando eu preciso. No monitoramento de obra, a mais crítica é a integridade. Pense bem: uma leitura adulterada pode esconder um recalque. Um limite de alerta alterado por alguém sem autorização pode silenciar o sistema. E a disponibilidade vem logo atrás, porque o alerta precisa chegar às 3 da manhã. A referência de gestão para isso é a ISO/IEC 27001, de sistemas de gestão de segurança da informação."

**[TELA]** Slide 12 — a cadeia do dado: ligue os controles um a um.

> "Olha a cadeia do dado: sensor, gateway, servidor de rede e broker, plataforma e painel. Cada elo vulnerável aparece em vermelho, e o invasor vai tentando entrar por eles. Embaixo, o gráfico mais importante: em amarelo, o recalque real subindo; em azul, o valor que aparece no painel. Com a integridade comprometida, o painel mostra um valor estável — o painel mente. A lista de vulnerabilidades de IoT do OWASP põe em primeiro lugar as senhas fracas, padrão ou embutidas. Então, primeiro controle: trocar a senha padrão. Segundo: MQTT com TLS — o LoRaWAN já cifra as mensagens de rádio com chaves AES-128, mas o caminho até a plataforma também precisa de criptografia. Terceiro: segmentação e privilégio mínimo, cada usuário só com o acesso de que precisa. Olha: com esses três, o painel volta a dizer a verdade. E completo com firmware atualizado e logs com cópia de segurança, para saber quem mudou o limite de alerta."

> "Pode parecer exagero pensar em ataque a um sistema de obra. Mas boa parte dos incidentes em IoT não é um ataque sofisticado. É um gateway exposto na internet com a senha de fábrica, encontrado por um robô que varre endereços o dia inteiro. Ou um ex-funcionário que ainda tem o login compartilhado da equipe. Ou um técnico que, para 'parar de tocar alarme', aumenta o limite de alerta sem avisar ninguém. Os controles que acabamos de ligar resolvem exatamente esses casos."

**[TELA]** Slide 13 — checklist mínimo antes de ligar o sistema.

> "Resumi tudo num checklist mínimo, para conferir antes de ligar o sistema: credenciais padrão trocadas, comunicação criptografada, contas individuais, rede segmentada, firmware atualizado, logs e cópias de segurança, inventário de dados pessoais com minimização e plano de resposta a incidentes. Eu clico em cada item, e a barra completa. Segurança e privacidade são requisitos de projeto, verificados antes da primeira leitura — e boa parte dessa lista vai virar cláusula do contrato."

### 5. Contratos, SLA e plano de resposta (12:50 – 16:20)

**[TELA]** Slide 14 — o plano de monitoramento como anexo do contrato.

> "Quarta pergunta: de quem são os dados e quem atende o alerta? A resposta está no contrato. Primeiro princípio: o plano de monitoramento é anexo do contrato, e não um extra. E ele precisa de seis blocos de cláusulas. Escopo: grandezas, instrumentos, posições e frequências. Níveis e resposta: quem faz o quê, em quanto tempo, em cada nível — o que se chama de TARP, trigger-action-response plan. SLA: disponibilidade da plataforma, tempo entre a leitura e o painel, prazo para reparar um sensor. Propriedade dos dados: do contratante, entregues em formato aberto, como CSV e IFC, no fim da obra. Confidencialidade e LGPD: os papéis de controlador e operador, a comunicação de incidentes, os requisitos de segurança. E responsabilidade técnica: a ART do profissional responsável pelo monitoramento."

> "Quero insistir na propriedade dos dados, porque é onde muita obra se complica. Imagine que, no meio da obra, a construtora troca de fornecedor de monitoramento. Se o contrato não disser que os dados são do contratante e que serão entregues em formato aberto, as séries históricas — o marco zero de todos os sensores — podem ficar presas na plataforma antiga. E, sem o histórico, o novo fornecedor começa do zero, sem saber se aquele recalque de 9 milímetros é novo ou acumulado. Dado de monitoramento só tem valor com a série completa."

**[TELA]** Slide 15 — calculadora de SLA.

> "Vamos traduzir um SLA em horas. Disponibilidade de 99,5% num mês de 30 dias. O que sobra é 0,5%: 30 vezes 24 vezes 0,005, que dá 3,6 horas fora do ar por mês. Parece pouco. Mas, se a escavação crítica pode precisar de um alerta justamente nessas 3,6 horas, o contrato deve pedir mais disponibilidade e, além disso, uma regra que funcione na borda, sem depender da nuvem, como vimos na Aula 3. Mexo para 99,9%: 43 minutos por mês."

**[TELA]** Slide 16 — o plano de resposta no contrato: verde, amarelo, laranja e vermelho.

> "E o plano de resposta. Olha a tabela: verde, rotina de leitura e relatório. Amarelo, atenção atingida: aumentar frequência, inspecionar e preparar o reforço, com o engenheiro da obra respondendo em 24 horas. Laranja, velocidade alta rumo ao alerta: reduzir o ritmo na frente e mobilizar o reforço, em 6 horas. Vermelho, alerta atingido: parar a frente, executar o reforço, avisar os vizinhos, com o responsável técnico de plantão, imediatamente. Os gatilhos vêm do projeto; os prazos, do contrato. E uma regra de ouro: sem nome e telefone ao lado de cada nível, o plano não funciona às 3 da manhã."

**[TELA]** Slide 17 — pausa para reflexão: segurança do trabalho ou vigilância?

> "Agora, uma pausa para reflexão. A construtora quer instalar reconhecimento facial em todos os acessos e uma IA que identifica, pelo rosto, quem está sem capacete, para aplicar advertências. O argumento é a segurança do trabalho — e ele é legítimo. Mas reconhecimento facial trata dado biométrico, sensível. Existem alternativas menos invasivas: crachá com RFID no acesso; detecção de capacete sem identificar a pessoa, com um alerta ao encarregado da frente. E tem o fator humano: trabalhadores que se sentem vigiados confiam menos. Então eu te pergunto: onde termina a segurança e começa a vigilância? Pese a finalidade, a necessidade — dá para atingir o objetivo com menos dados? —, a transparência, o prazo de guarda e quem vai ter acesso às imagens."

### 6. Atividade e encerramento (16:20 – 18:00)

**[TELA]** Slide 18 — atividade prática e pontos-chave.

> "A atividade é montar uma ficha de gestão do monitoramento para a obra da próxima aula, ou para outra que você escolher. Quatro partes: CAPEX, OPEX e o cálculo do valor esperado da perda evitada; o inventário de dados pessoais, com base legal e medida de minimização para cada um; cinco controles de segurança da informação; e as cláusulas contratuais, com um SLA numérico."

> "Recapitulando: custo é CAPEX mais OPEX, incluindo as horas de análise; benefício é perda evitada mais ganhos diretos. Imagens de obra contêm dados pessoais e precisam de base legal, finalidade e minimização; biometria é dado sensível. No monitoramento, integridade é segurança estrutural: senha padrão trocada, criptografia, segmentação e logs. E o plano de monitoramento é anexo do contrato, com escopo, plano de resposta, SLA, dados em formato aberto e ART."

**[TELA]** Slide 19 — encerramento.

> "Agora você sabe defender o monitoramento na reunião de aprovação. Na próxima aula, a última da disciplina, a gente junta tudo num projeto integrado de uma obra real, do primeiro sensor ao último contrato. Te espero na Aula 16!"

---

## Roteiro da Videoaula 16 — "Projeto integrado de monitoramento de uma obra (fechamento da disciplina)"

**Duração-alvo:** cerca de 18:10 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:50)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e esta é a Aula 16, a última da disciplina Drones e Sensores IoT no Monitoramento de Obras. Hoje não tem conteúdo novo. Tem uma coisa melhor: a gente vai usar tudo o que você aprendeu ao longo de quinze aulas para projetar, de ponta a ponta, o monitoramento de uma obra. E, ao fazer isso, vamos revisar a disciplina inteira."

**[TELA]** Slide 3 — foto do edifício em construção.

> "Lembra da atividade avaliativa da Unidade 1? Um edifício com dois subsolos, um sobrado antigo de um lado, um prédio do outro. Naquela época, você tinha os fundamentos: sabia por que monitorar, o que é malha fechada, o que é incerteza. Hoje você tem o drone, os sensores, o BIM, a inteligência artificial e a gestão. Hoje você tem tudo."

**[TELA]** Slide 4 — o caso Residencial Ipê.

> "Então vamos ao caso, que eu batizei de Residencial Ipê — nome fictício. Dois subsolos, escavação de 7 metros, terreno urbano de 2.400 metros quadrados, contenção em cortina de estacas atirantada. De um lado, a 3 metros da divisa, um sobrado antigo com fundação rasa. Do outro, um prédio de 8 pavimentos, com a garagem junto à divisa. Lençol freático a 4 metros de profundidade, com rebaixamento por poços. E a construtora, que contratou o projeto em BIM 4D, quer medir avanço físico e volumes todo mês. Vamos projetar o monitoramento em sete etapas."

### 2. O canteiro e os riscos (1:50 – 5:00)

**[TELA]** Slide 5 — o canteiro conectado em 3D.

> "Olha a cena 3D. É o canteiro conectado, e repare como cada unidade da disciplina aparece nela. Da Unidade 1, a malha fechada, a incerteza, a arquitetura IoT e as regras de voo. Da Unidade 2, o drone voando em faixas, que gera ortomosaico e volumes. Da Unidade 3, os sensores pulsando na escavação e nos vizinhos. E da Unidade 4, o BIM, a IA e a gestão amarrando tudo isso. Gire a cena e acompanhe um pacote de dados do sensor até a nuvem."

**[TELA]** Slide 6 — risco → grandeza → instrumento → frequência.

> "Etapa 1: riscos e grandezas. Todo plano começa pelos riscos, nunca pelos equipamentos. Quem começa pelo catálogo de sensores acaba com uma obra cheia de instrumentos medindo o que não importa. No Residencial Ipê, os riscos são: dano ao sobrado e ao prédio; a cortina se deslocando demais; a água subindo, com risco de ruptura de fundo; perda de carga nos tirantes; vibração durante a execução das estacas; e a evolução das trincas que o sobrado já tem. E a pergunta que orienta tudo é a da Aula 1: o que, se não for medido a tempo, causa dano?"

> "Etapa 2: o plano de instrumentação. Olha a tabela. Recalque: marcos e prismas nos pilares do sobrado e do prédio, lidos todo dia, e a cada 2 horas em atenção. Deslocamento da cortina: quatro inclinômetros e prismas no topo. Nível d'água: piezômetros de corda vibrante atrás da cortina, a cada 15 minutos, e a cada 5 em atenção. Carga: células em 10% dos tirantes. Vibração: sismógrafo de engenharia na fundação do sobrado, contínuo durante as estacas. E as trincas existentes: fissurômetros. Repare na última coluna: a frequência muda com o nível de resposta — é a amostragem adaptativa da Aula 3. E, antes de qualquer serviço, a vistoria cautelar dos vizinhos, com fotos datadas. Ela é o marco zero de qualquer discussão futura sobre danos."

> "E por que essas frequências? Porque a taxa de leitura segue a velocidade do fenômeno e a consequência do risco. O nível d'água pode subir em horas depois de uma chuva forte, e as consequências são graves: por isso, 15 minutos. O recalque de um sobrado evolui em dias: leitura diária basta na rotina. A vibração da cravação acontece em frações de segundo: o sismógrafo amostra centenas de vezes por segundo, como manda o Nyquist da Aula 2. E repare que nenhum risco crítico depende de um instrumento só: recalque tem marco e prisma; a cortina tem inclinômetro e prisma no topo. Redundância evita que um sensor com defeito dispare um alarme falso ou, pior, esconda um problema real."

### 3. Drone e arquitetura (5:00 – 7:40)

**[TELA]** Slide 7 — o voo mensal: plano, usos e regras.

> "Etapa 3: o drone. Um voo por mês, com multirrotor e câmera RGB, a 60 metros de altura. Com a câmera que usamos na Aula 14, isso dá um GSD de cerca de 1,6 centímetro por pixel. Pontos de controle ou RTK, como você aprendeu na Unidade 2. O produto: ortomosaico, modelo digital de superfície e nuvem de pontos, para medir o volume escavado e o avanço. Voos extras inspecionam as fachadas e as coberturas dos vizinhos, com câmera térmica se houver suspeita de infiltração. E as regras: RBAC 100, cadastro no SISANT, pedido no SARPAS e, como é mapeamento em faixas sobrepostas, aerolevantamento. E, por causa dos vizinhos, máscara de privacidade nas imagens."

> "Um detalhe de engenharia que faz diferença: o volume escavado medido pelo drone é a diferença entre duas superfícies, a do voo anterior e a do voo atual. Então, a qualidade do volume depende da qualidade das duas. Pontos de controle bem distribuídos, medidos pela topografia, e alguns pontos de verificação para conferir o resultado. Sem isso, um erro sistemático de poucos centímetros em altura, num terreno de 2 mil metros quadrados, vira dezenas de metros cúbicos de diferença na medição — e uma discussão na hora de pagar a empreiteira."

**[TELA]** Slide 8 — arquitetura IoT em quatro camadas.

> "Etapa 4: a arquitetura. As mesmas quatro camadas da Aula 3. Percepção: sensores e dataloggers a bateria, com amostragem adaptativa. Rede: LoRaWAN até um gateway com 4G e uma conexão de reserva. Plataforma: séries temporais, filtros, regras e limites na nuvem — a sombra digital da obra. Aplicação: o painel, mostrando valor, velocidade e tendência, e os alertas por mensagem. E um detalhe que salva obra: a regra crítica do nível d'água roda também na borda, no próprio gateway, para ligar a bomba reserva mesmo se a internet cair."

### 4. Malha fechada, plano de resposta e integração (7:40 – 12:20)

**[TELA]** Slide 9 — a malha fechada da cortina: atenção em 10 mm, alerta em 14 mm.

> "Agora, a malha fechada da cortina. No exemplo, o alerta é 14 milímetros — 0,2% da altura de 7 metros — e a atenção, 10 milímetros. São valores de projeto do exemplo, não de norma: numa obra real, quem define é o projetista da contenção. A simulação começa em malha fechada: a leitura é automática, o deslocamento passa da atenção, a equipe é avisada, o reforço é executado e a curva para de subir antes do alerta. Agora clico em malha aberta: leitura semanal, o número vai para o relatório e, quando alguém age, a curva já passou do alerta. É a lição da Aula 1, aplicada à nossa obra."

> "E tem um ponto sutil aqui. O que dispara a ação não é só o valor. Se o deslocamento está em 9 milímetros, ainda verde, mas subindo 2 milímetros por dia, em 2 ou 3 dias ele passa do alerta. Por isso, o painel desta obra também considera a velocidade: quando a projeção indica que o alerta chega em menos de 3 dias, a grandeza já fica amarela. Valor, velocidade e tendência, juntos, como você aprendeu na Unidade 3."

**[TELA]** Slide 10 — plano de resposta por cores.

> "Cada limite vira uma ação, com dono e prazo. Verde, abaixo de 10 milímetros: rotina, com a equipe de monitoramento. Amarelo, entre 10 e 14: aumentar a frequência, inspecionar e preparar o reforço, com o engenheiro da obra respondendo em 24 horas. Vermelho, acima de 14: parar a escavação naquela frente e executar o reforço, com o projetista e o responsável técnico, imediatamente. E o mesmo vale para recalque, nível d'água, carga e vibração. Lembra da regra de ouro da aula passada? Nome e telefone ao lado de cada cor."

**[TELA]** Slide 11 — BIM, sombra digital e IA.

> "Etapas 5 e 6: BIM e IA. O modelo BIM recebe a posição de cada instrumento, associada ao GUID dos elementos; recebe o 4D da escavação e das contenções; e, a cada voo, a nuvem de pontos, para a comparação as-built contra as-designed da Aula 13. Os elementos ficam coloridos pelo nível de alerta: é a sombra digital da obra, com o engenheiro fechando a malha. E a IA da Aula 14 faz duas coisas. Nas fotos periódicas das fachadas do sobrado, a triagem de fissuras novas, com revocação alta; o que ela marca, um engenheiro revisa, e a trinca relevante ganha fissurômetro. E, no ortomosaico, mede o avanço de escavação e estrutura, direto no 4D."

**[TELA]** Slide 12 — o painel integrado: clique em Chuva forte.

> "E tudo isso desemboca no painel. Seis quadros: recalque do sobrado, topo da cortina, nível d'água abaixo do fundo, carga no tirante, vibração e volume escavado em relação ao previsto. Cada quadro mostra o valor, a velocidade por dia, as últimas leituras e a cor do nível de resposta. Agora vou simular a madrugada de chuva da Aula 3. Clico em chuva forte. Olha o nível d'água subindo — ou seja, a distância até o fundo diminuindo. Quando cruza o limite da regra de borda, a bomba reserva liga sozinha, e o nível volta. E repare na cortina: ela acelera e fica amarela pela velocidade, antes de o valor chegar ao alerta. É exatamente isso que dá tempo de agir."

### 5. Exemplo numérico e gestão (12:20 – 15:00)

**[TELA]** Slide 13 — calculadora integrada: velocidade, volume, GSD e custo.

> "Vamos às contas. O inclinômetro I-2 mostra 11,5 milímetros no topo da cortina — já está no amarelo — subindo 1,2 milímetro por dia. Mantida a tendência, o alerta de 14 chega em 14 menos 11,5, dividido por 1,2: cerca de 2,1 dias. Então a frequência de leitura passa a cada 6 horas e o reforço é preparado agora, e não quando o vermelho acender. Volume: o drone mediu 3.150 metros cúbicos escavados no mês, contra 3.500 previstos no 4D: 90% do previsto. GSD do voo a 60 metros: cerca de 1,6 centímetro por pixel — ótimo para volume, inútil para fissura, que fica com o fissurômetro. E o custo: um monitoramento de 420 mil reais numa obra de 38 milhões representa cerca de 1,1% do custo da obra."

**[TELA]** Slide 14 — etapa 7: custo, LGPD, segurança e contrato.

> "Etapa 7: gestão, tudo o que vimos na Aula 15. Custo: CAPEX, OPEX e horas de análise, justificados pelo valor esperado da perda evitada. LGPD: inventário dos dados pessoais, base legal, máscara, desfoque e retenção. Segurança: credenciais trocadas, criptografia, contas individuais, logs e cópias. E contrato: o plano como anexo, com plano de resposta, SLA, dados em formato aberto e ART. Isso faz parte do projeto, e não de um anexo esquecido."

> "E, no caso do Residencial Ipê, a gestão tem uma particularidade: os vizinhos. O sobrado e o prédio não são clientes da obra, mas são os mais afetados por ela. Uma boa prática é apresentar o plano de monitoramento aos vizinhos antes do início, mostrar onde ficarão os marcos e os fissurômetros, combinar o acesso para as leituras e explicar como as imagens deles serão protegidas. Vizinho informado vira aliado: avisa quando aparece uma trinca nova e confia nos números quando eles dizem que está tudo bem."

### 6. A jornada da disciplina (15:00 – 16:30)

**[TELA]** Slide 15 — 16 aulas, uma pergunta.

> "Agora, olha para trás comigo. Você começou esta disciplina com uma trinca na garagem do vizinho e uma pergunta: a obra está como deveria estar? Na Unidade 1, aprendeu os fundamentos: por que monitorar, a malha fechada, o gêmeo digital, a incerteza das medições, a arquitetura IoT e as regras para voar. Na Unidade 2, colocou o drone em ação: planejamento de voo, fotogrametria, volumes, LiDAR e termografia. Na Unidade 3, conheceu os sensores geotécnicos, estruturais e ambientais, as séries temporais e os alertas. E, nesta unidade, integrou tudo: BIM e gêmeo, inteligência artificial e gestão. E o fio que amarra as 16 aulas é um só: medir, comparar com o limite, decidir, agir e medir de novo."

> "Repare que as tecnologias mudam rápido. O drone que você vai usar daqui a cinco anos não existe ainda; a plataforma de IA vai ser outra; talvez a rede não seja mais LoRaWAN. Mas as perguntas desta disciplina não envelhecem. O que medir? Com que incerteza? Com que frequência? Comparado a qual limite? Quem decide, e em quanto tempo? Quem responde se der errado? Quem domina essas perguntas consegue avaliar qualquer tecnologia nova — e separar a que resolve um problema da obra da que só gera gráficos bonitos."

### 7. Atividade e despedida (16:30 – 18:10)

**[TELA]** Slide 16 — atividade prática: seu projeto integrado.

> "A atividade final é o seu projeto integrado. Escolha uma obra real ou fictícia — uma escavação urbana, um viaduto, uma barragem de rejeitos, um retrofit hospitalar — e entregue um plano de monitoramento, em até 5 páginas, com as sete etapas desta aula: riscos e grandezas; tabela de instrumentação; plano de voo; arquitetura e plano de resposta por cores; integração BIM; uso de IA com métrica de avaliação; e ficha de gestão. O método é o mesmo para qualquer obra."

**[TELA]** Slide 17 — pontos-chave.

> "Os pontos-chave desta aula, e da disciplina: o plano começa pelos riscos e termina numa resposta. Drone dá cobertura, sensores dão frequência e topografia dá a referência. Valor, velocidade e tendência decidem juntos. BIM, nuvem de pontos e IA formam a sombra digital, e o engenheiro fecha a malha. E custo, LGPD, segurança e contrato fazem parte do projeto."

**[TELA]** Slide 18 — encerramento da disciplina.

> "E chegamos ao fim. Quero te dizer uma coisa antes de você ir. Nenhuma tecnologia desta disciplina substitui o engenheiro que conhece o solo, a estrutura e a obra. O drone não sabe o que é um recalque perigoso; o sensor não sabe quem chamar às 3 da manhã; a inteligência artificial não assina ART. Mas o engenheiro que domina essas ferramentas decide mais cedo, com mais confiança, e protege mais gente — os trabalhadores, os vizinhos e quem vai morar naquele prédio. É esse profissional que o mercado está procurando, e é esse profissional que você está pronto para ser. Foi uma alegria enorme fazer essa jornada com você. Obrigado pela dedicação ao longo dessas 16 aulas. Leve a malha fechada para cada obra da sua carreira. Até breve, e boa obra!"
