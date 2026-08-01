# Live 02 · Aula 04 — Kubernetes na prática & deploy completo

Roteiro prático da [aula4.html](aula4.html): deploy ponta a ponta da aplicação
**Livraria** (Streamlit + MongoDB) usando **Podman** + **minikube**, cobrindo
ConfigMap, Secret, probes, Service, Ingress, HPA, rolling update e rollback.

> **Ambiente já verificado e testado nesta máquina (28/07):** podman 5.8.4
> (rootless), kubectl v1.36.3, minikube v1.38.1 (instalado via brew), cluster
> criado e fluxo completo executado com sucesso. Se você está em outra máquina,
> siga o passo 0.

## Arquivos

| Arquivo | O que é | Slide da aula |
|---|---|---|
| `Dockerfile` | Imagem do app Streamlit | — |
| `docker-compose.yml` | Versão compose (aulas anteriores / teste rápido) | — |
| `k8s/01-configmap.yaml` | ConfigMap `web-config` — config fora do código | ConfigMap |
| `k8s/02-secret.yaml` | Secret `db-secret` — senha e URI do banco | Secret |
| `k8s/03-mongo.yaml` | PVC + Deployment + Service do MongoDB | Persistência (aula 2) |
| `k8s/04-app.yaml` | Deployment `web` (probes, resources) + Service | Probes / Quebra-cabeça |
| `k8s/05-ingress.yaml` | Ingress `livraria.local` → Service `web` | Ingress |
| `k8s/06-hpa.yaml` | HPA 2–10 réplicas, CPU 70% | Escala |
| `seed_clientes.py` | Popula 1000 clientes no Mongo | — |

---

## Passo 0 — Pré-requisitos (só se estiver em outra máquina)

```bash
# Fedora/Bazzite: podman já vem instalado. Verifique:
podman --version          # >= 4.x, testado com 5.8.4

# kubectl e minikube via Homebrew (não exige reboot em distros imutáveis):
brew install kubectl minikube

# minikube rootless precisa do socket do podman e de cgroups v2 delegados:
systemctl --user enable --now podman.socket
cat /sys/fs/cgroup/user.slice/user-$(id -u).slice/user@$(id -u).service/cgroup.controllers
# precisa listar pelo menos: cpu memory pids
```

## Passo 1 — Teste rápido só com Podman (sem Kubernetes)

Sanity check da aplicação antes de ir para o cluster:

```bash
podman compose up -d --build     # usa o docker-compose.yml (via podman-compose)
# abra http://localhost:8501  → "✅ Conectado ao MongoDB!"

# popular dados de exemplo (1000 clientes):
podman exec livraria-app python seed_clientes.py

podman compose down              # derruba antes de ir para o Kubernetes
```

## Passo 2 — Subir o cluster

```bash
minikube config set rootless true
minikube start --driver=podman --container-runtime=containerd --memory=4096 --cpus=2
```

Habilite os dois addons que a aula usa:

```bash
minikube addons enable metrics-server   # necessário para o HPA
minikube addons enable ingress          # necessário para o Ingress
```

Confira: `kubectl get nodes` deve mostrar o nó `minikube` como `Ready`.

## Passo 3 — Construir a imagem v1 dentro do cluster

O cluster não enxerga imagens do podman do host; construa direto nele:

```bash
minikube image build -t livraria-app:v1 .
```

## Passo 4 — Deploy ponta a ponta

```bash
kubectl apply -f k8s/
kubectl rollout status deploy/mongo
kubectl rollout status deploy/web
kubectl get pods            # 1 mongo + 2 web, todos 1/1 Running
```

O que acabou de subir (o "quebra-cabeça completo" do slide):

- **ConfigMap + Secret** → injetados no Pod `web` como variáveis de ambiente
  (`envFrom` / `secretKeyRef` em [k8s/04-app.yaml](k8s/04-app.yaml)).
- **Probes** → liveness e readiness em `/_stcore/health` (endpoint de saúde do
  Streamlit). Reinicia se travar; só recebe tráfego quando pronto.
