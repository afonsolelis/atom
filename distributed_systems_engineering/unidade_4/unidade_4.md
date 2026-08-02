# Unidade 4 — Operação, validação e evolução

Disciplina: Distributed Systems Engineering  
Professor-conteudista: Afonso Cesar Lelis Brandão  
Prazo de produção: 25 de agosto de 2026

## Relação da unidade com a atuação profissional

Projetar um sistema distribuído é apenas parte do trabalho de engenharia. A outra parte, tão exigente quanto a primeira, começa no instante em que o sistema entra em produção e passa a atender pessoas reais, sob carga real, sujeito a falhas reais. É nesse momento que surgem as perguntas que esta unidade responde: como saber o que está acontecendo dentro de dezenas de serviços distribuídos sem examinar cada um manualmente? Como confiar que os mecanismos de resiliência projetados nas unidades anteriores realmente funcionam sob falha, em vez de apenas parecerem funcionar no papel? Como processar volumes crescentes de dados sem transformar cada decisão de latência em um comprometimento de custo? E, ao final, como demonstrar, com evidências, que uma arquitetura atende aos requisitos que motivaram sua existência?

Essas perguntas não pertencem a um único cargo. Engenheiros de confiabilidade de site (SRE) e engenheiros de plataforma dependem de observabilidade e de testes de resiliência para manter acordos de nível de serviço. Engenheiros de dados e de machine learning dependem de processamento distribuído em lote e em fluxo para produzir informação a tempo de gerar valor. Arquitetos de solução dependem de avaliação arquitetural estruturada para justificar decisões perante áreas de negócio, segurança e finanças. Profissionais de desenvolvimento, ainda que não carreguem um desses títulos, cada vez mais precisam instrumentar o próprio código, participar de investigações de incidentes e defender escolhas técnicas com dados, não apenas com intuição.

O mercado de trabalho valoriza explicitamente essas competências. Vagas de SRE, observabilidade, engenharia de plataforma e engenharia de dados frequentemente exigem familiaridade com métricas, logs, traces, testes de carga, engenharia do caos e processamento distribuído — não como tópicos isolados, mas como um conjunto coerente de práticas que sustentam sistemas em produção. Empresas que operam plataformas de médio e grande porte tratam a capacidade de diagnosticar problemas complexos com rapidez, e de validar hipóteses de resiliência antes que um cliente as descubra por acidente, como diferencial competitivo direto.

Esta unidade também prepara o estudante para um momento recorrente da vida profissional: a defesa de uma arquitetura. Seja em uma revisão técnica interna, em uma proposta de investimento ou em uma auditoria de segurança e conformidade, o profissional será chamado a explicar por que um sistema foi projetado de determinada forma, quais riscos foram considerados e quais evidências sustentam a confiança depositada nele. A Aula 16, que encerra tanto esta unidade quanto a disciplina, situa exatamente esse desafio.

## O que você verá nesta unidade

A Unidade 4 acompanha a NexaOrder no momento em que a plataforma, já decomposta em serviços, orientada a eventos, orquestrada em contêineres e protegida por mecanismos de identidade e comunicação segura — como estabelecido na Unidade 3 —, precisa provar que funciona sob observação constante e sob estresse deliberado. Na Aula 13, você estudará observabilidade e diagnóstico distribuído, aprendendo a diferenciar monitoramento de observabilidade e a instrumentar serviços com métricas, logs e traces correlacionados. Na Aula 14, examinará resiliência, testes distribuídos e engenharia do caos, planejando experimentos controlados que revelam, antes de um incidente real, como o sistema se comporta diante de falhas. Na Aula 15, você estudará processamento distribuído de dados, computação de borda e funções como serviço, comparando alternativas para processar informação em lote, em fluxo e próximo ao usuário. Por fim, na Aula 16, você integrará tudo o que foi estudado nas quatro unidades para avaliar, revisar e defender uma arquitetura final para a NexaOrder — o encerramento da jornada iniciada na Aula 1.

## Aula 13 — Observabilidade e diagnóstico distribuído

### Situação-problema: um pedido que sumiu por doze segundos

Um cliente da NexaOrder relata que sua compra demorou doze segundos entre o clique em “finalizar pedido” e a confirmação na tela — um tempo muito acima do esperado, mas sem erro visível. A equipe de plantão abre o painel de infraestrutura: CPU, memória e uso de rede dos serviços de pedidos, estoque, pagamento e expedição estão dentro da faixa normal. Nenhum alerta disparou. Nenhum serviço reiniciou. Os logs de cada serviço, quando lidos isoladamente, também não mostram nada incomum: cada um registra que processou sua parte da requisição dentro de um tempo aceitável.

O problema é que ninguém consegue reconstruir a jornada completa daquele pedido específico através dos quatro serviços. Os logs existem, mas estão dispersos, sem um identificador comum que permita juntá-los na ordem certa. A equipe sabe que “alguma coisa” demorou doze segundos, mas não sabe onde, porque nunca projetou o sistema para responder a essa pergunta. Painéis que mostram médias agregadas de CPU e latência — o que a equipe chama, informalmente, de “monitoramento” — não ajudam quando o problema é um caso específico, raro e não previsto de antemão.

Esta aula constrói o vocabulário e as práticas necessárias para que perguntas desse tipo deixem de exigir arqueologia manual e passem a ter resposta em minutos.

### Monitoramento e observabilidade não são sinônimos

*Monitoramento* consiste em observar indicadores previamente definidos e disparar alertas quando eles ultrapassam limites conhecidos. Um painel de CPU, um alerta de taxa de erro acima de 5% e um aviso de disco cheio são exemplos típicos. O monitoramento responde bem a perguntas que já foram antecipadas: “a CPU está alta?”, “o serviço está respondendo?”.

*Observabilidade* é a propriedade de um sistema que permite inferir seu estado interno a partir dos dados que ele expõe externamente, mesmo diante de perguntas que ninguém formulou antes do incidente. Um sistema observável não exige que a equipe tenha previsto, com um painel específico, cada possível modo de falha. Em vez disso, ele expõe dados ricos e correlacionáveis — métricas, logs e *traces* — que podem ser combinados livremente para investigar qualquer comportamento, inclusive combinações raras de condições que nunca ocorreram antes.

A diferença é prática, não apenas terminológica. O incidente do pedido de doze segundos não seria resolvido por mais painéis de CPU: exigia a capacidade de fazer uma pergunta nova — “o que aconteceu com este pedido específico, atravessando todos os serviços?” — e obter uma resposta a partir dos dados já coletados, sem precisar reproduzir o problema manualmente.

### Os três pilares: métricas, logs e traces

A observabilidade moderna costuma se apoiar em três tipos complementares de telemetria.

*Métricas* são valores numéricos agregados ao longo do tempo, como número de requisições por segundo, taxa de erro ou percentual de utilização de um recurso. São compactas, baratas de armazenar por longos períodos e adequadas para detectar tendências e disparar alertas. Sua limitação é a agregação: uma métrica de taxa de erro de 0,5% não diz quais requisições falharam nem por quê.

*Logs* são registros discretos de eventos, normalmente em texto estruturado, produzidos por um componente em um instante específico. Um log pode registrar “pedido 48213 recebido”, “reserva de estoque confirmada” ou “falha ao chamar provedor de pagamento: timeout”. Logs são ricos em contexto local, mas, sem correlação entre serviços, permanecem fragmentos isolados.

*Traces* representam o caminho de uma única requisição através de múltiplos componentes, decompondo essa jornada em unidades chamadas *spans* — cada uma representando uma operação com início, fim e metadados. Um trace do pedido problemático mostraria, em uma única visualização, quanto tempo cada serviço consumiu e em que ordem as chamadas ocorreram, revelando exatamente onde os doze segundos foram gastos.

Nenhum dos três pilares substitui os outros. Métricas indicam que algo mudou; traces mostram onde, dentro de uma requisição específica, esse algo aconteceu; logs detalham o que exatamente ocorreu naquele ponto.

> **Recurso visual 1 — Os três pilares da observabilidade:** diagrama com três colunas (métricas, logs, traces) mostrando um mesmo incidente representado de três formas complementares, convergindo para uma investigação única.  
> **Texto alternativo:** diagrama mostra métricas, logs e traces como três fontes de dados distintas que, combinadas, permitem investigar um mesmo incidente na NexaOrder.

### Contexto e correlação distribuída

O elemento que transforma logs e traces dispersos em uma narrativa coerente é a *correlação*. Cada requisição que entra na NexaOrder recebe um identificador único — um identificador de correlação, frequentemente chamado de *trace ID* — no momento em que atinge o primeiro componente, geralmente o *gateway*. Esse identificador é propagado para cada chamada subsequente: quando o serviço de pedidos chama o serviço de estoque, o identificador viaja junto, em um cabeçalho da requisição; quando um evento é publicado para o serviço de expedição, o identificador viaja nos metadados da mensagem.

