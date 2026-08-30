# Questionário — Unidade 3

Quantidade obrigatória: 40 questões — 20 de asserção-razão (1 a 20) e 20 de interpretação (21 a 40).
Cinco alternativas por questão (a-e); alternativa correta marcada com `*` imediatamente antes da letra.
Distribuição da letra correta: 8 questões para cada uma das letras a, b, c, d, e, no total das 40 questões.

## Questões

### Asserção-razão

**1.** I. O requisito "o robô deve parar rapidamente se houver obstáculo" admite pelo menos três leituras incompatíveis: quão rápido é "rapidamente", o que exatamente deve parar, e a partir de que instante o prazo é contado.

PORQUE

II. Todo requisito formal deve ser expresso em uma única frase de linguagem natural, sem predicado executável associado, para preservar sua legibilidade pela equipe de segurança.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**2.** I. REQ-SAFE-001 é verificável por exploração de estados porque expressa uma restrição instantânea sobre variáveis lógicas do supervisor, sem depender de tempo decorrido.

PORQUE

II. REQ-SAFE-001 estabelece que nenhuma transição pode ter `torque_habilitado = True` simultaneamente com `obstaculo = True`, condição avaliável a cada transição isolada, sem necessidade de relógio.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**3.** I. Vivacidade (*liveness*) garante que nada de ruim jamais acontece ao sistema, sendo equivalente à propriedade de segurança (*safety*).

PORQUE

II. Alcançabilidade exige que, a partir de qualquer estado do sistema, exista sempre um caminho até o estado-alvo, e não apenas a existência de pelo menos um caminho a partir do estado inicial.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**4.** I. Tanto REQ-SAFE-004 (segurança) quanto REQ-SAFE-005 (vivacidade) puderam ser reformulados como invariantes de transição no supervisor do NexaBot.

PORQUE

II. O vetor de entradas do supervisor do NexaBot tem sete campos — seis booleanos e um contínuo (velocidade) —, este último usado para decidir quando uma desaceleração terminou.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**5.** I. REQ-SAFE-007, sobre velocidade linear, é verificado por exploração de estados discretos no mesmo módulo `modelcheck.py` usado para REQ-SAFE-001 a REQ-SAFE-005.

PORQUE

II. REQ-SAFE-007 trata de uma grandeza contínua (velocidade linear ≤ 1,20 m/s), fora do vetor de estados discreto do supervisor, sendo verificado por teste baseado em propriedades na Aula 12.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**6.** I. A busca em largura implementada em `modelcheck.py` explora exaustivamente todas as transições alcançáveis do supervisor do NexaBot a partir de OCIOSO.

PORQUE

II. Ferramentas como o NuSMV utilizam diagramas de decisão binária para representar simbolicamente o espaço de estados, evitando enumerar estado a estado.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**7.** I. CTL descreve propriedades sobre uma única trajetória de execução, enquanto LTL quantifica sobre a árvore de todas as trajetórias possíveis.

PORQUE

II. Na sintaxe de LTL, o operador $G$ significa "eventualmente", e o operador $F$ significa "globalmente".

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**8.** I. Um teste que passa mil vezes sem falhar não prova a ausência de falha no supervisor do NexaBot.

PORQUE

II. A exploração exaustiva de `modelcheck.py` não amostra: examina todas as combinações de entrada aplicáveis a cada estado alcançável e, ao encontrar uma violação, devolve o caminho completo até ela.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**9.** I. Na versão do supervisor em que, dentro do estado MOVENDO, o comando de partida do operador é avaliado antes do obstáculo, a exploração de estados reporta 8 violações de REQ-SAFE-001, mantendo os mesmos 6 estados e 768 transições da versão correta.

PORQUE

II. Essas violações ocorrem porque a inversão de prioridade torna a função de transição não determinística, produzindo dois estados de destino diferentes para a mesma entrada dentro de MOVENDO.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**10.** I. O contraexemplo do bug de prioridade encontrado na Aula 10 exige uma sequência de pelo menos cinco transições para expor a violação de REQ-SAFE-001.

PORQUE

II. O contraexemplo mais curto do bug de prioridade tem duas transições: de OCIOSO para MOVENDO por comando de partida, e de MOVENDO para MOVENDO mantendo o comando de partida junto com o obstáculo.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**11.** I. O autômato temporizado do watchdog em `timed.py` usa tempo discreto, contando períodos inteiros de $T_s$, em vez de relógios de valor real.

PORQUE

II. Um firmware embarcado tipicamente mede prazos contando ciclos (*ticks*) de um temporizador de hardware, não segundos contínuos, o que motiva o modelo discreto adotado no NexaBot.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**12.** I. A guarda temporal é a condição sobre o relógio válida enquanto o autômato permanece em um estado, e a invariante de localização é a condição que habilita uma transição.

PORQUE

II. No modelo do watchdog, DETECTANDO representa o gatilho físico ainda não reconhecido, e a cada período o ambiente escolhe confirmar a detecção ou continuar atrasando, até o limite `atraso_deteccao_max`.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**13.** I. Uma simulação típica do watchdog do NexaBot dificilmente amostra, ao mesmo tempo, o maior atraso de detecção admitido e a perda de um ciclo de atuação.

PORQUE

II. O UPPAAL verifica autômatos de tempo real contínuo usando relógios de valor real e zonas simbólicas, em vez de enumeração direta.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**14.** I. Com `atraso_deteccao_max` de 27 períodos, a verificação exaustiva do watchdog encontra 58 caminhos e reporta pior caso de 155 ms, configurando violação de REQ-SAFE-006.

PORQUE

II. O limite de REQ-SAFE-006 é avaliado com desigualdade estrita ($<$), de modo que exatamente 150 ms já configura violação do requisito.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**15.** I. O modelo do watchdog do NexaBot, sendo de tempo discreto, não precisa da maquinaria de zonas contínuas que o UPPAAL usa para relógios de valor real.

PORQUE

II. Isso ocorre porque o UPPAAL foi descontinuado e substituído por ferramentas de tempo discreto em toda a indústria automotiva.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**16.** I. Cobertura de linha de 100% em `supervisor.py` garante que qualquer sequência de estados capaz de expor um defeito de ordenação temporal foi exercitada pela suíte.

PORQUE

II. O bug de prioridade da Aula 10 pode conviver com 100% de cobertura de linha porque cada bloco condicional é executado isoladamente por algum teste, sem que nenhum precise encadear a sequência exata de duas transições que expõe o defeito.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
*d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**17.** I. No grafo do supervisor do NexaBot, a suíte gerada por percurso do grafo alcança 100% de cobertura de estados com apenas 5 casos de teste, mas cobre somente 5 das 25 arestas distintas do grafo.

