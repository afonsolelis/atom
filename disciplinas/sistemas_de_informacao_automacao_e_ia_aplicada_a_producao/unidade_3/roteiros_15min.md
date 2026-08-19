# Roteiros Estendidos (15+ minutos) — Unidade 3: Automação Industrial

- **Disciplina:** Sistemas de Informação, Automação e IA Aplicada à Produção
- **Conteudista:** Afonso Cesar Lelis Brandão
- **Videoaulas:** 9 a 12
- **Formato:** roteiro de narração **quase integral** — o texto em citação (>) é a fala completa, pronta para leitura no teleprompter ou gravação. Duração-alvo: **15 a 17 minutos** por aula, considerando ritmo de fala de 130–150 palavras por minuto mais as pausas naturais de apresentação.

> **Como usar:** leia as falas em citação na ordem. As marcações **[TELA]** indicam o recurso visual que deve estar no ar naquele momento. Os poucos bullets são lembretes de gesto/ênfase, não conteúdo novo.

---

## Roteiro da Videoaula 9 — "Sensor, atuador, controlador: o ABC da automação"

**Duração-alvo:** 15 a 17 minutos.

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide de capa da aula 9.

> "Olá! Seja muito bem-vindo, seja muito bem-vinda à Unidade 3 da nossa disciplina de Sistemas de Informação, Automação e IA Aplicada à Produção. Deixa eu te situar rapidinho no mapa da nossa jornada. Na Unidade 1, a gente construiu a base: o que é dado, o que é informação, o que é um sistema de informação. Na Unidade 2, a gente subiu para o andar corporativo: ERP, MES, CRM — os sistemas que rodam a empresa. E agora, nesta Unidade 3, a gente desce a escada. Desce literalmente até o chão de fábrica físico: sensores, atuadores, CLPs, SCADA. É a parte da disciplina que suja a mão de graxa — e eu te garanto que é uma das mais gostosas."

> "E eu quero começar com uma provocação. Toda automação industrial do planeta — da esteira do caixa do supermercado até uma plataforma de petróleo, de uma máquina de café automática até uma linha de montagem de carros — toda automação, sem exceção, é construída com o mesmo trio de blocos elementares: **sensor**, **controlador** e **atuador**. Três blocos. Só três. Se você dominar esse ABC hoje, todas as próximas aulas vão se encaixar como peças de Lego. Então respira, pega o caderno, e vamos nessa."

### 2. O que é automação industrial — e o que ela não é (1:30 – 3:30)

**[TELA]** Definição em destaque.

> "Vamos começar alinhando o vocabulário. Automação industrial é o uso de **sistemas de controle** para operar equipamentos e processos com **mínima ou nenhuma intervenção humana direta**. Guarda essa frase, porque ela cai em prova e cai na vida. E repara no propósito: a automação existe para substituir três tipos de trabalho. O trabalho **repetitivo**, que entedia e gera erro. O trabalho **perigoso**, que machuca gente. E o trabalho de **altíssima precisão**, que o ser humano simplesmente não consegue sustentar por oito horas seguidas."

> "Agora, um mito que eu preciso desfazer logo de cara: automação **não** nasceu com a Indústria 4.0. Não senhor. Automação existe desde a Segunda Revolução Industrial — linha de montagem, relés eletromecânicos, controle de máquinas a vapor. O que a Indústria 4.0 mudou não foi a automação em si; foi a **integração** da automação com dados, com internet e com inteligência artificial. Mas o esqueleto, a espinha dorsal, continua exatamente a mesma de cem anos atrás: sensor lê, controlador decide, atuador age."

> "E olha que interessante: você convive com isso todos os dias sem perceber. O ar-condicionado do seu quarto é uma malha de controle completa. O termostato é o sensor. A placa eletrônica é o controlador. O compressor é o atuador. Você define 23 graus — isso é o setpoint — e o sistema trabalha sozinho para manter. Automação industrial é isso, só que em escala de fábrica."

### 3. O ciclo básico de controle: malha fechada (3:30 – 6:00)

**[TELA]** Diagrama do ciclo: sensor → controlador → atuador → processo → sensor.

> "Presta atenção neste desenho, porque ele é a aula inteira resumida em uma imagem. Vou narrar o ciclo devagar. Primeiro: o **sensor lê** uma grandeza do processo — pode ser temperatura, pressão, velocidade, nível, o que for. Segundo: o **controlador compara** o valor lido com o valor desejado, que a gente chama de *setpoint*. Terceiro: o **controlador decide** o que fazer com base nessa comparação. Quarto: o **atuador age** — abre uma válvula, acelera um motor, liga uma resistência, desliga tudo. Quinto: o **processo muda** por causa dessa ação. E sexto: o **sensor lê de novo**. E o ciclo recomeça. E recomeça. E recomeça — o dia inteiro, a noite inteira, o ano inteiro."

> "Esse arranjo tem nome técnico: **controle em malha fechada**, ou *closed loop* em inglês. Fechada por quê? Porque a informação dá a volta completa: a consequência da ação volta para o sensor, que informa o controlador, que ajusta a próxima ação. A decisão depende do retorno da medição."

> "Existe também a **malha aberta**, que é o primo simplório: comando sem retorno. Quer um exemplo doméstico? A torradeira. Você gira o botão para dois minutos, e ela torra por dois minutos — ela não faz a menor ideia se o pão está torrado, queimado ou congelado. Ela só cumpre o tempo. Isso é malha aberta: age, mas não confere."

> "E aqui vai uma pergunta para você responder aí do outro lado: o chuveiro elétrico da sua casa é malha aberta ou fechada? Pensa dois segundos… A maioria é **aberta**! A resistência esquenta com potência fixa e quem fecha a malha é **você**, girando o registro quando a água está fria ou quente demais. Você é o sensor e o controlador do seu banho. Na automação industrial séria, a gente tira o humano desse papel: **malha fechada é o padrão**. Malha aberta só sobrevive em tarefa trivial."

### 4. Sensores: os sentidos da fábrica (6:00 – 9:00)

**[TELA]** Tabela de tipos de sensores, revelando linha a linha.

> "Vamos abrir o primeiro bloco do trio: o sensor. Sensor é o órgão dos sentidos da fábrica. A definição técnica: sensores **traduzem grandezas físicas em sinais elétricos** que o controlador consegue entender. Calor vira milivolts. Pressão vira miliampères. Movimento vira pulsos. Vamos passear pela tabela dos tipos mais usados — e eu quero que você repare que cada linha resolve uma dor real da indústria."

> "**Temperatura**: termopar, PT100, sensor infravermelho. Onde? Fornos, motores, câmaras de refrigeração. É provavelmente o sensor mais onipresente da indústria. **Pressão**: transdutores piezoelétricos, medindo força por área em compressores, tubulações, sistemas hidráulicos. **Vazão**: quanto fluido passa por segundo — medidores eletromagnéticos, ultrassônicos e o Coriolis, que é o rolls-royce da medição de vazão. **Nível**: quanto tem dentro do silo, do tanque, da caldeira — sensores capacitivos, ultrassônicos e de radar."

> "Seguindo: **posição e velocidade** — encoders, LVDTs, tacômetros — são os olhos dos robôs, das esteiras e das máquinas CNC; sem eles, nenhum movimento de precisão existe. **Vibração**: acelerômetros piezoelétricos. Anota esse, porque ele é a estrela da **manutenção preditiva** que a gente vai ver na Unidade 4 — a vibração de um motor conta a história da saúde dele. **Proximidade**: sensores indutivos, capacitivos e ópticos, detectando presença ou ausência de peça na esteira. E por fim, **visão**: câmera mais software, fazendo inspeção, contagem e segurança — outro gancho direto para a Unidade 4."

