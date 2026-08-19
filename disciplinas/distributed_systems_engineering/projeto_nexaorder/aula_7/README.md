# Aula 7 — Consenso e eleição de líder

**Videoaula correspondente:** Aula 7 — Consenso, eleição de líder e Raft.

## O que esta aula acrescentou ao projeto

- `services/estoque/app/consenso.py` — uma simulação determinística das regras
  centrais do Raft: `tolerancia_a_falhas(n)`, `ClusterRaft` com eleição por maioria,
  termos crescentes e replicação de log confirmada por maioria.
- `docs/consenso.md` — o que está implementado fielmente e o que é simplificação
  deliberada (sem rede real, sem tempo real, sem persistência).
- `docs/adr/0007-consenso-simulado-nao-embutido.md` — por que simular as regras em
  vez de embutir um Raft de produção.
- `tests/test_consenso.py` — 12 testes, incluindo a reprodução exata do incidente da
  situação-problema da aula: dois líderes simultâneos por promoção manual, e como a
  eleição por maioria torna isso estruturalmente impossível.

## O experimento central: por que número par não ajuda

```python
from app.consenso import tolerancia_a_falhas

tolerancia_a_falhas(5)  # 2
tolerancia_a_falhas(6)  # 2 — o mesmo! seis nós custam mais e não toleram mais falhas
tolerancia_a_falhas(7)  # 3 — só o sétimo nó (o próximo ímpar) aumenta a tolerância
```

## O experimento central: partição e segurança

`test_apos_curar_particao_lider_antigo_nao_recupera_maioria_sozinho` é o teste mais
importante da suíte: mostra que, mesmo depois que a rede volta a funcionar, um líder
antigo (em termo desatualizado) não consegue mais confirmar entradas, porque a maioria
já elegeu um líder novo em um termo mais alto. É a prova de que a eleição por maioria
resolve, de verdade, o incidente de dois líderes simultâneos da abertura da aula.

## Roteiro de condução

1. Rode `test_6_nos_nao_tolera_mais_falhas_que_5` e peça à turma para explicar por que
   isso não é um detalhe de implementação — é geometria da maioria.
2. Rode `test_grupo_minoritario_isolado_nao_consegue_eleger_lider` e
   `test_grupo_majoritario_elege_lider_apesar_da_particao` lado a lado — a mesma
   partição, dois resultados diferentes, dependendo de qual lado tem maioria.
3. Rode `test_apos_curar_particao_lider_antigo_nao_recupera_maioria_sozinho` e conecte
   de volta com a situação-problema: é exatamente esse mecanismo que impede o
   incidente de dois operadores promovendo dois líderes.
4. Feche com o ADR 0007: por que este projeto simula as regras em vez de implementar
   Raft de produção, e o que isso implica para quem for usar isso profissionalmente
   (usar uma ferramenta madura, não reescrever).

## Como rodar

```bash
make setup
make test        # 57 testes: 26 em pedidos, 31 em estoque
```

## Pergunta que fica em aberto

O consenso decide quem manda. Ele não resolve o problema de uma compra que atravessa
quatro serviços com quatro bancos de dados independentes — não existe mais uma
transação única capaz de garantir que os quatro passos aconteçam todos ou nenhum.
Essa é a última aula da Unidade 2: sagas, outbox/inbox e idempotência.

## Estado do projeto

```
docs/
  consenso.md                                          [novo]
  adr/0007-consenso-simulado-nao-embutido.md            [novo]
services/
  estoque/
    app/consenso.py                                     [novo]
    tests/test_consenso.py                               [novo]
```

57 testes (26 em pedidos, 31 em estoque).
