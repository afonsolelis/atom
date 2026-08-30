# Unidade 3 — Verificação formal e testes baseados em modelos

Disciplina: Model-Based Design for Cyber-Physical Systems
Professor-conteudista: Afonso Cesar Lelis Brandão

## Relação da unidade com a atuação profissional

Nas duas primeiras unidades, o NexaBot ganhou um modelo de planta fiel ao ensaio físico e um controlador com margem de estabilidade conhecida — isso responde a "o sistema funciona nos cenários que eu simulei?". Esta unidade responde a uma pergunta mais dura: "o sistema funciona em **todos** os cenários possíveis, incluindo aqueles em que ninguém pensou em testar?". Simulação amostra; verificação formal cobre o espaço inteiro — a diferença entre um protótipo de laboratório e um sistema qualificado para operar perto de pessoas.

Na indústria automotiva, a ISO 26262 exige, para os níveis mais altos de integridade de segurança (ASIL C e D), evidência de verificação formal e cobertura estrutural — não apenas "os testes passaram": um sistema de frenagem autônoma precisa provar que o comando de frenagem tem prioridade sobre qualquer outro modo, em qualquer sequência de eventos, não só nos cenários de pista. Na aeroespacial, a DO-178C impõe cobertura estrutural (MC/DC, nos níveis mais críticos) e rastreabilidade entre requisito, projeto e teste: um supervisor fly-by-wire não pode entrar em modo indefinido porque duas falhas concorrentes não foram previstas juntas no requisito. Dispositivos médicos programáveis vivem sob exigência equivalente (IEC 62304); acidentes reais já foram causados por condição de corrida entre estados que nenhum teste manual exercitou — o que a exploração exaustiva foi desenhada para encontrar antes do equipamento chegar ao paciente. Na robótica de armazém, caso central desta disciplina, a coexistência física entre AGVs e operadores transforma qualquer ambiguidade num requisito de parada de emergência em risco real: um robô de dezenas de quilos a mais de 1 m/s não tolera "geralmente para a tempo".

O que essas indústrias têm em comum não é a ferramenta, mas a disciplina de raciocínio: transformar requisito de segurança em propriedade matemática precisa, verificá-la exaustivamente, interpretar o contraexemplo quando a verificação falha, e gerar evidência rastreável ao requisito original. Esta unidade constrói essa disciplina, do texto ambíguo ao teste gerado por máquina.

## O que você verá nesta unidade

Na Aula 9, um requisito comum do NexaBot — "o robô deve parar rapidamente se houver obstáculo" — é dissecado em três leituras incompatíveis, de onde nascem os tipos de propriedade formal: invariante, alcançabilidade, segurança e vivacidade. Na Aula 10, o supervisor vira um sistema de transições explorado exaustivamente por busca em largura; um bug é introduzido de propósito, o verificador aponta a violação e devolve o contraexemplo, e LTL/CTL entram como vocabulário formal. Na Aula 11, o tempo deixa de ser implícito: um autômato temporizado modela o atraso real até o torque chegar a zero, e a verificação de pior caso mostra quando o prazo de 150 ms deixa de ser cumprido. Na Aula 12, o modelo verificado vira suíte de testes gerada automaticamente, com cobertura de estados, transições e guardas medida em números — e o Hypothesis mostra por que 100% de cobertura de linha ainda não prova nada.

O fio condutor é o supervisor de segurança do NexaBot — estados OCIOSO, MOVENDO, DESACELERANDO, PARADO_OBSTACULO, FALHA e EMERGENCIA — e os sete requisitos REQ-SAFE-001 a REQ-SAFE-007, progressivamente formalizados ao longo das quatro aulas.

## Aula 9 — Da especificação em texto à propriedade formal

### Situação-problema: um requisito, três leituras incompatíveis

O requisito chega à equipe assim, extraído de uma ata de reunião com a área de segurança do armazém: "o robô deve parar rapidamente se houver obstáculo." Ninguém discorda dele; ninguém, a partir dele, consegue decidir sozinho se uma implementação específica está correta. Um desenvolvedor lê "rapidamente" como "no próximo ciclo de controle"; outro lê "parar" como "velocidade do veículo zero", que fisicamente ainda leva centenas de milissegundos por inércia; um terceiro conta o prazo a partir do instante físico do obstáculo, outro a partir do instante em que o software, já passado o filtro do sensor, o reconhece. As três implementações são defensáveis diante do texto — e diferentes o suficiente para que uma passe em auditoria e outra cause um incidente.

### Por que a linguagem natural falha como especificação

Um requisito em linguagem natural tolera advérbios sem escala ("rapidamente"), verbos sem objeto explícito ("parar" o quê) e omite o instante de referência de qualquer prazo — não por erro de redação, mas porque depende de contexto compartilhado, que times diferentes preenchem de formas diferentes. Um requisito formal é aquele que dois leitores distintos, aplicando o mesmo processo mecânico de verificação, chegam sempre à mesma conclusão sobre se um comportamento o satisfaz — esse determinismo de julgamento, não elegância de prosa, separa requisito formalizado de requisito apenas escrito.

### As três leituras, resolvidas

Decompor o requisito expõe três perguntas sem resposta: (1) **quão rápido** é "rapidamente" — sem número, qualquer atraso satisfaz trivialmente; (2) **parar o quê** — o comando de torque (lógico, corte imediato) ou a velocidade linear (física, sujeita à inércia)?; (3) **a partir de que instante** o prazo é contado — do obstáculo físico, da detecção pelo sensor, ou da decisão do supervisor? A resolução do NexaBot separa as duas primeiras leituras em requisitos distintos. **REQ-SAFE-001** responde a "parar o quê" no nível lógico: nenhuma transição pode ter `torque_habilitado = True` com `obstaculo = True`, sem prazo algum — restrição instantânea, verificável a cada transição. **REQ-SAFE-006** responde a "quão rápido" e "a partir de quando": o torque físico chega a zero em no máximo 150 ms, contados do instante em que o gatilho físico está presente, já incorporando o pior caso de atraso de detecção e a perda de um ciclo de atuação. Um requisito ambíguo de uma linha vira dois requisitos formais, verificados por técnicas diferentes — o primeiro por exploração de estados (Aula 10), o segundo por autômato temporizado (Aula 11).

### Tipos de propriedade formal

