"""Conteúdo dos decks da Unidade 4 — Operação, validação e evolução."""

from slides_kit import (
    audiodescricao, capa, citacao, destaque, encerramento, formula, montar,
    numeros, p, pontos_chave, slide, sumario, tabela, ul,
)

SUB = "Unidade 4 — Operação, validação e evolução"

# ---------------------------------------------------------------- Aula 13

A13 = montar([
    capa(13, "Observabilidade e diagnóstico distribuído", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um quadro com os três "
        "pilares — métricas, logs e traces — convergindo para uma investigação única; um fluxo de "
        "propagação do identificador de correlação entre gateway, pedidos, estoque e pagamento; um "
        "painel numérico com o orçamento de erro mensal de doze mil requisições; um gráfico de consumo "
        "acelerado desse orçamento nos primeiros dez dias; e um diagrama de cascata do pedido de doze "
        "segundos, com a espera em fila dentro do span de pagamento."
    ),
    sumario("Observabilidade e diagnóstico distribuído", [
        "Monitoramento e observabilidade não são sinônimos",
        "Métricas, logs e traces: três pilares complementares",
        "Contexto e correlação distribuída",
        "Instrumentação com OpenTelemetry",
        "Indicadores de nível de serviço (SLI)",
        "Objetivos (SLO) e orçamento de erro",
        "Taxa de consumo e decisão operacional",
        "Diagnóstico de latência em cascata",
    ]),
    slide(13, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Distinguir</strong> monitoramento de observabilidade pelo tipo de pergunta que cada um responde.",
              "<strong>Combinar</strong> métricas, logs e traces reconhecendo o que cada pilar não consegue responder sozinho.",
              "<strong>Projetar</strong> a propagação de um identificador de correlação, inclusive em comunicação assíncrona.",
              "<strong>Escolher</strong> SLIs que reflitam a experiência do usuário, e não a saúde da infraestrutura.",
              "<strong>Calcular</strong> o orçamento de erro de um SLO e interpretar sua taxa de consumo.",
              "<strong>Ler</strong> um trace em cascata para localizar onde a latência foi realmente gasta.",
          ]), visual="map"),
    slide(13, "Situação-problema", "Um pedido que sumiu por doze segundos",
          p("Um cliente relata que a compra levou <strong>doze segundos</strong> entre o clique e a "
            "confirmação — sem erro visível. A equipe abre o painel de infraestrutura:") + "\n" +
          ul([
              "CPU, memória e rede dos quatro serviços <strong>dentro da faixa normal</strong>.",
              "<strong>Nenhum alerta</strong> disparou; <strong>nenhum serviço</strong> reiniciou.",
              "Cada log, lido isoladamente, registra <strong>tempo aceitável</strong> para a própria parte.",
              "Ninguém consegue <strong>reconstruir a jornada completa</strong> daquele pedido pelos quatro serviços.",
          ]) + "\n" +
          destaque("Os logs existem, mas <strong>sem um identificador comum</strong> que permita juntá-los na "
                   "ordem certa. A equipe sabe que “alguma coisa” demorou doze segundos, mas não sabe onde — "
                   "porque nunca projetou o sistema para responder a essa pergunta."),
          visual="timeline"),
    slide(13, "Conteúdo", "Monitoramento e observabilidade",
          tabela(["", "Monitoramento", "Observabilidade"], [
              ["O que faz", "Observa indicadores previamente definidos e alerta ao ultrapassar limites", "Permite inferir o estado interno a partir dos dados expostos"],
              ["Que perguntas responde", "As que já foram antecipadas: “a CPU está alta?”", "As que ninguém formulou antes do incidente"],
              ["Exige prever falhas?", "Sim — um painel por modo de falha esperado", "Não — expõe dados ricos e correlacionáveis"],
              ["No incidente dos 12 s", "Mais painéis de CPU não resolveriam", "Permite perguntar “o que houve com este pedido?” e obter resposta"],
          ]) + "\n" +
          destaque("A diferença é <strong>prática, não terminológica</strong>: observabilidade é a capacidade de "
                   "fazer uma pergunta nova e obtê-la respondida a partir de dados <em>já coletados</em>, sem "
                   "reproduzir o problema manualmente.")),
    slide(13, "Conteúdo", "Os três pilares",
          tabela(["Pilar", "O que é", "Força", "Limitação"], [
              ["<strong>Métricas</strong>", "Valores numéricos agregados ao longo do tempo", "Compactas, baratas de reter, boas para tendência e alerta", "A agregação esconde <em>quais</em> requisições falharam e por quê"],
              ["<strong>Logs</strong>", "Registros discretos de eventos, em texto estruturado", "Ricos em contexto local", "Sem correlação, permanecem fragmentos isolados"],
              ["<strong>Traces</strong>", "O caminho de uma requisição, decomposto em spans", "Mostram onde o tempo foi gasto e em que ordem", "Custo maior de instrumentação e armazenamento"],
          ]) + "\n" +
          destaque("Nenhum substitui os outros. <strong>Métricas</strong> indicam que algo mudou; "
                   "<strong>traces</strong> mostram onde, dentro de uma requisição específica, isso aconteceu; "
                   "<strong>logs</strong> detalham o que exatamente ocorreu naquele ponto.")),
    slide(13, "Conteúdo", "Contexto e correlação distribuída",
          p("O que transforma logs e traces dispersos em uma narrativa coerente é a <strong>correlação</strong>. "
            "Cada requisição recebe um identificador único no primeiro componente que a toca — normalmente o "
            "gateway.") + "\n" +
          ul([
              "<strong>1. O gateway gera</strong> o identificador de correlação (<em>trace ID</em>) na entrada.",
              "<strong>2. Chamadas síncronas</strong> propagam o identificador em um cabeçalho da requisição.",
              "<strong>3. Eventos assíncronos</strong> propagam o identificador nos metadados da mensagem.",
              "<strong>4. Cada serviço extrai e reinjeta</strong> — a propagação é responsabilidade explícita da instrumentação.",
          ]) + "\n" +
          destaque("Se <strong>um único serviço</strong> no meio do caminho falhar em propagar o contexto, o "
                   "trace se rompe ali — e a jornada completa deixa de poder ser reconstruída, mesmo que cada "
                   "serviço tenha registrado corretamente seus próprios dados."),
          visual="flow"),
    slide(13, "Erro comum", "Identificador de requisição não é dimensão de métrica",
          ul([
              "<strong>O impulso</strong> — “se o trace ID resolve os logs, vamos colocá-lo também nas métricas”.",
              "<strong>O problema</strong> — identificadores por requisição criam <strong>cardinalidade praticamente ilimitada</strong>.",
              "<strong>A consequência</strong> — o custo de armazenamento e consulta das métricas explode.",
              "<strong>O certo</strong> — métricas usam <em>dimensões agregáveis</em>: rota, código de status, região, versão.",
              "<strong>A ponte correta</strong> — <em>exemplars</em> ligam um ponto da métrica a um trace específico.",
              "<strong>A regra</strong> — métricas agregam; traces individualizam. Não troque os papéis.",
          ]), visual="compare"),
    slide(13, "Conteúdo", "Instrumentação com OpenTelemetry",
          p("Historicamente, cada fornecedor definia seu próprio formato de instrumentação — trocar de "
            "ferramenta significava reescrever código. O <strong>OpenTelemetry</strong> é um padrão aberto e "
            "neutro que unifica métricas, logs e traces sob uma mesma API.") + "\n" +
          ul([
              "<strong>Captura automática</strong> — chamadas HTTP recebidas e enviadas, consultas a banco, publicação e consumo de mensagens.",
              "<strong>Spans personalizados</strong> — o código adiciona operações de negócio como “reservar item” ou “autorizar pagamento”.",
              "<strong>Coletor</strong> — recebe a telemetria, processa e encaminha ao backend de armazenamento e visualização.",
              "<strong>Ganho real</strong> — trocar o sistema de análise costuma preservar a instrumentação, exigindo ajustar apenas o <em>exporter</em> ou o destino.",
          ]) + "\n" +
          destaque("O desacoplamento não é total: <strong>convenções semânticas, recursos proprietários e "
                   "capacidades diferentes</strong> entre ferramentas ainda podem exigir adaptações."),
          visual="map"),
    citacao(
        "“Monitoramento responde a perguntas antecipadas; observabilidade permite investigar perguntas "
        "que ninguém formulou antes do incidente.”",
        "— síntese da Aula 13"),
    slide(13, "Conteúdo", "SLI: escolher o que medir",
          p("Um <strong>indicador de nível de serviço</strong> é uma medida quantitativa do comportamento "
            "observado, calculada a partir de dados reais de produção. Bons SLIs refletem a experiência de "
            "quem usa o sistema:") + "\n" +
          ul([
              "Proporção de requisições de checkout <strong>concluídas com sucesso</strong> sobre o total de tentativas.",
              "Proporção de requisições concluídas <strong>dentro de um limite de latência</strong>, por exemplo 300 ms.",
              "Proporção de confirmações de pagamento processadas <strong>corretamente na primeira tentativa</strong>.",
          ]) + "\n" +
          destaque("O erro comum é escolher o indicador <strong>fácil de coletar</strong> — utilização média de "
                   "CPU — em vez do relevante. A CPU pode ficar confortável enquanto uma fração significativa "
                   "de pedidos falha por esgotamento de conexões. Um bom SLI é aquele que, "
                   "<strong>quando ruim, corresponde a uma experiência ruim</strong>."),
          visual="map"),
    slide(13, "Exemplo numérico", "Do SLO ao orçamento de erro",
          p("Um <strong>SLO</strong> é a meta definida para um SLI ao longo de um período: “99,9% dos "
            "checkouts concluídos com sucesso, medido mensalmente”. A diferença entre 100% e o SLO é o "
            "<strong>orçamento de erro</strong>:") + "\n" +
          formula("E = ( 1 − SLO ) × V") + "\n" +
          numeros([
              ("12.000.000", "requisições/mês (V)"),
              ("99,9%", "objetivo (SLO)"),
              ("12.000", "falhas toleradas (E)"),
              ("9.000", "consumidas em 10 dias"),
          ]) + "\n" +
          destaque("<strong>75% do orçamento em um terço do período</strong>: a taxa de consumo está muito acima "
                   "do que o restante do mês suporta. Esse número orienta uma decisão concreta — reduzir "
                   "mudanças arriscadas, priorizar estabilidade e investigar a causa antes que o orçamento se "
                   "esgote.")),
    slide(13, "Conteúdo", "O orçamento de erro legitima o risco calculado",
          ul([
              "<strong>Enquanto há orçamento</strong> — a equipe tem margem para implantar, experimentar e evoluir o sistema.",
              "<strong>Quando ele se esgota</strong> — uma política previamente acordada desloca a prioridade para a estabilidade.",
              "<strong>O ganho</strong> — o critério passa a ser <em>observável</em>, e não uma discussão subjetiva sobre o que é “seguro o suficiente”.",
              "<strong>O efeito cultural</strong> — confiabilidade deixa de ser oposta à entrega e passa a ser o que a torna sustentável.",
          ]) + "\n" +
          destaque("Sem orçamento declarado, toda discussão sobre ritmo de mudança vira <strong>opinião</strong>. "
                   "Com ele, vira <strong>leitura de um número</strong> combinado antecipadamente."),
          visual="compare"),
    slide(13, "Exemplo numérico", "O trace em cascata do pedido de doze segundos",
          tabela(["Span", "Duração", "O que revela"], [
              ["Gateway (raiz)", "12.000 ms", "O intervalo completo percebido pelo cliente"],
              ["Pedidos", "11.950 ms", "Quase todo o tempo está dentro deste span"],
              ["Estoque", "35 ms", "Descartado como suspeito"],
              ["Pagamento", "11.780 ms", "Concentra o caminho crítico"],
              ["↳ espera em fila", "11.450 ms", "<strong>A causa</strong> — não é o provedor externo"],
              ["↳ chamada ao provedor", "310 ms", "Comportamento normal"],
          ]) + "\n" +
          destaque("Spans aninhados <strong>não se somam</strong> como se fossem sequenciais: a cascata e as "
                   "relações pai-filho é que revelam a causa. A expedição, assíncrona, começa após a resposta e "
                   "<strong>não pertence ao caminho crítico</strong> do cliente.")),
    pontos_chave(13, [
        ("Duas capacidades distintas", "Monitoramento cobre o previsto; observabilidade permite investigar o que ninguém antecipou."),
        ("Três pilares, um incidente", "Métricas apontam a mudança, traces localizam o ponto, logs explicam o que houve ali."),
        ("Correlação é explícita", "O identificador só atravessa o sistema se cada serviço o extrair e reinjetar — inclusive em eventos."),
        ("Padrão neutro", "OpenTelemetry desacopla a instrumentação da ferramenta de análise, sem eliminar toda adaptação."),
        ("SLI olha o usuário", "Um bom indicador é ruim exatamente quando a experiência de quem usa o serviço é ruim."),
        ("Orçamento decide o ritmo", "A taxa de consumo do orçamento de erro converte confiabilidade em critério operacional observável."),
    ]),
    slide(13, "Atividade prática", "Mãos à obra: reconstruir um trace",
          p("Reconstrua, em tabela ou diagrama, o trace de um pedido que atravessa gateway, pedidos, "
            "estoque, pagamento e expedição.") + "\n" +
          ul([
              "<strong>1.</strong> Atribua a cada serviço um tempo de execução hipotético, em milissegundos.",
              "<strong>2.</strong> Identifique qual serviço concentra a maior parte do tempo total.",
              "<strong>3.</strong> Proponha um identificador de correlação e descreva sua propagação, incluindo o evento assíncrono da expedição.",
              "<strong>4.</strong> Defina um SLI e um SLO para o fluxo completo de checkout.",
              "<strong>5.</strong> Calcule o orçamento de erro mensal para um volume hipotético.",
              "<strong>6.</strong> Liste dois logs e duas métricas que, somados ao trace, confirmariam a causa raiz.",
          ]), visual="map"),
    encerramento(
        "Você já sabe instrumentar um sistema para responder a perguntas que ninguém previu, e converter "
        "confiabilidade em um número operável. Na próxima aula, deixamos de presumir que os mecanismos de "
        "resiliência funcionam e passamos a prová-lo deliberadamente.",
        "Próxima aula: Aula 14 — Resiliência, testes distribuídos e engenharia do caos."),
])

