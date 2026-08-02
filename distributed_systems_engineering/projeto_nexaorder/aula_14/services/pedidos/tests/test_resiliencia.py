"""Testa disjuntor, retry e timeout isoladamente, sem precisar de um
servidor de verdade — usa httpx.MockTransport para simular respostas."""

import httpx
import pytest

from app.resiliencia import (
    CircuitBreaker,
    CircuitoAberto,
    ClienteResiliente,
    ConfiguracaoDisjuntor,
    backoff_com_jitter,
)


# --- CircuitBreaker -----------------------------------------------------


def test_disjuntor_comeca_fechado():
    disjuntor = CircuitBreaker()
    assert disjuntor.estado == "fechado"
    assert disjuntor.permite_chamada() is True


def test_disjuntor_abre_com_60_por_cento_de_falha_em_janela_de_20():
    """Reproduz exatamente o exemplo numérico da Aula 4:
    12 falhas em 20 chamadas = 60%, acima do limite de 50%."""
    disjuntor = CircuitBreaker(ConfiguracaoDisjuntor(tamanho_janela=20, limite_taxa_erro=0.5))

    for _ in range(8):
        disjuntor.registrar_sucesso()
    for _ in range(12):
        disjuntor.registrar_falha()

    assert disjuntor.taxa_de_erro() == pytest.approx(0.6)
    assert disjuntor.estado == "aberto"
    assert disjuntor.permite_chamada() is False


def test_disjuntor_nao_abre_com_exatos_50_por_cento():
    """A regra é 'maior que' o limite, não 'maior ou igual'."""
    disjuntor = CircuitBreaker(ConfiguracaoDisjuntor(tamanho_janela=20, limite_taxa_erro=0.5))

    for _ in range(10):
        disjuntor.registrar_sucesso()
    for _ in range(10):
        disjuntor.registrar_falha()

    assert disjuntor.taxa_de_erro() == pytest.approx(0.5)
    assert disjuntor.estado == "fechado"


def test_disjuntor_semiaberto_fecha_apos_sucesso(monkeypatch):
    import time

    disjuntor = CircuitBreaker(
        ConfiguracaoDisjuntor(tamanho_janela=4, limite_taxa_erro=0.5, intervalo_semiaberto_segundos=0.01)
    )
    for _ in range(4):
        disjuntor.registrar_falha()
    assert disjuntor.estado == "aberto"

    time.sleep(0.02)
    assert disjuntor.estado == "semiaberto"

    disjuntor.registrar_sucesso()
    assert disjuntor.estado == "fechado"
    assert disjuntor.taxa_de_erro() == 0.0  # a janela foi reiniciada


def test_disjuntor_janela_nao_cresce_sem_limite_sob_volume_sustentado():
    """Unidade 4, Aula 14 — o equivalente, neste projeto, a um teste de
    duração (soak): o que um teste de carga de trinta minutos não revela é
    exatamente o que um volume sustentado revela — aqui, se uma estrutura
    interna cresce sem limite. `_janela` é uma lista que deveria ficar
    presa em `tamanho_janela` elementos para sempre, não importa quantas
    chamadas passem por ela; 5.000 chamadas bastam para provar isso sem
    precisar rodar por horas de verdade."""
    disjuntor = CircuitBreaker(ConfiguracaoDisjuntor(tamanho_janela=20, limite_taxa_erro=0.9))

    for i in range(5_000):
        if i % 3 == 0:
            disjuntor.registrar_falha()
        else:
            disjuntor.registrar_sucesso()
        assert len(disjuntor._janela) <= 20


def test_disjuntor_semiaberto_reabre_apos_nova_falha():
    import time

    disjuntor = CircuitBreaker(
        ConfiguracaoDisjuntor(tamanho_janela=4, limite_taxa_erro=0.5, intervalo_semiaberto_segundos=0.01)
    )
    for _ in range(4):
        disjuntor.registrar_falha()
    time.sleep(0.02)
    assert disjuntor.estado == "semiaberto"

    disjuntor.registrar_falha()
    assert disjuntor.estado == "aberto"


# --- backoff_com_jitter ---------------------------------------------------


def test_backoff_dobra_a_cada_tentativa_ate_o_teto():
    """Reproduz a progressão da Aula 2: 200, 400, 800, 1600, 3200 ms."""
    esperado_ms = [200, 400, 800, 1600, 3200]
    for tentativa, exponencial_esperado in enumerate(esperado_ms):
        tempo = backoff_com_jitter(tentativa, base_ms=200, teto_ms=5000, jitter_maximo_ms=0)
        assert tempo == pytest.approx(exponencial_esperado / 1000)


def test_backoff_respeita_o_teto():
    tempo = backoff_com_jitter(10, base_ms=200, teto_ms=5000, jitter_maximo_ms=0)
    assert tempo == pytest.approx(5.0)


def test_backoff_adiciona_jitter_dentro_do_intervalo():
    valores = {backoff_com_jitter(0, base_ms=200, teto_ms=5000, jitter_maximo_ms=100) for _ in range(20)}
    assert all(0.2 <= v <= 0.3 for v in valores)
    assert len(valores) > 1  # o jitter realmente varia entre chamadas


# --- ClienteResiliente -----------------------------------------------------


def _cliente_com_transporte(handler) -> httpx.AsyncClient:
    return httpx.AsyncClient(transport=httpx.MockTransport(handler))


@pytest.mark.asyncio
async def test_cliente_resiliente_repete_apos_falha_transitoria_e_depois_sucede():
    chamadas = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        chamadas["n"] += 1
        if chamadas["n"] < 3:
            return httpx.Response(503)
        return httpx.Response(201, json={"reserva_id": "abc"})

    disjuntor = CircuitBreaker()
    cliente = ClienteResiliente(_cliente_com_transporte(handler), disjuntor, max_tentativas=3)

    resposta = await cliente.post("http://estoque/reservas", json={}, trace_id="t1")

    assert resposta.status_code == 201
    assert chamadas["n"] == 3


@pytest.mark.asyncio
async def test_cliente_resiliente_desiste_apos_max_tentativas():
    def handler(request: httpx.Request) -> httpx.Response:
        return httpx.Response(503)

    disjuntor = CircuitBreaker()
    cliente = ClienteResiliente(_cliente_com_transporte(handler), disjuntor, max_tentativas=3)

    with pytest.raises(Exception):
        await cliente.post("http://estoque/reservas", json={}, trace_id="t1")


@pytest.mark.asyncio
async def test_cliente_resiliente_recusa_chamada_com_disjuntor_aberto_sem_tocar_rede():
    chamadas = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        chamadas["n"] += 1
        return httpx.Response(503)

    disjuntor = CircuitBreaker(ConfiguracaoDisjuntor(tamanho_janela=4, limite_taxa_erro=0.5))
    cliente = ClienteResiliente(_cliente_com_transporte(handler), disjuntor, max_tentativas=1)

    # Quatro chamadas de uma tentativa cada, todas falhando -> disjuntor abre.
    for _ in range(4):
        with pytest.raises(Exception):
            await cliente.post("http://estoque/reservas", json={}, trace_id="t1")

    assert disjuntor.estado == "aberto"
    chamadas_antes_de_abrir = chamadas["n"]

    with pytest.raises(CircuitoAberto):
        await cliente.post("http://estoque/reservas", json={}, trace_id="t1")

    # A quinta tentativa não incrementou o contador do handler: nunca tocou a rede.
    assert chamadas["n"] == chamadas_antes_de_abrir
