# Aula 15 — Processamento distribuído, edge e serverless

**Videoaula correspondente:** Aula 15 — Processamento distribuído, edge e serverless.

## O que esta aula acrescentou ao projeto

- **Um pipeline de detecção de fraude em fluxo**, o primeiro caso de uso real de
  processamento contínuo do projeto:
  - `services/pedidos/app/janela_evento.py` — janela por tempo de evento com marca
    d'água, pura (nunca lê o relógio).
  - `services/pedidos/app/eventos_dispositivo.py` — reaproveita o barramento da
    Aula 10 com uma nova chave de partição: `dispositivo_id`.
  - `POST /_admin/fraude/tentativa` + `GET /_admin/fraude/contagem/{id}` em
    `pedidos` — o pipeline conectado à API real, não só testado em isolamento.
- **`scripts/mapreduce.py`** — o lado lote: map/shuffle/reduce sobre um conjunto
  fechado, com reexecução de tarefa isolada sob falha (não do job inteiro).
- **`services/pedidos/app/faas.py`** — o efeito observável de inicialização a fria,
  quantificado contra o SLI de latência de 300ms que a Aula 13 já havia definido.
- **`services/pedidos/app/triagem_de_fraude.py`** — a resposta madura à pausa de
  reflexão do roteiro: triagem local para sinais simples, avaliação central para o
  que exige contexto histórico.
- `docs/processamento.md` e `docs/adr/0015-fraude-simulada-sem-plataforma-real.md`.

## A demonstração central: tempo de evento vs. tempo de processamento

`test_janela_por_tempo_de_evento_agrupa_mesmo_com_atraso_de_rede` reproduz o exemplo
exato do roteiro: dez tentativas em dez segundos no mesmo dispositivo, cinco
atrasadas pela rede em dois minutos.

- Por **tempo de evento**: as dez são reconhecidas como um único padrão.
- Por **tempo de processamento**: aparecem como dois grupos de cinco, em momentos
  diferentes — o alerta nunca dispara.

Mesmos dados, base de tempo diferente, conclusão oposta — o ponto central da aula,
provado com uma asserção lado a lado.

## Onde o cold start realmente importa

```python
# 400ms de inicialização a frio + 20ms de execução = 420ms
# > 300ms, o limite de SLI de latência do exemplo da Aula 13
```

`test_cold_start_no_caminho_sincrono_estoura_o_sli_de_latencia_da_aula_13` conecta a
FaaS desta aula ao orçamento de erro da Aula 13 com um número, não uma afirmação
solta.

## O pipeline de fluxo com quatro réplicas

`docs/kubernetes-execucao.md` roda esta aula em um cluster kind: as mesmas doze
tentativas que, em um processo, somam doze na janela viram **três em cada uma das
quatro réplicas** quando distribuídas por um `Service`. Nenhum erro em lugar nenhum, e
o alerta de fraude some. As quatro réplicas calculam a mesma partição para a mesma
chave — falta o roteamento que um framework de fluxo real acrescenta, não o cálculo.

## Roteiro de condução

1. Rode `test_janela_por_tempo_de_evento_agrupa_mesmo_com_atraso_de_rede` — narre a
   divergência entre as duas contagens sobre os mesmos dados.
2. Rode `POST /_admin/fraude/tentativa` algumas vezes via `/docs` e confirme a
   contagem em `GET /_admin/fraude/contagem/{id}` — o pipeline de verdade, rodando.
3. Rode `scripts/test_mapreduce.py::test_map_tolerante_a_falhas_reexecuta_so_a_tarefa_que_falhou`
   — mostre que a tarefa estável nunca é retocada.
4. Feche com `test_cold_start_no_caminho_sincrono_estoura_o_sli_de_latencia_da_aula_13`
   — a FaaS de uma aula quebrando o SLO de outra, quantificado.

## Como rodar

```bash
make setup
make test          # 208 testes: 108 pedidos, 49 estoque, 8 pagamento, 7 expedicao, 6 gateway, 30 scripts
make verificar      # fronteiras + instabilidade (Aula 9)
make validar-k8s    # os cinco manifests
make up             # contêineres (Docker ou Podman) com os cinco serviços de aplicação
make k8s-up         # cluster Kubernetes local (kind) com os manifests aplicados
make k8s-status     # pods, services e HPA do cluster
make k8s-down       # destrói o cluster
```

## Pergunta que fica em aberto

Este projeto agora cobre modelagem, arquitetura, código, tecnologia, replicação,
particionamento, consenso, sagas, limites de domínio, eventos, contêineres,
segurança, observabilidade, testes/caos e processamento — dezesseis aulas de
decisões, cada uma com código real e testado. A Aula 16 não acrescenta mecanismo
novo: reúne tudo isso em uma defesa arquitetural coerente.

## Estado do projeto

```
docs/
  processamento.md                                        [novo]
  kubernetes-execucao.md                                  [novo: o pipeline em 4 réplicas]
  adr/0015-fraude-simulada-sem-plataforma-real.md         [novo]
  adr/0011-manifests-validados-nao-aplicados.md           [alterado: os manifests foram aplicados]
k8s/kind/cluster.yaml + scripts/deploy_kind.sh             [novo: cluster kind de três nós]
services/pedidos/app/janela_evento.py                       [novo]
services/pedidos/app/eventos_dispositivo.py                  [novo]
services/pedidos/app/faas.py                                 [novo]
services/pedidos/app/triagem_de_fraude.py                    [novo]
services/pedidos/app/models.py                               [alterado: TentativaDePagamentoRequest]
services/pedidos/app/main.py                                 [alterado: pipeline de fraude + 2 endpoints]
services/pedidos/tests/test_janela_evento.py                 [novo: 6 testes]
services/pedidos/tests/test_eventos_dispositivo.py           [novo: 3 testes]
services/pedidos/tests/test_faas.py                          [novo: 6 testes]
services/pedidos/tests/test_triagem_de_fraude.py             [novo: 5 testes]
services/pedidos/tests/test_fraude_endpoint.py                [novo: 3 testes]
scripts/mapreduce.py + test                                   [novo: 4 testes]
```

208 testes, lote e fluxo lado a lado sobre o mesmo problema de negócio, tempo de
evento provado divergente de tempo de processamento com os números exatos do
roteiro.
