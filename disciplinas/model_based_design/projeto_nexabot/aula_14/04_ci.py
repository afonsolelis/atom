#!/usr/bin/env python3
"""Aula 14 — Script 4/5: mostra e valida o workflow de CI.

O que este script faz
----------------------
Carrega `.github/workflows/mbd-ci.yml` com `pyyaml`, imprime sua estrutura
(gatilhos, job, passos, na ordem em que rodam) e valida um conjunto de
propriedades que o workflow PRECISA ter para cumprir o que promete: rodar
pytest, rodar a checagem de equivalência SIL e gerar a matriz de
rastreabilidade a cada push/pull request.

Isto fecha o ciclo desta aula: não basta o workflow "parecer certo" — este
script o testa como se fosse mais um artefato do pipeline (o que, de fato,
é: seria trivialmente possível editar o YAML e esquecer um passo).

Como rodar
----------
    .venv/bin/python aula_14/04_ci.py

Saída esperada (resumo)
------------------------
Uma árvore com os passos do workflow e uma lista de checagens, todas "OK".
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import yaml  # noqa: E402

WORKFLOW_PATH = Path(__file__).resolve().parent.parent / ".github" / "workflows" / "mbd-ci.yml"


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def main() -> None:
    print(linha("="))
    print(f"Aula 14 — Validação do workflow de CI: {WORKFLOW_PATH.name}")
    print(linha("="))

    if not WORKFLOW_PATH.exists():
        print(f"\nERRO: workflow não encontrado em {WORKFLOW_PATH}")
        raise SystemExit(1)

    texto = WORKFLOW_PATH.read_text(encoding="utf-8")
    workflow = yaml.safe_load(texto)

    print(f"\nArquivo: {WORKFLOW_PATH}")
    print(f"Nome do workflow: {workflow.get('name')!r}")

    # A chave "on" do YAML é lida por pyyaml como booleano True (YAML 1.1)
    # em algumas versões -- normaliza para exibição.
    gatilhos = workflow.get("on", workflow.get(True))
    print(f"Gatilhos: {list(gatilhos.keys()) if isinstance(gatilhos, dict) else gatilhos}")

    jobs = workflow.get("jobs", {})
    print(f"Jobs definidos: {list(jobs.keys())}")

    checagens: list[tuple[str, bool]] = []

    checagens.append(("workflow tem pelo menos 1 job", len(jobs) >= 1))

    job = next(iter(jobs.values())) if jobs else {}
    passos = job.get("steps", [])
    print(f"\nPassos do job {next(iter(jobs), '?')!r} (na ordem em que rodam):")
    for i, passo in enumerate(passos, start=1):
        nome = passo.get("name", passo.get("uses", passo.get("run", "?")))
        print(f"  {i:>2}. {nome}")

    def _algum_passo_contem(trecho: str) -> bool:
        for passo in passos:
            run = passo.get("run", "") or ""
            if trecho in run:
                return True
        return False

    checagens.append(("roda pytest", _algum_passo_contem("pytest")))
    checagens.append(("roda a checagem de equivalência SIL (Aula 14)",
                       _algum_passo_contem("02_equivalencia.py")))
    checagens.append(("roda a suíte de regressão (Aula 14)",
                       _algum_passo_contem("03_regressao.py")))
    checagens.append(("gera a matriz de rastreabilidade (Aula 16)",
                       _algum_passo_contem("01_matriz_rastreabilidade.py")))
    checagens.append(("instala gcc (necessário para compilar o SIL)",
                       _algum_passo_contem("gcc")))
    checagens.append(("dispara em push e em pull_request",
                       isinstance(gatilhos, dict) and {"push", "pull_request"} <= gatilhos.keys()))

    print("\n" + linha("-"))
    print("Checagens de conteúdo do workflow:")
    print(linha("-"))
    todas_ok = True
    for descricao, ok in checagens:
        status = "OK" if ok else "FALHOU"
        if not ok:
            todas_ok = False
        print(f"  [{status:>6}] {descricao}")

    print("\n" + linha("="))
    if todas_ok:
        print("Workflow validado: todos os passos esperados estão presentes.")
    else:
        print("Workflow INCOMPLETO -- ver checagens marcadas FALHOU acima.")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