PORQUE

II. Isso ocorre porque o grafo do supervisor tem 36 arestas distintas, das quais a suíte por percurso cobre exatamente a metade.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
*c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**18.** I. Ao reintroduzir o bug de prioridade e configurar a busca do Hypothesis por violações de REQ-SAFE-001, a redução (*shrinking*) converge para a mesma sequência mínima de dois passos já identificada pelo verificador exaustivo da Aula 10.

PORQUE

II. A sequência mínima que viola REQ-SAFE-001 é, estruturalmente, o menor caminho possível até a violação, de modo que técnicas de busca independentes tendem a encontrá-la.

*a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

**19.** I. REQ-SAFE-007 é verificado dentro de `modelcheck.py`, junto dos demais REQ-SAFE, porque a velocidade linear integra o vetor de estados discreto do supervisor.

PORQUE

II. A verificação formal do REQ-SAFE-007 dispensa qualquer teste baseado em propriedades, pois o requisito pode ser reduzido a uma invariante de transição booleana como REQ-SAFE-001.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
*e. As asserções I e II são proposições falsas.

**20.** I. A exploração exaustiva demonstrou, com certeza matemática, que o supervisor como modelado satisfaz REQ-SAFE-001 a REQ-SAFE-005.

PORQUE

II. A suíte gerada por percurso do grafo, com 5 casos de teste, cobre 100% dos estados alcançáveis do supervisor do NexaBot.

a. As asserções I e II são proposições verdadeiras, e a II é uma justificativa correta da I.
*b. As asserções I e II são proposições verdadeiras, mas a II não é uma justificativa correta da I.
c. A asserção I é uma proposição verdadeira, e a II é uma proposição falsa.
d. A asserção I é uma proposição falsa, e a II é uma proposição verdadeira.
e. As asserções I e II são proposições falsas.

### Interpretação

**21.** O requisito original "o robô deve parar rapidamente se houver obstáculo" foi resolvido no NexaBot por meio de REQ-SAFE-001 e REQ-SAFE-006. Um novo requisito ambíguo chega à equipe: "o robô deve retomar o movimento assim que for seguro". Seguindo a mesma metodologia de decomposição da Aula 9, qual é o tratamento mais adequado para esse requisito?

a. Um único requisito informal basta, pois "seguro" já é suficientemente preciso para verificação automática.
b. O requisito deve ser descartado, pois retomada de movimento não é uma propriedade formalizável em sistemas ciberfísicos.
c. Deve ser expresso apenas como invariante de estado, já que toda condição de retomada de movimento é, por definição, uma restrição instantânea sem componente temporal.
*d. O requisito deve ser decomposto em ao menos duas leituras — a condição lógica que define "seguro" e um eventual prazo associado à retomada —, cada uma verificada pela técnica apropriada, como ocorreu com REQ-SAFE-001 e REQ-SAFE-006.
e. Basta reaproveitar literalmente o predicado de REQ-SAFE-001, pois todo requisito do NexaBot compartilha o mesmo predicado executável.

**22.** Analise o trecho de `nexabot/requisitos.py` que define o predicado de REQ-SAFE-005:

```
condicao_disparo = (
    estado is Estado.PARADO_OBSTACULO
    and not entradas.obstaculo
    and entradas.comando_partir
    and not entradas.emergencia
    and not entradas.falha_encoder
)
```

Esse predicado foi ajustado depois que o *model checker* apontou um contraexemplo. Qual foi a razão para incluir as condições `not entradas.emergencia` e `not entradas.falha_encoder`?

a. Sem essas condições, o supervisor jamais conseguiria retornar a MOVENDO a partir de PARADO_OBSTACULO, em nenhuma circunstância.
b. As condições foram adicionadas apenas por convenção de estilo do código, sem qualquer impacto sobre o resultado da verificação.
c. Elas transformam REQ-SAFE-005 de propriedade de vivacidade em invariante de estado simples, eliminando a necessidade de exploração de transições.
d. Elas evitam que o requisito seja aplicável ao estado FALHA, que já é tratado separadamente por REQ-SAFE-004.
*e. Sem elas, o texto original do requisito exigiria retomar o movimento mesmo diante de falha de encoder ou emergência concorrentes, o que seria inseguro — o contraexemplo revelou que o requisito, como escrito originalmente, não previa faltas concorrentes.

**23.** REQ-SAFE-003 afirma que o estado MOVENDO é alcançável a partir de OCIOSO, verificado em `modelcheck.py` por meio de `estado_alvo=lambda estado: estado is Estado.MOVENDO`. Qual afirmação descreve corretamente o que essa verificação garante?

a. Que o supervisor sempre transita para MOVENDO a partir de OCIOSO, qualquer que seja a entrada aplicada.
*b. Que existe pelo menos um caminho de entradas que leva o supervisor de OCIOSO a MOVENDO, sem exigir que isso ocorra em toda execução.
c. Que MOVENDO é um estado absorvente do supervisor, do qual não é possível sair por nenhuma entrada.
d. Que o número mínimo de transições necessárias para alcançar MOVENDO é sempre igual a um, para qualquer entrada.
e. Que a propriedade é temporizada, dependendo do valor do período de amostragem $T_s$.

**24.** O predicado de REQ-SAFE-004 em código é:

```
if estado is Estado.FALHA and proximo is not Estado.FALHA:
    return entradas.rearme
return True
```

Por que REQ-SAFE-004 é classificado como invariante *sobre a transição*, e não como invariante de estado simples?

a. Porque o predicado nunca é avaliado nas transições em que o estado atual não é FALHA, tornando-o irrelevante fora desse estado.
b. Porque invariantes de estado, por definição da Aula 9, não podem ser expressas como funções Python executáveis.
*c. Porque a condição depende do par (estado atual, próximo estado) sob uma entrada específica — não apenas de o supervisor estar em FALHA, mas de para onde ele está indo —, algo que uma invariante de estado isolada não conseguiria expressar.
d. Porque REQ-SAFE-004 é, na verdade, um requisito de alcançabilidade disfarçado de invariante.
e. Porque o predicado retorna sempre `True` quando o estado é diferente de FALHA, o que o torna uma propriedade trivialmente satisfeita em todo o espaço.

**25.** Um novo integrante da equipe observa que REQ-SAFE-001 é verificado por exploração de estados (Aula 10), enquanto REQ-SAFE-006 exige um autômato temporizado (Aula 11), mesmo os dois tendo nascido do mesmo requisito ambíguo original sobre parar diante de obstáculo. Qual é a explicação tecnicamente correta para essa diferença de tratamento?

