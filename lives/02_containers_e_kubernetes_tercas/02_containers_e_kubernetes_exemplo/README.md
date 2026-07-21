# Aula: containers e Kubernetes com Podman

Projeto didático de um CRUD de pacientes feito em Streamlit, persistido no MongoDB. Ele pode ser executado primeiro com Compose e depois implantado em um cluster Kubernetes local.

Na Aula 3, use também o [mapa dos manifests e guia de demonstração ao vivo](GUIA_DEMONSTRACAO_K8S.md), com troca de Pods, self-healing, escala, rollout e persistência.

> Os dados são fictícios. Não use dados reais de pacientes: este exemplo não implementa os controles de segurança, auditoria e privacidade exigidos para dados de saúde.

## Arquitetura

```text
Navegador :8501
       |
       v
Streamlit (app) ---- mongodb://mongo:27017 ----> MongoDB
                                                  |
                                              volume persistente
```

O exemplo cobre:

- imagem da aplicação com `Dockerfile`;
- dois serviços declarados em `compose.yaml`;
- rede interna, variáveis de ambiente, health checks e volume;
- operações de criar, consultar, atualizar e excluir pacientes;
- `Deployment`, `StatefulSet`, `Service`, `Secret` e volume no Kubernetes;
- probes e limites básicos de recursos.

## Pré-requisitos

Não é necessário instalar Docker Desktop. Podman executa imagens OCI e o arquivo Compose deste projeto.

### Nesta máquina (Bazzite/Fedora Atomic)

O Podman já está instalado. Confira:

```bash
podman --version
```

Instale as ferramentas de linha de comando no ambiente do usuário:

```bash
brew install podman-compose kubectl minikube
```

Feche e abra o terminal se algum comando ainda não estiver no `PATH`. Em uma máquina Bazzite sem Homebrew configurado, use uma Distrobox Fedora:

```bash
distrobox create --name aula-k8s --image registry.fedoraproject.org/fedora:latest
distrobox enter aula-k8s
sudo dnf install -y podman podman-compose kubernetes-client
```

O Minikube deve ser instalado no host para conseguir criar a máquina/cluster; siga a instalação oficial caso não use o Homebrew.

### Fedora tradicional

```bash
sudo dnf install -y podman podman-compose kubernetes-client
```

### Ubuntu/Debian

```bash
sudo apt update
sudo apt install -y podman podman-compose
```

Instale também `kubectl` e `minikube` pelos repositórios/instruções oficiais de cada projeto. Ao preparar computadores de alunos, faça essa etapa antes da aula e teste downloads de imagens na rede da instituição.

## Parte 1 — executar com Compose

Entre na pasta do projeto:

```bash
cd 02_containers_e_kubernetes_tercas/02_containers_e_kubernetes_exemplo
cp .env.example .env
```

Edite `.env` para não usar a senha de exemplo. O arquivo está ignorado no contexto da imagem. Então suba o ambiente:

```bash
podman compose up --build -d
```

`podman compose` encaminha o comando para um provedor Compose externo. Caso sua versão não o encontre, use diretamente:

```bash
podman-compose up --build -d
```

Abra <http://localhost:8501>. Para acompanhar e investigar:

```bash
podman compose ps
podman compose logs -f app
podman compose logs mongo
```

Teste a API de saúde do Streamlit:

```bash
curl http://localhost:8501/_stcore/health
```

Pare os containers sem apagar os pacientes:

```bash
podman compose down
```

Para reiniciar: `podman compose up -d`. O volume nomeado preserva os dados. Somente quando quiser apagar também o banco da aula:

```bash
podman compose down -v
```

## Docker x Podman

Os comandos são muito semelhantes:

| Docker | Podman |
|---|---|
| `docker build -t nome .` | `podman build -t nome .` |
| `docker images` | `podman images` |
| `docker ps` | `podman ps` |
| `docker compose up` | `podman compose up` |

Podman não exige um daemon central e pode trabalhar em modo *rootless*. Não é preciso criar um alias `docker=podman`; para a aula, usar o nome real deixa a ferramenta escolhida explícita.

## Parte 2 — Kubernetes local com Minikube e Podman

### 1. Iniciar o cluster

```bash
minikube config set rootless true
minikube start --driver=podman --container-runtime=containerd --cpus=2 --memory=4096
kubectl cluster-info
kubectl get nodes
```

O primeiro comando evita que o Minikube tente executar Podman com `sudo`. Se o driver rootless reclamar de delegação de cgroups, confira `podman info` e os pré-requisitos do driver Podman na documentação do Minikube. Em laboratório, teste isso previamente em cada sistema operacional.

### 2. Construir e carregar a imagem local

O Kubernetes não enxerga automaticamente as imagens armazenadas pelo Podman no host. Construa a aplicação, salve em um arquivo OCI/Docker e carregue no Minikube:

```bash
podman build -t localhost/aula-pacientes:1.0 .
podman save -o /tmp/aula-pacientes.tar localhost/aula-pacientes:1.0
minikube image load /tmp/aula-pacientes.tar
minikube image ls | grep aula-pacientes
```

O manifesto usa `imagePullPolicy: Never`, pois a imagem foi carregada localmente. Em produção, envie a imagem a um registry e use seu endereço completo.

### 3. Aplicar os manifests

