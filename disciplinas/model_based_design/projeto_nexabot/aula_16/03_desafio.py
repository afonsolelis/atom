#!/usr/bin/env python3
"""Aula 16 — Script 3/3: desafio — feche uma lacuna real da matriz de rastreabilidade.

O que este script faz
----------------------
Roda a matriz de rastreabilidade (Aula 16 script 1) e identifica, de forma
automática, quais requisitos NÃO têm nenhuma evidência de teste — uma
lacuna real do estado ATUAL do projeto, não uma lacuna fabricada para o
exercício. Como outras frentes da disciplina evoluem em paralelo, a lista
muda de execução para execução; o script lida com isso escolhendo, entre
algumas propostas de teste pré-escritas para requisitos conhecidos do
domínio da planta (REQ-PLANT-*), a primeira que ainda representa uma
lacuna real no momento em que roda.

DESAFIO: complete `PROPOSTAS_CONHECIDAS` com a proposta de teste para pelo
menos mais um requisito REQ-PLANT-* (ou amplie para outra família, se
quiser) e rode de novo -- o script mostra qual proposta foi de fato
necessária desta vez.

Como rodar
----------
    .venv/bin/python aula_16/03_desafio.py

Saída esperada (resumo)
------------------------
A lista de requisitos sem evidência de teste no momento em que o script
roda, a proposta de teste escolhida para preencher uma dessas lacunas (ou
uma mensagem de que todas as lacunas conhecidas já foram fechadas), e a
confirmação de que o requisito escolhido de fato carecia de teste.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.rastreabilidade import construir_matriz  # noqa: E402

# DESAFIO: adicione mais entradas aqui (ou amplie para outras famílias REQ-*).
# --- propostas de referência (apague e escreva as suas como exercício) ---
PROPOSTAS_CONHECIDAS: dict[str, str] = {
    "REQ-PLANT-001": (
        "Para os parâmetros de PARAMS, calcular os autovalores de A "
        "(nexabot.plant.state_space_matrices) com numpy.linalg.eigvals e os "
        "polos de nexabot.plant.transfer_function(PARAMS) (via control.tf; "
        "os polos são as raízes do denominador); comparar os dois conjuntos "
        "(ordenados) com numpy.testing.assert_allclose e tolerância relativa "
        "pequena (ex.: 1e-9) -- confirma que as duas representações do "
        "modelo (espaço de estados e função de transferência) descrevem o "
        "MESMO sistema."
    ),
    "REQ-PLANT-002": (
        "Gerar um sinal de controle u_pedido que ultrapasse V_max (ex.: "
        "u_pedido=100V) e chamar nexabot.plant.simulate com esse sinal; "
        "verificar que a tensão efetivamente aplicada (após o clip interno "
        "de simulate) nunca excede PARAMS.V_max em nenhuma amostra, e que a "
        "corrente resultante x[:,0] permanece abaixo de um múltiplo "
        "razoável de PARAMS.i_max (ex.: 2x, para acomodar transitórios)."
    ),
}


def linha(char: str = "-", n: int = 90) -> str:
    return char * n


def escolher_lacuna(sem_teste: list[str]) -> tuple[str, str] | None:
    """Escolhe, entre os requisitos sem evidência de teste, o primeiro para
    o qual há uma proposta pronta em `PROPOSTAS_CONHECIDAS`."""
    for requisito in sem_teste:
        if requisito in PROPOSTAS_CONHECIDAS:
            return requisito, PROPOSTAS_CONHECIDAS[requisito]
    return None


def main() -> None:
    print(linha("="))
    print("Aula 16 — Desafio: proponha um teste para uma lacuna real da matriz")
    print(linha("="))

    resultado = construir_matriz()
    sem_teste = [e.requisito for e in resultado.entradas if not e.arquivos_por_categoria("Teste")]

    print(f"\nRequisitos SEM evidência de teste agora ({len(sem_teste)}):")
    for r in sem_teste:
        marcador = " (proposta pronta abaixo)" if r in PROPOSTAS_CONHECIDAS else ""
        print(f"  - {r}{marcador}")

    escolha = escolher_lacuna(sem_teste)

    print("\n" + linha("="))
    if escolha is None:
        if sem_teste:
            print("Nenhuma das lacunas atuais tem proposta pronta em PROPOSTAS_CONHECIDAS.")
            print("Complete o desafio: escreva uma proposta para um dos requisitos acima.")
            print("(Não é uma falha do script -- é o convite para o exercício.)")
        else:
            print("Nenhuma lacuna encontrada: todos os requisitos já têm evidência de teste.")
            print("(Sinal de que outras frentes da disciplina já fecharam REQ-PLANT-* -- ótimo!")
            print(" Neste caso, o exercício é escolher um requisito e propor um SEGUNDO teste")
            print(" independente para reforçar a cobertura, não preencher uma lacuna vazia.)")
        return

    requisito, proposta = escolha
    print(f"Lacuna escolhida: {requisito}")
    print("\n" + linha("-"))
    print("Proposta de caso de teste:")
    print(linha("-"))
    print(proposta)

    print("\n" + linha("="))
    print(f"Confirmado: {requisito} está de fato entre os {len(sem_teste)} "
          "requisitos sem evidência de teste nesta execução.")
    print("Próximo passo real (fora deste script): escrever o teste em tests/,")
    print("rodá-lo, e então esta mesma lacuna desaparecer da próxima matriz gerada")
    print("por aula_16/01_matriz_rastreabilidade.py -- rastreabilidade que se atualiza")
    print("sozinha, o ponto central desta aula.")


if __name__ == "__main__":
    main()
