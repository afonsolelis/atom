# Roteiros das videoaulas 1 a 4 — Unidade 1 (20 minutos)

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 1: Fundamentos de sistemas ciberfísicos e modelagem da planta
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: aproximadamente 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, comandos, saídas de terminal e indicações de edição.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas, respiração e o tempo de leitura da saída de cada comando.

Plano de tempo de referência, adaptável ao ritmo de cada aula:

- 00:00–02:00 — abertura com a ferramenta já aberta (terminal ou editor; nenhuma aula começa por definição conceitual);
- 02:00–05:00 — situação-problema, ancorada em código já em execução;
- 05:00–13:00 — desenvolvimento conceitual, sempre explicando o que está sendo executado na tela;
- 13:00–17:00 — demonstração prática guiada, com os números reais medidos nos laboratórios;
- 17:00–19:00 — aplicação profissional;
- 19:00–20:00 — pontos-chave, desafio prático e transição.

Esta é uma disciplina de captura de tela, gravada com OBS Studio (tela e câmera), sem estúdio. Diferente de uma disciplina expositiva com deck de slides, aqui cada roteiro alterna somente entre blocos `TELA: terminal` — com o diretório `projeto_nexabot/` aberto e o ambiente virtual `.venv` já criado — e blocos `TELA: editor`, com o arquivo indicado aberto em fonte ampliada. Todo bloco de terminal traz o comando literal, em cerca de código, seguido da narração que descreve a saída real observada quando o comando roda; o professor não improvisa o que digita. Todos os comandos e números citados nestes quatro roteiros foram executados e conferidos em `projeto_nexabot/aula_01/` a `aula_04/`, com o interpretador `.venv/bin/python`, antes da escrita deste arquivo.

---

## Roteiro da Videoaula 1 — "O NexaBot que esquece a própria velocidade"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 1 — Sistemas ciberfísicos e o ciclo do design baseado em modelos. Esta é a primeira videoaula de toda a disciplina.

**Objetivo da videoaula:** ao final, o estudante deve conseguir caracterizar um sistema ciberfísico pelo acoplamento entre dinâmica contínua e lógica discreta, situar o design baseado em modelos no V-Model, ter o próprio ambiente de laboratório instalado e verificado, e explicar — com um número medido, não intuído — por que um comando de tensão fixo em malha aberta não sustenta a velocidade do NexaBot quando a carga muda.

**Mapa de tempo e telas:** 00:00 terminal (abertura da disciplina) · 01:15 editor: `params.py` · 02:15 terminal: instalação do ambiente com `uv` · 04:30 terminal: relatório de prontidão · 06:00 editor: `plant.py` (o que é um CPS) · 08:00 terminal: V-Model das 16 aulas · 10:00 terminal: primeira simulação · 12:00 terminal: malha aberta sob carga · 15:00 cálculo manual complementar · 16:30 aplicação profissional · 18:00 terminal: desafio da aula · 18:45 fechamento e transição.

### Abertura contextualizada

**[00:00–01:15 · TELA: terminal — terminal aberto em `~/projeto_nexabot`, prompt visível, nenhum comando ainda executado]**

Esta é a primeira aula da disciplina Design Baseado em Modelos para Sistemas Ciberfísicos. Eu sou o professor Afonso Brandão. As dezesseis videoaulas desta disciplina giram em torno de um único sistema físico: o NexaBot, um veículo autoguiado industrial de armazém, com tração por motor de corrente contínua de ímã permanente, redutor de relação vinte para um e roda de cinquenta milímetros de raio. Você vai encontrá-lo hoje como um motor sem nenhum controlador, e vai entregá-lo, na Aula 16, como um sistema modelado, controlado, verificado formalmente e com código embarcado gerado a partir do próprio modelo, com rastreabilidade de ponta a ponta, do requisito ao binário. A régua sobe unidade a unidade: esta primeira unidade constrói o modelo matemático da planta; a segunda fecha a malha de controle e leva o projeto ao domínio discreto; a terceira prova formalmente que o comportamento do sistema está correto; a quarta transforma tudo isso em código embarcado, com evidência. Este terminal, aberto na pasta `projeto_nexabot`, é o único ambiente que esta disciplina usa, e eu monto esse ambiente agora, ao vivo, diante de você.

**[01:15–02:15 · TELA: editor — `nexabot/params.py`]**

Abro o arquivo `params.py`, dentro do pacote `nexabot`. Este arquivo é a fonte única de verdade numérica de toda a disciplina: nenhum número usado nas dezesseis aulas existe fora dele. Ali estão os parâmetros elétricos do motor — resistência de armadura de um vírgula dois ohms, indutância de três vírgula cinco milihenries, constante de torque e de força contraeletromotriz, ambas de zero vírgula zero quarenta e cinco — e os parâmetros mecânicos: inércia refletida de dois vírgula cinco vezes dez elevado a menos quatro quilograma metro ao quadrado, atrito viscoso de oito vezes dez elevado a menos cinco. A classe também guarda os limites físicos do driver, vinte e quatro volts e doze ampères, e o período de amostragem do controlador embarcado, cinco milissegundos, cento e noventa e nove hertz arredondados para duzentos. Cada um desses números foi identificado a partir de um ensaio real na Aula 2. Nada aqui foi inventado, e é por isso que este arquivo é `frozen`: alterá-lo em tempo de execução quebraria a rastreabilidade entre modelo, código e teste.

**[02:15–04:30 · TELA: terminal — instalação do ambiente com `uv`]**

```bash
uv --version
cd projeto_nexabot
uv venv .venv
uv pip install --python .venv/bin/python \
    numpy scipy matplotlib sympy control \
    jinja2 hypothesis pytest coverage fmpy pyserial
```

A ferramenta que instala e gerencia o ambiente Python desta disciplina chama-se `uv`, na versão zero vírgula doze vírgula sete. Ela substitui, sozinha, o `pip`, o `venv` e o `virtualenv`, e é hoje o padrão de fato do ecossistema Python. O primeiro comando cria o ambiente virtual `.venv` em menos de dez milissegundos. O segundo instala, de uma só vez, as onze bibliotecas diretas desta disciplina: NumPy e SciPy para álgebra numérica, `python-control` para espaço de estados e função de transferência, SymPy para derivação simbólica, Matplotlib para as figuras, Jinja2 para geração de código C, Hypothesis e pytest para testes, coverage para cobertura, FMPy para co-simulação FMI e pySerial para a ponte com o hardware. O `uv` resolve toda essa árvore de dependências e instala em poucos segundos — a saída lista cada pacote, com a versão exata fixada. Não existe, nesta disciplina, nenhuma dependência de licença comercial: o estudante reproduz este mesmo ambiente na própria máquina, de graça, no dia seguinte à formatura.

### Desenvolvimento conceitual

**[04:30–06:00 · TELA: terminal — relatório de prontidão do ambiente]**

```bash
.venv/bin/python aula_01/01_ambiente.py
```

Este script confere, item a item, se o ambiente está pronto para gravar. A primeira tabela verifica as onze bibliotecas Python, cada uma com sua versão: NumPy dois vírgula cinco vírgula dois, SciPy um vírgula dezoito vírgula um, `control` zero vírgula dez vírgula dois, SymPy um vírgula quatorze, Matplotlib três vírgula onze — todas em verde. A segunda tabela confere ferramentas externas: o compilador GCC, necessário a partir da Unidade 4 para gerar código embarcado. A terceira tabela é a mais importante desta aula: ela relê o arquivo `params.py` que acabamos de abrir e confere, um a um, que os onze parâmetros do NexaBot batem com o que está documentado — inclusive o ganho estático de vinte e um vírgula dois mil cento e sessenta e quatro radianos por segundo por volt, que vamos reencontrar daqui a poucos minutos. A linha final diz, em verde: ambiente pronto, pode iniciar a Aula 1. Esta é uma regra desta disciplina, não um detalhe: nenhuma aula é gravada com esse relatório apontando qualquer pendência.

**[06:00–08:00 · TELA: editor — `nexabot/plant.py`]**

Com o ambiente pronto, abro `plant.py`, o modelo da planta do NexaBot. Este arquivo é a resposta prática à primeira pergunta conceitual da disciplina: o que é, afinal, um sistema ciberfísico? Um sistema ciberfísico integra, em um único projeto, computação discreta — software que decide, em passos — e dinâmica física contínua, grandezas como corrente e velocidade angular que evoluem segundo equações diferenciais. Vejam a função `derivative`: ela calcula a derivada da corrente e da velocidade a partir da tensão aplicada, obedecendo às leis de Kirchhoff e de Newton para rotação. Essa função representa a metade puramente física do NexaBot. Ela não sabe nada sobre software, sobre amostragem, sobre decisão. Mas nenhum motor real fica sozinho: um firmware lê o encoder a cada cinco milissegundos e decide uma nova tensão de comando. É esse acoplamento — dinâmica contínua entre duas leituras, evento discreto na leitura — que caracteriza um sistema híbrido, e é exatamente esse acoplamento que separa um sistema ciberfísico de um software comum: aqui, um erro de poucos milissegundos no cálculo do controlador não gera um dado incorreto na tela, gera um robô que perde sustentação de velocidade sobre um piso de fábrica, com carga em cima.

