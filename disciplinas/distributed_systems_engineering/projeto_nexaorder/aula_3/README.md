# Aula 3 — Primeiro serviço em código

**Videoaula correspondente:** Aula 3 — Concorrência, relógios e ordenação de eventos.

## O que esta aula acrescentou ao projeto

Tudo o que existia na Aula 2, mais o primeiro código executável: `services/pedidos`,
um serviço FastAPI real, com banco próprio, que implementa exatamente o contrato
escrito na Aula 2.

- `app/main.py` — a API: `POST /pedidos` (idempotente), `GET /pedidos/{id}`, `GET /saude`.
- `app/store.py` — persistência em SQLite, **arquivo próprio deste serviço**. Nenhum
  outro serviço vai ler `pedidos.db` diretamente — essa regra, formalizada só na
  Aula 9, já vale desde a primeira linha.
- `app/correlation.py` — gera e propaga o `X-Trace-Id`. Ainda não há um segundo
  serviço para observar a propagação de verdade, mas o mecanismo precisa nascer agora,
  porque a Aula 4 já introduz uma segunda chamada de rede.
- `app/lamport.py` — o relógio lógico de Lamport, implementado como classe reutilizável
  e usado para carimbar cada pedido criado.
- `tests/test_lamport.py` — reproduz **literalmente** a sequência de cinco eventos do
  roteiro da Aula 3 (Pedidos cria → envia → Estoque recebe → confirma → Pedidos
  recebe), com os mesmos números: 1, 2, 3, 4, 5.
- `tests/test_api_pedidos.py` — testa o contrato da Aula 2 contra o código real.

## Por que o relógio de Lamport aparece sem um segundo serviço rodando

O Estoque como serviço HTTP só nasce na Aula 5. Para não antecipar isso artificialmente,
o teste `test_sequencia_completa_pedidos_e_estoque_da_aula_3` simula a troca de
mensagens instanciando dois relógios (`pedidos` e `estoque`) dentro do próprio teste —
a mesma técnica de dois processos lógicos, sem a infraestrutura de rede ainda.
É a peça de infraestrutura pronta e testada, à espera do segundo processo real.

## Como rodar

```bash
make setup   # cria o venv e instala fastapi, uvicorn, pydantic, pytest
make test    # roda os 12 testes
make run     # sobe o serviço em http://127.0.0.1:8001
```

Com o serviço no ar:

```bash
curl -X POST http://127.0.0.1:8001/pedidos \
  -H "Content-Type: application/json" \
  -d '{"cliente_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","chave_idempotencia":"aula-3-demo","itens":[{"sku":"TECLADO-MEC-01","quantidade":1,"preco_unitario":349.90}]}'
```

A resposta traz `trace_id` e `carimbo_lamport` — os dois conceitos centrais desta aula,
visíveis no JSON que volta para o terminal.

## Roteiro de condução

1. Rode `make test` com a turma olhando. Abra `test_sequencia_completa_pedidos_e_estoque_da_aula_3`
   e mostre que os números do teste são os números do quadro.
2. Suba o serviço com `make run` e crie um pedido pelo curl. Chame duas vezes com a
   mesma `chave_idempotencia` e mostre que o `id` não muda — a primeira demonstração
   prática de idempotência, embora o mecanismo completo só feche na Aula 8.
3. Chame de novo sem cabeçalho `X-Trace-Id` e depois enviando um. Mostre que a API
   sempre devolve um, gerado ou propagado.
4. Pergunta para a turma: por que o `carimbo_lamport` do pedido não é o mesmo que o
   `criado_em`? Um é físico, o outro é lógico — a distinção inteira da Aula 3.

## Pergunta que fica em aberto

O serviço roda, mas sozinho, e sem proteção contra falha de rede. A Aula 4 escolhe a
tecnologia de resiliência (timeout, retry, circuit breaker) e sobe o primeiro
`docker-compose.yml` — a primeira vez que "rodar o projeto" deixa de significar "rodar
um processo".

## Estado do projeto

```
docs/                          (igual à Aula 2)
services/
  pedidos/                     [novo]
    app/
      main.py
      models.py
      store.py
      lamport.py
      correlation.py
    tests/
      test_api_pedidos.py
      test_lamport.py
    requirements.txt
Makefile                       [novo]
```

12 testes, 1 serviço, 0 dependências externas de infraestrutura (SQLite é arquivo local).
