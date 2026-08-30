#!/usr/bin/env python3
"""Aula 16 — Script 1/3: gera e mostra a matriz de rastreabilidade.

O que este script faz
----------------------
Chama `nexabot.rastreabilidade.construir_matriz` para varrer o projeto
inteiro atrás de identificadores `REQ-*`, imprime a matriz completa como
tabela ASCII no terminal e grava `rastreabilidade.md` na raiz do projeto
(o mesmo arquivo publicado como artefato pelo CI, ver
`.github/workflows/mbd-ci.yml`).

Funciona mesmo que módulos de outras frentes da disciplina (supervisor,
FMU, co-simulação, ...) ainda não existam neste checkout — a ausência vira
aviso, não erro (ver docstring de `nexabot/rastreabilidade.py`).

Como rodar
----------
    .venv/bin/python aula_16/01_matriz_rastreabilidade.py

Saída esperada (resumo)
------------------------
Uma tabela ASCII com um requisito por linha e em quais categorias de
arquivo (Modelo / Código gerado / Teste / Outros) cada um aparece, mais a
confirmação de que `rastreabilidade.md` foi escrito.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.rastreabilidade import gerar_e_salvar  # noqa: E402


def linha(char: str = "-", n: int = 118) -> str:
    return char * n


def _truncar(texto: str, n: int) -> str:
    return texto if len(texto) <= n else texto[: n - 1] + "…"


def main() -> None:
    print(linha("="))
    print("Aula 16 — Matriz de rastreabilidade requisito -> modelo -> código gerado -> teste")
    print(linha("="))

    resultado, destino = gerar_e_salvar()

    print(f"\nArquivos .py lidos: {resultado.n_arquivos_lidos} "
          f"({resultado.n_arquivos_com_erro} com erro de leitura)")
    print(f"Requisitos distintos encontrados: {len(resultado.entradas)}")

    if resultado.avisos:
        print("\nAvisos:")
        for aviso in resultado.avisos:
            print(f"  - {aviso}")

    print("\n" + linha("-"))
    header = f"{'requisito':<18} | {'descrição':<40} | {'modelo':>7} | {'gerado':>7} | {'teste':>6} | {'outros':>7}"
    print(header)
    print(linha("-", len(header)))
    for entrada in resultado.entradas:
        n_modelo = len(entrada.arquivos_por_categoria("Modelo"))
        n_gerado = len(entrada.arquivos_por_categoria("Código gerado"))
        n_teste = len(entrada.arquivos_por_categoria("Teste"))
        n_outros = len(entrada.arquivos_por_categoria("Outros"))
        print(f"{entrada.requisito:<18} | {_truncar(entrada.descricao, 40):<40} | "
              f"{n_modelo:>7} | {n_gerado:>7} | {n_teste:>6} | {n_outros:>7}")

    n_sem_teste = sum(1 for e in resultado.entradas if not e.arquivos_por_categoria("Teste"))
    print("\n" + linha("="))
    print(f"Requisitos sem NENHUMA evidência na coluna 'Teste': {n_sem_teste} de {len(resultado.entradas)}")
    print("(uma lacuna real de cobertura, não um erro do script -- ver aula_16/02_evidencias.py")
    print(" para a distinção entre 'ferramenta gera evidência' e 'processo certifica'.)")

    print(f"\nMatriz completa gravada em: {destino}")


if __name__ == "__main__":
    main()
