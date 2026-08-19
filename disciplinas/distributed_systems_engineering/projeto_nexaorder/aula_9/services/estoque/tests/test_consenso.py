"""Reproduz os números e o incidente do roteiro da Aula 7: maioria, número
ímpar de nós, eleição, replicação por maioria, e o comportamento sob
partição — só o lado majoritário progride."""

from __future__ import annotations

from app.consenso import ClusterRaft, EstadoNo, NoRaft, tamanho_da_maioria, tolerancia_a_falhas


def test_tolerancia_a_falhas_com_5_nos():
    assert tolerancia_a_falhas(5) == 2
    assert tamanho_da_maioria(5) == 3


def test_6_nos_nao_tolera_mais_falhas_que_5():
    """O argumento central para número ímpar: 6 nós custam mais e não
    entregam nenhuma tolerância adicional em relação a 5."""
    assert tolerancia_a_falhas(6) == tolerancia_a_falhas(5) == 2


def test_7_nos_tolera_uma_falha_a_mais_que_5():
    assert tolerancia_a_falhas(7) == 3
    assert tamanho_da_maioria(7) == 4


def test_eleicao_com_todos_os_nos_alcancaveis_elege_lider():
    cluster = ClusterRaft(["n0", "n1", "n2", "n3", "n4"])

    elegeu = cluster.iniciar_eleicao("n0")

    assert elegeu is True
    assert cluster.nos["n0"].estado == EstadoNo.LIDER
    assert cluster.nos["n0"].termo_atual == 1
    outros_lideres = [id_ for id_, no in cluster.nos.items() if id_ != "n0" and no.estado == EstadoNo.LIDER]
    assert outros_lideres == []


def test_no_nao_vota_duas_vezes_no_mesmo_termo():
    """A regra central que evita dois líderes no mesmo termo: um nó só
    concede um voto por termo."""
    no = NoRaft(id="n1")

    concedido_ao_primeiro = ClusterRaft._conceder_voto(no, termo_do_candidato=1, candidato_id="n0")
    concedido_ao_segundo = ClusterRaft._conceder_voto(no, termo_do_candidato=1, candidato_id="n2")

    assert concedido_ao_primeiro is True
    assert concedido_ao_segundo is False
    assert no.votou_em == "n0"


def test_no_vota_novamente_quando_ve_um_termo_maior():
    no = NoRaft(id="n1")
    ClusterRaft._conceder_voto(no, termo_do_candidato=1, candidato_id="n0")

    concedido = ClusterRaft._conceder_voto(no, termo_do_candidato=2, candidato_id="n2")

    assert concedido is True
    assert no.votou_em == "n2"
    assert no.termo_atual == 2


def test_replicar_entrada_confirma_com_maioria():
    cluster = ClusterRaft(["n0", "n1", "n2", "n3", "n4"])
    cluster.iniciar_eleicao("n0")

    confirmado = cluster.replicar_entrada("n0", "PedidoCriado:123")

    assert confirmado is True
    assert cluster.nos["n0"].indice_confirmado == 0
    quantos_receberam = sum(1 for no in cluster.nos.values() if no.log and no.log[-1].valor == "PedidoCriado:123")
    assert quantos_receberam == 5  # todos alcançáveis nesta rodada


def test_no_que_nao_e_lider_nao_pode_replicar():
    cluster = ClusterRaft(["n0", "n1", "n2"])
    cluster.iniciar_eleicao("n0")

    try:
        cluster.replicar_entrada("n1", "tentativa-invalida")
        assert False, "deveria ter levantado ValueError"
    except ValueError:
        pass


def test_grupo_minoritario_isolado_nao_consegue_eleger_lider():
    """5 nós, partição isola 2 — o grupo de 2 não alcança maioria (3)."""
    cluster = ClusterRaft(["n0", "n1", "n2", "n3", "n4"])
    cluster.particionar(["n0", "n1"])

    elegeu = cluster.iniciar_eleicao("n0")

    assert elegeu is False
    assert cluster.nos["n0"].estado == EstadoNo.SEGUIDOR


def test_grupo_majoritario_elege_lider_apesar_da_particao():
    """O grupo de 3 continua funcionando normalmente, isolado do de 2 —
    a mesma simetria da ilusão discutida na Aula 4."""
    cluster = ClusterRaft(["n0", "n1", "n2", "n3", "n4"])
    cluster.particionar(["n0", "n1"])

    elegeu = cluster.iniciar_eleicao("n2")

    assert elegeu is True
    assert cluster.nos["n2"].estado == EstadoNo.LIDER


def test_lider_particionado_nao_confirma_entrada_mesmo_estando_isolado():
    """Reproduz o incidente da situação-problema: o líder original ainda
    'acha' que manda, mas sozinho não alcança maioria — a entrada fica sem
    confirmação enquanto a partição persistir."""
    cluster = ClusterRaft(["n0", "n1", "n2", "n3", "n4"])
    cluster.iniciar_eleicao("n0")  # n0 líder do termo 1, todos alcançáveis

    cluster.particionar(["n0", "n1"])  # agora n0 fica isolado com n1

    confirmado = cluster.replicar_entrada("n0", "ReservaCancelada")

    assert confirmado is False
    assert cluster.nos["n0"].indice_confirmado == -1


def test_apos_curar_particao_lider_antigo_nao_recupera_maioria_sozinho():
    """Depois que o lado majoritário elegeu um novo líder em um termo mais
    alto, o líder antigo não volta a confirmar entradas só porque a rede
    voltou — a maioria já avançou de termo."""
    cluster = ClusterRaft(["n0", "n1", "n2", "n3", "n4"])
    cluster.iniciar_eleicao("n0")  # termo 1, n0 líder

    cluster.particionar(["n0", "n1"])
    cluster.iniciar_eleicao("n2")  # termo 2, eleito pelo lado majoritário

    cluster.curar_particao()

    confirmado = cluster.replicar_entrada("n0", "tentativa-pos-particao")

    # n2, n3, n4 já estão no termo 2 e rejeitam implicitamente a entrada de
    # um líder em termo mais antigo — n0 só conta consigo e com n1.
    assert confirmado is False
