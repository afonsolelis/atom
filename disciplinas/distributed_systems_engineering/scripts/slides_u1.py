"""Conteúdo dos decks da Unidade 1 — Fundamentos, comunicação, tempo e falhas."""

from slides_kit import (
    audiodescricao, capa, citacao, destaque, encerramento, formula, montar,
    numeros, p, pontos_chave, slide, sumario, tabela, ul,
)

SUB = "Unidade 1 — Fundamentos, comunicação, tempo e falhas"

# ---------------------------------------------------------------- Aula 1

A1 = montar([
    capa(1, "Pensar distribuído: conceitos, propriedades e compromissos", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, "
        "verde e ciano. O conteúdo aparece em cartões claros. Há cinco recursos visuais: um mapa "
        "conceitual dos quatro elementos que definem um sistema distribuído; um fluxo da compra "
        "na NexaOrder passando por pedidos, estoque, pagamento e expedição; um quadro comparativo "
        "entre escala vertical e horizontal; um painel numérico com o dimensionamento de "
        "instâncias e o custo de cada nove de disponibilidade; e uma linha do tempo de uma "
        "cobrança cuja resposta se perde na rede."
    ),
    sumario("Pensar distribuído: conceitos, propriedades e compromissos", [
        "O que caracteriza um sistema distribuído",
        "Por que distribuir: escalabilidade, disponibilidade e geografia",
        "Dimensionamento: da intuição à hipótese verificável",
        "Propriedades que mudam o raciocínio de projeto",
        "Transparência e o risco de esconder a rede",
        "Métricas que não devem ser confundidas",
        "Estilos arquiteturais iniciais",
        "Decisão arquitetural: requisito, mecanismo, compromisso e evidência",
    ]),
    slide(1, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Caracterizar</strong> um sistema distribuído a partir de pluralidade, autonomia, comunicação e coordenação.",
              "<strong>Justificar</strong> uma decisão de distribuição a partir de um requisito concreto, e não de tendência tecnológica.",
              "<strong>Estimar</strong> capacidade e disponibilidade com fórmulas simples, transformando intuição em hipótese verificável.",
              "<strong>Distinguir</strong> latência, throughput, disponibilidade e confiabilidade como dimensões diferentes.",
              "<strong>Reconhecer</strong> concorrência, ausência de estado global e falhas parciais como propriedades inerentes, não defeitos.",
              "<strong>Registrar</strong> decisões arquiteturais explicitando benefício, custo e evidência.",
          ]), visual="map"),
    slide(1, "Situação-problema", "Quando crescer deixa de ser apenas adicionar servidores",
          p("A NexaOrder nasceu em um único servidor: interface, regras de negócio e banco compartilhavam "
            "o mesmo ambiente. Com o crescimento das vendas, a equipe criou novas instâncias e separou "
            "catálogo, estoque, pagamento e expedição. A capacidade subiu — e apareceram comportamentos "
            "que ninguém programou:") + "\n" +
          ul([
              "Dois clientes compraram <strong>o último item</strong> do estoque.",
              "Uma cobrança foi processada <strong>mesmo após a interface informar erro</strong>.",
              "O painel de operações exibiu <strong>estados diferentes</strong> para o mesmo pedido.",
              "Nenhum desses incidentes veio de programação descuidada: são <strong>propriedades da distribuição</strong>.",
          ]), visual="compare"),
    slide(1, "Conteúdo", "O que é um sistema distribuído?",
          p("Componentes computacionais <strong>autônomos</strong> que se comunicam por rede e coordenam "
            "ações para um objetivo comum. Por definição, não há memória global instantânea nem relógio "
            "perfeito acessível a todos.") + "\n" +
          ul([
              "<strong>Pluralidade</strong> — há mais de um processo, contêiner, máquina ou nó participante.",
              "<strong>Autonomia</strong> — cada participante executa e pode falhar de forma independente.",
              "<strong>Comunicação</strong> — a cooperação acontece por mensagens transmitidas pela rede.",
              "<strong>Coordenação</strong> — o resultado depende da combinação das ações dos participantes.",
          ]) + "\n" +
          destaque("O determinante não é a distância física, e sim a <strong>separação entre participantes</strong> "
                   "com comunicação não instantânea. Um sistema é distribuído mesmo dentro de um único datacenter — "
                   "e várias funções no mesmo processo não formam, por si só, um sistema distribuído."),
          visual="map"),
    slide(1, "Conteúdo", "Uma operação para o cliente, quatro serviços para a arquitetura",
          p("Para quem compra, existe um único botão: <strong>comprar</strong>. Para a arquitetura, existe "
            "uma sequência de mensagens, estados intermediários e pontos de falha independentes.") + "\n" +
          ul([
              "<strong>Pedidos</strong> registra a intenção do cliente e coordena o restante do fluxo.",
              "<strong>Estoque</strong> reserva a unidade e responde se a reserva foi possível.",
              "<strong>Pagamento</strong> solicita autorização a um provedor externo à NexaOrder.",
              "<strong>Expedição</strong> prepara o envio depois que os passos anteriores convergem.",
          ]), visual="flow"),
    slide(1, "Conteúdo", "Por que distribuir?",
          p("Distribuir não é um objetivo isolado — é resposta a requisitos que uma arquitetura "
            "centralizada não atende de forma satisfatória.") + "\n" +
          ul([
              "<strong>Escalabilidade</strong> — sustentar crescimento de carga sem degradação incompatível com os objetivos do serviço.",
              "<strong>Disponibilidade</strong> — manter o serviço acessível quando um componente falha.",
              "<strong>Proximidade geográfica</strong> — reduzir latência e atender exigências de residência de dados.",
              "<strong>Autonomia organizacional</strong> — permitir que equipes evoluam partes do produto em ritmos diferentes.",
              "<strong>Integração entre organizações</strong> — cooperar com sistemas que não estão sob seu controle.",
              "<strong>Uso eficiente de recursos</strong> — dimensionar cada capacidade conforme a demanda que ela realmente recebe.",
          ]), visual="map"),
    slide(1, "Conteúdo", "Escala vertical e escala horizontal",
          ul([
              "<strong>Vertical</strong>: aumentar CPU, memória ou armazenamento de <em>uma</em> máquina. Operacionalmente simples.",
              "<strong>Horizontal</strong>: aumentar o número de instâncias que dividem o trabalho. Amplia capacidade por paralelismo.",
              "Limite da vertical: barreiras <strong>físicas e econômicas</strong> — sempre existe uma máquina maior, até não existir mais.",
              "Preço da horizontal: distribuição de requisições, <strong>concorrência, replicação e coordenação</strong>.",
              "A relação <strong>raramente é linear</strong>: o banco pode virar gargalo e o balanceamento tem custo próprio.",
              "Parte da carga <strong>não paraleliza</strong> — trechos que exigem coordenação limitam o ganho total.",
          ]), visual="compare"),
    slide(1, "Exemplo numérico", "Quantas instâncias sustentam o pico?",
          p("Estimar antes de escalar transforma uma decisão intuitiva em <strong>hipótese verificável</strong>. "
            "O número mínimo de instâncias parte da taxa de chegada no pico, da capacidade medida de uma "
            "instância e da utilização-alvo:") + "\n" +
          formula("N = ⌈ λ<sub>pico</sub> ÷ ( C<sub>instância</sub> × U<sub>alvo</sub> ) ⌉") + "\n" +
          numeros([
              ("800", "requisições/s no pico (λ)"),
              ("200", "req/s por instância (C)"),
              ("70%", "utilização-alvo (U)"),
              ("6", "instâncias (⌈5,71⌉)"),
          ]) + "\n" +
          p("A ingenuidade seria dividir 800 por 200 e provisionar 4 instâncias. A utilização-alvo de 70% "
            "existe justamente para <strong>não operar continuamente no limite</strong>. E a conta não "
            "substitui teste de carga: ela indica onde começar a medir.")),
    slide(1, "Conteúdo", "Disponibilidade: o preço de cada nove",
          p("Disponibilidade é a proporção de tempo em que o serviço cumpre sua função: "
            "<strong>A = tempo operacional ÷ tempo total observado</strong>. Cada nove adicional "
            "custa redundância, automação, observabilidade e recuperação.") + "\n" +
          tabela(["Disponibilidade", "Indisponibilidade em 30 dias", "O que ela exige na prática"], [
              ["99%", "≈ 7 h 12 min", "Redundância básica e recuperação manual"],
              ["99,9%", "≈ 43 min", "Múltiplas instâncias e desvio automático de tráfego"],
              ["99,99%", "≈ 4 min 19 s", "Zonas independentes, automação e ensaio de falhas"],
              ["99,999%", "≈ 26 s", "Investimento raramente justificável fora de domínios críticos"],
          ]) + "\n" +
          destaque("Redundância só protege se as instâncias <strong>não compartilharem o mesmo ponto de falha</strong>. "
                   "Duas instâncias no mesmo host não protegem contra a queda desse host.")),
    slide(1, "Conteúdo", "Geografia e autonomia organizacional",
          ul([
              "<strong>Proximidade reduz latência</strong> — posicionar recursos perto do usuário encurta o caminho da rede.",
              "<strong>Residência de dados</strong> — algumas informações precisam permanecer em uma jurisdição específica.",
              "<strong>Preço da cópia</strong> — é preciso decidir quando uma atualização se torna visível nas demais regiões.",
              "<strong>Conflitos e partições</strong> — o projeto define o que acontece durante uma interrupção entre regiões.",
              "<strong>Autonomia de equipes</strong> — serviços separados permitem implantar e evoluir partes independentemente.",
              "<strong>Monólito distribuído</strong> — se toda mudança exige coordenação simultânea, há distribuição técnica sem autonomia real.",
          ]), visual="compare"),
    citacao(
        "“Distribuir não é um objetivo isolado. É uma resposta a requisitos que uma arquitetura "
        "centralizada não atende de forma satisfatória.”",
        "— síntese da Aula 1"),
    slide(1, "Conteúdo", "Propriedades que mudam o raciocínio",
          ul([
              "<strong>Concorrência</strong> — componentes trabalham ao mesmo tempo e disputam recursos. Não basta a operação estar correta isolada: é preciso analisar quais ordens de execução preservam as invariantes.",
              "<strong>Sem estado global instantâneo</strong> — cada componente só vê o que já chegou até ele. Duas visões diferentes podem ser coerentes com as observações locais de cada um.",
              "<strong>Falhas parciais</strong> — um componente pode falhar enquanto outro funciona. Mensagem atrasada e serviço parado produzem o mesmo sintoma: silêncio.",
              "<strong>Heterogeneidade</strong> — linguagens, bancos, protocolos e versões convivem. Contratos e compatibilidade passam a fazer parte do sistema.",
          ]) + "\n" +
          destaque("Divergência não é sinônimo de erro. O projeto define <strong>quais estados podem divergir, "
                   "por quanto tempo e com qual mecanismo de convergência</strong>."),
          visual="map"),
    slide(1, "Conteúdo", "O silêncio ambíguo: cinco leituras de um mesmo timeout",
          p("Após um timeout na autorização de pagamento, a NexaOrder <strong>não sabe</strong> o que "
            "aconteceu do outro lado. Todas as hipóteses abaixo produzem exatamente o mesmo sintoma:") + "\n" +
          ul([
              "A requisição <strong>não chegou</strong> ao provedor.",
              "Chegou, mas <strong>ainda não foi processada</strong>.",
              "Foi processada e a <strong>resposta se perdeu</strong>.",
              "<strong>Continua em execução</strong> neste momento.",
              "<strong>Falhou</strong> antes de produzir qualquer efeito.",
          ]) + "\n" +
          destaque("Repetir sem proteção pode gerar <strong>cobrança duplicada</strong>; desistir de imediato "
                   "pode <strong>abandonar uma compra válida</strong>. A saída passa por idempotência, "
                   "identificação de operações, consulta de estado e reconciliação — temas das próximas aulas."),
          visual="timeline"),
    slide(1, "Conteúdo", "Transparência: útil para o usuário, perigosa para o projeto",
          p("Esconder localização, replicação e migração melhora a experiência externa. Esconder a rede "
            "do <strong>raciocínio interno</strong> do engenheiro produz projetos frágeis: uma chamada "
            "remota não é uma chamada local.") + "\n" +
          ul([
              "Tem latência <strong>maior e variável</strong>.",
              "Pode <strong>falhar sem que o destino tenha falhado</strong>.",
              "Pode <strong>produzir efeito sem retornar confirmação</strong>.",
              "Depende de <strong>serialização</strong> dos dados trafegados.",
              "Atravessa <strong>limites de segurança</strong> e de organização.",
              "Pode ser <strong>repetida</strong> e exige compatibilidade de contrato.",
          ]), visual="compare"),
    slide(1, "Conteúdo", "Quatro métricas que não devem ser confundidas",
          ul([
              "<strong>Latência</strong> — tempo para concluir uma operação. Médias escondem casos ruins; p95 de 300 ms significa que 5% das observações demoraram mais que isso.",
              "<strong>Throughput</strong> — trabalho concluído por unidade de tempo, como pedidos por segundo.",
              "<strong>Disponibilidade</strong> — o serviço consegue atender? Um endpoint pode responder e ainda estar funcionalmente indisponível.",
              "<strong>Confiabilidade</strong> — produzir resultados corretos de forma sustentada. Responder rápido e duplicar cobranças não é confiabilidade.",
          ]) + "\n" +
          destaque("Aumentar concorrência eleva o throughput <strong>até que algum recurso sature</strong>. "
                   "Depois do joelho da curva, as filas crescem e a latência sobe de forma abrupta — "
                   "desempenho e correção precisam ser avaliados em conjunto."),
          visual="compare"),
    slide(1, "Conteúdo", "Estilos arquiteturais iniciais",
          tabela(["Estilo", "Como organiza o fluxo", "Onde aparece o limite"], [
              ["Cliente-servidor", "Clientes solicitam; servidores fornecem recursos", "Um servidor concentra capacidade e disponibilidade"],
              ["Em camadas", "Apresentação, aplicação, domínio e dados", "Separar cada camada por rede acrescenta latência e falhas"],
              ["Peer-to-peer", "Participantes atuam como cliente e servidor", "Descoberta, confiança e consistência ficam mais difíceis"],
              ["Serviços", "Capacidades de negócio expostas por contratos", "Sem coesão e baixo acoplamento, vira monólito distribuído"],
          ]) + "\n" +
          destaque("Camadas ajudam a separar interesses, mas <strong>não exigem distribuição física</strong>. "
                   "Distribuir uma camada precisa ser decisão justificada, não consequência do desenho.")),
    slide(1, "Conteúdo", "Decisão arquitetural: benefício, custo e evidência",
          p("Uma decisão madura não afirma apenas que “microsserviços escalam” ou que “a nuvem garante "
            "disponibilidade”. Ela encadeia quatro elementos:") + "\n" +
          ul([
              "<strong>Requisito</strong> — processar 800 pedidos por segundo no pico.",
              "<strong>Decisão</strong> — manter múltiplas instâncias sem estado atrás de um balanceador.",
              "<strong>Compromisso</strong> — sessões locais deixam de ser confiáveis e o banco pode virar gargalo.",
              "<strong>Evidência</strong> — teste de carga com p95 abaixo do objetivo e falha controlada de uma instância.",
          ]), visual="cycle"),
    slide(1, "Pausa para reflexão", "Quando a resposta madura é não distribuir",
          p("Um sistema interno é usado por <strong>30 funcionários</strong>, processa poucas solicitações, "
            "opera em horário comercial e tolera alguns minutos de indisponibilidade. A equipe propõe "
            "dividi-lo em 20 microsserviços, com mensageria, múltiplos bancos e Kubernetes.") + "\n" +
          ul([
              "Quais <strong>requisitos</strong> justificariam essa distribuição?",
              "Quais <strong>custos operacionais</strong> seriam introduzidos?",
              "Que <strong>alternativa intermediária</strong> preservaria modularidade sem multiplicar falhas de rede?",
              "Quais <strong>métricas</strong> deveriam ser coletadas antes de decidir?",
          ]) + "\n" +
          destaque("Uma resposta tecnicamente madura pode recomendar um <strong>monólito modular</strong>. "
                   "Engenharia distribuída também consiste em reconhecer quando não distribuir.")),
    pontos_chave(1, [
        ("Definição", "Componentes autônomos que coordenam ações por mensagens, sem memória global instantânea nem relógio perfeito."),
        ("Requisito, não moda", "Escalabilidade, disponibilidade e autonomia trazem benefícios e introduzem coordenação e novos modos de falha."),
        ("Propriedades novas", "Concorrência, ausência de estado global e falhas parciais mudam o raciocínio de projeto, não apenas o código."),
        ("Métricas distintas", "Latência, throughput, disponibilidade e confiabilidade medem dimensões diferentes e não se substituem."),
        ("A rede não some", "Transparência simplifica a experiência do usuário; para o engenheiro, chamada remota nunca é chamada local."),
        ("Decisão explícita", "Toda decisão arquitetural registra requisito, mecanismo, compromisso e evidência de validação."),
    ]),
    slide(1, "Atividade prática", "Mãos à obra: registro de decisão arquitetural",
          p("Elabore um <strong>registro de decisão arquitetural</strong> de uma página para a NexaOrder. "
            "O texto precisa permitir que outra pessoa entenda por que a decisão foi tomada.") + "\n" +
          ul([
              "<strong>1.</strong> Selecione um requisito: capacidade, disponibilidade ou expansão geográfica.",
              "<strong>2.</strong> Descreva o estado atual da aplicação.",
              "<strong>3.</strong> Proponha uma decisão de distribuição.",
              "<strong>4.</strong> Liste pelo menos três benefícios esperados.",
              "<strong>5.</strong> Liste pelo menos três custos ou riscos introduzidos.",
              "<strong>6.</strong> Defina duas métricas e um experimento de validação.",
          ]) + "\n" +
          destaque("<strong>7.</strong> Represente a solução em um diagrama simples, indicando os componentes "
                   "envolvidos e por onde passa a comunicação.")),
    encerramento(
        "Você já reconhece o que caracteriza um sistema distribuído, sabe justificar a distribuição a partir "
        "de um requisito e identifica os compromissos que ela introduz. Na próxima aula, o foco passa a ser "
        "como esses componentes conversam: APIs, RPC e mensageria.",
        "Próxima aula: Aula 2 — Comunicação entre processos."),
])

