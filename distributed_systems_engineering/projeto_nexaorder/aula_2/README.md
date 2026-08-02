# Aula 2 — Arquitetura em Mermaid e contratos

**Videoaula correspondente:** Aula 2 — Comunicação entre processos: APIs, RPC e mensageria.

## O que esta aula acrescentou ao projeto

Tudo o que existia na Aula 1, mais:

- `docs/arquitetura.md` — o primeiro diagrama de componentes e o primeiro diagrama de
  sequência do sistema, ambos em Mermaid, renderizáveis direto no GitHub ou em
  qualquer visualizador Mermaid.
- `docs/adr/0002-comunicacao-sincrona-inicial.md` — por que o projeto começa
  deliberadamente síncrono, sabendo do custo, e qual evidência dispara a migração para
  eventos na Aula 10.
- `docs/contratos/api-pedidos.md` — o contrato REST de `pedidos`, escrito antes do
  código.
- `docs/contratos/eventos.md` — os quatro eventos de domínio (`PedidoCriado`,
  `EstoqueReservado`, `PagamentoAprovado`, `PedidoExpedido`), definidos antes de
  existir qualquer broker.

## Roteiro de condução

1. Abra `docs/arquitetura.md` e renderize o diagrama de componentes. Note as caixas
   tracejadas — elas ainda não são código. Pergunte à turma: por que desenhar antes de
   implementar?
2. Renderize o diagrama de sequência e refaça no quadro a conta da Aula 2:
   `0,999⁴ ≈ 0,996`. Conecte com o diagrama: cada seta síncrona é um fator dessa
   multiplicação.
3. Abra o contrato de API e o de eventos lado a lado. Mostre que o tempo verbal muda —
   `POST /pedidos` é imperativo (comando), `PedidoCriado` é particípio passado
   (evento) — e que essa diferença gramatical carrega uma diferença arquitetural.
4. Feche com o ADR 0002: a decisão de começar síncrono é deliberada, não ingenuidade.

## Pergunta que fica em aberto

O contrato existe no papel. Nada roda ainda. A Aula 3 escreve o primeiro código —
e com ele, a primeira vez em que dois eventos de processos diferentes precisam ser
ordenados.

## Estado do projeto

```
docs/
  modelo-dominio.md
  dimensionamento.md
  arquitetura.md              [novo]
  contratos/                  [novo]
    api-pedidos.md
    eventos.md
  adr/
    0001-por-que-distribuir.md
    0002-comunicacao-sincrona-inicial.md   [novo]
```

Ainda sem código, sem dependências, sem execução.
