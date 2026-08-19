"""Conteúdo dos decks da Unidade 2 — Dados distribuídos, consistência e coordenação."""

from slides_kit import (
    audiodescricao, capa, citacao, destaque, encerramento, formula, montar,
    numeros, p, pontos_chave, slide, sumario, tabela, ul,
)

SUB = "Unidade 2 — Dados distribuídos, consistência e coordenação"

# ---------------------------------------------------------------- Aula 5

A5 = montar([
    capa(5, "Replicação e modelos de consistência", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um quadro comparando "
        "replicação de líder único e multi-líder; uma linha do tempo do atraso de réplica de 150 "
        "milissegundos entre a confirmação no líder e a aplicação na réplica; uma matriz dos modelos de "
        "consistência forte, sequencial, causal e eventual; um painel numérico com a condição de quórum "
        "W mais R maior que N para cinco réplicas; e uma tabela relacionando catálogo, estoque e "
        "pagamento às garantias escolhidas para cada um."
    ),
    sumario("Replicação e modelos de consistência", [
        "Por que replicar dados",
        "Líder-seguidor e replicação multi-líder",
        "Replicação síncrona, assíncrona e semissíncrona",
        "Atraso de réplica e leituras obsoletas",
        "Consistência forte, sequencial, causal e eventual",
        "Garantias centradas no cliente",
        "Quóruns de leitura e escrita",
        "Uma garantia diferente para cada dado da NexaOrder",
    ]),
    slide(5, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Justificar</strong> a replicação a partir de disponibilidade, latência, escala de leitura ou durabilidade.",
              "<strong>Comparar</strong> líder-seguidor e multi-líder quanto à ordenação de escritas e ao risco de conflito.",
              "<strong>Explicar</strong> leituras obsoletas pelo atraso de réplica, sem tratá-las como defeito automático.",
              "<strong>Distinguir</strong> consistência forte, sequencial, causal e eventual pelas propriedades que cada uma garante.",
              "<strong>Dimensionar</strong> quóruns de leitura e escrita usando a condição W + R &gt; N.",
              "<strong>Escolher</strong> a garantia adequada por dado — e não por serviço inteiro.",
          ]), visual="map"),
    slide(5, "Situação-problema", "Três cópias, três respostas diferentes",
          p("Um banco por serviço ainda era ponto único de falha e gargalo de leitura. Manter cópias em "
            "vários nós resolveu a disponibilidade — e criou um problema novo:") + "\n" +
          ul([
              "Durante uma promoção, um cliente consultou o catálogo três vezes e recebeu <strong>três preços diferentes</strong>, todos “atuais”.",
              "Uma reserva confirmada em uma réplica <strong>não havia chegado a outra</strong>.",
              "Um segundo cliente conseguiu reservar <strong>a mesma unidade do mesmo produto</strong>.",
              "<strong>Nenhuma réplica mentiu</strong>: cada uma respondeu com exatidão ao que já havia recebido.",
          ]) + "\n" +
          destaque("O problema não foi a replicação. Foi <strong>não ter definido, para cada tipo de dado</strong>, "
                   "qual garantia de consistência era necessária e qual mecanismo a sustentaria."),
          visual="compare"),
    slide(5, "Conteúdo", "Por que replicar dados",
          p("Replicação é a manutenção de cópias do mesmo dado em nós diferentes. Quatro motivações "
            "aparecem com mais frequência:") + "\n" +
          ul([
              "<strong>Disponibilidade</strong> — se um nó falhar, outra cópia continua respondendo.",
              "<strong>Redução de latência</strong> — servir leituras a partir do nó geograficamente mais próximo.",
              "<strong>Escalabilidade de leitura</strong> — distribuir um grande volume de consultas entre várias réplicas.",
              "<strong>Durabilidade</strong> — reduzir a chance de perda definitiva após a falha de um único nó.",
          ]) + "\n" +
          destaque("Nenhum benefício é gratuito. Toda cópia adicional traz a pergunta central da aula: como manter "
                   "réplicas <strong>coerentes o suficiente para o uso pretendido</strong>, sem sacrificar o "
                   "benefício que motivou a replicação."),
          visual="map"),
    slide(5, "Conteúdo", "Líder-seguidor e multi-líder",
          tabela(["Critério", "Primário-réplica (líder-seguidor)", "Multi-líder"], [
              ["Quem aceita escrita", "Apenas o líder", "Mais de um nó, em regiões diferentes"],
              ["Ordenação das escritas", "Centralizada em um ponto, sem disputa", "Concorrente entre líderes"],
              ["Vantagem principal", "Sem conflito de escrita na operação normal", "Escrita local reduz a latência regional"],
              ["Custo principal", "Líder é gargalo e exige recuperação", "Exige regra explícita de resolução de conflito"],
              ["Risco típico", "Promoção mal coordenada gera split-brain", "Escritas concorrentes sobre o mesmo dado colidem"],
          ]) + "\n" +
          destaque("Se um centro de distribuição registra a saída de uma unidade enquanto outro registra uma "
                   "correção de inventário do mesmo item, é preciso decidir de antemão: <strong>prevalência do "
                   "último carimbo, mesclagem de campos ou intervenção manual</strong>. Sem regra explícita, o "
                   "comportamento em conflito é imprevisível.")),
    slide(5, "Conteúdo", "Quando a escrita é considerada concluída",
          ul([
              "<strong>Síncrona</strong> — o líder só confirma ao cliente depois que uma ou mais réplicas confirmaram ter recebido.",
              "<strong>Efeito da síncrona</strong> — mais durabilidade e menor risco de perda; em troca, mais latência e dependência da disponibilidade das réplicas.",
              "<strong>Assíncrona</strong> — o líder responde sem esperar; a propagação continua em segundo plano.",
              "<strong>Efeito da assíncrona</strong> — menor latência percebida, mas há uma janela em que a falha do líder perde uma escrita que nenhuma réplica durável recebeu.",
              "<strong>Semissíncrona</strong> — exige confirmação de apenas parte das réplicas.",
              "<strong>Por que importa</strong> — é exatamente a ideia que reaparece adiante como <em>quórum de escrita</em>.",
          ]), visual="compare"),
    slide(5, "Exemplo numérico", "Atraso de réplica e leituras obsoletas",
          p("O intervalo entre a confirmação no líder e a aplicação na réplica é o <strong>atraso de "
            "réplica</strong>. Enquanto ele existe, uma leitura na réplica devolve um valor mais antigo "
            "que o já confirmado no líder:") + "\n" +
          numeros([
              ("t₀", "líder confirma a escrita"),
              ("150 ms", "atraso da réplica (Δ)"),
              ("t₀ + Δ", "réplica aplica a escrita"),
              ("150 ms", "janela de leitura obsoleta"),
          ]) + "\n" +
          destaque("Isso explica o caso do catálogo: cada consulta pode ter sido atendida por uma réplica "
                   "diferente, <strong>cada uma em um ponto distinto da própria janela de atraso</strong>. O "
                   "atraso de réplica não é, isoladamente, um defeito — ele vira problema quando o processo de "
                   "negócio pressupõe, implicitamente, uma consistência que o sistema não oferece.")),
    citacao(
        "“Nenhuma réplica mentiu: cada uma respondeu com exatidão ao que já havia recebido.”",
        "— síntese da Aula 5"),
    slide(5, "Conteúdo", "Quatro modelos de consistência",
          tabela(["Modelo", "O que garante", "Custo típico"], [
              ["<strong>Forte</strong> (linearizabilidade)", "Comporta-se como se houvesse uma única cópia; toda leitura reflete a escrita concluída mais recente", "Mais coordenação: pode elevar latência ou reduzir disponibilidade sob falha"],
              ["<strong>Sequencial</strong>", "Todas as réplicas concordam com a mesma ordem de operações", "A ordem não precisa coincidir com o tempo real entre clientes distintos"],
              ["<strong>Causal</strong>", "Operações com relação de causa e efeito são vistas na mesma ordem por todos", "Operações concorrentes podem ser vistas em ordens diferentes"],
              ["<strong>Eventual</strong>", "Cessadas as escritas, as réplicas convergem para o mesmo valor", "Sem prazo definido nem garantia sobre a ordem observada no meio-tempo"],
          ]) + "\n" +
          destaque("A consistência causal é retomada direta da relação <strong>happened-before</strong> da Aula 3 — "
                   "o mesmo raciocínio, agora aplicado a réplicas de dados.")),
    slide(5, "Erro comum", "“Forte é melhor, eventual é pior”",
          p("Essa leitura é uma das confusões mais caras da área. Os modelos não formam uma escala "
            "universal de qualidade:") + "\n" +
          ul([
              "<strong>Forte não é “melhor” em absoluto</strong> — ela costuma exigir mais coordenação, e coordenação tem preço.",
              "<strong>Eventual não é “pior”</strong> — pode permitir menos coordenação, sem garantir automaticamente menor custo.",
              "<strong>Nem sempre é mais disponível</strong> — o resultado depende do protocolo e das falhas consideradas.",
              "<strong>A escolha depende do dado</strong> — do que ele representa e do risco que carrega para o negócio.",
          ]) + "\n" +
          destaque("A pergunta certa não é “qual modelo é o melhor?”, e sim <strong>“o que este dado específico "
                   "não pode tolerar?”</strong>."),
          visual="compare"),
    slide(5, "Conteúdo", "Garantias centradas no cliente",
          p("Boa parte do que o usuário percebe como “bug” pode ser resolvida sem exigir linearizabilidade "
            "global, com garantias de sessão:") + "\n" +
          ul([
              "<strong>Leitura das próprias escritas</strong> — o cliente sempre vê as alterações que ele mesmo fez.",
              "<strong>Leituras monotônicas</strong> — observado um valor, ele nunca verá um valor mais antigo depois.",
              "<strong>Escritas monotônicas</strong> — as escritas de um mesmo cliente são aplicadas na ordem emitida.",
              "<strong>Prefixo consistente</strong> — se B depende causalmente de A, ninguém observa B sem antes observar A.",
          ]) + "\n" +
          destaque("São garantias <strong>de sessão</strong>, não degraus de uma escala universal. Elas reduzem a "
                   "inconsistência percebida; o custo real depende do protocolo e da arquitetura."),
          visual="map"),
    slide(5, "Exemplo numérico", "Quóruns de leitura e escrita",
          p("Com o dado replicado em <strong>N</strong> nós, a escrita conclui quando confirmada por "
            "<strong>W</strong> réplicas e a leitura consulta <strong>R</strong> réplicas, reconciliando as "
            "respostas por metadados de versão. A condição clássica de interseção é:") + "\n" +
          formula("W + R &gt; N") + "\n" +
          numeros([
              ("N = 5", "réplicas do dado"),
              ("W = 3", "confirmam a escrita"),
              ("R = 3", "consultadas na leitura"),
              ("6 &gt; 5", "há interseção garantida"),
          ]) + "\n" +
          destaque("A interseção garante que ao menos uma resposta <strong>possa conter</strong> a versão "
                   "confirmada — desde que os quóruns sejam fixos (não <em>sloppy</em>) e o sistema compare "
                   "versões corretamente. A desigualdade sozinha <strong>não</strong> garante linearizabilidade "
                   "nem resolve escritas concorrentes: para isso, W &gt; N/2 mais versionamento e reconciliação.")),
    slide(5, "Conteúdo", "Combinações de quórum e seus compromissos",
          tabela(["Configuração", "Efeito na escrita", "Efeito na leitura"], [
              ["W = 1, R = N", "Rápida", "Cara e menos disponível: depende de todas as réplicas"],
              ["W = N, R = 1", "Cara e menos disponível: depende de todos os nós", "Rápida"],
              ["W + R &gt; N", "Equilibrada", "Interseção garantida com o quórum de escrita"],
              ["W + R ≤ N", "Prioriza disponibilidade", "Sem garantia de sobreposição: aceita leituras obsoletas"],
          ]) + "\n" +
          formula("N ≥ 2f + 1  &nbsp;→&nbsp;  réplicas mínimas para tolerar f falhas com maioria") + "\n" +
          p("Esse mesmo princípio de maioria reaparece na <strong>Aula 7</strong>, quando o assunto for consenso.")),
    slide(5, "Conteúdo", "Uma garantia diferente para cada dado",
          tabela(["Dado", "Garantia adequada", "Justificativa de negócio"], [
              ["<strong>Catálogo</strong>", "Consistência eventual", "Preço levemente desatualizado por segundos não compromete o negócio; prioriza disponibilidade e latência"],
              ["<strong>Estoque</strong>", "Garantias de cliente + quórum com sobreposição (N=3, W=2, R=2)", "Reserva exige controle explícito de concorrência para não vender a mesma unidade duas vezes"],
              ["<strong>Pagamento</strong>", "Próximo de consistência forte no registro da transação", "Maior rigidez; notificações associadas podem permanecer eventuais"],
          ]) + "\n" +
          destaque("Dizer apenas “W ≥ 2”, sem definir N, R e a regra de reconciliação, <strong>não basta</strong>. "
                   "Decompor o sistema <strong>por dado</strong>, e não por serviço inteiro, é uma das habilidades "
                   "centrais desta unidade.")),
    pontos_chave(5, [
        ("Replicar tem preço", "Melhora disponibilidade, latência e durabilidade — e introduz o problema de manter cópias coerentes."),
        ("Líder ordena", "Líder-seguidor centraliza a ordenação na operação normal; multi-líder reduz latência regional e exige regra de conflito."),
        ("Quando confirmar", "Síncrona reduz a janela de perda com mais coordenação; assíncrona responde antes e aceita risco maior."),
        ("Obsoleto não é errado", "O atraso de réplica explica leituras antigas sem que nenhuma réplica esteja incorreta."),
        ("Não há escala única", "Forte, sequencial, causal e eventual têm propriedades diferentes, não posições em uma régua de qualidade."),
        ("Quórum não basta sozinho", "W + R > N garante interseção; devolver a versão certa ainda exige metadados de versão e reconciliação."),
    ]),
    slide(5, "Atividade prática", "Mãos à obra: uma garantia por dado",
          p("Para catálogo, estoque e pagamento, entregue uma <strong>tabela de três linhas</strong> que "
            "permita comparação direta entre as escolhas.") + "\n" +
          ul([
              "<strong>1.</strong> O modelo de consistência mais adequado, com justificativa de negócio.",
              "<strong>2.</strong> O modelo de replicação: líder único ou multi-líder.",
              "<strong>3.</strong> Se a replicação será síncrona, assíncrona ou por quórum.",
              "<strong>4.</strong> Valores plausíveis de N, W e R para o caso escolhido.",
              "<strong>5.</strong> Um cenário de leitura obsoleta que seria <em>aceitável</em> para esse dado.",
              "<strong>6.</strong> Um cenário de leitura obsoleta que <em>não</em> seria aceitável, e por quê.",
          ]), visual="map"),
    encerramento(
        "Você já sabe escolher a garantia de consistência adequada a cada dado e dimensionar quóruns de "
        "leitura e escrita. Na próxima aula, o problema muda de natureza: não basta copiar o dado — é "
        "preciso dividi-lo, porque uma cópia inteira já não cabe em um nó.",
        "Próxima aula: Aula 6 — Particionamento, CAP e escalabilidade de dados."),
])

