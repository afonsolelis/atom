# Unidade 3 — Serviços, eventos e plataformas cloud-native

Disciplina: Distributed Systems Engineering  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de produção: 25 de agosto de 2026

## Relação da unidade com a atuação profissional

Nas duas primeiras unidades, a NexaOrder foi analisada sob a ótica da comunicação, do tempo lógico, das falhas parciais, da replicação e do consenso. Esta unidade desloca o foco para uma pergunta que toda equipe de engenharia enfrenta ao crescer: como organizar pessoas, código e dados em serviços que possam evoluir, falhar e escalar de forma independente — e como executar esses serviços de maneira confiável em uma plataforma compartilhada?

Profissionais de desenvolvimento *backend*, arquitetura de software, plataforma, DevOps e *Site Reliability Engineering* (SRE) lidam diariamente com decisões que aparecem nesta unidade. Definir os limites de um serviço mal feito custa caro: gera acoplamento disfarçado de modularidade, obriga equipes a coordenar implantações simultâneas e transforma uma arquitetura "de microsserviços" em um monólito distribuído, que soma a complexidade operacional da distribuição aos problemas de acoplamento do monólito original. Compreender contexto delimitado, autonomia de dados e comunicação entre serviços evita esse resultado.

A adoção de arquiteturas orientadas a eventos também deixou de ser exclusividade de empresas de grande escala. Plataformas de mensageria e transmissão de eventos hoje sustentam desde sistemas de pagamento até aplicações de logística e telemetria industrial. Engenheiros que compreendem tópicos, partições, grupos de consumidores e semânticas de entrega conseguem projetar fluxos que sobrevivem a reprocessamento, duplicação e picos de carga sem depender de sorte operacional.

Da mesma forma, contêineres e orquestradores como o Kubernetes tornaram-se a camada de execução padrão de boa parte da indústria. Um profissional que entende o laço de reconciliação — a lógica que compara estado desejado e estado observado e age para aproximar um do outro — diagnostica incidentes com mais precisão do que alguém que apenas executa comandos de implantação sem compreender o que ocorre por trás deles. Essa compreensão é frequentemente o que diferencia quem apenas opera uma plataforma de quem consegue projetá-la e depurá-la sob pressão.

Por fim, a segurança da comunicação entre serviços deixou de ser uma preocupação isolada de times de segurança da informação. Identidade de serviço, autenticação mútua, gestão de segredos e confiança zero são hoje responsabilidades compartilhadas por desenvolvedores, arquitetos e equipes de plataforma. Um fluxo de pagamento mal protegido não é apenas um risco técnico: é um risco de negócio, regulatório e reputacional. Ao final desta unidade, o estudante estará mais preparado para propor arquiteturas de serviços que sejam, ao mesmo tempo, modulares, observáveis, escaláveis e defensáveis diante de auditorias e ataques.

## O que você verá nesta unidade

A Unidade 3 acompanha a NexaOrder em sua transição de uma coleção de serviços definidos de forma intuitiva para uma arquitetura de serviços, eventos e plataforma deliberadamente projetada. Na Aula 9, você aprenderá a distinguir monólitos, monólitos modulares e microsserviços, e a usar contexto delimitado e capacidade de negócio para desenhar fronteiras de serviço que reduzam acoplamento sem multiplicar coordenação. Na Aula 10, a comunicação síncrona estudada na Unidade 1 dará lugar a uma arquitetura orientada a eventos, com tópicos, partições, grupos de consumidores e semânticas de entrega. Na Aula 11, você entrará na camada de execução: contêineres, Kubernetes e o laço de reconciliação que sustenta a recuperação automática de instâncias. Por fim, na Aula 12, a unidade se encerra com identidade de serviço, autenticação, criptografia em trânsito, gestão de segredos e *service mesh* — os mecanismos que tornam a comunicação entre serviços confiável mesmo em uma rede hostil.

O fio condutor continua sendo a NexaOrder. Os mesmos quatro serviços já apresentados — pedidos, estoque, pagamento e expedição — serão reorganizados, conectados por eventos, implantados em um cluster Kubernetes e protegidos por mecanismos de autenticação e autorização. Cada aula acrescenta uma camada à arquitetura sem descartar o que já foi construído nas unidades anteriores.

## Aula 9 — Decomposição em serviços e limites de domínio

### Situação-problema: dividir não é o mesmo que desacoplar

A NexaOrder já opera com quatro serviços aparentemente independentes: pedidos, estoque, pagamento e expedição. Ainda assim, a equipe de engenharia percebe sintomas incômodos. Uma alteração no formato do pedido frequentemente exige mudanças simultâneas no serviço de estoque, porque os dois compartilham a mesma tabela de itens em um banco de dados comum. As implantações precisam ser coordenadas: liberar o serviço de pagamento sem atualizar o serviço de pedidos no mesmo dia quebra o fluxo de checkout. E, apesar do nome "serviços", qualquer incidente em produção ainda exige que praticamente todo o time esteja disponível, porque poucas pessoas conhecem apenas uma parte do sistema.

Esses sintomas indicam que a separação existente foi feita por conveniência técnica — talvez inicialmente para distribuir carga, como discutido na Aula 1 — e não a partir de limites de negócio bem definidos. O resultado é um **monólito distribuído**: um sistema que paga o custo operacional da distribuição (rede, serialização, falhas parciais) sem colher o principal benefício da divisão em serviços, que é a autonomia de evolução e implantação. Esta aula estabelece os critérios para desenhar fronteiras de serviço que efetivamente desacoplem times, dados e ciclos de implantação.

### Monólito, monólito modular e microsserviços

Três formas de organizar um sistema aparecem com frequência em discussões arquiteturais, e é importante não tratá-las como um espectro linear de "pior" a "melhor".

- **Monólito:** todo o comportamento do sistema é implantado como uma única unidade executável. Módulos internos podem existir no código, mas o *deploy*, o processo e, em geral, o banco de dados são compartilhados.
- **Monólito modular:** mantém uma única unidade de implantação, mas impõe fronteiras internas rígidas entre módulos, com interfaces explícitas e, idealmente, esquemas de dados segregados dentro do mesmo banco. É uma arquitetura legítima, não apenas uma etapa de transição.
- **Microsserviços:** cada serviço é implantável, escalável e substituível de forma independente, possui seu próprio armazenamento de dados e se comunica com os demais por contratos explícitos, síncronos ou assíncronos.

Nenhuma das três opções é universalmente superior. Um monólito modular bem projetado pode ser mais barato de operar do que dezenas de microsserviços mal delimitados, especialmente em times pequenos. A escolha depende de requisitos de escala, de autonomia organizacional e da maturidade operacional disponível — o mesmo raciocínio de custo, benefício e evidência apresentado na Aula 1.

### Coesão, acoplamento e autonomia

Dois conceitos emprestados da engenharia de software orientam o desenho de fronteiras: **coesão**, o grau em que os elementos internos de um componente estão relacionados entre si e mudam juntos; e **acoplamento**, o grau em que um componente depende de detalhes internos de outro. Um bom limite de serviço maximiza coesão interna e minimiza acoplamento externo.

Um heurístico emprestado do desenho de componentes de software — e adaptável, com cautela, ao nível de serviços — é a métrica de instabilidade proposta por Robert C. Martin. Sejam $C_a$ o acoplamento aferente (quantos outros componentes dependem deste) e $C_e$ o acoplamento eferente (de quantos outros componentes este depende):

$$
I = \frac{C_e}{C_a + C_e}
$$

$I$ varia de 0 (totalmente estável, muito dependido e pouco dependente) a 1 (totalmente instável, muito dependente e pouco dependido). Suponha que o serviço de estoque da NexaOrder seja consultado por pedidos, pagamento e um painel administrativo ($C_a = 3$) e dependa apenas do serviço de catálogo para validar categorias de item ($C_e = 1$):

$$
I_{\text{estoque}} = \frac{1}{3 + 1} = 0{,}25
$$