> "Agora, um recado de engenheiro para engenheiro: sensor não se escolhe pelo nome, se escolhe pela **folha de dados**. Todo sensor tem especificações técnicas: faixa de medição, precisão, repetibilidade, tempo de resposta, temperatura de operação e grau de proteção IP — que eu vou explicar daqui a pouco. Comprar sensor errado é dinheiro jogado fora. E em ambiente crítico, é risco de acidente. A folha de dados é sua amiga."

### 5. Sinais: analógico versus digital e o padrão 4-20 mA (9:00 – 11:00)

**[TELA]** Comparativo: analógico (4-20 mA / 0-10 V) vs digital (on/off).

> "Beleza, o sensor mediu. Mas como essa medição viaja até o controlador? De duas formas. A primeira é o sinal **analógico**: um valor contínuo, que normalmente é representado por corrente — o famoso **4 a 20 miliampères** — ou por tensão, de **0 a 10 volts**. A temperatura sobe, a corrente sobe junto, proporcionalmente. A segunda forma é o sinal **digital**: discreto, liga ou desliga, zero ou um. O sensor de proximidade é o exemplo perfeito: peça presente, manda um; peça ausente, manda zero. Não existe meio termo."

> "Agora deixa eu te contar por que a indústria é apaixonada pelo 4-20 miliampères — porque tem uma sacada de engenharia linda aqui. Primeiro motivo: sinal de corrente sofre muito menos com interferência eletromagnética e com a distância do cabo do que sinal de tensão. Fábrica é um ambiente eletricamente barulhento — motores ligando, inversores chaveando — e a corrente atravessa esse caos com muito mais robustez."

> "Segundo motivo, e esse é o elegante: repara que o **zero da escala é 4 miliampères**, não zero miliampère. Por quê? Porque se o controlador ler **0 mA**, ele sabe instantaneamente que aconteceu uma de duas coisas: ou o fio rompeu, ou o sensor morreu. O próprio sinal denuncia o próprio defeito! Isso tem nome: *live zero*, o zero vivo. Se a escala começasse em zero, você nunca saberia se está medindo 'zero grau' ou se o cabo foi cortado. Engenharia boa é isso: o projeto que já prevê a falha."

> "Um exemplo rápido de conversão para fixar: termopar com faixa de 0 a 1200 graus em 4-20 mA. Então 4 miliampères significa 0 grau, 20 miliampères significa 1200 graus. E 12 miliampères — o meio da faixa elétrica — significa 600 graus, o meio da faixa térmica. Regra de três simples. Você vai fazer essa conta a vida inteira."

### 6. Atuadores: os músculos da fábrica (11:00 – 13:00)

**[TELA]** Tabela de atuadores.

> "Segundo bloco do trio: o atuador. Se o sensor é o sentido, o atuador é o **músculo**: ele converte sinal elétrico em ação física. Vamos à galeria."

> "**Motor elétrico**: movimento rotativo — esteiras, ventiladores, bombas. É o cavalo de batalha da indústria; deve haver bilhões deles rodando agora. **Servo-motor**: quando além de girar você precisa de **precisão de posição** — robôs, máquinas CNC. O servo sabe exatamente em que ângulo está. **Cilindro pneumático**: movimento linear com ar comprimido — rápido, limpo, barato — perfeito para prensas leves, fixação de peças, abre-e-fecha. **Cilindro hidráulico**: quando a força necessária é gigante — prensas pesadas, elevadores de carga. Óleo sob pressão move montanhas."

> "Continuando: **válvula solenoide**: abre e fecha fluxo de fluido sob comando elétrico — dosadores, tubulações. **Inversor de frequência**: esse merece destaque — ele controla a **velocidade** do motor elétrico variando a frequência da alimentação. Praticamente todo motor moderno tem um, e além do controle fino ele economiza energia de forma brutal, porque o motor gira só na velocidade necessária. **Resistência de aquecimento**: esquenta forno, caldeira, processo. E o **relé**: o veterano que liga e desliga circuitos elétricos."

> "E o mesmo recado dos sensores vale aqui: atuador também tem folha de dados — potência, torque, velocidade, precisão, vida útil em ciclos. Subdimensionou, quebra. Superdimensionou, pagou caro à toa."

### 7. Controladores: quem decide (13:00 – 14:30)

**[TELA]** Os 4 tipos: CLP, PID, DCS, PAC.

> "Terceiro bloco: entre o sentido e o músculo, precisa existir um **cérebro** — o controlador, que recebe a leitura, compara com o setpoint e decide. Na indústria, esse cérebro aparece em quatro sabores, e você precisa saber qual usar onde."

> "Sabor um: o **CLP**, Controlador Lógico Programável — de longe o mais comum nas fábricas brasileiras. Ele é tão importante que a próxima aula é **inteira** sobre ele, então hoje só registra o nome. Sabor dois: o **PID** — proporcional, integral, derivativo — o controlador clássico para variáveis contínuas como temperatura e pressão; hoje ele quase nunca é uma caixinha separada, ele vive como **função dentro do CLP**. Sabor três: o **DCS**, sistema de controle distribuído — o rei das indústrias de **processo contínuo**: química, petróleo, papel e celulose, energia. Ele distribui a inteligência pela planta inteira. E sabor quatro: o **PAC**, que é um híbrido de CLP com PC industrial, mais flexível e poderoso para aplicações complexas."

> "Regra de bolso para você levar: manufatura **discreta** — autopeças, eletrônicos, coisas que você conta de uma em uma — o CLP domina. Processo **contínuo** — fluidos, reações químicas, coisas que fluem — o DCS reina. E controle fino de uma variável contínua? PID, geralmente embutido no CLP. Cada cérebro no seu nicho."

### 8. Exemplo numérico completo: o forno a 152 graus (14:30 – 16:00)

**[TELA]** Esquema do forno com sensor, CLP, SSR e resistência.

> "Agora vamos montar um caso completo, de ponta a ponta, para o trio virar realidade. Missão de engenharia: um forno industrial precisa ficar entre **150 e 155 graus Celsius**. Vamos especificar juntos."

> "**Sensor**: termopar tipo K, com faixa de 0 a 1200 graus e precisão de mais ou menos 2 graus. Você pode perguntar: 'professor, 1200 graus para medir 152? Não é exagero?' — e a resposta é: o tipo K é robusto, barato e padrão de mercado; sobra de faixa não é problema, falta é. **Sinal**: 4-20 miliampères, pelos motivos que você já sabe — robustez e zero vivo. **Setpoint**: 152 graus, bem no meio da janela pedida, dando folga simétrica para os dois lados."

> "**Controlador**: um PID rodando dentro do CLP, lendo a temperatura uma vez por segundo. **Atuador**: resistência elétrica chaveada por um **SSR** — relé de estado sólido — com **modulação PWM**: liga e desliga muito rápido, e o que varia é a fração de tempo ligado dentro de cada ciclo. Temperatura abaixo de 152? A resistência fica ligada mais tempo no ciclo. Acima? Menos tempo. E uma **histerese de mais ou menos 1 grau** para o sistema não ficar liga-desliga-liga-desliga feito um interruptor nervoso."

