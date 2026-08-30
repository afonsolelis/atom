#!/usr/bin/env python3
"""Aula 12 — Script 03: a máquina de estados do hypothesis, ao vivo, achando e reduzindo um bug.

O que este script faz
----------------------
1. Roda `nexabot.mbt.SupervisorMachine` (hypothesis.stateful) contra o
   supervisor CORRETO: sorteia sequências de entradas e verifica os
   requisitos formais a cada passo — deve passar sempre.
2. Roda a MESMA técnica contra uma variante bugada do supervisor (o mesmo
   bug de prioridade da Aula 10 — comando_partir verificado antes do
   obstáculo em MOVENDO) e mostra o CASO REDUZIDO ("shrunk") que o
   hypothesis encontra: a sequência mínima de entradas que ainda viola
   REQ-SAFE-001.

Como rodar
----------
    .venv/bin/python aula_12/03_hypothesis.py

Saída esperada (resumo)
------------------------
Passo 1: "OK, nenhuma falha em N execuções aleatórias." Passo 2: uma
AssertionError de REQ-SAFE-001, com o hypothesis reduzindo a sequência de
entradas até o menor caso que ainda reproduz a falha (tipicamente 2 passos:
partir, depois obstáculo+partir simultâneos).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hypothesis import strategies as st  # noqa: E402
from hypothesis.stateful import RuleBasedStateMachine, rule  # noqa: E402

from nexabot.mbt import TestSupervisorMachine  # noqa: E402
from nexabot.requisitos import REQUISITOS_TRANSICAO  # noqa: E402
from nexabot.supervisor import ESTADO_INICIAL, Entradas, Estado, Saidas  # noqa: E402

_BOOL = st.booleans()
_VEL = st.floats(min_value=0.0, max_value=1.5, allow_nan=False, allow_infinity=False)


def _transition_com_bug(estado: Estado, entradas: Entradas):
    """O mesmo bug de `aula_10/02_contraexemplo.py`: comando_partir checado
    antes do obstáculo dentro de MOVENDO — reabilita torque com obstáculo
    presente, violando REQ-SAFE-001."""
    from nexabot.supervisor import transition as _correta

    if estado is Estado.MOVENDO:
        if entradas.comando_partir:
            return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)
    return _correta(estado, entradas)


class _MaquinaBugada(RuleBasedStateMachine):
    """Cópia de `nexabot.mbt.SupervisorMachine` usando `_transition_com_bug`."""

    def __init__(self) -> None:
        super().__init__()
        self.estado = ESTADO_INICIAL

    @rule(
        comando_partir=_BOOL,
        comando_parar=_BOOL,
        obstaculo=_BOOL,
        emergencia=_BOOL,
        falha_encoder=_BOOL,
        rearme=_BOOL,
        velocidade=_VEL,
    )
    def passo(self, comando_partir, comando_parar, obstaculo, emergencia, falha_encoder, rearme, velocidade):
        entrada = Entradas(
            comando_partir=comando_partir,
            comando_parar=comando_parar,
            obstaculo=obstaculo,
            emergencia=emergencia,
            falha_encoder=falha_encoder,
            rearme=rearme,
            velocidade=velocidade,
        )
        estado_antes = self.estado
        estado_depois, saida = _transition_com_bug(estado_antes, entrada)
        self.estado = estado_depois
        for req in REQUISITOS_TRANSICAO:
            assert req.verificar_transicao(estado_antes, entrada, saida, estado_depois), (
                f"{req.id} violado: {estado_antes.name} --[{entrada}]--> {estado_depois.name} "
                f"(saida={saida})"
            )


def main() -> None:
    print("=" * 78)
    print("AULA 12 — Hypothesis stateful: achar e reduzir um contraexemplo")
    print("=" * 78)

    print("\n[1] Supervisor CORRETO — rodando a máquina de estados do hypothesis...")
    try:
        TestSupervisorMachine().runTest()
        print("    OK — nenhuma violação encontrada em nenhuma sequência sorteada.")
    except AssertionError as exc:  # pragma: no cover - não deveria acontecer
        print(f"    FALHA INESPERADA: {exc}")
        raise

    print("\n[2] Supervisor BUGADO — mesma técnica, variante com bug injetado...")
    try:
        _MaquinaBugada.TestCase().runTest()
        print("    (inesperado: nenhuma falha encontrada na versão bugada)")
    except AssertionError as exc:
        print("    FALHA ENCONTRADA (esperado!) — hypothesis reduziu ao menor caso:")
        print(f"    {exc}")

    print(
        "\nCONCLUSÃO: hypothesis.stateful não substitui os casos gerados por"
        "\ncobertura (Aula 12/01) — ele os complementa, sorteando sequências"
        "\nlongas e inesperadas que a geração estruturada não cobriria, e"
        "\nreduzindo automaticamente qualquer falha ao menor caso reprodutível."
    )


if __name__ == "__main__":
    main()
