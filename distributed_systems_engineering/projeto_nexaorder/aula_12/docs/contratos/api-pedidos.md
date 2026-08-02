# Contrato de API — serviço Pedidos

Este é o primeiro contrato explícito do projeto. Ele existe antes do código
(implementado na Aula 3) porque um contrato escrito é o que permite testar
consumidor e provedor em separado — o assunto da Aula 14 (testes de contrato).

## `POST /pedidos`

Cria um pedido. Idempotente por `chave_idempotencia`.

**Requisição**

```json
{
  "cliente_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "chave_idempotencia": "6f1c0a2e-...-checkout-1",
  "itens": [
    { "sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90 }
  ]
}
```

**Resposta — `201 Created`**

```json
{
  "id": "b7e6c1d0-...",
  "estado": "RECEBIDO",
  "criado_em": "2026-08-01T14:32:10Z",
  "total": 349.90
}
```

**Resposta — `200 OK`** quando a `chave_idempotencia` já existe: devolve o mesmo
pedido, sem criar um segundo. Ver Aula 8 para o mecanismo completo de idempotência.

**Códigos de erro**

| Código | Situação |
|--------|----------|
| `400` | itens vazios, quantidade não positiva, ou payload malformado |
| `409` | mesma `chave_idempotencia`, corpo diferente do pedido original |
| `422` | violação de schema |

## `GET /pedidos/{id}`

Consulta o estado atual de um pedido — sem efeito colateral.

**Resposta — `200 OK`**

```json
{
  "id": "b7e6c1d0-...",
  "estado": "RESERVADO",
  "itens": [
    { "sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90 }
  ],
  "total": 349.90,
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736"
}
```

O campo `trace_id` existe desde a Aula 3 — é o identificador de correlação que
atravessa todos os serviços tocados por este pedido.

## Cabeçalhos comuns a todas as rotas

| Cabeçalho | Origem | Propósito |
|-----------|--------|-----------|
| `X-Trace-Id` | gerado por `pedidos` na entrada, propagado pelos demais | correlação de requisições (Aula 3) |
| `X-Idempotency-Key` | alternativa ao campo no corpo, para rotas sem corpo | idempotência (Aula 8) |

## Semântica de status

| Estado | Significa |
|--------|-----------|
| `RECEBIDO` | pedido registrado, estoque ainda não confirmado |
| `RESERVADO` | estoque confirmou a reserva |
| `PAGO` | pagamento autorizado |
| `EXPEDIDO` | remessa despachada |
| `CANCELADO` | qualquer etapa falhou de forma definitiva e as compensações já rodaram |

Este contrato é reimplementado literalmente em `services/pedidos` a partir da Aula 3.
