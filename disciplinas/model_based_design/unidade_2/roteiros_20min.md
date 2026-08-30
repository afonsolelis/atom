# Roteiros das videoaulas 5 a 8 — Unidade 2 (20 minutos)

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 2: Modelagem e simulação de sistemas de controle
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: aproximadamente 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, comandos, saídas de terminal, indicações de edição e fontes.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas, respiração e o tempo de leitura da saída na tela.

Esta é uma disciplina gravada por captura de tela e câmera, sem deck de slides: cada roteiro alterna entre blocos `TELA: terminal`, com o diretório `projeto_nexabot/` já aberto e o interpretador `.venv/bin/python`, e blocos `TELA: editor`, com um arquivo de `nexabot/` ou de `aula_0N/` aberto para leitura comentada. Todo comando citado em bloco de terminal foi executado durante a produção deste roteiro, e a saída descrita reflete exatamente o que apareceu na tela — nenhum número aqui é estimado ou arredondado além do que o próprio script já arredonda. Nenhuma aula começa em tela neutra: os dois primeiros minutos de cada videoaula já têm terminal ou editor abertos, com algo em andamento, e o gancho da aula nasce daquilo que já está na tela.

Plano de tempo de referência, adaptável ao ritmo de cada aula:

- 00:00–02:00 — abertura contextualizada, já em tela de terminal ou editor;
- 02:00–08:30 — desenvolvimento conceitual, em editor, com leitura comentada do código-fonte;
- 08:30–16:00 — demonstração ao vivo, em terminal, com os comandos e a saída real da aula;
- 16:00–18:30 — aplicação profissional (e, na Aula 7, pausa para reflexão com contagem regressiva);
- 18:30–20:00 — pontos-chave, atividade prática e encerramento.

O fio condutor das quatro aulas é fechar a malha de velocidade do NexaBot: a Aula 5 formaliza malha aberta contra malha fechada; a Aula 6 projeta e sintoniza o PID, tratando saturação e *windup* como parte do projeto, não como exceção; a Aula 7 discretiza esse controlador e fixa o contrato numérico do `DiscretePID` que a Unidade 4 traduzirá para C; e a Aula 8 acopla planta e controlador por co-simulação FMI 3.0, medindo o erro que esse acoplamento introduz. Cada roteiro é texto de narração pronto para leitura em voz alta, não notas de aula: frases completas, encadeamento explícito entre as ideias, sem recursos de oralidade informal.

---

## Roteiro da Videoaula 5 — "A carga muda, e a malha aberta erra de novo"

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 5 — Malha aberta, malha fechada e álgebra de diagramas de blocos.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de montar a malha fechada do NexaBot por álgebra de blocos em `python-control` e validar o resultado contra uma redução simbólica manual, definir as funções de sensibilidade $S$ e complementar $T$ e verificar numericamente a identidade $S+T=1$, explicar por que um polo na origem em $C(s)$ elimina o erro de regime a um distúrbio constante, e comparar quantitativamente a rejeição a um distúrbio de carga em malha aberta e em malha fechada.

**Mapa de tempo e telas:** 00:00 terminal com o resultado do script 1 já na tela · 01:40 editor: `aula_05/01_algebra_blocos.py`, série/paralelo/realimentação · 03:20 editor: definição de $S$ e $T$ · 05:10 editor: erro em regime e tipo de sistema · 07:00 editor: do PID como $C(s)$ à ponte para a Aula 6 · 08:30 terminal: `02_rejeicao_disturbio.py` · 11:00 terminal: `03_sensibilidade.py` · 13:30 terminal: `04_desafio.py` · 15:30 aplicação profissional · 17:30 pontos-chave e atividade · 19:00 encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: terminal — aula_05/01_algebra_blocos.py, tabelas já na tela]**

A tela mostra, neste exato momento, quatro tabelas comparando dois caminhos independentes de cálculo: de um lado, `sympy`, fazendo álgebra de frações símbolo a símbolo; do outro, `python-control`, chamando `ct.series`, `ct.parallel` e `ct.feedback`. As quatro tabelas terminam com a mesma palavra, em verde: bateram. Chegar a essa concordância, e entender por que ela importa, é o assunto desta aula.

Recuo até a Unidade 1. O NexaBot, com tensão fixa de armadura, perdia velocidade assim que uma carga era colocada sobre a plataforma — o robô simplesmente não sabia que a carga havia mudado, porque nada media o efeito e corrigia a tensão em resposta. Uma primeira tentativa de correção somou um deslocamento fixo à tensão, calibrado para a carga média observada em bancada. Funcionou até a próxima caixa mais pesada aparecer, e o deslocamento fixo, calibrado para outra carga, voltou a errar. O problema nunca esteve no valor do deslocamento. Está na ausência de realimentação. Esta aula formaliza, com números do próprio NexaBot, por que fechar a malha resolve esse problema de forma estrutural, e não apenas para o caso particular que foi calibrado.

Essa formalização segue um caminho específico, e vale adiantá-lo: primeiro escrevo a malha fechada em termos algébricos, depois defino duas funções que resumem tudo o que uma realimentação promete e custa, e só então chego ao caso concreto do NexaBot sob carga. É um caminho um pouco mais longo do que simplesmente testar um ganho por tentativa e erro, mas é o único que explica por que o resultado vale para qualquer carga, não apenas para a que foi medida em bancada.

### Desenvolvimento conceitual

**[01:40–03:20 · TELA: editor — aula_05/01_algebra_blocos.py, série, paralelo e realimentação]**

Abro o script que gerou a tela inicial. Ele monta um controlador proporcional-derivativo elementar — $K_p=6$ em paralelo com um bloco derivativo puro $K_d s$, com $K_d=0{,}01$ — e o coloca em série com a planta $G(s)$ do NexaBot, a mesma função de transferência de segunda ordem obtida na Unidade 1. Cada uma dessas três operações tem nome técnico: série multiplica duas funções de transferência, paralelo soma, e realimentação resolve $L/(1+L)$ para uma malha fechada. `ct.series`, `ct.parallel` e `ct.feedback`, do `python-control`, fazem exatamente essas três operações. Nada nelas é mágico: multiplicar frações, somar frações, isolar uma variável numa equação. A vantagem da biblioteca não é fazer algo que uma pessoa não possa fazer à mão — é evitar erro de álgebra em polinômios de grau mais alto, mantendo o resultado inteiramente auditável, ponto a ponto, contra o cálculo manual. É exatamente essa auditoria que as quatro tabelas na tela de abertura confirmaram: cada coeficiente de numerador e de denominador, calculado pelas duas vias, bateu dentro de uma tolerância relativa de um milionésimo.

**[03:20–05:10 · TELA: editor — a sensibilidade S e a complementar T]**

Com a malha fechada montada, cabe uma pergunta mais importante do que qualquer coeficiente isolado: o que uma realimentação negativa promete, e o que ela custa. Na realimentação negativa, a tensão deixa de ser fixa e passa a ser calculada por um controlador $C(s)$ a partir do erro entre referência e velocidade medida. Chamando $L(s)=C(s)G(s)$ o ganho de malha aberta, a saída em função da referência $R(s)$ e de um distúrbio de carga $T_l(s)$ se escreve como a soma de dois termos, ambos divididos pelo mesmo denominador $1+L(s)$.

Esses dois termos têm nome. A sensibilidade, $S(s)=1/(1+L(s))$, multiplica o efeito do distúrbio e do ruído de medição sobre a saída. A complementar, $T(s)=L(s)/(1+L(s))$, multiplica o efeito da referência. E, por construção algébrica direta, $S(s)+T(s)=1$, sempre, em qualquer frequência. Essa identidade tem uma consequência que qualquer projetista de controle precisa internalizar: não é possível tornar $S$ e $T$ pequenos na mesma frequência. Reduzir $S$ perto de zero, para rejeitar bem um distúrbio de baixa frequência, obriga $T$ a ficar perto de um nessa mesma faixa — o que é exatamente o que se quer para seguir a referência, mas também é o que amplifica ruído de sensor, caso esse ruído tenha energia relevante ali. Projetar $C(s)$ é decidir até que frequência vale a pena perseguir essa troca.

Vale registrar por que essa dedução importa mais do que qualquer número isolado que a demonstração vá mostrar daqui a pouco: ela é válida para qualquer $C(s)$ estabilizante, não apenas para o PID que a Aula 6 vai projetar. Um estudante que entende a identidade $S+T=1$ nunca vai prometer, num relatório de projeto, uma malha que rejeita perfeitamente distúrbio e rastreia perfeitamente referência na mesma faixa de frequência — porque sabe, de antemão, que essa promessa é algebricamente impossível de cumprir.

**[05:10–07:00 · TELA: editor — erro em regime permanente e o tipo do sistema]**

Uma segunda consequência prática da mesma álgebra: o número de integradores puros dentro de $L(s)$ define o que a literatura chama de tipo do sistema. A planta $G(s)$ do NexaBot não tem polo na origem — é tipo zero. Se o controlador $C(s)$ também não tiver, $L(s)$ permanece tipo zero, e o erro de regime a um distúrbio de carga constante é finito e diferente de zero, por menor que ele seja. Basta um único polo na origem em $C(s)$ para elevar $L(s)$ a tipo um: nesse caso, $S(0)$ tende a zero, e o erro de regime a qualquer distúrbio constante tende a zero também — independentemente dos valores numéricos escolhidos para os ganhos, desde que a malha resultante seja estável. O mesmo raciocínio, aplicado à referência em vez de ao distúrbio, explica por que um sistema tipo zero converge para um valor final sempre abaixo do que foi pedido, enquanto um sistema tipo um rastreia esse mesmo degrau sem erro de regime algum. A diferença entre chegar perto e chegar exatamente não depende de quão bem os ganhos foram ajustados: depende de quantos integradores existem dentro do laço.

**[07:00–08:30 · TELA: editor — do PID como C(s) à ponte para a Aula 6]**

