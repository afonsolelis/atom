# Roteiros das videoaulas 9 a 12 — Unidade 3 (20 minutos)

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 3: Verificação formal e testes baseados em modelos
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: aproximadamente 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, comandos, saídas de terminal, indicações de edição e fontes.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas, respiração e o tempo de leitura da saída na tela.

Esta é uma disciplina gravada por captura de tela e câmera, sem deck de slides: cada roteiro alterna entre blocos `TELA: terminal`, com o diretório `projeto_nexabot/` já aberto e o interpretador `.venv/bin/python`, e blocos `TELA: editor`, com um arquivo de `nexabot/` ou de `aula_0N/` aberto para leitura comentada. Todo comando citado em bloco de terminal foi executado durante a produção deste roteiro, e a saída descrita reflete exatamente o que apareceu na tela — nenhum número aqui é estimado ou arredondado além do que o próprio script já arredonda. Nenhuma aula começa em tela neutra: os dois primeiros minutos de cada videoaula já têm terminal ou editor abertos, com algo em andamento, e o gancho da aula nasce daquilo que já está na tela.

Plano de tempo de referência, adaptável ao ritmo de cada aula:

- 00:00–02:00 — abertura contextualizada, já em tela de terminal ou editor;
- 02:00–08:30 — desenvolvimento conceitual, em editor, com leitura comentada do código-fonte;
- 08:30–16:00 — demonstração ao vivo, em terminal, com os comandos e a saída real da aula;
- 16:00–18:30 — aplicação profissional (e, na Aula 11, pausa para reflexão com contagem regressiva);
- 18:30–20:00 — pontos-chave, atividade prática e encerramento.

O fio condutor das quatro aulas é o supervisor de segurança do NexaBot (`nexabot/supervisor.py`), seus seis estados alcançáveis — OCIOSO, MOVENDO, DESACELERANDO, PARADO_OBSTACULO, FALHA e EMERGENCIA — e os requisitos REQ-SAFE-001 a REQ-SAFE-007. Cada roteiro é texto de narração pronto para leitura em voz alta, não notas de aula: frases completas, encadeamento explícito entre as ideias, sem recursos de oralidade informal.

---

## Roteiro da Videoaula 9 — "Um requisito, três leituras: da ambiguidade à propriedade formal"

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 9 — Da especificação em texto à propriedade formal.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de identificar as três fontes de ambiguidade de um requisito em linguagem natural, classificar uma propriedade formal como invariante, alcançabilidade, segurança ou vivacidade, e traduzir um requisito de segurança do NexaBot num predicado Python executável.

**Mapa de tempo e telas:** 00:00 terminal com a tabela de requisitos já na tela · 01:40 editor: `supervisor.py` · 03:10 editor: `requisitos.py`, a dataclass `Requisito` · 05:00 editor: os sete requisitos rastreados · 07:00 editor: do predicado ao código · 08:30 terminal: `02_do_texto_a_propriedade.py` · 12:00 leitura do contraexemplo e da lição · 14:00 terminal: `03_desafio.py` · 16:00 aplicação profissional · 18:00 pontos-chave e atividade · 19:30 encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: terminal — aula_09/01_requisitos.py, tabela já na tela]**

A tela mostra a saída de um comando já executado: uma tabela com sete requisitos de segurança rastreados para o NexaBot. Seis têm verificação implementada nesta unidade; o sétimo registra, sem escondê-la, uma propriedade contínua ainda não verificada. Chegar a essa tabela de forma reproduzível é o assunto inteiro desta aula.

Recuo um passo. Há poucas semanas, um requisito chegou à equipe do NexaBot assim, extraído de uma ata de reunião com a área de segurança do armazém: "o robô deve parar rapidamente se houver obstáculo." Ninguém discordou dele. E, ao mesmo tempo, ninguém, sozinho, a partir desse texto, conseguiu decidir se uma implementação específica estava correta. Um desenvolvedor leu "rapidamente" como "no próximo ciclo de controle"; outro leu "parar" como "velocidade linear igual a zero", que fisicamente ainda leva centenas de milissegundos por inércia; um terceiro contou o prazo a partir do instante físico em que o obstáculo surge, outro a partir do instante em que o sensor, já filtrado, o reconhece. As três leituras são defensáveis diante do texto, e diferentes o bastante para que uma passe em auditoria e outra cause um incidente real, com um robô de dezenas de quilos em movimento perto de pessoas.

Esta aula existe para resolver exatamente esse problema: transformar um requisito ambíguo em propriedade formal, verificável por máquina, sem depender de interpretação pessoal de quem lê.

### Desenvolvimento conceitual

**[01:40–03:10 · TELA: editor — nexabot/supervisor.py, docstring de estados, entradas e saídas]**

Abro o arquivo que será o objeto de toda a Unidade 3: `nexabot/supervisor.py`. O cabeçalho documenta seis estados — OCIOSO, MOVENDO, DESACELERANDO, PARADO_OBSTACULO, FALHA e EMERGENCIA —, sete entradas booleanas ou numéricas — comando de partida, comando de parada, obstáculo, emergência, falha de encoder, rearme e velocidade — e duas saídas: torque habilitado e freio acionado. A função central, `transition`, recebe um estado e um conjunto de entradas e devolve o próximo estado e as saídas correspondentes. Ela é pura: mesma entrada, sempre a mesma saída, sem efeito colateral algum. Essa pureza não é estilo de código; é pré-condição técnica para tudo que vem a seguir. Um verificador formal precisa aplicar essa função milhares de vezes sobre estados hipotéticos, e só pode fazer isso com segurança se souber, com certeza, que aplicar a função não altera nada além do valor que ela devolve.

Este supervisor é o mesmo que a Unidade 2 já usava para orquestrar o motor do NexaBot. O que muda nesta unidade não é o código — é o que fazemos com ele: em vez de simulá-lo em alguns cenários escolhidos, vamos perguntar se ele se comporta corretamente em absolutamente todos os cenários possíveis.

**[03:10–05:00 · TELA: editor — nexabot/requisitos.py, a dataclass Requisito e os tipos]**

Rolo até `nexabot/requisitos.py`. Aqui mora a resposta à pergunta que abriu esta aula. Cada requisito é um objeto `Requisito`: um identificador rastreável no padrão REQ-SAFE-00N, um campo `tipo`, uma descrição em português e um predicado Python executável. Não sobra ambiguidade: o predicado devolve `True` ou `False` para uma transição específica, e qualquer pessoa que rode o mesmo código chega sempre à mesma resposta. É esse determinismo de julgamento — não elegância de prosa — que separa um requisito formalizado de um requisito apenas escrito.

O arquivo documenta cinco tipos de propriedade, e vale fixar cada um com precisão, porque o vocabulário vai acompanhar as próximas três aulas inteiras. Invariante é a condição que deve valer em toda transição alcançável, sempre — "isto nunca deixa de ser verdade". Alcançabilidade pergunta se existe pelo menos um caminho até um estado-alvo — "é possível chegar lá?" —, sem exigir que se chegue sempre. Segurança, em inglês *safety*, significa "nada de ruim acontece"; pode aparecer como invariante de estado ou, de forma mais sutil, como invariante sobre a própria transição — uma restrição sobre para onde o sistema tem permissão de ir a seguir, não sobre onde ele está agora. Vivacidade, *liveness*, é o oposto complementar: "algo bom eventualmente acontece" — o sistema não pode ficar preso esperando uma condição que nunca se resolve. E temporizado é a propriedade quantitativa sobre um relógio, que esta aula deixa anunciada e a Aula 11 verifica por inteiro.

**[05:00–07:00 · TELA: editor — nexabot/requisitos.py, os sete requisitos rastreados]**

Desço pelo arquivo e encontro os seis requisitos já implementados. REQ-SAFE-001 é invariante: nunca há torque habilitado enquanto o sensor de obstáculo estiver ativo, em nenhum estado. REQ-SAFE-002, também invariante: botão de emergência pressionado implica freio acionado e torque desabilitado, sem exceção. REQ-SAFE-003 é alcançabilidade pura: o estado MOVENDO precisa ser alcançável a partir de OCIOSO — sem essa garantia, o robô simplesmente nunca sairia do lugar, e isso também é um defeito de segurança, só que do tipo oposto ao que normalmente se imagina. REQ-SAFE-004 é o exemplo mais instrutivo de segurança como invariante de transição: a partir do estado FALHA, a única saída possível é por rearme explícito do operador — nunca por decurso de tempo, nunca por um novo comando, nunca por nenhuma outra condição concorrente. REQ-SAFE-005 é vivacidade: uma vez removido o obstáculo, com comando de partida do operador e nenhuma outra condição de segurança concorrente, o sistema deve voltar a MOVENDO — o robô não pode ficar preso em PARADO_OBSTACULO para sempre. E REQ-SAFE-006, o único temporizado: após a detecção de obstáculo, o torque físico precisa chegar a zero em no máximo $150\,\mathrm{ms}$, que equivalem a exatamente $30$ períodos de amostragem de $T_s = 5\,\mathrm{ms}$.

Essa correspondência resolve, ponto a ponto, a ambiguidade que abriu a aula. "Parar o quê" — o comando de torque, no nível lógico — vira REQ-SAFE-001, sem prazo algum, restrição instantânea. "Quão rápido" e "a partir de quando" viram REQ-SAFE-006, com o número $150\,\mathrm{ms}$ explícito e o instante de referência definido como o gatilho físico do obstáculo. Um requisito ambíguo de uma linha vira dois requisitos formais, verificados por técnicas diferentes: o primeiro por exploração de estados, na próxima aula; o segundo por autômato temporizado, na Aula 11.