### Demonstração ao vivo

**[08:00–10:00 · TELA: terminal — o V-Model das dezesseis aulas]**

```bash
.venv/bin/python aula_01/04_v_model.py
```

Este script desenha, em caracteres ASCII, o V-Model que organiza toda a disciplina — vou usá-lo como mapa para o restante do curso. O ramo esquerdo desce: requisitos do sistema, nas Aulas 1 e 2; arquitetura e modelo de planta, nas Aulas 2 e 3; projeto de controle, nas Aulas 4, 5 e 6; discretização e implementação embarcada, na Aula 7 e nas Aulas 13 e 14. No fundo do V está o código embarcado do NexaBot, gerado na Aula 13. O ramo direito sobe, verificando cada nível do ramo esquerdo no mesmo grau de abstração: teste unitário do controlador discreto na Aula 15; co-simulação de planta e controlador nas Aulas 11 e 12; verificação formal de segurança na Aula 10; teste baseado em modelo do supervisor na Aula 9; e, no topo, validação em hardware na Aula 16. A tabela que aparece embaixo lista as dez etapas, cada uma com a aula correspondente. O ponto central do design baseado em modelos está exatamente aqui: cada nível do ramo esquerdo já nasce como um modelo executável, verificável antes de existir qualquer hardware — o requisito de que o modelo da planta reproduza o ensaio de degrau com erro inferior a cinco por cento, por exemplo, é uma condição que testamos já na Aula 2, anos antes de qualquer placa eletrônica estar em produção.

**[10:00–12:00 · TELA: terminal — primeira simulação do NexaBot]**

```bash
.venv/bin/python aula_01/02_primeira_simulacao.py
```

Chegou o momento de ver o NexaBot em movimento pela primeira vez. O script aplica um degrau de doze volts ao motor, em malha aberta, partindo do repouso, e integra a planta por Runge-Kutta de quarta ordem — o mesmo integrador que, na Unidade 4, vai viver dentro de um FMU em C. Os dois gráficos ASCII mostram a velocidade angular subindo até se estabilizar perto de duzentos e cinquenta e cinco radianos por segundo, e a corrente de armadura subindo muito mais rápido, quase verticalmente, até um pico bem antes da velocidade sequer sair do lugar de forma perceptível — já um primeiro sinal da separação de escalas de tempo que a Aula 3 vai explicar. A tabela final resume os números: velocidade de regime de duzentos e cinquenta e quatro vírgula sessenta radianos por segundo, o equivalente a zero vírgula seis mil trezentos e sessenta e cinco metros por segundo; corrente de pico de nove vírgula quatro ampères; constante de tempo elétrica de dois vírgula noventa e dois milissegundos; constante de tempo mecânica de cento e quarenta e oito milissegundos. O ponto pedagógico que o próprio script imprime é o que sustenta esta aula inteira: em malha aberta, a velocidade de regime é imposta pelo ganho estático do motor, não escolhida livremente por quem projeta.

**[12:00–15:00 · TELA: terminal — a malha aberta falha sob carga variável]**

```bash
.venv/bin/python aula_01/03_malha_aberta_falha.py
```

Este é o script que motiva a disciplina inteira. O objetivo agora é manter um metro por segundo de velocidade linear, o que corresponde a quatrocentos radianos por segundo no eixo do motor. Sem carga nenhuma, a tensão calculada para sustentar esse alvo é de dezoito vírgula oitocentos e cinquenta e três volts — repare como esse valor já consome boa parte da folga de tensão do driver, que tem só vinte e quatro volts no total. O cenário simulado é o de um operador empilhando peso sobre o NexaBot ao longo do trajeto: o torque de carga refletido ao eixo cresce em rampa, de zero até cerca de trinta por cento do torque nominal, em dois segundos, enquanto a tensão de comando permanece fixa nos dezoito vírgula oitocentos e cinquenta e três volts calculados sem carga. O primeiro gráfico mostra a velocidade linear caindo continuamente, sem nunca voltar à referência de um metro por segundo. O segundo gráfico mostra o erro percentual subindo, e a tabela final entrega os números exatos: aos cinco décimos de segundo, o erro já é de quatro vírgula oitenta e oito por cento; a um segundo, onze vírgula cinquenta e um por cento; a um segundo e meio, dezoito vírgula vinte por cento; e, ao final dos dois segundos, vinte e quatro vírgula oitenta e oito por cento — praticamente um quarto da velocidade desejada, perdido, e nenhuma correção acontece, porque o controlador não está medindo a saída. É esse número, quase vinte e cinco por cento de erro, que qualquer requisito razoável de precisão de velocidade do NexaBot reprova.

### Aplicação profissional

**[15:00–16:30 · TELA: terminal — saída do script anterior ainda visível; cálculo manual complementar]**

Vale fazer, à mão, um segundo cenário mais simples que o da rampa: uma carga constante e moderada, de zero vírgula zero cinco newton-metro, em vez de uma rampa crescente. Partindo da mesma equação de regime permanente do motor, com a tensão fixa nos dezoito vírgula oitenta e cinco volts, a velocidade cai para aproximadamente trezentos e setenta e um vírgula sessenta e cinco radianos por segundo, ou zero vírgula novecentos e vinte e nove metros por segundo — um erro relativo de cerca de sete vírgula um por cento, permanente, porque nada no comando fixo o corrige. Este é o mesmo fenômeno do script anterior, só que sob uma carga menor e constante em vez de crescente: a malha aberta erra sempre que a condição física muda, seja a mudança abrupta ou gradual. E note-se, novamente, o quanto de margem já se perde: com o ganho estático de vinte e um vírgula dois mil cento e sessenta e quatro radianos por segundo por volt, os vinte e quatro volts máximos do driver produziriam, em regime e sem carga nenhuma, uma velocidade linear máxima de apenas um vírgula duzentos e setenta e três metros por segundo — pouquíssima folga para qualquer ação transitória de um controlador, tema que a Aula 4 retoma com números ainda mais desconfortáveis.

**[16:30–18:00 · TELA: terminal — aplicação profissional]**

Esse tipo de falha não é uma curiosidade de laboratório. Em veículos autônomos industriais, comandos de tensão fixos ou mal compensados sob variação de carga produzem exatamente esse efeito: colisões leves por atraso de reação, ou frenagens bruscas quando um sistema de segurança percebe o descasamento tarde demais. Na indústria automotiva, o mesmo argumento aparece em controle de tração e em suspensão ativa, onde a carga do veículo muda a cada passageiro ou cada carga transportada. Na aeroespacial, o argumento é ainda mais severo: uma aeronave que perde sustentação de altitude por um modelo aerodinâmico incompleto não tem para onde recuar — o relatório da Federal Aviation Administration sobre o acidente do Boeing 737 MAX, que está no material complementar desta unidade, documenta justamente um modelo de comportamento aerodinâmico incompleto combinado com uma lógica de controle que confiava demais em um único sensor. O argumento econômico do V-Model, que vimos há poucos minutos, é este: um defeito de modelagem descoberto em simulação custa uma fração do que custaria descoberto em campo, com hardware já fabricado e, em casos como esse, vidas em risco.

### Fechamento

**[18:00–18:45 · TELA: terminal — o desafio da aula]**

```bash
.venv/bin/python aula_01/05_desafio.py
```

Esta é a estrutura de desafio que se repete ao final de cada uma das dezesseis aulas: um esqueleto de função com um enunciado claro e um critério de aceitação numérico, que roda sem erro mesmo antes de ser implementado, avisando exatamente o que falta. O desafio de hoje pede um orçamento de energia de uma missão do NexaBot: simular a planta em malha aberta com dezoito volts, calcular a velocidade de regime, o tempo para percorrer cinquenta metros e a energia elétrica consumida nessa distância. A tela mostra o aviso amarelo de que a função ainda não está implementada, seguido da tabela com as faixas esperadas de resposta — entre zero vírgula noventa e um metro por segundo de velocidade de regime, entre cinquenta e cinquenta e seis segundos de percurso, e entre quinhentos e cinquenta e setecentos e cinquenta joules de energia. Essa é a sua tarefa depois desta aula.

**[18:45–20:00 · TELA: terminal — pontos-chave e transição]**

Recapitulando os pontos-chave desta primeira aula. Um sistema ciberfísico acopla dinâmica física contínua e lógica discreta, e um erro nesse acoplamento tem consequência física, não apenas digital. O V-Model organiza requisitos e projeto no ramo descendente, e verificação, no ramo ascendente, no mesmo nível de abstração — e o design baseado em modelos adianta essa verificação para antes de existir qualquer hardware. O NexaBot em malha aberta atinge duzentos e cinquenta e quatro vírgula sessenta radianos por segundo com um degrau de doze volts, mas, sob carga variável, o erro de velocidade cresce sem controle até quase vinte e cinco por cento em dois segundos — e nada corrige isso, porque não há realimentação. Sua atividade prática é mapear as dezesseis videoaulas desta disciplina sobre o V-Model que vimos há pouco, registrando em que ramo cada uma atua. Na próxima aula, saio do comportamento observado do motor e vou à origem dele: as duas equações diferenciais do circuito de armadura e do eixo mecânico, reescritas em espaço de estados com SymPy, e a identificação dos seis parâmetros físicos a partir de um ensaio de degrau — o "de onde vêm os números de `params.py`" que abrimos no começo desta aula.

