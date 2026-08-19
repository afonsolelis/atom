SERVICOS := pedidos estoque

.PHONY: setup test run-pedidos run-estoque verificar-compose up down logs

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

# Motor de contêiner — o projeto sobe igual em Docker ou em Podman.
# A detecção usa o que estiver instalado, nesta ordem de preferência.
# Para forçar um deles: make up COMPOSE="podman-compose"
COMPOSE ?= $(shell \
	if docker compose version >/dev/null 2>&1; then echo "docker compose"; \
	elif podman compose version >/dev/null 2>&1; then echo "podman compose"; \
	elif command -v podman-compose >/dev/null 2>&1; then echo "podman-compose"; \
	elif command -v docker-compose >/dev/null 2>&1; then echo "docker-compose"; \
	fi)

verificar-compose:
	@test -n "$(COMPOSE)" || { \
		echo "ERRO: nenhum motor de compose encontrado."; \
		echo "      Instale o Docker ou o Podman, ou informe o comando:"; \
		echo "      make up COMPOSE=\"<seu comando de compose>\""; \
		exit 1; \
	}
	@echo "--- compose: $(COMPOSE) ---"

up: verificar-compose
	$(COMPOSE) up --build

down: verificar-compose
	$(COMPOSE) down -v

logs: verificar-compose
	$(COMPOSE) logs -f
