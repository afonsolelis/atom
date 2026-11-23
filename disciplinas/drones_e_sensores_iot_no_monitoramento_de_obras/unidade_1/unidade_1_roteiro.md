# Roteiros das videoaulas — Unidade 1 — Fundamentos, Regulamentação e Planejamento de Voo

Disciplina: Drones e Sensores IoT no Monitoramento de Obras  
Professor: Afonso Cesar Lelis Brandão

> Cópia para a gravação, montada a partir de `roteiros_15min.md` (fala integral, versão a gravar) e do roteiro do vídeo introdutório de `unidade_1.md`. Os arquivos de origem não foram alterados.

> **Como usar:** leia as falas em citação (>) na ordem. As marcações **[TELA]** indicam o slide no ar naquele momento, pelo número no deck da aula (`slides/aulaN.html`).

---

## Roteiro do vídeo introdutório (até 2 min)

*As marcações [TELA] indicam os slides da apresentação do vídeo introdutório.*

**Abertura (0:00 – 0:20):**
[TELA: Slide 1 — capa; Slide 2 — audiodescrição; Slide 3 — Sobre o professor]
> "Olá! Eu sou o professor Afonso Brandão. Para quem usa audiodescrição: sou um homem de pele clara, com cabelos castanho-escuros curtos e barba cheia, também escura e bem aparada; tenho olhos castanhos e sobrancelhas grossas, e apareço em plano médio, de frente para a câmera. Seja muito bem-vindo(a) a Drones e Sensores IoT no Monitoramento de Obras."

**Conexão com o mercado (0:20 – 0:50):**
[TELA: Slide 4 — sumário; Slide 5 — foto aérea do canteiro; Slide 6 — canteiro conectado em 3D]
> "Toda obra tem a mesma pergunta diária: está tudo sob controle? O cronograma está em dia? O talude está se movendo? Quanto de terra já movimentamos? Hoje, um drone registra o canteiro inteiro em um voo, e sensores conversam com a nuvem dia e noite. Construtoras, concessionárias e empresas de instrumentação precisam de engenheiros que saibam usar esses dados para decidir."

**Conteúdo e diferencial (0:50 – 1:25):**
[TELA: Slide 7 — o que vamos monitorar; Slide 8 — do diário de obra ao canteiro conectado; Slide 9 — gêmeo digital em 3D; Slide 10 — 16 videoaulas em 4 unidades]
> "São quatro unidades. Primeiro, os fundamentos: indicadores de avanço da obra, tipos de drone e sensores, as regras de ANAC, DECEA e Anatel e o planejamento de um voo seguro. Depois, as imagens: fotogrametria, GNSS, ortomosaicos, nuvens de pontos e volumes. Em seguida, os sensores IoT e as redes que levam o dado do canteiro à nuvem. E, para fechar, painéis de alerta, integração com BIM, segurança do trabalho e proteção de dados."

**Benefício para o aluno (1:25 – 1:45):**
[TELA: Slide 11 — onde isso aparece na sua carreira; Slide 12 — como você será avaliado]
> "Ao final, você consegue **planejar** o monitoramento, **interpretar** os dados com senso crítico e **decidir** com base neles. Nas avaliações, a pergunta será sempre a mesma: o que o engenheiro deve fazer com esse dado?"

**Encerramento (1:45 – 2:00):**
[TELA: Slide 13 — encerramento]
> "Bora começar? A obra do futuro já está conectada e precisa de engenheiros que saibam ler o que ela está dizendo. Te espero na Aula 1!"

---

## Roteiro da Videoaula 1 — "A obra está atrasada? Como o drone transforma medição em resposta"

**Duração-alvo:** cerca de 18:00 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:40)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Eu sou o professor Afonso Brandão, e seja muito bem-vindo, muito bem-vinda à primeira aula da disciplina Drones e Sensores IoT no Monitoramento de Obras. IoT é a sigla em inglês para Internet das Coisas: objetos que medem e conversam com a rede sozinhos. E eu quero começar com uma cena que todo engenheiro de obra já viveu, ou vai viver. Reunião mensal com o cliente. Sala do contêiner, café, projetor ligado."

**[TELA]** Slide 3 — foto aérea do canteiro com a pergunta: "Afinal, estamos atrasados?".

> "O cronograma diz que, nesta data, a obra deveria estar com 37 e meio por cento executados. O mestre de obras acha que está 'mais ou menos em dia'. O financeiro informa que já foram gastos 1 milhão e 450 mil reais. E o cliente olha para você e pergunta: 'Afinal, engenheiro, estamos atrasados? Estamos gastando mais do que deveríamos?' Repara que ninguém na sala tem a resposta. O mestre tem uma impressão. O financeiro tem um número de gasto, mas não sabe quanto esse gasto comprou de obra. E o cronograma tem uma previsão, mas ninguém mediu o realizado com rigor."

> "Nesta aula, a gente vai entender por que e como se monitora uma obra, como se mede o avanço físico quando os serviços são tão diferentes entre si, e como dois índices simples — o IDP e o IDC — transformam medição em diagnóstico de prazo e de custo. E você vai ver exatamente onde o drone entra nessa conta. Vamos nessa."

### 2. Por que monitorar uma obra? (1:40 – 3:30)

**[TELA]** Slide 4 — Por que monitorar: as quatro dimensões (prazo, custo, segurança, qualidade).

> "Primeiro, uma definição que eu quero que você leve para a vida profissional. Monitorar é medir de forma sistemática, ao longo do tempo, grandezas que indicam se a obra está se comportando como o projeto e o planejamento previram. Repara nas três ideias dentro dessa frase. 'Sistemática' quer dizer que tem método: sempre do mesmo jeito, com o mesmo critério. 'Ao longo do tempo' quer dizer que uma medição isolada vale pouco — o que conta é a tendência. E 'como previram' quer dizer que existe uma referência para comparar. Sem referência, você tem um número, não tem uma informação."

> "E por que a gente monitora? As razões cabem em quatro dimensões clássicas da gestão. Prazo: o avanço físico real comparado ao cronograma — quantos metros cúbicos foram escavados, quantos pavimentos foram concretados. Custo: a medição de serviços para pagamento, o controle de perdas e de retrabalho. Segurança: das pessoas e das estruturas — recalques, deslocamento de contenções, nível d'água em escavações. E qualidade: prumo, nível, espessura, desempenho dos materiais."

> "Monitorar não é luxo: é a forma de transformar incerteza em informação. O orçamento partiu de uma produtividade estimada; o projeto de fundação partiu de alguns furos de sondagem. A realidade nunca é exatamente igual. O monitoramento é a obra respondendo ao planejamento: a hipótese estava certa — ou não. Nesta aula o foco vai ser prazo e custo; segurança e qualidade vão aparecer com força nas Unidades 3 e 4."

### 3. Do diário de obra ao canteiro conectado (3:30 – 5:10)

**[TELA]** Slide 5 — foto aérea do canteiro do Pronto-Socorro Central de Itapevi: as três fragilidades do jeito tradicional.

> "Como isso é feito tradicionalmente? Com o diário de obra, com vistorias visuais, com fotos de celular e com campanhas periódicas de topografia. Um técnico vai lá uma vez por mês, mede, anota na planilha, e o dado vira relatório alguns dias depois. Isso funciona — muita obra boa foi feita assim. Mas tem três fragilidades. A primeira é a baixa frequência: a medição é mensal, e muita coisa acontece entre duas medições. A segunda é o atraso: o dado leva dias para virar relatório e chegar a quem decide. E a terceira é a subjetividade: 'a escavação está quase no fim' significa uma coisa para o encarregado e outra para o fiscal do cliente."

**[TELA]** Slide 6 — o canteiro conectado em 3D (gire a cena).

> "No canteiro conectado, a lógica muda. Um drone sobrevoa o canteiro inteiro em vinte minutos e gera uma ortofoto — uma foto aérea com escala constante, que funciona como mapa — e um modelo 3D do terreno, de onde sai o volume escavado. Sensores em contenções e estruturas mandam leituras sozinhos para a nuvem. A frequência sobe, o atraso cai de dias para horas e, principalmente, o dado passa a ser quantitativo, datado e rastreável. Não é mais 'quase no fim': é 39 mil metros cúbicos medidos no dia 14, com o arquivo guardado. E repara que isso é exatamente o que os indicadores de controle precisam para funcionar."

### 4. O ciclo do controle: medir, comparar, decidir, agir (5:10 – 7:00)

