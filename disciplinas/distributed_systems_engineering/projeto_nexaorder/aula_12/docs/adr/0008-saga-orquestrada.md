# ADR 0008 — Saga orquestrada em vez de 2PC ou coreografia

- **Status:** aceito
- **Data:** correspondente à Unidade 2, Aula 8

## Contexto

A compra da NexaOrder atravessa quatro serviços, cada um com seu próprio banco. Não
existe mais uma transação única que garanta que todas as etapas aconteçam juntas ou
nenhuma.

## Decisão

Adotar uma saga **orquestrada**: `pedidos` coordena reservar estoque, autorizar
pagamento e solicitar expedição, com compensação explícita e automática em cascata
quando qualquer etapa falha.

## Por quê

2PC foi descartado porque bloqueia participantes quando o coordenador falha entre as
fases (demonstrado em `duas_fases.py`), e porque o risco agregado cresce rapidamente
com o número de participantes (~3,9% com 4 participantes a 1% cada). Coreografia foi
descartada porque, com compensação em cascata de até duas etapas, teria exigido que
cada serviço soubesse reagir a falhas de serviços que não chamou diretamente — a saga
inteira deixaria de existir em um único lugar auditável.

## Compromisso aceito

Existe um intervalo em que o pedido está parcialmente processado (por exemplo,
estoque reservado, pagamento ainda não autorizado). Esse estado intermediário é
visível via `GET /pedidos/{id}` — o campo `estado` reflete exatamente onde a saga
parou, o que é necessário para que suporte e observabilidade (Aula 13) consigam
diagnosticar um pedido travado.

Compensações também podem falhar (ver `_liberar_estoque` e `_estornar_pagamento` em
`main.py`, que engolem erros de rede deliberadamente) — uma compensação que falha
silenciosamente é, em produção, um incidente a ser alertado, não uma exceção a
propagar de volta ao cliente. A Aula 13 formaliza como observar isso.

## Evidência

`tests/test_saga.py` (lógica isolada) e `tests/test_saga_integracao.py` (HTTP real
entre quatro serviços) provam as três compensações da tabela em `docs/saga.md`,
incluindo a verificação de que o saldo de estoque volta ao valor original depois de
uma compensação.
