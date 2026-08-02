"""Conteúdo do deck de abertura da disciplina (aula 0).

Este é o único deck que apresenta o professor: os decks das aulas 1 a 16 tratam
apenas do conteúdo.
"""

from slides_kit import (
    audiodescricao, capa, citacao, destaque, encerramento, montar, numeros, p,
    pontos_chave, professor, slide, sumario, tabela, ul,
)

SUB = "Da aplicação em um servidor único à plataforma distribuída"

A0 = montar([
    capa(0, "Distributed Systems Engineering", SUB),
    audiodescricao(
        "O professor Afonso Cesar Lelis Brandão é um homem adulto de pele clara, cabelos curtos e "
        "escuros, olhos castanhos e barba cheia escura. Na fotografia, aparece de frente, usa um "
        "<em>headset</em> preto e um agasalho cinza de gola alta, diante de um fundo desfocado. Os "
        "slides usam fundo azul-marinho com molduras de triângulos em amarelo, verde e ciano, e o "
        "conteúdo aparece em cartões claros."
    ),
    professor(
        "Professor e conteudista da UniFECAF, com atuação em <strong>arquitetura de sistemas "
        "distribuídos e engenharia de software</strong>. Conduz a disciplina com foco no <em>porquê</em> "
        "de cada decisão arquitetural — não apenas no “como” — e aborda os fundamentos sem assumir "
        "conhecimento prévio, sempre conectados à <strong>prática de mercado</strong>."
    ),
    sumario("Apresentação da disciplina", [
        "Por que engenharia de sistemas distribuídos",
        "O que você será capaz de fazer ao final",
        "A NexaOrder: o caso que atravessa a disciplina",
        "As quatro unidades e as 16 videoaulas",
        "Como a disciplina funciona",
        "Como você será avaliado",
        "Bibliografia essencial",
    ]),
    slide(0, "Sobre a disciplina", "Por que engenharia de sistemas distribuídos",
          p("Toda vez que você compra algo pela internet, pede uma corrida ou movimenta dinheiro por um "
            "banco digital, há um <strong>sistema distribuído</strong> funcionando nos bastidores: serviços "
            "em máquinas diferentes, conversando por rede, sujeitos a atraso, concorrência e falha.") + "\n" +
          ul([
              "<strong>O mercado não contrata só quem programa</strong> — contrata quem sabe explicar por que um sistema se comporta de certo jeito quando cresce.",
              "<strong>As perguntas mudam</strong> — o que acontece se uma resposta demorar? Repetir a requisição é seguro? Qual evento aconteceu primeiro?",
              "<strong>Os erros custam caro</strong> — perda de dados, cobrança duplicada, indisponibilidade em cascata, arquitetura cara que não entrega o benefício esperado.",
              "<strong>A competência central</strong> — escalabilidade, disponibilidade, consistência e resiliência tratadas como decisões explícitas.",
          ]), visual="map"),
    slide(0, "Resultado de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Analisar</strong> os elementos fundamentais de um sistema distribuído e modelar sua comunicação.",
              "<strong>Projetar</strong> estratégias de distribuição e coordenação de estado, avaliando compromissos.",
              "<strong>Integrar</strong> serviços, eventos e plataformas cloud-native com segurança e identidade.",
              "<strong>Validar e operar</strong> sistemas por telemetria, testes e experimentos de falha.",
              "<strong>Avaliar</strong> arquiteturas considerando desempenho, escalabilidade, segurança, custo e confiabilidade.",
              "<strong>Defender</strong> cada decisão arquitetural com requisito, mecanismo, compromisso e evidência.",
          ]), visual="map"),
    slide(0, "Fio condutor", "A NexaOrder atravessa as quatro unidades",
          p("Em vez de exemplos soltos, a disciplina acompanha uma <strong>plataforma fictícia de pedidos, "
            "pagamentos e expedição</strong>. Ela começa simples, em um único servidor, e precisa crescer "
            "sem perder confiabilidade.") + "\n" +
          ul([
              "<strong>Pedidos</strong> registra a intenção do cliente e coordena o fluxo.",
              "<strong>Estoque</strong> reserva a unidade e responde se a reserva foi possível.",
              "<strong>Pagamento</strong> solicita autorização a um provedor externo.",
              "<strong>Expedição</strong> prepara o envio quando as etapas anteriores convergem.",
          ]) + "\n" +
          destaque("Cada unidade acrescenta decisões, mecanismos e evidências à mesma arquitetura. Toda "
                   "escolha será observada <strong>pelo benefício que oferece e pelos problemas que "
                   "introduz</strong> — nunca só pelo benefício."),
          visual="flow"),
    slide(0, "Estrutura", "Unidade 1 — Fundamentos, comunicação, tempo e falhas",
          p("<strong>Resultado</strong>: analisar os elementos fundamentais de um sistema distribuído, "
            "modelar sua comunicação e reconhecer como concorrência, tempo e falhas parciais afetam o "
            "comportamento observado.") + "\n" +
          ul([
              "<strong>Aula 1</strong> — Pensar distribuído: conceitos, propriedades e compromissos.",
              "<strong>Aula 2</strong> — Comunicação entre processos: APIs, RPC e mensageria.",
              "<strong>Aula 3</strong> — Concorrência, relógios e ordenação de eventos.",
              "<strong>Aula 4</strong> — Modelos de falha e desenho para recuperação.",
          ]), visual="timeline"),
    slide(0, "Estrutura", "Unidade 2 — Dados distribuídos, consistência e coordenação",
          p("<strong>Resultado</strong>: projetar estratégias de distribuição e coordenação de estado, "
            "avaliando os compromissos entre consistência, disponibilidade, desempenho e tolerância a falhas.") + "\n" +
          ul([
              "<strong>Aula 5</strong> — Replicação e modelos de consistência.",
              "<strong>Aula 6</strong> — Particionamento, CAP e escalabilidade de dados.",
              "<strong>Aula 7</strong> — Consenso, eleição de líder e Raft.",
              "<strong>Aula 8</strong> — Transações distribuídas, sagas e idempotência.",
          ]), visual="timeline"),
    slide(0, "Estrutura", "Unidade 3 — Serviços, eventos e plataformas cloud-native",
          p("<strong>Resultado</strong>: integrar serviços e eventos em plataformas de nuvem, definindo "
            "limites, comunicação, orquestração e segurança de forma coerente.") + "\n" +
          ul([
              "<strong>Aula 9</strong> — Limites de domínio, serviços e descoberta.",
              "<strong>Aula 10</strong> — Arquitetura orientada a eventos e plataformas de streaming.",
              "<strong>Aula 11</strong> — Contêineres, Kubernetes e reconciliação de estado.",
              "<strong>Aula 12</strong> — Identidade, comunicação segura e confiança zero.",
          ]), visual="timeline"),
    slide(0, "Estrutura", "Unidade 4 — Operação, validação e evolução",
          p("<strong>Resultado</strong>: validar e operar sistemas distribuídos por meio de telemetria, "
            "testes, experimentos de falha e avaliação arquitetural baseada em requisitos e indicadores.") + "\n" +
          ul([
              "<strong>Aula 13</strong> — Observabilidade: logs, métricas e rastreamento distribuído.",
              "<strong>Aula 14</strong> — Testes de resiliência e engenharia do caos.",
              "<strong>Aula 15</strong> — Processamento distribuído em lote e em fluxo.",
              "<strong>Aula 16</strong> — Projeto integrado e avaliação arquitetural.",
          ]), visual="timeline"),
    citacao(
        "“Toda decisão arquitetural precisa explicitar quatro coisas: qual requisito ela atende, "
        "qual mecanismo adota, qual custo introduz e como o resultado será medido.”",
        "— princípio que orienta a disciplina"),
    slide(0, "Percurso", "Como a disciplina funciona",
          numeros([
              ("4", "unidades"),
              ("16", "videoaulas"),
              ("1", "caso contínuo"),
              ("4", "atividades práticas por unidade"),
          ]) + "\n" +
          ul([
              "<strong>Texto-base por aula</strong> — o conceito desenvolvido com exemplos numéricos e situação-problema.",
              "<strong>Videoaula</strong> — a demonstração do raciocínio sobre a NexaOrder, não a leitura do texto.",
              "<strong>Atividade prática</strong> — você produz um artefato de engenharia: registro de decisão, contrato, análise de falhas.",
              "<strong>Material complementar</strong> — leitura da fonte, aprofundamento, podcast e artigo científico por unidade.",
          ])),
    slide(0, "Avaliação", "Como você será avaliado",
          tabela(["Instrumento", "Formato", "O que ele verifica"], [
              ["Quiz não avaliativo", "2 questões por unidade", "Autoverificação imediata após o estudo"],
              ["Questionário da unidade", "40 questões (asserção-razão e interpretação)", "Domínio conceitual e leitura de cenários"],
              ["AAI — Unidade 1", "1 questão dissertativa", "Aplicação dos fundamentos à NexaOrder"],
              ["Trabalho PBL", "Caso com entregável definido", "Projeto arquitetural completo e justificado"],
              ["Avaliação final", "10 questões dissertativas", "Integração das quatro unidades"],
          ]) + "\n" +
          destaque("As questões não cobram memorização de definição: elas apresentam um <strong>cenário</strong> "
                   "e pedem que você identifique o compromisso correto. Estudar “decorando” não funciona aqui.")),
    slide(0, "Orientação de estudo", "O que se espera de você",
          ul([
              "<strong>Pergunte “e se falhar?”</strong> — para cada mecanismo estudado, imagine o que acontece quando ele não responde.",
              "<strong>Refaça as contas</strong> — os exemplos numéricos são pequenos de propósito; refazê-los fixa o raciocínio.",
              "<strong>Não aceite “é mais escalável”</strong> — exija de si mesmo o requisito, o mecanismo, o custo e a evidência.",
              "<strong>Traga seu contexto</strong> — se você já trabalha com sistemas, compare cada decisão com o que vê no dia a dia.",
              "<strong>Reconheça quando não distribuir</strong> — engenharia madura também sabe recomendar a solução simples.",
              "<strong>Use o caso</strong> — a NexaOrder existe para você testar hipóteses sem risco de produção.",
          ]), visual="map"),
    slide(0, "Fundamentação", "Bibliografia essencial",
          ul([
              "<strong>KLEPPMANN, Martin.</strong> <em>Designing data-intensive applications</em>. Sebastopol: O’Reilly, 2017.",
              "<strong>TANENBAUM, A. S.; VAN STEEN, M.</strong> <em>Distributed systems</em>. 4. ed. [S. l.]: distributed-systems.net, 2023.",
              "<strong>COULOURIS, George et al.</strong> <em>Distributed systems: concepts and design</em>. 5. ed. Boston: Addison-Wesley, 2011.",
              "<strong>NEWMAN, Sam.</strong> <em>Building microservices</em>. 2. ed. Sebastopol: O’Reilly, 2021.",
              "<strong>BEYER, Betsy et al.</strong> <em>Site reliability engineering</em>. Sebastopol: O’Reilly, 2016.",
              "<strong>NYGARD, Michael T.</strong> <em>Release it!</em> 2. ed. Raleigh: Pragmatic Bookshelf, 2018.",
          ]) + "\n" +
          destaque("Cada aula traz ainda suas referências específicas, e cada unidade indica leitura da fonte, "
                   "material de aprofundamento, podcast e artigo científico. Organização bibliográfica "
                   "orientada pela <strong>ABNT NBR 6023:2018</strong>.")),
    pontos_chave(0, [
        ("Decisão, não moda", "Distribuir é resposta a um requisito concreto — e toda decisão carrega um custo que precisa ser declarado."),
        ("Um caso contínuo", "A NexaOrder acompanha as quatro unidades, acumulando decisões, mecanismos e evidências."),
        ("Compromissos explícitos", "Consistência, disponibilidade, latência e custo se equilibram; a disciplina treina esse equilíbrio."),
        ("Prática de engenharia", "Cada aula termina em um artefato: registro de decisão, contrato de evento, análise de falhas, plano de testes."),
    ]),
    encerramento(
        "Nas próximas 16 videoaulas, você vai acompanhar uma aplicação simples se transformar em uma "
        "plataforma distribuída — e vai aprender a justificar cada passo dessa transformação. Comece pela "
        "Aula 1, em que definimos o que caracteriza um sistema distribuído e por que distribuir muda o "
        "raciocínio de projeto.",
        "Primeira aula: Aula 1 — Pensar distribuído."),
])