Vale notar que essa não é a única decomposição possível, e reconhecer isso é parte do ofício. Um terceiro requisito, ainda em aberto nesta tabela, cobre a velocidade linear do robô — REQ-SAFE-007, que aparece no arquivo apenas como descrição, sem predicado, porque depende de uma grandeza contínua que este verificador não manipula. Deixo a lacuna anotada: ela reaparece na Aula 12, quando discutimos o que testes baseados em propriedades podem e não podem demonstrar sobre o modelo em malha fechada. Um requisito nem sempre é verificável pela primeira técnica que vem à cabeça, e reconhecer essa limitação é parte da engenharia.

**[07:00–08:30 · TELA: editor — do predicado ao código: verificar_transicao]**

Olho de perto a assinatura comum a quase todos esses predicados: `verificar_transicao(estado, entradas, saida, proximo_estado) -> bool`. Ela recebe os quatro elementos de uma transição individual — de onde se partiu, o que entrou, o que saiu, para onde se foi — e devolve um booleano. REQ-SAFE-001, por exemplo, se resume a uma única linha: não é verdade que o torque esteja habilitado e o obstáculo esteja presente, ao mesmo tempo. REQ-SAFE-004 é mais refinado: se o estado é FALHA e o próximo não é FALHA, então a entrada de rearme precisa ser verdadeira — caso contrário, a condição não se aplica e o requisito vale trivialmente. Essa forma de escrever — uma implicação lógica sobre uma transição, não sobre um estado isolado — é exatamente o que permite que segurança e vivacidade, apesar de conceitualmente distintas, sejam verificadas pelo mesmo mecanismo quando o sistema é determinístico, como veremos daqui a pouco na prática.

Um detalhe de engenharia de software importa aqui, e não é acessório: cada `Requisito` também carrega seu identificador REQ-SAFE-00N como campo de dados, não como comentário solto no código. Isso significa que a lista `REQUISITOS`, definida ao final do arquivo, pode ser percorrida programaticamente por qualquer outro script da disciplina — o verificador da próxima aula, o gerador de testes da Aula 12, e futuramente a matriz de rastreabilidade da Unidade 4 — sem que ninguém precise copiar manualmente a lista de identificadores em mais de um lugar. A rastreabilidade entre requisito e verificação não é uma tabela separada mantida à parte: ela nasce do próprio código.

### Demonstração ao vivo

**[08:30–12:00 · TELA: terminal — aula_09/02_do_texto_a_propriedade.py]**

Chega o momento de ver isso funcionando, com um caso real em que o próprio processo de formalização encontrou um problema na especificação original. Rodo o comando:

```
.venv/bin/python aula_09/02_do_texto_a_propriedade.py
```

A saída começa exibindo o requisito como a engenharia de sistemas o escreveria: "se o obstáculo for removido e o operador comandar a partida, o AGV deve voltar a se mover." Em seguida aparece a primeira formalização, deliberadamente ingênua, tradução quase literal do texto: se o estado é PARADO_OBSTACULO, o obstáculo não está mais presente e há comando de partida, então o próximo estado deve ser MOVENDO. Parece correta. É exatamente o tipo de tradução que uma pessoa cuidadosa produziria numa primeira tentativa.

O script então roda o verificador contra essa versão ingênua, e a tela mostra um contraexemplo real, não hipotético: partindo de OCIOSO, o comando de partida leva a MOVENDO; em seguida, o obstáculo aparece e o sistema vai para PARADO_OBSTACULO; na terceira transição, o operador comanda a partida de novo, mas simultaneamente ocorre uma falha de encoder — e o próximo estado correto é FALHA, não MOVENDO. A versão ingênua do requisito exigiria MOVENDO mesmo assim, porque nunca previu essa combinação. O texto original, ao dizer apenas "se o obstáculo for removido e houver comando de partida", presumiu implicitamente que nenhuma outra condição de segurança estaria ocorrendo ao mesmo tempo — uma suposição que ninguém escreveu, e que só um verificador exaustivo, testando combinações que uma pessoa não pensaria em testar manualmente, expôs.

**[12:00–14:00 · TELA: terminal — leitura do contraexemplo e da lição da aula]**

A tela continua mostrando a formalização corrigida, a que de fato está em produção em `nexabot/requisitos.py`: o próximo estado só precisa ser MOVENDO quando, além de obstáculo ausente e comando de partida presente, não há emergência e não há falha de encoder concorrentes. Rodando o verificador de novo contra essa versão corrigida, sobre o mesmo espaço de estados, o resultado passa de contraexemplo encontrado para zero violações.

Vale registrar a lição com todas as letras, porque ela é o ponto mais importante desta aula: verificação formal não serve só para achar bugs no código — serve também para achar bugs na própria especificação, antes que ela vire código, teste ou treinamento de operador. Se essa falha de encoder concorrente tivesse passado despercebida até a fase de testes manuais, provavelmente teria sido descoberta tarde, sob a forma de um comportamento inesperado difícil de reproduzir. Encontrá-la aqui, no nível do requisito, com um contraexemplo de três passos gerado em milissegundos, é ordens de grandeza mais barato.

**[14:00–16:00 · TELA: terminal — aula_09/03_desafio.py]**

Fecho a demonstração com o desafio da aula. Rodo:

```
.venv/bin/python aula_09/03_desafio.py
```

O script propõe uma propriedade adicional, em texto livre: "o robô nunca aciona o freio e habilita o torque ao mesmo tempo." A saída confirma zero violações sobre 768 transições exploradas. O comentário final levanta uma pergunta genuína: vale manter formalmente uma propriedade redundante como defesa em profundidade? Se a resposta for sim, ela precisa receber um identificador novo; REQ-SAFE-007 já pertence ao limite contínuo de velocidade. Redundância intencional é decisão de projeto, mas rastreabilidade sem ambiguidade é obrigatória.

### Aplicação profissional

**[16:00–18:00 · TELA: editor — requisitos.py, aplicação em normas de sistemas críticos]**

Por que uma equipe de armazém investiria tempo de engenharia sênior em reescrever um requisito de uma linha como um objeto Python com predicado formal? Porque, em qualquer indústria de sistemas críticos, essa etapa é obrigatória, não opcional. A ISO 26262, no setor automotivo, exige, para os níveis mais altos de integridade de segurança, evidência de verificação formal e rastreabilidade entre requisito e comportamento verificado — não apenas "os testes passaram". A DO-178C, na aeroespacial, impõe rastreabilidade entre requisito, projeto e teste, exatamente na forma de identificador único que aparece em cada `Requisito` desta base de código. A IEC 62304, em dispositivos médicos programáveis, cobra o mesmo tipo de disciplina, e acidentes reais nesse setor já foram causados por uma condição de corrida entre estados que nenhum teste manual chegou a exercitar — exatamente o tipo de combinação concorrente que o contraexemplo desta aula acabou de expor.

O que essas três normas têm em comum não é a ferramenta usada. É a exigência de que um requisito de segurança deixe de ser prosa e passe a ser algo que duas pessoas diferentes, seguindo o mesmo processo mecânico, verifiquem sempre da mesma forma. Um engenheiro capaz de fazer essa tradução — mesmo com ferramentas abertas como as desta disciplina — tem vantagem concreta sobre quem só testa manualmente até "parecer que funciona", porque ele consegue produzir a evidência que um auditor de qualquer uma dessas normas vai pedir.

Essa vantagem se manifesta de forma muito prática numa reunião de projeto: quando alguém pergunta "o que acontece se o obstáculo aparecer bem no instante em que o operador aciona a partida, e ao mesmo tempo o encoder falhar?", a resposta correta não é uma opinião de quem conhece bem o código, é a saída de um comando que qualquer pessoa da equipe pode rodar e conferir por conta própria. Essa é a diferença entre "eu acho que funciona assim" e "está provado que funciona assim, e aqui está o comando que você pode rodar para confirmar". Nenhuma norma de sistemas críticos aceita a primeira frase como evidência; todas aceitam a segunda.

### Fechamento

**[18:00–19:30 · TELA: editor — síntese e atividade prática]**

Recapitulando os pontos-chave desta aula. Um requisito em linguagem natural tolera ambiguidade de escala, de objeto e de instante de referência; um requisito formal exige que dois leitores cheguem sempre à mesma conclusão diante da mesma transição. "O robô deve parar rapidamente se houver obstáculo" admitiu, sozinho, pelo menos três leituras incompatíveis. Invariante, alcançabilidade, segurança e vivacidade cobrem a quase totalidade dos requisitos de um sistema ciberfísico como o NexaBot. REQ-SAFE-001, sem prazo, e REQ-SAFE-006, com prazo de $150\,\mathrm{ms}$, resolveram juntos a ambiguidade original de um único requisito mal escrito. E o próprio processo de formalizar um requisito, como vimos com REQ-SAFE-005, pode encontrar uma falha na especificação antes mesmo de qualquer verificação de código.

A atividade prática desta aula pede que você formalize dois requisitos adicionais do NexaBot — por exemplo, um limite de corrente de partida ou um requisito de registro de eventos de segurança. Para cada um, escreva o texto em linguagem natural como um cliente escreveria, identifique duas leituras ambíguas que ele admite, escreva o predicado Python equivalente à assinatura `verificar_transicao` e classifique o tipo de propriedade, justificando a escolha em duas frases.

**[19:30–20:00 · TELA: terminal — encerramento]**

Esta aula deixou pronto o vocabulário e o mecanismo para transformar requisito em predicado. A próxima aula usa exatamente esses predicados como entrada de um verificador que explora, de forma exaustiva, todo o espaço de estados do supervisor — e mostra, ao vivo, um bug real de prioridade sendo introduzido, diagnosticado por um contraexemplo, e corrigido, na mesma gravação. Até lá.

