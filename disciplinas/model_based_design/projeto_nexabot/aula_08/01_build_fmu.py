#!/usr/bin/env python
"""Aula 8 — Passo 1: compilar e empacotar o FMU FMI 3.0 da planta do NexaBot.

O QUE ESTE SCRIPT DEMONSTRA
----------------------------
Compila `nexabot/fmu/plant_fmu.c` (implementacao em C, do zero, das equacoes
do motor CC do NexaBot) com gcc, monta a arvore de diretorios exigida pelo
padrao FMI 3.0 (modelDescription.xml + binaries/x86_64-linux/*.so) e zipa
tudo em `nexabot/fmu/NexaBotPlant.fmu`. Ao final, imprime o conteudo do
.fmu gerado — o professor pode abrir o arquivo com `unzip -l` para mostrar
que e, de fato, um zip comum.

COMO RODAR
----------
    .venv/bin/python aula_08/01_build_fmu.py
"""

from __future__ import annotations

import subprocess
import sys
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FMU_PATH = REPO_ROOT / "nexabot" / "fmu" / "NexaBotPlant.fmu"


def linha(char: str = "=", n: int = 78) -> None:
    print(char * n)


def main() -> int:
    linha()
    print("AULA 8 — Passo 1: construir o FMU FMI 3.0 da planta do NexaBot")
    linha()
    print()
    print("Chamando: .venv/bin/python -m nexabot.fmu.build_fmu")
    print()
    sys.stdout.flush()

    result = subprocess.run(
        [sys.executable, "-m", "nexabot.fmu.build_fmu"],
        cwd=REPO_ROOT,
    )
    if result.returncode != 0:
        print("ERRO: a construcao do FMU falhou.", file=sys.stderr)
        return result.returncode

    print()
    linha("-")
    print(f"Confirmando o pacote gerado: {FMU_PATH}")
    linha("-")

    if not FMU_PATH.exists():
        print("ERRO: NexaBotPlant.fmu nao foi criado.", file=sys.stderr)
        return 1

    tamanho_kb = FMU_PATH.stat().st_size / 1024.0
    print(f"Tamanho do arquivo: {tamanho_kb:.1f} KB")
    print()
    print(f"{'tamanho [bytes]':>18}  arquivo dentro do .fmu")
    print("-" * 60)
    with zipfile.ZipFile(FMU_PATH) as zf:
        for info in zf.infolist():
            print(f"{info.file_size:>18}  {info.filename}")

    print()
    linha()
    print("RESULTADO: NexaBotPlant.fmu construido com sucesso.")
    print("Este e um FMU FMI 3.0 de Co-Simulation valido — a planta do")
    print("NexaBot (motor CC de tracao) inteira compilada em C nativo.")
    linha()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
