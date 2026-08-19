"""Serviço Pedidos — primeiro código executável do projeto (Aula 3).

Implementa o contrato de docs/contratos/api-pedidos.md: criar pedido (com
idempotência) e consultar pedido. Cada requisição recebe ou propaga um
trace_id e avança o relógio lógico de Lamport do processo.
"""

from __future__ import annotations

import os
import uuid
from typing import Any

from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.concurrency import run_in_threadpool

from .correlation import CABECALHO_TRACE_ID, definir_trace_id, gerar_trace_id, obter_trace_id
from .lamport import LamportClock
from .models import CriarPedidoRequest, EstadoPedido, PedidoResponse
from .store import RepositorioPedidos

CAMINHO_BANCO = os.environ.get("PEDIDOS_DB_PATH", "pedidos.db")

app = FastAPI(title="NexaOrder — Pedidos", version="0.3.0")
repositorio = RepositorioPedidos(CAMINHO_BANCO)
relogio = LamportClock()


@app.middleware("http")
async def middleware_correlacao(request: Request, chamar_proximo):
    """Gera um trace_id se a requisição não trouxer um, e o devolve sempre
    no cabeçalho de resposta. Ver docs/contratos/api-pedidos.md."""
    trace_id = request.headers.get(CABECALHO_TRACE_ID) or gerar_trace_id()
    definir_trace_id(trace_id)
    resposta = await chamar_proximo(request)
    resposta.headers[CABECALHO_TRACE_ID] = trace_id
    return resposta


def _para_resposta(pedido: dict[str, Any]) -> PedidoResponse:
    return PedidoResponse(
        id=pedido["id"],
        cliente_id=pedido["cliente_id"],
        estado=EstadoPedido(pedido["estado"]),
        itens=pedido["itens"],
        total=pedido["total"],
        criado_em=pedido["criado_em"],
        trace_id=pedido["trace_id"],
        carimbo_lamport=pedido["carimbo_lamport"],
    )


@app.post("/pedidos", status_code=201)
async def criar_pedido(corpo: CriarPedidoRequest):
    existente = await run_in_threadpool(
        repositorio.obter_por_chave_idempotencia, corpo.chave_idempotencia
    )
    if existente is not None:
        # Idempotência simples: mesma chave devolve o pedido já criado.
        # A versão completa, com verificação de corpo divergente e a
        # fronteira transacional junto ao evento, chega na Aula 8.
        return _para_resposta(existente)

    # Regra 1 de Lamport: criar o pedido é um evento local.
    carimbo = relogio.evento_local()

    pedido = {
        "id": str(uuid.uuid4()),
        "cliente_id": str(corpo.cliente_id),
        "chave_idempotencia": corpo.chave_idempotencia,
        "estado": EstadoPedido.RECEBIDO.value,
        "itens": [item.model_dump() for item in corpo.itens],
        "total": sum(item.quantidade * item.preco_unitario for item in corpo.itens),
        "criado_em": PedidoResponse.agora().isoformat(),
        "trace_id": obter_trace_id(),
        "carimbo_lamport": carimbo,
    }
    await run_in_threadpool(repositorio.salvar, pedido)
    return _para_resposta(pedido)


@app.get("/pedidos/{pedido_id}")
async def obter_pedido(pedido_id: str):
    pedido = await run_in_threadpool(repositorio.obter_por_id, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="pedido não encontrado")
    return _para_resposta(pedido)


@app.get("/saude")
async def saude():
    """Usado pela sonda de vivacidade a partir da Aula 11."""
    return {"status": "ok", "carimbo_lamport": relogio.valor}