Essa propagação não é automática por natureza da rede — é responsabilidade explícita da instrumentação de cada serviço extrair o identificador da requisição recebida e incluí-lo em qualquer chamada ou mensagem que produzir. Se um único serviço no meio do caminho falhar em propagar o contexto, o trace se rompe naquele ponto, e a jornada completa da requisição deixa de poder ser reconstruída, mesmo que cada serviço individualmente tenha registrado seus próprios dados.

Com o identificador de correlação presente em logs e spans, a equipe pode formular a pergunta “o que aconteceu com o pedido 48213?” e obter uma linha do tempo unificada. Identificadores por requisição não devem virar labels comuns de métricas, pois criam cardinalidade praticamente ilimitada; métricas usam dimensões agregáveis e podem se ligar a um trace específico por *exemplars*.

### Instrumentação com OpenTelemetry

A prática de expor métricas, logs e traces de forma consistente é chamada de *instrumentação*. Historicamente, cada fornecedor de ferramenta de observabilidade definia seu próprio formato de instrumentação, obrigando equipes a reescrever código sempre que trocavam de fornecedor. O *OpenTelemetry* surgiu como um padrão aberto e neutro em relação a fornecedor para instrumentação de aplicações, unificando a coleta de métricas, logs e traces sob uma mesma API e um mesmo protocolo de exportação.

Na prática, um serviço instrumentado com OpenTelemetry usa um *SDK* (kit de desenvolvimento de software) que pode capturar automaticamente operações comuns — chamadas HTTP recebidas e enviadas, consultas a banco de dados, publicação e consumo de mensagens — e permite que o próprio código adicione spans e atributos personalizados para operações de negócio relevantes, como “reservar item de estoque” ou “autorizar pagamento”. Os dados coletados são enviados a um coletor, que os processa e os encaminha para o sistema de armazenamento e visualização escolhido pela equipe.

Para a NexaOrder, adotar OpenTelemetry reduz o acoplamento da instrumentação do serviço de pedidos a uma ferramenta específica. Em muitos casos, trocar o sistema de análise de traces preserva a instrumentação principal e exige apenas ajustar o *exporter*, o coletor ou o destino. Convenções semânticas, recursos proprietários e capacidades diferentes entre ferramentas ainda podem exigir adaptações.

> **Recurso visual 2 — Fluxo de instrumentação com OpenTelemetry:** diagrama mostrando um serviço gerando spans e métricas via SDK, enviando-os a um coletor, que os encaminha a um backend de armazenamento e visualização.  
> **Texto alternativo:** diagrama ilustra a geração de telemetria por um serviço instrumentado, seu envio a um coletor OpenTelemetry e o encaminhamento para uma ferramenta de análise.

### Indicadores de nível de serviço: o que medir

Um *indicador de nível de serviço* (SLI, do inglês *service level indicator*) é uma medida quantitativa do comportamento observado de um serviço, calculada a partir de dados reais de produção. Bons SLIs refletem a experiência de quem usa o sistema, não apenas a saúde interna da infraestrutura. Para o fluxo de checkout da NexaOrder, exemplos razoáveis de SLI incluem:

- proporção de requisições de checkout concluídas com sucesso em relação ao total de tentativas;
- proporção de requisições concluídas dentro de um limite de latência aceitável (por exemplo, 300 ms);
- proporção de eventos de confirmação de pagamento processados corretamente na primeira tentativa.

Um erro comum é escolher indicadores fáceis de coletar — como utilização média de CPU — em vez de indicadores relevantes para o cliente. A CPU pode permanecer em níveis confortáveis enquanto uma fração significativa de pedidos falha por outro motivo, como esgotamento de conexões com o banco de dados ou lentidão em um provedor externo. Um SLI bem escolhido é aquele que, quando ruim, corresponde a uma experiência ruim para quem usa o serviço.

### Do indicador ao objetivo: SLO e orçamento de erro

Um *objetivo de nível de serviço* (SLO, do inglês *service level objective*) é a meta definida para um SLI ao longo de um período de tempo, como “99,9% das requisições de checkout devem ser concluídas com sucesso, medido mensalmente”. O SLO transforma um indicador contínuo em um critério binário de sucesso ou falha para o período observado.

A diferença entre 100% e o SLO definido é o *orçamento de erro*: a quantidade de falha que o sistema pode acumular sem violar a meta. Esse orçamento pode ser expresso como:

$$
E = (1 - SLO) \times V
$$

em que $E$ é o orçamento de erro em número de eventos, $SLO$ é o objetivo expresso como fração e $V$ é o volume total de eventos relevantes no período.

Considere que o checkout da NexaOrder processa, em média, 12.000.000 de requisições por mês, com um SLO de 99,9% de sucesso. O orçamento de erro mensal é:

$$
E = (1 - 0{,}999) \times 12.000.000 = 0{,}001 \times 12.000.000 = 12.000
$$

A equipe pode, portanto, acumular até 12.000 requisições malsucedidas ao longo do mês sem violar o objetivo. Se, nos primeiros dez dias do mês, o sistema já acumulou 9.000 falhas — 75% do orçamento total, em apenas um terço do período —, a *taxa de consumo* (ou *burn rate*) do orçamento está muito acima do que o restante do mês suporta. Esse número orienta uma decisão operacional concreta: reduzir a frequência de mudanças arriscadas, priorizar estabilidade e investigar a causa do consumo acelerado antes que o orçamento se esgote por completo.

O orçamento de erro tem um efeito adicional importante: ele legitima riscos calculados. Enquanto o orçamento não estiver esgotado, a equipe tem margem para implantar mudanças, experimentar e evoluir o sistema. Quando o orçamento se aproxima do limite, uma política previamente acordada deve deslocar a prioridade para a estabilidade, tornando o critério observável e menos dependente de uma discussão subjetiva sobre o que é “seguro o suficiente”.

> **Recurso visual 3 — Consumo do orçamento de erro ao longo do mês:** gráfico de linha mostrando o consumo acumulado de orçamento de erro em relação ao tempo decorrido do mês, com uma linha de referência representando o consumo esperado uniforme.  
> **Texto alternativo:** gráfico compara o consumo real do orçamento de erro do checkout com um ritmo de consumo uniforme esperado, evidenciando um consumo acelerado nos primeiros dez dias do mês.

### Diagnóstico de latência e dependências

Um trace distribuído representa a jornada de uma requisição como uma árvore de spans, cada um com um início, uma duração e, frequentemente, uma relação de dependência com o span que o originou. Ao visualizar essa árvore — normalmente como um diagrama de cascata (*waterfall*) —, é possível identificar rapidamente qual componente concentra a maior parte da latência observada.

Retomando o incidente, o trace apresenta uma árvore coerente: o span raiz do *gateway* dura 12.000 ms; dentro dele, o serviço de pedidos dura 11.950 ms; o estoque consome 35 ms; e o pagamento ocupa 11.780 ms no caminho crítico. Ao expandir pagamento, a equipe encontra 11.450 ms de espera em fila, 310 ms na chamada ao provedor e cerca de 20 ms de processamento local. A expedição, assíncrona, começa após a resposta e não pertence ao caminho crítico do cliente. Spans aninhados não devem ser somados como se fossem sequenciais; a cascata e as relações pai-filho revelam que a espera em pagamento explica quase todo o intervalo de doze segundos.

Esse tipo de análise também revela dependências ocultas: um serviço aparentemente rápido pode, internamente, aguardar uma resposta de outro serviço que não aparece nos painéis de infraestrutura, mas aparece claramente como um span filho no trace. A observabilidade transforma a pergunta “por que essa requisição foi lenta?” de uma investigação artesanal em uma leitura direta de dados já coletados.

> **Recurso visual 4 — Trace em cascata de um pedido:** diagrama temporal com spans aninhados do gateway, pedidos, estoque e pagamento; o pagamento contém uma espera em fila de 11.450 ms e uma chamada externa de 310 ms. A expedição aparece após a resposta, fora do caminho crítico.
> **Texto alternativo:** diagrama de cascata de uma requisição de doze segundos mostra a longa espera em fila dentro do span de pagamento e distingue a expedição assíncrona do caminho crítico do cliente.

### Atividade prática

Reconstrua, em formato de tabela ou diagrama, o trace de um pedido da NexaOrder que atravessa gateway, pedidos, estoque, pagamento e expedição.