# ---------------------------------------------------------------- Aula 2

A2 = montar([
    capa(2, "Comunicação entre processos: APIs, RPC e mensageria", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um fluxo HTTP "
        "síncrono em que pedidos aguarda estoque e pagamento antes de responder ao cliente; um quadro "
        "comparativo entre fila ponto a ponto e publicação-assinatura; um painel numérico com a "
        "progressão do backoff exponencial de 200 ms a 3,2 s; um fluxo de retentativa protegida por "
        "chave de idempotência; e uma tabela comparando o fluxo síncrono encadeado com o fluxo "
        "orientado a eventos da NexaOrder."
    ),
    sumario("Comunicação entre processos: APIs, RPC e mensageria", [
        "Comunicação síncrona e assíncrona: quando esperar e quando seguir",
        "HTTP e APIs orientadas a recursos",
        "RPC e contratos de interface",
        "Serialização e evolução de esquema",
        "Filas, publicação-assinatura e eventos",
        "Timeouts, retries, backoff e jitter",
        "Idempotência e correlação de requisições",
        "Dois fluxos de criação de pedido comparados",
    ]),
    slide(2, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Decidir</strong> entre comunicação síncrona e assíncrona a partir do contrato entre serviços, não do hábito.",
              "<strong>Modelar</strong> APIs orientadas a recursos com semântica de verbos e códigos de status bem definidos.",
              "<strong>Evoluir</strong> esquemas de mensagem sem quebrar consumidores implantados em versões anteriores.",
              "<strong>Distinguir</strong> fila de publicação-assinatura, e evento de comando.",
              "<strong>Dimensionar</strong> timeouts e políticas de retentativa com backoff exponencial e jitter.",
              "<strong>Tornar</strong> operações repetíveis com segurança usando chave de idempotência e correlação.",
          ]), visual="map"),
    slide(2, "Situação-problema", "Quando a chamada deixa de ser local",
          p("Após decompor a NexaOrder em serviços, a equipe manteve o hábito do monólito: cada etapa "
            "chamava a seguinte e <strong>esperava a resposta</strong> antes de prosseguir. Com pouco "
            "tráfego, funcionava. Sob campanha de vendas, mudou de comportamento:") + "\n" +
          ul([
              "Uma lentidão no provedor de pagamento <strong>prendeu conexões</strong> no serviço de estoque.",
              "Pedidos esperava estoque; o cliente via a tela de carregamento por <strong>vários segundos</strong>.",
              "Clientes cancelavam e tentavam de novo, gerando <strong>dois pedidos para o mesmo carrinho</strong>.",
              "Respostas chegavam depois da expiração da interface: pedido <strong>“pendente” apesar de processado</strong>.",
          ]) + "\n" +
          destaque("Duas perguntas passaram a organizar o projeto: <strong>quando faz sentido esperar</strong> "
                   "uma resposta antes de continuar, e <strong>quando basta registrar a intenção</strong> e "
                   "seguir em frente? Não há resposta universal — depende do contrato, da tolerância a atraso "
                   "e do tratamento de falhas."),
          visual="compare"),
    slide(2, "Conteúdo", "Comunicação síncrona e assíncrona",
          ul([
              "<strong>Síncrona</strong> — quem solicita aguarda a resposta antes de continuar. Uma chamada, um resultado, fluxo linear e fácil de raciocinar.",
              "<strong>Assíncrona</strong> — quem solicita registra a intenção e segue. O resultado chega por outro canal: notificação, evento posterior ou consulta de status.",
              "<strong>Custo da síncrona</strong> — em cadeias longas, a latência percebida se aproxima da <em>soma</em> das latências do caminho crítico.",
              "<strong>Ganho da assíncrona</strong> — reduz o acoplamento temporal: o pagamento pode estar indisponível sem impedir que o pedido seja aceito.",
          ]) + "\n" +
          destaque("Nenhum modelo é superior em abstrato. Síncrono serve quando o cliente precisa da resposta "
                   "<strong>para decidir o próximo passo</strong> — conferir se o item ainda existe antes da tela "
                   "de pagamento. Assíncrono serve quando o resultado pode ser processado depois — emitir nota "
                   "fiscal, avisar o centro de distribuição."),
          visual="compare"),
    slide(2, "Exemplo numérico", "O que o encadeamento síncrono custa",
          p("Em um modelo simplificado com etapas obrigatórias e falhas independentes, a latência do fluxo "
            "soma as etapas e a disponibilidade do fluxo é o <strong>produto</strong> das disponibilidades:") + "\n" +
          formula("A<sub>fluxo</sub> = A<sub>pedidos</sub> × A<sub>estoque</sub> × A<sub>pagamento</sub> × A<sub>expedição</sub>") + "\n" +
          numeros([
              ("99,9%", "por etapa"),
              ("4", "etapas encadeadas"),
              ("99,6%", "disponibilidade do fluxo"),
              ("≈ 2 h 53 min", "indisponível por mês"),
          ]) + "\n" +
          p("Quatro etapas com 99,9% cada não entregam 99,9% — entregam <strong>0,999⁴ ≈ 99,6%</strong>. "
            "O encadeamento multiplica as chances de falha, e dependências compartilhadas ou falhas "
            "correlacionadas exigem medição conjunta, não apenas a multiplicação teórica.")),
    slide(2, "Conteúdo", "HTTP e APIs orientadas a recursos",
          p("Cada entidade relevante do domínio — um pedido, uma reserva, uma cobrança — vira um "
            "<strong>recurso</strong> identificado por uma URI, e as operações se expressam por verbos.") + "\n" +
          tabela(["Elemento", "Semântica", "Exemplo na NexaOrder"], [
              ["<code>POST</code>", "Cria um recurso e devolve um identificador", "<code>POST /pedidos</code>"],
              ["<code>GET</code>", "Consulta o estado atual, sem efeito colateral", "<code>GET /pedidos/{id}</code>"],
              ["<code>PUT</code> / <code>PATCH</code>", "Substitui ou atualiza parcialmente", "<code>PATCH /pedidos/{id}</code>"],
              ["Faixa 2xx", "Sucesso", "<code>201 Created</code> na criação do pedido"],
              ["Faixa 4xx", "Erro do cliente: dado inválido ou recurso inexistente", "<code>404</code> em pedido que não existe"],
              ["Faixa 5xx", "Erro do servidor", "<code>503</code> quando o estoque não responde"],
          ]) + "\n" +
          destaque("<strong>Sem estado</strong> (<em>stateless</em>) é uma decisão arquitetural da API, não uma "
                   "garantia do protocolo. Quando adotada, qualquer instância pode atender qualquer requisição — "
                   "é o que torna o balanceamento simples.")),
    slide(2, "Conteúdo", "RPC e contratos de interface",
          ul([
              "<strong>O que é</strong> — invocar <code>estoque.reservarItem(pedidoId, itemId, qtd)</code> como se fosse função local; o mecanismo transforma isso em mensagem de rede.",
              "<strong>O risco</strong> — é exatamente a transparência que a Aula 1 apontou: conveniente para quem usa, perigosa para quem projeta.",
              "<strong>Falhas que a função local não tem</strong> — rede indisponível, mensagem perdida, resposta ausente mesmo com a operação concluída.",
              "<strong>O valor real</strong> — o contrato explícito: métodos, tipos de parâmetro e retorno, e erros possíveis, descritos em uma IDL.",
              "<strong>Geração de código</strong> — cliente e servidor compatíveis são gerados do mesmo contrato, reduzindo divergência manual.",
              "<strong>Síncrono não é o protocolo</strong> — HTTP e RPC sustentam interações assíncronas; síncrono/assíncrono descreve o <em>contrato de interação</em>.",
          ]), visual="compare"),
    slide(2, "Conteúdo", "Serialização e evolução de esquema",
          p("Serializar é transformar dados em memória em bytes transmissíveis. O formato (JSON, binário) "
            "afeta tamanho e desempenho — mas o problema crítico é a <strong>evolução do esquema</strong>: "
            "serviços independentes são implantados em momentos diferentes.") + "\n" +
          ul([
              "<strong>Campos novos são opcionais</strong>, com valor padrão bem definido quando ausentes.",
              "<strong>Não remova nem renomeie</strong> campos que consumidores existentes ainda utilizam.",
              "<strong>Versione explicitamente</strong> quando a mudança for de fato incompatível.",
              "<strong>Teste a compatibilidade</strong> entre versões de produtor e consumidor antes de implantar.",
          ]) + "\n" +
          destaque("Ignorar esses cuidados transforma uma alteração aparentemente local — um novo campo "
                   "<code>canalVenda</code> — em uma <strong>interrupção distribuída</strong>, sentida por "
                   "serviços que a equipe de pedidos talvez nem saiba que existem."),
          visual="map"),
    citacao(
        "“Uma chamada RPC pode falhar de formas que uma chamada local nunca falha: a resposta pode "
        "não retornar mesmo que a operação remota tenha sido concluída.”",
        "— síntese da Aula 2"),
    slide(2, "Conteúdo", "Fila e publicação-assinatura",
          p("A comunicação assíncrona costuma passar por um <em>broker</em>, que recebe, armazena "
            "temporariamente e entrega mensagens — desacoplando o tempo de vida do produtor do consumidor.") + "\n" +
          ul([
              "<strong>Fila (ponto a ponto)</strong> — cada mensagem vai a <em>um único</em> consumidor entre os que competem por ela.",
              "<strong>Uso típico da fila</strong> — distribuir trabalho: processar reservas em paralelo por várias instâncias do mesmo serviço.",
              "<strong>Publicação-assinatura</strong> — cada mensagem de um tópico é entregue a <em>todos</em> os assinantes interessados.",
              "<strong>Uso típico do pub-sub</strong> — notificar vários serviços sobre o mesmo acontecimento sem acoplar o produtor a essa lista.",
          ]), visual="compare"),
    slide(2, "Conteúdo", "Evento e comando: uma distinção que muda o acoplamento",
          ul([
              "<strong>Evento</strong> — registro de algo que <em>já aconteceu</em>: <code>PedidoCriado</code>, <code>PagamentoAprovado</code>.",
              "<strong>Comando</strong> — solicitação de uma <em>ação futura</em>: <code>ReservarEstoque</code>.",
              "<strong>Quem publica evento não escolhe quem reage</strong> — estoque, antifraude e um futuro serviço de recomendação assinam o mesmo evento.",
              "<strong>Benefício</strong> — novos consumidores entram sem alterar o produtor.",
              "<strong>Custo</strong> — não há resposta imediata: quem publica não sabe, no mesmo instante, se e como os assinantes reagirão.",
              "<strong>Consequência de projeto</strong> — o estado do pedido deixa de ser binário e passa a ser uma <em>progressão</em> a ser rastreada.",
          ]), visual="map"),
    slide(2, "Conteúdo", "Timeout, retry, backoff e jitter",
          p("Toda chamada de rede precisa de um limite de espera. Sem ele, uma dependência lenta retém "
            "recursos indefinidamente e propaga lentidão — foi o que aconteceu na situação-problema.") + "\n" +
          ul([
              "<strong>Timeout</strong> — não prova que a operação falhou; indica que a resposta não chegou no prazo tolerado.",
              "<strong>Retry só para falha transitória</strong> — e apenas se ainda houver prazo no orçamento e a repetição for segura.",
              "<strong>Erro permanente não se retenta</strong> — validações 4xx, prazo esgotado ou sinais de sobrecarga pedem falha imediata ou controle de admissão.",
              "<strong>Thundering herd</strong> — retentar sem cuidado joga uma nova onda sobre um serviço já sobrecarregado, piorando a situação.",
              "<strong>Backoff exponencial</strong> — cada tentativa espera mais que a anterior, dando tempo de recuperação.",
              "<strong>Jitter</strong> — soma aleatória que evita que todos os clientes retentem no mesmo instante.",
          ]), visual="map"),
    slide(2, "Exemplo numérico", "A progressão do backoff exponencial",
          formula("t<sub>n</sub> = min( t<sub>base</sub> × 2<sup>n</sup> , t<sub>máx</sub> ) + U(0, t<sub>jitter</sub>)") + "\n" +
          p("Com <strong>t<sub>base</sub> = 200 ms</strong> e <strong>t<sub>máx</sub> = 5000 ms</strong>, "
            "o componente exponencial (sem jitter) evolui assim:") + "\n" +
          numeros([
              ("200 ms", "n = 0"),
              ("400 ms", "n = 1"),
              ("800 ms", "n = 2"),
              ("1,6 s", "n = 3"),
              ("3,2 s", "n = 4"),
          ]) + "\n" +
          destaque("Sem o teto, a espera de <strong>n = 5</strong> seria de <strong>6,4 s</strong> — impraticável "
                   "para quem aguarda. O jitter soma alguns milissegundos aleatórios a cada valor, espalhando as "
                   "tentativas mesmo quando muitos clientes falharam ao mesmo tempo.")),
    slide(2, "Conteúdo", "Idempotência: tornar a retentativa segura",
          p("Uma operação é <strong>idempotente</strong> quando executá-la mais de uma vez produz o mesmo "
            "efeito que executá-la uma vez. Consultar um pedido é idempotente por natureza; criar um pedido, "
            "sem cuidado adicional, <strong>não é</strong>.") + "\n" +
          ul([
              "<strong>1. O cliente gera a chave</strong> de idempotência <em>antes</em> do primeiro envio.",
              "<strong>2. A chave acompanha</strong> o pedido original e toda retentativa da mesma operação.",
              "<strong>3. O serviço registra</strong> as chaves já processadas junto com o resultado.",
              "<strong>4. Chave repetida</strong> devolve o resultado da primeira execução, sem criar um novo pedido.",
          ]) + "\n" +
          destaque("Backoff e jitter espalham as tentativas no tempo, mas <strong>não resolvem a duplicação</strong>: "
                   "se a operação já produziu efeito no destino, repeti-la sem chave de idempotência gera "
                   "cobrança duplicada."),
          visual="flow"),
    slide(2, "Conteúdo", "Correlação: reconstruir o caminho de uma operação",
          ul([
              "<strong>O que é</strong> — um identificador que acompanha uma operação lógica por várias chamadas, mensagens e retentativas.",
              "<strong>Diferença da chave de idempotência</strong> — a chave evita <em>duplicar efeito</em>; a correlação permite <em>reconstruir o caminho</em>.",
              "<strong>Atravessa serviços</strong> — o mesmo identificador segue de pedidos a estoque, pagamento e expedição.",
              "<strong>Base da observabilidade</strong> — sem correlação, um incidente vira uma coleção de logs que ninguém consegue costurar.",
              "<strong>Decidido no contrato</strong> — precisa ser previsto no desenho da comunicação, não improvisado durante o incidente.",
              "<strong>Retomada na Unidade 4</strong> — traces e spans se apoiam exatamente nessa ideia.",
          ]), visual="map"),
    slide(2, "Conteúdo", "Dois fluxos de criação de pedido, lado a lado",
          tabela(["Critério", "Síncrono encadeado", "Orientado a eventos"], [
              ["Resposta ao cliente", "Confirmação completa em uma única resposta", "Status “processando”, imediato"],
              ["Latência percebida", "Soma das etapas do caminho crítico", "Apenas o registro da intenção"],
              ["Falha de uma etapa", "Indisponibiliza o fluxo inteiro", "Gera evento próprio e pode acionar compensação"],
              ["Novos consumidores", "Exigem alterar quem chama", "Assinam o evento sem tocar no produtor"],
              ["Custo introduzido", "Acoplamento temporal forte", "Rastrear etapa, tratar fora de ordem, comunicar progressão"],
          ]) + "\n" +
          destaque("No fluxo por eventos, a sequência <code>PedidoCriado</code> → <code>EstoqueReservado</code> → "
                   "<code>PagamentoAprovado</code> → <code>PedidoEnviado</code> preserva as <strong>pré-condições "
                   "de negócio</strong>. Consumidores sem pré-condição, como antifraude, reagem direto a "
                   "<code>PedidoCriado</code>.")),
    pontos_chave(2, [
        ("Síncrono soma", "Simplifica o raciocínio, mas soma latências e propaga indisponibilidade pela cadeia de chamadas."),
        ("Assíncrono desacopla", "Reduz o acoplamento temporal ao custo de resposta não imediata e de maior complexidade de rastreamento."),
        ("Contratos importam", "APIs de recursos e RPC têm ênfases diferentes; em ambos, o contrato explícito é o que sustenta a evolução."),
        ("Esquema evolui", "Produtores e consumidores são implantados em momentos distintos: compatibilidade é requisito, não detalhe."),
        ("Retry com critério", "Timeout limita a espera; retry com backoff e jitter só vale para falha transitória, dentro de um orçamento."),
        ("Idempotência e correlação", "A chave evita duplicar efeito; o identificador de correlação torna a operação rastreável de ponta a ponta."),
    ]),
    slide(2, "Atividade prática", "Mãos à obra: o contrato do evento PedidoCriado",
          p("Modele o contrato do evento <code>PedidoCriado</code> e documente as decisões em meia página, "
            "como se fossem apresentadas à equipe de arquitetura.") + "\n" +
          ul([
              "<strong>1.</strong> Liste campos obrigatórios e opcionais da mensagem, indicando o tipo de dado.",
              "<strong>2.</strong> Inclua chave de idempotência e identificador de correlação, justificando cada um.",
              "<strong>3.</strong> Descreva uma mudança futura de esquema e como introduzi-la sem quebrar consumidores.",
              "<strong>4.</strong> Separe reações independentes das que exigem pré-condição comprovada.",
              "<strong>5.</strong> Justifique por que a expedição não pode começar antes da aprovação do pagamento.",
              "<strong>6.</strong> Defina uma política limitada de retry com backoff, jitter e orçamento de tentativas.",
          ]), visual="map"),
    encerramento(
        "Você já sabe escolher entre esperar e seguir em frente, modelar contratos que sobrevivem à evolução "
        "e proteger chamadas de rede com timeout, retry e idempotência. Na próxima aula, enfrentamos a pergunta "
        "que a mensageria deixa em aberto: qual evento aconteceu primeiro?",
        "Próxima aula: Aula 3 — Concorrência, relógios e ordenação de eventos."),
])

