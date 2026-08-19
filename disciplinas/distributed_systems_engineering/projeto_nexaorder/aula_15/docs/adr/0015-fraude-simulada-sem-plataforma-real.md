# ADR 0015 — Detecção de fraude simulada, sem framework de fluxo, FaaS ou CDN reais

- **Status:** aceito
- **Data:** correspondente à Unidade 4, Aula 15

## Contexto

A Aula 15 introduz quatro peças de infraestrutura que este sandbox não tem como
executar de verdade: um framework de processamento em fluxo com particionamento
distribuído (Flink, Kafka Streams), um cluster MapReduce real (Spark, Hadoop), uma
plataforma FaaS com provisionamento elástico real (Lambda, Cloud Functions) e pontos
de borda geograficamente distribuídos (uma CDN com compute). Nenhum desses quatro
tem como ser executado ou validado neste ambiente de desenvolvimento — mesma classe
de limite dos ADRs 0003, 0007, 0010 e 0011.

## Decisão

Implementar os mecanismos centrais de cada peça como módulos Python reais e
testados, sem a infraestrutura por trás:

- `services/pedidos/app/janela_evento.py` — janela por tempo de evento com marca
  d'água, nunca lendo o relógio (todo tempo é passado pelo chamador).
- `services/pedidos/app/eventos_dispositivo.py` — reaproveita o barramento em
  memória da Aula 10 (`docs/adr/0010-barramento-em-memoria.md`), com uma chave de
  partição diferente.
- `scripts/mapreduce.py` — as três fases (map, shuffle, reduce) sobre dados em
  memória, com reexecução de tarefa isolada.
- `services/pedidos/app/faas.py` — o efeito observável de inicialização a frio
  (latência), sem simular provisionamento real.
- `services/pedidos/app/triagem_de_fraude.py` — a decisão local-vs-central, sem
  pontos de borda geograficamente distribuídos de verdade.

## Por quê

O valor pedagógico da aula está nos MECANISMOS e nas DECISÕES de arquitetura — quando
usar tempo de evento em vez de processamento, como dimensionar partições, onde o
custo de inicialização a frio importa, o que fica na borda e o que exige o centro —
não na operação de um cluster Flink ou de uma função Lambda real. Cada módulo aqui é
honesto sobre o que mede: `janela_evento.py` mede a lógica de agrupamento por tempo
de evento (real, testável, correta), não a entrega de eventos por uma rede real.
`faas.py` mede o efeito da inicialização a frio sobre a latência (o que importa para
a decisão de onde usar FaaS), não o provisionamento de contêineres.

## Compromisso aceito

Não é demonstrado: um cluster de processamento distribuído real (com tarefas
paralelas em nós diferentes, rede real na fase de shuffle), uma plataforma FaaS
elástica de verdade, nem pontos de borda geograficamente distintos com latência de
rede real entre eles. O que este projeto prova é a lógica que decidiria o
comportamento correto nesses sistemas reais, não a operação deles.

O pipeline de fraude também não está conectado à saga de compra (`app/saga.py`):
`POST /_admin/fraude/tentativa` é um endpoint de demonstração, no mesmo espírito de
`POST /_admin/publicar-eventos` (Aula 10) — prova que o mecanismo funciona de ponta a
ponta dentro do processo, sem se comprometer com onde, na jornada real de checkout,
uma tentativa seria de fato reportada (produção exigiria instrumentar o ponto de
entrada do gateway de pagamento, fora do escopo desta aula).

## Evidência

`services/pedidos/tests/test_janela_evento.py` reproduz o exemplo exato do roteiro
(dez tentativas, cinco atrasadas em dois minutos) e prova a divergência entre tempo
de evento e de processamento. `test_eventos_dispositivo.py` reproduz o dimensionamento
de partições (5.000/750 → 7). `scripts/test_mapreduce.py` prova as três fases e a
reexecução de uma tarefa isolada. `test_faas.py` prova que um cold start no caminho
síncrono do checkout ultrapassaria o SLI de 300ms da Aula 13. `test_triagem_de_fraude.py`
prova a resposta madura da pausa de reflexão. `test_fraude_endpoint.py` prova que o
pipeline está de fato acessível pela API, não só testado em isolamento.
