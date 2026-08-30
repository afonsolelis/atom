#!/usr/bin/env bash
# Sobe o NexaOrder da Aula 11 em um cluster Kubernetes real e local (kind).
#
#   ./scripts/deploy_kind.sh          # cria o cluster, constrói, carrega e aplica
#   ./scripts/deploy_kind.sh destruir # remove o cluster
#
# Pré-requisitos: docker (usuário no grupo `docker`), kind e kubectl no PATH.
# Ver docs/kubernetes-execucao.md para a instalação dos binários.
set -euo pipefail

CLUSTER=nexaorder
SERVICOS=(pedidos estoque pagamento expedicao gateway)
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$RAIZ"

if [[ "${1:-}" == "destruir" ]]; then
  kind delete cluster --name "$CLUSTER"
  exit 0
fi

echo "==> cluster kind"
kind get clusters 2>/dev/null | grep -qx "$CLUSTER" \
  || kind create cluster --config k8s/kind/cluster.yaml --wait 120s
kubectl config use-context "kind-$CLUSTER"

echo "==> imagens"
for s in "${SERVICOS[@]}"; do
  docker build -q -t "nexaorder/$s:latest" "./services/$s"
  kind load docker-image "nexaorder/$s:latest" --name "$CLUSTER"
done

echo "==> manifests"
kubectl apply -f k8s/

# Os manifests não declaram imagePullPolicy. Com a tag `:latest` o padrão do
# Kubernetes é `Always`, que aqui falharia: as imagens estão só no containerd
# dos nós (via `kind load`), não em um registro. Em um cluster com registro de
# verdade este patch não é necessário — por isso ele fica no script, e não no
# manifesto.
for s in "${SERVICOS[@]}"; do
  kubectl patch deployment "$s" --type=json \
    -p '[{"op":"add","path":"/spec/template/spec/containers/0/imagePullPolicy","value":"IfNotPresent"}]' \
    >/dev/null
done

# O Service `gateway` é LoadBalancer; em kind não há provedor de nuvem, mas o
# NodePort alocado funciona. Fixá-lo em 30080 casa com o extraPortMappings de
# k8s/kind/cluster.yaml, publicando o gateway em http://localhost:8080.
kubectl patch service gateway --type=json \
  -p '[{"op":"replace","path":"/spec/ports/0/nodePort","value":30080}]' >/dev/null

echo "==> metrics-server (o HPA de pedidos precisa de métricas de CPU)"
if ! kubectl get deployment metrics-server -n kube-system >/dev/null 2>&1; then
  kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
  # kind usa certificados de kubelet auto-assinados.
  kubectl patch deployment metrics-server -n kube-system --type=json \
    -p '[{"op":"add","path":"/spec/template/spec/containers/0/args/-","value":"--kubelet-insecure-tls"}]' \
    >/dev/null
fi

echo "==> aguardando"
for s in "${SERVICOS[@]}"; do kubectl rollout status "deployment/$s" --timeout=180s; done

kubectl get pods -o wide
kubectl get svc
echo
echo "gateway: http://localhost:8080/saude"
