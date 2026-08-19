# ADR 0001 — Por que distribuir a NexaOrder

- **Status:** aceito
- **Data:** correspondente ao início do ciclo de vida do projeto (Unidade 1, Aula 1)

## Contexto

A NexaOrder nasceu como uma aplicação em um único processo, com interface, regras de
negócio e banco de dados no mesmo ambiente. Isso funcionou enquanto o volume de vendas
era baixo. Com o crescimento projetado para a campanha de fim de ano, três requisitos
deixaram de ser atendidos por uma arquitetura centralizada:

1. **Escalabilidade** — o pico projetado de 800 requisições por segundo excede o que uma
   única instância sustenta com folga operacional.
2. **Disponibilidade** — uma falha no processo único derruba catálogo, pedidos, estoque,
   pagamento e expedição simultaneamente, mesmo quando o problema afeta apenas um deles.
3. **Integração externa** — o provedor de pagamento é um sistema de terceiros, fora do
   controle da NexaOrder, e a comunicação com ele precisa ser tratada como rede, não
   como chamada local.

## Decisão

Distribuir a NexaOrder em serviços autônomos, cada um responsável por uma capacidade de
negócio (catálogo, pedidos, estoque, pagamento, expedição), comunicando-se por rede.

Este projeto será construído incrementalmente, aula a aula, começando pela modelagem de
domínio e terminando em uma plataforma operável, observável e testada por experimentos
controlados.

## Compromisso aceito

Distribuir introduz concorrência, ausência de estado global instantâneo e falha parcial
como propriedades estruturais, não como defeitos a corrigir. O restante da disciplina —
e deste projeto — trata de desenhar para essas propriedades, não de eliminá-las.

Custos concretos aceitos desde já:

- Latência de rede entre serviços, onde antes havia chamada de função.
- Necessidade de um mecanismo explícito de correlação para diagnosticar uma jornada que
  atravessa múltiplos processos (resolvido a partir da Aula 3).
- Impossibilidade de uma transação única cobrindo todo o fluxo de compra (resolvido pela
  saga da Aula 8).

## Evidência

A decisão será validada por:

- Teste de carga sustentando 800 req/s com p95 abaixo de 400 ms (formalizado na Aula 14).
- Ausência de indisponibilidade cruzada entre serviços não relacionados durante a falha
  isolada de um deles (validado por experimento de caos, Aula 14).

## Alternativas consideradas

| Alternativa | Por que foi descartada |
|-------------|-------------------------|
| Escalar verticalmente o monólito atual | Tem teto físico e econômico; não resolve disponibilidade nem integração com o provedor externo |
| Monólito modular (módulos internos, banco único) | Resolveria parte da organização do código, mas não a integração com o pagamento externo nem a necessidade de escalar catálogo e pedidos de forma independente |

O monólito modular permanece uma alternativa legítima para partes do sistema que não
exigem escala ou autonomia independentes — ele volta a ser discutido na Aula 9.
