#!/usr/bin/env python3
"""Aula 15 — Script 3/4: watchdog real, contra um alvo de verdade travado de propósito.

O que este script faz
----------------------
Usa `nexabot.hil.Watchdog` para chamar `LoopbackTarget.step()` com um
prazo (`deadline_s`). O comando `STEP r y delay_ms` do protocolo (ver
`nexabot/firmware/main_loopback.c`) faz o ALVO DE VERDADE atrasar sua
resposta em `delay_ms` milissegundos antes de responder -- não é um mock
em Python fingindo estar lento, é o subprocesso C realmente dormindo antes
de escrever no pipe.

Demonstra três casos, todos contra o mesmo `LoopbackTarget`/`Watchdog`:

1. resposta dentro do prazo -> passa normalmente;
2. resposta fora do prazo -> o watchdog devolve comando seguro (u=0V) e
   sinaliza a falha (REQ-SAFE-004: torque zero quando o alvo não responde);
3. recuperação -> como uma chamada que já estourou o prazo pode nunca
   terminar, o watchdog encerra o alvo (`target.close()`) em vez de
   arriscar travar o laço host para sempre; o script então reconecta
   (recria o `LoopbackTarget`) e mostra que o laço volta a operar
   normalmente -- o mesmo papel que um supervisor cumpriria reiniciando um
   microcontrolador travado.

Como rodar
----------
    .venv/bin/python aula_15/03_watchdog_real.py

Saída esperada (resumo)
------------------------
Uma tabela com os três casos, mostrando "estourou_prazo" True só no caso 2,
e uma confirmação de que o laço volta a funcionar após a reconexão.
"""

from __future__ import annotations

import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from nexabot.hil import LoopbackTarget, Watchdog  # noqa: E402
from nexabot.params import PARAMS  # noqa: E402


def linha(char: str = "-", n: int = 78) -> str:
    return char * n


def main() -> None:
    print(linha("="))
    print("Aula 15 — Watchdog real contra um alvo travado de propósito")
    print(linha("="))

    ganhos = dict(Kp=2.0, Ki=40.0, Kd=0.02, Ts=PARAMS.Ts, u_max=PARAMS.V_max, tau_f=0.01, Kaw=1.0)
    prazo_s = 3 * ganhos["Ts"]  # 3 períodos de amostragem -- folga razoável sobre Ts=5ms
    print(f"\nPrazo do watchdog: {prazo_s * 1e3:.1f} ms (3x Ts = {ganhos['Ts']*1e3:.1f} ms)")

    target = LoopbackTarget(**ganhos)
    watchdog = Watchdog(deadline_s=prazo_s)

    casos = [
        ("dentro do prazo (delay_ms=0)", 0.0),
        ("FORA do prazo (delay_ms=200, alvo trava de propósito)", 200.0),
    ]

    print("\n" + linha("-"))
    header = f"{'caso':<55} | {'u [V]':>8} | {'estourou_prazo':>15} | {'tempo real [ms]':>15}"
    print(header)
    print(linha("-", len(header)))

    resultados = []
    for descricao, delay_ms in casos:
        inicio = time.perf_counter()
        u, estourou = watchdog.guarded_step(target, r=3.0, y=0.0, delay_ms=delay_ms)
        tempo_real_ms = (time.perf_counter() - inicio) * 1e3
        resultados.append((descricao, u, estourou, tempo_real_ms))
        print(f"{descricao:<55} | {u:>8.3f} | {str(estourou):>15} | {tempo_real_ms:>15.2f}")

    print(f"\nNota sobre a coluna 'tempo real': o watchdog DETECTA o estouro em ~{prazo_s*1e3:.0f} ms")
    print("(o prazo declarado) -- o tempo total maior no caso 2 é o custo de encerrar")
    print("de verdade um alvo que ainda está processando a resposta lenta: `close()`")
    print("tenta um encerramento gracioso (QUIT), e o processo só consegue ler esse")
    print("comando depois de terminar de dormir e escrever a resposta pendente no")
    print("pipe -- só se isso também não terminar em 2s é que `close()` mata o")
    print("processo à força. Ou seja: a DECISÃO do watchdog (u=0V seguro) já foi")
    print("tomada no prazo declarado; o tempo extra é só o custo de desligar o alvo.")

    print("\n" + linha("-"))
    print("Após o estouro, o watchdog encerrou o processo do alvo (kill_target_on_timeout=True).")
    print("Um supervisor real reconectaria/reiniciaria o alvo antes de continuar o laço:")
    target = LoopbackTarget(**ganhos)  # "reboot" do alvo, como um supervisor faria
    u_pos_recuperacao, estourou_pos = watchdog.guarded_step(target, r=3.0, y=0.0)
    print(f"  novo LoopbackTarget criado, step normal -> u={u_pos_recuperacao:.3f} V, "
          f"estourou_prazo={estourou_pos}")

    watchdog.close()
    target.close()

    print("\n" + linha("="))
    print("Verificações:")
    ok_caso1 = resultados[0][2] is False
    ok_caso2 = resultados[1][2] is True and resultados[1][1] == 0.0
    ok_recuperacao = estourou_pos is False and u_pos_recuperacao != 0.0
    print(f"  caso 1 (dentro do prazo) não estourou:            {'OK' if ok_caso1 else 'FALHOU'}")
    print(f"  caso 2 (fora do prazo) estourou com u=0V seguro:  {'OK' if ok_caso2 else 'FALHOU'}")
    print(f"  recuperação após reconectar o alvo funciona:      {'OK' if ok_recuperacao else 'FALHOU'}")

    if not (ok_caso1 and ok_caso2 and ok_recuperacao):
        raise SystemExit(1)

    print("\nLição (REQ-SAFE-004): um watchdog não é só 'esperar menos' -- é decidir o que")
    print("fazer quando o prazo estoura (comando seguro) E como se recuperar sem travar")
    print("o laço host esperando por uma resposta que pode nunca chegar.")


if __name__ == "__main__":
    main()
