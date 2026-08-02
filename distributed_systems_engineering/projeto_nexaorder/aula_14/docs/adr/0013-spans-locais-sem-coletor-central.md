# ADR 0013 — Spans locais por serviço, sem coletor central (OpenTelemetry Collector)

- **Status:** aceito
- **Data:** correspondente à Unidade 4, Aula 13

## Contexto

A Aula 13 propõe o OpenTelemetry como padrão de instrumentação: uma API neutra de
fornecedor, com captura automática, um coletor que recebe telemetria de vários
processos e a encaminha a um backend de armazenamento e visualização (Jaeger, Tempo,
um SaaS de observabilidade). Integrar o SDK real do OpenTelemetry, um `otel-collector`
no `docker-compose.yml` e um backend de consulta exigiria rede entre contêineres e
armazenamento externo — indisponível neste ambiente de desenvolvimento (mesma classe
de limite dos ADRs 0003, 0007, 0010 e 0011).

## Decisão

Cada serviço mede seus próprios spans com `app/tracing.py` (duração real, via
`time.perf_counter()`, não números inventados) e os guarda em memória, indexados por
trace_id, expostos via `GET /_admin/spans/{trace_id}`. A reconstrução de uma cascata
entre serviços é feita por fora, em `scripts/reconstruir_trace.py`, operando sobre a
união dos spans que cada serviço relataria a um coletor real.

## Por quê

Um `otel-collector` no `docker-compose.yml` sem nenhum SDK real conectado a ele criaria
a aparência de integração sem integração — exatamente o tipo de lacuna que as ADRs
anteriores evitaram documentando o limite explicitamente, em vez de escondê-lo atrás de
um serviço decorativo. A interface pública (`ColetorDeSpans.spans_do_trace`,
`iniciar_span`) foi desenhada para que trocar por um SDK OpenTelemetry real seja uma
substituição de implementação: quem usa `iniciar_span` como gerenciador de contexto não
precisaria mudar.

## Compromisso aceito

O projeto não demonstra, em execução real, o que um coletor de verdade faz: agregação
entre processos distintos ao vivo, exportação para um backend externo, amostragem
(sampling) de spans sob alto volume. A reconstrução de uma cascata entre serviços aqui
é feita chamando `/_admin/spans/{trace_id}` em cada serviço manualmente (ou por teste),
não por um coletor que os recebe automaticamente à medida que são gerados.

O exemplo numérico do roteiro (o pedido de doze segundos) não é reproduzido ao vivo:
este sandbox não tem latência de rede real nem um provedor de pagamento externo lento
de propósito, então os números exatos do roteiro (11.450 ms de espera em fila, 310 ms
de chamada ao provedor) só existem como um conjunto de dados de teste em
`scripts/test_reconstruir_trace.py` — o algoritmo de reconstrução é real e testado; os
números daquele caso específico são o exemplo do roteiro, não uma medição.

## Evidência

`services/pedidos/tests/test_observabilidade.py` prova os três módulos isoladamente e o
comportamento HTTP dos endpoints administrativos. `test_saga_integracao.py::test_spans_da_saga_formam_uma_arvore_com_a_saga_como_raiz`
prova, com chamadas de rede reais entre quatro aplicações FastAPI, que os spans
aninham corretamente e todos carregam o mesmo trace_id.
`services/gateway/tests/test_gateway.py::test_trace_id_do_gateway_se_propaga_para_os_servicos_downstream`
prova que o trace_id chega a estoque, pagamento e expedição — a lacuna que existia até
a Aula 12 (o gateway nunca reenviava o cabeçalho). `scripts/test_reconstruir_trace.py`
prova o algoritmo de reconstrução contra o exemplo numérico exato do roteiro,
incluindo os dois cuidados de leitura que ele explicita (spans aninhados não se somam;
trabalho assíncrono não relacionado, mesmo mais longo, não é o gargalo do caminho
crítico).
