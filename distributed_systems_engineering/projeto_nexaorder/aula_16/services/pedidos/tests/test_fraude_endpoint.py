"""Prova que o pipeline de detecção de fraude da Aula 15 está de fato
conectado à API, não só testado em isolamento — mesmo padrão de
`test_publicador.py` (Aula 10) para os endpoints administrativos."""

from __future__ import annotations


def test_registrar_tentativa_publica_no_topico_e_ingere_na_janela(cliente_api):
    resposta = cliente_api.post(
        "/_admin/fraude/tentativa", json={"dispositivo_id": "disp-1", "tempo_evento_ms": 0}
    )

    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["aceito"] is True
    assert 0 <= corpo["particao"] < 7  # NUM_PARTICOES_TENTATIVAS do exemplo da aula


def test_contagem_reflete_tentativas_registradas_na_janela(cliente_api):
    for i in range(4):
        cliente_api.post(
            "/_admin/fraude/tentativa", json={"dispositivo_id": "disp-2", "tempo_evento_ms": i * 1000}
        )

    resposta = cliente_api.get("/_admin/fraude/contagem/disp-2?fim_da_janela_ms=3000")

    assert resposta.json()["contagem_na_janela"] == 4


def test_dispositivos_diferentes_tem_contagens_independentes(cliente_api):
    cliente_api.post("/_admin/fraude/tentativa", json={"dispositivo_id": "disp-a", "tempo_evento_ms": 0})

    resposta = cliente_api.get("/_admin/fraude/contagem/disp-b?fim_da_janela_ms=0")

    assert resposta.json()["contagem_na_janela"] == 0
