"""Conteúdo dos decks da Unidade 3 — Serviços, eventos e plataformas cloud-native."""

from slides_kit import (
    audiodescricao, capa, citacao, codigo, destaque, encerramento, formula,
    montar, numeros, p, pontos_chave, slide, sumario, tabela, ul,
)

SUB = "Unidade 3 — Serviços, eventos e plataformas cloud-native"

# ---------------------------------------------------------------- Aula 9

A9 = montar([
    capa(9, "Decomposição em serviços e limites de domínio", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um mapa de contextos "
        "delimitados da NexaOrder mostrando que “item” muda de significado entre catálogo e estoque; um "
        "painel numérico com o cálculo da instabilidade do serviço de estoque; um quadro comparando "
        "banco de dados compartilhado e dados por serviço; um fluxo de composição via API Gateway; e um "
        "checklist com seis sintomas de monólito distribuído."
    ),
    sumario("Decomposição em serviços e limites de domínio", [
        "Monólito, monólito modular e microsserviços",
        "Coesão, acoplamento e a métrica de instabilidade",
        "Contexto delimitado e capacidade de negócio",
        "O princípio de dados por serviço",
        "API Gateway e composição de respostas",
        "Comunicação conversacional como sintoma",
        "Os seis sinais do monólito distribuído",
        "Do diagnóstico à decisão de fronteira",
    ]),
    slide(9, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Comparar</strong> monólito, monólito modular e microsserviços sem tratá-los como escala de qualidade.",
              "<strong>Aplicar</strong> coesão e acoplamento como critérios explícitos de desenho de fronteira.",
              "<strong>Calcular</strong> a instabilidade de um serviço a partir de suas dependências aferentes e eferentes.",
              "<strong>Identificar</strong> contextos delimitados a partir de termos que mudam de significado.",
              "<strong>Diagnosticar</strong> um monólito distribuído pelos seus sintomas operacionais.",
              "<strong>Registrar</strong> uma decisão de fronteira com requisito, decisão, compromisso e evidência.",
          ]), visual="map"),
    slide(9, "Situação-problema", "Dividir não é o mesmo que desacoplar",
          p("A NexaOrder já opera com quatro serviços aparentemente independentes. Ainda assim, a equipe "
            "convive com sintomas incômodos:") + "\n" +
          ul([
              "Alterar o formato do pedido <strong>exige mudar o estoque junto</strong> — os dois compartilham a mesma tabela de itens.",
              "Liberar pagamento sem atualizar pedidos <strong>no mesmo dia quebra o checkout</strong>.",
              "Qualquer incidente exige <strong>praticamente todo o time</strong> disponível.",
              "A separação foi feita por conveniência técnica, <strong>não por limites de negócio</strong>.",
          ]) + "\n" +
          destaque("O resultado é um <strong>monólito distribuído</strong>: paga-se o custo operacional da "
                   "distribuição — rede, serialização, falhas parciais — sem colher o benefício principal, que é "
                   "a autonomia de evolução e implantação."),
          visual="compare"),
    slide(9, "Conteúdo", "Três formas de organizar um sistema",
          tabela(["Forma", "Unidade de implantação", "Dados", "Quando faz sentido"], [
              ["<strong>Monólito</strong>", "Uma única unidade executável", "Banco geralmente compartilhado", "Times pequenos, domínio ainda em descoberta"],
              ["<strong>Monólito modular</strong>", "Uma única unidade, com fronteiras internas rígidas", "Esquemas segregados dentro do mesmo banco", "Arquitetura legítima, não apenas etapa de transição"],
              ["<strong>Microsserviços</strong>", "Cada serviço implanta e escala de forma independente", "Armazenamento próprio por serviço", "Escala e autonomia organizacional justificam o custo operacional"],
          ]) + "\n" +
          destaque("Nenhuma é universalmente superior. Um monólito modular bem projetado pode ser "
                   "<strong>mais barato de operar</strong> do que dezenas de microsserviços mal delimitados — "
                   "o mesmo raciocínio de custo, benefício e evidência da Aula 1.")),
    slide(9, "Conteúdo", "Coesão, acoplamento e autonomia",
          ul([
              "<strong>Coesão</strong> — o grau em que os elementos internos de um componente se relacionam e <em>mudam juntos</em>.",
              "<strong>Acoplamento</strong> — o grau em que um componente depende de <em>detalhes internos</em> de outro.",
              "<strong>O bom limite</strong> — maximiza coesão interna e minimiza acoplamento externo.",
              "<strong>Autonomia é a consequência</strong> — se a fronteira estiver certa, o time implanta sem coordenar com os outros.",
          ]) + "\n" +
          destaque("Fronteira não é uma questão de gosto: ela se manifesta em <strong>quantas implantações "
                   "precisam ser coordenadas</strong> e em quantas pessoas precisam estar presentes num incidente."),
          visual="map"),
    slide(9, "Exemplo numérico", "Instabilidade: transformando acoplamento em número",
          p("Um heurístico de Robert C. Martin, adaptável com cautela ao nível de serviços. Sejam "
            "<strong>C<sub>a</sub></strong> o acoplamento aferente (quantos dependem deste) e "
            "<strong>C<sub>e</sub></strong> o eferente (de quantos este depende):") + "\n" +
          formula("I = C<sub>e</sub> ÷ ( C<sub>a</sub> + C<sub>e</sub> )") + "\n" +
          numeros([
              ("3", "consumidores do estoque (Cₐ)"),
              ("1", "dependência do estoque (Cₑ)"),
              ("0,25", "instabilidade resultante"),
              ("0 → 1", "estável → instável"),
          ]) + "\n" +
          destaque("Valor baixo indica serviço <strong>estável</strong>: muito pressionado por consumidores e "
                   "pouco dependente de outros. Instabilidade alta indica menos pressão externa, porém maior "
                   "sujeição a mudanças nas dependências. A métrica <strong>não substitui julgamento de "
                   "negócio nem mede criticidade</strong> — apenas torna parte do acoplamento discutível.")),
    slide(9, "Conteúdo", "Contexto delimitado e capacidade de negócio",
          p("O <em>Domain-Driven Design</em> oferece dois conceitos para desenhar fronteiras:") + "\n" +
          ul([
              "<strong>Contexto delimitado</strong> — a fronteira dentro da qual um modelo de domínio e sua linguagem têm significado consistente.",
              "<strong>Capacidade de negócio</strong> — algo que a organização faz para gerar valor, como “gerenciar estoque”, independentemente de como é implementado.",
              "<strong>Para o catálogo</strong>, “item” é uma descrição comercial: preço, imagens, categorias.",
              "<strong>Para o estoque</strong>, o mesmo “item” é quantidade física em um depósito, com número de série e localização.",
          ]) + "\n" +
          destaque("Tratar essas duas visões como o <strong>mesmo modelo de dados compartilhado</strong> é uma "
                   "fonte comum de acoplamento acidental: uma mudança no significado de “item” para o catálogo "
                   "pode quebrar silenciosamente o controle de estoque."),
          visual="compare"),
    slide(9, "Conteúdo", "Dados por serviço",
          p("Consequência direta de contextos bem definidos: <strong>cada serviço possui e controla seu "
            "próprio armazenamento</strong>, e nenhum outro serviço o acessa diretamente — nem por leitura.") + "\n" +
          ul([
              "<strong>Toda interação passa por contrato explícito</strong> — uma API, uma mensagem ou um evento publicado.",
              "<strong>O custo aparente</strong> — perde-se a conveniência de um <code>JOIN</code> entre tabelas de serviços diferentes.",
              "<strong>O custo é deliberado</strong> — sem ele, qualquer alteração de esquema quebra quem lê a tabela diretamente.",
              "<strong>Sem ele, a fronteira não existe</strong> — mesmo que exista um repositório de código separado.",
          ]) + "\n" +
          destaque("Foi exatamente esse o erro da NexaOrder: permitir que <strong>pedidos e pagamento lessem a "
                   "mesma tabela de itens do estoque</strong>."),
          visual="map"),
    citacao(
        "“A divisão física em repositórios ou processos não produz, por si só, autonomia real.”",
        "— síntese da Aula 9"),
    slide(9, "Conteúdo", "API Gateway e composição",
          p("Expor todos os serviços diretamente acopla a topologia interna aos consumidores externos e "
            "multiplica autenticação e limitação de taxa em cada serviço. O gateway concentra o ponto de "
            "entrada:") + "\n" +
          ul([
              "<strong>Rotear</strong> a requisição para o serviço correto.",
              "<strong>Compor</strong> respostas de múltiplos serviços em uma única resposta.",
              "<strong>Aplicar</strong> autenticação e limitação de taxa em um só lugar.",
              "<strong>Ocultar</strong> a decomposição interna dos consumidores externos.",
          ]) + "\n" +
          destaque("A tela de detalhes do pedido precisa de dados de pedidos, estoque e expedição: o gateway "
                   "consulta os três e devolve uma resposta única. Mas ele <strong>não deve acumular regras de "
                   "negócio</strong> — quando isso acontece, vira um novo monólito escondido atrás de uma "
                   "fachada de microsserviços."),
          visual="flow"),
    slide(9, "Conteúdo", "Comunicação entre serviços e o sintoma conversacional",
          ul([
              "<strong>Síncrona (HTTP, RPC)</strong> — simplicidade e resposta imediata, mas propaga indisponibilidade pela cadeia.",
              "<strong>Assíncrona (eventos)</strong> — reduz o acoplamento temporal, ao custo de raciocínio mais complexo sobre consistência.",
              "<strong>Comunicação conversacional</strong> — um único caso de uso dispara dezenas de chamadas remotas entre serviços.",
              "<strong>O que ela revela</strong> — a fronteira foi traçada no lugar errado: responsabilidades fortemente relacionadas foram separadas sem necessidade.",
          ]) + "\n" +
          destaque("Contar <strong>quantas chamadas remotas</strong> um caso de uso exige é um dos diagnósticos "
                   "mais baratos e mais reveladores de fronteira mal desenhada."),
          visual="compare"),
    slide(9, "Diagnóstico", "Seis sinais de monólito distribuído",
          ul([
              "<strong>1.</strong> Implantações de serviços diferentes precisam ser coordenadas no mesmo horário.",
              "<strong>2.</strong> Qualquer mudança de esquema em um serviço quebra outros serviços.",
              "<strong>3.</strong> Um incidente em um serviço exige presença de praticamente todo o time.",
              "<strong>4.</strong> Serviços compartilham tabelas, filas ou segredos sem contrato explícito.",
              "<strong>5.</strong> A topologia de chamadas de um único caso de uso é profunda e conversacional.",
              "<strong>6.</strong> Times não conseguem testar ou implantar sem depender de outros no mesmo instante.",
          ]) + "\n" +
          destaque("Nenhum sintoma isolado é definitivo. <strong>Vários ao mesmo tempo</strong> indicam que a "
                   "divisão física não produziu autonomia — use a lista como roteiro de autodiagnóstico em uma "
                   "retrospectiva de arquitetura."),
          visual="map"),
    slide(9, "Conteúdo", "Do diagnóstico à decisão de fronteira",
          p("Como na Aula 1, a decisão precisa explicitar quatro elementos. Para a NexaOrder:") + "\n" +
          ul([
              "<strong>Requisito</strong> — eliminar a necessidade de coordenar implantações entre pedidos e estoque.",
              "<strong>Decisão</strong> — separar “item de catálogo” de “unidade em estoque”, com armazenamento próprio e comunicação por eventos de reserva e liberação.",
              "<strong>Compromisso</strong> — consultas que hoje usam <code>JOIN</code> local passam a exigir composição ou réplicas de leitura assíncronas, com atraso de propagação.",
              "<strong>Evidência</strong> — número de implantações que exigiram coordenação simultânea, antes e depois, medido ao longo de um trimestre.",
          ]), visual="cycle"),
    pontos_chave(9, [
        ("Três opções válidas", "Monólito, monólito modular e microsserviços são escolhas arquiteturais; a decisão depende de requisitos, não de tendência."),
        ("Coesão dentro, acoplamento fora", "Um bom limite agrupa o que muda junto e isola o que não deveria mudar junto."),
        ("Termos revelam fronteiras", "Onde um mesmo termo muda de significado, provavelmente há dois contextos delimitados diferentes."),
        ("Dados por serviço", "Acesso direto ao armazenamento alheio anula a fronteira, mesmo com repositórios separados."),
        ("Gateway sem negócio", "Ele concentra composição e políticas transversais — regras de domínio ali criam um monólito escondido."),
        ("Sintomas se somam", "Implantações coordenadas e chamadas conversacionais são evidências práticas de fronteira mal traçada."),
    ]),
    slide(9, "Atividade prática", "Mãos à obra: definir os limites de serviço",
          p("Entregue um diagrama e uma tabela de justificativas que permita a outra pessoa compreender a "
            "fronteira proposta <strong>sem explicação verbal adicional</strong>.") + "\n" +
          ul([
              "<strong>1.</strong> Liste as capacidades de negócio da NexaOrder, incluindo as que julgar necessárias.",
              "<strong>2.</strong> Identifique o contexto delimitado de cada capacidade.",
              "<strong>3.</strong> Registre onde o significado de um termo comum muda entre contextos.",
              "<strong>4.</strong> Proponha a divisão resultante, indicando qual serviço possui qual armazenamento.",
              "<strong>5.</strong> Calcule a instabilidade aproximada de dois serviços da sua proposta.",
              "<strong>6.</strong> Liste três sintomas que a nova divisão elimina e <em>um novo risco</em> que ela introduz.",
          ]), visual="map"),
    encerramento(
        "Você já sabe desenhar fronteiras que desacoplam times, dados e ciclos de implantação — e "
        "diagnosticar quando isso não aconteceu. Na próxima aula, substituímos a cadeia de chamadas "
        "síncronas por uma arquitetura orientada a eventos.",
        "Próxima aula: Aula 10 — Arquitetura orientada a eventos."),
])

