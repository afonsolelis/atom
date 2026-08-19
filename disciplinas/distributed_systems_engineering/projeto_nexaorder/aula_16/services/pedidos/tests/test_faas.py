"""Prova o custo de inicialização a frio e por que ele importa em um
caminho síncrono, mas não em um assíncrono — Unidade 4, Aula 15."""

from __future__ import annotations

from app.faas import AmbienteFaas

LIMITE_SLI_LATENCIA_DO_CHECKOUT_MS = 300  # o mesmo limite do exemplo de SLO da Aula 13


def test_primeira_invocacao_de_uma_funcao_e_sempre_fria():
    ambiente = AmbienteFaas()

    resultado = ambiente.invocar("enviar_email_confirmacao", agora_ms=0, duracao_execucao_ms=50)

    assert resultado.houve_inicializacao_a_frio is True
    assert resultado.latencia_total_ms == 450


def test_segunda_invocacao_dentro_da_janela_de_aquecimento_e_quente():
    ambiente = AmbienteFaas()
    ambiente.invocar("enviar_email_confirmacao", agora_ms=0, duracao_execucao_ms=50)

    resultado = ambiente.invocar("enviar_email_confirmacao", agora_ms=1_000, duracao_execucao_ms=50)

    assert resultado.houve_inicializacao_a_frio is False
    assert resultado.latencia_total_ms == 50


def test_invocacao_apos_a_janela_de_aquecimento_volta_a_ser_fria():
    ambiente = AmbienteFaas(janela_de_aquecimento_ms=60_000)
    ambiente.invocar("enviar_email_confirmacao", agora_ms=0, duracao_execucao_ms=50)

    resultado = ambiente.invocar("enviar_email_confirmacao", agora_ms=120_000, duracao_execucao_ms=50)

    assert resultado.houve_inicializacao_a_frio is True


def test_funcoes_diferentes_tem_estado_de_aquecimento_independente():
    ambiente = AmbienteFaas()
    ambiente.invocar("enviar_email_confirmacao", agora_ms=0, duracao_execucao_ms=50)

    resultado_outra_funcao = ambiente.invocar("gerar_nota_fiscal", agora_ms=1_000, duracao_execucao_ms=50)

    assert resultado_outra_funcao.houve_inicializacao_a_frio is True


def test_cold_start_fora_do_caminho_sincrono_e_imperceptivel():
    """A confirmação por e-mail é assíncrona (Aula 8/10) — mesmo fria, a
    latência não é percebida por ninguém no checkout."""
    ambiente = AmbienteFaas()

    resultado = ambiente.invocar("enviar_email_confirmacao", agora_ms=0, duracao_execucao_ms=50)

    assert resultado.latencia_total_ms < 1_000


def test_cold_start_no_caminho_sincrono_estoura_o_sli_de_latencia_da_aula_13():
    """Se 'avaliar_risco_no_checkout' fosse uma FaaS fria no caminho
    síncrono da compra, o custo de inicialização sozinho já ultrapassaria
    o limite de 300ms do exemplo de SLI de latência da Aula 13 — o
    argumento exato do roteiro para não usar FaaS onde o cold start
    incide sobre o p95 prometido."""
    ambiente = AmbienteFaas()

    resultado = ambiente.invocar("avaliar_risco_no_checkout", agora_ms=0, duracao_execucao_ms=20)

    assert resultado.latencia_total_ms > LIMITE_SLI_LATENCIA_DO_CHECKOUT_MS