**[TELA]** Slide 7 — o ciclo dado → informação → decisão → ação, revelado passo a passo.

> "Agora, o primeiro alerta da disciplina: dado sozinho não salva obra nenhuma. O valor está no ciclo que o dado percorre. Primeira etapa: dado — a leitura bruta. 'Foram escavados 39 mil metros cúbicos.' Isso, sozinho, não diz se é bom ou ruim. Segunda: informação — o dado comparado a uma referência. 'O previsto para hoje era 45 mil.' Agora eu entendo: estou atrasado na terraplenagem. Terceira: decisão — o julgamento técnico de quem tem conhecimento e autoridade. 'Vamos mobilizar mais uma escavadeira na frente norte.' E quarta: ação — a escavadeira chegando de fato ao canteiro."

**[TELA]** Slide 8 — malha aberta × malha fechada, com a analogia do termostato.

> "A engenharia de controle tem um nome para isso. Em malha aberta, você mede e arquiva: a medição vira relatório, o relatório vai para a pasta, e ninguém compara com a referência a tempo de agir. Em malha fechada, a medição realimenta a execução: medir, comparar, decidir, agir — e medir de novo, para confirmar que a escavadeira extra resolveu. A analogia clássica é o ar-condicionado com termostato: ele mede a temperatura, compara com os 23 graus que você escolheu, liga ou desliga o compressor e mede de novo."

> "E esse ciclo não é novidade na construção. O Aldo Dórea Mattos, no livro Planejamento e controle de obras, que é bibliografia básica desta disciplina, coloca no centro do controle o ciclo PDCA: planejar, executar, verificar e agir. É a mesma malha fechada. O que a tecnologia faz é encurtar o ciclo e torná-lo confiável. Quando esse laço passa a ser automático e contínuo entre a obra e um modelo digital, a gente fala em gêmeo digital — um tema que volta na Unidade 4. Por enquanto, guarde: a tecnologia que não encurta nem torna mais confiável o ciclo de controle é enfeite."

### 5. Avanço físico e curva S (7:00 – 9:20)

**[TELA]** Slide 9 — avanço físico ponderado: serviços com unidades diferentes e pesos pelo orçamento.

> "Agora a pergunta técnica: como medir o avanço de uma obra em que a terraplenagem é medida em metros cúbicos, a estaca em metros, a forma em metros quadrados e a estrutura em pavimentos? Não dá para somar metros cúbicos com metros. A solução é ponderar cada serviço pelo peso dele no orçamento. O peso é o custo do serviço dividido pelo custo total. O avanço físico da obra é a soma, para todos os serviços, do peso vezes a porcentagem executada daquele serviço."

> "Um exemplo rápido: se a terraplenagem representa 30% do orçamento e está 65% executada, ela contribui com 0,30 vezes 0,65, ou seja, 19,5 pontos percentuais para o avanço da obra. Faz isso para cada serviço e soma. É simples, mas tem uma consequência importante: o avanço físico depende da qualidade da medição de cada serviço. Se o volume de terraplenagem está errado, o avanço da obra inteira está errado."

**[TELA]** Slide 10 — curva S previsto × realizado (passe o mouse pelos meses).

> "E aqui entra uma das ferramentas mais usadas do controle de obras: a curva S. Pegue o avanço previsto em cada período, acumule mês a mês e desenhe. A curva sai com formato de S. No começo, ela é suave: é a mobilização, o canteiro sendo montado, pouca produção. No meio, fica íngreme: é a produção plena, várias frentes trabalhando ao mesmo tempo. E no fim volta a se achatar: acabamentos, testes, desmobilização."

> "A curva S pode ser física, em porcentagem, ou físico-financeira, em reais. Ela é a linha de base. A cada medição, você desenha a curva do realizado por cima. Se o realizado está abaixo do previsto, a obra está atrasada; se está acima, adiantada. Olha a tela: no mês 5, a curva prevista está em 37 e meio por cento, e a realizada em 32 e meio. A diferença é visual, imediata. Qualquer pessoa na reunião entende."

### 6. Valor agregado: IDP e IDC (9:20 – 12:20)

**[TELA]** Slide 11 — as três grandezas: VP, VA e CR.

> "Só que a curva S física responde só metade da pergunta do cliente. Ela diz se estamos atrasados, mas não diz se estamos gastando demais. Para juntar prazo e custo, existe a análise de valor agregado. Ela usa três grandezas, todas em reais e acumuladas até a data de controle."

> "A primeira é o VP, valor planejado: quanto do orçamento deveria ter sido executado até hoje, segundo o cronograma. A segunda é o VA, valor agregado: quanto do orçamento corresponde ao que foi de fato executado. A conta é o avanço físico vezes o orçamento total, que a gente chama de ONT, orçamento no término. E a terceira é o CR, custo real: quanto efetivamente se gastou para executar o que foi executado."

> "Repara na sutileza do VA. Ele não é o que eu gastei; é o quanto vale, a preço de orçamento, aquilo que eu construí. Se eu executei 32 e meio por cento de uma obra de 4 milhões, eu agreguei 1 milhão e 300 mil reais de obra — não importa quanto eu tenha pago por isso."

**[TELA]** Slide 12 — os índices IDP e IDC e a estimativa no término.

> "Com as três grandezas, saem dois índices. O IDP, índice de desempenho de prazo, é VA dividido por VP: o que eu agreguei sobre o que eu deveria ter agregado. Menor que 1, a obra está atrasada. O IDC, índice de desempenho de custo, é VA dividido por CR: o que eu agreguei sobre o que eu gastei. Menor que 1, cada real gasto está comprando menos de um real de obra. E dá para projetar: a estimativa no término, a ENT, é aproximadamente o orçamento dividido pelo IDC — quanto a obra vai custar se o desempenho de custo continuar igual."

> "E agora o ponto que liga tudo à nossa disciplina. O VA depende inteiramente da medição do executado. Se a medição é ruim, o IDP e o IDC são ruins, e a decisão é ruim. O drone entra justamente aqui: volumes de terraplenagem, áreas de pavimentação, número de pavimentos, frentes de fachada — tudo medido de forma rápida, frequente e rastreável."

### 7. O que drones e sensores resolvem — e o que não resolvem (12:20 – 13:40)

**[TELA]** Slide 13 — o que resolve e o que não resolve, com a foto da estação total robótica e do prisma.

> "Então vamos ser honestos sobre a tecnologia. Drones e sensores resolvem cobertura — o canteiro inteiro num voo; frequência — medições semanais em vez de mensais; acesso — fachadas e taludes sem expor ninguém; e rastreabilidade — o dado datado e georreferenciado, que serve até como prova numa disputa contratual sobre medição."

> "Mas eles não resolvem cronograma mal feito. Não resolvem orçamento sem estrutura analítica — se eu não sei quanto custa cada serviço, não tenho os pesos. Não resolvem a falta de alguém com autoridade para decidir. E a topografia não desaparece: essa foto é de uma estação total com prisma. É a topografia, com estação total e GNSS, que fornece os pontos de controle e valida o levantamento com drone. Uma tecnologia complementa a outra."

### 8. Exemplo numérico: respondendo ao cliente (13:40 – 16:30)

**[TELA]** Slide 14 — calculadora do avanço ponderado e do valor agregado (valores iniciais do exemplo).

> "Agora vamos responder ao cliente da abertura, com valores ilustrativos. Uma obra industrial com orçamento de 4 milhões de reais e quatro serviços. Terraplenagem: 1 milhão e 200 mil, peso 0,30. Contenção: 800 mil, peso 0,20. Fundações: 1 milhão, peso 0,25. Estrutura: 1 milhão, peso 0,25."

> "Na medição do mês 5, o drone mediu 39 mil metros cúbicos escavados, de um total de 60 mil: 65% da terraplenagem. A medição de campo indicou 40% da contenção, 20% das fundações e a estrutura ainda não começou. O avanço físico: 0,30 vezes 0,65, mais 0,20 vezes 0,40, mais 0,25 vezes 0,20, mais zero. Dá 0,195 mais 0,08 mais 0,05: 0,325, ou 32 e meio por cento. O VA: 0,325 vezes 4 milhões, 1 milhão e 300 mil reais."

> "O cronograma previa 37 e meio por cento: VP de 1 milhão e 500 mil. O financeiro informou CR de 1 milhão e 450 mil. IDP: 1,3 dividido por 1,5, aproximadamente 0,87. IDC: 1,3 dividido por 1,45, aproximadamente 0,90. ENT: 4 milhões dividido por 0,90, cerca de 4 milhões e 460 mil."

