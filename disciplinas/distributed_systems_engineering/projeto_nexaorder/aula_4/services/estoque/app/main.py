"""Estoque — nesta aula, um dublê controlável.

Existe para dar a `pedidos` uma dependência de rede real contra a qual testar
timeout, retry e disjuntor. Ainda não tem persistência nem lógica de saldo —
isso chega na Aula 5, quando o assunto passa a ser replicação e consistência.
A rota `/_debug/config` permite injetar falha e atraso, propositalmente, para
demonstrar o disjuntor abrindo em aula.
"""

from __future__ import annotations

import asyncio
import random
import uuid

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="NexaOrder — Estoque (dublê controlável)", version="0.4.0")


class ConfiguracaoFalha(BaseModel):
    falhar_percentual: int = 0  # 0 a 100
    atraso_ms: int = 0


class ReservarRequest(BaseModel):
    pedido_id: str
    sku: str
    quantidade: int


_config = ConfiguracaoFalha()


@app.post("/_debug/config")
async def configurar_falha(config: ConfiguracaoFalha) -> ConfiguracaoFalha:
    """Só existe para permitir a demonstração em aula do disjuntor abrindo.
    Um serviço real nunca exporia um controle de falha deliberada como este
    fora de um ambiente de teste."""
    global _config
    _config = config
    return _config


@app.post("/reservas", status_code=201)
async def reservar(corpo: ReservarRequest) -> dict:
    if _config.atraso_ms:
        await asyncio.sleep(_config.atraso_ms / 1000)
    if random.randint(1, 100) <= _config.falhar_percentual:
        raise HTTPException(status_code=503, detail="estoque indisponível (falha simulada)")
    return {
        "reserva_id": str(uuid.uuid4()),
        "pedido_id": corpo.pedido_id,
        "sku": corpo.sku,
        "quantidade": corpo.quantidade,
        "estado": "ATIVA",
    }


@app.get("/saude")
async def saude() -> dict:
    return {"status": "ok", "config_falha_ativa": _config.model_dump()}
