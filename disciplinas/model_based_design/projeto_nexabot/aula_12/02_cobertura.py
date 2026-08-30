#!/usr/bin/env python3
"""Aula 12 — Script 02: cobertura de modelo (estados/transições) E cobertura de linhas.

O que este script faz
----------------------
Duas noções de cobertura, lado a lado, para deixar clara a diferença:

  (a) COBERTURA DE MODELO: quantos estados e transições do supervisor a
      suíte de testes gerada na Aula 12/01 realmente exercitou — medida por
      `nexabot.mbt.medir_cobertura`, sem nenhuma ferramenta externa.
  (b) COBERTURA DE LINHAS: quantas linhas de código de `nexabot/supervisor.py`
      foram executadas ao rodar `tests/test_supervisor.py` — medida pela
      ferramenta padrão `coverage.py`, invocada como subprocesso (o mesmo
      comando que o estudante rodaria na linha de comando).

Como rodar
----------
    .venv/bin/python aula_12/02_cobertura.py

Saída esperada (resumo)
------------------------
100% de cobertura de estados e de transições (suíte MBT); pytest com todos
os testes passando; cobertura de linhas de `nexabot/supervisor.py` próxima
de 100% (a suíte MBT + hypothesis exercitam toda a lógica de transição).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))

from nexabot.mbt import gerar_casos_cobertura_estados, gerar_casos_cobertura_transicoes, medir_cobertura  # noqa: E402
from nexabot.modelcheck import explorar  # noqa: E402


def cobertura_de_modelo() -> None:
    print("-" * 78)
    print("(a) COBERTURA DE MODELO — estados e transições do supervisor")
    print("-" * 78)
    resultado = explorar()
    casos_estado = gerar_casos_cobertura_estados(resultado)
    casos_transicao = gerar_casos_cobertura_transicoes(resultado)
    cobertura = medir_cobertura(casos_estado + casos_transicao, resultado)

    print(f"  estados cobertos:    {cobertura['estados_cobertos']}/{cobertura['estados_totais']} "
          f"({cobertura['pct_estados']:.1f}%)")
    print(f"  transições cobertas: {cobertura['transicoes_cobertas']}/{cobertura['transicoes_totais']} "
          f"({cobertura['pct_transicoes']:.1f}%)")


def cobertura_de_linhas() -> None:
    print("\n" + "-" * 78)
    print("(b) COBERTURA DE LINHAS — coverage.py sobre nexabot/supervisor.py")
    print("-" * 78)
    print("  Comando: coverage run -m pytest tests/test_supervisor.py -q")
    print("           coverage report -m --include='*/nexabot/supervisor.py,*/nexabot/requisitos.py'\n")

    python = sys.executable
    subprocess.run(
        [python, "-m", "coverage", "run", "-m", "pytest", "tests/test_supervisor.py", "-q"],
        cwd=RAIZ,
        check=True,
    )
    resultado = subprocess.run(
        [
            python,
            "-m",
            "coverage",
            "report",
            "-m",
            "--include=*/nexabot/supervisor.py,*/nexabot/requisitos.py,*/nexabot/modelcheck.py,*/nexabot/mbt.py,*/nexabot/timed.py",
        ],
        cwd=RAIZ,
        check=True,
        capture_output=True,
        text=True,
    )
    print(resultado.stdout)


def main() -> None:
    print("=" * 78)
    print("AULA 12 — Cobertura: do modelo E de linhas de código")
    print("=" * 78)
    cobertura_de_modelo()
    cobertura_de_linhas()


if __name__ == "__main__":
    main()
