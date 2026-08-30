# Execução real dos manifests em um cluster local (kind) — Aula 15

O ADR 0011 (Aula 11) registrou que os manifests tinham sido validados
estruturalmente, mas nunca aplicados. **Isso deixou de ser verdade**: os cinco
manifests desta aula — mais o `Secret` da Aula 12 — subiram em um cluster kind de
três nós. Este documento registra como reproduzir e, principalmente, **o que acontece
com o pipeline de fluxo desta aula quando `pedidos` tem quatro réplicas** — a pergunta
que o `docker-compose`, com uma instância só, nunca chega a fazer.

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

## A janela por tempo de evento não sobrevive à escala horizontal

O experimento: doze tentativas do mesmo dispositivo, em doze segundos de tempo de
evento, com uma janela de 60 segundos. Duas execuções, mesmos dados.

**A) Todas as tentativas chegam à mesma réplica** — o que os testes desta aula
assumem, porque neles há um só processo:

```
partição escolhida: 4
contagem na janela nesta réplica: 12
```

Doze. Um alerta com limiar de, digamos, dez tentativas em sessenta segundos dispara.

**B) As mesmas doze, distribuídas pelas quatro réplicas** — o que um `Service` do
Kubernetes de fato faz:

```
partição calculada em cada envio: 2 2 2 2 2 2 2 2 2 2 2 2
contagem na janela, por réplica:
  pedidos-8696549fdf-8gxjj -> 3
  pedidos-8696549fdf-b8pzt -> 3
  pedidos-8696549fdf-s48wg -> 3
  pedidos-8696549fdf-v9vbg -> 3
```

Nenhuma réplica vê mais de três. O alerta **nunca dispara**, e não há erro em lugar
nenhum: cada Pod respondeu 201, cada contagem está correta para os dados que aquele
Pod recebeu. O padrão de fraude simplesmente deixou de existir como padrão.

### O detalhe que torna isso interessante

Repare na linha das partições: **as quatro réplicas calcularam a mesma partição, 2**,
para a mesma chave. `escolher_particao` (Aula 10) é determinístico e funciona
perfeitamente. A decisão de roteamento está correta em todos os Pods.

O que falta não é o cálculo — é alguém **obrigar** o evento a ir para o consumidor
dono daquela partição. Em um Kafka com grupo de consumidores, a partição 2 tem um dono
único, e todo evento de `disp-B` chega nele. Aqui, cada réplica calcula a partição
certa e depois guarda o evento em sua própria memória, porque `Topico` e
`JanelaPorTempoDeEvento` vivem dentro do processo (ADR 0010, ADR 0015).

É a diferença exata entre *particionar por chave* e *rotear por partição* — e ela é
invisível enquanto houver um processo só. `docs/processamento.md` explica o
particionamento; este documento mostra o que acontece sem o roteamento que o
acompanha.

### O que isso não invalida

A lógica da janela está certa: no cenário A ela agrupa as doze corretamente por tempo
de evento, e é isso que `test_janela_por_tempo_de_evento_agrupa_mesmo_com_atraso_de_rede`
prova. O que o cluster acrescenta é o requisito de plataforma que a Aula 15 descreve e
que este projeto não implementa: estado com chave, roteado de forma estável para o
mesmo consumidor, e persistido fora do processo. Um pipeline de fluxo sem isso é um
pipeline de fluxo de uma réplica só — ou seja, sem escala.

### Como reproduzir

```bash
make k8s-up
PODS=($(kubectl get pods -l app=pedidos --field-selector=status.phase=Running -o name))
# cenário A: 12 POSTs em ${PODS[0]}; cenário B: 12 POSTs alternando entre as 4
kubectl exec ${PODS[0]} -- python -c "..."   # /_admin/fraude/tentativa
kubectl exec <cada-pod> -- python -c "..."   # /_admin/fraude/contagem/<dispositivo>
```

## O resto do cluster, como nas aulas anteriores

- **Doze réplicas `Ready`** nos dois workers, com as duas sondas (`/saude`, `/pronto`).
- **A saga completa roda dentro do cluster**, pelo DNS do Kubernetes e com o token
  HMAC da Aula 12 assinado pelo `Secret` aleatório.
- **`emptyDir` + réplicas dividem o estado de banco** — ver
  `aula_13/docs/kubernetes-execucao.md`, seção 2, para a demonstração com o gateway.
- **O experimento de caos com `kubectl scale --replicas=0`** — ver
  `aula_14/docs/kubernetes-execucao.md`, e o defeito que ele encontrou.

O achado desta aula é de outra natureza: não é um Pod que cai nem um dado que se
divide, é uma **conclusão de negócio** que desaparece sem que nada acuse erro.