1. Atribua a cada serviço um tempo de execução hipotético (em milissegundos).
2. Identifique qual serviço concentra a maior parte do tempo total.
3. Proponha um identificador de correlação e descreva como ele deveria ser propagado entre os serviços, incluindo o caso de um evento assíncrono publicado para a expedição.
4. Defina um SLI e um SLO para o fluxo completo de checkout.
5. Calcule o orçamento de erro mensal para um volume hipotético de requisições.
6. Liste dois logs e duas métricas que, combinados ao trace, ajudariam a confirmar a causa raiz da lentidão identificada.

### Síntese da aula

- Monitoramento responde a perguntas antecipadas; observabilidade permite investigar perguntas não previstas a partir de dados já coletados.
- Métricas, logs e traces são pilares complementares, não substitutos entre si.
- A correlação distribuída depende de um identificador propagado explicitamente entre serviços e mensagens, inclusive em comunicação assíncrona.
- O OpenTelemetry padroniza a instrumentação de forma neutra em relação a fornecedor de ferramenta.
- SLIs devem refletir a experiência do usuário, não apenas a saúde interna da infraestrutura.
- O orçamento de erro converte o SLO em uma quantidade concreta de falha tolerável, orientando decisões operacionais sobre ritmo de mudança.
- Traces em cascata permitem localizar, dentro de uma requisição específica, qual componente concentra a latência observada.

### Roteiro da Videoaula 13 — “Doze segundos de silêncio: seguindo um pedido pelo sistema”

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está no arquivo `roteiros_20min.md` desta unidade, retomando o incidente da situação-problema como fio condutor da demonstração.

### Referências da aula

- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O’Reilly Media, 2017.
- BEYER, Betsy; JONES, Chris; PETOFF, Jennifer; MURPHY, Niall Richard (org.). *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol: O’Reilly Media, 2016.
- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.

## Aula 14 — Resiliência, testes distribuídos e engenharia do caos

### Situação-problema: o teste que nunca foi feito

Durante uma promoção de fim de ano, o provedor de pagamento utilizado pela NexaOrder apresentou uma instabilidade de poucos minutos. O circuito de proteção implementado na Unidade 1, projetado exatamente para esse cenário, deveria isolar a falha e permitir que o restante do sistema continuasse operando em modo degradado. Na prática, o comportamento observado foi diferente: o serviço de pedidos, que aguardava a resposta do pagamento de forma síncrona em um ponto do código que ninguém havia testado sob falha, acumulou conexões pendentes até esgotar seu próprio limite de capacidade. O efeito se propagou: o serviço de estoque, que dependia do serviço de pedidos para confirmar reservas, também começou a apresentar lentidão.

A equipe técnica sabia, em tese, que mecanismos de resiliência haviam sido implementados. O que faltava era a prática de validá-los deliberadamente, antes que um evento real os testasse pela primeira vez, sob a pior condição possível: tráfego de pico. Esta aula trata de como transformar suposições sobre resiliência em evidências obtidas por meio de testes estruturados e experimentos controlados.

### A pirâmide de testes em um sistema distribuído

A pirâmide de testes organiza diferentes tipos de teste por escopo, velocidade e custo de manutenção. Na base, testes unitários verificam uma função ou classe isoladamente, executando em milissegundos. No nível seguinte, testes de integração verificam a interação entre um componente e suas dependências diretas, como um banco de dados ou uma fila. No topo, testes de ponta a ponta (*end-to-end*) verificam um fluxo completo de negócio atravessando múltiplos serviços reais.

Em sistemas distribuídos, o topo da pirâmide é particularmente caro: um teste de ponta a ponta do fluxo de compra da NexaOrder exige que pedidos, estoque, pagamento e expedição estejam todos disponíveis e configurados de forma coerente, tornando o teste lento, frágil a mudanças não relacionadas e difícil de depurar quando falha. A recomendação prática é manter uma base ampla de testes unitários e de contrato, complementada por um número reduzido e cuidadosamente escolhido de testes de integração e de ponta a ponta, cobrindo os fluxos mais críticos para o negócio.

### Testes de contrato: verificar acordos sem executar tudo junto

Um *teste de contrato* verifica se dois serviços que se comunicam — um consumidor e um provedor — concordam sobre o formato e o significado das mensagens trocadas, sem exigir que ambos estejam em execução simultânea durante o teste. Na abordagem orientada pelo consumidor, o serviço de estoque, consumidor dos eventos publicados pelo serviço de pedidos, define expectativas explícitas sobre os campos que espera receber. Essas expectativas são publicadas em um repositório compartilhado. No pipeline de integração contínua do serviço de pedidos, antes de qualquer implantação, o contrato é verificado automaticamente: se um campo esperado por estoque deixar de existir ou mudar de nome, o pipeline falha antes que a mudança chegue à produção.

Esse mecanismo teria detectado, por exemplo, uma alteração silenciosa no nome de um campo de evento de pedido — um problema recorrente em arquiteturas orientadas a eventos, discutido na Unidade 3, e frequentemente responsável por falhas sutis que só aparecem em produção, muito depois de a mudança ter sido implantada.

### Testes de carga, estresse e duração

Três tipos de teste avaliam o comportamento do sistema sob diferentes perfis de demanda, e é comum confundi-los:

- **teste de carga:** verifica se o sistema sustenta o tráfego esperado — por exemplo, o volume típico de um dia normal, ou o pico projetado de uma campanha — sem violar os objetivos de latência e erro definidos;
- **teste de estresse:** aumenta a carga progressivamente além do esperado, até identificar o ponto em que o sistema falha, revelando sua capacidade máxima e seu modo de degradação;
- **teste de duração** (*soak test*): mantém uma carga sustentada, geralmente próxima do esperado, por um período prolongado — horas ou dias —, revelando problemas que só aparecem com o tempo, como vazamentos de memória, esgotamento gradual de conexões ou acúmulo de dados temporários não liberados.

Os três testes respondem a perguntas diferentes: o teste de carga confirma que o sistema atende ao que foi prometido; o teste de estresse revela onde ele quebra; o teste de duração revela como ele se degrada quando exposto ao tempo, não apenas ao volume instantâneo.

> **Recurso visual 5 — Comparação entre teste de carga, estresse e duração:** três gráficos lado a lado mostrando o perfil de carga aplicado ao longo do tempo em cada tipo de teste.  
> **Texto alternativo:** três gráficos comparam o padrão de carga aplicado em testes de carga, de estresse e de duração, evidenciando objetivos distintos para cada um.

### Engenharia do caos: injetar falha para aprender

A *engenharia do caos* é a prática de conduzir experimentos controlados que injetam falhas deliberadas — latência adicional, erros simulados, indisponibilidade de um componente — em um sistema, com o objetivo de observar seu comportamento real diante de condições adversas, em vez de presumi-lo. A prática nasceu da constatação de que sistemas distribuídos em produção enfrentam combinações de falha raras demais para serem previstas por completo em revisão de código, mas frequentes o suficiente, na escala de milhares de componentes, para acontecerem de tempos em tempos.

Diferente de um teste determinístico de unidade, um experimento de caos começa com uma hipótese explícita e mensurável sobre o estado estável e tenta refutá-la sob uma perturbação controlada. A pergunta “o que acontece quando isso falha?” é transformada em uma expectativa verificável; resultados inesperados continuam valiosos, mas não dispensam critérios definidos antes da execução.

### Hipótese de estado estável

Todo experimento de caos bem projetado começa pela definição de uma *hipótese de estado estável*: uma expectativa mensurável e específica sobre o comportamento normal do sistema, formulada antes de qualquer falha ser injetada. A hipótese não é “o sistema deve continuar funcionando” — afirmação vaga demais para ser verificada — mas algo como: “em condições normais, a taxa de conclusão de pedidos permanece acima de 98% e a latência p95 do checkout permanece abaixo de 400 ms; durante a indisponibilidade simulada do provedor de pagamento, o circuito de proteção deve ser acionado, o sistema deve degradar graciosamente informando o cliente, e a taxa de conclusão de pedidos não deve cair abaixo de 90%”.

Essa hipótese exige, como pré-requisito, que a equipe já saiba medir a taxa de conclusão de pedidos e a latência p95 continuamente — o que conecta diretamente esta aula à instrumentação de observabilidade estudada na Aula 13. Sem métricas confiáveis, não há como confirmar ou refutar a hipótese durante o experimento.

### Raio de impacto e mecanismos de interrupção

Um princípio central da engenharia do caos responsável é começar pequeno. O *raio de impacto* (*blast radius*) de um experimento deve ser limitado deliberadamente — afetando, por exemplo, apenas 1% do tráfego real, um único ambiente controlado, ou um pequeno subconjunto de instâncias — antes de ser ampliado gradualmente, à medida que a equipe ganha confiança sobre o comportamento observado. Junto ao raio de impacto limitado, todo experimento em produção precisa de um mecanismo de interrupção imediata (*kill switch*): um comando ou automação capaz de encerrar a injeção de falha instantaneamente, caso os indicadores de negócio ultrapassem um limite de degradação predefinido.

