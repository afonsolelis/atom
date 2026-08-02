"""Persistência do serviço Pagamento — banco próprio, como todos os outros."""

from __future__ import annotations

import sqlite3
import uuid
from pathlib import Path
from typing import Any

ESQUEMA = """
CREATE TABLE IF NOT EXISTS cobrancas (
    id TEXT PRIMARY KEY,
    pedido_id TEXT NOT NULL,
    chave_idempotencia TEXT NOT NULL UNIQUE,
    valor REAL NOT NULL,
    estado TEXT NOT NULL,
    referencia_externa TEXT
);
"""


class RepositorioPagamento:
    def __init__(self, caminho_banco: str | Path) -> None:
        self._caminho = str(caminho_banco)
        with self._conectar() as conexao:
            conexao.executescript(ESQUEMA)

    def _conectar(self) -> sqlite3.Connection:
        conexao = sqlite3.connect(self._caminho)
        conexao.row_factory = sqlite3.Row
        return conexao

    def obter_por_chave_idempotencia(self, chave: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            linha = conexao.execute(
                "SELECT * FROM cobrancas WHERE chave_idempotencia = ?", (chave,)
            ).fetchone()
        return dict(linha) if linha else None

    def criar_cobranca(
        self, pedido_id: str, chave_idempotencia: str, valor: float, estado: str, referencia_externa: str
    ) -> dict[str, Any]:
        cobranca_id = str(uuid.uuid4())
        with self._conectar() as conexao:
            conexao.execute(
                """
                INSERT INTO cobrancas
                    (id, pedido_id, chave_idempotencia, valor, estado, referencia_externa)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (cobranca_id, pedido_id, chave_idempotencia, valor, estado, referencia_externa),
            )
        return {
            "id": cobranca_id,
            "pedido_id": pedido_id,
            "chave_idempotencia": chave_idempotencia,
            "valor": valor,
            "estado": estado,
            "referencia_externa": referencia_externa,
        }

    def obter_por_id(self, cobranca_id: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            linha = conexao.execute("SELECT * FROM cobrancas WHERE id = ?", (cobranca_id,)).fetchone()
        return dict(linha) if linha else None

    def estornar(self, cobranca_id: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            conexao.execute(
                "UPDATE cobrancas SET estado = 'ESTORNADA' WHERE id = ? AND estado = 'AUTORIZADA'",
                (cobranca_id,),
            )
        return self.obter_por_id(cobranca_id)

    def listar_por_pedido(self, pedido_id: str) -> list[dict[str, Any]]:
        with self._conectar() as conexao:
            linhas = conexao.execute(
                "SELECT * FROM cobrancas WHERE pedido_id = ?", (pedido_id,)
            ).fetchall()
        return [dict(linha) for linha in linhas]
