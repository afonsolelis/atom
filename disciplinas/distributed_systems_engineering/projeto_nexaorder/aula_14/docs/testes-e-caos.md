# Testes, resiliência distribuída e engenharia do caos — Unidade 4, Aula 14

## O incidente que esta aula corrige

Até a Aula 13, o disjuntor, o retry com backoff e a saga com compensação existiam e
tinham testes unitários — mas nunca haviam sido exercitados por um cenário que
simulasse a falha real que motivou sua criação, do jeito que aconteceria em produção:
uma indisponibilidade externa sustentada, sob tráfego concorrente. Um mecanismo de
resiliência nunca exercitado é uma hipótese, não uma proteção — exatamente o
diagnóstico do roteiro sobre o incidente da promoção de fim de ano.

## A pirâmide de testes deste projeto

Este projeto já seguia, sem o rótulo, a forma da pirâmide:

- **Base — unitários**: `test_lamport.py`, `test_resiliencia.py`, `test_particionamento.py`,
  `test_consenso.py`, `test_saga.py`, `test_barramento.py`, `test_seguranca.py`,
  `test_observabilidade.py` e outros — funções e classes isoladas, em milissegundos,
  sem rede nem banco real.
- **Meio — integração**: `test_saldo_e_reservas.py`, `test_pagamento.py`, cada
  `test_sondas.py` — um serviço e seu próprio banco SQLite, via `TestClient`.
- **Topo — ponta a ponta**: `test_saga_integracao.py`, `test_gateway.py` — quatro (ou
  cinco) aplicações FastAPI reais, conectadas por `httpx.ASGITransport`, sem Docker.

O topo é deliberadamente pequeno: poucos arquivos, concentrados nos fluxos mais
críticos (a saga completa, a composição do gateway), não uma tentativa de cobrir tudo
com o tipo de teste mais caro — a recomendação exata do roteiro.

## Testes de contrato: mais baratos que ponta a ponta

`services/pedidos/tests/contratos.py` declara, por provedor, só os campos que o
código de `pedidos` efetivamente lê (`app/saga.py`) — não o esquema inteiro de cada
serviço. `test_contratos.py` verifica cada contrato contra a aplicação real do
provedor, sem precisar da saga inteira em execução, e prova que o mecanismo detecta
de verdade um campo removido (a mudança silenciosa de nome de campo que a Aula 10 já
havia discutido a propósito de evolução de esquema). Ver
`docs/adr/0014-testes-de-contrato-sem-broker.md` para o que não é reproduzido (um
broker de contratos real, com dois pipelines de CI).

## Carga, estresse e duração: três perguntas diferentes

- **Carga** (`services/estoque/tests/test_desempenho.py`) — 40 requisições reais a
  `/reservas`, dentro da capacidade de 50 do balde de fichas (Aula 12): o sistema
  atende ao esperado sem erro e com latência aceitável.
- **Estresse** — este projeto já tinha um, sem o rótulo, desde a Aula 12:
  `services/estoque/tests/test_seguranca.py::test_limitador_de_taxa_protege_reservas_de_verdade_via_http`
  aplica 90 requisições reais — acima da capacidade — e prova que o sistema falha de
  forma controlada (`429`, não um travamento ou um `500`). Não duplicamos esse teste
  aqui; nomeá-lo corretamente já é o ponto — as três perguntas do roteiro (esperado,
  limite, duração) frequentemente já têm resposta em testes que existem por outro
  motivo, só faltando o vocabulário certo para reconhecê-los.
- **Duração (soak)** — este projeto não roda por horas de verdade, então o soak é
  reinterpretado como o que ele realmente detecta: crescimento sem limite de uma
  estrutura interna sob volume sustentado, não sob tempo decorrido.
  `test_disjuntor_janela_nao_cresce_sem_limite_sob_volume_sustentado` (5.000 chamadas)
  e `test_contador_com_dimensoes_de_baixa_cardinalidade_nao_cresce_sem_limite_sob_volume`
  (5.000 incrementos) prova isso para a janela do disjuntor (Aula 4) e para o contador
  de métricas (Aula 13) — as duas estruturas deste projeto mais parecidas com o
  vazamento de memória gradual que o roteiro descreve.

## O experimento de caos

`test_experimento_de_caos_indisponibilidade_total_do_pagamento`, em
`services/pedidos/tests/test_saga_integracao.py`, é um experimento de verdade, com as
cinco salvaguardas do cartão do roteiro:

| Campo | Valor neste experimento |
|---|---|
| Hipótese de estado estável | Sob indisponibilidade total do pagamento, nenhum pedido fica em estado inconsistente — todos terminam totalmente compensados, e o disjuntor abre |
| Perturbação | `falhar_percentual=100` em pagamento (a alavanca de injeção de falha da Aula 4/5) |
| Métricas de controle | `estado_final`/`compensacoes` de cada pedido; estado do disjuntor via `GET /saude` |
| Raio de impacto | Ambiente de teste isolado, zero tráfego real |
| Critério de interrupção | Kill switch: `falhar_percentual` de volta a 0 |