*a. REQ-SAFE-001 é uma restrição lógica instantânea sobre variáveis discretas, verificável a cada transição isolada; REQ-SAFE-006 envolve uma grandeza temporal de pior caso, que exige um modelo com estados de tempo explícito.
b. REQ-SAFE-006 é mais importante para a segurança do robô do que REQ-SAFE-001, e por isso recebe uma técnica de verificação mais sofisticada.
c. A diferença de tratamento é arbitrária; qualquer um dos dois requisitos poderia ser verificado por exploração de estados pura, sem perda de precisão.
d. REQ-SAFE-001 não pode ser verificado por *model checking* porque envolve o sensor físico de obstáculo, um componente fora do software.
e. REQ-SAFE-006 usa autômato temporizado apenas porque o UPPAAL exige esse formato para representar qualquer requisito de segurança.

**26.** Considere a fórmula CTL $AG\,\neg(\mathit{torque\_habilitado} \land \mathit{obstaculo})$, usada para expressar REQ-SAFE-001. Qual leitura está correta?

a. Existe algum caminho de execução em que `torque_habilitado` e `obstaculo` nunca ocorrem juntos.
b. Eventualmente, ao longo de algum caminho, `torque_habilitado` e `obstaculo` deixam de ocorrer juntos.
c. Em todo caminho de execução, existe algum instante em que `torque_habilitado` e `obstaculo` ocorrem juntos.
d. No próximo estado de todo caminho de execução, `torque_habilitado` e `obstaculo` não ocorrem juntos.
*e. Em todos os caminhos e em todos os estados alcançáveis, nunca é o caso de `torque_habilitado` e `obstaculo` serem simultaneamente verdadeiros.

**27.** O *model checker* relata, para a versão do supervisor em que, dentro de MOVENDO, o comando de partida é avaliado antes do obstáculo, o seguinte contraexemplo:

```
OCIOSO
  --[{comando_partir, v=0.00}]--> MOVENDO
  --[{comando_partir, obstaculo, v=0.00}]--> MOVENDO
```

Qual é a interpretação tecnicamente correta desse contraexemplo?

a. Ele prova que o supervisor tem, no total, exatamente duas transições possíveis a partir de OCIOSO, em qualquer versão do código.
b. Ele demonstra que, nessa versão do supervisor, `torque_habilitado` permanece `True` mesmo com `falha_encoder` ativa, violando REQ-SAFE-004.
c. Ele mostra que o bug de prioridade afeta apenas as transições que partem de OCIOSO, sem qualquer relação com o estado MOVENDO.
*d. Ele demonstra que, com comando de partida e obstáculo simultâneos, o supervisor mantém `torque_habilitado = True` dentro de MOVENDO — violando REQ-SAFE-001 —, mas não prova, por si só, que nenhuma outra combinação de entradas também viola algum requisito.
e. Ele prova que o supervisor, na versão com bug, nunca mais alcança o estado FALHA em nenhuma trajetória.

**28.** Um supervisor de armazém compõe o autômato do NexaBot (6 estados) com um autômato de zona de exclusão (4 estados) e um autômato de fila de tarefas (10 estados), todos operando em paralelo e de forma independente. Qual é o número aproximado de estados do produto, no pior caso, antes de qualquer redução por alcançabilidade?

a. 20, somando os estados dos três autômatos (6 + 4 + 10).
*b. 240, multiplicando os estados dos três autômatos (6 × 4 × 10).
c. 6, pois o maior autômato individual determina sozinho o total do produto.
d. 60, multiplicando apenas dois dos três autômatos (6 × 10) e ignorando o de zona de exclusão.
e. 4, pois o menor autômato individual limita o crescimento do produto.

**29.** Uma equipe decide substituir a exploração exaustiva de `modelcheck.py` por um teste aleatório que sorteia 10.000 sequências de entrada e verifica se alguma viola REQ-SAFE-001, rodando-o sobre a versão do supervisor com o bug de prioridade (8 violações entre 768 transições exploradas). Qual afirmação é a mais correta sobre essa substituição?

*a. Mesmo que o teste aleatório encontre a violação com alta probabilidade dado o número de sequências sorteadas, apenas a exploração exaustiva garante, por construção, que nenhuma transição alcançável ficou de fora — ausência de violação encontrada pelo teste aleatório nunca seria prova de corretude.
b. O teste aleatório é estritamente equivalente à exploração exaustiva sempre que o número de sequências sorteadas excede o número de transições do modelo.
c. A exploração exaustiva se torna desnecessária a partir de 10.000 sequências aleatórias, pois esse volume cobre estatisticamente 100% do espaço de estados.
d. O teste aleatório encontraria sempre exatamente as mesmas 8 violações, na mesma ordem, que a exploração exaustiva relata.
e. Substituir a exploração por teste aleatório elimina a explosão de estados sem qualquer perda de garantia formal sobre o modelo.

**30.** No `modelcheck.py`, cada estado alcançável recebe exatamente 128 entradas possíveis durante a busca em largura. Se uma exploração relatasse 6 estados alcançáveis, mas apenas 700 transições (em vez de 768), qual seria a interpretação tecnicamente correta?

a. O supervisor teria se tornado não determinístico, produzindo destinos diferentes para a mesma entrada.
b. REQ-SAFE-003, de alcançabilidade, deixaria automaticamente de ser satisfeito nessa exploração.
*c. Haveria uma inconsistência no próprio mecanismo de exploração — como algum estado não recebendo todas as 128 entradas —, pois 6 estados alcançáveis implicam, por construção do algoritmo, exatamente $6 \times 128 = 768$ transições.
d. Isso indicaria que o número real de estados alcançáveis é $700/128 \approx 5{,}47$, um valor fracionário de estados.
e. Isso seria esperado, pois nem toda entrada precisa ser testada contra todo estado alcançável na busca em largura.

**31.** Considerando o autômato temporizado do watchdog com $T_s = 5\,\mathrm{ms}$ e limite de REQ-SAFE-006 de 30 períodos (150 ms), e sabendo que o pior caso corresponde a `atraso_deteccao_max` mais 3 períodos (atraso máximo, confirmação e ciclo perdido), qual é o pior caso, em períodos e em ms, para `atraso_deteccao_max = 26` períodos (130 ms)?

a. 26 períodos = 130 ms, ainda dentro do limite de 150 ms.
b. 27 períodos = 135 ms, ainda dentro do limite de 150 ms.
c. 28 períodos = 140 ms, ainda dentro do limite de 150 ms.
d. 30 períodos = 150 ms, exatamente no limite de REQ-SAFE-006.
*e. 29 períodos = 145 ms, ainda dentro do limite de 150 ms, com margem de um período de amostragem.