- **Invariante:** condição que deve valer em todo estado ou transição alcançável — "isto nunca deixa de ser verdade".
- **Alcançabilidade:** existe pelo menos um caminho até um estado-alvo — "é possível chegar lá?", sem exigir que se chegue sempre.
- **Segurança (*safety*):** "nada de ruim acontece"; pode ser invariante de estado ou invariante *sobre a transição* — restrição sobre para onde o sistema pode ir a seguir.
- **Vivacidade (*liveness*):** "algo bom eventualmente acontece" — o sistema não fica preso esperando uma condição que nunca se resolve.

Por o supervisor ser determinístico, tanto REQ-SAFE-004 (segurança) quanto REQ-SAFE-005 (vivacidade) puderam ser reformuladas como invariantes de transição — "toda vez que a condição de disparo ocorre, a transição resultante é esta" —, o que simplifica a verificação sem perder o significado original.

### Do texto ao predicado executável

Em `nexabot/requisitos.py`, cada requisito é um objeto `Requisito` com identificador, um campo `tipo` e um predicado Python executável: `verificar_transicao(estado, entradas, saida, proximo_estado) -> bool` para invariantes e segurança/vivacidade sobre a transição, ou `estado_alvo(estado) -> bool` para alcançabilidade. Não sobra ambiguidade: o predicado devolve `True` ou `False` para uma transição específica, e qualquer pessoa que rode o mesmo código chega à mesma resposta.

#### Exemplo numérico completo: os sete REQ-SAFE classificados

| Requisito | Tipo | Verificação |
| --- | --- | --- |
| REQ-SAFE-001 | invariante | exploração de estados (Aula 10) |
| REQ-SAFE-002 | invariante | exploração de estados (Aula 10) |
| REQ-SAFE-003 | alcançabilidade | exploração de estados (Aula 10) |
| REQ-SAFE-004 | segurança (invariante de transição) | exploração de estados (Aula 10) |
| REQ-SAFE-005 | vivacidade (invariante de transição) | exploração de estados (Aula 10) |
| REQ-SAFE-006 | temporizado | autômato temporizado (Aula 11) |
| REQ-SAFE-007 | invariante | teste baseado em propriedades (Aula 12) |

REQ-SAFE-006 fixa numericamente "quão rápido": $d_{stop\_max} = 0{,}150\,\mathrm{s}$, que com $T_s = 5\,\mathrm{ms}$ equivale a exatamente 30 períodos de controle. Já REQ-SAFE-007 — velocidade linear ≤ 1,20 m/s — é invariante sobre uma grandeza contínua, fora do vetor de estados discreto do supervisor; fica de fora do `modelcheck.py` desta unidade e é adiado para a Aula 12, onde exige rodar planta e controlador junto do supervisor — um limite explícito da técnica, não um descuido.

### Laboratório da aula

Em `projeto_nexabot/aula_09/`, `01_requisitos.py` imprime os sete requisitos rastreados, classificados por tipo; o REQ-SAFE-007 aparece explicitamente sem predicado discreto. `02_do_texto_a_propriedade.py` submete uma formalização ingênua de REQ-SAFE-005 ao verificador, mostra o contraexemplo com falha de encoder concorrente e confirma zero violações após incluir as precondições de segurança. `03_desafio.py` pede a formalização de uma propriedade adicional, sobre freio e torque, e confere o predicado nas 768 transições sem reutilizar o identificador REQ-SAFE-007.

### Atividade prática

Formalize dois requisitos adicionais do NexaBot (por exemplo, limite de corrente de partida ou registro de eventos de segurança): escreva o texto em linguagem natural, identifique duas leituras ambíguas, escreva o predicado Python equivalente e classifique o tipo, justificando em duas frases.

### Síntese da aula

- Requisito em linguagem natural tolera ambiguidade de escala, objeto e instante; requisito formal exige que dois leitores cheguem sempre à mesma conclusão.
- "O robô deve parar rapidamente se houver obstáculo" admite pelo menos três leituras incompatíveis.
- Invariante, alcançabilidade, segurança e vivacidade cobrem a quase totalidade dos requisitos de sistemas ciberfísicos.
- REQ-SAFE-001 (lógica, sem prazo) e REQ-SAFE-006 (prazo de 150 ms) resolvem, juntos, a ambiguidade original.
- REQ-SAFE-007, sobre grandeza contínua, permanece como lacuna rastreada: exige planta, controlador e domínio operacional explícito, não apenas exploração do supervisor discreto.

### Roteiro da Videoaula 9 — "Um requisito, três leituras: da ambiguidade à propriedade formal"

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está em `roteiros_20min.md` desta unidade, usando a dissecação do requisito ambíguo do NexaBot como demonstração central.

### Referências da aula

- BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008.
- BERRY, Daniel M.; KAMSTIES, Erik; KRIEGER, Michael M. *From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity*. Waterloo: University of Waterloo, 2003.
- LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.

> **Recurso visual 1 — As três leituras do requisito ambíguo.** Ilustrar o texto original ramificando em três caixas: "quão rápido?", "parar o quê?" e "a partir de quando?", cada uma levando a uma implementação diferente.
> *Texto alternativo:* diagrama mostra um requisito em linguagem natural se ramificando em três interpretações distintas e incompatíveis.

> **Recurso visual 2 — Da ambiguidade a REQ-SAFE-001 e REQ-SAFE-006.** Diagrama de funil: o requisito original entra e sai como dois requisitos formais, um combinacional e um temporizado.
> *Texto alternativo:* diagrama de funil mostra um requisito ambíguo decomposto em dois requisitos formais distintos.

> **Recurso visual 3 — Os quatro tipos de propriedade formal.** Quadro comparativo com invariante, alcançabilidade, segurança e vivacidade, cada um com exemplo do NexaBot.
> *Texto alternativo:* tabela visual compara os quatro tipos de propriedade formal usando exemplos do supervisor do NexaBot.

> **Recurso visual 4 — Tabela dos sete REQ-SAFE classificados.** Reprodução em destaque da tabela do exemplo numérico, como cartão de referência da unidade.
> *Texto alternativo:* tabela lista os sete requisitos de segurança do NexaBot com tipo formal e método de verificação.

## Aula 10 — Model checking: espaço de estados, LTL, CTL e contraexemplos

### Situação-problema: o bug que passou em toda revisão manual