### Indicações de edição e recursos visuais

- Bloco de abertura (00:00–01:15): manter o terminal limpo, prompt curto, fonte ampliada; sem overlay de slide.
- `params.py` (01:15–02:15): destacar em zoom progressivo cada campo da dataclass conforme a narração cita o valor.
- Instalação do ambiente (02:15–04:30): acelerar levemente o trecho de resolução de dependências do `uv` se a captura real ficar mais lenta que o narrado, mantendo o áudio íntegro.
- Recurso visual 1 — diagrama do V-Model com as dezesseis aulas mapeadas: já é gerado em ASCII pelo próprio script `04_v_model.py`; a equipe de edição pode sobrepor uma versão gráfica equivalente em pós-produção, preservando os mesmos dez degraus e a mesma legenda de aulas.
  *Texto alternativo:* Diagrama em V mostra o ramo de definição descendo por requisitos, arquitetura, controle e implementação embarcada, e o ramo de verificação subindo por SIL, co-simulação, verificação formal e HIL, com as dezesseis aulas da disciplina distribuídas nos dez degraus.
- Recurso visual 2 — gráfico de velocidade e corrente da primeira simulação (10:00): o PNG real já é salvo em `figuras/aula01_primeira_simulacao.png`; usar como inserção em tela cheia por três segundos ao citar os números de regime.
- Recurso visual 3 — gráfico de erro percentual crescente sob carga (12:00–15:00): PNG real em `figuras/aula01_malha_aberta_falha.png`; sincronizar o realce da curva com a leitura da tabela de erro.
- Ao citar $18{,}85\,\mathrm{V}$ e o erro de $7{,}1\%$ (15:00), exibir a fórmula $V = \omega\left(\dfrac{Rb}{K_t}+K_e\right)+\dfrac{R\,\tau_{\text{carga}}}{K_t}$ como legenda inferior, sem cobrir o terminal.
- Encerramento (18:45–20:00): vinheta curta de transição, sem cortar a última frase.

### Fontes e links de mídia

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011 — referência conceitual, sem reprodução de trecho externo.
- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017 — referência conceitual, sem reprodução de trecho externo.
- ESTADOS UNIDOS. Federal Aviation Administration. *Boeing 737 MAX Flight Control System*: Joint Authorities Technical Review. Washington, D.C., 2019 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; gráficos e diagramas devem ser produzidos a partir dos PNGs reais gerados em `projeto_nexabot/figuras/` e do texto-base da Aula 1 (`unidade_1.md`).

---

## Roteiro da Videoaula 2 — "Um motor sem manual: encontrando os parâmetros que ninguém entregou"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 2 — Da equação diferencial ao espaço de estados, com identificação por dados.

**Objetivo da videoaula:** ao final, o estudante deve conseguir derivar a forma em espaço de estados de um sistema físico a partir de leis de conservação, explicar por que o estado é a memória mínima do sistema, identificar parâmetros físicos por mínimos quadrados não lineares a partir de um ensaio de degrau, validar o modelo identificado em dados retidos e reconhecer por que a taxa de amostragem do ensaio precisa exceder em muito a do controlador embarcado.

**Mapa de tempo e telas:** 00:00 editor: `01_sympy_derivacao.py` (situação-problema) · 01:30 terminal: derivação simbólica · 04:00 desenvolvimento conceitual sobre estado · 06:00 terminal: espaço de estados vs. função de transferência · 08:00 conceito de identificação por mínimos quadrados · 09:30 terminal: ensaio e ajuste · 13:00 terminal: validação e o efeito da subamostragem · 16:00 aplicação profissional · 17:30 atividade prática · 18:30 fechamento e transição.

### Abertura contextualizada

**[00:00–01:30 · TELA: editor — `aula_02/01_sympy_derivacao.py`, com o cursor sobre as duas equações diferenciais do motor]**

Na aula anterior, vimos o NexaBot perder velocidade sob carga em malha aberta. Hoje resolvo a pergunta que fica: de onde vêm os números que descrevem esse motor? Na prática, uma equipe raramente recebe o motor de tração com um datasheet completo — o fornecedor protege parâmetros internos, ou o motor já sofreu desgaste em uso, ou simplesmente o equipamento chegou ao chão de fábrica sem a folha de especificações que o projeto original previa. A resposta da engenharia de controle para essa lacuna é a identificação de sistemas: aplicar um sinal conhecido, medir a resposta e ajustar os parâmetros de um modelo físico até reproduzi-la, sem nunca abrir a carcaça do motor. Este arquivo aberto no editor, `01_sympy_derivacao.py`, é o ponto de partida: ele usa a biblioteca SymPy para derivar simbolicamente as equações do motor, sem nenhum atalho numérico e sem nenhuma chance de erro de álgebra manual — o tipo de erro que, cometido à mão numa planilha, custa horas de depuração mais tarde. As duas equações que aparecem na tela — a malha elétrica de armadura e a malha mecânica do eixo — são exatamente as leis de Kirchhoff e de Newton para rotação aplicadas ao NexaBot, as mesmas duas leis físicas que qualquer curso de circuitos e de mecânica já apresentou, só que agora escritas para servir de entrada a um projeto de controle.

### Desenvolvimento conceitual

**[01:30–04:00 · TELA: terminal — derivação simbólica das matrizes]**

```bash
.venv/bin/python aula_02/01_sympy_derivacao.py
```

A tela mostra, primeiro, as duas equações diferenciais em notação simbólica: a derivada da corrente depende da tensão aplicada, da resistência vezes a corrente e da constante de força contraeletromotriz vezes a velocidade; a derivada da velocidade depende da constante de torque vezes a corrente, do atrito viscoso vezes a velocidade e do torque de carga. O script isola cada derivada e monta, automaticamente, a forma matricial $\dot{x}=Ax+Bu$, $y=Cx+Du$. Em seguida substitui os números de `params.py` e compara três fontes ao mesmo tempo: a substituição simbólica, uma conta feita à mão e já verificada, e a implementação numérica de `plant.py`. As três batem: a matriz $A$ tem menos trezentos e quarenta e dois vírgula oito mil setecentos e um e menos doze vírgula oito mil quinhentos e setenta e um na primeira linha, e cento e oitenta vírgula zero e menos zero vírgula trinta e dois na segunda; a matriz $B$ tem duzentos e oitenta e cinco vírgula sete mil cento e quarenta e três e zero. A diferença máxima entre as três fontes é da ordem de dez elevado a menos quinze — erro de arredondamento de ponto flutuante, não divergência de modelo. Esse é o argumento central desta seção: espaço de estados não é física nova, é reescrita mecânica de duas equações diferenciais acopladas de primeira ordem, e o computador prova isso rodando as três contas em paralelo.

**[04:00–06:00 · TELA: terminal — o estado como memória mínima]**

O estado deste sistema é o vetor $x=[i,\omega]^T$: corrente de armadura e velocidade angular. A definição formal de estado é esta: é o menor conjunto de variáveis cujo valor presente, somado à entrada futura, determina completamente a evolução futura do sistema. Corrente e velocidade cumprem essa condição para o NexaBot — conhecendo os dois agora e a tensão que será aplicada daqui para frente, a trajetória inteira está determinada, sem precisar de mais nenhuma informação sobre o passado, nem sobre como o motor chegou àquele estado. Note que isso descarta, por exemplo, a posição angular acumulada do eixo: ela não influencia a taxa de variação futura de corrente nem de velocidade, então não faz parte do estado mínimo deste modelo, ainda que seja uma grandeza perfeitamente mensurável. Essa forma $\dot{x}=Ax+Bu$, $y=Cx+Du$ é a entrada padrão para tudo que vem depois nesta disciplina: análise de polos na próxima aula, projeto de controlador na Aula 4, discretização na Aula 7. E repare em algo que a matriz $A$ já revela, sem nenhuma conta adicional: os elementos da primeira linha estão na casa das centenas, e os da segunda, na casa das unidades — um primeiro indício, ainda antes de calcular qualquer polo, de que a dinâmica elétrica evolui numa escala de tempo muito mais rápida que a mecânica. A Aula 3 formaliza exatamente essa observação, com os polos exatos e a razão precisa entre as duas dinâmicas.

**[06:00–08:00 · TELA: terminal — espaço de estados e função de transferência são o mesmo sistema]**

```bash
.venv/bin/python aula_02/02_estado_vs_transferencia.py
```

Este segundo script confere uma segunda equivalência: a mesma dinâmica pode ser escrita como espaço de estados ou como função de transferência, sem perder nem inventar informação. O script converte a state-space que acabamos de derivar em função de transferência com `control.tf`, e compara com a fórmula fechada de `plant.py` — os polos batem em menos sete vírgula dois mil cento e cinquenta e um e menos trezentos e trinta e cinco vírgula noventa e seis mil e duzentos radianos por segundo, exatamente, e o ganho estático bate em vinte e um vírgula dois mil cento e sessenta e quatro radianos por segundo por volt nas duas formas, com diferença da ordem de dez elevado a menos quinze. Em seguida, o mesmo degrau de doze volts é simulado por dois caminhos independentes: a resposta ao degrau da função de transferência, calculada pelo solver de equações diferenciais do `python-control`, e o integrador Runge-Kutta manual de `plant.py`, o mesmo que usamos na Aula 1. O erro máximo entre as duas curvas é de oito por dez elevado a menos seis radianos por segundo — zero vírgula zero zero zero zero por cento do pico —, e essa diferença residual vem só do método numérico de integração, não da física representada.

