# Aula 11 — Contêineres e Kubernetes

**Videoaula correspondente:** Aula 11 — Contêineres, Kubernetes e reconciliação.

## O que esta aula acrescentou ao projeto

- `GET /pronto` em todos os cinco serviços — sonda de **prontidão**, distinta de
  `GET /saude` (vivacidade, existente desde a Aula 4/8). Nos quatro serviços com
  banco, verifica acesso real ao SQLite; no gateway, verifica se `pedidos` está
  alcançável — a única dependência que realmente importa para ele funcionar.
- `k8s/` — cinco manifests (`Deployment` + `Service` por serviço, mais um `HPA` para
  `pedidos`), com sondas, `resources.requests`/`limits` e `rollingUpdate` declarados.
- `scripts/validar_manifests_k8s.py` — um linter estrutural real para os manifests,
  no mesmo espírito de `verificar_fronteiras.py` (Aula 9). Roda contra os cinco
  manifests do projeto e passa.
- `docs/kubernetes.md` e `docs/adr/0011-manifests-validados-nao-aplicados.md` — o que
  está implementado e validado, e por que não há um cluster real aplicando isso.

## Por que vivacidade e prontidão fazem coisas diferentes

```bash
curl http://localhost:8002/saude    # -> sempre 200 se o processo responde
curl http://localhost:8002/pronto   # -> 200 se o banco está acessível, 503 se não
```

Um processo travado precisa reiniciar — é isso que a vivacidade aciona. Um banco
temporariamente inacessível não se resolve reiniciando o processo; a resposta certa é
tirar o Pod do tráfego até o banco voltar — é isso que a prontidão faz, sem reiniciar
nada. `tests/test_sondas.py` (em cada serviço) prova as duas rotas separadamente.

## O experimento central: validar os próprios manifests

```bash
python3 scripts/validar_manifests_k8s.py
```

```
✓ Sondas de vivacidade e prontidão: nenhuma violação
✓ Requests e limits de recursos: nenhuma violação
✓ Services apontam para Deployment existente: nenhuma violação
✓ HPA aponta para Deployment existente: nenhuma violação
```

## Roteiro de condução

1. Abra `k8s/pedidos.yaml` e mostre o comentário no topo: os números do HPA (4
   réplicas, 60% de alvo) são os mesmos do exemplo do roteiro. Refaça a conta no
   quadro: `⌈4 × 85/60⌉ = 6`.
2. Rode `scripts/test_validar_manifests_k8s.py` e mostre um teste que quebra um
   manifest de propósito (`test_deployment_sem_readiness_probe_e_detectado`) — prove
   que o validador não é decorativo.
3. Compare `k8s/gateway.yaml` com `k8s/estoque.yaml`: o gateway não tem
   `volumeMounts` nem variável de banco — a mesma ausência de estado da Aula 9,
   agora visível também no manifesto de implantação.
4. Feche com o ADR 0011: por que este projeto documenta o limite (sem Docker/K8s
   disponíveis aqui) em vez de fingir uma execução que não aconteceu.

## Como rodar

```bash
make setup
make test          # 128 testes: 60 pedidos, 38 estoque, 8 pagamento, 7 expedicao, 5 gateway, 10 scripts
make verificar      # fronteiras + instabilidade (Aula 9)
make validar-k8s    # os cinco manifests
make up             # contêineres (Docker ou Podman) com os cinco serviços de aplicação
make k8s-up         # cluster Kubernetes local (kind) com os cinco manifests aplicados
make k8s-status     # pods, services e HPA do cluster
make k8s-down       # destrói o cluster
```

Os manifests deixaram de ser só validados: `docs/kubernetes-execucao.md` registra a
execução real em um cluster kind de três nós — incluindo os três problemas que só
aparecem no cluster e que a validação estrutural não pegava.

## Pergunta que fica em aberto

Mesmo com sondas e manifests corretos, qualquer serviço ainda aceita chamada de
qualquer outro, sem verificar identidade — o incidente que abre a Aula 12: nada
impede `expedicao` de chamar `pagamento` e solicitar um estorno que nunca foi
autorizado a pedir.

## Estado do projeto

```
docs/
  kubernetes.md                                    [novo]
  adr/0011-manifests-validados-nao-aplicados.md     [novo]
k8s/                                                 [novo diretório]
  estoque.yaml, pagamento.yaml, expedicao.yaml
  pedidos.yaml (com HPA)
  gateway.yaml
scripts/
  requirements.txt                                  [novo: pyyaml, pytest]
  validar_manifests_k8s.py                          [novo]
  test_validar_manifests_k8s.py                     [novo]
services/*/app/main.py                               [alterado: GET /pronto]
services/*/app/store.py                              [alterado: verificar_conexao]
services/*/tests/test_sondas.py                       [novo]
Makefile                                              [alterado: setup/test cobrem scripts/, alvo validar-k8s]
```

128 testes, 5 serviços com duas sondas cada, 5 manifests Kubernetes validados
estruturalmente.