Antes de uma demonstração fora do laboratório, altere a senha didática em `k8s/secret.yaml`. Em seguida:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/secret.yaml
kubectl apply -f k8s/mongo.yaml
kubectl apply -f k8s/app.yaml
kubectl get all,pvc -n aula-pacientes
kubectl wait --for=condition=ready pod -l app=mongo -n aula-pacientes --timeout=180s
kubectl wait --for=condition=available deployment/pacientes-app -n aula-pacientes --timeout=180s
```

### 4. Acessar a aplicação

Deixe este comando executando e abra <http://localhost:8501>:

```bash
kubectl port-forward service/pacientes-app 8501:8501 -n aula-pacientes
```

Em outro terminal, pratique observabilidade:

```bash
kubectl get pods -n aula-pacientes -w
kubectl logs deployment/pacientes-app -n aula-pacientes
kubectl describe pod -l app=pacientes-app -n aula-pacientes
kubectl exec -it mongo-0 -n aula-pacientes -- mongosh -u admin -p admin-aula --authenticationDatabase admin
```

### 5. Demonstrar atualização e escala

Depois de alterar o código, use uma nova tag para tornar a atualização visível:

```bash
podman build -t localhost/aula-pacientes:1.1 .
podman save -o /tmp/aula-pacientes-1.1.tar localhost/aula-pacientes:1.1
minikube image load /tmp/aula-pacientes-1.1.tar
kubectl set image deployment/pacientes-app app=localhost/aula-pacientes:1.1 -n aula-pacientes
kubectl rollout status deployment/pacientes-app -n aula-pacientes
kubectl rollout history deployment/pacientes-app -n aula-pacientes
```

O Streamlit poderia ter várias réplicas, mas este exemplo mantém uma para consumir menos memória. Para demonstrar:

```bash
kubectl scale deployment/pacientes-app --replicas=2 -n aula-pacientes
kubectl get pods -n aula-pacientes
```

Não escale o MongoDB apenas aumentando `replicas`: banco distribuído exige replica set, configuração e estratégia de armazenamento próprias.

### 6. Limpeza

Apagar o namespace remove os objetos e o PVC da aula:

```bash
kubectl delete namespace aula-pacientes
minikube stop
```

Para remover inteiramente o cluster local:

```bash
minikube delete
```

## Ordem sugerida para a aula

1. Executar `main.py` localmente e discutir por que `localhost` muda dentro de um container.
2. Construir a imagem e apresentar camadas, `COPY`, `RUN`, `CMD`, porta e health check.
3. Subir o Compose e identificar serviço, rede e volume.
4. Fazer o CRUD e reiniciar containers para provar a persistência.
5. Comparar Compose (execução multi-container) com Kubernetes (orquestração).
6. Criar o cluster, carregar a imagem e aplicar cada manifesto separadamente.
7. Usar `get`, `describe`, `logs`, probes, rollout e escala.
8. Limpar os recursos ao final.

## Solução de problemas

**`podman compose` informa que não há provider:** instale `podman-compose` e tente `podman-compose up --build`.

**A porta 8501 ou 27017 já está ocupada:** descubra o processo/container com `podman ps` e `ss -ltnp`. Pare o serviço conflitante ou altere apenas o lado esquerdo do mapeamento em `compose.yaml`.

**O app inicia antes do banco:** o Compose já usa o health check do MongoDB. Veja `podman compose logs mongo`. No Kubernetes, acompanhe `kubectl get pods -n aula-pacientes -w`.

**`ImagePullBackOff`/`ErrImageNeverPull`:** confirme que a tag do manifesto é idêntica à retornada por `minikube image ls`; repita a etapa de carregar a imagem.

**Minikube encerra com `Error downloading kic artifacts: not yet implemented`:** essa é uma limitação que pode ocorrer na combinação Minikube/Podman rootless. Atualize ambos e tente novamente. Para uma aula que não pode depender dessa combinação, prepare previamente uma VM Linux com Minikube ou use `kind` com seu suporte experimental a Podman; os manifests do diretório `k8s/` continuam os mesmos.

**PVC fica `Pending`:** verifique `kubectl get storageclass` e `kubectl describe pvc -n aula-pacientes`. O Minikube normalmente fornece uma classe padrão; clusters diferentes podem exigir `storageClassName`.

**Mudou a senha depois que o Mongo já tinha dados:** as variáveis `MONGO_INITDB_*` só inicializam um diretório vazio. Para reiniciar a aula do zero, remova conscientemente o volume (`podman compose down -v`) ou o namespace/PVC do Kubernetes.

## Arquivos

```text
.
├── main.py              # CRUD Streamlit
├── requirements.txt     # dependências Python
├── Dockerfile           # imagem da aplicação
├── compose.yaml         # app + MongoDB
├── .env.example         # modelo de configuração local
└── k8s/
    ├── namespace.yaml
    ├── secret.yaml
    ├── mongo.yaml       # Service + StatefulSet + PVC
    └── app.yaml         # Deployment + Service
```

Referências oficiais: [Podman](https://podman.io/docs), [Podman Compose](https://docs.podman.io/en/latest/markdown/podman-compose.1.html), [Minikube](https://minikube.sigs.k8s.io/docs/start/), [kubectl](https://kubernetes.io/docs/tasks/tools/) e [Kubernetes](https://kubernetes.io/docs/home/).
