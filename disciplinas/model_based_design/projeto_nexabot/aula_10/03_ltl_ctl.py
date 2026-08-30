#!/usr/bin/env python3
"""Aula 10 — Script 03: segurança x vivacidade, na prática, sobre o mesmo modelo.

O que este script faz
----------------------
Explica a diferença clássica entre propriedade de SEGURANÇA ("nada de ruim
acontece" — G(¬ruim), sempre refutável por um contraexemplo FINITO) e
propriedade de VIVACIDADE ("algo bom eventualmente acontece" — F(bom) ou
G(p -> F q), que em geral só é refutável por um contraexemplo INFINITO, um
ciclo que evita para sempre o estado bom). Mostra as duas categorias com
requisitos reais do NexaBot e, por o supervisor ser determinístico, verifica
ambas exaustivamente sobre o mesmo espaço de estados do `modelcheck.py`.

Como rodar
----------
    .venv/bin/python aula_10/03_ltl_ctl.py

Saída esperada (resumo)
------------------------
Uma tabela comparando REQ-SAFE-001/002/004 (segurança) com REQ-SAFE-005
(vivacidade), incluindo, para a vivacidade, uma demonstração de como um
CICLO no grafo de estados seria o contraexemplo (e por que ele não existe
aqui).
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.modelcheck import explorar, verificar_invariantes  # noqa: E402
from nexabot.requisitos import REQ_SAFE_001, REQ_SAFE_002, REQ_SAFE_004, REQ_SAFE_005  # noqa: E402
from nexabot.supervisor import Entradas, Estado  # noqa: E402


def explicacao() -> None:
    print("Segurança (\"safety\", LTL: G ¬ruim):")
    print("  - 'Nada de ruim jamais acontece.'")
    print("  - Contraexemplo é sempre um caminho FINITO até o estado ruim.")
    print("  - Ex.: REQ-SAFE-001, REQ-SAFE-002 (invariantes) e REQ-SAFE-004")
    print("    ('só sai de FALHA por rearme' — é uma restrição sobre TODA")
    print("    transição, não sobre um estado isolado).")
    print()
    print("Vivacidade (\"liveness\", LTL: G(p -> F q)):")
    print("  - 'Sempre que p acontece, eventualmente q acontece depois.'")
    print("  - Contraexemplo em geral é um caminho INFINITO — um ciclo (lasso)")
    print("    alcançável que nunca passa por q. Não dá para refutar vivacidade")
    print("    olhando só um prefixo finito de execução.")
    print("  - Ex.: REQ-SAFE-005 ('obstáculo removido + partida => MOVENDO').")


def demonstrar_seguranca() -> None:
    print("\n" + "-" * 78)
    print("Verificação de SEGURANÇA (REQ-SAFE-001, 002, 004)")
    print("-" * 78)
    resultado = explorar()
    for req in (REQ_SAFE_001, REQ_SAFE_002, REQ_SAFE_004):
        violacoes = verificar_invariantes(resultado, [req])
        print(f"  {req.id} ({req.tipo}): {len(violacoes)} violação(ões) em {resultado.n_transicoes} transições")
    print("\n  Cada verificação aqui é local: olhamos toda transição isoladamente,")
    print("  sem precisar seguir caminho algum até o infinito.")


def demonstrar_vivacidade() -> None:
    print("\n" + "-" * 78)
    print("Verificação de VIVACIDADE (REQ-SAFE-005)")
    print("-" * 78)
    resultado = explorar()
    violacoes = verificar_invariantes(resultado, [REQ_SAFE_005])
    print(f"  {REQ_SAFE_005.id}: {len(violacoes)} violação(ões)")
    print(
        "\n  Como o supervisor é DETERMINÍSTICO, 'eventualmente' colapsa em"
        "\n  'na PRÓXIMA transição': não existe not-determinismo que permita"
        "\n  adiar a resposta para depois, então a propriedade de vivacidade"
        "\n  pôde ser checada transição a transição, como uma invariante."
    )

    print("\n  Para tornar isso concreto: um SUPERVISOR BUGADO que violasse")
    print("  vivacidade teria um ciclo que evita MOVENDO para sempre. Vamos")
    print("  construir um e mostrar o ciclo (sem alterar o supervisor real):")

    def transition_trava_obstaculo(estado, entradas):
        # Variante hipotética: uma vez em PARADO_OBSTACULO, NUNCA mais sai,
        # mesmo com o obstáculo removido e comando de partida — um bug de
        # vivacidade clássico ("estado absorvente indevido").
        from nexabot.supervisor import Saidas

        if estado is Estado.PARADO_OBSTACULO:
            return Estado.PARADO_OBSTACULO, Saidas(torque_habilitado=False, freio_acionado=True)
        from nexabot.supervisor import transition as transicao_real

        return transicao_real(estado, entradas)

    resultado_bug = explorar(transition_fn=transition_trava_obstaculo)
    entrada_livre = Entradas(comando_partir=True, obstaculo=False)
    destino, _ = transition_trava_obstaculo(Estado.PARADO_OBSTACULO, entrada_livre)
    print(
        f"\n  Nessa variante, a partir de PARADO_OBSTACULO com obstáculo=False e"
        f"\n  comando_partir=True, o próximo estado é {destino.name} (deveria"
        f"\n  ser MOVENDO) — PARADO_OBSTACULO virou um ciclo de tamanho 1 que"
        f"\n  nunca alcança MOVENDO. Isto é exatamente o 'lasso' que um"
        f"\n  verificador de LTL relataria como contraexemplo de vivacidade."
    )
    violacoes_bug = verificar_invariantes(resultado_bug, [REQ_SAFE_005])
    print(f"\n  Verificando REQ-SAFE-005 nessa variante: {len(violacoes_bug)} violação(ões) (esperado: > 0)")
    assert len(violacoes_bug) > 0


def main() -> None:
    print("=" * 78)
    print("AULA 10 — Segurança x Vivacidade, na prática")
    print("=" * 78)
    print()
    explicacao()
    demonstrar_seguranca()
    demonstrar_vivacidade()


if __name__ == "__main__":
    main()