> "Agora a resposta ao cliente, em duas frases. 'A obra está atrasada: agregamos 87% do valor que deveríamos ter agregado até hoje. E estamos acima do custo: cada real gasto agregou 90 centavos de obra; mantido esse desempenho, o custo final ficaria cerca de 460 mil reais acima do orçamento.' Isso é muito diferente de 'está mais ou menos em dia'."

**[TELA]** Slide 15 — sensibilidade: arraste o controle do volume medido de 39.000 para 36.000 m³.

> "E um detalhe que mostra por que a exatidão importa. Vou arrastar o volume medido de 39 mil para 36 mil metros cúbicos — um erro de 3 mil, 5% do total. O avanço da terraplenagem cai 5 pontos, e o VA cai 60 mil reais. Sessenta mil reais de diferença na medição, que podem virar pagamento a mais ou a menos para o empreiteiro. Por isso, na Unidade 2, a gente vai se preocupar tanto com pontos de controle e precisão do levantamento: a exatidão do drone é dinheiro."

### 9. Atividade prática + encerramento (16:30 – 18:00)

**[TELA]** Slide 16 — Atividade prática.

> "Sua missão até a próxima aula. Escolha uma obra que você conhece — pode ser uma obra pública noticiada na sua cidade. Liste quatro serviços principais, atribua a cada um um custo estimado e um avanço executado. Calcule o avanço físico ponderado e o VA. Arbitre um VP e um CR plausíveis, calcule IDP e IDC e escreva o diagnóstico em duas frases, como eu fiz para o cliente. E, por fim, indique quais avanços poderiam ser medidos por drone, quais por sensor e quais exigem medição convencional."

**[TELA]** Slide 17 — Pontos-chave; Slide 18 — encerramento e gancho para a Aula 2.

> "Vamos amarrar. Monitorar é medir de forma sistemática, ao longo do tempo, se a obra se comporta como previsto em prazo, custo, segurança e qualidade. O valor está no ciclo medir, comparar, decidir, agir e medir de novo — a malha fechada, o PDCA. O avanço físico pondera cada serviço pelo peso no orçamento, e acumulado no tempo forma a curva S. IDP é VA sobre VP; IDC é VA sobre CR. E o drone torna a medição do executado frequente e rastreável."

> "Mas qual drone faz essa medição? Com qual sensor? Uma câmera comum basta, ou eu preciso de câmera térmica, de LiDAR, de câmera multiespectral? E um drone que mede volume serve para inspecionar fachada? É o assunto da próxima aula: os tipos de drone e os sensores embarcados. Te espero na Aula 2. Um abraço!"

---

## Roteiro da Videoaula 2 — "Um drone serve para tudo? O sensor certo para cada pergunta da obra"

**Duração-alvo:** cerca de 18:10 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:20)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à segunda aula. Na aula passada, a gente viu que o drone entra no controle da obra medindo o executado. Hoje eu quero abrir o drone e olhar para o que ele carrega, porque nem todo drone serve para tudo. E começo com uma cena."

**[TELA]** Slide 3 — os dois pedidos: loteamento de 120 ha e fachada com placas descolando.

> "Dois pedidos chegam no mesmo dia. O primeiro, da gerência: o volume escavado de um loteamento de 120 hectares — mais de cem campos de futebol. O segundo, do síndico de um condomínio de 15 anos: onde as placas cerâmicas da fachada estão descolando, antes que uma caia na calçada. A construtora tem um único drone, pequeno, com câmera comum. Ele serve para os dois? A resposta é não — e, no fim desta aula, você vai saber explicar por quê, e o que comprar ou contratar para cada caso. Vamos conhecer as famílias de drones, os componentes e os sensores embarcados."

### 2. Drone, UA, UAS e RPA: os termos (1:20 – 2:10)

**[TELA]** Slide 4 — os termos UA, UAS e RPA, com o esquema aeronave + estação + enlace.

> "Primeiro, os nomes. 'Drone' é o nome popular — o que a gente fala no canteiro. A regulamentação fala em aeronave não tripulada, a UA, e em sistema de aeronave não tripulada, o UAS. E por que 'sistema'? Porque o UAS é a aeronave mais a estação de pilotagem remota e o enlace de comando entre elas. Se o rádio falha, o sistema falha, mesmo com a aeronave perfeita. A literatura técnica também usa RPA, a aeronave remotamente pilotada. E um lembrete: drone sobre obra, para uma construtora, é uso profissional, e segue as regras que você vai ver na Aula 3."

### 3. As três famílias: multirrotor, asa fixa e VTOL (2:10 – 4:00)

**[TELA]** Slide 5 — as três famílias lado a lado.

> "Existem três grandes famílias. A primeira é o multirrotor — quadricóptero, hexacóptero, octocóptero, conforme o número de hélices. Ele decola na vertical, paira parado no ar e manobra com precisão. Isso faz dele o ideal para inspeção de fachadas e estruturas, e para áreas pequenas, como o canteiro urbano. A limitação é a autonomia: tipicamente de 20 a 45 minutos. Ficar parado no ar é caro: os rotores sustentam todo o peso o tempo todo."

> "A segunda é a asa fixa. Voa como um avião: a asa gera a sustentação, e o motor só empurra para frente. Isso é muito mais eficiente, e ela cobre centenas de hectares por voo. É a preferida em rodovias, ferrovias e grandes terraplenagens. Mas precisa de área para pousar — às vezes de barriga, no capim — e não paira em frente a uma trinca."

**[TELA]** Slide 6 — foto do VTOL tail-sitter pousado na vertical.

> "E a terceira é o VTOL, da sigla em inglês para decolagem e pouso vertical. É um híbrido: decola e pousa na vertical, como o multirrotor, e voa em cruzeiro como asa fixa. A foto na tela é um VTOL do tipo tail-sitter, que fica 'sentado' na cauda antes de decolar. Ele junta o melhor dos dois mundos para mapear grandes áreas sem pista. Então, primeira resposta à nossa cena: o loteamento de 120 hectares pede asa fixa ou VTOL; a fachada pede multirrotor."

### 4. Componentes de um drone (4:00 – 6:10)

**[TELA]** Slide 7 — drone em 3D, montado, com as hélices girando. Clique em Vista explodida quando a fala pedir; as peças se separam em cerca de 2 segundos.

> "Agora vamos abrir o drone. Clico em vista explodida, e as peças se separam. Começando pela estrutura, o frame: fibra de carbono ou compósitos, leve e rígida. Motores e ESC: os motores são elétricos do tipo brushless, sem escovas, e cada um é acionado por um controlador eletrônico de velocidade, o ESC. É ele que varia a rotação de cada hélice centenas de vezes por segundo para manter o drone estável."

> "No centro, a controladora de voo: o cérebro. Ela estabiliza a aeronave e executa as missões automáticas — aquele voo em linhas paralelas que você vai planejar na Aula 4. Para saber onde está, ela usa o receptor GNSS, de navegação por satélite. E aqui tem um detalhe que importa muito para a engenharia: com RTK — a correção cinemática em tempo real —, a posição de cada foto chega ao nível de centímetros, o que reduz a necessidade de pontos de controle em campo. Reduz — não elimina. Na Unidade 2, você vai ver por quê."

> "Para saber como está inclinado e para onde aponta, a controladora usa a IMU, a unidade inercial, com acelerômetros e giroscópios, e a bússola. A energia vem da bateria LiPo, de polímero de lítio: alta densidade de energia, mas sensível a frio, calor e armazenamento — tema da Aula 4. O gimbal é o suporte estabilizado que mantém o sensor firme mesmo com vento. E o rádio faz o enlace de comando e de vídeo com a estação de pilotagem — e precisa de homologação da Anatel, como você vai ver na próxima aula."

**[TELA]** Slide 8 — os componentes de verdade: motor brushless, bateria e plataforma profissional com gimbal de câmeras de zoom e térmica.

> "E aqui estão esses componentes de verdade: o motor sem escovas, a bateria e uma plataforma profissional, com braços de fibra de carbono e, embaixo, um gimbal com câmera de zoom e câmera térmica. Repara que o drone é uma plataforma: o que define o trabalho que ele faz é o sensor que ele carrega."

### 5. Câmera RGB: a carga útil da fotogrametria (6:10 – 7:50)

