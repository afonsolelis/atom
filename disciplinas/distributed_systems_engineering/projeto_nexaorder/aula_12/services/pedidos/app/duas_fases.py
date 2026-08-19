"""Confirmação em duas fases (2PC) — Unidade 2, Aula 8.

Implementado apenas para demonstrar, em teste, exatamente o que o roteiro
descreve: o 2PC garante atomicidade distribuída, mas bloqueia participantes
quando o coordenador falha entre as duas fases. Não é usado em nenhum fluxo
real do projeto — a partir desta mesma aula, o projeto adota sagas
(`app/saga.py`), que trocam bloqueio por compensação.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class VotoParticipante(StrEnum):
    PRONTO = "pronto"
    ABORTAR = "abortar"


class EstadoParticipante(StrEnum):
    INICIAL = "inicial"
    PREPARADO = "preparado"  # executou provisoriamente, bloqueou recursos
    CONFIRMADO = "confirmado"
    DESFEITO = "desfeito"


@dataclass
class Participante:
    nome: str
    voto: VotoParticipante = VotoParticipante.PRONTO
    estado: EstadoParticipante = field(default=EstadoParticipante.INICIAL)

    def preparar(self) -> VotoParticipante:
        self.estado = EstadoParticipante.PREPARADO
        return self.voto

    def confirmar(self) -> None:
        self.estado = EstadoParticipante.CONFIRMADO

    def desfazer(self) -> None:
        self.estado = EstadoParticipante.DESFEITO


class CoordenadorDuasFases:
    """Conduz a transação distribuída em duas fases: preparação e decisão."""

    def __init__(self, participantes: list[Participante]) -> None:
        self.participantes = participantes

    def executar(self, coordenador_falha_apos_preparar: bool = False) -> str:
        votos = [p.preparar() for p in self.participantes]

        if coordenador_falha_apos_preparar:
            # O cenário crítico do roteiro: o coordenador cai depois da fase
            # de preparação, antes de comunicar a decisão. Cada participante
            # já executou provisoriamente e bloqueou recursos — e não pode
            # decidir sozinho se deve confirmar ou desfazer.
            return "coordenador_falhou_participantes_bloqueados"

        if all(voto == VotoParticipante.PRONTO for voto in votos):
            for participante in self.participantes:
                participante.confirmar()
            return "confirmado"

        for participante in self.participantes:
            participante.desfazer()
        return "abortado"


def risco_agregado(probabilidade_falha_individual: float, numero_de_participantes: int) -> float:
    """1 − (1 − p)^n — a probabilidade de pelo menos um participante falhar
    ou estar lento. Com p=1% e n=4, dá aproximadamente 3,9% — quase quatro
    vezes o risco individual, o argumento numérico contra o 2PC em fluxos
    com muitos participantes."""
    return 1 - (1 - probabilidade_falha_individual) ** numero_de_participantes
