"""Prova a resposta madura da pausa para reflexão do roteiro da Aula 15
("vamos processar tudo na borda"): triagem local para sinais simples,
avaliação central para o que exige contexto histórico."""

from __future__ import annotations

from app.triagem_de_fraude import Decisao, Tentativa, avaliacao_central, triagem_local


def test_sinal_simples_e_bloqueado_na_borda_sem_precisar_do_centro():
    tentativa = Tentativa("disp-1", "hash-cartao-1", cartoes_testados_nesta_sessao=4)

    assert triagem_local(tentativa) == Decisao.BLOQUEAR


def test_sinal_no_limite_ainda_bloqueia_na_borda():
    tentativa = Tentativa("disp-1", "hash-cartao-1", cartoes_testados_nesta_sessao=3)

    assert triagem_local(tentativa) == Decisao.BLOQUEAR


def test_sinal_ambiguo_e_encaminhado_para_avaliacao_central():
    """Um único cartão testado não é, sozinho, sinal suficiente para
    bloquear na borda — depende de contexto histórico que só o centro tem,
    o próprio argumento da pausa de reflexão do roteiro."""
    tentativa = Tentativa("disp-1", "hash-cartao-1", cartoes_testados_nesta_sessao=1)

    assert triagem_local(tentativa) == Decisao.ENCAMINHAR_PARA_CENTRAL


def test_avaliacao_central_bloqueia_com_contexto_historico_amplo():
    """O exemplo do roteiro: quarenta cartões em 24h, em cinco cidades —
    contexto que nenhum ponto de borda isolado possui, só o centro."""
    assert avaliacao_central(contagem_na_janela_de_evento=40, limite_da_janela=10) == Decisao.BLOQUEAR


def test_avaliacao_central_libera_sem_padrao_historico():
    assert avaliacao_central(contagem_na_janela_de_evento=2, limite_da_janela=10) == Decisao.LIBERAR
