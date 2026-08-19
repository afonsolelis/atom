"""Prova o dimensionamento de partições do exemplo numérico da Aula 15
(Slide 7) e que tentativas do mesmo dispositivo caem sempre na mesma
partição — a mesma propriedade da Aula 10, aplicada a uma chave diferente."""

from __future__ import annotations

from app.barramento import Topico
from app.eventos_dispositivo import (
    CAPACIDADE_POR_PARTICAO_POR_SEGUNDO,
    NOME_TOPICO_TENTATIVAS,
    NUM_PARTICOES_TENTATIVAS,
    TAXA_DE_PICO_TENTATIVAS_POR_SEGUNDO,
    publicar_tentativa,
)


def test_numero_minimo_de_particoes_do_exemplo_da_aula_15():
    """5.000 tentativas/s de pico, 750/s de capacidade por partição -> 7."""
    assert TAXA_DE_PICO_TENTATIVAS_POR_SEGUNDO == 5_000
    assert CAPACIDADE_POR_PARTICAO_POR_SEGUNDO == 750
    assert NUM_PARTICOES_TENTATIVAS == 7


def test_tentativas_do_mesmo_dispositivo_caem_sempre_na_mesma_particao():
    topico = Topico(NOME_TOPICO_TENTATIVAS, NUM_PARTICOES_TENTATIVAS)

    for i in range(5):
        publicar_tentativa(topico, "disp-1", {"tempo_evento_ms": i * 1000})

    particao = topico.particao_da_chave("disp-1")
    assert topico.tamanho_particao(particao) == 5


def test_tentativas_de_dispositivos_diferentes_preservam_ordem_por_dispositivo():
    """A propriedade que a Aula 15 exige: os eventos de UM dispositivo
    chegam em ordem à mesma partição — mesmo com outros dispositivos
    publicando eventos intercalados no mesmo tópico."""
    topico = Topico(NOME_TOPICO_TENTATIVAS, NUM_PARTICOES_TENTATIVAS)

    for i in range(4):
        publicar_tentativa(topico, "disp-1", {"seq": i})
        publicar_tentativa(topico, "disp-2", {"seq": i})

    particao_disp1 = topico.particao_da_chave("disp-1")
    eventos_disp1 = [e for e in topico.ler_particao(particao_disp1) if e.chave == "disp-1"]

    assert [e.payload["seq"] for e in eventos_disp1] == [0, 1, 2, 3]