> "E um aviso de quem já viu isso na prática: sintonizar as três constantes do PID — a proporcional, a integral e a derivativa — é meio ciência, meio arte. PID mal ajustado faz o forno oscilar feito gangorra, ou demorar uma eternidade para estabilizar. Isso se aprende com o processo, errando em ambiente controlado. Respeita quem sabe sintonizar malha: é ouro no mercado."

### 9. Grau de proteção IP + atividade + encerramento (16:00 – 17:00)

**[TELA]** Escala IP66 → IP69K; depois, enunciado da atividade.

> "Último conceito técnico do dia: o **grau de proteção IP**, de *Ingress Protection*. Todo sensor e atuador industrial tem essa classificação. **IP66**: protegido contra poeira e jato d'água. **IP67**: totalmente vedado contra poeira e aguenta imersão de até um metro por trinta minutos. **IP68**: imersão contínua. **IP69K**: aguenta jato de água **quente sob alta pressão** — pensa na lavagem agressiva de uma fábrica de alimentos. Em ambiente industrial pesado — química, alimentos, mineração — IP67 para cima não é luxo, é requisito de projeto."

> "Sua missão até a próxima aula: escolhe **um** equipamento que você conhece bem — ar-condicionado, geladeira, máquina de lavar, serve qualquer um. E responde quatro perguntas: que **sensores** ele tem e o que medem? Que **atuadores** e o que fazem? Onde mora o **controlador** e como ele decide? E: é malha **fechada ou aberta**? Faz de verdade, escreve. Esse exercício treina o olhar de engenheiro — depois dele, você nunca mais olha para uma máquina do mesmo jeito."

> "Na próxima aula, a gente abre o cérebro mais usado do chão de fábrica brasileiro: o **CLP**. Você vai entender o ciclo de varredura, conhecer as cinco linguagens da norma IEC 61131-3 e aprender a ler a famosa **lógica ladder** — a linguagem que se lê como um esquema elétrico. Te espero lá. Um abraço!"

---

## Roteiro da Videoaula 10 — "CLP e lógica ladder: o cérebro do chão de fábrica"

**Duração-alvo:** 15 a 17 minutos.

### 1. Abertura + pausa para reflexão (0:00 – 2:00)

**[TELA]** Slide de capa da aula 10.

> "Olá! Seja bem-vindo, seja bem-vinda de volta. Deixa eu te contar um fato: se você entrar em **qualquer** fábrica brasileira de médio porte para cima — qualquer uma, de alimentos a autopeças — você vai esbarrar em CLPs. Dezenas deles. Eles são o cérebro mais comum do chão de fábrica nacional e mundial. E hoje a gente vai abrir esse cérebro: entender o que ele é, como ele pensa, e aprender a ler a linguagem que ele fala."

> "Mas antes, uma **pausa para reflexão** — e eu quero que você leve a sério. Imagina que você precisa projetar o seguinte sistema: uma lâmpada deve ligar quando alguém aperta um botão… **mas só se** uma outra chave estiver fechada… **e** ela deve desligar sozinha depois de 30 segundos. Pergunta: como você **descreveria** essa regra, passo a passo, de forma que uma máquina execute sem ambiguidade? Pausa o vídeo por dez, quinze segundos, e formula mentalmente. Pode falar em voz alta, ninguém está ouvindo."

> "Formulou? Guarda a sua resposta. No final desta aula, a gente vai escrever **exatamente** essa regra — em lógica ladder — e você vai comparar com o que pensou. Combinado? Então vamos."

### 2. O que é um CLP e por que ele domina (2:00 – 4:30)

**[TELA]** Definição + foto de CLP com módulos.

> "CLP — Controlador Lógico Programável — é, na definição formal, um **computador industrial** dedicado a executar lógica de controle, operando em ciclos contínuos de leitura de entradas, execução de programa e escrita de saídas. E ele tem história: nasceu em **1969**, na indústria automobilística americana. O problema da época? Os painéis de controle eram armários com **centenas de relés físicos** cabeados um a um. Cada mudança no processo — cada novo modelo de carro — significava semanas de eletricistas refazendo fiação. O CLP nasceu para acabar com isso: a lógica sai do cabo e vai para o software."

> "E por que ele dominou o mundo? Cinco características, e eu quero que você entenda o **porquê** de cada uma. Primeira: ele é **robusto** — projetado para aguentar vibração, calor, poeira, umidade. Um PC de escritório colocado ali morreria em semanas; o CLP vive décadas. Segunda: ele é **confiável** — opera 24 horas por dia, 7 dias por semana, com taxa de falha baixíssima. E precisa ser, porque fábrica parada é dinheiro queimando por minuto."

> "Terceira: ele é **tempo real** — responde em **milissegundos**, sempre, deterministicamente. Não existe 'aguarde, atualizando o sistema' no meio da produção. Quarta: ele é **modular** — precisa de mais dezesseis entradas? Encaixa um módulo. Precisa falar Ethernet industrial? Outro módulo. Cresce conforme a necessidade. E quinta, a que mudou a história: ele é **programável em campo**. Mudou o processo? O engenheiro reescreve a lógica e transfere para o CLP — **sem trocar um único fio**. Essa foi a revolução de 1969, e é ela que sustenta o CLP no trono até hoje."

### 3. O ciclo de varredura — scan cycle (4:30 – 6:30)

**[TELA]** Diagrama do ciclo: leitura → execução → escrita → diagnóstico → repete.

> "Agora, como esse cérebro pensa? Todo CLP do mundo, de qualquer marca, de qualquer tamanho, roda o mesmo loop eterno, chamado **ciclo de varredura** — *scan cycle*. São quatro passos. Passo um: **leitura de entradas** — o CLP fotografa o estado de todos os sensores conectados, todos de uma vez. Passo dois: **execução do programa** — ele roda a lógica programada, de cima a baixo, linha por linha, sobre aquela fotografia. Passo três: **escrita de saídas** — ele comanda os atuadores conforme o que a lógica decidiu. Passo quatro: **diagnóstico interno** — uma checagem rápida da própria saúde. E… volta ao passo um. Para sempre."

> "Quanto tempo leva uma volta completa? Tipicamente entre **5 e 50 milissegundos**, dependendo do tamanho do programa. Faz a conta comigo: 20 milissegundos por ciclo significa **50 varreduras por segundo**. O CLP olha para a fábrica inteira, pensa e age cinquenta vezes por segundo. É isso que 'tempo real' significa na prática."

> "E um detalhe fino, desses que separam o aluno bom do excelente: repara que as entradas são **congeladas** numa fotografia no início do ciclo. O programa inteiro executa sobre a **mesma foto** — mesmo que um sensor mude no meio da execução, o programa só vê a mudança na próxima varredura. Por quê? **Consistência lógica**: todas as linhas do programa decidem sobre o mesmo retrato do mundo. Sem isso, uma metade do programa poderia decidir com um valor e a outra metade com outro. Elegante, né?"

### 4. Anatomia do CLP (6:30 – 8:30)

**[TELA]** Tabela de componentes sobre a foto do equipamento.

> "Vamos abrir o gabinete e olhar a anatomia. No centro, a **CPU** — o processador que executa a lógica; o cérebro do cérebro. Ao lado, os **módulos de entrada**, que recebem os sinais dos sensores — tanto os digitais, liga-desliga, quanto os analógicos, como o nosso 4-20 miliampères da aula passada. Depois, os **módulos de saída**, que comandam os atuadores: motores, válvulas, sinaleiros."