**32.** Suponha que a equipe do NexaBot proponha um prazo mais rígido para REQ-SAFE-006, de 100 ms, mantendo $T_s = 5\,\mathrm{ms}$ e a relação pior caso = `atraso_deteccao_max` + 3 períodos. A quantos períodos de amostragem esse novo prazo corresponde, e qual seria o novo `atraso_deteccao_max` máximo admissível?

*a. 20 períodos; o novo `atraso_deteccao_max` máximo admissível cairia para 17 períodos (85 ms), bem abaixo dos 27 períodos (135 ms) atuais.
b. 20 períodos; o `atraso_deteccao_max` máximo admissível permaneceria em 27 períodos, pois o prazo do requisito não afeta essa margem.
c. 30 períodos; o prazo de 100 ms equivaleria ao mesmo limite atual de REQ-SAFE-006, sem qualquer alteração de margem.
d. 5 períodos; o `atraso_deteccao_max` deveria ser reduzido para exatamente zero períodos.
e. 100 períodos, pois cada milissegundo do novo prazo corresponderia a um período de amostragem inteiro.

**33.** Repetindo a varredura de `atraso_deteccao_max` sem permitir ciclo perdido (`permite_ciclo_perdido=False`), a relação entre atraso e pior caso passa a ser pior caso = `atraso_deteccao_max` + 2 períodos, um período a menos do que com ciclo perdido permitido. Qual é o maior `atraso_deteccao_max`, em períodos e em ms, que ainda mantém REQ-SAFE-006 satisfeito nesse cenário?

a. 27 períodos (135 ms), o mesmo valor do cenário com ciclo perdido permitido.
b. 30 períodos (150 ms), pois sem ciclo perdido o prazo deixaria de ser um fator limitante do projeto.
c. 25 períodos (125 ms), com margem menor do que a do cenário com ciclo perdido permitido.
*d. 28 períodos (140 ms), um período a mais de margem do que os 27 períodos (135 ms) admitidos com ciclo perdido habilitado.
e. 29 períodos (145 ms), pois a ausência de ciclo perdido eliminaria por completo a restrição de prazo.

**34.** Uma trajetória do autômato temporizado do watchdog é registrada como `DETECTANDO@t0 -> DETECTANDO@t1 -> COMANDANDO@t2 -> COMANDANDO@t3 -> ZERADO@t4`. Considerando $T_s = 5\,\mathrm{ms}$, qual é a leitura correta dessa trajetória?

a. O torque chegou a zero em exatamente 2 períodos, pois há apenas duas ocorrências do estado COMANDANDO.
b. Essa trajetória viola REQ-SAFE-006, pois envolve mais de duas transições entre o gatilho e ZERADO.
*c. O torque chegou a zero em 4 períodos (20 ms) a partir do gatilho, com um período de atraso de detecção e um ciclo perdido em COMANDANDO — bem dentro do limite de 150 ms.
d. A trajetória é inválida, pois o autômato do watchdog não permite permanecer em COMANDANDO por mais de um período.
e. O relógio da trajetória reinicia a cada transição, de modo que o tempo total até ZERADO não pode ser obtido somando os períodos.

**35.** A equipe do NexaBot decide aumentar a margem de segurança e fixar `atraso_deteccao_max` em 24 períodos (120 ms), mantendo $T_s = 5\,\mathrm{ms}$ e a relação pior caso = `atraso_deteccao_max` + 3 períodos. Qual é a margem restante, em ms, até o limite de 150 ms de REQ-SAFE-006?

a. 10 ms de margem restante até o limite de REQ-SAFE-006.
*b. 15 ms de margem restante, pois o pior caso passa a ser de 27 períodos (135 ms), abaixo do limite de 30 períodos (150 ms).
c. 20 ms de margem restante, calculados diretamente a partir dos 120 ms de atraso admitido pelo projeto.
d. 0 ms de margem restante, pois o prazo já estaria exatamente no limite de REQ-SAFE-006.
e. 5 ms de margem restante, correspondendo a exatamente um período de amostragem.

**36.** No grafo do supervisor do NexaBot, a transição MOVENDO → MOVENDO é habilitada por 8 das 128 entradas possíveis a partir de MOVENDO, enquanto FALHA → FALHA é habilitada por 96 delas. Qual é a implicação correta para uma suíte que pretenda alcançar cobertura de condições de guarda?

*a. Cobrir a aresta MOVENDO → MOVENDO exige exercitar proporcionalmente uma fração muito menor do espaço de entradas do que cobrir FALHA → FALHA, cujas 96 combinações representam uma superfície de teste bem maior para a mesma cobertura completa.
b. As duas arestas exigem exatamente o mesmo número de casos de teste, pois cobertura de guarda não depende do número de entradas habilitantes de cada aresta.
c. A aresta com menos entradas habilitantes (MOVENDO → MOVENDO) é sempre mais difícil de cobrir integralmente do que a que tem mais entradas.
d. Cobertura de condições de guarda é impossível de medir quando o número de entradas habilitantes difere entre arestas do mesmo grafo.
e. A suíte por percurso do grafo já cobre automaticamente as 96 combinações de FALHA → FALHA, pois o estado FALHA é visitado ao menos uma vez.

**37.** A suíte por percurso do grafo do supervisor usa 5 casos de teste sobre um grafo com 25 arestas distintas (de um máximo teórico de 36 pares origem-destino). Qual é a cobertura de transições dessa suíte, aproximadamente?

a. 100%, pois a suíte já alcança 100% de cobertura de estados, e os dois critérios coincidem por construção.
b. 5%, calculados diretamente como 5 dividido por 100.
*c. 20%, calculados como 5 das 25 arestas distintas efetivamente existentes no grafo do supervisor.
d. 13,9%, calculados como 5 das 36 combinações teóricas de pares origem-destino.
e. 25%, calculados como a razão entre as 25 arestas existentes e as 100 combinações de referência.

**38.** A exploração exaustiva de `modelcheck.py` demonstrou que o supervisor, como modelado, satisfaz REQ-SAFE-001 a REQ-SAFE-005, e o autômato temporizado de `timed.py` demonstrou que REQ-SAFE-006 é satisfeito dentro dos parâmetros verificados. Se o sensor físico de obstáculo do NexaBot, na prática, apresentar um atraso de detecção maior do que o parametrizado em `atraso_deteccao_max`, qual é a conclusão tecnicamente correta?

