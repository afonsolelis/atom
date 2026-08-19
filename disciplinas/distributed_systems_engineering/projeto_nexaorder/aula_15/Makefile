SERVICOS := pedidos estoque pagamento expedicao gateway

.PHONY: setup test verificar validar-k8s run-pedidos run-estoque run-pagamento run-expedicao run-gateway verificar-compose up down logs

setup:
	@for s in $(SERVICOS); do \
		echo "--- setup $$s ---"; \
		python3 -m venv services/$$s/.venv; \
		services/$$s/.venv/bin/pip install --quiet --upgrade pip; \
		services/$$s/.venv/bin/pip install --quiet -r services/$$s/requirements.txt; \
	done
	@echo "--- setup scripts ---"
	python3 -m venv scripts/.venv
	scripts/.venv/bin/pip install --quiet --upgrade pip
	scripts/.venv/bin/pip install --quiet -r scripts/requirements.txt

test:
	@for s in $(SERVICOS); do \
		echo "--- test $$s ---"; \
		(cd services/$$s && .venv/bin/pytest tests/ -v) || exit 1; \
	done
	@echo "--- test scripts ---"
	scripts/.venv/bin/pytest scripts/ -v

verificar:
	scripts/.venv/bin/python3 scripts/verificar_fronteiras.py
	scripts/.venv/bin/python3 scripts/calcular_instabilidade.py

validar-k8s:
	scripts/.venv/bin/python3 scripts/validar_manifests_k8s.py

run-pedidos:
	cd services/pedidos && ESTOQUE_BASE_URL=http://localhost:8002 PAGAMENTO_BASE_URL=http://localhost:8003 EXPEDICAO_BASE_URL=http://localhost:8004 .venv/bin/uvicorn app.main:app --reload --port 8001

run-estoque:
	cd services/estoque && .venv/bin/uvicorn app.main:app --reload --port 8002

run-pagamento:
	cd services/pagamento && .venv/bin/uvicorn app.main:app --reload --port 8003

run-expedicao:
	cd services/expedicao && .venv/bin/uvicorn app.main:app --reload --port 8004

run-gateway:
	cd services/gateway && PEDIDOS_BASE_URL=http://localhost:8001 ESTOQUE_BASE_URL=http://localhost:8002 PAGAMENTO_BASE_URL=http://localhost:8003 EXPEDICAO_BASE_URL=http://localhost:8004 .venv/bin/uvicorn app.main:app --reload --port 8000

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