### Indicações de edição e recursos visuais

- 00:00–01:40 — manter zoom na tabela de saída do terminal, com destaque de cor sequencial em cada linha conforme a narração cita o tipo do requisito.
- Inserir Recurso visual 1 — as três leituras do requisito ambíguo se ramificando em três caixas — sobreposto à narração, aproximadamente em 01:20.
- Inserir Recurso visual 3 — quadro comparativo dos quatro tipos de propriedade formal — sobreposto ao editor, aproximadamente em 04:00.
- Inserir Recurso visual 4 — tabela dos sete REQ-SAFE classificados — em tela cheia, aproximadamente em 06:30.
- 08:30–14:00 — reduzir a velocidade de rolagem do terminal na leitura do contraexemplo; pausa de 2 segundos após a linha do contraexemplo antes de prosseguir a narração.
- Inserir Recurso visual 2 — diagrama de funil do requisito original decompondo-se em REQ-SAFE-001 e REQ-SAFE-006 — aproximadamente em 17:00.
- 19:40–20:00 — vinheta de encerramento com chamada para a Videoaula 10.

### Fontes e links de mídia

- BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008 — referência conceitual, sem reprodução de trecho externo.
- BERRY, Daniel M.; KAMSTIES, Erik; KRIEGER, Michael M. *From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity*. Waterloo: University of Waterloo, 2003 — referência conceitual, sem reprodução de trecho externo.
- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas e tabelas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 9 (`unidade_3.md`) e da saída real dos scripts de `projeto_nexabot/aula_09/`.

---

## Roteiro da Videoaula 10 — "O bug que a revisão de código não viu: contraexemplos em ação"

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 10 — Model checking: espaço de estados, LTL, CTL e contraexemplos.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de descrever o supervisor como um sistema de transições explorado por busca em largura, distinguir propriedades de segurança e de vivacidade pela forma do contraexemplo, ler e interpretar um contraexemplo real de violação, e explicar por que verificação exaustiva não é a mesma coisa que teste repetido.

**Mapa de tempo e telas:** 00:00 terminal com o bug já injetado · 01:40 editor: `nexabot/modelcheck.py`, a busca em largura · 04:00 editor: explosão de estados e LTL/CTL · 07:00 terminal: `01_explora_estados.py`, a versão correta · 09:30 terminal: `02_contraexemplo.py`, o bug, o contraexemplo e a correção na mesma tomada · 14:00 terminal: `03_ltl_ctl.py`, segurança versus vivacidade · 16:00 aplicação profissional e honestidade técnica · 18:00 pontos-chave e atividade · 19:30 encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: editor — aula_10/02_contraexemplo.py, função transition_com_bug já aberta]**

O arquivo já está aberto na função `transition_com_bug`, uma variante do supervisor com um erro de ordem de prioridade absolutamente realista: dentro do bloco que trata o estado MOVENDO, a condição de comando de partida do operador é verificada antes da condição de obstáculo, em vez de depois. É o tipo de bug que nasce de um copiar-e-colar malfeito — alguém reaproveitou o bloco de PARADO_OBSTACULO, que de fato testa comando de partida antes de qualquer outra coisa, e esqueceu que dentro de MOVENDO a prioridade tem que ser exatamente a oposta.

Em revisão de código, cada bloco isolado parece correto: "se há comando de partida, reabilita o torque" é uma frase perfeitamente razoável de se ler linha a linha. O defeito só aparece numa combinação específica de entradas, e é justamente esse tipo de defeito que a exploração exaustiva de estados foi desenhada para capturar, e que uma revisão manual, por mais cuidadosa que seja, tende a não perceber.

Esta aula é o coração da Unidade 3. Vamos ver esse bug ser introduzido, diagnosticado por um contraexemplo real e corrigido, na mesma tomada, sem cortes.

### Desenvolvimento conceitual

**[01:40–04:00 · TELA: editor — nexabot/modelcheck.py, a função explorar e a busca em largura]**

Fecho a variante bugada por um instante e abro `nexabot/modelcheck.py`, o verificador que vai fazer todo o trabalho pesado desta aula. Formalmente, o supervisor é um sistema de transições $(S, \Sigma, \rightarrow)$: seis estados $S$, um conjunto de entradas $\Sigma$ — o produto cartesiano dos seis campos booleanos de `Entradas` mais as amostras de velocidade usadas na verificação — e uma relação $\rightarrow$ dada pela função pura `transition`. A palavra "pura", que já destaquei na aula passada, agora ganha seu papel prático: é ela que permite ao verificador aplicar a função milhares de vezes sobre estados hipotéticos, sem jamais precisar desfazer efeito colateral algum.

O mecanismo é uma busca em largura clássica, a mesma estrutura de dados que se aprende em qualquer curso de algoritmos, aplicada aqui a um problema de engenharia de segurança. A função `explorar` parte do estado inicial OCIOSO, mantém uma fila de estados a visitar e, a cada estado retirado da fila, aplica a transição para absolutamente **todas** as entradas possíveis, registra cada resultado e enfileira todo estado ainda não visitado. O processo termina quando a fila esvazia — quando toda transição alcançável já foi registrada. A diferença central em relação a um teste aleatório, que pode rodar mil vezes sem jamais sortear a combinação exata que expõe um defeito, é que essa busca garante, por construção, que nenhuma transição alcançável fica de fora.

Um ponto merece destaque antes de seguir: a busca em largura, aqui, não simula o robô no tempo — ela não avança "um segundo por vez" como uma simulação da Unidade 2 faria. Ela enumera possibilidades lógicas, sem relação alguma com o relógio de parede. Isso é o que torna a verificação tão mais rápida do que qualquer campanha de simulação equivalente: em vez de escolher alguns cenários e rodá-los do início ao fim, o verificador examina, de uma só vez, toda combinação possível de estado corrente e entrada, e monta o grafo completo de transições alcançáveis como resultado.

**[04:00–07:00 · TELA: editor — explosão de estados, LTL e CTL]**

Dois conceitos adicionais valem ser fixados antes da demonstração. O primeiro é a explosão de estados: o espaço do NexaBot é pequeno — seis estados e $2^6 \times 2 = 128$ entradas distintas por estado, o que dá $768$ transições no total — e por isso cabe inteiro numa busca de menos de um milissegundo, como veremos daqui a pouco. Esse conforto não escala: cada autômato composto multiplica, não soma, o espaço de estados — $n$ vezes $m$ para autômatos de $n$ e $m$ estados. Um supervisor de armazém real, com múltiplos AGVs, estações de carga e zonas de exclusão coordenadas entre si, alcança rapidamente milhões ou bilhões de estados. Essa é a explosão de estados, o limite conhecido do *model checking* de estados explícitos como o que construímos aqui. Ferramentas de mercado como o NuSMV, citado na pilha desta disciplina como contraparte industrial, mitigam esse limite com representações simbólicas, baseadas em diagramas de decisão binária, que evitam enumerar estado a estado — mas essa necessidade só faz sentido depois de ver, como estamos vendo agora, exatamente onde a enumeração explícita deixa de caber.

O segundo conceito é o vocabulário formal para descrever propriedades sobre trajetórias. A lógica temporal linear, LTL, descreve propriedades sobre uma única trajetória de execução, com quatro operadores centrais: $G$, globalmente; $F$, eventualmente; $X$, no próximo estado; e $U$, até que. A lógica de árvore de computação, CTL, descreve propriedades sobre a árvore inteira de trajetórias possíveis, combinando um quantificador de caminho — $A$, para todo caminho, ou $E$, existe um caminho — com um operador temporal, formando combinações como $AG\,\phi$, $EF\,\phi$, $AF\,\phi$ e $EG\,\phi$. No vocabulário do NexaBot, REQ-SAFE-001 se escreve $AG\,\neg(\mathit{torque\_habilitado} \land \mathit{obstaculo})$ — em todo estado, de todo caminho, nunca torque habilitado com obstáculo presente; e REQ-SAFE-003 se escreve $EF\,(\mathit{estado} = \mathrm{MOVENDO})$ — existe algum caminho que leva a MOVENDO. O verificador que construímos aqui não implementa um motor genérico de LTL ou CTL; ele verifica, de forma especializada, invariantes de transição e alcançabilidade, os dois padrões que cobrem todos os REQ-SAFE desta disciplina. Mas o vocabulário CTL permite comunicar essas mesmas propriedades a qualquer ferramenta padrão de mercado, NuSMV incluído, sem perder precisão na tradução.

### Demonstração ao vivo

**[07:00–09:30 · TELA: terminal — aula_10/01_explora_estados.py]**

Rodo primeiro a versão correta, sem bug algum:

```
.venv/bin/python aula_10/01_explora_estados.py
```

A saída confirma, em números, tudo que acabei de descrever: 6 estados alcançáveis — OCIOSO, MOVENDO, DESACELERANDO, PARADO_OBSTACULO, FALHA e EMERGENCIA —, 768 transições exploradas, em um tempo de exploração de 0,884 milissegundos. Abaixo, a verificação de cada requisito de transição: REQ-SAFE-001, REQ-SAFE-002, REQ-SAFE-004 e REQ-SAFE-005, todos com zero violações sobre as 768 transições. E, separadamente, a verificação de alcançabilidade de REQ-SAFE-003: MOVENDO é alcançável em exatamente um passo, com a testemunha impressa na tela — a partir de OCIOSO, basta a entrada de comando de partida para chegar a MOVENDO. Essa é a linha de base: um sistema correto, com evidência de correção gerada em menos de um milissegundo, não por amostragem, mas por exame de toda transição possível.

**[09:30–13:00 · TELA: terminal — aula_10/02_contraexemplo.py, o bug e o contraexemplo]**