Isso conecta diretamente com a estrutura que domina a indústria de controle: o PID. Formalmente, o PID é apenas um caso particular de $C(s)$, e a parte que importa aqui é reconhecer que $K_p+K_i/s+K_ds$ tem exatamente um polo na origem — o suficiente, pela álgebra que acabei de descrever, para elevar $L(s)$ a tipo um e eliminar o erro de regime, sem exigir realimentação de nenhuma variável além da própria velocidade medida pelo encoder. É por isso que o PID é a resposta industrial dominante quando só existe um sensor de saída: ele entrega ação integral e derivativa sobre um único sinal medido, sem exigir sensor adicional de corrente, ao contrário da realimentação de estados que a Unidade 1 já havia projetado. Mas reconhecer que a estrutura resolve o problema em teoria é uma coisa; escolher os três ganhos que a fazem funcionar sobre o motor real do NexaBot, sem violar o limite físico de $24\,\mathrm{V}$, é bem menos trivial — e é exatamente o assunto da Aula 6.

### Demonstração ao vivo

**[08:30–11:00 · TELA: terminal — aula_05/02_rejeicao_disturbio.py]**

Chega o momento de ver essa diferença de tipo de sistema virar número, e não apenas argumento. Rodo:

```
.venv/bin/python aula_05/02_rejeicao_disturbio.py
```

O cenário é o seguinte: o NexaBot de cruzeiro a $1{,}00\,\mathrm{m/s}$, ou seja, $400\,\mathrm{rad/s}$ no eixo do motor, com tensão de regime de $18{,}853\,\mathrm{V}$ sem carga. Em $t=0{,}10\,\mathrm{s}$, aplico um degrau de torque de carga de $162$ miliNewton-metro — trinta por cento do torque nominal do motor em corrente máxima. A primeira parte da tela mostra a malha aberta: a velocidade cai suavemente da referência e se estabiliza em $0{,}7771\,\mathrm{m/s}$, um erro final de $22{,}3\%$ que simplesmente permanece ali, porque nada na malha aberta sabe que o erro existe. A segunda parte mostra a malha fechada, com o PID discreto de $K_p=2{,}0$, $K_i=50{,}0$ e $K_d=0{,}001$ amostrado a $5\,\mathrm{ms}$: a velocidade mal se move fora da faixa de referência, o erro final registrado é de menos de um milésimo por cento — essencialmente zero —, e a tabela final confirma que a malha nunca saiu da faixa de dois por cento em torno do alvo. A tensão de regime sobe de $18{,}85\,\mathrm{V}$ para $23{,}17\,\mathrm{V}$, com um pico transitório que toca exatamente o teto de $24{,}00\,\mathrm{V}$ — o controlador usa quase toda a margem que resta, mas não precisa mais do que isso.

O mesmo degrau de torque, aplicado às duas malhas, desloca a malha aberta para um novo regime permanente, vinte e dois por cento abaixo do alvo, e a mantém lá indefinidamente; a malha fechada mede o erro a cada período de amostragem e o realimenta, até zerá-lo. Essa é a rejeição a distúrbio prometida pela ação integral, e ela deixou de ser um argumento algébrico para virar um número reproduzível na tela.

**[11:00–13:30 · TELA: terminal — aula_05/03_sensibilidade.py]**

Rodo agora o script que confirma a identidade $S+T=1$ numericamente, e não apenas por manipulação simbólica:

```
.venv/bin/python aula_05/03_sensibilidade.py
```

Com o PID contínuo equivalente $K_p=2$, $K_i=50$, $K_d=0{,}001$ e filtro derivativo $N=20$, o script varre duzentas frequências entre $0{,}01$ e um milhão de radianos por segundo e mede, em cada uma, o módulo de $S(j\omega)+T(j\omega)-1$. O maior desvio observado em toda essa varredura foi de $4{,}45\times10^{-16}$ — ruído de ponto flutuante, não uma aproximação. A tabela de frequências marcantes conta a história completa: perto de zero, $|S|$ vale praticamente zero, cerca de $-100{,}5$ decibéis, e $|T|$ vale um — a malha segue a referência e rejeita distúrbio de baixa frequência quase perfeitamente. No cruzamento da malha aberta, perto de $250\,\mathrm{rad/s}$, os dois módulos se aproximam de um simultaneamente. E exatamente ali perto, em $364\,\mathrm{rad/s}$, $|S|$ atinge seu pico, $1{,}4931$ — mais de um, a chamada água-cama da sensibilidade: reduzir $S$ numa faixa de frequência necessariamente eleva $S$ em outra, e a soma constante com $T$ garante que essa troca nunca pode ser eliminada, apenas deslocada de frequência. Em alta frequência, $10^5\,\mathrm{rad/s}$, o padrão se inverte: $|S|$ volta a um e $|T|$ cai para praticamente zero, quase $-100$ decibéis — a malha filtra ruído de sensor nessa faixa, ao custo de não seguir nenhuma referência que tivesse energia ali, o que nunca é o caso para o NexaBot.

**[13:30–15:30 · TELA: terminal — aula_05/04_desafio.py]**

Fecho a demonstração com o desafio da aula. Rodo:

```
.venv/bin/python aula_05/04_desafio.py
```

O enunciado propõe um cenário mais exigente: o NexaBot de cruzeiro a $1{,}0\,\mathrm{m/s}$ recebe, em $t=0{,}15\,\mathrm{s}$, um degrau de torque de carga de trinta e três por cento do torque nominal — $178{,}2$ miliNewton-metro, próximo do limite que os $24\,\mathrm{V}$ ainda conseguem compensar em regime, de modo que a malha não sobra folga. A tela, sem a função ainda implementada, mostra o aviso amarelo esperado — "ainda não implementado" — seguido da tabela de critérios de aceitação: erro de regime entre zero e cinco centésimos por cento, sobressinal entre zero e três por cento, e tempo de recuperação até vinte milissegundos. Rodando a implementação de referência com os mesmos ganhos do script anterior, esses três critérios se cumprem folgadamente; e o próprio enunciado adverte que ganhos "fracos" — por exemplo, $K_p=0{,}2$, $K_i=5$ — recuperam em cerca de oitenta e cinco milissegundos e falham o critério de tempo, uma ilustração direta de que ter ação integral não basta: o valor do ganho integral também importa, e é exatamente esse ajuste fino que a Aula 6 formaliza.

### Aplicação profissional

**[15:30–17:30 · TELA: terminal — mesma tela do desafio, aplicação profissional]**

A distinção entre malha aberta e malha fechada que acabei de demonstrar não é um exercício acadêmico isolado do NexaBot: é a diferença entre um produto que funciona em laboratório e um produto que funciona em campo. No controle de cruzeiro automotivo, a malha aberta manteria o acelerador numa posição fixa calibrada para um trecho plano — e falharia assim que a estrada começasse a subir, exatamente como o NexaBot falhava sob carga. A malha fechada mede a velocidade real do veículo e corrige o comando de combustível ou de torque elétrico continuamente, o mesmo princípio algébrico desta aula, aplicado a uma planta de ordem mais alta.

A identidade $S+T=1$ também tem nome fora da academia: é o motivo pelo qual engenheiros de controle discutem largura de banda de malha fechada como uma decisão explícita de projeto, não como um número que "quanto maior, melhor". Um sistema de piloto automático de aeronave, por exemplo, precisa de $T$ próximo de um na faixa de frequência das manobras normais de voo, mas precisa de $S$ pequeno — e portanto $T$ pequeno — na faixa de frequência de rajadas de vento e de ruído de sensores inerciais, sob pena de o próprio controlador amplificar uma vibração que, sem ele, seria inofensiva. Todo projeto sério de malha fechada é, no fundo, essa mesma negociação entre rejeitar distúrbio e não amplificar ruído, expressa pela mesma soma constante que a malha do NexaBot acabou de confirmar numericamente.

Em braços robóticos industriais, o mesmo compromisso aparece sob outro nome: rigidez de malha. Uma malha "rígida", com $T$ próximo de um numa faixa larga, segue trajetórias com precisão, mas transmite ao efetuador qualquer vibração mecânica ou ruído elétrico que exista naquela mesma faixa — e a solução profissional nunca é "aumentar o ganho até parar de vibrar", porque isso apenas desloca o problema para outra frequência, exatamente como a água-cama da sensibilidade descreve.

### Fechamento

**[17:30–19:00 · TELA: editor — síntese e atividade prática]**

Recapitulando os pontos-chave desta aula. `ct.series`, `ct.parallel` e `ct.feedback` reproduzem exatamente a álgebra de frações que uma redução simbólica manual produz — a biblioteca evita erro em graus altos, não substitui o raciocínio. $S(s)+T(s)=1$ vale em qualquer frequência, e essa soma constante impõe um limite físico: nenhum projeto reduz sensibilidade a distúrbio e resposta a referência na mesma frequência ao mesmo tempo. O número de integradores em $L(s)$, e não o valor dos ganhos, decide se o erro de regime a um distúrbio constante é nulo ou apenas pequeno. E, sob o mesmo degrau de trinta por cento do torque nominal, a malha aberta do NexaBot perdeu vinte e dois vírgula três por cento de velocidade permanentemente, enquanto a malha fechada com ação integral recuperou a referência exata.

A atividade prática desta aula pede o seguinte: repita o cálculo de erro de regime da malha aberta para um degrau de torque de carga de quarenta por cento do nominal, usando as mesmas equações de equilíbrio do texto-base; em seguida, usando `aula_05/03_sensibilidade.py`, identifique a faixa de frequência em que $|S(j\omega)|$ é menor que um décimo e explique, em duas frases, o que essa faixa representa para a rejeição de distúrbios de baixa frequência no NexaBot.

**[19:00–20:00 · TELA: terminal — encerramento]**

Esta aula formalizou por que fechar a malha resolve, de forma estrutural, o problema de perda de velocidade sob carga que abriu toda a disciplina. A próxima aula projeta o controlador PID completo para o NexaBot, com sintonia por Ziegler-Nichols, métricas objetivas de aceitação, e um problema que a teoria de hoje ainda não tocou: o que acontece com o integrador quando o atuador de $24\,\mathrm{V}$ simplesmente não consegue entregar a tensão que o erro pede. Até lá.

