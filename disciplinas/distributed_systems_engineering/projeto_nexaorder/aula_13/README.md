# Aula 13 — Observabilidade e diagnóstico distribuído

**Videoaula correspondente:** Aula 13 — Observabilidade e diagnóstico distribuído.

## O que esta aula acrescentou ao projeto

- `services/*/app/logs_estruturados.py`, `metricas.py`, `tracing.py` — em todos os
  cinco serviços: logs em JSON com trace_id anexado, um contador de métricas que
  recusa dimensões de alta cardinalidade (`DimensaoDeAltaCardinalidade`), e spans com
  duração real medida via `time.perf_counter()`, aninháveis via `ContextVar`.
- `app/correlation.py` (que só existia em `pedidos` desde a Aula 3) agora existe em
  `estoque`, `pagamento`, `expedicao` e `gateway` — e cada um ganha
  `middleware_observabilidade`, unindo os três pilares na mesma passagem.
- **O gateway passa a propagar o trace_id.** Até a Aula 12, ele o gerava ou recebia na
  borda e nunca reenviava — nenhuma das quatro chamadas que faz carregava
  `X-Trace-Id`. Corrigido, e provado por
  `test_trace_id_do_gateway_se_propaga_para_os_servicos_downstream`.
- **O salto assíncrono passa a propagar o trace_id.** `Evento` (em
  `services/pedidos/app/barramento.py`) ganha o campo `trace_id`; `publicador.py` o
  preenche a partir do payload da outbox ao publicar — o terceiro passo da
  propagação, o mais frequentemente esquecido segundo o roteiro.
- `GET /_admin/spans/{trace_id}` e `GET /_admin/metricas` em cada serviço.
  `pedidos` encadeia spans filhos em cada etapa da saga (`reservar_estoque`,
  `autorizar_pagamento`, `solicitar_expedicao` e suas compensações); `gateway`
  encadeia spans filhos em suas três buscas concorrentes.
- `scripts/reconstruir_trace.py` + `scripts/orcamento_de_erro.py` — os dois exemplos
  numéricos do roteiro (o trace em cascata do pedido de doze segundos; o orçamento de
  erro de 12 mil falhas/mês) reproduzidos como código testado.
- `docs/observabilidade.md` e `docs/adr/0013-spans-locais-sem-coletor-central.md`.

## As duas lacunas reais que esta aula fecha

Até a Aula 12, mesmo com `pedidos` gerando e enviando um trace_id desde a Aula 3, a
jornada se rompia em dois pontos concretos e verificáveis neste próprio projeto:

1. O **gateway** nunca reenviava o `X-Trace-Id` recebido — o primeiro salto já
   perdia a correlação, mesmo com os outros quatro serviços perfeitamente
   instrumentados.
2. O **barramento de eventos** não carregava trace_id nenhum — o salto assíncrono
   (Aula 8/10) sempre foi um ponto cego, mesmo que o trace_id já estivesse disponível
   no payload da outbox desde o primeiro dia.

Ambos têm teste provando a correção — não é afirmação em prosa.

## O gargalo real não é o suspeito óbvio

```bash
python3 scripts/reconstruir_trace.py   # (biblioteca — ver scripts/test_reconstruir_trace.py)
```

Reproduzindo os números exatos do roteiro (gateway 12.000 ms, pagamento 11.780 ms,
com um filho de 11.450 ms de espera em fila e outro de 310 ms no provedor externo),
`maior_gargalo` aponta a espera em fila — não o provedor externo, o suspeito
intuitivo por estar fora do controle da equipe. E ignora corretamente a árvore
assíncrona da expedição (120.000 ms), mesmo sendo numericamente maior, porque ela não
pertence ao caminho que o cliente esperou.

## Cardinalidade não é teórica aqui

`test_metricas_nao_explodem_com_muitos_pedidos_distintos` (em `services/pedidos`)
bate `GET /pedidos/{id}` com 60 UUIDs distintos e prova que a métrica não quebra: o
middleware usa `request.scope["route"].path` (o padrão da rota) para métricas, e
`request.url.path` (o caminho exato) para o nome do span — dois níveis de agregação
diferentes, cada um correto para seu pilar.

## Roteiro de condução

1. Rode `test_spans_da_saga_formam_uma_arvore_com_a_saga_como_raiz` (em
   `services/pedidos`) — mostra, com chamadas de rede reais entre quatro aplicações
   FastAPI, uma árvore de spans genuína (não simulada) se formando durante uma compra.
2. Rode `scripts/test_reconstruir_trace.py` e mostre `maior_gargalo` acertando a
   espera em fila, não o provedor externo — a virada do roteiro.
3. Rode `scripts/test_orcamento_de_erro.py::test_dia_estimado_de_esgotamento_bate_com_o_roteiro`
   — do SLO à decisão de adiar um lançamento, em uma linha de código.
4. Feche com `test_contador_recusa_dimensao_que_vaza_identificador_por_requisicao` —
   o erro de cardinalidade, impossível de cometer silenciosamente neste projeto.

## Como rodar

```bash
make setup
make test          # 167 testes: 76 pedidos, 48 estoque, 8 pagamento, 7 expedicao, 6 gateway, 22 scripts
make verificar      # fronteiras + instabilidade (Aula 9)
make validar-k8s    # os cinco manifests
make up             # contêineres (Docker ou Podman) com os cinco serviços de aplicação
```

## Pergunta que fica em aberto

Observabilidade permite ver o que o sistema fez. Não prova que a resiliência
desenhada desde a Unidade 1 — disjuntor, retry, saga — funciona sob falha real, nem
que o sistema se recupera do jeito que o projeto sempre presumiu. Essa validação
deliberada é a pergunta da Aula 14.

## Estado do projeto

```
docs/
  observabilidade.md                                    [novo]
  adr/0013-spans-locais-sem-coletor-central.md          [novo]
services/*/app/logs_estruturados.py                      [novo, idêntico em cada serviço]
services/*/app/metricas.py                                [novo, idêntico em cada serviço]
services/*/app/tracing.py                                 [novo, idêntico em cada serviço]
services/{estoque,pagamento,expedicao,gateway}/app/correlation.py  [novo — só pedidos tinha]
services/*/app/main.py                                    [alterado: middleware_observabilidade, /_admin/spans e /_admin/metricas]
services/pedidos/app/main.py                              [alterado: spans filhos em cada etapa da saga]
services/gateway/app/main.py                              [alterado: propaga X-Trace-Id às 4 chamadas downstream]
services/pedidos/app/barramento.py                        [alterado: Evento.trace_id]
services/pedidos/app/publicador.py                        [alterado: propaga trace_id ao publicar]
services/pedidos/tests/test_observabilidade.py            [novo: 14 testes]
services/pedidos/tests/test_saga_integracao.py            [alterado: +1 teste (árvore de spans)]
services/pedidos/tests/test_publicador.py                 [alterado: +1 teste (trace_id no evento)]
services/gateway/tests/test_gateway.py                    [alterado: +1 teste (propagação via gateway)]
scripts/reconstruir_trace.py + test                        [novo: 6 testes]
scripts/orcamento_de_erro.py + test                        [novo: 6 testes]
```

167 testes, os três pilares como código real e testado em cada um dos cinco
serviços, e as duas lacunas de propagação (gateway, barramento) fechadas com prova.
