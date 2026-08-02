# Sagas, outbox/inbox e idempotência — Unidade 2, Aula 8

## Por que não 2PC

`services/pedidos/app/duas_fases.py` implementa e testa o 2PC — não para uso no
projeto, mas para provar, em código, os três comportamentos do roteiro:
- confirma quando todos os participantes votam pronto;
- aborta quando qualquer um vota abortar;
- **bloqueia os participantes** se o coordenador falhar entre preparar e decidir.

`tests/test_duas_fases.py::test_risco_agregado_com_quatro_participantes_a_um_por_cento`
reproduz o argumento numérico: com 4 participantes a 1% de chance de lentidão cada,
o risco agregado do fluxo sobe para ~3,9% — quase quatro vezes o risco individual.

## A saga adotada: orquestrada, com compensação

`services/pedidos/app/saga.py` implementa `SagaCompra`: uma sequência de transações
locais — reservar estoque, autorizar pagamento, solicitar expedição — cada uma
confinada ao seu próprio serviço e banco, sem bloqueio entre elas.

É **orquestrada**, não coreografada: `pedidos` decide a próxima etapa e conduz a
compensação, em vez de cada serviço reagir a eventos dos outros sem coordenador
central. A escolha se justifica pelo tamanho do fluxo (poucos passos, mas com
compensação em cascata) — o roteiro registra que coreografia funciona melhor para
poucos passos e acoplamento mínimo; aqui, a necessidade de auditar a saga inteira em
um único lugar pesou mais.

### Compensações por etapa

| Etapa falhou em | Compensações executadas, em ordem |
|-------------------|--------------------------------------|
| `reservar_estoque` | nenhuma — nada foi feito ainda |
| `autorizar_pagamento` | liberar a reserva de estoque |
| `solicitar_expedicao` | estornar o pagamento, depois liberar a reserva de estoque |

`tests/test_saga.py` prova as três linhas da tabela isoladamente, com etapas
simuladas. `tests/test_saga_integracao.py` prova as mesmas três linhas com HTTP real
entre `pedidos`, `estoque`, `pagamento` e `expedicao` — inclusive verificando que o
saldo de estoque realmente volta ao valor original depois da compensação.

## Idempotência: a mesma ideia, agora em três serviços

Cada chamada de saga carrega uma chave de idempotência derivada do `pedido_id` e do
nome da etapa (`f"{pedido_id}:pagamento"`, `f"{pedido_id}:expedicao"`). Isso significa
que, se o `ClienteResiliente` (Aula 4) retentar uma chamada depois de um timeout, a
segunda tentativa não duplica o efeito — `pagamento` e `expedicao` devolvem o mesmo
recurso já criado, exatamente como `pedidos` já fazia desde a Aula 3.

Isto é o **inbox** do roteiro: um mecanismo de deduplicação, do lado de quem recebe a
requisição, que só funciona porque a verificação da chave e a criação do recurso
acontecem na mesma transação local (ver `store.py` de cada serviço).

## Outbox: metade implementada, metade adiada

`services/pedidos/app/store.py` grava, na mesma transação SQLite que cria o pedido,
uma linha na tabela `outbox` com o evento `PedidoCriado`. É a metade que resolve o
problema da escrita dupla: o pedido e o evento pendente existem juntos, ou nenhum dos
dois existe.

A outra metade — um processo que lê a outbox e publica de fato os eventos — só existe
a partir da Aula 10, quando há um broker para publicar. `tests/test_outbox.py` prova
a metade implementada com `eventos_pendentes()` e `marcar_publicado()`.

## Decisão registrada

Ver `docs/adr/0008-saga-orquestrada.md`.
