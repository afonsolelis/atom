SERVICOS := pedidos estoque

.PHONY: setup test run-pedidos run-estoque up down logs

setup:
	@for s in $(SERVICOS); do \
		echo "--- setup $$s ---"; \
		python3 -m venv services/$$s/.venv; \
		services/$$s/.venv/bin/pip install --quiet --upgrade pip; \
		services/$$s/.venv/bin/pip install --quiet -r services/$$s/requirements.txt; \
	done

test:
	@for s in $(SERVICOS); do \
		echo "--- test $$s ---"; \
		(cd services/$$s && .venv/bin/pytest tests/ -v) || exit 1; \
	done

run-pedidos:
	cd services/pedidos && ESTOQUE_BASE_URL=http://localhost:8002 .venv/bin/uvicorn app.main:app --reload --port 8001

run-estoque:
	cd services/estoque && .venv/bin/uvicorn app.main:app --reload --port 8002

up:
	docker compose up --build

down:
	docker compose down -v

logs:
	docker compose logs -f
