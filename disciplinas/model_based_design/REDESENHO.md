# Redesenho para público introdutório

> **Por que este documento existe.** As videoaulas 1 e 2 foram gravadas e o
> resultado mostrou o problema: o material chega "com os dois pés na porta".
> Ele entra em Kirchhoff, espaço de estados e Laplace sem nunca ter dito o que
> é `rad/s`, o que é uma equação diferencial ou o que significa "estado". Foi
> escrito para quem já sabia. O público é introdutório.
>
> Este arquivo é o plano da correção: aula por aula, **o que sai da videoaula**
> para abrir espaço e **qual chão entra no lugar**. O padrão pedagógico que
> rege tudo isso está na seção 3 de `DIRETRIZES_PRODUCAO.md`.

## A restrição que molda tudo

O contrato fixa **16 videoaulas de 20 minutos** e a ementa oficial. Não dá para
ir mais devagar e cobrir a mesma coisa: 20 minutos são 20 minutos. Então cada
aula perde o tópico mais avançado que carregava, e o tempo liberado vira o
"Chão da aula".

Nada é apagado. O que sai da videoaula vai para um destes três lugares, sempre
nomeado no texto da aula, na seção "O que ficou de fora":

| Destino | Quando | Como o aluno chega lá |
| --- | --- | --- |
| **Notebook** | O assunto é operacional: o aluno precisa ver rodar, não precisa derivar | Célula extra no `.ipynb` da própria aula, marcada como *Aprofundamento* |
| **Material complementar** | O assunto é conceitual e existe boa fonte externa | Seção da unidade, com link |
| **Aula posterior** | O assunto fica mais fácil depois de outro conceito | Citado como "voltamos a isso na Aula N" |

## Unidade 1 — Modelar a planta

### Aula 1 — Sistemas ciberfísicos e o ciclo do design baseado em modelos

**Ideia central:** um comando fixo não sustenta velocidade quando a carga muda.

| | |
| --- | --- |
| **Chão que entra** | O que é `rad/s` (uma volta = 6,28 rad; 100 rad/s ≈ 16 voltas por segundo, e a roda de 50 mm anda 0,25 m/s). O que é um *modelo* (uma conta que imita o robô, para errar no computador em vez de errar no chão de fábrica). O que é *malha aberta* (mandar e não conferir). |
| **Sai da videoaula** | A instalação do ambiente passo a passo com `uv` (vira notebook + `README`, com um vídeo curto de apoio). O V-Model completo das 16 aulas — fica só a metade descendente, "primeiro o modelo, depois o código". |
| **Fica** | A demonstração da queda de velocidade sob carga. É o gancho da disciplina inteira. |

### Aula 2 — Da equação diferencial ao espaço de estados

**Ideia central:** duas contas de física descrevem o motor inteiro.

Esta é a aula mais pesada do curso hoje: abre com Kirchhoff, emenda Newton
rotacional, monta as matrizes A/B/C/D e ainda cobre mínimos quadrados não
linear, Levenberg-Marquardt, ruído gaussiano e quantização de ADC.

| | |
| --- | --- |
| **Chão que entra** | O que é uma *equação diferencial* — uma frase que diz o quanto uma coisa muda por segundo, não uma fórmula fechada. O que é *estado* — a memória do sistema; para saber o futuro do motor bastam duas coisas de agora, a corrente e a velocidade. O que cada letra é fisicamente: `R` é o quanto o fio resiste, `J` é o quanto o eixo custa a acelerar, `b` é o atrito que rouba giro. |
| **Sai da videoaula** | Mínimos quadrados não linear, Levenberg-Marquardt, região de confiança, `fit%`, sobreajuste, ruído de ADC e quantização de encoder. Tudo isso vira **uma frase** na aula ("os cinco números foram ajustados até a conta bater com o ensaio") e o algoritmo vai para o notebook. |
| **Fica** | As duas equações, o significado de estado, e o ganho estático como conferência barata. |
| **Vira aula 2 e não duas** | O corte é grande o bastante para caber. Se no ensaio de gravação ainda estourar, a identificação migra inteira para a Aula 3. |