> "Completando o rack: a **fonte de alimentação** — tipicamente 24 volts, o padrão industrial. Os **módulos de comunicação** — Ethernet industrial, serial, às vezes fibra óptica ou wireless — que conectam o CLP aos outros sistemas, incluindo o SCADA que veremos na próxima aula. E a **interface de programação**, geralmente Ethernet ou USB, por onde o programa entra."

> "E como se programa? Num software rodando num PC comum. Cada fabricante tem o seu: **Studio 5000** da Rockwell, **TIA Portal** da Siemens, **GX Works** da Mitsubishi. O fluxo é sempre o mesmo: você escreve a lógica no computador, testa, simula, e **transfere** para o CLP. A partir daí, o CLP executa sozinho, ininterruptamente, por meses e anos — até alguém mandar uma versão nova. O PC pode até ser desligado; o CLP nem percebe."

### 5. As cinco linguagens da IEC 61131-3 (8:30 – 10:30)

**[TELA]** Lista das 5 linguagens, revelando uma a uma.

> "E em que linguagem se escreve essa lógica? Existe uma norma internacional — a **IEC 61131-3** — que padroniza **cinco linguagens** de programação de CLP. Vou apresentar as cinco, e você vai ver que cada uma tem sua personalidade."

> "Número um: **Ladder Logic**, ou LD — a linguagem gráfica em formato de escada, que imita diagramas elétricos. É a protagonista de hoje e daqui a pouco a gente mergulha nela. Número dois: **Function Block Diagram**, FBD — blocos gráficos conectados por linhas; ótima para processamento de sinal e controle contínuo. Número três: **Structured Text**, ST — uma linguagem textual que lembra Pascal; é a escolha para lógica complexa, cálculo, laços; quem vem de programação se sente em casa. Número quatro: **Instruction List**, IL — estilo assembly, linha por linha; está oficialmente aposentada, você só encontra em código legado. E número cinco: **Sequential Function Chart**, SFC — diagramas de máquina de estados; perfeita para processos sequenciais do tipo etapa um, etapa dois, etapa três."

> "Você precisa dominar as cinco? Não. Precisa saber que existem e reconhecer cada uma quando encontrar. Mas precisa entender por que a **ladder ainda reina absoluta no Brasil** — e a razão é histórica e humana. Quando os CLPs chegaram nas fábricas nos anos setenta e oitenta, quem estava lá para operá-los eram os **técnicos eletricistas**, gente acostumada a ler esquemas de relés a vida inteira. A ladder foi desenhada **de propósito** para que essas pessoas lessem um programa de computador como leriam um diagrama elétrico. Foi uma decisão de design centrada no usuário — décadas antes desse termo existir. E deu tão certo que dura até hoje."

### 6. Ladder: os elementos básicos (10:30 – 12:30)

**[TELA]** Símbolos: contato NA, contato NF, bobina, timer, contador.

> "Vamos ao vocabulário da ladder. Imagina dois trilhos verticais — como os lados de uma escada — representando a energia. Entre eles, degraus horizontais, os *rungs*, onde a lógica é montada. Cada degrau é uma frase: condições à esquerda, consequência à direita."

> "Os elementos. Primeiro: o **contato normalmente aberto**, NA — dois tracinhos paralelos. Ele **deixa a corrente passar quando a variável vale 1**. Botão apertado? Passa. Segundo: o **contato normalmente fechado**, NF — os mesmos tracinhos com uma barra no meio. Ele é o contrário: **deixa passar quando a variável vale 0**. Ele é o 'NÃO' da lógica. Terceiro: a **bobina** — um parêntese duplo no fim do degrau — é a **saída**: se o degrau energizou, a bobina liga o que estiver associado a ela: motor, lâmpada, válvula."

> "Tem também a **bobina com retenção** — *latch* e *unlatch* — que liga e **permanece** ligada mesmo que a condição suma, até receber ordem explícita de desligar. Os **temporizadores** — TON, que conta tempo para ligar, e TOF, para desligar. E os **contadores** — CTU contando para cima, CTD para baixo — contando peças, ciclos, eventos."

> "E agora a metáfora que resolve oitenta por cento da leitura de ladder do mundo. Presta atenção: contatos em **série** — um depois do outro no mesmo degrau — formam um **E** lógico: **todos** precisam fechar para a corrente chegar à bobina. Contatos em **paralelo** — um em cima do outro — formam um **OU**: basta **um** fechar. Série é E. Paralelo é OU. Grava isso, tatua isso, porque com essa regra você lê quase qualquer programa ladder que encontrar na vida."

### 7. Resolvendo a reflexão: a lâmpada dos 30 segundos (12:30 – 14:30)

**[TELA]** O diagrama ladder do exemplo (botão + chave + timer), degrau a degrau.

> "Hora de pagar a promessa da abertura. A regra era: lâmpada liga com botão, mas só se a chave estiver fechada, e desliga sozinha após 30 segundos. Olha o diagrama na tela — são só dois degraus — e repara que dá para **ler em voz alta**, como uma frase."

> "**Degrau um**, lendo da esquerda para a direita: contato NA do botão B1, em série com o contato NA da chave S1, em série com um contato **NF** do sinal L_TEMPO… terminando na bobina da lâmpada L. Tradução: **SE** o botão está apertado **E** a chave está fechada **E** o temporizador ainda **não** estourou — **ENTÃO** liga a lâmpada. Viu o E, o E, e o NÃO? Série, série, contato fechado."

> "**Degrau dois**: contato NA da própria lâmpada L, alimentando um bloco **TON de 30 segundos** chamado T1. Tradução: **SE** a lâmpada está acesa, **ENTÃO** o temporizador começa a contar. Quando ele completa os 30 segundos, o sinal L_TEMPO vira 1… e o que acontece lá no degrau um? O contato **NF** de L_TEMPO **abre**, corta a corrente do degrau, e a lâmpada **apaga**. O sistema se desliga sozinho, exatamente como pedido."

> "Compara com a resposta que você formulou na abertura. Aposto que a sua descrição em português tinha as mesmas peças: um E, outro E, um 'enquanto não', um 'depois de 30 segundos'. A ladder é isso: **lógica de controle que se lê como frase**. Aquela regra virou dois degraus de escada. E é assim que milhões de máquinas no mundo estão programadas neste exato momento."

### 8. Mercado de CLPs e o exemplo numérico do payback (14:30 – 16:30)

**[TELA]** Marcas; depois, os números do caso da linha de enchimento.

> "Uma palavra sobre mercado, porque você vai encontrar essas marcas na vida real. Nos Estados Unidos e forte no Brasil: **Rockwell Automation**, dona da linha Allen-Bradley. Líder europeu e global: **Siemens**, com as famílias S7-1200 e S7-1500. Forte na Ásia: **Mitsubishi**. Concorrente histórico: **Schneider Electric**, herdeira da Modicon — que, aliás, foi a marca do primeiro CLP da história. Em nichos: Omron, Beckhoff, B&R. E as brasileiras, que merecem registro: **WEG**, **Altus** e **HI Tecnologia**. E como se escolhe? Na vida real, a decisão raramente é 'qual é o melhor do mundo' — é **integração com o legado que a fábrica já tem, suporte técnico local e preço**."

> "E automação com CLP se paga? Vamos fazer a conta juntos, com um caso de linha de enchimento de garrafas. **Cenário antes**: processo manual, dois operadores enchendo 800 garrafas por hora, custo de mão de obra de 3.500 reais por operador — 7.000 reais por mês. **Cenário depois**: linha automatizada com CLP, sensores e atuadores, produzindo **2.400 garrafas por hora** — o triplo — e um único supervisor cuidando de três linhas ao mesmo tempo. **Investimento**: 220 mil reais, tudo incluído."

