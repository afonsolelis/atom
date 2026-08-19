# Roteiros das videoaulas 13 a 16 — Unidade 4 (20 minutos)

Disciplina: Distributed Systems Engineering
Professor-conteudista: Afonso Cesar Lelis Brandão
Unidade 4: Operação, validação e evolução
Duração-alvo de cada videoaula: 20 minutos.
Narração prevista: aproximadamente 2.200 a 2.700 palavras faladas por videoaula, sem contar títulos, marcações de tempo, indicações de edição e fontes.
Ritmo de referência: 115 a 130 palavras por minuto, já considerando pausas, respiração e construção progressiva dos recursos visuais.

Cada roteiro acompanha, slide a slide, o deck HTML da aula correspondente em `unidade_4/slides/`. As marcações entre colchetes duplos indicam o intervalo de tempo e o slide que deve estar na tela naquele momento. O avanço de slide é o principal marcador de edição: quando a marcação muda, o slide muda.

Plano de tempo de referência, adaptável ao ritmo de cada aula:

- 00:00–01:45 — capa, audiodescrição e sumário;
- 01:45–04:00 — objetivos de aprendizagem e situação-problema;
- 04:00–13:00 — desenvolvimento conceitual;
- 13:00–16:00 — demonstração, exemplos numéricos e estudo de caso;
- 16:00–18:00 — aplicação profissional e pausa para reflexão;
- 18:00–20:00 — pontos-chave, atividade prática e fechamento.

Os quatro roteiros a seguir correspondem às Aulas 13 a 16 da Unidade 4, encerrando a trajetória da NexaOrder. Cada roteiro é um texto de narração pronto para gravação, e não notas de aula. O registro é o de exposição didática contínua, próximo ao de um livro-texto lido em voz alta: frases completas, encadeamento explícito entre as ideias e ausência de recursos de oralidade informal.

---

## Roteiro da Videoaula 13 — “Um pedido que sumiu por doze segundos”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 13 — Observabilidade e diagnóstico distribuído.