### Indicações de edição e recursos visuais

- Inserir Recurso visual 2 da unidade — curvas $|S(j\omega)|$ crescente e $|T(j\omega)|$ decrescente com a soma constante destacada — sobreposto ao editor, aproximadamente em 04:00.
- 08:30–11:00 — tela dividida: à esquerda a curva de velocidade em malha aberta estabilizando abaixo da referência; à direita a malha fechada, quase imperceptível fora da faixa de referência.
- Inserir Recurso visual 3 da unidade — degrau de torque com a curva aberta em $0{,}777\,\mathrm{m/s}$ e a fechada retornando a $1{,}000\,\mathrm{m/s}$ — aproximadamente em 09:30.
- 11:00–13:30 — congelar a tabela de frequências marcantes com zoom na linha do pico de sensibilidade, $w=364\,\mathrm{rad/s}$.
- 19:40–20:00 — vinheta de encerramento com chamada para a Videoaula 6.

### Fontes e links de mídia

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011 — referência conceitual, sem reprodução de trecho externo.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013 — referência conceitual, sem reprodução de trecho externo.
- ÅSTRÖM, Karl Johan; MURRAY, Richard M. *Feedback Systems: An Introduction for Scientists and Engineers*. 2. ed. Princeton: Princeton University Press, 2021 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas e gráficos devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 5 (`unidade_2.md`) e da saída real dos scripts de `projeto_nexabot/aula_05/`.

---

## Roteiro da Videoaula 6 — "O integrador que não sabia parar"

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 6 — PID na prática: sintonia, métricas e anti-*windup*.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de descrever o contrato numérico do `DiscretePID`, obter o ganho crítico $K_u$ e o período crítico $T_u$ do NexaBot na malha discreta, aplicar Ziegler-Nichols e comparar sintonias por quatro métricas objetivas, e explicar — tendo visto acontecer e ser corrigido na mesma gravação — por que o *windup* do integrador exige uma correção explícita por *back-calculation*.

**Mapa de tempo e telas:** 00:00 terminal com o *windup* já em andamento · 01:40 editor: `nexabot/controllers.py`, o contrato do `DiscretePID` · 03:20 editor: por que o ganho crítico só aparece na malha discreta · 05:00 editor: métricas de aceitação e o mecanismo do *windup* · 06:40 editor: anti-*windup* por *back-calculation* · 08:30 terminal: `01_ganho_critico.py` · 10:30 terminal: `02_ziegler_nichols.py` e `03_ajuste_fino.py` · 12:30 terminal: `04_antiwindup.py`, o erro e a correção na mesma tomada · 16:30 aplicação profissional · 18:00 pontos-chave e atividade · 19:00 encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: terminal — aula_06/04_antiwindup.py, saída "SEM anti-windup" já na tela]**

A tela mostra, já em andamento, a primeira metade da saída de um script que vou rodar por completo daqui a pouco. Pede-se ao NexaBot uma velocidade de $4{,}0\,\mathrm{m/s}$ — $1\,600\,\mathrm{rad/s}$ no eixo do motor —, fisicamente impossível: o teto do motor em $24\,\mathrm{V}$ contínuos é de apenas $1{,}273\,\mathrm{m/s}$. O gráfico ASCII na tela mostra a tensão de comando colada no teto de $24\,\mathrm{V}$ por meio segundo inteiro, e a velocidade subindo até um patamar bem abaixo do que foi pedido, porque não existe tensão suficiente para chegar lá. Isso, sozinho, já seria apenas saturação — um limite físico sendo respeitado. O problema real aparece meio segundo depois, quando a referência cai para um valor perfeitamente alcançável, e o robô ainda assim demora quase dois segundos e meio para obedecer. Entender por que essa demora acontece, e como eliminá-la sem tocar no motor, é o assunto inteiro desta aula.

Esse cenário não é artificial. Um operador de armazém que digita uma velocidade de cruzeiro errada, um perfil de movimento mal calculado por um planejador de trajetória, ou simplesmente uma referência momentaneamente acima do que a bateria consegue sustentar sob carga — qualquer um desses casos reais entrega ao controlador exatamente o mesmo tipo de pedido inatingível que a tela está mostrando agora. A pergunta que interessa não é "isso pode acontecer": é "o que o controlador faz depois que isso acontece e a situação volta ao normal".

### Desenvolvimento conceitual

**[01:40–03:20 · TELA: editor — nexabot/controllers.py, o contrato do DiscretePID]**

Abro `nexabot/controllers.py`, o arquivo que vai acompanhar a disciplina até a Unidade 4. A classe `DiscretePID` implementa um contrato numérico exato, o mesmo que a Aula 7 vai justificar do ponto de vista de discretização, e que a Unidade 4 vai traduzir literalmente para C. O erro é $e[k]=r[k]-y[k]$. O termo integral se atualiza por $I[k]=I[k-1]+K_iT_se[k]$ — uma soma acumulada, Euler para trás. O termo derivativo passa por um filtro de primeira ordem, porque a derivada pura amplificaria o ruído de quantização do encoder que a Aula 7 mede em detalhe: $D[k]=\bigl(K_d(e[k]-e[k-1])+\tau_fD[k-1]\bigr)/(\tau_f+T_s)$. A soma dos três termos, $u_{ns}=K_pe[k]+I[k]+D[k]$, é saturada entre $-24$ e $24\,\mathrm{V}$ antes de ser aplicada. E, sempre que a saturação corta o comando, uma última linha entra em ação — a linha que resolve o problema desta aula, e que descrevo em detalhe daqui a pouco. Note que o estado inteiro do controlador cabe em duas variáveis, `integral` e `d_state`: decisivo para um microcontrolador de memória limitada, e uma das razões pelas quais essa estrutura, e não uma alternativa mais sofisticada, domina a indústria.

**[03:20–05:00 · TELA: editor — por que o ganho crítico só aparece na malha discreta]**

O método clássico de Ziegler-Nichols pede que se eleve o ganho proporcional puro, sem integral nem derivativo, até a malha entrar em oscilação sustentada — o ganho crítico $K_u$ — e que se meça o período dessa oscilação, o período crítico $T_u$. Aqui está um detalhe técnico que separa teoria de prática de verdade: o motor do NexaBot é uma planta de segunda ordem com dois polos reais, sem zero, e, em tempo contínuo, com realimentação proporcional pura, essa planta jamais entra em oscilação sustentada, para nenhum valor de ganho — o critério de Routh-Hurwitz para esse sistema é satisfeito para qualquer $K_p$ positivo. Ou seja, a receita clássica de Ziegler-Nichols simplesmente não teria onde "pegar" se a busca fosse feita na malha contínua ideal.

O que abre espaço para a oscilação é a discretização real do controlador embarcado, rodando a $T_s=5\,\mathrm{ms}$, duzentos hertz. Ao discretizar a planta por retenção de ordem zero nesse período, aparece um atraso de fase que a planta contínua nunca teve, e é esse atraso, e só ele, que permite ao ganho proporcional discreto cruzar o limite de estabilidade. A busca do ganho crítico desta aula, portanto, não é feita analiticamente sobre $G(s)$: é feita numericamente sobre a malha discreta de fato, e o valor encontrado reflete o mesmo controlador embarcado que vai rodar de verdade no NexaBot.

**[05:00–06:40 · TELA: editor — métricas de aceitação e o mecanismo do windup]**

Quatro métricas quantificam objetivamente uma sintonia. Sobressinal percentual mede o quanto a resposta ultrapassa a referência. Tempo de subida mede a rapidez entre dez e noventa por cento do valor final. Tempo de acomodação mede quanto tempo leva até a resposta entrar, e permanecer, dentro de uma faixa de dois por cento em torno do alvo. E o ISE, a integral do erro ao quadrado ao longo do tempo, penaliza tanto erro grande quanto erro prolongado — uma única sintonia pode ter sobressinal baixo e ainda assim ISE alto, se o erro persistir por muito tempo em módulo pequeno, então nenhuma dessas quatro métricas substitui as outras três.

Voltando à equação do termo integral, $I[k]=I[k-1]+K_iT_se[k]$: essa soma cresce enquanto o erro for diferente de zero, e a equação, isolada, não sabe nada sobre saturação. Peça ao NexaBot uma velocidade acima do que os $24\,\mathrm{V}$ sustentam, e o erro nunca vai a zero — o integrador cresce, indefinidamente, mesmo que a tensão calculada já ultrapasse, de muito, o que o driver consegue de fato entregar. Esse crescimento sem correspondência física é o *windup*: o nome vem exatamente da imagem de uma mola sendo enrolada além do que ela jamais vai poder liberar de uma vez.

O efeito só se manifesta quando a referência muda de novo. Enquanto ela permanece fixa e inatingível, o integrador cresce silenciosamente, sem nenhum sintoma visível na tensão de comando, que já está presa no teto de vinte e quatro volts de qualquer forma. É exatamente por isso que esse defeito costuma escapar de um teste rápido em bancada: só aparece no instante seguinte, quando a condição que o causou já passou, e o sistema deveria estar se comportando normalmente outra vez.

**[06:40–08:30 · TELA: editor — anti-windup por back-calculation]**

A correção que resolve isso, chamada *back-calculation*, mora na última linha do contrato que abri há pouco: sempre que a saída saturada $u[k]$ difere da saída calculada $u_{ns}$, o integrador recebe uma correção proporcional a essa diferença, $I[k]\leftarrow I[k]+K_{aw}(u[k]-u_{ns})T_s$. O nome descreve exatamente o mecanismo: em vez de impedir a priori que o integrador cresça, o cálculo normal acontece sem alteração, e a posteriori se recalcula quanto desse crescimento deveria ter sido descontado, porque a planta nunca recebeu o comando correspondente. Sem saturação, $u$ e $u_{ns}$ coincidem, a correção é zero, e o `DiscretePID` se comporta como um PID comum. Sob saturação, a correção reduz o integrador na exata proporção do comando que não pôde ser aplicado — nem mais, nem menos. É esse único termo, ativado apenas quando necessário, que a demonstração ao vivo desta aula vai ligar e desligar diante dos seus olhos, na mesma referência inalcançável que abriu a aula.

