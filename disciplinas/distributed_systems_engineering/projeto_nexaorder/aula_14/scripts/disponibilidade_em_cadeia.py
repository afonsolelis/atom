"""Disponibilidade combinada em cadeia — Unidade 4, Aula 14.

Retoma o cálculo já apresentado na Aula 2, agora sob outro propósito: não
para dimensionar, mas para justificar por que testes deliberados — não a
leitura do código, não a revisão em pull request, não a confiança na
biblioteca — são o que revela se disjuntor, degradação graciosa e
processamento assíncrono de fato atenuam esse efeito na prática.
"""

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
