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
    from app.seguranca import emitir_token

    # A maioria dos testes exercita o comportamento de negócio, não a
    # autorização em si — por isso o cliente padrão já se autentica como
    # "pedidos", a única identidade autorizada nas rotas protegidas
    # (Aula 12). Os testes de autorização em si usam um cliente à parte,
    # sem este cabeçalho ou com uma identidade diferente.
    cabecalhos_padrao = {"Authorization": f"Bearer {emitir_token('pedidos')}"}

    with TestClient(app, headers=cabecalhos_padrao) as cliente:
        yield cliente