**[TELA]** Slide 9 — a câmera RGB: tamanho do sensor, distância focal e obturador (alterne global × rolling shutter na simulação).

> "A carga útil — o payload — é o que o drone leva para trabalhar. A mais usada, de longe, é a câmera RGB — de red, green e blue, a câmera comum. Com ela se faz a fotogrametria, que gera o ortomosaico, o modelo 3D e o cálculo de volumes — exatamente o volume de terraplenagem que alimentou o valor agregado da Aula 1."

> "E aqui vai um aviso de quem já viu muita compra errada: megapixel não é tudo. Três características pesam mais. O tamanho do sensor: sensores maiores captam mais luz e têm pixels maiores, com menos ruído. A distância focal: junto com a altura de voo, ela define o tamanho de cada pixel no terreno — o GSD, que a gente calcula na Aula 4. E o obturador. Olha a simulação: com obturador mecânico, global, o quadro inteiro é exposto ao mesmo tempo. Agora eu troco para eletrônico, o rolling shutter: as linhas são lidas em sequência, e, com o drone em movimento, a imagem sai levemente torta. Para fotogrametria de precisão, o obturador mecânico é o preferido; com rolling shutter, voa-se mais devagar ou o software corrige."

### 6. Multiespectral e térmica (7:50 – 10:50)

**[TELA]** Slide 10 — mapa NDVI de imagens multiespectrais.

> "A segunda carga útil é a câmera multiespectral. Ela registra bandas estreitas da luz, inclusive o infravermelho próximo, que o nosso olho não vê. A vegetação saudável reflete muito infravermelho próximo e absorve o vermelho. Combinando as duas bandas, calcula-se um índice como o NDVI, o índice de vegetação por diferença normalizada. O mapa na tela vai do roxo, vegetação fraca, ao verde, vegetação vigorosa. Na obra, isso serve para verificar se a hidrossemeadura de um talude pegou, ou para acompanhar a recuperação de uma área degradada exigida no licenciamento ambiental."

**[TELA]** Slide 11 — termograma da torre com as varandas: pontes térmicas em amarelo e laranja.

> "A terceira é a câmera térmica. Todo corpo acima do zero absoluto emite radiação infravermelha — no infravermelho térmico, bem diferente do próximo. A câmera térmica, em geral com um sensor chamado microbolômetro, na faixa de 8 a 14 micrômetros, mede essa radiação e a converte em temperatura aparente, mostrada em cores falsas no termograma. Olha esta torre fotografada num dia frio: as bordas das lajes das varandas aparecem em amarelo e laranja. É calor escapando pelas pontes térmicas."

> "Agora, a palavra-chave é 'aparente'. A conversão depende da emissividade do material — quanto ele emite em relação a um emissor ideal — e da temperatura refletida do entorno. Concreto, reboco e cerâmica fosca têm emissividade alta e se comportam bem. Vidro e metal polido têm emissividade baixa e refletem o calor de outras coisas — do céu, do prédio da frente, do próprio piloto. O termograma pode 'mentir'."

**[TELA]** Slide 12 — as três aplicações em fachada: descolamento, umidade e pontes térmicas.

> "Por isso, em obra, o que interessa é a diferença de temperatura entre regiões, não o valor absoluto. Três aplicações clássicas. Descolamento de revestimento: a placa solta tem uma camada de ar atrás, que isola; sob sol, ela aquece mais rápido que a placa aderida e aparece mais quente. Umidade e infiltração: a água evaporando resfria a superfície, e aparecem manchas frias. E pontes térmicas e instalações: perdas de calor em vigas e lajes, painéis elétricos e conexões aquecidos. Segunda resposta à nossa cena: a fachada do condomínio pede um multirrotor com câmera térmica. E o termograma diz onde olhar; a confirmação vem do ensaio de percussão no local."

### 7. LiDAR embarcado (10:50 – 12:40)

**[TELA]** Slide 13 — drone com LiDAR e a animação dos múltiplos retornos (clique em Disparar pulso).

> "A quarta carga útil é o LiDAR — de light detection and ranging, detecção e medição de distância por luz. Ele emite pulsos de laser, centenas de milhares por segundo, e mede o tempo de ida e volta de cada um. A distância é a velocidade da luz vezes esse tempo, dividido por 2, porque o pulso vai e volta. Combinando a distância com a posição do drone, dada pelo GNSS, e com a atitude, dada pela IMU, cada pulso vira um ponto 3D."

> "E aqui está a mágica. Clico em disparar pulso. O feixe tem alguns centímetros de diâmetro quando chega à árvore. Parte da energia volta da copa, parte de um galho e parte do chão, passando pelas frestas. São os múltiplos retornos. Classificando o último retorno, eu obtenho o terreno mesmo sob a vegetação — onde a fotogrametria só vê as copas. Cuidado com a frase popular de que 'o laser atravessa as folhas': ele não atravessa, ele passa pelos vãos. Mata muito fechada ainda deixa poucos pontos no solo."

> "O LiDAR também mede superfícies sem textura, como uma laje lisa, onde a fotogrametria falha, e funciona sem luz. O preço é alto: o sistema exige GNSS e IMU de excelente qualidade, porque um pequeno erro de atitude desloca o ponto lá embaixo. Os produtos do LiDAR — nuvens de pontos, modelos do terreno — você vai aprofundar na Aula 7."

### 8. Como escolher + exemplo numérico (12:40 – 16:30)

**[TELA]** Slide 14 — tabela: pergunta da obra × aeronave × sensor.

> "Vamos organizar a escolha. A tabela está na tela; eu destaco a lógica. Volume e avanço de um canteiro urbano: multirrotor com RGB e RTK ou pontos de controle. Terraplenagem ou rodovia de centenas de hectares: asa fixa ou VTOL com RGB. Terreno natural sob mata: LiDAR. Descolamento e infiltração em fachada: multirrotor com térmica e, de preferência, uma câmera de zoom junto. Recuperação vegetal de taludes: multiespectral. A regra cabe numa frase: a pergunta define o sensor; a geometria da obra define a aeronave."

> "E uma dica de gestão: nem sempre vale a pena comprar. Uma construtora que mede volume toda semana em vários canteiros urbanos justifica ter o seu multirrotor com RGB. Já o LiDAR, a térmica de alta resolução ou o VTOL para uma rodovia costumam ser contratados de empresas especializadas, por campanha. A decisão de comprar ou contratar segue a frequência de uso — e, como você vai ver na próxima aula, a capacidade de cumprir as exigências regulatórias."

**[TELA]** Slide 15 — calculadora do tempo de voo do pulso LiDAR (alvo inicial em 80 m).

> "Agora, duas contas que mostram que esses sensores são instrumentos de medição, com limites. Primeira, o LiDAR. Um alvo no solo a 80 metros. O tempo de ida e volta é 2 vezes 80, dividido por 3 vezes 10 elevado a 8 metros por segundo. Dá cerca de 5,3 vezes 10 elevado a menos 7 segundos: 533 nanossegundos. Meio microssegundo. E se a eletrônica errar 1 nanossegundo na medição do tempo? A distância erra a velocidade da luz vezes 1 nanossegundo, dividido por 2: 15 centímetros. Por isso o LiDAR exige eletrônica de altíssima precisão — e custa o que custa."

**[TELA]** Slide 16 — calculadora do pixel térmico na fachada (distância inicial de 10 m; leve a 30 m quando a fala pedir).

> "Segunda conta, a térmica. Uma câmera de 640 por 512 pixels, com pixel de 12 micrômetros e focal de 13 milímetros. O campo de visão instantâneo de um pixel, o IFOV, é o pixel dividido pela focal: 12 micrômetros sobre 13 milímetros, cerca de 0,92 miliradiano. A 10 metros da fachada, cada pixel cobre 10 vezes 0,92: uns 9,2 milímetros. Para medir um defeito com confiança, a regra prática é que ele ocupe pelo menos 3 por 3 pixels. Então o menor defeito confiável a 10 metros tem cerca de 2,8 centímetros."

> "Agora eu levo o drone a 30 metros da fachada. Cada pixel passa a cobrir 2,8 centímetros, e o menor defeito confiável passa a uns 8,3 centímetros. E por que eu voaria a 30 metros? Guarde esse número: na próxima aula você vai descobrir que 30 metros é a distância mínima de pessoas não envolvidas na categoria aberta. Ou seja: a distância de voo é, ao mesmo tempo, uma decisão de resolução e de segurança."

