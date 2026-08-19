# ADR 0016 — A defesa arquitetural não introduz mecanismo novo; audita o que já existe

- **Status:** aceito
- **Data:** correspondente à Unidade 4, Aula 16 (encerramento do projeto)

## Contexto

Todas as ADRs anteriores (0001–0015) documentam uma decisão de implementação: uma
tecnologia adotada, um mecanismo simplificado, um limite de infraestrutura aceito. A
Aula 16 é estruturalmente diferente — o próprio roteiro abre afirmando que, "em vez
de apresentar um mecanismo novo, ela consiste em sustentar tecnicamente tudo o que
foi estudado". Cabia decidir como essa diferença se refletiria no código deste
projeto.

## Decisão

Não adicionar nenhum serviço, endpoint de negócio ou mecanismo de domínio novo.
Adicionar apenas: (1) uma extensão do módulo de disponibilidade da Aula 14 com a
fórmula de redundância paralela (o contraste que a Aula 16 pede), (2) um recálculo,
com evidência real, do dimensionamento original da Aula 1, e (3) um script de
critérios de aceite que converte em código executável um princípio que, até aqui,
só existia em prosa nos ADRs anteriores. O restante do trabalho desta aula é
documentação: `docs/defesa-arquitetural.md`.

## Por quê

Inventar um mecanismo novo só para que a Aula 16 "tivesse código" contradiria o
próprio ponto da aula. O valor pedagógico aqui não é aprender mais uma técnica — é
demonstrar que as quinze anteriores, combinadas, sustentam um argumento. Forçar uma
peça de código sem função arquitetural real teria sido a mesma armadilha que os ADRs
anteriores evitaram consistentemente: criar aparência de trabalho sem trabalho real
por trás (ver ADR 0010).

As três adições que este ADR aceita têm todas função argumentativa direta na defesa,
não decorativa: a redundância paralela é o contraponto numérico que fecha o arco
aberto pela cadeia sequencial da Aula 14; o recálculo do dimensionamento fecha o arco
aberto literalmente por `docs/dimensionamento.md` desde a Aula 1 ("a Aula 16 recalcula
os mesmos números com evidências operacionais reais"); e o script de critérios de
aceite é a única forma de o princípio "seguro e observável por padrão" deixar de ser
sugestão e virar critério verificável, exatamente como o roteiro exige.

## Compromisso aceito

Este projeto encerra sem RPO/RTO implementados, sem réplica de banco, sem coletor de
observabilidade central e sem mTLS real — todos nomeados explicitamente na análise de
SPOF de `docs/defesa-arquitetural.md`. Uma defesa arquitetural honesta lista esses
limites como próximos passos, não os esconde para parecer mais completa. É a mesma
disciplina de honestidade que toda ADR anterior já praticava, aplicada agora ao
projeto como um todo, não a uma decisão isolada.

## Evidência

`scripts/test_disponibilidade_em_cadeia.py` prova a redundância paralela e seu
contraste estrutural com a cadeia sequencial. `services/pedidos/tests/test_dimensionamento_com_evidencias.py`
prova o recálculo com capacidade medida ao vivo. `scripts/test_verificar_criterios_de_aceite.py`
prova que o gate aprova os cinco serviços reais e detecta de verdade um serviço
incompleto — nos dois sentidos, não só o caminho feliz.
