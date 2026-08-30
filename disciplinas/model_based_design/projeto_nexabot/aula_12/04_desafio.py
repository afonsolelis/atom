#!/usr/bin/env python3
"""Aula 12 — Script 04: desafio — feche o buraco de cobertura.

O que este script faz
----------------------
A suíte de cobertura de TRANSIÇÕES da Aula 12/01 cobre todo par (origem,
destino) alcançável, mas não cobre toda COMBINAÇÃO de entradas relevante
para uma mesma transição — por exemplo, chegar a FALHA a partir de MOVENDO
tanto por `falha_encoder` sozinho quanto por `falha_encoder` simultâneo a
`comando_parar`. Este desafio pede para o estudante escrever um caso de
teste ADICIONAL, não gerado automaticamente, para uma combinação específica,
e verificar que ele passa.

Como rodar
----------
    .venv/bin/python aula_12/04_desafio.py

Saída esperada (resumo)
------------------------
Um relatório do "buraco" de cobertura (uma transição que a suíte cobre com
uma única combinação de entradas, entre várias possíveis) e o resultado do
caso de teste extra do estudante, PASSOU ou FALHOU.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.mbt import gerar_casos_cobertura_transicoes  # noqa: E402
from nexabot.modelcheck import explorar, formatar_entrada  # noqa: E402
from nexabot.supervisor import Entradas, Estado, Supervisor  # noqa: E402


def encontrar_buraco_de_cobertura():
    """Acha uma transição (origem, destino) alcançável por MAIS de uma
    combinação de entradas distinta, mas cuja suíte gerada só exercita uma."""
    resultado = explorar()
    combinacoes_por_par: dict[tuple[Estado, Estado], set] = {}
    for t in resultado.transicoes:
        chave = (t.origem, t.destino)
        combinacoes_por_par.setdefault(chave, set()).add(formatar_entrada(t.entrada))

    # a suíte gerada usa 1 representante por par — o "buraco" é qualquer par
    # com mais de uma combinação de entrada possível
    candidatos = [(par, combos) for par, combos in combinacoes_por_par.items() if len(combos) > 1]
    candidatos.sort(key=lambda kv: (kv[0][0].name, kv[0][1].name))
    return candidatos[0] if candidatos else None


def caso_de_teste_do_estudante() -> bool:
    """DESAFIO: complete este teste para a combinação de entradas escolhida.

    Exemplo já resolvido: chegar a FALHA a partir de MOVENDO com
    `falha_encoder` E `comando_parar` simultâneos (não só `falha_encoder`
    isolado, que é o representante escolhido automaticamente pela Aula 12/01).
    """
    sup = Supervisor()
    sup.step(Entradas(comando_partir=True))
    assert sup.state is Estado.MOVENDO

    # --- ESCREVA AQUI a entrada da combinação não coberta ---
    sup.step(Entradas(falha_encoder=True, comando_parar=True))

    return sup.state is Estado.FALHA


def main() -> None:
    print("=" * 78)
    print("AULA 12 — Desafio: feche um buraco de cobertura de combinações")
    print("=" * 78)

    buraco = encontrar_buraco_de_cobertura()
    if buraco is not None:
        (origem, destino), combinacoes = buraco
        print(f"\nExemplo de buraco de cobertura encontrado: {origem.name} -> {destino.name}")
        print(f"  {len(combinacoes)} combinações de entrada distintas levam a essa transição;")
        print("  a suíte gerada automaticamente exercita só UMA delas (a primeira encontrada).")

    print("\nRodando o caso de teste extra do estudante...")
    passou = caso_de_teste_do_estudante()
    print(f"  status: {'PASSOU' if passou else 'FALHOU'}")

    if passou:
        print("\nParabéns — a combinação extra também leva ao estado esperado.")
        print("Pergunta para discussão: vale a pena adicionar TODAS as combinações")
        print("de entrada a uma suíte de regressão, ou cobertura de (origem, destino)")
        print("já é evidência suficiente, dado que a lógica de prioridade é a mesma?")


if __name__ == "__main__":
    main()