a. As provas permanecem válidas para o NexaBot físico sem qualquer ressalva, pois *model checking* verifica diretamente o comportamento do hardware.
b. REQ-SAFE-001 deixaria automaticamente de ser satisfeito, pois ele depende diretamente do atraso de detecção real do sensor físico.
c. A suíte gerada pelo Hypothesis compensaria automaticamente esse desvio de sensor, sem necessidade de qualquer reverificação.
d. O problema seria resolvido apenas aumentando artificialmente o número de estados alcançáveis do supervisor no modelo.
*e. A prova de REQ-SAFE-006 deixaria de se sustentar para o sistema físico, pois vale apenas para o modelo como parametrizado — *model checking* prova propriedades do modelo, não do sistema físico, e a validade da conclusão depende da fidelidade do modelo à realidade.

**39.** Uma equipe roda `03_hypothesis.py` sobre muitas sequências geradas contra o supervisor correto, e nenhuma violação de requisito é encontrada. Qual conclusão é tecnicamente sustentável?

a. A ausência de violação em 500 sequências equivale à prova da exploração exaustiva da Aula 10, pois 500 é um número suficientemente grande de tentativas.
*b. A ausência de violação é consistente com um supervisor correto, mas não constitui prova formal equivalente à exploração exaustiva, que examina todas as combinações possíveis, não uma amostra, por maior que seja.
c. O resultado prova que as 25 arestas do grafo do supervisor foram todas cobertas pelas 500 sequências sorteadas.
d. A ausência de violação prova que REQ-SAFE-006, de natureza temporizada, também está satisfeito pelo supervisor.
e. O resultado invalida a exploração exaustiva da Aula 10, por usar uma técnica de busca diferente sobre o mesmo modelo.

**40.** Para alcançar cobertura completa das 25 arestas distintas do grafo do supervisor, a equipe estima precisar de, no mínimo, 25 casos de teste — um por aresta. Isso corresponde a qual afirmação sobre a hierarquia de critérios de cobertura discutida na Aula 12?

a. Cobertura de arestas é menos exigente do que cobertura de estados, bastando ser numericamente maior do que o número de estados do grafo.
b. Cobertura de condições de guarda é menos exigente do que cobertura de transições, pois toda aresta tem exatamente uma única condição de guarda associada.
c. Uma suíte com 25 casos, cobrindo todas as arestas, cobre automaticamente 100% das condições de guarda de cada uma, pois cobertura de transição implica cobertura de guarda.
*d. Cobrir as 25 arestas ainda não garante cobertura de condições de guarda, pois cada aresta pode ser alcançada por número variável de combinações de entrada — cobri-la uma vez não exercita as demais combinações que também a habilitam.
e. A cobertura de arestas é equivalente à cobertura de linha de código, pois ambas medem apenas se uma instrução foi executada.

## Gabarito e feedbacks

**Questão 1** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira — um requisito formal exige justamente um predicado executável, não uma frase única sem ele.
- b. Incorreta: a asserção II é falsa, não verdadeira, pelo mesmo motivo.
- c. Correta: a decomposição do requisito em três leituras incompatíveis (I) é verdadeira, conforme a situação-problema da Aula 9; a exigência de frase única sem predicado (II) é falsa, pois é exatamente o predicado executável que elimina a ambiguidade.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 2** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que REQ-SAFE-001 é verificável por exploração de estados — é uma condição instantânea, avaliável transição a transição, sem relógio.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 3** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — vivacidade é "algo bom eventualmente acontece", propriedade distinta de segurança ("nada de ruim acontece").
- d. Incorreta: a asserção II também é falsa — alcançabilidade exige apenas um caminho a partir do estado inicial, não de qualquer estado.
- e. Correta: a I confunde vivacidade com segurança, dois tipos de propriedade distintos da Aula 9; a II exige alcançabilidade de todo estado, quando a definição correta exige apenas existência de um caminho a partir do inicial.

**Questão 4** (correta: b)
- a. Incorreta: a II é verdadeira como fato isolado sobre o vetor de entradas, mas não justifica por que REQ-SAFE-004 e REQ-SAFE-005 puderam virar invariantes de transição — isso decorre do determinismo do supervisor, não da composição do vetor de entradas.
- b. Correta: ambas as asserções são verdadeiras — a reformulação de REQ-SAFE-004 e REQ-SAFE-005 como invariantes de transição, e a composição de sete campos em `Entradas` —, mas a segunda não explica a primeira.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 5** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — REQ-SAFE-007 fica de fora de `modelcheck.py`, justamente por tratar de grandeza contínua fora do vetor de estados discreto; a II descreve corretamente esse limite e a técnica de verificação adequada (Aula 12).
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 6** (correta: b)
- a. Incorreta: a II é verdadeira sobre o NuSMV, mas não justifica por que a BFS de `modelcheck.py` explora exaustivamente — são mecanismos distintos (enumeração explícita versus representação simbólica).
- b. Correta: ambas as asserções são verdadeiras, mas a técnica do NuSMV citada na II não é a razão pela qual a BFS de `modelcheck.py`, de estados explícitos, consegue explorar exaustivamente o espaço do supervisor.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 7** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — a definição está invertida: LTL descreve trajetórias, CTL quantifica sobre a árvore de trajetórias.
- d. Incorreta: a asserção II também é falsa — a definição está invertida: $G$ significa "globalmente" e $F$ significa "eventualmente".
- e. Correta: a I inverte as definições de LTL e CTL da Aula 10, e a II inverte os significados de $G$ e $F$; ambas são falsas.

**Questão 8** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que um teste que nunca falha não prova corretude — a exploração exaustiva, ao contrário da amostragem, examina todas as combinações.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 9** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I reproduz corretamente o exemplo numérico da Aula 10 — 8 violações de REQ-SAFE-001, mantendo 6 estados e 768 transições, iguais aos da versão correta; a II é falsa, pois a função de transição continua determinística e pura em ambas as versões — o bug está na ordem de avaliação dentro do código, não em não determinismo introduzido.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 10** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — o contraexemplo mais curto tem exatamente duas transições, não cinco; a II descreve corretamente esse contraexemplo mínimo apresentado na Aula 10.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 11** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que o modelo do watchdog usa tempo discreto — a analogia com a contagem de ciclos de um temporizador de hardware real.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 12** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I troca as definições — guarda temporal habilita transição, invariante de localização vale enquanto se permanece num estado; a II descreve corretamente o comportamento não determinístico do ambiente em DETECTANDO.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 13** (correta: b)
- a. Incorreta: a II é verdadeira sobre o UPPAAL, mas não justifica por que a simulação típica não amostra o pior caso do watchdog do NexaBot — são fatos independentes.
- b. Correta: ambas as asserções são verdadeiras, mas a descrição do UPPAAL na II não é a razão pela qual simulações típicas raramente combinam atraso máximo e ciclo perdido simultaneamente.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 14** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — em 27 períodos a exploração encontra 56 caminhos e reporta 150 ms, ainda conforme, não 58 caminhos e 155 ms.
- d. Incorreta: a asserção II também é falsa — a verificação usa desigualdade não estrita ($\leq$), de modo que exatamente 150 ms ainda é conforme.
- e. Correta: a I troca os números do exemplo numérico da Aula 11 (27 períodos é a fronteira ainda conforme, não a violação); a II inverte o tipo de desigualdade usada na verificação.

