# Execução real dos manifests em um cluster local (kind) — Aula 14

O ADR 0011 (Aula 11) registrou que os manifests tinham sido validados
estruturalmente, mas nunca aplicados. **Isso deixou de ser verdade**: os cinco
manifests desta aula — mais o `Secret` da Aula 12 — subiram em um cluster kind de
três nós. Este documento registra como reproduzir e, principalmente, **o experimento
de caos desta aula executado contra Pods de verdade**, com a perturbação aplicada
pelo próprio Kubernetes (`kubectl scale --replicas=0`) em vez de por uma alavanca
dentro da aplicação — foi assim que ele encontrou um defeito que a suíte de testes
não pegava.

## Instalação (Linux x86_64, sem sudo)

`kubectl` e `kind` são binários únicos; vão para `~/.local/bin`, que já está no PATH.

```bash
curl -sSLo kubectl "https://dl.k8s.io/release/v1.34.0/bin/linux/amd64/kubectl"
curl -sSLo kubectl.sha256 "https://dl.k8s.io/release/v1.34.0/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
install -m 0755 kubectl ~/.local/bin/kubectl

curl -sSLo kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-amd64
install -m 0755 kind ~/.local/bin/kind
```

> **Nota de versão.** O kind v0.30.0 sobe nós `kindest/node:v1.34.0`. Vale fixar o
> `kubectl` na mesma minor: o suporte oficial de skew é de um minor para cada lado.

O kind precisa de um motor de contêiner, e o usuário precisa estar no grupo `docker`:

```bash
sudo usermod -aG docker "$USER"   # se ainda não estiver no grupo
newgrp docker                     # ou reabrir a sessão; sem isso, "permission denied"
```

Para rodar os testes e os scripts, além do Python 3.12 é preciso ter os módulos de
empacotamento — em Debian/Ubuntu/Mint eles não vêm com o interpretador:

```bash
sudo apt-get install -y python3-pip python3-venv   # `make setup` falha sem isto
```

## Subir tudo

```bash
make k8s-up       # ./scripts/deploy_kind.sh — cria cluster, constrói, carrega e aplica
make k8s-status   # pods, services e HPA
make k8s-down     # destrói o cluster
```

O cluster (`k8s/kind/cluster.yaml`) tem um control-plane e dois workers, para que as
réplicas fiquem de fato em nós diferentes, e publica o NodePort 30080 na porta 8080 do
host. As portas 8000–8004 ficam livres de propósito: são as do `docker-compose`, que
pode continuar rodando em paralelo.

**O segredo de assinatura não vem de `k8s/segredos.yaml`.** O script cria o `Secret`
imperativamente, com valor aleatório gerado na hora — que é exatamente o que o
comentário daquele manifesto diz que se deve fazer. `segredos.yaml` documenta a forma
do objeto; é o único manifesto que `deploy_kind.sh` não aplica.

## O experimento de caos, agora com a perturbação vinda do orquestrador

O experimento em `test_saga_integracao.py` injeta falha com `falhar_percentual=100`:
o pagamento **responde**, só que com erro. No cluster existe uma perturbação mais
severa e mais realista — retirar o serviço do ar:

```bash
kubectl scale deployment pagamento --replicas=0
kubectl get endpoints pagamento     # ENDPOINTS: <none>
```

O Service continua existindo, o DNS continua resolvendo, e não há endpoint atrás
dele. Quem chama não recebe erro nem timeout: recebe **conexão recusada**.

### O defeito que isso revelou

Rodado contra o estágio da Aula 13, o resultado foi:

```
saga 1 -> HTTP 500 | estado do pedido: RECEBIDO
saga 2 -> HTTP 500 | estado do pedido: RECEBIDO
saga 3 -> HTTP 500 | estado do pedido: RECEBIDO
/saude: {'disjuntor_pagamento': 'fechado', ...}
saldo de estoque na réplica atingida: 99 → 96
```

Três falhas simultâneas de uma propriedade que o projeto afirmava ter desde a Aula 4:

1. A saga **não compensou** — estourou como erro interno no meio do caminho.
2. O disjuntor **não abriu**, exatamente no cenário para o qual ele existe.
3. Três reservas de estoque ficaram **penduradas para sempre**.

A causa é uma linha: `app/resiliencia.py` e `app/main.py` capturavam
`httpx.TimeoutException`. Um provedor fora do ar não dá timeout — ele levanta
`httpx.ConnectError`, que **não** é subclasse de `TimeoutException`. A exceção escapava
do `ClienteResiliente` (sem retentativa, sem registrar falha no disjuntor), escapava
das etapas da saga (sem virar `EtapaFalhou`) e chegava ao FastAPI como erro 500.