Um valor baixo sugere um serviço relativamente estável, adequado para concentrar regras centrais de domínio, já que mudanças nele tendem a propagar impacto para outros. Serviços com instabilidade alta — muitos consumidores externos e poucas dependências — tendem a tolerar melhor mudanças frequentes. A métrica não substitui julgamento de negócio, mas transforma uma impressão subjetiva de "esse serviço está muito enredado" em um número discutível pela equipe.

### Contexto delimitado e capacidade de negócio

O *Domain-Driven Design* oferece dois conceitos particularmente úteis para desenhar fronteiras: **contexto delimitado** (*bounded context*), a fronteira dentro da qual um modelo de domínio e sua linguagem têm significado consistente; e **capacidade de negócio** (*business capability*), algo que a organização faz para gerar valor, como "gerenciar estoque" ou "processar pagamentos", independentemente de como isso é implementado.

Na NexaOrder, a palavra "item" significa coisas diferentes em contextos diferentes. Para o catálogo, um item é uma descrição comercial com preço, imagens e categorias. Para o estoque, o mesmo item é uma quantidade física disponível em um depósito, com número de série e localização. Tratar essas duas visões como o mesmo modelo de dados compartilhado é uma fonte comum de acoplamento acidental: uma mudança no significado de "item" para o catálogo pode quebrar silenciosamente o controle de estoque. Reconhecer contextos delimitados diferentes autoriza — e recomenda — que cada serviço mantenha seu próprio modelo, mesmo que ambos se refiram, em linguagem natural, ao "mesmo" conceito.

### Dados por serviço

Uma consequência direta de contextos delimitados bem definidos é o princípio de **dados por serviço**: cada serviço possui e controla seu próprio armazenamento, e nenhum outro serviço acessa esse armazenamento diretamente — nem por leitura. Toda interação passa por um contrato explícito: uma API, uma mensagem ou um evento publicado.

Esse princípio parece custoso à primeira vista, porque elimina a conveniência de um `JOIN` entre tabelas de serviços diferentes. O custo é deliberado: sem ele, qualquer alteração de esquema em um serviço pode quebrar consumidores que leem sua tabela diretamente, e a "fronteira do serviço" deixa de existir na prática, mesmo que exista um repositório de código separado. A NexaOrder havia cometido exatamente esse erro ao permitir que pedidos e pagamento lessem a mesma tabela de itens do estoque.

### API Gateway e composição

Quando um cliente externo — aplicativo móvel, painel administrativo ou parceiro comercial — precisa de dados que vêm de múltiplos serviços, expor todos os serviços diretamente cria acoplamento entre a topologia interna e os consumidores externos, além de multiplicar preocupações de autenticação e limitação de taxa em cada serviço.

Um **API Gateway** concentra o ponto de entrada externo. Ele pode rotear requisições para o serviço correto, agregar respostas de múltiplos serviços em uma única resposta (**composição**), aplicar autenticação, limitar taxa de requisições e ocultar a decomposição interna. Uma tela de detalhes do pedido na NexaOrder, por exemplo, pode exigir dados de pedidos, estoque e expedição; o gateway consulta os três e devolve uma resposta única ao cliente, evitando que o aplicativo móvel precise conhecer three serviços distintos e orquestrar as chamadas por conta própria.

O gateway não deve, porém, acumular regras de negócio. Quando isso acontece, ele se transforma em um novo monólito escondido atrás de uma fachada de microsserviços — um risco discutido adiante.

> **Recurso visual 1 — Mapa de contextos delimitados da NexaOrder:** representar catálogo, estoque, pedidos, pagamento e expedição como círculos com fronteiras destacadas, indicando que "item" tem significado próprio em catálogo e em estoque.  
> **Texto alternativo:** diagrama de contextos delimitados mostra cinco áreas de negócio da NexaOrder com fronteiras explícitas e uma anotação de que o conceito "item" varia de significado entre catálogo e estoque.

### Comunicação entre serviços

A comunicação entre serviços recupera temas da Aula 2: chamadas síncronas (HTTP, RPC) oferecem simplicidade e resposta imediata, mas propagam indisponibilidade — se o serviço de pagamento está lento, quem o chama de forma síncrona também fica lento. Chamadas assíncronas, por mensagens ou eventos (tema da próxima aula), reduzem esse acoplamento temporal, ao custo de maior complexidade de raciocínio sobre consistência.

Um sintoma de fronteiras mal desenhadas é a **comunicação excessivamente conversacional** (*chatty communication*): um único caso de uso do cliente dispara dezenas de chamadas remotas entre serviços para ser concluído. Isso costuma indicar que a fronteira foi traçada no lugar errado — talvez duas responsabilidades fortemente relacionadas tenham sido separadas sem necessidade.

> **Recurso visual 2 — Banco de dados compartilhado versus dados por serviço:** dois diagramas lado a lado; o primeiro mostra pedidos, estoque e pagamento acessando a mesma tabela de itens; o segundo mostra cada serviço com seu próprio armazenamento, comunicando-se por contratos explícitos.  
> **Texto alternativo:** comparação visual entre uma arquitetura com banco de dados compartilhado, sujeita a acoplamento oculto, e uma arquitetura com dados isolados por serviço.

### Riscos do monólito distribuído

Alguns sinais recorrentes ajudam a diagnosticar um monólito distribuído:

- implantações de serviços diferentes precisam ser coordenadas no mesmo horário;
- qualquer mudança de esquema em um serviço quebra outros serviços;
- um incidente em um serviço exige presença de praticamente todo o time;
- serviços compartilham diretamente tabelas, filas ou segredos sem contrato explícito;
- a topologia de chamadas para um único caso de uso é profunda e conversacional;
- times não conseguem testar ou implantar seus serviços sem depender de outros times no mesmo instante.

Nenhum desses sintomas isolados é definitivo, mas a presença de vários ao mesmo tempo indica que a divisão física em repositórios ou processos não produziu autonomia real.

> **Recurso visual 3 — Composição via API Gateway:** ilustrar um aplicativo cliente enviando uma única requisição a um gateway, que consulta pedidos, estoque e expedição em paralelo e devolve uma resposta agregada.  
> **Texto alternativo:** diagrama mostra um gateway central recebendo uma requisição do cliente e distribuindo chamadas para três serviços, compondo uma resposta única.

### Do diagnóstico à decisão de fronteira

Assim como na Aula 1, uma decisão de fronteira de serviço deveria explicitar requisito, decisão, compromisso e evidência. Para a NexaOrder:

- requisito: eliminar a necessidade de coordenar implantações entre pedidos e estoque;
- decisão: separar o modelo de "item de catálogo" do modelo de "unidade em estoque", com armazenamento próprio para cada serviço e comunicação por eventos de reserva e liberação;
- compromisso: consultas que hoje usam `JOIN` local precisarão ser reconstruídas por composição ou por réplicas de leitura assíncronas, com atraso de propagação;
- evidência: número de implantações que exigiram coordenação simultânea antes e depois da mudança, medido ao longo de um trimestre.

> **Recurso visual 4 — Checklist de sintomas do monólito distribuído:** quadro com os seis sintomas listados, para uso como roteiro de autodiagnóstico em uma retrospectiva de arquitetura.  
> **Texto alternativo:** lista visual de verificação com seis sintomas típicos de um monólito distribuído, usada como ferramenta de diagnóstico em equipe.

### Atividade prática

Defina os limites de serviço da NexaOrder a partir do estado atual descrito nesta aula.

1. Liste as capacidades de negócio da NexaOrder (catálogo, estoque, pedidos, pagamento, expedição e outras que você julgar necessárias).
2. Para cada capacidade, identifique o contexto delimitado correspondente e registre onde o significado de um termo comum (como "item" ou "pedido") muda entre contextos.
3. Proponha a divisão de serviços resultante, indicando qual serviço possui qual armazenamento de dados.
4. Calcule a instabilidade aproximada ($I = C_e / (C_a + C_e)$) de dois serviços da sua proposta, a partir de dependências que você mesmo estimar.
5. Liste três sintomas de monólito distribuído que a nova divisão elimina e um novo risco que ela introduz.

O resultado deve caber em um diagrama e uma tabela de justificativas, permitindo que outra pessoa da equipe compreenda a fronteira proposta sem precisar de explicação verbal adicional.

