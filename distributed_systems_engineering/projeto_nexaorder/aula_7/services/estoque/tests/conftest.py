import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture()
def cliente_api(tmp_path, monkeypatch):
    """Cria uma instância da API com um banco SQLite descartável por teste
    e uma réplica de leitura própria — nenhum estado vaza entre testes."""
    banco = tmp_path / "estoque_teste.db"
    monkeypatch.setenv("ESTOQUE_DB_PATH", str(banco))
    monkeypatch.setenv("ATRASO_REPLICA_SEGUNDOS", "0.05")  # mais rápido para os testes

    for nome_modulo in list(sys.modules):
        if nome_modulo == "app.main" or nome_modulo.startswith("app.main."):
            del sys.modules[nome_modulo]

    from fastapi.testclient import TestClient
    from app.main import app

    with TestClient(app) as cliente:
        yield cliente