**Deck de apoio:** `unidade_4/slides/aula13.html` — 18 slides (capa, audiodescrição, sumário, 14 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de distinguir monitoramento de observabilidade, combinar métricas, logs e traces reconhecendo os limites de cada pilar, projetar a propagação de um identificador de correlação, escolher SLIs que reflitam a experiência do usuário, calcular o orçamento de erro de um SLO e ler um trace em cascata.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 monitoramento e observabilidade · 05:30 os três pilares · 07:20 contexto e correlação · 09:00 erro comum de cardinalidade · 10:20 OpenTelemetry · 12:00 citação · 12:20 escolher o SLI · 13:50 exemplo numérico do orçamento de erro · 15:40 orçamento legitima risco · 17:00 trace em cascata · 19:00 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 13, primeira da Unidade 4, e a pergunta central da disciplina se desloca pela última vez. Até aqui, tratamos de como construir. A partir desta unidade, a questão é outra: como verificar que aquilo que foi construído está efetivamente funcionando?

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: os slides usam fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo aparece em cartões claros. São cinco recursos visuais: o quadro comparativo entre monitoramento e observabilidade, a tabela dos três pilares, o diagrama da propagação do identificador de correlação, a fórmula do orçamento de erro e o trace em cascata com spans aninhados. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo demonstrando por que monitoramento e observabilidade não são sinônimos. Apresento depois os três pilares — métricas, logs e traces — e o que cada um não consegue responder isoladamente. Trato em seguida de contexto e correlação distribuída, e da instrumentação com OpenTelemetry. Passo então aos indicadores de nível de serviço, os SLIs, aos objetivos, os SLOs, e ao orçamento de erro que deles decorre. Fecho lendo um trace em cascata para descobrir onde foram parar os doze segundos.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir distinguir monitoramento de observabilidade pelo tipo de pergunta que cada um responde. Deve combinar métricas, logs e traces reconhecendo o que cada pilar não consegue responder sozinho. Deve projetar a propagação de um identificador de correlação, inclusive em comunicação assíncrona. Deve escolher SLIs que reflitam a experiência do usuário, e não a saúde da infraestrutura. Deve calcular o orçamento de erro de um SLO e interpretar sua taxa de consumo. E deve ler um trace em cascata para localizar onde a latência foi realmente gasta.

**[02:20–03:50 · Slide 4 — Situação-problema]**

O incidente que abre a aula é particularmente difícil justamente porque todos os indicadores aparentavam normalidade.

Um cliente relata que a compra levou doze segundos entre o clique e a confirmação. Não houve erro visível e a compra foi concluída; apenas demorou muito além do razoável.

A equipe consulta o painel de infraestrutura. CPU, memória e rede dos quatro serviços permanecem dentro da faixa normal. Nenhum alerta foi disparado e nenhum serviço reiniciou. Examinados os logs, cada registro, lido isoladamente, indica um tempo perfeitamente aceitável para a etapa correspondente.

O problema real é este: ninguém consegue reconstruir a jornada completa daquele pedido pelos quatro serviços. Os logs existem, mas sem um identificador comum que permita ordená-los e relacioná-los.

A equipe sabe que alguma etapa consumiu doze segundos, mas não sabe qual — e não sabe porque o sistema jamais foi projetado para responder a esse tipo de pergunta.

### Desenvolvimento conceitual

**[03:50–05:30 · Slide 5 — Monitoramento e observabilidade]**

Convém separar dois termos frequentemente usados como sinônimos, embora não o sejam.

*[indicação de edição: inserir Recurso visual 49 da Aula 13 — quadro comparativo entre monitoramento e observabilidade, revelado linha a linha]*

Monitoramento observa indicadores previamente definidos e alerta quando ultrapassam limites. Responde a perguntas antecipadas: a CPU está alta? A taxa de erro superou 1%? Por isso, exige que as falhas sejam previstas — cada modo de falha esperado demanda seu próprio painel.

Observabilidade permite inferir o estado interno do sistema a partir dos dados que ele expõe. Responde a perguntas não formuladas antes do incidente e não exige previsão de falhas; exige a exposição de dados ricos e correlacionáveis.

Aplicado ao incidente em questão: painéis adicionais de CPU não contribuiriam em nada, pois a CPU estava normal. A observabilidade permite perguntar o que ocorreu com aquele pedido específico e obter resposta.

A diferença é prática, não terminológica. Observabilidade é a capacidade de formular uma pergunta nova e respondê-la a partir de dados já coletados, sem reproduzir o problema manualmente. Se a investigação exige acrescentar um log e aguardar a repetição do problema, o que existe é monitoramento, não observabilidade.

**[05:30–07:20 · Slide 6 — Os três pilares]**

São três pilares, e o essencial é entender o que cada um não faz.

*[indicação de edição: inserir Recurso visual 50 da Aula 13 — tabela dos três pilares, com força e limitação de cada um]*

Métricas são valores numéricos agregados ao longo do tempo. Sua força está em serem compactas, baratas de reter e adequadas a tendências e alertas. Sua limitação é que a agregação oculta quais requisições falharam e por quê: sabe-se que 2% falharam, mas não quais.

Logs são registros discretos de eventos, em texto estruturado. Sua força é a riqueza de contexto local, pois mostram exatamente o que aquele serviço estava executando. Sua limitação é que, sem correlação, permanecem fragmentos isolados — foi precisamente isso que inviabilizou a investigação da NexaOrder.

Traces são o caminho de uma requisição, decomposto em spans. Sua força é mostrar onde o tempo foi consumido e em que ordem. Sua limitação é o custo mais elevado de instrumentação e de armazenamento.

A regra fundamental é que nenhum deles substitui os demais. Métricas indicam que algo mudou. Traces localizam onde, dentro de uma requisição específica, a mudança ocorreu. Logs detalham o que exatamente aconteceu naquele ponto. Trata-se de uma investigação em três etapas, e a omissão de qualquer uma delas cria um ponto cego.

**[07:20–09:00 · Slide 7 — Contexto e correlação distribuída]**

O que transforma logs e traces dispersos em uma narrativa coerente é a correlação.

*[indicação de edição: inserir Recurso visual 51 da Aula 13 — propagação do identificador de correlação pelos quatro serviços, incluindo o salto assíncrono]*

O mecanismo tem quatro passos. Primeiro: o gateway gera o identificador de correlação — o trace ID — na entrada, no primeiro componente que toca a requisição. Segundo: chamadas síncronas propagam o identificador em um cabeçalho da requisição. Terceiro: eventos assíncronos propagam o identificador nos metadados da mensagem. Quarto: cada serviço extrai e reinjeta o identificador — a propagação é responsabilidade explícita da instrumentação.

O terceiro passo merece atenção especial, por ser o mais frequentemente omitido. Muitas equipes instrumentam adequadamente as chamadas HTTP e perdem por completo o rastro quando o fluxo atravessa uma fila ou um tópico. Em uma arquitetura orientada a eventos como a construída na Unidade 3, isso significa perder metade da jornada.

O alerta mais importante é este: se um único serviço no percurso deixar de propagar o contexto, o trace se rompe naquele ponto. A jornada completa torna-se irreconstituível, ainda que todos os demais serviços estejam perfeitamente instrumentados. A propagação funciona como uma corrente, e vale pelo elo mais fraco.

**[09:00–10:20 · Slide 8 — Erro comum: identificador de requisição não é dimensão de métrica]**

Cabe antecipar um erro custoso, que costuma surgir justamente quando a equipe adota a correlação com entusiasmo.

O impulso é compreensível: se o identificador de trace resolveu o problema dos logs, a tentação é incluí-lo também nas métricas.

O problema é que identificadores por requisição criam cardinalidade praticamente ilimitada. Cada requisição gera um valor novo de dimensão, e o sistema de métricas passa a armazenar uma série temporal por requisição. O custo de armazenamento e de consulta das métricas cresce de forma explosiva e, em muitos casos, compromete o próprio sistema de observabilidade.

A prática correta é outra: métricas empregam dimensões agregáveis — rota, código de status, região, versão —, ou seja, atributos com poucos valores possíveis.

Existe uma ponte adequada entre os dois mundos, denominada exemplar: ela vincula um ponto específico da métrica a um trace individual. Observado o pico de latência no gráfico, é possível abrir um exemplo concreto daquele pico.

A regra sintetiza os dois papéis: métricas agregam, traces individualizam.

**[10:20–12:00 · Slide 9 — Instrumentação com OpenTelemetry]**

Resta a questão de como instrumentar tudo isso sem criar dependência de um fornecedor.

Historicamente, cada fornecedor definia seu próprio formato de instrumentação. Trocar de ferramenta implicava reescrever código de instrumentação em todos os serviços, o que, na prática, inviabilizava a troca.

O OpenTelemetry é um padrão aberto e neutro que unifica métricas, logs e traces sob uma mesma API.

Ele oferece captura automática de elementos comuns: chamadas HTTP recebidas e enviadas, consultas a banco de dados, publicação e consumo de mensagens. Disso resulta uma base de instrumentação obtida com escrita mínima de código.

Sobre essa base, acrescentam-se spans personalizados com as operações de negócio relevantes — reservar item, autorizar pagamento. É nesse momento que a telemetria deixa de ser estritamente técnica e passa a expressar a linguagem do domínio.

Há ainda o coletor: componente que recebe a telemetria, processa e encaminha ao backend de armazenamento e visualização.

O ganho efetivo é que trocar o sistema de análise costuma preservar a instrumentação, exigindo apenas o ajuste do exportador ou do destino.

Cabe, porém, uma qualificação: o desacoplamento não é total. Convenções semânticas, recursos proprietários e capacidades distintas entre ferramentas ainda podem exigir adaptações. O padrão reduz substancialmente o custo de troca, sem eliminá-lo.

**[12:00–12:20 · Slide 10 — Citação]**

Esta frase sintetiza a primeira metade da aula: monitoramento responde a perguntas antecipadas; observabilidade permite investigar perguntas que ninguém formulou antes do incidente.

### Demonstração, exemplo ou estudo de caso

**[12:20–13:50 · Slide 11 — SLI: escolher o que medir]**

A discussão passa agora de como coletar para o que medir.

Um indicador de nível de serviço, o SLI, é uma medida quantitativa do comportamento observado, calculada a partir de dados reais de produção. Bons SLIs refletem a experiência de quem usa o sistema.

Três exemplos para a NexaOrder. A proporção de requisições de checkout concluídas com sucesso sobre o total de tentativas. A proporção de requisições concluídas dentro de um limite de latência — 300 milissegundos, por exemplo. E a proporção de confirmações de pagamento processadas corretamente na primeira tentativa.

Os três indicadores tratam de resultado para o cliente, e não de consumo de recurso de máquina.

O erro comum consiste em escolher o indicador de coleta mais simples — utilização média de CPU — em lugar do indicador relevante. A CPU pode permanecer em 40% enquanto uma fração significativa de pedidos falha por esgotamento de conexões, cenário exatamente equivalente ao do incidente da Aula 4.

O teste para um bom SLI é o seguinte: quando ele se degrada, a experiência de quem usa o serviço também se degrada. Sem essa correspondência, o indicador escolhido é inadequado, e a equipe passará plantões inteiros diante de gráficos que não explicam a reclamação do cliente.

**[13:50–15:40 · Slide 12 — Exemplo numérico: do SLO ao orçamento de erro]**

Do indicador, passamos ao objetivo.

Um SLO é a meta definida para um SLI ao longo de um período — por exemplo, 99,9% dos checkouts concluídos com sucesso, medido mensalmente.

Daí decorre o conceito mais relevante desta aula. A diferença entre 100% e o SLO constitui o orçamento de erro.

*[indicação de edição: inserir Recurso visual 52 da Aula 13 — fórmula do orçamento de erro, seguida da barra de consumo preenchendo 75%]*

A fórmula é: o orçamento é igual a 1 menos o SLO, multiplicado pelo volume.

Os números do exemplo são estes. Volume de 12 milhões de requisições por mês e SLO de 99,9%. O cálculo: 1 menos 0,999 resulta em 0,001; multiplicado por 12 milhões, resulta em 12 mil falhas toleradas no mês.

O dado seguinte altera a análise: a equipe consumiu 9 mil dessas falhas nos primeiros 10 dias.

A leitura é direta. Nove mil de doze mil correspondem a 75% do orçamento, consumidos em um terço do período. A taxa de consumo excede em muito o que o restante do mês comporta: mantido esse ritmo, o orçamento se esgota por volta do dia 14.

Esse número orienta decisões concretas, e não uma discussão subjetiva: reduzir mudanças arriscadas, priorizar correções de confiabilidade e adiar o lançamento previsto para o dia 20.

**[15:40–17:00 · Slide 13 — O orçamento de erro legitima o risco calculado]**

A consequência organizacional desse conceito supera a consequência técnica.

Enquanto há orçamento disponível, a equipe dispõe de margem para implantar, experimentar e evoluir o sistema. O orçamento não constitui penalidade; constitui autorização para assumir risco calculado.

Esgotado o orçamento, uma política previamente acordada desloca a prioridade para a estabilidade. O termo previamente é essencial: a regra é estabelecida antes, quando não há pressão sobre a equipe.

O ganho é que o critério se torna observável, em lugar de uma discussão subjetiva sobre o que seria suficientemente seguro. Sem orçamento declarado, toda conversa sobre ritmo de mudança se converte em opinião — a área de produto avalia que é possível acelerar, a de infraestrutura avalia que não, e prevalece quem tem mais influência. Com orçamento declarado, a decisão passa a ser a leitura de um número acordado com antecedência.

O efeito mais profundo é de outra ordem: confiabilidade deixa de opor-se à entrega e passa a ser aquilo que a torna sustentável. A questão não é qualidade contra velocidade, e sim qual velocidade cabe na qualidade prometida.

### Aplicação profissional

**[17:00–19:00 · Slide 14 — O trace em cascata do pedido de doze segundos]**

Resta resolver o incidente que abriu a aula.

*[indicação de edição: inserir Recurso visual 53 da Aula 13 — trace em cascata com spans aninhados, revelando uma linha por vez e destacando o span de espera em fila]*

Com a instrumentação implantada, a equipe abre o trace daquele pedido específico. Os dados são os seguintes.

O span raiz, no gateway, registra 12 mil milissegundos — o intervalo completo percebido pelo cliente, coerente com a reclamação.

O span de pedidos registra 11.950 milissegundos. Quase todo o tempo está contido nele, o que exclui o gateway como origem do problema.

O span de estoque registra 35 milissegundos, e é imediatamente descartado como suspeito. Sem o trace, essa eliminação consumiria horas de investigação.

O span de pagamento registra 11.780 milissegundos, o que identifica o caminho crítico.

A descoberta está no detalhamento. Dentro do span de pagamento existem dois filhos: espera em fila, com 11.450 milissegundos, e chamada ao provedor externo, com 310 milissegundos.

Esse resultado merece atenção. A hipótese intuitiva seria atribuir a demora ao provedor externo de pagamento, suspeito habitual por estar fora do controle da equipe. O provedor, contudo, respondeu em 310 milissegundos, comportamento inteiramente normal. O tempo foi consumido na espera em fila interna, provavelmente por esgotamento do pool de conexões.

Sem o trace, a equipe teria aberto um chamado junto ao provedor. Com o trace, ela identifica que a causa é interna.

Dois cuidados de leitura evitam interpretações equivocadas. Primeiro: spans aninhados não se somam como se fossem sequenciais — 11.450 mais 310 não corresponde ao total, porque um está contido no outro. São a cascata e a relação pai-filho que revelam a causa. Segundo: a expedição, por ser assíncrona, inicia após a resposta ao cliente e não integra o caminho crítico, podendo levar minutos sem afetar a percepção de ninguém.

### Fechamento

**[19:00–19:40 · Slides 15 e 16 — Pontos-chave e atividade prática]**

Recapitulando. Duas capacidades distintas: monitoramento cobre o previsto, observabilidade permite investigar o que ninguém antecipou. Três pilares, um incidente: métricas apontam a mudança, traces localizam o ponto, logs explicam o que houve ali. Correlação é explícita: o identificador só atravessa o sistema se cada serviço o extrair e reinjetar, inclusive em eventos. Padrão neutro: o OpenTelemetry desacopla a instrumentação da ferramenta de análise, sem eliminar toda adaptação. SLI olha o usuário: um bom indicador é ruim exatamente quando a experiência de quem usa o serviço é ruim. E o orçamento decide o ritmo: a taxa de consumo converte confiabilidade em critério operacional observável.

Na atividade prática, você vai reconstruir o trace de um pedido atravessando gateway, pedidos, estoque, pagamento e expedição: atribuir tempos hipotéticos a cada serviço, identificar qual concentra a maior parte do tempo, propor um identificador de correlação e descrever sua propagação incluindo o evento assíncrono da expedição, definir um SLI e um SLO para o checkout, calcular o orçamento de erro mensal para um volume hipotético e listar dois logs e duas métricas que, somados ao trace, confirmariam a causa raiz.

**[19:40–20:00 · Slide 17 — Encerramento]**

Esta aula forma a capacidade de instrumentar um sistema para responder a perguntas não previstas e de converter confiabilidade em um número operável. A próxima aula passa da observação à intervenção: como validar deliberadamente que a resiliência desenhada na Unidade 1 funciona de fato.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 13 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com o painel “tudo verde” contrastando com a reclamação do cliente (02:20–03:50).
- Recurso visual 49 — quadro comparativo entre monitoramento e observabilidade (aproximadamente 04:00).
- Recurso visual 50 — tabela dos três pilares, com força e limitação de cada um (aproximadamente 05:40).
- Recurso visual 51 — propagação do identificador de correlação, incluindo o salto assíncrono (aproximadamente 07:30).
- Slide 10 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (12:00).
- Recurso visual 52 — fórmula do orçamento de erro e barra de consumo em 75% (aproximadamente 14:00).
- Recurso visual 53 — trace em cascata, revelado linha a linha, com o span de espera em fila destacado (17:00–19:00).
- Slide 17 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- BEYER, Betsy et al. (org.). *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol: O’Reilly Media, 2016 — referência conceitual, sem reprodução de trecho externo.
- SIGELMAN, Benjamin H. et al. *Dapper, a large-scale distributed systems tracing infrastructure*. Mountain View: Google, 2010 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; quadros, tabelas, fórmulas e o trace em cascata devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 13 (`unidade_4.md`) e do deck `unidade_4/slides/aula13.html`.

---

## Roteiro da Videoaula 14 — “O teste que nunca foi feito”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 14 — Resiliência, testes distribuídos e engenharia do caos.

**Deck de apoio:** `unidade_4/slides/aula14.html` — 18 slides (capa, audiodescrição, sumário, 14 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de dimensionar a pirâmide de testes reconhecendo o custo do topo, aplicar testes de contrato, distinguir testes de carga, estresse e duração, formular uma hipótese de estado estável mensurável, delimitar raio de impacto e critério de interrupção, e calcular a disponibilidade combinada de uma cadeia de serviços.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:50 pirâmide de testes · 05:30 testes de contrato · 07:20 carga, estresse e duração · 09:00 engenharia do caos · 10:40 hipótese de estado estável · 12:20 citação · 12:40 raio de impacto e interrupção · 14:40 exemplo numérico da cadeia · 16:10 postmortem · 17:40 pausa para reflexão · 19:00 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 14, dedicada a resiliência, testes distribuídos e engenharia do caos. A aula anterior tratou de enxergar o sistema por dentro; esta emprega essa visibilidade para confirmar ou refutar aquilo que até então era apenas suposição.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: a pirâmide de testes, o diagrama do teste de contrato no pipeline, o quadro dos três tipos de teste de desempenho, o cartão do experimento de caos e a fórmula da disponibilidade combinada em cadeia. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo revisitando a pirâmide de testes aplicada a um sistema distribuído, contexto em que o topo é consideravelmente mais caro. Apresento depois os testes de contrato, que verificam acordos sem exigir a execução de todo o sistema. Separo em seguida testes de carga, estresse e duração. Trato então de engenharia do caos: as razões para injetar falha deliberadamente, a formulação de uma hipótese de estado estável e a delimitação do raio de impacto e do mecanismo de interrupção. Fecho demonstrando por que a resiliência de cada serviço isolado não basta, e como conduzir um postmortem sem culpabilização.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir dimensionar a pirâmide de testes reconhecendo o custo do topo em sistemas distribuídos. Deve aplicar testes de contrato para detectar incompatibilidade antes da implantação. Deve distinguir teste de carga, de estresse e de duração pela pergunta que cada um responde. Deve formular uma hipótese de estado estável mensurável para um experimento de caos. Deve delimitar raio de impacto e critério de interrupção antes de executar em produção. E deve calcular a disponibilidade combinada de uma cadeia de serviços e interpretar o resultado.

**[02:20–03:50 · Slide 4 — Situação-problema]**

O incidente é o seguinte. Durante uma promoção de fim de ano, o provedor de pagamento apresentou instabilidade de poucos minutos — ocorrência rotineira em provedores externos.

O circuito de proteção desenhado na Unidade 1 deveria isolar essa falha, mas não foi o que ocorreu.

O serviço de pedidos aguardava a resposta de forma síncrona, em um trecho de código jamais testado sob condição de falha. As conexões pendentes se acumularam até esgotar o limite de capacidade, e o estoque, que dependia de pedidos para confirmar reservas, também se tornou lento.

O diagnóstico merece atenção. A equipe sabia, em tese, que os mecanismos de proteção existiam: alguém os implementou, alguém revisou o código, alguém registrou a tarefa como concluída.

Faltava a prática de validá-los deliberadamente. Sem essa validação, o primeiro teste dos mecanismos foi realizado por um evento real, sob a pior condição possível, que é o tráfego de pico.

Um mecanismo de resiliência nunca exercitado é uma hipótese, não uma proteção.

### Desenvolvimento conceitual

**[03:50–05:30 · Slide 5 — A pirâmide de testes em um sistema distribuído]**

Convém partir do que já é conhecido antes de introduzir a complicação.

*[indicação de edição: inserir Recurso visual 54 da Aula 14 — pirâmide de testes com as três camadas proporcionalmente dimensionadas]*

Testes unitários verificam uma função ou classe isoladamente, executando em milissegundos. Formam a base ampla da pirâmide.

Testes de integração verificam a interação entre um componente e suas dependências diretas — banco de dados, fila, cache.

Testes de ponta a ponta verificam um fluxo completo atravessando múltiplos serviços reais. Formam o topo estreito.

Nada disso é novo. O que muda em sistemas distribuídos é o custo particularmente elevado do topo. Um teste de ponta a ponta do checkout da NexaOrder exige pedidos, estoque, pagamento e expedição simultaneamente disponíveis e coerentes. Ele é lento, frágil diante de mudanças não relacionadas — a alteração de um campo pela equipe de expedição compromete o teste de checkout — e de difícil diagnóstico quando falha.

A recomendação prática é manter a base ampla de testes unitários e de contrato, com um conjunto reduzido e criteriosamente escolhido de testes de integração e de ponta a ponta, concentrado nos fluxos mais críticos. A tentativa de cobrir tudo no topo produz uma suíte lenta e pouco confiável.

**[05:30–07:20 · Slide 6 — Testes de contrato]**

A interação entre serviços pode ser coberta sem o custo do teste de ponta a ponta por meio dos testes de contrato.

Um teste de contrato verifica se consumidor e provedor concordam sobre o formato e o significado das mensagens, sem exigir que ambos estejam em execução simultânea. É essa última característica que o torna econômico.

*[indicação de edição: inserir Recurso visual 55 da Aula 14 — fluxo do teste de contrato, do consumidor ao pipeline do produtor]*

O mecanismo tem quatro passos. Primeiro, o consumidor declara: o estoque define expectativas explícitas sobre os campos que espera receber. Segundo, publicação: essas expectativas vão para um repositório compartilhado. Terceiro, verificação no pipeline: a integração contínua do produtor valida o contrato antes de qualquer implantação. Quarto, falha antecipada: se um campo esperado sumir ou mudar de nome, o pipeline falha antes de chegar à produção.

O valor prático é considerável. Esse mecanismo detectaria exatamente a alteração silenciosa no nome de um campo, problema discutido na Aula 10 a propósito da evolução de esquema. Trata-se de ocorrência recorrente em arquiteturas orientadas a eventos, responsável por falhas sutis que se manifestam muito depois da implantação, quando a mudança já não é lembrada.

Há também uma inversão de responsabilidade: o consumidor declara o que necessita, e o produtor fica obrigado a honrá-lo. Isso explicita um acordo que, sem o teste, existiria apenas na memória de quem escreveu o código.

**[07:20–09:00 · Slide 7 — Carga, estresse e duração]**

Três tipos de teste de desempenho, com três perguntas diferentes.

*[indicação de edição: inserir Recurso visual 56 da Aula 14 — quadro dos três testes, com a curva característica de cada um]*

Teste de carga aplica o tráfego esperado — o dia típico ou o pico projetado. A pergunta que ele responde é: o sistema atende ao que foi prometido, sem violar as metas de latência e de erro?

Teste de estresse aplica carga crescente, além da esperada, até que o sistema falhe. A pergunta é dupla: onde ele falha e como se degrada ao falhar? A segunda parte é decisiva — um sistema que rejeita o excesso de forma controlada é preferível a um que se torna inteiramente indisponível.

Teste de duração, ou soak, aplica carga sustentada por horas ou dias. A pergunta é: como ele se degrada exposto ao tempo, e não ao volume instantâneo?

É esse terceiro tipo que revela o que os demais não alcançam: vazamentos de memória, esgotamento gradual de conexões e acúmulo de dados temporários não liberados. São problemas invisíveis em trinta minutos de teste, mas capazes de indisponibilizar o sistema no quarto dia de operação contínua.

**[09:00–10:40 · Slide 8 — Engenharia do caos]**

Chegamos ao tema que dá nome à aula.

Engenharia do caos é conduzir experimentos controlados que injetam falhas deliberadas — latência adicional, erros simulados, indisponibilidade de um componente — para observar o comportamento real do sistema, em vez de presumi-lo.

A justificativa para essa prática é a seguinte: sistemas distribuídos enfrentam combinações de falha raras demais para que uma revisão de código as antecipe. A leitura do código dificilmente suscita a pergunta sobre o que ocorreria se o pagamento se tornasse lento exatamente enquanto o estoque estivesse rebalanceando partições.

Essas combinações, contudo, são suficientemente frequentes: na escala de milhares de componentes, ocorrem periodicamente. O que é raro individualmente torna-se comum de forma agregada — mesmo raciocínio do cálculo de cauda de latência da Aula 6.

A diferença em relação a um teste unitário está no método: o experimento de caos parte de uma hipótese explícita e procura refutá-la sob perturbação controlada. Trata-se de método científico aplicado à produção, não de perturbação arbitrária.

Um cuidado importante: resultados inesperados são valiosos e constituem, de fato, o objetivo do experimento. Isso não dispensa, porém, critérios definidos antes da execução. Executar sem critérios não configura experimento, e sim um incidente provocado.

**[10:40–12:20 · Slide 9 — Hipótese de estado estável]**

Todo experimento bem projetado começa por uma expectativa mensurável e específica sobre o comportamento normal, formulada antes de qualquer falha ser injetada.

O contraste esclarece o ponto. Uma hipótese vaga seria afirmar que o sistema deve continuar funcionando — formulação impossível de verificar, pois não define o que significa funcionar: responder de alguma forma, responder rapidamente ou não perder pedidos?

A versão utilizável, para a NexaOrder, é outra. Em condições normais: taxa de conclusão acima de 98% e p95 do checkout abaixo de 400 milissegundos. Durante a indisponibilidade simulada: o circuito de proteção deve ser acionado e o sistema deve degradar de forma controlada. Critério de sucesso: a taxa de conclusão de pedidos não deve cair abaixo de 90%.

Formulada dessa maneira, a hipótese pode ser confirmada ou refutada por um número.

Há um pré-requisito implícito, que conecta esta aula à anterior: a equipe precisa já ser capaz de medir taxa de conclusão e p95 continuamente. Sem as métricas da Aula 13, nada pode ser confirmado ou refutado durante o experimento — injeta-se a falha sem qualquer instrumento de leitura.

Observabilidade não é pré-requisito burocrático do caos: é o instrumento de medida do experimento.

**[12:20–12:40 · Slide 10 — Citação]**

Esta frase delimita a fronteira ética e profissional da prática: raio de impacto limitado e capacidade de interrupção imediata separam um experimento de caos responsável de simplesmente causar uma falha em produção.

### Demonstração, exemplo ou estudo de caso

**[12:40–14:40 · Slide 11 — Raio de impacto e mecanismo de interrupção]**

Essas duas salvaguardas merecem detalhamento.

Quanto ao raio de impacto, a orientação é começar pequeno: um por cento do tráfego real, um ambiente controlado ou um subconjunto reduzido de instâncias. A ampliação deve ser gradual, acompanhando a confiança adquirida sobre o comportamento observado.

Quanto à interrupção, são necessários um kill switch — comando ou automação capaz de encerrar a injeção de falha instantaneamente — e um gatilho declarado, acionado quando os indicadores de negócio ultrapassam um limite de degradação predefinido.

*[indicação de edição: inserir Recurso visual 57 da Aula 14 — cartão do experimento com os cinco campos, preenchidos um a um]*

Todos esses elementos se documentam em um cartão de experimento. Para a NexaOrder, ele se apresenta assim.

Hipótese de estado estável: conclusão de pedidos maior ou igual a 90% durante a perturbação. Perturbação: indisponibilidade simulada do provedor de pagamento. Métricas de controle: taxa de conclusão, p95 do checkout e estado do circuito de proteção. Raio de impacto: 1% do tráfego, em uma única região. Critério de interrupção: conclusão abaixo de 85% por mais de 60 segundos.

São cinco campos, e preenchê-los é o que converte uma ideia arriscada em um experimento defensável perante a gestão. A impossibilidade de preencher os cinco indica que o experimento ainda não está pronto para execução.

**[14:40–16:10 · Slide 12 — Exemplo numérico: por que a resiliência de cada serviço não basta]**

Uma conta já apresentada na Aula 2 retorna aqui com outro propósito.

Quatro serviços, cada um com 99,9% de disponibilidade individual, em cadeia estritamente sequencial e sem tolerância a falha parcial.

A disponibilidade do fluxo é 0,999 elevado a 4, que dá aproximadamente 0,996 — ou seja, 99,6%.

Traduzido em impacto: contrataram-se quatro componentes de 99,9% e obteve-se um fluxo de 99,6%, o que corresponde a aproximadamente quatro vezes mais indisponibilidade do que a de qualquer componente isolado.

A leitura relevante é que a composição entrega resultado pior do que cada componente individualmente. Isso não é detalhe, e sim propriedade estrutural de cadeias sequenciais.

Por essa razão, circuitos de proteção, degradação graciosa e processamento assíncrono não são refinamentos opcionais a serem acrescentados quando houver tempo disponível. São eles que impedem que a composição degrade a disponibilidade agregada.

O argumento da aula se completa aqui: apenas testes deliberados — não a leitura do código, não a revisão em pull request, não a confiança na biblioteca — revelam se esses mecanismos efetivamente atenuam esse efeito na prática. Foi precisamente essa lacuna que produziu o incidente da abertura.

**[16:10–17:40 · Slide 13 — Postmortem sem culpabilização]**

Depois de um incidente real, ou de um experimento que revela comportamento inesperado, segue-se a etapa final: a aprendizagem estruturada.

O relatório de postmortem reconstrói a linha do tempo do incidente, os fatores contribuintes e as ações de melhoria, com responsáveis e prazos.

O princípio que o organiza é o seguinte: incidentes em sistemas complexos raramente têm causa única atribuível a uma pessoa. Eles emergem de combinações de decisões de projeto, lacunas de teste e condições operacionais que, isoladamente, pareciam razoáveis.

Isso não constitui indulgência, e sim precisão. A conclusão de que alguém deixou de configurar um timeout produz pouco aprendizado e leva à repetição do incidente sob outra forma.

Duas orientações práticas se impõem. Primeira: não interromper a análise na causa imediata. O esgotamento de conexões é o sintoma, não a explicação. Segunda: perguntar por que sucessivamente. Por que o circuito não impediu o esgotamento? Por que nenhum teste revelou a lacuna antes? Por que aquele trecho de código nunca foi exercitado sob falha?

O objetivo final é identificar mudanças sistêmicas, e não apenas correções pontuais de código. A correção pontual resolve o incidente em questão; a mudança sistêmica resolve a categoria inteira.

### Aplicação profissional

**[17:40–19:00 · Slide 14 — Pausa para reflexão]**

A aula se encerra com uma objeção comum na prática profissional, que exigirá resposta em algum momento da carreira.

A equipe decide não realizar nenhum experimento de caos em produção, argumentando que os testes de integração em homologação são suficientes.

*[indicação de edição: pausar a narração por 10 segundos com o texto “Homologação garante confiança suficiente?” na tela]*

Quatro perguntas orientam a análise: que diferenças entre homologação e produção podem invalidar essa suposição? Por que testes de integração, ainda que bem escritos, podem não revelar o comportamento sob falhas parciais e concorrência real? Que argumento demonstraria à liderança que um experimento de raio limitado é mais seguro do que aguardar um incidente real? E que evidências de observabilidade, nos termos da Aula 13, seriam necessárias antes de autorizar o primeiro experimento em produção?

Um elemento auxilia a resposta. Ambientes de homologação raramente reproduzem volume de tráfego, diversidade de dados e condições de rede reais: operam com fração do tráfego, dados sintéticos e uma rede sem congestionamento.

O argumento que costuma prevalecer junto à liderança é este: o caos controlado reduz o risco de que essas lacunas sejam descobertas pela primeira vez durante um incidente sem controle. A questão não é testar ou não testar em produção, e sim descobrir a falha em um experimento restrito a 1% do tráfego, em horário de baixa demanda, ou descobri-la em 100% do tráfego durante o pico anual de vendas.

### Fechamento

**[19:00–19:40 · Slides 15 e 16 — Pontos-chave e atividade prática]**

Recapitulando. Base ampla, topo estreito: unitários e contratos sustentam a cobertura, e ponta a ponta fica reservado aos fluxos mais críticos. Contrato detecta antes: a incompatibilidade entre consumidor e provedor aparece no pipeline, não em produção. Três testes, três perguntas: carga confirma o prometido, estresse revela o limite, duração revela a degradação no tempo. Hipótese antes da falha: sem uma expectativa mensurável definida previamente, o experimento não confirma nem refuta nada. Pequeno e interrompível: raio de impacto limitado e kill switch são o que tornam o experimento aceitável em produção. E a cadeia degrada: compor serviços reduz a disponibilidade agregada, e só mecanismos testados revertem esse efeito.

Na atividade prática, você vai planejar um experimento controlado de indisponibilidade do serviço de pagamento: formular a hipótese de estado estável com os indicadores observados, definir e justificar o raio de impacto inicial, descrever o mecanismo de interrupção imediata e o critério que o aciona, listar as métricas, logs e traces necessários para avaliar o resultado, descrever em três frases a estrutura do postmortem caso surja uma falha inesperada e indicar qual mudança sistêmica você proporia se a hipótese for refutada.

**[19:40–20:00 · Slide 17 — Encerramento]**

Esta aula forma a capacidade de transformar suposições sobre resiliência em evidências obtidas por testes estruturados e experimentos controlados. A próxima aula trata de outro tema: como processar volume em lote, em fluxo, em funções e na borda.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 14 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com a cascata de esgotamento de conexões (02:20–03:50).
- Recurso visual 54 — pirâmide de testes, com o topo destacado como caro (aproximadamente 04:00).
- Recurso visual 55 — fluxo do teste de contrato, do consumidor ao pipeline do produtor (aproximadamente 05:40).
- Recurso visual 56 — quadro dos três testes de desempenho, com a curva de cada um (aproximadamente 07:30).
- Slide 10 — citação em tela cheia, com 3 segundos de silêncio antes da leitura (12:20).
- Recurso visual 57 — cartão do experimento de caos, preenchido campo a campo (aproximadamente 13:40).
- Slide 12 — cálculo da disponibilidade em cadeia, com a queda de 99,9% para 99,6% destacada (aproximadamente 14:50).
- Slide 14 — pausa de reflexão de 10 segundos (aproximadamente 18:00).
- Slide 17 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- BASIRI, Ali et al. Chaos engineering. *IEEE Software*, v. 33, n. 3, p. 35-41, 2016. DOI: 10.1109/MS.2016.60 — referência conceitual, sem reprodução de trecho externo.
- ROSENTHAL, Casey; JONES, Nora. *Chaos Engineering: System Resiliency in Practice*. Sebastopol: O’Reilly Media, 2020 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; pirâmides, quadros, cartões e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 14 (`unidade_4.md`) e do deck `unidade_4/slides/aula14.html`.

---

## Roteiro da Videoaula 15 — “Detectar fraude antes que o pagamento seja aprovado”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 15 — Processamento distribuído, edge e serverless.

**Deck de apoio:** `unidade_4/slides/aula15.html` — 18 slides (capa, audiodescrição, sumário, 14 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de decidir entre lote e fluxo a partir de até quando a informação pode esperar, descrever map, shuffle e reduce e sua generalização em DAGs, dimensionar partições de um pipeline de fluxo, distinguir tempo de evento de tempo de processamento, avaliar o custo de inicialização a frio e ponderar ganho de latência contra complexidade na computação de borda.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:40 lote e fluxo · 05:30 MapReduce e DAGs · 07:20 exemplo numérico das partições · 09:00 mais partições, mais coordenação · 10:20 citação · 10:40 tempo de evento e de processamento · 12:30 marcas d’água · 14:00 funções como serviço · 15:40 computação de borda · 17:20 pausa para reflexão · 19:00 pontos-chave e atividade · 19:40 encerramento.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a Aula 15, dedicada a processamento distribuído, computação de borda e funções como serviço. Toda a aula se organiza em torno de uma única pergunta de negócio, cuja resposta altera integralmente a arquitetura adotada.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: o quadro comparativo entre lote e fluxo, o diagrama das fases de map, shuffle e reduce, a fórmula do dimensionamento de partições, a linha do tempo comparando tempo de evento e de processamento, e a tabela de borda, regional e centralizado. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo separando processamento em lote e em fluxo. Apresento depois MapReduce e sua generalização em grafos acíclicos dirigidos. Trato em seguida de particionamento e tolerância a falhas em fluxo, e da distinção entre tempo de evento e tempo de processamento, com janelas e marcas d’água. Examino então funções como serviço e o custo de inicialização a frio, bem como a computação de borda, ponderando latência e complexidade. Fecho com o critério que articula todo o conteúdo: a escolha a partir do requisito de negócio.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir decidir entre lote e fluxo a partir de até quando a informação pode esperar. Deve descrever as fases de map, shuffle e reduce e sua generalização em DAGs. Deve dimensionar partições de um pipeline de fluxo a partir da taxa de eventos. Deve distinguir tempo de evento de tempo de processamento e escolher a base da janela. Deve avaliar o custo de inicialização a frio em caminhos sensíveis à latência. E deve ponderar ganho de latência contra complexidade operacional na computação de borda.

**[02:20–03:40 · Slide 4 — Situação-problema]**

A NexaOrder passou a registrar tentativas de fraude com um padrão característico: múltiplos cartões em sequência rápida, a partir do mesmo dispositivo, testando quais dados seriam aceitos.

A primeira proposta técnica da equipe foi razoável e barata: um job a cada hora, lendo o histórico e sinalizando padrões para revisão no dia seguinte.

A área de risco rejeita a proposta com um argumento simples e decisivo: uma hora é suficiente para que dezenas de tentativas fraudulentas sejam aprovadas. Quando o relatório for emitido, a perda financeira já terá ocorrido.

A decisão precisa ocorrer em segundos, no momento da tentativa.

Essa exigência, originada do negócio e não da engenharia, altera integralmente o tipo de arquitetura de processamento necessária. É esse deslocamento que a aula percorre.

### Desenvolvimento conceitual

**[03:40–05:30 · Slide 5 — Lote e fluxo]**

Os dois paradigmas merecem comparação cuidadosa.

*[indicação de edição: inserir Recurso visual 58 da Aula 15 — quadro comparativo entre lote e fluxo, revelado linha a linha]*

Sobre o que cada um opera: o processamento em lote opera sobre um conjunto finito e delimitado, coletado ao longo de um período. O processamento em fluxo opera sobre uma sequência potencialmente ilimitada de eventos — que nunca termina.

Quando processa: o lote processa de uma só vez, depois de o conjunto estar formado. O fluxo processa cada evento, ou pequenos grupos, assim que ele fica disponível.

A vantagem de cada um: o lote oferece simplicidade, pois o conjunto é conhecido e finito, permitindo ordenar, contar e reprocessar livremente. O fluxo oferece decisão no instante em que o fato ocorre.

Casos típicos: o lote atende relatórios diários, cálculo de comissões mensais e reprocessamento histórico. O fluxo atende detecção de fraude, alertas operacionais e contadores em tempo real.

A conclusão a destacar é que a escolha não é apenas técnica. Trata-se de decisão de negócio sobre até quando uma informação pode esperar antes de perder valor. No caso da fraude, a informação perde praticamente todo o valor em minutos. Em um relatório de comissões, ela pode aguardar o fechamento do mês sem qualquer perda.

**[05:30–07:20 · Slide 6 — MapReduce e a generalização em DAGs]**

Convém entender como o processamento em lote distribui trabalho, pois o princípio reaparece no processamento em fluxo.

*[indicação de edição: inserir Recurso visual 59 da Aula 15 — diagrama das três fases, com os dados fluindo entre elas]*

O modelo clássico é o MapReduce, com três fases.

Map: transforma cada registro de entrada independentemente, produzindo pares de chave e valor intermediários. Como cada registro é tratado sozinho, essa fase paraleliza perfeitamente.

Shuffle: redistribui os pares intermediários entre os nós, agrupando-os pela chave correspondente. É a fase mais custosa, por envolver tráfego de rede em larga escala, e costuma dominar o tempo total de execução.

Reduce: agrupa e combina os pares por chave, produzindo o resultado final.

Os frameworks modernos generalizaram essa ideia em DAGs — grafos acíclicos dirigidos — encadeando várias etapas além do par map-reduce, e otimizando o plano de execução como um todo.

A tolerância a falhas segue um princípio que merece registro: se um nó falha durante uma tarefa, o framework a reatribui a outro nó, reexecutando-a a partir dos dados intermediários já persistidos, sem reiniciar o job inteiro e sem exigir intervenção manual para a falha isolada. Trata-se de reconciliação, no mesmo espírito da Aula 11, aplicada agora a tarefas de processamento.

**[07:20–09:00 · Slide 7 — Exemplo numérico: dimensionando as partições do pipeline]**

Pipelines de fluxo também particionam o trabalho, distribuindo eventos por uma chave. No caso em análise, a chave natural é o identificador do dispositivo, o que garante que todos os eventos de um mesmo dispositivo sejam processados em ordem, pela mesma partição.

É exatamente a mesma lógica de chave apresentada na Aula 10, e ela é essencial aqui: detectar cinco cartões testados em trinta segundos no mesmo dispositivo exige que esses cinco eventos cheguem ao mesmo destino, na ordem correta.

A fórmula é a familiar: o número de partições é o teto da divisão entre a taxa de eventos e a capacidade por partição.

Os números da NexaOrder são estes: pico de 5 mil tentativas por segundo e capacidade de 750 por segundo por partição. O cálculo: 5000 dividido por 750 resulta em 6,67, arredondado para cima em 7 partições no mínimo.

Sete partições atendem ao pico com alguma margem. Uma ressalva, contudo, é importante: a conta não substitui um teste de carga real do pipeline completo. Ela ignora o custo de embaralhamento entre etapas e o custo de acessar o contexto necessário à avaliação, como o histórico recente daquele dispositivo. Em um pipeline de detecção, buscar o estado anterior costuma ser mais caro que processar o evento em si.

**[09:00–10:20 · Slide 8 — Mais partições, mais coordenação]**

Cabe perguntar por que não se define um número muito maior de partições, resolvendo o problema em definitivo.

A razão é que mais partições significam mais paralelismo disponível, mas também mais complexidade de coordenação e de tolerância a falhas.

Cada partição precisa registrar seu avanço de forma persistente — o progresso duradouro. Isso garante que, em caso de falha do consumidor, o processamento recomece do ponto certo, sem perder nem duplicar eventos, além do que a semântica de entrega escolhida permitir.

Trata-se exatamente da mesma discussão sobre at-least-once e efeito efetivamente único conduzida na Unidade 3, agora em outro contexto. Os conceitos da disciplina não constituem compartimentos isolados: reaparecem sempre que o mesmo problema estrutural se manifesta.

**[10:20–10:40 · Slide 9 — Citação]**

Esta frase enuncia o critério central da aula: a escolha entre lote e fluxo é uma decisão de negócio sobre até quando uma informação pode esperar antes de perder valor.

### Demonstração, exemplo ou estudo de caso

**[10:40–12:30 · Slide 10 — Tempo de evento e tempo de processamento]**

Há uma distinção essencial em processamento de fluxo cuja omissão produz resultados gravemente incorretos.

*[indicação de edição: inserir Recurso visual 60 da Aula 15 — linha do tempo dupla, com o mesmo evento posicionado em dois instantes diferentes]*

Tempo de evento é o instante em que o fato ocorreu no domínio de negócio — o momento exato da tentativa de pagamento, no relógio do cliente.

Tempo de processamento é o instante em que o pipeline efetivamente processa aquele evento, segundos ou minutos depois.

A escolha entre eles determina o resultado. Uma janela baseada em tempo de evento produz resultados mais fiéis à realidade do negócio, mas exige tratar atraso e desordem, pois eventos podem chegar fora de sequência e eventos antigos podem chegar depois de eventos recentes. Uma janela baseada em tempo de processamento é simples de implementar, porém pode distorcer a análise.

Considere a pergunta de detecção de fraude: quantas tentativas com o mesmo dispositivo ocorreram no último minuto? A resposta varia conforme a base de tempo escolhida.

Se um dispositivo realizou dez tentativas em dez segundos, mas a rede atrasou cinco delas em dois minutos, a janela por tempo de processamento identifica dois grupos de cinco e não dispara o alerta. A janela por tempo de evento identifica as dez em conjunto e dispara. A fraude é a mesma; a detecção depende inteiramente dessa escolha.

**[12:30–14:00 · Slide 11 — Marcas d’água e tolerância a atraso]**

Resta a questão de como fechar uma janela por tempo de evento, dada a impossibilidade de saber se ainda chegará um evento atrasado.

É essa a função das marcas d’água. Uma marca d’água é uma estimativa de até que ponto, no tempo de evento, o pipeline já recebeu a maior parte dos dados — uma indicação de que, provavelmente, todos os eventos até aquele instante já foram processados.

Complementarmente, existe a tolerância a atraso: período adicional configurável que mantém a janela aberta antes do fechamento definitivo.

Em conjunto, esses mecanismos permitem admitir eventos atrasados sem abandonar o conceito de janela e sem esperar indefinidamente.

O compromisso é evidente e exige escolha explícita: janelas que fecham cedo perdem eventos tardios e, portanto, subestimam. Janelas que demoram atrasam a decisão — e, no caso da fraude, decisão atrasada equivale a decisão inútil.

Trata-se da mesma família de problema do timeout da Aula 4: quanto tempo esperar antes de concluir que a resposta não virá? Não existe valor universalmente correto; existe decisão consciente.

**[14:00–15:40 · Slide 12 — Funções como serviço e inicialização a frio]**

Passemos a um modelo de execução distinto: funções como serviço, o FaaS.

O FaaS executa um trecho de código em resposta a um evento — uma requisição HTTP, uma mensagem em fila, um arquivo criado — sem provisionamento contínuo de servidor. A cobrança incide sobre a execução, não sobre o tempo ocioso.

O modelo é vantajoso em cargas esporádicas e de volume variável. O envio do e-mail de confirmação de pedido é exemplo característico: ocorre em rajadas, é rápido e não justifica manter uma instância permanentemente em espera.

O custo está na inicialização a frio. Sem uma instância previamente ativa, a plataforma precisa inicializar um novo ambiente de execução antes de processar o evento, o que acrescenta latência.

O essencial é identificar quando esse custo é relevante. Em uma notificação assíncrona, a latência adicional não é percebida por ninguém, pois o e-mail chega uma fração de segundo depois.

Já em um caminho síncrono sensível à latência, como parte do fluxo de checkout, essa mesma latência incide diretamente sobre o p95 comprometido no SLO da Aula 13. Nesse caso, o modelo aparentemente econômico produz custo elevado em experiência do usuário.

**[15:40–17:20 · Slide 13 — Computação de borda: latência contra complexidade]**

Por fim, a computação de borda. A borda aproxima o processamento dos dispositivos, executando lógica em pontos geograficamente distribuídos, em vez de centralizá-la em uma região de nuvem.

*[indicação de edição: inserir Recurso visual 61 da Aula 15 — tabela comparando borda, regional e centralizado nos quatro critérios]*

Três localizações merecem comparação.

Na borda: latência mais baixa; contexto disponível limitado a sinais simples e locais do dispositivo; complexidade operacional alta, pela necessidade de manter versões de regras sincronizadas em muitos pontos.

Regional: latência intermediária; contexto parcial agregado; complexidade média.

Centralizada: latência mais alta; contexto de histórico amplo e completo; e complexidade operacional baixa, porque existe um único lugar para atualizar.

O padrão é claro: latência e contexto operam em sentidos opostos. Quanto mais próximo do usuário, menor o contexto disponível sobre ele.

A conclusão prática é que o ganho de latência tem preço. Manter lógica em múltiplos pontos aumenta a complexidade e nem sempre reduz custo. A orientação geral é reservar ao centro os modelos que dependem de histórico amplo, e destinar à borda os sinais simples e locais.

### Aplicação profissional

**[17:20–19:00 · Slide 14 — Pausa para reflexão: “vamos processar tudo na borda”]**

Esses critérios podem ser aplicados a uma proposta concreta, do tipo que costuma surgir na prática profissional.

A área de risco propõe processar toda a análise de fraude exclusivamente na borda, eliminando a dependência de uma região central, sob o argumento de que isso reduziria a latência a zero e eliminaria custos de rede.

*[indicação de edição: pausar a narração por 10 segundos com o texto “Tudo na borda: o que essa proposta ignora?” na tela]*

Quatro perguntas orientam a análise: que sinais de fraude dependem de contexto histórico dificilmente disponível apenas na borda? Que riscos operacionais decorrem de manter lógica duplicada em muitos pontos, sobretudo na atualização de um modelo? Em que medida a afirmação de latência reduzida a zero é tecnicamente imprecisa? E que combinação de borda e centro atenderia à decisão em segundos sem abrir mão do histórico?

As respostas são as seguintes. Quanto ao contexto: a constatação de que determinado dispositivo tentou quarenta cartões nas últimas 24 horas, em cinco cidades diferentes, constitui sinal de alto poder discriminante, e exige histórico agregado que nenhum ponto de borda isolado possui.

Quanto ao risco operacional: atualizar um modelo de fraude em duzentos pontos de presença, com versões possivelmente divergentes, é um problema de coordenação distribuída — exatamente a classe de problema tratada ao longo de toda a disciplina.

Quanto à latência zero: ela é fisicamente impossível. Processar próximo ao usuário reduz a latência de rede, mas não a elimina, tampouco elimina o tempo de processamento.

A resposta madura raramente consiste em concentrar tudo em um único lugar. Consiste em triagem local para sinais simples — bloqueio imediato de padrões evidentes na borda — combinada com avaliação aprofundada centralizada para o que exige contexto. Latência baixa onde ela é determinante; contexto completo onde ele é determinante.

### Fechamento

**[19:00–19:40 · Slides 15 e 16 — Pontos-chave e atividade prática]**

Recapitulando. Lote espera, fluxo não: lote atende análises que toleram espera, e fluxo atende decisões que precisam sair em segundos. Map, shuffle, reduce: o modelo se generalizou em DAGs, e a tolerância a falhas vem da reexecução de tarefas isoladas. Partição dimensiona: o número mínimo relaciona a taxa de eventos à capacidade comprovada por consumidor. Dois tempos diferentes: tempo de evento e de processamento divergem, e marcas d’água admitem atraso sem descartar a janela. FaaS troca ocioso por frio: reduz custo em carga esporádica ao preço de latência adicional na inicialização. E borda não é grátis: reduz latência de sinais simples, mas aumenta complexidade e nem sempre reduz custo.

Na atividade prática, você vai comparar três arquiteturas para a detecção de fraude quase em tempo real — lote horário, fluxo centralizado particionado por dispositivo, e triagem na borda combinada com fluxo centralizado. Você vai estimar a latência típica entre a tentativa e a decisão em cada uma, calcular as partições necessárias para 8 mil eventos por segundo com consumidor de mil por segundo, avaliar a capacidade de considerar o histórico do dispositivo, apontar o principal risco operacional de cada alternativa, recomendar uma delas justificando por latência, custo e complexidade, e indicar qual evidência coletaria para validar a recomendação em produção.

**[19:40–20:00 · Slide 17 — Encerramento]**

Esta aula forma a capacidade de escolher entre lote, fluxo, funções e borda a partir do requisito de negócio, e de dimensionar o pipeline resultante. A última aula da disciplina integra todo o percurso: como defender uma arquitetura completa com requisitos, riscos, custo e evidências.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 15 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com a sequência de cartões testados em um mesmo dispositivo (02:20–03:40).
- Recurso visual 58 — quadro comparativo entre lote e fluxo (aproximadamente 03:50).
- Recurso visual 59 — diagrama das fases de map, shuffle e reduce (aproximadamente 05:40).
- Slide 7 — cálculo do número de partições, com os quatro números em sequência (aproximadamente 07:30).
- Slide 9 — citação em tela cheia (10:20).
- Recurso visual 60 — linha do tempo dupla de tempo de evento e tempo de processamento (aproximadamente 10:50).
- Recurso visual 61 — tabela de borda, regional e centralizado (aproximadamente 15:50).
- Slide 14 — pausa de reflexão de 10 segundos (aproximadamente 17:40).
- Slide 17 — vinheta de encerramento e chamada para a próxima aula (últimos 15 segundos).

### Fontes e links de mídia

- DEAN, Jeffrey; GHEMAWAT, Sanjay. MapReduce: simplified data processing on large clusters. *Communications of the ACM*, v. 51, n. 1, p. 107-113, 2008. DOI: 10.1145/1327452.1327492 — referência conceitual, sem reprodução de trecho externo.
- AKIDAU, Tyler; CHERNYAK, Slava; LAX, Reuven. *Streaming Systems*. Sebastopol: O’Reilly Media, 2018 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; quadros, diagramas, fórmulas e linhas do tempo devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 15 (`unidade_4.md`) e do deck `unidade_4/slides/aula15.html`.

---

## Roteiro da Videoaula 16 — “Defender a arquitetura diante do conselho”

**Vínculo com o plano de aprendizagem:** Unidade 4, Aula 16 — Projeto integrado e avaliação arquitetural.

**Deck de apoio:** `unidade_4/slides/aula16.html` — 19 slides (capa, audiodescrição, sumário, 15 de conteúdo e encerramento).

**Objetivo da videoaula:** ao final, o estudante deve ser capaz de explicitar tensões entre requisitos funcionais e atributos de qualidade e resolvê-las por dado, estimar capacidade a partir de evidências operacionais, escrever um ADR completo, conduzir uma análise de pontos únicos de falha, definir RPO e RTO a partir de requisitos de negócio e defender uma arquitetura completa com requisitos, riscos, custo e evidências.

**Mapa de tempo e slides:** 00:00 capa · 00:25 audiodescrição · 00:55 sumário · 01:40 objetivos · 02:20 situação-problema · 03:40 requisitos e atributos de qualidade · 05:20 exemplo numérico revisitado · 07:00 registros de decisão arquitetural · 08:40 as decisões acumuladas · 10:10 citação · 10:30 pontos únicos de falha · 12:20 RPO e RTO · 13:50 seguro e observável por padrão · 15:10 exemplo numérico da redundância paralela · 16:50 custo e evolução · 18:00 a trajetória completa · 19:00 pontos-chave e atividade · 19:30 encerramento da disciplina.

### Abertura contextualizada

**[00:00–00:25 · Slide 0 — Capa]**

Esta é a última aula da disciplina, dedicada ao projeto integrado e à avaliação arquitetural. O exercício proposto difere de todos os anteriores: em vez de apresentar um mecanismo novo, ele consiste em sustentar tecnicamente tudo o que foi estudado.

**[00:25–00:55 · Slide 1 — Audiodescrição]**

A audiodescrição desta aula: mantemos o fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o conteúdo em cartões claros. São cinco recursos visuais: a tabela comparando insumos estimados e insumos medidos, a estrutura de um registro de decisão arquitetural, a retrospectiva das decisões por unidade, a fórmula da redundância paralela e o quadro final da trajetória da NexaOrder. Descrevo cada um conforme aparecem.

**[00:55–01:40 · Slide 2 — Sumário]**

Este é o percurso da aula. Começo separando requisitos funcionais de atributos de qualidade e demonstrando como resolver a tensão entre eles. Revisito depois a estimativa de carga e capacidade da Aula 1, agora com insumos distintos. Apresento em seguida os registros de decisão arquitetural, conduzo uma análise de pontos únicos de falha e defino RPO e RTO. Trato de segurança e observabilidade desde o projeto, de custo, sustentabilidade e evolução, e fecho revendo a trajetória completa da NexaOrder pelas quatro unidades.

**[01:40–02:20 · Slide 3 — Objetivos de aprendizagem]**

Ao final da aula, você deve conseguir explicitar tensões entre requisitos funcionais e atributos de qualidade, e resolvê-las por dado. Deve estimar capacidade a partir de evidências operacionais, e não de suposições. Deve escrever um ADR completo, com contexto, alternativas, decisão e consequências aceitas. Deve conduzir uma análise de pontos únicos de falha atenta a dependências ocultas. Deve definir RPO e RTO a partir de requisitos de negócio, e não de conveniência técnica. E deve defender uma arquitetura completa com requisitos, riscos, custo e evidências.

**[02:20–03:40 · Slide 4 — Situação-problema]**

A situação desta aula não é um incidente, e sim uma reunião.

A diretoria convoca a engenharia para uma revisão formal, antes de aprovar o orçamento do próximo ciclo. A questão não é se o sistema funciona — isso já está demonstrado, pois o sistema está em operação e os pedidos estão sendo processados.

As perguntas são outras três. Por que essa arquitetura sustenta o crescimento previsto? Por que ela resiste às falhas mais prováveis? E por que justifica o investimento contínuo que exige?

Nenhuma dessas perguntas se responde com um diagrama elegante ou com o nome de uma tecnologia. A resposta exige requisitos, estimativas, decisões documentadas e evidências.

É precisamente isso que a disciplina inteira preparou para produzir. Esta aula estrutura essa defesa.

### Desenvolvimento conceitual

**[03:40–05:20 · Slide 5 — Requisitos funcionais e atributos de qualidade]**

O ponto de partida é o vocabulário da avaliação.

Requisitos funcionais definem o que o sistema deve fazer: o cliente deve conseguir finalizar uma compra. Atributos de qualidade definem como ele deve se comportar: desempenho, disponibilidade, segurança, manutenibilidade, escalabilidade, custo.

A primeira afirmação é contraintuitiva para muitos: não há hierarquia entre os dois na avaliação arquitetural. Atributos de qualidade não constituem requisitos não funcionais de segunda ordem. Um sistema que finaliza compras em quarenta segundos cumpre o requisito funcional e, ainda assim, falha por completo.

O ponto central é que ambos entram em tensão, e resolver essa tensão explicitamente é parte essencial do trabalho de projeto.

O caso da NexaOrder ilustra isso. A área de produto demanda latência mínima no catálogo, com abertura imediata da página. A área de confiabilidade demanda garantias mais fortes no saldo de estoque, para que não se venda o que não existe.

Uma avaliação imatura escolheria um dos lados, priorizando desempenho ou consistência em bloco. Uma avaliação madura não faz essa escolha em termos absolutos: aceita leitura eventualmente consistente no catálogo e exige consistência mais forte no instante da reserva.

O raciocínio é exatamente o da Aula 5: a decisão é por dado, não por sistema inteiro.

**[05:20–07:00 · Slide 6 — Exemplo numérico: a mesma fórmula, insumos diferentes]**

O ponto seguinte encerra um arco aberto na primeira aula.

*[indicação de edição: inserir Recurso visual 62 da Aula 16 — tabela comparando os insumos da Aula 1 e os da Aula 16, lado a lado]*

A fórmula da Aula 1 estabelecia que o número de instâncias é o teto da divisão entre a taxa de pico e o produto da capacidade da instância pela utilização-alvo.

Três unidades depois, a fórmula permanece idêntica. O que mudou foram os insumos, que deixaram de ser suposições.

A capacidade por instância, na Aula 1, era uma estimativa isolada, pouco mais que uma aproximação informada. Nesta aula, ela provém de testes de carga reais, conduzidos com o rigor apresentado na Aula 14.

A taxa de pico, na Aula 1, era projeção de negócio. Agora é refinada por métricas históricas, coletadas pela instrumentação da Aula 13.

A utilização-alvo, que na Aula 1 era convenção adotada por hábito, agora é calibrada pelo orçamento de erro e pelo SLO acordado com o negócio.

A lição é que a avaliação arquitetural madura não estima capacidade a partir de suposições, e sim de evidências operacionais acumuladas ao longo do ciclo de vida do sistema. A fórmula é a mesma; a qualidade da resposta é substancialmente distinta.

**[07:00–08:40 · Slide 7 — Registros de decisão arquitetural]**

O instrumento de documentação que sustenta a defesa é o ADR, registro de decisão arquitetural.

Um ADR documenta uma escolha significativa: o contexto que a motivou, as alternativas consideradas, a decisão tomada e as consequências esperadas.

A diferença entre um registro inadequado e um registro completo é reveladora.

Não constitui um ADR a mera declaração de que se decidiu adotar determinada tecnologia. Um nome de produto não é registro útil: dois anos depois, ninguém consegue avaliar se a decisão permanece válida.

Constitui um ADR o registro de por que a orquestração automatizada era necessária e qual problema operacional resolvia; de quais alternativas foram avaliadas — implantação manual, serviço gerenciado mais simples; e de quais consequências foram aceitas — a curva de aprendizado da equipe, o custo de operação do cluster.

O ADR registra, portanto, o motivo e o preço, e não apenas a escolha.

O valor de reunir esses registros é permitir que qualquer pessoa recém-integrada à equipe compreenda não apenas o estado atual do sistema, mas o raciocínio que conduziu a ele. Sem esse registro, cada nova geração de engenheiros examina decisões antigas sem acesso ao contexto, atribui incompetência a quem as tomou e reescreve o sistema, repetindo os mesmos erros.

**[08:40–10:10 · Slide 8 — As decisões que a NexaOrder acumulou]**

A defesa começa a tomar forma na retrospectiva das decisões acumuladas.

*[indicação de edição: inserir Recurso visual 63 da Aula 16 — retrospectiva das decisões centrais por unidade, revelada linha a linha]*

Da Unidade 1, a decisão central foi manter múltiplas instâncias sem estado atrás de um balanceador. O compromisso aceito: sessões locais deixam de ser confiáveis, e o banco pode virar gargalo.

Da Unidade 2, consistência eventual no catálogo e forte na reserva de estoque. O compromisso: duas políticas convivendo no mesmo sistema, com regras distintas — o que exige que a equipe saiba explicar qual vale onde.

Da Unidade 3, decomposição por contexto delimitado e arquitetura orientada a eventos. O compromisso: composição explícita no lugar de JOIN, e a necessidade de rastrear a progressão de cada pedido.

Da Unidade 4, observabilidade instrumentada e política de testes de resiliência. O compromisso: custo contínuo de telemetria e de experimentos controlados.

A coluna da direita concentra o essencial: toda decisão tem um preço declarado. Uma arquitetura defensável não é aquela isenta de custos, e sim aquela cujos custos foram escolhidos conscientemente e estão registrados.

**[10:10–10:30 · Slide 9 — Citação]**

Esta é a frase que encerra a disciplina: cada decisão arquitetural deve ser tratada como hipótese verificável, e não como dogma.

### Demonstração, exemplo ou estudo de caso

**[10:30–12:20 · Slide 10 — Análise de pontos únicos de falha]**

Passemos à parte da defesa que trata de risco.

A análise de SPOF — single point of failure — identifica componentes cuja indisponibilidade isolada comprometeria todo o fluxo, mesmo com o restante do sistema em operação normal. Ela exige atenção especial às dependências ocultas.

A NexaOrder pode ser percorrida sob essa lente.

O gateway: sua indisponibilidade compromete a entrada de todos os fluxos externos? Em caso afirmativo, trata-se de um SPOF, por mais confiável que seja o componente.

O banco de dados de pedidos: há réplica promovível e o failover foi ensaiado? O termo ensaiado é decisivo — um failover nunca testado permanece hipótese, conforme discutido na Aula 14.

O sistema de mensageria: uma instância isolada utilizada por todas as réplicas de pagamento constitui SPOF dissimulado. O diagrama exibe quatro réplicas de pagamento e aparenta redundância, mas as quatro dependem da mesma fila.

O provedor de identidade: sem ele, o mTLS e a autorização deixam de funcionar, e o sistema inteiro perde a capacidade de comunicação interna.

O coletor de observabilidade: sua indisponibilidade priva a equipe de visibilidade justamente durante o incidente. É o SPOF habitualmente omitido das listas, por não estar no caminho da requisição — embora esteja no caminho do diagnóstico.

A armadilha central é que réplicas em várias zonas não eliminam o SPOF se todas dependerem de um único componente não replicado. É a mesma lição da Aula 1 sobre redundância que compartilha ponto de falha, aplicada agora ao sistema como um todo.

**[12:20–13:50 · Slide 11 — Plano de recuperação: RPO e RTO]**

Identificados os riscos, segue-se o plano de recuperação, expresso em dois números.

RPO, recovery point objective, mede quanto de dado o negócio aceita perder. Na NexaOrder, aproximadamente 5 minutos — que é o intervalo da replicação assíncrona para a região secundária. Se a região primária for perdida, os últimos 5 minutos de escrita podem não estar lá.

RTO, recovery time objective, mede em quanto tempo o serviço precisa voltar. Na NexaOrder, aproximadamente 15 minutos — o tempo de promover a região secundária e restabelecer o serviço.

O aspecto decisivo na discussão com a diretoria é que esses dois números se definem a partir de requisitos de negócio, e não de conveniência técnica.

A pergunta pertinente não é quanto a engenharia consegue entregar, e sim quantos minutos de pedidos a empresa aceita perder e por quantos minutos aceita permanecer indisponível. A resposta a essas perguntas orienta diretamente decisões de replicação, frequência de backup e automação de failover.

A ordem inversa não produz plano algum. Definir RPO e RTO a partir do que a infraestrutura atual já alcança equivale a descrever o estado vigente sob outra denominação.

**[13:50–15:10 · Slide 12 — Seguro e observável por padrão]**

Há um princípio de processo que sustenta todo o conteúdo das Unidades 3 e 4.

Segurança e observabilidade tratadas como camadas acrescentadas ao final tendem a permanecer incompletas e a exigir correções custosas. O princípio é amplamente reconhecido em tese e, ainda assim, frequentemente violado na prática, porque no início do projeto essas dimensões aparentam ser adiáveis.

A prática recomendada as incorpora ao desenho inicial de cada componente, e o meio de garantir isso é converter princípios em perguntas de aceite.

Todo novo serviço nasce com identidade própria e comunicação autenticada? Todo novo fluxo crítico nasce instrumentado, com métricas, logs e traces correlacionáveis? Ou a instrumentação é acrescentada somente após o primeiro incidente que a tornou indispensável?

O passo decisivo é organizacional, e não técnico: essas perguntas devem se tornar critérios de aceite de um novo serviço, e não sugestões em um documento de boas práticas. Um serviço sem identidade e sem instrumentação não entra em produção, do mesmo modo que não entra um serviço sem testes.

**[15:10–16:50 · Slide 13 — Exemplo numérico: cadeia sequencial e redundância paralela]**

Um último cálculo encerra o arco aberto na Aula 2 e retomado na Aula 14.

*[indicação de edição: inserir Recurso visual 64 da Aula 16 — fórmula da redundância paralela contrastada com a da cadeia sequencial]*

Considere uma instância com 99,5% de disponibilidade, valor modesto. Acrescentem-se três réplicas independentes, sem dependência compartilhada, atrás de um balanceador que direciona o tráfego para qualquer réplica saudável.

A disponibilidade combinada é 1 menos a probabilidade de todas falharem: 1 menos 0,005 elevado a 3, que dá aproximadamente 0,999999875. Isso é cerca de sete noves.

A comparação com a cadeia sequencial da Aula 14, que reduzia quatro serviços de 99,9% para 99,6%, evidencia o contraste.

A diferença é expressiva e estrutural. Em série, as disponibilidades se multiplicam e o resultado piora. Em paralelo, as indisponibilidades se multiplicam e o resultado melhora de forma acentuada.

Duas ressalvas se impõem, dado o efeito persuasivo desse número de sete noves. Primeira: o cálculo pressupõe independência de falha. Três réplicas no mesmo rack, ou dependentes do mesmo banco, não são independentes, e o valor real fica muito abaixo do calculado. Segunda: o arranjo triplica o custo de manutenção.

A conclusão é dupla. O que sustenta disponibilidade elevada é redundância paralela com independência de falha, e não a simples multiplicação de instâncias. E o ganho só se justifica pelo valor de negócio que a disponibilidade adicional efetivamente entrega: sete noves em um serviço interno representam investimento sem retorno.

**[16:50–18:00 · Slide 14 — Custo, sustentabilidade e evolução]**

O último tema da defesa é a razão de o investimento ser contínuo.

Nenhuma arquitetura permanece ótima. Padrões de tráfego mudam, requisitos novos surgem, decisões envelhecem. O que era adequado há dois anos pode ser inadequado hoje, sem que tenha havido erro à época.

O desperdício típico é a capacidade provisionada para o pico e mantida constante em horários de demanda mínima, o que significa pagar pelo volume de pico durante períodos de tráfego reduzido.

A resposta inadequada a esse desperdício é eliminar a redundância necessária aos picos — economia que produz o incidente seguinte.

A resposta madura é o escalonamento automático, que ajusta a capacidade à demanda observada, conforme o mecanismo da Aula 11, preservando as metas de disponibilidade definidas sem manter recursos ociosos custeados por padrão.

O princípio a registrar é que a evolução contínua integra o projeto, e não indica que ele tenha sido mal executado. Um sistema que nunca muda não é maduro; está abandonado.

### Aplicação profissional

**[18:00–19:00 · Slide 15 — A trajetória completa da NexaOrder]**

Cabe encerrar examinando o percurso completo.

*[indicação de edição: inserir Recurso visual 65 da Aula 16 — quadro da trajetória completa, revelando uma unidade por vez]*

A Unidade 1 estabeleceu os fundamentos: o que caracteriza um sistema distribuído, como processos se comunicam, por que tempo e ordenação deixam de ser triviais e como falhas parciais exigem contenção deliberada.

A Unidade 2 tratou dos dados: replicação, particionamento, CAP e PACELC, consenso via Raft, transações distribuídas com sagas e idempotência.

A Unidade 3 tratou dos serviços: limites de domínio explícitos, arquitetura orientada a eventos, orquestração em contêineres e comunicação segura.

A Unidade 4 tratou da operação: observabilidade para diagnosticar, testes e caos para validar, processamento em escala e avaliação arquitetural integrada.

O ponto final da disciplina é este: nenhuma unidade entrega, isoladamente, uma arquitetura completa. É possível reunir fundamentos sólidos e operar sem visibilidade alguma; dispor de observabilidade impecável sobre um monólito distribuído; ou manter serviços bem delimitados sobre dados inconsistentes.

É a combinação — fundamentos sólidos, dados bem distribuídos, serviços bem delimitados e operação validada — que sustenta um sistema em produção, sob carga real, ao longo do tempo.

### Fechamento

**[19:00–19:30 · Slides 16 e 17 — Pontos-chave e atividade prática]**

Recapitulando. Tensão é normal: requisitos funcionais e atributos de qualidade colidem, e a avaliação resolve isso por dado, não em bloco. Estimar com evidência: depois de quatro unidades, capacidade se calcula com testes de carga e métricas históricas reais. ADR guarda o porquê: um registro útil traz contexto, alternativas e consequências aceitas, não um nome de tecnologia. SPOF se esconde: réplicas em várias zonas não bastam se todas dependerem de um mesmo componente não replicado. RPO e RTO vêm do negócio, e orientam replicação, backup e failover — não o contrário. E paralelo, não sequencial: redundância independente eleva a disponibilidade, enquanto encadear serviços a reduz.

A atividade prática desta aula é a defesa arquitetural completa da NexaOrder para uma banca de revisão: três requisitos funcionais e três atributos de qualidade, com uma tensão explícita e como foi resolvida; um ADR completo para uma decisão de qualquer unidade da disciplina; uma análise de pontos únicos de falha com ao menos dois riscos não triviais; RPO e RTO para o fluxo de pedidos com justificativa de negócio; a descrição de como segurança e observabilidade entram no desenho de um novo serviço; e um cenário de pico e um de falha, explicando a resposta da arquitetura com evidências das aulas anteriores.

**[19:30–20:00 · Slide 18 — Encerramento da disciplina]**

Chegamos ao encerramento da disciplina.

A NexaOrder começou como uma aplicação em um único servidor, na qual duas pessoas adquiriam o mesmo último item sem que houvesse explicação disponível para o fenômeno. Essa explicação agora existe: é possível nomear a concorrência que o permitiu, o mecanismo que a controla, o custo que esse mecanismo introduz e a evidência que comprovaria seu funcionamento.

Essa é a diferença que a disciplina se propôs a produzir: não a memorização de padrões, mas a compreensão de por que cada um existe, o que cobra em troca e como verificar se cumpre o que promete.

Fica a formulação apresentada no slide de citação: cada decisão arquitetural deve ser tratada como hipótese verificável, e não como dogma. As tecnologias mudarão; esse raciocínio permanece.

Encerro aqui o percurso, com votos de bons estudos e de boa prática profissional — especialmente nos momentos em que algum sistema falhar.

### Indicações de edição e recursos visuais

- Slide 0 — capa da Aula 16 (00:00–00:25).
- Slide 1 — audiodescrição narrada integralmente (00:25–00:55).
- Slide 4 — situação-problema, com as três perguntas da diretoria destacadas uma a uma (02:20–03:40).
- Recurso visual 62 — tabela comparando insumos da Aula 1 e da Aula 16 (aproximadamente 05:30).
- Slide 7 — estrutura de um ADR, contrastando o registro inútil e o registro completo (aproximadamente 07:10).
- Recurso visual 63 — retrospectiva das decisões centrais por unidade (aproximadamente 08:50).
- Slide 9 — citação em tela cheia, com 5 segundos de silêncio antes da leitura (10:10).
- Slide 10 — análise de SPOF, com cada componente sendo marcado conforme a narração (aproximadamente 10:40).
- Recurso visual 64 — fórmula da redundância paralela contrastada com a da cadeia sequencial (aproximadamente 15:20).
- Recurso visual 65 — quadro da trajetória completa da NexaOrder, revelando uma unidade por vez (18:00–19:00).
- Slide 18 — encerramento da disciplina, com vinheta final estendida (últimos 30 segundos).

### Fontes e links de mídia

- BASS, Len; CLEMENTS, Paul; KAZMAN, Rick. *Software Architecture in Practice*. 4. ed. Boston: Addison-Wesley, 2021 — referência conceitual, sem reprodução de trecho externo.
- NYGARD, Michael T. Documenting architecture decisions. *Cognitect Blog*, 2011 — referência conceitual, sem reprodução de trecho externo.
- Nenhuma mídia de terceiros é incorporada; tabelas, quadros retrospectivos e fórmulas devem ser produzidos originalmente pela equipe de edição a partir do texto-base da Aula 16 (`unidade_4.md`) e do deck `unidade_4/slides/aula16.html`.
