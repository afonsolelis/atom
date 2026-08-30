#!/usr/bin/env python3
"""Aula 09 — Script 02: de um requisito ambíguo em texto livre à propriedade formal.

O que este script faz
----------------------
Mostra um requisito de segurança tal como ele apareceria numa especificação
de sistema real — em português corrido, cheio de ambiguidade — e a sua
formalização como predicado Python. Em seguida conta a história real (não
hipotética!) de como o model checker desta disciplina *encontrou* uma
ambiguidade na primeira formalização de REQ-SAFE-005 e obrigou a corrigi-la.

Como rodar
----------
    .venv/bin/python aula_09/02_do_texto_a_propriedade.py

Saída esperada (resumo)
------------------------
O texto ambíguo, a primeira formalização (ingênua), o contraexemplo real que
o model checker encontrou contra ela, e a formalização corrigida — que é a
que está de fato em `nexabot/requisitos.py`.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.modelcheck import explorar, formatar_caminho, reconstruir_caminho  # noqa: E402
from nexabot.requisitos import REQ_SAFE_005  # noqa: E402
from nexabot.supervisor import Entradas, Estado  # noqa: E402

TEXTO_AMBIGUO = (
    '"Se o obstáculo for removido e o operador comandar a partida, o AGV '
    'deve voltar a se mover."'
)


def _req_safe_005_ingenua(estado, entradas, saida, proximo) -> bool:
    """Primeira tentativa de formalização — tradução literal do texto acima."""
    if estado is Estado.PARADO_OBSTACULO and not entradas.obstaculo and entradas.comando_partir:
        return proximo is Estado.MOVENDO
    return True


def encontrar_contraexemplo_da_versao_ingenua():
    resultado = explorar()
    for t in resultado.transicoes:
        if not _req_safe_005_ingenua(t.origem, t.entrada, t.saida, t.destino):
            caminho = reconstruir_caminho(resultado, t.origem) + [t]
            return caminho
    return None


def main() -> None:
    print("=" * 78)
    print("AULA 09 — Do texto ambíguo à propriedade formal (REQ-SAFE-005)")
    print("=" * 78)

    print("\n[1] Requisito como o cliente/engenharia de sistemas escreveria:\n")
    print(f"    {TEXTO_AMBIGUO}")

    print("\n[2] Primeira formalização (tradução literal, ingênua):\n")
    print(
        "    if estado == PARADO_OBSTACULO and not obstaculo and comando_partir:\n"
        "        assert proximo_estado == MOVENDO"
    )

    print("\n[3] Rodando o model checker contra a versão ingênua...\n")
    caminho = encontrar_contraexemplo_da_versao_ingenua()
    if caminho is None:
        print("    Nenhum contraexemplo encontrado (inesperado!).")
    else:
        print("    CONTRAEXEMPLO ENCONTRADO — a versão ingênua é falsa em geral:")
        print(formatar_caminho(caminho))
        ultima = caminho[-1]
        print(
            f"\n    Na última transição, entradas.falha_encoder="
            f"{ultima.entrada.falha_encoder}, mas o requisito ingênuo exigia "
            f"MOVENDO mesmo assim. O texto original não previa uma falha de "
            f"encoder simultânea — ele estava implicitamente assumindo que "
            f"nenhuma outra condição de segurança concorrente ocorreria."
        )

    print("\n[4] Formalização corrigida, em produção (nexabot/requisitos.py):\n")
    print(f"    {REQ_SAFE_005.descricao}\n")
    print(
        "    if (estado == PARADO_OBSTACULO and not obstaculo and comando_partir\n"
        "            and not emergencia and not falha_encoder):\n"
        "        assert proximo_estado == MOVENDO"
    )

    print("\n[5] Verificando a versão corrigida contra o mesmo espaço de estados...\n")
    resultado = explorar()
    violacoes = [
        t
        for t in resultado.transicoes
        if not REQ_SAFE_005.verificar_transicao(t.origem, t.entrada, t.saida, t.destino)
    ]
    print(f"    Violações encontradas: {len(violacoes)} (esperado: 0)")

    print("\nLIÇÃO: verificação formal não serve só para achar bugs no código —")
    print("também serve para achar bugs na PRÓPRIA especificação, antes que ela")
    print("vire código, teste ou treinamento de operador.")


if __name__ == "__main__":
    main()