> "Agora, a lição mais importante desta conta: o ganho **não** está no salário economizado — 3.500 reais por mês não paga projeto nenhum. O ganho está no **volume**. São 1.600 garrafas a mais por hora; em oito horas de turno, **12.800 garrafas adicionais por dia**. A 80 centavos de margem por garrafa, isso dá **10.240 reais por dia** de margem adicional. Se o mercado absorver tudo, o payback sai em **menos de um mês**. Num cenário realista, com rampa de vendas gradual, **três a seis meses**. Guarda a moral da história: o retorno da automação raramente vem de cortar gente — vem de **produzir mais com o mesmo**."

### 9. Atividade + encerramento e gancho (16:30 – 17:00)

**[TELA]** Enunciado da atividade da esteira.

> "Sua missão de casa, e ela é deliciosa: desenhe — em ladder, ou descreva em português estruturado — a lógica de uma esteira que só pode ligar quando o botão Iniciar for pressionado **E** a porta de segurança estiver fechada **E** não houver produto na estação seguinte. E que deve desligar **imediatamente** se o botão Parar for pressionado **OU** a porta abrir **OU** o sensor detectar produto. Dica de ouro: lembra da regra — série é E, paralelo é OU. As condições de desligar entram em paralelo."

> "E na próxima aula a gente sobe um degrau na pirâmide: o CLP controla **uma** máquina — mas quem enxerga a **fábrica inteira** em tempo real, com telas, alarmes e históricos? É o **SCADA**, os olhos da fábrica. Te espero lá. Um abraço!"

---

## Roteiro da Videoaula 11 — "SCADA: os olhos da fábrica"

**Duração-alvo:** 15 a 17 minutos.

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide de capa da aula 11.

> "Olá! Bem-vindo, bem-vinda de volta. Na aula passada a gente conheceu o CLP — o cérebro que controla uma máquina, em milissegundos, com sua lógica ladder. Agora eu quero que você imagine uma fábrica de verdade: quarenta máquinas, trezentos sensores, oito fornos, doze esteiras. E me responde: como é que **um operador humano** enxerga tudo isso ao mesmo tempo? Como ele fica sabendo, em segundos — não em meia hora — que o forno sete saiu da temperatura? Como ele descobre que a pressão da linha três está subindo devagarzinho há duas horas?"

> "A resposta é o sistema que dá nome a esta aula: o **SCADA**. Se o CLP é o cérebro de cada máquina, o SCADA é o **olho** que vê a fábrica inteira em tempo real — e a **memória** que registra tudo o que aconteceu. Hoje a gente entende como ele funciona por dentro: as telas, os protocolos, os alarmes — inclusive por que alarme mal projetado já causou tragédia. Vamos lá."

### 2. O que é SCADA e onde ele mora na pirâmide (1:30 – 3:30)

**[TELA]** Definição + mini-pirâmide ISA-95 com o nível 2 destacado.

> "SCADA é sigla para *Supervisory Control And Data Acquisition* — supervisão, controle e aquisição de dados. A definição em uma frase: é o sistema que **supervisiona e controla** equipamentos industriais distribuídos, **adquire e armazena** dados em tempo real, e **gera alarmes** quando algo sai do esperado. Três verbos: supervisionar, registrar, alertar."

> "E onde ele mora na arquitetura da fábrica? Lembra da pirâmide ISA-95 que a gente apresentou na Unidade 2? O SCADA ocupa o **nível 2**: acima dos CLPs, que estão no nível 1, e abaixo do MES, que está no nível 3. E aqui vai uma frase-síntese que organiza tudo: **o CLP decide em milissegundos; o SCADA mostra e alarma em segundos; o MES coordena em horas**. Cada camada no seu ritmo, cada uma alimentando a de cima. Na Aula 12 a gente fecha essa pirâmide inteira — hoje o foco é o andar do meio."

### 3. As oito funções de um SCADA típico (3:30 – 6:00)

**[TELA]** Lista das 8 funções, revelando uma a uma.

> "O que um SCADA típico entrega? Oito funções. Vou passar por todas, porque juntas elas formam o retrato completo. **Um**: telas de operação — a chamada **HMI**, interface homem-máquina — desenhos da planta com valores atualizados ao vivo; a gente detalha já já. **Dois**: **coleta de dados** dos CLPs e sensores, através de protocolos industriais — Modbus, OPC, EtherNet/IP — que também vamos destrinchar hoje. **Três**: o **histórico**, o famoso *data historian* — cada leitura de cada sensor armazenada com carimbo de tempo. Parece burocracia, mas anota: esse histórico é a matéria-prima da análise de processo e, lá na Unidade 4, da inteligência artificial. Sem historian, não há manutenção preditiva."

> "**Quatro**: **alarmes** — quando uma variável sai da faixa aceitável, o operador é avisado na hora; é o coração operacional do sistema, e tem uma seção só para ele daqui a pouco. **Cinco**: **gráficos de tendência** — a variável plotada ao longo do tempo. É o que permite perguntar: 'o forno está derivando lentamente há três horas?' — uma deriva lenta que nenhum olhar pontual pegaria. **Seis**: **receitas** — conjuntos de parâmetros salvos por produto. Troca de produto na linha? Em vez de redigitar quarenta valores, carrega a receita. Menos tempo, menos erro humano."

> "**Sete**: **relatórios** — produção do turno, do lote, do dia, exportados para análise. E **oito**: **controle limitado** — o operador pode comandar partidas, paradas e ajustes direto da tela. E repara no adjetivo: controle **limitado**. Quem controla mesmo, em tempo real, milissegundo a milissegundo, é o CLP lá embaixo. O SCADA supervisiona e comanda em alto nível. Cada um no seu nível da pirâmide — essa divisão de trabalho é sagrada na automação."

### 4. HMI: a tela que o operador vê — e a norma ISA-101 (6:00 – 8:30)

**[TELA]** Foto de sala de controle + os 3 princípios da ISA-101.

> "Vamos falar da parte do SCADA que encosta no ser humano: a **HMI**, *Human-Machine Interface*. É a tela — ou o paredão de telas — diante da qual o operador passa oito horas por dia. E aqui mora um dos erros mais caros da automação industrial: projetar uma tela bonita para o **engenheiro que a criou**, e inútil para o **operador que vive nela**."

> "As telas típicas de um sistema bem montado: uma **visão geral** — o mapa da planta com indicadores resumidos; **telas de detalhe** por equipamento, com todos os parâmetros de uma máquina específica; a lista de **alarmes ativos**; as **tendências**; o **histórico de eventos** — o diário de bordo de tudo o que aconteceu; e os **relatórios** de turno e lote."

> "E existe uma norma inteira sobre como desenhar boas HMIs: a **ISA-101**. Ela se resume em três princípios. Princípio um: **foco no operador** — a tela existe para quem opera, não para quem projetou. O operador precisa identificar um problema em **segundos**, não decifrar um painel de avião. Princípio dois: **hierarquia visual** — informação crítica salta aos olhos; ruído visual é eliminado. E princípio três: **padronização** — equipamentos similares têm telas similares. O operador do turno da noite não pode ter que reaprender a interface a cada máquina."

