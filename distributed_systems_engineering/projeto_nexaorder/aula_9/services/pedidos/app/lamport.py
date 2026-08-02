"""Relógio lógico de Lamport — Unidade 1, Aula 3.

Implementa as três regras propostas por Lamport (1978) para ordenar eventos por
causalidade, sem depender de relógio físico:

1. Evento local ou envio: incrementa o contador em 1.
2. Ao enviar: o carimbo anexado à mensagem é o do evento de envio.
3. Ao receber: o contador vira max(local, recebido) + 1.

Garantia: se A aconteceu antes de B (na relação happened-before), então
carimbo(A) < carimbo(B). A recíproca não vale — dois eventos concorrentes
podem receber carimbos diferentes sem que um tenha causado o outro. Esse
limite é o motivo de existirem relógios vetoriais (retomados na Aula 6, quando
o projeto precisar detectar concorrência com certeza entre partições).
"""

from __future__ import annotations

import threading


class LamportClock:
    """Contador lógico thread-safe para um único processo."""

    def __init__(self, valor_inicial: int = 0) -> None:
        self._valor = valor_inicial
        self._lock = threading.Lock()

    @property
    def valor(self) -> int:
        with self._lock:
            return self._valor

    def evento_local(self) -> int:
        """Regra 1 — evento que não envolve troca de mensagem."""
        with self._lock:
            self._valor += 1
            return self._valor

    def enviar(self) -> int:
        """Regra 2 — o envio em si também é um evento local; o valor
        resultante é o carimbo que viaja na mensagem."""
        return self.evento_local()

    def receber(self, carimbo_recebido: int) -> int:
        """Regra 3 — ajusta o contador ao receber uma mensagem carimbada."""
        with self._lock:
            self._valor = max(self._valor, carimbo_recebido) + 1
            return self._valor
