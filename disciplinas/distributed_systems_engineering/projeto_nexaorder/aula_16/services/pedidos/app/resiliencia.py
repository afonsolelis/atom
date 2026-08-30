"""Padrões de resiliência — Unidade 1, Aula 4.

Três peças, usadas juntas em `ClienteResiliente`: timeout por tentativa,
retry com backoff exponencial e jitter (mesma fórmula da Aula 2), e um
disjuntor (circuit breaker) com os números do exemplo da Aula 4 — janela de
20 chamadas, limite de 50% de falhas.
"""

from __future__ import annotations

import asyncio
import random
import time
from dataclasses import dataclass, field


class CircuitoAberto(Exception):
    """O disjuntor está aberto: a chamada é rejeitada sem tocar a rede."""


class FalhaTransitoria(Exception):
    """Erro que justifica retentativa: timeout ou 5xx."""


def backoff_com_jitter(
    tentativa: int,
    base_ms: int = 200,
    teto_ms: int = 5000,
    jitter_maximo_ms: int = 100,
) -> float:
    """tempo(n) = min(base × 2^n, teto) + aleatório[0, jitter_máximo) — Aula 2.

    Devolve o tempo de espera em segundos.
    """
    componente_exponencial = min(base_ms * (2**tentativa), teto_ms)
    jitter = random.uniform(0, jitter_maximo_ms)
    return (componente_exponencial + jitter) / 1000


@dataclass
class ConfiguracaoDisjuntor:
    tamanho_janela: int = 20
    limite_taxa_erro: float = 0.5
    intervalo_semiaberto_segundos: float = 5.0


@dataclass
class CircuitBreaker:
    """Estados: fechado, aberto, semiaberto — Aula 4, Slide 11."""

    config: ConfiguracaoDisjuntor = field(default_factory=ConfiguracaoDisjuntor)
    _janela: list[bool] = field(default_factory=list, init=False)
    _estado: str = field(default="fechado", init=False)
    _aberto_desde: float | None = field(default=None, init=False)

    @property
    def estado(self) -> str:
        if self._estado == "aberto" and self._passou_intervalo_de_recuperacao():
            self._estado = "semiaberto"
        return self._estado

    def taxa_de_erro(self) -> float:
        if not self._janela:
            return 0.0
        falhas = self._janela.count(False)
        return falhas / len(self._janela)

    def permite_chamada(self) -> bool:
        return self.estado != "aberto"

    def registrar_sucesso(self) -> None:
        if self._estado == "semiaberto":
            # Estado semiaberto: uma chamada de teste bem-sucedida fecha o disjuntor.
            self._estado = "fechado"
            self._janela.clear()
            self._aberto_desde = None
            return
        self._acumular(True)

    def registrar_falha(self) -> None:
        if self._estado == "semiaberto":
            # Falhou o teste em semiaberto: volta para aberto imediatamente.
            self._abrir()
            return
        self._acumular(False)
        janela_completa = len(self._janela) >= self.config.tamanho_janela
        if janela_completa and self.taxa_de_erro() > self.config.limite_taxa_erro:
            self._abrir()

    def _acumular(self, sucesso: bool) -> None:
        self._janela.append(sucesso)
        if len(self._janela) > self.config.tamanho_janela:
            self._janela.pop(0)

    def _abrir(self) -> None:
        self._estado = "aberto"
        self._aberto_desde = time.monotonic()

    def _passou_intervalo_de_recuperacao(self) -> bool:
        if self._aberto_desde is None:
            return False
        decorrido = time.monotonic() - self._aberto_desde
        return decorrido >= self.config.intervalo_semiaberto_segundos


class ClienteResiliente:
    """Combina timeout, retry com backoff+jitter e disjuntor em uma única
    chamada HTTP. Ver docs/adr/0004-resiliencia-timeout-retry-disjuntor.md."""

    def __init__(
        self,
        cliente_http,
        disjuntor: CircuitBreaker,
        timeout_segundos: float = 1.0,
        max_tentativas: int = 3,
    ) -> None:
        self._cliente = cliente_http
        self._disjuntor = disjuntor
        self._timeout_segundos = timeout_segundos
        self._max_tentativas = max_tentativas

    async def post(self, url: str, json: dict, trace_id: str, cabecalhos_extras: dict[str, str] | None = None):
        import httpx

        if not self._disjuntor.permite_chamada():
            raise CircuitoAberto(f"disjuntor aberto para {url}")

        cabecalhos = {"X-Trace-Id": trace_id, **(cabecalhos_extras or {})}

        ultimo_erro: Exception | None = None
        for tentativa in range(self._max_tentativas):
            try:
                resposta = await self._cliente.post(
                    url,
                    json=json,
                    headers=cabecalhos,
                    timeout=self._timeout_segundos,
                )
                if resposta.status_code >= 500:
                    raise FalhaTransitoria(f"{url} devolveu {resposta.status_code}")
                self._disjuntor.registrar_sucesso()
                return resposta
            # `TransportError`, e não `TimeoutException`: um provedor
            # INDISPONÍVEL não dá timeout, ele recusa a conexão
            # (`httpx.ConnectError`). Até a Aula 13 só o timeout era
            # capturado aqui, e uma indisponibilidade total escapava sem
            # retentativa, sem contar para o disjuntor e sem virar
            # `EtapaFalhou` — o disjuntor nunca abria justamente no caso
            # em que ele mais importa. Foi o experimento de caos da Aula 14,
            # rodado em cluster, que revelou isso
            # (ver docs/testes-e-caos.md e docs/kubernetes-execucao.md).
            except (httpx.TransportError, FalhaTransitoria) as erro:
                ultimo_erro = erro
                self._disjuntor.registrar_falha()
                ultima_tentativa = tentativa == self._max_tentativas - 1
                if ultima_tentativa:
                    raise
                await asyncio.sleep(backoff_com_jitter(tentativa))

        # Inalcançável: o laço sempre retorna ou levanta antes de sair.
        raise ultimo_erro  # pragma: no cover