### Aula 3 — Laplace e função de transferência

**Ideia central:** existe um jeito de trocar cálculo por álgebra.

Hoje a aula usa Laplace sem dizer o que Laplace faz.

| | |
| --- | --- |
| **Chão que entra** | O que a transformada de Laplace *faz*, em uma frase: transforma derivada em multiplicação, então uma equação diferencial vira uma equação comum. O que é um *polo*, em linguagem de comportamento: a velocidade com que o sistema esquece o que aconteceu. O que é *constante de tempo*: o tempo para chegar a 63% do valor final — e por que 63% e não 100%. |
| **Sai da videoaula** | Diagrama de Bode, margem de fase, margem de ganho e largura de banda. Migram para a **Aula 7**, onde já existe o problema de estabilidade que os torna necessários. Zeros também saem: o NexaBot não tem zero relevante. |
| **Fica** | Polos, constantes de tempo e a separação de escalas — a elétrica é rápida, a mecânica é lenta. |

### Aula 4 — Controlabilidade, observabilidade e realimentação

**Ideia central:** nem todo projeto correto no papel cabe nos 24 V do driver.

| | |
| --- | --- |
| **Chão que entra** | Controlabilidade em português: *consigo levar o robô a qualquer velocidade que eu queira, com o motor que eu tenho?* Observabilidade: *consigo descobrir a corrente sem medir a corrente?* O que é *saturação*: o driver só tem 24 V, e pedir mais não faz aparecer mais. |
| **Sai da videoaula** | A fórmula de Ackermann e a construção das matrizes de controlabilidade e observabilidade à mão. O aluno usa `control.place` e entende o critério pelo resultado, não pela derivação. As matrizes vão para o notebook. |
| **Fica** | A demonstração de alocar polos cada vez mais rápidos até a tensão estourar. É o momento em que a física impõe o limite, e ele é visual. |

## Unidade 2 — Fechar a malha

### Aula 5 — Malha aberta, malha fechada e diagramas de blocos

**Ideia central:** medir e corrigir é o que separa um robô que funciona de um que não.

| | |
| --- | --- |
| **Chão que entra** | Realimentação com o chuveiro e o termostato antes de qualquer bloco. O que é *erro* (o que eu queria menos o que eu tenho). O que é *regime permanente* (depois que parou de balançar). |
| **Sai da videoaula** | Funções de sensibilidade `S` e complementar `T`, e "tipo de sistema". Vão para material complementar; a aula guarda só a conclusão prática — com integrador, o erro em regime vai a zero. |
| **Fica** | A mesma conta em malha aberta e em malha fechada, lado a lado, com os números do NexaBot. |

### Aula 6 — PID na prática

**Ideia central:** três ajustes, três comportamentos, e um que quebra tudo se você esquecer o limite do driver.

| | |
| --- | --- |
| **Chão que entra** | O que cada letra faz, em português: **P** reage ao erro de agora, **I** lembra do erro acumulado, **D** antecipa para onde o erro está indo. Cada um demonstrado sozinho antes de juntar. |
| **Sai da videoaula** | A derivação de Ziegler-Nichols pelo ganho crítico. Fica a receita e o resultado; a teoria vai para o notebook. Filtro da ação derivativa vira nota. |
| **Fica** | Anti-windup. É visual, é um erro real e a correção aparece na mesma tela — exatamente o tipo de conteúdo que funciona em vídeo. |

### Aula 7 — Discretização e período de amostragem

**Ideia central:** o controlador não vê o robô o tempo todo, só de tempos em tempos — e se olhar pouco demais, derruba tudo.

| | |
| --- | --- |
| **Chão que entra** | Amostragem com a analogia da câmera: filme contínuo contra fotos a cada tanto. Por que 5 ms e não 50 ms. O que é Hz e como ele se relaciona com o período. Aqui entram também **Bode e margem de fase**, que vieram da Aula 3, agora com um problema concreto para resolver. |
| **Sai da videoaula** | A comparação Euler para frente / Euler para trás / Tustin / ZOH. A aula adota **Tustin** e explica por quê em uma frase; as outras três ficam no notebook, lado a lado, para o aluno comparar rodando. |
| **Fica** | A varredura de `Ts` até o sistema instabilizar. É o momento mais didático da unidade. |