# ---------------------------------------------------------------- Aula 6

A6 = montar([
    capa(6, "Particionamento, CAP e escalabilidade de dados", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um quadro comparando "
        "particionamento por faixa, por hash e por diretório; um painel numérico com a fração de chaves "
        "redistribuída pelo hashing consistente ao adicionar o décimo nó; um cálculo da probabilidade de "
        "cauda de latência em uma consulta que atinge oito partições; um diagrama de dois grupos de nós "
        "separados por rede rompida, contrastando o comportamento CP e o AP; e uma matriz de decisão "
        "PACELC para catálogo, estoque e pagamento."
    ),
    sumario("Particionamento, CAP e escalabilidade de dados", [
        "Particionamento horizontal e sua diferença para replicação",
        "Estratégias por faixa, por hash e por diretório",
        "Hashing consistente e nós virtuais",
        "Rebalanceamento e pontos quentes",
        "Particionamento e replicação combinados",
        "Consultas entre partições e cauda de latência",
        "O teorema CAP durante uma partição de rede",
        "PACELC: o compromisso que existe todos os dias",
    ]),
    slide(6, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Diferenciar</strong> particionamento de replicação e reconhecer por que produção combina os dois.",
              "<strong>Escolher</strong> a estratégia de partição adequada aos padrões de consulta mais frequentes.",
              "<strong>Calcular</strong> a fração de chaves redistribuída ao adicionar um nó com hashing consistente.",
              "<strong>Diagnosticar</strong> pontos quentes e propor mitigações distintas para leitura e escrita.",
              "<strong>Aplicar</strong> o teorema CAP ao comportamento do sistema durante uma partição de rede.",
              "<strong>Usar</strong> o PACELC para explicar o custo de consistência fora de cenários de falha.",
          ]), visual="map"),
    slide(6, "Situação-problema", "Quando uma cópia inteira já não cabe em um nó",
          p("Resolvida a coerência entre réplicas, a NexaOrder encontrou um segundo limite: o catálogo "
            "chegou a milhões de produtos e o histórico de pedidos, a bilhões de registros. Replicar a "
            "base inteira em cada nó ficou inviável.") + "\n" +
          ul([
              "Era preciso <strong>dividir os dados</strong>, não apenas copiá-los.",
              "A primeira tentativa: produtos de <strong>“A” a “M”</strong> em um nó, de <strong>“N” a “Z”</strong> em outro.",
              "Uma campanha concentrada em produtos com <strong>“S”</strong> sobrecarregou um único nó.",
              "O outro nó permaneceu ocioso: <strong>dividir exige estratégia</strong>, não um corte arbitrário.",
          ]), visual="compare"),
    slide(6, "Conteúdo", "Particionamento horizontal",
          p("Particionamento horizontal (<em>sharding</em>) divide um conjunto de dados em partições "
            "menores, cada uma servida por um subconjunto de nós.") + "\n" +
          ul([
              "<strong>Replicação copia</strong> — mantém cópias completas do mesmo dado em nós diferentes.",
              "<strong>Particionamento divide</strong> — distribui fatias diferentes de um mesmo conjunto.",
              "<strong>Produção combina os dois</strong> — cada partição é, por sua vez, replicada para garantir disponibilidade.",
              "<strong>O objetivo</strong> — deixar volume de dados e volume de operações crescerem distribuindo trabalho, em vez de exigir tudo de um nó.",
          ]), visual="map"),
    slide(6, "Conteúdo", "Três estratégias de particionamento",
          tabela(["Estratégia", "Como decide a partição", "Vantagem", "Limitação"], [
              ["<strong>Faixa</strong>", "Intervalos contíguos da chave (jan/fev, A–M/N–Z)", "Consultas por intervalo atingem partições contíguas", "Pontos quentes quando a distribuição real não é uniforme"],
              ["<strong>Hash</strong>", "Função de espalhamento aplicada à chave", "Distribuição aproximadamente uniforme entre partições", "Consulta por intervalo perde eficiência; chave popular continua concentrando"],
              ["<strong>Diretório</strong>", "Tabela explícita de mapeamento chave → partição", "Flexibilidade máxima para rebalancear", "Componente adicional que pode virar ponto único de falha"],
          ]) + "\n" +
          destaque("O hash reduz pontos quentes causados por <strong>concentração em faixas</strong>, mas não "
                   "resolve uma <strong>única chave muito popular</strong> — e espalha chaves originalmente "
                   "próximas entre partições distintas.")),
    slide(6, "Exemplo numérico", "Hashing consistente: o custo de crescer",
          p("O hash simples <code>hash(chave) mod N</code> redistribui quase todas as chaves quando N muda. "
            "O hashing consistente organiza o espaço como um <strong>anel</strong>: a chave vai ao primeiro nó "
            "encontrado em sentido horário, e só as chaves entre o novo nó e seu vizinho anterior se movem.") + "\n" +
          formula("fração redistribuída ≈ 1 ÷ ( N + 1 )") + "\n" +
          numeros([
              ("9", "nós existentes"),
              ("+1", "nó adicionado"),
              ("≈ 10%", "das chaves se movem"),
              ("~100%", "com hash simples e módulo"),
          ]) + "\n" +
          destaque("Cada nó físico costuma receber <strong>100 ou 200 posições virtuais</strong> espalhadas pelo "
                   "anel. Com uma posição só, a carga dependeria do acaso de onde o nó caiu; com nós virtuais, a "
                   "soma dos segmentos se aproxima da média esperada e <strong>reduz a variância de carga</strong> "
                   "sem mudar a lógica de atribuição.")),
    slide(6, "Conteúdo", "Rebalanceamento e pontos quentes",
          p("Mesmo com hashing consistente, uma <strong>única chave</strong> pode concentrar tráfego "
            "desproporcional — um produto em promoção relâmpago puxando quase todas as leituras de estoque.") + "\n" +
          ul([
              "<strong>Ponto quente de leitura</strong> — cache, réplicas de leitura e visão materializada, com invalidação ou versão que explicite a defasagem tolerada.",
              "<strong>Ponto quente de escrita</strong> — sufixos aleatórios funcionam para escritas agregáveis, como contadores.",
              "<strong>Cuidado com o fan-out</strong> — se toda leitura precisar consultar todas as subchaves, o gargalo piora em vez de melhorar.",
              "<strong>Estoque autoritativo</strong> — a reserva não pode ser dividida ingenuamente: mantenha regra única de concorrência, cotas por partição ou decisão serializada por produto.",
              "<strong>Durante o pico</strong> — isolar temporariamente o item e aplicar controle de admissão.",
              "<strong>Rebalancear move carga, não só dados</strong> — origem e destino processam tráfego normal e transferência ao mesmo tempo; daí o <em>throttling</em> e as janelas de menor tráfego.",
          ]), visual="map"),
    citacao(
        "“Uma decisão registrada apenas como ‘usamos hash consistente’ está incompleta sem a decisão "
        "complementar: sob partição de rede, esse dado prioriza consistência ou disponibilidade?”",
        "— síntese da Aula 6"),
    slide(6, "Conteúdo", "Particionamento e replicação combinados",
          p("Uma arquitetura típica particiona os dados em <strong>P</strong> partições e replica cada "
            "partição em <strong>R</strong> nós — um cluster com <strong>P × R</strong> réplicas distribuídas.") + "\n" +
          ul([
              "<strong>Dentro de cada partição</strong> — valem os conceitos da Aula 5: líder-seguidor ou multi-líder, quóruns de leitura e escrita.",
              "<strong>Entre as partições</strong> — valem os conceitos desta aula: chave, estratégia e rebalanceamento.",
              "<strong>Falha de um nó físico</strong> — afeta apenas as partições cujas réplicas ele hospedava, não o sistema inteiro.",
              "<strong>Condição</strong> — a escrita só é comprometida <em>se</em> as réplicas restantes não formarem o quórum exigido; havendo quórum, a partição segue disponível com menor margem para novas falhas.",
          ]), visual="map"),
    slide(6, "Exemplo numérico", "Scatter-gather e a cauda de latência",
          p("Uma consulta que combina dados de várias partições exige <strong>dispersão e coleta</strong>: "
            "vai a todas as partições relevantes e agrega os resultados parciais. O tempo total é determinado "
            "pela <strong>partição mais lenta a responder</strong>.") + "\n" +
          formula("P(ao menos uma lenta) = 1 − (1 − 0,05)<sup>8</sup> ≈ 0,34") + "\n" +
          numeros([
              ("8", "partições atingidas"),
              ("20 ms", "resposta média"),
              ("5%", "chance de cauda por partição"),
              ("34%", "das consultas sofrem a cauda"),
          ]) + "\n" +
          destaque("Mais de <strong>um terço</strong> das consultas que tocam oito partições tende a sofrer a "
                   "cauda de pelo menos uma — mesmo com cada partição lenta apenas 5% das vezes. É um argumento "
                   "numérico direto para <strong>projetar chaves que evitem consultas dispersas</strong> "
                   "(assumindo ocorrências independentes, apenas para este cálculo).")),
    slide(6, "Conteúdo", "O teorema CAP",
          p("Durante uma <strong>partição de rede</strong> — quando nós deixam de se comunicar entre si — um "
            "sistema replicado não pode oferecer simultaneamente:") + "\n" +
          ul([
              "<strong>Consistência (C)</strong> — toda leitura reflete a escrita mais recente confirmada.",
              "<strong>Disponibilidade (A)</strong> — toda requisição a um nó ativo recebe resposta, mesmo sem garantia de ser a mais recente.",
              "<strong>Tolerância a partição (P)</strong> — o sistema continua operando apesar da perda de comunicação entre alguns nós.",
          ]) + "\n" +
          destaque("Como partições são <strong>inevitáveis</strong> em sistemas reais, P não é opcional na prática. "
                   "A escolha relevante ocorre entre <strong>C e A durante o período em que a partição persiste</strong> — "
                   "fora dela, um sistema pode oferecer alta consistência e alta disponibilidade ao mesmo tempo."),
          visual="triangle"),
    slide(6, "Conteúdo", "CP e AP: dois comportamentos sob partição",
          tabela(["", "Sistema CP", "Sistema AP"], [
              ["Durante a partição", "Rejeita ou atrasa respostas no lado que não garante a versão mais recente", "Continua respondendo em ambos os lados"],
              ["O que preserva", "Consistência", "Disponibilidade"],
              ["O que arrisca", "Indisponibilidade parcial enquanto a partição durar", "Valores divergentes entre os lados"],
              ["Depois da partição", "Nada a reconciliar", "Reconciliação necessária ao restabelecer a comunicação"],
              ["Uso típico na NexaOrder", "Reserva de estoque e confirmação de pagamento", "Leitura do catálogo de produtos"],
          ])),
    slide(6, "Conteúdo", "PACELC: o compromisso de todos os dias",
          p("O CAP descreve apenas o comportamento sob partição. O <strong>PACELC</strong> estende a análise: "
            "<strong>se há partição (P)</strong>, escolhe-se entre disponibilidade (A) e consistência (C); "
            "<strong>caso contrário (E, else)</strong>, escolhe-se entre latência (L) e consistência (C).") + "\n" +
          ul([
              "<strong>Partições são raras</strong> — o compromisso latência × consistência ocorre a <em>cada operação</em>.",
              "<strong>Custo constante</strong> — exigir confirmação de todas as réplicas antes de responder paga latência sempre, não só na falha.",
              "<strong>Comunicação com o negócio</strong> — o PACELC deixa claro que consistência tem impacto no dia a dia, não apenas em cenários excepcionais.",
              "<strong>Decisão completa</strong> — “como particionar” e “o que fazer sob partição” são duas decisões, não uma.",
          ]), visual="compare"),
    slide(6, "Conteúdo", "Matriz de decisão da NexaOrder",
          tabela(["Dado", "Notação PACELC", "Comportamento esperado"], [
              ["<strong>Catálogo</strong>", "PA / EL", "Sob partição, disponibilidade; fora dela, latência, com convergência eventual"],
              ["<strong>Pagamento</strong>", "PC / EC", "Prioriza consistência sempre, mesmo recusando ou atrasando uma resposta"],
              ["<strong>Estoque — leitura informativa</strong>", "PA / EL", "Saldo aproximado tolera disponibilidade maior em situações de baixo risco"],
              ["<strong>Estoque — reserva efetiva</strong>", "PC", "Aproxima-se de CP para evitar vender o mesmo item duas vezes"],
          ]) + "\n" +
          destaque("O mesmo serviço aparece em <strong>duas linhas diferentes</strong>: a decisão é por "
                   "<strong>operação sobre o dado</strong>, não por serviço inteiro.")),
    pontos_chave(6, [
        ("Dividir, não só copiar", "Particionamento distribui fatias de um conjunto; complementa a replicação em vez de substituí-la."),
        ("Faixa favorece intervalo", "Consultas por período ficam eficientes, mas a distribuição real das chaves pode criar pontos quentes."),
        ("Hash espalha chaves", "Distribui bem chaves distintas ao custo da consulta por intervalo — e não resolve uma chave popular."),
        ("Anel reduz migração", "Hashing consistente move ≈1/(N+1) das chaves ao adicionar um nó, em vez de quase todas."),
        ("CAP vale na partição", "A escolha entre consistência e disponibilidade só se impõe enquanto a comunicação estiver rompida."),
        ("PACELC vale sempre", "Fora da partição, o compromisso é entre latência e consistência — e ele ocorre a cada operação."),
    ]),
    slide(6, "Atividade prática", "Mãos à obra: escolher chaves de partição",
          p("Escolha as chaves de partição para <strong>pedidos</strong> e <strong>estoque</strong> da "
            "NexaOrder e documente as decisões.") + "\n" +
          ul([
              "<strong>1.</strong> Defina a chave e a estratégia (faixa, hash ou diretório) de cada dado.",
              "<strong>2.</strong> Justifique a escolha pelos padrões de consulta mais comuns do sistema.",
              "<strong>3.</strong> Simule um produto virando ponto quente durante uma campanha.",
              "<strong>4.</strong> Descreva o efeito esperado sobre a partição correspondente.",
              "<strong>5.</strong> Proponha uma mitigação concreta, distinguindo leitura de escrita.",
              "<strong>6.</strong> Classifique cada dado como CP ou AP e verifique se a escolha se sustenta na lógica do PACELC.",
          ]), visual="map"),
    encerramento(
        "Você já sabe dividir dados sem criar pontos quentes e explicar, com CAP e PACELC, o que o sistema "
        "faz quando a rede se rompe. Na próxima aula, atacamos a pergunta que ficou em aberto na Aula 5: "
        "como um conjunto de nós concorda, sozinho, sobre quem é o líder legítimo?",
        "Próxima aula: Aula 7 — Consenso, eleição de líder e Raft."),
])

