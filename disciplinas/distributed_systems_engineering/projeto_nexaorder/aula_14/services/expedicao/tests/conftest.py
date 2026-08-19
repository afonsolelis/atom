import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))


@pytest.fixture()
def cliente_api(tmp_path, monkeypatch):
    banco = tmp_path / "expedicao_teste.db"
    monkeypatch.setenv("EXPEDICAO_DB_PATH", str(banco))

    for nome_modulo in list(sys.modules):
        if nome_modulo == "app.main" or nome_modulo.startswith("app.main."):
            del sys.modules[nome_modulo]

    from fastapi.testclient import TestClient
    from app.main import app
    from app.seguranca import emitir_token

    # Ver estoque/tests/conftest.py: o cliente padrão já se autentica como
    # "pedidos" (Aula 12), a única identidade autorizada nas rotas
    # protegidas deste serviço.
    cabecalhos_padrao = {"Authorization": f"Bearer {emitir_token('pedidos')}"}

    with TestClient(app, headers=cabecalhos_padrao) as cliente:
        yield cliente
