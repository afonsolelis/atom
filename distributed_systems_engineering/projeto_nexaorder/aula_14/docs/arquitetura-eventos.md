# Arquitetura orientada a eventos — Unidade 3, Aula 10

## O que está implementado, e o que é simplificação

`services/pedidos/app/barramento.py` implementa `Topico`, `escolher_particao` e
`GrupoConsumidores` — em memória, dentro do processo de `pedidos`, sem rede real.
É a mesma decisão de simplificação já tomada para consenso (Aula 7, ADR 0007) e para
2PC (Aula 8): a mecânica importa mais, para o objetivo didático, do que a
infraestrutura de transporte.

**O que isso significa na prática:** este projeto não integra Redpanda ou Kafka de
verdade. Um `docker-compose.yml` com um serviço de broker, sem nenhum código
cliente conectado a ele, criaria a aparência de integração sem a integração —
por isso ele não foi adicionado. A migração para um broker real seria uma troca do
`Topico` em memória por um cliente Kafka/Redpanda (`aiokafka`, por exemplo), mantendo
exatamente a mesma interface pública (`publicar`, `ler_particao`, `GrupoConsumidores`)
— a prova de que a abstração está no lugar certo.

## Comando, evento e notificação

O contrato da Aula 2 (`docs/contratos/eventos.md`) já definia `PedidoCriado` como
evento de domínio — particípio passado, sem destinatário específico. Esta aula é a
primeira em que esse evento é **publicado** de verdade (em memória) em vez de apenas
gravado na outbox (Aula 8).

## O publicador fecha a outbox

`services/pedidos/app/publicador.py::publicar_eventos_pendentes` lê a tabela outbox
(Aula 8), publica cada evento pendente no tópico `pedidos-eventos` — usando o
`pedido_id` como chave de partição — e marca como publicado. `POST
/_admin/publicar-eventos` aciona isso manualmente; em produção, um processo
contínuo faria o mesmo em laço.

## Partições: por que a chave é `pedido_id`

Todos os eventos de um mesmo pedido precisam chegar em ordem a quem os consome —
`PedidoCriado` antes de `EstoqueReservado`, antes de `PagamentoAprovado`. Isso só é
garantido dentro de uma partição. Particionar por `pedido_id` garante que a sequência
inteira de um pedido caia sempre na mesma partição.
`tests/test_barramento.py::test_particionamento_por_tipo_de_evento_quebra_a_ordem_do_pedido`
demonstra o erro oposto: particionar pelo tipo do evento espalha a sequência de um
pedido entre partições diferentes, e a ordem se perde.

## Dimensionamento: o mesmo cálculo da Aula 1, aplicado a partições

```
N = ⌈ taxa_de_eventos_no_pico / capacidade_por_consumidor ⌉
N = ⌈ 1200 / 150 ⌉ = 8
```

`NUM_PARTICOES_PEDIDOS = 8` em `publicador.py` não é um número arbitrário — é este
cálculo, com os mesmos números do roteiro da Aula 10.

## Grupos de consumidores

`main.py` cria um grupo `auditoria` com uma única instância, que lê o tópico
`pedidos-eventos` via `GET /_admin/auditoria/consumir`. Cada chamada só devolve
eventos novos desde a última leitura — o deslocamento (offset) avança por chamada,
exatamente como um consumidor real avançaria por partição.
`tests/test_barramento.py::test_dois_grupos_independentes_leem_o_mesmo_topico_sem_interferir`
prova que múltiplos grupos podem coexistir sem interferência — a base para,
futuramente, adicionar um segundo grupo (por exemplo, `notificacoes`) sem tocar no
primeiro.

## Evolução de esquema

`tests/test_evolucao_esquema.py` prova, com exemplos concretos, as duas direções de
compatibilidade já discutidas na Aula 2: um consumidor antigo ignora um campo novo
(compatibilidade prospectiva); um consumidor novo aplica um valor padrão para um
campo ausente em um evento antigo (compatibilidade retroativa); e renomear um campo
sem transição quebra o consumidor antigo — a mudança perigosa.

## Decisão registrada

Ver `docs/adr/0010-barramento-em-memoria.md`.
