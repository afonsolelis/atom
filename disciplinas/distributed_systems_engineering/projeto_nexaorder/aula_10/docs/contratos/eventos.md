# Contrato de eventos — NexaOrder

> **Atualização da Aula 10:** `PedidoCriado` agora é publicado de verdade — ver
> `services/pedidos/app/publicador.py` e `docs/arquitetura-eventos.md`. Os demais
> eventos (`EstoqueReservado`, `PagamentoAprovado`, `PedidoExpedido`) continuam
> descritos aqui como contrato, mas ainda viajam por chamada HTTP síncrona dentro da
> saga (Aula 8) — a saga orquestrada permanece o mecanismo de coordenação
> transacional; a publicação de eventos serve consumidores adicionais (auditoria,
> e no futuro notificações), não substitui os passos da saga.

Estes eventos foram definidos na Aula 2, antes de existir qualquer transporte para
eles — um contrato de mensagem precisa existir **antes** do código que o consome, do
mesmo jeito que o contrato de API.

Convenção de nome: `SubstantivoParticípio` — o tempo verbal do passado marca que é
um fato consumado, não uma ordem (ver Aula 10, comando vs. evento).

## `PedidoCriado`

Publicado por `pedidos` assim que a intenção de compra é registrada.

```json
{
  "tipo": "PedidoCriado",
  "versao": 1,
  "pedido_id": "b7e6c1d0-...",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "ocorrido_em": "2026-08-01T14:32:10Z",
  "dados": {
    "cliente_id": "3fa85f64-...",
    "itens": [{ "sku": "TECLADO-MEC-01", "quantidade": 1, "preco_unitario": 349.90 }],
    "total": 349.90
  }
}
```

**Chave de partição (Aula 6 e 10):** `pedido_id` — garante que todos os eventos deste
pedido cheguem em ordem à mesma partição.

## `EstoqueReservado` / `EstoqueIndisponivel`

Publicado por `estoque` em resposta a `PedidoCriado`.

```json
{
  "tipo": "EstoqueReservado",
  "versao": 1,
  "pedido_id": "b7e6c1d0-...",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "ocorrido_em": "2026-08-01T14:32:11Z",
  "dados": { "reserva_id": "9c4f...", "sku": "TECLADO-MEC-01", "quantidade": 1 }
}
```

## `PagamentoAprovado` / `PagamentoRecusado`

```json
{
  "tipo": "PagamentoAprovado",
  "versao": 1,
  "pedido_id": "b7e6c1d0-...",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "ocorrido_em": "2026-08-01T14:32:13Z",
  "dados": { "cobranca_id": "1a2b...", "valor": 349.90, "referencia_externa": "prov-8899" }
}
```

## `PedidoExpedido`

```json
{
  "tipo": "PedidoExpedido",
  "versao": 1,
  "pedido_id": "b7e6c1d0-...",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "ocorrido_em": "2026-08-01T14:35:40Z",
  "dados": { "remessa_id": "77aa...", "codigo_rastreio": "NX-000123-BR" }
}
```

## Regras de evolução (aplicadas a partir da Aula 10)

- Campo novo: sempre opcional, com valor padrão bem definido quando ausente.
- Nunca remover ou renomear um campo que consumidores existentes ainda usam.
- Mudança incompatível: versionar explicitamente (`"versao": 2`) e publicar nos dois
  formatos durante a transição.

## Pré-condição de negócio que os eventos não substituem

Mesmo desacoplados por eventos, a sequência `PedidoCriado → EstoqueReservado →
PagamentoAprovado → PedidoExpedido` preserva uma ordem de negócio: a expedição nunca
pode reagir antes da aprovação do pagamento. Desacoplamento não autoriza expedir antes
de cobrar — a implementação dessa regra é o assunto da Aula 8 (saga).