Uma reorganização no código do supervisor troca a ordem de duas verificações dentro do estado MOVENDO: em vez de avaliar o obstáculo primeiro, o código passa a avaliar o comando do operador antes de tudo — "o operador é quem manda no robô, faz sentido testar o comando dele primeiro". A revisão de código aprova. Testada manualmente com os cenários de sempre, a máquina se comporta como esperado: com obstáculo e sem comando, ela para; com comando e sem obstáculo, ela anda. O defeito só aparece na combinação em que as duas entradas chegam juntas: o operador mantém o comando de partida pressionado **enquanto** o sensor acusa obstáculo. Nessa combinação, o ramo do comando resolve a transição antes que o obstáculo seja sequer consultado, e o supervisor mantém o torque habilitado com um obstáculo à frente. Nenhum teste manual comum aplica as duas entradas ao mesmo tempo; um verificador exaustivo aplica todas as combinações em menos de um milissegundo.

### O modelo como sistema de transições, explorado por busca em largura

Formalmente, o supervisor é um sistema de transições $(S, \Sigma, \rightarrow)$: seis estados $S$, um conjunto de entradas $\Sigma$ (produto cartesiano dos seis campos booleanos de `Entradas` e das amostras de velocidade usadas na verificação) e uma relação $\rightarrow$ dada pela função pura `transition(estado, entradas) -> (estado', saida)`. A pureza — sem efeito colateral, mesma entrada sempre produz a mesma saída — permite ao verificador de `nexabot/modelcheck.py` aplicar a função milhares de vezes sem jamais precisar desfazer nada. O verificador não amostra: enumera por completo o espaço de entradas e percorre o grafo por busca em largura (BFS) a partir de OCIOSO, aplicando a transição para **toda** entrada possível a cada estado retirado da fila e enfileirando todo estado ainda não visitado, até a fila esvaziar — quando toda transição alcançável já foi registrada. Diferente de um teste aleatório, que pode rodar mil vezes sem sortear a combinação que expõe um defeito, essa busca garante, por construção, que nenhuma transição alcançável fica de fora.

### Explosão de estados

O espaço do NexaBot é pequeno — seis estados e $2^6 \times 2 = 128$ entradas por estado — e por isso cabe numa busca de menos de um milissegundo. Esse conforto não escala: cada autômato composto multiplica, não soma, o espaço de estados ($n \times m$ para autômatos de $n$ e $m$ estados). Um supervisor de armazém com múltiplos AGVs e zonas de exclusão alcança rapidamente milhões ou bilhões de estados — a **explosão de estados**, limite conhecido do *model checking* de estados explícitos. Ferramentas como o NuSMV mitigam isso com representações simbólicas (diagramas de decisão binária) que evitam enumerar estado a estado — fora do escopo aqui, mas cuja necessidade só faz sentido depois de ver onde a exploração explícita deixa de caber.

### LTL e CTL

LTL descreve propriedades sobre uma trajetória: $G$ (globalmente), $F$ (eventualmente), $X$ (próximo estado) e $U$ (até). CTL descreve propriedades sobre a árvore de trajetórias, combinando quantificador de caminho ($A$ — para todo; $E$ — existe) com operador temporal: $AG\,\phi$, $EF\,\phi$, $AF\,\phi$, $EG\,\phi$. No vocabulário do NexaBot, REQ-SAFE-001 é $AG\,\neg(\mathit{torque\_habilitado} \land \mathit{obstaculo})$; REQ-SAFE-003 é $EF\,(\mathit{estado} = \mathrm{MOVENDO})$. O verificador de `modelcheck.py` não implementa um motor genérico de LTL/CTL — verifica, de forma especializada, invariantes de transição e alcançabilidade, os dois padrões que cobrem os REQ-SAFE desta disciplina —, mas o vocabulário CTL permite comunicar essas mesmas propriedades a qualquer ferramenta padrão da indústria, NuSMV incluído.

### O contraexemplo como saída mais valiosa

Uma ferramenta que só responde "satisfeita" ou "violada" já seria útil, mas o que justifica modelar formalmente é o que vem junto de "violada": o **contraexemplo**, a sequência concreta de entradas que leva o sistema, passo a passo, até a falha. Isso também responde a uma pergunta recorrente: um teste que passa mil vezes prova ausência de falha? Não — apenas não amostrou a combinação que falha. Um verificador exaustivo não amostra: examina todas as combinações e, ao achar uma falha, entrega o caminho completo até ela.

#### Exemplo numérico completo: o bug, o contraexemplo e a correção

Sobre a versão correta, `explorar()` alcança **6 estados** e **768 transições** (6 × 128) em menos de **1 ms**, sem violações. Com a inversão de prioridade (comando de partida avaliado antes do obstáculo), a mesma exploração mantém 6 estados e 768 transições, mas reporta **8 violações** de REQ-SAFE-001. O contraexemplo mais curto:

```
OCIOSO
  --[{comando_partir, v=0.00}]--> MOVENDO
  --[{comando_partir, obstaculo, v=0.00}]--> MOVENDO
```

Duas transições bastam: a primeira parte do repouso e leva a MOVENDO, o que é legítimo; a segunda mantém o comando de partida e acrescenta o obstáculo. Na transição final, o supervisor com bug permanece em MOVENDO com `torque_habilitado = True` e `obstaculo = True` ao mesmo tempo — exatamente a combinação que REQ-SAFE-001 proíbe. Revertida a ordem de avaliação, a exploração volta a zero violações sobre as mesmas 768 transições. Estados e transições não mudam entre as duas versões: só o resultado da verificação de REQ-SAFE-001 muda — o que torna o contraexemplo preciso, isolando a falha em duas transições específicas.

A correção cabe em três linhas e é instrutiva por si só. Na versão com bug, o ramo `comando_partir` era avaliado primeiro e o ramo `obstaculo` depois. Na versão correta, o obstáculo é avaliado primeiro e `comando_partir` sequer é consultado dentro de MOVENDO: em um supervisor de segurança, a condição que protege pessoas precede a que atende conveniência de operação. Ordem de avaliação, em máquina de estados, é semântica — não é estilo.

### Laboratório da aula

Em `projeto_nexabot/aula_10/`, `01_explora_estados.py` roda `explorar()` e imprime 6 estados alcançáveis e 768 transições. `02_contraexemplo.py` verifica `transition_com_bug`, mostra 8 violações de REQ-SAFE-001 e o caminho mínimo, depois confirma zero violações na versão corrigida. `03_ltl_ctl.py` compara segurança e vivacidade e constrói um laço que viola a vivacidade. `04_desafio.py` convida o estudante a ativar uma das variantes de bug e interpretar o contraexemplo resultante.

### Atividade prática

Escreva em CTL a propriedade de REQ-SAFE-002 e de REQ-SAFE-004, explicando por que a segunda é invariante *sobre a transição*, não de estado. Depois, usando `02_contraexemplo.py` como modelo, introduza uma segunda alteração deliberada (por exemplo, remover a checagem de `falha_encoder` em PARADO_OBSTACULO) e reporte o requisito violado, quantas transições o violam e o contraexemplo mais curto.

