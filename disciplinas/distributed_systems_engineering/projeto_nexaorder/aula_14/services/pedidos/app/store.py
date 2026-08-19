"""Persistência do serviço Pedidos.

Usa SQLite via a biblioteca padrão, em um arquivo próprio deste serviço —
`pedidos.db`. Nenhum outro serviço tem, ou terá, acesso a este arquivo: essa é
a regra de "dados por serviço" que a Aula 9 formaliza, mas que o projeto
já respeita desde a primeira linha de código.

As operações são síncronas (a API do stdlib `sqlite3` é síncrona) e chamadas
a partir de rotas assíncronas via `run_in_threadpool`, para não bloquear o
loop de eventos do FastAPI.

A partir da Aula 8, `salvar` também grava um evento pendente na tabela
`outbox`, na mesma transação da escrita de negócio — o padrão outbox, que
resolve o problema da escrita dupla. Ninguém publica esses eventos ainda:
o publicador chega na Aula 10, junto com o broker.
"""

from __future__ import annotations

import json
import sqlite3
import uuid
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
CREATE TABLE IF NOT EXISTS outbox (
    id TEXT PRIMARY KEY,
    pedido_id TEXT NOT NULL,
    tipo TEXT NOT NULL,
    payload_json TEXT NOT NULL,
    criado_em TEXT NOT NULL,
    publicado INTEGER NOT NULL DEFAULT 0
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

    def verificar_conexao(self) -> bool:
        """Usado pela sonda de prontidão (Aula 11)."""
        try:
            with self._conectar() as conexao:
                conexao.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False

    def salvar(self, pedido: dict[str, Any]) -> None:
        """Grava o pedido e o evento PedidoCriado na outbox, na mesma
        transação: os dois existem juntos, ou nenhum dos dois existe."""
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
            payload = {
                "tipo": "PedidoCriado",
                "versao": 1,
                "pedido_id": pedido["id"],
                "trace_id": pedido["trace_id"],
                "ocorrido_em": pedido["criado_em"],
                "dados": {
                    "cliente_id": pedido["cliente_id"],
                    "itens": pedido["itens"],
                    "total": pedido["total"],
                },
            }
            conexao.execute(
                """
                INSERT INTO outbox (id, pedido_id, tipo, payload_json, criado_em, publicado)
                VALUES (?, ?, ?, ?, ?, 0)
                """,
                (str(uuid.uuid4()), pedido["id"], "PedidoCriado", json.dumps(payload), pedido["criado_em"]),
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

    def eventos_pendentes(self) -> list[dict[str, Any]]:
        """Lê os eventos ainda não publicados. Só existe consumidor real a
        partir da Aula 10 — até lá, serve para provar em teste que a
        outbox está sendo alimentada corretamente."""
        with self._conectar() as conexao:
            linhas = conexao.execute(
                "SELECT * FROM outbox WHERE publicado = 0 ORDER BY criado_em"
            ).fetchall()
        return [
            {**dict(linha), "payload": json.loads(linha["payload_json"])}
            for linha in linhas
        ]

    def marcar_publicado(self, evento_id: str) -> None:
        with self._conectar() as conexao:
            conexao.execute("UPDATE outbox SET publicado = 1 WHERE id = ?", (evento_id,))

    @staticmethod
    def _linha_para_dict(linha: sqlite3.Row) -> dict[str, Any]:
        dado = dict(linha)
        dado["itens"] = json.loads(dado.pop("itens_json"))
        return dado