# ---------------------------------------------------------------- Aula 10

A10 = montar([
    capa(10, "Arquitetura orientada a eventos", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um quadro distinguindo "
        "comando, evento de domínio e notificação; um diagrama de um tópico com oito partições "
        "distribuídas entre um grupo de consumidores; um painel numérico com o cálculo do número mínimo "
        "de partições para 1200 eventos por segundo; três linhas do tempo comparando as semânticas "
        "at-most-once, at-least-once e exactly-once; e uma sequência do fluxo de eventos do pedido na "
        "NexaOrder."
    ),
    sumario("Arquitetura orientada a eventos", [
        "Comando, evento de domínio e notificação",
        "Produtores, consumidores, tópicos e partições",
        "Ordenação garantida dentro da partição",
        "Grupos de consumidores e paralelismo",
        "Retenção e reprocessamento",
        "At-most-once, at-least-once e exactly-once",
        "Evolução de esquemas e compatibilidade",
        "O ciclo do pedido reorganizado por eventos",
    ]),
    slide(10, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Distinguir</strong> comando, evento de domínio e notificação pelo acoplamento que cada um cria.",
              "<strong>Escolher</strong> a chave de particionamento que preserva a ordem necessária ao negócio.",
              "<strong>Dimensionar</strong> o número mínimo de partições a partir da taxa de pico e da capacidade do consumidor.",
              "<strong>Explicar</strong> o que acontece com a carga quando um grupo de consumidores rebalanceia.",
              "<strong>Comparar</strong> as três semânticas de entrega quanto a perda e duplicação.",
              "<strong>Evoluir</strong> esquemas de evento preservando compatibilidade retroativa e prospectiva.",
          ]), visual="map"),
    slide(10, "Situação-problema", "Quando a cadeia de chamadas síncronas quebra tudo",
          p("Com fronteiras mais claras, um problema persiste: o checkout chama pedidos, que chama "
            "<em>de forma síncrona</em> estoque, que chama pagamento, que chama expedição.") + "\n" +
          ul([
              "Se qualquer serviço estiver lento, <strong>a cadeia inteira fica lenta</strong>.",
              "Se qualquer um estiver indisponível, <strong>o pedido falha por completo</strong>.",
              "Isso vale mesmo quando a etapa afetada <strong>não é urgente</strong>, como a notificação de expedição.",
              "A saída: reorganizar a comunicação em torno de <strong>fatos que já aconteceram</strong>.",
          ]) + "\n" +
          destaque("Eventos permitem que outros serviços observem e reajam <strong>no próprio ritmo</strong>, "
                   "sem bloquear quem os publicou."),
          visual="timeline"),
    slide(10, "Conteúdo", "Comando, evento de domínio e notificação",
          tabela(["Tipo", "O que expressa", "Destinatário", "Acoplamento"], [
              ["<strong>Comando</strong>", "Uma solicitação para que algo aconteça", "Específico; pode aceitar ou recusar", "Direto: quem envia sabe quem recebe e espera aceitação"],
              ["<strong>Evento de domínio</strong>", "O registro de um fato que já ocorreu", "Nenhum em particular", "Baixo: quem publica não sabe, nem precisa saber, quem consome"],
              ["<strong>Notificação</strong>", "Aviso leve de que algo aconteceu", "Interessados", "Baixo; sem dados completos, convida a buscar mais informação"],
          ]) + "\n" +
          destaque("A NexaOrder passa a tratar <code>pedido criado</code>, <code>estoque reservado</code>, "
                   "<code>pagamento aprovado</code> e <code>pedido expedido</code> como <strong>eventos de "
                   "domínio</strong> publicados por seus respectivos serviços.")),
    slide(10, "Conteúdo", "Tópicos, partições e deslocamento",
          ul([
              "<strong>Tópico</strong> — canal nomeado por tipo de evento ou por agregado de negócio.",
              "<strong>Produtores</strong> publicam eventos em um tópico; <strong>consumidores</strong> leem sem remover a mensagem para os demais.",
              "<strong>Vários serviços</strong> processam o mesmo evento de forma independente — diferente de uma fila tradicional.",
              "<strong>Partição</strong> — sequência ordenada e imutável de eventos, identificada por um deslocamento (<em>offset</em>) crescente.",
              "<strong>Chave</strong> — determina a partição de destino; normalmente o identificador do agregado, como o número do pedido.",
              "<strong>Efeito da chave</strong> — todos os eventos daquele pedido caem na mesma partição.",
          ]), visual="map"),
    slide(10, "Conteúdo", "Ordenação: uma garantia por partição",
          p("A plataforma garante ordem <strong>dentro</strong> de uma partição, <strong>não entre</strong> "
            "partições diferentes.") + "\n" +
          ul([
              "<strong>Com chave estável</strong> — os eventos do pedido 4021 chegam na mesma partição e são lidos na ordem publicada: criado → reservado → aprovado → expedido.",
              "<strong>Entre pedidos diferentes</strong> — a ordem relativa pode variar, e isso geralmente não é problema: são agregados distintos.",
              "<strong>Chave errada quebra tudo</strong> — particionar por <em>tipo de evento</em> espalha eventos do mesmo pedido entre partições.",
              "<strong>Consequência</strong> — o consumidor observaria “pagamento aprovado” antes de “pedido criado”.",
          ]), visual="timeline"),
    slide(10, "Conteúdo", "Grupos de consumidores",
          p("Um <strong>grupo de consumidores</strong> é um conjunto de instâncias que divide entre si as "
            "partições de um tópico — cada partição atribuída a <em>exatamente uma</em> instância do grupo "
            "por vez.") + "\n" +
          ul([
              "<strong>Escala horizontal</strong> — tópico com 6 partições e grupo de 3 consumidores: cada instância processa ~2 partições.",
              "<strong>Grupos são independentes</strong> — o painel operacional e o disparo de e-mails leem o mesmo tópico, cada um no seu ritmo.",
              "<strong>Rebalanceamento</strong> — se uma instância falha, suas partições são redistribuídas entre as remanescentes.",
              "<strong>O custo do rebalanceamento</strong> — 3 instâncias para 8 partições viram 2 instâncias para 8: a carga por instância sobe e a capacidade total pode cair até uma nova réplica entrar.",
          ]), visual="map"),
    slide(10, "Exemplo numérico", "Quantas partições sustentam o pico?",
          formula("P = ⌈ λ<sub>pico</sub> ÷ C<sub>consumidor</sub> ⌉") + "\n" +
          numeros([
              ("1200", "eventos/s no pico (λ)"),
              ("150", "eventos/s por consumidor (C)"),
              ("8", "partições mínimas"),
              ("8", "teto de paralelismo útil"),
          ]) + "\n" +
          destaque("Adicionar um <strong>nono consumidor</strong> ao grupo não aumentaria o throughput: não "
                   "haveria uma nona partição para atribuir a ele, e a instância ficaria ociosa. O número de "
                   "partições é um <strong>limite estrutural de paralelismo</strong> e deve ser definido com "
                   "folga em relação à carga de pico esperada.")),
    citacao(
        "“Quem publica um evento não sabe, e não precisa saber, quem o consome.”",
        "— síntese da Aula 10"),
    slide(10, "Conteúdo", "Retenção e reprocessamento",
          p("Diferente de uma fila, em que a mensagem some após o consumo, a plataforma de eventos "
            "<strong>retém</strong> mensagens por um período configurável, independentemente de terem sido "
            "lidas. Isso viabiliza o reprocessamento.") + "\n" +
          tabela(["Retenção", "O que permite", "O que custa"], [
              ["Poucas horas", "Recuperação de falhas imediatas", "Praticamente elimina a correção retroativa"],
              ["Sete dias", "Corrigir na segunda-feira um defeito reprocessando a semana anterior", "Armazenamento moderado"],
              ["Indefinida", "Registro histórico completo, útil para auditoria", "Custo de armazenamento crescente no tempo"],
          ]) + "\n" +
          destaque("O log de eventos só pode ser tratado como <strong>fonte de verdade</strong> quando foi "
                   "deliberadamente projetado para isso: retenção suficiente, eventos completos e imutáveis, "
                   "versionamento e garantias de durabilidade. Retenção não é “quanto mais, melhor”.")),
    slide(10, "Conteúdo", "Três semânticas de entrega",
          tabela(["Semântica", "Comportamento", "Quando ocorre"], [
              ["<strong>At-most-once</strong>", "Zero ou uma entrega: nunca duplica, mas pode perder", "O consumidor confirma o recebimento antes de concluir o processamento"],
              ["<strong>At-least-once</strong>", "Uma ou mais entregas: duplicação é possível e esperada", "Publicação durável, retenção vigente e retries disponíveis"],
              ["<strong>Exactly-once</strong>", "Um efeito observável por evento, dentro de uma fronteira declarada", "Combina at-least-once com deduplicação ou idempotência no consumidor"],
          ]) + "\n" +
          destaque("O “exactly-once” <strong>não elimina duplicações na transmissão</strong> e não se estende "
                   "automaticamente a efeitos fora da fronteira transacional. Ao chamar um provedor de pagamento, "
                   "é preciso idempotência ponta a ponta ou reconciliação explícita do resultado.")),
    slide(10, "Conteúdo", "Evolução de esquemas e compatibilidade",
          p("Eventos publicados hoje podem ser lidos por serviços implantados semanas depois — e um "
            "consumidor antigo pode continuar em produção enquanto o produtor já publica um formato novo.") + "\n" +
          ul([
              "<strong>Retroativa (backward)</strong> — o consumidor <em>novo</em> lê eventos publicados no esquema antigo.",
              "<strong>Prospectiva (forward)</strong> — o consumidor <em>antigo</em> lê eventos do esquema novo, ignorando campos desconhecidos.",
              "<strong>Mudança segura</strong> — aditiva: adicionar <code>canal_venda</code> como campo opcional não quebra ninguém.",
              "<strong>Mudança perigosa</strong> — renomear <code>valor_total</code> para <code>valor_liquido</code> sem transição quebra a compatibilidade.",
          ]) + "\n" +
          destaque("Remover, renomear ou mudar o tipo de um campo exige <strong>estratégia explícita de "
                   "migração</strong> — por exemplo, publicar temporariamente nos dois formatos."),
          visual="compare"),
    slide(10, "Conteúdo", "O ciclo do pedido reorganizado",
          p("Reunindo os elementos da aula, nenhum serviço chama o seguinte de forma síncrona e bloqueante — "
            "cada um <strong>reage a fatos publicados</strong> no seu próprio ritmo:") + "\n" +
          ul([
              "<strong>Pedidos</strong> recebe um comando síncrono do cliente, valida e publica <code>pedido criado</code>.",
              "<strong>Estoque</strong> consome, tenta reservar e publica <code>estoque reservado</code> ou <code>estoque indisponível</code>.",
              "<strong>Pagamento</strong> consome <code>estoque reservado</code> e publica <code>pagamento aprovado</code> ou <code>recusado</code>.",
              "<strong>Expedição</strong> consome <code>pagamento aprovado</code> e publica <code>pedido expedido</code>.",
          ]), visual="flow"),
    pontos_chave(10, [
        ("Três tipos de mensagem", "Comando acopla ao destinatário; evento de domínio registra um fato sem destinatário; notificação apenas avisa."),
        ("A ordem é por partição", "Só existe garantia de ordem dentro de uma partição — a chave decide o que permanece ordenado."),
        ("Partições limitam a escala", "O paralelismo útil de um grupo de consumidores nunca ultrapassa o número de partições do tópico."),
        ("Retenção habilita correção", "Reter eventos permite reprocessar e reconstruir estado — com custo de armazenamento proporcional."),
        ("Duplicata é o normal", "At-least-once é a configuração comum; o efeito único é responsabilidade do desenho do consumidor."),
        ("Esquema evolui aditivamente", "Campos opcionais preservam compatibilidade; remover ou renomear exige migração explícita."),
    ]),
    slide(10, "Atividade prática", "Mãos à obra: tópicos, chaves e grupos",
          p("Desenhe os tópicos, chaves e grupos de consumidores para o ciclo de vida do pedido.") + "\n" +
          ul([
              "<strong>1.</strong> Liste no mínimo quatro eventos de domínio do ciclo do pedido.",
              "<strong>2.</strong> Defina, para cada um, o tópico e a chave de particionamento.",
              "<strong>3.</strong> Justifique a escolha da chave em termos da ordenação necessária.",
              "<strong>4.</strong> Defina dois grupos de consumidores distintos lendo o mesmo tópico com finalidades diferentes.",
              "<strong>5.</strong> Calcule o número mínimo de partições para uma taxa de pico hipotética.",
              "<strong>6.</strong> Indique a semântica de entrega que cada consumidor deveria adotar, e por quê.",
          ]), visual="map"),
    encerramento(
        "Você já sabe desacoplar o ciclo do pedido com eventos, chaves e grupos de consumidores — e "
        "dimensionar o paralelismo que isso permite. Na próxima aula, descemos para a camada de execução: "
        "quem garante que essas instâncias continuem existindo?",
        "Próxima aula: Aula 11 — Contêineres, Kubernetes e reconciliação."),
])

