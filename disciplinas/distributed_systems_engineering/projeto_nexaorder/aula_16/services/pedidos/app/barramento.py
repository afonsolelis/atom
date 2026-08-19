"""Barramento de eventos em memória — Unidade 3, Aula 10.

Simula os quatro conceitos centrais de uma plataforma de eventos como
Kafka ou Redpanda: tópico, partição, deslocamento (offset) e grupo de
consumidores. Não é rede real nem persistência em disco — é uma estrutura
em memória, síncrona e determinística, para tornar os mecanismos
observáveis em teste, do mesmo espírito que `consenso.py` (Aula 7).

Em produção, este módulo seria substituído por um cliente Kafka/Redpanda
real, apontando para o broker declarado em `docker-compose.yml`
(ver docs/arquitetura-eventos.md).
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from typing import Any


def escolher_particao(chave: str, num_particoes: int) -> int:
    """hash(chave) módulo N — a estratégia correta para particionamento de
    tópico, porque o número de partições de um tópico é fixo após a
    criação (ao contrário do número de nós de um cluster, que muda com
    frequência e por isso usa hashing consistente — ver Aula 6)."""
    digest = hashlib.sha256(chave.encode()).hexdigest()
    return int(digest, 16) % num_particoes


@dataclass
class Evento:
    chave: str
    tipo: str
    payload: dict[str, Any]
    offset: int = -1  # atribuído no momento da publicação
    trace_id: str = ""  # Aula 13: o terceiro passo da propagação — o salto
    # assíncrono é o mais frequentemente esquecido, porque não há um
    # cabeçalho HTTP óbvio para carregar o identificador; aqui ele viaja
    # como metadado do próprio evento (ver docs/observabilidade.md).


@dataclass
class Topico:
    """Um tópico dividido em N partições. Cada partição é uma sequência
    ordenada e imutável — nunca se remove um evento já publicado (retenção
    é tratada à parte, ver `docs/arquitetura-eventos.md`)."""

    nome: str
    num_particoes: int
    _particoes: list[list[Evento]] = field(init=False)

    def __post_init__(self) -> None:
        self._particoes = [[] for _ in range(self.num_particoes)]

    def publicar(self, chave: str, tipo: str, payload: dict[str, Any], trace_id: str = "") -> Evento:
        indice_particao = escolher_particao(chave, self.num_particoes)
        evento = Evento(
            chave=chave,
            tipo=tipo,
            payload=payload,
            offset=len(self._particoes[indice_particao]),
            trace_id=trace_id,
        )
        self._particoes[indice_particao].append(evento)
        return evento

    def particao_da_chave(self, chave: str) -> int:
        return escolher_particao(chave, self.num_particoes)

    def ler_particao(self, indice_particao: int, a_partir_do_offset: int = 0) -> list[Evento]:
        return self._particoes[indice_particao][a_partir_do_offset:]

    def tamanho_particao(self, indice_particao: int) -> int:
        return len(self._particoes[indice_particao])


class GrupoConsumidores:
    """Divide as partições de um tópico entre instâncias nomeadas. Cada
    partição é atribuída a exatamente uma instância do grupo por vez —
    a regra central que dá escala horizontal ao consumo (Aula 10)."""

    def __init__(self, topico: Topico, nome_grupo: str, instancias: list[str]) -> None:
        if not instancias:
            raise ValueError("um grupo de consumidores precisa de ao menos uma instância")
        self.topico = topico
        self.nome_grupo = nome_grupo
        self._instancias = list(instancias)
        self._offsets: dict[int, int] = {i: 0 for i in range(topico.num_particoes)}
        self._atribuicao = self._atribuir_particoes()

    def _atribuir_particoes(self) -> dict[int, str]:
        """Round-robin simples: partição i vai para a instância i % len(instancias)."""
        return {
            particao: self._instancias[particao % len(self._instancias)]
            for particao in range(self.topico.num_particoes)
        }

    def particoes_da_instancia(self, instancia: str) -> list[int]:
        return [p for p, i in self._atribuicao.items() if i == instancia]

    def consumir(self, instancia: str) -> list[Evento]:
        """Lê, para a instância indicada, todos os eventos novos nas
        partições atribuídas a ela, avançando o deslocamento do grupo."""
        eventos_lidos: list[Evento] = []
        for particao in self.particoes_da_instancia(instancia):
            offset_atual = self._offsets[particao]
            novos = self.topico.ler_particao(particao, offset_atual)
            eventos_lidos.extend(novos)
            self._offsets[particao] = offset_atual + len(novos)
        return eventos_lidos

    def rebalancear(self, novas_instancias: list[str]) -> None:
        """Simula uma instância entrando ou saindo do grupo — as partições
        são redistribuídas, mas os deslocamentos já confirmados persistem
        (o grupo não reprocessa o que já leu, ao contrário de um consumidor
        completamente novo lendo desde o início — ver retenção)."""
        if not novas_instancias:
            raise ValueError("um grupo de consumidores precisa de ao menos uma instância")
        self._instancias = list(novas_instancias)
        self._atribuicao = self._atribuir_particoes()

    def deslocamento(self, particao: int) -> int:
        return self._offsets[particao]
