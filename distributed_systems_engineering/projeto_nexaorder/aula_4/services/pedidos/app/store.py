"""Persistência do serviço Pedidos.

Usa SQLite via a biblioteca padrão, em um arquivo próprio deste serviço —
`pedidos.db`. Nenhum outro serviço tem, ou terá, acesso a este arquivo: essa é
a regra de "dados por serviço" que a Aula 9 formaliza, mas que o projeto
já respeita desde a primeira linha de código.

As operações são síncronas (a API do stdlib `sqlite3` é síncrona) e chamadas
a partir de rotas assíncronas via `run_in_threadpool`, para não bloquear o
loop de eventos do FastAPI.
"""

from __future__ import annotations

import json
import sqlite3
from pathlib import Path
from typing import Any


ESQUEMA = """
CREATE TABLE IF NOT EXISTS pedidos (
    id TEXT PRIMARY KEY,
    cliente_id TEXT NOT NULL,
    chave_idempotencia TEXT NOT NULL UNIQUE,
    estado TEXT NOT NULL,
    itens_json TEXT NOT NULL,
    total REAL NOT NULL,
    criado_em TEXT NOT NULL,
    trace_id TEXT NOT NULL,
    carimbo_lamport INTEGER NOT NULL
);
"""


class RepositorioPedidos:
    """Acesso ao banco de dados próprio do serviço Pedidos."""

    def __init__(self, caminho_banco: str | Path) -> None:
        self._caminho = str(caminho_banco)
        with self._conectar() as conexao:
            conexao.executescript(ESQUEMA)

    def _conectar(self) -> sqlite3.Connection:
        conexao = sqlite3.connect(self._caminho)
        conexao.row_factory = sqlite3.Row
        return conexao

    def salvar(self, pedido: dict[str, Any]) -> None:
        with self._conectar() as conexao:
            conexao.execute(
                """
                INSERT INTO pedidos
                    (id, cliente_id, chave_idempotencia, estado, itens_json,
                     total, criado_em, trace_id, carimbo_lamport)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    pedido["id"],
                    pedido["cliente_id"],
                    pedido["chave_idempotencia"],
                    pedido["estado"],
                    json.dumps(pedido["itens"]),
                    pedido["total"],
                    pedido["criado_em"],
                    pedido["trace_id"],
                    pedido["carimbo_lamport"],
                ),
            )

    def obter_por_id(self, pedido_id: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            linha = conexao.execute(
                "SELECT * FROM pedidos WHERE id = ?", (pedido_id,)
            ).fetchone()
        return self._linha_para_dict(linha) if linha else None

    def obter_por_chave_idempotencia(self, chave: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            linha = conexao.execute(
                "SELECT * FROM pedidos WHERE chave_idempotencia = ?", (chave,)
            ).fetchone()
        return self._linha_para_dict(linha) if linha else None

    def atualizar_estado(self, pedido_id: str, novo_estado: str) -> None:
        with self._conectar() as conexao:
            conexao.execute(
                "UPDATE pedidos SET estado = ? WHERE id = ?", (novo_estado, pedido_id)
            )

    @staticmethod
    def _linha_para_dict(linha: sqlite3.Row) -> dict[str, Any]:
        dado = dict(linha)
        dado["itens"] = json.loads(dado.pop("itens_json"))
        return dado