Esses dois elementos — raio de impacto limitado e capacidade de interrupção imediata — são o que diferencia um experimento de caos responsável de simplesmente “causar uma falha em produção e esperar o melhor”.

> **Recurso visual 6 — Progressão do raio de impacto:** diagrama mostrando a ampliação gradual do escopo de um experimento de caos, de um ambiente de testes para 1% do tráfego real e, por fim, para um escopo maior, após validação em cada etapa.  
> **Texto alternativo:** diagrama ilustra a expansão progressiva e controlada do raio de impacto de experimentos de caos ao longo do tempo, conforme a confiança da equipe aumenta.

> **Recurso visual 7 — Cartão do experimento de caos:** quadro com hipótese de estado estável, perturbação, métricas de controle, raio de impacto, critério de interrupção e evidência esperada.
> **Texto alternativo:** cartão de planejamento relaciona hipótese, falha injetada, indicadores observados, limite de impacto e condição de abortar o experimento.

### Um exemplo numérico: por que a resiliência de cada serviço não é suficiente

Suponha que os serviços de pedidos, estoque, pagamento e expedição da NexaOrder apresentem, individualmente, disponibilidade de 99,9% cada um. Em um modelo simplificado que assume falhas independentes e mede os quatro componentes no mesmo intervalo, se o fluxo depender de uma cadeia estritamente sequencial — sem tolerância a falha parcial —, a disponibilidade combinada é o produto das disponibilidades individuais. Na prática, dependências compartilhadas e falhas correlacionadas exigem medição conjunta e podem produzir resultado pior:

$$
A_{\text{fluxo}} = A_{\text{pedidos}} \times A_{\text{estoque}} \times A_{\text{pagamento}} \times A_{\text{expedição}}
$$

$$
A_{\text{fluxo}} = 0{,}999^4 \approx 0{,}996
$$

Um fluxo composto por quatro serviços de 99,9% de disponibilidade individual entrega, na ausência de mecanismos de resiliência, aproximadamente 99,6% de disponibilidade combinada — um valor sensivelmente pior que o de cada componente isolado. Esse resultado explica por que circuitos de proteção, degradação graciosa e processamento assíncrono desacoplado, estudados nas unidades anteriores, não são refinamentos opcionais: sem eles, a composição de serviços tende a produzir uma disponibilidade agregada inferior à de qualquer serviço individual, e apenas testes deliberados — não a leitura do código — revelam se esses mecanismos realmente atenuam esse efeito na prática.

### Recuperação e aprendizagem operacional

Depois de um incidente real ou de um experimento de caos que revela um comportamento inesperado, a etapa final é a aprendizagem estruturada, tipicamente conduzida por meio de um *postmortem* — um relatório que reconstrói a linha do tempo do incidente, identifica fatores contribuintes e propõe ações de melhoria com responsáveis e prazos definidos. A prática de *postmortem sem culpabilização* (*blameless postmortem*) parte do princípio de que incidentes em sistemas complexos raramente têm uma única causa atribuível a uma pessoa; eles emergem de combinações de decisões de projeto, lacunas de teste e condições operacionais que, isoladamente, pareciam razoáveis.

Um postmortem eficaz não termina na identificação da causa imediata — no caso da situação-problema, o esgotamento de conexões no serviço de pedidos. Ele investiga por que o circuito de proteção não impediu esse esgotamento, por que nenhum teste de contrato ou experimento de caos havia revelado essa lacuna antes, e quais mudanças sistêmicas — não apenas correções pontuais de código — reduzem a chance de recorrência.

### Pausa para reflexão

Considere: a equipe da NexaOrder decide não realizar nenhum experimento de caos em produção, argumentando que os testes de integração em ambiente de homologação já garantem confiança suficiente sobre a resiliência do sistema.

Reflita:

1. Que diferenças entre o ambiente de homologação e o ambiente de produção podem invalidar essa suposição?
2. Por que testes de integração, mesmo bem escritos, podem não revelar o comportamento sob falhas parciais e concorrência real de milhares de usuários simultâneos?
3. Que argumento você usaria para convencer a liderança técnica de que um experimento de caos com raio de impacto limitado é mais seguro do que esperar por um incidente real para descobrir as mesmas informações?
4. Que evidências de observabilidade, estudadas na Aula 13, seriam necessárias antes de autorizar o primeiro experimento em produção?

Uma resposta tecnicamente madura reconhece que ambientes de homologação raramente reproduzem volume de tráfego, diversidade de dados e condições de rede reais, e que a engenharia do caos, quando conduzida com raio de impacto limitado e mecanismo de interrupção, reduz o risco de descobrir essas lacunas pela primeira vez durante um incidente sem controle.

### Atividade prática

Planeje um experimento controlado de indisponibilidade do serviço de pagamento da NexaOrder.

1. Formule uma hipótese de estado estável mensurável, incluindo os indicadores que serão observados.
2. Defina o raio de impacto inicial do experimento e justifique a escolha.
3. Descreva o mecanismo de interrupção imediata e o critério que o aciona.
4. Liste os dados de observabilidade (métricas, logs, traces) necessários para avaliar o resultado do experimento.
5. Descreva, em três frases, como seria a estrutura de um postmortem caso o experimento revele uma falha inesperada.

### Síntese da aula

- A pirâmide de testes recomenda uma base ampla de testes unitários e de contrato, com uso seletivo de testes de integração e de ponta a ponta.
- Testes de contrato detectam incompatibilidades entre serviços sem exigir execução simultânea de ambos.
- Testes de carga, estresse e duração respondem a perguntas distintas sobre o comportamento do sistema sob demanda.
- Engenharia do caos injeta falhas deliberadas para observar o comportamento real do sistema, em vez de presumi-lo.
- Todo experimento de caos deve partir de uma hipótese de estado estável mensurável.
- Raio de impacto limitado e mecanismo de interrupção imediata tornam o experimento seguro o suficiente para produção.
- A disponibilidade combinada de uma cadeia de serviços tende a ser inferior à de cada serviço isolado, na ausência de mecanismos de resiliência testados.
- Postmortems sem culpabilização buscam causas sistêmicas, não responsáveis individuais.

### Roteiro da Videoaula 14 — “O circuito que não segurou: planejando um experimento de caos”

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está no arquivo `roteiros_20min.md` desta unidade, utilizando o incidente do provedor de pagamento como demonstração central.

### Referências da aula

- BEYER, Betsy; JONES, Chris; PETOFF, Jennifer; MURPHY, Niall Richard (org.). *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol: O’Reilly Media, 2016.
- BASIRI, Ali et al. Chaos engineering. *IEEE Software*, v. 33, n. 3, p. 35-41, 2016. DOI: 10.1109/MS.2016.60.
- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O’Reilly Media, 2017.

## Aula 15 — Processamento distribuído, edge e serverless

### Situação-problema: detectar fraude antes que o pagamento seja aprovado

A NexaOrder passou a registrar tentativas de fraude: compradores usando múltiplos cartões em sequência rápida, a partir do mesmo dispositivo, testando quais dados de pagamento seriam aceitos. O time de risco propõe um pipeline capaz de sinalizar esse padrão antes que o pagamento seja aprovado — não depois, quando o prejuízo já ocorreu. A primeira proposta técnica sugere um job que roda a cada hora, lendo o histórico de tentativas de pagamento e sinalizando padrões suspeitos para revisão manual no dia seguinte.

O time de risco rejeita a proposta: uma hora é tempo suficiente para dezenas de tentativas fraudulentas serem aprovadas. A decisão precisa ocorrer em segundos, no momento da tentativa. Essa exigência muda completamente o tipo de arquitetura de processamento necessária — e é o ponto de partida desta aula, que examina como sistemas distribuídos processam grandes volumes de dados, seja em lote, seja em fluxo contínuo, e como decisões de localização de processamento afetam custo e latência.

### Processamento em lote e processamento em fluxo

O *processamento em lote* (*batch*) opera sobre um conjunto de dados finito e delimitado, coletado ao longo de um período, processado de uma só vez. É adequado para análises que não exigem resposta imediata: relatórios diários de vendas, cálculo de comissões mensais, reprocessamento histórico após uma correção de dados. Sua vantagem é a simplicidade de raciocínio: o conjunto de dados é conhecido e finito no momento do processamento.

O *processamento em fluxo* (*streaming*) opera sobre uma sequência potencialmente ilimitada de eventos, processando cada evento — ou pequenos grupos de eventos — assim que ele se torna disponível, sem esperar a formação de um lote completo. Para a detecção de fraude descrita na situação-problema, o processamento em fluxo é a escolha adequada: cada tentativa de pagamento é avaliada no instante em que ocorre, permitindo bloqueio antes da aprovação, algo que um pipeline horário jamais conseguiria oferecer.