### Demonstração ao vivo

**[08:00–09:30 · TELA: terminal — por que ajustar a trajetória inteira, e não pontos isolados]**

Com o modelo confirmado por três caminhos independentes, a pergunta muda: e se os seis parâmetros físicos não fossem conhecidos? É esse o cenário do ensaio de identificação que rodo a seguir. A técnica usada aqui é mínimos quadrados não lineares: em vez de estimar derivadas ponto a ponto — o que amplificaria o ruído de medição —, o algoritmo simula a planta inteira para cada conjunto candidato e ajusta a trajetória simulada à medida. O `scipy.optimize.least_squares` usa aqui o método *trust region reflective*, escolhido porque aceita os limites positivos impostos aos parâmetros físicos. O próximo script acrescenta duas imperfeições realistas de bancada: ruído e quantização do conversor analógico-digital na corrente, além da quantização do encoder na velocidade.

**[09:30–13:00 · TELA: terminal — o ensaio de degrau e o ajuste por mínimos quadrados]**

```bash
.venv/bin/python aula_02/03_identificacao.py
```

O script aplica um degrau de doze volts por oito décimos de segundo, amostrado a cinco quilohertz, e gera quatro mil e uma amostras, salvas em `data/ensaio_degrau.csv`. Os dois gráficos ASCII mostram a corrente e a velocidade medidas, já com o ruído e a quantização visíveis — a velocidade, em particular, aparece em pequenos degraus, efeito direto da quantização do encoder. O ajuste parte de um palpite inicial deliberadamente distante da verdade, com até sessenta por cento de erro, como aconteceria numa bancada real onde só se conhece a ordem de grandeza do motor, e converge em apenas onze avaliações da função de resíduo. A tabela final compara os seis parâmetros identificados com os valores verdadeiros: resistência com zero vírgula zero mil duzentos e setenta e nove por cento de erro, indutância com menos zero vírgula zero seiscentos e vinte e oito por cento, as duas constantes eletromecânicas com zero vírgula zero zero noventa e nove por cento, inércia com zero vírgula zero duzentos e cinquenta e um por cento e atrito viscoso com menos zero vírgula mil setecentos e oitenta e três por cento — todos abaixo de dois décimos de um por cento, muitíssimo abaixo do limiar de aceitação de dois por cento que a tabela usa como referência de cor.

**[13:00–16:00 · TELA: terminal — validação em dados retidos e o efeito da subamostragem]**

```bash
.venv/bin/python aula_02/04_validacao.py
```

Ajustar bem o próprio conjunto usado no treino não basta — o modelo pode ter se ajustado ao ruído específico daquele ensaio. Este script valida o modelo identificado contra um segundo ensaio, com amplitude de oito volts em vez de doze e outra semente de ruído, nunca usado no ajuste. A métrica é o `fit` percentual: oitenta e seis vírgula cinquenta e cinco por cento para a velocidade e noventa e oito vírgula zero quatro por cento para a corrente — o modelo generaliza bem para dados que nunca viu. A segunda parte deste script é o ponto pedagógico central da aula: repetir a mesma identificação, mas amostrando o ensaio a cinco milissegundos, o período de amostragem do controlador embarcado, em vez de cinco quilohertz. O resultado é revelador: o erro da indutância salta de menos zero vírgula zero seiscentos e vinte e oito por cento para mais seis vírgula seiscentos e dezenove por cento — cerca de cento e cinco vezes pior —, e o erro do atrito viscoso salta de menos zero vírgula dezessete oitenta e três por cento para menos quatro vírgula quatrocentos e vinte e dois por cento. E note o detalhe mais perigoso deste resultado: o `fit` percentual de velocidade praticamente não muda, de oitenta e seis vírgula cinquenta e cinco para oitenta e seis vírgula cinquenta e dois por cento — o problema fica escondido atrás de um indicador agregado que parece bom. A causa é física: a constante de tempo elétrica do motor, de dois vírgula noventa e dois milissegundos, é menor que o próprio período de amostragem de cinco milissegundos; a subida da corrente acontece quase inteira entre duas amostras consecutivas, e o ajuste perde a capacidade de separar resistência de indutância a partir só do ponto final dessa subida — um fenômeno de subamostragem, análogo ao *aliasing* de um sinal amostrado abaixo da sua própria frequência característica. Note que os outros quatro parâmetros — as duas constantes eletromecânicas, a inércia e, em menor grau, o próprio atrito — continuam bem identificados nas duas taxas de amostragem, porque eles governam a dinâmica mecânica, muito mais lenta, e essa dinâmica continua bem amostrada mesmo a duzentos hertz. É só a dupla resistência-indutância, presa à constante de tempo mais rápida do sistema, que sofre o efeito.

### Aplicação profissional

**[16:00–17:30 · TELA: terminal — identificação de sistemas na indústria]**

Esse cuidado com a taxa de amostragem do ensaio de identificação não é exclusividade acadêmica. Em robótica industrial, equipes de comissionamento identificam parâmetros de motores e de juntas exatamente assim: aplicando degraus controlados numa bancada instrumentada, muito antes de o robô sair da fábrica, porque abrir um atuador já montado para medir resistência e indutância diretamente é caro e, em muitos casos, destrutivo. Na indústria automotiva, a mesma técnica identifica parâmetros de motores de tração elétrica a partir de ensaios de bancada de alta taxa de amostragem, justamente para não repetir o erro que acabamos de ver: usar a taxa de amostragem do controlador de produção — tipicamente muito mais lenta que a dinâmica elétrica do motor — para o próprio ensaio de identificação, o que corrompe silenciosamente os parâmetros elétricos recuperados. A regra prática que fica desta aula é simples de enunciar e fácil de esquecer sob pressão de cronograma: a bancada de identificação precisa amostrar significativamente mais rápido que a dinâmica mais rápida que se pretende identificar — nunca à taxa do controlador final. Vale ainda registrar por que a validação em dados retidos, que fizemos há pouco, é indispensável nesse contexto: um ajuste que parece excelente no próprio conjunto de treino pode estar, sem que ninguém perceba, absorvendo o ruído específico daquele ensaio em vez da física do motor — só um segundo conjunto de dados, nunca usado no ajuste, expõe esse tipo de sobreajuste antes que ele chegue à linha de produção.

### Fechamento

**[17:30–18:30 · TELA: terminal — atividade prática]**

Sua atividade prática usa o segundo conjunto de dados do script `04_validacao.py`, o ensaio de oito volts, como se fosse o único disponível: rode a identificação sobre ele, reportando parâmetro, valor identificado, valor verdadeiro e erro percentual para os seis parâmetros. Depois, discuta se o erro de resistência e de indutância fica maior ou menor que o de inércia e de atrito viscoso, e proponha uma explicação ligada à separação de escalas de tempo que acabamos de discutir — a mesma separação, aliás, que a Aula 3 vai calcular com precisão a partir dos polos do sistema. Registre também qual taxa de amostragem você usou nesse segundo ensaio, porque essa escolha, como acabamos de ver, decide sozinha se o resultado é confiável ou apenas parece confiável.

**[18:30–20:00 · TELA: terminal — pontos-chave e transição]**

Recapitulando. As leis de Kirchhoff e de Newton para rotação modelam o eixo do NexaBot em duas equações diferenciais de primeira ordem, e o SymPy converte isso mecanicamente em espaço de estados, sem risco de erro de álgebra manual. O estado $x=[i,\omega]^T$ é a memória mínima do sistema, e a forma $\dot{x}=Ax+Bu$ é a entrada padrão para tudo que vem a seguir. Sem parâmetros conhecidos, mínimos quadrados não lineares os recupera de um ensaio de degrau com erro abaixo de dois décimos de um por cento, ajustando a trajetória inteira em vez de pontos isolados. E a bancada de identificação precisa amostrar muito mais rápido que o controlador final, porque amostrar à taxa de cinco milissegundos do controlador embarcado faz o erro da indutância saltar cento e cinco vezes, mesmo com o `fit` de velocidade parecendo, à primeira vista, praticamente inalterado. Na próxima aula, aplico a transformada de Laplace às mesmas duas equações que derivamos hoje, chego à função de transferência do NexaBot e calculo os dois polos que explicam, com precisão, por que a corrente parece reagir quase instantaneamente enquanto a velocidade ainda está subindo.

### Indicações de edição e recursos visuais