### Demonstração ao vivo

**[08:30–10:30 · TELA: terminal — aula_06/01_ganho_critico.py]**

Rodo o script que localiza o ganho crítico na malha discreta real:

```
.venv/bin/python aula_06/01_ganho_critico.py
```

O script discretiza a planta por retenção de ordem zero em $T_s=5\,\mathrm{ms}$ e varia o ganho proporcional discreto por bisseção, até o maior polo de malha fechada tocar exatamente o círculo unitário. A tabela na tela confirma: ganho crítico $K_u=3{,}6911$, com o polo dominante em $-0{,}1432+0{,}9897j$, correspondendo a um período crítico $T_u=18{,}324\,\mathrm{ms}$. Logo abaixo, a simulação da malha fechada exatamente nesse ganho, com proporcional puro, mostra a oscilação sustentada prometida pela definição do método: a amplitude pico a pico da velocidade fica em $11{,}40\,\mathrm{rad/s}$ na primeira metade do regime observado e $11{,}35\,\mathrm{rad/s}$ na segunda — praticamente idêntica, o que confirma que a oscilação nem cresce nem decai, exatamente a assinatura do limite de estabilidade que o método pede para ser identificado.

**[10:30–12:30 · TELA: terminal — aula_06/02_ziegler_nichols.py e aula_06/03_ajuste_fino.py]**

Com $K_u$ e $T_u$ em mãos, aplico a fórmula clássica de Ziegler-Nichols e comparo com um ajuste manual. Rodo os dois scripts em sequência:

```
.venv/bin/python aula_06/02_ziegler_nichols.py
.venv/bin/python aula_06/03_ajuste_fino.py
```

O primeiro entrega a sintonia clássica: $K_p=2{,}2147$, $K_i=241{,}7223$, $K_d=0{,}005073$. Simulando um degrau de $400\,\mathrm{rad/s}$, essa sintonia produz sobressinal de $24{,}84\%$, tempo de subida de $159$ milissegundos e tempo de acomodação de $633{,}5$ milissegundos, com a tensão de comando saturada em $24\,\mathrm{V}$ durante boa parte do transitório. O segundo script compara essa sintonia clássica com a variante "sem sobressinal" de Ziegler-Nichols e com um ajuste manual, $K_p=1{,}3$, $K_i=15$, $K_d=0{,}01$. A tabela final mostra algo que não é óbvio antes de medir: as duas sintonias de Ziegler-Nichols têm praticamente o mesmo tempo de subida, cento e cinquenta e nove milissegundos, porque o erro inicial já satura o atuador em vinte e quatro volts para qualquer uma delas — é a física do motor saturado, não o valor exato dos ganhos, que domina essa fase inicial. A diferença aparece depois: o ajuste manual reduz o sobressinal para $22{,}77\%$ e, mais relevante, entrega o menor ISE dos três, $9\,469{,}5$, contra $9\,926{,}5$ da sintonia clássica e $9\,933{,}2$ da variante sem sobressinal — ao custo de um tempo de acomodação um pouco maior, $669$ milissegundos. Para um AGV que carrega paletes, sobressinal e ISE menores pesam mais do que alguns milissegundos extras de acomodação, porque um sobressinal de velocidade é o que realmente arrisca deslocar a carga sobre a plataforma.

**[12:30–16:30 · TELA: terminal — aula_06/04_antiwindup.py, o erro e a correção na mesma tomada]**

Chega o momento mais importante desta unidade. Rodo o script inteiro, do início ao fim, sem interrupção:

```
.venv/bin/python aula_06/04_antiwindup.py
```

O cenário usa a sintonia manual que acabei de validar, $K_p=1{,}3$, $K_i=15$, $K_d=0{,}01$. Na primeira meia hora simulada de zero a meio segundo, a referência é a mesma velocidade irreal de $4{,}0\,\mathrm{m/s}$ que abriu esta videoaula; em $t=0{,}5\,\mathrm{s}$, ela cai para $0{,}5\,\mathrm{m/s}$ — segura e plenamente alcançável. A tela mostra primeiro o caso sem nenhuma correção, com ganho de anti-*windup* $K_{aw}=0{,}0$: a tensão fica colada em $24\,\mathrm{V}$ durante toda a primeira fase, a velocidade sobe até um teto físico de cerca de $509\,\mathrm{rad/s}$, e, quando a referência cai, o integrador está em $9\,251{,}6$ — um número que não tem mais nenhuma relação com o que a planta pode receber. A velocidade demora $2\,256{,}5$ milissegundos para voltar e permanecer dentro da faixa de dois por cento do novo alvo.

Sem cortar a gravação, a segunda metade da mesma execução mostra o caso com anti-*windup* ligado, $K_{aw}=2{,}0$, sob exatamente a mesma referência. O pico de velocidade na primeira fase é praticamente idêntico, cerca de $509\,\mathrm{rad/s}$ também — isso não é efeito do anti-*windup*, é simplesmente o teto físico do motor em tensão máxima, herdado da própria fase irreal, e nenhuma correção de integrador muda onde a velocidade já estava no instante da troca de referência. O que muda de verdade é a velocidade de recuperação: no instante da comutação, o integrador está em $4\,668{,}2$, praticamente metade do valor anterior, e a velocidade volta à faixa de dois por cento em $872{,}5$ milissegundos — cerca de dois vírgula seis vezes mais rápido do que sem a correção. Mesma sintonia, mesma referência, mesma tomada: a única diferença entre um robô que demora mais de dois segundos para obedecer a uma ordem de desaceleração e um robô que obedece em menos de um segundo é uma única linha de código, ativada apenas quando o atuador satura.

### Aplicação profissional

**[16:30–18:00 · TELA: terminal — mesma tela do anti-windup, aplicação profissional]**

Para um AGV de armazém que compartilha corredor com pessoas, essa diferença entre dois segundos e vinte e cinco centésimos e menos de um segundo não é apenas uma questão de qualidade de controle: é diretamente relevante para os requisitos de segurança do NexaBot, o mesmo tipo de exigência que a Unidade 3 vai formalizar e verificar. Um robô que demora tempo demais para desacelerar depois que uma ordem de parada é dada, porque o integrador está "carregado" de um transitório anterior, é um risco físico real, não uma imperfeição estética do gráfico.

*Windup* de integrador não é peculiaridade do NexaBot. Qualquer atuador físico satura — válvulas industriais, motores de tração automotiva, superfícies de controle de aeronaves — e qualquer controlador com ação integral, rodando contra esse atuador, herda o mesmo problema se não for corrigido. Sistemas de piloto automático de aeronaves clássicos sofreram, historicamente, do mesmo efeito ao trocar de modo de voo com o comando de profundor saturado; controladores industriais de processo, em refinarias e plantas químicas, adotam variantes do mesmo *back-calculation* para evitar que uma válvula travada por horas produza um transitório violento assim que ela volta a responder. O mecanismo que acabei de demonstrar em código Python de algumas linhas é, em essência, o mesmo que protege sistemas de missão muito mais crítica do que um AGV de armazém.

Um detalhe profissional que vale registrar: nenhuma dessas indústrias trata anti-*windup* como um recurso opcional de sintonia fina, a ser adicionado depois que o resto do controlador já está funcionando. Ele entra na especificação do controlador desde o primeiro dia, junto com o próprio limite de atuação, exatamente como esta aula tratou os dois assuntos juntos, e não em sequência separada. Um controlador sem anti-*windup*, testado apenas com referências alcançáveis, pode passar em todos os testes de bancada e ainda assim falhar de forma severa no primeiro dia de operação real, quando alguém — pessoa ou algoritmo de planejamento — pedir, uma única vez, algo que o atuador não consegue entregar.

### Fechamento

**[18:00–19:00 · TELA: editor — síntese e atividade prática]**

Recapitulando. O contrato do `DiscretePID` combina proporcional, integral por Euler para trás e derivativo filtrado, com saturação e anti-*windup* explícitos — o mesmo contrato que a Unidade 4 vai traduzir literalmente para C. O ganho crítico do NexaBot só aparece na malha discreta real, $K_u\approx3{,}6911$ e $T_u\approx18{,}324\,\mathrm{ms}$, porque a planta contínua jamais oscilaria sob proporcional puro. Sobressinal, tempo de subida, tempo de acomodação e ISE, juntos, decidem qual sintonia é a mais adequada — e, para o NexaBot, o ajuste manual venceu por ter o menor ISE e o menor sobressinal, apesar de acomodar um pouco mais devagar. E o *windup* do integrador, visto acontecer e ser corrigido na mesma gravação, reduziu o tempo de recuperação em cerca de dois vírgula seis vezes com uma única linha de correção.

A atividade prática desta aula pede o seguinte: repita a demonstração de `aula_06/04_antiwindup.py` alterando apenas o ganho de anti-*windup* para $K_{aw}=0{,}5$ e depois para $K_{aw}=5{,}0$, registre o tempo de recuperação em cada caso e explique, com base no que muda no integrador, por que um ganho de anti-*windup* muito alto também não é automaticamente a melhor escolha.

**[19:00–20:00 · TELA: terminal — encerramento]**

Esta aula projetou e sintonizou o controlador PID do NexaBot, e mostrou, na prática, por que tratar saturação e *windup* é parte do projeto, não uma correção de última hora. Todo o trabalho de hoje ainda rodou sobre uma planta amostrada de forma idealizada. A próxima aula discretiza essa mesma malha de verdade, justifica numericamente por que o período de amostragem de cinco milissegundos foi escolhido, e mostra exatamente o ponto em que economizar ciclos de processamento deixa de ser uma otimização segura e passa a comprometer a estabilidade. Até lá.

### Indicações de edição e recursos visuais