A escolha entre lote e fluxo não é apenas técnica — é uma decisão de negócio sobre até quando uma informação pode esperar antes de perder valor.

### MapReduce e a generalização em DAGs

O modelo *MapReduce*, descrito por Dean e Ghemawat, popularizou uma forma de processar grandes volumes de dados distribuídos em um cluster de máquinas, dividindo o trabalho em duas fases principais: *map*, que transforma cada registro de entrada independentemente, produzindo pares de chave e valor intermediários; e *reduce*, que agrupa e combina esses pares por chave, produzindo o resultado final. Entre as duas fases ocorre o *embaralhamento* (*shuffle*): a redistribuição dos pares intermediários entre os nós responsáveis pela fase de redução, agrupando-os pela chave correspondente.

Frameworks modernos de processamento distribuído generalizaram essa ideia para *grafos acíclicos dirigidos* (DAGs, do inglês *directed acyclic graphs*), permitindo encadear múltiplas etapas de transformação, filtragem e agregação, não apenas o par map-reduce original. Em ambos os casos, a tolerância a falhas segue um princípio comum: se um nó falha durante uma tarefa, o framework reatribui essa tarefa a outro nó disponível, reexecutando-a a partir dos dados intermediários já persistidos, sem exigir que todo o job seja reiniciado do zero nem intervenção manual para uma falha isolada de um único nó.

> **Recurso visual 8 — Fases de um job MapReduce sobre o histórico da NexaOrder:** diagrama mostrando dados de entrada divididos entre tarefas de mapeamento, seguidos por embaralhamento por chave e tarefas de redução produzindo o resultado agregado.
> **Texto alternativo:** diagrama ilustra as fases de mapeamento, embaralhamento e redução aplicadas ao histórico de pedidos da NexaOrder.

### Particionamento, embaralhamento e tolerância a falhas em fluxo

Pipelines de processamento em fluxo também particionam o trabalho, tipicamente distribuindo eventos entre partições de acordo com uma chave — por exemplo, o identificador do dispositivo que originou a tentativa de pagamento, garantindo que todos os eventos de um mesmo dispositivo sejam processados em ordem, pela mesma partição. Quanto mais partições, maior o paralelismo disponível, mas também maior a complexidade de coordenação e de tolerância a falhas: cada partição precisa ter seu progresso registrado de forma duradoura, para que, em caso de falha do processo consumidor, o processamento possa ser retomado do ponto correto, sem perder nem duplicar eventos além do que a semântica de entrega escolhida permitir — tema já examinado na Unidade 3, ao tratar de plataformas de eventos.

Um exemplo numérico ilustra o dimensionamento de partições. Se o pipeline de detecção de fraude precisa processar um pico de 5.000 eventos de tentativa de pagamento por segundo, e cada consumidor de uma partição sustenta, de forma comprovada por teste de carga, até 750 eventos por segundo, o número mínimo de partições necessárias é:

$$
P = \left\lceil \frac{\lambda_{\text{eventos}}}{C_{\text{partição}}} \right\rceil = \left\lceil \frac{5.000}{750} \right\rceil = \left\lceil 6{,}67 \right\rceil = 7
$$

Sete partições atendem ao pico estimado com uma margem, mas essa conta não substitui um teste de carga real do pipeline completo, incluindo o custo de embaralhamento e de acesso a qualquer dado de contexto necessário à avaliação de fraude, como o histórico recente do dispositivo.

### Tempo de evento, tempo de processamento e janelas

Em processamento de fluxo, é essencial distinguir *tempo de evento* — o instante em que o evento efetivamente ocorreu no domínio de negócio, como o momento exato da tentativa de pagamento — do *tempo de processamento* — o instante em que o pipeline efetivamente processa esse evento, que pode ser alguns segundos, ou em casos de instabilidade de rede, minutos depois.

Análises que dependem de janelas de tempo — por exemplo, “quantas tentativas de pagamento com o mesmo dispositivo ocorreram no último minuto?” — precisam decidir se a janela é calculada com base no tempo de evento ou no tempo de processamento. Janelas baseadas em tempo de evento produzem resultados mais fiéis à realidade do negócio, mas exigem lidar com eventos que chegam atrasados ou fora de ordem. O mecanismo típico para isso é a *marca d’água* (*watermark*): uma estimativa de até que ponto no tempo de evento o pipeline já recebeu a maior parte dos dados, combinada com uma tolerância configurável a atraso (*allowed lateness*), que mantém uma janela aberta por um período adicional antes de considerá-la definitivamente fechada.

> **Recurso visual 9 — Janela por tempo de evento e marca d’água:** linha do tempo com eventos pontuais, chegada atrasada, limite da marca d’água e janela ainda aberta pela tolerância configurada.
> **Texto alternativo:** linha do tempo diferencia o instante real dos eventos do instante de processamento e mostra como uma marca d’água admite eventos atrasados antes de fechar a janela.

### Funções como serviço e o custo da inicialização a frio

*Funções como serviço* (FaaS, do inglês *functions as a service*) permitem executar um trecho de código em resposta a um evento — uma requisição HTTP, uma mensagem em uma fila, um arquivo criado em um armazenamento —, sem que a equipe precise provisionar ou manter um servidor continuamente em execução. A plataforma aloca automaticamente o ambiente necessário no momento da invocação e cobra, tipicamente, pelo tempo de execução efetivo, não por capacidade ociosa.

Esse modelo é particularmente adequado para cargas esporádicas e de volume variável, como o envio de uma notificação por e-mail sempre que um pedido é confirmado. Seu custo está na *inicialização a frio* (*cold start*): quando não existe uma instância da função já ativa e “aquecida”, a plataforma precisa inicializar um novo ambiente de execução antes de processar a requisição, adicionando latência que pode ser irrelevante para uma notificação assíncrona, mas problemática para um caminho síncrono sensível à latência, como parte do fluxo de checkout.

### Computação de borda e o compromisso entre custo e latência

A *computação de borda* (*edge computing*) aproxima o processamento dos dispositivos que geram ou consomem os dados, executando lógica em pontos geograficamente distribuídos, próximos ao usuário, em vez de centralizá-la em uma única região de nuvem. Para a NexaOrder, isso poderia significar avaliar sinais simples de fraude — como velocidade incomum de digitação ou padrões básicos de comportamento do dispositivo — diretamente em um ponto de borda próximo ao cliente, reduzindo a latência da primeira triagem.

Esse ganho de latência tem contrapartida: manter lógica distribuída em múltiplos pontos de borda aumenta a complexidade operacional, exige sincronizar versões de modelos ou regras em muitos locais, e nem sempre reduz custo — o processamento de borda pode ser mais caro por unidade, especialmente quando exige contexto histórico amplo que só está disponível de forma centralizada. A decisão apropriada pondera a redução de latência obtida contra a complexidade e o custo introduzidos, reservando modelos mais complexos, que dependam de contexto histórico amplo, para o processamento centralizado, e sinais simples e locais para a borda.

> **Recurso visual 10 — Compromisso entre custo e latência no processamento de borda:** gráfico posicionando processamento centralizado, próximo e de borda por eixos de latência e custo operacional, evidenciando a ausência de uma opção universalmente superior.
> **Texto alternativo:** gráfico compara processamento centralizado, regional e de borda em termos de latência típica e custo operacional relativo.

### Pausa para reflexão

O time de risco da NexaOrder propõe processar toda a análise de fraude exclusivamente na borda, eliminando qualquer dependência de uma região central de nuvem, argumentando que isso reduzirá a latência a zero e eliminará custos de rede.

Reflita:

1. Que tipos de sinal de fraude dependem de contexto histórico que dificilmente estaria disponível apenas em um ponto de borda?
2. Que riscos operacionais surgem de manter lógica de decisão duplicada em múltiplos pontos de borda, especialmente quando um modelo de fraude precisa ser atualizado?
3. Em que medida a afirmação de que a latência seria “reduzida a zero” é tecnicamente imprecisa?
4. Que combinação de processamento em borda e processamento centralizado atenderia melhor ao requisito original de decisão em segundos, sem abrir mão de contexto histórico relevante?

### Atividade prática

Compare, para o cenário de detecção de fraude quase em tempo real da NexaOrder, três alternativas de arquitetura de processamento: (a) pipeline em lote horário; (b) pipeline em fluxo centralizado, particionado por dispositivo; (c) triagem inicial na borda combinada com avaliação mais profunda em pipeline de fluxo centralizado.

1. Para cada alternativa, estime a latência típica entre a tentativa de pagamento e a decisão de bloqueio ou liberação.
2. Identifique, para a alternativa (b), quantas partições seriam necessárias para um pico de 8.000 eventos por segundo, considerando um consumidor capaz de processar 1.000 eventos por segundo.
3. Avalie cada alternativa quanto à capacidade de considerar o histórico do dispositivo, não apenas o evento isolado.
4. Recomende uma alternativa, justificando a escolha com base em latência, custo e complexidade operacional.