# ---------------------------------------------------------------- Aula 3

A3 = montar([
    capa(3, "Concorrência, relógios e ordenação de eventos", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um painel numérico "
        "com o desvio máximo de relógio acumulado em uma hora; uma sequência com as três regras da "
        "relação happened-before; uma tabela com a evolução dos relógios lógicos de Lamport entre "
        "Pedidos, Estoque e Pagamento; uma comparação posição a posição dos vetores (2,3,0) e (2,1,2), "
        "em que nenhum domina o outro; e um quadro contrastando ordem parcial e ordem total."
    ),
    sumario("Concorrência, relógios e ordenação de eventos", [
        "A ausência de um relógio global",
        "Relógios físicos, desvio e sincronização",
        "A relação happened-before",
        "Relógios lógicos de Lamport",
        "Relógios vetoriais e detecção de concorrência",
        "Ordem total, ordem parcial e causalidade",
        "Conflitos concorrentes em estoque e pagamento",
        "Política de resolução definida a priori",
    ]),
    slide(3, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Explicar</strong> por que carimbos de hora físicos não ordenam com segurança eventos de processos diferentes.",
              "<strong>Estimar</strong> o desvio máximo entre relógios a partir da taxa de drift e do intervalo de sincronização.",
              "<strong>Aplicar</strong> a relação happened-before para identificar pares causalmente relacionados.",
              "<strong>Calcular</strong> relógios lógicos de Lamport ao longo de uma sequência de eventos e mensagens.",
              "<strong>Comparar</strong> relógios vetoriais para afirmar, com certeza, que dois eventos são concorrentes.",
              "<strong>Definir</strong> uma política de resolução de conflito antes que o conflito ocorra em produção.",
          ]), visual="map"),
    slide(3, "Situação-problema", "Qual evento aconteceu primeiro?",
          p("O painel de operações da NexaOrder ordena eventos pelo carimbo de hora físico do servidor de "
            "origem. Em um incidente, <code>ReservaCancelada</code> apareceu <strong>antes</strong> de "
            "<code>PagamentoAprovado</code>. A equipe concluiu que o cancelamento veio primeiro e "
            "<strong>estornou o pagamento automaticamente</strong>.") + "\n" +
          ul([
              "Depois se descobriu: o relógio do servidor de pagamento estava <strong>atrasado</strong>.",
              "A ordem exibida refletia a ordem dos <strong>carimbos</strong>, não a dos acontecimentos.",
              "O problema não é configuração: é <strong>estrutural</strong>.",
              "Não existe relógio único capaz de ordenar eventos de processos diferentes com precisão absoluta.",
          ]), visual="timeline"),
    slide(3, "Conteúdo", "A ausência de um relógio global",
          ul([
              "<strong>Dentro de um processo</strong>, instruções ocorrem em sequência total: comparar “antes” e “depois” é trivial.",
              "<strong>Entre processos</strong>, cada um tem seu relógio local e não há sinal instantâneo que os sincronize perfeitamente.",
              "<strong>A rede introduz atraso variável</strong> entre envio e chegada, e essa variação não pode ser eliminada.",
              "<strong>Consequência</strong> — “o pagamento foi recusado antes ou depois da reserva?” não se responde comparando carimbos independentes.",
          ]) + "\n" +
          destaque("Um carimbo de hora físico reflete apenas o relógio local de quem o gerou — "
                   "e <strong>relógios locais divergem</strong>."),
          visual="map"),
    slide(3, "Exemplo numérico", "Quanto dois relógios podem divergir em uma hora",
          p("Relógios de computadores comuns sofrem <strong>desvio</strong> (<em>drift</em>) causado por "
            "variações no oscilador. A sincronização por rede reduz a divergência periodicamente, mas "
            "não a elimina entre sincronizações sucessivas:") + "\n" +
          formula("δ<sub>máx</sub> ≤ ε + 2 ρ T") + "\n" +
          numeros([
              ("50 ppm", "taxa de drift (ρ)"),
              ("3600 s", "sem sincronizar (T)"),
              ("360 ms", "desvio acumulado"),
              ("2×", "um adianta, o outro atrasa"),
          ]) + "\n" +
          destaque("Com ε = 0, ρ = 0,00005 e T = 3600 s: <strong>δ ≤ 2 × 0,00005 × 3600 = 0,36 s</strong>. "
                   "Suficiente para <strong>inverter</strong>, em um painel ordenado por carimbo físico, dois "
                   "eventos separados por menos de 360 ms. Sincronizar com mais frequência reduz a parcela de "
                   "drift, mas não elimina a inversão para eventos suficientemente próximos.")),
    slide(3, "Conteúdo", "A relação happened-before",
          p("Diante da impossibilidade de confiar em relógios físicos, Leslie Lamport propôs uma relação "
            "lógica (→) que ordena eventos por <strong>causalidade observável</strong>, não por tempo de relógio:") + "\n" +
          ul([
              "<strong>1. Mesmo processo</strong> — se <em>a</em> e <em>b</em> ocorrem no mesmo processo e <em>a</em> executa antes, então a → b.",
              "<strong>2. Mensagem</strong> — se <em>a</em> é o envio de uma mensagem e <em>b</em> é o recebimento dela, então a → b.",
              "<strong>3. Transitividade</strong> — se a → b e b → c, então a → c.",
          ]) + "\n" +
          destaque("Dois eventos sem nenhuma dessas relações, direta ou transitiva, são "
                   "<strong>concorrentes</strong>: nenhum pode ter causado o outro. Essa noção não depende de "
                   "proximidade no tempo físico — depende exclusivamente de existir ou não um caminho causal."),
          visual="flow"),
    slide(3, "Conteúdo", "Relógios lógicos de Lamport: as três regras",
          ul([
              "<strong>Evento local ou envio</strong> — incremente o contador em 1 e use o novo valor como carimbo do evento.",
              "<strong>Ao enviar</strong> — inclua na mensagem o carimbo atribuído ao evento de envio.",
              "<strong>Ao receber</strong> — ajuste o contador para <strong>máx(C<sub>local</sub>, C<sub>msg</sub>) + 1</strong>.",
              "<strong>Garantia</strong> — se a → b, então C(a) &lt; C(b): causalidade implica ordem numérica crescente.",
          ]) + "\n" +
          formula("C<sub>recebimento</sub> = máx( C<sub>local</sub> , C<sub>msg</sub> ) + 1"),
          visual="flow"),
    slide(3, "Exemplo numérico", "Lamport aplicado a um trecho da NexaOrder",
          tabela(["#", "Processo", "Ação", "Antes", "Depois"], [
              ["1", "Pedidos", "Cria o pedido (evento local)", "0", "1"],
              ["2", "Pedidos", "Envia “reservar item” ao Estoque, anexando 2", "1", "2"],
              ["3", "Estoque", "Recebe a mensagem (C<sub>msg</sub> = 2)", "0", "máx(0,2)+1 = 3"],
              ["4", "Estoque", "Envia “reserva confirmada”, anexando 4", "3", "4"],
              ["5", "Pedidos", "Recebe a confirmação (C<sub>msg</sub> = 4)", "2", "máx(2,4)+1 = 5"],
          ]) + "\n" +
          destaque("O evento 5 recebeu carimbo 5, maior que o 2 que iniciou a troca e que o 4 do envio anterior — "
                   "<strong>a → b ⇒ C(a) &lt; C(b)</strong> foi respeitado ao longo de toda a cadeia.")),
    citacao(
        "“O relógio de Lamport ordena, mas não distingue causalidade de coincidência: dois eventos "
        "concorrentes também recebem carimbos diferentes.”",
        "— síntese da Aula 3"),
    slide(3, "Conteúdo", "O limite de Lamport: ordem não é causalidade",
          ul([
              "<strong>A garantia vale em um sentido só</strong> — a → b implica C(a) &lt; C(b), mas a recíproca não é verdadeira.",
              "<strong>Coincidência numérica</strong> — se Pagamento chegasse ao carimbo 5 só por eventos internos, o empate não indicaria relação causal alguma.",
              "<strong>Concorrência não é detectável</strong> — o contador único não guarda de <em>quem</em> veio cada avanço.",
              "<strong>Consequência prática</strong> — comparar carimbos de Lamport não autoriza afirmar que um evento causou o outro.",
          ]) + "\n" +
          destaque("É exatamente essa limitação que motiva o relógio vetorial: guardar uma posição "
                   "<strong>por processo</strong>, e não um número só."),
          visual="compare"),
    slide(3, "Conteúdo", "Relógios vetoriais",
          p("Em vez de um contador, cada processo mantém um <strong>vetor</strong> com uma posição por "
            "processo do sistema:") + "\n" +
          ul([
              "<strong>Evento local</strong> — incrementa apenas a própria posição no vetor.",
              "<strong>Ao enviar</strong> — anexa o vetor completo à mensagem.",
              "<strong>Ao receber</strong> — atualiza cada posição para o maior valor entre o próprio e o recebido, e então incrementa a própria.",
              "<strong>Comparação</strong> — a → b se todas as posições de V(a) forem ≤ às de V(b), com ao menos uma estritamente menor.",
          ]) + "\n" +
          destaque("Se <strong>nenhum vetor domina o outro</strong>, os eventos são genuinamente concorrentes — "
                   "e o relógio vetorial permite afirmar isso <em>com certeza</em>, ao contrário do relógio de Lamport."),
          visual="map"),
    slide(3, "Exemplo numérico", "Dois eventos concorrentes, posição a posição",
          p("Vetores na ordem <strong>(Pedidos, Estoque, Pagamento)</strong>. O cancelamento da reserva "
            "ocorre no Estoque, por timeout do cliente; a aprovação ocorre no provedor de pagamento:") + "\n" +
          tabela(["Posição", "ReservaCancelada (2,3,0)", "PagamentoAprovado (2,1,2)", "Comparação"], [
              ["Pedidos", "2", "2", "Empate"],
              ["Estoque", "3", "1", "Maior no cancelamento"],
              ["Pagamento", "0", "2", "Maior na aprovação"],
          ]) + "\n" +
          destaque("Nenhum vetor domina o outro: os eventos são <strong>concorrentes</strong>. Nenhum causou o "
                   "outro — e o sistema precisa de uma <strong>regra de negócio explícita</strong> para decidir "
                   "qual prevalece, porque a ordem causal, sozinha, não resolve o conflito.")),
    slide(3, "Conteúdo", "Ordem total, ordem parcial e causalidade",
          ul([
              "<strong>Ordem parcial</strong> — é o que happened-before define: alguns pares são comparáveis, outros são concorrentes e incomparáveis.",
              "<strong>Ordem total</strong> — compara todo par de eventos; surge naturalmente dentro de um processo ou por imposição externa.",
              "<strong>Como se impõe</strong> — por um sequenciador central ou por desempate determinístico usando o identificador do processo.",
              "<strong>O que ela não faz</strong> — impor ordem total sobre eventos concorrentes <em>não recupera</em> a causalidade que nunca existiu.",
              "<strong>Quando é útil</strong> — quando o sistema precisa de uma decisão única e consistente sobre qual atualização “vence”.",
              "<strong>O erro conceitual</strong> — confundir a posição escolhida arbitrariamente com a afirmação de que um evento causou o outro.",
          ]), visual="compare"),
    slide(3, "Conteúdo", "Conflitos concorrentes em estoque e pagamento",
          p("O incidente da abertura pode agora ser reformulado com precisão: cancelamento e aprovação eram "
            "<strong>concorrentes</strong>. Nenhuma sincronização de relógio físico eliminaria isso, porque a "
            "concorrência é estrutural — os eventos ocorreram em processos diferentes, sem troca de mensagem "
            "entre si antes de acontecerem.") + "\n" +
          ul([
              "<strong>Priorizar o cancelamento</strong> — conservador: evita cobrar por item indisponível, mas pode gerar estorno desnecessário.",
              "<strong>Priorizar a aprovação</strong> — otimista: pode gerar cobrança para item que não será enviado.",
              "<strong>Tratar como exceção</strong> — suspender o pedido para revisão manual ou automatizada.",
              "<strong>Qualquer uma é legítima</strong> — o erro é não escolher e deixar a ordem de chegada acidental decidir.",
          ]), visual="compare"),
    slide(3, "Pausa para reflexão", "O que os dados realmente autorizam concluir",
          p("No incidente, <code>ReservaCancelada</code> aparece <strong>três segundos antes</strong> de "
            "<code>PagamentoAprovado</code>, e o relógio do servidor de pagamento estava atrasado.") + "\n" +
          ul([
              "A conclusão “o cancelamento ocorreu primeiro” está <strong>logicamente garantida</strong> pelos dados disponíveis?",
              "Que informação, se registrada nos eventos, permitiria decidir se há relação causal ou apenas concorrência?",
              "Com relógios vetoriais, o sistema saberia <strong>qual deve prevalecer</strong> — ou apenas que ambos são concorrentes?",
              "Que política de negócio a NexaOrder deveria adotar diante desse par concorrente?",
          ]) + "\n" +
          destaque("Não existe uma única resposta correta para a última pergunta. Existe, porém, uma resposta "
                   "<strong>ausente</strong> que caracteriza um sistema mal projetado: não ter pensado no "
                   "cenário antes de ele acontecer em produção.")),
    pontos_chave(3, [
        ("Sem relógio global", "Relógios físicos de máquinas diferentes divergem por desvio acumulado; carimbos não ordenam com segurança."),
        ("Causalidade observável", "Happened-before ordena por execução local e troca de mensagens, não por tempo de relógio."),
        ("Lamport ordena", "Causalidade implica ordem numérica crescente — mas a recíproca não vale."),
        ("Vetores detectam", "Comparados posição a posição, permitem afirmar com certeza que dois eventos são concorrentes."),
        ("Ordem total é escolha", "Pode ser imposta artificialmente, sem recuperar relações causais que nunca existiram."),
        ("Política a priori", "Eventos concorrentes sobre o mesmo dado exigem regra de resolução definida antes do incidente."),
    ]),
    slide(3, "Atividade prática", "Mãos à obra: construir carimbos de Lamport",
          p("Construa os carimbos lógicos para a sequência abaixo, com Pedidos (Pd), Estoque (Es) e "
            "Expedição (Ex) iniciando em zero. Para cada evento, calcule o contador resultante e indique "
            "qual regra foi aplicada.") + "\n" +
          ul([
              "<strong>1–2.</strong> Pd cria o pedido (local) e envia ao Es a solicitação de reserva.",
              "<strong>3–4.</strong> Es recebe a solicitação e registra a baixa no estoque físico (local).",
              "<strong>5–6.</strong> Es envia a confirmação a Pd, que a recebe e ajusta seu contador.",
              "<strong>7–8.</strong> Pd envia a Ex a solicitação de expedição; Ex recebe e ajusta.",
          ]) + "\n" +
          destaque("Ao final, identifique <strong>dois eventos concorrentes</strong> da sequência — caso existam — "
                   "justificando com base na definição de happened-before, e não na proximidade dos carimbos.")),
    encerramento(
        "Você já sabe raciocinar sobre tempo e ordem sem depender cegamente de relógios físicos, e reconhece "
        "quando dois eventos são genuinamente concorrentes. Na próxima aula, tratamos do que acontece quando "
        "um componente não responde: modelos de falha e desenho para recuperação.",
        "Próxima aula: Aula 4 — Modelos de falha e desenho para recuperação."),
])