### Aula 8 — Co-simulação planta-controlador

**Ideia central:** quando dois simuladores conversam, o erro nasce na conversa.

Esta é a aula mais desalinhada com o público. FMI 3.0 é assunto de quem já
trabalha com integração de modelos.

| | |
| --- | --- |
| **Chão que entra** | Por que dois simuladores separados, com a analogia de duas pessoas remando sem se olhar e se corrigindo a cada tantas remadas. O que é *passo de comunicação*. |
| **Sai da videoaula** | A anatomia do padrão FMI, a estrutura do FMU e a verificação do FMU contra o modelo de referência. Viram notebook e material complementar. |
| **Fica** | A demonstração de que o erro de acoplamento cresce com `H`. É um número, é visível e é a lição inteira. |

## Unidade 3 — Provar

### Aula 9 — Da especificação em texto à propriedade formal

**Ideia central:** a mesma frase em português vira três programas diferentes.

Esta é a aula mais bem calibrada do curso hoje. Mudança pequena.

| | |
| --- | --- |
| **Chão que entra** | Um exemplo de ambiguidade do dia a dia antes do requisito técnico — uma instrução doméstica que duas pessoas cumprem de jeitos opostos. O que é um *predicado* (uma pergunta que só aceita sim ou não). |
| **Sai da videoaula** | A taxonomia completa de tipos de propriedade. Ficam dois: *segurança* ("nunca acontece") e *vivacidade* ("uma hora acontece"). |
| **Fica** | As três leituras incompatíveis do mesmo requisito. É o melhor gancho da unidade. |

### Aula 10 — Model checking

**Ideia central:** o computador testa todos os caminhos, não uma amostra deles.

| | |
| --- | --- |
| **Chão que entra** | O que é *espaço de estados*, com a analogia do mapa de todas as posições possíveis de um jogo. O que é *busca em largura*. Por que "testei muito" não é o mesmo que "provei". |
| **Sai da videoaula** | **CTL sai inteiro.** A aula fica só com LTL, e mesmo assim com dois operadores: "sempre" e "uma hora". CTL vai para material complementar. Explosão de estados vira uma frase e um número, não uma seção. |
| **Fica** | O contraexemplo. Ver a ferramenta devolver a sequência exata que quebra o sistema é o que vende a técnica. |

### Aula 11 — Autômatos temporizados e prazo

**Ideia central:** "responde rápido" não é requisito; "responde em até 150 ms" é.

| | |
| --- | --- |
| **Chão que entra** | O que é um *relógio* no modelo, com a analogia do cronômetro que zera. Por que o pior caso quase nunca aparece em teste comum. |
| **Sai da videoaula** | Invariantes de localização e a semântica formal de guardas. Ficam como notação lida, não derivada. UPPAAL vira menção de mercado, não demonstração. |
| **Fica** | O watchdog que nunca falhou em teste e falha na prova formal. |

### Aula 12 — Testes gerados do modelo e cobertura

**Ideia central:** passar em todos os testes não é prova de nada se os testes forem fracos.

| | |
| --- | --- |
| **Chão que entra** | O que é *cobertura*, com a analogia de conferir um texto lendo só metade das linhas. O que é um teste *baseado em propriedade* contra um teste de exemplo. |
| **Sai da videoaula** | Os critérios formais de cobertura de grafo (arestas, caminhos, condição/decisão). Fica um: cobrir toda transição. O resto vai para o notebook. |
| **Fica** | Hypothesis encontrando um caso que ninguém escreveu à mão, e reduzindo ele ao mínimo. |

## Unidade 4 — Embarcar

### Aula 13 — Geração automática de código

**Ideia central:** o código que ninguém digita é o código que ninguém digita errado.

