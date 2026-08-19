# Aula 12 — Segurança entre serviços

**Videoaula correspondente:** Aula 12 — Segurança em sistemas distribuídos.

## O que esta aula acrescentou ao projeto

- `services/*/app/seguranca.py` — em todos os cinco serviços: `emitir_token` /
  `verificar_token` (identidade assinada com HMAC-SHA256), a dependência FastAPI
  `exigir_identidade(identidades_permitidas)` (401 sem identidade válida, 403 com
  identidade válida mas não autorizada) e `BaldeDeFichas` (limitador de taxa por
  token bucket).
- `estoque`, `pagamento` e `expedicao` passam a exigir identidade `"pedidos"` em
  todas as rotas mutáveis (`POST`) — cada uma só aceita quem legitimamente deveria
  chamá-la.
- `pedidos` emite seu próprio token uma vez na inicialização e o anexa a todas as
  cinco chamadas que faz aos outros serviços (`_reservar_estoque`, `_liberar_estoque`,
  `_autorizar_pagamento`, `_estornar_pagamento`, `_solicitar_expedicao`).
- `estoque` ganha um limitador de taxa real (capacidade 50, reposição 20/s — os
  números do exemplo do roteiro) protegendo `POST /reservas`.
- `.env.example`, `docker-compose.yml` e `k8s/segredos.yaml` — o segredo de
  assinatura (`NEXAORDER_SEGREDO_ASSINATURA`) sempre vem de variável de ambiente,
  nunca hardcoded; `k8s/*.yaml` (exceto gateway) ganham `envFrom.secretRef`.
- `docs/seguranca.md` e `docs/adr/0012-identidade-por-token-hmac.md` — o que está
  implementado (HMAC) e por que não é mTLS de verdade.
- `services/pedidos/tests/test_saga_integracao.py` — um teste que reproduz
  literalmente o incidente da aula: uma compra completa, seguida de uma tentativa de
  `expedicao` estornar o pagamento dela, agora recusada com `403`.

## O incidente central, resolvido

Até a Aula 11, qualquer serviço podia chamar `POST /cobrancas/{id}/estornar` em
`pagamento` — nada verificava quem estava do outro lado da chamada. Isso é
exatamente o que `test_expedicao_nao_pode_solicitar_estorno_de_pagamento` prova
corrigido: uma compra real de ponta a ponta, seguida de uma tentativa de estorno
feita com o token de `expedicao` — recusada com `403` — e sem token nenhum —
recusada com `401`.

## Autenticação não é autorização

```bash
curl -X POST http://localhost:8003/cobrancas/ID/estornar                     # 401 — quem é você?
curl -X POST http://localhost:8003/cobrancas/ID/estornar -H "Authorization: Bearer expedicao.assinatura-forjada"  # 401 — assinatura não bate
curl -X POST http://localhost:8003/cobrancas/ID/estornar -H "Authorization: Bearer <token válido de expedicao>"    # 403 — você é expedicao, mas não pode fazer isto
curl -X POST http://localhost:8003/cobrancas/ID/estornar -H "Authorization: Bearer <token válido de pedidos>"      # 200 — autenticado e autorizado
```

`tests/test_seguranca.py` (em `services/estoque`) prova as quatro combinações
isoladamente.

## Roteiro de condução

1. Abra `services/estoque/app/seguranca.py` e mostre `emitir_token`/`verificar_token`
   — assinatura HMAC, não criptografia de canal; explique a diferença para mTLS.
2. Rode `test_expedicao_nao_pode_solicitar_estorno_de_pagamento` e mostre a saída:
   compra completa, depois `403` na tentativa de estorno indevido.
3. Rode `test_limitador_de_taxa_protege_reservas_de_verdade_via_http` — 90 chamadas
   reais por HTTP, ~50 aceitas, o resto recusado com `429`.
4. Feche com `docs/seguranca.md`, a tabela das quatro ameaças do roteiro e onde cada
   uma já era mitigada por mecanismos de aulas anteriores.

## Como rodar

```bash
cp .env.example .env   # e gere um segredo real (ver comentário no arquivo)
make setup
make test          # 129 testes: 61 pedidos, 48 estoque, 8 pagamento, 7 expedicao, 5 gateway, 10 scripts
make verificar      # fronteiras + instabilidade (Aula 9)
make validar-k8s    # os cinco manifests, agora com envFrom.secretRef
make up             # docker compose injeta NEXAORDER_SEGREDO_ASSINATURA nos serviços
```

## Pergunta que fica em aberto

Identidade e autorização resolvem quem pode chamar quem — mas não dizem nada sobre
o que está acontecendo *dentro* de uma cadeia de chamadas em produção: quanto tempo
cada etapa levou, onde uma requisição lenta realmente gastou tempo, o que aconteceu
nos serviços entre o pedido do cliente e a resposta. Essa é a pergunta da Aula 13.

## Estado do projeto

```
docs/
  seguranca.md                                          [novo]
  adr/0012-identidade-por-token-hmac.md                 [novo]
services/*/app/seguranca.py                              [novo, idêntico em cada serviço]
services/{estoque,pagamento,expedicao}/app/main.py        [alterado: Depends(exigir_identidade(...)) nas rotas mutáveis]
services/estoque/app/main.py                              [alterado: BaldeDeFichas em POST /reservas]
services/pedidos/app/main.py                              [alterado: emite e anexa token a todas as chamadas de saída]
services/{estoque,pagamento,expedicao}/tests/conftest.py  [alterado: cliente_api autentica como "pedidos" por padrão]
services/estoque/tests/test_seguranca.py                  [novo: 10 testes]
services/pedidos/tests/test_saga_integracao.py            [alterado: +1 teste do incidente central]
.env.example                                              [novo]
docker-compose.yml                                        [alterado: injeta NEXAORDER_SEGREDO_ASSINATURA]
k8s/segredos.yaml                                         [novo: Secret ilustrativo]
k8s/{estoque,pagamento,expedicao,pedidos}.yaml             [alterado: envFrom.secretRef]
```

129 testes, identidade verificável e autorização por menor privilégio em três
serviços, limitador de taxa protegendo a rota mais sensível a rajada.