### Síntese da aula

- Processamento em lote atende análises que toleram espera; processamento em fluxo atende decisões que exigem resposta em segundos.
- O modelo MapReduce e sua generalização em DAGs organizam processamento distribuído em fases de transformação, embaralhamento e agregação, com tolerância a falhas por reexecução de tarefas isoladas.
- O dimensionamento de partições relaciona a taxa de eventos esperada à capacidade comprovada de cada consumidor.
- Tempo de evento e tempo de processamento podem divergir; marcas d’água e tolerância a atraso tratam eventos fora de ordem sem descartar o conceito de janela.
- Funções como serviço reduzem custo ocioso para cargas esporádicas, ao custo de latência adicional em inicializações a frio.
- Computação de borda reduz latência para sinais simples e locais, mas aumenta complexidade operacional e nem sempre reduz custo.
- A escolha entre lote, fluxo, FaaS e borda deve partir do requisito de negócio sobre até quando uma informação pode esperar antes de perder valor.

### Roteiro da Videoaula 15 — “Segundos, não horas: detectando fraude em tempo quase real”

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está no arquivo `roteiros_20min.md` desta unidade, comparando as três alternativas de processamento apresentadas na atividade prática.

### Referências da aula

- DEAN, Jeffrey; GHEMAWAT, Sanjay. MapReduce: simplified data processing on large clusters. *Communications of the ACM*, v. 51, n. 1, p. 107-113, 2008. DOI: 10.1145/1327452.1327492.
- KLEPPMANN, Martin. *Designing Data-Intensive Applications*. Sebastopol: O’Reilly Media, 2017.
- TANENBAUM, Andrew S.; VAN STEEN, Maarten. *Distributed Systems*. 4. ed. [S. l.]: distributed-systems.net, 2023.

## Aula 16 — Projeto integrado e avaliação arquitetural

### Situação-problema: defender a arquitetura diante do conselho

A diretoria da NexaOrder convoca a equipe de engenharia para uma revisão formal antes de aprovar o orçamento do próximo ciclo. A pergunta não é “o sistema funciona?” — isso já foi demonstrado. A pergunta é: “por que confiamos que esta arquitetura sustenta o crescimento previsto, resiste às falhas mais prováveis e vale o investimento contínuo que exige?”. A equipe precisa responder com requisitos, estimativas, decisões documentadas e evidências — não com afirmações genéricas sobre a qualidade do sistema.

Esta última aula da disciplina integra tudo o que foi estudado nas quatro unidades em um exercício de avaliação arquitetural completa: dos requisitos que justificam cada decisão até a revisão final da jornada da NexaOrder, de uma aplicação simples em um único servidor até uma plataforma distribuída, observável, testada e defensável.

### Requisitos funcionais e atributos de qualidade

*Requisitos funcionais* descrevem o que o sistema deve fazer: “o cliente deve conseguir finalizar uma compra”, “o estoque deve ser reservado antes da confirmação do pagamento”. *Atributos de qualidade* — também chamados de requisitos não funcionais — descrevem como o sistema deve se comportar sob determinadas condições: desempenho, disponibilidade, segurança, capacidade de manutenção, escalabilidade, custo.

Os dois tipos de requisito não têm importância desigual na avaliação arquitetural; eles frequentemente entram em tensão, e resolver essa tensão de forma explícita é parte central do trabalho de projeto. Por exemplo, o time de produto da NexaOrder pode desejar latência mínima na exibição do catálogo, enquanto o time de confiabilidade exige garantias mais fortes de consistência no saldo de estoque exibido. Uma avaliação madura não escolhe um lado de forma absoluta: aceita leituras eventualmente consistentes no catálogo, onde uma pequena divergência é tolerável, mas exige consistência mais forte no instante da reserva de estoque durante o checkout, onde a divergência tem custo direto — retomando, de forma aplicada, os modelos de consistência estudados na Unidade 2.

### Estimativa de carga e capacidade, revisitada

A Aula 1 desta disciplina apresentou uma fórmula simples para estimar o número mínimo de instâncias necessárias para sustentar um pico de tráfego:

$$
N = \left\lceil \frac{\lambda_{\text{pico}}}{C_{\text{instância}} \times U_{\text{alvo}}} \right\rceil
$$

Passadas três unidades de decisões arquiteturais — replicação, particionamento, consenso, sagas, decomposição em serviços, orquestração e, agora, observabilidade e testes —, essa mesma fórmula continua válida, mas seus insumos deixaram de ser estimativas isoladas: $C_{\text{instância}}$ pode agora ser obtido de testes de carga reais, conduzidos com o rigor discutido na Aula 14, e $\lambda_{\text{pico}}$ pode ser refinado a partir de métricas históricas reais, coletadas pela instrumentação apresentada na Aula 13. A avaliação arquitetural madura não estima capacidade a partir de suposições — ela estima a partir de evidências operacionais acumuladas ao longo do ciclo de vida do sistema.

### Decisões e registros arquiteturais

Um *registro de decisão arquitetural* (ADR, do inglês *architecture decision record*) documenta uma escolha significativa de arquitetura, incluindo o contexto que a motivou, as alternativas consideradas, a decisão tomada e as consequências esperadas. Um ADR não é apenas um nome de tecnologia anotado — “decidimos usar Kubernetes” não é um registro útil por si só. Um ADR completo explicaria, por exemplo, por que a orquestração automatizada foi necessária, quais alternativas foram avaliadas (como implantação manual ou um serviço gerenciado mais simples), e quais consequências — como a curva de aprendizado da equipe ou o custo de operação do cluster — foram aceitas conscientemente.

Ao longo das quatro unidades, a NexaOrder acumulou dezenas de decisões que mereceriam registros formais: adoção de múltiplas instâncias sem estado (Unidade 1), escolha de modelo de consistência para estoque e catálogo (Unidade 2), decomposição em serviços e arquitetura orientada a eventos (Unidade 3), estratégia de observabilidade e política de testes de resiliência (Unidade 4). Reunir esses registros permite que qualquer pessoa nova na equipe compreenda não apenas o estado atual do sistema, mas o raciocínio que levou a ele.

> **Recurso visual 11 — Linha do tempo de decisões arquiteturais da NexaOrder:** linha do tempo com marcos das quatro unidades, cada um associado a uma decisão arquitetural registrada em um ADR.
> **Texto alternativo:** linha do tempo relaciona cada unidade da disciplina a uma decisão arquitetural central adotada pela NexaOrder, do modelo de instâncias sem estado à estratégia de observabilidade.

### Análise de pontos únicos de falha

A *análise de pontos únicos de falha* (SPOF, do inglês *single point of failure*) identifica componentes cuja indisponibilidade isolada comprometeria todo o fluxo, mesmo que o restante do sistema permaneça saudável. Essa análise exige atenção a dependências ocultas: réplicas de um serviço distribuídas em múltiplas zonas de disponibilidade não eliminam automaticamente todos os pontos únicos de falha do sistema como um todo, se todas elas dependerem de um único componente não replicado — por exemplo, uma instância isolada do sistema de mensageria que todas as réplicas do serviço de pagamento utilizam para publicar eventos.

Revisar a NexaOrder sob essa lente, ao final da disciplina, significa percorrer cada componente crítico — gateway, banco de dados de pedidos, sistema de mensageria, provedor de identidade, coletor de observabilidade — e verificar se sua indisponibilidade isolada derrubaria o fluxo completo de compra, mesmo que todo o restante da arquitetura estivesse saudável.

### Plano de consistência e recuperação

O plano de recuperação de um sistema distribuído normalmente se expressa por dois indicadores complementares: o *objetivo de ponto de recuperação* (RPO, do inglês *recovery point objective*), que mede a quantidade máxima de dados que o negócio aceita perder em uma falha — tipicamente expresso como um intervalo de tempo desde o último backup ou replicação bem-sucedida —, e o *objetivo de tempo de recuperação* (RTO, do inglês *recovery time objective*), que mede o tempo máximo aceitável para restabelecer o serviço após uma interrupção.

Se a NexaOrder replica de forma assíncrona o banco de dados de pedidos para uma região secundária a cada cinco minutos, e o plano prevê que a equipe consiga promover essa região e restabelecer o serviço em até quinze minutos após um desastre na região primária, o RPO aproximado do plano é de cinco minutos — a possível perda de dados entre a última replicação bem-sucedida e o desastre — e o RTO aproximado é de quinze minutos — o tempo necessário para restabelecer o serviço. Esses dois números, definidos a partir de requisitos de negócio e não de conveniência técnica, orientam diretamente decisões de replicação, frequência de backup e automação de failover.