### Síntese da aula

- Monólito, monólito modular e microsserviços são opções arquiteturais válidas; a escolha depende de requisitos, não de tendência.
- Coesão alta dentro do serviço e acoplamento baixo entre serviços orientam o desenho de fronteiras.
- Contexto delimitado e capacidade de negócio ajudam a identificar onde um mesmo termo muda de significado.
- Dados por serviço evita acoplamento oculto por esquema compartilhado, ao custo de composição explícita entre serviços.
- Um API Gateway concentra composição e políticas transversais, mas não deve acumular regras de negócio.
- Comunicação excessivamente conversacional e implantações coordenadas são sintomas de monólito distribuído.
- Toda decisão de fronteira deve explicitar requisito, decisão, compromisso e evidência.

### Roteiro da Videoaula 9 — “Serviços separados, mas ainda amarrados: como desenhar fronteiras de verdade”

O roteiro falado e as indicações de edição serão desenvolvidos no arquivo `roteiros_20min.md`, usando o diagnóstico do monólito distribuído da NexaOrder como demonstração central.

### Referências da aula

- DRAGONI, N. et al. Microservices: yesterday, today, and tomorrow. In: MAZZARA, M.; MEYER, B. (org.). *Present and Ulterior Software Engineering*. Cham: Springer, 2017. DOI: 10.1007/978-3-319-67425-4_12.
- NEWMAN, Sam. *Building Microservices*. 2. ed. Sebastopol: O'Reilly Media, 2021.
- RICHARDSON, Chris. *Microservices Patterns*. Shelter Island: Manning, 2018.

## Aula 10 — Arquitetura orientada a eventos

### Situação-problema: quando a cadeia de chamadas síncronas quebra tudo

Com fronteiras de serviço mais claras, a NexaOrder ainda enfrenta um problema. O fluxo de checkout chama o serviço de pedidos, que chama de forma síncrona o serviço de estoque, que chama de forma síncrona o serviço de pagamento, que chama de forma síncrona o serviço de expedição. Se qualquer um desses serviços estiver lento, a cadeia inteira fica lenta; se qualquer um estiver indisponível, o pedido falha por completo, mesmo quando a indisponibilidade é temporária e afeta apenas uma etapa não urgente, como a notificação de expedição.

A equipe decide reorganizar parte da comunicação em torno de eventos: fatos que já aconteceram e que outros serviços podem observar e reagir, no seu próprio ritmo, sem bloquear quem os publicou. Esta aula constrói o vocabulário e os mecanismos necessários para projetar esse tipo de arquitetura.

### Evento de domínio, comando e notificação

É comum confundir três tipos de mensagem em sistemas orientados a eventos:

- **Comando:** uma solicitação para que algo aconteça, endereçada a um destinatário específico, que pode aceitar ou recusar (por exemplo, "reservar 1 unidade do item X").
- **Evento de domínio:** o registro de um fato que já ocorreu, publicado sem destinatário específico (por exemplo, "pedido 4021 criado", "pagamento 4021 aprovado").
- **Notificação:** um aviso leve de que algo aconteceu, geralmente sem os dados completos do evento, convidando o interessado a buscar mais informação se necessário.

A distinção importa porque comandos criam acoplamento direto (quem envia sabe quem deve receber e espera uma resposta de aceitação), enquanto eventos de domínio favorecem baixo acoplamento (quem publica não sabe, e não precisa saber, quem consome). A arquitetura orientada a eventos da NexaOrder passa a tratar "pedido criado", "estoque reservado", "pagamento aprovado" e "pedido expedido" como eventos de domínio publicados por seus respectivos serviços.

### Produtores, consumidores, tópicos e partições

Uma plataforma de transmissão de eventos organiza mensagens em **tópicos**, canais nomeados por tipo de evento ou por agregado de negócio. **Produtores** publicam eventos em um tópico; **consumidores** leem esses eventos, tipicamente sem remover a mensagem para outros consumidores, o que permite que múltiplos serviços processem o mesmo evento de forma independente.

Para permitir paralelismo e escala, um tópico é dividido em **partições**. Cada partição mantém uma sequência ordenada e imutável de eventos, identificada por um deslocamento (*offset*) crescente. Um evento publicado em um tópico é direcionado a uma partição específica, geralmente com base em uma **chave** (por exemplo, o identificador do pedido), garantindo que todos os eventos daquele pedido caiam na mesma partição.

### Ordenação por partição

A plataforma garante ordem **dentro** de uma partição, não entre partições diferentes. Se todos os eventos do pedido 4021 usam a chave "4021", eles chegarão na mesma partição e serão lidos na ordem em que foram publicados: criado, estoque reservado, pagamento aprovado, expedido. Eventos de pedidos diferentes podem ser processados fora de ordem relativa entre si, o que geralmente não é um problema, já que pertencem a agregados de negócio distintos.

Escolher mal a chave de particionamento compromete essa garantia. Se a NexaOrder particionasse por região geográfica em vez de por identificador de pedido, dois eventos do mesmo pedido processados em regiões diferentes poderiam cair em partições distintas e chegar fora de ordem ao consumidor.

### Grupos de consumidores

Um **grupo de consumidores** é um conjunto de instâncias que dividem entre si o trabalho de consumir as partições de um tópico, de modo que cada partição seja atribuída a exatamente uma instância do grupo em um dado momento. Isso permite escalar o processamento horizontalmente: com um tópico de 6 partições e um grupo de 3 consumidores, cada instância processa, em média, 2 partições.

Grupos diferentes são independentes entre si: o grupo que atualiza o painel operacional da NexaOrder e o grupo que dispara e-mails de confirmação podem consumir o mesmo tópico de eventos de pedido, cada um em seu próprio ritmo, sem interferir um no outro.

Um exemplo numérico de dimensionamento: se um tópico precisa sustentar uma taxa de pico de $\lambda_{\text{pico}} = 1200$ eventos por segundo e cada consumidor processa, de forma sustentável, $C_{\text{consumidor}} = 150$ eventos por segundo, o número mínimo de partições — e, portanto, o limite superior de paralelismo útil do grupo de consumidores — é:

$$
P = \left\lceil \frac{\lambda_{\text{pico}}}{C_{\text{consumidor}}} \right\rceil
= \left\lceil \frac{1200}{150} \right\rceil = 8
$$

Adicionar um nono consumidor ao grupo não aumentaria o throughput, porque não haveria uma nona partição para atribuir a ele; a instância ficaria ociosa. O número de partições é, portanto, um limite estrutural de paralelismo que deve ser definido com folga em relação à carga de pico esperada.

Um grupo de consumidores também se reorganiza automaticamente diante de falhas, em um processo chamado **rebalanceamento**: se uma instância falha, as partições que estavam sob sua responsabilidade são redistribuídas entre as instâncias remanescentes do mesmo grupo. Se um grupo de 3 instâncias responsável por 8 partições perde uma instância, as 2 restantes passam a dividir as 8 partições entre si — o processamento continua, ainda que com throughput reduzido por instância, até que uma nova réplica seja adicionada. Esse comportamento reproduz, na camada de consumo de eventos, o mesmo princípio de redundância sem ponto único de falha discutido na Aula 1.

> **Recurso visual 1 — Tópico com partições e grupo de consumidores:** diagrama de um tópico "eventos-pedido" com 8 partições, chaves por identificador de pedido, e duas instâncias de um grupo de consumidores dividindo as partições entre si.  
> **Texto alternativo:** diagrama mostra oito partições de um tópico distribuídas entre instâncias de um grupo de consumidores, cada partição atribuída a exatamente uma instância.

### Retenção e reprocessamento

Diferente de uma fila tradicional, em que uma mensagem é removida após ser consumida, uma plataforma de eventos costuma reter mensagens por um período configurável — horas, dias ou de forma indefinida — independentemente de terem sido lidas. Isso permite **reprocessamento**: um novo consumidor pode ser iniciado do início da retenção para reconstruir um estado a partir do histórico completo de eventos, ou um consumidor existente pode retroceder seu deslocamento para corrigir um erro de processamento identificado após a publicação original.