Agora, o momento central da unidade. Rodo:

```
.venv/bin/python aula_10/02_contraexemplo.py
```

O script primeiro roda o mesmo verificador contra a versão bugada que já mostrei no editor. A tela mostra: 768 transições exploradas — o tamanho do espaço não muda, só o comportamento em algumas transições —, e 8 violações de REQ-SAFE-001. Logo abaixo, o contraexemplo completo, do estado inicial até a violação: partindo de OCIOSO, o comando de partida leva a MOVENDO; em seguida, com comando de partida **e** obstáculo presentes ao mesmo tempo, o próximo estado permanece MOVENDO, e a saída mostra `torque_habilitado=True` com `obstaculo=True` — exatamente a condição que REQ-SAFE-001 proíbe. A linha final do relatório é explícita: na transição final, com obstáculo verdadeiro e comando de partida verdadeiro, a saída habilitou torque quando deveria ter desabilitado.

Esse contraexemplo de dois passos é a evidência que vale mais do que qualquer relatório de "propriedade violada" isolado: ele diz exatamente qual sequência de entradas leva o sistema à falha, o que permite depurar em minutos um defeito que, sem essa informação, poderia levar dias para ser reproduzido manualmente.

**[13:00–14:00 · TELA: terminal — a correção verificada na mesma tomada]**

Sem cortar a gravação, o mesmo script roda agora o verificador contra a versão corrigida, a que está de fato em `nexabot/supervisor.py`. A tela mostra, imediatamente abaixo do bloco anterior: 768 transições exploradas, zero violações de REQ-SAFE-001. E o script encerra com o resumo comparativo, lado a lado: bugada, 8 violações; corrigida, 0 violações. A correção, como o próprio comentário no código explica, é uma simples inversão de ordem: na versão com bug, o comando de partida é testado primeiro, e o obstáculo depois; na versão correta, o obstáculo é testado primeiro — ele manda —, o comando de parada em segundo, e o comando de partida sequer é testado dentro do bloco de MOVENDO, porque, com o supervisor já em movimento, receber "partir" de novo não deveria ter efeito nenhum. O código muda de duas linhas trocadas de posição, e o resultado muda de oito violações de segurança para zero.

**[14:00–16:00 · TELA: terminal — aula_10/03_ltl_ctl.py, segurança versus vivacidade]**

Fecho a demonstração com o terceiro script, que separa dois conceitos que até aqui tratamos quase como sinônimos. Rodo:

```
.venv/bin/python aula_10/03_ltl_ctl.py
```

A tela explica e em seguida verifica, na mesma execução, REQ-SAFE-001, REQ-SAFE-002 e REQ-SAFE-004 como propriedades de segurança — zero violações em 768 transições, cada uma verificada localmente, olhando cada transição isolada, sem seguir caminho algum até o infinito. Depois verifica REQ-SAFE-005, vivacidade, também com zero violações, e explica por quê: como o supervisor é determinístico, não existe não determinismo que permita adiar a resposta para depois — "eventualmente" colapsa em "na próxima transição", e por isso a propriedade de vivacidade pôde ser checada transição a transição, exatamente como uma invariante.

Para tornar o contraste concreto, o script constrói, sem alterar o supervisor real, uma variante deliberadamente bugada em que PARADO_OBSTACULO, ao receber obstáculo removido e comando de partida, permanece em PARADO_OBSTACULO em vez de ir para MOVENDO. Isso cria um ciclo de tamanho um que nunca alcança MOVENDO — e a verificação dessa variante contra REQ-SAFE-005 reporta 8 violações. Essa figura, um ciclo alcançável que evita para sempre o estado desejado, é exatamente o que um verificador de LTL chamaria de "lasso": a assinatura visual clássica de um contraexemplo de vivacidade, contraponto direto ao contraexemplo finito de duas transições que vimos há pouco para a segurança.

### Aplicação profissional

**[16:00–18:00 · TELA: editor — modelcheck.py, honestidade técnica]**

Uma pergunta profissional inevitável, e que vale colocar sem rodeios: um teste que passa mil vezes prova ausência de falha? A resposta é não. Um teste repetido mil vezes apenas não sorteou, nas mil tentativas, a combinação específica que expõe o defeito. A exploração exaustiva que acabamos de rodar não amostra: examina todas as $768$ transições possíveis, e é justamente por isso que ela encontrou, com certeza, as $8$ violações da versão bugada, e confirmou, com a mesma certeza, as $0$ violações da versão corrigida.

E aqui cabe uma honestidade técnica que precisa acompanhar qualquer aplicação séria de *model checking*: o que acabamos de provar é que o supervisor, **como modelado** em `nexabot/supervisor.py`, satisfaz REQ-SAFE-001, 002, 004 e 005. Essa prova não se estende automaticamente ao NexaBot físico se o modelo divergir da realidade — um sensor com atraso maior do que o suposto, uma entrada que o modelo não representa, um modo de falha do hardware que ninguém previu no vetor de `Entradas`. *Model checking* prova propriedades do modelo, não do sistema físico; a conclusão vale exatamente o quanto o modelo for fiel àquilo que ele pretende representar. Essa ressalva não diminui o valor do que fizemos: ela define, com precisão, o que uma prova formal garante e o que continua sendo responsabilidade de outras etapas — identificação de parâmetros, testes de integração, evidência de campo — completarem. É exatamente por isso que a Unidade 4 desta disciplina trata de gerar código a partir do modelo e demonstrar equivalência numérica entre os dois: sem essa etapa, tudo que provamos aqui perde ligação com o binário que realmente roda no NexaBot.

Nas normas de sistemas críticos que já citamos na aula anterior, essa distinção entre "prova sobre o modelo" e "prova sobre o sistema" é exatamente o que motiva exigências adicionais de rastreabilidade e de equivalência entre modelo e código — nenhuma delas aceita a prova formal como suficiente, sozinha, sem essa cadeia completa de evidências.

Isso também responde a uma objeção comum de quem vê pela primeira vez um verificador exaustivo funcionar: "se está tudo provado, por que ainda precisamos de testes de hardware e de campo?" Precisamos porque a prova é condicional ao modelo, e o modelo é uma simplificação deliberada da realidade — seis estados discretos e sete entradas booleanas, quando o NexaBot físico tem sensores com ruído, atrasos de comunicação e modos de falha de hardware que nenhum vetor de `Entradas` capturou ainda. Verificação formal não substitui teste de integração; ela elimina, com certeza matemática, uma classe inteira de erros de lógica de controle antes que qualquer teste de hardware precise ser gasto procurando por eles.

### Fechamento

**[18:00–19:30 · TELA: editor — síntese e atividade prática]**

Recapitulando os pontos-chave. O supervisor é um sistema de transições $(S, \Sigma, \rightarrow)$, e a busca em largura explora exaustivamente toda transição alcançável a partir do estado inicial. Explosão de estados é o crescimento multiplicativo que aparece ao compor autômatos, e é o limite prático do *model checking* de estados explícitos como o desta aula. LTL descreve trajetórias com $G$, $F$, $X$ e $U$; CTL descreve árvores de trajetórias com $AG$, $EF$, $AF$ e $EG$. Um teste sem falha observada não prova ausência de falha; exploração exaustiva não amostra, examina tudo. E, no NexaBot, vimos ao vivo $768$ transições produzindo $8$ ou $0$ violações de REQ-SAFE-001, dependendo unicamente da ordem de duas verificações dentro de um único bloco de código — a diferença entre um bug real de segurança e a correção que o elimina.

A atividade prática desta aula pede o seguinte: usando `aula_10/02_contraexemplo.py` como modelo, introduza uma segunda alteração deliberada no supervisor — por exemplo, remova a checagem de falha de encoder dentro do bloco de PARADO_OBSTACULO — e reporte qual requisito é violado, quantas das 768 transições violam esse requisito, e qual é o contraexemplo mais curto que o verificador encontra. Compare esse contraexemplo com o de REQ-SAFE-001 que vimos hoje: ele tem o mesmo tamanho? Envolve os mesmos estados?

**[19:30–20:00 · TELA: terminal — encerramento]**

Esta aula mostrou o mecanismo mais valioso da verificação formal: não apenas dizer que algo está errado, mas mostrar exatamente onde e como. A próxima aula leva essa mesma disciplina para uma dimensão que até aqui tratamos como implícita: o tempo. Vamos verificar, de forma exaustiva, o prazo de $150\,\mathrm{ms}$ de REQ-SAFE-006, e encontrar a fronteira exata em que ele deixa de ser cumprido. Até lá.

### Indicações de edição e recursos visuais

- Inserir Recurso visual 5 — grafo de estados do supervisor, com FALHA e EMERGENCIA destacados como absorventes — sobreposto ao editor, aproximadamente em 02:30.
- Inserir Recurso visual 6 — sequência de quadros mostrando o avanço da busca em largura pelos seis estados — aproximadamente em 03:00.
- Inserir Recurso visual 8 — quadro comparativo de sintaxe LTL/CTL — em tela cheia, aproximadamente em 06:00.
- 09:30–13:00 — este é o trecho mais importante da aula: não cortar; reduzir a velocidade de leitura do contraexemplo na tela e destacar com caixa vermelha a linha `torque_habilitado=True` seguida de caixa verde na re-execução corrigida.
- Inserir Recurso visual 7 — diagrama do contraexemplo de dois passos, com a transição final destacada e a anotação "REQ-SAFE-001 violado aqui" — sobreposto próximo de 11:00.
- 14:00–16:00 — usar tela dividida: à esquerda a verificação de segurança (contraexemplo finito), à direita o "lasso" da vivacidade, com uma seta animada percorrendo o ciclo.
- 19:40–20:00 — vinheta de encerramento com chamada para a Videoaula 11.

