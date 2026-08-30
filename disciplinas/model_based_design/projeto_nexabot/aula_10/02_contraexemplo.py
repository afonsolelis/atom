#!/usr/bin/env python3
"""Aula 10 — Script 02: um bug de verdade, o contraexemplo que o expõe, e a correção.

O que este script faz
----------------------
1. Define `transition_com_bug`, uma variante do supervisor com um erro de
   ordem de prioridade REALISTA: o comando de partida do operador é
   verificado ANTES do sensor de obstáculo (em vez de depois), então um
   `comando_partir=True` chega a religar o torque mesmo com o obstáculo
   ainda presente. É o tipo de bug que passa despercebido em revisão de
   código porque cada bloco, isolado, "parece" correto.
2. Roda o model checker (`nexabot.modelcheck`) contra essa variante e exibe
   o CONTRAEXEMPLO exato: a sequência de (estado, entrada) da inicial até a
   violação de REQ-SAFE-001.
3. Roda o mesmo checker contra a versão corrigida (`nexabot.supervisor`,
   sem o bug) e mostra 0 violações — a correção ao vivo.

Como rodar
----------
    .venv/bin/python aula_10/02_contraexemplo.py

Saída esperada (resumo)
------------------------
Para a versão com bug: pelo menos 1 violação de REQ-SAFE-001, com o
contraexemplo impresso passo a passo. Para a versão corrigida: 0 violações.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.modelcheck import explorar, formatar_caminho, verificar_invariantes  # noqa: E402
from nexabot.requisitos import REQ_SAFE_001  # noqa: E402
from nexabot.supervisor import Entradas, Estado, Saidas, transition  # noqa: E402


def transition_com_bug(estado: Estado, entradas: Entradas) -> tuple[Estado, Saidas]:
    """Variante BUGADA de `nexabot.supervisor.transition`.

    O bug: dentro do bloco de MOVENDO, o `comando_partir` (que não deveria
    fazer sentido nenhum estando já em MOVENDO, mas aparece aqui por causa
    de um copy-paste malfeito do bloco de PARADO_OBSTACULO) é verificado
    ANTES do obstáculo, então ele "reabilita" o torque incondicionalmente.
    Isso é exatamente o tipo de erro de refatoração que acontece quando
    alguém reordena blocos "só para deixar mais legível" sem rodar o
    verificador de novo.
    """
    if entradas.emergencia:
        return Estado.EMERGENCIA, Saidas(torque_habilitado=False, freio_acionado=True)
    if estado is Estado.EMERGENCIA:
        novo = Estado.OCIOSO if entradas.rearme else Estado.EMERGENCIA
        return novo, Saidas(torque_habilitado=False, freio_acionado=True)
    if entradas.falha_encoder:
        return Estado.FALHA, Saidas(torque_habilitado=False, freio_acionado=True)
    if estado is Estado.FALHA:
        novo = Estado.OCIOSO if entradas.rearme else Estado.FALHA
        return novo, Saidas(torque_habilitado=False, freio_acionado=True)

    if estado is Estado.OCIOSO:
        if entradas.obstaculo:
            return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)
        if entradas.comando_partir:
            return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)
        return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)

    if estado is Estado.MOVENDO:
        # <<< BUG: comando_partir checado antes do obstáculo >>>
        if entradas.comando_partir:
            return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)
        if entradas.obstaculo:
            return Estado.PARADO_OBSTACULO, Saidas(torque_habilitado=False, freio_acionado=True)
        if entradas.comando_parar:
            return Estado.DESACELERANDO, Saidas(torque_habilitado=False, freio_acionado=True)
        return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)

    if estado is Estado.DESACELERANDO:
        if entradas.obstaculo:
            return Estado.PARADO_OBSTACULO, Saidas(torque_habilitado=False, freio_acionado=True)
        if entradas.parado():
            return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)
        return Estado.DESACELERANDO, Saidas(torque_habilitado=False, freio_acionado=True)

    if estado is Estado.PARADO_OBSTACULO:
        if entradas.obstaculo:
            return Estado.PARADO_OBSTACULO, Saidas(torque_habilitado=False, freio_acionado=True)
        if entradas.comando_partir:
            return Estado.MOVENDO, Saidas(torque_habilitado=True, freio_acionado=False)
        return Estado.OCIOSO, Saidas(torque_habilitado=False, freio_acionado=False)

    raise AssertionError(f"estado não tratado: {estado!r}")


def main() -> None:
    print("=" * 78)
    print("AULA 10 — Um bug real, o contraexemplo, e a correção")
    print("=" * 78)

    print("\n[1] Rodando o model checker contra a versão COM BUG (transition_com_bug)...\n")
    resultado_bug = explorar(transition_fn=transition_com_bug)
    violacoes_bug = verificar_invariantes(resultado_bug, [REQ_SAFE_001])
    print(f"    Transições exploradas: {resultado_bug.n_transicoes}")
    print(f"    Violações de {REQ_SAFE_001.id}: {len(violacoes_bug)}")

    if violacoes_bug:
        print("\n    CONTRAEXEMPLO (da inicial até a violação):\n")
        print(formatar_caminho(violacoes_bug[0].caminho))
        t = violacoes_bug[0].caminho[-1]
        print(
            f"\n    Na transição final: estado={t.origem.name}, "
            f"obstaculo={t.entrada.obstaculo}, comando_partir={t.entrada.comando_partir} "
            f"=> saida.torque_habilitado={t.saida.torque_habilitado} "
            f"(deveria ser False!)"
        )
    else:
        print("    (inesperado: nenhuma violação encontrada na versão com bug)")

    print("\n[2] Rodando o mesmo checker contra a versão CORRIGIDA (nexabot.supervisor)...\n")
    resultado_ok = explorar(transition_fn=transition)
    violacoes_ok = verificar_invariantes(resultado_ok, [REQ_SAFE_001])
    print(f"    Transições exploradas: {resultado_ok.n_transicoes}")
    print(f"    Violações de {REQ_SAFE_001.id}: {len(violacoes_ok)}")

    print("\n[3] A correção (diff conceitual):")
    print("    ANTES (bugado):  if comando_partir: ...        # 1º")
    print("                     if obstaculo: ...              # 2º")
    print("    DEPOIS (correto): if obstaculo: ...             # 1º — obstáculo manda")
    print("                      if comando_parar: ...         # 2º")
    print("                      (comando_partir nem é testado em MOVENDO)")

    print(
        f"\nRESUMO: bugada={len(violacoes_bug)} violação(ões) | "
        f"corrigida={len(violacoes_ok)} violação(ões)."
    )
    assert len(violacoes_bug) > 0, "o bug deveria ser detectável"
    assert len(violacoes_ok) == 0, "a versão corrigida não deveria violar REQ-SAFE-001"


if __name__ == "__main__":
    main()