### Síntese da aula

- O supervisor é um sistema de transições $(S, \Sigma, \rightarrow)$; a busca em largura explora exaustivamente toda transição alcançável.
- Explosão de estados é o crescimento multiplicativo ao compor autômatos — o limite prático do *model checking* de estados explícitos.
- LTL descreve trajetórias ($G$, $F$, $X$, $U$); CTL descreve árvores de trajetórias ($AG$, $EF$, $AF$, $EG$).
- Um teste sem falha observada não prova ausência de falha; exploração exaustiva não amostra, examina tudo.
- O contraexemplo é o produto mais valioso da verificação: no NexaBot, 6 estados e 768 transições produzem 0 ou 8 violações dependendo unicamente da ordem de duas verificações no código.

### Roteiro da Videoaula 10 — "O bug que a revisão de código não viu: contraexemplos em ação"

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está em `roteiros_20min.md` desta unidade, usando a introdução e correção do bug de prioridade como demonstração central.

### Referências da aula

- BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008.
- CLARKE, Edmund M.; GRUMBERG, Orna; PELED, Doron. *Model Checking*. Cambridge: MIT Press, 1999.
- NuSMV. *NuSMV: a New Symbolic Model Checker*. Disponível em: <https://nusmv.fbk.eu/>.

> **Recurso visual 5 — Grafo de estados do supervisor.** Diagrama com os seis estados e as transições entre eles, destacando FALHA e EMERGENCIA como absorventes.
> *Texto alternativo:* diagrama de grafo mostra os seis estados do supervisor do NexaBot e as transições entre eles.

> **Recurso visual 6 — Busca em largura no espaço de estados.** Sequência de quadros mostrando a fila de BFS avançando estado por estado até cobrir todos os seis.
> *Texto alternativo:* sequência ilustra o avanço da busca em largura pelo espaço de estados do supervisor.

> **Recurso visual 7 — O contraexemplo de duas transições.** Diagrama do caminho OCIOSO → MOVENDO → MOVENDO, com a transição final destacada, o obstáculo aceso e a anotação "REQ-SAFE-001 violado aqui: torque habilitado com obstáculo".
> *Texto alternativo:* diagrama mostra o contraexemplo de duas transições, terminando em movimento com obstáculo detectado e torque ainda habilitado, destacando a violação do requisito de parada.

> **Recurso visual 8 — Sintaxe LTL e CTL lado a lado.** Quadro com $G$, $F$, $X$, $U$ (LTL) e $AG$, $EF$, $AF$, $EG$ (CTL).
> *Texto alternativo:* tabela compara a sintaxe da lógica temporal linear e da lógica de árvore de computação.

## Aula 11 — Autômatos temporizados e o requisito de prazo

### Situação-problema: o watchdog que nunca falhou em nenhum teste

REQ-SAFE-001 garante, de forma combinacional, que nenhuma transição habilita torque com obstáculo presente — uma abstração de tempo zero. No NexaBot físico, entre o obstáculo aparecer e o torque chegar a zero existem atrasos reais: filtro de debounce do sensor, tempo de varredura do laço, possibilidade de um ciclo de atuação ser perdido por jitter. Em centenas de acionamentos manuais na bancada, o torque sempre chegou a zero bem antes de 150 ms. Essa evidência não cobre o pior caso — atraso de detecção máximo combinado com ciclo perdido, simultaneamente —, porque um teste manual amostra o que é fácil de reproduzir, não o que é matematicamente possível.

### Relógios, invariantes de localização e guardas temporais

Um autômato temporizado estende um sistema de transições com relógios que avançam com o tempo e podem ser testados e reiniciados nas transições. O modelo do watchdog em `nexabot/timed.py` usa tempo discreto: o relógio conta períodos de $T_s$ inteiros, como um temporizador de hardware conta ciclos, não segundos contínuos — o que torna a verificação exaustiva por enumeração direta, sem a maquinaria de zonas contínuas que o UPPAAL exige para relógios reais. Duas construções organizam o tempo: a **invariante de localização**, condição sobre o relógio válida enquanto o autômato permanece num estado, e a **guarda temporal**, condição que habilita uma transição. No NexaBot, `DETECTANDO` é o gatilho físico ainda não reconhecido; `COMANDANDO`, o supervisor já cortando torque; `ZERADO`, o torque em zero (absorvente nesta análise). A cada período em `DETECTANDO`, o ambiente escolhe confirmar ou continuar atrasando, até `atraso_deteccao_max`; em `COMANDANDO`, escolhe um ciclo de atuação bem-sucedido ou, uma única vez, um ciclo perdido. Verificar um requisito temporizado de pior caso significa explorar exaustivamente todas essas escolhas não determinísticas e reportar a maior contagem de períodos até `ZERADO`. Diferente da Aula 10, aqui o que importa não é se um estado é alcançável, mas o **valor máximo** de uma grandeza (o relógio) sobre todas as trajetórias.

### Por que o pior caso não aparece em simulação típica

Uma simulação típica amostra um atraso de detecção próximo do valor médio e, na maioria das execuções, não inclui perda de ciclo, por ser rara por construção. O pior caso exige as duas condições no extremo, simultaneamente: o maior atraso admitido **e** a perda do ciclo. A chance de amostrar por acaso exatamente essa combinação é baixa o suficiente para que centenas de execuções de bancada nunca a exponham — por isso "nunca falhou em teste" não é evidência de que o pior caso respeita o prazo.

### Contraparte industrial: UPPAAL

O UPPAAL verifica a mesma classe de propriedade sobre autômatos de tempo real **contínuo**, com relógios de valor real e guardas em intervalos, checados por zonas simbólicas em vez de enumeração direta. O mesmo watchdog, em UPPAAL, trocaria o contador discreto por um relógio contínuo $x$, uma invariante $x \leq d_{atraso\_max}$ em `DETECTANDO` e uma consulta $AG\,(x \leq 0{,}150)$ restrita a `ZERADO` — sustentando prazos que não são múltiplos exatos do período de amostragem, o que o modelo discreto construído aqui, fiel ao firmware real, não precisa expressar.

### Pausa para reflexão

