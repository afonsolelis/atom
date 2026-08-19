.PHONY: setup test run

setup:
	python3 -m venv services/pedidos/.venv
	services/pedidos/.venv/bin/pip install -r services/pedidos/requirements.txt

test:
	cd services/pedidos && .venv/bin/pytest tests/ -v

run:
	cd services/pedidos && .venv/bin/uvicorn app.main:app --reload --port 8001
