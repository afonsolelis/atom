"""Prova que o gate de critérios de aceite (Aula 16) funciona nos dois
sentidos: aprova os cinco serviços reais do projeto, e detecta de verdade
um serviço que não cumpre um critério — não é decorativo."""

from __future__ import annotations

from verificar_criterios_de_aceite import RAIZ_SERVICES, verificar_servico


def test_todos_os_servicos_reais_do_projeto_cumprem_os_criterios_de_aceite():
    servicos = sorted(p for p in RAIZ_SERVICES.iterdir() if p.is_dir())

    assert len(servicos) == 5  # pedidos, estoque, pagamento, expedicao, gateway
    for servico in servicos:
        assert verificar_servico(servico) == [], f"{servico.name} não deveria ter violações"


def test_deteccao_de_servico_sem_identidade(tmp_path):
    servico_incompleto = tmp_path / "servico-sem-identidade"
    (servico_incompleto / "app").mkdir(parents=True)
    (servico_incompleto / "app" / "logs_estruturados.py").touch()
    (servico_incompleto / "app" / "metricas.py").touch()
    (servico_incompleto / "app" / "tracing.py").touch()
    (servico_incompleto / "tests").mkdir()
    (servico_incompleto / "tests" / "test_algo.py").touch()

    violacoes = verificar_servico(servico_incompleto)

    assert len(violacoes) == 1
    assert "seguranca.py" in violacoes[0]


def test_deteccao_de_servico_sem_nenhum_teste(tmp_path):
    servico_sem_testes = tmp_path / "servico-sem-testes"
    diretorio_app = servico_sem_testes / "app"
    diretorio_app.mkdir(parents=True)
    for arquivo in ("seguranca.py", "logs_estruturados.py", "metricas.py", "tracing.py"):
        (diretorio_app / arquivo).touch()

    violacoes = verificar_servico(servico_sem_testes)

    assert violacoes == [f"{servico_sem_testes.name}: nenhum arquivo de teste encontrado"]