# ---------------------------------------------------------------- Aula 14

A14 = montar([
    capa(14, "Resiliência, testes distribuídos e engenharia do caos", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: uma pirâmide de testes "
        "com base ampla de unitários e topo estreito de ponta a ponta; três gráficos comparando os "
        "perfis de carga dos testes de carga, estresse e duração; um diagrama da ampliação progressiva "
        "do raio de impacto de um experimento de caos; um cartão de planejamento de experimento com "
        "hipótese, perturbação e critério de interrupção; e um painel numérico com a disponibilidade "
        "combinada de quatro serviços de 99,9%."
    ),
    sumario("Resiliência, testes distribuídos e engenharia do caos", [
        "A pirâmide de testes em um sistema distribuído",
        "Testes de contrato: verificar acordos sem executar tudo",
        "Testes de carga, estresse e duração",
        "Engenharia do caos: injetar falha para aprender",
        "Hipótese de estado estável",
        "Raio de impacto e mecanismo de interrupção",
        "Por que a resiliência de cada serviço não basta",
        "Postmortem sem culpabilização",
    ]),
    slide(14, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Dimensionar</strong> a pirâmide de testes reconhecendo o custo do topo em sistemas distribuídos.",
              "<strong>Aplicar</strong> testes de contrato para detectar incompatibilidade antes da implantação.",
              "<strong>Distinguir</strong> teste de carga, de estresse e de duração pela pergunta que cada um responde.",
              "<strong>Formular</strong> uma hipótese de estado estável mensurável para um experimento de caos.",
              "<strong>Delimitar</strong> raio de impacto e critério de interrupção antes de executar em produção.",
              "<strong>Calcular</strong> a disponibilidade combinada de uma cadeia de serviços e interpretar o resultado.",
          ]), visual="map"),
    slide(14, "Situação-problema", "O teste que nunca foi feito",
          p("Durante uma promoção de fim de ano, o provedor de pagamento apresentou instabilidade de poucos "
            "minutos. O circuito de proteção da Unidade 1 <strong>deveria</strong> isolar a falha. Não foi o "
            "que aconteceu:") + "\n" +
          ul([
              "O serviço de pedidos aguardava a resposta de forma síncrona <strong>em um ponto do código que ninguém havia testado sob falha</strong>.",
              "Conexões pendentes se acumularam até <strong>esgotar o limite de capacidade</strong>.",
              "O estoque, que dependia de pedidos para confirmar reservas, <strong>também ficou lento</strong>.",
              "A equipe sabia, <em>em tese</em>, que os mecanismos existiam.",
          ]) + "\n" +
          destaque("O que faltava era a prática de <strong>validá-los deliberadamente</strong> — antes que um "
                   "evento real os testasse pela primeira vez, sob a pior condição possível: tráfego de pico."),
          visual="timeline"),
    slide(14, "Conteúdo", "A pirâmide de testes em um sistema distribuído",
          ul([
              "<strong>Unitários</strong> — verificam uma função ou classe isoladamente, executando em milissegundos. Base ampla.",
              "<strong>Integração</strong> — verificam a interação entre um componente e suas dependências diretas, como banco ou fila.",
              "<strong>Ponta a ponta</strong> — verificam um fluxo completo atravessando múltiplos serviços reais. Topo estreito.",
          ]) + "\n" +
          destaque("Em sistemas distribuídos, o <strong>topo é particularmente caro</strong>: um teste de ponta a "
                   "ponta do checkout exige pedidos, estoque, pagamento e expedição disponíveis e coerentes — "
                   "lento, frágil a mudanças não relacionadas e difícil de depurar. A recomendação: base ampla de "
                   "unitários e de contrato, com um número <strong>reduzido e bem escolhido</strong> de "
                   "integração e ponta a ponta, nos fluxos mais críticos."),
          visual="pyramid"),
    slide(14, "Conteúdo", "Testes de contrato",
          p("Um teste de contrato verifica se consumidor e provedor <strong>concordam sobre o formato e o "
            "significado</strong> das mensagens — sem exigir que ambos estejam em execução simultânea.") + "\n" +
          ul([
              "<strong>1. O consumidor declara</strong> — o estoque define expectativas explícitas sobre os campos que espera receber.",
              "<strong>2. Publicação</strong> — essas expectativas vão para um repositório compartilhado.",
              "<strong>3. Verificação no pipeline</strong> — o CI do produtor valida o contrato antes de qualquer implantação.",
              "<strong>4. Falha antecipada</strong> — se um campo esperado sumir ou mudar de nome, o pipeline falha antes da produção.",
          ]) + "\n" +
          destaque("Esse mecanismo detectaria a <strong>alteração silenciosa no nome de um campo</strong> — "
                   "problema recorrente em arquiteturas orientadas a eventos e responsável por falhas sutis que "
                   "só aparecem muito depois da implantação."),
          visual="flow"),
    slide(14, "Conteúdo", "Carga, estresse e duração",
          tabela(["Teste", "O que aplica", "A pergunta que responde"], [
              ["<strong>Carga</strong>", "O tráfego esperado: dia típico ou pico projetado", "O sistema atende ao que foi prometido, sem violar latência e erro?"],
              ["<strong>Estresse</strong>", "Carga crescente além do esperado, até falhar", "Onde ele quebra — e como se degrada ao quebrar?"],
              ["<strong>Duração</strong> (soak)", "Carga sustentada por horas ou dias", "Como ele se degrada exposto ao tempo, não ao volume instantâneo?"],
          ]) + "\n" +
          destaque("O teste de duração revela o que os outros dois escondem: <strong>vazamentos de memória, "
                   "esgotamento gradual de conexões e acúmulo de dados temporários</strong> não liberados.")),
    slide(14, "Conteúdo", "Engenharia do caos: injetar falha para aprender",
          p("Conduzir <strong>experimentos controlados</strong> que injetam falhas deliberadas — latência "
            "adicional, erros simulados, indisponibilidade de um componente — para <em>observar</em> o "
            "comportamento real, em vez de presumi-lo.") + "\n" +
          ul([
              "<strong>Por que existe</strong> — sistemas distribuídos enfrentam combinações de falha raras demais para revisão de código prever.",
              "<strong>Mas frequentes o bastante</strong> — na escala de milhares de componentes, elas acontecem de tempos em tempos.",
              "<strong>Diferente de um teste unitário</strong> — parte de uma hipótese explícita e tenta <em>refutá-la</em> sob perturbação controlada.",
              "<strong>Resultados inesperados são valiosos</strong> — mas não dispensam critérios definidos <em>antes</em> da execução.",
          ]), visual="map"),
    slide(14, "Conteúdo", "Hipótese de estado estável",
          p("Todo experimento bem projetado começa por uma expectativa <strong>mensurável e específica</strong> "
            "sobre o comportamento normal, formulada antes de qualquer falha ser injetada.") + "\n" +
          ul([
              "<strong>Vago demais</strong> — “o sistema deve continuar funcionando”. Impossível de verificar.",
              "<strong>Em condições normais</strong> — taxa de conclusão acima de <strong>98%</strong> e p95 do checkout abaixo de <strong>400 ms</strong>.",
              "<strong>Durante a indisponibilidade simulada</strong> — o circuito de proteção deve ser acionado e o sistema degradar graciosamente.",
              "<strong>Critério de sucesso</strong> — a taxa de conclusão de pedidos não deve cair abaixo de <strong>90%</strong>.",
          ]) + "\n" +
          destaque("A hipótese exige um pré-requisito: a equipe já precisa <strong>saber medir</strong> taxa de "
                   "conclusão e p95 continuamente. Sem as métricas da Aula 13, não há como confirmar nem refutar "
                   "nada durante o experimento."),
          visual="map"),
    citacao(
        "“Raio de impacto limitado e capacidade de interrupção imediata separam um experimento de caos "
        "responsável de simplesmente causar uma falha em produção e esperar o melhor.”",
        "— síntese da Aula 14"),
    slide(14, "Conteúdo", "Raio de impacto e mecanismo de interrupção",
          ul([
              "<strong>Comece pequeno</strong> — 1% do tráfego real, um ambiente controlado ou um pequeno subconjunto de instâncias.",
              "<strong>Amplie gradualmente</strong> — só à medida que a equipe ganha confiança sobre o comportamento observado.",
              "<strong>Kill switch</strong> — comando ou automação capaz de encerrar a injeção de falha instantaneamente.",
              "<strong>Gatilho declarado</strong> — os indicadores de negócio ultrapassarem um limite de degradação predefinido.",
          ]) + "\n" +
          tabela(["Elemento do cartão do experimento", "Exemplo para a NexaOrder"], [
              ["Hipótese de estado estável", "Conclusão de pedidos ≥ 90% durante a perturbação"],
              ["Perturbação", "Indisponibilidade simulada do provedor de pagamento"],
              ["Métricas de controle", "Taxa de conclusão, p95 do checkout, estado do circuito"],
              ["Raio de impacto", "1% do tráfego, em uma única região"],
              ["Critério de interrupção", "Conclusão abaixo de 85% por mais de 60 segundos"],
          ])),
    slide(14, "Exemplo numérico", "Por que a resiliência de cada serviço não basta",
          p("Quatro serviços com <strong>99,9%</strong> de disponibilidade individual, em cadeia estritamente "
            "sequencial e sem tolerância a falha parcial:") + "\n" +
          formula("A<sub>fluxo</sub> = 0,999<sup>4</sup> ≈ 0,996") + "\n" +
          numeros([
              ("99,9%", "por serviço"),
              ("4", "serviços em cadeia"),
              ("99,6%", "disponibilidade combinada"),
              ("≈ 4×", "mais indisponibilidade"),
          ]) + "\n" +
          destaque("A composição entrega <strong>pior</strong> que cada componente isolado. É por isso que "
                   "circuitos de proteção, degradação graciosa e processamento assíncrono <strong>não são "
                   "refinamentos opcionais</strong> — e apenas testes deliberados, não a leitura do código, "
                   "revelam se eles realmente atenuam esse efeito na prática.")),
    slide(14, "Conteúdo", "Postmortem sem culpabilização",
          p("Depois de um incidente real ou de um experimento que revela comportamento inesperado, a etapa "
            "final é a <strong>aprendizagem estruturada</strong>.") + "\n" +
          ul([
              "<strong>O que o relatório reconstrói</strong> — a linha do tempo do incidente, os fatores contribuintes e as ações de melhoria, com responsáveis e prazos.",
              "<strong>O princípio</strong> — incidentes em sistemas complexos raramente têm uma única causa atribuível a uma pessoa.",
              "<strong>De onde eles emergem</strong> — combinações de decisões de projeto, lacunas de teste e condições operacionais que, isoladas, pareciam razoáveis.",
              "<strong>Não pare na causa imediata</strong> — o esgotamento de conexões é o sintoma, não a explicação.",
              "<strong>Pergunte por quê</strong> — por que o circuito não impediu o esgotamento? Por que nenhum teste revelou a lacuna antes?",
              "<strong>Busque mudanças sistêmicas</strong> — e não apenas correções pontuais de código.",
          ]), visual="map"),
    slide(14, "Pausa para reflexão", "“Homologação já garante confiança suficiente”?",
          p("A equipe decide não realizar nenhum experimento de caos em produção, argumentando que os testes "
            "de integração em homologação bastam.") + "\n" +
          ul([
              "Que <strong>diferenças entre homologação e produção</strong> podem invalidar essa suposição?",
              "Por que testes de integração, mesmo bem escritos, podem não revelar o comportamento sob <strong>falhas parciais e concorrência real</strong>?",
              "Que argumento convenceria a liderança de que um experimento com raio limitado é <strong>mais seguro</strong> que esperar um incidente real?",
              "Que <strong>evidências de observabilidade</strong> da Aula 13 seriam necessárias antes de autorizar o primeiro experimento em produção?",
          ]) + "\n" +
          destaque("Ambientes de homologação raramente reproduzem volume de tráfego, diversidade de dados e "
                   "condições de rede reais. O caos controlado <strong>reduz</strong> o risco de descobrir essas "
                   "lacunas pela primeira vez durante um incidente sem controle.")),
    pontos_chave(14, [
        ("Base ampla, topo estreito", "Unitários e contratos sustentam a cobertura; ponta a ponta fica reservado aos fluxos mais críticos."),
        ("Contrato detecta antes", "A incompatibilidade entre consumidor e provedor aparece no pipeline, não em produção."),
        ("Três testes, três perguntas", "Carga confirma o prometido, estresse revela o limite, duração revela a degradação no tempo."),
        ("Hipótese antes da falha", "Sem uma expectativa mensurável definida previamente, o experimento não confirma nem refuta nada."),
        ("Pequeno e interrompível", "Raio de impacto limitado e kill switch são o que tornam o experimento aceitável em produção."),
        ("A cadeia degrada", "Compor serviços reduz a disponibilidade agregada; só mecanismos testados revertem esse efeito."),
    ]),
    slide(14, "Atividade prática", "Mãos à obra: planejar um experimento de caos",
          p("Planeje um experimento controlado de indisponibilidade do serviço de pagamento.") + "\n" +
          ul([
              "<strong>1.</strong> Formule a hipótese de estado estável, incluindo os indicadores observados.",
              "<strong>2.</strong> Defina o raio de impacto inicial e justifique a escolha.",
              "<strong>3.</strong> Descreva o mecanismo de interrupção imediata e o critério que o aciona.",
              "<strong>4.</strong> Liste as métricas, logs e traces necessários para avaliar o resultado.",
              "<strong>5.</strong> Descreva, em três frases, a estrutura do postmortem caso surja uma falha inesperada.",
              "<strong>6.</strong> Indique qual mudança sistêmica você proporia se a hipótese for refutada.",
          ]), visual="map"),
    encerramento(
        "Você já sabe transformar suposições sobre resiliência em evidências obtidas por testes estruturados "
        "e experimentos controlados. Na próxima aula, mudamos de assunto: como processar grandes volumes de "
        "dados quando a decisão precisa sair em segundos, não em horas.",
        "Próxima aula: Aula 15 — Processamento distribuído, edge e serverless."),
])