**Questão 15** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I é verdadeira — o modelo discreto do NexaBot evita a maquinaria de zonas contínuas do UPPAAL, por usar relógio inteiro em períodos; a II é falsa, pois o UPPAAL segue em uso, e a razão para o modelo discreto é a fidelidade ao firmware real, não uma suposta descontinuação da ferramenta.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 16** (correta: d)
- a. Incorreta: a asserção I é falsa, não verdadeira.
- b. Incorreta: a asserção I é falsa, não verdadeira.
- c. Incorreta: a asserção I é falsa, e a II é verdadeira, não falsa.
- d. Correta: a I é falsa — cobertura de linha não garante que sequências específicas de estados foram exercitadas; a II descreve corretamente por que o bug de prioridade sobrevive a 100% de cobertura de linha.
- e. Incorreta: a asserção II é verdadeira, não falsa.

**Questão 17** (correta: c)
- a. Incorreta: a asserção II é falsa, não verdadeira.
- b. Incorreta: a asserção II é falsa, não verdadeira.
- c. Correta: a I reproduz corretamente o exemplo numérico da Aula 12 (5 casos, 100% de estados, 5 de 25 arestas); a II é falsa, pois o grafo tem 25 arestas distintas, não 36 (esse é o máximo teórico de pares), e 5/25 é 20%, não metade.
- d. Incorreta: a asserção I é verdadeira, não falsa.
- e. Incorreta: a asserção I é verdadeira, não falsa.

**Questão 18** (correta: a)
- a. Correta: ambas as asserções são verdadeiras, e a II explica corretamente por que Hypothesis e verificador exaustivo convergem para o mesmo contraexemplo mínimo — ele é, estruturalmente, o menor caminho até a violação de REQ-SAFE-001.
- b. Incorreta: a II realmente justifica a I nesta questão.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 19** (correta: e)
- a. Incorreta: as duas asserções são falsas, não verdadeiras.
- b. Incorreta: as duas asserções são falsas, não verdadeiras.
- c. Incorreta: a asserção I é falsa — REQ-SAFE-007 fica de fora do `modelcheck.py` justamente porque velocidade linear não integra o vetor de estados discreto do supervisor.
- d. Incorreta: a asserção II também é falsa — REQ-SAFE-007, sobre grandeza contínua, não pode ser reduzido a uma invariante booleana como REQ-SAFE-001, e por isso exige teste baseado em propriedades.
- e. Correta: a I afirma erroneamente que velocidade integra o vetor de estados discreto; a II afirma erroneamente que o requisito dispensa teste baseado em propriedades; ambas contradizem o texto da Aula 12.

**Questão 20** (correta: b)
- a. Incorreta: a II é verdadeira sobre a suíte por percurso, mas não justifica a certeza matemática da exploração exaustiva sobre REQ-SAFE-001 a REQ-SAFE-005 — são resultados de técnicas diferentes.
- b. Correta: ambas as asserções são verdadeiras, mas a cobertura de estados da suíte por percurso (II) não é a razão pela qual a exploração exaustiva (I) tem certeza matemática — essa certeza vem de examinar todas as transições, não da suíte gerada depois.
- c. Incorreta: a asserção II também é verdadeira, não falsa.
- d. Incorreta: a asserção I também é verdadeira, não falsa.
- e. Incorreta: as duas asserções são verdadeiras, não falsas.

**Questão 21** (correta: d)
- a. Incorreta: um requisito informal com "seguro" sem definição operacional reproduziria exatamente a ambiguidade que a Aula 9 mostra ser insustentável.
- b. Incorreta: retomada de movimento é perfeitamente formalizável, como demonstra a própria formalização de REQ-SAFE-005 no NexaBot.
- c. Incorreta: nem toda condição de retomada é instantânea — pode haver um prazo físico associado, como ocorre com REQ-SAFE-006.
- d. Correta: a metodologia da Aula 9 é decompor a ambiguidade em leituras distintas (condição lógica e eventual prazo), cada uma verificada pela técnica adequada, exatamente como REQ-SAFE-001 e REQ-SAFE-006.
- e. Incorreta: reaproveitar o predicado de REQ-SAFE-001 sem adaptação ignoraria que o novo requisito trata de uma condição de retomada, não de corte de torque diante de obstáculo.

**Questão 22** (correta: e)
- a. Incorreta: o supervisor consegue retornar a MOVENDO a partir de PARADO_OBSTACULO em muitas circunstâncias; as condições adicionadas restringem apenas os casos de falta concorrente.
- b. Incorreta: as condições têm impacto direto sobre quais transições satisfazem o predicado, não são apenas estilo de código.
- c. Incorreta: REQ-SAFE-005 continua sendo invariante de transição (vivacidade expressa como tal), não se torna invariante de estado simples.
- d. Incorreta: FALHA já é tratado por REQ-SAFE-004, mas a razão de excluir `falha_encoder` e `emergencia` do disparo de REQ-SAFE-005 é evitar retomada insegura, não redundância com outro requisito.
- e. Correta: o texto da Aula 9 relata explicitamente que o contraexemplo revelou faltas concorrentes não previstas no requisito original, motivando as qualificações adicionadas.

**Questão 23** (correta: b)
- a. Incorreta: alcançabilidade não exige que a transição ocorra sempre, apenas que exista um caminho possível.
- b. Correta: alcançabilidade, por definição da Aula 9, exige apenas a existência de um caminho, sem garantir que ele seja sempre percorrido.
- c. Incorreta: MOVENDO não é absorvente — o supervisor pode sair dele por comando de parada, obstáculo, falha ou emergência.
- d. Incorreta: o número de transições até MOVENDO depende da entrada e do caminho, não é fixo em um.
- e. Incorreta: REQ-SAFE-003 é classificado como alcançabilidade, verificada por exploração de estados, não como propriedade temporizada.

**Questão 24** (correta: c)
- a. Incorreta: o predicado é avaliado em toda transição, mas retorna `True` trivialmente fora de FALHA — isso não explica por que é invariante de transição.
- b. Incorreta: invariantes de estado também podem ser expressas como predicados Python; a distinção não é sobre executabilidade.
- c. Correta: a condição depende do par (estado, próximo estado) sob uma entrada, não apenas do estado atual — exatamente a definição de invariante de transição da Aula 9.
- d. Incorreta: REQ-SAFE-004 não verifica existência de caminho, e sim uma restrição sobre toda transição que sai de FALHA.
- e. Incorreta: o predicado retornar `True` fora de FALHA não o torna trivial — a exigência não trivial está justamente nas transições que saem de FALHA.

