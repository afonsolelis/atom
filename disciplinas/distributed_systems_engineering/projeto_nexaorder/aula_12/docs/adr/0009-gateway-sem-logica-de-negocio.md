# ADR 0009 — Gateway sem lógica de negócio nem banco próprio

- **Status:** aceito
- **Data:** correspondente à Unidade 3, Aula 9

## Contexto

O cliente externo da NexaOrder precisaria, sem um gateway, conhecer os quatro
serviços internos e suas quatro URLs para montar uma única tela de detalhes de
pedido. Isso acopla o consumidor externo à decomposição interna do sistema.

## Decisão

Introduzir `services/gateway`, com uma única rota de composição
(`GET /pedidos/{id}/resumo`), sem banco de dados próprio e sem regra de negócio.

## Por quê

O roteiro é explícito sobre o risco: "quando isso acontece, o gateway vira um novo
monólito escondido atrás de uma fachada de microsserviços". Manter o gateway
burro — sem estado, sem decisão — é o que impede esse desfecho. Qualquer regra sobre
o que um pedido "pode" fazer a seguir continua vivendo exclusivamente na saga de
`pedidos`.

## Compromisso aceito

O gateway introduz um ponto adicional de latência (até quatro chamadas de rede em
paralelo) e um novo componente que precisa estar no ar para a experiência composta
funcionar plenamente — embora as consultas auxiliares sejam best-effort, a consulta
ao pedido em si continua sendo uma dependência obrigatória. Isso é aceito porque o
ganho — desacoplar o cliente da topologia interna — supera o custo de mais um serviço
simples e sem estado para operar.

## Evidência

`tests/test_gateway.py` prova a composição com HTTP real entre as quatro
aplicações, incluindo o caso em que reservas, cobranças e remessas ainda não existem
(pedido recém-criado) e o caso de pedido inexistente.
