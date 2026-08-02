"""Gateway — Unidade 3, Aula 9.

Compõe uma visão única de um pedido a partir de quatro serviços, para que
quem consome a API não precise conhecer a decomposição interna da
NexaOrder nem seja afetado se essa decomposição mudar amanhã.

Deliberadamente sem regra de negócio e sem banco de dados próprio: o único
trabalho do gateway é rotear e compor. Quando um gateway acumula lógica de
domínio, ele vira um novo monólito escondido atrás de uma fachada de
microsserviços — o alerta do próprio roteiro da Aula 9
(ver docs/limites-de-dominio.md).
"""

from __future__ import annotations

import asyncio
import os
from typing import Any

import httpx
from fastapi import FastAPI, HTTPException

PEDIDOS_BASE_URL = os.environ.get("PEDIDOS_BASE_URL", "http://localhost:8001")
ESTOQUE_BASE_URL = os.environ.get("ESTOQUE_BASE_URL", "http://localhost:8002")
PAGAMENTO_BASE_URL = os.environ.get("PAGAMENTO_BASE_URL", "http://localhost:8003")
EXPEDICAO_BASE_URL = os.environ.get("EXPEDICAO_BASE_URL", "http://localhost:8004")

app = FastAPI(title="NexaOrder — Gateway", version="0.9.0")
_cliente_http = httpx.AsyncClient()


async def _buscar_lista_best_effort(url: str) -> list[dict[str, Any]]:
    """As consultas auxiliares (reservas, cobranças, remessas) toleram
    falha: se um desses serviços estiver fora do ar, a composição não
    falha por inteiro — só aquela seção volta vazia. A consulta ao pedido
    em si, em `resumo_do_pedido`, é a única obrigatória."""
    try:
        resposta = await _cliente_http.get(url, timeout=2.0)
        if resposta.status_code == 200:
            return resposta.json()
    except httpx.HTTPError:
        pass
    return []


@app.get("/pedidos/{pedido_id}/resumo")
async def resumo_do_pedido(pedido_id: str) -> dict[str, Any]:
    """Um único ponto de entrada para o que, internamente, são quatro
    serviços com quatro bancos independentes. Compare com o exemplo do
    roteiro: 'a tela de detalhes do pedido precisa de dados de pedidos,
    estoque e expedição — o gateway consulta os três e devolve uma
    resposta única'."""
    try:
        resposta_pedido = await _cliente_http.get(f"{PEDIDOS_BASE_URL}/pedidos/{pedido_id}", timeout=2.0)
    except httpx.HTTPError as erro:
        raise HTTPException(status_code=503, detail=f"serviço de pedidos indisponível: {erro}") from erro

    if resposta_pedido.status_code == 404:
        raise HTTPException(status_code=404, detail="pedido não encontrado")
    if resposta_pedido.status_code >= 500:
        raise HTTPException(status_code=503, detail="serviço de pedidos retornou erro")

    pedido = resposta_pedido.json()

    reservas, cobrancas, remessas = await asyncio.gather(
        _buscar_lista_best_effort(f"{ESTOQUE_BASE_URL}/reservas/por-pedido/{pedido_id}"),
        _buscar_lista_best_effort(f"{PAGAMENTO_BASE_URL}/cobrancas/por-pedido/{pedido_id}"),
        _buscar_lista_best_effort(f"{EXPEDICAO_BASE_URL}/remessas/por-pedido/{pedido_id}"),
    )

    return {
        "pedido": pedido,
        "reservas": reservas,
        "cobrancas": cobrancas,
        "remessas": remessas,
    }


@app.get("/saude")
async def saude() -> dict[str, Any]:
    return {"status": "ok"}
