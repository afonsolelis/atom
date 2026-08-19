# ADR 0006 — Particionamento: biblioteca testada, sem fragmentação física do estoque

- **Status:** aceito
- **Data:** correspondente à Unidade 2, Aula 6

## Contexto

A Aula 6 apresenta hashing consistente como técnica para dividir dados entre múltiplos
nós minimizando o custo de rebalanceamento. Uma implementação fisicamente completa
exigiria múltiplas instâncias de `estoque`, cada uma com seu próprio banco, mais um
mecanismo de roteamento que soubesse a qual instância uma consulta deveria ir.

## Decisão

Implementar e testar exaustivamente a lógica de particionamento
(`services/estoque/app/particionamento.py`), sem fragmentar fisicamente o serviço de
estoque nesta aula.

## Por quê

O ganho pedagógico de hashing consistente está na matemática — na diferença entre
mover ~100% e mover ~10% das chaves — e essa matemática é inteiramente demonstrável
sem infraestrutura adicional. Fragmentar `estoque` agora exigiria construir
coordenação entre partições antes de ter consenso (Aula 7) ou sagas (Aula 8) prontos
para lidar com o que essa coordenação exige — colocaria a infraestrutura na frente do
raciocínio que a justifica.

## Compromisso aceito

Um aluno lendo apenas o código do serviço de estoque não vê `particionamento.py` em
uso em nenhuma rota HTTP. Isso é proposital e está documentado — a biblioteca existe
para ser reaproveitada na Aula 10 (partição de tópico por `pedido_id`), e é apresentada
como tal, não escondida como se fosse óbvio que ela "ainda não faz nada".

## Evidência

A migração para uso real é validada, na Aula 10, verificando que a chave de
partição escolhida (`pedido_id`) preserva a ordem dos eventos de um mesmo pedido —
o requisito que motivou originalmente esta biblioteca.
