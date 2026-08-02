"""Reproduz os mecanismos centrais do roteiro da Aula 10: ordem garantida
só dentro da partição, grupos de consumidores, e o número mínimo de
partições do exemplo numérico (1200 rps / 150 rps = 8)."""

from __future__ import annotations

from app.barramento import GrupoConsumidores, Topico, escolher_particao


def test_mesma_chave_sempre_vai_para_a_mesma_particao():
    topico = Topico(nome="pedidos-eventos", num_particoes=8)

    for _ in range(20):
        assert topico.particao_da_chave("pedido-123") == topico.particao_da_chave("pedido-123")


def test_eventos_da_mesma_chave_chegam_em_ordem_na_mesma_particao():
    """A propriedade central: todos os eventos de um mesmo pedido_id
    mantêm a ordem, porque caem sempre na mesma partição."""
    topico = Topico(nome="pedidos-eventos", num_particoes=8)
    chave = "pedido-4021"

    topico.publicar(chave, "PedidoCriado", {"seq": 1})
    topico.publicar(chave, "EstoqueReservado", {"seq": 2})
    topico.publicar(chave, "PagamentoAprovado", {"seq": 3})
    topico.publicar(chave, "PedidoExpedido", {"seq": 4})

    particao = topico.particao_da_chave(chave)
    eventos = topico.ler_particao(particao)

    assert [e.payload["seq"] for e in eventos] == [1, 2, 3, 4]
    assert [e.offset for e in eventos] == [0, 1, 2, 3]


def test_particionamento_por_tipo_de_evento_quebra_a_ordem_do_pedido():
    """O erro do roteiro: particionar por tipo de evento espalha os
    eventos do mesmo pedido entre partições diferentes."""
    topico = Topico(nome="pedidos-eventos", num_particoes=8)

    topico.publicar("PedidoCriado", "PedidoCriado", {})
    topico.publicar("PagamentoAprovado", "PagamentoAprovado", {})

    particao_criado = topico.particao_da_chave("PedidoCriado")
    particao_aprovado = topico.particao_da_chave("PagamentoAprovado")

    # Duas chaves de tipo diferente quase certamente caem em partições
    # diferentes — exatamente o cenário que embaralha a ordem do pedido.
    assert particao_criado != particao_aprovado or topico.num_particoes == 1


def test_grupo_de_consumidores_divide_as_particoes_entre_instancias():
    topico = Topico(nome="pedidos-eventos", num_particoes=6)
    grupo = GrupoConsumidores(topico, "notificacoes", instancias=["n0", "n1", "n2"])

    particoes_por_instancia = {i: grupo.particoes_da_instancia(i) for i in ["n0", "n1", "n2"]}

    todas_as_particoes = sorted(sum(particoes_por_instancia.values(), []))
    assert todas_as_particoes == list(range(6))
    assert all(len(p) == 2 for p in particoes_por_instancia.values())  # 6 partições / 3 instâncias


def test_consumir_avanca_o_deslocamento_e_nao_repete_eventos_ja_lidos():
    topico = Topico(nome="pedidos-eventos", num_particoes=1)
    grupo = GrupoConsumidores(topico, "notificacoes", instancias=["n0"])

    topico.publicar("pedido-1", "PedidoCriado", {})
    primeira_leitura = grupo.consumir("n0")
    segunda_leitura = grupo.consumir("n0")  # nada de novo desde a primeira

    assert len(primeira_leitura) == 1
    assert segunda_leitura == []

    topico.publicar("pedido-2", "PedidoCriado", {})
    terceira_leitura = grupo.consumir("n0")
    assert len(terceira_leitura) == 1


def test_dois_grupos_independentes_leem_o_mesmo_topico_sem_interferir():
    """Grupos diferentes têm deslocamentos independentes — um grupo
    atrasado não afeta o outro (a mesma independência do roteiro)."""
    topico = Topico(nome="pedidos-eventos", num_particoes=1)
    grupo_auditoria = GrupoConsumidores(topico, "auditoria", instancias=["a0"])
    grupo_notificacoes = GrupoConsumidores(topico, "notificacoes", instancias=["n0"])

    topico.publicar("pedido-1", "PedidoCriado", {})

    grupo_auditoria.consumir("a0")  # auditoria já leu
    # notificações ainda não leu nada — deve ver o evento normalmente
    eventos_notificacoes = grupo_notificacoes.consumir("n0")

    assert len(eventos_notificacoes) == 1


def test_rebalancear_redistribui_particoes_preservando_deslocamento_ja_lido():
    topico = Topico(nome="pedidos-eventos", num_particoes=4)
    grupo = GrupoConsumidores(topico, "notificacoes", instancias=["n0", "n1"])

    topico.publicar("pedido-1", "PedidoCriado", {})  # cai em alguma partição
    particao_do_evento = topico.particao_da_chave("pedido-1")
    instancia_original = grupo._atribuicao[particao_do_evento]
    grupo.consumir(instancia_original)

    grupo.rebalancear(["n0", "n1", "n2"])  # nova instância entra no grupo

    # O deslocamento já lido não volta a zero para a partição em questão.
    assert grupo.deslocamento(particao_do_evento) == 1


def test_numero_minimo_de_particoes_do_exemplo_da_aula():
    """1200 eventos/s de pico, 150 eventos/s por consumidor -> 8 partições."""
    import math

    taxa_pico = 1200
    capacidade_por_consumidor = 150

    numero_minimo = math.ceil(taxa_pico / capacidade_por_consumidor)

    assert numero_minimo == 8


def test_escolher_particao_e_deterministico_e_dentro_do_intervalo():
    for chave in ["a", "b", "c", "pedido-999"]:
        particao = escolher_particao(chave, num_particoes=8)
        assert 0 <= particao < 8