### Fontes e links de mídia

- BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008 — referência conceitual, sem reprodução de trecho externo.
- CLARKE, Edmund M.; GRUMBERG, Orna; PELED, Doron. *Model Checking*. Cambridge: MIT Press, 1999 — referência conceitual, sem reprodução de trecho externo.
- NuSMV. *NuSMV: a New Symbolic Model Checker*. Disponível em: <https://nusmv.fbk.eu/> — contraparte industrial citada, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas e tabelas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 10 (`unidade_3.md`) e da saída real dos scripts de `projeto_nexabot/aula_10/`.

---

## Roteiro da Videoaula 11 — "O prazo que ninguém violou em teste: verificando o pior caso do watchdog"

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 11 — Autômatos temporizados e o requisito de prazo.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicar o que são relógios, invariantes de localização e guardas temporais num autômato temporizado, verificar exaustivamente um requisito de prazo de pior caso, e justificar por que uma simulação típica não é evidência suficiente sobre o pior caso.

**Mapa de tempo e telas:** 00:00 terminal com o watchdog rodando · 01:40 editor: `nexabot/timed.py`, estados e relógio · 04:00 editor: invariante de localização e guarda temporal · 06:30 editor: pior caso versus alcançabilidade · 08:30 terminal: `01_watchdog.py`, cenário nominal · 10:30 terminal: `02_pior_caso.py`, a varredura completa · 14:00 aplicação profissional: UPPAAL e simulação típica · 16:30 terminal: `03_desafio.py` · 18:00 pausa para reflexão com contagem regressiva · 19:00 pontos-chave e encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: terminal — aula_11/01_watchdog.py, saída já na tela]**

A tela mostra a saída de um comando já executado: uma tabela com o pior caso do tempo que o NexaBot leva para zerar o torque depois de detectar um obstáculo — 5 períodos de amostragem, ou $25{,}0\,\mathrm{ms}$, dentro de um limite de $30$ períodos, $150\,\mathrm{ms}$. Esse número parece uma folga confortável. E, ainda assim, esta aula inteira existe porque uma folga confortável, medida num cenário, não é a mesma coisa que uma garantia de pior caso.

O REQ-SAFE-001, que verificamos na aula passada, garante, de forma combinacional, que nenhuma transição do supervisor habilita torque com obstáculo presente. Isso é uma abstração de tempo zero: o modelo lógico não representa nenhum atraso. No NexaBot físico, entre o instante em que o obstáculo aparece e o instante em que o torque efetivamente chega a zero, existem atrasos reais — o filtro de *debounce* do sensor, o tempo de varredura do laço de controle, a possibilidade concreta de um ciclo de atuação ser perdido por *jitter* de escalonamento. Em centenas de acionamentos manuais de bancada, o torque sempre chegou a zero bem antes de $150\,\mathrm{ms}$. Essa evidência, por mais numerosa que seja, não cobre necessariamente o pior caso — a combinação exata de atraso de detecção máximo com a perda de um ciclo de atuação, simultaneamente —, porque um teste manual amostra o que é fácil de reproduzir na bancada, não o que é matematicamente possível de acontecer.

### Desenvolvimento conceitual

**[01:40–04:00 · TELA: editor — nexabot/timed.py, os quatro estados e o relógio discreto]**

Abro `nexabot/timed.py`. Um autômato temporizado estende um sistema de transições comuns com relógios: variáveis que avançam com o tempo e que podem ser testadas e reiniciadas nas transições. A escolha de projeto mais importante deste módulo está no comentário do cabeçalho: o relógio conta em número inteiro de períodos de amostragem $T_s$, não em segundos contínuos — exatamente como um temporizador de hardware conta ciclos de *timer*, não frações reais de segundo. Isso torna a verificação exaustiva possível por simples enumeração direta, sem a maquinaria de zonas contínuas que ferramentas de tempo real como o UPPAAL exigem para relógios de valor real.

Quatro estados organizam o autômato. NORMAL é o estado em que nenhum gatilho de parada está ativo e o torque está livre. DETECTANDO representa o gatilho físico já presente, mas ainda não reconhecido pelo supervisor — o intervalo em que o filtro do sensor ainda está processando. COMANDANDO é o supervisor já reconhecendo o evento e cortando o torque. E ZERADO, tratado como absorvente nesta análise, é o torque fisicamente confirmado em zero.

Note a diferença de propósito em relação ao supervisor lógico da Aula 10: aquele modelo tinha seis estados que descreviam o **modo de operação** do robô — ocioso, movendo, em falha. Este autômato tem quatro estados que descrevem, isoladamente, **a evolução de um único evento de parada de emergência** no tempo, do instante em que o gatilho físico aparece até o instante em que o torque efetivamente zera. São dois modelos complementares, com propósitos distintos, e por isso vivem em módulos separados: `supervisor.py` decide o quê fazer; `timed.py` mede quanto tempo leva para a decisão se tornar realidade física.

**[04:00–06:30 · TELA: editor — invariante de localização, guarda temporal e as escolhas do ambiente]**

Duas construções organizam o comportamento do relógio dentro de cada estado. A invariante de localização é a condição sobre o relógio que precisa continuar válida enquanto o autômato permanece naquele estado — por exemplo, o relógio não pode ultrapassar o atraso máximo de detecção admitido enquanto o autômato ainda está em DETECTANDO. A guarda temporal é a condição sobre o relógio que habilita uma transição específica — por exemplo, só é possível avançar de DETECTANDO para COMANDANDO se o relógio ainda está dentro do limite permitido.

A cada período em DETECTANDO, o modelo dá ao ambiente duas escolhas não determinísticas: confirmar a detecção agora, passando a COMANDANDO, ou continuar atrasando, até o limite parametrizado como `atraso_deteccao_max`. A cada período em COMANDANDO, o ambiente escolhe entre um ciclo de atuação bem-sucedido, que leva direto a ZERADO, ou, uma única vez por trajetória, um ciclo de atuação perdido, que consome mais um período sem cortar o torque. Verificar exaustivamente significa, então, explorar **todas** as combinações dessas escolhas — não uma amostra delas — e reportar a maior contagem de períodos encontrada em qualquer trajetória possível até ZERADO.

**[06:30–08:30 · TELA: editor — pior caso como otimização sobre trajetórias]**

Vale marcar a diferença em relação à aula anterior. Na Aula 10, o verificador respondia perguntas do tipo "existe violação em alguma transição?" ou "existe caminho até este estado?" — perguntas de existência. Aqui, a pergunta muda de natureza: não é se um estado é alcançável, é qual é o **valor máximo** de uma grandeza — o relógio — sobre todas as trajetórias possíveis. É uma otimização sobre o espaço de trajetórias, não uma busca por um único caminho que satisfaça uma condição. Essa diferença é sutil no código, mas decisiva na engenharia: o resultado que importa não é "existe um jeito de zerar o torque a tempo", e sim "não existe jeito nenhum de zerar o torque fora do prazo".

### Demonstração ao vivo

**[08:30–10:30 · TELA: terminal — aula_11/01_watchdog.py]**

Rodo o cenário nominal de projeto:

```
.venv/bin/python aula_11/01_watchdog.py
```

A saída mostra os parâmetros do NexaBot: $T_s = 5{,}0\,\mathrm{ms}$, $d_{stop\_max} = 150\,\mathrm{ms}$. O cenário verificado admite atraso de detecção de até 2 períodos, mais 1 ciclo de atuação perdido, opcional. A tabela de grandezas mostra 6 caminhos explorados de forma exaustiva, limite do requisito em 30 períodos ou $150\,\mathrm{ms}$, pior caso encontrado em 5 períodos ou $25{,}0\,\mathrm{ms}$, margem de segurança de $125{,}0\,\mathrm{ms}$, e a confirmação de que REQ-SAFE-006 está satisfeito. Abaixo, a trajetória exata do pior caminho: DETECTANDO no instante zero, avançando período a período até o instante dois, então COMANDANDO nos instantes três e quatro, chegando a ZERADO no instante cinco — três períodos de atraso de detecção somados ao ciclo de atuação perdido, efetivamente usado nessa trajetória.

Seis caminhos, para um cenário que parece simples, já é mais do que uma pessoa testaria manualmente na bancada em uma sessão de testes. E, mesmo assim, seis caminhos explorados exaustivamente é pouco comparado ao que vem a seguir: até aqui fixamos o atraso máximo de detecção em 2 períodos, um valor de projeto específico. A próxima demonstração pergunta algo mais ambicioso — para qual atraso de detecção, entre todos os valores possíveis, o prazo de $150\,\mathrm{ms}$ deixa de ser cumprido?

**[10:30–14:00 · TELA: terminal — aula_11/02_pior_caso.py, a varredura completa]**

Agora transformamos o atraso de detecção de constante em parâmetro de varredura. Rodo:

```
.venv/bin/python aula_11/02_pior_caso.py
```

A saída é uma tabela extensa, varrendo o atraso de detecção de 0 a 32 períodos. Cada linha mostra o atraso admitido, o pior caso resultante em períodos e em milissegundos, e se o requisito continua satisfeito. O padrão é linear e absolutamente regular até certo ponto: com atraso zero, pior caso de 3 períodos, $15\,\mathrm{ms}$; com atraso de $10$ períodos, pior caso de $13$ períodos, $65\,\mathrm{ms}$; a folga cresce junto com o atraso admitido, sempre "SIM" na coluna de conformidade — até a linha de atraso igual a $27$ períodos, onde o pior caso soma exatamente $30$ períodos, exatamente $150\,\mathrm{ms}$, ainda "SIM", porque a verificação usa o operador menor-ou-igual. Na linha seguinte, atraso igual a $28$ períodos, o pior caso soma $31$ períodos, $155\,\mathrm{ms}$ — e a coluna muda para "NÃO", com a tabela destacando essa como a primeira violação. Todas as linhas seguintes, até $32$ períodos, continuam violando o requisito.