# ---------------------------------------------------------------- Aula 4

A4 = montar([
    capa(4, "Modelos de falha e desenho para recuperação", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um quadro com os "
        "quatro modelos de falha — parada, omissão, temporização e comportamento arbitrário; um "
        "diagrama de duas zonas de disponibilidade isoladas por um rompimento de rede; um ciclo de "
        "estados do circuit breaker entre fechado, aberto e semiaberto; um painel numérico com a taxa "
        "de erro de 12 falhas em 20 chamadas; e um diagrama do serviço de pedidos dividido em dois "
        "compartimentos de conexões isolados."
    ),
    sumario("Modelos de falha e desenho para recuperação", [
        "Modelos de falha: parada, omissão, temporização e bizantina",
        "Falha parcial e detectores de falha imperfeitos",
        "Particionamento de rede e split-brain",
        "Redundância não basta: isolamento",
        "Timeout como decisão, não como prova",
        "Circuit breaker: fechado, aberto e semiaberto",
        "Bulkhead e degradação graciosa",
        "Objetivos de confiabilidade explícitos",
    ]),
    slide(4, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Classificar</strong> falhas em parada, omissão, temporização e comportamento arbitrário.",
              "<strong>Reconhecer</strong> detectores de falha como estimativas sujeitas a falso positivo e falso negativo.",
              "<strong>Identificar</strong> o risco de divergência de estado (split-brain) em um particionamento de rede.",
              "<strong>Aplicar</strong> circuit breaker, bulkhead e degradação graciosa como padrões complementares de contenção.",
              "<strong>Calcular</strong> a taxa de erro que dispara a abertura de um disjuntor sobre uma janela de chamadas.",
              "<strong>Ligar</strong> cada investimento em resiliência a um objetivo de confiabilidade declarado.",
          ]), visual="map"),
    slide(4, "Situação-problema", "Quando lentidão vira colapso",
          p("Durante uma campanha de vendas, o provedor externo de pagamento <strong>não ficou "
            "indisponível</strong> — apenas passou a responder devagar. O serviço de pedidos o chamava de "
            "forma síncrona, sem limite de recursos dedicados:") + "\n" +
          ul([
              "As conexões disponíveis para pagamento <strong>se esgotaram rapidamente</strong>.",
              "O mesmo conjunto de conexões atendia <strong>consultas de pedidos antigos</strong>.",
              "Em minutos, quem só queria consultar o status de uma compra <strong>também deixou de receber resposta</strong>.",
              "<strong>Nenhuma linha de código continha erro</strong>: faltou contenção.",
          ]) + "\n" +
          destaque("A pergunta que organiza a aula: <strong>como conter o raio de impacto de uma falha</strong> "
                   "antes que ela vire um colapso mais amplo?"),
          visual="timeline"),
    slide(4, "Conteúdo", "Quatro modelos de falha",
          tabela(["Modelo", "Comportamento", "Onde aparece"], [
              ["<strong>Parada</strong> (crash)", "Para de funcionar e permanece parado; não emite respostas incorretas", "O mais benigno e o mais comum em infraestrutura bem operada"],
              ["<strong>Omissão</strong>", "Deixa de enviar ou receber algumas mensagens, e continua para as demais", "Perda de pacotes, fila cheia, descarte seletivo sob sobrecarga"],
              ["<strong>Temporização</strong>", "Responde corretamente, mas fora do prazo esperado", "O provedor de pagamento lento da situação-problema"],
              ["<strong>Arbitrária</strong> (bizantina)", "Produz respostas incorretas, inconsistentes ou maliciosas", "Sistemas que atravessam fronteiras de confiança"],
          ]) + "\n" +
          destaque("Presumir que <strong>qualquer dependência externa pode falhar por parada, omissão ou "
                   "temporização</strong> — e desenhar para isso — cobre a maioria dos incidentes reais sem "
                   "pagar o custo de proteção contra comportamento arbitrário.")),
    slide(4, "Conteúdo", "Falha parcial e detectores de falha",
          p("Um <strong>detector de falhas</strong> é o mecanismo — implícito ou explícito — que um componente "
            "usa para decidir se trata outro como indisponível. Detectores reais nunca são perfeitos:") + "\n" +
          ul([
              "<strong>Falso positivo</strong> — declara indisponível um componente que apenas está lento.",
              "<strong>Falso negativo</strong> — demora a perceber uma indisponibilidade real.",
              "<strong>Detectar rápido</strong> aumenta o risco de falso positivo.",
              "<strong>Esperar mais</strong> reduz falsos positivos, mas atrasa a reação a falhas reais.",
          ]) + "\n" +
          destaque("Na NexaOrder, o detector pode ser tão simples quanto contar falhas consecutivas, ou combinar "
                   "taxa de erro, latência e health checks. O essencial: <strong>qualquer detector é uma "
                   "estimativa, não uma certeza</strong> — e o resto do desenho deve considerar essa incerteza."),
          visual="compare"),
    slide(4, "Conteúdo", "Particionamento de rede e split-brain",
          ul([
              "<strong>O que é</strong> — um subconjunto de componentes perde comunicação com outro, embora cada lado continue funcionando internamente.",
              "<strong>Simetria da ilusão</strong> — de cada lado, o outro parece indisponível; tecnicamente, nenhum dos dois está caído.",
              "<strong>O perigo</strong> — ambos os lados continuarem aceitando escrita de forma independente.",
              "<strong>Split-brain</strong> — réplicas do estoque em duas zonas aceitam reservas para os mesmos itens, cada uma se julgando a única responsável.",
              "<strong>Consequência</strong> — divergência de estado que precisará ser reconciliada depois, muitas vezes com perda ou conflito de dados.",
              "<strong>Retomada na Unidade 2</strong> — replicação, tolerância a partição e consenso aprofundam o tema.",
          ]), visual="map"),
    slide(4, "Conteúdo", "Redundância não basta: o princípio do isolamento",
          p("Redundância só protege se as instâncias <strong>não compartilharem o mesmo ponto de falha</strong> "
            "e houver desvio de tráfego. Esta aula acrescenta um segundo princípio: impedir que a degradação de "
            "uma dependência se propague para partes que não dependem dela.") + "\n" +
          ul([
              "<strong>O que houve</strong> — pedidos usava o mesmo conjunto de conexões para chamar o pagamento e para atender consultas.",
              "<strong>O efeito</strong> — todas as conexões ficaram ocupadas esperando o pagamento.",
              "<strong>O dano</strong> — não sobrou capacidade para consultas, que nada tinham a ver com pagamento.",
              "<strong>A lição</strong> — a ausência de isolamento transformou uma degradação pontual em indisponibilidade ampla.",
          ]), visual="compare"),
    citacao(
        "“Um timeout não é prova de que a operação falhou; é a decisão de que a espera deixou de valer a pena.”",
        "— síntese da Aula 4"),
    slide(4, "Conteúdo", "Timeout como decisão deliberada",
          ul([
              "<strong>Curto demais</strong> — trata operações lentas, mas ainda válidas, como se tivessem falhado.",
              "<strong>Efeito colateral</strong> — desperdiça trabalho em andamento e, com retentativa, pode duplicar efeito.",
              "<strong>Longo demais</strong> — mantém recursos presos, amplia o risco de esgotamento de conexões.",
              "<strong>Efeito colateral</strong> — propaga lentidão exatamente como na situação-problema desta aula.",
          ]) + "\n" +
          destaque("Não existe valor universalmente correto. O valor apropriado depende da <strong>latência "
                   "típica observada</strong> na operação, da criticidade da resposta imediata e do custo de "
                   "manter o recurso ocupado enquanto se espera."),
          visual="compare"),
    slide(4, "Conteúdo", "Circuit breaker: três estados",
          p("O disjuntor formaliza a decisão de <strong>parar de tentar</strong> uma dependência que falha "
            "repetidamente, em vez de desperdiçar recursos em chamadas com alta probabilidade de falhar.") + "\n" +
          ul([
              "<strong>Fechado</strong> — chamadas fluem normalmente; o disjuntor monitora a taxa de falhas.",
              "<strong>Aberto</strong> — ultrapassado o limite, rejeita chamadas de imediato, sem sequer tentar a dependência.",
              "<strong>Semiaberto</strong> — decorrido o intervalo, permite um número limitado de chamadas de teste.",
              "<strong>Volta ao fechado</strong> se os testes passarem; <strong>retorna ao aberto</strong> se falharem.",
          ]), visual="cycle"),
    slide(4, "Exemplo numérico", "Quando o disjuntor abre",
          formula("taxa de erro = chamadas com falha ÷ total de chamadas na janela") + "\n" +
          p("A NexaOrder define limite de <strong>50%</strong> de falhas em uma janela das últimas "
            "<strong>20 chamadas</strong> ao provedor de pagamento, e observa <strong>12 falhas</strong>:") + "\n" +
          numeros([
              ("12", "chamadas com falha"),
              ("20", "chamadas na janela"),
              ("60%", "taxa de erro"),
              ("50%", "limite configurado"),
          ]) + "\n" +
          destaque("Como 60% excede o limite, o disjuntor <strong>abre</strong>: as chamadas seguintes são "
                   "rejeitadas pelo próprio serviço de pedidos, <strong>sem esperar o timeout de rede</strong>. "
                   "Isso libera recursos para consultas de pedidos existentes — exatamente o isolamento que "
                   "faltou no incidente original.")),
    slide(4, "Conteúdo", "Bulkhead: compartimentar os recursos",
          p("O anteparo aplica o isolamento de forma estrutural: conexões, threads e filas são particionadas "
            "<strong>por dependência ou por criticidade</strong>.") + "\n" +
          ul([
              "<strong>Compartimento do pagamento</strong> — conjunto de conexões exclusivo para chamadas ao provedor.",
              "<strong>Compartimento das consultas</strong> — conjunto separado, imune ao esgotamento do primeiro.",
              "<strong>Efeito</strong> — a lentidão do pagamento esgota apenas o próprio compartimento.",
              "<strong>A metáfora</strong> — anteparos de um navio: ele continua flutuando mesmo com um compartimento alagado.",
          ]), visual="map"),
    slide(4, "Conteúdo", "Degradação graciosa",
          ul([
              "<strong>O que é</strong> — continuar oferecendo uma versão reduzida do serviço quando uma dependência não essencial falha.",
              "<strong>Exemplo</strong> — o checkout omite as recomendações de produto e prossegue com a compra.",
              "<strong>A alternativa ruim</strong> — bloquear o cliente porque um componente acessório está fora.",
              "<strong>Pré-requisito</strong> — classificar de antemão quais dependências são essenciais e quais são acessórias.",
              "<strong>Não é só engenharia</strong> — essa classificação é uma decisão de produto tanto quanto técnica.",
              "<strong>Complementaridade</strong> — disjuntor detecta e corta; anteparo contém; degradação graciosa mantém o serviço de pé.",
          ]), visual="map"),
    slide(4, "Conteúdo", "Objetivos de confiabilidade",
          p("Detectores, isolamento, disjuntores, anteparos e degradação graciosa servem a um objetivo "
            "<strong>mensurável</strong>, não a uma aspiração vaga de “o sistema não pode cair”.") + "\n" +
          tabela(["Objetivo declarado", "Orçamento mensal de indisponibilidade", "Leitura prática"], [
              ["99% no fluxo de pedidos", "≈ 7 h 12 min", "Aceitável para operações internas de baixo impacto"],
              ["99,9% no fluxo de pedidos", "≈ 43 min", "Alvo típico de um fluxo de receita direta"],
              ["99,99% no fluxo de pedidos", "≈ 4 min 19 s", "Exige zonas independentes e ensaio recorrente de falhas"],
          ]) + "\n" +
          destaque("Um objetivo explícito estabelece um <strong>orçamento de indisponibilidade tolerável</strong> "
                   "e permite decidir quando investir mais e quando o nível já é suficiente. Resiliência sem "
                   "objetivo declarado vira investimento sem critério de parada.")),
    slide(4, "Transição", "O que a Unidade 2 vai perguntar",
          p("Esta unidade tratou de comunicação, ordenação e falhas em processos individuais. Um fio comum "
            "atravessa as quatro aulas: componentes autônomos, conectados por rede imperfeita, "
            "<strong>discordam temporariamente</strong> sobre o estado — e o projeto precisa prever isso em "
            "vez de negá-lo. A Unidade 2 desloca a mesma pergunta para os dados:") + "\n" +
          ul([
              "Como manter <strong>réplicas</strong> de um mesmo dado consistentes entre si?",
              "Como o sistema deve se comportar durante uma <strong>partição de rede</strong>, sem violar suas garantias mais importantes?",
              "Que mecanismos garantem <strong>acordo</strong> quando múltiplos nós precisam concordar sobre um único fato?",
              "Como sustentar <strong>transações</strong> que atravessam serviços, com sagas e idempotência?",
          ]), visual="map"),
    pontos_chave(4, [
        ("Quatro modelos", "Parada, omissão, temporização e comportamento arbitrário; a maioria dos incidentes cotidianos é das três primeiras."),
        ("Detector estima", "Falsos positivos e falsos negativos são inevitáveis: o desenho deve conviver com a incerteza, não presumir certeza."),
        ("Partição não é queda", "Os dois lados continuam vivos e isolados; aceitar escrita em ambos gera split-brain e divergência de estado."),
        ("Isolar, não só duplicar", "Redundância sem isolamento não impede que a degradação de uma dependência atinja partes não relacionadas."),
        ("Padrões complementares", "Circuit breaker corta o desperdício, bulkhead compartimenta recursos e degradação graciosa preserva o essencial."),
        ("Objetivo declarado", "Resiliência se mede contra um alvo explícito de disponibilidade, com orçamento de indisponibilidade conhecido."),
    ]),
    slide(4, "Atividade prática", "Mãos à obra: análise de modos de falha",
          p("Analise o fluxo de criação de pedidos (pedidos → estoque → pagamento → expedição) e apresente o "
            "resultado em uma tabela: etapa, modo de falha, efeito sem proteção, proteção proposta.") + "\n" +
          ul([
              "<strong>1.</strong> Para cada uma das quatro etapas, liste ao menos um modo de falha plausível.",
              "<strong>2.</strong> Descreva o efeito observável pelas etapas vizinhas se nenhuma proteção for aplicada.",
              "<strong>3.</strong> Proponha ao menos uma proteção: timeout ajustado, circuit breaker, bulkhead ou degradação graciosa.",
              "<strong>4.</strong> Identifique qual etapa deveria acionar degradação graciosa e qual deveria interromper o fluxo.",
              "<strong>5.</strong> Justifique a diferença com base na criticidade de negócio, não na facilidade técnica.",
              "<strong>6.</strong> Estime, para uma das etapas, um objetivo de disponibilidade e o orçamento correspondente em minutos por mês.",
          ]), visual="map"),
    encerramento(
        "Você fecha a Unidade 1 com vocabulário para nomear modos de falha e padrões para conter a propagação "
        "de uma degradação. A Unidade 2 leva essas mesmas perguntas para os dados: replicação, consistência, "
        "particionamento, CAP, consenso e transações distribuídas.",
        "Próxima unidade: Unidade 2 — Replicação, consistência, consenso e transações."),
])
