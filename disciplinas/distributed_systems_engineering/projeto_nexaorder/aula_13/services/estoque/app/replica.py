"""Réplica de leitura assíncrona — Unidade 2, Aula 5.

Simula o comportamento de uma réplica alimentada por replicação assíncrona:
toda escrita é propagada ao líder imediatamente, e à réplica depois de um
atraso fixo. Enquanto esse atraso não passa, uma leitura na réplica devolve
um valor mais antigo que o já confirmado no líder — exatamente o fenômeno
descrito no roteiro ("atraso de réplica e leituras obsoletas").

Isto é uma simplificação didática sobre uma estrutura em memória, não um
mecanismo de replicação real entre bancos — o objetivo é tornar a janela de
150 ms observável em teste, não reproduzir um protocolo de replicação.
"""

from __future__ import annotations

import asyncio


class ReplicaLeitura:
    """Réplica com atraso de propagação fixo."""

    ATRASO_PADRAO_SEGUNDOS = 0.150  # o mesmo número do roteiro da Aula 5

    def __init__(self, atraso_segundos: float = ATRASO_PADRAO_SEGUNDOS) -> None:
        self._atraso = atraso_segundos
        self._saldos: dict[str, int] = {}
        self._tarefas_pendentes: set[asyncio.Task] = set()

    def propagar(self, sku: str, novo_saldo: int) -> None:
        """Agenda a aplicação da escrita na réplica, após o atraso configurado.

        Não bloqueia: quem chama (o líder, logo após confirmar a escrita)
        segue em frente sem esperar a réplica.
        """
        tarefa = asyncio.create_task(self._aplicar_apos_atraso(sku, novo_saldo))
        self._tarefas_pendentes.add(tarefa)
        tarefa.add_done_callback(self._tarefas_pendentes.discard)

    async def _aplicar_apos_atraso(self, sku: str, novo_saldo: int) -> None:
        await asyncio.sleep(self._atraso)
        self._saldos[sku] = novo_saldo

    def ler(self, sku: str) -> int | None:
        """Leitura eventual: pode devolver `None` ou um valor desatualizado
        se a propagação ainda não chegou."""
        return self._saldos.get(sku)

    async def aguardar_propagacao_pendente(self) -> None:
        """Só para uso em teste: espera as tarefas de propagação em voo
        terminarem, para tornar as asserções determinísticas."""
        pendentes = list(self._tarefas_pendentes)
        if pendentes:
            await asyncio.gather(*pendentes)