# ---------------------------------------------------------------- Aula 15

A15 = montar([
    capa(15, "Processamento distribuído, edge e serverless", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um fluxo com as fases "
        "de mapeamento, embaralhamento e redução aplicadas ao histórico de pedidos; um painel numérico "
        "com o dimensionamento de sete partições para cinco mil eventos por segundo; uma linha do tempo "
        "distinguindo tempo de evento de tempo de processamento, com a marca d’água admitindo eventos "
        "atrasados; um quadro sobre inicialização a frio em funções como serviço; e um gráfico comparando "
        "processamento centralizado, regional e de borda por latência e custo."
    ),
    sumario("Processamento distribuído, edge e serverless", [
        "Processamento em lote e em fluxo",
        "MapReduce e a generalização em DAGs",
        "Particionamento e tolerância a falhas em fluxo",
        "Tempo de evento e tempo de processamento",
        "Janelas e marcas d’água",
        "Funções como serviço e inicialização a frio",
        "Computação de borda: latência contra complexidade",
        "Escolher a partir do requisito de negócio",
    ]),
    slide(15, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Decidir</strong> entre lote e fluxo a partir de até quando a informação pode esperar.",
              "<strong>Descrever</strong> as fases de map, shuffle e reduce e sua generalização em DAGs.",
              "<strong>Dimensionar</strong> partições de um pipeline de fluxo a partir da taxa de eventos.",
              "<strong>Distinguir</strong> tempo de evento de tempo de processamento e escolher a base da janela.",
              "<strong>Avaliar</strong> o custo de inicialização a frio em caminhos sensíveis à latência.",
              "<strong>Ponderar</strong> ganho de latência contra complexidade operacional na computação de borda.",
          ]), visual="map"),
    slide(15, "Situação-problema", "Detectar fraude antes que o pagamento seja aprovado",
          p("A NexaOrder passou a registrar tentativas de fraude: <strong>múltiplos cartões em sequência "
            "rápida</strong>, a partir do mesmo dispositivo, testando quais dados seriam aceitos.") + "\n" +
          ul([
              "A primeira proposta técnica: um <em>job</em> a cada hora, lendo o histórico e sinalizando padrões para revisão no dia seguinte.",
              "O time de risco <strong>rejeita</strong>: uma hora basta para dezenas de tentativas fraudulentas serem aprovadas.",
              "A decisão precisa ocorrer <strong>em segundos</strong>, no momento da tentativa.",
              "Essa exigência muda completamente <strong>o tipo de arquitetura de processamento</strong> necessária.",
          ]), visual="timeline"),
    slide(15, "Conteúdo", "Lote e fluxo",
          tabela(["", "Processamento em lote", "Processamento em fluxo"], [
              ["Sobre o que opera", "Conjunto finito e delimitado, coletado ao longo de um período", "Sequência potencialmente ilimitada de eventos"],
              ["Quando processa", "De uma só vez, depois de formado o lote", "Cada evento, ou pequenos grupos, assim que disponível"],
              ["Vantagem", "Simplicidade: o conjunto é conhecido e finito", "Decisão no instante em que o fato ocorre"],
              ["Casos típicos", "Relatórios diários, comissões mensais, reprocessamento histórico", "Detecção de fraude, alertas operacionais, contadores ao vivo"],
          ]) + "\n" +
          destaque("A escolha <strong>não é apenas técnica</strong>: é uma decisão de negócio sobre até quando "
                   "uma informação pode esperar antes de <strong>perder valor</strong>.")),
    slide(15, "Conteúdo", "MapReduce e a generalização em DAGs",
          ul([
              "<strong>Map</strong> — transforma cada registro de entrada independentemente, produzindo pares de chave e valor intermediários.",
              "<strong>Shuffle</strong> — redistribui os pares intermediários entre os nós, agrupando-os pela chave correspondente.",
              "<strong>Reduce</strong> — agrupa e combina os pares por chave, produzindo o resultado final.",
              "<strong>DAGs</strong> — frameworks modernos generalizam a ideia em grafos acíclicos dirigidos, encadeando várias etapas além do par map-reduce.",
          ]) + "\n" +
          destaque("A tolerância a falhas segue um princípio comum: se um nó falha durante uma tarefa, o "
                   "framework <strong>reatribui essa tarefa</strong> a outro nó, reexecutando-a a partir dos "
                   "dados intermediários já persistidos — sem reiniciar o job inteiro nem exigir intervenção "
                   "manual para a falha isolada de um único nó."),
          visual="flow"),
    slide(15, "Exemplo numérico", "Dimensionando as partições do pipeline",
          p("Pipelines de fluxo também particionam o trabalho, distribuindo eventos por uma chave — aqui, o "
            "<strong>identificador do dispositivo</strong>, garantindo que todos os eventos de um mesmo "
            "dispositivo sejam processados em ordem, pela mesma partição.") + "\n" +
          formula("P = ⌈ λ<sub>eventos</sub> ÷ C<sub>partição</sub> ⌉") + "\n" +
          numeros([
              ("5.000/s", "pico de tentativas (λ)"),
              ("750/s", "capacidade por partição (C)"),
              ("6,67", "resultado da divisão"),
              ("7", "partições mínimas"),
          ]) + "\n" +
          destaque("Sete partições atendem ao pico com margem — mas a conta <strong>não substitui um teste de "
                   "carga real</strong> do pipeline completo, incluindo o custo de embaralhamento e o acesso ao "
                   "contexto necessário à avaliação, como o histórico recente do dispositivo.")),
    slide(15, "Conteúdo", "Mais partições, mais coordenação",
          ul([
              "<strong>Mais partições</strong> — mais paralelismo disponível para o pipeline.",
              "<strong>Também mais complexidade</strong> — de coordenação e de tolerância a falhas.",
              "<strong>Progresso duradouro</strong> — cada partição precisa registrar seu avanço de forma persistente.",
              "<strong>Retomada correta</strong> — em caso de falha do consumidor, o processamento recomeça do ponto certo.",
              "<strong>Sem perder nem duplicar</strong> — além do que a semântica de entrega escolhida permitir.",
              "<strong>Tema já visto</strong> — é a mesma discussão de at-least-once e efeito único da Unidade 3.",
          ]), visual="map"),
    citacao(
        "“A escolha entre lote e fluxo é uma decisão de negócio sobre até quando uma informação pode "
        "esperar antes de perder valor.”",
        "— síntese da Aula 15"),
    slide(15, "Conteúdo", "Tempo de evento e tempo de processamento",
          p("Distinção essencial em processamento de fluxo:") + "\n" +
          ul([
              "<strong>Tempo de evento</strong> — o instante em que o fato ocorreu no domínio de negócio: o momento exato da tentativa de pagamento.",
              "<strong>Tempo de processamento</strong> — o instante em que o pipeline efetivamente processa o evento, segundos ou minutos depois.",
              "<strong>Janela por tempo de evento</strong> — resultados mais fiéis à realidade do negócio, mas exige lidar com atraso e desordem.",
              "<strong>Janela por tempo de processamento</strong> — simples de implementar, porém pode distorcer a análise.",
          ]) + "\n" +
          destaque("“Quantas tentativas com o mesmo dispositivo ocorreram no último minuto?” — a resposta "
                   "<strong>muda</strong> conforme a base de tempo escolhida para a janela."),
          visual="compare"),
    slide(15, "Conteúdo", "Marcas d’água e tolerância a atraso",
          ul([
              "<strong>Marca d’água</strong> — estimativa de até que ponto, no tempo de evento, o pipeline já recebeu a maior parte dos dados.",
              "<strong>Tolerância a atraso</strong> — período adicional configurável que mantém a janela aberta antes de fechá-la em definitivo.",
              "<strong>O que resolvem juntas</strong> — admitir eventos que chegaram atrasados sem descartar o conceito de janela.",
              "<strong>O compromisso</strong> — janelas que fecham cedo perdem eventos tardios; janelas que demoram atrasam a decisão.",
          ]), visual="timeline"),
    slide(15, "Conteúdo", "Funções como serviço e inicialização a frio",
          p("<strong>FaaS</strong> executa um trecho de código em resposta a um evento — requisição HTTP, "
            "mensagem em fila, arquivo criado — sem provisionar servidor continuamente. A cobrança é, "
            "tipicamente, pelo tempo de execução efetivo.") + "\n" +
          ul([
              "<strong>Onde brilha</strong> — cargas esporádicas e de volume variável, como enviar e-mail de confirmação de pedido.",
              "<strong>Inicialização a frio</strong> — sem instância “aquecida”, a plataforma precisa inicializar um novo ambiente antes de processar.",
              "<strong>Quando é irrelevante</strong> — em uma notificação assíncrona, a latência extra não é percebida.",
              "<strong>Quando é problemática</strong> — em um caminho síncrono sensível à latência, como parte do fluxo de checkout.",
          ]), visual="map"),
    slide(15, "Conteúdo", "Computação de borda: latência contra complexidade",
          p("A borda aproxima o processamento dos dispositivos, executando lógica em pontos geograficamente "
            "distribuídos em vez de centralizá-la em uma região de nuvem.") + "\n" +
          tabela(["Localização", "Latência típica", "Contexto disponível", "Complexidade operacional"], [
              ["<strong>Borda</strong>", "Mais baixa", "Sinais simples e locais do dispositivo", "Alta: versões de regras sincronizadas em muitos locais"],
              ["<strong>Regional</strong>", "Intermediária", "Contexto parcial agregado", "Média"],
              ["<strong>Centralizada</strong>", "Mais alta", "Histórico amplo e completo", "Baixa: um único lugar para atualizar"],
          ]) + "\n" +
          destaque("O ganho de latência <strong>não vem de graça</strong>: manter lógica em múltiplos pontos "
                   "aumenta a complexidade e <strong>nem sempre reduz custo</strong>. Reserve modelos que "
                   "dependem de histórico amplo para o centro, e sinais simples e locais para a borda."),
          visual="compare"),
    slide(15, "Pausa para reflexão", "“Vamos processar tudo na borda”",
          p("O time de risco propõe processar toda a análise de fraude <em>exclusivamente</em> na borda, "
            "eliminando dependência de uma região central e argumentando que isso reduzirá a latência a zero "
            "e eliminará custos de rede.") + "\n" +
          ul([
              "Que <strong>sinais de fraude dependem de contexto histórico</strong> que dificilmente estaria disponível só na borda?",
              "Que <strong>riscos operacionais</strong> surgem de manter lógica duplicada em muitos pontos, sobretudo ao atualizar um modelo?",
              "Em que medida a afirmação de latência <strong>“reduzida a zero”</strong> é tecnicamente imprecisa?",
              "Que <strong>combinação</strong> de borda e centro atenderia à decisão em segundos sem abrir mão do histórico?",
          ]) + "\n" +
          destaque("A resposta madura raramente é “tudo em um lugar só”. É uma <strong>triagem local</strong> "
                   "para sinais simples, com avaliação profunda centralizada para o que exige contexto.")),
    pontos_chave(15, [
        ("Lote espera, fluxo não", "Lote atende análises que toleram espera; fluxo atende decisões que precisam sair em segundos."),
        ("Map, shuffle, reduce", "O modelo se generalizou em DAGs; a tolerância a falhas vem da reexecução de tarefas isoladas."),
        ("Partição dimensiona", "O número mínimo relaciona a taxa de eventos à capacidade comprovada por consumidor."),
        ("Dois tempos diferentes", "Tempo de evento e de processamento divergem; marcas d’água admitem atraso sem descartar a janela."),
        ("FaaS troca ocioso por frio", "Reduz custo em carga esporádica ao preço de latência adicional na inicialização."),
        ("Borda não é grátis", "Reduz latência de sinais simples, mas aumenta complexidade e nem sempre reduz custo."),
    ]),
    slide(15, "Atividade prática", "Mãos à obra: comparar três arquiteturas",
          p("Compare, para a detecção de fraude quase em tempo real, três alternativas: <strong>(a)</strong> "
            "lote horário; <strong>(b)</strong> fluxo centralizado particionado por dispositivo; "
            "<strong>(c)</strong> triagem na borda combinada com fluxo centralizado.") + "\n" +
          ul([
              "<strong>1.</strong> Estime a latência típica entre a tentativa e a decisão em cada alternativa.",
              "<strong>2.</strong> Para a alternativa (b), calcule as partições necessárias para 8.000 eventos/s com consumidor de 1.000/s.",
              "<strong>3.</strong> Avalie cada alternativa quanto à capacidade de considerar o <em>histórico</em> do dispositivo.",
              "<strong>4.</strong> Aponte o principal risco operacional de cada uma.",
              "<strong>5.</strong> Recomende uma alternativa, justificando por latência, custo e complexidade.",
              "<strong>6.</strong> Indique qual evidência você coletaria para validar a recomendação em produção.",
          ]), visual="map"),
    encerramento(
        "Você já sabe escolher entre lote, fluxo, funções e borda a partir do requisito de negócio — e "
        "dimensionar o pipeline resultante. Na última aula da disciplina, integramos tudo: como defender "
        "uma arquitetura inteira diante de requisitos, riscos e custo.",
        "Próxima aula: Aula 16 — Projeto integrado e avaliação arquitetural."),
])