A conclusão impressa ao final transforma esse número de um exercício acadêmico numa restrição de engenharia concreta: o filtro de *debounce* do sensor de obstáculo do NexaBot precisa garantir um atraso de detecção estritamente menor que $28$ períodos, isto é, $140\,\mathrm{ms}$, para manter a margem de segurança de REQ-SAFE-006, considerando também um ciclo de atuação perdido no pior caso. Esse número — $28$ períodos, nem $27$ nem $29$ — não veio de uma regra de bolso; veio de examinar exaustivamente todas as trajetórias possíveis do autômato temporizado.

### Aplicação profissional

**[14:00–16:30 · TELA: editor — timed.py, UPPAAL e o argumento da simulação típica]**

Antes de fechar a aula, vale responder com precisão uma pergunta que qualquer engenheiro de bancada faria: por que dedicar uma verificação exaustiva a um watchdog que, em centenas de testes manuais, nunca chegou nem perto de $150\,\mathrm{ms}$? Porque uma simulação típica amostra um atraso de detecção próximo do valor médio e, na maioria das execuções, nem sequer inclui a perda de um ciclo, por essa ser rara por construção. O pior caso exige as duas condições no extremo, simultaneamente: o maior atraso admitido **e** a perda do ciclo, ao mesmo tempo, na mesma trajetória. A chance de uma execução aleatória de bancada sortear exatamente essa combinação é baixa o suficiente para que centenas de acionamentos manuais nunca a exponham espontaneamente — e é exatamente por isso que "nunca falhou em teste" não é evidência de que o pior caso respeita o prazo.

A contraparte industrial citada na correspondência ferramental desta disciplina é o UPPAAL, que verifica a mesma classe de propriedade sobre autômatos de tempo real contínuo, com relógios de valor real e guardas expressas em intervalos, verificados por zonas simbólicas em vez de enumeração direta como fizemos aqui. O mesmo watchdog, modelado em UPPAAL, trocaria o contador discreto por um relógio contínuo $x$, uma invariante $x \leq d_{atraso\_max}$ enquanto em DETECTANDO, e uma consulta temporizada equivalente a $AG\,(x \leq 0{,}150)$ restrita ao estado ZERADO. O modelo discreto que construímos aqui é exatamente o que um firmware amostrado a período fixo $T_s$ efetivamente implementa; o modelo contínuo do UPPAAL sustenta prazos que não são múltiplos exatos do período de amostragem, e por isso é a ferramenta certa quando essa restrição não se aplica.

Essa escolha entre modelo discreto e modelo contínuo não é uma questão de preferência estética entre ferramentas: é uma decisão de engenharia sobre o que o firmware realmente faz. Um microcontrolador amostrado a $T_s$ fixo só pode agir em múltiplos inteiros do período — ele não tem como "reagir em $2{,}7$ períodos"; a decisão acontece no próximo *tick* do temporizador, nem antes nem depois. Um modelo de tempo discreto captura exatamente essa restrição, o que o torna, para esta classe de firmware, uma representação mais fiel do sistema real do que um modelo de tempo contínuo seria — apesar de, à primeira vista, o tempo contínuo parecer "mais preciso". Precisão de modelo não é sobre representar o tempo da forma mais fina possível; é sobre representar o tempo da forma que o sistema realmente experimenta.

### Pausa para reflexão

**[16:30–18:30 · TELA: terminal — aula_11/03_desafio.py]**

Antes da pausa, um último resultado. Rodo:

```
.venv/bin/python aula_11/03_desafio.py
```

O script generaliza o autômato para tolerar não apenas um, mas um número arbitrário de ciclos de atuação perdidos consecutivos, com o atraso de detecção fixo no valor nominal de projeto, 2 períodos. A tabela mostra a varredura de zero a seis ciclos perdidos permitidos: com zero, pior caso de $4$ períodos, $20\,\mathrm{ms}$; com seis ciclos perdidos, pior caso de $10$ períodos, $50\,\mathrm{ms}$ — ainda folgadamente dentro do limite de $150\,\mathrm{ms}$. O requisito tolera todos os cenários testados até aqui, o que é evidência da folga real de projeto do watchdog, mas evidência de um tipo diferente da que a tabela anterior mostrou: aqui variamos ciclos perdidos com atraso fixo; ali variamos atraso com um ciclo perdido fixo. Nenhuma das duas varreduras, isoladamente, cobre a combinação de atraso extremo com múltiplos ciclos perdidos simultâneos — uma pergunta em aberto que fica registrada para quem quiser levar esse modelo adiante.

**[18:30–19:00 · TELA: terminal — pausa para reflexão, contagem regressiva]**

Pause a gravação por um instante e reflita sobre quatro perguntas. Primeira: quantas execuções aleatórias de bancada seriam necessárias para sortear, por acaso, a combinação exata de atraso máximo com ciclo perdido, entre as dezenas de trajetórias possíveis do autômato? Segunda: que outras grandezas do NexaBot têm essa mesma estrutura — pior caso raro, mas matematicamente inevitável? Terceira: a afirmação "o watchdog nunca ultrapassou $30\,\mathrm{ms}$ em teste" descreve o comportamento típico ou o pior caso — e que pergunta, feita a quem afirma isso, distingue as duas coisas? Quarta: qual parâmetro de projeto a equipe efetivamente controla para manter o pior caso dentro do prazo, e o que acontece com essa garantia se ele for relaxado sem reverificação?

*[indicação de edição: inserir tela de pausa com contagem regressiva de 10 segundos e o texto "Pense e continue"]*

Uma resposta madura para essas quatro perguntas reconhece que ausência de falha observada, por maior que seja o número de observações, nunca substitui a demonstração de que o pior caso matematicamente possível também respeita o prazo.

### Fechamento

**[19:00–19:40 · TELA: editor — pontos-chave e atividade prática]**

Recapitulando. Um autômato temporizado estende um sistema de transições com relógios testados e reiniciados nas transições. O modelo do watchdog usa tempo discreto, em períodos de $T_s = 5\,\mathrm{ms}$, refletindo exatamente como um firmware embarcado mede prazos. Invariante de localização e guarda temporal organizam quanto tempo permanecer num estado e quando é permitido transitar. Verificação de pior caso explora todas as escolhas do ambiente e reporta o valor máximo do relógio, não apenas se um estado é alcançável. E, no NexaBot, o prazo de $150\,\mathrm{ms}$ é respeitado até $27$ períodos de atraso de detecção — exatamente $150\,\mathrm{ms}$ no limite — e violado a partir de $28$ períodos, $155\,\mathrm{ms}$: uma fronteira exata, obtida por enumeração completa, não uma estimativa.

A atividade prática pede que você use `aula_11/02_pior_caso.py` para determinar o maior atraso de detecção, em milissegundos, que ainda mantém REQ-SAFE-006 satisfeito com ciclo perdido permitido, e repita a varredura com a opção de ciclo perdido desativada. Compare as duas margens de projeto resultantes e explique, em termos de engenharia, por que essa diferença justifica tratar a perda de um ciclo de atuação como evento reconhecido e limitado no escalonamento do firmware, e não apenas como uma ocorrência rara que se ignora.

**[19:40–20:00 · TELA: terminal — encerramento]**

Esta aula transformou "o watchdog nunca falhou" em uma fronteira numérica exata, obtida por enumeração exaustiva de todas as trajetórias temporizadas possíveis. A próxima aula fecha a unidade transformando o mesmo modelo verificado em uma suíte de testes gerada automaticamente, com cobertura medida em números — e mostra por que cem por cento de cobertura de linha de código, sozinho, ainda não prova coisa alguma. Até lá.

### Indicações de edição e recursos visuais

- Inserir Recurso visual 9 — autômato temporizado do watchdog, com os quatro estados, a invariante de localização em DETECTANDO e as duas escolhas não determinísticas — sobreposto ao editor, aproximadamente em 02:30.
- 08:30–10:30 — destacar em cor sólida a trajetória impressa (`DETECTANDO@t0 -> ... -> ZERADO@t5`) conforme a narração a percorre.
- Inserir Recurso visual 10 — gráfico de linha do atraso de detecção contra o pior caso em milissegundos, cruzando $150\,\mathrm{ms}$ entre 27 e 28 períodos — em tela cheia, aproximadamente em 12:00.
- 12:00–13:30 — congelar a tabela do terminal exatamente nas linhas de atraso 26, 27 e 28, com zoom, antes de prosseguir.
- Inserir Recurso visual 11 — comparação entre o autômato de tempo discreto do NexaBot e o equivalente contínuo em UPPAAL — sobreposto ao editor, aproximadamente em 15:30.
- 18:30–18:40 — tela de pausa com contagem regressiva de 10 segundos, texto "Pense e continue", sem áudio de fundo.
- 19:40–20:00 — vinheta de encerramento com chamada para a Videoaula 12.

### Fontes e links de mídia

- BENGTSSON, Johan; YI, Wang. Timed Automata: Semantics, Algorithms and Tools. In: DESEL, Jörg; REISIG, Wolfgang; ROZENBERG, Grzegorz (org.). *Lectures on Concurrency and Petri Nets*. Berlin: Springer, 2004. (LNCS, v. 3098). DOI: 10.1007/978-3-540-27755-2_3 — referência conceitual, sem reprodução de trecho externo.
- ALUR, Rajeev; DILL, David L. A theory of timed automata. *Theoretical Computer Science*, v. 126, n. 2, p. 183-235, 1994. DOI: 10.1016/0304-3975(94)90010-8 — referência conceitual, sem reprodução de trecho externo.
- UPPAAL. *UPPAAL Documentation*. Disponível em: <https://uppaal.org/documentation/> — contraparte industrial citada, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas e gráficos devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 11 (`unidade_3.md`) e da saída real dos scripts de `projeto_nexabot/aula_11/`.

