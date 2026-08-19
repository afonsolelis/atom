# ADR 0007 — Simular consenso, não embutir Raft de produção

- **Status:** aceito
- **Data:** correspondente à Unidade 2, Aula 7

## Contexto

A Aula 7 ensina consenso via Raft. Uma implementação de produção real (rede,
temporizadores, persistência de log, recuperação de nó) é um projeto de várias
semanas por si só — bibliotecas maduras como etcd ou Consul existem exatamente porque
"apenas implementar Raft direito" é conhecidamente difícil.

## Decisão

Implementar uma simulação determinística e síncrona das regras de consenso
(maioria, termos, confirmação por maioria, comportamento sob partição), sem rede real
e sem persistência, em `services/estoque/app/consenso.py`.

## Por quê

O objetivo pedagógico da aula é o raciocínio — por que maioria, por que termo
crescente, por que um líder antigo não pode voltar a mandar depois que a maioria
avançou — não a engenharia de rede que um Raft real exigiria. Uma simulação síncrona
torna esse raciocínio inteiramente testável, com asserções exatas, sem introduzir
falhas de teste por tempo real (flakiness) que atrapalhariam a didática.

## Compromisso aceito

O módulo não está integrado a nenhum fluxo HTTP do projeto. Isso é proposital e está
registrado — em produção, ninguém reescreve Raft; usa-se uma ferramenta madura para
coordenar liderança e delega-se o problema de aplicação (aqui, "qual instância de
estoque pode escrever") para o resultado dessa coordenação.

## Evidência

`tests/test_consenso.py` reproduz, com asserções exatas, os quatro comportamentos que
a Aula 7 exige entender: tolerância a falhas por maioria, eleição correta com todos
os nós alcançáveis, o lado minoritário não progredindo sob partição, e a segurança do
líder antigo não corromper o log depois que a partição sara.