### 9. Atividade prática + encerramento (16:30 – 18:10)

**[TELA]** Slide 17 — Atividade prática.

> "Sua missão: escolha duas obras bem diferentes — por exemplo, a reforma de fachada de um prédio e a duplicação de uma rodovia. Para cada uma, escreva a pergunta que o levantamento deve responder, escolha a aeronave e o sensor e justifique pela geometria e pelo objetivo. Depois, pegue a ficha técnica de um drone comercial e identifique a autonomia, o tipo de obturador, o tamanho do sensor, se tem RTK e qual o grau de proteção contra água e poeira."

**[TELA]** Slide 18 — Pontos-chave; Slide 19 — encerramento e gancho para a Aula 3.

> "Vamos amarrar. Multirrotor paira e inspeciona; asa fixa cobre grandes áreas; VTOL junta os dois. Por dentro: frame, motores e ESC, controladora, GNSS e RTK, IMU, bateria LiPo, gimbal e rádio. E os sensores: RGB para fotogrametria, multiespectral para vegetação, térmica para diferenças de temperatura e LiDAR para o terreno sob a mata. A pergunta define o sensor; a geometria define a aeronave."

> "Você já sabe escolher o drone e o sensor. Mas fica a pergunta que pode custar caro: pode voar? A aeronave está cadastrada? O piloto está habilitado? Quem autoriza o uso do espaço aéreo sobre a obra? E aqueles 30 metros? Na próxima aula, as regras do jogo no Brasil: ANAC, DECEA e Anatel. Te espero na Aula 3. Um abraço!"

---

## Roteiro da Videoaula 3 — "Pode voar aqui? O que ANAC, DECEA e Anatel exigem antes da decolagem"

**Duração-alvo:** cerca de 18:30 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:10)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à terceira aula. Começo com uma cena muito comum. A construtora comprou um drone. Chegou a caixa no escritório da obra, e o gerente fala: 'Amanhã cedo, quero o canteiro voado'. Tira da caixa, carrega a bateria e decola, certo?"

**[TELA]** Slide 3 — foto do piloto remoto com o controle na mão: "Antes de tudo: pode voar?"

> "Errado. Antes de decolar, tem uma lista de perguntas. A aeronave está cadastrada? O piloto está habilitado? Tem seguro? O voo foi solicitado ao controle do espaço aéreo? O rádio do equipamento é homologado? E, se o voo for para gerar ortomosaico, precisa de autorização do Ministério da Defesa? Nesta aula, você vai conhecer quem regula o quê no Brasil — um arcabouço que acabou de mudar, e isso é importante — e vai sair com um checklist regulatório na mão."

### 2. Três órgãos, três perguntas (1:10 – 2:20)

**[TELA]** Slide 4 — os três órgãos: ANAC, DECEA e Anatel, cada um com a sua pergunta.

> "A operação de um drone no Brasil responde a três perguntas, e cada uma tem um 'dono'. Primeira: a aeronave, o operador e o piloto podem voar? Quem responde é a ANAC, a Agência Nacional de Aviação Civil: cadastro, categorias de operação, habilitação, seguro. Segunda: o espaço aéreo pode ser usado ali, naquela hora? Quem responde é o DECEA, o Departamento de Controle do Espaço Aéreo, do Comando da Aeronáutica. Terceira: o rádio do equipamento pode transmitir? Quem responde é a Anatel. E somam-se a elas o Ministério da Defesa, quando o voo é aerolevantamento, e a LGPD, porque imagem de pessoa é dado pessoal. Uma confusão comum é achar que 'tirar a autorização da ANAC' resolve tudo. Não resolve: são portas diferentes, e todas precisam estar abertas."

### 3. ANAC: do RBAC-E nº 94 ao RBAC nº 100 (2:20 – 6:30)

**[TELA]** Slide 5 — do RBAC-E nº 94 (classes por peso) ao RBAC nº 100 (categorias por risco).

> "Comecemos pela ANAC. Por quase uma década, a referência foi o RBAC-E número 94, de 2017 — que, aliás, está na bibliografia da nossa disciplina. Ele classificava as aeronaves pelo peso máximo de decolagem, em três classes: Classe 1, acima de 150 quilos; Classe 2, de 25 a 150; e Classe 3, até 25 quilos. Você ainda vai encontrar essas classes em contratos e editais."

> "Em junho de 2026, a ANAC aprovou o RBAC número 100, pela Resolução número 805, de 15 de junho de 2026. Ele substituiu o RBAC-E 94. E a mudança de filosofia é grande: em vez de classificar a aeronave pelo peso, passa a classificar a operação pelo risco. Faz sentido: um drone de 5 quilos sobre uma multidão é mais perigoso que um de 20 quilos sobre um descampado. Os atos emitidos sob o RBAC-E 94 continuam válidos até serem revistos, e quem já tinha autorização que não cabe na categoria aberta tem 2 anos para obter uma nova."

**[TELA]** Slide 6 — as três categorias de operação: aberta, específica e certificada.

> "São três categorias. A categoria aberta: peso em voo até 25 quilos, em linha de visada visual — o VLOS, com o piloto vendo o drone — ou estendida, o EVLOS, com a ajuda de um observador; até 120 metros — 400 pés — acima do solo, em áreas distantes de terceiros. E aqui vem o número que você precisa decorar: em nenhuma hipótese a menos de 30 metros horizontais de pessoas não envolvidas e não anuentes, a não ser que exista uma barreira mecânica capaz de protegê-las. E ela exige uma avaliação de risco operacional atualizada, que só fica facultativa se a operação estiver a mais de 150 metros dessas pessoas ou protegida por barreira."

> "A categoria específica entra quando algum critério da aberta não é atendido: voo além da linha de visada — o BVLOS —, acima de 120 metros, aeronave acima de 25 quilos. Aí o operador demonstra a segurança por uma avaliação de risco, num método aceito pela ANAC, como o SORA — criado pelo grupo internacional de autoridades JARUS —, ou por um cenário padrão; conforme a complexidade, ele ainda obtém o COE, o Cadastro de Operador na categoria específica. E a categoria certificada é para operações de alto risco, como transporte de artigos perigosos, com certificação da aeronave, do operador e do piloto. Para obra, você vai viver entre a aberta e a específica."

**[TELA]** Slide 7 — escala real em 3D: o prédio de 40 pavimentos (120 m), o círculo de 30 m e o de 150 m.

> "Olha a cena em escala real: um prédio de 40 pavimentos de 3 metros é o teto da categoria aberta. Eu levo o drone até o limite e aproximo das pessoas até o círculo vermelho de 30 metros; com a barreira ligada, a regra muda. No canteiro urbano, pessoas não envolvidas e não anuentes são o pedestre, o vizinho, o motorista; os seus operários, informados e de acordo, são outra situação. Lembra da câmera térmica da aula passada, que a 30 metros enxergava defeitos de 8 centímetros? Agora você sabe de onde veio esse número."

**[TELA]** Slide 8 — os números do RBAC nº 100 e os cartões SISANT, Piloto e Seguro.

> "Além das categorias, o RBAC 100 traz outros requisitos. As aeronaves das categorias aberta e específica são cadastradas no SISANT, o sistema de aeronaves não tripuladas da ANAC, com cadastro válido por 24 meses e identificação na própria aeronave. O piloto remoto precisa ser aprovado em exame de conhecimento teórico da ANAC — e aqui tem uma transição: o exame passa a ser exigível a partir de 1º de janeiro de 2027. E as operações devem ter seguro com cobertura de danos a terceiros — o seguro que o setor chama de RETA —, com poucas exceções."

> "E os drones pequenininhos? Os de até 250 gramas ficam fora do RBAC 100, com regras simplificadas da Resolução 806 — desde que voem até 120 metros e em linha de visada. Mas atenção a dois detalhes: é 250 gramas, não 25 quilos; e eles continuam sujeitos às regras do DECEA."

### 4. DECEA: o espaço aéreo tem dono (6:30 – 8:40)

**[TELA]** Slide 9 — foto da placa de zona proibida para drones: "O espaço aéreo tem dono".

> "Isso nos leva à segunda porta. A ANAC cuida da aeronave e do operador. Mas o espaço aéreo — inclusive o que está sobre o seu canteiro — é do DECEA. A ICA 100-40, a instrução do Comando da Aeronáutica para aeronaves não tripuladas, na edição de 2026, determina que o acesso ao espaço aéreo seja solicitado pelo SARPAS, o sistema de solicitação de acesso. Não importa se o drone é pequeno e o voo é baixo: passa pelo SARPAS — inclusive o drone de 250 gramas."

