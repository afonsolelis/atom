"""Geração automática de código C do controlador PID do NexaBot (Unidade 4).

Este pacote é o elo "modelo -> código" da disciplina: `derive.py` deriva
simbolicamente as equações de diferenças do PID discreto a partir da forma
contínua (com SymPy), e `generate.py` usa essa derivação, os ganhos e os
parâmetros de `nexabot.params`/`nexabot.controllers` para renderizar C
portável pelos templates Jinja2 em `templates/`.

Rastreabilidade: REQ-CTRL-001, REQ-CTRL-002, REQ-CTRL-003, REQ-CODEGEN-001
(o código gerado deve ser matematicamente equivalente ao modelo de
referência `DiscretePID`), REQ-CODEGEN-002 (rastreabilidade automática no
cabeçalho do arquivo gerado).
"""

from __future__ import annotations

__all__ = ["derive", "generate"]