O watchdog nunca falhou em nenhum teste de bancada, e ainda assim esta aula dedica uma verificação exaustiva a ele. Reflita: (1) quantas execuções aleatórias seriam necessárias para amostrar por acaso a combinação exata de atraso máximo com ciclo perdido, entre dezenas de trajetórias possíveis? (2) que outras grandezas do NexaBot têm a mesma estrutura de "pior caso raro, mas matematicamente inevitável"? (3) "o watchdog nunca ultrapassou 30 ms em teste" fala do comportamento típico ou do pior caso — que pergunta distingue as duas? (4) que parâmetro de projeto a equipe controla para manter o pior caso dentro do prazo, e o que acontece se ele for relaxado sem reverificação? Uma resposta madura reconhece que ausência de falha observada, por maior que seja o número de observações, nunca substitui a demonstração de que o pior caso matematicamente possível também respeita o prazo.

#### Exemplo numérico completo: a fronteira exata da violação

Com o valor de projeto do filtro do sensor, `atraso_deteccao_max = 2` períodos (10 ms), a verificação explora **6 caminhos** e reporta pior caso de **5 períodos = 25 ms** — bem dentro do limite de 150 ms (30 períodos). Tratando `atraso_deteccao_max` como parâmetro de varredura: em 27 períodos (135 ms de margem), a exploração encontra **56 caminhos** e o pior soma **30 períodos = 150 ms** — exatamente no limite, ainda conforme, porque a verificação usa $\leq$. Em 28 períodos (140 ms), encontra **58 caminhos** e o pior soma **31 períodos = 155 ms** — violação. A trajetória violadora sempre tem a mesma estrutura: atraso máximo permitido, período a período, mais o ciclo perdido consumido antes de zerar o torque. Isso transforma "150 ms" de número no papel em restrição de projeto verificada sobre o filtro do sensor: relaxá-lo além de 27 períodos exige reverificar REQ-SAFE-006.

### Laboratório da aula

Em `projeto_nexabot/aula_11/`, `01_watchdog.py` constrói o autômato com atraso máximo de detecção igual a 2 períodos e imprime 6 caminhos, pior caso de 5 períodos ($25\,\mathrm{ms}$) e a trajetória até `ZERADO`. `02_pior_caso.py` varre o atraso de 0 a 32 períodos e localiza a fronteira: 27 ainda atende exatamente $150\,\mathrm{ms}$; 28 leva a $155\,\mathrm{ms}$ e viola o requisito. `03_desafio.py` generaliza o número de ciclos de atuação perdidos consecutivamente e mede quanto a folga nominal tolera.

### Atividade prática

Usando `02_pior_caso.py`, confirme o maior `atraso_deteccao_max` que ainda satisfaz REQ-SAFE-006 quando um ciclo de atuação pode ser perdido. Depois, adapte `03_desafio.py` para ampliar a busca até que apareça a primeira quantidade de ciclos perdidos que viole o prazo. Registre a fronteira e explique por que o escalonamento precisa limitar explicitamente perdas consecutivas.

### Síntese da aula

- Autômato temporizado estende um sistema de transições com relógios testados e reiniciados nas transições.
- O modelo do watchdog usa tempo discreto, em períodos de $T_s = 5\,\mathrm{ms}$, refletindo como um firmware mede prazos.
- Invariante de localização e guarda temporal organizam quanto tempo permanecer num estado e quando transitar.
- Verificação de pior caso explora todas as escolhas do ambiente e reporta o valor máximo do relógio — não apenas alcançabilidade.
- O pior caso combina condições extremas simultâneas que simulação típica raramente amostra.
- No NexaBot, 150 ms é respeitado até 27 períodos (150 ms exatos) e violado a partir de 28 (155 ms) — fronteira exata, não estimativa.

### Roteiro da Videoaula 11 — "O prazo que ninguém violou em teste: verificando o pior caso do watchdog"

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está em `roteiros_20min.md` desta unidade, usando a varredura até a fronteira exata de violação como demonstração central.

### Referências da aula

- BENGTSSON, Johan; YI, Wang. Timed Automata: Semantics, Algorithms and Tools. In: DESEL, Jörg; REISIG, Wolfgang; ROZENBERG, Grzegorz (org.). *Lectures on Concurrency and Petri Nets*. Berlin: Springer, 2004. (LNCS, v. 3098). DOI: 10.1007/978-3-540-27755-2_3.
- UPPAAL. *UPPAAL Documentation*. Disponível em: <https://uppaal.org/documentation/>.
- ALUR, Rajeev; DILL, David L. A theory of timed automata. *Theoretical Computer Science*, v. 126, n. 2, p. 183-235, 1994. DOI: 10.1016/0304-3975(94)90010-8.

> **Recurso visual 9 — Autômato temporizado do watchdog.** Diagrama com os quatro estados, a invariante de localização em DETECTANDO e as duas escolhas não determinísticas por transição.
> *Texto alternativo:* diagrama de autômato temporizado mostra os quatro estados do watchdog com relógio, invariantes e guardas.

> **Recurso visual 10 — Varredura do atraso de detecção.** Gráfico de linha com `atraso_deteccao_max` no eixo horizontal e o pior caso em ms no eixo vertical, cruzando 150 ms entre 27 e 28 períodos.
> *Texto alternativo:* gráfico mostra o pior caso crescendo com o atraso admitido, cruzando 150 ms entre 27 e 28 períodos.

> **Recurso visual 11 — Discreto versus contínuo: NexaBot e UPPAAL.** Dois diagramas do mesmo autômato, um com relógio inteiro em períodos, outro com relógio real e guardas em intervalos.
> *Texto alternativo:* comparação entre o modelo de tempo discreto do watchdog e o modelo de tempo contínuo equivalente em UPPAAL.

## Aula 12 — Testes gerados a partir do modelo e cobertura

### Situação-problema: a suíte passa, mas o que ela realmente cobre?

A suíte automatizada do supervisor passa integralmente, e a ferramenta de cobertura reporta 100% de linhas executadas em `supervisor.py`. Para um relatório tradicional, isso fecharia o assunto — mas o bug de prioridade da Aula 10 poderia conviver com 100% de cobertura de linha, porque cada `if` é executado por algum teste isolado; nenhum precisa encadear os dois passos exatos (falha de encoder seguida de emergência sem rearme) que expõem o defeito. Cobertura de linha mede se o código foi executado, não se a combinação certa de estados e entradas foi exercitada.

### Teste baseado em modelo e critérios de cobertura