> "A antecedência do pedido cresce com o risco. Um voo além da linha de visada, por exemplo, pede a solicitação com 8 dias de antecedência. E a localização importa muito: muitas obras urbanas ficam perto de aeroportos, helipontos de hospitais e prédios, ou de áreas restritas. Nesses casos, a análise é específica, e o pedido pode ser negado ou exigir condições. Antes de prometer um voo ao cliente, abra o mapa e veja o que existe em volta."

**[TELA]** Slide 10 — calendário do SARPAS: a sexta-feira do voo e a segunda-feira do pedido.

> "E agora um ponto que pega muita obra de surpresa: o aerolevantamento. Se você voa em faixas sobrepostas para gerar ortomosaico, modelo do terreno ou planta planialtimétrica — exatamente o levantamento que mediu os 39 mil metros cúbicos da Aula 1 —, isso é aerolevantamento, pelo artigo 8º da Portaria 3.703 do Ministério da Defesa. Só pode ser executado por entidade inscrita no ministério. Pelo artigo 38, áreas pequenas — dentro de um círculo de até 2,2 quilômetros de raio, ou menos de 15 quilômetros quadrados — ficam pré-autorizadas, desde que atendidas condições cumulativas, como não tocar áreas sujeitas a restrição. Mas a pré-autorização não dispensa a inscrição, nem o pedido no SARPAS, que sai com 4 dias corridos de antecedência. Para voar na sexta-feira, dia 20, o pedido sai até a segunda-feira, dia 16. Já a foto de inspeção ou o vídeo de avanço, sem faixas sobrepostas, não é aerolevantamento."

### 5. Anatel e LGPD (8:40 – 10:20)

**[TELA]** Slide 11 — o selo de homologação Anatel e as faixas de 2,4 GHz e 5,8 GHz.

> "Terceira porta: a Anatel. O drone transmite: o enlace de comando, o vídeo e, às vezes, correções RTK pela rede celular. Todo transmissor comercializado e usado no Brasil precisa ser homologado pela Anatel, que verifica se o equipamento opera nas faixas e potências permitidas — os drones costumam usar as faixas de 2,4 e de 5,8 gigahertz. Na prática: confira o selo e o código de homologação no equipamento ou na embalagem, e desconfie do importado 'sem selo', comprado barato no exterior. E guarde isso para a Unidade 3: a mesma exigência vale para os rádios dos sensores IoT — LoRaWAN, Wi-Fi, celular."

**[TELA]** Slide 12 — LGPD: imagem de pessoa é dado pessoal.

> "E uma porta que não é aeronáutica, mas é lei: a LGPD, a Lei Geral de Proteção de Dados, a Lei 13.709 de 2018. Imagens que identificam trabalhadores, vizinhos e placas de veículos são dados pessoais. Defina a finalidade do voo, capture só o necessário, controle quem acessa e por quanto tempo guarda. A gente aprofunda isso na Aula 16, que fecha a disciplina. E, por fim, a responsabilidade: o cumprimento das regras é do operador e do piloto remoto. Voo irregular gera sanções e pode invalidar a cobertura do seguro — justamente quando você mais precisaria dele."

### 6. Exemplo numérico: quanto do canteiro dá para voar? (10:20 – 12:50)

**[TELA]** Slide 13 — planta do canteiro de 80 × 50 m com a calçada e a faixa de 30 m (arraste a linha de pedestres).

> "Vamos aplicar, com valores ilustrativos. Um canteiro urbano retangular de 80 por 50 metros, 4 mil metros quadrados. Ao longo do lado de 80 metros, uma calçada movimentada; nos outros lados, muros de lotes vazios. A construtora quer voar em categoria aberta, sem barreira mecânica, a 60 metros de altura."

> "Para manter 30 metros horizontais dos pedestres, eu só posso sobrevoar a faixa do terreno que está a mais de 30 metros da calçada. A largura dessa faixa é 50 menos 30: 20 metros. A área voável é 80 vezes 20: 1.600 metros quadrados. Dividindo por 4 mil, 40%. Só 40% do canteiro pode ser sobrevoado diretamente."

> "E agora? Repara que a conta não acaba na reprovação; ela abre alternativas de engenharia. Primeira: interditar a calçada durante o voo, com autorização da prefeitura, num horário de pouco movimento. Segunda: uma barreira capaz de proteger as pessoas — e atenção, um tapume comum não foi pensado para segurar um drone caindo. Terceira: enquadrar a operação na categoria específica, com avaliação de risco. E, como é um mapeamento em faixas sobrepostas, entra o aerolevantamento: empresa inscrita e pedido no SARPAS com 4 dias corridos. O planejamento regulatório faz parte do cronograma do levantamento."

### 7. Pausa para reflexão: o voo que 'ninguém vai notar' (12:50 – 14:50)

**[TELA]** Slide 14 — Pausa para reflexão: "Quinta-feira, 17h".

> "Agora, a pausa para reflexão. Quinta-feira, cinco da tarde. O gerente do contrato liga: 'Preciso do ortomosaico do canteiro amanhã às nove para a reunião com o cliente. É um voo de 15 minutos, ninguém vai notar'. Você sabe que o pedido no SARPAS para aerolevantamento exige 4 dias, que às oito da manhã a calçada estará cheia de pedestres e que o piloto ainda não fez o exame teórico. O que você faz?"

> "Pausa o vídeo e pense um pouco antes de continuar. Pese os dois lados. O custo de chegar à reunião sem o produto é real: o cliente vai cobrar. Mas compare com o custo de um drone caindo sobre um pedestre, de um seguro que não cobre um voo irregular e de uma autuação para a empresa — e para você."

> "E aí vem a parte que separa o engenheiro do executor: existe uma alternativa legal que atenda parcialmente ao cliente? Talvez fotos de inspeção, sem faixas sobrepostas, voadas dentro da área voável, mostrando o avanço visual. Talvez o último ortomosaico regular, combinado com a medição de campo da semana. E, principalmente, como você comunica isso ao gerente — com a mesma clareza com que respondeu ao cliente na Aula 1, com números e alternativas. Segurança em primeiro lugar não é slogan pendurado no contêiner: é uma decisão que o engenheiro toma, e assina."

### 8. O checklist regulatório (14:50 – 16:30)

**[TELA]** Slide 15 — checklist interativo com nove itens; marque-os enquanto fala, sem ler cada um.

> "Tudo isso cabe num checklist de nove itens, que está na tela. Eu vou marcando. Categoria no RBAC 100, com a verificação dos 30 metros. Cadastro no SISANT. Piloto habilitado. Seguro contra terceiros. Avaliação de risco. Pedido no SARPAS, com a antecedência certa. Aerolevantamento: sim ou não, e por quê. Homologação Anatel. E LGPD. Três deles pegam mais gente: o SARPAS, o aerolevantamento quando é mapeamento e a LGPD. Imprime a lista e cola na tampa da maleta do drone."

> "E um último caso, para treinar: um multirrotor de 9 quilos, em linha de visada, a 80 metros, sobre um canteiro urbano, com a área sob o voo isolada e os 30 metros respeitados, fazendo mapeamento. Cabe na categoria aberta? Cabe. Mas 'categoria aberta' não quer dizer 'liberado': continuam valendo SISANT, piloto, seguro, SARPAS, Anatel — e, por ser mapeamento, o aerolevantamento."

### 9. Atividade prática + encerramento (16:30 – 18:30)

**[TELA]** Slide 16 — Atividade prática.

> "Sua missão: escolha uma obra da sua cidade e monte o checklist regulatório para voar sobre ela. Enquadramento no RBAC 100, verificando os 30 metros com uma planta ou uma imagem de satélite. SISANT, piloto, seguro, avaliação de risco, SARPAS com a antecedência, aerolevantamento — sim ou não, e por quê —, Anatel e LGPD. E abra um mapa para ver se há aeródromo ou heliponto por perto. Você vai se surpreender com quantas obras estão perto de um heliponto."

**[TELA]** Slide 17 — Pontos-chave; Slide 18 — encerramento e gancho para a Aula 4.

