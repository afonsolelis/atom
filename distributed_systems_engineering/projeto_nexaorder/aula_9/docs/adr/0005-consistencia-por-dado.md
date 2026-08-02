# ADR 0005 — Consistência por dado, não por serviço

- **Status:** aceito
- **Data:** correspondente à Unidade 2, Aula 5

## Contexto

O serviço `estoque` guarda dois tipos de informação com riscos completamente
diferentes: o saldo exibido ao navegar (informativo) e o saldo verificado no momento
de reservar (decisório). Aplicar a mesma política de consistência aos dois obrigaria
a escolher entre pagar o custo de consistência forte também na navegação, ou aceitar
o risco de consistência eventual também na reserva.

## Decisão

O saldo é lido de duas fontes diferentes dependendo do propósito da leitura:
- leitura informativa → réplica (eventual, mais barata, pode atrasar até 150 ms);
- decisão de reservar → líder (forte, sempre atual, mais cara).

A escrita é sempre única, no líder — não existe "escrita eventual" neste projeto.

## Compromisso aceito

A rota `GET /saldo/{sku}?consistencia=eventual` pode devolver um valor que já mudou
no líder. Isso é aceito deliberadamente para esse caso de uso. A rota equivalente com
`consistencia=forte` sempre bate no líder, e portanto não escala tão bem quanto a
eventual sob alta concorrência de leitura — um compromisso que a Aula 6 (particionamento)
volta a discutir quando o volume de leitura crescer além do que uma única réplica
comporta.

## Evidência

`tests/test_replica.py` prova a janela de atraso com um cronômetro real.
`tests/test_saldo_e_reservas.py` prova que a reserva nunca decrementa abaixo de zero,
mesmo quando duas reservas concorrentes disputam a mesma unidade — a garantia que só
a leitura forte contra o líder pode sustentar.
