# Segurança entre serviços — Unidade 3, Aula 12

## O incidente que esta aula corrige

Até a Aula 11, nada impedia `expedicao` de chamar `POST /cobrancas/{id}/estornar` em
`pagamento` e solicitar um reembolso que nunca autorizou pedir — exatamente a
situação-problema do roteiro. `tests/test_saga_integracao.py::test_expedicao_nao_pode_solicitar_estorno_de_pagamento`
(em `services/pedidos`) reproduz esse cenário literalmente — uma compra real,
completa, seguida de uma tentativa de estorno por uma identidade sem permissão — e
prova que agora ela é recusada com `403`.

## O que está implementado, e o que é simplificação

Implementado e testado, em todos os cinco serviços:

- **Identidade verificável**: `services/*/app/seguranca.py` — `emitir_token` e
  `verificar_token`, com assinatura HMAC-SHA256. Cada serviço que chama outro
  apresenta um token identificando-se; quem recebe verifica a assinatura antes de
  aceitar a identidade alegada.
- **Autorização por menor privilégio**: `exigir_identidade({"pedidos"})` como
  dependência FastAPI nas rotas mutáveis de `estoque`, `pagamento` e `expedicao`.
  Cada uma aceita apenas a identidade que legitimamente deveria chamá-la.
- **Limitador de taxa por balde de fichas**: `BaldeDeFichas`, com os mesmos números
  do exemplo do roteiro (capacidade 50, reposição 20/s), protegendo `POST /reservas`
  em `estoque`.

**Simplificação deliberada**: o mecanismo de identidade aqui é um token HMAC, não TLS
mútuo. Não há certificado, não há autoridade certificadora, não há canal
criptografado — o princípio demonstrado é o mesmo do roteiro (identidade que viaja
com o chamador, não com o endereço de rede), mas a implementação de produção real
exigiria PKI, o que este ambiente de desenvolvimento não tem infraestrutura para
demonstrar (mesma classe de limite dos ADRs 0003, 0007 e 0011).

## Autenticação e autorização são perguntas diferentes

`tests/test_seguranca.py` prova as duas separadamente:

- **401** — identidade ausente ou token com assinatura inválida (a pergunta "quem é
  você" não pôde ser respondida).
- **403** — identidade válida, mas não autorizada para esta operação específica (a
  pergunta "quem é você" foi respondida; a resposta é "alguém sem permissão para
  isto").

Um serviço com certificado válido — ou, aqui, token válido — ainda pode não ter
autorização para uma operação específica. É exatamente o ponto do roteiro sobre
autenticação sem autorização.

## Balde de fichas: proteção, não punição

`tests/test_seguranca.py::test_limitador_de_taxa_protege_reservas_de_verdade_via_http`
prova, batendo na rota HTTP real, que uma rajada de 90 chamadas a `/reservas` é
majoritariamente absorvida pela capacidade (50) e o excedente recusado com `429` —
não para punir quem fez a rajada, mas para proteger o serviço de uma sobrecarga que
comprometeria a disponibilidade para todos os outros chamadores.

## As quatro ameaças do roteiro, e onde este projeto já mitiga cada uma

| Ameaça | Mitigação já presente no projeto |
|--------|-------------------------------------|
| Repetição (replay) | Chave de idempotência (Aula 8) — reenviar a mesma operação não duplica o efeito |
| Movimento lateral | Identidade + autorização por menor privilégio (esta aula) |
| Amplificação por retry | Backoff com jitter e disjuntor (Aula 4) |
| Exposição de segredos | `.env.example` versionado sem o valor real; `NEXAORDER_SEGREDO_ASSINATURA` sempre lido de variável de ambiente, nunca hardcoded (ver `k8s/segredos.yaml`) |

Nenhuma dessas mitigações foi inventada nesta aula — o padrão do roteiro se confirma:
segurança, aqui, reinterpreta sob ótica adversarial mecanismos que o projeto já
tinha por outras razões.

## Decisão registrada

Ver `docs/adr/0012-identidade-por-token-hmac.md`.
