# ADR 0010 — Barramento de eventos em memória, sem broker real integrado

- **Status:** aceito
- **Data:** correspondente à Unidade 3, Aula 10

## Contexto

A Aula 10 pede tópicos, partições, grupos de consumidores e semânticas de entrega.
Integrar um broker real (Redpanda ou Kafka) exigiria um cliente Python assíncrono
(`aiokafka` ou equivalente), um container de broker no `docker-compose.yml`, e
validação em um ambiente com Docker disponível — indisponível neste ambiente de
desenvolvimento (ver `docs/adr/0003-stack-tecnologica.md`, que já registrava esse
limite para o Compose desde a Aula 4).

## Decisão

Implementar `Topico`, `escolher_particao` e `GrupoConsumidores` em memória, dentro do
processo de `pedidos`, sem adicionar um serviço de broker ao `docker-compose.yml`.

## Por quê

Um `docker-compose.yml` com um serviço Redpanda sem nenhum código cliente conectado
a ele criaria a aparência de integração sem integração real — exatamente o tipo de
lacuna silenciosa que as ADRs anteriores (0006, 0007) evitaram documentando
explicitamente. Preferimos declarar o limite a fingir que ele não existe.

A interface pública do módulo (`publicar`, `ler_particao`, `GrupoConsumidores`) foi
desenhada para que a troca por um cliente Kafka real seja uma substituição de
implementação, não uma reescrita de quem a usa — `publicador.py` e o endpoint de
consumo em `main.py` não precisariam mudar de assinatura.

## Compromisso aceito

O projeto não demonstra, em execução real, comportamentos que só um broker de
verdade produz: reinício do processo preservando o tópico, replicação do broker
entre múltiplos nós, ou latência de rede real entre produtor e consumidor. Esses
comportamentos são descritos em prosa em `docs/arquitetura-eventos.md` e no roteiro
da Aula 10, mas não são executáveis neste repositório.

## Evidência

`tests/test_barramento.py` (9 testes) prova ordenação por partição, paralelismo de
grupos de consumidores, independência entre grupos e rebalanceamento.
`tests/test_publicador.py` prova que o publicador fecha o padrão outbox da Aula 8.
`tests/test_evolucao_esquema.py` prova as regras de compatibilidade de esquema.
