# Aula 14 — Resiliência, testes distribuídos e engenharia do caos

**Videoaula correspondente:** Aula 14 — Resiliência, testes distribuídos e engenharia do caos.

## O que esta aula acrescentou ao projeto

- `services/pedidos/tests/contratos.py` + `test_contratos.py` — testes de contrato
  reais: `pedidos`, como consumidor, declara só os campos que seu próprio código lê
  de estoque/pagamento/expedição, e verifica isso contra a aplicação real de cada
  provedor — sem precisar da saga inteira em execução.
- `services/estoque/tests/test_desempenho.py` — um teste de carga real: 40
  requisições dentro da capacidade do balde de fichas (Aula 12), com asserção de
  taxa de erro e p95.
- Dois testes de duração (soak), reinterpretados para o que este projeto pode
  realmente provar sem rodar por horas: `test_disjuntor_janela_nao_cresce_sem_limite_sob_volume_sustentado`
  e `test_contador_com_dimensoes_de_baixa_cardinalidade_nao_cresce_sem_limite_sob_volume`
  — 5.000 operações cada, provando que duas estruturas internas (a janela do
  disjuntor, o contador de métricas) não crescem sem limite sob volume.
- **O experimento de caos** — `test_experimento_de_caos_indisponibilidade_total_do_pagamento`,
  em `services/pedidos/tests/test_saga_integracao.py`: injeta indisponibilidade total
  no provedor de pagamento (a alavanca da Aula 4/5), prova que todo pedido termina
  totalmente compensado, que o disjuntor abre e protege chamadas subsequentes em
  menos de 50 ms, e que um kill switch restaura o funcionamento completo.
- `scripts/disponibilidade_em_cadeia.py` — reproduz o exemplo numérico do roteiro:
  quatro serviços de 99,9% em cadeia compõem ~99,6%, quase quatro vezes mais
  indisponibilidade do que qualquer componente isolado.
- `docs/testes-e-caos.md` e `docs/adr/0014-testes-de-contrato-sem-broker.md`.

## O experimento de caos, com as cinco salvaguardas do roteiro

| Campo | Valor |
|---|---|
| Hipótese | Sob indisponibilidade total do pagamento, nenhum pedido fica inconsistente — todos são totalmente compensados, e o disjuntor abre |
| Perturbação | `falhar_percentual=100` em pagamento |
| Métricas de controle | `estado_final`/`compensacoes` de cada pedido; `GET /saude` |
| Raio de impacto | Ambiente de teste isolado |
| Critério de interrupção | Kill switch: `falhar_percentual` de volta a 0 |

Este experimento se desvia deliberadamente do número literal do roteiro
("conclusão ≥ 90%"): esse número presume um caminho de pagamento degradado que este
projeto não implementa. Sob falha total sem fallback, **0% de conclusão é o
resultado correto** — a hipótese que este projeto de fato sustenta, e que o
experimento confirma, é outra: nenhum pedido fica preso, e a proteção é rápida (não
só eventual). Ver `docs/testes-e-caos.md` para a justificativa completa — o próprio
tipo de resultado inesperado que o roteiro aponta como o valor de um experimento de
caos real.

## O experimento de caos encontrou um defeito de verdade

Rodado no cluster, com a perturbação vinda do orquestrador
(`kubectl scale deployment pagamento --replicas=0`) em vez de da alavanca interna
`falhar_percentual`, o experimento reprovou o sistema: três compras devolveram HTTP
500, o disjuntor não abriu e três reservas de estoque ficaram penduradas. A causa era
`httpx.TimeoutException` no lugar de `httpx.TransportError` — um provedor fora do ar
recusa a conexão, não dá timeout. Corrigido nesta aula, com
`test_experimento_de_caos_pagamento_fora_do_ar_tambem_compensa` como regressão e o
registro completo em `docs/kubernetes-execucao.md`.

É o experimento fazendo exatamente o que o roteiro promete: revelar o que a leitura do
código e 180 testes verdes não revelaram.

## Por que a composição degrada mais do que qualquer serviço isolado

```bash
cd scripts && .venv/bin/python3 -c \
  "from disponibilidade_em_cadeia import disponibilidade_em_cadeia as d; print(d([0.999]*4))"
# 0.996005996001
```

`pedidos → estoque, pagamento, expedição` é exatamente essa cadeia — a razão pela
qual disjuntor, compensação e processamento assíncrono não são refinamento opcional
neste projeto desde a Aula 4.

## Roteiro de condução

1. Rode `test_experimento_de_caos_indisponibilidade_total_do_pagamento` e narre as
   cinco fases: perturbação, taxa de conclusão observada, disjuntor aberto, proteção
   rápida (< 50 ms), kill switch, recuperação completa.
2. Rode `test_contratos.py` e depois `test_verificar_contrato_detecta_campo_removido`
   — mostre que o mecanismo pega uma quebra de verdade.
3. Rode os dois testes de soak e explique por que "5.000 chamadas" substitui "5 dias"
   neste ambiente — o que se testa é a estrutura, não o relógio.
4. Feche com `scripts/test_disponibilidade_em_cadeia.py` — o número que legitima
   por que a Unidade 1 já tratava resiliência como obrigatória.

## Como rodar

```bash
make setup
make test          # 181 testes: 85 pedidos, 49 estoque, 8 pagamento, 7 expedicao, 6 gateway, 26 scripts
make verificar      # fronteiras + instabilidade (Aula 9)
make validar-k8s    # os cinco manifests
make up             # contêineres (Docker ou Podman) com os cinco serviços de aplicação
make k8s-up         # cluster Kubernetes local (kind) com os manifests aplicados
make k8s-status     # pods, services e HPA do cluster
make k8s-down       # destrói o cluster
```

## Pergunta que fica em aberto

Testes e experimentos de caos validam comportamento sob falha, não sob volume
sustentado de dados nem sob a forma como esse volume chega — em lote, em fluxo
contínuo, na borda. Essa é a pergunta da Aula 15.

## Estado do projeto

```
docs/
  testes-e-caos.md                                      [novo]
  kubernetes-execucao.md                                [novo: o experimento em cluster]
  adr/0014-testes-de-contrato-sem-broker.md             [novo]
  adr/0011-manifests-validados-nao-aplicados.md         [alterado: os manifests foram aplicados]
services/pedidos/app/resiliencia.py                       [CORRIGIDO: httpx.TransportError, não TimeoutException]
services/pedidos/app/main.py                              [CORRIGIDO: idem, nas 5 etapas da saga]
k8s/kind/cluster.yaml + scripts/deploy_kind.sh             [novo: cluster kind de três nós]
services/pedidos/tests/contratos.py                       [novo]
services/pedidos/tests/test_contratos.py                  [novo: 5 testes]
services/estoque/tests/test_desempenho.py                 [novo: 1 teste de carga]
services/pedidos/tests/test_resiliencia.py                 [alterado: +1 teste soak]
services/pedidos/tests/test_observabilidade.py             [alterado: +1 teste soak]
services/pedidos/tests/test_saga_integracao.py             [alterado: +2 experimentos de caos]
scripts/disponibilidade_em_cadeia.py + test                 [novo: 4 testes]
```

181 testes, os três tipos de teste de desempenho nomeados corretamente, um
experimento de caos determinístico com hipótese, kill switch e recuperação provados.
