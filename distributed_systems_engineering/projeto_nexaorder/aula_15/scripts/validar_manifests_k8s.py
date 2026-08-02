#!/usr/bin/env python3
"""Validador estático de manifests Kubernetes — Unidade 3, Aula 11.

Não substitui `kubectl apply --dry-run` nem um cluster real — verifica
apenas regras estruturais que este projeto considera obrigatórias:

1. Todo Deployment tem `livenessProbe` e `readinessProbe` em cada
   contêiner (Aula 11: as duas sondas têm papéis diferentes, e um
   Deployment sem uma delas é uma lacuna, não uma escolha).
2. Todo contêiner declara `resources.requests` e `resources.limits`.
3. Todo Service tem um `selector` que corresponde às labels de algum
   Deployment do conjunto de manifests.
4. Todo HPA (`HorizontalPodAutoscaler`) referencia, em `scaleTargetRef`,
   um Deployment que de fato existe no conjunto.

Uso: python3 scripts/validar_manifests_k8s.py [diretorio]
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

RAIZ_PROJETO = Path(__file__).resolve().parent.parent


def carregar_documentos(diretorio_k8s: Path) -> list[dict[str, Any]]:
    documentos: list[dict[str, Any]] = []
    for arquivo in sorted(diretorio_k8s.glob("*.yaml")):
        for doc in yaml.safe_load_all(arquivo.read_text()):
            if doc:
                doc["_arquivo"] = arquivo.name
                documentos.append(doc)
    return documentos


def _containers(deployment: dict[str, Any]) -> list[dict[str, Any]]:
    return deployment.get("spec", {}).get("template", {}).get("spec", {}).get("containers", [])


def verificar_sondas(deployments: list[dict[str, Any]]) -> list[str]:
    violacoes = []
    for dep in deployments:
        nome = dep["metadata"]["name"]
        for container in _containers(dep):
            if "livenessProbe" not in container:
                violacoes.append(f"{dep['_arquivo']}: Deployment '{nome}' sem livenessProbe")
            if "readinessProbe" not in container:
                violacoes.append(f"{dep['_arquivo']}: Deployment '{nome}' sem readinessProbe")
    return violacoes


def verificar_recursos(deployments: list[dict[str, Any]]) -> list[str]:
    violacoes = []
    for dep in deployments:
        nome = dep["metadata"]["name"]
        for container in _containers(dep):
            recursos = container.get("resources", {})
            if "requests" not in recursos:
                violacoes.append(f"{dep['_arquivo']}: Deployment '{nome}' sem resources.requests")
            if "limits" not in recursos:
                violacoes.append(f"{dep['_arquivo']}: Deployment '{nome}' sem resources.limits")
    return violacoes


def verificar_services_apontam_para_deployment_existente(
    services: list[dict[str, Any]], deployments: list[dict[str, Any]]
) -> list[str]:
    violacoes = []
    labels_dos_deployments = [
        dep.get("spec", {}).get("selector", {}).get("matchLabels", {}) for dep in deployments
    ]
    for svc in services:
        nome = svc["metadata"]["name"]
        seletor = svc.get("spec", {}).get("selector", {})
        if not any(seletor == labels for labels in labels_dos_deployments):
            violacoes.append(
                f"{svc['_arquivo']}: Service '{nome}' não corresponde a nenhum Deployment do conjunto"
            )
    return violacoes


def verificar_hpa_aponta_para_deployment_existente(
    hpas: list[dict[str, Any]], deployments: list[dict[str, Any]]
) -> list[str]:
    violacoes = []
    nomes_dos_deployments = {dep["metadata"]["name"] for dep in deployments}
    for hpa in hpas:
        alvo = hpa.get("spec", {}).get("scaleTargetRef", {}).get("name")
        if alvo not in nomes_dos_deployments:
            violacoes.append(
                f"{hpa['_arquivo']}: HPA '{hpa['metadata']['name']}' aponta para "
                f"Deployment inexistente '{alvo}'"
            )
    return violacoes


def executar(diretorio_k8s: Path) -> int:
    documentos = carregar_documentos(diretorio_k8s)
    deployments = [d for d in documentos if d.get("kind") == "Deployment"]
    services = [d for d in documentos if d.get("kind") == "Service"]
    hpas = [d for d in documentos if d.get("kind") == "HorizontalPodAutoscaler"]

    print(f"Manifests carregados: {len(deployments)} Deployment(s), {len(services)} Service(s), "
          f"{len(hpas)} HPA(s)\n")

    verificacoes = {
        "Sondas de vivacidade e prontidão": verificar_sondas(deployments),
        "Requests e limits de recursos": verificar_recursos(deployments),
        "Services apontam para Deployment existente": verificar_services_apontam_para_deployment_existente(
            services, deployments
        ),
        "HPA aponta para Deployment existente": verificar_hpa_aponta_para_deployment_existente(
            hpas, deployments
        ),
    }

    total_violacoes = 0
    for nome_verificacao, violacoes in verificacoes.items():
        if violacoes:
            print(f"✗ {nome_verificacao}: {len(violacoes)} violação(ões)")
            for v in violacoes:
                print(f"    - {v}")
        else:
            print(f"✓ {nome_verificacao}: nenhuma violação")
        total_violacoes += len(violacoes)

    print()
    if total_violacoes:
        print(f"FALHOU: {total_violacoes} violação(ões) encontrada(s).")
        return 1
    print("OK: nenhuma violação encontrada.")
    return 0


if __name__ == "__main__":
    diretorio = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ_PROJETO / "k8s"
    sys.exit(executar(diretorio))