- Abertura (00:00–01:30): zoom sobre as duas equações diferenciais no editor, sem rolagem rápida.
- Derivação simbólica (01:30–04:00): capturar a tela de terminal completa; se a saída colorida do SymPy não renderizar bem em compressão de vídeo, sobrepor legenda com a matriz $A$ em LaTeX: $A=\begin{bmatrix}-R/L & -K_e/L\\ K_t/J & -b/J\end{bmatrix}$.
- Recurso visual 1 — comparação das três fontes das matrizes $A$ e $B$ (aproximadamente 03:00): já é a tabela ASCII do próprio script; sobrepor destaque verde nas células com diferença desprezível.
- Recurso visual 2 — sobreposição das curvas de espaço de estados e função de transferência (07:00): PNG real em `figuras/aula02_estado_vs_transferencia.png`.
- Recurso visual 3 — tabela de parâmetros identificados versus verdadeiros (11:30): PNG real em `figuras/aula02_identificacao_ajuste.png`.
- Recurso visual 4 — comparação lado a lado do erro de identificação a 5 kHz contra 5 ms (14:30): PNGs reais em `figuras/aula02_validacao_held_out.png` e `figuras/aula02_aliasing_ts_controlador.png`; se possível, exibir os dois PNGs em tela dividida durante a narração do salto de erro.
- Encerramento (18:30–20:00): manter o terminal em tela até o corte final, sem vinheta gráfica cobrindo os últimos números citados.

### Fontes e links de mídia

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011 — referência conceitual, sem reprodução de trecho externo.
- NISE, Norman S. *Engenharia de sistemas de controle*. 6. ed. Rio de Janeiro: LTC, 2013 — referência conceitual, sem reprodução de trecho externo.
- NILSSON, James W.; RIEDEL, Susan A. *Circuitos elétricos*. 10. ed. São Paulo: Pearson, 2016 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; gráficos e tabelas devem ser produzidos a partir dos PNGs reais gerados em `projeto_nexabot/figuras/` e do texto-base da Aula 2 (`unidade_1.md`).

---

## Roteiro da Videoaula 3 — "Dois polos, uma pergunta: dá para ignorar o mais rápido?"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 3 — Laplace, função de transferência e resposta em frequência.

**Objetivo da videoaula:** ao final, o estudante deve conseguir aplicar a transformada de Laplace para obter a função de transferência de um sistema físico, interpretar polos como constantes de tempo, reconhecer separação de escalas de tempo em um sistema de segunda ordem, ler margens de ganho e de fase e banda passante em um diagrama de Bode, e explicar por que uma malha proporcional contínua sobre essa planta nunca desestabiliza — por mais agressivo que seja o ganho.

**Mapa de tempo e telas:** 00:00 editor: `01_laplace_sympy.py` (situação-problema) · 01:30 terminal: Laplace simbólico · 04:00 desenvolvimento: polos e constantes de tempo · 06:00 terminal: polos, zeros e separação de escalas · 08:30 desenvolvimento: por que a velocidade parece de primeira ordem · 10:30 terminal: diagrama de Bode e margens · 13:30 terminal: varredura de Kp e o limite que não vem · 16:30 aplicação profissional · 18:00 pausa para reflexão · 19:00 pontos-chave e atividade · 19:40 fechamento.

### Abertura contextualizada

**[00:00–01:30 · TELA: editor — `aula_03/01_laplace_sympy.py`, com as duas EDOs do motor no topo do arquivo]**

Observando a resposta do NexaBot a um degrau de tensão, a velocidade angular parece obedecer a uma dinâmica simples, de primeira ordem — uma curva suave, sem oscilação, subindo até um patamar, exatamente como vimos na primeira simulação da Aula 1. A corrente de armadura, porém, sobe muito mais rápido, quase instantânea na escala em que a velocidade evolui. O sistema tem duas variáveis de estado e, portanto, dois polos: é de segunda ordem. Mas se comporta, na escala de observação da velocidade, quase como se tivesse só um. Essa aparente contradição não é um defeito do modelo, nem um artefato da simulação — é uma propriedade do próprio sistema físico, e esta aula explica exatamente por quê, transformando o modelo em espaço de estados da Aula 2 em função de transferência pela transformada de Laplace, calculando os dois polos do NexaBot e medindo, com precisão, a separação entre eles.

### Desenvolvimento conceitual

**[01:30–04:00 · TELA: terminal — Laplace simbólico e a função de transferência]**

```bash
.venv/bin/python aula_03/01_laplace_sympy.py
```

A transformada de Laplace converte uma equação diferencial linear, com condições iniciais nulas, em uma equação algébrica em $s$, substituindo cada derivada por multiplicação por $s$. Aplicada às duas equações do motor que derivamos na Aula 2, ela transforma o sistema de equações diferenciais acopladas em duas equações algébricas, resolvíveis por eliminação direta — sem precisar resolver as duas equações diferenciais simultaneamente no domínio do tempo, o que exigiria muito mais trabalho algébrico. O script resolve esse sistema simbolicamente e chega à função de transferência $G(s)=\Omega(s)/V(s)$, na forma canônica $K_t$ dividido por $LJs^2+(RJ+Lb)s+(Rb+K_tK_e)$. Depois, ele substitui os números de `params.py` e faz uma conferência que vale a pena destacar: o coeficiente independente do denominador, dois vírgula cento e vinte e um por dez elevado a menos três, poderia parecer um erro de digitação à primeira vista, por ter uma ordem de grandeza tão diferente dos outros dois coeficientes — a saída confirma, algebricamente, que é exatamente o valor correto de resistência vezes atrito mais constante de torque vezes constante de força contraeletromotriz, e que ele bate com o ganho estático de vinte e um vírgula dois mil cento e sessenta e quatro radianos por segundo por volt que já vimos duas vezes nas aulas anteriores. Esse tipo de checagem cruzada, comparando um número novo com um número já conhecido de outra fonte, é um hábito barato que evita levar um erro de sinal ou de digitação adiante para as próximas quatro aulas.

**[04:00–06:00 · TELA: terminal — polos como constantes de tempo]**

Antes de calcular os polos numericamente, vale fixar o que eles significam fisicamente. Os polos de $G(s)$ são as raízes do denominador, e cada polo real negativo $p$ gera, na resposta natural do sistema, um modo que decai como $e^{pt}$, com constante de tempo $\tau=-1/p$. Quanto mais negativo o polo, mais rápido esse modo desaparece — um polo em menos cem some, na prática, em uma fração do tempo que um polo em menos dez levaria para sumir. $G(s)$ do NexaBot não tem nenhum zero finito, o que simplifica a leitura: não há nenhum termo no numerador cancelando ou realçando parcialmente algum desses modos, então os dois polos, sozinhos, ditam toda a forma da resposta que já observamos na Aula 1: a subida rápida da corrente e a subida mais lenta da velocidade correspondem, respectivamente, ao polo mais negativo e ao polo mais próximo de zero. É essa correspondência direta entre polo e comportamento observado que torna a análise de polos tão valiosa no projeto de controle: ela permite prever a forma da resposta antes mesmo de simular.

### Demonstração ao vivo

**[06:00–08:30 · TELA: terminal — os dois polos e a separação de escalas]**

```bash
.venv/bin/python aula_03/02_polos_zeros.py
```

O script calcula os polos de duas formas independentes, por `control.poles` e por `numpy.roots`, e as duas coincidem: menos trezentos e trinta e cinco vírgula noventa e seis e menos sete vírgula duzentos e quinze radianos por segundo. Seus inversos fornecem as constantes de tempo modais exatas: dois vírgula novecentos e setenta e seis milissegundos e cento e trinta e oito vírgula seis milissegundos. A saída compara esses valores com as aproximações desacopladas já usadas, $L/R$, dois vírgula novecentos e dezesseis milissegundos, e $JR$ dividido por $K_tK_e$, cento e quarenta e oito vírgula cento e quarenta e oito milissegundos. A diferença vem do acoplamento eletromecânico mantido no modelo completo; não é erro numérico. A razão exata entre os modos é quarenta e seis vírgula seis. O script ainda compara o modelo completo com uma redução de primeira ordem. O erro máximo é cerca de cinco radianos por segundo, ou dois vírgula dois por cento do valor final, perto de onze vírgula sete milissegundos, e depois decai; ambos convergem ao mesmo regime porque preservam o ganho estático.

**[08:30–10:30 · TELA: terminal — por que a velocidade parece de primeira ordem]**

Esse resultado explica, com precisão numérica, a observação que abriu esta aula. O modo elétrico, associado ao polo mais negativo, decai em poucos milissegundos — antes que a velocidade, comandada pelo polo lento, tenha saído perceptivelmente do lugar. Do ponto de vista de quem está olhando só para a velocidade, é como se a corrente já tivesse "terminado" de reagir antes de a dinâmica relevante começar a se mover — daí a aparência de sistema de primeira ordem, mesmo o modelo sendo, de fato, de segunda ordem. Essa separação de escalas de tempo, de quase duas ordens de grandeza, não é uma curiosidade matemática isolada: ela é o argumento numérico que vai justificar, na Aula 7, a escolha do período de amostragem de cinco milissegundos do controlador embarcado do NexaBot — amostrar mais rápido que isso captura pouca informação nova sobre a dinâmica mecânica, que é a que o controlador de velocidade realmente precisa acompanhar.

**[10:30–13:30 · TELA: terminal — diagrama de Bode, margens e banda passante]**

```bash
.venv/bin/python aula_03/03_bode.py
```

