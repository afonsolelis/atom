# Consenso e eleição de líder — Unidade 2, Aula 7

## O incidente que motiva o módulo

O roteiro da Aula 7 abre com um incidente concreto: o líder do estoque fica
inacessível, dois operadores promovem dois seguidores diferentes, sem coordenar entre
si, e por alguns minutos o sistema tem dois líderes aceitando escritas ao mesmo tempo.

O diagnóstico da aula é que o problema real não é a indisponibilidade do líder — isso
é esperado. O problema é resolver a promoção **manualmente**, sem um mecanismo que
garanta, sozinho, que só um líder existe por vez.

`services/estoque/app/consenso.py` implementa esse mecanismo, simplificado: eleição
por maioria com termos crescentes, no espírito do Raft.

## O que está implementado, e o que é simplificação

Implementado e testado:
- `tolerancia_a_falhas(n)` — f = piso((N-1)/2). `test_6_nos_nao_tolera_mais_falhas_que_5`
  reproduz exatamente o argumento do roteiro para número ímpar de nós.
- Eleição por maioria, com um nó votando no máximo uma vez por termo.
- Replicação de log confirmada apenas quando uma maioria do cluster (não apenas dos
  nós alcançáveis) recebeu a entrada.
- Comportamento sob partição: o lado minoritário não elege líder nem confirma
  entradas; o lado majoritário continua operando.
- Segurança após a partição sanar: um líder antigo, em termo desatualizado, não
  recupera a maioria sozinho — os nós que já avançaram de termo rejeitam
  implicitamente suas entradas.

Simplificado, deliberadamente:
- Não há rede real nem tempo real. Eleição e replicação são chamadas de método,
  síncronas e determinísticas — o oposto de um sistema real, onde exatamente a
  incerteza de tempo é o problema. A simplificação existe para tornar o teste
  determinístico; o roteiro continua sendo a referência para o comportamento sob
  tempo real (temporizadores aleatórios, thundering herd de candidaturas).
- Não há verificação de consistência do log via `prevLogIndex`/`prevLogTerm` como no
  Raft real — os nós deste projeto sempre recebem entradas em ordem, sem lacunas.
- Não há persistência do estado do nó em disco — um nó "reiniciado" simplesmente não
  existe neste modelo.

## Onde isso se conecta ao resto do projeto

Este módulo não está — ainda — plugado a nenhuma rota HTTP de `estoque`. Ele
demonstra o raciocínio de consenso isoladamente, do mesmo jeito que
`particionamento.py` (Aula 6) demonstrou hashing consistente isoladamente. Um cluster
de consenso real coordenando qual instância de estoque pode escrever exigiria um
sistema como etcd, Consul ou Raft embutido em produção — fora do escopo de código
deste projeto didático, mas exatamente o tipo de peça que essas ferramentas resolvem.

## Decisão registrada

Ver `docs/adr/0007-consenso-simulado-nao-embutido.md`.
