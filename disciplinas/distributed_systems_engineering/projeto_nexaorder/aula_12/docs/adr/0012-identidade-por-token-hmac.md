# ADR 0012 — Identidade entre serviços por token HMAC, não TLS mútuo

- **Status:** aceito
- **Data:** correspondente à Unidade 3, Aula 12

## Contexto

A Aula 12 pede identidade verificável entre serviços — no roteiro, via TLS mútuo
(mTLS), tipicamente distribuído por um service mesh. Implementar mTLS de verdade
exige uma autoridade certificadora, rotação de certificados e, normalmente, um proxy
lateral por Pod — infraestrutura que este projeto não tem como demonstrar sem um
cluster real (mesma classe de limite do ADR 0011).

## Decisão

Implementar identidade por token assinado com HMAC-SHA256, compartilhando um segredo
simétrico entre os serviços (`NEXAORDER_SEGREDO_ASSINATURA`), com uma dependência
FastAPI (`exigir_identidade`) que autentica e autoriza por rota.

## Por quê

O princípio que a aula pede — identidade que viaja com o chamador, não com o
endereço de rede — é inteiramente demonstrável com HMAC, sem exigir PKI. O incidente
central da aula (`expedicao` conseguindo pedir um estorno em `pagamento`) é
igualmente corrigido por essa abordagem mais simples, com os mesmos códigos HTTP
(`401`/`403`) que uma implementação com mTLS produziria.

## Compromisso aceito

HMAC com segredo compartilhado tem uma fraqueza que mTLS não tem: qualquer serviço
que conhece o segredo pode forjar a identidade de qualquer outro. Em produção real,
isso seria inaceitável — é exatamente por isso que mTLS usa um par de chaves
assimétrico por serviço, não um segredo único compartilhado. Este projeto aceita essa
fraqueza conscientemente, documentada aqui, em troca de não precisar de
infraestrutura de PKI para provar o princípio em teste.

## Evidência

`tests/test_seguranca.py` prova emissão, verificação, rejeição de token forjado e a
distinção 401/403. `tests/test_saga_integracao.py::test_expedicao_nao_pode_solicitar_estorno_de_pagamento`
prova que o incidente da situação-problema da Aula 12 está corrigido, com uma compra
real de ponta a ponta seguida da tentativa de ataque.