# ---------------------------------------------------------------- Aula 11

A11 = montar([
    capa(11, "Contêineres, Kubernetes e reconciliação", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um manifesto YAML de "
        "Deployment com quatro réplicas do serviço de pagamento; um ciclo com as três etapas do laço de "
        "reconciliação — observar, comparar e agir; uma tabela das sondas de vivacidade, prontidão e "
        "inicialização; um painel numérico com o cálculo do escalonamento automático de quatro para seis "
        "réplicas; e uma sequência de atualização gradual mantendo a capacidade saudável."
    ),
    sumario("Contêineres, Kubernetes e reconciliação", [
        "Imagem, contêiner e imutabilidade",
        "Cluster, nó, Pod, Deployment e Service",
        "Estado desejado e estado observado",
        "Controladores e o laço de reconciliação",
        "Sondas: vivacidade, prontidão e inicialização",
        "Descoberta, balanceamento e configuração",
        "Escalonamento automático horizontal",
        "Atualizações graduais sem perder capacidade",
    ]),
    slide(11, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Explicar</strong> o que a imutabilidade de imagens garante — e o que ela não garante.",
              "<strong>Distinguir</strong> os papéis de Pod, Deployment e Service em uma mesma aplicação.",
              "<strong>Descrever</strong> o laço de reconciliação entre estado desejado e estado observado.",
              "<strong>Diferenciar</strong> sonda de vivacidade de sonda de prontidão pelo efeito de cada falha.",
              "<strong>Calcular</strong> o número de réplicas resultante de um escalonamento automático horizontal.",
              "<strong>Reconhecer</strong> quando a recuperação automática está mascarando um defeito determinístico.",
          ]), visual="map"),
    slide(11, "Situação-problema", "A instância que se recupera sozinha (e a que não deveria)",
          p("Em uma madrugada de alta demanda, uma instância do serviço de pagamento trava e para de "
            "responder. Minutos depois, <strong>sem intervenção humana</strong>, uma nova instância aparece, "
            "assume o tráfego e o incidente quase passa despercebido.") + "\n" +
          ul([
              "<strong>Quem decidiu</strong> recriar a instância?",
              "<strong>Como o sistema sabia</strong> que ela deveria existir?",
              "E se a causa do travamento for um defeito que <strong>volta a acontecer a cada reinício</strong>?",
              "A recuperação não é mágica: é um <strong>laço de reconciliação</strong> rodando continuamente.",
          ]) + "\n" +
          destaque("Compreender esse laço é o que permite diferenciar uma <strong>recuperação saudável</strong> "
                   "de um <strong>sintoma que está sendo mascarado</strong>."),
          visual="timeline"),
    slide(11, "Conteúdo", "Imagem, contêiner e imutabilidade",
          ul([
              "<strong>Imagem</strong> — pacote autocontido com código, dependências e instruções de execução, construído em camadas imutáveis.",
              "<strong>Contêiner</strong> — instância em execução dessa imagem, isolada em processos, sistema de arquivos e, em geral, rede.",
              "<strong>Diferença para VM</strong> — o contêiner compartilha o núcleo do sistema operacional do hospedeiro.",
              "<strong>Imutabilidade</strong> — em vez de corrigir uma instância em execução, publica-se nova imagem e substituem-se os contêineres.",
          ]) + "\n" +
          destaque("A imutabilidade reduz a divergência do <strong>artefato de aplicação</strong> entre "
                   "ambientes. Ela <strong>não elimina</strong> diferenças de configuração, infraestrutura, "
                   "dados, arquitetura do host ou serviços externos — essas variáveis continuam exigindo "
                   "controle e teste."),
          visual="map"),
    slide(11, "Conteúdo", "Os objetos centrais do Kubernetes",
          tabela(["Objeto", "O que é", "Na NexaOrder"], [
              ["<strong>Cluster</strong>", "Conjunto de máquinas gerenciadas como uma unidade", "O ambiente inteiro da plataforma"],
              ["<strong>Nó</strong>", "Máquina física ou virtual que executa contêineres", "Cada servidor do cluster"],
              ["<strong>Pod</strong>", "Menor unidade implantável; contêineres que compartilham rede e armazenamento local", "Uma instância do serviço de pagamento"],
              ["<strong>Deployment</strong>", "Declara quantas réplicas devem existir e como atualizar", "Quatro réplicas de pagamento"],
              ["<strong>Service</strong>", "Expõe um conjunto de Pods sob endereço de rede estável", "O endereço que estoque usa para alcançar pagamento"],
          ])),
    slide(11, "Conteúdo", "Estado desejado e estado observado",
          p("O usuário <strong>não instrui passo a passo</strong>: declara o resultado e delega ao "
            "sistema alcançá-lo e mantê-lo.") + "\n" +
          codigo("""apiVersion: apps/v1
kind: Deployment
metadata:
  name: pagamento
spec:
  replicas: 4
  selector:
    matchLabels: { app: pagamento }
  template:
    metadata:
      labels: { app: pagamento }
    spec:
      containers:
        - name: pagamento
          image: nexaorder/pagamento:1.7.0""", "Estado desejado declarado em manifesto") + "\n" +
          destaque("Restando <strong>três dos quatro</strong> Pods, há divergência entre o desejado e o "
                   "observado — e é ela que aciona a reconciliação.")),
    slide(11, "Conteúdo", "Controladores e o laço de reconciliação",
          p("Um <strong>controlador</strong> observa o estado atual, compara com o desejado e age para "
            "reduzir a diferença. O laço <strong>não roda uma vez</strong>: roda indefinidamente, em ciclos "
            "curtos.") + "\n" +
          ul([
              "<strong>1. Observar</strong> — qual é a condição real do cluster neste momento?",
              "<strong>2. Comparar</strong> — em que ela diverge do que foi declarado?",
              "<strong>3. Agir</strong> — executar o que reduz essa diferença, e voltar ao início.",
          ]) + "\n" +
          destaque("<strong>Pod removido</strong> → o controlador vê três dos quatro e cria outro. "
                   "<strong>Processo travado em Pod vivo</strong>, com sonda de vivacidade falhando → o kubelet "
                   "reinicia o contêiner no mesmo Pod. Os dois produzem recuperação automática, mas atuam em "
                   "<strong>níveis diferentes</strong>."),
          visual="cycle"),
    slide(11, "Limite da automação", "Reconciliação restaura quantidade, não causa raiz",
          ul([
              "<strong>O que o laço restaura</strong> — a quantidade e o estado de execução declarados.",
              "<strong>O que ele não resolve</strong> — a causa raiz de uma falha recorrente.",
              "<strong>Reinício em loop</strong> — se o Pod trava por defeito de código sob certa carga, o Kubernetes o recria indefinidamente.",
              "<strong>O risco real</strong> — o problema fica mascarado justamente porque a disponibilidade parece preservada.",
          ]) + "\n" +
          destaque("Reconciliação automática é um <strong>mecanismo de disponibilidade, não uma prova de "
                   "correção</strong> — exatamente o mesmo raciocínio já aplicado a timeouts na Aula 4."),
          visual="compare"),
    slide(11, "Conteúdo", "Como o cluster percebe que algo não vai bem",
          tabela(["Sonda", "O que verifica", "Efeito quando falha"], [
              ["<strong>Vivacidade</strong> (liveness)", "Se o contêiner ainda consegue progredir", "O kubelet reinicia o contêiner, conforme a política do Pod"],
              ["<strong>Prontidão</strong> (readiness)", "Se o Pod está apto a receber tráfego", "O Pod segue executando, mas sai dos destinos prontos do Service"],
              ["<strong>Inicialização</strong> (startup)", "Se a aplicação lenta ainda está subindo", "Protege a partida sem disparar reinícios prematuros"],
          ]) + "\n" +
          destaque("Sondas devem verificar <strong>sinais úteis</strong> sem transformar uma dependência "
                   "externa instável em <strong>reinícios em cascata</strong> por todo o cluster.")),
    citacao(
        "“Reconciliação automática é um mecanismo de disponibilidade, não uma prova de correção.”",
        "— síntese da Aula 11"),
    slide(11, "Conteúdo", "Descoberta, balanceamento, configuração e dados",
          ul([
              "<strong>Pods são voláteis</strong> — recebem endereços internos que mudam a cada substituição.",
              "<strong>Service</strong> — associa nome estável e endereço fixo a Pods selecionados por rótulos, distribuindo tráfego entre os saudáveis.",
              "<strong>ConfigMaps</strong> — configuração não sensível, injetada em tempo de execução.",
              "<strong>Secrets</strong> — dados sensíveis; variáveis de ambiente não mudam no processo já iniciado e exigem reinício controlado.",
              "<strong>Volumes projetados</strong> — recebem atualização eventual, mas a aplicação precisa reler o arquivo.",
              "<strong>Armazenamento persistente</strong> — vincula um volume ao ciclo de vida da aplicação, e não ao Pod, cujo disco local é efêmero.",
          ]), visual="map"),
    slide(11, "Exemplo numérico", "Escalonamento automático horizontal",
          formula("N<sub>desejado</sub> = ⌈ N<sub>atual</sub> × ( U<sub>atual</sub> ÷ U<sub>alvo</sub> ) ⌉") + "\n" +
          numeros([
              ("4", "réplicas atuais"),
              ("85%", "CPU observada"),
              ("60%", "CPU alvo"),
              ("6", "réplicas desejadas"),
          ]) + "\n" +
          destaque("⌈4 × 85/60⌉ = ⌈5,67⌉ = <strong>6</strong>. O autoescalonador ajusta o Deployment, e o "
                   "<strong>laço de reconciliação</strong> se encarrega de criar os dois novos Pods — os dois "
                   "mecanismos operam em conjunto, cada um no seu nível.")),
    slide(11, "Exemplo numérico", "Atualização gradual sem perder capacidade",
          p("Um Deployment de <strong>6 réplicas</strong> configurado para no máximo <strong>1 "
            "indisponível</strong> e <strong>1 excedente</strong> durante a transição:") + "\n" +
          ul([
              "<strong>1.</strong> Cria 1 Pod com a versão nova — total de 7 Pods (6 antigos + 1 novo).",
              "<strong>2.</strong> Aguarda o Pod novo passar na sonda de prontidão.",
              "<strong>3.</strong> Remove 1 Pod antigo, voltando a 6 no total.",
              "<strong>4.</strong> Repete até que todas as réplicas estejam na versão nova.",
          ]) + "\n" +
          destaque("A capacidade saudável <strong>nunca cai abaixo de 5 nem ultrapassa 7</strong>. Se o Pod novo "
                   "falhar repetidamente na prontidão, o avanço trava. E atenção: o Deployment <strong>não faz "
                   "rollback automático por padrão</strong> — a equipe ou uma automação externa precisa observar "
                   "a condição de progresso e decidir pausar ou reverter."),
          visual="timeline"),
    slide(11, "Pausa para reflexão", "Robustez ou mascaramento?",
          p("O reinício em loop de um Pod é, ao mesmo tempo, prova da robustez do laço de reconciliação e "
            "risco de esconder defeitos.") + "\n" +
          ul([
              "Além de “o serviço está no ar”, que <strong>sinais</strong> revelariam que um Pod está sendo recriado repetidamente?",
              "Um Pod que trava sob alta carga e é recriado com sucesso está, <strong>do ponto de vista de negócio</strong>, resolvido?",
              "Qual a diferença entre <strong>tolerar falhas transitórias</strong> e, sem perceber, <strong>esconder um defeito determinístico</strong>?",
              "Como alertas de reinício, <code>progressDeadlineSeconds</code> e automação externa interromperiam uma implantação defeituosa?",
          ]) + "\n" +
          destaque("Note que um Deployment <strong>não oferece um número máximo de reinícios</strong>, como Jobs "
                   "oferecem com <code>backoffLimit</code> — a interrupção depende de política operacional "
                   "declarada pela equipe.")),
    pontos_chave(11, [
        ("Imutável, mas não igual", "A imagem reduz divergência do artefato; configuração, dados e dependências externas ainda variam."),
        ("Cinco objetos bastam", "Cluster, nó, Pod, Deployment e Service organizam praticamente toda a execução."),
        ("Declare o resultado", "O laço de reconciliação compara desejado e observado e age continuamente para aproximá-los."),
        ("Disponibilidade ≠ correção", "A recuperação automática restaura quantidade e execução, nunca a causa raiz do defeito."),
        ("Sondas decidem o destino", "Vivacidade reinicia o contêiner; prontidão apenas retira o Pod do tráfego."),
        ("Capacidade preservada", "Escalonamento e atualização gradual ajustam réplicas e versão sem derrubar o serviço."),
    ]),
    slide(11, "Atividade prática", "Mãos à obra: interpretar manifestos e recuperação",
          ul([
              "<strong>1.</strong> A partir do manifesto da aula, descreva o que ocorre se <em>dois Pods terminarem</em>.",
              "<strong>2.</strong> Descreva, separadamente, o que ocorre se dois Pods apenas <em>falharem na prontidão</em>, mantendo-se em execução.",
              "<strong>3.</strong> Calcule o número de réplicas de um HPA para N = 6, U<sub>atual</sub> = 92% e U<sub>alvo</sub> = 65%.",
              "<strong>4.</strong> Descreva um cenário plausível de reinício em loop para o serviço de estoque.",
              "<strong>5.</strong> Proponha um sinal de observabilidade que revelaria o problema antes de afetar clientes.",
              "<strong>6.</strong> Explique, em poucas frases, a diferença entre o papel do Deployment e o do Service nesse cenário.",
          ]), visual="map"),
    encerramento(
        "Você já sabe como o cluster mantém suas instâncias de pé — e quando essa automação está escondendo "
        "um defeito. Na última aula da unidade, tratamos do que ainda falta: garantir que apenas quem deve "
        "falar com um serviço consiga falar com ele.",
        "Próxima aula: Aula 12 — Segurança e comunicação confiável entre serviços."),
])

