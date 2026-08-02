#!/usr/bin/env python3
"""Verificador estático de fronteiras — Unidade 3, Aula 9.

Um script real, executável em CI, que audita três dos seis sinais de
monólito distribuído listados no roteiro:

1. Nenhum serviço importa código-fonte de outro serviço diretamente
   (sinal 4 do roteiro: "serviços compartilham tabelas, filas ou segredos
   sem contrato explícito" — aqui, generalizado para qualquer import
   direto de código).
2. Cada serviço com persistência declara seu próprio caminho de banco de
   dados, e nenhum dois serviços apontam para o mesmo caminho por padrão
   (sinal 4 do roteiro, na forma mais literal: banco compartilhado).
3. Cada serviço tem seu próprio `requirements.txt` e `Dockerfile` — pode
   ser testado, construído e implantado isoladamente dos demais.

Uso: python3 scripts/verificar_fronteiras.py
Saída: relatório por serviço; código de saída 1 se houver violação.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

RAIZ_PROJETO = Path(__file__).resolve().parent.parent
RAIZ_SERVICES = RAIZ_PROJETO / "services"


def _nomes_dos_servicos() -> list[str]:
    if not RAIZ_SERVICES.exists():
        return []
    return sorted(p.name for p in RAIZ_SERVICES.iterdir() if p.is_dir())


def verificar_imports_cruzados(servicos: list[str]) -> list[str]:
    """Nenhum serviço deveria importar o pacote `app` de outro serviço
    diretamente pelo caminho de arquivo — cada um só conhece a si mesmo."""
    violacoes = []
    padrao_import_de_outro_servico = re.compile(
        r"^\s*(?:from|import)\s+(" + "|".join(re.escape(s) for s in servicos) + r")\b"
    )
    for servico in servicos:
        pasta_app = RAIZ_SERVICES / servico / "app"
        if not pasta_app.exists():
            continue
        for arquivo_py in pasta_app.rglob("*.py"):
            for numero_linha, linha in enumerate(arquivo_py.read_text().splitlines(), start=1):
                casamento = padrao_import_de_outro_servico.match(linha)
                if casamento and casamento.group(1) != servico:
                    violacoes.append(
                        f"{servico}: {arquivo_py.relative_to(RAIZ_PROJETO)}:{numero_linha} "
                        f"importa código de '{casamento.group(1)}' diretamente"
                    )
    return violacoes


def verificar_banco_proprio(servicos: list[str]) -> list[str]:
    """Cada serviço com persistência deve declarar uma variável de
    ambiente de caminho de banco distinta das dos demais."""
    violacoes = []
    padrao_variavel_banco = re.compile(r'os\.environ\.get\("(\w*_DB_PATH)"')
    variavel_por_servico: dict[str, str] = {}

    for servico in servicos:
        arquivo_main = RAIZ_SERVICES / servico / "app" / "main.py"
        if not arquivo_main.exists():
            continue
        casamento = padrao_variavel_banco.search(arquivo_main.read_text())
        if casamento:
            variavel_por_servico[servico] = casamento.group(1)

    vistas: dict[str, str] = {}
    for servico, variavel in variavel_por_servico.items():
        if variavel in vistas:
            violacoes.append(
                f"{servico} e {vistas[variavel]} usam a mesma variável de banco '{variavel}'"
            )
        else:
            vistas[variavel] = servico
    return violacoes


def verificar_implantavel_isoladamente(servicos: list[str]) -> list[str]:
    """Cada serviço precisa de requirements.txt e Dockerfile próprios —
    prova estrutural de que pode ser construído e implantado sozinho."""
    violacoes = []
    for servico in servicos:
        pasta_servico = RAIZ_SERVICES / servico
        if not (pasta_servico / "requirements.txt").exists():
            violacoes.append(f"{servico}: sem requirements.txt próprio")
        if not (pasta_servico / "Dockerfile").exists():
            violacoes.append(f"{servico}: sem Dockerfile próprio")
    return violacoes


def executar() -> int:
    servicos = _nomes_dos_servicos()
    print(f"Serviços encontrados: {', '.join(servicos)}\n")

    verificacoes = {
        "Imports cruzados entre serviços": verificar_imports_cruzados(servicos),
        "Banco de dados compartilhado": verificar_banco_proprio(servicos),
        "Implantável isoladamente (requirements + Dockerfile)": verificar_implantavel_isoladamente(servicos),
    }

    total_violacoes = 0
    for nome_verificacao, violacoes in verificacoes.items():
        if violacoes:
            print(f"✗ {nome_verificacao}: {len(violacoes)} violação(ões)")
            for violacao in violacoes:
                print(f"    - {violacao}")
        else:
            print(f"✓ {nome_verificacao}: nenhuma violação")
        total_violacoes += len(violacoes)

    print()
    if total_violacoes:
        print(f"FALHOU: {total_violacoes} violação(ões) de fronteira encontrada(s).")
        return 1
    print("OK: nenhuma violação de fronteira encontrada.")
    return 0


if __name__ == "__main__":
    sys.exit(executar())
