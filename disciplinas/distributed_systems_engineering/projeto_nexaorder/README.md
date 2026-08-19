# Projeto NexaOrder — construção incremental

Este diretório contém o projeto prático da disciplina **Distributed Systems Engineering**,
construído em dezesseis incrementos, um por videoaula.

## Como usar em aula

Cada pasta `aula_N/` é **o projeto inteiro naquele estágio**, não apenas o que mudou.
Para conduzir a aula, abra a pasta correspondente, leia o `README.md` dela — que descreve
o que foi acrescentado, por quê, e traz um roteiro de condução sugerido — e execute o
que já existir ali.

```bash
cd aula_7
cat README.md          # o que esta aula acrescentou
make setup && make test   # sobe o que já existe neste estágio
```

A partir da Aula 3 há código executável. A partir da Aula 4 há `compose` — e o mesmo
`make up` sobe a stack tanto em Docker quanto em Podman (ver abaixo). Na Aula 12 a
plataforma já sobe com identidade e autorização entre os cinco serviços; na Aula 16,
com os cinco serviços, observabilidade, resiliência testada sob caos real e um
pipeline de fluxo, junto de uma defesa arquitetural completa.

## O que cada aula acrescenta

| Aula | Tema da videoaula | Incremento no projeto |
|------|-------------------|------------------------|
| 1 | Fundamentos e decisão de distribuir | Modelo de domínio, dimensionamento (`N = ⌈λ/(c·u)⌉`), ADR 0001 |
| 2 | Comunicação entre processos | Diagramas em Mermaid, contratos de API e de evento, ADR 0002 |
| 3 | Concorrência, relógios e ordenação | Primeiro serviço em código: `pedidos`, com relógio de Lamport e correlação de trace_id |
| 4 | Modelos de falha e recuperação | ADR de stack (Python/FastAPI/SQLite), disjuntor + retry + backoff, primeiro `compose` |
| 5 | Replicação e consistência | Réplica de leitura com atraso de 150 ms; consistência forte na reserva, eventual no catálogo |
| 6 | Particionamento, CAP e PACELC | Hashing consistente, anel de partições, matriz PACELC da NexaOrder |
| 7 | Consenso e eleição de líder | Simulação determinística de eleição, replicação de log e partição de rede (estilo Raft) |
| 8 | Sagas e idempotência | Serviços `pagamento` e `expedicao`; saga orquestrada com compensação; outbox/inbox |
| 9 | Limites de domínio | Serviço `gateway` (sem lógica de negócio); `verificar_fronteiras.py`; instabilidade (I = Ce/(Ca+Ce)) |
| 10 | Arquitetura orientada a eventos | Barramento em memória com tópicos/partições/grupos de consumidores; publicador de outbox |
| 11 | Contêineres e Kubernetes | Sonda de prontidão; manifests Deployment/Service/HPA; validador estrutural de manifests |
| 12 | Segurança entre serviços | Identidade por token HMAC, autorização por menor privilégio, limitador de taxa (balde de fichas) |
| 13 | Observabilidade | Logs estruturados, métricas com proteção de cardinalidade, tracing com spans reais aninhados |
| 14 | Testes e engenharia do caos | Testes de contrato, de carga, de duração (soak); experimento de caos determinístico com kill switch |
| 15 | Processamento em fluxo e lote | Janela por tempo de evento com marca d'água; MapReduce; custo de cold start; triagem local/central |
| 16 | Projeto integrado | Defesa arquitetural: SPOF, RPO/RTO, retrospectiva das 16 ADRs, critérios de aceite executáveis |

## Fio condutor

O sistema é a **NexaOrder**, a mesma plataforma fictícia de pedidos, pagamentos e
expedição usada nos roteiros das videoaulas. Os números que aparecem no código são os
mesmos números das aulas: 800 requisições/s no pico (Aula 1), 150 ms de atraso de
réplica (Aula 5), 8 partições para o tópico de pedidos (Aula 10), 50% de limite de
falhas no disjuntor (Aula 4), 5.000/750 → 7 partições no pipeline de fraude (Aula 15),
e "sete noves" de disponibilidade com três réplicas independentes (Aula 16). O aluno
reencontra no terminal o número que viu no slide — isso é deliberado.

## Honestidade sobre o que é real e o que é simplificado

Este projeto não tem Docker, Kubernetes, um broker de eventos ou um coletor de
observabilidade reais neste ambiente de desenvolvimento. Em vez de fingir essa
integração, cada limite está documentado explicitamente em `docs/adr/000N-*.md` de
cada aula — 16 ADRs ao todo, cada um seguindo o formato contexto/decisão/porquê/
compromisso aceito/evidência. `aula_16/docs/defesa-arquitetural.md` reúne essa
disciplina em uma retrospectiva única, incluindo uma análise de pontos únicos de
falha que nomeia honestamente o que este projeto ainda não mitiga (réplica de banco,
RPO/RTO, um coletor central) — não só o que já foi resolvido.

## Como validar qualquer aula

Todas as aulas seguem o mesmo fluxo, a partir da própria pasta:

```bash
make setup              # cria um venv por serviço + um para scripts/
make test                # roda a suíte completa de testes
make verificar            # fronteiras de domínio + instabilidade (a partir da Aula 9)
make validar-k8s          # manifests Kubernetes (a partir da Aula 11)
make criterios-de-aceite  # identidade + observabilidade + testes, por serviço (Aula 16)
make up                   # contêineres: Docker ou Podman (a partir da Aula 4)
```

Nem todo alvo existe em toda aula — cada `README.md` de aula lista os que se aplicam
naquele estágio.

## Docker ou Podman

Nenhum alvo do `Makefile` chama `docker` diretamente. O motor de contêiner é detectado
na hora do `make up`, nesta ordem: `docker compose`, `podman compose`, `podman-compose`,
`docker-compose`. Quem tem Docker instalado não percebe diferença; quem usa Podman
roda os mesmos comandos, sem editar nada.

```bash
make up                              # detecta o motor disponível e sobe a stack
make up COMPOSE="podman-compose"     # força um motor específico
make verificar-compose               # só mostra qual motor seria usado
```

Se nenhum dos quatro for encontrado, `make up` para com uma mensagem explicando o que
instalar, em vez de falhar com "command not found".

Os `Dockerfile` e os `docker-compose.yml` são padrão OCI e não têm nada específico de
Docker — o Podman os lê sem conversão. A stack da Aula 5 foi validada ponta a ponta em
Podman 5.8 com podman-compose 1.6, incluindo `healthcheck`, `depends_on:
service_healthy`, volume nomeado e a janela de leitura obsoleta de 150 ms observada por
`curl`.
