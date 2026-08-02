# Contêineres e Kubernetes — Unidade 3, Aula 11

## O que está implementado, e o que é simplificação

Os cinco manifests em `k8s/` (`Deployment` + `Service` por serviço, mais um `HPA`
para `pedidos`) são YAML real, validado estruturalmente por
`scripts/validar_manifests_k8s.py` — não são apenas ilustrativos. O que não é
possível neste ambiente: aplicá-los a um cluster real (`kubectl apply`), porque não
há Docker nem Kubernetes disponíveis aqui (a mesma limitação registrada desde o
ADR 0003, agora estendida a `kind`/`minikube`). A validação, portanto, é estrutural
— sintaxe, campos obrigatórios, referências cruzadas corretas — não comportamental.

## As cinco peças que Kubernetes automatiza

| Objeto | Cuida de | Onde aparece nos manifests |
|--------|----------|------------------------------|
| Cluster | conjunto de máquinas gerenciadas como unidade | fora do escopo deste repositório |
| Nó | máquina que executa contêineres | idem |
| Pod | menor unidade implantável | `spec.template` de cada Deployment |
| Deployment | quantas réplicas, qual versão, como atualizar | `k8s/*.yaml`, campo `spec.replicas` e `spec.strategy` |
| Service | endereço estável para os Pods | bloco `kind: Service` em cada arquivo |

## Estado desejado, estado observado, laço de reconciliação

Um `Deployment` com `replicas: 2` é uma declaração de intenção, não uma sequência de
comandos. Se um Pod cai, o controlador do Kubernetes observa a divergência entre
desejado (2) e observado (1), e cria outro — sem que ninguém precise agir. Este
projeto não tem como demonstrar esse laço em execução (exigiria um cluster real),
mas o comportamento é o mesmo mecanismo provado, em outro domínio, por
`services/pedidos/app/consenso.py` (Aula 7): um controlador comparando estado
desejado e observado, continuamente.

## Duas sondas, dois papéis

Implementadas em todos os cinco serviços (`services/*/app/main.py`):

- **`GET /saude` — vivacidade.** Falhar aqui faz o kubelet reiniciar o contêiner. Só
  falha se o processo travou.
- **`GET /pronto` — prontidão.** Falhar aqui só tira o Pod dos destinos do Service —
  sem reiniciar. Verifica uma dependência real: acesso ao banco (nos quatro serviços
  com persistência) ou alcançabilidade de `pedidos` (no gateway, que não tem banco
  próprio — ver Aula 9, ADR 0009).

A distinção importa porque as duas falhas pedem reações diferentes: um processo
travado precisa reiniciar; um banco temporariamente inacessível não — reiniciar não
resolveria nada, e tirar o Pod do tráfego até o banco voltar é a resposta correta.

## Escalonamento automático: o exemplo do roteiro, nos números do manifesto

`k8s/pedidos.yaml` declara `replicas: 4` e um HPA com `averageUtilization: 60`. São
exatamente os números do exemplo da Aula 11: com 4 réplicas atuais observando 85% de
CPU contra um alvo de 60%,

```
N = ⌈ replicas_atuais × utilização_observada / utilização_alvo ⌉
N = ⌈ 4 × 85 / 60 ⌉ = ⌈ 5,67 ⌉ = 6
```

O HPA ajustaria `pedidos` para 6 réplicas. Este cálculo não roda de fato neste
projeto (exigiria metrics-server em um cluster real observando CPU real) — está
documentado aqui como a mesma conta da Aula 11, aplicada ao serviço mais instável do
projeto (Aula 9: `pedidos` tem I=0,75, o candidato natural a escalar sob carga).

## Atualização gradual

`spec.strategy.rollingUpdate` em cada Deployment declara `maxUnavailable: 1` e
`maxSurge: 1`. Para `pedidos` (4 réplicas), isso significa que a capacidade saudável
durante uma atualização nunca cai abaixo de 3 nem ultrapassa 5 — a mesma lógica do
exemplo de 6 réplicas do roteiro (capacidade entre 5 e 7), escalada para o tamanho
real deste Deployment.

## Decisão registrada

Ver `docs/adr/0011-manifests-validados-nao-aplicados.md`.
