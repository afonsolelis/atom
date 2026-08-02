"""Simulação simplificada de consenso (Raft) — Unidade 2, Aula 7.

Não é uma implementação de produção: não há rede real, e a passagem de
tempo não é o relógio do sistema operacional — eleição e replicação são
disparadas explicitamente por quem chama, o que torna o comportamento
determinístico e testável. O que se preserva, fielmente, são as regras:
maioria decide, termos crescem, um nó não vota duas vezes no mesmo termo, e
uma entrada só é confirmada quando uma maioria a recebeu.

O incidente que motiva este módulo é o da situação-problema da Aula 7: uma
promoção manual de réplica, feita por dois operadores sem coordenação, gerou
dois líderes simultâneos. Este módulo formaliza a pergunta que resolve isso:
como um conjunto de nós concorda, sozinho, sobre quem é o líder legítimo?
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum


class EstadoNo(StrEnum):
    SEGUIDOR = "seguidor"
    CANDIDATO = "candidato"
    LIDER = "lider"


def tolerancia_a_falhas(n: int) -> int:
    """f = piso((N-1)/2) — quantas falhas um cluster de N nós tolera
    mantendo maioria. Ver por que 6 nós não tolera mais falhas que 5."""
    return (n - 1) // 2


def tamanho_da_maioria(n: int) -> int:
    return n // 2 + 1


@dataclass
class EntradaDeLog:
    termo: int
    valor: str


@dataclass
class NoRaft:
    id: str
    estado: EstadoNo = EstadoNo.SEGUIDOR
    termo_atual: int = 0
    votou_em: str | None = None
    log: list[EntradaDeLog] = field(default_factory=list)
    indice_confirmado: int = -1


class ClusterRaft:
    """Orquestra N nós e simula eleição e replicação de log de forma
    síncrona e determinística. Suporta particionar um subconjunto de nós
    para observar o comportamento do lado minoritário."""

    def __init__(self, ids_dos_nos: list[str]) -> None:
        self._nos: dict[str, NoRaft] = {id_: NoRaft(id=id_) for id_ in ids_dos_nos}
        self._particionados: set[str] = set()

    @property
    def nos(self) -> dict[str, NoRaft]:
        return self._nos

    def particionar(self, ids_isolados: list[str]) -> None:
        self._particionados = set(ids_isolados)

    def curar_particao(self) -> None:
        self._particionados.clear()

    def _nos_alcancaveis(self, origem: str) -> list[NoRaft]:
        """Nós que `origem` consegue contatar. Um nó particionado não
        alcança ninguém, e ninguém o alcança."""
        if origem in self._particionados:
            return []
        return [
            no
            for id_, no in self._nos.items()
            if id_ != origem and id_ not in self._particionados
        ]

    def iniciar_eleicao(self, candidato_id: str) -> bool:
        """Incrementa o termo, solicita votos aos nós alcançáveis, e se
        torna líder se alcançar maioria do cluster inteiro (não apenas dos
        nós alcançáveis — é isso que impede uma minoria de eleger líder)."""
        candidato = self._nos[candidato_id]
        candidato.termo_atual += 1
        candidato.estado = EstadoNo.CANDIDATO
        candidato.votou_em = candidato_id
        votos = 1  # o candidato vota em si mesmo

        for no in self._nos_alcancaveis(candidato_id):
            if self._conceder_voto(no, candidato.termo_atual, candidato_id):
                votos += 1

        if votos >= tamanho_da_maioria(len(self._nos)):
            candidato.estado = EstadoNo.LIDER
            for id_, no in self._nos.items():
                if id_ != candidato_id and id_ not in self._particionados:
                    no.estado = EstadoNo.SEGUIDOR
            return True

        candidato.estado = EstadoNo.SEGUIDOR
        return False

    @staticmethod
    def _conceder_voto(no: NoRaft, termo_do_candidato: int, candidato_id: str) -> bool:
        if termo_do_candidato < no.termo_atual:
            return False
        if termo_do_candidato > no.termo_atual:
            # Termo maior descoberto: atualiza e libera o voto deste termo.
            no.termo_atual = termo_do_candidato
            no.votou_em = None
            no.estado = EstadoNo.SEGUIDOR
        if no.votou_em is None or no.votou_em == candidato_id:
            no.votou_em = candidato_id
            return True
        return False  # já votou em outro candidato neste termo

    def replicar_entrada(self, lider_id: str, valor: str) -> bool:
        """O líder anexa uma entrada ao próprio log e a replica aos nós
        alcançáveis cujo termo não seja maior que o dele. Confirma somente
        se uma maioria do cluster total (não só dos alcançáveis) recebeu."""
        lider = self._nos[lider_id]
        if lider.estado != EstadoNo.LIDER:
            raise ValueError(f"{lider_id} não é o líder atual")

        entrada = EntradaDeLog(termo=lider.termo_atual, valor=valor)
        lider.log.append(entrada)
        indice_da_entrada = len(lider.log) - 1

        confirmacoes = 1  # o próprio líder
        for no in self._nos_alcancaveis(lider_id):
            if no.termo_atual > lider.termo_atual:
                continue  # nó já viu um termo mais novo — rejeita implicitamente
            no.log.append(entrada)
            confirmacoes += 1

        if confirmacoes >= tamanho_da_maioria(len(self._nos)):
            lider.indice_confirmado = indice_da_entrada
            return True
        return False
