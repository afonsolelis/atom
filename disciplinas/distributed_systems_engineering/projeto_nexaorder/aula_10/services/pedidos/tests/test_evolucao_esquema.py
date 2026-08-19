"""Evolução de esquema aditiva — Unidade 3, Aula 10 (retoma a Aula 2).

Prova as duas direções de compatibilidade com exemplos concretos: um
consumidor antigo lendo um evento no formato novo, e um consumidor novo
lendo um evento no formato antigo."""


def test_consumidor_antigo_ignora_campo_novo_do_produtor():
    """Compatibilidade prospectiva (forward): o produtor evoluiu para v2,
    acrescentando 'canal_venda'. Um consumidor que só conhece a v1
    continua funcionando, simplesmente ignorando o campo novo."""
    payload_v2 = {"pedido_id": "p1", "total": 100.0, "canal_venda": "app"}

    def consumidor_versao_1(payload: dict) -> dict:
        return {"pedido_id": payload["pedido_id"], "total": payload["total"]}

    resultado = consumidor_versao_1(payload_v2)

    assert resultado == {"pedido_id": "p1", "total": 100.0}


def test_consumidor_novo_usa_valor_padrao_para_campo_ausente_em_evento_antigo():
    """Compatibilidade retroativa (backward): um consumidor já atualizado
    para a v2 continua lendo eventos antigos (v1), aplicando um valor
    padrão bem definido para o campo que a v1 não tinha."""
    payload_v1 = {"pedido_id": "p1", "total": 100.0}

    def consumidor_versao_2(payload: dict) -> dict:
        return {
            "pedido_id": payload["pedido_id"],
            "total": payload["total"],
            "canal_venda": payload.get("canal_venda", "desconhecido"),
        }

    resultado = consumidor_versao_2(payload_v1)

    assert resultado["canal_venda"] == "desconhecido"


def test_renomear_campo_sem_transicao_quebra_o_consumidor_antigo():
    """A mudança perigosa do roteiro: renomear em vez de adicionar."""
    payload_renomeado = {"pedido_id": "p1", "valor_liquido": 100.0}  # era "total"

    def consumidor_versao_1(payload: dict) -> dict:
        return {"pedido_id": payload["pedido_id"], "total": payload["total"]}

    try:
        consumidor_versao_1(payload_renomeado)
        assert False, "deveria ter levantado KeyError — o campo 'total' não existe mais"
    except KeyError:
        pass
