"""Persistência do serviço Expedição — banco próprio."""

from __future__ import annotations

import sqlite3
import uuid
from pathlib import Path
from typing import Any

ESQUEMA = """
CREATE TABLE IF NOT EXISTS remessas (
    id TEXT PRIMARY KEY,
    pedido_id TEXT NOT NULL,
    chave_idempotencia TEXT NOT NULL UNIQUE,
    estado TEXT NOT NULL,
    codigo_rastreio TEXT
);
"""


class RepositorioExpedicao:
    def __init__(self, caminho_banco: str | Path) -> None:
        self._caminho = str(caminho_banco)
        with self._conectar() as conexao:
            conexao.executescript(ESQUEMA)

    def _conectar(self) -> sqlite3.Connection:
        conexao = sqlite3.connect(self._caminho)
        conexao.row_factory = sqlite3.Row
        return conexao

    def verificar_conexao(self) -> bool:
        """Usado pela sonda de prontidão (Aula 11)."""
        try:
            with self._conectar() as conexao:
                conexao.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False

    def obter_por_chave_idempotencia(self, chave: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            linha = conexao.execute(
                "SELECT * FROM remessas WHERE chave_idempotencia = ?", (chave,)
            ).fetchone()
        return dict(linha) if linha else None

    def criar_remessa(self, pedido_id: str, chave_idempotencia: str) -> dict[str, Any]:
        remessa_id = str(uuid.uuid4())
        codigo_rastreio = f"NX-{uuid.uuid4().hex[:6].upper()}-BR"
        with self._conectar() as conexao:
            conexao.execute(
                """
                INSERT INTO remessas (id, pedido_id, chave_idempotencia, estado, codigo_rastreio)
                VALUES (?, ?, ?, ?, ?)
                """,
                (remessa_id, pedido_id, chave_idempotencia, "ETIQUETA_GERADA", codigo_rastreio),
            )
        return {
            "id": remessa_id,
            "pedido_id": pedido_id,
            "chave_idempotencia": chave_idempotencia,
            "estado": "ETIQUETA_GERADA",
            "codigo_rastreio": codigo_rastreio,
        }

    def obter_por_id(self, remessa_id: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            linha = conexao.execute("SELECT * FROM remessas WHERE id = ?", (remessa_id,)).fetchone()
        return dict(linha) if linha else None

    def cancelar(self, remessa_id: str) -> dict[str, Any] | None:
        with self._conectar() as conexao:
            conexao.execute(
                "UPDATE remessas SET estado = 'CANCELADA' WHERE id = ? AND estado = 'ETIQUETA_GERADA'",
                (remessa_id,),
            )
        return self.obter_por_id(remessa_id)

    def listar_por_pedido(self, pedido_id: str) -> list[dict[str, Any]]:
        with self._conectar() as conexao:
            linhas = conexao.execute(
                "SELECT * FROM remessas WHERE pedido_id = ?", (pedido_id,)
            ).fetchall()
        return [dict(linha) for linha in linhas]