- **Service `web`** → IP interno estável na porta 80 → 8501.
- **Ingress** → roteia `livraria.local` para o Service.
- **HPA** → 2 a 10 réplicas, alvo de 70% de CPU.

## Passo 5 — Acessar a aplicação

> **Importante (podman rootless):** o IP do cluster (`minikube ip`) **não é
> acessível** direto do host. Use `kubectl port-forward` — é o caminho testado.

**Via Service** (dia a dia / demo principal):

```bash
kubectl port-forward svc/web 8501:80
# abra http://localhost:8501
```

**Via Ingress** (para demonstrar o roteamento por host):

```bash
kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80
curl -H "Host: livraria.local" http://localhost:8080/_stcore/health   # → ok

# para abrir no navegador como http://livraria.local:8080 (opcional):
echo "127.0.0.1 livraria.local" | sudo tee -a /etc/hosts
```

## Passo 6 — Popular dados

O seed roda dentro de um Pod do app (que já tem `pymongo` e o `MONGO_URI`):

```bash
POD=$(kubectl get pods -l app=web -o jsonpath='{.items[0].metadata.name}')
kubectl cp seed_clientes.py $POD:/app/seed_clientes.py
kubectl exec $POD -- python seed_clientes.py
```

Recarregue o dashboard: 1000 clientes.

## Passo 7 — HPA: escala automática sob carga

Em um terminal, deixe o HPA visível:

```bash
watch kubectl get hpa,pods -l app=web
```

Em outro, gere carga (loop de requisições contra o Service):

```bash
kubectl run carga --image=busybox --restart=Never -- \
  /bin/sh -c 'while true; do wget -q -O- http://web >/dev/null 2>&1; done'
```

Em 1–2 minutos o `TARGETS` passa de 70% e o HPA cria novas réplicas
(`kubectl get events --sort-by=.lastTimestamp | tail` mostra o
`SuccessfulRescale`). Para encerrar a carga:

```bash
kubectl delete pod carga
# a redução de réplicas demora ~5 min (janela de estabilização padrão do HPA)
```

## Passo 8 — Rolling update & rollback

Faça uma mudança visível e construa a **v2**:

```bash
sed -i 's/📚 Menu - Livraria/📚 Menu - Livraria (v2)/' app.py
minikube image build -t livraria-app:v2 .
git checkout app.py        # desfaz a edição local; a v2 já está na imagem
```

Rolling update — acompanhe com a página aberta, o site não cai:

```bash
kubectl set image deploy/web web=livraria-app:v2
kubectl rollout status deploy/web
# recarregue o navegador → menu mostra "(v2)"
```

Deu ruim? Rollback imediato:

```bash
kubectl rollout undo deploy/web
kubectl rollout status deploy/web
# navegador volta a mostrar a v1
```

## Comandos de inspeção úteis durante a aula

```bash
kubectl get all                      # visão geral
kubectl describe pod <nome>          # eventos, probes, envs
kubectl logs -l app=web -f           # logs do app
kubectl top pods                     # consumo (metrics-server)
kubectl get hpa web                  # estado do autoscaler
kubectl get configmap web-config -o yaml
kubectl get secret db-secret -o yaml # valores em base64 (não criptografados!)
```

## Solução de problemas

| Sintoma | Causa provável / correção |
|---|---|
| `TARGETS <unknown>` no HPA | Métricas demoram ~2 min após o Pod subir; confirme `kubectl top pods` |
| Pod `web` em `ErrImageNeverPull` | Imagem não foi construída no cluster — repita o passo 3 |
| Pod `web` reiniciando (probe) | `kubectl describe pod` → veja eventos; Mongo pode não estar pronto ainda |
| App com erro de conexão Mongo | `kubectl logs deploy/mongo`; confira o Secret `db-secret` |
| `minikube ip` não responde | Normal em rootless — use `kubectl port-forward` (passo 5) |
| `minikube start` falha | `minikube delete --all` e repita o passo 2 |

## Limpeza no fim da aula

```bash
kubectl delete -f k8s/       # remove app, banco, ingress, hpa (PVC incluso)
minikube stop                # pausa o cluster (mantém estado)
# ou, para apagar tudo:
minikube delete
```
