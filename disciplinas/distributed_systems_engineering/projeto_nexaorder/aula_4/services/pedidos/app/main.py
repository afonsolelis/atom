"""Serviço Pedidos (Aula 3 + Aula 4).

Implementa o contrato de docs/contratos/api-pedidos.md: criar pedido (com
idempotência) e consultar pedido. Cada requisição recebe ou propaga um
trace_id e avança o relógio lógico de Lamport do processo.

A partir da Aula 4, reservar estoque passa a ser uma chamada de rede real,
protegida por timeout, retry com backoff e disjuntor
(docs/adr/0004-resiliencia-timeout-retry-disjuntor.md).
"""

from __future__ import annotations

import os
import uuid
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.concurrency import run_in_threadpool

from .correlation import CABECALHO_TRACE_ID, definir_trace_id, gerar_trace_id, obter_trace_id
from .lamport import LamportClock
from .models import CriarPedidoRequest, EstadoPedido, PedidoResponse
from .resiliencia import CircuitBreaker, CircuitoAberto, ClienteResiliente, FalhaTransitoria
from .store import RepositorioPedidos

CAMINHO_BANCO = os.environ.get("PEDIDOS_DB_PATH", "pedidos.db")
ESTOQUE_BASE_URL = os.environ.get("ESTOQUE_BASE_URL", "http://localhost:8002")

app = FastAPI(title="NexaOrder — Pedidos", version="0.4.0")
repositorio = RepositorioPedidos(CAMINHO_BANCO)
relogio = LamportClock()

_cliente_http = httpx.AsyncClient()
_disjuntor_estoque = CircuitBreaker()
_cliente_estoque = ClienteResiliente(_cliente_http, _disjuntor_estoque)


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


@app.post("/pedidos/{pedido_id}/reservar-estoque")
async def reservar_estoque(pedido_id: str):
    """Chama o serviço Estoque para reservar os itens do pedido.

    Separado de `criar_pedido` de propósito: criar o pedido é uma decisão
    local que não deveria depender da rede; reservar estoque é a primeira
    etapa que atravessa uma fronteira de processo, e é aqui que timeout,
    retry e disjuntor entram em ação.
    """
    pedido = await run_in_threadpool(repositorio.obter_por_id, pedido_id)
    if pedido is None:
        raise HTTPException(status_code=404, detail="pedido não encontrado")

    if not _disjuntor_estoque.permite_chamada():
        raise HTTPException(
            status_code=503,
            detail="disjuntor aberto para o serviço de estoque — tente novamente em instantes",
        )

    item = pedido["itens"][0]
    try:
        resposta = await _cliente_estoque.post(
            f"{ESTOQUE_BASE_URL}/reservas",
            json={"pedido_id": pedido_id, "sku": item["sku"], "quantidade": item["quantidade"]},
            trace_id=pedido["trace_id"],
        )
    except CircuitoAberto as erro:
        raise HTTPException(status_code=503, detail=str(erro)) from erro
    except (httpx.TimeoutException, FalhaTransitoria) as erro:
        raise HTTPException(
            status_code=503,
            detail=f"estoque indisponível após retentativas: {erro}",
        ) from erro

    pedido["estado"] = EstadoPedido.RESERVADO.value
    await run_in_threadpool(repositorio.atualizar_estado, pedido_id, EstadoPedido.RESERVADO.value)
    pedido["estado"] = EstadoPedido.RESERVADO.value
    return {"pedido_id": pedido_id, "estado": "RESERVADO", "reserva": resposta.json()}


@app.get("/saude")
async def saude():
    """Usado pela sonda de vivacidade a partir da Aula 11."""
    return {
        "status": "ok",
        "carimbo_lamport": relogio.valor,
        "disjuntor_estoque": _disjuntor_estoque.estado,
    }