# ---------------------------------------------------------------- Aula 7

A7 = montar([
    capa(7, "Consenso, eleição de líder e Raft", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um painel numérico "
        "com a tolerância a falhas de um cluster de cinco nós; uma tabela comparando clusters de três, "
        "cinco e sete nós; uma linha do tempo de eleição mostrando temporizadores aleatórios expirando "
        "em instantes diferentes; um ciclo de replicação do Raft, do recebimento da operação à aplicação "
        "na máquina de estados; e um painel com a latência mínima de confirmação em cenários regional e "
        "intercontinental."
    ),
    sumario("Consenso, eleição de líder e Raft", [
        "O problema do consenso: válido, uniforme e irrevogável",
        "Maioria e quórum: quantas falhas um cluster tolera",
        "Máquina de estados replicada",
        "Eleição de líder e temporizadores aleatórios",
        "Termos, log replicado e confirmação",
        "Segurança e progresso no Raft",
        "Consenso e CAP: o lado minoritário",
        "Limites e custos do consenso",
    ]),
    slide(7, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Enunciar</strong> o problema do consenso pelas três propriedades que a decisão precisa satisfazer.",
              "<strong>Calcular</strong> quantas falhas um cluster de N nós tolera mantendo maioria.",
              "<strong>Explicar</strong> por que clusters de consenso usam número ímpar de nós.",
              "<strong>Descrever</strong> a eleição de líder do Raft e o papel dos temporizadores aleatórios.",
              "<strong>Distinguir</strong> segurança de progresso, e reconhecer que só o progresso depende de maioria ativa.",
              "<strong>Dimensionar</strong> o custo de latência de uma confirmação por consenso.",
          ]), visual="map"),
    slide(7, "Situação-problema", "Quem manda quando o líder some",
          p("O nó líder do estoque na região sul ficou inacessível por falha de rede. A equipe de plantão "
            "precisou promover um seguidor manualmente — e <strong>dois operadores, sem se comunicar, "
            "promoveram dois nós diferentes</strong> quase ao mesmo tempo.") + "\n" +
          ul([
              "Por alguns minutos, o sistema teve <strong>dois líderes aceitando escritas</strong>.",
              "Parte das reservas feitas nesse intervalo <strong>divergiu entre os dois</strong>.",
              "O problema real não era a indisponibilidade do líder.",
              "Era: <strong>como um conjunto de nós concorda sozinho</strong> sobre quem é o líder legítimo, mesmo com falhas?",
          ]) + "\n" +
          destaque("Resolver consenso manualmente é exatamente o que produz <strong>split-brain</strong>: "
                   "decisões concorrentes tomadas sem coordenação."),
          visual="timeline"),
    slide(7, "Conteúdo", "O problema do consenso",
          p("Consenso é fazer um conjunto de nós concordar sobre <strong>um único valor</strong>, mesmo na "
            "presença de falhas, de modo que a decisão seja:") + "\n" +
          ul([
              "<strong>Válida</strong> — o valor decidido foi de fato proposto por algum nó.",
              "<strong>Uniforme</strong> — todos os nós corretos decidem o mesmo valor.",
              "<strong>Irrevogável</strong> — uma vez decidido, o valor não muda.",
          ]) + "\n" +
          destaque("O problema aparece sempre que o sistema precisa de uma <strong>única fonte de verdade</strong>: "
                   "qual nó é o líder, qual foi a próxima operação aplicada ao log, qual transação foi confirmada."),
          visual="map"),
    slide(7, "Exemplo numérico", "Maioria: quantas falhas um cluster tolera",
          p("Algoritmos como o Raft se apoiam no princípio de maioria: uma decisão só vale quando aceita "
            "por <strong>mais da metade</strong> dos nós. É o mesmo quórum da Aula 5, aplicado agora à "
            "escolha do líder e às entradas confirmadas do log.") + "\n" +
          formula("f = ⌊ ( N − 1 ) ÷ 2 ⌋") + "\n" +
          numeros([
              ("N = 5", "nós no cluster"),
              ("f = 2", "falhas toleradas"),
              ("3", "nós formam maioria"),
              ("ímpar", "tamanho preferido"),
          ]) + "\n" +
          destaque("Adicionar um nó <strong>par</strong> não aumenta a tolerância: de 5 para 6, f = ⌊5/2⌋ continua "
                   "igual a 2 — apenas um nó a mais para coordenar. É por isso que números pares raramente fazem "
                   "sentido em clusters de consenso.")),
    slide(7, "Conteúdo", "Escolhendo o tamanho do cluster",
          tabela(["Nós (N)", "Falhas toleradas (f)", "Maioria exigida", "Compromisso"], [
              ["3", "1", "2", "Menor fan-out e menor custo; tolera apenas uma falha"],
              ["5", "2", "3", "Equilíbrio comum entre tolerância a falhas e custo de coordenação"],
              ["7", "3", "4", "Mais tolerância; aumenta tráfego, armazenamento e custo operacional"],
          ]) + "\n" +
          destaque("Como as mensagens são enviadas <strong>em paralelo</strong>, a latência não cresce "
                   "linearmente com N: ela depende da resposta necessária para <strong>completar o quórum</strong> "
                   "e da carga adicional introduzida.")),
    slide(7, "Conteúdo", "Máquina de estados replicada",
          ul([
              "<strong>A abstração</strong> — cada nó mantém uma réplica que pode estar temporariamente em um índice diferente do log.",
              "<strong>A garantia</strong> — réplicas que partem do mesmo estado e aplicam o mesmo prefixo de operações determinísticas na mesma ordem chegam ao mesmo estado.",
              "<strong>Seguidores atrasados convergem</strong> à medida que recebem e aplicam esse prefixo.",
              "<strong>A transformação</strong> — o problema de manter réplicas consistentes vira um problema mais restrito: acordo sobre o <strong>prefixo confirmado de um log ordenado</strong>.",
          ]), visual="map"),
    slide(7, "Conteúdo", "Eleição de líder",
          p("O Raft elege <strong>no máximo um líder por termo</strong>. Esse líder recebe novas operações "
            "e as replica para os seguidores.") + "\n" +
          ul([
              "<strong>1. Silêncio</strong> — os seguidores deixam de receber sinais válidos do líder.",
              "<strong>2. Temporizadores expiram</strong> — cada seguidor tem um temporizador <em>aleatório</em>, que vence em instante diferente.",
              "<strong>3. Candidatura</strong> — o primeiro a expirar torna-se candidato e solicita votos.",
              "<strong>4. Maioria elege</strong> — quem recebe votos da maioria vira líder do novo termo.",
          ]) + "\n" +
          destaque("O uso de temporizadores <strong>aleatórios, e não fixos</strong>, é deliberado: se todos "
                   "disparassem no mesmo instante, poderiam empatar repetidamente e atrasar a formação de um "
                   "novo líder. Um líder antigo e isolado pode ainda se julgar líder, mas não confirma nada sem "
                   "maioria e recua ao observar um termo maior."),
          visual="flow"),
    citacao(
        "“A segurança do Raft vale mesmo durante uma partição de rede; a disponibilidade depende de haver, "
        "em algum momento, comunicação suficiente entre a maioria dos nós.”",
        "— síntese da Aula 7"),
    slide(7, "Conteúdo", "Termos, log replicado e confirmação",
          p("O tempo, no Raft, é dividido em <strong>termos</strong> numerados sequencialmente. Cada termo "
            "tem no máximo um líder, e toda mensagem carrega o número do termo — permitindo rejeitar ordens "
            "de um líder antigo que ainda não percebeu ter sido substituído.") + "\n" +
          ul([
              "<strong>1. O líder anexa</strong> a nova operação ao log, no termo corrente.",
              "<strong>2. Replica</strong> aos seguidores por mensagens de <em>append entries</em>.",
              "<strong>3. Confirma</strong> ao armazenar essa entrada do termo corrente em uma maioria.",
              "<strong>4. Aplica</strong> à máquina de estados e só então devolve o resultado ao cliente.",
          ]), visual="cycle"),
    slide(7, "Detalhe crítico", "Por que uma entrada antiga não se confirma sozinha",
          p("Uma entrada de <strong>termo anterior</strong> não é confirmada diretamente só porque passou a "
            "aparecer em uma maioria.") + "\n" +
          ul([
              "<strong>Ela se torna confirmada indiretamente</strong> quando uma entrada posterior do termo corrente é confirmada.",
              "<strong>Por quê</strong> — sem essa regra, uma entrada replicada em maioria poderia ainda ser sobrescrita por um líder futuro.",
              "<strong>Combinada</strong> às restrições de eleição e de consistência do log, ela garante que entradas confirmadas <strong>sobrevivam a trocas de líder</strong>.",
              "<strong>Consequência prática</strong> — “está na maioria” não é sinônimo de “está confirmado”.",
          ]), visual="compare"),
    slide(7, "Conteúdo", "Segurança e progresso",
          tabela(["Propriedade", "O que o Raft garante", "De que depende"], [
              ["<strong>Segurança</strong> (safety)", "No máximo um líder por termo; só um líder com maioria confirma entradas; entrada confirmada nunca é perdida ou substituída", "Vale mesmo sob partição de rede ou atraso arbitrário de mensagens"],
              ["<strong>Progresso</strong> (liveness)", "O cluster eventualmente elege um líder e continua processando operações", "Exige maioria ativa trocando mensagens com atrasos compatíveis com os timeouts de eleição"],
          ]) + "\n" +
          destaque("Note a assimetria. Uma maioria apenas “conectada”, mas submetida indefinidamente a atrasos "
                   "incompatíveis com os temporizadores, <strong>não garante progresso</strong> — as garantias "
                   "de segurança, porém, permanecem intactas.")),
    slide(7, "Conteúdo", "Consenso e CAP: o lado minoritário",
          p("Se um cluster de cinco nós se divide em um grupo de <strong>três</strong> e outro de "
            "<strong>dois</strong> por uma partição de rede:") + "\n" +
          ul([
              "<strong>Grupo de três</strong> — é maioria: elege líder e continua aceitando escritas.",
              "<strong>Grupo de dois</strong> — permanece sem líder até a partição ser resolvida.",
              "<strong>Nenhum dos dois está “caído”</strong> — ambos operam, apenas isolados.",
              "<strong>Aplicação direta do CAP</strong> — o Raft escolhe <strong>consistência (CP)</strong> em detrimento da disponibilidade do lado minoritário.",
          ]), visual="map"),
    slide(7, "Exemplo numérico", "O custo de latência do consenso",
          p("Cada operação confirmada exige, no mínimo, uma rodada de comunicação entre o líder e "
            "seguidores suficientes para formar maioria. Como os envios são paralelos, a latência é "
            "determinada pela resposta que <strong>completa o quórum</strong>:") + "\n" +
          numeros([
              ("4 ms", "RTT entre 3 zonas próximas"),
              ("≈ 4 ms", "confirmação mínima"),
              ("120 ms", "RTT intercontinental"),
              ("≈ 120 ms", "confirmação mínima"),
          ]) + "\n" +
          destaque("São <strong>30 vezes</strong> a latência mínima, antes de qualquer processamento. É por isso "
                   "que clusters de consenso ficam com nós relativamente próximos entre si, ainda que o sistema "
                   "sirva usuários globais por outras camadas de replicação e cache.")),
    slide(7, "Conteúdo", "Limites e custos do consenso",
          ul([
              "<strong>Throughput limitado pelo líder</strong> — é a capacidade dele de processar e replicar que define o teto do grupo.",
              "<strong>Escala de escrita vem do particionamento</strong> — em vários grupos de consenso, não de múltiplos líderes no mesmo log.",
              "<strong>Pressupõe falhas de parada ou de rede</strong> — nós que param ou ficam inacessíveis.",
              "<strong>Não trata falhas bizantinas</strong> — nós que enviam informações deliberadamente incorretas.",
              "<strong>Consenso bizantino existe</strong> — está fora do escopo desta disciplina, mas é relevante em redes de blockchain público.",
              "<strong>Consenso não é grátis</strong> — usá-lo onde uma garantia mais fraca bastaria é desperdício de latência.",
          ]), visual="map"),
    slide(7, "Pausa para reflexão", "Maioria, topologia e disponibilidade real",
          p("Um cluster de cinco nós está distribuído em três zonas: <strong>duas em A, duas em B, uma em "
            "C</strong>. Uma falha isola completamente a zona C e degrada parcialmente a comunicação entre "
            "A e B, sem isolá-las por completo.") + "\n" +
          ul([
              "Considerando apenas o critério de maioria, quais <strong>combinações de nós</strong> ainda elegeriam um líder?",
              "Que diferença faz distribuir cinco nós em <strong>três zonas</strong> em vez de concentrá-los em duas?",
              "Operando com apenas <strong>três nós</strong>, o que uma manutenção programada que retira um nó significaria?",
              "Que <strong>evidência operacional</strong> — métrica, log ou alerta — revelaria que o cluster está sem maioria?",
          ]) + "\n" +
          destaque("O objetivo é praticar o raciocínio sobre maioria, topologia física e disponibilidade, "
                   "retomando o conceito de <strong>zonas independentes de falha</strong> da Unidade 1.")),
    pontos_chave(7, [
        ("Três propriedades", "A decisão de consenso precisa ser válida, uniforme e irrevogável, mesmo com falhas."),
        ("Maioria define tudo", "Um cluster de N nós tolera ⌊(N−1)/2⌋ falhas; números pares não aumentam a tolerância."),
        ("Log em vez de estado", "A máquina de estados replicada troca o problema de consistência pelo acordo sobre um log ordenado."),
        ("Um líder por termo", "Temporizadores aleatórios reduzem empates e aceleram a formação de um novo líder."),
        ("Confirmação tem regra", "Entradas de termos anteriores só se confirmam indiretamente, junto com uma entrada do termo corrente."),
        ("CP por construção", "Sob partição, apenas o lado majoritário progride; o minoritário fica sem líder até a rede voltar."),
    ]),
    slide(7, "Atividade prática", "Mãos à obra: simular um cluster Raft",
          p("Simule, em papel ou na ferramenta de sua escolha, um cluster Raft de <strong>cinco nós</strong>. "
            "Entregue um diagrama e uma descrição textual curta de cada etapa.") + "\n" +
          ul([
              "<strong>1.</strong> Desenhe o cluster e identifique o líder inicial no termo 1.",
              "<strong>2.</strong> Simule a falha do líder e descreva a sequência até a eleição do novo líder.",
              "<strong>3.</strong> Indique o novo número de termo resultante dessa eleição.",
              "<strong>4.</strong> Simule três novas operações e sua replicação aos seguidores.",
              "<strong>5.</strong> Indique o termo e o ponto exato em que cada operação é considerada confirmada.",
              "<strong>6.</strong> Simule a volta do nó que falhou e descreva como seu log é reconciliado.",
          ]), visual="map"),
    encerramento(
        "Você já sabe como um conjunto de nós elege um líder e mantém um log replicado sem intervenção "
        "manual — e a que custo. Na última aula da unidade, o problema atravessa os serviços: como manter "
        "uma compra coerente quando ela toca quatro bancos de dados independentes?",
        "Próxima aula: Aula 8 — Transações distribuídas, sagas e idempotência."),
])