> "Vamos amarrar. A ANAC regula aeronave, operador e piloto; o DECEA, o espaço aéreo, pela ICA 100-40 e pelo SARPAS; a Anatel homologa os rádios. O RBAC 100, de 2026, substituiu o RBAC-E 94 e classifica operações por risco: aberta, específica e certificada. Na aberta: até 25 quilos, linha de visada, até 120 metros e nunca a menos de 30 metros de pessoas não envolvidas e não anuentes. Mapeamento em faixas sobrepostas é aerolevantamento. E imagem de pessoa é dado pessoal."

> "Agora você já sabe se pode voar. Falta saber como voar. A que altura? Com quanta sobreposição entre fotos? Em qual aplicativo eu desenho a missão? E o vento, a chuva, a bateria no frio? Na próxima aula, que fecha a Unidade 1, a gente planeja a missão completa e monta os procedimentos de segurança. Te espero na Aula 4. Um abraço!"

---

## Roteiro da Videoaula 4 — "Vento fraco no chão, rajada a 70 metros: o voo seguro começa antes da decolagem"

**Duração-alvo:** cerca de 18:40 (17 a 19 minutos).

### 1. Abertura (0:00 – 1:20)

**[TELA]** Slide 1 — capa; Slide 2 — sumário.

> "Olá! Bem-vindo, bem-vinda à quarta aula — a que fecha a Unidade 1. Até aqui, você viu por que medir a obra, qual drone e qual sensor usar e o que a lei exige. Hoje a gente coloca o drone no ar — mas do jeito profissional, que começa no chão. E começo com uma história que acontece mais do que se imagina."

**[TELA]** Slide 3 — o voo que voltou com 8% de bateria e as fotos tremidas.

> "O levantamento do canteiro de 12 hectares está autorizado; o pedido no SARPAS foi aceito. Às sete da manhã, o piloto decola com vento fraco no chão. A 70 metros, o drone luta contra rajadas, gasta bateria na volta contra o vento e pousa com 8% de carga, a 200 metros do ponto previsto. No escritório, metade das fotos saiu tremida, e o modelo tem buracos. Ninguém quebrou regra nenhuma da aula passada. O que faltou foi planejamento. Nesta aula, você vai aprender a planejar a missão, a ler o tempo antes de decolar e a seguir os procedimentos de segurança que separam um voo profissional de uma aposta."

### 2. Tipos de missão (1:20 – 2:50)

**[TELA]** Slide 4 — os tipos de missão: grade, grade dupla/oblíqua, corredor, órbita e manual (animação de cada trajetória).

> "Primeiro, o tipo de missão, que segue o objetivo. Mapeamento em área, em grade: faixas paralelas, como um cortador de grama, com a câmera apontada para baixo. É o voo do ortomosaico, do modelo de terreno e do volume. Grade dupla e oblíqua: faixas cruzadas e câmera inclinada, para modelos 3D de edificações, com as fachadas. Corredor, ou linear: faixas ao longo de um eixo — rodovia, ferrovia, adutora, linha de transmissão. Órbita e pontos de passagem, os waypoints: o voo ao redor de uma estrutura ou por pontos definidos — ótimo para registrar o avanço sempre do mesmo ângulo, mês após mês. E o voo manual, para inspecionar detalhes, sempre com o piloto em linha de visada."

### 3. Os parâmetros do plano: GSD, altura e sobreposição (2:50 – 5:20)

**[TELA]** Slide 5 — GSD: o tamanho do pixel no terreno (arraste a altura e veja o pixel crescer).

> "Agora os parâmetros. O primeiro é o GSD — ground sample distance, a distância de amostragem no solo. É o tamanho, no terreno, de um pixel da imagem. Por semelhança de triângulos entre o sensor e o terreno, GSD é a altura acima do terreno vezes o tamanho do pixel no sensor, dividido pela distância focal. GSD de 2 centímetros quer dizer que cada pixel 'enxerga' um quadrado de 2 por 2 centímetros no chão. Olha a simulação: eu arrasto a altura de 50 para 100 metros, e o pixel dobra. Dobrar a altura dobra o GSD. Por isso o 'quanto mais alto, mais rápido' do nosso piloto cobra um preço em resolução."

**[TELA]** Slide 6 — a faixa imageada e a sobreposição lateral entre faixas vizinhas.

> "A largura da faixa que cada foto cobre no terreno é o número de pixels no sentido transversal ao voo vezes o GSD. E as faixas vizinhas precisam se sobrepor: o espaçamento entre faixas é a largura da faixa vezes 1 menos a sobreposição lateral. Para fotogrametria de obra, usam-se em geral 75 a 80% de sobreposição frontal, entre fotos da mesma faixa, e 65 a 75% lateral, entre faixas. Por que tanto? Porque a fotogrametria precisa ver cada ponto do terreno em várias fotos, de posições diferentes. A teoria fica para a Aula 5; aqui, você só precisa saber escolher os números."

> "E com o espaçamento entre faixas você calcula quanto um voo cobre: a velocidade, vezes o tempo útil, vezes o espaçamento. Como o cortador de grama: velocidade vezes tempo vezes a largura que avança a cada passada. Por fim, a velocidade tem limite: durante a exposição da foto, o drone anda, e esse arrasto deve ficar abaixo de meio pixel, senão a foto sai tremida — lembra das fotos do nosso piloto?"

### 4. Aplicativos de missão: DJI Pilot e Pix4Dcapture (5:20 – 7:20)

**[TELA]** Slide 7 — tela de um aplicativo de planejamento: o polígono, as faixas e os parâmetros calculados.

> "Ninguém calcula essas faixas na mão no campo. Os aplicativos de planejamento transformam os parâmetros numa rota automática. No DJI Pilot, o aplicativo das aeronaves corporativas da DJI, você escolhe o tipo de missão — mapeamento de área, oblíqua, linear ou waypoints —, desenha o polígono sobre o mapa e define o GSD ou a altura, as sobreposições, a velocidade e o que o drone faz ao terminar. O Pix4Dcapture, hoje chamado PIX4Dcapture Pro, faz o mesmo para drones de vários fabricantes, com grades simples, duplas e órbitas, e ainda envia as fotos direto para o processamento. E existem opções abertas, como o Mission Planner, que está na tela, e o QGroundControl."

> "Mas preste atenção nesta frase: o aplicativo calcula; quem responde pelo plano é o engenheiro. Quatro conferências que o aplicativo não faz por você. Primeira: a altura é sobre o terreno, não sobre a decolagem; se o canteiro tem um morro de 20 metros, ali o drone voa mais baixo, o GSD melhora, a faixa encolhe e a sobreposição cai — e aparecem os buracos no modelo. Use o voo acompanhando o relevo, ou planeje pelo ponto mais alto. Segunda: os obstáculos — grua, torre, fios. Terceira: o polígono tem que caber no que foi autorizado no SARPAS. E quarta: a altura de retorno automático, que a gente vê daqui a pouco."

### 5. Condições meteorológicas (7:20 – 10:00)

**[TELA]** Slide 8 — o vento cresce com a altura: perfil de vento animado de 10 m a 120 m.

> "Agora, o tempo. O vento é o principal limitador do voo, e eu quero que você guarde três coisas. Primeira: o vento aumenta com a altura. O que você sente no chão, junto ao tapume, subestima o que o drone enfrenta a 70 metros. Olha o perfil na tela: a seta cresce à medida que sobe. Segunda: as rajadas mandam mais do que a média. Um vento médio aceitável com rajadas fortes derruba a qualidade das fotos e a margem de segurança. Terceira: o voo contra o vento consome mais bateria — e a volta para casa, se for contra o vento, pode ser a parte mais cara da missão. Foi exatamente o que aconteceu com o nosso piloto."

**[TELA]** Slide 9 — a biruta e o anemômetro portátil.

> "Como decidir? Respeite o limite de resistência ao vento do fabricante, com folga: uma regra prática é não passar de uns dois terços dele. Meça no local, com um anemômetro portátil como este da tela, e observe uma biruta ou qualquer referência de vento. Essa biruta está quase toda inflada: vento considerável. E consulte as fontes oficiais: a REDEMET, do DECEA, traz o METAR e o TAF — o boletim e a previsão dos aeródromos próximos —, e o INMET traz a previsão do tempo."

**[TELA]** Slide 10 — chuva, visibilidade e luz: as condições para uma boa fotogrametria.

> "Chuva e umidade danificam motores e eletrônica. Mesmo aeronaves com grau de proteção IP toleram chuva leve, não temporal. Visibilidade e teto de nuvens condicionam a linha de visada. E a luz conta para a qualidade: para fotogrametria, prefira sol alto, com sombras curtas, ou céu uniformemente nublado. Manhã cedo e fim de tarde dão sombras longas, que confundem o processamento e escondem detalhes."

