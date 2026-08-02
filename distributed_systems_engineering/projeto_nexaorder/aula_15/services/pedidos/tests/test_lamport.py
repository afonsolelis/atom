"""Reproduz, teste por teste, a sequência numérica trabalhada no roteiro
da Aula 3: Pedidos e Estoque começam em zero e trocam cinco eventos."""

from app.lamport import LamportClock


def test_evento_local_incrementa_em_um():
    relogio = LamportClock()
    assert relogio.evento_local() == 1
    assert relogio.evento_local() == 2


def test_receber_usa_o_maximo_entre_local_e_recebido_mais_um():
    relogio = LamportClock(valor_inicial=0)
    # Regra 3: max(0, 2) + 1 = 3
    assert relogio.receber(carimbo_recebido=2) == 3


def test_sequencia_completa_pedidos_e_estoque_da_aula_3():
    """Pedidos e Estoque começam ambos com contador zero."""
    pedidos = LamportClock()
    estoque = LamportClock()

    # Evento 1 — Pedidos cria o pedido (evento local): 0 -> 1
    evento_1 = pedidos.evento_local()
    assert evento_1 == 1

    # Evento 2 — Pedidos envia "reservar item": 1 -> 2, anexa 2 à mensagem
    carimbo_da_mensagem = pedidos.enviar()
    assert carimbo_da_mensagem == 2

    # Evento 3 — Estoque recebe a mensagem com carimbo 2: max(0, 2) + 1 = 3
    evento_3 = estoque.receber(carimbo_da_mensagem)
    assert evento_3 == 3

    # Evento 4 — Estoque envia a confirmação: 3 -> 4
    carimbo_confirmacao = estoque.enviar()
    assert carimbo_confirmacao == 4

    # Evento 5 — Pedidos recebe a confirmação com carimbo 4: max(2, 4) + 1 = 5
    evento_5 = pedidos.receber(carimbo_confirmacao)
    assert evento_5 == 5

    # A propriedade central: A aconteceu antes de B implica carimbo(A) < carimbo(B).
    assert evento_1 < carimbo_da_mensagem < evento_3 < carimbo_confirmacao < evento_5


def test_dois_relogios_independentes_podem_empatar_sem_relacao_causal():
    """O limite de Lamport: carimbos iguais não implicam causalidade.

    Um terceiro processo, sem nunca trocar mensagem com os outros dois,
    pode alcançar o mesmo valor só por eventos internos — coincidência
    de contagem, não causalidade (ver Aula 3, "O limite de Lamport")."""
    pagamento = LamportClock()
    for _ in range(5):
        pagamento.evento_local()

    pedidos = LamportClock()
    estoque = LamportClock()
    pedidos.evento_local()
    carimbo = pedidos.enviar()
    estoque.receber(carimbo)
    estoque.enviar()
    valor_pedidos = pedidos.receber(carimbo_recebido=4)

    assert pagamento.valor == valor_pedidos == 5
    # O empate numérico não autoriza afirmar relação causal entre os dois.