O diagrama de Bode representa a resposta em frequência da planta, e permite ler diretamente dois indicadores centrais de projeto de controle: a margem de ganho e a margem de fase. A curva de magnitude em ASCII que aparece no terminal mostra a mesma separação de escalas em outra linguagem: dois pontos de quebra, um perto de sete radianos por segundo e outro perto de trezentos e trinta e seis, correspondentes exatamente aos dois polos — abaixo do primeiro, a curva é praticamente plana; entre os dois pontos de quebra, ela cai a vinte decibéis por década, como um sistema de primeira ordem se comportaria; e depois do segundo ponto de quebra, cai a quarenta decibéis por década, revelando o segundo polo. A tabela de resumo entrega os números: margem de fase de setenta vírgula cento e sessenta e sete graus, medida em cento e quarenta vírgula noventa e sete radianos por segundo; margem de ganho infinita, porque a fase desta planta nunca cruza cento e oitenta graus negativos em frequência finita — ela é passa-baixa de segunda ordem sem zeros, e a fase só se aproxima assintoticamente desse limite quando a frequência tende ao infinito; e banda passante de sete vírgula dois mil e noventa e nove radianos por segundo, bem próxima do polo mecânico. Essa proximidade não é coincidência: é de novo o polo lento que limita a velocidade de resposta do sistema em malha aberta, não o rápido. Uma margem de fase de setenta graus é, pelos critérios usuais de projeto de controle, uma margem confortável — valores acima de quarenta e cinco graus costumam ser considerados seguros, e o NexaBot, em malha aberta, já está bem acima disso.

**[13:30–16:30 · TELA: terminal — o Kp cresce, e a malha nunca desestabiliza]**

```bash
.venv/bin/python aula_03/04_estabilidade.py
```

Este último script varre o ganho proporcional de zero vírgula cinco até cinquenta, fechando a malha com realimentação unitária, e tabula margem de fase e sobressinal para cada valor. O comportamento é claro e, à primeira vista, tranquilizador: com Kp igual a zero vírgula cinco, a margem de fase é de oitenta e três vírgula zero seis graus e o sobressinal é praticamente nulo; conforme Kp sobe, a margem de fase cai continuamente — a quarenta e seis vírgula noventa e dois graus em Kp igual a três, a vinte e seis vírgula noventa e quatro graus em Kp igual a dez — e o sobressinal sobe continuamente, até setenta e um vírgula vinte e nove por cento no maior Kp testado, cinquenta. Mas — e este é o resultado contraintuitivo desta aula — a margem de fase nunca chega a zero, e o sobressinal nunca chega a cem por cento: em nenhum ponto dessa varredura de zero vírgula cinco a cinquenta a malha desestabiliza. Isso quebra uma expectativa comum de quem já viu sistemas de ordem mais alta perderem estabilidade ao aumentar o ganho: aqui, por mais que o sobressinal fique visualmente ruim, setenta e um por cento é uma resposta de péssima qualidade para qualquer aplicação prática, mas ainda é uma resposta estável, que converge. A explicação vem direto da análise de Routh-Hurwitz sobre o denominador de malha fechada: o termo que Kp introduz soma-se ao coeficiente independente, que já era positivo, sem nunca torná-lo negativo. Para qualquer Kp positivo, os três coeficientes do polinômio característico permanecem positivos — condição suficiente, para um sistema de segunda ordem, de estabilidade garantida. Vale registrar a generalização: qualquer sistema linear de segunda ordem, sem zeros, realimentado por um ganho proporcional puro, compartilha essa mesma garantia — a instabilidade por ganho excessivo só aparece a partir de sistemas de terceira ordem ou mais, ou quando algum atraso adicional entra na malha, como o atraso computacional que a Aula 7 introduz.

### Aplicação profissional

**[16:30–18:00 · TELA: terminal — onde essa análise aparece na indústria]**

Diagramas de Bode e margens de estabilidade são a linguagem comum de projeto de controle em praticamente toda a indústria que lida com atuadores eletromecânicos: sistemas de direção assistida elétrica no setor automotivo, atuadores de superfícies de controle na aeroespacial, e malhas de velocidade de robôs industriais, como o próprio NexaBot. Um engenheiro de controle raramente projeta olhando só para a resposta ao degrau no tempo; o diagrama de Bode é o instrumento que permite comparar, lado a lado, várias propostas de controlador antes mesmo de simular qualquer uma delas no tempo. Redução de ordem de modelo — descartar o polo rápido e tratar o sistema como se fosse de primeira ordem — é prática corrente nessas indústrias, precisamente porque simplifica o projeto do controlador sem custo relevante, contanto que a dinâmica descartada não seja a que o requisito de segurança está de olho. E aqui cabe uma reflexão que fecha esta aula.

### Pausa para reflexão

**[18:00–19:00 · TELA: terminal — pausa para reflexão com contagem regressiva]**

O polo elétrico do NexaBot é cerca de quarenta e seis vezes mais rápido que o mecânico. Muitos projetos de controle industrial desprezam a dinâmica elétrica nessa situação, tratando o motor como um sistema de primeira ordem — é a redução de ordem de modelo que acabei de mencionar.

*[indicação de edição: pausar a narração por dez segundos, contagem regressiva de dez a zero visível na tela, com o texto "É legítimo desprezar o polo elétrico aqui? O que se perde?"]*

Pare a gravação mentalmente e responda, por escrito, a três perguntas antes de continuar. Primeira: que efeito essa simplificação tem sobre a precisão do modelo em frequências próximas de trezentos e trinta e cinco vírgula noventa e seis radianos por segundo, onde o polo descartado normalmente atuaria? Segunda: que efeito ela tem sobre a análise da corrente de armadura, que está diretamente ligada ao limite de doze ampères do driver do NexaBot — um requisito de segurança, não um detalhe de desempenho? E terceira: essa resposta mudaria se o controlador amostrasse a cada cinco milissegundos, um período já próximo da constante de tempo elétrica de dois vírgula noventa e dois milissegundos? Não existe uma resposta universal para essa reflexão. A legitimidade de descartar o polo rápido depende inteiramente do que o modelo reduzido precisa responder — e é exatamente esse tipo de julgamento, apoiado em número e não em intuição, que separa um projeto de controle maduro de um projeto ingênuo.

### Fechamento

**[19:00–19:40 · TELA: terminal — pontos-chave e atividade prática]**

Recapitulando. A transformada de Laplace converte as duas equações acopladas do motor em uma função de transferência algébrica, sem perda de informação. O NexaBot tem dois polos reais, menos trezentos e trinta e cinco vírgula noventa e seis e menos sete vírgula duzentos e quinze radianos por segundo, com constantes de tempo de dois vírgula noventa e dois milissegundos e cento e quarenta e oito milissegundos — uma separação de quarenta e seis vírgula seis vezes que explica por que a velocidade parece de primeira ordem. O diagrama de Bode expõe essa separação como dois pontos de quebra e entrega margem de fase de setenta vírgula dezessete graus, margem de ganho infinita e banda passante de sete vírgula dois um radianos por segundo. E, resultado que vale reter com cuidado: em malha contínua com controlador proporcional puro, esta planta nunca desestabiliza, por maior que seja o ganho — algo que muda radicalmente assim que a malha passa a ser amostrada, tema que retomamos na Aula 7. Sua atividade prática é obter, com `python-control`, as margens de ganho e de fase em malha aberta e, por varredura, encontrar o ganho proporcional que levaria a margem de fase da malha fechada equivalente a zero grau — registrando por que esse valor é um limite de referência, e não um valor de projeto.

**[19:40–20:00 · TELA: terminal — encerramento]**

Esta aula deixa três resultados formados: obter uma função de transferência a partir de leis físicas, interpretar polos como constantes de tempo e ler margens de estabilidade num diagrama de Bode. Na próxima e última aula desta unidade, verifico se o NexaBot é controlável e observável, projeto uma primeira realimentação de estados e descubro, com números, o exato ponto em que um projeto matematicamente correto passa a exigir mais tensão do que o driver tem para entregar.

### Indicações de edição e recursos visuais

- Abertura (00:00–01:30): manter as duas EDOs visíveis no editor durante toda a fala de contextualização.
- Recurso visual 1 — mapa de polos no plano complexo $s$, com os pontos em $-7{,}215$ e $-335{,}96$ sobre o eixo real negativo (aproximadamente 06:30).
  *Texto alternativo:* Mapa de polos no plano complexo mostra os dois polos reais negativos do NexaBot, ambos no semiplano esquerdo de estabilidade.
- Recurso visual 2 — sobreposição do modelo completo de segunda ordem e do modelo reduzido de primeira ordem (07:30): a comparação ASCII já é gerada pelo próprio script `02_polos_zeros.py`; reproduzir em gráfico de linha na edição, com a faixa de erro destacada nos primeiros 20 ms.
- Recurso visual 3 — diagrama de Bode completo, magnitude e fase (11:00): PNG real em `figuras/aula03_bode.png`.
- Ao citar a fórmula do desvio-padrão de Routh-Hurwitz (15:00), exibir em tela o denominador de malha fechada $8{,}75\times10^{-7}s^2+3{,}0028\times10^{-4}s+(2{,}121\times10^{-3}+K_p\cdot0{,}045)$, com o termo em $K_p$ destacado.
- Pausa para reflexão (18:00–19:00): contagem regressiva de 10 segundos em tela cheia, texto fixo "É legítimo desprezar o polo elétrico aqui? O que se perde?", sem áudio de fundo.
- Encerramento (19:40–20:00): vinheta curta, sem cobrir a última frase de transição.

