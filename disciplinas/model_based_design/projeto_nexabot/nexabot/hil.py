"""Camada HIL (Hardware-in-the-Loop) do NexaBot.

A planta roda em Python (RK4 de passo fixo, a mesma integração de
`nexabot.plant.simulate`), em tempo real ou acelerada; o controlador roda
"no alvo" — um processo separado que fala um protocolo de linha simples,
o mesmo em ambos os back-ends:

- `LoopbackTarget`: o executável C compilado (`nexabot/firmware/main_loopback.c`,
  ligado ao PID gerado na Aula 13) rodando como subprocesso local, lendo e
  escrevendo em stdin/stdout. Funciona de verdade neste ambiente sem
  hardware — é o back-end usado para gravar a Aula 15.
- `SerialTarget`: a mesma interface sobre uma porta serial real
  (ESP32/Arduino, ver `nexabot/firmware/src/main.cpp`), via `pyserial`.
  Requer hardware conectado — não roda nesta máquina.

`run_closed_loop_hil` fecha a malha e mede jitter (variação do período do
laço) e latência (tempo de ida-e-volta de cada `target.step()`) — as duas
métricas que decidem se um laço de controle discreto pode ser confiável em
um alvo real.

Rastreabilidade: REQ-CTRL-001..003 (o alvo reproduz o contrato de
DiscretePID), REQ-SAFE-004 (watchdog: zerar torque quando o alvo não
responde dentro do prazo).
"""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import time
from abc import ABC, abstractmethod
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeoutError
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import numpy as np

from . import plant
from .codegen.generate import generate_pid_controller
from .controllers import DiscretePID
from .params import PARAMS, NexaBotParams

FIRMWARE_DIR = Path(__file__).parent / "firmware"


class TargetError(RuntimeError):
    """Erro de protocolo ou de comunicação com o alvo HIL."""


class Target(ABC):
    """Interface comum de um alvo HIL: um PID rodando "fora" do processo
    host, acessível pelo protocolo de linha documentado em
    `nexabot/firmware/main_loopback.c`."""

    @abstractmethod
    def step(self, r: float, y: float, delay_ms: float = 0.0) -> float:
        """Pede um passo de controle e devolve u[k] [V].

        `delay_ms` (opcional, só usado em testes de watchdog) pede ao alvo
        que atrase sua resposta propositalmente — simula um laço lento ou
        travado sem precisar derrubar o processo.
        """

    @abstractmethod
    def reset(self) -> None:
        """Zera o estado interno do controlador no alvo (REQ-SAFE-004)."""

    @abstractmethod
    def close(self) -> None:
        """Encerra a comunicação com o alvo e libera recursos."""


