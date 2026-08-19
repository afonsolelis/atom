"""Segurança entre serviços — Unidade 3, Aula 12.

Duas peças, deliberadamente simplificadas (ver docs/seguranca.md):

1. Identidade verificável por serviço, via token assinado com HMAC — no
   lugar de TLS mútuo real, que exigiria uma autoridade certificadora e
   canal criptografado que este projeto não tem infraestrutura para
   demonstrar. O princípio é o mesmo: a identidade viaja com o chamador,
   não com o endereço de rede.
2. Limitador de taxa por balde de fichas, com os mesmos parâmetros do
   exemplo numérico do roteiro.

Este arquivo é deliberadamente quase idêntico em cada serviço — cada um
mantém sua própria cópia, porque serviços independentes não compartilham
código-fonte entre si (Aula 9), mesmo quando o código é conceitualmente o
mesmo.
"""

from __future__ import annotations

import hashlib
import hmac
import os
import time
from dataclasses import dataclass, field

from fastapi import Header, HTTPException

SEGREDO_ASSINATURA = os.environ.get(
    "NEXAORDER_SEGREDO_ASSINATURA", "segredo-de-desenvolvimento-nao-usar-em-producao"
)


class TokenInvalido(Exception):
    pass


def emitir_token(identidade: str) -> str:
    """Emite um token: identidade + assinatura HMAC-SHA256.

    NÃO é TLS mútuo — não há certificado nem autoridade certificadora.
    É uma simplificação que prova o mesmo princípio (identidade verificável,
    não baseada em endereço de rede) sem exigir PKI. Ver docs/seguranca.md.
    """
    assinatura = hmac.new(SEGREDO_ASSINATURA.encode(), identidade.encode(), hashlib.sha256).hexdigest()
    return f"{identidade}.{assinatura}"


def verificar_token(token: str) -> str:
    """Devolve a identidade do portador, ou levanta TokenInvalido."""
    try:
        identidade, assinatura = token.rsplit(".", 1)
    except ValueError as erro:
        raise TokenInvalido("formato de token inválido") from erro

    assinatura_esperada = hmac.new(
        SEGREDO_ASSINATURA.encode(), identidade.encode(), hashlib.sha256
    ).hexdigest()
    if not hmac.compare_digest(assinatura, assinatura_esperada):
        raise TokenInvalido("assinatura não confere")
    return identidade


def exigir_identidade(identidades_permitidas: set[str]):
    """Fábrica de dependência FastAPI: autentica via cabeçalho Authorization
    e autoriza apenas as identidades explicitamente permitidas — o
    princípio do menor privilégio, aplicado rota a rota."""

    async def verificar(authorization: str | None = Header(default=None)) -> str:
        if authorization is None or not authorization.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="identidade não apresentada")
        token = authorization.removeprefix("Bearer ")
        try:
            identidade = verificar_token(token)
        except TokenInvalido as erro:
            raise HTTPException(status_code=401, detail=str(erro)) from erro
        if identidade not in identidades_permitidas:
            raise HTTPException(
                status_code=403,
                detail=f"'{identidade}' autenticado, mas não autorizado para esta operação",
            )
        return identidade

    return verificar


@dataclass
class BaldeDeFichas:
    """Limitador de taxa — Aula 12. `capacidade` é o pico absorvido,
    `taxa_reposicao_por_segundo` é a taxa sustentável de longo prazo."""

    capacidade: int
    taxa_reposicao_por_segundo: float
    _fichas: float = field(init=False)
    _ultima_reposicao: float = field(init=False)

    def __post_init__(self) -> None:
        self._fichas = float(self.capacidade)
        self._ultima_reposicao = time.monotonic()

    def _repor(self) -> None:
        agora = time.monotonic()
        decorrido = agora - self._ultima_reposicao
        self._fichas = min(self.capacidade, self._fichas + decorrido * self.taxa_reposicao_por_segundo)
        self._ultima_reposicao = agora

    def consumir(self, quantidade: int = 1) -> bool:
        self._repor()
        if self._fichas >= quantidade:
            self._fichas -= quantidade
            return True
        return False

    @property
    def fichas_disponiveis(self) -> float:
        self._repor()
        return self._fichas
