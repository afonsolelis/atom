# ADR 0011 — Manifests Kubernetes validados estruturalmente, não aplicados

- **Status:** aceito
- **Data:** correspondente à Unidade 3, Aula 11

## Contexto

Este ambiente de desenvolvimento não tem Docker nem Kubernetes disponíveis (mesma
restrição do ADR 0003, que já impedia validar o `docker-compose.yml` por execução).
A Aula 11 pede Deployment, Service, sondas e HPA — objetos cujo comportamento real só
se observa com um cluster de verdade.

## Decisão

Escrever os cinco manifests (`k8s/*.yaml`) como YAML correto e completo, e validá-los
estruturalmente com `scripts/validar_manifests_k8s.py`, em vez de simular
comportamento de cluster que não pode ser executado aqui.

## Por quê

A alternativa de não escrever os manifests deixaria a aula sem nenhum artefato
concreto. A alternativa de fingir uma execução (por exemplo, um "cluster falso" em
Python simulando o kubelet) inflaria a complexidade do projeto sem ensinar Kubernetes
de verdade — o valor de Kubernetes está exatamente nas garantias que a ferramenta
real oferece, não em uma reimplementação didática dela.

## Compromisso aceito

Ninguém rodou `kubectl apply` contra estes manifests neste projeto. Erros que só
apareceriam em um cluster real — por exemplo, uma referência de imagem inexistente
no registro, ou uma quantidade de recurso que o nó não consegue alocar — não são
detectados pela validação estrutural. Isso é aceito e documentado: a validação prova
que o YAML está bem formado e internamente consistente, não que o cluster aceitaria
aplicá-lo.

## Evidência

`scripts/validar_manifests_k8s.py` roda contra os cinco manifests reais e passa.
`scripts/test_validar_manifests_k8s.py` prova que o validador detecta cada uma das
quatro classes de violação que ele afirma verificar, com casos negativos construídos
deliberadamente.
