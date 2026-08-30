# Aula 16 — Projeto integrado e avaliação arquitetural

**Videoaula correspondente:** Aula 16 — Projeto integrado e avaliação arquitetural (encerramento da disciplina).

## O que esta aula acrescentou ao projeto

Esta aula é estruturalmente diferente das quinze anteriores: o próprio roteiro abre
dizendo que ela "não apresenta um mecanismo novo — consiste em sustentar
tecnicamente tudo o que foi estudado". Por isso, o código novo é deliberadamente
pequeno, e o trabalho principal é documental (ver ADR 0016 para essa decisão):

- **`docs/defesa-arquitetural.md`** — o documento central: as tensões entre
  requisitos funcionais e atributos de qualidade resolvidas por dado, a
  retrospectiva das 15 ADRs por unidade com seus compromissos aceitos, uma análise
  honesta de pontos únicos de falha (incluindo os que este projeto AINDA não
  mitiga), RPO/RTO derivados do requisito de negócio, e a trajetória completa das
  quatro unidades.
- **`scripts/verificar_criterios_de_aceite.py`** — converte "todo serviço nasce com
  identidade e instrumentação" de princípio em prosa para gate executável, no mesmo
  espírito de `verificar_fronteiras.py` (Aula 9). Roda contra os cinco serviços reais
  e passa.
- **`scripts/disponibilidade_em_cadeia.py`** ganha `disponibilidade_redundancia_paralela`
  — o contraste numérico final: cadeia sequencial piora, redundância paralela
  independente melhora — sete noves a partir de três réplicas de 99,5%.
- **`scripts/dimensionamento_com_evidencias.py`** + `services/pedidos/tests/test_dimensionamento_com_evidencias.py`
  — recalcula o `N = 6` da Aula 1 com um insumo medido ao vivo nesta própria suíte,
  não suposto.
- **`docs/adr/0016-defesa-arquitetural-nao-introduz-mecanismo-novo.md`**.

## A análise de SPOF, sem embelezamento

`docs/defesa-arquitetural.md` não lista só riscos já mitigados. Registra, com a
mesma honestidade de todas as ADRs anteriores, o que este projeto **ainda não tem**:
nenhuma réplica de banco, um barramento de eventos que não sobrevive a um reinício,
um segredo de identidade compartilhado por HMAC, nenhum RPO/RTO implementado. Uma
defesa arquitetural madura nomeia esses limites como próximos passos — não os
esconde para parecer mais completa.

## A unidade inteira rodou em um cluster de verdade

`docs/kubernetes-execucao.md` consolida o que as quatro aulas desta unidade
encontraram ao aplicar os manifests em um cluster kind de três nós — incluindo um
defeito de correção que 180 testes verdes não pegavam (a Aula 14 o encontrou e
corrigiu). A seção 4 de `docs/defesa-arquitetural.md` deixou de ser previsão e passou
a citar medição.

## O mesmo cálculo, insumo que deixou de ser suposição

`docs/dimensionamento.md` (Aula 1) previa 6 instâncias a partir de três suposições.
`test_capacidade_medida_ao_vivo_recalcula_o_numero_de_instancias_da_aula_1` bate em
`POST /pedidos` de verdade, mede quantas requisições por segundo esta suíte
realmente sustenta, e alimenta a mesma fórmula com esse número — fechando um arco
aberto desde a primeira aula do projeto.

## Roteiro de condução

1. Abra `docs/defesa-arquitetural.md` e leia a seção 4 (SPOF) em voz alta — é o
   ponto mais honesto do documento.
2. Rode `make criterios-de-aceite` e mostre os cinco serviços aprovados.
3. Rode `scripts/test_disponibilidade_em_cadeia.py::test_redundancia_paralela_e_estruturalmente_oposta_a_cadeia_sequencial`
   — os mesmos três componentes, leitura oposta conforme a topologia.
4. Feche revisitando `docs/dimensionamento.md` ao lado do novo teste de capacidade
   medida — o mesmo número da Aula 1, agora com procedência diferente.

## Como rodar

```bash
make setup
make test                # 217 testes: 109 pedidos, 49 estoque, 8 pagamento, 7 expedicao, 6 gateway, 38 scripts
make verificar            # fronteiras + instabilidade (Aula 9)
make validar-k8s          # os cinco manifests (Aula 11)
make criterios-de-aceite  # identidade + observabilidade + testes, por serviço (Aula 16)
make up                   # contêineres (Docker ou Podman) com os cinco serviços de aplicação
make k8s-up               # cluster Kubernetes local (kind) com os manifests aplicados
make k8s-status           # pods, services e HPA do cluster
make k8s-down             # destrói o cluster
```

## A trajetória completa

Dezesseis pastas, cada uma o projeto inteiro até aquele ponto — não um diff, uma
aplicação completa e executável. `aula_1` modela o domínio; `aula_16` roda cinco
serviços com identidade, observabilidade, resiliência testada sob caos real, e um
pipeline de fluxo, com 217 testes verdes e uma defesa arquitetural honesta sobre o
que ainda falta para produção. É essa combinação — fundamentos, dados, serviços e
operação — que a Aula 16 argumenta ser o que sustenta um sistema real, e é essa
combinação que este projeto constrói, aula a aula, para ser mostrada, não só
descrita.

## Estado do projeto

```
docs/
  defesa-arquitetural.md                                              [novo]
  kubernetes-execucao.md                                              [novo: a unidade em cluster]
  adr/0016-defesa-arquitetural-nao-introduz-mecanismo-novo.md         [novo]
  adr/0011-manifests-validados-nao-aplicados.md                       [alterado: os manifests foram aplicados]
k8s/kind/cluster.yaml + scripts/deploy_kind.sh                         [novo: cluster kind de três nós]
scripts/disponibilidade_em_cadeia.py                                    [alterado: +disponibilidade_redundancia_paralela]
scripts/dimensionamento_com_evidencias.py + test                        [novo: 2 testes]
scripts/verificar_criterios_de_aceite.py + test                         [novo: 3 testes]
services/pedidos/tests/test_dimensionamento_com_evidencias.py           [novo: 1 teste]
Makefile                                                                  [alterado: alvo criterios-de-aceite]
```

217 testes, 16 ADRs, uma análise de pontos únicos de falha sem embelezamento, e o
argumento completo — requisitos, riscos, custo e evidências — que fecha a
disciplina.