Para a NexaOrder, essa propriedade permite, por exemplo, reconstruir o painel de métricas de vendas do zero após uma correção de bug no serviço que o alimenta, sem precisar de um mecanismo de exportação separado — os eventos já publicados são a fonte da verdade.

O período de retenção é uma decisão de custo e utilidade, não uma configuração "quanto mais, melhor" por padrão. Reter eventos por sete dias, por exemplo, permite corrigir um defeito percebido numa segunda-feira reprocessando o histórico completo da semana anterior; reter por poucas horas praticamente elimina essa possibilidade, ao custo de menor armazenamento; reter indefinidamente aproxima o tópico de um registro histórico completo, útil para auditoria, mas com custo de armazenamento crescente ao longo do tempo. A escolha, portanto, deve explicitar o requisito de recuperação e auditoria que está sendo atendido, assim como qualquer outra decisão arquitetural desta disciplina.

### Semânticas de entrega: at-most-once, at-least-once e exactly-once

A entrega de um evento entre produtor e consumidor está sujeita às mesmas falhas parciais discutidas na Aula 4: uma mensagem pode não chegar, um reconhecimento pode se perder, um consumidor pode falhar após processar mas antes de confirmar. Três semânticas descrevem o comportamento resultante:

- **At-most-once:** cada evento é entregue zero ou uma vez; nunca duplicado, mas pode ser perdido. Ocorre quando o consumidor confirma o recebimento antes de concluir o processamento.
- **At-least-once:** cada evento é entregue uma ou mais vezes; nunca perdido, mas pode ser duplicado. Ocorre quando o consumidor confirma apenas após concluir o processamento, e uma falha entre o processamento e a confirmação leva a uma nova entrega.
- **Exactly-once:** cada evento produz exatamente um efeito observável, mesmo diante de reentregas. Não elimina a duplicação na transmissão, mas a torna invisível para o efeito final, normalmente combinando at-least-once com deduplicação ou operações idempotentes no consumidor — o mesmo princípio de idempotência estudado na Aula 8.

Na prática, a maioria das plataformas de eventos amplamente utilizadas oferece garantias fortes de at-least-once por padrão, deixando a responsabilidade de alcançar um comportamento efetivamente único para o desenho do consumidor. A NexaOrder, por exemplo, faz o consumidor de "pagamento aprovado" verificar se o identificador do evento já foi processado antes de disparar a expedição, absorvendo duplicações sem efeito duplicado.

> **Recurso visual 2 — Três semânticas de entrega lado a lado:** três linhas do tempo comparando at-most-once (mensagem perdida), at-least-once (mensagem duplicada) e exactly-once (efeito único apesar de duplicação na transmissão).  
> **Texto alternativo:** comparação visual entre as três semânticas de entrega, evidenciando perda, duplicação e efeito único conforme o caso.

### Evolução de esquemas e compatibilidade

Eventos publicados hoje podem ser consumidos por serviços implantados semanas depois, e um consumidor antigo pode continuar em produção enquanto o produtor já publica um novo formato. Por isso, o esquema de um evento deve evoluir de forma controlada:

- **compatibilidade retroativa (backward):** um consumidor com o esquema novo consegue ler eventos publicados com o esquema antigo;
- **compatibilidade prospectiva (forward):** um consumidor com o esquema antigo consegue ler eventos publicados com o esquema novo, geralmente ignorando campos desconhecidos;
- mudanças seguras tendem a ser aditivas (novos campos opcionais); remover ou renomear um campo existente, ou alterar seu tipo, costuma quebrar compatibilidade e exige uma estratégia explícita de migração, como publicar temporariamente em dois formatos.

Se a NexaOrder decidir adicionar um campo `canal_venda` ao evento "pedido criado", consumidores antigos que ignoram campos desconhecidos continuam funcionando; se decidir renomear `valor_total` para `valor_liquido` sem transição, qualquer consumidor não atualizado passará a interpretar o pedido como se não tivesse valor.

> **Recurso visual 3 — Evolução de esquema:** diagrama mostrando um evento v1 com campos base, um evento v2 com um campo opcional adicionado, e um consumidor v1 lendo o evento v2 sem erro.  
> **Texto alternativo:** diagrama de evolução de esquema evidenciando adição de campo opcional preservando compatibilidade retroativa e prospectiva.

### Comandos, eventos e a NexaOrder reorganizada

Reunindo os elementos desta aula, o fluxo de pedidos da NexaOrder pode ser reorganizado da seguinte forma: o serviço de pedidos recebe um comando síncrono do cliente ("criar pedido"), valida a solicitação e, em caso de sucesso, publica o evento de domínio "pedido criado". O serviço de estoque consome esse evento, tenta reservar os itens e publica "estoque reservado" ou "estoque indisponível". O serviço de pagamento consome "estoque reservado" e publica "pagamento aprovado" ou "pagamento recusado". O serviço de expedição consome "pagamento aprovado" e publica "pedido expedido". Nenhum desses serviços chama o seguinte de forma síncrona e bloqueante; cada um reage a fatos publicados no seu próprio ritmo.

> **Recurso visual 4 — Fluxo de eventos do pedido:** linha do tempo com os quatro serviços da NexaOrder publicando e consumindo eventos em sequência, sem chamadas síncronas diretas entre eles.  
> **Texto alternativo:** diagrama de fluxo orientado a eventos mostra pedidos, estoque, pagamento e expedição conectados exclusivamente por eventos publicados e consumidos, sem chamadas síncronas diretas.

### Atividade prática

Desenhe os tópicos, chaves e grupos de consumidores para o ciclo de vida do pedido na NexaOrder.

1. Liste os eventos de domínio do ciclo do pedido (mínimo quatro), definindo para cada um o tópico e a chave de particionamento.
2. Justifique a escolha da chave em termos de ordenação necessária.
3. Defina pelo menos dois grupos de consumidores distintos que leem o mesmo tópico com finalidades diferentes (por exemplo, expedição e métricas).
4. Calcule o número mínimo de partições necessário para sustentar uma taxa de pico hipotética, usando a fórmula apresentada nesta aula.
5. Descreva qual semântica de entrega (at-least-once, at-most-once ou exactly-once por deduplicação) cada consumidor deveria adotar e por quê.

### Síntese da aula

- Comandos, eventos de domínio e notificações têm propósitos e níveis de acoplamento diferentes.
- Tópicos e partições organizam eventos; a ordem só é garantida dentro de uma partição.
- A chave de particionamento determina quais eventos permanecem ordenados entre si.
- Grupos de consumidores permitem paralelismo horizontal, limitado pelo número de partições.
- Retenção possibilita reprocessamento e reconstrução de estado a partir do histórico.
- At-most-once, at-least-once e exactly-once descrevem compromissos diferentes entre perda e duplicação.
- Evolução de esquema exige mudanças aditivas e compatibilidade explícita entre versões.

### Roteiro da Videoaula 10 — “Parar de esperar: como eventos desacoplam o ciclo do pedido”

O roteiro falado e as indicações de edição serão desenvolvidos no arquivo `roteiros_20min.md`, usando a reorganização do fluxo de checkout da NexaOrder como demonstração central.

### Referências da aula

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O'Reilly Media, 2017.
- NEWMAN, Sam. *Building Microservices*. 2. ed. Sebastopol: O'Reilly Media, 2021.
- Apache Kafka Documentation. Disponível em: <https://kafka.apache.org/documentation/>.

## Aula 11 — Contêineres, Kubernetes e reconciliação

### Situação-problema: a instância que se recupera sozinha (e a que não deveria)

Com serviços mais bem delimitados e comunicação orientada a eventos, a NexaOrder precisa decidir como executar tudo isso de forma confiável. Em uma madrugada de alta demanda, uma instância do serviço de pagamento trava e para de responder. Minutos depois, sem qualquer intervenção humana, uma nova instância aparece no lugar, assume o tráfego e o incidente praticamente passa despercebido pelos usuários. A equipe de plantão, porém, fica intrigada: quem decidiu recriar a instância? Como o sistema sabia que ela deveria existir? E se a causa do travamento fosse um defeito que volta a acontecer a cada reinício?

