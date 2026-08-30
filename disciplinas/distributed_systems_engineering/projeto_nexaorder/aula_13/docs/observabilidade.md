# Observabilidade e diagnóstico distribuído — Unidade 4, Aula 13

## O incidente que esta aula corrige

Até a Aula 12, um cliente reclamando de uma compra lenta era irrespondível: os
painéis de CPU/memória/rede estavam normais, nenhum alerta disparou, e os logs de
cada serviço, lidos isoladamente, indicavam tempos aceitáveis. Ninguém conseguia
reconstruir a jornada completa daquele pedido pelos serviços, porque faltava um
identificador comum ligando os fragmentos — exatamente a situação-problema do
roteiro.

Duas lacunas concretas do projeto tornavam isso pior do que precisava ser, e ambas
são fechadas nesta aula:

1. **O gateway nunca propagava o trace_id.** Ele o gerava (ou recebia) na borda e o
   perdia no primeiro salto — nenhuma das quatro chamadas que faz a
   pedidos/estoque/pagamento/expedicao enviava o cabeçalho `X-Trace-Id`. Corrigido em
   `services/gateway/app/main.py` (ver `test_trace_id_do_gateway_se_propaga_para_os_servicos_downstream`).
2. **Estoque, pagamento, expedição e o próprio gateway nunca extraíam o trace_id
   recebido.** Só `pedidos` tinha `correlation.py` e o middleware que o lê. Os outros
   quatro serviços ganham a mesma peça nesta aula.

## Monitoramento não é observabilidade

Monitoramento observa indicadores previamente definidos e alerta quando ultrapassam
limites — responde a perguntas antecipadas. Observabilidade permite inferir o estado
interno do sistema a partir de dados já coletados, sem reproduzir o problema
manualmente — responde a perguntas que ninguém formulou antes do incidente.

O teste prático: se investigar exige acrescentar um log e esperar o problema se
repetir, o que existe é monitoramento. Se a resposta já está nos dados coletados, é
observabilidade. `services/pedidos/tests/test_saga_integracao.py::test_spans_da_saga_formam_uma_arvore_com_a_saga_como_raiz`
faz exatamente isso: reconstrói, depois do fato, qual etapa de uma compra levou mais
tempo — sem ter instrumentado esse caso específico de antemão.

## Os três pilares, mapeados ao código

| Pilar | Módulo | Força | O que não faz sozinho |
|---|---|---|---|
| Métricas | `app/metricas.py` — `ContadorComRotulos` | Compacto, barato, bom para tendência e alerta | Agregação esconde qual requisição falhou |
| Logs | `app/logs_estruturados.py` — `registrar` | Contexto rico do que aconteceu naquele serviço | Sem correlação, é um fragmento isolado |
| Traces | `app/tracing.py` — `Span`, `ColetorDeSpans`, `iniciar_span` | Mostra onde o tempo foi gasto e em que ordem | Custo maior de instrumentação e armazenamento |

Nenhum substitui os outros. Uma investigação real é: métrica aponta que algo mudou,
trace localiza onde, log detalha o que houve ali — as três etapas de
`scripts/reconstruir_trace.py` e `docs/adr/0013-spans-locais-sem-coletor-central.md`
seguem exatamente essa ordem.

## Contexto e correlação: os quatro passos

1. O gateway gera o trace_id na entrada, se a requisição não trouxer um
   (`gerar_trace_id()` em `middleware_observabilidade`).
2. Chamadas síncronas propagam via cabeçalho `X-Trace-Id` — mecanismo que já existia
   desde a Aula 3/4 nas chamadas de `pedidos`, e que esta aula estende ao gateway.
3. **Eventos assíncronos propagam nos metadados da mensagem** — o passo mais
   frequentemente esquecido, segundo o roteiro. Até esta aula, `Evento` (em
   `app/barramento.py`) não tinha campo de trace_id; `publicador.py` publicava sem
   ele. Agora `Evento.trace_id` existe e é preenchido a partir do payload da outbox
   (que já carregava o trace_id desde a Aula 3 — só não era promovido a metadado do
   evento). Ver `test_evento_publicado_carrega_o_trace_id_do_pedido`.
4. Cada serviço extrai e reinjeta o identificador — é isso que
   `middleware_observabilidade` faz em cada um dos cinco serviços agora.

