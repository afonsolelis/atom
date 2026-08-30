"""Compila e empacota o FMU FMI 3.0 `NexaBotPlant.fmu` (Aula 8).

Este script:

1. Compila `plant_fmu.c` com gcc em uma biblioteca compartilhada
   (`-shared -fPIC -O2`), usando os cabecalhos FMI 3.0 oficiais baixados em
   `nexabot/fmu/headers/`.
2. Monta a arvore de diretorios exigida pelo padrao FMI 3.0:

       NexaBotPlant.fmu (zip)
       ├── modelDescription.xml
       └── binaries/
           └── x86_64-linux/
               └── NexaBotPlant.so

3. Zipa a arvore em `nexabot/fmu/NexaBotPlant.fmu`.

Uso (a partir da raiz do projeto, com o venv do projeto):

    .venv/bin/python -m nexabot.fmu.build_fmu

Rastreabilidade: REQ-PLANT-001 (a planta do FMU e a mesma de plant.py).
"""

from __future__ import annotations

import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

FMU_DIR = Path(__file__).resolve().parent
SOURCE_C = FMU_DIR / "plant_fmu.c"
HEADERS_DIR = FMU_DIR / "headers"
MODEL_DESCRIPTION = FMU_DIR / "modelDescription.xml"
MODEL_IDENTIFIER = "NexaBotPlant"
PLATFORM_TUPLE = "x86_64-linux"
OUTPUT_FMU = FMU_DIR / f"{MODEL_IDENTIFIER}.fmu"


def compile_shared_library(build_dir: Path) -> Path:
    """Compila plant_fmu.c em binaries/<platform>/NexaBotPlant.so."""
    binaries_dir = build_dir / "binaries" / PLATFORM_TUPLE
    binaries_dir.mkdir(parents=True, exist_ok=True)
    shared_lib = binaries_dir / f"{MODEL_IDENTIFIER}.so"

    cmd = [
        "gcc",
        "-shared",
        "-fPIC",
        "-O2",
        "-Wall",
        "-Wextra",
        "-I",
        str(HEADERS_DIR),
        "-o",
        str(shared_lib),
        str(SOURCE_C),
        "-lm",
    ]

    print("== Compilando plant_fmu.c com gcc ==")
    print(" ".join(cmd))
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    result.check_returncode()

    if not shared_lib.exists():
        raise RuntimeError(f"gcc terminou sem erro mas {shared_lib} nao foi criado")

    print(f"OK: biblioteca compartilhada gerada em {shared_lib}")
    return shared_lib


def assemble_fmu_tree(build_dir: Path) -> None:
    """Copia modelDescription.xml para a raiz da arvore do FMU."""
    if not MODEL_DESCRIPTION.exists():
        raise FileNotFoundError(f"modelDescription.xml nao encontrado em {MODEL_DESCRIPTION}")
    shutil.copy2(MODEL_DESCRIPTION, build_dir / "modelDescription.xml")
    print(f"OK: modelDescription.xml copiado para {build_dir / 'modelDescription.xml'}")


def zip_fmu(build_dir: Path, output_path: Path) -> None:
    """Zipa a arvore do FMU (modelDescription.xml + binaries/) em .fmu."""
    if output_path.exists():
        output_path.unlink()

    with zipfile.ZipFile(output_path, mode="w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(build_dir.rglob("*")):
            if path.is_file():
                arcname = path.relative_to(build_dir)
                zf.write(path, arcname)

    print(f"OK: FMU empacotado em {output_path}")


def print_zip_contents(fmu_path: Path) -> None:
    """Imprime o conteudo do .fmu gerado, para conferencia visual ao vivo."""
    print()
    print(f"== Conteudo de {fmu_path.name} ==")
    with zipfile.ZipFile(fmu_path, mode="r") as zf:
        for info in zf.infolist():
            print(f"  {info.file_size:>8} bytes  {info.filename}")


def main() -> None:
    build_dir = FMU_DIR / "_build_tmp"
    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True)

    try:
        compile_shared_library(build_dir)
        assemble_fmu_tree(build_dir)
        zip_fmu(build_dir, OUTPUT_FMU)
    finally:
        shutil.rmtree(build_dir, ignore_errors=True)

    print_zip_contents(OUTPUT_FMU)
    print()
    print(f"FMU pronto: {OUTPUT_FMU}")


if __name__ == "__main__":
    main()