**Questão 25** (correta: a)
- a. Correta: essa é exatamente a distinção da Aula 9 — REQ-SAFE-001 é lógico/instantâneo (exploração de estados), REQ-SAFE-006 é temporal de pior caso (autômato temporizado).
- b. Incorreta: a técnica de verificação usada não decorre de importância relativa entre requisitos, e sim da natureza da propriedade (lógica versus temporal).
- c. Incorreta: REQ-SAFE-006, por envolver relógio e pior caso, não pode ser verificado apenas por exploração de estados puros, como o texto explicita.
- d. Incorreta: REQ-SAFE-001 é verificado por *model checking* normalmente, pois a condição sobre `torque_habilitado` e `obstaculo` é uma variável de software, não o sensor físico em si.
- e. Incorreta: a escolha por autômato temporizado decorre da natureza do requisito, não de uma exigência do UPPAAL, que é apenas uma ferramenta de referência industrial.

**Questão 26** (correta: e)
- a. Incorreta: essa leitura corresponde a $EF\,\neg\phi$, com quantificador existencial, não à fórmula $AG\,\neg\phi$ do enunciado.
- b. Incorreta: essa leitura também descreve um operador existencial-eventual, não o operador universal-globalmente da fórmula.
- c. Incorreta: essa leitura inverte a negação da fórmula, afirmando o oposto do que ela expressa.
- d. Incorreta: essa leitura corresponde ao operador $AX$ (próximo estado em todo caminho), não ao operador $AG$ (globalmente em todo caminho).
- e. Correta: $AG\,\phi$ significa "para todo caminho e em todo estado alcançável, $\phi$"; aplicado à negação da conjunção, isso é exatamente REQ-SAFE-001.

**Questão 27** (correta: d)
- a. Incorreta: o contraexemplo mostra apenas um caminho de duas transições, não o número total de transições possíveis a partir de OCIOSO.
- b. Incorreta: o contraexemplo não envolve `falha_encoder`; a violação é de REQ-SAFE-001, sobre `obstaculo` e `torque_habilitado` dentro de MOVENDO.
- c. Incorreta: o bug tem relação direta com MOVENDO — é justamente a ordem de avaliação das entradas dentro desse estado que causa a violação.
- d. Correta: o contraexemplo prova especificamente essa violação de REQ-SAFE-001, mas — ponto central da Aula 10 — não descarta a existência de outras violações em outras combinações de entrada não mostradas nesse caminho.
- e. Incorreta: o contraexemplo não trata de alcançabilidade do estado FALHA, e sim de manutenção indevida de torque dentro de MOVENDO.

**Questão 28** (correta: b)
- a. Incorreta: a composição de autômatos multiplica, não soma, os espaços de estado — a explosão de estados é multiplicativa, conforme a Aula 10.
- b. Correta: $6 \times 4 \times 10 = 240$, refletindo o crescimento multiplicativo da explosão de estados ao compor autômatos independentes.
- c. Incorreta: nenhum autômato individual determina sozinho o produto; todos contribuem multiplicativamente.
- d. Incorreta: ignorar um dos três autômatos subestima o espaço real do produto composto.
- e. Incorreta: o menor autômato não limita o produto; ele apenas contribui como um fator multiplicativo entre outros.

**Questão 29** (correta: a)
- a. Correta: a exploração exaustiva garante, por construção, cobertura total do espaço declarado; teste aleatório, mesmo com muitas amostras, nunca oferece essa garantia quando não encontra violação.
- b. Incorreta: número de amostras superior ao de transições não torna as duas técnicas equivalentes — amostragem aleatória pode repetir ou deixar de sortear combinações específicas.
- c. Incorreta: cobertura estatística aproximada não é cobertura total; a exploração exaustiva continua sendo a única com garantia formal.
- d. Incorreta: um sorteio aleatório não reproduz necessariamente a mesma ordem, nem garante encontrar exatamente as mesmas 8 violações.
- e. Incorreta: substituir por amostragem aleatória não elimina a explosão de estados; apenas troca garantia formal por evidência probabilística.

**Questão 30** (correta: c)
- a. Incorreta: o cenário não menciona mudança na função de transição, apenas uma discrepância na contagem de transições exploradas.
- b. Incorreta: REQ-SAFE-003 depende de alcançabilidade de MOVENDO, não do número total de transições exploradas.
- c. Correta: com 6 estados alcançáveis e 128 entradas por estado, o total exato de transições exploradas deve ser $6 \times 128 = 768$; um valor menor indica falha no próprio mecanismo de exploração.
- d. Incorreta: o número de estados alcançáveis é sempre um inteiro; a discrepância está nas transições exploradas por estado, não no número de estados.
- e. Incorreta: o algoritmo de `modelcheck.py` aplica, por definição, toda entrada possível a cada estado retirado da fila — não é opcional.

**Questão 31** (correta: e)
- a. Incorreta: 26 períodos corresponderia ao valor de `atraso_deteccao_max`, não ao pior caso, que soma mais 3 períodos.
- b. Incorreta: 27 períodos e 135 ms correspondem a somar apenas 1 período ao atraso, não os 3 períodos da relação dada.
- c. Incorreta: 28 períodos e 140 ms correspondem a somar apenas 2 períodos ao atraso, não os 3 da relação dada.
- d. Incorreta: 30 períodos e 150 ms seriam o pior caso para `atraso_deteccao_max = 27`, não para 26.
- e. Correta: $26 + 3 = 29$ períodos, e $29 \times 5\,\mathrm{ms} = 145\,\mathrm{ms}$, dentro do limite de 150 ms com margem de um período.

**Questão 32** (correta: a)
- a. Correta: $100\,\mathrm{ms} / 5\,\mathrm{ms} = 20$ períodos; resolvendo $x + 3 \leq 20$, o novo `atraso_deteccao_max` máximo é 17 períodos (85 ms), bem abaixo dos 27 períodos atuais.
- b. Incorreta: reduzir o prazo do requisito reduz proporcionalmente a margem admissível para o atraso de detecção, não a mantém inalterada.
- c. Incorreta: 30 períodos corresponderia ao limite atual de 150 ms, não ao novo prazo mais rígido de 100 ms.
- d. Incorreta: reduzir `atraso_deteccao_max` a zero seria excessivamente conservador; o cálculo correto permite até 17 períodos.
- e. Incorreta: a conversão de ms para períodos usa $T_s$ como divisor (100/5 = 20), não uma correspondência de um para um entre ms e períodos.