**Um desvio deliberado do número do roteiro, e por quê.** O roteiro usa, no exemplo
numérico, "conclusão não deve cair abaixo de 90%" como critério de sucesso durante a
perturbação. Esse número presume um sistema com caminho de pagamento degradado (fila,
reprocessamento posterior) — este projeto não implementa isso: sob falha total do
pagamento, sem fallback, a saga rejeita e compensa, e 0% de conclusão é o resultado
**correto**, não uma falha do experimento. A hipótese que este experimento de fato
testa e confirma é outra, mais adequada ao que este projeto realmente promete:
nenhum pedido fica preso, e o disjuntor protege ativamente (a última tentativa antes
do kill switch falha em menos de 50 ms, sem tocar a rede — não é só eventualmente
protegido, é protegido rápido). O experimento também prova a recuperação: depois do
kill switch, um novo pedido conclui por completo.

Este é, ele mesmo, um exemplo do que o roteiro descreve como o valor de um
experimento de caos: um resultado que uma leitura do código não teria antecipado — a
diferença entre a hipótese "de manual" e a hipótese que este sistema específico
realmente sustenta.

## Por que a cadeia degrada mais do que qualquer serviço isolado

`scripts/disponibilidade_em_cadeia.py` reproduz o exemplo numérico do roteiro: quatro
serviços de 99,9% de disponibilidade, em cadeia sequencial sem tolerância a falha
parcial, compõem ~99,6% — quase quatro vezes mais indisponibilidade do que qualquer
componente isolado. `pedidos → estoque, pagamento, expedição` é exatamente essa
cadeia. É por isso que disjuntor, compensação e processamento assíncrono não são
refinamento opcional neste projeto — são o que evita que a composição de serviços
saudáveis produza um fluxo pior do que qualquer um deles.

## A segunda perturbação: o provedor que não está lá

`falhar_percentual=100` produz um provedor que **responde com erro**. Existe um modo
de falha diferente e mais comum em produção: o provedor que **não está no ar** — o
processo caiu, o Deployment foi a zero réplicas, o Service não tem endpoint. Quem
chama não recebe erro nem timeout: recebe conexão recusada.

Aplicando essa perturbação pelo próprio Kubernetes
(`kubectl scale deployment pagamento --replicas=0`) contra o estágio da Aula 13, o
experimento encontrou um defeito real, e não uma confirmação:

```
saga 1 -> HTTP 500 | estado do pedido: RECEBIDO
saga 2 -> HTTP 500 | estado do pedido: RECEBIDO
saga 3 -> HTTP 500 | estado do pedido: RECEBIDO
/saude: {'disjuntor_pagamento': 'fechado', ...}
saldo de estoque: 99 → 96
```

A saga não compensou, o disjuntor não abriu, e três reservas de estoque ficaram
penduradas. A causa: `app/resiliencia.py` e `app/main.py` capturavam
`httpx.TimeoutException`, e `httpx.ConnectError` não é subclasse dela — a exceção
escapava do cliente resiliente (sem retentativa, sem contar para o disjuntor), escapava
das etapas da saga (sem virar `EtapaFalhou`) e virava erro 500.

A correção — capturar `httpx.TransportError`, superclasse comum de timeout e de erro
de conexão — está no código desta aula, com
`test_experimento_de_caos_pagamento_fora_do_ar_tambem_compensa` como regressão. Depois
dela, nove sagas seguidas sob indisponibilidade total compensam todas, o disjuntor abre
na sétima (a janela é de 20 chamadas, e cada saga gasta 3) e a proteção passa a custar
13 ms em vez de 1.780 ms. O registro completo está em `docs/kubernetes-execucao.md`.

**Este é o argumento desta aula em forma de fato.** Nenhum dos 180 testes anteriores
pegava o defeito, e não por descuido: todos usavam a única alavanca de falha que o
projeto tinha, e essa alavanca produz um provedor que responde. Um mecanismo de
resiliência nunca exercitado contra o modo de falha certo continua sendo uma hipótese
— mesmo com cobertura de teste alta.

## Postmortem sem culpabilização

Este projeto não tem um incidente de produção real para postmortemizar — mas o
padrão de "por quê" sucessivos se aplica ao próprio processo de construção: por que o
disjuntor de pagamento nunca havia sido exercitado sob falha real antes desta aula?
Porque testá-lo exigia orquestrar quatro serviços reais e uma falha determinística —
o mesmo custo que a Aula 14 descreve como a razão do topo estreito da pirâmide. A
mudança sistêmica não é "escrever mais um teste": é o que esta aula formaliza —
reconhecer que mecanismos de resiliência exigem uma categoria própria de teste,
diferente de unitário e de integração comum.

## Decisão registrada

Ver `docs/adr/0014-testes-de-contrato-sem-broker.md`.