### Fontes e links de mídia

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011 — referência conceitual, sem reprodução de trecho externo.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013 — referência conceitual, sem reprodução de trecho externo.
- ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; gráficos e diagramas devem ser produzidos a partir do PNG real gerado em `projeto_nexabot/figuras/aula03_bode.png` e do texto-base da Aula 3 (`unidade_1.md`).

---

## Roteiro da Videoaula 4 — "Correto na matemática, impossível no driver"

**Vínculo com o plano de aprendizagem:** Unidade 1, Aula 4 — Controlabilidade, observabilidade e realimentação de estados. Última aula da unidade.

**Objetivo da videoaula:** ao final, o estudante deve conseguir verificar controlabilidade e observabilidade pelo posto das matrizes de Kalman, projetar uma realimentação de estados por alocação de polos, reconhecer o compromisso entre desempenho e esforço de controle no LQR, e explicar como um observador de Luenberger reconstrói uma variável de estado não medida.

**Mapa de tempo e telas:** 00:00 editor: `04_desafio.py` do supervisor (situação-problema) · 01:30 terminal: controlabilidade e observabilidade · 04:00 desenvolvimento: realimentação de estados · 06:00 terminal: alocação de polos e o preço da agressividade · 09:30 desenvolvimento: LQR como o mesmo compromisso via otimização · 10:30 terminal: varredura de LQR · 14:00 terminal: observador de Luenberger · 16:30 aplicação profissional · 18:00 atividade prática e síntese · 19:00 transição para a Unidade 2 · 19:40 fechamento.

### Abertura contextualizada

**[00:00–01:30 · TELA: editor — `aula_04/02_alocacao_polos.py`, com a função `state_feedback_gain` em destaque]**

Um engenheiro júnior recebe a tarefa de deixar o NexaBot mais responsivo. Ele aplica realimentação de estados, escolhe polos de malha fechada bem mais rápidos que os naturais do sistema — operação matematicamente válida, como esta aula vai confirmar — e a simulação entrega exatamente o que foi pedido: a velocidade atinge a referência muito mais rápido que antes. Ao inspecionar a tensão de comando que essa lei de controle exige, porém, o valor ultrapassa os vinte e quatro volts do driver, em ordens de grandeza. O projeto está matematicamente correto, e ao mesmo tempo fisicamente impossível — nenhuma equação foi violada, e ainda assim o resultado não pode ser fabricado. Esta é a última aula da Unidade 1, e ela fecha exatamente esse ciclo: controlabilidade, observabilidade, realimentação de estados e o limite físico que a matemática, sozinha, não enxerga.

### Desenvolvimento conceitual

**[01:30–04:00 · TELA: terminal — controlabilidade e observabilidade]**

```bash
.venv/bin/python aula_04/01_ctrb_obsv.py
```

Antes de projetar qualquer controlador, é preciso responder a duas perguntas estruturais sobre o modelo. Um sistema é controlável quando alguma entrada é capaz de conduzir o estado de qualquer condição inicial a qualquer condição final em tempo finito, e isso se verifica pelo posto da matriz de controlabilidade, formada por $B$ e $AB$ lado a lado. Um sistema é observável quando o estado inteiro pode ser reconstruído a partir só da saída medida, e isso se verifica pelo posto da matriz de observabilidade, formada por $C$ empilhado sobre $CA$. A tela mostra as duas matrizes calculadas para o NexaBot: a matriz de controlabilidade tem determinante de aproximadamente um vírgula quatrocentos e sessenta e nove por dez elevado a sete, e a de observabilidade tem determinante de menos cento e oitenta — ambos não nulos, então as duas matrizes têm posto completo, igual a dois. O NexaBot é totalmente controlável e totalmente observável. Fisicamente, isso significa duas coisas concretas: a tensão de armadura, sozinha, é capaz de levar corrente e velocidade a qualquer par de valores desejado; e, mesmo o encoder só medindo velocidade — a corrente não tem sensor dedicado —, a forma como a velocidade reage no tempo carrega informação suficiente para reconstruir a corrente. Vale notar que essas duas propriedades são condições necessárias, mas não suficientes, para viabilidade de um projeto: um sistema pode ser perfeitamente controlável e, ainda assim, exigir um comando fisicamente irrealizável para atingir um objetivo de desempenho específico. Essa distinção entre existência matemática de solução e viabilidade física de implementação é exatamente o fio que atravessa o restante desta aula, e a segunda propriedade, a observabilidade, é o que o observador desta aula vai explorar, mais adiante.

**[04:00–06:00 · TELA: terminal — realimentação de estados e o compromisso desempenho-esforço]**

Confirmada a controlabilidade, a lei de controle $u=-Kx+\bar{N}r$ posiciona os polos de malha fechada em qualquer localização desejada, escolhendo o vetor de ganhos $K$ de modo que a matriz $A-BK$ tenha exatamente os autovalores pedidos — esse é o teorema de alocação de polos, e ele garante que a solução existe sempre que o par $(A,B)$ for controlável, exatamente a condição que acabamos de confirmar. O termo $\bar{N}r$ é um ganho de pré-compensação, calculado para que o erro de regime seja nulo diante de uma referência constante. O compromisso central desta aula já aparece aqui, em forma de intuição, antes de qualquer número: partindo do repouso, com o estado inicial zerado, o termo $-Kx$ é nulo, e o comando inicial é dominado inteiramente pelo termo $\bar{N}r$. Polos de malha fechada mais rápidos, em geral, exigem um ganho $K$ maior — e, como $\bar{N}$ é calculado em função de $K$ para preservar o erro de regime nulo, ele também cresce. O comando inicial cresce, portanto, proporcionalmente à velocidade de resposta que se está pedindo ao sistema. É essa proporcionalidade, ainda qualitativa neste ponto, que os dois cenários numéricos a seguir vão tornar precisa.

### Demonstração ao vivo

**[06:00–09:30 · TELA: terminal — dois cenários de alocação de polos]**

```bash
.venv/bin/python aula_04/02_alocacao_polos.py
```

Este script materializa o compromisso em dois cenários concretos, ambos perseguindo a mesma referência: quatrocentos radianos por segundo, ou um metro por segundo de velocidade linear, partindo do repouso. O cenário moderado aloca polos duplos em menos setecentos e menos vinte radianos por segundo — duas vírgula oito e duas vírgula uma vezes mais rápidos que os polos naturais, pareados por magnitude. O ganho resultante é $K$ igual a um vírgula trinta e um oitenta e nove e zero vírgula dois mil duzentos e vinte e sete, com pré-compensação de zero vírgula dois mil setecentos e vinte e dois. O pico de tensão exigido pela lei de controle ideal, sem saturar, já é de cento e oito vírgula oitenta e nove volts — mais de quatro vezes o limite do driver. Quando a saturação em vinte e quatro volts é respeitada, a resposta real ainda chega perto da referência, com tempo de acomodação de duzentos e cinquenta e seis vírgula quarenta e nove milissegundos e um pequeno erro de regime de três vírgula cinquenta e seis radianos por segundo. O segundo cenário, agressivo, aloca polos em menos três mil e menos três mil e quinhentos radianos por segundo. O pico de tensão ideal, aqui, é de oitenta e um mil, seiscentos e sessenta e sete volts — mais de três mil vezes o limite físico do driver. Saturada em vinte e quatro volts, a resposta real deixa de ser ditada pelos polos escolhidos e passa a ser ditada, na prática, pelo próprio limite do atuador: o controlador vira, de fato, um comando liga-desliga em mais ou menos vinte e quatro volts, com tempo de acomodação de duzentos e seis vírgula sessenta e um milissegundos — nem tão diferente do cenário moderado, apesar de pedir, na teoria, uma resposta centenas de vezes mais rápida. Alocar polos sem checar a tensão exigida é, portanto, ilusório: o projeto só é válido se a lei de controle respeitar o limite do atuador em toda a faixa de operação esperada. Vale notar que os dois cenários fecham com tempo de acomodação real bastante parecido, duzentos e cinquenta e seis contra duzentos e seis milissegundos, apesar de o cenário agressivo pedir polos centenas de vezes mais rápidos na teoria — a saturação nivela os dois resultados por baixo, e é justamente esse nivelamento que denuncia, sem precisar de mais nenhuma conta, que o segundo projeto nunca respeitou o limite físico do driver.

**[09:30–10:30 · TELA: terminal — o LQR enfrenta o mesmo compromisso, por outro caminho]**

O regulador linear quadrático, o LQR, chega ao mesmo tipo de solução por um caminho diferente. Em vez de escolher os polos diretamente, quem projeta escolhe duas matrizes de peso: $Q$, que penaliza o desvio de cada variável de estado, e $R$, que penaliza o esforço de controle. Um algoritmo de otimização calcula o ganho $K$ que minimiza esse custo combinado, integrado ao longo de todo o horizonte de tempo. Aumentar a penalidade sobre o erro de estado, ou diminuir a penalidade sobre o esforço, desloca os polos resultantes para mais rápido — a mesma família de soluções da alocação direta de polos, só que obtida por otimização, com a vantagem de poder ponderar cada estado individualmente: por exemplo, penalizar mais a corrente do que a velocidade, se o limite térmico do motor for a preocupação principal do projeto, algo que a alocação direta de polos não oferece de forma tão natural.

