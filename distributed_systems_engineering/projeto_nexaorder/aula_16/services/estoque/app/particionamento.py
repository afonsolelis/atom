"""Particionamento e hashing consistente — Unidade 2, Aula 6.

Duas estratégias, comparadas com números: hash simples (módulo N) e hashing
consistente com anel e nós virtuais. A biblioteca é testada e correta aqui;
sua aplicação real dentro do projeto aparece na Aula 10, quando o broker de
eventos precisa decidir a partição de cada mensagem por `pedido_id` — o
mesmo raciocínio matemático, aplicado a um tópico em vez de a uma hipotética
fragmentação física do serviço de estoque.
"""

from __future__ import annotations

import bisect
import hashlib


def hash_simples(chave: str, num_particoes: int) -> int:
    """Estratégia ingênua: hash(chave) módulo N.

    Rápida e óbvia, mas qualquer mudança em N reatribui a maior parte das
    chaves — ver o teste que reproduz o "aproximadamente 100%" do roteiro.
    """
    digest = hashlib.sha256(chave.encode()).hexdigest()
    return int(digest, 16) % num_particoes


class AnelConsistente:
    """Hashing consistente com nós virtuais.

    Cada nó físico recebe várias posições (`nos_virtuais_por_no`) espalhadas
    pelo anel, para que a carga de cada nó não dependa do acaso de onde ele
    caiu — ver `docs/particionamento-e-pacelc.md`.
    """

    def __init__(self, nos_virtuais_por_no: int = 100) -> None:
        self._nos_virtuais_por_no = nos_virtuais_por_no
        self._anel: dict[int, str] = {}
        self._posicoes_ordenadas: list[int] = []
        self._nos: set[str] = set()

    @staticmethod
    def _hash(texto: str) -> int:
        return int(hashlib.sha256(texto.encode()).hexdigest(), 16)

    def adicionar_no(self, no: str) -> None:
        if no in self._nos:
            return
        self._nos.add(no)
        for indice in range(self._nos_virtuais_por_no):
            posicao = self._hash(f"{no}#{indice}")
            self._anel[posicao] = no
        self._posicoes_ordenadas = sorted(self._anel)

    def remover_no(self, no: str) -> None:
        if no not in self._nos:
            return
        self._nos.discard(no)
        for indice in range(self._nos_virtuais_por_no):
            posicao = self._hash(f"{no}#{indice}")
            self._anel.pop(posicao, None)
        self._posicoes_ordenadas = sorted(self._anel)

    def localizar(self, chave: str) -> str:
        """Cada chave vai ao primeiro nó encontrado em sentido horário."""
        if not self._anel:
            raise ValueError("anel vazio: nenhum nó foi adicionado")
        posicao = self._hash(chave)
        indice = bisect.bisect(self._posicoes_ordenadas, posicao)
        if indice == len(self._posicoes_ordenadas):
            indice = 0
        return self._anel[self._posicoes_ordenadas[indice]]

    @property
    def nos(self) -> frozenset[str]:
        return frozenset(self._nos)


def fracao_redistribuida(
    chaves: list[str], anel_antes: AnelConsistente, anel_depois: AnelConsistente
) -> float:
    """Proporção de chaves cujo nó de destino muda entre dois estados do anel."""
    if not chaves:
        return 0.0
    mudou = sum(1 for chave in chaves if anel_antes.localizar(chave) != anel_depois.localizar(chave))
    return mudou / len(chaves)
