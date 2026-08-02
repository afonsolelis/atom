"""Triagem local vs. avaliação central — Unidade 4, Aula 15.

Implementa a resposta madura da pausa para reflexão do roteiro ("vamos
processar tudo na borda"): não tudo na borda, não tudo no centro. Sinais
simples e locais bloqueiam na borda, sem esperar por um serviço central;
sinais que dependem de contexto histórico agregado — a contagem de
tentativas na janela por tempo de evento (`app/janela_evento.py`), o
histórico do dispositivo em outras regiões — exigem avaliação central,
porque nenhum ponto de borda isolado possui esse contexto sozinho.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class Decisao(str, Enum):
    BLOQUEAR = "BLOQUEAR"
    ENCAMINHAR_PARA_CENTRAL = "ENCAMINHAR_PARA_CENTRAL"
    LIBERAR = "LIBERAR"


@dataclass
class Tentativa:
    dispositivo_id: str
    numero_cartao_hash: str
    cartoes_testados_nesta_sessao: int  # sinal simples, disponível na própria borda


LIMITE_CARTOES_NA_BORDA = 3  # sinal simples e local: N cartões distintos na mesma sessão


def triagem_local(tentativa: Tentativa) -> Decisao:
    """Decide só com sinais que a própria borda já tem, sem chamar o
    centro — é o que torna a triagem local rápida. Um único cartão testado
    não é, sozinho, sinal suficiente para bloquear: precisa do contexto
    histórico que só a avaliação central tem."""
    if tentativa.cartoes_testados_nesta_sessao >= LIMITE_CARTOES_NA_BORDA:
        return Decisao.BLOQUEAR
    return Decisao.ENCAMINHAR_PARA_CENTRAL


def avaliacao_central(contagem_na_janela_de_evento: int, limite_da_janela: int) -> Decisao:
    """Usa contexto que só o centro tem: a contagem agregada na janela por
    tempo de evento, que depende do histórico recente do dispositivo em
    todas as regiões — não só na que o atendeu (o exemplo do roteiro:
    quarenta cartões em 24h, em cinco cidades diferentes)."""
    if contagem_na_janela_de_evento >= limite_da_janela:
        return Decisao.BLOQUEAR
    return Decisao.LIBERAR