### 6. Temperatura, bateria e clima espacial (10:00 – 11:40)

**[TELA]** Slide 11 — a bateria LiPo e a curva de tensão no frio e no calor.

> "A bateria LiPo merece atenção especial. No frio, a resistência interna aumenta, a tensão cai sob carga e a bateria entrega menos energia útil — o alarme de bateria baixa pode tocar bem antes do esperado. No calor, ela se degrada: em dias acima de 35 graus, comuns no verão brasileiro, motores, eletrônica e bateria aquecem, e o ar menos denso exige mais potência dos motores. Consulte a faixa de operação do fabricante, aqueça as baterias antes de voar em dias frios e reduza o tempo útil planejado nas condições extremas."

**[TELA]** Slide 12 — o índice Kp e a cintilação ionosférica sobre o Brasil.

> "E tem um 'tempo' que pouca gente olha: o clima espacial. O índice Kp, de 0 a 9, mede a atividade geomagnética; a partir de 5 temos tempestade geomagnética, que pode degradar o GNSS. E aqui tem uma particularidade brasileira: como o Brasil está perto do equador magnético, a cintilação ionosférica — uma perturbação nos sinais dos satélites —, comum depois do pôr do sol em períodos de alta atividade solar, pode prejudicar o RTK mesmo com Kp baixo. Se o seu RTK não fixa no fim da tarde, essa pode ser a explicação."

### 7. Procedimentos de segurança (11:40 – 14:20)

**[TELA]** Slide 13 — checklist antes, durante e depois do voo.

> "Agora os procedimentos de segurança, em três momentos. Antes do voo: documentos — SISANT, habilitação, seguro, autorização no SARPAS, avaliação de risco; meteorologia e Kp; inspeção da aeronave — hélices, braços, baterias carregadas e equilibradas, firmware; calibração de bússola e IMU quando o aplicativo pedir; a altura de retorno automático; e a área de segurança: decolagem e pouso isolados, sem circulação de pessoas, e um briefing rápido com o observador."

> "Durante o voo: manter a linha de visada; monitorar bateria, sinal e GNSS; guardar reserva de bateria para o retorno com vento contrário; e interromper se uma pessoa não anuente entrar na área. Depois do voo: registrar data, local, duração e ocorrências; inspecionar a aeronave; conferir as fotos ainda em campo — descobrir o buraco no modelo no escritório custa um novo voo — e armazenar as baterias com carga de armazenamento, nunca totalmente cheias por semanas."

**[TELA]** Slide 14 — simulação de emergências: clique em Perda de enlace com a grua no caminho.

> "E as emergências. Perda de enlace: o drone entra em retorno automático, o RTH, sobe até a altura configurada e volta em linha reta para casa. Olha a simulação: o RTH está configurado em 30 metros, e há uma grua de 55 metros no caminho. Clico em perda de enlace: o drone sobe a 30 metros e... vai direto na grua. Por isso a altura de RTH tem que ficar acima do maior obstáculo, com margem. Perda de GNSS: o drone passa a modo de atitude e deriva com o vento — o piloto assume no manual. Bateria crítica: pousar no local seguro mais próximo. E aeronave tripulada à vista — um helicóptero, por exemplo: descer e se afastar. Ela tem prioridade, sempre."

> "Repare que nenhuma dessas respostas pode ser inventada na hora. Num voo, as emergências se resolvem em segundos, e quem decide bem é quem já decidiu antes: a altura de retorno foi configurada no planejamento, o local alternativo de pouso foi escolhido na vistoria, o observador sabe o que gritar e para quem. Por isso as grandes operadoras treinam as emergências no simulador e repetem o briefing antes de cada voo, mesmo quando a equipe é a mesma da semana passada. E, se algo der errado, registre: o relatório de ocorrência, com o log de voo do aplicativo, é a matéria-prima para melhorar o procedimento da próxima vez — de novo, a malha fechada da Aula 1, agora aplicada à própria segurança da operação."

### 8. Exemplo numérico: altura, cobertura e vento (14:20 – 17:10)

**[TELA]** Slide 15 — calculadora: altura máxima para o GSD, faixa e espaçamento.

> "Vamos às contas, com valores ilustrativos. Uma câmera de 20 megapixels, com 5.472 por 3.648 pixels, pixel de 2,41 micrômetros e focal de 8,8 milímetros. O contrato pede GSD de no máximo 2 centímetros. A altura máxima é o GSD vezes a focal, dividido pelo pixel: 0,02 vezes 8,8, dividido por 0,00241 — dá cerca de 73 metros. Adoto 70 metros, com folga para o relevo. O GSD fica em 1,92 centímetro. A faixa: 5.472 pixels vezes 1,92 centímetro, uns 105 metros. Com 70% de sobreposição lateral, o espaçamento entre faixas é 105 vezes 0,3: 31,5 metros."

**[TELA]** Slide 16 — o canteiro de 12 ha voado em faixas; a área por voo do multirrotor e do VTOL.

> "Quanto um voo cobre? Multirrotor com 30 minutos de autonomia, dos quais 70% são úteis — tirando reserva, decolagem, pouso e curvas —: 21 minutos, 1.260 segundos, a 6 metros por segundo. A área: 6 vezes 1.260 vezes 31,5, cerca de 238 mil metros quadrados — uns 23,8 hectares. O canteiro de 12 hectares da Aula 1 cabe num voo, com folga. Um VTOL a 16 metros por segundo, com 41 minutos úteis, cobriria uns 124 hectares — é a escolha da Aula 2 para rodovias."

**[TELA]** Slide 17 — calculadora do vento na altura de voo (vento no solo inicial de 6 m/s).

> "E agora a conta que teria salvado o nosso piloto. O anemômetro mede 6 metros por segundo a 10 metros de altura. Pela lei de potência do perfil de vento, com expoente ilustrativo de 0,2, típico de terreno com obstáculos, o vento a 70 metros é 6 vezes 7 elevado a 0,2. Sete elevado a 0,2 dá cerca de 1,48. O vento a 70 metros: perto de 8,9 metros por segundo. Se o fabricante indica resistência de 12 metros por segundo, o limite prático de dois terços é 8. O vento na altura de voo passa do limite: o voo deve ser adiado — ou feito mais baixo, com mais faixas. O vento 'fraco' do chão era forte lá em cima. A decisão estava numa conta de um minuto."

> "E repare como as três contas conversam. Se eu decido voar mais baixo para fugir do vento, digamos a 50 metros, o GSD melhora para uns 1,4 centímetro, mas a faixa encolhe para uns 75 metros, o espaçamento cai para uns 22 metros e a área por voo cai junto — talvez eu precise de uma segunda bateria. Planejar é isso: cada escolha mexe nas outras, e o engenheiro fecha o conjunto antes de decolar."

### 9. Atividade prática, síntese da unidade e prévia da Unidade 2 (17:10 – 18:40)

**[TELA]** Slide 18 — Atividade prática e pontos-chave.

> "Sua missão: instale um aplicativo de planejamento — DJI Pilot, Pix4Dcapture ou o Mission Planner, que é gratuito — ou use as fórmulas da aula, se não tiver drone. Para uma obra de sua escolha, desenhe o polígono, defina GSD, altura, sobreposições e velocidade, e anote o número de faixas, de fotos e o tempo de voo. Depois, consulte a REDEMET ou o INMET e o índice Kp do dia, e escreva a decisão: voa ou não voa, com justificativa. E feche com o seu checklist pré-voo, em uma página."

**[TELA]** Slide 19 — prévia da Unidade 2: fotogrametria, GNSS, ortomosaico, nuvem de pontos e volumes.

> "E com isso fechamos a Unidade 1. Você sabe por que e como medir o avanço da obra, com curva S e valor agregado; qual drone e qual sensor usar para cada pergunta; o que ANAC, DECEA e Anatel exigem; e como planejar um voo seguro. Na Unidade 2, as fotos desse voo viram produto de engenharia: a fotogrametria e os pontos de controle, o GNSS e a precisão, o ortomosaico, os modelos de superfície e as nuvens de pontos — e o cálculo de volumes, que volta direto para a curva S e para o valor agregado."

**[TELA]** Slide 20 — encerramento: "Unidade 1 concluída".

> "Foi um prazer construir esses fundamentos com você. Te espero na Unidade 2. Um abraço!"
