# Aula 4 — Escolha de tecnologia, resiliência e primeiro Compose

**Videoaula correspondente:** Aula 4 — Modelos de falha e desenho para recuperação.

## O que esta aula acrescentou ao projeto

Tudo o que existia na Aula 3, mais um segundo serviço e a proteção da chamada entre
os dois:

- `docs/adr/0003-stack-tecnologica.md` — por que Python/FastAPI/SQLite/Compose, com
  as alternativas descartadas e o compromisso aceito.
- `docs/adr/0004-resiliencia-timeout-retry-disjuntor.md` — a decisão de proteger a
  chamada `pedidos → estoque` com timeout, retry e disjuntor, com os mesmos números do
  roteiro da Aula 4.
- `services/pedidos/app/resiliencia.py` — `CircuitBreaker` (janela de 20, limite de
  50%), `backoff_com_jitter` (a mesma fórmula da Aula 2) e `ClienteResiliente`, que
  combina os três.
- `POST /pedidos/{id}/reservar-estoque` — novo endpoint em `pedidos`, a primeira
  chamada de rede real do projeto entre dois processos distintos.
- `services/estoque/` — **um dublê controlável**, não o serviço final. Aceita
  `POST /reservas` e expõe `POST /_debug/config` para injetar falha e atraso sob
  demanda, exatamente para poder demonstrar o disjuntor abrindo em aula. A persistência
  e a simulação de réplica chegam na Aula 5.
- `Dockerfile` em cada serviço e o primeiro `docker-compose.yml` do projeto.

## Por que Estoque nasce como dublê, e não como serviço completo

O foco desta aula é a *proteção* da chamada de rede, não a lógica de negócio do outro
lado dela. Um dublê com falha e atraso controláveis por HTTP ensina exatamente o que a
Aula 4 pede — sem antecipar réplica, consistência ou persistência, que pertencem à
Aula 5. É o mesmo raciocínio de "stub antes do real" que qualquer equipe usa para
testar resiliência sem esperar a outra equipe terminar.

## Como rodar

**Sem contêineres**, dois terminais:

```bash
make setup
make run-estoque    # terminal 1 — porta 8002
make run-pedidos    # terminal 2 — porta 8001
```

**Com contêineres** (requer Docker ou Podman instalado):

```bash
make up              # sobe os contêineres (Docker ou Podman)
```

Demonstração do disjuntor abrindo:

```bash
# cria um pedido
curl -s -X POST http://localhost:8001/pedidos -H "Content-Type: application/json" \
  -d '{"cliente_id":"3fa85f64-5717-4562-b3fc-2c963f66afa6","chave_idempotencia":"aula-4-demo","itens":[{"sku":"TECLADO-MEC-01","quantidade":1,"preco_unitario":349.90}]}'

# configura o estoque para falhar sempre
curl -s -X POST http://localhost:8002/_debug/config -d '{"falhar_percentual": 100, "atraso_ms": 0}'

# chame reservar-estoque repetidamente para o mesmo pedido — depois de algumas
# chamadas, o disjuntor abre e a resposta passa a ser imediata (sem esperar timeout)
curl -s -X POST http://localhost:8001/pedidos/<id>/reservar-estoque -w "\n%{http_code}\n"
```

## Roteiro de condução

1. Abra o ADR 0003 e explique a escolha de stack — inclusive o que foi descartado e
   por quê. Deixe claro que SQLite por serviço é uma escolha didática, registrada
   como tal.
2. Abra `resiliencia.py` e ligue cada trecho de código à sua contraparte no roteiro:
   `backoff_com_jitter` é a fórmula da Aula 2; `CircuitBreaker` é o exemplo numérico
   da Aula 4 (janela de 20, limite de 50%).
3. Rode `tests/test_resiliencia.py::test_disjuntor_abre_com_60_por_cento_de_falha_em_janela_de_20`
   isolado, depois `test_integracao_estoque.py::test_disjuntor_abre_de_verdade_apos_falhas_http_repetidas` —
   o segundo prova que o comportamento também vale de ponta a ponta, com dois
   processos reais trocando HTTP.
4. Se houver Docker ou Podman disponível, faça a demonstração ao vivo do bloco acima. Se não,
   rode os dois `make run-*` em terminais separados — o efeito é o mesmo.

## Pergunta que fica em aberto

O disjuntor protege `pedidos` de uma falha em `estoque`, mas o dado de estoque em si
ainda não existe de verdade — está tudo em memória, sem réplica, sem consistência
declarada. A Aula 5 substitui o dublê por um serviço com persistência real e introduz
o primeiro atraso de réplica do projeto.

## Estado do projeto

```
docs/
  adr/
    0003-stack-tecnologica.md              [novo]
    0004-resiliencia-timeout-retry-disjuntor.md   [novo]
services/
  pedidos/
    app/
      resiliencia.py                       [novo]
      main.py                              [alterado: POST /pedidos/{id}/reservar-estoque]
      store.py                             [alterado: atualizar_estado]
    tests/
      test_resiliencia.py                  [novo]
      test_integracao_estoque.py           [novo]
    Dockerfile                             [novo]
  estoque/                                 [novo — dublê controlável]
    app/main.py
    tests/test_estoque_stub.py
    Dockerfile
docker-compose.yml                          [novo]
Makefile                                    [alterado: setup/test para múltiplos serviços, up/down/logs]
```

30 testes (26 em pedidos, 4 em estoque), 2 serviços, 1º `make up` (compose) do projeto.
