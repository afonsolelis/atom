"""Reproduz o exemplo central do roteiro da Aula 15 (Slide 10): dez
tentativas de pagamento em dez segundos, no mesmo dispositivo — mas a rede
atrasa cinco delas em dois minutos. A janela por tempo de evento reconhece
as dez como um único padrão; uma janela por tempo de processamento veria
dois grupos de cinco e nunca dispararia o alerta."""

from __future__ import annotations

from app.janela_evento import JanelaPorTempoDeEvento, Tentativa


def test_janela_por_tempo_de_evento_agrupa_mesmo_com_atraso_de_rede():
    janela = JanelaPorTempoDeEvento(duracao_ms=60_000, tolerancia_atraso_ms=150_000)

    # Cinco tentativas chegam no prazo: tempo de evento e de processamento coincidem.
    for i in range(5):
        janela.ingerir(Tentativa("disp-1", tempo_evento_ms=i * 1000, tempo_processamento_ms=i * 1000))
    # Cinco tentativas do MESMO padrão são atrasadas pela rede em dois minutos.
    for i in range(5, 10):
        janela.ingerir(Tentativa("disp-1", tempo_evento_ms=i * 1000, tempo_processamento_ms=120_000))

    contagem_por_evento = janela.contagem_na_janela("disp-1", fim_da_janela_ms=9_000)
    assert contagem_por_evento == 10  # a fraude é reconhecida como um único padrão

    # Uma janela de processamento fechada aos 9s só vê as cinco no prazo.
    assert janela.contagem_por_tempo_de_processamento("disp-1", fim_da_janela_ms=9_000) == 5
    # E quando as outras cinco finalmente chegam, aos 120s, formam uma
    # segunda janela de processamento — nunca as dez juntas.
    assert janela.contagem_por_tempo_de_processamento("disp-1", fim_da_janela_ms=120_000) == 5


def test_marca_dagua_e_tempo_de_processamento_menos_tolerancia():
    janela = JanelaPorTempoDeEvento(duracao_ms=60_000, tolerancia_atraso_ms=30_000)

    assert janela.avancar_marca_dagua(tempo_processamento_atual_ms=100_000) == 70_000


def test_marca_dagua_nunca_recua():
    janela = JanelaPorTempoDeEvento(duracao_ms=60_000, tolerancia_atraso_ms=30_000)

    janela.avancar_marca_dagua(100_000)
    assert janela.avancar_marca_dagua(50_000) == 70_000  # não recua para 20_000


def test_janela_so_fecha_depois_que_a_marca_dagua_a_ultrapassa():
    janela = JanelaPorTempoDeEvento(duracao_ms=60_000, tolerancia_atraso_ms=10_000)

    janela.avancar_marca_dagua(tempo_processamento_atual_ms=65_000)  # marca = 55_000
    assert janela.esta_fechada(fim_da_janela_ms=60_000) is False

    janela.avancar_marca_dagua(tempo_processamento_atual_ms=75_000)  # marca = 65_000
    assert janela.esta_fechada(fim_da_janela_ms=60_000) is True


def test_tolerancia_maior_mantem_a_janela_aberta_por_mais_tempo():
    """O compromisso do roteiro, em números: com tolerância curta, o mesmo
    avanço de tempo de processamento já fecha a janela; com tolerância
    longa, a janela continua aberta, admitindo os atrasados — ao custo de
    atrasar a decisão."""
    janela_curta = JanelaPorTempoDeEvento(duracao_ms=60_000, tolerancia_atraso_ms=5_000)
    janela_longa = JanelaPorTempoDeEvento(duracao_ms=60_000, tolerancia_atraso_ms=130_000)

    janela_curta.avancar_marca_dagua(tempo_processamento_atual_ms=65_000)
    janela_longa.avancar_marca_dagua(tempo_processamento_atual_ms=65_000)

    assert janela_curta.esta_fechada(fim_da_janela_ms=60_000) is True
    assert janela_longa.esta_fechada(fim_da_janela_ms=60_000) is False


def test_contagem_e_isolada_por_dispositivo():
    janela = JanelaPorTempoDeEvento(duracao_ms=60_000, tolerancia_atraso_ms=10_000)

    janela.ingerir(Tentativa("disp-1", tempo_evento_ms=0, tempo_processamento_ms=0))
    janela.ingerir(Tentativa("disp-2", tempo_evento_ms=0, tempo_processamento_ms=0))
    janela.ingerir(Tentativa("disp-2", tempo_evento_ms=1000, tempo_processamento_ms=1000))

    assert janela.contagem_na_janela("disp-1", fim_da_janela_ms=1000) == 1
    assert janela.contagem_na_janela("disp-2", fim_da_janela_ms=1000) == 2