# ---------------------------------------------------------------- Aula 8

A8 = montar([
    capa(8, "Transações distribuídas, sagas e idempotência", SUB),
    audiodescricao(
        "Os slides desta aula usam fundo azul-marinho com molduras de triângulos em amarelo, verde e "
        "ciano, e o conteúdo aparece em cartões claros. Há cinco recursos visuais: um fluxo das duas "
        "fases da confirmação em duas fases; um painel numérico com o risco multiplicativo de quatro "
        "participantes; um quadro comparando saga coreografada e orquestrada; um fluxo do padrão outbox "
        "gravando alteração e evento na mesma transação local; e uma sequência da saga da NexaOrder com "
        "as etapas normais e as compensações."
    ),
    sumario("Transações distribuídas, sagas e idempotência", [
        "Atomicidade local e atomicidade distribuída",
        "Confirmação em duas fases e o problema do bloqueio",
        "Sagas coreografadas e orquestradas",
        "Ações compensatórias e o que elas não desfazem",
        "O problema da escrita dupla e o padrão outbox",
        "Deduplicação atômica com o padrão inbox",
        "At-least-once e efeito efetivamente único",
        "A saga completa da NexaOrder",
    ]),
    slide(8, "Objetivos de aprendizagem", "O que você será capaz de fazer",
          ul([
              "<strong>Explicar</strong> por que a atomicidade de um banco não se estende a operações entre serviços.",
              "<strong>Descrever</strong> as duas fases do 2PC e identificar o cenário de bloqueio do coordenador.",
              "<strong>Modelar</strong> uma saga com transações locais e ações compensatórias correspondentes.",
              "<strong>Escolher</strong> entre coreografia e orquestração a partir do número de passos e da necessidade de rastreio.",
              "<strong>Aplicar</strong> os padrões outbox e inbox para eliminar escrita dupla e efeito duplicado.",
              "<strong>Projetar</strong> operações idempotentes que sobrevivam a reentregas at-least-once.",
          ]), visual="map"),
    slide(8, "Situação-problema", "Uma compra, quatro serviços, nenhuma transação única",
          p("Com replicação, particionamento e consenso resolvidos <em>dentro</em> de cada serviço, restou o "
            "problema que atravessa todos eles: uma compra toca pedidos, estoque, pagamento e expedição — "
            "cada um com seu próprio banco.") + "\n" +
          ul([
              "Não existe mais uma <strong>transação única</strong> capaz de garantir que os quatro passos aconteçam todos ou nenhum.",
              "Em teste de carga: o pagamento <strong>foi autorizado</strong>.",
              "Uma falha de rede impediu a confirmação de chegar a tempo ao serviço de pedidos.",
              "O cliente viu a interface travada, tentou de novo — e <strong>dois pagamentos</strong> foram processados para a mesma compra.",
          ]), visual="timeline"),
    slide(8, "Conteúdo", "Atomicidade local e distribuída",
          ul([
              "<strong>Dentro de um banco</strong> — a atomicidade é responsabilidade do próprio sistema: aplica todas as operações ou nenhuma, mesmo em caso de falha.",
              "<strong>Entre bancos independentes</strong> — nenhuma transação única garante essa propriedade automaticamente.",
              "<strong>O que resta</strong> — um mecanismo <em>explícito</em> de coordenação entre os serviços.",
              "<strong>A escolha desta aula</strong> — coordenar bloqueando (2PC) ou coordenar compensando (sagas).",
          ]), visual="compare"),
    slide(8, "Conteúdo", "Confirmação em duas fases (2PC)",
          p("Um coordenador conduz a transação distribuída em duas etapas:") + "\n" +
          ul([
              "<strong>1. Preparação</strong> — o coordenador pergunta a cada participante se está pronto para confirmar sua parte.",
              "<strong>2. Resposta</strong> — cada participante executa provisoriamente, <em>bloqueia os recursos</em> e responde “pronto” ou “abortar”.",
              "<strong>3. Confirmação</strong> — se todos responderam “pronto”, o coordenador ordena a confirmação definitiva.",
              "<strong>4. Aborto</strong> — se algum respondeu “abortar” ou não respondeu a tempo, o coordenador ordena desfazer em todos.",
          ]) + "\n" +
          destaque("O 2PC <strong>garante</strong> atomicidade distribuída — ao custo de manter recursos "
                   "bloqueados durante toda a espera pela decisão."),
          visual="flow"),
    slide(8, "Conteúdo", "O bloqueio do 2PC",
          ul([
              "<strong>O cenário crítico</strong> — o coordenador falha depois da preparação e antes de comunicar a decisão final.",
              "<strong>O efeito</strong> — os participantes ficam bloqueados, incapazes de decidir sozinhos se confirmam ou desfazem.",
              "<strong>A recuperação</strong> — exige registrar a decisão de forma durável antes da falha.",
              "<strong>E ainda</strong> — em geral, um processo que consulte o registro do coordenador assim que ele voltar.",
              "<strong>O custo cresce</strong> com o número de participantes e com a duração da transação.",
              "<strong>Por isso</strong> — o 2PC é pouco usado em operações de negócio longas, sendo mais comum em transações curtas dentro do mesmo domínio de infraestrutura.",
          ]), visual="map"),
    slide(8, "Exemplo numérico", "Por que mais participantes pioram o risco",
          p("Se cada um dos quatro serviços tem, isoladamente, <strong>1%</strong> de chance de estar lento "
            "ou indisponível em um dado instante — tratando os eventos como independentes apenas para este "
            "cálculo — a chance de <strong>pelo menos um</strong> atrasar a transação é:") + "\n" +
          formula("P(ao menos um lento) = 1 − (1 − 0,01)<sup>4</sup> ≈ 3,9%") + "\n" +
          numeros([
              ("1%", "risco por serviço"),
              ("4", "participantes no 2PC"),
              ("3,9%", "risco da transação"),
              ("≈ 4×", "o risco isolado"),
          ]) + "\n" +
          destaque("Quanto mais participantes um coordenador precisa reunir, maior a chance de a transação "
                   "inteira ficar <strong>refém do elo mais lento</strong>. Somado ao risco de bloqueio na falha "
                   "do coordenador, é o argumento decisivo contra o 2PC em fluxos com muitos serviços "
                   "independentes.")),
    citacao(
        "“Uma compensação nem sempre é o inverso perfeito da operação original: estornar um pagamento já "
        "processado pode envolver taxas e prazos diferentes de simplesmente não ter cobrado.”",
        "— síntese da Aula 8"),
    slide(8, "Conteúdo", "Sagas: transações locais encadeadas",
          p("Uma <strong>saga</strong> substitui a transação distribuída única por uma sequência de "
            "transações locais, cada uma confinada a um serviço e encadeada por eventos ou comandos.") + "\n" +
          ul([
              "<strong>Sem desfazer instantâneo</strong> — quando uma etapa falha, a saga não reverte tudo como o 2PC.",
              "<strong>Compensação</strong> — executa ações que revertem <em>logicamente</em> o efeito das etapas já concluídas.",
              "<strong>Sem bloqueio global</strong> — cada transação local confirma e libera seus recursos imediatamente.",
              "<strong>O preço</strong> — existe um intervalo em que o sistema está parcialmente aplicado, e isso precisa ser visível.",
          ]), visual="map"),
    slide(8, "Conteúdo", "Coreografada ou orquestrada",
          tabela(["Critério", "Saga coreografada", "Saga orquestrada"], [
              ["Coordenação", "Cada serviço publica eventos; os demais reagem", "Um orquestrador central envia comandos explícitos"],
              ["Onde está o fluxo", "Implícito, disperso entre os serviços", "Explícito, concentrado em um componente"],
              ["Rastreabilidade", "Difícil saber em que etapa uma saga está", "Fácil de acompanhar e auditar"],
              ["Melhor para", "Poucos passos e acoplamento mínimo", "Fluxos longos com muitas compensações"],
              ["Cuidado", "O processo de negócio não existe em lugar nenhum", "O orquestrador concentra conhecimento — mas, ao contrário do 2PC, não bloqueia recursos"],
          ])),
    slide(8, "Conteúdo", "Ações compensatórias",
          p("Como não há transação global para desfazer, cada etapa que altera estado precisa de uma "
            "compensação capaz de revertê-la de forma <strong>consistente com o negócio</strong>:") + "\n" +
          ul([
              "<strong>Reservar estoque</strong> → compensação: liberar a reserva.",
              "<strong>Autorizar pagamento</strong> → compensação: estornar o valor autorizado.",
              "<strong>Gerar etiqueta de expedição</strong> → compensação: cancelar a etiqueta antes do despacho.",
          ]) + "\n" +
          destaque("A compensação <strong>nem sempre é o inverso perfeito</strong>. Estornar um pagamento pode "
                   "envolver taxas, prazos ou políticas comerciais diferentes de nunca ter cobrado — por isso, "
                   "projetar a compensação é uma <strong>decisão de negócio</strong> tanto quanto técnica."),
          visual="flow"),
    slide(8, "Conteúdo", "Escrita dupla e o padrão outbox",
          p("O <strong>problema da escrita dupla</strong>: o serviço grava no banco e depois publica o evento. "
            "Se falhar entre as duas operações, o evento nunca é publicado — ou é publicado sem que a "
            "alteração tenha sido confirmada.") + "\n" +
          ul([
              "<strong>1. Uma única transação local</strong> grava a alteração de negócio <em>e</em> o evento em uma tabela auxiliar.",
              "<strong>2. Mesmo banco</strong> — a tabela <em>outbox</em> vive dentro do banco do próprio serviço.",
              "<strong>3. Processo separado</strong> lê essa tabela e publica os eventos de forma confiável.",
              "<strong>4. Resultado</strong> — evento e estado ficam consistentes, sem transação distribuída entre banco e mensageria.",
          ]), visual="flow"),
    slide(8, "Conteúdo", "Inbox: deduplicação que só funciona atômica",
          p("O <em>inbox</em> complementa o outbox do lado do consumidor — e o detalhe que o torna correto "
            "é a <strong>fronteira transacional</strong>:") + "\n" +
          ul([
              "<strong>Em uma única transação local</strong> — insere o identificador da mensagem (com restrição de unicidade) <em>e</em> aplica a alteração de negócio.",
              "<strong>Identificador já existe</strong> — a mensagem é duplicata e seu efeito não se repete.",
              "<strong>Falha antes do commit</strong> — tanto o registro do ID quanto a alteração são revertidos; a reentrega tentará de novo.",
              "<strong>Em transações separadas é inseguro</strong> — uma falha entre as etapas descarta uma mensagem cujo efeito nunca ocorreu.",
          ]) + "\n" +
          destaque("Para efeitos <strong>externos</strong> ao banco local, o inbox precisa ser combinado com "
                   "outbox, estados intermediários ou idempotência no próprio destino."),
          visual="flow"),
    slide(8, "Conteúdo", "At-least-once e efeito efetivamente único",
          ul([
              "<strong>Entrega pelo menos uma vez</strong> — a mensageria reentrega em caso de dúvida: duplicatas são <em>esperadas</em>, não excepcionais.",
              "<strong>“Exactly-once” dos produtos</strong> — existe dentro de limites específicos; o efeito de negócio ponta a ponta ainda depende das fronteiras transacionais.",
              "<strong>Efetivamente único</strong> — combina deduplicação, alteração de estado atômica e operações idempotentes.",
              "<strong>Chave por operação lógica</strong> — criada antes do primeiro envio, reutilizada em todas as retentativas daquela operação.",
              "<strong>Fronteira atômica</strong> — verificar/inserir a chave, aplicar a mudança e armazenar o resultado, tudo junto.",
              "<strong>No incidente do pagamento</strong> — as duas tentativas carregariam a mesma chave; o serviço devolveria o resultado registrado sem cobrar de novo.",
          ]), visual="map"),
    slide(8, "Conteúdo", "A saga completa da NexaOrder",
          p("Uma saga <strong>orquestrada</strong> para a compra, com as compensações explícitas:") + "\n" +
          tabela(["Etapa", "Transação local", "Compensação se falhar adiante"], [
              ["1", "Reservar estoque", "Liberar a reserva"],
              ["2", "Autorizar pagamento", "Estornar o valor autorizado"],
              ["3", "Confirmar pedido", "Marcar o pedido como cancelado"],
              ["4", "Solicitar expedição", "Cancelar a etiqueta antes do despacho"],
          ]) + "\n" +
          destaque("Cada etapa publica seu evento via <strong>outbox</strong>; cada consumidor grava o "
                   "<strong>inbox</strong> e o efeito de negócio na mesma transação local; e a <strong>chave de "
                   "idempotência</strong> da operação é reutilizada nas retentativas. Se a autorização falhar, a "
                   "compensação libera a reserva; se a expedição falhar depois do pagamento, estorna e libera.")),
    slide(8, "Transição", "O que a Unidade 3 vai perguntar",
          p("Esta unidade tratou de como os dados da NexaOrder são replicados, particionados, coordenados "
            "por consenso e mantidos coerentes por sagas. A Unidade 3 parte desse alicerce para tratar da "
            "organização dos <strong>próprios serviços</strong>:") + "\n" +
          ul([
              "Como decompor a NexaOrder em <strong>limites de domínio</strong> bem definidos?",
              "Como uma arquitetura <strong>orientada a eventos</strong> organiza produtores, consumidores e tópicos?",
              "Como <strong>contêineres e Kubernetes</strong> automatizam implantação e recuperação desses serviços?",
              "Como garantir <strong>comunicação segura</strong> e identidade entre eles?",
          ]) + "\n" +
          destaque("Os padrões <strong>outbox</strong> e as <strong>sagas</strong> estudados aqui reaparecem como "
                   "parte central da arquitetura orientada a eventos da próxima unidade.")),
    pontos_chave(8, [
        ("Atomicidade não se estende", "A garantia de um único banco não cobre operações que atravessam múltiplos serviços."),
        ("2PC bloqueia", "Garante atomicidade distribuída, mas prende recursos e fica vulnerável à falha do coordenador."),
        ("Saga compensa", "Substitui a transação única por transações locais encadeadas com ações compensatórias."),
        ("Coreografia ou orquestração", "A primeira dispensa coordenador; a segunda torna o fluxo explícito e rastreável."),
        ("Outbox e inbox", "Outbox elimina a escrita dupla; inbox só evita efeito duplicado se ID e alteração estiverem na mesma transação."),
        ("Idempotência fecha a conta", "Como a entrega é at-least-once, o efeito único depende de a operação ser idempotente."),
    ]),
    slide(8, "Atividade prática", "Mãos à obra: modelar a saga completa",
          p("Modele a saga pedido–estoque–pagamento–expedição e represente o resultado em um diagrama de "
            "fluxo com as etapas normais e as de compensação <strong>claramente distinguidas</strong>.") + "\n" +
          ul([
              "<strong>1.</strong> Liste as etapas na ordem correta e a ação compensatória de cada uma.",
              "<strong>2.</strong> Escolha entre coreografia e orquestração, justificando para este fluxo.",
              "<strong>3.</strong> Indique em quais etapas o padrão outbox deve ser aplicado, e por quê.",
              "<strong>4.</strong> Defina onde a chave de idempotência é criada, reutilizada e verificada.",
              "<strong>5.</strong> Mostre a fronteira transacional em que o consumidor grava o inbox e aplica o efeito.",
              "<strong>6.</strong> Explique o que ocorre se houver falha antes do commit dessa transação.",
          ]), visual="map"),
    encerramento(
        "Você fecha a Unidade 2 sabendo manter uma operação coerente entre quatro bancos independentes, sem "
        "coordenador bloqueante e sem duplicar efeitos. A Unidade 3 muda o foco dos dados para os serviços: "
        "limites de domínio, eventos, Kubernetes e comunicação segura.",
        "Próxima unidade: Unidade 3 — Serviços, eventos e plataformas cloud-native."),
])