---

## Roteiro da Videoaula 12 — "Cobertura não é correção: gerando e testando a partir do modelo"

**Vínculo com o plano de aprendizagem:** Unidade 3, Aula 12 — Testes gerados a partir do modelo e cobertura.

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de gerar casos de teste diretamente de um modelo formal, distinguir cobertura de estados, de transições e de condições de guarda, explicar por que cobertura de linha de código não é evidência de correção, e articular o limite entre o que o *model checking* prova e o que permanece em aberto até a Unidade 4.

**Mapa de tempo e telas:** 00:00 terminal com a suíte gerada rodando · 01:40 editor: `nexabot/mbt.py`, geração por percurso do grafo · 04:00 editor: três critérios de cobertura · 06:30 editor: Hypothesis e redução · 08:30 terminal: `01_gera_testes.py` · 10:30 terminal: `02_cobertura.py`, modelo e linhas lado a lado · 12:30 terminal: `03_hypothesis.py`, achar e reduzir o bug da Aula 10 · 14:30 terminal: `04_desafio.py` e a suíte pytest completa · 16:00 aplicação profissional: REQ-SAFE-007 e o limite do modelo · 18:00 pontos-chave e atividade · 19:00 transição para a Unidade 4 e encerramento.

### Abertura contextualizada

**[00:00–01:40 · TELA: terminal — aula_12/02_cobertura.py, relatório de cobertura já na tela]**

A tela mostra um relatório de cobertura já produzido: cobertura de estados do supervisor em $100\%$, cobertura de transições em $100\%$, e cobertura de linhas de código de `nexabot/supervisor.py`, medida pelo `coverage.py`, em $97\%$. Para um relatório tradicional de qualidade de software, esses três números fechariam o assunto satisfatoriamente. E, ainda assim, esta aula existe para mostrar que eles não fecham.

Lembre-se do bug de prioridade que introduzimos e corrigimos na Aula 10: comando de partida verificado antes do obstáculo dentro do bloco de MOVENDO, violando REQ-SAFE-001 em oito das $768$ transições. Esse bug conviveria perfeitamente com cem por cento de cobertura de linha, porque cada `if` daquele bloco é executado por algum teste isolado — nenhum teste isolado precisa encadear exatamente os dois passos, comando de partida seguido de obstáculo simultâneo, que expõem o defeito. Cobertura de linha mede se o código foi executado; não mede se a combinação certa de estados, entradas e histórico foi exercitada. Esta aula fecha a Unidade 3 mostrando como gerar uma suíte que responde à pergunta certa, e onde até essa suíte encontra seu próprio limite.

### Desenvolvimento conceitual

**[01:40–04:00 · TELA: editor — nexabot/mbt.py, geração por percurso do grafo]**

Abro `nexabot/mbt.py`. Teste baseado em modelo, ou MBT, deriva casos de teste automaticamente de um modelo formal — no NexaBot, o mesmo grafo de estados e transições que o verificador da Aula 10 já explorou — em vez de depender da intuição manual de um engenheiro escrevendo casos um a um. Isso torna a cobertura resultante mensurável, não uma promessa subjetiva de "testamos bastante".

A técnica de geração aqui é por **percurso do grafo**: para cada estado, escolhe-se a transição de exemplo que o revela pela primeira vez — essencialmente, a árvore geradora da própria busca em largura da Aula 10. Para seis estados, essa árvore tem cinco transições, e essas cinco transições já alcançam cem por cento de cobertura de estados. Mas o grafo completo do supervisor tem $25$ arestas distintas — pares origem-destino diferentes, sobre um máximo teórico de $6 \times 6 = 36$ pares possíveis, já que nem todo par de estados tem transição direta entre si. Cinco transições cobrem cem por cento dos estados e apenas vinte por cento das arestas. O número "cem por cento", isolado, esconde por completo essa insuficiência.

**[04:00–06:30 · TELA: editor — os três critérios de cobertura, em ordem crescente de exigência]**

Três critérios organizam essa hierarquia, em ordem crescente de exigência. Cobertura de estados é a fração dos estados visitados pela suíte — o critério mais fraco. Cobertura de transições é a fração dos pares origem-destino efetivamente percorridos, sempre mais exigente do que cobertura de estados, porque visitar todo estado não implica ter percorrido toda transição entre eles. E cobertura de condições de guarda é a fração das combinações de entrada que habilitam uma transição específica — o critério mais exigente de todos, porque uma mesma aresta do grafo pode ser alcançada por dezenas de combinações de entrada diferentes, e exercitar apenas uma delas não garante nada sobre as demais.

No grafo do supervisor, essa variação é enorme: a transição de MOVENDO para MOVENDO é alcançada por apenas $8$ das $128$ entradas possíveis a partir de MOVENDO; a transição de FALHA para FALHA, por $96$ delas. Uma suíte que cobre a aresta MOVENDO-MOVENDO com uma única combinação de entrada cobriu, na melhor das hipóteses, um oitavo do que essa aresta realmente representa.

Essa disparidade não é acidente de implementação — ela reflete a própria política de segurança do supervisor. FALHA é quase absorvente: a maioria das combinações de entrada, estando o sistema em FALHA, simplesmente mantém o sistema em FALHA, porque só o rearme explícito muda esse estado. MOVENDO, ao contrário, é sensível: poucas combinações de entrada mantêm o robô em movimento, porque qualquer uma de várias condições de segurança concorrentes já basta para tirá-lo dali. Uma suíte de cobertura bem projetada precisa refletir essa assimetria, dedicando mais casos às arestas mais sensíveis, e não distribuir esforço de teste igualmente entre todas elas.

**[06:30–08:30 · TELA: editor — Hypothesis, teste baseado em propriedades e redução]**

A segunda técnica desta aula ataca o problema de um ângulo diferente. Teste baseado em propriedades declara uma condição que deve valer para **qualquer** entrada de um domínio, e a ferramenta — aqui, a biblioteca Hypothesis — gera automaticamente sequências de entradas, tentando ativamente violar essa condição. No NexaBot, a propriedade é o próprio `verificar_transicao` de cada `Requisito`: para toda sequência de entradas aplicada passo a passo ao supervisor, todo requisito precisa continuar satisfeito. Diferente da suíte por percurso, que decide de antemão exatamente o que testar, o Hypothesis explora dirigido por heurísticas internas, incluindo sistematicamente casos de borda — exatamente o tipo de sequência curta e inesperada que expôs REQ-SAFE-001 na Aula 10, e que uma suíte manual dificilmente teria previsto sozinha.

Quando o Hypothesis encontra uma violação, a sequência bruta que ele sorteia é tipicamente longa e cheia de passos irrelevantes para a falha. A redução, em inglês *shrinking*, remove e simplifica passos, um de cada vez, testando a cada tentativa se a violação ainda persiste, até chegar à menor sequência que ainda a reproduz. Isso não é um detalhe cosmético: uma falha relatada como "sequência de trinta passos" é quase inútil para depurar; a mesma falha, reduzida a dois passos, aponta o defeito com precisão cirúrgica.

### Demonstração ao vivo

**[08:30–10:30 · TELA: terminal — aula_12/01_gera_testes.py]**

Rodo a geração da suíte:

```
.venv/bin/python aula_12/01_gera_testes.py
```

A saída mostra duas suítes. A primeira, cobertura de estados, com seis casos: um para cada estado alcançável, cada um listando os estados esperados no percurso e as entradas aplicadas para chegar lá — por exemplo, o caso que cobre DESACELERANDO percorre OCIOSO, MOVENDO, DESACELERANDO, com as entradas de comando de partida seguida de comando de parada. A segunda suíte, cobertura de transições, com vinte e cinco casos — um para cada uma das vinte e cinco arestas do grafo, incluindo transições de um estado de volta a si mesmo, como PARADO_OBSTACULO para PARADO_OBSTACULO. O resumo final confirma: seis casos de estados mais vinte e cinco casos de transições, trinta e um casos ao todo, todos gerados diretamente do modelo — nenhum escrito à mão — e todos executados com sucesso.

**[10:30–12:30 · TELA: terminal — aula_12/02_cobertura.py, modelo e linhas lado a lado]**

Agora, o relatório completo de cobertura. Rodo:

```
.venv/bin/python aula_12/02_cobertura.py
```

A primeira parte da saída confirma a cobertura de modelo: seis de seis estados, cem por cento; vinte e cinco de vinte e cinco transições, cem por cento — a suíte de trinta e um casos que acabamos de gerar cobre o grafo inteiro. A segunda parte roda o `coverage.py` de fato, medindo linhas de código executadas pela suíte pytest completa: `nexabot/mbt.py` em cem por cento; `nexabot/modelcheck.py` em setenta e um por cento; `nexabot/requisitos.py` em noventa e um por cento; `nexabot/supervisor.py` — o próprio supervisor sob verificação — em noventa e sete por cento; `nexabot/timed.py` em noventa e seis por cento; e o total dos módulos de verificação em oitenta e nove por cento, faltando quarenta e duas das trezentas e setenta e nove instruções, a maioria em ramos de erro e de depuração que a suíte de segurança não precisa exercitar.