> "E deixa eu te dar a regra de ouro do design moderno de HMI, que soa contraintuitiva: se está tudo normal, a tela deve ser **quase toda cinza**. Isso mesmo, cinza, sóbria, quase sem graça. Por quê? Porque **cor é um recurso escasso** — ela deve gritar apenas quando algo exige atenção. Uma tela que parece árvore de Natal, colorida e piscante o tempo todo, **esconde** o problema em vez de mostrar. Tela boa é tela que fica invisível até o momento em que precisa gritar."

### 5. Protocolos industriais: como o SCADA conversa (8:30 – 11:00)

**[TELA]** Lista de protocolos com seus nichos.

> "Agora, um problema prático que todo integrador enfrenta: a fábrica real é uma **Torre de Babel**. Tem um CLP Siemens comprado em 2010, uma balança com Modbus de 2005, um robô novo que fala OPC UA, um medidor de energia de outra marca. O SCADA precisa conversar com **todos**. E para isso existem os protocolos industriais — as línguas da fábrica. Vamos ao mapa."

> "**Modbus**: o veterano, nascido nos anos setenta. Simples, aberto, roda em qualquer hardware. É o protocolo dos **legados** — e como fábrica não joga equipamento fora, ele continua sendo o padrão de fato em milhões de instalações. **Profibus e Profinet**: o mundo Siemens — o Profinet é a versão sobre Ethernet industrial. **EtherNet/IP**: o mundo Rockwell. **CC-Link**: o mundo Mitsubishi. Percebe o padrão? Cada gigante criou seu dialeto — e durante décadas, integrar marcas diferentes foi um pesadelo caro."

> "Por isso a importância dos dois últimos. **OPC UA**: o padrão **aberto e moderno**, independente de fabricante. E ele não transporta só o número — transporta **semântica**: o que é aquele dado, em que unidade está, de que equipamento veio, em que contexto. É o protocolo que está virando a **língua franca** da indústria: todo equipamento novo já vem falando OPC UA. E o **MQTT**: levíssimo, nascido para telemetria, o favorito das aplicações de IIoT que vimos na disciplina de Indústria 4.0."

> "O resumo honesto do mercado é este: **OPC UA é o presente dos equipamentos novos e o futuro do setor; Modbus é o presente teimoso dos equipamentos antigos**. E o engenheiro de automação vive exatamente aí, traduzindo entre os dois mundos. Quem domina protocolos nunca fica sem trabalho."

### 6. Alarmes: o coração operacional — e o perigo do alarm flood (11:00 – 13:30)

**[TELA]** Os 4 princípios da ISA-18.2; citar Texas City e Bhopal.

> "Chegamos ao tema mais sério da aula. O **alarme** é o grito de socorro do sistema — algo saiu da faixa aceitável e um humano precisa saber. E existe uma norma internacional inteira dedicada só a isso, a **ISA-18.2**. Por que tanta cerimônia para um 'bip'? Porque gestão ruim de alarmes já esteve entre os fatores de **tragédias industriais reais** — o acidente da refinaria de Texas City em 2005, o desastre de Bhopal em 1984. Alarme mal projetado, no limite, mata. Então presta atenção nos quatro princípios."

> "Princípio um: **todo alarme deve exigir uma ação**. Se toca um alarme e a resposta certa é 'não faz nada', aquilo não é alarme — é ruído. E ruído é perigoso, porque **treina o operador a ignorar**. Princípio dois: **prioridade clara** — vermelho para o crítico, amarelo para o alerta, azul para o informativo. E sem inflação de vermelho: se tudo é crítico, nada é crítico."

> "Princípio três: **volume sob controle**. A referência prática: mais de **seis a dez alarmes ativos por turno** e a operação entra na zona de risco do chamado **alarm flood** — a enxurrada de alarmes. Sabe o que o operador faz diante de cinquenta alarmes tocando ao mesmo tempo? Silencia todos. Inclusive o único que importava. É exatamente esse mecanismo que aparece nos relatórios dos grandes acidentes: o alarme certo tocou — afogado no meio de duzentos irrelevantes. Princípio quatro: **reconhecimento e registro** — o operador acusa o recebimento do alarme e registra o que fez. Isso vira histórico, o histórico vira aprendizado, e o aprendizado vira prevenção."

> "Moral da seção: engenharia de alarmes não é detalhe de configuração — é disciplina de segurança. Quando você participar de um projeto SCADA, dedique à filosofia de alarmes o mesmo respeito que dedica ao dimensionamento elétrico."

### 7. Exemplo numérico: a cerâmica dos oito fornos (13:30 – 15:30)

**[TELA]** Números do caso, antes vs depois, lado a lado.

> "Vamos ver o SCADA pagar a própria conta, com números. Cenário: uma fábrica de cerâmica com **oito fornos** em operação contínua, 24 horas por dia."

> "**Situação sem SCADA centralizado**: o operador faz **ronda física** de forno em forno, prancheta na mão, a cada 30 minutos. Consequência matemática: um desvio pode ficar **até 30 minutos** acontecendo sem ninguém saber. E o problema crítico ali é a queda de chama: quando acontece, o lote inteiro que estava queimando perde qualidade — custo médio de **8 mil reais por evento**. Frequência histórica: quatro a seis eventos por mês."

> "**Situação com SCADA e HMI bem configurados**: temperatura de cada forno na tela, em tempo real, com alarme instantâneo ao sair da faixa. Detecção em **menos de um minuto**. A intervenção rápida salva o lote: o custo por evento cai para 2 mil reais. E tem um efeito de segunda ordem ainda mais bonito: com o **histórico** do historian, a equipe mapeia as **causas** das quedas de chama e passa a preveni-las — a frequência cai para um a dois eventos por mês."

> "Agora a conta. Antes: cinco eventos vezes 8 mil reais — **40 mil reais por mês** de perda. Depois: um evento e meio vezes 2 mil — **3 mil por mês**. Economia: **37 mil reais por mês**, ou **444 mil reais por ano**. O investimento típico — software, integração com os CLPs, telas, treinamento — fica entre 300 e 500 mil reais. **Payback em cerca de doze meses**. E repara na elegância: o ganho veio de **duas** alavancas somadas — detectar mais rápido, graças ao alarme, e acontecer menos, graças ao histórico. O alarme e o historian trabalhando em dupla."

### 8. Players de mercado (15:30 – 16:15)

**[TELA]** Nomes dos players.

> "Uma passada rápida pelo mercado, para você reconhecer os nomes. **Rockwell FactoryTalk** e **Siemens WinCC**: os tops de linha de cada gigante, perfeitamente integrados aos seus próprios CLPs. **Wonderware**, hoje da AVEVA: o independente clássico, multiplataforma. **Ignition**, da Inductive Automation: o moderno da turma — baseado em web, licenciamento amigável, em plena ascensão no mundo inteiro. E o orgulho nacional: a **Elipse Software**, gaúcha, líder brasileira com o Elipse E3 e o Elipse Power, fortíssima em saneamento e energia. E a **Indusoft**, também brasileira, que foi adquirida pela AVEVA — sinal de que a gente sabe fazer software industrial por aqui."

### 9. Atividade + encerramento e gancho (16:15 – 17:00)

**[TELA]** Enunciado da atividade.

> "Sua missão até a próxima aula: projete mentalmente — melhor ainda, no papel — um SCADA para uma operação que você conhece. Quatro decisões: quais **cinco variáveis** vão na tela principal? Quais **três alarmes críticos** você configuraria — lembrando: cada um deve exigir uma ação? Que **histórico** mais ajudaria nas análises futuras? E que **integração** com ERP ou MES faria diferença? Guarda essas respostas, porque elas conectam direto com a próxima aula."

