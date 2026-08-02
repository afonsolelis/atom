"""Identificador de correlação — Unidade 1, Aula 3 / Unidade 4, Aula 13.

Todo pedido carrega um `trace_id` gerado na entrada do sistema. Ele viaja em
um cabeçalho HTTP (`X-Trace-Id`) e é devolvido em toda resposta, para que uma
jornada que atravesse múltiplos serviços possa ser reconstruída depois — o
problema exato que abre o roteiro da Aula 13 ("um pedido que sumiu por doze
segundos").

Nesta aula existe apenas um serviço, então a propagação entre processos ainda
não é observável. O mecanismo é construído agora porque, sem ele, a Aula 4
(que introduz uma segunda chamada de rede, ainda que a um stub) já nasceria
sem como correlacionar as duas pontas.
"""

from __future__ import annotations

import uuid
from contextvars import ContextVar

_trace_id_atual: ContextVar[str] = ContextVar("trace_id_atual", default="")

CABECALHO_TRACE_ID = "X-Trace-Id"


def gerar_trace_id() -> str:
    """Gera um identificador de 32 caracteres hexadecimais, no mesmo formato
    usado por W3C Trace Context — o padrão que a Aula 13 adota via OpenTelemetry."""
    return uuid.uuid4().hex


def obter_trace_id() -> str:
    """Lê o trace_id do contexto da requisição corrente."""
    return _trace_id_atual.get()


def definir_trace_id(trace_id: str) -> None:
    _trace_id_atual.set(trace_id)
