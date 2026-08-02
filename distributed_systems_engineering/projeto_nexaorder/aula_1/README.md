# Aula 1 — Modelagem e a decisão de distribuir

**Videoaula correspondente:** Aula 1 — Pensar distribuído: conceitos, propriedades e compromissos.

## O que esta aula acrescentou ao projeto

Nada ainda executa. E isso é proposital: a primeira decisão de um sistema distribuído
não é de código, é de **fronteira e de justificativa**.

Três artefatos entram no projeto:

- `docs/modelo-dominio.md` — as entidades da NexaOrder, os agregados e o glossário.
  É aqui que se descobre que a palavra "item" significa duas coisas diferentes.
- `docs/dimensionamento.md` — as contas de capacidade e disponibilidade que
  transformam intuição em hipótese verificável.
- `docs/adr/0001-por-que-distribuir.md` — o primeiro registro de decisão arquitetural,
  com requisito, decisão, compromisso e evidência.

## Roteiro de condução

1. Abra `docs/modelo-dominio.md` e percorra o glossário. Pergunte à turma o que é um
   "item" — e mostre que catálogo e estoque respondem coisas diferentes.
2. Abra `docs/dimensionamento.md` e refaça a conta das seis instâncias no quadro.
   O ponto é a utilização-alvo de 70%: quatro instâncias "dariam conta" e sacrificariam
   toda a folga.
3. Abra o ADR 0001 e mostre a estrutura de quatro campos. Deixe claro que todo o resto
   do semestre seguirá esse formato.

## Pergunta que fica em aberto

O modelo descreve *o que* o sistema faz. Ele não diz **como as partes conversam** —
se esperando resposta ou seguindo em frente. É o assunto da Aula 2.

## Estado do projeto

```
docs/
  modelo-dominio.md
  dimensionamento.md
  adr/0001-por-que-distribuir.md
```

Sem código, sem dependências, sem execução.