**Questão 33** (correta: d)
- a. Incorreta: 27 períodos é o valor máximo com ciclo perdido permitido; sem ciclo perdido, a margem é maior, não igual.
- b. Incorreta: mesmo sem ciclo perdido, o prazo de 150 ms continua sendo um limite ativo, pois o atraso de detecção ainda soma períodos ao pior caso.
- c. Incorreta: 25 períodos subestima a margem real; o cálculo com a relação dada permite até 28 períodos.
- d. Correta: resolvendo $x + 2 \leq 30$, o máximo é $x = 28$ períodos (140 ms), um período a mais do que os 27 períodos (135 ms) do cenário com ciclo perdido.
- e. Incorreta: 29 períodos violaria o limite ($29 + 2 = 31 > 30$); a ausência de ciclo perdido reduz o pior caso, mas não elimina a restrição de prazo.

**Questão 34** (correta: c)
- a. Incorreta: o relógio final da trajetória é `t4`, ou seja, 4 períodos, não 2 — a contagem de ocorrências de COMANDANDO não equivale ao valor final do relógio.
- b. Incorreta: 4 períodos (20 ms) está muito abaixo do limite de 150 ms de REQ-SAFE-006; não há violação.
- c. Correta: o relógio avança de t0 a t4 (4 períodos = 20 ms), com um período extra em DETECTANDO (atraso de detecção) e um período extra em COMANDANDO (ciclo perdido), antes de ZERADO.
- d. Incorreta: o modelo permite permanecer em COMANDANDO por mais de um período exatamente para representar a escolha não determinística de um ciclo perdido.
- e. Incorreta: o relógio da trajetória é cumulativo desde o gatilho (`t0`), e o valor final (`t4`) já representa o tempo total decorrido.

**Questão 35** (correta: b)
- a. Incorreta: 10 ms subestima a margem; o cálculo correto resulta em 15 ms.
- b. Correta: $24 + 3 = 27$ períodos = 135 ms; a margem até 150 ms é $150 - 135 = 15\,\mathrm{ms}$.
- c. Incorreta: a margem não é calculada subtraindo o atraso admitido diretamente do limite, e sim a partir do pior caso já somado aos 3 períodos adicionais.
- d. Incorreta: 0 ms de margem só ocorreria se o pior caso atingisse exatamente 30 períodos (150 ms), o que não é o caso para 24 períodos de atraso.
- e. Incorreta: 5 ms subestima a margem real de 15 ms calculada pela relação dada.

**Questão 36** (correta: a)
- a. Correta: cobrir todas as combinações que habilitam MOVENDO → MOVENDO (8 entradas) é uma tarefa proporcionalmente menor do que cobrir as 96 que habilitam FALHA → FALHA, o que ilustra por que cobertura de guarda é o critério mais exigente da hierarquia.
- b. Incorreta: o número de casos necessário para cobertura completa de guarda depende diretamente de quantas combinações habilitam cada aresta.
- c. Incorreta: menos entradas habilitantes torna a cobertura completa mais fácil, não mais difícil, pois há menos combinações a exercitar.
- d. Incorreta: cobertura de guarda é mensurável mesmo com número variável de entradas habilitantes por aresta — é justamente essa variação que a métrica captura.
- e. Incorreta: visitar o estado FALHA uma vez cobre apenas uma das 96 combinações de entrada que mantêm FALHA → FALHA, não todas elas.

**Questão 37** (correta: c)
- a. Incorreta: 100% de cobertura de estados não implica 100% de cobertura de transições — a Aula 12 mostra exatamente essa discrepância.
- b. Incorreta: o cálculo de porcentagem de cobertura de arestas usa o total de arestas existentes (25) como denominador, não 100.
- c. Correta: $5/25 = 20\%$, exatamente o valor relatado no exemplo numérico da Aula 12 para a suíte por percurso do grafo.
- d. Incorreta: 36 é o máximo teórico de pares origem-destino, não o número de arestas de fato existentes no grafo do supervisor.
- e. Incorreta: o denominador correto é 25 (arestas existentes), não 100.

**Questão 38** (correta: e)
- a. Incorreta: *model checking* verifica o modelo formal, não o comportamento físico direto do hardware — essa é a ressalva central de encerramento da unidade.
- b. Incorreta: REQ-SAFE-001 é uma restrição lógica instantânea sobre variáveis de software, independente do valor do atraso de detecção do sensor.
- c. Incorreta: o Hypothesis testa o modelo fechado com as suposições parametrizadas; não compensa automaticamente um desvio de parâmetro físico não modelado.
- d. Incorreta: aumentar o número de estados alcançáveis do modelo não corrige uma divergência entre o parâmetro modelado e o comportamento físico real do sensor.
- e. Correta: a prova de REQ-SAFE-006 vale apenas dentro dos parâmetros verificados; um atraso físico maior do que o modelado invalida a conclusão para o sistema real, exatamente o ponto de honestidade técnica da Aula 12.

**Questão 39** (correta: b)
- a. Incorreta: nenhuma quantidade de amostras aleatórias equivale à garantia da exploração exaustiva, que examina todas as combinações possíveis, não uma amostra.
- b. Correta: ausência de violação em uma amostra é evidência favorável, mas não prova formal — distinção central entre teste baseado em propriedades e exploração exaustiva.
- c. Incorreta: rodar sequências aleatórias contra os requisitos de transição não mede nem garante cobertura das 25 arestas do grafo.
- d. Incorreta: REQ-SAFE-006 é temporizado e verificado por autômato temporizado (Aula 11); não é exercitado pelas sequências booleanas do Hypothesis sobre `REQUISITOS_TRANSICAO`.
- e. Incorreta: técnicas diferentes que não encontram violação não se invalidam mutuamente; ausência de violação em uma não contradiz zero violações na outra.

**Questão 40** (correta: d)
- a. Incorreta: cobertura de arestas é mais exigente do que cobertura de estados, não menos — visitar todo estado não implica percorrer toda transição.
- b. Incorreta: cobertura de condições de guarda é mais exigente do que cobertura de transições, não menos, pois uma mesma aresta pode ter várias combinações de entrada habilitantes.
- c. Incorreta: cobertura de transição não implica cobertura de guarda — MOVENDO → MOVENDO, por exemplo, tem 8 combinações habilitantes, e cobrir a aresta uma vez não as cobre todas.
- d. Correta: a hierarquia da Aula 12 estabelece que cobertura de transições não garante cobertura de guardas, pois cada aresta pode ser alcançada por número variável de combinações de entrada.
- e. Incorreta: cobertura de arestas mede combinações de estado (origem, destino) percorridas no modelo, não execução de instruções de código-fonte.