Cem por cento de cobertura de modelo e noventa e sete por cento de cobertura de linha no supervisor: são números altos e genuinamente informativos, mas eles respondem perguntas diferentes uma da outra, e nenhuma delas, isoladamente, garante que a combinação exata de estados e entradas que expôs o bug da Aula 10 foi de fato exercitada.

**[12:30–14:30 · TELA: terminal — aula_12/03_hypothesis.py, achando e reduzindo o mesmo bug]**

Fecho o núcleo da demonstração conectando as duas técnicas ao mesmo bug da Aula 10. Rodo:

```
.venv/bin/python aula_12/03_hypothesis.py
```

A primeira parte roda a máquina de estados do Hypothesis contra o supervisor correto: nenhuma violação encontrada em nenhuma sequência sorteada. A segunda parte reintroduz a mesma variante bugada — comando de partida verificado antes do obstáculo em MOVENDO — e a tela mostra o Hypothesis encontrando a falha e reduzindo automaticamente a sequência até o menor caso: a partir de MOVENDO, uma única transição com comando de partida verdadeiro e obstáculo verdadeiro simultaneamente já viola REQ-SAFE-001, com torque habilitado na saída. É a mesma violação, na mesma condição, que o verificador exaustivo da Aula 10 encontrou por busca em largura — só que agora encontrada por uma técnica completamente diferente, sorteio aleatório dirigido por heurística seguido de redução automática. Duas rotas independentes convergindo para o mesmo contraexemplo mínimo é evidência de que ele é, estruturalmente, o menor caminho possível até essa violação — não um acidente de uma técnica específica.

**[14:30–16:00 · TELA: terminal — aula_12/04_desafio.py e a suíte pytest completa]**

Rodo os dois últimos comandos desta aula. Primeiro, o desafio:

```
.venv/bin/python aula_12/04_desafio.py
```

A saída identifica um buraco de cobertura concreto: a transição de DESACELERANDO para DESACELERANDO tem oito combinações de entrada distintas que a levam, e a suíte gerada por percurso do grafo exercita apenas uma delas — a primeira que a busca em largura encontrou. O script então roda um caso de teste extra, cobrindo uma segunda combinação, e confirma que ele também passa. Em seguida, a suíte pytest completa da unidade:

```
.venv/bin/python -m pytest tests/test_supervisor.py -v
```

A última linha da saída resume tudo que construímos ao longo de quatro aulas em uma única sentença: quarenta e três testes, todos passando. Esses quarenta e três testes não são quarenta e três casos escritos manualmente ao longo do semestre: são a suíte de trinta e um casos gerada por percurso do grafo, mais os casos de propriedades que codificam diretamente os seis requisitos de transição de `nexabot/requisitos.py`, mais o caso extra do desafio que acabamos de fechar. Cada um deles rastreia de volta a um requisito com identificador ou a uma aresta específica do grafo do supervisor — é essa cadeia de rastreabilidade, e não o número quarenta e três isoladamente, que dá valor a essa suíte como evidência.

### Aplicação profissional

**[16:00–18:00 · TELA: editor — REQ-SAFE-007 e o limite do que o modelo prova]**

Antes de fechar a unidade, é preciso retomar uma pendência deliberadamente aberta desde a Aula 9: REQ-SAFE-007, o limite de velocidade linear de $1{,}20\,\mathrm{m/s}$. Ele não apareceu em nenhuma verificação, e a razão é estrutural: o supervisor trata velocidade apenas de forma binária, por `parado()`, sem carregar o valor contínuo no vetor explorado pelo `modelcheck.py`. Verificá-lo de verdade exige planta, controlador, supervisor e domínio operacional explícito. O Hypothesis pode procurar contraexemplos em muitas combinações, mas não converte amostragem em prova exaustiva; por isso a lacuna permanece aberta nesta disciplina.

Esse limite específico abre a porta para o ponto de honestidade técnica que fecha a unidade inteira, e que já anunciei na Aula 10: *model checking* prova propriedades do modelo, não do sistema físico. A exploração exaustiva demonstrou, com certeza matemática, que o supervisor, como modelado, satisfaz REQ-SAFE-001 a REQ-SAFE-005, e que o autômato temporizado, como modelado, satisfaz REQ-SAFE-006 dentro dos parâmetros verificados. Nenhuma dessas provas se estende automaticamente ao NexaBot físico se o modelo divergir da realidade — um sensor com atraso maior do que o parametrizado, um firmware que perde mais de um ciclo sob carga real, uma velocidade que ultrapassa o previsto sob uma perturbação que ninguém modelou. A qualidade da conclusão depende inteiramente da fidelidade do modelo à realidade que ele pretende representar — e é exatamente isso que justifica a existência da Unidade 4: gerar código C a partir deste mesmo modelo e demonstrar equivalência numérica entre os dois, sem a qual tudo o que provamos nestas quatro aulas perde ligação com o binário que efetivamente roda embarcado no NexaBot.

### Fechamento

**[18:00–19:00 · TELA: editor — pontos-chave e atividade prática]**

Recapitulando os pontos-chave da unidade inteira. Teste baseado em modelo deriva casos de teste do próprio modelo formal, tornando a cobertura mensurável, não subjetiva. Cobertura de estados, de transições e de condições de guarda formam uma hierarquia de exigência crescente: uma árvore geradora mínima, com apenas cinco transições, já cobre cem por cento dos seis estados, mas apenas cinco das vinte e cinco arestas do grafo — vinte por cento —, e é exatamente por isso que a suíte que geramos e rodamos nesta aula vai além dessa árvore mínima, com vinte e cinco casos de transição, para de fato fechar as cem por cento de arestas que vimos no relatório de cobertura. O Hypothesis gera sequências dirigidas por heurística, incluindo casos de borda que uma suíte de exemplo tende a não prever, e a redução minimiza automaticamente qualquer falha até sua forma mínima. Cobertura de linha mede código executado, não combinações de estado e histórico — cem por cento dela convive, sem contradição, com um bug de sequência inteiro não coberto. E, finalmente, verificação formal prova propriedades do modelo, não do sistema físico; a validade de qualquer prova desta unidade depende inteiramente da fidelidade do modelo à realidade que o NexaBot vai efetivamente enfrentar em operação.

A atividade prática pede o seguinte: escolha três arestas do grafo do supervisor com número de entradas habilitantes muito diferente entre si — por exemplo, oito e noventa e seis — e projete, para cada uma, duas combinações de entrada distintas. Em seguida, rode `aula_12/03_hypothesis.py` com quinhentas sequências sobre o supervisor correto, em vez do número padrão, e reporte se alguma violação inesperada aparece. Se nenhuma aparecer, explique por escrito por que a ausência de violação em quinhentas sequências aleatórias não equivale à prova da exploração exaustiva da Aula 10 — a resposta está no que "aleatório" e "exaustivo" significam, e essa distinção é, no fundo, o argumento central desta unidade inteira.

**[19:00–20:00 · TELA: terminal — transição para a Unidade 4 e encerramento]**

Chegamos ao final da Unidade 3 com um resultado sólido: o modelo do supervisor está formalmente verificado, o requisito de prazo tem margem de projeto conhecida com precisão de um período de amostragem, e a suíte gerada a partir do próprio modelo tem cobertura medida em números, não presumida por inspeção visual do código. Falta a etapa que conecta tudo isso ao hardware que realmente vai operar dentro do armazém: transformar este mesmo modelo validado em código C, demonstrar equivalência numérica entre modelo e código, executá-lo em configuração *software-in-the-loop* e *hardware-in-the-loop*, e montar a matriz de rastreabilidade que liga cada REQ-SAFE ao teste que efetivamente o sustenta. A Unidade 4 é exatamente onde a correção que provamos aqui precisa sobreviver, sem se perder no caminho, até o binário embarcado que controla o NexaBot de verdade. Até lá.

### Indicações de edição e recursos visuais

- Inserir Recurso visual 12 — pirâmide dos três critérios de cobertura, estados na base, transições no meio, condições de guarda no topo — sobreposto ao editor, aproximadamente em 05:00.
- Inserir Recurso visual 13 — grafo do supervisor com as vinte e cinco arestas em cinza claro e as cinco cobertas por uma suíte mínima destacadas em cor sólida — aproximadamente em 03:30.
- 10:30–12:30 — congelar a tabela de cobertura de linhas com zoom nas colunas `Stmts`, `Miss` e `Cover`, destacando `supervisor.py` em 97%.
- Inserir Recurso visual 14 — sequência mostrando a redução de uma trajetória longa do Hypothesis até a sequência mínima de um passo — sobreposta ao terminal, aproximadamente em 13:30.
- Inserir Recurso visual 15 — diagrama com o modelo verificado de um lado, "provado", e o NexaBot físico do outro, ligados por seta tracejada rotulada "fidelidade do modelo — não garantida por este processo" — em tela cheia, aproximadamente em 17:00.
- 19:00–20:00 — vinheta de encerramento da Unidade 3, com chamada explícita para a Unidade 4.

### Fontes e links de mídia

- UTTING, Mark; LEGEARD, Bruno. *Practical Model-Based Testing: A Tools Approach*. San Francisco: Morgan Kaufmann, 2007 — referência conceitual, sem reprodução de trecho externo.
- MACIVER, David R.; HATFIELD-DODDS, Zac et al. Hypothesis: A New Approach to Property-Based Testing. *Journal of Open Source Software*, v. 4, n. 43, p. 1891, 2019. DOI: 10.21105/joss.01891 — referência conceitual, sem reprodução de trecho externo.
- AMMANN, Paul; OFFUTT, Jeff. *Introduction to Software Testing*. 2. ed. Cambridge: Cambridge University Press, 2016 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; diagramas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 12 (`unidade_3.md`) e da saída real dos scripts de `projeto_nexabot/aula_12/`.