# ---------------------------------------------------------------- Aula 12

A12 = montar([
    capa(12, "Segurança e comunicação confiável entre serviços", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um quadro comparando "
        "comunicação interna em texto claro e comunicação protegida por TLS mútuo; um diagrama de service "
        "mesh com proxies laterais junto a cada serviço e um plano de controle central; um painel "
        "numérico do algoritmo de balde de fichas com capacidade 50 e reposição de 20 fichas por segundo; "
        "um quadro com quatro ameaças específicas de sistemas distribuídos; e uma sequência das quatro "
        "verificações de segurança em uma chamada de pedidos para pagamento."
    ),
    sumario("Segurança e comunicação confiável entre serviços", [
        "Identidade de serviço e confiança zero",
        "Autenticação, autorização e menor privilégio",
        "TLS e TLS mútuo na comunicação interna",
        "Gestão e rotação de segredos",
        "Gateway, proxy lateral e service mesh",
        "Limitação de taxa e proteção contra sobrecarga",
        "Ameaças específicas de sistemas distribuídos",
        "Um fluxo autenticado de ponta a ponta",
    ]),
    slide(12, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Contrapor</strong> segurança de perímetro e confiança zero em uma arquitetura de serviços.",
              "<strong>Separar</strong> autenticação de autorização e aplicar o princípio do menor privilégio.",
              "<strong>Explicar</strong> o que o TLS mútuo garante — e o que ele deliberadamente não garante.",
              "<strong>Justificar</strong> a gestão externa de segredos pelo tempo de resposta a um incidente.",
              "<strong>Dimensionar</strong> um limitador de taxa por balde de fichas, distinguindo pico de regime permanente.",
              "<strong>Reconhecer</strong> ameaças que exploram propriedades já estudadas de comunicação e falha.",
          ]), visual="map"),
    slide(12, "Situação-problema", "Qualquer serviço pode falar com qualquer serviço?",
          p("Uma revisão de segurança na NexaOrder revela um risco que estava à vista o tempo todo:") + "\n" +
          ul([
              "Nada impede que <strong>expedição chame pagamento e solicite um reembolso</strong>, operação nunca prevista para ela.",
              "A comunicação interna acontece <strong>em texto claro</strong> dentro do cluster.",
              "Não há verificação de identidade <strong>além do endereço de rede</strong>.",
              "As credenciais do provedor de pagamento estão <strong>em arquivo de configuração versionado</strong>.",
          ]) + "\n" +
          destaque("Confiabilidade aqui é mais ampla que disponibilidade: é confiar que a mensagem "
                   "<strong>vem de quem diz vir</strong>, que <strong>não foi alterada</strong>, que cada serviço "
                   "só faz <strong>o que lhe é explicitamente permitido</strong> e que segredos não ficam "
                   "expostos por conveniência operacional."),
          visual="compare"),
    slide(12, "Conteúdo", "Perímetro e confiança zero",
          ul([
              "<strong>Modelo de perímetro</strong> — tudo dentro da rede interna é relativamente confiável; a proteção se concentra na borda.",
              "<strong>Por que ele falha</strong> — com dezenas de serviços e múltiplos times, um único componente comprometido ganha acesso amplo.",
              "<strong>Confiança zero</strong> — nenhuma requisição é confiável apenas por vir de dentro da rede.",
              "<strong>Identidade verificável</strong> — cada serviço tem certificado ou token criptográfico associado <em>a ele</em>, não ao seu endereço de rede.",
              "<strong>Toda comunicação é autenticada</strong> — mesmo entre serviços do mesmo cluster, como se cruzasse fronteira não confiável.",
              "<strong>Referência formal</strong> — a publicação especial do NIST sobre arquitetura de confiança zero.",
          ]), visual="compare"),
    slide(12, "Conteúdo", "Autenticação, autorização e menor privilégio",
          p("Duas perguntas complementares — e nenhuma delas substitui a outra:") + "\n" +
          ul([
              "<strong>Autenticação</strong> — “quem está fazendo esta requisição?”",
              "<strong>Autorização</strong> — “o que essa identidade tem permissão para fazer?”",
              "<strong>Menor privilégio</strong> — cada identidade recebe apenas as permissões estritamente necessárias, nada além.",
              "<strong>Na NexaOrder</strong> — expedição autentica-se como “expedição” e é autorizada apenas a consultar status e confirmar envio.",
          ]) + "\n" +
          destaque("Um serviço pode estar <strong>corretamente autenticado</strong> e ainda assim não ter "
                   "autorização para uma operação específica — o reembolso continua fora do alcance da "
                   "expedição, mesmo que a rede permita a chamada."),
          visual="map"),
    slide(12, "Conteúdo", "TLS e TLS mútuo",
          ul([
              "<strong>TLS</strong> — protege dados em trânsito contra leitura e alteração por terceiros, com criptografia entre as duas pontas.",
              "<strong>TLS tradicional na web</strong> — apenas o servidor apresenta certificado.",
              "<strong>TLS mútuo (mTLS)</strong> — <em>ambas</em> as partes apresentam certificados e verificam a identidade uma da outra.",
              "<strong>O que o mTLS resolve</strong> — o serviço de pagamento passa a autenticar a identidade de quem o chamou.",
              "<strong>O que ele não resolve</strong> — uma política de autorização <em>separada</em> decide se aquela identidade pode executar a operação.",
              "<strong>A conclusão</strong> — estar na mesma rede não basta; ter certificado válido também não concede, por si só, permissão de reembolso.",
          ]), visual="compare"),
    slide(12, "Conteúdo", "Gestão de segredos: por que o cofre importa",
          p("Credenciais, chaves de API e certificados não devem ficar em imagens, arquivos versionados ou "
            "variáveis definidas manualmente. A diferença aparece <strong>no momento do incidente</strong>:") + "\n" +
          tabela(["Onde está o segredo", "Como trocar após comprometimento", "Tempo até a contenção"], [
              ["Embutido na imagem", "Publicar nova imagem, testar e reimplantar todos os Pods afetados", "Horas — a credencial exposta segue válida nesse intervalo"],
              ["Gestor de segredos com rotação", "Rotacionar o valor; o Pod consulta o segredo atual quando precisa", "Segundos — sem nova publicação de imagem"],
          ]) + "\n" +
          destaque("Um gestor de segredos controla acesso, <strong>registra auditoria de uso</strong> e permite "
                   "<strong>rotação</strong> periódica. Essa diferença de velocidade de resposta costuma "
                   "determinar se um incidente fica contido ou se prolonga por dias.")),
    citacao(
        "“Estar na mesma rede não basta; possuir um certificado válido também não concede, por si só, "
        "permissão para reembolsar ou cobrar.”",
        "— síntese da Aula 12"),
    slide(12, "Conteúdo", "Gateway, proxy lateral e service mesh",
          p("Implementar autenticação, criptografia, limitação de taxa e autorização <em>dentro do código de "
            "cada serviço</em> é custoso e propenso a inconsistência.") + "\n" +
          ul([
              "<strong>Proxy lateral (sidecar)</strong> — processo auxiliar junto a cada instância, no mesmo Pod, que intercepta todo o tráfego de entrada e saída.",
              "<strong>O ganho</strong> — as políticas se aplicam de forma uniforme, sem que a aplicação as implemente.",
              "<strong>Service mesh</strong> — proxies laterais coordenados por um plano de controle que distribui configuração, certificados e políticas.",
              "<strong>Papéis complementares</strong> — o gateway protege a borda voltada a clientes externos; o proxy lateral protege a comunicação interna.",
          ]) + "\n" +
          destaque("Com service mesh, aplicar <strong>mTLS entre todos os serviços</strong> da NexaOrder não "
                   "exige alterar o código de pedidos, estoque, pagamento e expedição — e ainda produz métricas "
                   "uniformes de comunicação, tema retomado na Unidade 4."),
          visual="map"),
    slide(12, "Exemplo numérico", "Balde de fichas: absorvendo picos sem cair",
          p("Um balde de capacidade <strong>C</strong> é reabastecido a <strong>r</strong> fichas por segundo; "
            "cada requisição consome uma ficha, e requisições sem ficha são recusadas ou colocadas em espera.") + "\n" +
          formula("λ<sub>sustentável</sub> = r &nbsp;&nbsp;|&nbsp;&nbsp; pico absorvido = C") + "\n" +
          numeros([
              ("50", "capacidade do balde (C)"),
              ("20/s", "taxa de reposição (r)"),
              ("90", "requisições em 1 segundo"),
              ("40", "recusadas ou atrasadas"),
          ]) + "\n" +
          destaque("O balde absorve as primeiras <strong>50</strong> imediatamente e recusa ou atrasa as "
                   "<strong>40</strong> restantes até que novas fichas sejam repostas — protegendo o serviço de "
                   "uma sobrecarga que comprometeria a disponibilidade <strong>para todos os chamadores</strong>, "
                   "não apenas para a origem da rajada.")),
    slide(12, "Conteúdo", "Quatro ameaças que exploram a distribuição",
          tabela(["Ameaça", "Como funciona", "Mitigação"], [
              ["<strong>Repetição (replay)</strong>", "Mensagem legítima capturada e reenviada para produzir efeito indevido", "Identificador único persistido, janela de validade, verificação de integridade e rejeição atômica de IDs já consumidos"],
              ["<strong>Movimento lateral</strong>", "Serviço de baixo privilégio comprometido é usado para alcançar serviços sensíveis", "Autenticação mútua e menor privilégio entre todos os serviços, não só na borda"],
              ["<strong>Amplificação por retry</strong>", "Repetição agressiva transforma indisponibilidade parcial em sobrecarga generalizada", "Backoff, jitter e orçamento de tentativas, como na Aula 2"],
              ["<strong>Exposição de segredos</strong>", "Segredos em imagens, logs ou repositórios ficam acessíveis muito além do escopo pretendido", "Gestor de segredos com rotação e auditoria"],
          ]) + "\n" +
          destaque("As quatro <strong>reinterpretam, sob ótica adversarial</strong>, conceitos já estudados: "
                   "replay explora a mesma ausência de identificação de operação discutida em idempotência; "
                   "amplificação reproduz o padrão de retry sem backoff da Aula 2.")),
    slide(12, "Conteúdo", "Um fluxo autenticado: pedidos → pagamento",
          p("Reunindo os elementos da aula, uma chamada do serviço de pedidos ao de pagamento deveria "
            "atravessar, no mínimo, quatro verificações:") + "\n" +
          ul([
              "<strong>1. TLS mútuo</strong> — ambos os lados apresentam certificados válidos, emitidos por autoridade confiável do cluster.",
              "<strong>2. Autorização</strong> — a identidade “pedidos” pode solicitar autorizações de pagamento, mas <em>não</em> reembolsos.",
              "<strong>3. Limitação de taxa</strong> — aplicada pelo proxy lateral do serviço de pagamento, protegendo-o de sobrecarga.",
              "<strong>4. Identificador único</strong> — anexado à requisição, permitindo rejeitar repetições indevidas.",
          ]), visual="flow"),
    slide(12, "Transição", "O que a Unidade 4 vai perguntar",
          p("Com serviços delimitados, comunicação orientada a eventos, execução orquestrada e comunicação "
            "segura, a arquitetura da NexaOrder está <strong>estruturalmente completa</strong>. A Unidade 4 "
            "muda o foco de “como construir” para “como saber que está funcionando”:") + "\n" +
          ul([
              "Como enxergar o sistema por dentro com <strong>logs, métricas e rastreamento distribuído</strong>?",
              "Como provar que a resiliência funciona, com <strong>testes e engenharia do caos</strong>?",
              "Como processar grandes volumes em <strong>lote e em fluxo</strong>?",
              "Como <strong>avaliar e evoluir</strong> a arquitetura a partir de requisitos e indicadores?",
          ]), visual="map"),
    pontos_chave(12, [
        ("Perímetro não basta", "Confiança zero trata cada requisição interna como se cruzasse uma fronteira não confiável."),
        ("Duas perguntas distintas", "Autenticação identifica quem chama; autorização decide o que essa identidade pode fazer."),
        ("mTLS autentica, não autoriza", "Certificado válido prova identidade; a permissão vem de uma política separada."),
        ("Segredo fora do artefato", "Rotação em segundos versus horas é o que separa um incidente contido de um incidente prolongado."),
        ("Política sem tocar no código", "O service mesh aplica mTLS, autorização e limitação de taxa de forma uniforme via proxies laterais."),
        ("Ameaças reciclam conceitos", "Replay, movimento lateral e amplificação exploram, com intenção maliciosa, propriedades já estudadas."),
    ]),
    slide(12, "Atividade prática", "Mãos à obra: um fluxo autenticado e autorizado",
          p("Elabore o fluxo de segurança entre os serviços de pedido e pagamento da NexaOrder.") + "\n" +
          ul([
              "<strong>1.</strong> Descreva as identidades envolvidas e o mecanismo de autenticação mútua entre elas.",
              "<strong>2.</strong> Defina as permissões da identidade “pedidos”, aplicando menor privilégio.",
              "<strong>3.</strong> Indique explicitamente quais operações ela <em>não</em> pode executar.",
              "<strong>4.</strong> Especifique onde os segredos são armazenados e com que política de rotação.",
              "<strong>5.</strong> Dimensione um balde de fichas para o serviço de pagamento, justificando C e r.",
              "<strong>6.</strong> Explique como o desenho impede um ataque de repetição da requisição de cobrança.",
          ]), visual="map"),
    encerramento(
        "Você fecha a Unidade 3 com uma arquitetura estruturalmente completa: serviços delimitados, "
        "comunicação por eventos, execução orquestrada e tráfego autenticado. A Unidade 4 responde à "
        "pergunta que sobra: como saber que tudo isso está mesmo funcionando?",
        "Próxima unidade: Unidade 4 — Operação, validação e evolução."),
])