> **Recurso visual 12 — Árvore de atributos de qualidade:** árvore que parte dos objetivos de negócio e ramifica em disponibilidade, desempenho, segurança, recuperabilidade e custo, ligando cada atributo a um cenário mensurável e a uma evidência.
> **Texto alternativo:** árvore relaciona objetivos de negócio da NexaOrder a cinco atributos de qualidade, respectivos cenários de teste e evidências operacionais.

### Segurança e observabilidade desde o projeto

Segurança e observabilidade, quando tratadas como preocupações adicionadas ao final do desenvolvimento, tendem a ser incompletas e caras de corrigir. A prática recomendada — muitas vezes descrita como “segura e observável por padrão” — incorpora identidade de serviço, autenticação, autorização e instrumentação de telemetria como parte do desenho inicial de cada componente, não como uma camada acrescentada depois que o sistema já está em produção, retomando diretamente os temas de comunicação confiável estudados na Unidade 3 e de instrumentação estudados na Aula 13 desta unidade.

Na revisão final da NexaOrder, essa prática se traduz em perguntas concretas: todo novo serviço nasce com identidade própria e comunicação autenticada? Todo novo fluxo crítico nasce instrumentado com métricas, logs e traces correlacionáveis, ou a instrumentação é adicionada apenas depois do primeiro incidente que a exigiu?

### Custo, sustentabilidade e evolução

Uma arquitetura distribuída não permanece ótima indefinidamente. Padrões de tráfego mudam, novos requisitos surgem, e decisões que faziam sentido em uma escala menor podem se tornar ineficientes — ou insuficientes — em uma escala maior. Um exemplo comum: capacidade provisionada para o pico de tráfego, mas mantida constante mesmo em horários de baixíssima demanda, gera custo elevado sem benefício correspondente de desempenho ou confiabilidade. A resposta madura não é eliminar a redundância necessária para os picos, mas adotar mecanismos de escalonamento automático que ajustem a capacidade à demanda observada, preservando as metas de disponibilidade definidas, sem manter recursos ociosos pagos por padrão.

Um exemplo numérico ilustra por que redundância bem distribuída, e não apenas duplicada, compensa seu custo. Se uma única instância de um serviço crítico apresenta disponibilidade individual de 99,5%, e três réplicas independentes — sem dependência compartilhada de um único ponto de falha — operam atrás de um balanceador que redireciona tráfego para qualquer réplica saudável, a disponibilidade combinada, considerando que o serviço fica indisponível apenas se todas as réplicas falharem simultaneamente, é:

$$
A_{\text{réplicas}} = 1 - (1 - A)^n
$$

$$
A_{\text{réplicas}} = 1 - (1 - 0{,}995)^3 = 1 - 0{,}005^3 = 1 - 0{,}000000125 \approx 0{,}999999875
$$

Três réplicas independentes elevam a disponibilidade de 99,5% para algo próximo de sete “noves” — um resultado muito superior ao obtido pela composição sequencial de serviços vista na Aula 14, evidenciando que redundância paralela e independência de falha, não apenas a multiplicação de instâncias, é o que sustenta disponibilidade combinada elevada. Esse ganho tem custo: manter três réplicas custa aproximadamente três vezes mais que manter uma, e a decisão de investir nesse ganho depende do valor de negócio que a disponibilidade adicional realmente entrega.

> **Recurso visual 13 — Disponibilidade combinada: cadeia sequencial versus redundância paralela:** dois diagramas lado a lado comparando a disponibilidade resultante de uma cadeia sequencial de serviços e de réplicas paralelas independentes de um mesmo serviço.
> **Texto alternativo:** diagramas comparam como a disponibilidade combinada se degrada em uma cadeia sequencial de serviços e melhora com réplicas paralelas independentes.

### Revisão integral da NexaOrder

Ao final da disciplina, vale reconstruir a trajetória completa da NexaOrder. A Unidade 1 estabeleceu os fundamentos: o que caracteriza um sistema distribuído, como processos se comunicam, como o tempo e a ordenação de eventos deixam de ser triviais, e como falhas parciais exigem desenho explícito para recuperação. A Unidade 2 tratou da distribuição de dados: replicação, particionamento, o teorema CAP, consenso via Raft e transações distribuídas com sagas e idempotência. A Unidade 3 decompôs o sistema em serviços com limites de domínio explícitos, adotou arquitetura orientada a eventos, orquestração em contêineres e comunicação segura entre serviços. Esta Unidade 4 fechou o ciclo: observabilidade para diagnosticar o sistema em produção, testes e engenharia do caos para validar resiliência antes que um incidente a valide à força, processamento distribuído para extrair valor de dados em escala, e, agora, avaliação arquitetural integrada para justificar cada decisão perante requisitos, riscos e custo.

Nenhuma dessas quatro unidades, isoladamente, entrega uma arquitetura completa. É a combinação — fundamentos sólidos, dados bem distribuídos, serviços bem delimitados e operação validada — que sustenta um sistema como a NexaOrder em produção, sob carga real, por anos.

### Atividade prática

Prepare uma defesa arquitetural completa da NexaOrder para uma banca de revisão.

1. Liste três requisitos funcionais e três atributos de qualidade que orientam a arquitetura, explicitando ao menos uma tensão entre eles e como foi resolvida.
2. Escreva um ADR completo para uma decisão de sua escolha, tomada em qualquer unidade da disciplina.
3. Realize uma análise de pontos únicos de falha, identificando ao menos dois riscos não triviais.
4. Defina RPO e RTO para o fluxo de pedidos, com justificativa de negócio.
5. Descreva como segurança e observabilidade estão incorporadas desde o desenho de um novo serviço hipotético.
6. Apresente um cenário de carga (pico de tráfego) e um cenário de falha (indisponibilidade de um componente crítico) e explique como a arquitetura responde a cada um, com evidências das aulas anteriores.

### Encerramento da disciplina: da aplicação em um servidor à plataforma distribuída

Esta é a última aula de *Distributed Systems Engineering*. Vale reconhecer o percurso. A NexaOrder começou, na Aula 1, como uma aplicação simples, instalada em um único servidor, onde duas pessoas conseguiam comprar o mesmo último item sem que ninguém soubesse explicar por quê. Dezesseis aulas depois, ela se tornou uma plataforma distribuída com serviços delimitados, comunicação assíncrona, replicação e consenso, orquestração automatizada, segurança de ponta a ponta, observabilidade contínua e testes de resiliência deliberados — cada decisão registrada, cada compromisso explicitado, cada garantia sustentada por evidência, não por esperança.

Essa trajetória reflete a natureza real do trabalho de quem projeta e opera sistemas distribuídos: não existe uma arquitetura definitiva, entregue de uma vez, que resolve todos os problemas para sempre. Existe um processo contínuo de observar, questionar, testar, ajustar e documentar — o mesmo processo que esta disciplina tentou reproduzir, unidade após unidade, em torno de um único caso que cresceu junto com o conteúdo.

Ao profissional que conclui esta disciplina, fica um convite: continue tratando cada decisão arquitetural como uma hipótese verificável, não como um dogma. Sistemas distribuídos não recompensam quem memoriza padrões, mas quem sabe perguntar “o que acontece se isso falhar?”, medir a resposta e ajustar o projeto com base nela. Essa é a competência central da engenharia de sistemas distribuídos, e ela permanece relevante independentemente de qual tecnologia específica estiver em voga daqui a alguns anos. Boa jornada — e bons sistemas, mesmo quando, especialmente quando, algo neles falhar.

### Síntese da aula

- Requisitos funcionais e atributos de qualidade frequentemente entram em tensão, e a avaliação arquitetural madura resolve essa tensão de forma explícita e diferenciada por contexto.
- A estimativa de capacidade se torna mais confiável quando alimentada por dados reais de observabilidade e testes de carga, em vez de suposições isoladas.
- ADRs documentam contexto, alternativas, decisão e consequências, permitindo que decisões futuras sejam avaliadas à luz do que já foi decidido.
- A análise de pontos únicos de falha deve considerar dependências compartilhadas ocultas, não apenas a redundância aparente de cada componente isolado.
- RPO e RTO traduzem tolerância de negócio a perda de dados e a indisponibilidade em metas técnicas mensuráveis.
- Segurança e observabilidade incorporadas desde o projeto custam menos e falham menos do que quando adicionadas reativamente após um incidente.
- Redundância paralela e independente eleva a disponibilidade combinada de forma muito mais eficaz do que a composição sequencial de serviços.
- A jornada da NexaOrder, das quatro unidades, ilustra que arquitetura distribuída é um processo contínuo de decisão, evidência e revisão — não um estado final.

