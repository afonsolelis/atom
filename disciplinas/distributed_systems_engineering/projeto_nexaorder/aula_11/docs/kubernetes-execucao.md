# Execução real dos manifests em um cluster local (kind)

O ADR 0011 registrou que os manifests da Aula 11 tinham sido validados
estruturalmente, mas nunca aplicados — não havia Docker nem Kubernetes na máquina
de escrita. **Isso deixou de ser verdade**: os cinco manifests foram aplicados em um
cluster kind de três nós e o fluxo da saga rodou de ponta a ponta dentro dele. Este
documento registra como reproduzir e o que a execução revelou.

## Instalação (Linux x86_64, sem sudo)

`kubectl` e `kind` são binários únicos; vão para `~/.local/bin`, que já está no PATH.

```bash
KV=$(curl -sSL https://dl.k8s.io/release/stable.txt)      # ou v1.34.0, ver nota
curl -sSLo kubectl "https://dl.k8s.io/release/${KV}/bin/linux/amd64/kubectl"
curl -sSLo kubectl.sha256 "https://dl.k8s.io/release/${KV}/bin/linux/amd64/kubectl.sha256"
echo "$(cat kubectl.sha256)  kubectl" | sha256sum --check
install -m 0755 kubectl ~/.local/bin/kubectl

curl -sSLo kind https://kind.sigs.k8s.io/dl/v0.30.0/kind-linux-amd64
install -m 0755 kind ~/.local/bin/kind
```

> **Nota de versão.** O kind v0.30.0 sobe nós `kindest/node:v1.34.0`. Vale fixar o
> `kubectl` em v1.34.0 também: o suporte oficial de skew é de um minor para cada
> lado, e `stable.txt` já aponta para v1.37.0.

O kind precisa de um motor de contêiner. O Docker já estava instalado nesta máquina;
faltava só a sessão enxergar o grupo `docker` (o usuário tinha sido adicionado, mas
sem novo login):

```bash
sudo usermod -aG docker "$USER"   # se ainda não estiver no grupo
newgrp docker                     # ou reabrir a sessão; sem isso, "permission denied"
```

## Subir tudo

```bash
./scripts/deploy_kind.sh          # cria cluster, constrói, carrega e aplica
./scripts/deploy_kind.sh destruir # remove o cluster
```

O cluster (`k8s/kind/cluster.yaml`) tem um control-plane e dois workers, para que as
réplicas fiquem de fato em nós diferentes, e publica o NodePort 30080 na porta 8080
do host. As portas 8000–8004 ficam livres de propósito: são as do `docker-compose` da
Aula 9, que pode continuar rodando em paralelo.

## O que a execução revelou (e a validação estrutural não pegava)

Três coisas — exatamente a classe de erro que o ADR 0011 admitia não detectar.

**1. `imagePullPolicy` ausente com a tag `:latest`.** O padrão do Kubernetes para
`:latest` é `Always`. As imagens estão só no containerd dos nós, via
`kind load docker-image`, e não em um registro: sem `IfNotPresent` os doze Pods param
em `ErrImagePull`. O `deploy_kind.sh` aplica esse patch fora do manifesto, porque em
um cluster com registro de verdade o `Always` é o comportamento correto.

**2. `type: LoadBalancer` fica `<pending>` para sempre.** Não há provedor de nuvem
no kind. O Service continua funcionando pelo NodePort que o Kubernetes aloca de
qualquer forma — o script o fixa em 30080 para casar com o `extraPortMappings`.

**3. `emptyDir` + `replicas: 2` divide o estado.** Este é o achado que mais importa
para a disciplina. Cada réplica monta seu próprio `emptyDir`, logo seu próprio
SQLite. Inicializar o saldo pelo Service atinge **uma** réplica; a outra segue sem o
SKU. E ao apagar um Pod, o ReplicaSet recria — com o volume vazio:

```
$ for i in $(seq 8); do curl -so /dev/null -w '%{http_code} ' \
    http://localhost:8080/pedidos/$ID/resumo; done
200 200 200 200 200 200 200 404
```

O 404 não é bug do gateway: é o `pedidos` com quatro réplicas e quatro bancos
distintos, e o Service sorteando entre elas. Escala horizontal só é gratuita para
serviço sem estado — o gateway, que é o único sem volume, escala sem nenhum desses
sintomas. Um `emptyDir` é armazenamento *efêmero por Pod*, não do serviço; a correção
real é `StatefulSet` + `PersistentVolumeClaim`, ou um banco fora do cluster.

## O que funcionou como escrito

- **As doze réplicas subiram e ficaram `Ready`** nos dois workers, com as duas sondas
  distintas: `/saude` (vivacidade) e `/pronto` (prontidão).
- **A saga completa rodou dentro do cluster**, com `pedidos` alcançando `estoque`,
  `pagamento` e `expedicao` pelo DNS do Kubernetes (`http://estoque:8000`), sem
  nenhum endereço IP no manifesto:
  ```json
  {"sucesso": true, "estado_final": "EXPEDIDO", "falhou_em": null, "compensacoes": []}
  ```
- **Reconciliação.** `kubectl delete pod` em uma réplica de `estoque`: o ReplicaSet
  criou a substituta em segundos, sem intervenção. É a diferença entre declarar o
  estado desejado e executar passos de implantação.
- **O HPA leu métricas reais** depois do metrics-server (instalado pelo script, com
  `--kubelet-insecure-tls`, porque o kubelet do kind usa certificado auto-assinado):
  ```
  NAME      REFERENCE            TARGETS      MINPODS  MAXPODS  REPLICAS
  pedidos   Deployment/pedidos   cpu: 2%/60%  2        10       4
  ```
  Com 2% contra um alvo de 60%, o HPA reduz para o `minReplicas: 2` — o oposto do
  exemplo do roteiro (`⌈4 × 85/60⌉ = 6`), que precisa de carga para aparecer.
- **A prontidão do gateway oscilou sob carga.** Nos eventos:
  `Readiness probe failed: HTTP probe failed with statuscode: 503`. O `/pronto` do
  gateway checa se `pedidos` está alcançável; quando a chamada estoura o timeout, o
  Pod sai do Service e volta sozinho no ciclo seguinte, **sem reiniciar**. É a sonda
  fazendo exatamente o que a Aula 11 diz que ela faz.

## Comandos do roteiro de aula

```bash
kubectl get pods -o wide                 # réplicas espalhadas pelos nós
kubectl get svc                          # gateway LoadBalancer <pending> + NodePort
kubectl get hpa pedidos                  # cpu: N%/60%
kubectl top pods                         # métricas por Pod
kubectl delete pod -l app=estoque --field-selector … # reconciliação ao vivo
kubectl describe pod <pod> | grep -A3 Liveness       # as duas sondas declaradas
curl http://localhost:8080/saude         # gateway pelo NodePort
```