**[10:30–14:00 · TELA: terminal — varredura de Q e R, a mesma fronteira em outra roupagem]**

```bash
.venv/bin/python aula_04/03_lqr.py
```

O script varre dezesseis combinações de $Q$ igual a diagonal de um e um segundo peso, entre um e mil, e $R$ entre zero vírgula zero um e dez, tabulando, para cada uma, tempo de acomodação, pico de tensão e a energia de controle, medida pela integral de $u$ ao quadrado no tempo. Os dois extremos da varredura ilustram bem o compromisso: a combinação mais suave, com o segundo peso de $Q$ igual a um e $R$ igual a dez, entrega tempo de acomodação de oitenta e cinco milissegundos, com pico de tensão de cento e vinte e sete vírgula nove volts. A combinação mais agressiva, com o segundo peso de $Q$ igual a mil e $R$ igual a zero vírgula zero um, entrega tempo de acomodação de menos de um milissegundo — mas exige um pico de tensão de cento e vinte e seis mil, quatrocentos e noventa e um volts, com uma energia de controle da ordem de um milhão e duzentos e sessenta e cinco mil unidades, contra trezentas e oito na combinação mais suave. E o dado mais contundente da tabela inteira: das dezesseis combinações varridas, todas exigem pico de tensão acima dos vinte e quatro volts disponíveis — o LQR não cria desempenho de graça, ele só torna explícito, em números, o mesmo compromisso que a alocação de polos escondia atrás de uma escolha de localização feita às cegas.

**[14:00–16:30 · TELA: terminal — o observador de Luenberger estima o que não é medido]**

```bash
.venv/bin/python aula_04/04_observador.py
```

Voltando à observabilidade confirmada no início desta aula: o encoder do NexaBot mede só a velocidade, nunca a corrente diretamente. Um observador de Luenberger resolve esse problema construindo uma cópia do modelo da planta que roda em paralelo, corrigida continuamente pelo erro entre a velocidade medida de verdade e a velocidade que a própria cópia prevê. O script projeta esse observador por alocação de polos do erro de estimação, escolhendo polos em menos dois mil e quinhentos e menos oitenta radianos por segundo — cerca de três vírgula seis e quatro vezes mais rápidos que os polos de malha fechada de referência do cenário moderado. O ganho resultante é $L$ igual a menos três mil cento e sessenta e três e dois mil duzentos e trinta e sete. Para deixar claro que o observador não faz mágica, ele parte de um chute inicial deliberadamente errado — uma corrente estimada de um ampère e uma velocidade estimada de trinta radianos por segundo, contra corrente e velocidade reais nulas no início. O erro de estimação da corrente chega a um pico de trinta e quatro vírgula cinco ampères logo no início, mas decai com a constante de tempo do polo mais lento do observador, e cai para menos zero vírgula zero zero zero quatorze ampères aos cento e cinquenta milissegundos — convergência efetivamente completa, sem que o observador nunca tenha medido a corrente diretamente. Ele só viu a tensão aplicada e a velocidade do encoder, e isso bastou, porque o sistema é observável.

### Aplicação profissional

**[16:30–18:00 · TELA: terminal — o limite do atuador na indústria, e o observador como economia de sensor]**

Este par de resultados — o limite de tensão e o observador de estado — aparece constantemente em projetos reais. Em veículos elétricos e em robótica industrial, o dimensionamento de um controlador precisa sempre confrontar o desempenho desejado com a tensão de barramento disponível: um controlador matematicamente ótimo, que exige tensão além do que a bateria e o inversor entregam, simplesmente não existe fora da simulação — o sistema real vai operar saturado, com comportamento diferente do previsto, exatamente como vimos no cenário agressivo. É por isso que equipes de engenharia de controle experientes checam o pico de comando exigido antes de validar qualquer projeto por simulação isolada, e é exatamente essa disciplina que os scripts desta aula automatizam. E observadores de estado, como o de Luenberger, sustentam uma prática comum de engenharia chamada controle sem sensor, ou *sensorless*: em motores de tração e em compressores industriais, eliminar um sensor de corrente ou de posição reduz custo, peso e um ponto a mais de falha mecânica — desde que a observabilidade do sistema, verificada logo no início desta aula, garanta que a informação que falta pode ser reconstruída a partir do que já se mede.

### Fechamento

**[18:00–19:00 · TELA: terminal — atividade prática e pontos-chave]**

Sua atividade prática usa o terceiro script desta aula: escolha três pares de $Q$ e $R$, mantendo $R$ fixo em zero vírgula um e variando a penalidade sobre a velocidade em pelo menos uma ordem de grandeza entre cada par. Para cada um, registre o ganho $K$, o pico de tensão para o mesmo degrau de quatrocentos radianos por segundo partindo do repouso, e o tempo de acomodação — identificando o par mais agressivo que ainda respeita os vinte e quatro volts do driver. Recapitulando os pontos-chave desta aula: controlabilidade e observabilidade, verificadas pelo posto das matrizes de Kalman, garantem que existe uma entrada capaz de levar o estado a qualquer valor e que esse estado pode ser reconstruído pela saída — e o NexaBot tem posto completo nas duas. A realimentação de estados aloca polos de malha fechada em qualquer posição, mas ganhos maiores exigem comandos proporcionalmente maiores, e polos poucas vezes mais rápidos que os naturais já bastam para estourar o limite de tensão do driver. O LQR enfrenta exatamente o mesmo compromisso, por otimização de $Q$ e $R$, sem escapar dele. E um observador de Luenberger reconstrói uma variável de estado nunca medida diretamente, desde que o sistema seja observável — o que o NexaBot é.

**[19:00–19:40 · TELA: terminal — transição para a Unidade 2]**

Encerro aqui a Unidade 1. Ao longo de quatro aulas, você modelou o NexaBot a partir de leis físicas, identificou seus seis parâmetros a partir de dados de ensaio com ruído realista, calculou seus dois polos e sua separação de escalas de tempo, e agora dispõe de um primeiro controlador em espaço de estados, com o limite de implementabilidade já quantificado em volts, não apenas intuído. Falta, no entanto, a estrutura de controle mais usada na indústria de fato: o PID, com sintonia consagrada e tratamento explícito de saturação e de acúmulo indevido no integrador, o chamado *anti-windup*. E falta levar esse controlador para o domínio discreto em que o microcontrolador do NexaBot efetivamente vive, amostrando a cada cinco milissegundos, e não em tempo contínuo como fizemos até aqui. A Unidade 2 fecha exatamente essas duas lacunas.

**[19:40–20:00 · TELA: terminal — encerramento]**

Esta unidade constrói o modelo; a próxima fecha a malha. Na Aula 5, comparo formalmente malha aberta e malha fechada, com a álgebra de blocos do `python-control`, sobre a mesma planta que você já conhece de cor. Até lá.

### Indicações de edição e recursos visuais

- Abertura (00:00–01:30): destacar no editor a assinatura da função `state_feedback_gain`, sem rolar o arquivo inteiro.
- Recurso visual 1 — matrizes de controlabilidade e de observabilidade, com determinantes e postos (aproximadamente 02:30): a tabela ASCII já é a saída real do script `01_ctrb_obsv.py`.
  *Texto alternativo:* Terminal exibe as matrizes de controlabilidade e observabilidade do NexaBot, ambas com posto completo igual a dois.
- Recurso visual 2 — tensão de pico exigida nos dois cenários de alocação de polos, moderado e agressivo (aproximadamente 08:30): PNGs reais em `figuras/aula04_alocacao_moderado.png` e `figuras/aula04_alocacao_agressivo.png`; exibir lado a lado se o layout de edição permitir.
- Recurso visual 3 — varredura de $Q$ e $R$ do LQR, pico de tensão contra tempo de acomodação (aproximadamente 12:30): PNG real em `figuras/aula04_lqr_esforco_agressivo.png`.
- Recurso visual 4 — convergência do observador de corrente, real contra estimada (aproximadamente 15:30): PNGs reais em `figuras/aula04_observador_corrente_real.png` e `figuras/aula04_observador_corrente_estimada.png`.
- Ao citar a lei de controle (04:30), exibir em tela $u=-Kx+\bar{N}r$, com $\bar{N}=1/\big(C(-(A-BK))^{-1}B\big)$ como legenda inferior.
- Transição para a Unidade 2 (19:00–19:40): tom de fechamento de unidade, não apenas de aula; considerar um card curto "Unidade 1 concluída" antes da vinheta final.

### Fontes e links de mídia

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011 — referência conceitual, sem reprodução de trecho externo.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013 — referência conceitual, sem reprodução de trecho externo.
- ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021 — referência conceitual, sem reprodução de trecho externo.
- KALMAN, Rudolf E. On the general theory of control systems. *IRE Transactions on Automatic Control*, v. 4, n. 3, p. 110, dez. 1959. DOI: 10.1109/TAC.1959.1104873 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; gráficos e diagramas devem ser produzidos a partir dos PNGs reais gerados em `projeto_nexabot/figuras/` e do texto-base da Aula 4 (`unidade_1.md`).