### Roteiro da Videoaula 16 — “Da aplicação em um servidor à plataforma distribuída: encerrando a jornada da NexaOrder”

O roteiro falado completo, com narração pronta para gravação, marcações de edição e fontes, está no arquivo `roteiros_20min.md` desta unidade, encerrando a disciplina com uma retrospectiva da trajetória da NexaOrder pelas quatro unidades.

### Referências da aula

- LAMPSON, Butler W. Hints for computer system design. In: ACM SYMPOSIUM ON OPERATING SYSTEMS PRINCIPLES, 9., 1983, Bretton Woods. *Proceedings [...]*. New York: ACM, 1983. p. 33-48. DOI: 10.1145/800217.806614.
- COULOURIS, George et al. *Distributed Systems: Concepts and Design*. 5. ed. Boston: Addison-Wesley, 2011.
- BEYER, Betsy; JONES, Chris; PETOFF, Jennifer; MURPHY, Niall Richard (org.). *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol: O’Reilly Media, 2016.

## Atividades, síntese e material complementar

### Quiz não avaliativo

**Questão 1.** Uma equipe afirma que seu sistema é observável porque mantém um painel com quinze gráficos de CPU, memória e uso de disco, atualizados em tempo real para cada um de seus doze serviços. Do ponto de vista da diferença entre monitoramento e observabilidade estudada na Aula 13, essa afirmação é:

a. Correta, pois observabilidade é definida exclusivamente pelo número de painéis mantidos pela equipe.
b. Correta, pois métricas de infraestrutura são sempre suficientes para investigar qualquer incidente, independentemente da sua causa.
c. Incorreta, pois observabilidade exige que nenhum painel de infraestrutura seja mantido pela equipe.
*d. Incorreta, pois esses painéis exemplificam monitoramento de indicadores previamente conhecidos; observabilidade exige, adicionalmente, a capacidade de investigar perguntas não antecipadas a partir de métricas, logs e traces correlacionados.
e. Incorreta, pois observabilidade só pode ser alcançada com uma única ferramenta comercial específica, independentemente de sua funcionalidade.

*Feedback:* painéis de CPU, memória e disco são exemplos típicos de monitoramento: indicadores conhecidos, observados continuamente, adequados para alertar sobre condições previstas. Observabilidade é uma propriedade mais ampla, que depende da capacidade de correlacionar métricas, logs e traces para responder a perguntas específicas e não antecipadas — como “o que aconteceu com o pedido 48213?” —, e não do número de painéis existentes nem de uma ferramenta específica.

**Questão 2.** Em um experimento de engenharia do caos, a equipe decide injetar indisponibilidade total do serviço de pagamento em 100% do tráfego de produção, na primeira execução do experimento, sem qualquer mecanismo de interrupção imediata configurado, argumentando que essa é a forma mais rápida de obter dados conclusivos. Essa decisão está:

a. Correta, pois o raio de impacto de um experimento de caos deve sempre ser o máximo possível, para maximizar a quantidade de dados coletados.
b. Correta, desde que o experimento seja realizado fora do horário comercial, independentemente de qualquer outro cuidado.
c. Incorreta, pois experimentos de caos nunca devem ser realizados em ambiente de produção, apenas em ambientes de teste isolados.
*d. Incorreta, pois viola dois princípios centrais da prática responsável de engenharia do caos: limitar o raio de impacto inicial e garantir um mecanismo de interrupção imediata caso indicadores de negócio se degradem além de um limite aceitável.
e. Incorreta, pois experimentos de caos não podem, em nenhuma hipótese, ser aplicados a serviços de pagamento.

*Feedback:* a prática responsável de engenharia do caos recomenda começar com um raio de impacto limitado — uma pequena fração do tráfego ou um subconjunto controlado de instâncias — e ampliá-lo gradualmente conforme a confiança da equipe aumenta, sempre com um mecanismo de interrupção imediata disponível. Afetar 100% do tráfego real sem possibilidade de interrupção contraria esses dois princípios e transforma um experimento controlado em um incidente autoinduzido sem controle.

### Síntese da unidade

- Observabilidade complementa o monitoramento tradicional, permitindo investigar perguntas não antecipadas a partir de métricas, logs e traces correlacionados por um identificador comum propagado entre serviços.
- SLIs bem escolhidos refletem a experiência de quem usa o sistema; SLOs e orçamentos de erro convertem esses indicadores em metas mensuráveis que orientam decisões operacionais concretas.
- Testes de contrato, carga, estresse e duração respondem a perguntas complementares sobre corretude e comportamento sob demanda, e nenhum deles substitui a validação de resiliência sob falha real.
- Engenharia do caos transforma suposições sobre resiliência em evidências, por meio de experimentos com hipótese de estado estável, raio de impacto limitado e mecanismo de interrupção imediata.
- A escolha entre processamento em lote e em fluxo depende de até quando uma informação pode esperar antes de perder valor para o negócio; MapReduce e seus sucessores em DAG generalizam o processamento distribuído com tolerância a falhas por reexecução de tarefas.
- Funções como serviço e computação de borda ampliam as opções de onde e como processar dados, cada uma com compromissos próprios entre custo, latência e complexidade operacional.
- Avaliação arquitetural madura conecta requisitos funcionais e atributos de qualidade a decisões documentadas, análise de pontos únicos de falha, metas de recuperação e revisão contínua de custo.
- A trajetória completa da NexaOrder, das quatro unidades, demonstra que arquitetura distribuída é um processo contínuo de decisão, evidência e revisão, não um projeto que termina em uma entrega única.

### Material complementar

#### Direto da Fonte

**Texto provocativo:** Esta unidade defendeu que confiabilidade se mede, não se declara. Este livro é o registro de como uma organização de grande escala transformou essa ideia em prática cotidiana: os capítulos indicados tratam de monitoramento distribuído e de testes de confiabilidade, ligando SLIs, SLOs e orçamento de erro a decisões concretas sobre ritmo de mudança.

**Referência:** BEYER, Betsy; JONES, Chris; PETOFF, Jennifer; MURPHY, Niall Richard (org.). *Site Reliability Engineering: How Google Runs Production Systems*. Sebastopol: O'Reilly Media, 2016. Capítulos sobre monitoramento distribuído e testes de confiabilidade.

**Link de acesso:** disponível na Biblioteca Virtual da instituição.

**Aula indicada:** Aula 13, após "Do indicador ao objetivo: SLO e orçamento de erro".

#### Para Mergulhar no Assunto

**Texto provocativo:** Se o volume anterior explica os princípios, este mostra como implantá-los em uma equipe que já tem sistema em produção e prazo apertado. Os capítulos de implementação trazem modelos prontos de definição de SLO, de política de orçamento de erro e de revisão de incidentes — insumos diretos para o plano de evidências que você monta na Aula 16.

**Referência:** BEYER, Betsy et al. *The Site Reliability Workbook: Practical Ways to Implement SRE*. Sebastopol: O'Reilly Media, 2018.

**Link de acesso:** <https://sre.google/workbook/table-of-contents/>. Acesso em: 1 ago. 2026.

**Aula indicada:** Aula 16, durante a construção do plano de evidências arquiteturais.

#### Podcast

**Texto provocativo:** A Aula 14 insistiu que engenharia do caos não é derrubar componentes e observar o resultado. Nesta apresentação, um dos formuladores da prática detalha a diferença entre experimento e acidente: hipótese de estado estável, raio de impacto e critério de interrupção. É a referência a citar quando alguém propuser "testar em produção" sem esses três elementos.

**Referência:** ROSENTHAL, Casey. *Principles of Chaos Engineering*. SREcon17 Americas. Berkeley: USENIX Association, 2017. 1 vídeo.

**Link de acesso:** <https://www.usenix.org/conference/srecon17americas/program/presentation/rosenthal>. Acesso em: 1 ago. 2026.

**Trecho obrigatório:** 00:00–35:00 (35 minutos), cobrindo definição, hipótese e condução do experimento.

**Aula indicada:** Aula 14, após "Hipótese de estado estável".

#### Artigo científico

**Texto provocativo:** Este é o texto que consolidou a engenharia do caos como disciplina, e não como folclore de engenharia. Escrito por quem operou a prática em escala de streaming global, ele apresenta os princípios fundadores e, sobretudo, os limites: o que um experimento pode demonstrar e o que ele nunca vai demonstrar sobre a resiliência de um sistema.

**Referência:** BASIRI, Ali et al. Chaos engineering. *IEEE Software*, v. 33, n. 3, p. 35-41, maio/jun. 2016. DOI: 10.1109/MS.2016.60.

**Link de acesso:** <https://doi.org/10.1109/MS.2016.60>. Acesso em: 1 ago. 2026.

**Aula indicada:** Aula 14, antes da atividade prática de planejamento do experimento.