# ---------------------------------------------------------------- Aula 16

A16 = montar([
    capa(16, "Projeto integrado e avaliação arquitetural", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: uma linha do tempo das "
        "decisões arquiteturais da NexaOrder ao longo das quatro unidades; um mapa de análise de pontos "
        "únicos de falha percorrendo gateway, banco, mensageria e coletor; uma árvore de atributos de "
        "qualidade ligando objetivos de negócio a cenários mensuráveis; um painel numérico comparando "
        "cadeia sequencial e redundância paralela; e um quadro-resumo da trajetória completa da disciplina."
    ),
    sumario("Projeto integrado e avaliação arquitetural", [
        "Requisitos funcionais e atributos de qualidade",
        "Estimativa de carga e capacidade, revisitada",
        "Registros de decisão arquitetural (ADR)",
        "Análise de pontos únicos de falha",
        "Plano de recuperação: RPO e RTO",
        "Segurança e observabilidade desde o projeto",
        "Custo, sustentabilidade e evolução",
        "A trajetória completa da NexaOrder",
    ]),
    slide(16, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Explicitar</strong> tensões entre requisitos funcionais e atributos de qualidade, e resolvê-las por dado.",
              "<strong>Estimar</strong> capacidade a partir de evidências operacionais, não de suposições.",
              "<strong>Escrever</strong> um ADR completo: contexto, alternativas, decisão e consequências aceitas.",
              "<strong>Conduzir</strong> uma análise de pontos únicos de falha atenta a dependências ocultas.",
              "<strong>Definir</strong> RPO e RTO a partir de requisitos de negócio, não de conveniência técnica.",
              "<strong>Defender</strong> uma arquitetura completa com requisitos, riscos, custo e evidências.",
          ]), visual="map"),
    slide(16, "Situação-problema", "Defender a arquitetura diante do conselho",
          p("A diretoria convoca a engenharia para uma revisão formal antes de aprovar o orçamento do "
            "próximo ciclo. A pergunta <strong>não</strong> é “o sistema funciona?” — isso já foi "
            "demonstrado. A pergunta é:") + "\n" +
          ul([
              "Por que confiamos que esta arquitetura <strong>sustenta o crescimento previsto</strong>?",
              "Por que acreditamos que ela <strong>resiste às falhas mais prováveis</strong>?",
              "Por que ela <strong>vale o investimento contínuo</strong> que exige?",
              "A resposta precisa vir com <strong>requisitos, estimativas, decisões documentadas e evidências</strong> — não com afirmações genéricas.",
          ]), visual="compare"),
    slide(16, "Conteúdo", "Requisitos funcionais e atributos de qualidade",
          ul([
              "<strong>Requisitos funcionais</strong> — o que o sistema deve fazer: “o cliente deve conseguir finalizar uma compra”.",
              "<strong>Atributos de qualidade</strong> — como ele deve se comportar: desempenho, disponibilidade, segurança, manutenibilidade, escalabilidade, custo.",
              "<strong>Não há hierarquia</strong> entre os dois na avaliação arquitetural.",
              "<strong>Eles entram em tensão</strong> — e resolver essa tensão explicitamente é parte central do trabalho de projeto.",
          ]) + "\n" +
          destaque("Produto quer <strong>latência mínima no catálogo</strong>; confiabilidade quer "
                   "<strong>garantias mais fortes no saldo de estoque</strong>. Uma avaliação madura não escolhe "
                   "um lado de forma absoluta: aceita leitura eventualmente consistente no catálogo e exige "
                   "consistência mais forte <strong>no instante da reserva</strong>."),
          visual="compare"),
    slide(16, "Exemplo numérico", "A mesma fórmula, insumos diferentes",
          p("A Aula 1 apresentou esta fórmula com números estimados. Três unidades depois, ela continua "
            "válida — mas os insumos <strong>deixaram de ser suposições</strong>:") + "\n" +
          formula("N = ⌈ λ<sub>pico</sub> ÷ ( C<sub>instância</sub> × U<sub>alvo</sub> ) ⌉") + "\n" +
          tabela(["Insumo", "Na Aula 1", "Na Aula 16"], [
              ["C<sub>instância</sub>", "Estimativa isolada", "Obtido de testes de carga reais, com o rigor da Aula 14"],
              ["λ<sub>pico</sub>", "Projeção de negócio", "Refinado por métricas históricas da instrumentação da Aula 13"],
              ["U<sub>alvo</sub>", "Convenção", "Calibrado pelo orçamento de erro e pelo SLO acordado"],
          ]) + "\n" +
          destaque("A avaliação arquitetural madura <strong>não estima capacidade a partir de suposições</strong> — "
                   "ela estima a partir de evidências operacionais acumuladas ao longo do ciclo de vida.")),
    slide(16, "Conteúdo", "Registros de decisão arquitetural",
          p("Um <strong>ADR</strong> documenta uma escolha significativa: o contexto que a motivou, as "
            "alternativas consideradas, a decisão tomada e as consequências esperadas.") + "\n" +
          ul([
              "<strong>Não é um ADR</strong> — “decidimos usar Kubernetes”. Um nome de tecnologia não é um registro útil.",
              "<strong>É um ADR</strong> — por que a orquestração automatizada era necessária.",
              "<strong>Alternativas avaliadas</strong> — implantação manual, um serviço gerenciado mais simples.",
              "<strong>Consequências aceitas</strong> — curva de aprendizado da equipe, custo de operação do cluster.",
          ]) + "\n" +
          destaque("Reunir esses registros permite que <strong>qualquer pessoa nova na equipe</strong> compreenda "
                   "não apenas o estado atual do sistema, mas o raciocínio que levou até ele."),
          visual="map"),
    slide(16, "Retrospectiva", "As decisões que a NexaOrder acumulou",
          tabela(["Unidade", "Decisão central registrada", "Compromisso aceito"], [
              ["<strong>1</strong>", "Múltiplas instâncias sem estado atrás de um balanceador", "Sessões locais deixam de ser confiáveis; o banco pode virar gargalo"],
              ["<strong>2</strong>", "Consistência eventual no catálogo, forte na reserva de estoque", "Duas políticas convivendo no mesmo sistema, com regras distintas"],
              ["<strong>3</strong>", "Decomposição por contexto delimitado e arquitetura orientada a eventos", "Composição explícita no lugar de <code>JOIN</code>; rastreio de progressão"],
              ["<strong>4</strong>", "Observabilidade instrumentada e política de testes de resiliência", "Custo contínuo de telemetria e de experimentos controlados"],
          ]), visual="timeline"),
    citacao(
        "“Continue tratando cada decisão arquitetural como uma hipótese verificável, não como um dogma.”",
        "— encerramento da disciplina"),
    slide(16, "Conteúdo", "Análise de pontos únicos de falha",
          p("A análise de <strong>SPOF</strong> identifica componentes cuja indisponibilidade isolada "
            "comprometeria todo o fluxo, mesmo com o restante do sistema saudável. Ela exige atenção a "
            "<strong>dependências ocultas</strong>:") + "\n" +
          ul([
              "<strong>Gateway</strong> — sua queda derruba a entrada de todos os fluxos externos?",
              "<strong>Banco de dados de pedidos</strong> — há réplica promovível e failover ensaiado?",
              "<strong>Sistema de mensageria</strong> — uma instância isolada usada por <em>todas</em> as réplicas de pagamento é um SPOF disfarçado.",
              "<strong>Provedor de identidade</strong> — sem ele, o mTLS e a autorização param de funcionar.",
              "<strong>Coletor de observabilidade</strong> — sua queda cega a equipe justamente durante o incidente.",
              "<strong>A armadilha</strong> — réplicas em várias zonas não eliminam o SPOF se todas dependerem de um único componente não replicado.",
          ]), visual="map"),
    slide(16, "Conteúdo", "Plano de recuperação: RPO e RTO",
          tabela(["Indicador", "O que mede", "Exemplo da NexaOrder"], [
              ["<strong>RPO</strong> (recovery point objective)", "Quanto de dado o negócio aceita perder", "≈ 5 min — o intervalo da replicação assíncrona para a região secundária"],
              ["<strong>RTO</strong> (recovery time objective)", "Em quanto tempo o serviço precisa voltar", "≈ 15 min — promover a região secundária e restabelecer o serviço"],
          ]) + "\n" +
          destaque("Definidos a partir de <strong>requisitos de negócio, não de conveniência técnica</strong>, "
                   "esses dois números orientam diretamente decisões de replicação, frequência de backup e "
                   "automação de failover — e não o contrário.")),
    slide(16, "Conteúdo", "Seguro e observável por padrão",
          p("Segurança e observabilidade tratadas como camadas adicionadas ao final tendem a ficar "
            "<strong>incompletas e caras de corrigir</strong>. A prática recomendada as incorpora ao desenho "
            "inicial de cada componente.") + "\n" +
          ul([
              "Todo novo serviço nasce com <strong>identidade própria</strong> e comunicação autenticada?",
              "Todo novo fluxo crítico nasce <strong>instrumentado</strong> com métricas, logs e traces correlacionáveis?",
              "Ou a instrumentação é acrescentada <strong>apenas depois do primeiro incidente</strong> que a exigiu?",
              "Essas perguntas viram <strong>critérios de aceite</strong> de um novo serviço, não sugestões.",
          ]), visual="map"),
    slide(16, "Exemplo numérico", "Cadeia sequencial e redundância paralela",
          p("Uma instância com <strong>99,5%</strong> de disponibilidade; três réplicas independentes — sem "
            "dependência compartilhada — atrás de um balanceador que desvia para qualquer réplica saudável:") + "\n" +
          formula("A<sub>réplicas</sub> = 1 − ( 1 − A )<sup>n</sup> = 1 − 0,005<sup>3</sup> ≈ 0,999999875") + "\n" +
          numeros([
              ("99,5%", "uma instância"),
              ("3", "réplicas independentes"),
              ("≈ 7 noves", "disponibilidade combinada"),
              ("≈ 3×", "o custo de manter"),
          ]) + "\n" +
          destaque("Compare com a <strong>cadeia sequencial</strong> da Aula 14, que degradava 99,9% para 99,6%. "
                   "O que sustenta disponibilidade alta é <strong>redundância paralela com independência de "
                   "falha</strong> — não a simples multiplicação de instâncias. E o ganho depende do valor de "
                   "negócio que a disponibilidade adicional realmente entrega.")),
    slide(16, "Conteúdo", "Custo, sustentabilidade e evolução",
          ul([
              "<strong>Nenhuma arquitetura permanece ótima</strong> — padrões de tráfego mudam, requisitos surgem, decisões envelhecem.",
              "<strong>O desperdício típico</strong> — capacidade provisionada para o pico e mantida constante em horários de baixíssima demanda.",
              "<strong>A resposta errada</strong> — eliminar a redundância necessária para os picos.",
              "<strong>A resposta madura</strong> — escalonamento automático que ajusta a capacidade à demanda observada.",
              "<strong>A restrição</strong> — preservando as metas de disponibilidade definidas, sem recursos ociosos pagos por padrão.",
              "<strong>O princípio</strong> — evolução contínua é parte do projeto, não sinal de que ele foi mal feito.",
          ]), visual="map"),
    slide(16, "Retrospectiva", "A trajetória completa da NexaOrder",
          tabela(["Unidade", "O que estabeleceu"], [
              ["<strong>1 — Fundamentos</strong>", "O que caracteriza um sistema distribuído, como processos se comunicam, por que tempo e ordenação deixam de ser triviais e como falhas parciais exigem desenho explícito"],
              ["<strong>2 — Dados</strong>", "Replicação, particionamento, CAP e PACELC, consenso via Raft, transações distribuídas com sagas e idempotência"],
              ["<strong>3 — Serviços</strong>", "Limites de domínio explícitos, arquitetura orientada a eventos, orquestração em contêineres e comunicação segura"],
              ["<strong>4 — Operação</strong>", "Observabilidade para diagnosticar, testes e caos para validar, processamento em escala e avaliação arquitetural integrada"],
          ]) + "\n" +
          destaque("Nenhuma unidade entrega, isoladamente, uma arquitetura completa. É a <strong>combinação</strong> — "
                   "fundamentos sólidos, dados bem distribuídos, serviços bem delimitados e operação validada — "
                   "que sustenta um sistema em produção, sob carga real, por anos.")),
    pontos_chave(16, [
        ("Tensão é normal", "Requisitos funcionais e atributos de qualidade colidem; a avaliação resolve isso por dado, não em bloco."),
        ("Estimar com evidência", "Depois de quatro unidades, capacidade se calcula com testes de carga e métricas históricas reais."),
        ("ADR guarda o porquê", "Um registro útil traz contexto, alternativas e consequências aceitas — não um nome de tecnologia."),
        ("SPOF se esconde", "Réplicas em várias zonas não bastam se todas dependerem de um mesmo componente não replicado."),
        ("RPO e RTO vêm do negócio", "Os dois números orientam replicação, backup e failover — e não o contrário."),
        ("Paralelo, não sequencial", "Redundância independente eleva a disponibilidade; encadear serviços a reduz."),
    ]),
    slide(16, "Atividade prática", "Mãos à obra: a defesa arquitetural completa",
          p("Prepare a defesa arquitetural da NexaOrder para uma banca de revisão.") + "\n" +
          ul([
              "<strong>1.</strong> Liste três requisitos funcionais e três atributos de qualidade, com uma tensão explícita entre eles e como foi resolvida.",
              "<strong>2.</strong> Escreva um ADR completo para uma decisão de qualquer unidade da disciplina.",
              "<strong>3.</strong> Realize uma análise de pontos únicos de falha com ao menos dois riscos não triviais.",
              "<strong>4.</strong> Defina RPO e RTO para o fluxo de pedidos, com justificativa de negócio.",
              "<strong>5.</strong> Descreva como segurança e observabilidade entram no desenho de um novo serviço.",
              "<strong>6.</strong> Apresente um cenário de pico e um de falha, explicando a resposta da arquitetura com evidências das aulas anteriores.",
          ]), visual="map"),
    encerramento(
        "A NexaOrder começou como uma aplicação em um único servidor, onde duas pessoas compravam o mesmo "
        "último item sem que ninguém soubesse explicar por quê. Dezesseis aulas depois, é uma plataforma "
        "distribuída, observável, testada e defensável — com cada decisão registrada e cada garantia "
        "sustentada por evidência, não por esperança. Continue perguntando “o que acontece se isso falhar?”, "
        "meça a resposta e ajuste o projeto com base nela.",
        "Fim da disciplina. Boa jornada — e bons sistemas, especialmente quando algo neles falhar."),
])