Teste baseado em modelo (*model-based testing*, MBT) deriva casos de teste automaticamente de um modelo formal — no NexaBot, o mesmo grafo já usado pelo verificador da Aula 10 — em vez de depender da intuição manual de um engenheiro, tornando a cobertura resultante mensurável, não uma promessa subjetiva. Três critérios, em ordem crescente de exigência: **cobertura de estados** (fração dos estados visitados), **cobertura de transições** (fração dos pares origem–destino percorridos, sempre mais exigente, pois visitar todo estado não implica percorrer toda transição) e **cobertura de condições de guarda** (fração das combinações de entrada que habilitam uma transição específica, mais exigente ainda, pois uma mesma aresta pode ser alcançada por dezenas de combinações diferentes).

No grafo do supervisor, a exploração da Aula 10 revela **25 arestas distintas** sobre um máximo teórico de $6 \times 6 = 36$ pares — não há, por exemplo, transição direta de OCIOSO para DESACELERANDO. Cada aresta é alcançada por número muito variável de entradas: MOVENDO → MOVENDO por apenas 8 das 128 a partir de MOVENDO; FALHA → FALHA por 96 delas.

### Geração de suíte por percurso do grafo

Uma suíte por **percurso do grafo** escolhe, para cada estado, a transição de exemplo que o revela pela primeira vez — a árvore geradora da própria busca em largura. Para 6 estados, essa árvore tem **5 transições**, que alcançam **100% de cobertura de estados**, mas apenas **5 das 25 arestas (20%)** e fração ainda menor de condições de guarda: o "100%" de estados, sozinho, esconde por completo essa insuficiência.

### Teste baseado em propriedades com Hypothesis e redução

Teste baseado em propriedades declara uma condição que deve valer para **qualquer** entrada de um domínio, e a ferramenta gera automaticamente sequências, tentando ativamente violá-la. No NexaBot, a propriedade é o próprio `verificar_transicao` de cada `Requisito`: para toda sequência de `Entradas` aplicada passo a passo, todo requisito deve continuar satisfeito. Diferente da suíte por percurso, que decide de antemão o que testar, o Hypothesis explora dirigido por heurísticas, incluindo casos de borda — o tipo de sequência de dois passos que expôs REQ-SAFE-001 na Aula 10, com duas entradas ativas ao mesmo tempo, que uma suíte manual tenderia a não prever.

Quando o Hypothesis encontra uma violação, a sequência bruta é tipicamente longa e cheia de passos irrelevantes. A **redução** (*shrinking*) remove e simplifica passos, um de cada vez, testando a cada tentativa se a violação persiste, até a menor sequência que ainda a reproduz. Reintroduzido o bug de prioridade e configurada a busca por violações de REQ-SAFE-001, a redução converge para a mesma sequência mínima de dois passos já identificada pelo verificador exaustivo — as duas técnicas chegam ao mesmo contraexemplo mínimo por rotas diferentes, porque ele é, estruturalmente, o menor caminho que viola o requisito.

### Por que cobertura de linha não é evidência de correção

Uma suíte de exemplo, escrita para exercitar cada ramo de `transition()` isoladamente, alcança 100% de cobertura de linha muito antes de precisar reproduzir a sequência de dois passos que expõe REQ-SAFE-001: o bloco que trata MOVENDO executa corretamente em isolamento tanto na versão certa quanto na com bug — a diferença só aparece quando o estado é alcançado por uma transição anterior específica e recebe, na seguinte, o comando de partida e o obstáculo ao mesmo tempo. Cobertura de linha, de transição e de guarda respondem perguntas diferentes; nenhuma isoladamente é evidência suficiente de correção.

#### Exemplo numérico completo: da suíte de 5 testes ao Hypothesis

Resumindo: a suíte por percurso, com **5 casos**, cobre **100% dos estados** e **20% das 25 arestas**, deixando a maioria das combinações de guarda de cada aresta não exercitada — cobrir as 25 exigiria no mínimo 25 casos. O Hypothesis, gerando 200 sequências aleatórias de até 10 passos contra os seis requisitos de transição, não reporta porcentagem de cobertura: para o supervisor correto, nenhuma sequência viola requisito algum; para a versão com bug, a primeira violação costuma aparecer nas primeiras dezenas de sequências, e a redução converge, de forma reprodutível, à mesma sequência mínima de 2 passos.

### REQ-SAFE-007 revisitado e o limite do que o modelo discreto prova

REQ-SAFE-007 — velocidade linear ≤ 1,20 m/s — não aparece em nenhuma verificação desta unidade até aqui, deliberadamente: o supervisor trata velocidade apenas de forma binária (`parado()`), sem o valor contínuo no vetor de estados que `modelcheck.py` explora. Verificá-lo exige rodar planta, controlador e supervisor juntos, definir o domínio operacional e checar a propriedade sobre toda trajetória relevante. O Hypothesis pode amostrar esse domínio e encontrar contraexemplos, mas não transforma uma amostra em prova exaustiva; por isso o requisito continua marcado como lacuna, em vez de ser declarado verificado. Esse limite fecha a unidade com o ponto de honestidade técnica central: ***model checking* prova propriedades do modelo, não do sistema físico**. A exploração exaustiva demonstrou, com certeza matemática, que o supervisor **como modelado** satisfaz REQ-SAFE-001 a REQ-SAFE-005, e que o autômato temporizado **como modelado** satisfaz REQ-SAFE-006 dentro dos parâmetros verificados — nenhuma dessas provas se estende automaticamente ao NexaBot físico se o modelo divergir da realidade. A qualidade da conclusão depende inteiramente da fidelidade do modelo — o que justifica a Unidade 4, ao gerar código do mesmo modelo e demonstrar equivalência numérica entre modelo e código.

### Transição para a Unidade 4

O modelo do supervisor está formalmente verificado, o requisito de prazo tem margem de projeto conhecida e a suíte gerada a partir do modelo tem cobertura medida, não presumida. Falta transformar o modelo validado em código C, demonstrar equivalência numérica entre modelo e código, executá-lo em SIL e HIL, e montar a matriz de rastreabilidade que liga cada REQ-SAFE ao teste que o sustenta — a Unidade 4 é onde a correção provada aqui precisa sobreviver à travessia até o binário embarcado.

### Laboratório da aula

Em `projeto_nexabot/aula_12/`, `01_gera_testes.py` produz 6 casos para cobertura de estados e 25 para cobertura de transições, todos executados com sucesso. `02_cobertura.py` coloca cobertura do modelo e cobertura de linhas lado a lado. `03_hypothesis.py` executa a máquina de estados contra o supervisor correto e contra uma variante com bug, reduzindo o contraexemplo ao caso mínimo de dois passos. `04_desafio.py` mostra que cobrir uma aresta não cobre todas as combinações de entradas que a habilitam e pede um caso adicional.