- Inserir Recurso visual 4 da unidade — velocidade oscilando sob $K_p=K_u=3{,}691$ com $T_u$ marcado entre dois picos — sobreposto ao terminal, aproximadamente em 09:30.
- Inserir Recurso visual 6 da unidade — diagrama do PID discreto com o ramo de anti-*windup* realimentando $(u-u_{ns})\times K_{aw}$ ao integrador — sobreposto ao editor, aproximadamente em 07:30.
- 12:30–16:30 — este é o trecho mais importante da aula: não cortar a gravação entre as duas metades do script; destacar com caixa vermelha o integrador em $9\,251{,}6$ (sem correção) e com caixa verde o integrador em $4\,668{,}2$ (com correção), no instante exato da troca de referência.
- Inserir Recurso visual 7 da unidade — curva do integrador subindo sem limite e curva do integrador contido, lado a lado — sobreposto ao terminal, aproximadamente em 14:30.
- 19:40–20:00 — vinheta de encerramento com chamada para a Videoaula 7.

### Fontes e links de mídia

- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011 — referência conceitual, sem reprodução de trecho externo.
- ÅSTRÖM, Karl Johan; RUNDQWIST, Lars. Integrator windup and how to avoid it. In: AMERICAN CONTROL CONFERENCE, 1989, Pittsburgh. *Proceedings [...]*. Pittsburgh: IEEE, 1989. p. 1693-1698. DOI: 10.23919/ACC.1989.4790464 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas e gráficos devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 6 (`unidade_2.md`) e da saída real dos scripts de `projeto_nexabot/aula_06/`.

---

## Roteiro da Videoaula 7 — "Trinta amostras por constante de tempo: de onde vem esse número"

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 7 — Discretização e escolha do período de amostragem.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de distinguir Euler para frente, Euler para trás, Tustin e retenção de ordem zero como métodos de discretização, justificar numericamente a escolha de $T_s$ a partir das constantes de tempo do NexaBot, quantificar o custo de um atraso computacional de um ciclo em margem de fase, e explicar por que a resolução do encoder domina o desempenho da malha mais do que a resolução do PWM.

**Mapa de tempo e telas:** 00:00 terminal já com a proposta arriscada na tela · 01:40 editor: Euler, Tustin e ZOH, e por que o `DiscretePID` usa Euler para trás · 03:10 editor: escolha de $T_s$ a partir de $\tau_m$ · 04:40 editor: atraso computacional e margem de fase · 06:10 editor: quantização de encoder e de PWM · 07:30 terminal: `01_euler_tustin_zoh.py` · 09:30 terminal: `02_escolha_de_ts.py` · 11:30 terminal: `03_atraso_computacional.py` · 13:30 terminal: `04_quantizacao.py` · 15:00 terminal: `05_desafio.py` · 16:30 aplicação profissional · 18:00 pausa para reflexão, contagem regressiva · 18:40 pontos-chave e atividade · 19:30 encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: editor — aula_07/02_escolha_de_ts.py, tabela de varredura já na tela]**

O editor já mostra, na tela, a tabela que o script `02_escolha_de_ts.py` produz ao rodar: dezoito valores de período de amostragem, de meio milissegundo a cem milissegundos, cada um classificado como bom desempenho, degradado ou instável. Um colega de firmware propôs, na semana passada, liberar tempo de processamento para outras tarefas — leitura de sensores de segurança, telemetria — aumentando o período de amostragem do laço de velocidade do NexaBot, hoje em cinco milissegundos, para algo bem maior. O argumento era razoável à primeira vista: "a malha funcionou bem nas simulações contínuas da aula passada, alguns milissegundos a mais não deveriam fazer diferença." A tabela na tela já adianta que esse argumento tem um limite exato, e que ultrapassá-lo não é uma questão de desempenho um pouco pior — é uma questão de a malha simplesmente parar de funcionar.

### Desenvolvimento conceitual

**[01:40–03:10 · TELA: editor — Euler, Tustin e retenção de ordem zero]**

Três formas de transformar uma equação diferencial contínua num mapa discreto aparecem nesta aula, cada uma com um uso técnico específico. O método de Euler para frente aproxima a derivada por $(x[k+1]-x[k])/T_s$: simples, mas com menos margem de estabilidade herdada. O Euler para trás usa $(x[k]-x[k-1])/T_s$ — é exatamente essa forma que o `DiscretePID`, já apresentado na Aula 6, adota para o termo integral, porque ela dispensa valor futuro e mantém estabilidade numérica sem exigir histórico adicional. A transformação de Tustin, ou bilinear, $s\approx(2/T_s)\,(z-1)/(z+1)$, preserva melhor a resposta em frequência, ao custo de distorcer frequências próximas à metade da taxa de amostragem. E a retenção de ordem zero, o ZOH, modela a planta assumindo que a tensão de comando fica constante entre amostras — exatamente como um PWM digital de fato se comporta na prática. Por isso, quando esta aula discretiza a planta contínua do NexaBot para analisar a malha fechada, o método usado é especificamente o ZOH: o objetivo não é aproximar a planta da forma matematicamente mais elegante, é reproduzir exatamente o que a eletrônica de potência realmente faz entre um instante de amostragem e o seguinte. O controlador, por ser código executado pelo microcontrolador e não um circuito com retenção física, é livre para adotar a regra mais conveniente de implementar — daí o Euler para trás do `DiscretePID`.

**[03:10–04:40 · TELA: editor — escolha de Ts a partir das constantes de tempo]**

A escolha do período de amostragem parte das escalas de tempo estabelecidas na Unidade 1. O polo lento do modelo acoplado fornece cento e trinta e oito vírgula seis milissegundos; a aproximação mecânica desacoplada fornece cento e quarenta e oito vírgula um. A literatura de controle digital usa, como faixa inicial, dez a trinta amostras por constante dominante, sempre com confirmação na malha real. Com $T_s=5\,\mathrm{ms}$, temos vinte e sete vírgula sete amostras pelo valor modal exato ou vinte e nove vírgula seis pela aproximação. Os dois caminhos colocam cinco milissegundos dentro da faixa; a varredura que faremos é a evidência final.

**[04:40–06:10 · TELA: editor — atraso computacional e margem de fase]**

Um segundo custo, além da distorção de frequência já mencionada, aparece em qualquer implementação real: o tempo entre ler o sensor e efetivamente atualizar a tensão de comando nunca é zero. Um ciclo inteiro de atraso computacional se comporta, no modelo linear da malha, como um atraso de transporte $e^{-sT_s}$ — um bloco extra que não muda o módulo de nenhuma frequência, mas subtrai fase em todas elas, e subtrai mais fase quanto maior for $\omega$ multiplicado por $T_s$. Na prática, isso significa que o mesmo atraso de um ciclo custa pouca margem de fase quando $T_s$ é pequeno, e custa muita margem quando $T_s$ é grande — porque a fase perdida cresce proporcionalmente ao próprio período de amostragem, não é uma penalidade fixa em graus. Esse é exatamente o efeito que a demonstração desta aula vai medir e confirmar contra a previsão analítica.

**[06:10–07:30 · TELA: editor — quantização de encoder e de PWM]**

Um terceiro efeito, independente dos dois anteriores, vem da resolução finita dos sensores e atuadores digitais. O encoder mede posição em pulsos inteiros, e a velocidade estimada por diferença entre amostras sucessivas herda essa granularidade — quanto menor $T_s$, ou quanto menor a resolução do encoder, mais ruidosa essa estimativa fica, o que significa que reduzir $T_s$ para ganhar margem de estabilidade tem um custo colateral que a análise puramente linear das seções anteriores não captura. O PWM, por sua vez, é quantizado tipicamente entre dez e doze bits entre zero e a tensão máxima; a resolução resultante, de dezenas de milivolts, costuma ser desprezível, mas deixa de ser irrelevante em malhas de ganho muito alto. Escolher $T_s$ é, portanto, equilibrar três efeitos simultâneos — margem de fase, atraso computacional e ruído de quantização — e não apenas o primeiro deles isoladamente, como a demonstração de hoje vai mostrar em números.

### Demonstração ao vivo

**[07:30–09:30 · TELA: terminal — aula_07/01_euler_tustin_zoh.py]**

Rodo a comparação entre os três métodos de discretização:

```
.venv/bin/python aula_07/01_euler_tustin_zoh.py
```

A um degrau de doze volts, discretizado a cinco milissegundos, a tela mostra: Euler para frente com erro RMS de $1{,}0858\,\mathrm{rad/s}$ e erro final de $0{,}0820\,\mathrm{rad/s}$, ou $0{,}0323\%$; Tustin com erro RMS de $1{,}3234\,\mathrm{rad/s}$ e erro final de apenas $0{,}0149\,\mathrm{rad/s}$, $0{,}0059\%$; e o ZOH com erro RMS da ordem de $10^{-9}\,\mathrm{rad/s}$ e erro final da ordem de $10^{-13}$ — ruído numérico, essencialmente exato. O ponto que a tela destaca é sutil e vale registrar com cuidado: o ZOH é exato aqui porque a hipótese dele — tensão mantida constante entre amostras — é literalmente como o driver do NexaBot aplica a tensão; Tustin acerta melhor o valor final porque a transformação bilinear preserva exatamente o ganho em corrente contínua; mas o erro RMS do transitório inteiro é, neste caso específico, um pouco menor no Euler do que no Tustin. A lição não é que um método seja sempre melhor que o outro — é que a métrica certa depende do que importa para o problema em questão.

**[09:30–11:30 · TELA: terminal — aula_07/02_escolha_de_ts.py]**

Rodo agora a varredura completa de período de amostragem, com um PID fixo, moderado — $K_p=0{,}5$, $K_i=5{,}0$, $K_d=0{,}0005$ — contra um degrau de $50\,\mathrm{rad/s}$:

```
.venv/bin/python aula_07/02_escolha_de_ts.py
```