> "E a próxima aula fecha a unidade com chave de ouro: a gente vai juntar **tudo** — sensor, CLP, SCADA, MES, ERP — numa única imagem, a **pirâmide ISA-95**, e encarar o desafio que define a competitividade industrial deste século: a convergência entre **TI e OT**. Te espero lá. Um abraço!"

---

## Roteiro da Videoaula 12 — "Pirâmide ISA-95: fechando o ciclo TI ↔ OT"

**Duração-alvo:** 15 a 17 minutos.

### 1. Abertura (0:00 – 1:30)

**[TELA]** Slide de capa da aula 12.

> "Olá! Bem-vindo, bem-vinda à última aula da Unidade 3 — e esta é uma aula especial, porque é uma aula de **síntese**. Pensa em tudo o que você já viu: na Aula 9, sensores e atuadores. Na Aula 10, o CLP. Na Aula 11, o SCADA. E lá atrás, na Unidade 2, o MES e o ERP. Até agora, foram peças soltas — cada uma apresentada de perto, no detalhe. Hoje a gente afasta a câmera e monta o quebra-cabeça inteiro numa única imagem: a **pirâmide ISA-95**."

> "E depois de montar a pirâmide, a gente vai encarar a pergunta de um milhão de dólares — literalmente, porque é disso que se trata: como fazer o mundo da **TI**, a tecnologia da informação, conversar com o mundo da **OT**, a tecnologia operacional? Eu te adianto o spoiler: quem responde bem a essa pergunta define quem é competitivo na indústria do século 21. Vamos fechar a unidade."

### 2. A pirâmide ISA-95 completa (1:30 – 4:30)

**[TELA]** Pirâmide de 5 níveis, revelando de baixo para cima, nível a nível.

> "A norma internacional **ISA-95** — também publicada como **IEC 62264** — organiza toda a tecnologia de uma planta industrial em **cinco níveis** hierárquicos. Vou construir a pirâmide de baixo para cima, porque é assim que o dado nasce e sobe."

> "**Nível zero**: o equipamento físico. Sensores, atuadores, motores, válvulas — o mundo material, operando em tempo real, em milissegundos. É a nossa Aula 9. **Nível um**: o controle — CLP, DCS, PID. Decisões de milissegundos a segundos: manter a temperatura, ligar o motor, fechar a válvula. É a nossa Aula 10. **Nível dois**: a supervisão — SCADA e HMI. Decisões de segundos a minutos: alarmar, registrar, mostrar ao operador. Aula 11, semana passada."

> "**Nível três**: a execução da manufatura — o MES, que vimos na Unidade 2. Decisões de horas a turnos: que ordem de produção roda agora, em que máquina, com que prioridade. E **nível quatro**: o negócio — o ERP. Decisões de dias a meses: quanto comprar, quanto produzir, onde investir. Também da Unidade 2."

> "E qual é a chave de leitura da pirâmide? O **tempo**. Repara na tabela: quanto mais **baixo** o nível, mais **rápida** a decisão e mais **físico** o sistema — o sensor decide em milissegundos se a temperatura passou do limite. Quanto mais **alto**, mais **lenta** a decisão e mais **estratégico** o sistema — o ERP decide em meses se vale a pena construir outra fábrica. E o fluxo é uma via de mão dupla: cada nível **fornece dados** para o nível de cima e **recebe comandos** do nível de cima. O dado nasce no sensor e sobe; a decisão nasce na diretoria e desce."

> "E deixa eu te mostrar uma coisa bonita: sem você perceber, nós passamos as últimas semanas **subindo essa pirâmide degrau por degrau** — sensor, CLP, SCADA, e antes disso MES e ERP. O curso inteiro estava desenhado sobre essa imagem. Agora ela é sua."

### 3. TI versus OT: dois mundos, duas filosofias (4:30 – 7:30)

**[TELA]** Tabela comparativa TI × OT, linha a linha.

> "Agora pega a pirâmide e corta ao meio. Do **nível 3 para cima** — MES, ERP, BI, CRM, e-mail, intranet — é o mundo da **TI**, a Tecnologia da Informação: foco em dados e processos de negócio. Do **nível 2 para baixo** — SCADA, CLPs, sensores, atuadores — é o mundo da **OT**, a Tecnologia Operacional: foco em processos físicos e operação em tempo real. E esses dois mundos, historicamente, são **duas tribos diferentes**: equipes diferentes, fornecedores diferentes, congressos diferentes, e — principalmente — prioridades diferentes. Deixa eu dramatizar o contraste, porque ele explica décadas de conflito corporativo."

> "**Prioridade número um**: para a TI, é a **confidencialidade** do dado — o pesadelo da TI é vazamento. Para a OT, é a **disponibilidade** do processo — o pesadelo da OT é a planta parada. Para a TI, vazar dado é a tragédia; para a OT, **parar** é a tragédia. **Atualização de sistema**: a TI atualiza hoje à noite, sem dó — patch de segurança não espera. A OT responde: 'de jeito nenhum' — parada não programada custa fortunas, e mexer no que funciona é risco. **Vida útil**: a TI troca tudo a cada três a cinco anos. Na OT, um CLP roda **quinze, vinte, trinta anos**. Existe CLP em operação no Brasil hoje que é mais velho que muitos de vocês — e funcionando perfeitamente."

> "**Sistema operacional**: na TI, atualizado. Na OT, é comum encontrar um Windows antigo rodando o supervisório — porque funciona, porque o software não roda em outro, e porque ninguém quer ser o responsável pela parada. **Quem opera**: TI corporativa de um lado; operadores e engenheiros de manutenção do outro."

> "E aqui está o ponto que eu quero que você leve: **nenhum dos dois está errado**. São filosofias moldadas por riscos diferentes, ambas racionais no seu contexto. O problema — e a oportunidade da sua geração — é que essas duas tribos agora **precisam** trabalhar juntas."

### 4. Por que TI e OT precisam conversar agora (7:30 – 9:30)

**[TELA]** Os 4 motivos da convergência.

> "Por que 'agora'? Porque até uns 2010, TI e OT podiam viver separadas sem grande prejuízo — o ERP recebia números digitados no fim do mês e a fábrica rodava. Hoje, não dá mais. Quatro motivos."

> "Motivo um: as **decisões de negócio** passaram a depender de dados do chão de fábrica **em tempo real**. O diretor que espera a planilha consolidada de sexta-feira perde para o concorrente que enxerga a produção agora. Motivo dois: a **otimização da operação** roda em algoritmos hospedados em servidores de TI — o dado da OT precisa chegar lá. Motivo três, o exemplo mais claro de todos: a **manutenção preditiva** — que vamos destrinchar na Unidade 4 — combina sensores de vibração, que são OT, com modelos de inteligência artificial, que são TI. Um sem o outro simplesmente não existe. E motivo quatro: a **visão única do cliente** — cruzar a reclamação que entrou no CRM com o lote, a máquina e o turno que produziram aquela peça. Isso exige TI e OT de mãos dadas."

> "Anota esta frase: **a convergência TI-OT é o tema central da tecnologia industrial desta década**. E anota a consequência para a sua carreira: o profissional que entende **dos dois mundos** — que fala de ERP de manhã e de CLP à tarde, sem gaguejar — é exatamente o que esta disciplina está formando. E esse profissional vale ouro no mercado."

### 5. Como integrar na prática: as três abordagens (9:30 – 11:30)