### Atividade prática

Escolha três arestas com número de entradas habilitantes muito diferente e projete duas combinações distintas para cada uma. Depois, rode `03_hypothesis.py` sobre o supervisor correto; se nenhuma violação aparecer, explique por que essa ausência não equivale à prova da exploração exaustiva da Aula 10.

### Síntese da aula

- Teste baseado em modelo deriva casos de teste do próprio modelo formal, tornando a cobertura mensurável, não subjetiva.
- Cobertura de estados, transições e condições de guarda formam hierarquia de exigência crescente; 100% em um não implica cobertura alta no seguinte — no supervisor, 5 casos cobrem 100% dos estados mas só 20% das 25 arestas.
- Hypothesis gera sequências dirigidas por heurística, incluindo casos de borda que suítes de exemplo tendem a não prever; a redução minimiza automaticamente uma falha até sua forma mínima.
- Cobertura de linha mede código executado, não combinações de estado e histórico; 100% dela convive com um bug de sequência não coberto.
- REQ-SAFE-007, sobre grandeza contínua, não foi verificado nesta unidade; testes sobre o modelo fechado podem procurar violações, mas uma conclusão de garantia exige domínio e critério de cobertura explícitos.
- *Model checking* prova propriedades do modelo, não do sistema físico; a validade depende inteiramente da fidelidade do modelo à realidade.

### Roteiro da Videoaula 12 — "Cobertura não é correção: gerando e testando a partir do modelo"

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está em `roteiros_20min.md` desta unidade, usando a progressão da suíte por percurso ao Hypothesis com *shrinking* como demonstração central.

### Referências da aula

- UTTING, Mark; LEGEARD, Bruno. *Practical Model-Based Testing: A Tools Approach*. San Francisco: Morgan Kaufmann, 2007.
- MACIVER, David R.; HATFIELD-DODDS, Zac et al. Hypothesis: A New Approach to Property-Based Testing. *Journal of Open Source Software*, v. 4, n. 43, p. 1891, 2019. DOI: 10.21105/joss.01891.
- AMMANN, Paul; OFFUTT, Jeff. *Introduction to Software Testing*. 2. ed. Cambridge: Cambridge University Press, 2016.

> **Recurso visual 12 — Três critérios de cobertura em pirâmide.** Pirâmide com cobertura de estados na base, transições no meio e condições de guarda no topo.
> *Texto alternativo:* diagrama em pirâmide mostra os três critérios de cobertura em ordem crescente de exigência.

> **Recurso visual 13 — Suíte de 5 testes sobre o grafo de 25 arestas.** Grafo com as 25 arestas em cinza claro e as 5 cobertas pela suíte mínima destacadas em cor sólida.
> *Texto alternativo:* diagrama de grafo mostra as vinte e cinco transições do supervisor, com cinco destacadas como cobertas por uma suíte mínima.

> **Recurso visual 14 — Redução de um contraexemplo pelo Hypothesis.** Sequência de caixas mostrando uma trajetória longa encolhendo, passo a passo, até a sequência mínima de 2 passos.
> *Texto alternativo:* sequência ilustra a redução automática de um contraexemplo longo até sua forma mínima de duas transições.

> **Recurso visual 15 — Onde o modelo termina e o sistema físico começa.** Diagrama com o modelo verificado de um lado ("provado") e o NexaBot físico do outro, ligados por seta tracejada rotulada "fidelidade do modelo — não garantida por este processo".
> *Texto alternativo:* diagrama contrasta o modelo formalmente verificado com o sistema físico, indicando que a validade da prova depende da fidelidade do modelo.

## Atividades, síntese e material complementar

### Quiz não avaliativo

**Questão 1.** O requisito "o robô deve parar rapidamente se houver obstáculo" foi decomposto em REQ-SAFE-001 (torque nunca habilitado com obstáculo presente, sem prazo) e REQ-SAFE-006 (torque físico zero em no máximo 150 ms). Essa decomposição em dois requisitos, em vez de um único mais elaborado, se justifica principalmente porque:

a. REQ-SAFE-001 é mais importante do que REQ-SAFE-006 e por isso merece identificador próprio.
b. um requisito formal nunca pode ter mais de uma condição numérica.
*c. as duas leituras — "parar o quê" (instantâneo, lógico) e "quão rápido/a partir de quando" (temporal, físico) — exigem técnicas de verificação diferentes.
d. REQ-SAFE-006 substitui integralmente REQ-SAFE-001, tornando-o redundante.
e. a linguagem natural exige sempre exatamente dois requisitos formais por frase.

*Feedback conceitual:* REQ-SAFE-001 é restrição instantânea sobre variável de software, verificável por exploração de estados; REQ-SAFE-006 é restrição de tempo real sobre variável física, exigindo autômato temporizado. Misturar as duas leituras num só predicado misturaria técnicas de verificação incompatíveis.

**Questão 2.** Uma suíte de testes do supervisor, escrita para exercitar cada ramo de `transition()` isoladamente, alcança 100% de cobertura de linha em `supervisor.py`. O bug de prioridade que permitia sair de FALHA sem rearme diante de emergência concorrente não é detectado por essa suíte. A explicação mais precisa é que:

a. a suíte está mal escrita e deveria ser descartada por completo.
b. cobertura de linha de 100% é impossível em código com múltiplos `if`.
*c. cobertura de linha mede se cada instrução foi executada por algum teste isolado, não se a combinação específica de estados e entradas ao longo do tempo que expõe o defeito foi exercitada.
d. o bug só pode ser encontrado por revisão de código, nunca por teste automatizado.
e. o defeito está em uma linha de código que não pertence a `supervisor.py`.

*Feedback conceitual:* cada bloco que trata FALHA executa corretamente quando testado isoladamente — a diferença só aparece numa sequência específica de duas transições. Cobertura de linha mede código executado, não combinações de estado e histórico; por isso pode chegar a 100% sem expor o defeito.

### Síntese da unidade

