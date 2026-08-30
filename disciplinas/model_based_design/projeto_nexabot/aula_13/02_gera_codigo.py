#!/usr/bin/env python3
"""Aula 13 — Gera o código C (script 2/4).

Instancia um `DiscretePID` com os ganhos de referência do NexaBot, gera
`pid_controller.h`/`.c` com `nexabot.codegen.generate.generate_pid_controller`
e imprime o C gerado na tela, junto com o bloco de rastreabilidade e o hash
dos parâmetros — a evidência de que o arquivo veio do modelo, não de
digitação manual.

Também demonstra a PROPRIEDADE central de um gerador de código correto:
gerar duas vezes com os MESMOS ganhos produz o MESMO hash de parâmetros
(determinismo), e gerar com ganhos DIFERENTES produz um hash diferente.

Rodar:
    .venv/bin/python aula_13/02_gera_codigo.py

Saída esperada (resumo): caminhos dos arquivos gerados, o conteúdo de
`pid_controller.c`, e duas checagens "OK" de determinismo do hash.

Rastreabilidade: evidência de TESTE de REQ-CODEGEN-002 (rastreabilidade
automática no cabeçalho do arquivo gerado) — verifica que o hash muda se,
e somente se, os parâmetros do modelo mudam.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from nexabot.codegen.generate import generate_pid_controller  # noqa: E402
from nexabot.controllers import DiscretePID  # noqa: E402


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def main() -> None:
    print(linha("="))
    print("Aula 13 — Geração de código C a partir do modelo DiscretePID")
    print(linha("="))

    pid = DiscretePID(Kp=2.0, Ki=40.0, Kd=0.02)
    print(f"\nGanhos do modelo: Kp={pid.Kp}, Ki={pid.Ki}, Kd={pid.Kd}, "
          f"Ts={pid.Ts}, u_max={pid.u_max}, tau_f={pid.tau_f}, Kaw={pid.Kaw}")

    resultado = generate_pid_controller(pid)
    print(f"\nArquivos gerados:")
    print(f"  {resultado.header_path}")
    print(f"  {resultado.source_path}")
    print(f"\nHash SHA-256 dos parâmetros: {resultado.params_hash}")
    print(f"Gerado em (UTC): {resultado.generated_at_iso}")

    print("\n" + linha("-"))
    print(f"Conteúdo de {resultado.source_path.name}:")
    print(linha("-"))
    print(resultado.source_path.read_text(encoding="utf-8"))

    print(linha("="))
    print("Checagem de determinismo do hash de rastreabilidade")
    print(linha("="))

    r2 = generate_pid_controller(pid)
    igual = resultado.params_hash == r2.params_hash
    print(f"Gerar de novo com os MESMOS ganhos -> mesmo hash? "
          f"{'OK' if igual else 'FALHOU'} ({resultado.params_hash[:16]}... == {r2.params_hash[:16]}...)")
    if not igual:
        raise SystemExit(1)

    pid_diferente = DiscretePID(Kp=3.5, Ki=40.0, Kd=0.02)
    r3 = generate_pid_controller(pid_diferente)
    diferente = resultado.params_hash != r3.params_hash
    print(f"Gerar com ganhos DIFERENTES (Kp=3.5) -> hash diferente? "
          f"{'OK' if diferente else 'FALHOU'}")
    if not diferente:
        raise SystemExit(1)

    print("\nConclusão: o hash no cabeçalho do C gerado muda se, e somente se,")
    print("os parâmetros do modelo mudam — rastreabilidade verificável, não alegada.")


if __name__ == "__main__":
    main()
