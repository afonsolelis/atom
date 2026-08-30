#!/usr/bin/env python3
"""Aula 1 — Script 4/5: o V-Model de MBD mapeado nas 16 aulas da disciplina.

O que este script demonstra
----------------------------
Model-Based Design segue classicamente o "V-Model": requisitos e arquitetura
descem pelo lado esquerdo do V até a implementação, e verificação/validação
sobem pelo lado direito, testando contra o mesmo nível de especificação em
que desceram. Este script imprime o V-Model do NexaBot com as 16 aulas da
disciplina posicionadas em cada degrau — é o mapa mental que os alunos vão
usar até a Aula 16.

Como rodar
----------
    .venv/bin/python aula_01/04_v_model.py
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexabot import viz  # noqa: E402

# (lado, nível, rótulo, aulas)  — "esq" desce (definição), "dir" sobe (V&V)
DEGRAUS = [
    ("esq", "Requisitos do sistema (REQ-*)", "Aulas 1-2"),
    ("esq", "Arquitetura e modelo de planta (EDO -> espaço de estados)", "Aulas 2-3"),
    ("esq", "Projeto de controle (PID, alocação de polos, LQR)", "Aulas 4-6"),
    ("esq", "Discretização e implementação embarcada (Ts, C, HIL)", "Aulas 7, 13-14"),
    ("fundo", "CÓDIGO EMBARCADO / FIRMWARE DO NEXABOT", "Aula 13 (codegen)"),
    ("dir", "Teste unitário do controlador discreto (SIL)", "Aula 15"),
    ("dir", "Co-simulação planta + controlador (FMU / cosim)", "Aulas 11-12"),
    ("dir", "Verificação formal de propriedades de segurança (model checking)", "Aula 10"),
    ("dir", "Teste baseado em modelo (MBT) do supervisor de missão", "Aula 9"),
    ("dir", "Validação em hardware-in-the-loop (HIL) e aceitação final", "Aula 16"),
]


def _linha_v(indice_total: int, indice: int, largura: int) -> str:
    """Desenha uma linha do "V" com o texto do degrau centralizado no braço certo."""
    meio = largura // 2
    passo = meio // max(1, indice_total)
    recuo_esq = passo * (indice_total - indice)
    recuo_dir = passo * (indice_total - indice)
    linha = [" "] * largura
    if 0 <= recuo_esq < largura:
        linha[recuo_esq] = "\\"
    pos_dir = largura - 1 - recuo_dir
    if 0 <= pos_dir < largura:
        linha[pos_dir] = "/"
    return "".join(linha)


def desenhar_v_model() -> None:
    """Imprime o V-Model em modo ASCII, com as aulas anotadas em cada braço."""
    n_esq = sum(1 for lado, *_ in DEGRAUS if lado == "esq")
    n_dir = sum(1 for lado, *_ in DEGRAUS if lado == "dir")
    n_max = max(n_esq, n_dir)
    largura = 2 * n_max * 3 + 3

    esquerda = [d for d in DEGRAUS if d[0] == "esq"]
    direita = [d for d in DEGRAUS if d[0] == "dir"]
    fundo = [d for d in DEGRAUS if d[0] == "fundo"][0]

    print(viz.negrito("Lado esquerdo do V — DEFINIÇÃO (desce)") + "      " +
          viz.negrito("Lado direito do V — VERIFICAÇÃO/VALIDAÇÃO (sobe)"))
    print()
    for i, (_, rotulo, aulas) in enumerate(esquerda):
        print(f"  ▸ {rotulo}  [{viz.amarelo(aulas)}]")
        print(_linha_v(n_esq, i + 1, largura))

    print(f"\n  {viz.vermelho('▣')} {viz.negrito(fundo[1])}  [{viz.amarelo(fundo[2])}]\n")

    for i, (_, rotulo, aulas) in enumerate(reversed(direita)):
        print(_linha_v(n_dir, len(direita) - i, largura))
        print(f"  {'▸'} {rotulo}  [{viz.amarelo(aulas)}]")


def main() -> int:
    print(viz.titulo("NexaBot — Aula 1 — O V-Model de MBD e as 16 aulas da disciplina"))

    desenhar_v_model()

    print()
    linhas = [[str(i + 1), rotulo, aulas, "definição" if lado == "esq" else
               ("implementação" if lado == "fundo" else "verificação/validação")]
              for i, (lado, rotulo, aulas) in enumerate(DEGRAUS)]
    viz.tabela(["#", "degrau do V-Model", "aulas", "papel"], linhas,
               titulo_tabela="Tabela de rastreabilidade: degrau -> aulas")

    print("\n" + viz.negrito("Ponto pedagógico:"))
    print("  Cada seta que desce a esquerda tem uma seta correspondente subindo a")
    print("  direita, no MESMO nível de abstração: o modelo de planta da Aula 2-3 é")
    print("  verificado pela co-simulação das Aulas 11-12; o controlador discreto da")
    print("  Aula 7 é verificado pelo teste unitário SIL da Aula 15; os requisitos da")
    print("  Aula 1 só se fecham com a validação HIL da Aula 16. Isso é rastreabilidade")
    print("  de ponta a ponta — o motivo de existir um REQ-* em cada arquivo do projeto.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