| | |
| --- | --- |
| **Chão que entra** | O que é *ponto flutuante* contra *ponto fixo*, com a analogia de dinheiro em centavos inteiros contra dinheiro com casas infinitas. O que é um *hash* e por que ele serve de assinatura. |
| **Sai da videoaula** | A derivação simbólica em SymPy, passo a passo, da forma contínua à equação de diferenças. Vira notebook; a aula mostra a entrada e a saída, não a álgebra. |
| **Fica** | O bloco de rastreabilidade no cabeçalho do C gerado, e o hash mudando quando um ganho muda. |

### Aula 14 — Software-in-the-loop

**Ideia central:** "equivalente" só vale como palavra depois de virar número.

Aula bem calibrada. Mudança pequena.

| | |
| --- | --- |
| **Chão que entra** | O que é *épsilon de máquina*, sem teoria de ponto flutuante: o menor degrau que o computador consegue representar, e por que dois cálculos corretos podem discordar nessa casa. |
| **Sai da videoaula** | Integração contínua e a configuração do GitHub Actions. Vira material complementar. |
| **Fica** | O bug real e sua correção na mesma tomada. |

### Aula 15 — Hardware-in-the-loop, tempo real e jitter

**Ideia central:** o mesmo código, no hardware de verdade, dá outro resultado — e o motivo tem nome.

| | |
| --- | --- |
| **Chão que entra** | O que é *tempo real* (não é "rápido", é "no prazo, sempre"). O que é *jitter*, com a analogia do ônibus que passa a cada 10 minutos mas nunca no minuto certo. |
| **Sai da videoaula** | O protocolo de linha em detalhe (quadro, checksum, sincronismo). Vira notebook e `README` do laboratório. |
| **Fica** | O jitter medido sobre o período de 5 ms, e o watchdog disparando. |

### Aula 16 — Rastreabilidade, certificação e fechamento

**Ideia central:** evidência não é a mesma coisa que certificado, e saber a diferença é o que te contrata.

Aula conceitual, já acessível. Mudança pequena.

| | |
| --- | --- |
| **Chão que entra** | O que é uma *norma* e o que significa "nível de criticidade", com um exemplo do que muda entre um brinquedo e um freio. |
| **Sai da videoaula** | A discussão de qualificação de ferramenta segundo o DO-330. Fica a ideia, sai o detalhe normativo. |
| **Fica** | Percorrer uma linha inteira da matriz de rastreabilidade, do requisito ao binário. E o fechamento. |

## Notebooks

Um `.ipynb` por aula, em `notebooks/`, nomeados `aula_NN_assunto.ipynb`.

Estrutura fixa de cada notebook:

1. **O que você vai fazer aqui** — em três linhas, sem jargão.
2. **Antes de começar** — o chão da aula, agora executável: célula que imprime
   `100 rad/s` convertido em voltas por segundo e em metros por segundo.
3. **Passo a passo**, uma célula por ideia, cada uma precedida de texto em
   português explicando o que a célula faz *antes* de o aluno rodar.
4. **Mexa aqui** — célula com um valor destacado para o aluno alterar, e a
   pergunta do que ele espera que aconteça antes de rodar de novo.
5. **Aprofundamento** — o conteúdo que saiu da videoaula, marcado como opcional.
6. **Se deu erro** — os dois ou três erros mais prováveis e o que fazer.

Os notebooks importam de `projeto_nexabot/nexabot/`, então nenhum número é
reescrito: `params.py` continua sendo a fonte única de verdade.

## Ordem de execução

1. `DIRETRIZES_PRODUCAO.md` seção 3 — o padrão pedagógico. **Feito.**
2. Este arquivo — o mapa de cortes. **Feito.**
3. Unidade 1: `unidade_1.md`, `roteiros_20min.md`, 4 notebooks.
4. Unidade 2, 3 e 4, na mesma forma.
5. Decks HTML das 17 aulas, alinhados ao novo texto.
6. Questionários: reconferir as 160 questões contra o conteúdo que saiu.
7. `avaliacao_dissertativa.md` e `entrega_trabalho.md`, mesma conferência.
