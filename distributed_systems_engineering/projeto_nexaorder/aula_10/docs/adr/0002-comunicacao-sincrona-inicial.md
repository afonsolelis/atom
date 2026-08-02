# ADR 0002 — Começar com comunicação síncrona, migrar depois

- **Status:** aceito
- **Data:** correspondente à Unidade 1, Aula 2

## Contexto

A Aula 2 apresenta o par síncrono/assíncrono e mostra, com números, que o encadeamento
síncrono multiplica indisponibilidade: quatro serviços com 99,9% cada, encadeados,
entregam 99,6% ao fluxo — quase três vezes mais indisponibilidade que qualquer um
isoladamente.

Ainda assim, o projeto começa síncrono.

## Decisão

Implementar o caminho feliz de `pedidos → estoque → pagamento → expedição` como
chamadas HTTP síncronas até a Aula 8 (sagas) e migrar para eventos na Aula 10.

## Por quê

Duas razões, e nenhuma delas é "porque é mais simples de programar":

1. **Pedagógica** — o curso precisa que o aluno sinta o problema do acoplamento
   temporal antes de receber a solução. Pular direto para eventos removeria a
   motivação da Aula 8 (sagas) e da Aula 10 (arquitetura orientada a eventos).
2. **Arquitetural** — dividir trabalho (fila) e difundir informação (eventos) exige que
   os contratos de mensagem já estejam estáveis. Esses contratos são definidos nesta
   mesma aula (`docs/contratos/eventos.md`) exatamente para que a migração da Aula 10
   seja uma troca de transporte, não uma reescrita de modelo.

## Compromisso aceito

Entre a Aula 3 e a Aula 8, o sistema herda exatamente o problema que a Aula 2
descreveu: uma falha ou lentidão em pagamento propaga-se para pedidos, e uma falha em
expedição pode travar uma compra já paga. Isso é proposital — a Aula 4 introduz
timeout, retry e circuit breaker como primeira linha de defesa, e a Aula 8 remove o
problema pela raiz com sagas.

## Evidência de que a migração deve ocorrer

A migração da Aula 10 é justificada pela mesma conta desta ADR: a disponibilidade
combinada do fluxo síncrono, medida em teste de carga (Aula 14), deve ficar
mensuravelmente abaixo da disponibilidade de cada serviço isolado. Se a medição não
confirmar isso, a decisão de migrar precisa ser revista — não é dogma, é hipótese.
