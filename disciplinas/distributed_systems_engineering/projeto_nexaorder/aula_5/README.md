# Aula 5 — Replicação e consistência

**Videoaula correspondente:** Aula 5 — Replicação e modelos de consistência.

## O que esta aula acrescentou ao projeto

`services/estoque` deixa de ser um dublê e ganha persistência real, saldo por SKU e a
invariante mais cara do domínio: nunca vender o que não existe.

- `app/store.py` — `ArmazenLider`: fonte única de escrita, com transação que verifica
  saldo, decrementa e registra a reserva atomicamente.
- `app/replica.py` — `ReplicaLeitura`: réplica em memória, alimentada de forma
  assíncrona a cada escrita no líder, com **atraso fixo de 150 ms** — o mesmo número
  do exemplo numérico do roteiro.
- `GET /saldo/{sku}?consistencia=forte|eventual` — a mesma pergunta de negócio
  respondida por duas fontes diferentes, com custo e frescor diferentes.
- `docs/consistencia-por-dado.md` e `docs/adr/0005-consistencia-por-dado.md` — a
  matriz de decisão: por que a leitura informativa do saldo é eventual e a decisão de
  reservar é sempre forte.
- `_debug/config` (a injeção de falha da Aula 4) continua funcionando — a Aula 5 soma
  capacidades, não substitui as anteriores.

## O experimento central: a janela de leitura obsoleta

```bash
curl -X POST http://localhost:8002/estoque/TECLADO-MEC-01/inicializar -d '{"quantidade": 10}'
curl -X POST http://localhost:8001/pedidos/<id>/reservar-estoque   # decrementa para 9

curl "http://localhost:8002/saldo/TECLADO-MEC-01?consistencia=eventual"   # ainda 10, ou vazio
sleep 0.2
curl "http://localhost:8002/saldo/TECLADO-MEC-01?consistencia=eventual"   # agora 9

curl "http://localhost:8002/saldo/TECLADO-MEC-01?consistencia=forte"      # sempre 9, sem esperar
```

`tests/test_replica.py::test_atraso_padrao_e_150ms_como_no_roteiro_da_aula_5` prova
esse intervalo com um cronômetro real — não é um número documentado, é um número
medido a cada execução da suíte.

## Roteiro de condução

1. Rode a demonstração acima ao vivo (ou via `tests/test_replica.py`, se não houver
   tempo). O ponto: nenhuma das duas respostas está errada. Cada uma é honesta com a
   fonte que consultou.
2. Rode `tests/test_saldo_e_reservas.py::test_reservas_concorrentes_nao_vendem_mais_do_que_existe`
   e mostre que, de duas reservas concorrentes contra 1 unidade, exatamente uma vence
   — a invariante que só a leitura forte contra o líder sustenta.
3. Abra `docs/consistencia-por-dado.md` e peça à turma para classificar um dado que
   ainda não apareceu no projeto (ex.: o histórico de pedidos de um cliente) como
   forte ou eventual, com justificativa.
4. Feche com o ADR 0005: a decisão não é "qual consistência o sistema usa", é "o que
   este dado não pode tolerar".

## Como rodar

```bash
make setup
make test        # 39 testes: 26 em pedidos, 13 em estoque
make up           # docker compose, se houver Docker disponível
```

## Pergunta que fica em aberto

A réplica vive em memória, dentro do mesmo processo — não existe ainda uma segunda
instância física de `estoque`, nem uma chave que decida para qual partição um dado
vai. A Aula 6 introduz particionamento de verdade e as contas de hashing consistente.

## Estado do projeto

```
docs/
  consistencia-por-dado.md                 [novo]
  adr/0005-consistencia-por-dado.md        [novo]
services/
  estoque/
    app/
      store.py                             [reescrito: ArmazenLider com saldo real]
      replica.py                           [novo: ReplicaLeitura com atraso de 150ms]
      main.py                              [reescrito: /estoque/{sku}/inicializar, /saldo/{sku}]
    tests/
      test_saldo_e_reservas.py             [novo]
      test_replica.py                      [novo]
      test_estoque_stub.py                 [atualizado para saldo real]
  pedidos/
    tests/test_integracao_estoque.py       [atualizado: semeia saldo antes de reservar]
```

39 testes (26 em pedidos, 13 em estoque), 2 serviços, 1 invariante de negócio
protegida por transação.
