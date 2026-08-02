"""Prova que o validador de manifests realmente detecta violações — não só
que passa nos manifests já corretos do projeto. Rode com o venv
compartilhado: `python3 -m pytest scripts/`."""

from validar_manifests_k8s import (
    verificar_hpa_aponta_para_deployment_existente,
    verificar_recursos,
    verificar_services_apontam_para_deployment_existente,
    verificar_sondas,
)


def _deployment(nome: str, **overrides) -> dict:
    container = {
        "name": nome,
        "livenessProbe": {"httpGet": {"path": "/saude", "port": 8000}},
        "readinessProbe": {"httpGet": {"path": "/pronto", "port": 8000}},
        "resources": {"requests": {"cpu": "100m"}, "limits": {"cpu": "500m"}},
    }
    container.update(overrides.pop("container_overrides", {}))
    return {
        "_arquivo": f"{nome}.yaml",
        "kind": "Deployment",
        "metadata": {"name": nome},
        "spec": {
            "selector": {"matchLabels": {"app": nome}},
            "template": {"spec": {"containers": [container]}},
        },
        **overrides,
    }


def test_deployment_correto_nao_gera_violacao_de_sondas():
    assert verificar_sondas([_deployment("estoque")]) == []


def test_deployment_sem_readiness_probe_e_detectado():
    dep = _deployment("estoque", container_overrides={})
    del dep["spec"]["template"]["spec"]["containers"][0]["readinessProbe"]

    violacoes = verificar_sondas([dep])

    assert len(violacoes) == 1
    assert "readinessProbe" in violacoes[0]


def test_deployment_sem_liveness_probe_e_detectado():
    dep = _deployment("estoque")
    del dep["spec"]["template"]["spec"]["containers"][0]["livenessProbe"]

    violacoes = verificar_sondas([dep])

    assert len(violacoes) == 1
    assert "livenessProbe" in violacoes[0]


def test_deployment_sem_resources_e_detectado():
    dep = _deployment("estoque")
    del dep["spec"]["template"]["spec"]["containers"][0]["resources"]

    violacoes = verificar_recursos([dep])

    assert len(violacoes) == 2  # falta requests e falta limits


def test_service_sem_deployment_correspondente_e_detectado():
    deployments = [_deployment("estoque")]
    services = [
        {
            "_arquivo": "orfao.yaml",
            "metadata": {"name": "servico-orfao"},
            "spec": {"selector": {"app": "servico-que-nao-existe"}},
        }
    ]

    violacoes = verificar_services_apontam_para_deployment_existente(services, deployments)

    assert len(violacoes) == 1
    assert "servico-orfao" in violacoes[0]


def test_hpa_apontando_para_deployment_inexistente_e_detectado():
    deployments = [_deployment("pedidos")]
    hpas = [
        {
            "_arquivo": "hpa-errado.yaml",
            "metadata": {"name": "hpa-errado"},
            "spec": {"scaleTargetRef": {"name": "servico-que-nao-existe"}},
        }
    ]

    violacoes = verificar_hpa_aponta_para_deployment_existente(hpas, deployments)

    assert len(violacoes) == 1