**[TELA]** As 3 abordagens lado a lado.

> "Muito bem, estamos convencidos de que precisa integrar. **Como?** Existem três abordagens principais, e você precisa saber recomendar a certa para cada situação."

> "Abordagem um: o **gateway de dados**. Um servidor intermediário que lê dos CLPs e do SCADA de um lado, e entrega para os sistemas de TI via APIs do outro. É o tradutor posicionado na fronteira. Vantagens: pragmático, relativamente barato, não mexe em nada do que já existe. É o **primeiro passo clássico** de quem está começando a jornada."

> "Abordagem dois: **OPC UA puro**. Se o parque de equipamentos é novo, ele já fala OPC UA nativamente — e aí os sistemas de TI podem consumir os dados **direto**, sem intermediário, com semântica rica. É elegante e limpo… mas depende de um luxo que poucas fábricas têm: equipamento novo em tudo quanto é canto."

> "Abordagem três: a **plataforma IIoT** — Siemens Mindsphere, AWS IoT, PTC ThingWorx. Uma camada de software especializada que coleta os dados da OT, e cuida de **tudo**: segurança, normalização, histórico, escalabilidade, e exposição organizada para a TI. É a abordagem mais completa e mais estratégica — e também a mais cara, exigindo maturidade digital da empresa para valer a pena."

> "Regra prática de consultor, guarda aí: fábrica **começando** a jornada → gateway. Parque **renovado** → OPC UA direto. Operação **grande, multi-planta, com estratégia de dados** → plataforma IIoT. Não existe resposta única; existe resposta adequada ao momento de cada empresa. Desconfie de quem oferece a mesma solução para todo mundo."

### 6. Cibersegurança: o pedágio obrigatório da convergência (11:30 – 13:30)

**[TELA]** IEC 62443 + modelo Purdue em zonas.

> "Agora o alerta mais sério da aula. No exato momento em que você conecta a OT à TI, a OT **herda todos os riscos** que antes eram só da TI: ransomware, acesso indevido, vazamento de dados. E pensa comigo na diferença de gravidade: um ransomware que criptografa o servidor de e-mail é um problemão — dias de dor de cabeça, talvez resgate. Mas um ransomware que **para uma planta química**, ou uma linha de envase de alimentos, ou uma subestação de energia? Isso é outra categoria de problema. Isso é risco físico, ambiental, humano."

> "Por isso existe a norma **IEC 62443**, que já apareceu na disciplina de Indústria 4.0 — ela define como proteger sistemas de automação industrial. E o **modelo Purdue**, que se alinha à pirâmide ISA-95, organiza a defesa em **zonas**: cada nível da pirâmide é separado do nível adjacente por firewalls e regras de fronteira. O dado atravessa fronteiras **controladas e inspecionadas** — nunca, jamais, um cabo direto ligando o ERP no CLP. Se um invasor compromete o nível 4, ele encontra um muro antes do nível 3; se compromete o 3, outro muro antes do 2. Defesa em profundidade."

> "E grava esta frase, porque ela serve para a prova e para a carreira: **cibersegurança industrial hoje é pré-requisito, não diferencial**. Projeto de integração TI-OT que não tem capítulo de segurança não é projeto — é um incidente com data marcada."

### 7. Exemplo numérico do ROI + caso Ambev (13:30 – 15:45)

**[TELA]** Números do gateway, antes vs depois; depois, o pipeline da Ambev.

> "Vamos fechar com números e com um caso real. Primeiro, a conta de uma integração básica — chão de fábrica dentro do ERP — numa fábrica que tem CLPs nos equipamentos mas **nenhuma** integração."

> "**Cenário antes**: o operador anota a produção **em papel**; no fim do turno, o supervisor digita tudo no ERP. Faz a conta comigo: duas horas de digitação por turno, três turnos por dia, cinco dias por semana, quatro semanas — **120 horas por mês** de trabalho puramente burocrático. E digitação manual erra: uns **5%** dos lançamentos. E erro de apontamento custa caro — decisão tomada sobre número errado, problema fiscal, estoque fantasma: estimados **30 mil reais por mês**."

> "**Cenário depois**, com um gateway de integração: o dado sai do CLP e entra **sozinho** no ERP. Digitação despenca para 5 horas por mês — só as exceções. O erro cai para menos de meio por cento; o custo de erro, para 3 mil reais mensais. **Somando os ganhos**: 115 horas liberadas vezes 50 reais a hora, são 5.750 reais; mais 27 mil de erros evitados — **32.750 reais por mês**, quase **400 mil reais por ano**. O investimento — gateway, integração, projeto — fica em torno de **250 mil reais**. **Payback: cerca de oito meses**. Para um projeto de infraestrutura, é um retorno excelente."

> "E isso é só o degrau básico. Quer ver o degrau máximo dessa escada? Olha a **Ambev**. Em cada cervejaria do grupo no Brasil: CLPs em todos os equipamentos — nível 1. SCADA supervisionando em tempo real — nível 2. MES coordenando as ordens de produção — nível 3. Tudo conectado ao ERP corporativo — nível 4. E ainda um andar acima da pirâmide: os dados de todas as plantas sobem para um **data lake** central, onde modelos de **inteligência artificial** rodam previsão de demanda e otimização de processo. Resultado: decisão corporativa baseada em dado **real** do chão de fábrica, em tempo quase real. É a pirâmide ISA-95 inteira, viva, respirando e integrada — e é referência mundial no setor de bebidas. É para isso que a gente estuda."

### 8. Atividade prática (15:45 – 16:30)

**[TELA]** As 4 perguntas da atividade.

> "Sua missão de fechamento da unidade — e presta atenção, porque ela conversa direto com a atividade avaliativa da disciplina. Pega aquela empresa que você vem analisando desde a Unidade 1 e responde com honestidade: **um** — em qual nível da pirâmide ISA-95 ela tem mais maturidade hoje? **Dois** — onde está a maior lacuna? O clássico é ter ERP no topo e o chão de fábrica desconectado lá embaixo, com um abismo no meio. **Três** — qual **uma única** integração TI-OT traria o maior impacto no menor prazo? E **quatro** — quais riscos de cibersegurança essa integração cria, e como o modelo Purdue os mitigaria? Quatro respostas honestas valem mais do que vinte slides bonitos. Escreve."

### 9. Encerramento da unidade + gancho para a U4 (16:30 – 17:00)

**[TELA]** Slide de fechamento com a pirâmide completa + teaser da U4.

> "E com isso fechamos a Unidade 3. Recapitula o caminho comigo: o trio **sensor-controlador-atuador** girando em malha fechada; o **CLP** com seu ciclo de varredura e sua lógica ladder; o **SCADA** com seus olhos, seu historian e seus alarmes; e hoje, a **pirâmide completa** com a convergência TI-OT. Você agora enxerga a fábrica **inteira** — do parafuso ao ERP. Pouca gente no mercado tem essa visão de ponta a ponta. Você tem."

> "E na Unidade 4 vem a coroação da disciplina: **Inteligência Artificial aplicada à produção**. Previsão de demanda, manutenção preditiva, visão computacional para qualidade, IA generativa na engenharia. E repara na costura: tudo o que construímos até aqui — o dado que nasce no sensor, sobe pelo CLP, passa pelo SCADA e chega aos sistemas corporativos — é exatamente o **combustível** que a IA precisa para funcionar. Sem a pirâmide, não há IA industrial. Você está pronto. Te espero na última unidade. Um abraço!"
