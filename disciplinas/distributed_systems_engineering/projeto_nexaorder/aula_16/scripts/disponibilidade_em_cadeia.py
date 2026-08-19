"""Disponibilidade combinada — cadeia sequencial e redundância paralela —
Unidade 4, Aulas 14 e 16.

A cadeia sequencial (Aula 14) retoma o cálculo já apresentado na Aula 2,
sob o propósito de justificar por que testes deliberados — não a leitura
do código, não a revisão em pull request, não a confiança na biblioteca —
são o que revela se disjuntor, degradação graciosa e processamento
assíncrono de fato atenuam esse efeito na prática.

A redundância paralela (Aula 16, Slide 13) fecha o contraste: em série, as
disponibilidades se multiplicam e o resultado piora; em paralelo, as
INDISPONIBILIDADES se multiplicam e o resultado melhora de forma
acentuada — desde que as réplicas falhem de forma independente."""

from __future__ import annotations


def disponibilidade_em_cadeia(disponibilidades: list[float]) -> float:
    """Disponibilidade de uma cadeia estritamente sequencial e sem
    tolerância a falha parcial: o produto das disponibilidades
    individuais. A cadeia só responde se cada elo responder."""
    resultado = 1.0
    for disponibilidade in disponibilidades:
        resultado *= disponibilidade
    return resultado


def indisponibilidade(disponibilidade: float) -> float:
    return 1 - disponibilidade


def razao_de_indisponibilidade(disponibilidade_cadeia: float, disponibilidade_componente: float) -> float:
    """Quantas vezes mais indisponível a cadeia é do que qualquer
    componente isolado — a leitura de impacto do exemplo do roteiro:
    contrataram-se componentes de 99,9% e obteve-se um fluxo com quase
    quatro vezes mais indisponibilidade do que qualquer um deles."""
    return indisponibilidade(disponibilidade_cadeia) / indisponibilidade(disponibilidade_componente)


def disponibilidade_redundancia_paralela(disponibilidades: list[float]) -> float:
    """Disponibilidade de réplicas independentes atrás de um balanceador
    que direciona tráfego para qualquer réplica saudável: 1 menos a
    probabilidade de TODAS falharem ao mesmo tempo. Só é válida sob a
    premissa de independência de falha — réplicas no mesmo rack, ou que
    dependem do mesmo banco, não são independentes, e o valor real fica
    muito abaixo do calculado (ver docs/defesa-arquitetural.md)."""
    probabilidade_de_todas_falharem = 1.0
    for disponibilidade in disponibilidades:
        probabilidade_de_todas_falharem *= indisponibilidade(disponibilidade)
    return 1 - probabilidade_de_todas_falharem
