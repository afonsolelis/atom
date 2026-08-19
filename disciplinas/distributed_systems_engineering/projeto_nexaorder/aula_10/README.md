# Aula 10 — Arquitetura orientada a eventos

**Videoaula correspondente:** Aula 10 — Arquitetura orientada a eventos.

## O que esta aula acrescentou ao projeto

- `services/pedidos/app/barramento.py` — `Topico`, `escolher_particao` e
  `GrupoConsumidores`: um barramento de eventos em memória, com as mesmas garantias
  de ordem-por-partição e paralelismo-por-grupo de uma plataforma real.
- `services/pedidos/app/publicador.py` — fecha o padrão outbox da Aula 8: lê os
  eventos pendentes e os publica no tópico `pedidos-eventos`, particionado por
  `pedido_id`, com `NUM_PARTICOES_PEDIDOS = 8` calculado pela mesma fórmula da Aula 1.
- `POST /_admin/publicar-eventos` e `GET /_admin/auditoria/consumir` — os dois
  endpoints que tornam o publicador e um grupo de consumidores observáveis via HTTP.
- `docs/arquitetura-eventos.md` e `docs/adr/0010-barramento-em-memoria.md` — o que
  está implementado fielmente e por que não há um broker real (Redpanda/Kafka)
  integrado neste projeto.
- `tests/test_evolucao_esquema.py` — as três regras de compatibilidade de esquema da
  Aula 2, agora com exemplos de código, não apenas prosa.

## Por que não há Redpanda no docker-compose

Isto é uma decisão registrada, não uma lacuna esquecida. Adicionar um serviço de
broker ao Compose sem nenhum código cliente conectado a ele criaria a aparência de
integração sem integração de fato — o ADR 0010 explica a decisão e o que mudaria se
um broker real fosse integrado depois (troca de implementação, não de interface).

## O experimento central: ordem por partição

```python
from app.barramento import Topico

topico = Topico(nome="pedidos-eventos", num_particoes=8)
chave = "pedido-4021"

topico.publicar(chave, "PedidoCriado", {"seq": 1})
topico.publicar(chave, "EstoqueReservado", {"seq": 2})
topico.publicar(chave, "PagamentoAprovado", {"seq": 3})
topico.publicar(chave, "PedidoExpedido", {"seq": 4})

particao = topico.particao_da_chave(chave)
[e.payload["seq"] for e in topico.ler_particao(particao)]
# -> [1, 2, 3, 4] — sempre nesta ordem, porque caem sempre na mesma partição
```

## Roteiro de condução

1. Rode `tests/test_barramento.py::test_eventos_da_mesma_chave_chegam_em_ordem_na_mesma_particao`
   e depois `test_particionamento_por_tipo_de_evento_quebra_a_ordem_do_pedido` — o
   argumento inteiro da escolha de chave, em dois testes.
2. Rode `tests/test_barramento.py::test_numero_minimo_de_particoes_do_exemplo_da_aula`
   e conecte com `NUM_PARTICOES_PEDIDOS = 8` em `publicador.py` — não é coincidência,
   é a mesma conta.
3. Com o serviço no ar (`make run-pedidos`), crie um pedido, chame
   `POST /_admin/publicar-eventos` e depois `GET /_admin/auditoria/consumir` duas
   vezes seguidas — mostre que a segunda chamada devolve lista vazia, porque o
   deslocamento já avançou.
4. Feche com `tests/test_evolucao_esquema.py::test_renomear_campo_sem_transicao_quebra_o_consumidor_antigo`
   — a mudança perigosa, com um `KeyError` real, não apenas descrita em texto.

## Como rodar

```bash
make setup
make test         # 108 testes: 58 pedidos, 36 estoque, 6 pagamento, 5 expedicao, 3 gateway
make up            # contêineres (Docker ou Podman) com os cinco serviços (broker de eventos não incluído — ver ADR 0010)
```

## Pergunta que fica em aberto

A comunicação continua majoritariamente síncrona — a saga da Aula 8 não foi
substituída, só ganhou uma trilha adicional de eventos publicados. Os serviços rodam
como processos soltos, sem orquestração, sem sonda de saúde real e sem escalonamento
automático. A Unidade 4 começa pela Aula 11 respondendo exatamente a isso:
contêineres e Kubernetes.

## Estado do projeto

```
docs/
  arquitetura-eventos.md                     [novo]
  adr/0010-barramento-em-memoria.md          [novo]
  contratos/eventos.md                       [atualizado: nota da Aula 10]
services/
  pedidos/
    app/
      barramento.py                          [novo]
      publicador.py                          [novo]
      main.py                                [alterado: /_admin/publicar-eventos, /_admin/auditoria/consumir]
    tests/
      test_barramento.py                     [novo]
      test_publicador.py                     [novo]
      test_evolucao_esquema.py               [novo]
```

108 testes (58 pedidos, 36 estoque, 6 pagamento, 5 expedicao, 3 gateway), 1 barramento
de eventos com ordem garantida por partição, provada em teste.
