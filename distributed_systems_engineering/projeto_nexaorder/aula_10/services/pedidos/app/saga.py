"""Saga orquestrada da compra — Unidade 2, Aula 8.

Substitui a transação distribuída única (que não existe) por uma sequência
de transações locais encadeadas, com compensação explícita para cada etapa
que precisar ser desfeita. A orquestração acontece em `pedidos` — é a saga
orquestrada, e não coreografada, porque o fluxo de uma compra precisa ser
auditável em um único lugar (ver a comparação em `docs/saga.md`).

As etapas são injetadas como funções assíncronas, para que a lógica de
orquestração seja testável sem depender de HTTP real — quem monta a saga em
`main.py` é responsável por converter falhas de rede, timeout e disjuntor
em `EtapaFalhou`, para que este módulo não precise conhecer esses detalhes.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Awaitable, Callable


class EtapaFalhou(Exception):
    """Sinaliza que uma etapa da saga não pôde ser concluída, por qualquer
    motivo — timeout, disjuntor aberto, resposta de erro."""


@dataclass
class PassoCompensado:
    nome: str
    referencia: str


@dataclass
class ResultadoSaga:
    sucesso: bool
    estado_final: str
    reserva_id: str | None = None
    cobranca_id: str | None = None
    remessa_id: str | None = None
    falhou_em: str | None = None
    compensacoes: list[PassoCompensado] = field(default_factory=list)


class SagaCompra:
    """Orquestra reservar estoque, autorizar pagamento e solicitar
    expedição, compensando na ordem inversa quando uma etapa falha."""

    def __init__(
        self,
        reservar_estoque: Callable[[], Awaitable[dict[str, Any]]],
        liberar_estoque: Callable[[str], Awaitable[None]],
        autorizar_pagamento: Callable[[], Awaitable[dict[str, Any]]],
        estornar_pagamento: Callable[[str], Awaitable[None]],
        solicitar_expedicao: Callable[[], Awaitable[dict[str, Any]]],
    ) -> None:
        self._reservar_estoque = reservar_estoque
        self._liberar_estoque = liberar_estoque
        self._autorizar_pagamento = autorizar_pagamento
        self._estornar_pagamento = estornar_pagamento
        self._solicitar_expedicao = solicitar_expedicao

    async def executar(self) -> ResultadoSaga:
        try:
            reserva = await self._reservar_estoque()
        except EtapaFalhou:
            return ResultadoSaga(sucesso=False, estado_final="RECEBIDO", falhou_em="reservar_estoque")

        reserva_id = reserva["reserva_id"]

        try:
            cobranca = await self._autorizar_pagamento()
        except EtapaFalhou:
            await self._liberar_estoque(reserva_id)
            return ResultadoSaga(
                sucesso=False,
                estado_final="RECEBIDO",
                reserva_id=reserva_id,
                falhou_em="autorizar_pagamento",
                compensacoes=[PassoCompensado("liberar_estoque", reserva_id)],
            )

        cobranca_id = cobranca["id"]

        try:
            remessa = await self._solicitar_expedicao()
        except EtapaFalhou:
            await self._estornar_pagamento(cobranca_id)
            await self._liberar_estoque(reserva_id)
            return ResultadoSaga(
                sucesso=False,
                estado_final="PAGO",
                reserva_id=reserva_id,
                cobranca_id=cobranca_id,
                falhou_em="solicitar_expedicao",
                compensacoes=[
                    PassoCompensado("estornar_pagamento", cobranca_id),
                    PassoCompensado("liberar_estoque", reserva_id),
                ],
            )

        return ResultadoSaga(
            sucesso=True,
            estado_final="EXPEDIDO",
            reserva_id=reserva_id,
            cobranca_id=cobranca_id,
            remessa_id=remessa["id"],
        )
