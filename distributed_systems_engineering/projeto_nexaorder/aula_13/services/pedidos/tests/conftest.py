import os
import sys
import tempfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture()
def cliente_api(tmp_path, monkeypatch):
    """Cria uma instância da API com um banco SQLite descartável por teste."""
    banco = tmp_path / "pedidos_teste.db"
    monkeypatch.setenv("PEDIDOS_DB_PATH", str(banco))

    # Os módulos precisam ser (re)importados depois de definir a variável de
    # ambiente, porque `main.py` lê o caminho do banco na importação.
    for nome_modulo in list(sys.modules):
        if nome_modulo == "app.main" or nome_modulo.startswith("app.main."):
            del sys.modules[nome_modulo]

    from fastapi.testclient import TestClient
    from app.main import app

    with TestClient(app) as cliente:
        yield cliente