- Requisito em linguagem natural tolera ambiguidade de escala, objeto e instante de referência; requisito formal exige que dois leitores cheguem sempre à mesma conclusão.
- Invariante, alcançabilidade, segurança e vivacidade cobrem a quase totalidade dos requisitos de segurança de sistemas ciberfísicos, cada um apontando para uma técnica de verificação.
- Exploração exaustiva por busca em largura garante cobertura total do espaço declarado, ao custo do crescimento multiplicativo da explosão de estados.
- LTL e CTL fornecem vocabulário formal ($G$, $F$, $X$, $U$; $AG$, $EF$, $AF$, $EG$) independente de qualquer ferramenta específica.
- O contraexemplo é o produto mais valioso da verificação formal; zero violações é garantia categoricamente diferente de "nenhum teste falhou até agora".
- Autômatos temporizados verificam prazos de pior caso explorando exaustivamente as escolhas do ambiente, que simulação típica raramente amostra em conjunto.
- Cobertura de estados, transições e guardas formam hierarquia crescente; teste baseado em propriedades com redução encontra e minimiza casos que uma suíte de exemplos deixaria de fora.
- *Model checking* prova propriedades do modelo formal, nunca diretamente do sistema físico; a validade prática depende da fidelidade do modelo à realidade.

### Material complementar

#### Direto da Fonte

**Texto provocativo:** As Aulas 9 e 10 constroem, do zero, um verificador de estados explícitos e apresentam LTL e CTL. Este livro é a referência que sustenta ambos, com o mesmo rigor usado aqui, e explica exatamente por que a busca em largura funciona — e onde deixa de caber.

**Referência:** BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008. Capítulos sobre sistemas de transição, LTL e CTL.

**Link de acesso:** disponível na Biblioteca Virtual da instituição.

**Aula indicada:** Aula 10, após "LTL e CTL".

#### Para Mergulhar no Assunto

**Texto provocativo:** Este livro não é sobre *model checking* — é sobre por que sistemas seguros falham mesmo quando cada componente funciona corretamente isolado. Ilumina, em retrospecto, exatamente o tipo de falha que esta unidade caça: a combinação de condições concorrentes que nenhuma peça isolada deixava prever.

**Referência:** LEVESON, Nancy G. *Engineering a Safer World: Systems Thinking Applied to Safety*. Cambridge: MIT Press, 2011.

**Link de acesso:** disponível na Biblioteca Virtual da instituição.

**Aula indicada:** Aula 9, após "Por que a linguagem natural falha como especificação".

#### Podcast

**Texto provocativo:** Antes de escrever sobre métodos formais profissionalmente, Hillel Wayne deu esta palestra mostrando, ao vivo, como o TLA+ encontra bugs de concorrência que testes unitários sistematicamente não encontram. É a mesma lógica desta unidade: modelar, verificar exaustivamente, deixar a ferramenta devolver o contraexemplo.

**Referência:** STRANGE LOOP. *Tackling Concurrency Bugs with TLA+ — Hillel Wayne*. [S. l.: s. n.], 2017. 1 vídeo. Publicado no YouTube.

**Link de acesso:** <https://www.youtube.com/watch?v=_9B__0S21y8>. Acesso em: 30 jul. 2026.

**Trecho obrigatório:** 00:00–25:00 (25 minutos), limitado à motivação e à demonstração de um contraexemplo encontrado pela ferramenta.

**Aula indicada:** Aula 10, após "Explosão de estados".

#### Artigo científico

**Texto provocativo:** Engenheiros da AWS descrevem como métodos formais deixaram de ser curiosidade acadêmica e passaram a integrar o projeto de sistemas de produção em escala global — incluindo bugs de concorrência que só se manifestariam sob condições raras, a mesma categoria de defeito que o contraexemplo da Aula 10 exemplifica em escala reduzida.

**Referência:** NEWCOMBE, Chris et al. How Amazon Web Services Uses Formal Methods. *Communications of the ACM*, v. 58, n. 4, p. 66-73, 2015. DOI: 10.1145/2699417.

**Link de acesso:** <https://doi.org/10.1145/2699417>. Acesso em: 30 jul. 2026.

**Aula indicada:** Aula 12, após "Por que cobertura de linha não é evidência de correção".

## Referências da unidade

ALUR, Rajeev; DILL, David L. A theory of timed automata. *Theoretical Computer Science*, v. 126, n. 2, p. 183-235, 1994. DOI: 10.1016/0304-3975(94)90010-8.

AMMANN, Paul; OFFUTT, Jeff. *Introduction to Software Testing*. 2. ed. Cambridge: Cambridge University Press, 2016.

BAIER, Christel; KATOEN, Joost-Pieter. *Principles of Model Checking*. Cambridge: MIT Press, 2008.

BENGTSSON, Johan; YI, Wang. Timed Automata: Semantics, Algorithms and Tools. In: DESEL, Jörg; REISIG, Wolfgang; ROZENBERG, Grzegorz (org.). *Lectures on Concurrency and Petri Nets*. Berlin: Springer, 2004. (LNCS, v. 3098). DOI: 10.1007/978-3-540-27755-2_3.

BERRY, Daniel M.; KAMSTIES, Erik; KRIEGER, Michael M. *From Contract Drafting to Software Specification: Linguistic Sources of Ambiguity*. Waterloo: University of Waterloo, 2003.

CLARKE, Edmund M.; GRUMBERG, Orna; PELED, Doron. *Model Checking*. Cambridge: MIT Press, 1999.

LEE, Edward Ashford; SESHIA, Sanjit A. *Introduction to Embedded Systems: A Cyber-Physical Systems Approach*. 2. ed. Cambridge: MIT Press, 2017.

LEVESON, Nancy G. *Engineering a Safer World: Systems Thinking Applied to Safety*. Cambridge: MIT Press, 2011.

MACIVER, David R.; HATFIELD-DODDS, Zac et al. Hypothesis: A New Approach to Property-Based Testing. *Journal of Open Source Software*, v. 4, n. 43, p. 1891, 2019. DOI: 10.21105/joss.01891.

NEWCOMBE, Chris et al. How Amazon Web Services Uses Formal Methods. *Communications of the ACM*, v. 58, n. 4, p. 66-73, 2015. DOI: 10.1145/2699417.

NuSMV. *NuSMV: a New Symbolic Model Checker*. Disponível em: <https://nusmv.fbk.eu/>. Acesso em: 30 jul. 2026.

STRANGE LOOP. *Tackling Concurrency Bugs with TLA+ — Hillel Wayne*. [S. l.: s. n.], 2017. 1 vídeo. Publicado no YouTube. Disponível em: <https://www.youtube.com/watch?v=_9B__0S21y8>. Acesso em: 30 jul. 2026.

UPPAAL. *UPPAAL Documentation*. Disponível em: <https://uppaal.org/documentation/>. Acesso em: 30 jul. 2026.

UTTING, Mark; LEGEARD, Bruno. *Practical Model-Based Testing: A Tools Approach*. San Francisco: Morgan Kaufmann, 2007.
