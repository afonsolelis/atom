# Particionamento, CAP e PACELC — Unidade 2, Aula 6

## Particionamento na NexaOrder

`services/estoque/app/particionamento.py` implementa e testa duas estratégias:

- `hash_simples(chave, N)` — módulo N. Simples, mas qualquer mudança em N reatribui
  quase todas as chaves (`tests/test_particionamento.py::test_hash_simples_redistribui_quase_tudo_ao_mudar_n`).
- `AnelConsistente` — hashing consistente com nós virtuais. Adicionar um nó a um anel
  de 9 move aproximadamente 1/(9+1) = 10% das chaves
  (`test_anel_consistente_move_aproximadamente_um_sobre_n_mais_um`), contra
  aproximadamente 100% do hash simples.

**Onde isso é usado de verdade no projeto:** ainda em lugar nenhum, nesta aula. A
biblioteca está pronta e testada, mas o projeto não fragmenta fisicamente o estoque em
múltiplas instâncias — isso exigiria múltiplos bancos de dados coordenados, o que
o escopo deste projeto didático não cobre. O uso real chega na Aula 10: o tópico de
eventos é particionado por `pedido_id`, e é o mesmo raciocínio de hashing consistente
que decide para qual partição cada evento vai.

## O teorema CAP aplicado à NexaOrder

Durante uma partição de rede, um sistema replicado não pode oferecer simultaneamente
consistência e disponibilidade completas. A escolha relevante é entre C e A, e só
durante o período em que a partição persiste.

| Dado | Escolha sob partição | Por quê |
|------|------------------------|---------|
| Reserva de estoque | **CP** | melhor recusar a operação do que vender duas vezes o mesmo item |
| Autorização de pagamento | **CP** | maior risco financeiro e regulatório do sistema |
| Leitura informativa de saldo | **AP** | melhor mostrar um número possivelmente desatualizado do que uma página de erro |
| Catálogo (não implementado como serviço) | **AP** | mesma lógica da leitura de estoque |

Note que **estoque aparece duas vezes**, com escolhas opostas — a mesma lição da
Aula 5 (consistência é por dado, não por serviço), agora com outro vocabulário.

## PACELC — o compromisso que vale todos os dias

O CAP descreve apenas o comportamento sob partição, e partições são raras. O PACELC
estende a análise: **P**artição → escolha entre **A** e **C**; **E**lse (fora de
partição) → escolha entre **L**atência e **C**onsistência.

| Dado | Classificação PACELC | Leitura |
|------|------------------------|---------|
| Catálogo | **PA/EL** | sob partição prioriza disponibilidade; fora dela, prioriza latência |
| Reserva de estoque | **PC/EC** | sempre prioriza consistência, com ou sem partição |
| Leitura informativa de estoque | **PA/EL** | mesmo raciocínio do catálogo |
| Pagamento | **PC/EC** | prioriza consistência sempre, mesmo ao custo de recusar ou atrasar |

O código já reflete isso, mesmo sem "partição de rede" simulada: `GET
/saldo/{sku}?consistencia=eventual` é a implementação concreta de **EL** (latência
sobre consistência, fora de qualquer partição) para a leitura informativa; `POST
/reservas`, sempre contra o líder, é a implementação concreta de **EC** para a
decisão de vender.

## Decisão registrada

Ver `docs/adr/0006-particionamento-nao-implementado-fisicamente.md`.
