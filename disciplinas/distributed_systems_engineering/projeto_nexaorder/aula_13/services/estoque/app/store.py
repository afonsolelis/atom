"""Armazenamento do Estoque — a fonte de verdade (líder), Unidade 2, Aula 5.

Toda escrita acontece aqui primeiro, dentro de uma transação: verificar
saldo, decrementar, registrar a reserva. É a invariante mais cara do
sistema — o saldo de um SKU nunca fica negativo — e ela só pode ser
garantida no líder, nunca na réplica de leitura.
"""

from __future__ import annotations

import sqlite3
import uuid
from pathlib import Path
from typing import Any

ESQUEMA = """
CREATE TABLE IF NOT EXISTS saldo (
    sku TEXT PRIMARY KEY,
    quantidade INTEGER NOT NULL CHECK (quantidade >= 0)
);
CREATE TABLE IF NOT EXISTS reservas (
    id TEXT PRIMARY KEY,
    pedido_id TEXT NOT NULL,
    sku TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    estado TEXT NOT NULL
);
"""


class SaldoInsuficiente(Exception):
    pass


class ArmazenLider:
    """Único escritor de saldo e reservas — o "líder" da Aula 5."""

    def __init__(self, caminho_banco: str | Path) -> None:
        self._caminho = str(caminho_banco)
        with self._conectar() as conexao:
            conexao.executescript(ESQUEMA)

    def _conectar(self) -> sqlite3.Connection:
        conexao = sqlite3.connect(self._caminho)
        conexao.row_factory = sqlite3.Row
        conexao.execute("PRAGMA foreign_keys = ON")
        return conexao

    def verificar_conexao(self) -> bool:
        """Usado pela sonda de prontidão (Aula 11): confirma que o banco
        está acessível, não apenas que o processo está vivo."""
        try:
            with self._conectar() as conexao:
                conexao.execute("SELECT 1")
            return True
        except sqlite3.Error:
            return False

    def definir_saldo_inicial(self, sku: str, quantidade: int) -> None:
        with self._conectar() as conexao:
            conexao.execute(
                """
                INSERT INTO saldo (sku, quantidade) VALUES (?, ?)
                ON CONFLICT(sku) DO UPDATE SET quantidade = excluded.quantidade
                """,
                (sku, quantidade),
            )

    def saldo_atual(self, sku: str) -> int | None:
        with self._conectar() as conexao:
            linha = conexao.execute(
                "SELECT quantidade FROM saldo WHERE sku = ?", (sku,)
            ).fetchone()
        return linha["quantidade"] if linha else None

    def reservar(self, pedido_id: str, sku: str, quantidade: int) -> dict[str, Any]:
        """Transação atômica: verifica, decrementa e registra — nesta ordem,
        na mesma conexão, para que a invariante de saldo não-negativo nunca
        seja violada mesmo sob chamadas concorrentes."""
        with self._conectar() as conexao:
            linha = conexao.execute(
                "SELECT quantidade FROM saldo WHERE sku = ?", (sku,)
            ).fetchone()
            disponivel = linha["quantidade"] if linha else 0
            if disponivel < quantidade:
                raise SaldoInsuficiente(
                    f"saldo insuficiente para {sku}: disponível {disponivel}, solicitado {quantidade}"
                )

            novo_saldo = disponivel - quantidade
            if linha is None:
                conexao.execute("INSERT INTO saldo (sku, quantidade) VALUES (?, ?)", (sku, novo_saldo))
            else:
                conexao.execute("UPDATE saldo SET quantidade = ? WHERE sku = ?", (novo_saldo, sku))

            reserva_id = str(uuid.uuid4())
            conexao.execute(
                "INSERT INTO reservas (id, pedido_id, sku, quantidade, estado) VALUES (?, ?, ?, ?, ?)",
                (reserva_id, pedido_id, sku, quantidade, "ATIVA"),
            )

        return {"reserva_id": reserva_id, "novo_saldo": novo_saldo}

    def liberar_reserva(self, reserva_id: str) -> dict[str, Any] | None:
        """Compensação da Aula 8: devolve a quantidade ao saldo e marca a
        reserva como liberada. Só age sobre reservas ainda ATIVAs — liberar
        uma reserva já liberada não deve devolver saldo duas vezes."""
        with self._conectar() as conexao:
            linha = conexao.execute(
                "SELECT * FROM reservas WHERE id = ? AND estado = 'ATIVA'", (reserva_id,)
            ).fetchone()
            if linha is None:
                return None

            conexao.execute(
                "UPDATE saldo SET quantidade = quantidade + ? WHERE sku = ?",
                (linha["quantidade"], linha["sku"]),
            )
            conexao.execute(
                "UPDATE reservas SET estado = 'LIBERADA' WHERE id = ?", (reserva_id,)
            )
            novo_saldo = conexao.execute(
                "SELECT quantidade FROM saldo WHERE sku = ?", (linha["sku"],)
            ).fetchone()["quantidade"]

        return {"reserva_id": reserva_id, "estado": "LIBERADA", "sku": linha["sku"], "novo_saldo": novo_saldo}

    def listar_por_pedido(self, pedido_id: str) -> list[dict[str, Any]]:
        """Usado pelo gateway (Aula 9) para compor a visão consolidada de
        um pedido sem que o cliente precise conhecer o serviço de estoque."""
        with self._conectar() as conexao:
            linhas = conexao.execute(
                "SELECT * FROM reservas WHERE pedido_id = ?", (pedido_id,)
            ).fetchall()
        return [dict(linha) for linha in linhas]
