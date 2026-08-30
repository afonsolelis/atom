# Execução real dos manifests em um cluster local (kind) — Aula 16

O ADR 0011 (Aula 11) registrou que os manifests tinham sido validados
estruturalmente, mas nunca aplicados. **Isso deixou de ser verdade**: os cinco
manifests desta aula — mais o `Secret` da Aula 12 — subiram em um cluster kind de
três nós, e a plataforma inteira rodou dentro dele. Este documento é o registro
consolidado da Unidade 4 em cluster: reúne o que cada aula da unidade encontrou e o
que isso muda na defesa arquitetural de `docs/defesa-arquitetural.md`.

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

## O estado final, medido

```
NAME                       READY  STATUS   NODE
estoque-844d4bff6f-h4jx9   1/1    Running  nexaorder-worker2
estoque-844d4bff6f-kt466   1/1    Running  nexaorder-worker
expedicao-88fc47946-8ngp8  1/1    Running  nexaorder-worker
expedicao-88fc47946-n4564  1/1    Running  nexaorder-worker2
gateway-64c7dc7747-8vzl6   1/1    Running  nexaorder-worker2
gateway-64c7dc7747-v76gq   1/1    Running  nexaorder-worker
pagamento-744d874764-jhznx 1/1    Running  nexaorder-worker
pagamento-744d874764-qmcbt 1/1    Running  nexaorder-worker2
pedidos-d9c676f5d-2dnkt    1/1    Running  nexaorder-worker2
pedidos-d9c676f5d-6qqxb    1/1    Running  nexaorder-worker
pedidos-d9c676f5d-lkg74    1/1    Running  nexaorder-worker
pedidos-d9c676f5d-lwbst    1/1    Running  nexaorder-worker2

NAME     REFERENCE            TARGETS      MINPODS  MAXPODS  REPLICAS
pedidos  Deployment/pedidos   cpu: 2%/60%  2        10       4
```

Doze réplicas `Ready`, distribuídas pelos dois workers, HPA lendo CPU real do
metrics-server. A saga completa, executada de dentro do cluster:

```json
{"sucesso": true, "estado_final": "EXPEDIDO", "falhou_em": null, "compensacoes": []}
```

`pedidos` alcança os outros três serviços pelo DNS do Kubernetes (`http://estoque:8000`),
sem nenhum endereço IP em manifesto, com o token HMAC da Aula 12 assinado pelo segredo
aleatório que `deploy_kind.sh` cria no momento da implantação. O gateway responde em
`http://localhost:8080/saude` pelo NodePort.

## O que a Unidade 4 encontrou em cluster

Cada aula desta unidade rodou no cluster e encontrou uma coisa diferente. As três
juntas formam a lista de prontidão que a seção 4 de `docs/defesa-arquitetural.md`
chama de "o que precisaria mudar antes de uma implantação real" — agora com evidência,
não com previsão.

| Aula | O que o cluster revelou | Onde está registrado |
|---|---|---|
| 13 | Um trace, dez spans, sete Pods: a propagação funciona, a leitura não existe. Nenhuma consulta devolve o trace inteiro. | `aula_13/docs/kubernetes-execucao.md` |
| 13 | `emptyDir` + réplicas: o 404 do gateway não é aleatório por requisição, é fixo por conexão. 24 requisições seguidas ao mesmo pedido, 24 erros — até o gateway reabrir o pool. | idem, seção 2 |
| 14 | **Um defeito real**: um provedor fora do ar recusa conexão, não dá timeout. `httpx.ConnectError` escapava do cliente resiliente, da saga e do disjuntor. Três compras devolveram 500 e vazaram estoque. Corrigido. | `aula_14/docs/kubernetes-execucao.md` |
| 15 | A janela por tempo de evento não sobrevive a quatro réplicas: doze tentativas viram três em cada Pod, e o alerta de fraude some sem nenhum erro. | `aula_15/docs/kubernetes-execucao.md` |

## O que isso acrescenta à defesa arquitetural

A seção 4 de `docs/defesa-arquitetural.md` listava, por análise, os pontos únicos de
falha que este projeto ainda não mitiga. O cluster confirmou os três principais e
mudou o tom de um deles:

- **Banco por serviço (SQLite em `emptyDir`)** — confirmado, e pior do que a análise
  sugeria: não é só "não há réplica promovível", é que *ter mais de uma réplica já
  quebra a leitura*, de forma determinística e silenciosa.
- **Barramento de eventos em memória** — confirmado pela Aula 15 sob outra forma: não
  é só que ele não sobrevive a um reinício; ele não sobrevive a uma segunda réplica.
- **Coletor de observabilidade** — a análise dizia "não há um SPOF porque não há
  coletor". O cluster mostra o custo dessa ausência: dez fragmentos de um trace em
  sete Pods, sem consulta que os junte.

E acrescenta um item que a análise não tinha, porque nenhum teste o alcançava: **o
disjuntor não abria sob indisponibilidade total**. Uma defesa arquitetural que
afirmasse "temos disjuntor, retry e compensação" estaria, até a Aula 14, dizendo algo
falso sobre o modo de falha mais comum em produção. É o argumento do slide de
encerramento em forma concreta: decisão arquitetural é hipótese verificável, e
verificar custa infraestrutura.

## Reproduzir a unidade inteira

```bash
cd aula_13 && make k8s-up   # traces por Pod, 404 fixo do gateway
cd aula_14 && make k8s-up   # experimento de caos com kubectl scale --replicas=0
cd aula_15 && make k8s-up   # janela de fraude com 4 réplicas
cd aula_16 && make k8s-up   # a plataforma completa
make k8s-down               # em qualquer uma
```

Uma aula por vez: as quatro usam o mesmo nome de cluster (`nexaorder`) e a mesma porta
8080 do host. `make k8s-down` antes de trocar de aula.
