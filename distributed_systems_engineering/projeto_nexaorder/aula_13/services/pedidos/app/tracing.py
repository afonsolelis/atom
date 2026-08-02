"""Tracing distribuído local — Unidade 4, Aula 13.

Em uma implantação real, um coletor central (Jaeger, Tempo, o backend por
trás do OpenTelemetry) agregaria os spans relatados por múltiplos
processos. Aqui, cada serviço mede e guarda os seus próprios spans em
memória, indexados por trace_id, e os expõe via `GET /_admin/spans/{trace_id}`
— a reconstrução da cascata entre serviços acontece do lado de fora, em
`scripts/reconstruir_trace.py` (ver docs/adr/0013-spans-locais-sem-coletor-central.md
para o porquê de não integrar um coletor real).

`iniciar_span` mede duração real com `time.perf_counter()` — os spans
produzidos aqui não são números inventados, são a duração de código que
realmente executou.
"""

from __future__ import annotations

import time
import uuid
from contextvars import ContextVar
from dataclasses import dataclass

from .correlation import obter_trace_id

_span_pai_atual: ContextVar[str | None] = ContextVar("span_pai_atual", default=None)


@dataclass
class Span:
    nome: str
    servico: str
    trace_id: str
    span_id: str
    span_pai_id: str | None
    inicio_ms: float
    fim_ms: float | None = None

    @property
    def duracao_ms(self) -> float:
        if self.fim_ms is None:
            raise ValueError("span ainda não foi finalizado")
        return self.fim_ms - self.inicio_ms

    def para_dict(self) -> dict:
        return {
            "nome": self.nome,
            "servico": self.servico,
            "trace_id": self.trace_id,
            "span_id": self.span_id,
            "span_pai_id": self.span_pai_id,
            "inicio_ms": self.inicio_ms,
            "fim_ms": self.fim_ms,
            "duracao_ms": self.duracao_ms,
        }


class ColetorDeSpans:
    """Guarda os spans finalizados deste processo, agrupados por
    trace_id — o suficiente para responder "o que aconteceu com este
    pedido específico", sem exigir um backend externo."""

    def __init__(self) -> None:
        self._spans: dict[str, list[Span]] = {}

    def registrar(self, span: Span) -> None:
        self._spans.setdefault(span.trace_id, []).append(span)

    def spans_do_trace(self, trace_id: str) -> list[dict]:
        return [s.para_dict() for s in self._spans.get(trace_id, [])]


class iniciar_span:
    """Gerenciador de contexto — síncrono e assíncrono — que mede a
    duração real de um trecho de código e registra o span no coletor
    informado. Aninha automaticamente sob o span pai do contexto atual, se
    houver, por meio de uma `ContextVar` — o mesmo mecanismo de propagação
    implícita usado por `correlation.py` desde a Aula 3."""

    def __init__(self, coletor: ColetorDeSpans, nome: str, servico: str) -> None:
        self._coletor = coletor
        self._nome = nome
        self._servico = servico
        self._token = None
        self._span: Span | None = None

    def _iniciar(self) -> Span:
        pai = _span_pai_atual.get()
        self._span = Span(
            nome=self._nome,
            servico=self._servico,
            trace_id=obter_trace_id(),
            span_id=uuid.uuid4().hex[:16],
            span_pai_id=pai,
            inicio_ms=time.perf_counter() * 1000,
        )
        self._token = _span_pai_atual.set(self._span.span_id)
        return self._span

    def _finalizar(self) -> None:
        assert self._span is not None
        self._span.fim_ms = time.perf_counter() * 1000
        self._coletor.registrar(self._span)
        _span_pai_atual.reset(self._token)

    def __enter__(self) -> Span:
        return self._iniciar()

    def __exit__(self, *_exc: object) -> None:
        self._finalizar()

    async def __aenter__(self) -> Span:
        return self._iniciar()

    async def __aexit__(self, *_exc: object) -> None:
        self._finalizar()
