"""Logs estruturados — Unidade 4, Aula 13.

Substitui texto livre por uma linha JSON por evento, sempre com o trace_id
do contexto anexado. É isso que transforma um log em algo correlacionável,
em vez de um fragmento isolado — o problema central do incidente que abre a
aula: "os logs existem, mas sem um identificador comum que permita
ordená-los e relacioná-los".
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any

from .correlation import obter_trace_id


def construir_registro(nome_evento: str, servico: str, **campos: Any) -> dict[str, Any]:
    """Função pura — o formato do registro, sem o efeito colateral de
    imprimir. Testável sem capturar stdout."""
    return {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "servico": servico,
        "evento": nome_evento,
        "trace_id": obter_trace_id(),
        **campos,
    }


def registrar(nome_evento: str, servico: str, **campos: Any) -> dict[str, Any]:
    """Constrói o registro e o emite como uma linha JSON em stdout — o
    formato que qualquer coletor de log (Fluent Bit, Vector, etc.) processa
    sem depender de parsing frágil de texto livre."""
    registro = construir_registro(nome_evento, servico, **campos)
    print(json.dumps(registro, ensure_ascii=False))
    return registro