A tabela que já estava parcialmente na tela na abertura desta aula agora aparece completa: bom desempenho até aproximadamente $T_s=8{,}26\,\mathrm{ms}$, com sobressinal ainda abaixo de dez por cento; degradação perceptível a partir de $T_s\approx11{,}29\,\mathrm{ms}$, com sobressinal subindo rapidamente até passar de cento e setenta por cento em cinquenta milissegundos; e instabilidade — a amplitude ultrapassando três vezes a referência — a partir de $T_s\approx44{,}34\,\mathrm{ms}$, fronteira que o script refina por bisseção. O período nominal do firmware do NexaBot, cinco milissegundos, fica bem dentro da faixa de bom desempenho, com folga considerável até o limiar de degradação.

**[11:30–13:30 · TELA: terminal — aula_07/03_atraso_computacional.py]**

Rodo o script que isola o efeito de um único ciclo de atraso computacional:

```
.venv/bin/python aula_07/03_atraso_computacional.py
```

A tela mostra duas colunas de margem de fase, com e sem um atraso extra de um ciclo, para dois períodos de amostragem. Em $T_s=5\,\mathrm{ms}$, a margem sem atraso é de $66{,}19$ graus, e cai para $43{,}61$ graus com o atraso — uma perda de $22{,}58$ graus, que a própria tabela confirma bater exatamente com a previsão teórica $\omega_{gc}\cdot T_s$: a malha permanece estável. Em $T_s=20\,\mathrm{ms}$, a margem sem atraso já é mais estreita, $32{,}51$ graus, e o mesmo atraso de um ciclo agora custa $96{,}37$ graus — muito mais, porque a fase perdida por amostra de atraso é proporcional ao próprio $T_s$ — derrubando a margem para $-63{,}86$ graus: instável. A simulação temporal, logo abaixo na mesma tela, confirma essa previsão analítica sem margem para dúvida: em vinte milissegundos com o atraso de um ciclo, a velocidade angular satura e diverge, chegando a mais de cento e cinquenta radianos por segundo para uma referência de apenas cinquenta.

**[13:30–15:00 · TELA: terminal — aula_07/04_quantizacao.py]**

Rodo o script que isola o efeito da resolução do encoder e do PWM:

```
.venv/bin/python aula_07/04_quantizacao.py
```

A primeira tabela isola o encoder, com PWM ideal: com cento e vinte e oito pulsos por volta, o sobressinal sobe para $12{,}45\%$, o erro em regime chega a $0{,}7021\,\mathrm{rad/s}$, e o desvio padrão do chattering da tensão de comando é de $1{,}5681\,\mathrm{V}$; com dois mil e quarenta e oito pulsos por volta, esses três números caem para valores próximos do caso ideal. A segunda tabela isola o PWM, com encoder ideal: mesmo com apenas oito bits de resolução — um passo de tensão de quase dezenove centésimos de volt — o chattering de comando fica em $0{,}0927\,\mathrm{V}$, quase dezessete vezes menor do que o chattering causado pelo encoder grosseiro. O ruído de quantização do sensor entra direto na malha de realimentação, afetando os termos proporcional e integral a cada ciclo; o degrau de quantização do atuador é filtrado pela própria inércia mecânica da planta, com sua constante de tempo de cento e quarenta e oito milissegundos, muito maior que o período de amostragem. Entre os dois, é o encoder que domina o desempenho desta malha.

**[15:00–16:30 · TELA: terminal — aula_07/05_desafio.py]**

Fecho a demonstração com o desafio, que amarra os três efeitos anteriores num único veredito de aprovação. Rodo:

```
.venv/bin/python aula_07/05_desafio.py
```

O enunciado pede que, dado um PID fixo e um período de amostragem candidato, o script decida se a malha é estável e se atende um sobressinal máximo de vinte por cento. Com a implementação de referência, para $T_s=5\,\mathrm{ms}$ o veredito é estável e aprovado, com sobressinal entre dois e cinco por cento; para $T_s=20\,\mathrm{ms}$, a malha continua estável, mas o sobressinal sobe para entre vinte e cinco e trinta e cinco por cento, reprovando; e para $T_s=50\,\mathrm{ms}$, a malha simplesmente diverge, reprovada independentemente de qualquer outro número. Um único critério de engenharia, aplicado de forma automática, já teria barrado a proposta que abriu esta videoaula antes mesmo de qualquer teste em bancada.

### Aplicação profissional

**[16:30–18:00 · TELA: editor — aplicação profissional: escolha de Ts em produtos reais]**

A escolha do período de amostragem raramente é revisitada depois que um produto embarcado entra em produção — e é exatamente por isso que ela precisa ser certa desde o início, com margem verificada, não apenas testada uma vez em condições ideais de bancada. Controladores de motores em veículos elétricos, sistemas de estabilização de drones e controladores de processo industrial compartilham exatamente essa mesma tensão de três frentes: aumentar $T_s$ libera ciclos de CPU para outras tarefas, mas reduz margem de fase, amplia o custo de qualquer atraso computacional adicional, e às vezes até piora — nunca melhora — a estimativa de velocidade por diferenciação de posição. A prática de engenharia que sustenta essa decisão é sempre a mesma que esta aula acabou de demonstrar: uma varredura numérica da malha real, e não uma regra de bolso aplicada sem verificação.

Vale também uma nota sobre o que esta aula deliberadamente não fez: os ganhos usados na varredura de período de amostragem não foram os de Ziegler-Nichols clássico da Aula 6, e sim um PID mais moderado. A razão é honesta e vale registrar: testando os ganhos clássicos neste mesmo degrau, o termo integral, muito mais agressivo, satura o atuador com sobressinal de sessenta a noventa por cento já em períodos de amostragem pequenos, o que mascararia justamente o efeito de $T_s$ que esta aula pretende isolar. Escolher o cenário certo para uma medição, sem esconder essa escolha do leitor, também é parte do ofício.

### Pausa para reflexão

**[18:00–18:30 · TELA: terminal — pausa para reflexão]**

Antes de fechar, pause a gravação e reflita sobre quatro perguntas. Primeira: a varredura desta aula tratou cada período de amostragem como um valor fixo e exato — mas um microcontrolador real não executa cada ciclo em exatamente cinco milissegundos; interrupções concorrentes e comunicação com outros subsistemas produzem *jitter*, uma variação ciclo a ciclo do período efetivo. Se esse *jitter* levar, ocasionalmente, um ciclo a durar oito ou dez milissegundos, a malha do NexaBot ainda está longe da fronteira de instabilidade medida hoje? Segunda: e se um pico de carga de processamento atrasar um único ciclo isolado para vinte milissegundos, isso é um evento raro e inofensivo, ou evidência de que a margem calculada em regime permanente não descreve o pior caso que o sistema pode enfrentar em campo? Terceira: qual dos três efeitos desta aula — distorção de discretização, atraso computacional, ou quantização de sensor — você reduziria primeiro, se pudesse escolher apenas um, sabendo que o encoder já domina sobre o PWM? Quarta: essa mesma pergunta sobre pior caso, e não apenas comportamento típico, vai reaparecer, formalizada com rigor matemático, já na Unidade 3.

**[18:30–18:40 · TELA: terminal — contagem regressiva]**

*[indicação de edição: inserir tela de pausa com contagem regressiva de 10 segundos e o texto "Pense e continue"]*

**[18:40–19:30 · TELA: editor — pontos-chave e atividade prática]**

Recapitulando os pontos-chave desta aula. Euler para frente, Euler para trás e Tustin discretizam de formas diferentes; o ZOH modela especificamente o que um atuador de tensão constante entre amostras realmente faz, e é por isso que a análise da malha fechada desta aula o usa. O período de cinco milissegundos do NexaBot dá cerca de vinte e nove vírgula seis amostras por constante de tempo mecânica, dentro da faixa recomendada de dez a trinta. A malha, com o PID moderado usado nesta aula, permanece com bom desempenho até cerca de oito vírgula vinte e seis milissegundos, degrada progressivamente depois disso, e se torna instável a partir de aproximadamente quarenta e quatro vírgula trinta e quatro milissegundos. Um único ciclo de atraso computacional custa mais margem de fase quanto maior for o período de amostragem, porque essa perda é proporcional a $\omega_{gc}\cdot T_s$, não uma penalidade fixa. E, entre encoder e PWM, é o encoder que domina o desempenho da malha, porque seu ruído de quantização entra direto na realimentação.

A atividade prática pede o seguinte: usando `aula_07/05_desafio.py` como base, repita a verificação de aprovação para o PID sintonizado manualmente na Aula 6, $K_p=1{,}3$, $K_i=15$, $K_d=0{,}01$, nos mesmos três períodos de amostragem, e reporte se o veredito de aprovação muda em relação ao PID moderado usado nesta aula — e, se mudar, explique por que um controlador mais agressivo tolera menos folga de período de amostragem.

**[19:30–20:00 · TELA: terminal — encerramento]**

Esta aula fechou o contrato numérico do `DiscretePID` e justificou, com uma varredura real, o período de amostragem que sustenta toda a malha do NexaBot. A próxima aula acopla essa mesma planta, agora compilada como componente independente em C, ao controlador Python por co-simulação FMI, e mede exatamente o preço de espaçar a comunicação entre os dois — um problema estruturalmente parecido com o que acabamos de ver hoje, mas em outra camada da arquitetura. Até lá.

### Indicações de edição e recursos visuais

- Inserir Recurso visual 8 da unidade — respostas ao degrau de Euler para frente, Euler para trás e Tustin sobrepostas — sobreposto ao editor, aproximadamente em 02:30.
- Inserir Recurso visual 9 da unidade — maior módulo de polo em função de $T_s$, cruzando o limite de instabilidade perto de $44{,}3\,\mathrm{ms}$ — em tela cheia, aproximadamente em 10:00.
- 11:30–13:30 — congelar a tabela de margem de fase com zoom nas duas linhas ($T_s=5$ e $T_s=20\,\mathrm{ms}$), destacando a coluna de perda em graus.
- Inserir Recurso visual 10 da unidade — linha do tempo de um ciclo de controle real, leitura, cálculo e atuação — sobreposto ao editor, aproximadamente em 05:30.
- 18:00–18:40 — tela de pausa com contagem regressiva de 10 segundos, texto "Pense e continue", sem áudio de fundo.
- 19:40–20:00 — vinheta de encerramento com chamada para a Videoaula 8.

