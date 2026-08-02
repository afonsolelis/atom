# Aula 8 — Sagas, outbox/inbox e idempotência

**Videoaula correspondente:** Aula 8 — Transações distribuídas, sagas e idempotência.

Esta é a aula que fecha o fluxo de compra da NexaOrder de ponta a ponta. É a maior
até aqui: dois serviços novos e a orquestração que os une a `pedidos` e `estoque`.

## O que esta aula acrescentou ao projeto

- `services/pagamento/` — novo serviço: autoriza cobranças de forma idempotente,
  compensável via `POST /cobrancas/{id}/estornar`.
- `services/expedicao/` — novo serviço: gera etiqueta de remessa de forma idempotente,
  compensável via `POST /remessas/{id}/cancelar`.
- `services/estoque/app/store.py` — nova compensação, `liberar_reserva`, que devolve
  o saldo e marca a reserva como liberada.
- `services/pedidos/app/duas_fases.py` — simulador de 2PC, só para demonstrar em
  teste por que o projeto não o adota: bloqueio de participantes e risco agregado.
- `services/pedidos/app/saga.py` — `SagaCompra`: orquestra as três etapas com
  compensação automática em cascata.
- `services/pedidos/app/store.py` — outbox: todo `PedidoCriado` agora é gravado na
  mesma transação que o pedido, pronto para ser publicado a partir da Aula 10.
- `POST /pedidos/{id}/finalizar-compra` — o novo endpoint que executa a saga completa.

## O experimento central: compensação em cascata

```bash
docker compose up --build
curl -X POST http://localhost:8002/estoque/TECLADO-MEC-01/inicializar -d '{"quantidade": 100}'

# força a expedição a falhar sempre
curl -X POST http://localhost:8004/_debug/config -d '{"falhar_percentual": 100}'

PEDIDO_ID=$(curl -s -X POST http://localhost:8001/pedidos -d '...' | jq -r .id)
curl -X POST http://localhost:8001/pedidos/$PEDIDO_ID/finalizar-compra
# -> sucesso: false, falhou_em: "solicitar_expedicao"
#    compensacoes: [estornar_pagamento, liberar_estoque]

curl http://localhost:8002/saldo/TECLADO-MEC-01?consistencia=forte
# -> o saldo voltou a 100: a compensação funcionou de verdade, não só no papel
```

`tests/test_saga_integracao.py` automatiza exatamente essa verificação, com HTTP real
entre as quatro aplicações.

## Roteiro de condução

1. Rode `tests/test_duas_fases.py::test_2pc_bloqueia_participantes_se_coordenador_falha_apos_preparar`
   e `test_risco_agregado_com_quatro_participantes_a_um_por_cento` — o argumento
   completo contra 2PC, em dois testes.
2. Rode `tests/test_saga.py` (lógica isolada, com etapas simuladas) e depois
   `tests/test_saga_integracao.py` (HTTP real). Mostre que são as mesmas três
   asserções de compensação, provadas em dois níveis diferentes.
3. Abra `store.py` de `pedidos` e mostre a tabela `outbox` sendo escrita na mesma
   transação do pedido. Rode `tests/test_outbox.py` e explique: ninguém publica isso
   ainda, e está tudo bem — a Aula 10 traz o publicador.
4. Feche com o ADR 0008 e a pergunta que a Aula 9 resolve: será que `estoque` e
   `pedidos` continuam realmente isolados um do outro, ou o acoplamento se escondeu
   em algum lugar que ninguém olhou ainda?

## Como rodar

```bash
make setup
make test        # 85 testes: 42 pedidos, 34 estoque, 5 pagamento, 4 expedicao
make up           # docker compose com os quatro serviços
```

## Pergunta que fica em aberto

O fluxo de compra está completo, mas os quatro serviços ainda se enxergam por HTTP
síncrono, ponto a ponto, com URLs fixas configuradas por variável de ambiente. A
Unidade 3 começa questionando se as fronteiras entre eles estão realmente onde
deveriam, e a Aula 10 substitui essas chamadas síncronas por eventos.

## Estado do projeto

```
docs/
  saga.md                                    [novo]
  adr/0008-saga-orquestrada.md               [novo]
services/
  pagamento/                                 [novo serviço]
    app/store.py, main.py
    tests/test_pagamento.py
  expedicao/                                 [novo serviço]
    app/store.py, main.py
    tests/test_expedicao.py
  estoque/
    app/store.py                             [alterado: liberar_reserva]
    app/main.py                              [alterado: POST /reservas/{id}/liberar]
  pedidos/
    app/duas_fases.py                        [novo]
    app/saga.py                              [novo]
    app/store.py                             [alterado: outbox]
    app/main.py                              [alterado: POST /pedidos/{id}/finalizar-compra]
docker-compose.yml                            [alterado: 4 serviços]
Makefile                                      [alterado: 4 serviços]
```

85 testes (42 pedidos, 34 estoque, 5 pagamento, 4 expedicao), 4 serviços, 1 saga
completa com compensação verificada de ponta a ponta.