Se um único serviço no percurso deixar de propagar o contexto, o trace se rompe
naquele ponto, mesmo que todos os demais estejam perfeitamente instrumentados — a
propagação vale pelo elo mais fraco.

## O erro de cardinalidade, impossível de cometer silenciosamente

O impulso comum, depois de adotar correlação, é reaproveitar o trace_id como rótulo
de métrica. O problema: cada requisição gera um valor novo, e o sistema de métricas
passa a guardar uma série temporal por requisição.

`ContadorComRotulos.incrementar` (`app/metricas.py`) recusa qualquer dimensão não
declarada de antemão, e recusa uma dimensão declarada assim que ela ultrapassa um
número razoável de valores distintos — levantando `DimensaoDeAltaCardinalidade`. Ver
`test_contador_recusa_dimensao_que_vaza_identificador_por_requisicao`.

Na prática, `middleware_observabilidade` usa `request.scope["route"].path` (o
**padrão** da rota, como `/pedidos/{pedido_id}`) para métricas, e `request.url.path`
(o caminho **exato**, com o ID de verdade) para o nome do span. É a mesma requisição,
dois níveis de agregação diferentes, cada um correto para seu pilar —
`test_metricas_nao_explodem_com_muitos_pedidos_distintos` prova isso batendo 60 IDs
distintos na mesma rota e checando que a métrica não quebra.

Essa proteção tem um limite conhecido, aceito por simplicidade: uma rota verdadeiramente
inexistente (sem `scope["route"]`) cai de volta no caminho exato — em um serviço com
rotas fixas como este, isso não é um problema prático, mas seria uma superfície de
ataque de cardinalidade em um serviço público exposto a caminhos arbitrários.

## SLI, SLO e orçamento de erro

Um SLI (`scripts/orcamento_de_erro.py::sli_proporcao`) é sempre uma proporção sobre o
resultado que o cliente observa — checkout concluído, latência dentro do limite,
pagamento confirmado na primeira tentativa — nunca utilização de CPU. O teste: quando
o SLI se degrada, a experiência do usuário também se degrada.

O orçamento de erro é `(1 - SLO) × volume`. `scripts/test_orcamento_de_erro.py`
reproduz o exemplo do roteiro: volume de 12 milhões/mês, SLO de 99,9% → orçamento de
12 mil falhas; 9 mil consumidas nos primeiros 10 dias → 75% do orçamento em um terço
do período → esgotamento estimado por volta do dia 14. Esse número orienta decisão
concreta (reduzir mudanças arriscadas, adiar lançamento), não uma discussão subjetiva.

## Reconstruindo a cascata

`scripts/reconstruir_trace.py` implementa os dois cuidados de leitura do roteiro:

- Spans aninhados não se somam como sequenciais — a duração do filho está contida na
  do pai (`filho_esta_contido_no_pai`).
- Trabalho assíncrono com o mesmo trace_id mas em uma árvore de spans independente
  (a expedição, aqui) não faz parte do caminho crítico, mesmo durando mais
  (`maior_gargalo` restringe a busca à subárvore da requisição — ver
  `test_gargalo_ignora_arvore_assincrona_mais_longa_mas_nao_relacionada`).

`scripts/test_reconstruir_trace.py` reproduz os números exatos do incidente do
roteiro e prova que o algoritmo chega à mesma conclusão: o gargalo é a espera pelo
pool de conexões dentro de pagamento, não o provedor externo.

## O que muda quando os serviços estão em Pods diferentes

Tudo acima é verificado por teste, com quatro aplicações FastAPI no mesmo processo.
`docs/kubernetes-execucao.md` registra a mesma jornada em um cluster kind de três nós,
e a diferença é instrutiva: a **propagação** continua correta — um único trace_id
atravessou quatro serviços por rede real — mas a **leitura** deixa de existir. Os dez
spans daquela compra ficaram espalhados por sete Pods, um pedaço em cada um, e
`GET /_admin/spans/{trace_id}` pelo Service devolve o pedaço de uma réplica sorteada.

Não é um detalhe de implantação: é a razão de um coletor central existir. Instrumentar
sem agregar produz exatamente o que esta aula abriu criticando — fragmentos que,
lidos isoladamente, parecem normais.

## Decisão registrada

Ver `docs/adr/0013-spans-locais-sem-coletor-central.md`.
