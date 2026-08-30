#!/usr/bin/env python3
"""Aula 11 — Script 01: verificando o watchdog temporizado do REQ-SAFE-006.

O que este script faz
----------------------
Roda `nexabot.timed.verificar_req_safe_006`, que explora exaustivamente o
autômato temporizado de tempo discreto do watchdog (relógio em múltiplos de
Ts = 5 ms) para o cenário nominal de projeto do NexaBot: atraso de detecção
de sensor de até 2 períodos (10 ms) e possibilidade de 1 ciclo de atuação
perdido. Imprime o pior caminho encontrado e confere que ele respeita o
prazo de 150 ms (30 períodos).

Como rodar
----------
    .venv/bin/python aula_11/01_watchdog.py

Saída esperada (resumo)
------------------------
Pior caso: 5 períodos = 25,0 ms, dentro do limite de 30 períodos = 150 ms.
6 caminhos possíveis explorados exaustivamente.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.params import PARAMS  # noqa: E402
from nexabot.timed import formatar_caminho_temporizado, verificar_req_safe_006  # noqa: E402


def main() -> None:
    print("=" * 78)
    print("AULA 11 — Verificação exaustiva do watchdog temporizado (REQ-SAFE-006)")
    print("=" * 78)

    print(f"\nParâmetros do NexaBot: Ts = {PARAMS.Ts * 1000:.1f} ms, "
          f"d_stop_max = {PARAMS.d_stop_max * 1000:.0f} ms")

    atraso_max = 2
    resultado = verificar_req_safe_006(atraso_deteccao_max=atraso_max, permite_ciclo_perdido=True)

    print(f"\nCenário verificado: atraso de detecção do sensor até {atraso_max} período(s), "
          "mais 1 ciclo de atuação perdido (opcional).")

    print("\n+--------------------------------------------+----------------------+")
    print("| GRANDEZA                                    | VALOR                |")
    print("+--------------------------------------------+----------------------+")
    linhas = [
        ("caminhos explorados (exaustivo)", str(resultado.n_caminhos_explorados)),
        ("limite do requisito", f"{resultado.limite_periodos} períodos = {resultado.limite_ms:.0f} ms"),
        ("pior caso encontrado", f"{resultado.pior_caso_periodos} períodos = {resultado.pior_caso_ms:.1f} ms"),
        ("margem de segurança", f"{resultado.limite_ms - resultado.pior_caso_ms:.1f} ms"),
        ("REQ-SAFE-006 satisfeito?", "SIM" if resultado.ok else "NÃO"),
    ]
    for rotulo, valor in linhas:
        print(f"| {rotulo:<44} | {valor:<20} |")
    print("+--------------------------------------------+----------------------+")

    print("\nPior caminho (trajetória do autômato temporizado até ZERADO):")
    print(f"  {formatar_caminho_temporizado(resultado.pior_caminho)}")
    print(
        f"\n  Interpretação: {resultado.pior_caminho.atraso_deteccao_periodos} período(s) em "
        f"DETECTANDO (atraso de sensor) + tempo em COMANDANDO "
        f"(ciclo perdido usado: {resultado.pior_caminho.usou_ciclo_perdido})."
    )

    assert resultado.ok, "REQ-SAFE-006 deveria valer no cenário nominal"
    print("\nRESULTADO: REQ-SAFE-006 verificado com sucesso no cenário nominal de projeto.")


if __name__ == "__main__":
    main()
