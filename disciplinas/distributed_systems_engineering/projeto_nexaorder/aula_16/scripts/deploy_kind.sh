#!/usr/bin/env bash
# Sobe o NexaOrder da Aula 16 em um cluster Kubernetes real e local (kind).
#
#   ./scripts/deploy_kind.sh          # cria o cluster, constrói, carrega e aplica
#   ./scripts/deploy_kind.sh destruir # remove o cluster
#
# Pré-requisitos: docker (usuário no grupo `docker`), kind e kubectl no PATH.
# Ver docs/kubernetes-execucao.md para a instalação dos binários.
set -euo pipefail

CLUSTER=${CLUSTER:-nexaorder}
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

# O segredo de assinatura HMAC (Aula 12) é criado IMPERATIVAMENTE, com um
# valor aleatório gerado agora — que é exatamente o que o comentário de
# k8s/segredos.yaml diz que se deve fazer ("nunca commitado"). Por isso
# segredos.yaml é o único manifesto que este script não aplica: ele
# documenta a FORMA do objeto, não um valor utilizável.
echo "==> segredo de assinatura (aleatório, criado imperativamente)"
kubectl create secret generic nexaorder-segredos \
  --from-literal=NEXAORDER_SEGREDO_ASSINATURA="$(head -c 32 /dev/urandom | base64)" \
  --dry-run=client -o yaml | kubectl apply -f - >/dev/null

echo "==> imagens"
for s in "${SERVICOS[@]}"; do
  docker build -q -t "nexaorder/$s:latest" "./services/$s"
  kind load docker-image "nexaorder/$s:latest" --name "$CLUSTER"
done

echo "==> manifests"
for manifesto in k8s/*.yaml; do
  [[ "$(basename "$manifesto")" == "segredos.yaml" ]] && continue
  kubectl apply -f "$manifesto"
done

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

# Reexecutar o script sobre um cluster que já existe recarrega a imagem no
# containerd dos nós, mas o manifesto continua idêntico — `kubectl apply` não
# detecta mudança nenhuma e os Pods seguem com o código antigo. A tag
# `:latest` é a mesma; o que mudou foi o conteúdo dela. O rollout explícito é
# o que faz o cluster pegar o build novo.
echo "==> rollout (recarrega o código novo sob a mesma tag :latest)"
for s in "${SERVICOS[@]}"; do kubectl rollout restart "deployment/$s" >/dev/null; done

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