### Fontes e links de mídia

- FRANKLIN, Gene F.; POWELL, J. David; WORKMAN, Michael L. *Digital Control of Dynamic Systems*. 3. ed. Menlo Park: Addison-Wesley, 1997 — referência conceitual, sem reprodução de trecho externo.
- WESCOTT, Tim. PID without a PhD. *Embedded Systems Programming*, [s. l.], out. 2000 — referência conceitual, sem reprodução de trecho externo.
- OGATA, Katsuhiko. *Engenharia de controle moderno*. 5. ed. São Paulo: Pearson, 2011 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas e tabelas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 7 (`unidade_2.md`) e da saída real dos scripts de `projeto_nexabot/aula_07/`.

---

## Roteiro da Videoaula 8 — "Dois relógios, um só resultado: o preço de espaçar a comunicação"

**Vínculo com o plano de aprendizagem:** Unidade 2, Aula 8 — Co-simulação planta-controlador com FMI 3.0.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar por que planta e controlador são simulados por integradores independentes, descrever a estrutura de um FMU de co-simulação FMI 3.0, verificar um FMU isoladamente contra a implementação de referência antes de atribuir qualquer erro ao acoplamento, e quantificar como o erro de acoplamento cresce com o passo de comunicação.

**Mapa de tempo e telas:** 00:00 terminal com a co-simulação básica convergindo · 01:40 editor: `nexabot/fmu/plant_fmu.c` e o `modelDescription.xml` · 03:10 editor: `nexabot/cosim.py`, o mestre de co-simulação e o acoplamento Jacobi · 04:40 editor: erro de acoplamento e sua relação com $T_s$ · 06:00 editor: ligação com o `DiscretePID` e a Unidade 4 · 07:20 terminal: `01_build_fmu.py` · 09:00 terminal: `02_inspecta_fmu.py` · 10:20 terminal: `verify_fmu.py` · 11:40 terminal: `03_cosim_basica.py` · 13:20 terminal: `04_erro_de_acoplamento.py` · 15:20 aplicação profissional · 16:50 pontos-chave e desafio · 18:00 transição para a Unidade 3 e encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: terminal — aula_08/03_cosim_basica.py, tabela de convergência já na tela]**

A tela mostra uma tabela já em execução: tempo, referência, velocidade medida e tensão de comando, coluna a coluna, avançando em passos de cinquenta milissegundos. A velocidade converge suavemente para exatamente $1{,}0000\,\mathrm{m/s}$, e a tensão de comando se estabiliza em $18{,}8533\,\mathrm{V}$ — o mesmo valor de regime permanente que a Unidade 1 já havia calculado analiticamente para essa velocidade de cruzeiro. O que essa tabela não mostra, à primeira vista, é que ela vem de dois programas completamente separados conversando entre si: a planta do NexaBot, compilada como uma biblioteca C independente, e o controlador PID, ainda em Python, trocando dados a cada cinco milissegundos através de um padrão aberto chamado FMI. Um integrante da equipe de firmware sugeriu, na reunião passada, espaçar essa troca para cinquenta milissegundos em vez de cinco, para reduzir a sobrecarga de comunicação, argumentando que o prejuízo seria pequeno. Esta aula mede esse prejuízo, em vez de presumir que ele é pequeno.

Note a semelhança estrutural com as duas aulas anteriores desta unidade: primeiro projetamos um controlador, depois discretizamos essa malha e justificamos o período de amostragem com números, e agora, nesta aula final da unidade, colocamos essa mesma malha inteira dentro de uma segunda camada de amostragem — o passo de comunicação entre dois programas independentes. É a mesma pergunta de fundo, "quanto tempo entre atualizações ainda é seguro", aplicada a uma nova camada da arquitetura.

### Desenvolvimento conceitual

**[01:40–03:10 · TELA: editor — nexabot/fmu/plant_fmu.c e modelDescription.xml]**

Abro `nexabot/fmu/plant_fmu.c`: a mesma planta do motor CC de tração do NexaBot, com as mesmas equações e os mesmos parâmetros de `nexabot/plant.py`, agora escrita do zero em C nativo. O arquivo implementa as funções da interface FMI 3.0 realmente usadas — instanciar, entrar e sair do modo de inicialização, avançar um passo de simulação, ler e escrever variáveis — além de dezenas de funções obrigatórias de interfaces que este FMU não usa, mas que precisam existir como esboços honestos para que qualquer ferramenta compatível com FMI consiga carregar o arquivo sem erro. Ao lado, `modelDescription.xml` declara as cinco variáveis do modelo: tempo, como variável independente; tensão de armadura e torque de carga, como entradas; velocidade angular e corrente, como saídas. Essa descrição em XML é a fonte de verdade das referências de valor que qualquer ferramenta usa para ler e escrever no modelo — não é gerada dinamicamente, é parte do pacote.

**[03:10–04:40 · TELA: editor — nexabot/cosim.py, o mestre de co-simulação e o acoplamento Jacobi]**

Passo para `nexabot/cosim.py`, o mestre de co-simulação que orquestra os dois lados. A cada passo de comunicação $H$, o mestre lê a saída mais recente da planta — a velocidade angular —, calcula a lei de controle em Python usando o mesmo `DiscretePID` que já apareceu nas duas aulas anteriores, escreve a nova tensão de volta no FMU, e então chama a função de avanço de tempo do FMU, `doStep`, para avançar exatamente $H$ segundos. Entre um ponto de comunicação e o seguinte, cada lado mantém a última entrada recebida constante — uma retenção de ordem zero imposta pelo próprio protocolo de co-simulação, distinta da retenção de ordem zero do atuador físico que a Aula 7 já discutiu, mas de efeito qualitativamente análogo. Essa disciplina, em que os dois modelos avançam usando apenas os valores trocados no início de cada intervalo $H$, tem nome técnico: acoplamento Jacobi. Alternativas mais elaboradas, como acoplamento Gauss-Seidel ou passo de comunicação adaptativo, reduzem o erro resultante sem exigir reduzir $H$ uniformemente — mas ficam fora do escopo desta aula, e valem como próximo passo para quem quiser aprofundar o tema.

**[04:40–06:00 · TELA: editor — erro de acoplamento e sua relação com Ts]**

O ponto conceitual central desta aula é o seguinte: quanto maior $H$, mais desatualizada fica a informação que cada lado usa para decidir o que fazer — a planta continua recebendo a mesma tensão antiga por mais tempo, e o controlador só percebe o efeito dessa tensão quando o próximo ponto de comunicação chega. Esse é exatamente o mesmo tipo de efeito que a Aula 7 mediu para o período de amostragem do controlador embarcado: aumentar o intervalo entre atualizações degrada, primeiro, a fidelidade do transitório, e, além de um certo limiar, compromete a própria estabilidade da malha. A diferença é que, aqui, $H$ não é apenas o período de amostragem do controlador — é também o intervalo em que a planta em C fica sem saber que a tensão mudou. Os dois efeitos se somam na mesma variável.

Vale marcar por que essa distinção importa na prática: numa implementação Python direta, sem FMI, o único período relevante é o $T_s$ do `DiscretePID`, porque a planta é apenas uma função chamada dentro do mesmo processo, sem retenção adicional alguma. A partir do momento em que a planta vira um FMU externo, coordenado por um mestre de co-simulação, o passo de comunicação $H$ se torna um segundo parâmetro de projeto, independente de $T_s$ em princípio, mas que, na prática desta disciplina, quase sempre é escolhido igual a $T_s$ — e é justamente por isso que aumentar $H$ sem cuidado equivale, na prática, a aumentar o período de amostragem de todo o sistema, com as mesmas consequências que a Aula 7 já mediu.

**[06:00–07:20 · TELA: editor — ligação com o DiscretePID e a Unidade 4]**

O controlador usado nesta co-simulação já é o mesmo `DiscretePID`, com o contrato numérico fechado na Aula 7 — nenhuma equação nova aparece aqui. O que muda, de fato, é o lado da planta: em vez de uma função Python chamada diretamente, ela agora é um binário C, carregado por uma interface padronizada, exatamente como aconteceria se a planta tivesse sido desenvolvida por outra equipe, em outra ferramenta, sem acesso ao código-fonte original. Na Unidade 4, é o controlador que vai deixar de ser Python e passar a ser C gerado automaticamente a partir do mesmo modelo — mas os limites de $H$ que esta aula está prestes a medir não vêm da linguagem em que o controlador está escrito. Eles vêm da física da planta e da dinâmica da malha de controle, e por isso são exatamente os mesmos limites que a Unidade 4 vai herdar, independentemente de qual lado do acoplamento estiver escrito em qual linguagem.

### Demonstração ao vivo

**[07:20–09:00 · TELA: terminal — aula_08/01_build_fmu.py]**

Rodo o primeiro passo, a construção do FMU:

```
.venv/bin/python aula_08/01_build_fmu.py
```

A tela mostra o `gcc` compilando `plant_fmu.c` com otimização, gerando a biblioteca compartilhada `NexaBotPlant.so`, e em seguida empacotando essa biblioteca junto com o `modelDescription.xml` num único arquivo, `NexaBotPlant.fmu` — que, apesar da extensão diferente, é simplesmente um `.zip` comum. A confirmação final lista o conteúdo interno: pouco mais de vinte e três mil bytes de biblioteca binária e menos de três mil bytes de descrição XML, totalizando um pacote de sete vírgula dois quilobytes. Esse arquivo pequeno é um FMU FMI 3.0 de co-simulação inteiramente válido — a planta inteira do NexaBot, compilada em C nativo, pronta para ser carregada por qualquer ferramenta compatível com o padrão.

**[09:00–10:20 · TELA: terminal — aula_08/02_inspecta_fmu.py]**

Rodo a inspeção desse pacote, usando a biblioteca `fmpy`, a mesma que ferramentas comerciais de simulação usam para ler um FMU:

```
.venv/bin/python aula_08/02_inspecta_fmu.py
```