A correção é trocar a classe capturada por `httpx.TransportError`, a superclasse comum
de timeout e de erro de conexão. `test_experimento_de_caos_pagamento_fora_do_ar_tambem_compensa`
é a regressão: ele falha com `httpx.ConnectError` no código antigo e passa no novo.

Vale insistir no ponto pedagógico, porque é o argumento inteiro desta aula: **nenhum
teste desta suíte pegava isso**, e não por descuido. Todos usavam a única alavanca de
falha que o projeto tinha — `falhar_percentual` —, e essa alavanca produz um provedor
que responde. "Provedor ausente" é outro modo de falha, e só apareceu quando a
perturbação passou a vir do orquestrador, e não de dentro da aplicação.

### O experimento completo, depois da correção

Nove compras seguidas com `pagamento` em zero réplicas:

```
  saga 1: ok   1700.0 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=fechado
  saga 2: ok    651.2 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=fechado
  saga 3: ok   1697.7 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=fechado
  saga 4: ok   1712.5 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=fechado
  saga 5: ok   1751.3 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=fechado
  saga 6: ok   1766.9 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=fechado
  saga 7: ok   1780.6 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=aberto
  saga 8: ok     13.6 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=aberto
  saga 9: ok     12.0 ms  estado=RECEBIDO  compensou=['liberar_estoque']  disjuntor=aberto

saldo de estoque antes: 100 / 100     depois das 9 sagas: 100 / 100
```

As cinco salvaguardas do cartão do roteiro, preenchidas com o que se observou:

| Campo | Valor observado no cluster |
|---|---|
| Hipótese de estado estável | Nenhum pedido fica inconsistente; todos compensam; o disjuntor abre |
| Perturbação | `kubectl scale deployment pagamento --replicas=0` |
| Métricas de controle | `estado_final`/`compensacoes` por saga; `disjuntor_pagamento` em `/saude`; saldo por réplica de estoque |
| Raio de impacto | Cluster local de desenvolvimento, zero tráfego real |
| Critério de interrupção | `kubectl scale deployment pagamento --replicas=2` |

Três leituras que o teste em processo não dá:

- **A janela do disjuntor é de 20 chamadas, e cada saga gasta 3.** Por isso ele abre
  só na sétima saga, não na primeira. O teste unitário reduz a janela para 4 para não
  depender disso; o cluster mostra o número real — mais de vinte segundos de falhas
  antes da proteção entrar. Se isso é aceitável ou não, é decisão de projeto, e agora
  é uma decisão informada por um número medido.
- **A proteção vale ~130×.** 1.780 ms com o disjuntor fechado (três tentativas mais
  backoff, todas contra um endpoint inexistente) contra 13,6 ms com ele aberto.
- **Nenhuma reserva vazou.** O saldo voltou a 100 nas duas réplicas: a compensação de
  estoque rodou nas nove sagas, inclusive naquelas em que o disjuntor já estava aberto
  e o pagamento sequer foi tentado.

### Kill switch e recuperação

```
kubectl scale deployment pagamento --replicas=2
  recuperação: ok EXPEDIDO | disjuntor: fechado
saldo final: 99 / 100      ← a única compra que concluiu de verdade
```

O disjuntor volta sozinho para `fechado` pelo estado semiaberto, sem reinício de Pod
e sem intervenção — o mesmo mecanismo da Aula 4, agora exercitado contra uma
indisponibilidade real de infraestrutura.

## O que mais o cluster mostrou

- **`emptyDir` + réplicas dividem o estado.** O saldo é inicializado, e conferido,
  réplica a réplica: as duas cópias de `estoque` têm bancos independentes. Ver a
  seção equivalente em `aula_13/docs/kubernetes-execucao.md`, onde isso é explorado
  com o gateway.
- **Reconciliação.** `kubectl delete pod` em qualquer réplica: o ReplicaSet cria a
  substituta em segundos — mas o banco dela nasce vazio, porque `emptyDir` é
  armazenamento efêmero *por Pod*. Reconciliação de processo não é reconciliação de
  dado.
- **`imagePullPolicy` e `LoadBalancer`**: os dois ajustes que `deploy_kind.sh` aplica
  fora do manifesto, pelas razões documentadas no próprio script.

## Comandos do roteiro de aula

```bash
make k8s-up
kubectl get pods -o wide
kubectl scale deployment pagamento --replicas=0     # perturbação
kubectl get endpoints pagamento                     # ENDPOINTS: <none>
kubectl exec <pod-de-pedidos> -- python -c "..."    # rodar as sagas de dentro
kubectl scale deployment pagamento --replicas=2     # kill switch
make k8s-down
```