Essa recuperação automática não é mágica: é o resultado de contêineres imutáveis executando sobre um orquestrador — nesta disciplina, o Kubernetes — que mantém continuamente um **laço de reconciliação** entre o que deveria existir e o que de fato existe. Compreender esse laço é o que permite diferenciar uma recuperação saudável de um sintoma que está sendo mascarado.

### Imagem, contêiner e imutabilidade

Uma **imagem de contêiner** é um pacote autocontido com o código da aplicação, suas dependências e as instruções necessárias para executá-la, construído a partir de camadas imutáveis. Um **contêiner** é uma instância em execução dessa imagem, isolada em termos de processos, sistema de arquivos e, em geral, rede, mas compartilhando o núcleo do sistema operacional do hospedeiro — diferente de uma máquina virtual completa.

A **imutabilidade** é uma convenção central: em vez de corrigir uma instância em execução, a prática recomendada é publicar uma nova imagem e substituir os contêineres antigos por novos, criados a partir dela. Isso elimina a divergência silenciosa entre ambientes — o problema clássico de "funciona na minha máquina" — porque a imagem publicada é exatamente o que roda em produção, sem alterações manuais posteriores.

### Cluster, nó, Pod, Deployment e Service

O Kubernetes organiza a execução de contêineres em torno de alguns objetos centrais:

- **Cluster:** o conjunto de máquinas (nós) gerenciadas como uma unidade.
- **Nó (node):** uma máquina, física ou virtual, que executa contêineres.
- **Pod:** a menor unidade implantável do Kubernetes; agrupa um ou mais contêineres que compartilham rede e armazenamento local, geralmente executados juntos porque são fortemente relacionados.
- **Deployment:** um objeto que declara quantas réplicas de um Pod devem existir e como atualizações devem ser aplicadas ao longo do tempo.
- **Service:** um objeto que expõe um conjunto de Pods sob um endereço de rede estável, mesmo quando Pods individuais são substituídos.

Na NexaOrder, o serviço de pagamento seria representado por um Deployment com, por exemplo, quatro réplicas de um Pod, e um Service estável que outros serviços usam para alcançá-lo, sem precisar conhecer os endereços de rede voláteis de cada Pod individual.

### Estado desejado e estado observado

O conceito central do Kubernetes é a separação entre **estado desejado** — o que um usuário declarou, por exemplo, em um manifesto — e **estado observado**, a condição real do cluster em um dado momento. O usuário não instrui o Kubernetes passo a passo sobre como criar uma instância; ele declara "quero quatro réplicas saudáveis deste Pod" e delega ao sistema a responsabilidade de alcançar e manter esse estado.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: pagamento
spec:
  replicas: 4
  template:
    spec:
      containers:
        - name: pagamento
          image: nexaorder/pagamento:1.7.0