A tela confirma a versão do padrão, FMI três ponto zero, a interface suportada, co-simulação, e lista as cinco variáveis do modelo com suas causalidades: tensão de armadura e torque de carga como entradas, velocidade angular e corrente como saídas, tempo como variável independente. A segunda parte da tela roda `fmpy.dump`, que qualquer ferramenta compatível mostraria ao abrir esse mesmo arquivo — sem nenhum conhecimento do código-fonte em C que o gerou, apenas lendo o `modelDescription.xml` e reconhecendo a biblioteca binária pelo nome do modelo.

**[10:20–11:40 · TELA: terminal — nexabot/fmu/verify_fmu.py]**

Antes de atribuir qualquer diferença de resultado ao efeito de acoplamento, preciso isolar um outro tipo de erro: o de a planta em C simplesmente não reproduzir fielmente a planta em Python. Rodo:

```
.venv/bin/python -m nexabot.fmu.verify_fmu
```

Esse script aplica exatamente a mesma sequência de entradas em degraus ao FMU em C e à função `plant.simulate` em Python, e compara amostra a amostra. A tela mostra erro relativo máximo de $5{,}497\times10^{-10}\%$ em velocidade angular e $1{,}783\times10^{-8}\%$ em corrente — ruído de ponto flutuante, não um erro de modelagem: as duas implementações rodam o mesmo integrador de Runge-Kutta de quarta ordem sobre a mesma entrada. Essa separação importa metodologicamente: sem ela, um erro de acoplamento grande e um erro de implementação do FMU seriam indistinguíveis a partir de um único gráfico de trajetória divergente, e a equipe poderia gastar dias depurando o compilador C quando o problema real estivesse, na verdade, na escolha do passo de comunicação.

**[11:40–13:20 · TELA: terminal — aula_08/03_cosim_basica.py]**

Com o FMU verificado, rodo a co-simulação básica completa, a mesma que já estava parcialmente na tela na abertura desta videoaula:

```
.venv/bin/python aula_08/03_cosim_basica.py
```

Com passo de comunicação $H=5\,\mathrm{ms}$ — o mesmo período de amostragem do `DiscretePID` — e degrau de referência de $1{,}0\,\mathrm{m/s}$, a velocidade converge para exatamente $400{,}0000\,\mathrm{rad/s}$, e a tensão final se estabiliza em $18{,}8533\,\mathrm{V}$, batendo com o valor de regime já conhecido da Unidade 1. As métricas da resposta ao degrau mostram sobressinal de $23{,}430\%$, tempo de subida de $160$ milissegundos e tempo de acomodação de $605$ milissegundos — números muito próximos dos que a mesma sintonia produziria acoplada diretamente em Python, sem a ponte FMI, confirmando que, neste passo de comunicação, o acoplamento introduz pouco ou nenhum prejuízo perceptível.

**[13:20–15:20 · TELA: terminal — aula_08/04_erro_de_acoplamento.py]**

Chega o ponto pedagógico central desta aula: transformar o passo de comunicação de constante em parâmetro de varredura. Rodo:

```
.venv/bin/python aula_08/04_erro_de_acoplamento.py
```

O script compara a mesma co-simulação sob cinco valores de $H$ — um, cinco, dez, vinte e cinquenta milissegundos — contra uma referência quase contínua, com $H=0{,}5\,\mathrm{ms}$. A tabela final mostra o erro RMS relativo crescendo de forma monotônica e nada sutil: $0{,}0284\%$ em um milissegundo, $0{,}2544\%$ em cinco, $0{,}5332\%$ em dez, $1{,}0775\%$ em vinte, e $6{,}2299\%$ em cinquenta milissegundos — mais de duzentas vezes o erro do caso de um milissegundo. O erro máximo instantâneo segue o mesmo padrão, chegando a quase catorze por cento no passo de cinquenta milissegundos. A proposta que abriu esta videoaula, de espaçar a comunicação para cinquenta milissegundos para reduzir sobrecarga, não é uma otimização barata: o controlador reage cada vez mais tarde, e a tensão de comando fica retida por cada vez mais tempo em relação ao que a planta física realmente precisa naquele instante — o erro de acoplamento deixou de ser um conceito abstrato e virou um número concreto, direto na tela.

### Aplicação profissional

**[15:20–16:50 · TELA: editor — FMI na indústria automotiva e aeroespacial]**

A Functional Mock-up Interface não é uma escolha pedagógica desta disciplina: é o padrão aberto mais adotado pela indústria automotiva e aeroespacial exatamente para o problema que acabei de demonstrar — integrar modelos desenvolvidos por equipes diferentes, em ferramentas diferentes, sem forçar todo mundo a um único ambiente de simulação. Uma montadora pode desenvolver o modelo de powertrain numa ferramenta de dinâmica veicular, o modelo de bateria numa ferramenta de eletroquímica, e o controlador de tração numa terceira ferramenta ainda, e acoplar os três por FMI para simular o veículo inteiro, sem que nenhuma das três equipes precise expor o código-fonte proprietário às outras — apenas a interface padronizada de entradas, saídas e passo de comunicação.

E a decisão que domina o resultado final dessa integração é sempre a mesma que esta aula acabou de medir: o passo de comunicação escolhido entre os modelos. Uma equipe de integração que reduz esse passo apenas para "parecer mais preciso", sem medir o efeito real como fizemos aqui, desperdiça tempo de simulação; uma equipe que aumenta o passo sem medir o custo corre o risco oposto, e mais grave: produzir um resultado qualitativamente errado, acreditando que está apenas perdendo um pouco de precisão.

### Fechamento

**[16:50–18:00 · TELA: terminal — pontos-chave e desafio]**

Recapitulando os pontos-chave desta aula. Co-simulação mantém integradores independentes — aqui, um binário em C e um script em Python — que trocam dados apenas em pontos de comunicação espaçados por $H$, em vez de integrar um modelo único monolítico. Um FMU de co-simulação é, por dentro, apenas um `.zip` com uma descrição XML e uma biblioteca binária, e qualquer ferramenta compatível com FMI consegue carregá-lo sem conhecer o código-fonte original. Verificar o FMU isoladamente contra a implementação de referência, como fez `verify_fmu.py`, separa erro de implementação de erro de acoplamento — os dois seriam indistinguíveis sem essa etapa. E, para o NexaBot, o erro de acoplamento cresce continuamente com $H$, de menos de três centésimos por cento em um milissegundo a mais de seis por cento em cinquenta milissegundos.

A atividade prática desta aula é o desafio que fica em `aula_08/05_desafio.py`: implementar um torque de carga em rampa, simulando o NexaBot subindo uma inclinação física real, e comparar a rejeição desse distúrbio pela mesma co-simulação sob um passo de comunicação pequeno e sob um passo grande — verificando se a mesma degradação medida hoje para um degrau de referência também aparece, e na mesma proporção, para um distúrbio de carga contínuo em vez de um degrau instantâneo.

**[18:00–20:00 · TELA: terminal — transição para a Unidade 3 e encerramento]**

Esta unidade fechou a malha de velocidade do NexaBot, sintonizou-a tratando saturação e *windup* como parte do projeto, discretizou-a com um período de amostragem numericamente justificado, e acoplou planta e controlador por co-simulação, medindo exatamente o preço de espaçar essa comunicação. Toda evidência produzida ao longo dessas quatro aulas veio de simulação — e simulação, por mais cuidadosa que seja a escolha dos cenários, sempre responde à mesma pergunta limitada: o que o sistema faz nos cenários que alguém escolheu simular.

A Unidade 3 muda essa pergunta de forma radical. Em vez de simular alguns cenários específicos do supervisor de segurança do NexaBot, a próxima unidade verifica exaustivamente **todos** os cenários alcançáveis a partir do estado inicial — não uma amostra deles, o espaço inteiro — e prova, com certeza matemática, que requisitos de segurança como nunca habilitar torque com obstáculo presente jamais são violados, em nenhuma combinação de entradas possível. Essa diferença entre mostrar o que o sistema faz em alguns cenários e provar o que ele faz em todos é exatamente o salto que separa engenharia de controle de engenharia de sistemas críticos verificados formalmente. Até a Unidade 3.

### Indicações de edição e recursos visuais

- Inserir Recurso visual 11 da unidade — FMU da planta e controlador como caixas independentes, coordenadas por um mestre de co-simulação que troca dados só nos múltiplos de $H$ — sobreposto ao editor, aproximadamente em 03:30.
- Inserir Recurso visual 12 da unidade — árvore de diretórios do `.fmu`, com `modelDescription.xml` na raiz e a biblioteca binária em `binaries/x86_64-linux/` — sobreposto ao terminal, aproximadamente em 08:00.
- Inserir Recurso visual 13 da unidade — erro de acoplamento crescendo com $H$ em escala logarítmica, um, cinco, dez, vinte e cinquenta milissegundos no eixo x — em tela cheia, aproximadamente em 14:00.
- 13:20–15:20 — congelar a tabela final de `04_erro_de_acoplamento.py` com zoom, destacando a linha de cinquenta milissegundos.
- 18:00–20:00 — vinheta de encerramento da Unidade 2, com chamada explícita para a Unidade 3.

### Fontes e links de mídia

- MODELICA ASSOCIATION. *Functional Mock-up Interface Specification*, version 3.0, 2022 — referência conceitual, sem reprodução de trecho externo.
- BLOCHWITZ, Torsten et al. Functional mockup interface 2.0: the standard for tool independent exchange of simulation models. In: INTERNATIONAL MODELICA CONFERENCE, 9., 2012, Munique. *Proceedings [...]*. Linköping: Linköping University Electronic Press, 2012. p. 173-184 — referência conceitual, sem reprodução de trecho externo.
- FRANKLIN, Gene F.; POWELL, J. David; EMAMI-NAEINI, Abbas. *Sistemas de controle para engenharia*. 6. ed. Porto Alegre: Bookman, 2013 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas e gráficos devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 8 (`unidade_2.md`) e da saída real dos scripts de `projeto_nexabot/aula_08/` e `nexabot/fmu/`.