@dataclass
class LoopbackTarget(Target):
    """Alvo rodando como subprocesso local: `main_loopback` compilado e
    ligado ao PID gerado a partir dos mesmos ganhos.

    Compila o firmware de loopback com o C gerado pela Aula 13 na
    construção do objeto — cada instância é, portanto, um alvo com os
    ganhos exatos passados aqui, exatamente como aconteceria ao gravar
    esses ganhos na flash de um microcontrolador real.
    """

    Kp: float
    Ki: float
    Kd: float = 0.0
    Ts: float = PARAMS.Ts
    u_max: float = PARAMS.V_max
    tau_f: float = 0.01
    Kaw: float = 1.0
    build_dir: Path | None = None

    def __post_init__(self) -> None:
        gcc = shutil.which("gcc")
        if gcc is None:
            raise TargetError(
                "gcc não encontrado no PATH — necessário para compilar "
                "main_loopback.c com o PID gerado."
            )

        pid_model = DiscretePID(
            Kp=self.Kp, Ki=self.Ki, Kd=self.Kd, Ts=self.Ts,
            u_max=self.u_max, tau_f=self.tau_f, Kaw=self.Kaw,
        )
        self._tmpdir = None
        if self.build_dir is None:
            self._tmpdir = tempfile.TemporaryDirectory(prefix="nexabot_hil_")
            build_dir = Path(self._tmpdir.name)
        else:
            build_dir = Path(self.build_dir)
            build_dir.mkdir(parents=True, exist_ok=True)

        self.generated = generate_pid_controller(pid_model, output_dir=build_dir)

        exe_path = build_dir / "loopback_target"
        cmd = [
            gcc, "-std=c11", "-Wall", "-Wextra", "-O2",
            "-I", str(build_dir),
            str(FIRMWARE_DIR / "main_loopback.c"),
            str(self.generated.source_path),
            "-o", str(exe_path), "-lm",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            raise TargetError(f"gcc falhou ao compilar main_loopback.c:\n{result.stderr}")
        self.exe_path = exe_path

        self._proc = subprocess.Popen(
            [str(exe_path), repr(self.Kp), repr(self.Ki), repr(self.Kd),
             repr(self.Ts), repr(self.u_max), repr(self.tau_f), repr(self.Kaw)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            text=True, bufsize=1,
        )

    def step(self, r: float, y: float, delay_ms: float = 0.0) -> float:
        if self._proc.poll() is not None:
            raise TargetError("processo do alvo loopback já encerrou")
        assert self._proc.stdin is not None and self._proc.stdout is not None
        if delay_ms:
            self._proc.stdin.write(f"STEP {r!r} {y!r} {delay_ms!r}\n")
        else:
            self._proc.stdin.write(f"STEP {r!r} {y!r}\n")
        self._proc.stdin.flush()
        line = self._proc.stdout.readline()
        if not line:
            err = self._proc.stderr.read() if self._proc.stderr else ""
            raise TargetError(f"alvo loopback encerrou inesperadamente: {err}")
        parts = line.strip().split()
        if len(parts) != 2 or parts[0] != "U":
            raise TargetError(f"resposta inesperada do alvo: {line!r}")
        return float(parts[1])

    def reset(self) -> None:
        assert self._proc.stdin is not None and self._proc.stdout is not None
        self._proc.stdin.write("RESET\n")
        self._proc.stdin.flush()
        line = self._proc.stdout.readline()
        if line.strip() != "OK":
            raise TargetError(f"RESET não confirmado pelo alvo: {line!r}")

    def close(self) -> None:
        if self._proc.poll() is None:
            try:
                if self._proc.stdin is not None:
                    self._proc.stdin.write("QUIT\n")
                    self._proc.stdin.flush()
                self._proc.wait(timeout=2.0)
            except Exception:
                self._proc.kill()
        if self._tmpdir is not None:
            self._tmpdir.cleanup()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass


@dataclass
class SerialTarget(Target):
    """Alvo real por porta serial (ESP32/Arduino), mesmo protocolo de linha
    do `LoopbackTarget` — ver `nexabot/firmware/src/main.cpp` e
    `platformio.ini`.

    Requer hardware físico conectado a `port`; não roda nesta máquina de
    desenvolvimento (sem placa conectada). Existe para que o mesmo código
    de laço de controle (`run_closed_loop_hil`) funcione sem alteração ao
    trocar de "PC sem hardware" para "bancada com ESP32 real".
    """

    port: str
    baudrate: int = 115200
    timeout_s: float = 1.0
    boot_delay_s: float = 2.0

    def __post_init__(self) -> None:
        try:
            import serial
        except ImportError as exc:  # pragma: no cover - pyserial já é dependência do projeto
            raise TargetError(
                "pyserial não disponível — necessário para SerialTarget."
            ) from exc
        self._serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout_s)
        # ESP32/Arduino reiniciam ao abrir a porta serial (reset por DTR); é
        # preciso aguardar o boot antes de trocar mensagens.
        time.sleep(self.boot_delay_s)

    def step(self, r: float, y: float, delay_ms: float = 0.0) -> float:
        if delay_ms:
            msg = f"STEP {r!r} {y!r} {delay_ms!r}\n"
        else:
            msg = f"STEP {r!r} {y!r}\n"
        self._serial.write(msg.encode("ascii"))
        line = self._serial.readline().decode("ascii", errors="replace").strip()
        if not line.startswith("U "):
            raise TargetError(f"resposta inesperada do alvo serial: {line!r}")
        return float(line[2:])

    def reset(self) -> None:
        self._serial.write(b"RESET\n")
        line = self._serial.readline().decode("ascii", errors="replace").strip()
        if line != "OK":
            raise TargetError(f"RESET não confirmado pelo alvo serial: {line!r}")

    def close(self) -> None:
        self._serial.close()


@dataclass
class HilRunResult:
    """Log de uma execução de `run_closed_loop_hil` com métricas de tempo."""

    t: np.ndarray
    r: np.ndarray
    y: np.ndarray
    u: np.ndarray
    latencias_s: np.ndarray
    periodos_loop_s: np.ndarray
    Ts_nominal_s: float

    @property
    def jitter_stats(self) -> dict:
        """Estatísticas de jitter (variação do período do laço) e latência
        (tempo de ida-e-volta de cada chamada ao alvo), em milissegundos."""
        periodos_ms = self.periodos_loop_s * 1e3
        desvio_ms = (self.periodos_loop_s - self.Ts_nominal_s) * 1e3
        lat_ms = self.latencias_s * 1e3
        return {
            "n_amostras": int(len(self.latencias_s)),
            "Ts_nominal_ms": self.Ts_nominal_s * 1e3,
            "periodo_medio_ms": float(np.mean(periodos_ms)) if len(periodos_ms) else float("nan"),
            "jitter_desvio_padrao_ms": float(np.std(desvio_ms)) if len(desvio_ms) else float("nan"),
            "jitter_pico_a_pico_ms": (
                float(np.max(periodos_ms) - np.min(periodos_ms)) if len(periodos_ms) else float("nan")
            ),
            "atraso_maximo_ms": float(np.max(np.abs(desvio_ms))) if len(desvio_ms) else float("nan"),
            "latencia_media_ms": float(np.mean(lat_ms)),
            "latencia_p95_ms": float(np.percentile(lat_ms, 95)),
            "latencia_maxima_ms": float(np.max(lat_ms)),
        }


def run_closed_loop_hil(
    target: Target,
    r_of_t: Callable[[float], float],
    t_end: float,
    Ts: float = PARAMS.Ts,
    p: NexaBotParams = PARAMS,
    real_time: bool = True,
    dt_integration: float = 1.0e-4,
) -> HilRunResult:
    """Fecha a malha planta (Python) + controlador (alvo) por `t_end` segundos.

    Com `real_time=True` (padrão), o laço dorme o tempo necessário para
    respeitar `Ts` de parede a parede — é o modo que produz jitter/latência
    comparáveis a um laço embarcado de verdade. Com `real_time=False`, o
    laço roda o mais rápido possível (útil em regressão/CI, onde só
    interessa a trajetória, não o tempo real).
    """
    n_steps = int(round(t_end / Ts))
    t_log = np.zeros(n_steps + 1)
    y_log = np.zeros(n_steps + 1)
    u_log = np.zeros(n_steps)
    r_log = np.zeros(n_steps)
    latencias = np.zeros(n_steps)
    loop_starts = np.zeros(n_steps)

    x = np.zeros(2)  # [corrente, velocidade angular do motor]
    target.reset()
    t = 0.0

    n_sub = max(1, int(round(Ts / dt_integration)))
    sub_dt = Ts / n_sub

    for k in range(n_steps):
        loop_starts[k] = time.perf_counter()

        r = float(r_of_t(t))
        y = float(x[1])

        call_start = time.perf_counter()
        u = target.step(r, y)
        latencias[k] = time.perf_counter() - call_start

        for _ in range(n_sub):
            k1 = plant.derivative(x, u, 0.0, p)
            k2 = plant.derivative(x + 0.5 * sub_dt * k1, u, 0.0, p)
            k3 = plant.derivative(x + 0.5 * sub_dt * k2, u, 0.0, p)
            k4 = plant.derivative(x + sub_dt * k3, u, 0.0, p)
            x = x + (sub_dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

        t += Ts
        t_log[k + 1] = t
        y_log[k + 1] = x[1]
        u_log[k] = u
        r_log[k] = r

        if real_time:
            elapsed = time.perf_counter() - loop_starts[k]
            remaining = Ts - elapsed
            if remaining > 0:
                time.sleep(remaining)

    y_log[0] = 0.0
    periodos = np.diff(loop_starts) if n_steps > 1 else np.array([])

    return HilRunResult(
        t=t_log[:-1], r=r_log, y=y_log[:-1], u=u_log,
        latencias_s=latencias, periodos_loop_s=periodos, Ts_nominal_s=Ts,
    )


@dataclass
class Watchdog:
    """Watchdog de prazo do laço de controle (REQ-SAFE-004).

    Executa `target.step(...)` em uma thread auxiliar e impõe um prazo
    (`deadline_s`); se o alvo não responder a tempo, devolve comando seguro
    (torque zero) e sinaliza a falha — em vez de travar o laço host
    esperando indefinidamente por um alvo que pode nunca responder (UART
    engasgada, firmware travado, etc.).
    """

    deadline_s: float
    kill_target_on_timeout: bool = True
    _executor: ThreadPoolExecutor = field(
        default_factory=lambda: ThreadPoolExecutor(max_workers=1), repr=False
    )

    def guarded_step(self, target: Target, r: float, y: float, delay_ms: float = 0.0):
        """Devolve `(u, estourou_prazo)`. Em estouro, `u = 0.0` (seguro).

        Importante: um `target.step()` que já estourou o prazo pode nunca
        responder (UART travada, firmware em loop infinito) — não é seguro
        simplesmente "esperar mais um pouco" na próxima chamada, porque a
        thread auxiliar continuaria ocupada pela chamada antiga para
        sempre. Por isso, por padrão (`kill_target_on_timeout=True`), um
        estouro força o encerramento do alvo (`target.close()`), como um
        watchdog real reiniciaria um microcontrolador travado: a chamada
        pendente é liberada (o pipe fecha, a leitura bloqueada recebe EOF)
        e cabe ao chamador reconectar/recriar o alvo antes do próximo passo
        — exatamente o papel do supervisor (REQ-SAFE-004).
        """
        future = self._executor.submit(target.step, r, y, delay_ms)
        try:
            u = future.result(timeout=self.deadline_s)
            return float(u), False
        except FutureTimeoutError:
            if self.kill_target_on_timeout:
                try:
                    target.close()
                except Exception:
                    pass
            return 0.0, True

    def close(self) -> None:
        self._executor.shutdown(wait=False, cancel_futures=True)
