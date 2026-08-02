# ADR 0004 — Timeout, retry e disjuntor na chamada a Estoque

- **Status:** aceito
- **Data:** correspondente à Unidade 1, Aula 4

## Contexto

`pedidos` passa a chamar `estoque` por HTTP para reservar um item. Sem proteção,
uma lentidão em `estoque` prende as conexões de `pedidos` indefinidamente e propaga a
degradação — exatamente o incidente descrito no roteiro da Aula 4 ("um serviço lento
não é um serviço fora do ar").

## Decisão

A chamada de `pedidos` a `estoque` passa por três camadas, nesta ordem:

1. **Timeout** de 1 segundo por tentativa. Não prova que a operação falhou — indica
   que a resposta não chegou dentro do prazo tolerado.
2. **Retry** com backoff exponencial e jitter, no máximo 3 tentativas, apenas para
   falhas transitórias (timeout ou 5xx). Erros 4xx nunca são retentados.
3. **Disjuntor** com janela das últimas 20 chamadas e limite de 50% de falhas — os
   mesmos números do exemplo numérico da Aula 4. Quando aberto, rejeita chamadas
   imediatamente, sem tentar a rede.

Implementado em `services/pedidos/app/resiliencia.py`.

## Por quê

Timeout sozinho não basta: sem retry, uma falha transitória vira erro definitivo
desnecessariamente. Retry sozinho não basta: sob degradação sustentada, retentar
sem critério cria o efeito manada e piora o que já estava ruim. O disjuntor existe
para o caso em que o problema não é uma falha isolada, mas uma degradação contínua —
nesse caso, a resposta certa é parar de tentar, não insistir mais rápido.

## Compromisso aceito

Enquanto o disjuntor estiver aberto, toda tentativa de reservar estoque falha de
imediato, mesmo que a instância específica de `estoque` que atenderia a chamada esteja
saudável. É um falso positivo aceito deliberadamente — a alternativa é continuar
mandando tráfego para uma dependência que, na média da janela observada, está falhando
mais da metade das vezes.

## Evidência

`tests/test_resiliencia.py` demonstra, com um transporte HTTP simulado, que:
- 12 falhas em uma janela de 20 chamadas (60%) abrem o disjuntor;
- com o disjuntor aberto, nenhuma chamada adicional chega a tocar a rede;
- uma chamada de teste bem-sucedida no estado semiaberto fecha o disjuntor de novo.
