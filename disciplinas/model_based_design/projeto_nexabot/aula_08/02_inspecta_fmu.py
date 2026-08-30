#!/usr/bin/env python
"""Aula 8 — Passo 2: inspecionar o modelDescription.xml do FMU com o fmpy.

O QUE ESTE SCRIPT DEMONSTRA
----------------------------
Usa `fmpy.read_model_description` para ler `modelDescription.xml` de dentro
do `.fmu` (sem descompactar manualmente) e lista as variaveis do modelo —
nome, valueReference, causalidade (input/output/independent), variabilidade
e valor inicial. Tambem mostra os metadados do modelo (nome, versao FMI,
tipo de interface suportada — Co-Simulation) e roda `fmpy.dump` para uma
segunda visao, mais completa, do FMU.

Este e o passo em que o professor mostra "o FMU nao e uma caixa-preta
opaca": o contrato de entradas/saidas e legivel em XML antes mesmo de
carregar o binario.

COMO RODAR
----------
    .venv/bin/python aula_08/02_inspecta_fmu.py
"""

from __future__ import annotations

from pathlib import Path

import fmpy
from fmpy import read_model_description

REPO_ROOT = Path(__file__).resolve().parent.parent
FMU_PATH = REPO_ROOT / "nexabot" / "fmu" / "NexaBotPlant.fmu"


def linha(char: str = "=", n: int = 78) -> None:
    print(char * n)


def main() -> int:
    if not FMU_PATH.exists():
        print(f"ERRO: {FMU_PATH} nao existe. Rode antes:")
        print("  .venv/bin/python aula_08/01_build_fmu.py")
        return 1

    linha()
    print("AULA 8 — Passo 2: inspecionar o modelDescription.xml com o fmpy")
    linha()
    print()

    md = read_model_description(str(FMU_PATH))

    print("== Metadados do modelo ==")
    print(f"  modelName             : {md.modelName}")
    print(f"  fmiVersion            : {md.fmiVersion}")
    print(f"  instantiationToken    : {md.guid}")
    print(f"  generationTool        : {md.generationTool}")
    interfaces = []
    if md.modelExchange is not None:
        interfaces.append("ModelExchange")
    if md.coSimulation is not None:
        interfaces.append("CoSimulation")
    print(f"  interfaces suportadas : {', '.join(interfaces) or '(nenhuma)'}")
    if md.coSimulation is not None:
        print(f"  modelIdentifier (CS)  : {md.coSimulation.modelIdentifier}")
        print(f"  passo variavel (CS)   : {md.coSimulation.canHandleVariableCommunicationStepSize}")

    print()
    print("== Variaveis do modelo (ModelVariables) ==")
    print(f"{'nome':<12} {'vr':>3} {'causalidade':<12} {'variabilidade':<12} {'start':>8}  descricao")
    print("-" * 100)
    for v in md.modelVariables:
        start = "" if v.start is None else f"{float(v.start):.3g}"
        descricao = (v.description or "")[:48]
        print(f"{v.name:<12} {v.valueReference:>3} {v.causality:<12} {v.variability:<12} {start:>8}  {descricao}")

    print()
    print("== Estrutura do modelo (ModelStructure) ==")
    print(f"  saidas declaradas: {[u.variable.name for u in md.outputs]}")

    print()
    linha("-")
    print("== fmpy.dump(NexaBotPlant.fmu) — visao completa do fmpy ==")
    linha("-")
    fmpy.dump(str(FMU_PATH))

    print()
    linha()
    n_in = sum(1 for v in md.modelVariables if v.causality == "input")
    n_out = sum(1 for v in md.modelVariables if v.causality == "output")
    print(f"RESULTADO: {len(md.modelVariables)} variaveis no total "
          f"({n_in} entrada(s), {n_out} saida(s), 1 independente 'time').")
    linha()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
