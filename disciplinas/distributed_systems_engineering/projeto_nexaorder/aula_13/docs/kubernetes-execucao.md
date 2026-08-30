# Execução real dos manifests em um cluster local (kind) — Aula 13

O ADR 0011 (Aula 11) registrou que os manifests tinham sido validados
estruturalmente, mas nunca aplicados. **Isso deixou de ser verdade**: os cinco
manifests desta aula — mais o `Secret` da Aula 12 — subiram em um cluster kind de
três nós, e a saga completa rodou dentro dele. Este documento registra como
reproduzir e, principalmente, o que a observabilidade da Aula 13 revela quando os
serviços estão de fato em Pods separados.

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

## O que a execução revelou

### 1. Um trace, dez fragmentos, sete Pods — a defesa do ADR 0013, ao vivo

Uma compra com `X-Trace-Id: trace-aula13-cluster` percorreu quatro serviços. Os spans
existem, todos com o mesmo trace_id — e cada um mora no Pod que fez o trabalho:

```
pedidos-686677f99d-2wlzl   5 spans  [POST /pedidos, POST /pedidos/{id}/finalizar-compra,
                                     reservar_estoque, autorizar_pagamento, solicitar_expedicao]
pedidos-686677f99d-dr542   0 spans
pedidos-686677f99d-fs6pl   0 spans
pedidos-686677f99d-k6j6s   0 spans
estoque-8d4fc544f-t66kq    2 spans  [POST /reservas, persistir_reserva]
estoque-8d4fc544f-xghxk    0 spans
pagamento-7cdf5bd599-6s5mt 2 spans  [POST /cobrancas, persistir_cobranca]
pagamento-7cdf5bd599-cxnk6 0 spans
expedicao-84dbb64d69-k6sjq 1 span   [POST /remessas]
expedicao-84dbb64d69-4n5sb 0 spans
```

A propagação funciona: o `X-Trace-Id` atravessou os quatro serviços por chamadas de
rede reais entre Pods, e não por `ASGITransport` em processo, como nos testes.

O que **não** funciona é a leitura. `GET /_admin/spans/{trace_id}` pelo Service
devolve os spans de **uma** réplica sorteada — em 12 réplicas, dez fragmentos de um
único trace. Reconstruir a cascata exige perguntar a cada Pod, um a um, e juntar na
mão. Não existe consulta que devolva o trace inteiro. Este é, literalmente, o
compromisso aceito no `docs/adr/0013-spans-locais-sem-coletor-central.md` — e ele só
dói quando há mais de um processo. Um coletor central não é sofisticação: é o que
torna a instrumentação utilizável.

### 2. `emptyDir` + réplicas: o 404 não é aleatório, é fixo

O pedido criado existe em exatamente **uma** das quatro réplicas de `pedidos` — cada
uma monta seu próprio `emptyDir`, logo seu próprio SQLite:

```
pedidos-686677f99d-2wlzl -> TEM o pedido
pedidos-686677f99d-dr542 -> HTTP 404
pedidos-686677f99d-fs6pl -> HTTP 404
pedidos-686677f99d-k6j6s -> HTTP 404
```

A parte contraintuitiva é o comportamento pelo gateway. O Service balanceia
**conexões**, não requisições, e o `httpx.AsyncClient` do gateway mantém a conexão
aberta. O resultado é determinístico por Pod de gateway, não aleatório por requisição:

```
24 requisições seguidas ao gateway:  404 (24/24)
kubectl rollout restart deployment/gateway
  reinício 1:  404 404 404 404 404 404 404 404   ← as duas réplicas caíram na errada
  reinício 2:  200 404 200 404 404 404 404 404   ← uma acertou, a outra não
  reinício 3:  200 200 200 200 200 200 200 200   ← as duas acertaram
```

Mesmos dados, mesmo pedido, mesma requisição: o resultado depende de qual conexão
cada réplica de gateway abriu quando subiu. Escala horizontal só é gratuita para
serviço sem estado. `emptyDir` é armazenamento *efêmero por Pod*, não do serviço; a
correção real é `StatefulSet` + `PersistentVolumeClaim`, ou um banco fora do cluster.

### 3. A falha que os testes desta aula não pegam

Com `kubectl scale deployment pagamento --replicas=0`, três compras seguidas:

```
saga 1 -> HTTP 500 | estado do pedido: RECEBIDO
saga 2 -> HTTP 500 | estado do pedido: RECEBIDO
saga 3 -> HTTP 500 | estado do pedido: RECEBIDO
/saude: {'disjuntor_pagamento': 'fechado', ...}
saldo de estoque na réplica atingida: 99 → 96
```

Três coisas erradas de uma vez: a saga estourou como erro interno em vez de
compensar, o disjuntor **não abriu** — justamente no caso em que ele mais importa — e
três unidades de estoque ficaram reservadas para sempre.

A causa está em `app/resiliencia.py` e `app/main.py`: até esta aula, ambos capturam
`httpx.TimeoutException`. Um provedor **fora do ar** não dá timeout — ele recusa a
conexão (`httpx.ConnectError`), que não é subclasse de `TimeoutException`. A alavanca
`falhar_percentual=100`, usada nos testes desde a Aula 4, faz o provedor *responder*
com erro; ela nunca exercitou o caso em que o provedor não está lá.

**Isto não é corrigido nesta aula, deliberadamente** — é a pergunta que a Aula 14
existe para responder, e a resposta está em `aula_14/docs/testes-e-caos.md`. Vale
registrar aqui o que a Aula 13 acrescenta ao diagnóstico: os três pilares mostram
*que* algo quebrou e *onde*; não impedem que quebre.

## O que funcionou como escrito

- **As doze réplicas subiram e ficaram `Ready`** nos dois workers, com as duas sondas
  distintas: `/saude` (vivacidade) e `/pronto` (prontidão).
- **A saga completa rodou dentro do cluster**, com `pedidos` alcançando os outros
  serviços pelo DNS do Kubernetes (`http://estoque:8000`), sem nenhum IP no manifesto,
  e com o token HMAC da Aula 12 assinado pelo segredo aleatório do `Secret`.
- **Reconciliação.** `kubectl delete pod` em uma réplica: o ReplicaSet cria a
  substituta em segundos, sem intervenção.
- **O HPA leu métricas reais** depois do metrics-server (instalado pelo script com
  `--kubelet-insecure-tls`, porque o kubelet do kind usa certificado auto-assinado).

## Comandos do roteiro de aula

```bash
kubectl get pods -o wide                      # réplicas espalhadas pelos nós
kubectl get svc                               # gateway LoadBalancer <pending> + NodePort
kubectl get hpa pedidos                       # cpu: N%/60%
kubectl exec <pod> -- python -c "import urllib.request; \
  print(urllib.request.urlopen('http://localhost:8000/_admin/spans/<trace>').read())"
curl http://localhost:8080/saude              # gateway pelo NodePort
```
