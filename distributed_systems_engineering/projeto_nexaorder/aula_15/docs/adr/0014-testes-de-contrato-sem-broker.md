# ADR 0014 — Testes de contrato por verificação direta, sem broker (Pact)

- **Status:** aceito
- **Data:** correspondente à Unidade 4, Aula 14

## Contexto

A Aula 14 descreve testes de contrato no formato consumidor-orientado: o consumidor
declara expectativas, publica em um repositório compartilhado, e o pipeline de
integração contínua do provedor as verifica antes de qualquer implantação — sem que
consumidor e provedor precisem estar em execução simultânea (o modelo do Pact e
ferramentas equivalentes). Integrar um broker de contratos real exigiria um serviço
adicional, publicação/consulta via rede, e dois pipelines de CI distintos (consumidor
publicando, provedor verificando) — infraestrutura de CI que este ambiente de
desenvolvimento não tem (mesma classe de limite dos ADRs anteriores sobre
infraestrutura indisponível neste sandbox).

## Decisão

`pedidos`, como consumidor, declara contratos como dados simples em
`services/pedidos/tests/contratos.py` (só os campos que seu próprio código lê — ver
`app/saga.py`) e `verificar_contrato` os checa contra a aplicação real de cada
provedor, carregada em processo via o mesmo mecanismo de carregamento dinâmico já
usado por `test_saga_integracao.py` desde a Aula 4.

## Por quê

O valor central de um teste de contrato, segundo o roteiro, é detectar uma mudança
silenciosa de formato **antes** de um teste de ponta a ponta caro (ou pior, de
produção). Isso é obtido aqui sem broker: `test_contratos.py` roda em milissegundos,
sobe só o provedor sob teste (não os quatro serviços da saga), e falha exatamente
quando um campo declarado desaparece — `test_verificar_contrato_detecta_campo_removido`
prova que o mecanismo não é decorativo.

## Compromisso aceito

O que não é reproduzido: publicação assíncrona de contratos, verificação do provedor
sem o consumidor em execução, e o próprio pipeline de CI de duas pontas que o roteiro
descreve. Neste projeto, consumidor (o teste) e provedor (a aplicação real) rodam no
mesmo processo de teste — mais parecido com um teste de schema de resposta do que com
Pact em sua forma completa. A interface (`verificar_contrato`, os dicionários de
contrato) foi desenhada para que migrar para um broker real seja uma troca de
mecanismo de publicação/execução, não uma reescrita do que já está declarado.

## Evidência

`services/pedidos/tests/test_contratos.py` (5 testes) prova os três contratos
cumpridos pelas aplicações reais de estoque, pagamento e expedição, e prova que o
verificador detecta tanto um campo removido quanto tolera campos novos — a assimetria
correta de um contrato orientado a consumidor.
