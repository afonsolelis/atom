"""Estoque — Aula 4 (dublê controlável) + Aula 5 (persistência e réplica).

Mantém a injeção de falha da Aula 4 (`/_debug/config`), útil para continuar
demonstrando o disjuntor de `pedidos`, e acrescenta o que estava faltando:
saldo real por SKU, a invariante de não vender o que não existe, e uma
réplica de leitura com atraso de propagação — o assunto central desta aula.
"""

from __future__ import annotations

import asyncio
import os
import random
from typing import Any

from fastapi import FastAPI, HTTPException, Query, Response
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

from .replica import ReplicaLeitura
from .store import ArmazenLider, SaldoInsuficiente

CAMINHO_BANCO = os.environ.get("ESTOQUE_DB_PATH", "estoque.db")
ATRASO_REPLICA_SEGUNDOS = float(
    os.environ.get("ATRASO_REPLICA_SEGUNDOS", ReplicaLeitura.ATRASO_PADRAO_SEGUNDOS)
)

app = FastAPI(title="NexaOrder — Estoque", version="0.5.0")
lider = ArmazenLider(CAMINHO_BANCO)
replica = ReplicaLeitura(atraso_segundos=ATRASO_REPLICA_SEGUNDOS)


class ConfiguracaoFalha(BaseModel):
    falhar_percentual: int = 0  # 0 a 100 — herdado da Aula 4
    atraso_ms: int = 0


class ReservarRequest(BaseModel):
    pedido_id: str
    sku: str
    quantidade: int


class InicializarSaldoRequest(BaseModel):
    quantidade: int


_config_falha = ConfiguracaoFalha()


@app.post("/_debug/config")
async def configurar_falha(config: ConfiguracaoFalha) -> ConfiguracaoFalha:
    """Herdado da Aula 4 — injeção de falha só para demonstração em aula."""
    global _config_falha
    _config_falha = config
    return _config_falha


@app.post("/estoque/{sku}/inicializar")
async def inicializar_saldo(sku: str, corpo: InicializarSaldoRequest) -> dict[str, Any]:
    """Só existe para preparar o cenário de demonstração/teste — em produção
    o saldo inicial viria de um processo de carga de catálogo, fora do
    escopo implementado deste projeto (ver docs/consistencia-por-dado.md)."""
    await run_in_threadpool(lider.definir_saldo_inicial, sku, corpo.quantidade)
    replica.propagar(sku, corpo.quantidade)
    return {"sku": sku, "quantidade": corpo.quantidade}


@app.post("/reservas", status_code=201)
async def reservar(corpo: ReservarRequest) -> dict[str, Any]:
    if _config_falha.atraso_ms:
        await asyncio.sleep(_config_falha.atraso_ms / 1000)
    if random.randint(1, 100) <= _config_falha.falhar_percentual:
        raise HTTPException(status_code=503, detail="estoque indisponível (falha simulada)")

    try:
        resultado = await run_in_threadpool(lider.reservar, corpo.pedido_id, corpo.sku, corpo.quantidade)
    except SaldoInsuficiente as erro:
        raise HTTPException(status_code=409, detail=str(erro)) from erro

    replica.propagar(corpo.sku, resultado["novo_saldo"])

    return {
        "reserva_id": resultado["reserva_id"],
        "pedido_id": corpo.pedido_id,
        "sku": corpo.sku,
        "quantidade": corpo.quantidade,
        "estado": "ATIVA",
    }


@app.post("/reservas/{reserva_id}/liberar")
async def liberar_reserva(reserva_id: str) -> dict[str, Any]:
    """Compensação da saga (Aula 8): usada quando uma etapa posterior
    falha e a reserva de estoque precisa ser desfeita."""
    resultado = await run_in_threadpool(lider.liberar_reserva, reserva_id)
    if resultado is None:
        raise HTTPException(status_code=404, detail="reserva não encontrada ou já liberada")

    replica.propagar(resultado["sku"], resultado["novo_saldo"])
    return resultado


@app.get("/reservas/por-pedido/{pedido_id}")
async def listar_reservas_do_pedido(pedido_id: str) -> list[dict[str, Any]]:
    """Consulta usada pelo gateway (Aula 9) para compor a visão de um
    pedido sem expor a estrutura interna do estoque ao cliente final."""
    return await run_in_threadpool(lider.listar_por_pedido, pedido_id)


@app.get("/saldo/{sku}")
async def consultar_saldo(
    sku: str,
    consistencia: str = Query(default="forte", pattern="^(forte|eventual)$"),
) -> dict[str, Any]:
    """`consistencia=forte` lê do líder — sempre reflete a última escrita
    confirmada. `consistencia=eventual` lê da réplica — pode devolver um
    valor desatualizado por até `ATRASO_REPLICA_SEGUNDOS`.

    Ver docs/consistencia-por-dado.md para qual consistência a NexaOrder
    usa para cada dado, e por quê.
    """
    if consistencia == "eventual":
        valor = replica.ler(sku)
        fonte = "replica"
    else:
        valor = await run_in_threadpool(lider.saldo_atual, sku)
        fonte = "lider"

    if valor is None:
        raise HTTPException(status_code=404, detail=f"sem saldo conhecido para {sku} nesta fonte ({fonte})")

    return {"sku": sku, "quantidade": valor, "fonte": fonte, "consistencia": consistencia}


@app.get("/saude")
async def saude() -> dict[str, Any]:
    """Sonda de vivacidade (Aula 11): só confirma que o processo responde.
    Uma falha aqui faz o kubelet reiniciar o contêiner."""
    return {"status": "ok", "config_falha_ativa": _config_falha.model_dump()}


@app.get("/pronto")
async def pronto(response: Response) -> dict[str, Any]:
    """Sonda de prontidão (Aula 11): confirma que a instância pode
    atender tráfego agora — aqui, que o banco está acessível. Uma falha
    aqui apenas tira o Pod dos destinos do Service; não o reinicia."""
    banco_acessivel = await run_in_threadpool(lider.verificar_conexao)
    if not banco_acessivel:
        response.status_code = 503
    return {"pronto": banco_acessivel}
