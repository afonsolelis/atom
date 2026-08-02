"""SLI, SLO e orçamento de erro — Unidade 4, Aula 13.

Um SLO por si só não orienta nenhuma decisão; o orçamento de erro que dele
decorre, sim. Reproduz o exemplo numérico do roteiro: volume de 12 milhões
de requisições por mês, SLO de 99,9%, e o consumo observado nos primeiros
10 dias — a leitura que orienta adiar um lançamento, não uma opinião sobre
o que seria "razoavelmente seguro".
"""

from __future__ import annotations

import math


def orcamento_de_erro(volume_do_periodo: int, slo: float) -> int:
    """Número de falhas toleradas no período, dado o SLO. `1 - slo` é a
    fração do volume que ainda cumpre o objetivo mesmo falhando."""
    return round((1 - slo) * volume_do_periodo)


def fracao_consumida(falhas_consumidas: int, orcamento_total: int) -> float:
    return falhas_consumidas / orcamento_total


def dia_estimado_de_esgotamento(falhas_consumidas: int, orcamento_total: int, dias_decorridos: int) -> int:
    """Projeção linear simples: mantido o ritmo observado até agora, em
    que dia do período o orçamento chegaria a zero. Não é uma previsão
    precisa — é o número que transforma "estamos consumindo rápido demais"
    de sensação em critério operacional (ver docs/observabilidade.md)."""
    taxa_diaria = falhas_consumidas / dias_decorridos
    return math.ceil(orcamento_total / taxa_diaria)


def sli_proporcao(resultados_bons: int, total: int) -> float:
    """Um SLI é sempre uma proporção sobre o resultado observado pelo
    cliente — checkout concluído, latência dentro do limite, pagamento
    confirmado na primeira tentativa — nunca uma métrica de recurso de
    máquina como utilização de CPU (o erro comum do roteiro)."""
    if total == 0:
        return 1.0
    return resultados_bons / total