```

Esse manifesto simplificado declara o estado desejado: quatro réplicas do contêiner de imagem `nexaorder/pagamento:1.7.0`. Se apenas três estiverem em execução no momento seguinte — porque uma travou —, existe uma divergência entre desejado e observado.

### Controladores e o laço de reconciliação

Um **controlador** é um processo que observa continuamente o estado atual, compara com o estado desejado e executa ações para reduzir a diferença entre os dois — o **laço de reconciliação**. Esse laço não é executado uma única vez; ele roda indefinidamente, em ciclos curtos, reagindo tanto a mudanças declaradas por humanos quanto a mudanças observadas no ambiente, como a falha de um Pod.

Quando a instância de pagamento trava na situação-problema desta aula, o controlador de Deployment observa que apenas três dos quatro Pods desejados estão saudáveis e cria um novo Pod para restaurar o número declarado. Esse comportamento é o que produz a recuperação automática percebida pela equipe de plantão — sem que ninguém precise executar um comando manual.

É importante reconhecer o limite dessa automação: o laço de reconciliação restaura a **quantidade** e o **estado de execução** declarados, não a **causa raiz** de uma falha recorrente. Se o Pod trava repetidamente por um defeito de código sob determinada condição de carga, o Kubernetes continuará recriando-o indefinidamente — um padrão conhecido como reinício em loop —, mascarando um problema que precisa de diagnóstico humano.

Mas como o Kubernetes sabe, na prática, que um Pod deixou de estar saudável? Essa percepção depende de **sondas** configuradas pela equipe responsável pelo serviço. Uma **sonda de vivacidade** (*liveness probe*) verifica periodicamente se o processo dentro do contêiner ainda responde; se deixar de responder, o Pod é considerado não saudável e substituído. Uma **sonda de prontidão** (*readiness probe*) verifica se o Pod já está apto a receber tráfego — útil logo após a inicialização, quando o processo já existe, mas ainda pode estar carregando configuração; um Pod que falha na sonda de prontidão é temporariamente removido dos destinos válidos de um Service, sem ser recriado. Sondas mal configuradas — por exemplo, uma sonda de vivacidade que verifica apenas se uma porta de rede está aberta, sem checar se o serviço realmente processa uma requisição de negócio — podem indicar "saudável" para um Pod que já não cumpre sua função, escondendo o problema do próprio laço de reconciliação que deveria corrigi-lo.

> **Recurso visual 1 — Laço de reconciliação:** diagrama circular com três etapas — observar estado atual, comparar com estado desejado, agir para reduzir a diferença — retornando ao início.  
> **Texto alternativo:** diagrama circular ilustra o laço de reconciliação do Kubernetes, com as etapas observar, comparar e agir se repetindo continuamente.

### Descoberta e balanceamento

Como Pods são substituídos com frequência e recebem endereços de rede internos voláteis, os serviços não podem se comunicar apontando diretamente para um Pod específico. Um **Service** resolve isso associando um nome estável e um endereço fixo a um conjunto de Pods selecionados por rótulos, distribuindo o tráfego recebido entre os Pods saudáveis disponíveis — uma forma de **descoberta de serviço** combinada com **balanceamento de carga** interno ao cluster.

Quando o serviço de estoque da NexaOrder precisa consultar o serviço de pagamento, ele se comunica com o nome estável do Service correspondente; o Kubernetes se encarrega de rotear essa chamada para uma das réplicas saudáveis do Deployment de pagamento, mesmo que os Pods por trás desse Service tenham sido recriados dezenas de vezes ao longo do dia.

### Configuração, segredos e armazenamento

Contêineres imutáveis não devem embutir configuração específica de ambiente ou credenciais na própria imagem. O Kubernetes separa essas preocupações em objetos próprios: **ConfigMaps**, para configuração não sensível (como o nome de um tópico de eventos), e **Secrets**, para dados sensíveis (como credenciais de acesso a um provedor de pagamento), ambos injetados nos Pods em tempo de execução, sem alterar a imagem publicada.

Para dados que precisam sobreviver à substituição de um Pod — o que Pods, por padrão, não garantem, já que seu armazenamento local é efêmero —, o Kubernetes oferece mecanismos de **armazenamento persistente**, que vinculam um volume de disco ao ciclo de vida de uma aplicação, independentemente de qual Pod específico o está usando em um dado momento.

> **Recurso visual 2 — Service roteando para Pods saudáveis:** diagrama de um Service estável recebendo tráfego e distribuindo entre três Pods do Deployment de pagamento, com um quarto Pod recém-substituído.  
> **Texto alternativo:** diagrama mostra um Service central distribuindo tráfego para pods saudáveis de um Deployment, com um pod adicional sendo recriado ao fundo.

### Escalonamento e atualizações graduais

O **escalonamento automático horizontal** (*Horizontal Pod Autoscaler*) ajusta o número de réplicas de um Deployment com base em métricas observadas, como utilização de CPU. A fórmula usada pelo Kubernetes para calcular o número desejado de réplicas, de forma simplificada, é:

$$
N_{\text{desejado}} = \left\lceil N_{\text{atual}} \times \frac{U_{\text{atual}}}{U_{\text{alvo}}} \right\rceil
$$

Se o Deployment de pagamento da NexaOrder possui $N_{\text{atual}} = 4$ réplicas, a utilização média observada de CPU é $U_{\text{atual}} = 85\%$ e o alvo configurado é $U_{\text{alvo}} = 60\%$:

$$
N_{\text{desejado}} = \left\lceil 4 \times \frac{85}{60} \right\rceil = \left\lceil 5{,}67 \right\rceil = 6
$$

O autoescalonador ajustaria o Deployment para seis réplicas, e o laço de reconciliação se encarregaria de criar os dois novos Pods necessários para atingir esse novo estado desejado.

**Atualizações graduais** (*rolling updates*) aplicam uma nova versão de imagem substituindo réplicas antigas por novas de forma incremental, respeitando limites configuráveis de quantas réplicas podem ficar indisponíveis ou excedentes durante a transição, para que a atualização não derrube a capacidade total do serviço.

Um exemplo concreto ajuda a fixar o mecanismo. Se o Deployment de pagamento possui 6 réplicas e a atualização é configurada para permitir, no máximo, 1 réplica indisponível e 1 réplica excedente durante a transição, o Kubernetes cria inicialmente 1 Pod com a versão nova — totalizando 7 Pods, 6 antigos e 1 novo —, aguarda esse Pod passar na sonda de prontidão e só então remove 1 Pod antigo, voltando a 6 no total. O ciclo se repete até que todas as réplicas estejam na versão nova, sem que a capacidade saudável caia abaixo de 5 nem ultrapasse 7 em nenhum momento. Se o Pod novo falhar repetidamente na sonda de prontidão, a atualização pode ser interrompida automaticamente antes de substituir todas as réplicas, evitando que um defeito na versão nova comprometa o serviço inteiro de uma só vez.

> **Recurso visual 3 — Atualização gradual:** sequência de quatro instantâneos de um Deployment substituindo réplicas da versão 1.6.0 pela versão 1.7.0, uma de cada vez, mantendo o total de réplicas saudáveis.  
> **Texto alternativo:** sequência mostra a substituição gradual de réplicas de uma versão antiga por uma nova, sem redução do total de instâncias disponíveis.

### Pausa para reflexão

O reinício em loop de um Pod é, ao mesmo tempo, uma prova da robustez do laço de reconciliação e um risco de mascaramento de defeitos.

Reflita:

1. Que sinais, além do simples "o serviço está no ar", uma equipe deveria monitorar para perceber que um Pod está sendo recriado repetidamente?
2. Um Pod que trava sob alta carga e é recriado com sucesso está, de fato, "resolvido" do ponto de vista de negócio?
3. Que diferença existe entre usar o Kubernetes para tolerar falhas transitórias e usá-lo, sem perceber, para esconder um defeito determinístico de código?
4. Como um manifesto poderia declarar um limite de reinícios que force intervenção humana, em vez de tentativas indefinidas?

Uma resposta tecnicamente madura reconhece que reconciliação automática é um mecanismo de disponibilidade, não uma prova de correção — o mesmo raciocínio já aplicado a timeouts na Aula 4.

### Atividade prática

Interprete manifestos e acompanhe a recuperação automática de uma instância.

1. A partir do manifesto simplificado apresentado nesta aula, descreva em texto o que o Kubernetes faria se duas das quatro réplicas do serviço de pagamento ficassem indisponíveis simultaneamente.
2. Calcule o número de réplicas resultante de um Horizontal Pod Autoscaler para $N_{\text{atual}} = 6$, $U_{\text{atual}} = 92\%$ e $U_{\text{alvo}} = 65\%$.
3. Descreva um cenário de reinício em loop plausível para o serviço de estoque da NexaOrder e proponha um sinal de observabilidade que revelaria o problema antes que afetasse clientes.
4. Explique, em poucas frases, a diferença entre o papel de um Deployment e o papel de um Service no cenário descrito.

### Síntese da aula

- Imagens de contêiner imutáveis eliminam divergência silenciosa entre ambientes.
- Cluster, nó, Pod, Deployment e Service são os objetos centrais que organizam a execução no Kubernetes.
- O laço de reconciliação compara estado desejado e estado observado e age continuamente para aproximar um do outro.
- Recuperação automática restaura quantidade e execução declaradas, não a causa raiz de um defeito recorrente.
- Services oferecem descoberta e balanceamento estáveis diante de Pods voláteis.
- ConfigMaps, Secrets e armazenamento persistente separam configuração, segredos e dados do ciclo de vida da imagem.
- Escalonamento automático e atualizações graduais ajustam capacidade e versão sem interromper o serviço.

### Roteiro da Videoaula 11 — “Quem recriou essa instância? Dentro do laço de reconciliação do Kubernetes”

O roteiro falado e as indicações de edição serão desenvolvidos no arquivo `roteiros_20min.md`, usando a recuperação automática do serviço de pagamento da NexaOrder como demonstração central.

### Referências da aula

- BURNS, B. et al. Borg, Omega, and Kubernetes. *Communications of the ACM*, 2016. DOI: 10.1145/2890784.
- BURNS, Brendan. *Designing Distributed Systems*. 2. ed. Sebastopol: O'Reilly Media, 2024.
- Kubernetes Documentation. Disponível em: <https://kubernetes.io/docs/>.

## Aula 12 — Segurança e comunicação confiável entre serviços

### Situação-problema: qualquer serviço pode falar com qualquer serviço?

A NexaOrder agora executa vários serviços independentes, conectados por eventos e orquestrados pelo Kubernetes. Um novo risco se torna evidente durante uma revisão de segurança: nada, hoje, impede que o serviço de expedição chame diretamente o serviço de pagamento e solicite um reembolso, mesmo que essa não seja uma operação prevista para ele. A comunicação interna acontece em texto claro dentro do cluster, sem verificação de identidade além do endereço de rede, e as credenciais do provedor de pagamento estão embutidas em um arquivo de configuração acessível a qualquer pessoa com acesso ao repositório.

Esta aula trata da confiabilidade da comunicação entre serviços em um sentido mais amplo do que apenas disponibilidade: confiar que uma mensagem vem de quem afirma ser a origem, que ela não foi alterada em trânsito, que cada serviço só pode fazer o que lhe é explicitamente permitido, e que segredos não ficam expostos por conveniência operacional.

### Identidade de serviço e confiança zero

Em arquiteturas tradicionais, a segurança de rede costuma se basear em perímetro: tudo dentro da rede interna é considerado relativamente confiável, e a proteção se concentra na borda. Esse modelo se torna frágil em sistemas distribuídos com dezenas de serviços, múltiplos times e ambientes de nuvem, porque um único componente comprometido dentro do perímetro ganha acesso amplo.

O modelo de **confiança zero** (*zero trust*) parte do princípio oposto: nenhuma requisição é confiável apenas por vir de dentro da rede interna. Cada serviço possui uma **identidade** verificável — geralmente um certificado ou token criptográfico associado a ele, e não apenas ao seu endereço de rede — e toda comunicação, mesmo entre serviços no mesmo cluster, é autenticada e autorizada explicitamente, como se estivesse cruzando uma fronteira não confiável. Esse é o modelo formalizado, entre outras referências, pela publicação especial do NIST sobre arquitetura de confiança zero.

### Autenticação, autorização e menor privilégio

**Autenticação** responde à pergunta "quem está fazendo esta requisição?"; **autorização** responde à pergunta "o que essa identidade tem permissão para fazer?". As duas são complementares e não substituem uma à outra: um serviço pode ser autenticado corretamente e, ainda assim, não ter autorização para uma operação específica.

O princípio do **menor privilégio** determina que cada identidade — serviço, time ou pessoa — deve receber apenas as permissões estritamente necessárias para sua função, nada além disso. Aplicado à NexaOrder, isso significa que o serviço de expedição deveria ser autenticado como "expedição" e autorizado apenas a consultar o status de um pedido e confirmar o envio, sem qualquer permissão sobre operações de reembolso do serviço de pagamento — mesmo que a rede, tecnicamente, permita que a chamada seja feita.

### TLS e proteção em trânsito

O protocolo TLS (*Transport Layer Security*) protege dados em trânsito contra leitura e alteração por terceiros, usando criptografia entre as duas pontas de uma comunicação. Em arquiteturas de serviços internos, é cada vez mais comum adotar **TLS mútuo** (*mutual TLS*, ou mTLS), em que ambas as partes — não apenas o servidor, como em conexões web tradicionais — apresentam certificados e verificam a identidade uma da outra antes de trocar dados.

Isso significa que, em uma arquitetura com mTLS bem configurada, o serviço de pagamento só aceitaria uma conexão de um chamador cujo certificado comprove uma identidade autorizada, tornando inviável que um serviço não autenticado — ou um invasor que tenha obtido acesso à rede interna — inicie uma conexão válida simplesmente por estar na mesma rede.

> **Recurso visual 1 — Comunicação sem e com mTLS:** dois diagramas comparando uma chamada interna em texto claro sem verificação de identidade e uma chamada protegida por TLS mútuo com certificados em ambas as pontas.  
> **Texto alternativo:** comparação entre comunicação interna não autenticada e comunicação protegida por TLS mútuo, evidenciando verificação de identidade em ambas as pontas.

### Gestão de segredos

Credenciais, chaves de API e certificados — coletivamente chamados de **segredos** — não deveriam ser embutidos em imagens de contêiner, arquivos de configuração versionados ou variáveis de ambiente definidas manualmente. A prática recomendada é armazená-los em um sistema dedicado de **gestão de segredos**, que controla acesso, registra auditoria de uso e permite **rotação** periódica — a substituição programada de uma credencial antiga por uma nova, reduzindo a janela de exposição caso um segredo tenha sido comprometido sem que a equipe tenha percebido.

Na NexaOrder, a credencial do provedor de pagamento deveria ser injetada no Pod correspondente em tempo de execução por um sistema de segredos, nunca lida de um arquivo versionado no repositório de código — retomando o objeto Secret do Kubernetes apresentado na Aula 11, que costuma se integrar a sistemas externos de gestão de segredos mais completos.

A diferença prática entre as duas abordagens aparece justamente no momento de um incidente. Se uma credencial embutida em imagem for comprometida, a única forma de trocá-la é publicar uma nova versão da imagem, testá-la e reimplantá-la em todos os Pods afetados — um processo que pode levar horas, durante as quais a credencial exposta permanece válida. Se a credencial estiver em um sistema de gestão de segredos com rotação automatizada, trocá-la pode ser uma operação de segundos, sem exigir nova publicação de imagem, porque o Pod consulta o valor atual do segredo no momento em que precisa dele. Essa diferença de velocidade de resposta costuma determinar se um incidente de segurança fica contido ou se se prolonga por dias.

### Gateway, proxy lateral e service mesh

Implementar autenticação, criptografia em trânsito, limitação de taxa e políticas de autorização dentro do código de cada serviço, de forma repetida, é custoso e propenso a inconsistência. Um padrão amplamente adotado é o **proxy lateral** (*sidecar*): um processo auxiliar implantado junto a cada instância de serviço — no Kubernetes, tipicamente no mesmo Pod —, que intercepta todo o tráfego de entrada e saída e aplica essas políticas de forma uniforme, sem que o código da aplicação precise implementá-las diretamente.

Quando esses proxies laterais são coordenados por um plano de controle central que distribui configuração, certificados e políticas para todos eles, o conjunto é chamado de **service mesh**. Um service mesh permite, por exemplo, aplicar mTLS entre todos os serviços da NexaOrder de forma centralizada, sem alterar o código de pedidos, estoque, pagamento e expedição individualmente, além de coletar métricas uniformes de comunicação entre serviços — tema retomado na Unidade 4.

O **gateway**, apresentado na Aula 9 como ponto de entrada externo, e o proxy lateral do service mesh, interno ao cluster, cumprem papéis complementares: um protege a borda voltada para clientes externos; o outro protege a comunicação entre serviços internos.

> **Recurso visual 2 — Service mesh com proxies laterais:** diagrama dos quatro serviços da NexaOrder, cada um acompanhado de um proxy lateral, todos coordenados por um plano de controle central que distribui certificados e políticas.  
> **Texto alternativo:** diagrama de service mesh mostra proxies laterais junto a cada serviço da NexaOrder, coordenados por um plano de controle central.

### Limitação de taxa e proteção contra sobrecarga

Além de autenticar e autorizar, um serviço precisa se proteger contra volume excessivo de requisições, seja por tráfego legítimo em pico, seja por uso indevido. Um mecanismo comum é o **balde de fichas** (*token bucket*): um balde de capacidade $C$ fichas é reabastecido a uma taxa constante $r$ fichas por segundo; cada requisição consome uma ficha, e requisições sem ficha disponível são recusadas ou colocadas em espera.

Se o serviço de pagamento da NexaOrder define um balde com capacidade $C = 50$ fichas e taxa de reposição $r = 20$ fichas por segundo, ele tolera picos curtos de até 50 requisições simultâneas — o **estouro** (*burst*) — e, em regime permanente, sustenta no máximo:

$$
\lambda_{\text{sustentável}} = r = 20 \text{ requisições por segundo}
$$

Se uma rajada de 90 requisições chega em um único segundo, o balde absorve as primeiras 50 imediatamente e recusa ou atrasa as 40 restantes até que novas fichas sejam repostas, protegendo o serviço de uma sobrecarga que poderia comprometer sua disponibilidade para todos os chamadores, não apenas para a origem da rajada.

> **Recurso visual 3 — Balde de fichas:** ilustração de um balde com fichas sendo reposto a taxa constante e requisições consumindo fichas; uma rajada acima da capacidade é parcialmente recusada.  
> **Texto alternativo:** ilustração do algoritmo de balde de fichas mostrando reposição constante, consumo por requisição e recusa de excedente durante uma rajada.

### Ameaças específicas de sistemas distribuídos

Algumas ameaças exploram propriedades discutidas ao longo da disciplina, e não apenas falhas de implementação isoladas:

- **Ataque de repetição (*replay*):** uma mensagem legítima capturada é reenviada posteriormente para produzir um efeito indevido; mitigado por identificadores únicos de operação e janelas de validade, retomando idempotência da Aula 8.
- **Movimento lateral:** um invasor que compromete um serviço de baixo privilégio tenta usar essa posição para alcançar serviços mais sensíveis; mitigado por autenticação mútua e autorização de menor privilégio entre todos os serviços, não apenas na borda.
- **Amplificação por retry:** políticas agressivas de repetição, discutidas na Aula 2, podem transformar uma indisponibilidade parcial em uma sobrecarga generalizada, se todos os chamadores retentarem simultaneamente sem *backoff*.
- **Exposição de segredos por configuração:** segredos embutidos em imagens, logs ou repositórios tornam-se acessíveis a qualquer pessoa com acesso a esses artefatos, muito além do escopo pretendido.

Vale notar como essas quatro ameaças reinterpretam, sob a ótica de um adversário ativo, conceitos já estudados em unidades anteriores. O ataque de repetição explora a mesma ausência de identificação de operação discutida ao tratar de idempotência, agora com intenção maliciosa em vez de falha de rede acidental. A amplificação por retry reproduz o mesmo padrão de repetição sem *backoff* discutido na Aula 2, com o agravante de que cada tentativa fracassada gera novas tentativas, que geram mais carga, que geram mais falhas — um ciclo que se autoalimenta. Essa continuidade reforça que segurança de sistemas distribuídos não é uma disciplina isolada dos demais temas do curso: ela reaproveita, sob premissa adversarial, praticamente todos os conceitos de comunicação, falha e resiliência já estudados.

### Um fluxo autenticado e autorizado: pedido e pagamento

Reunindo os elementos desta aula, uma chamada do serviço de pedidos ao serviço de pagamento na NexaOrder deveria seguir, no mínimo: conexão estabelecida por TLS mútuo, com ambos os lados apresentando certificados válidos emitidos por uma autoridade confiável do cluster; autorização verificando que a identidade "pedidos" tem permissão explícita para solicitar autorizações de pagamento, mas não reembolsos; limitação de taxa aplicada pelo proxy lateral do serviço de pagamento, protegendo-o de sobrecarga; e um identificador único de operação anexado à requisição, permitindo que o serviço de pagamento rejeite repetições indevidas.

> **Recurso visual 4 — Fluxo autenticado pedido → pagamento:** diagrama passo a passo com verificação de certificado mútuo, checagem de autorização por identidade, aplicação de limite de taxa e verificação de idempotência antes do processamento.  
> **Texto alternativo:** diagrama de sequência mostra as quatro verificações de segurança aplicadas a uma chamada do serviço de pedidos ao serviço de pagamento.

### Transição para a Unidade 4

Com serviços delimitados, comunicação orientada a eventos, execução orquestrada e comunicação segura, a arquitetura da NexaOrder está estruturalmente completa. A Unidade 4 muda o foco de "como construir" para "como saber que está funcionando e continuar funcionando": observabilidade e diagnóstico distribuído, resiliência e engenharia do caos, processamento distribuído de dados, computação de borda e funções como serviço, encerrando com o projeto integrado e a avaliação arquitetural final da NexaOrder.

### Atividade prática

Elabore um fluxo autenticado e autorizado entre os serviços de pedido e pagamento da NexaOrder.

1. Descreva as identidades envolvidas e o mecanismo de autenticação mútua entre elas.
2. Defina uma política de autorização de menor privilégio para a identidade "pedidos" em relação às operações do serviço de pagamento.
3. Configure, em termos textuais, um balde de fichas para o endpoint de autorização de pagamento, justificando capacidade e taxa de reposição escolhidas.
4. Identifique uma ameaça específica de sistemas distribuídos (repetição, movimento lateral ou amplificação por retry) que esse fluxo deveria resistir, e explique o mecanismo de mitigação correspondente.

### Síntese da aula

- Confiança zero trata toda comunicação, mesmo interna, como potencialmente não confiável até prova de identidade.
- Autenticação e autorização respondem perguntas diferentes e são ambas necessárias.
- TLS mútuo protege dados em trânsito e verifica identidade em ambas as pontas da comunicação.
- Segredos devem ser geridos por sistemas dedicados, com rotação, nunca embutidos em imagens ou repositórios.
- Proxies laterais e service mesh centralizam políticas de segurança sem replicá-las em cada serviço.
- Limitação de taxa, como o balde de fichas, protege serviços de sobrecarga legítima ou indevida.
- Ataques de repetição, movimento lateral e amplificação por retry exploram propriedades específicas de sistemas distribuídos.

### Roteiro da Videoaula 12 — “Confiar em quê? Autenticação, TLS mútuo e menor privilégio entre serviços”

O roteiro falado e as indicações de edição serão desenvolvidos no arquivo `roteiros_20min.md`, usando o fluxo autenticado entre pedidos e pagamento da NexaOrder como demonstração central.

### Referências da aula

- ROSE, S. et al. *Zero trust architecture*. Gaithersburg: NIST, 2020. (NIST Special Publication 800-207). DOI: 10.6028/NIST.SP.800-207.
- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.
- NEWMAN, Sam. *Building Microservices*. 2. ed. Sebastopol: O'Reilly Media, 2021.

## Atividades, síntese e material complementar

### Quiz não avaliativo

**Questão 1.** Um time decide separar dois módulos fortemente relacionados em serviços distintos, alegando que "microsserviços escalam melhor". Após a mudança, toda alteração de negócio passa a exigir implantação coordenada dos dois serviços no mesmo dia, e ambos continuam lendo diretamente a mesma tabela de banco de dados. Esse cenário caracteriza principalmente:

a. uma arquitetura orientada a eventos bem-sucedida.
b. um monólito modular corretamente implementado.
*c. um monólito distribuído, porque a separação física não eliminou o acoplamento de dados e implantação.
d. uma aplicação de confiança zero.
e. um exemplo de escalonamento automático horizontal.

*Feedback:* a separação em processos distintos não é, por si só, garantia de autonomia. Quando dois serviços compartilham esquema de dados e precisam ser implantados juntos, eles somam a complexidade operacional da rede aos problemas de acoplamento de um monólito — o padrão conhecido como monólito distribuído, discutido na Aula 9.

**Questão 2.** Um Deployment do Kubernetes declara quatro réplicas de um serviço. Após a falha inesperada de uma instância, o número de réplicas em execução volta a quatro poucos segundos depois, sem qualquer comando manual. Esse comportamento é resultado direto de:

a. uma configuração de TLS mútuo entre os Pods.
b. um grupo de consumidores rebalanceando partições.
*c. o laço de reconciliação, que compara estado desejado e estado observado e age para reduzir a diferença entre eles.
d. a aplicação do princípio de menor privilégio.
e. a evolução de esquema de um evento de domínio.

*Feedback:* o Kubernetes não executa uma sequência fixa de passos para "consertar" uma falha; ele mantém um laço contínuo que observa o estado atual do cluster, compara com o estado desejado declarado pelo usuário e cria, remove ou substitui Pods para reduzir a diferença entre os dois — mecanismo central discutido na Aula 11.

### Síntese da unidade

- Fronteiras de serviço bem desenhadas combinam alta coesão interna, baixo acoplamento externo, contexto delimitado e dados de propriedade exclusiva de cada serviço.
- Um API Gateway concentra composição e políticas transversais para clientes externos, sem acumular regras de negócio.
- Arquiteturas orientadas a eventos substituem cadeias síncronas bloqueantes por publicação e consumo assíncrono, ao custo de raciocinar sobre ordenação por partição e semânticas de entrega.
- Grupos de consumidores permitem paralelismo horizontal limitado pelo número de partições de um tópico.
- Contêineres imutáveis e o laço de reconciliação do Kubernetes sustentam recuperação automática de instâncias, mas não substituem diagnóstico humano de causa raiz.
- Configuração, segredos e armazenamento persistente são geridos separadamente da imagem de contêiner, permitindo implantações imutáveis e seguras.
- Confiança zero, autenticação mútua, menor privilégio e service mesh tornam a comunicação entre serviços confiável mesmo dentro de uma rede considerada interna.
- Limitação de taxa e mitigação de ameaças específicas de sistemas distribuídos protegem serviços de sobrecarga e abuso, complementando os mecanismos de resiliência já estudados na Unidade 1.

### Material complementar

**Direto da Fonte**

NEWMAN, Sam. *Building Microservices*. 2. ed. Sebastopol: O'Reilly Media, 2021. Recomenda-se a leitura dos capítulos iniciais sobre modelagem de limites de serviço e do capítulo dedicado à decomposição de um monólito existente, que aprofundam os critérios de contexto delimitado e dados por serviço apresentados na Aula 9. Disponível na Biblioteca Virtual da instituição.

**Para Mergulhar**

LEWIS, James; FOWLER, Martin. Microservices. *martinfowler.com*, 25 mar. 2014. Disponível em: <https://martinfowler.com/articles/microservices.html>. Acesso em: 30 jul. 2026. O artigo original que popularizou o termo "microsserviços" complementa a discussão da Aula 9 sobre coesão, acoplamento e capacidade de negócio, com exemplos de organizações reais.

**Podcast**

GOTO Conferences. *When To Use Microservices (And When Not!) • Sam Newman & Martin Fowler*. YouTube, 2020. Disponível em: <https://www.youtube.com/watch?v=GBTdnfD6s5Q>. Acesso em: 30 jul. 2026. Conversa entre dois dos autores mais citados sobre microsserviços, discutindo quando essa decisão arquitetural é, de fato, justificada — reforçando o raciocínio de requisito, decisão, compromisso e evidência retomado ao longo desta unidade.

**Artigo científico**

BURNS, B. et al. Borg, Omega, and Kubernetes. *Communications of the ACM*, v. 59, n. 5, p. 50-57, 2016. DOI: 10.1145/2890784. O artigo, escrito por engenheiros do Google responsáveis pelos sistemas que precederam e inspiraram o Kubernetes, descreve as lições operacionais que moldaram o modelo de estado desejado e o laço de reconciliação apresentados na Aula 11.
