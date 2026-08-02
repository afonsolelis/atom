"""Critérios de aceite de um novo serviço — Unidade 4, Aula 16.

O roteiro é direto sobre isto: "essas perguntas devem se tornar critérios
de aceite de um novo serviço, e não sugestões em um documento de boas
práticas". Este script converte os princípios acumulados ao longo da
disciplina em um gate executável — o mesmo espírito de
`verificar_fronteiras.py` (Aula 9) e `validar_manifests_k8s.py` (Aula 11),
aplicado agora a identidade e observabilidade: um serviço sem elas não é
aprovado, do mesmo modo que não seria aprovado sem testes.
"""

from __future__ import annotations

from pathlib import Path

RAIZ_SERVICES = Path(__file__).resolve().parent.parent / "services"

ARQUIVOS_EXIGIDOS_POR_SERVICO = {
    "seguranca.py": "identidade própria e comunicação autenticada (Aula 12)",
    "logs_estruturados.py": "logs estruturados correlacionáveis (Aula 13)",
    "metricas.py": "métricas com proteção de cardinalidade (Aula 13)",
    "tracing.py": "traces aninháveis (Aula 13)",
}


def verificar_servico(diretorio_servico: Path) -> list[str]:
    """Devolve os critérios de aceite não cumpridos por um serviço. Lista
    vazia significa serviço aprovado."""
    violacoes: list[str] = []
    diretorio_app = diretorio_servico / "app"

    for arquivo, descricao in ARQUIVOS_EXIGIDOS_POR_SERVICO.items():
        if not (diretorio_app / arquivo).is_file():
            violacoes.append(f"{diretorio_servico.name}: falta {arquivo} — {descricao}")

    diretorio_tests = diretorio_servico / "tests"
    if not diretorio_tests.is_dir() or not any(diretorio_tests.glob("test_*.py")):
        violacoes.append(f"{diretorio_servico.name}: nenhum arquivo de teste encontrado")

    return violacoes


def executar() -> list[str]:
    servicos = sorted(p for p in RAIZ_SERVICES.iterdir() if p.is_dir())
    todas_violacoes: list[str] = []
    for servico in servicos:
        todas_violacoes.extend(verificar_servico(servico))

    print(f"Serviços avaliados: {', '.join(s.name for s in servicos)}\n")
    if todas_violacoes:
        for violacao in todas_violacoes:
            print(f"✗ {violacao}")
    else:
        print("✓ Todos os serviços cumprem os critérios de aceite (identidade, observabilidade, testes).")
    return todas_violacoes


if __name__ == "__main__":
    violacoes_encontradas = executar()
    raise SystemExit(1 if violacoes_encontradas else 0)
