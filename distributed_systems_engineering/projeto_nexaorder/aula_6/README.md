# Aula 6 — Particionamento, CAP e PACELC

**Videoaula correspondente:** Aula 6 — Particionamento, CAP e escalabilidade de dados.

## O que esta aula acrescentou ao projeto

- `services/estoque/app/particionamento.py` — `hash_simples` e `AnelConsistente`
  (hashing consistente com nós virtuais), com os números do roteiro reproduzidos em
  teste: hash simples redistribui ~100% das chaves ao mudar N; o anel consistente
  redistribui ~1/(N+1).
- `docs/particionamento-e-pacelc.md` — a matriz PACELC da NexaOrder: catálogo e
  leitura de estoque como PA/EL, reserva de estoque e pagamento como PC/EC.
- `docs/adr/0006-particionamento-nao-implementado-fisicamente.md` — por que a
  biblioteca existe e está testada, mas o estoque não é fisicamente fragmentado nesta
  aula (isso teria que esperar consenso e sagas prontos para lidar com a coordenação
  que exigiria).

## Por que a biblioteca não está "em uso" em nenhuma rota

Isto é deliberado, e documentado no ADR 0006 em vez de deixado como lacuna silenciosa.
O ganho pedagógico do hashing consistente está na matemática — mover ~10% em vez de
~100% — e essa matemática se prova inteiramente em testes, sem exigir uma segunda
instância física de `estoque`. A aplicação real da mesma biblioteca chega na Aula 10,
quando o tópico de eventos precisa decidir a partição de cada mensagem por
`pedido_id`.

## Roteiro de condução

1. Rode `test_hash_simples_redistribui_quase_tudo_ao_mudar_n` e
   `test_anel_consistente_move_aproximadamente_um_sobre_n_mais_um` lado a lado.
   A diferença entre os dois números é o argumento inteiro da aula.
2. Rode `test_nos_virtuais_reduzem_variancia_de_carga_entre_nos` e explique por que
   um único nó virtual por nó físico deixa a carga desigual — é pura geometria do
   anel, não sorte.
3. Abra `docs/particionamento-e-pacelc.md` e mostre a linha dupla do estoque: leitura
   é PA/EL, reserva é PC/EC. Pergunte por que o mesmo serviço aparece duas vezes com
   classificações opostas.
4. Feche com o ADR 0006 — nem toda técnica apresentada em aula precisa estar "em
   produção" no mesmo instante em que é ensinada; às vezes o correto é documentar o
   adiamento.

## Como rodar

```bash
make setup
make test        # 45 testes: 26 em pedidos, 19 em estoque
```

## Pergunta que fica em aberto

O anel consistente decide **onde** um dado mora. Ele não decide **quem manda** quando
duas réplicas discordam sobre o estado — essa é a pergunta da Aula 7: como um
conjunto de nós concorda sozinho sobre um líder, mesmo com falhas.

## Estado do projeto

```
docs/
  particionamento-e-pacelc.md                              [novo]
  adr/0006-particionamento-nao-implementado-fisicamente.md  [novo]
services/
  estoque/
    app/particionamento.py                    [novo]
    tests/test_particionamento.py             [novo]
```

45 testes (26 em pedidos, 19 em estoque).
