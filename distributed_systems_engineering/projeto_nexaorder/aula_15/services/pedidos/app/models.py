"""Esquemas de entrada e saída — implementam literalmente o contrato
registrado em docs/contratos/api-pedidos.md (Aula 2)."""

from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, Field, field_validator


class EstadoPedido(StrEnum):
    RECEBIDO = "RECEBIDO"
    RESERVADO = "RESERVADO"
    PAGO = "PAGO"
    EXPEDIDO = "EXPEDIDO"
    CANCELADO = "CANCELADO"


class ItemPedido(BaseModel):
    sku: str
    quantidade: int = Field(gt=0)
    preco_unitario: float = Field(gt=0)


class CriarPedidoRequest(BaseModel):
    cliente_id: UUID
    chave_idempotencia: str = Field(min_length=1)
    itens: list[ItemPedido]

    @field_validator("itens")
    @classmethod
    def itens_nao_pode_ser_vazio(cls, valor: list[ItemPedido]) -> list[ItemPedido]:
        if not valor:
            raise ValueError("um pedido precisa de ao menos um item")
        return valor


class TentativaDePagamentoRequest(BaseModel):
    """Aula 15 — entrada do pipeline de detecção de fraude em fluxo. O
    tempo de evento vem de quem chama (o cliente, ou um gateway de
    pagamento); o tempo de processamento é sempre o relógio real deste
    serviço no instante da ingestão (ver app/main.py)."""

    dispositivo_id: str = Field(min_length=1)
    tempo_evento_ms: int


class PedidoResponse(BaseModel):
    id: str
    cliente_id: str
    estado: EstadoPedido
    itens: list[ItemPedido]
    total: float
    criado_em: datetime
    trace_id: str
    carimbo_lamport: int

    @staticmethod
    def agora() -> datetime:
        return datetime.now(timezone.utc)
