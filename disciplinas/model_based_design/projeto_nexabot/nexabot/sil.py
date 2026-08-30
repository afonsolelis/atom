"""Ponte SIL (Software-in-the-Loop) do NexaBot.

Compila o C gerado pela Aula 13 (`nexabot.codegen.generate`) como biblioteca
compartilhada com `gcc` e o carrega em processo via `ctypes`, expondo uma
classe `SILController` com a mesma interface `.step(r, y)` do modelo de
referência `nexabot.controllers.DiscretePID`.

O ponto central da Aula 14 é `compare_model_vs_code`: roda o modelo Python e
o código C compilado sobre a mesma sequência de entradas e devolve o erro
máximo absoluto amostra a amostra — a evidência de que "o código gerado é
equivalente ao modelo" deixa de ser uma alegação e passa a ser um número
medido.

Rastreabilidade: REQ-CODEGEN-001 (equivalência numérica código gerado x
modelo), REQ-CTRL-001..003 (o contrato numérico verificado é o de
`DiscretePID`).
"""

from __future__ import annotations

import ctypes
import shutil
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from .codegen.generate import generate_pid_controller
from .controllers import DiscretePID

GCC = shutil.which("gcc")


class SILCompilationError(RuntimeError):
    """Erro ao compilar o C gerado como biblioteca compartilhada."""


def _find_gcc() -> str:
    if GCC is None:
        raise SILCompilationError(
            "gcc não encontrado no PATH — necessário para compilar o C gerado "
            "em biblioteca compartilhada (SIL). Instale gcc (build-essential)."
        )
    return GCC


class _PidCStruct(ctypes.Structure):
    """Layout idêntico a `pid_controller_t` (todos os campos `double`, sem
    padding relevante — ordem tem que bater exatamente com o `.h` gerado)."""

    _fields_ = [
        ("Kp", ctypes.c_double),
        ("Ki", ctypes.c_double),
        ("Kd", ctypes.c_double),
        ("Ts", ctypes.c_double),
        ("u_max", ctypes.c_double),
        ("tau_f", ctypes.c_double),
        ("Kaw", ctypes.c_double),
        ("integral", ctypes.c_double),
        ("e_prev", ctypes.c_double),
        ("d_state", ctypes.c_double),
    ]


class _PidFixedCStruct(ctypes.Structure):
    """Layout idêntico a `pid_fixed_controller_t` (todos os campos int32_t)."""

    _fields_ = [
        ("Kp", ctypes.c_int32),
        ("Ki", ctypes.c_int32),
        ("Kd", ctypes.c_int32),
        ("Ts", ctypes.c_int32),
        ("u_max", ctypes.c_int32),
        ("tau_f", ctypes.c_int32),
        ("Kaw", ctypes.c_int32),
        ("integral", ctypes.c_int32),
        ("e_prev", ctypes.c_int32),
        ("d_state", ctypes.c_int32),
    ]


def compile_shared_library(
    source_path: Path, output_dir: Path | None = None, extra_cflags: tuple[str, ...] = ()
) -> Path:
    """Compila `source_path` (e o `.h` no mesmo diretório) em uma `.so`.

    Usa `-O2` (otimizado, como em produção) por padrão; passe
    `extra_cflags=("-O0",)` para depuração sem otimização.
    """
    gcc = _find_gcc()
    source_path = Path(source_path)
    output_dir = Path(output_dir) if output_dir else source_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    lib_path = output_dir / "libpid_sil.so"

    cmd = [
        gcc,
        "-std=c11",
        "-Wall",
        "-Wextra",
        "-O2",
        *extra_cflags,
        "-fPIC",
        "-shared",
        "-o",
        str(lib_path),
        str(source_path),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise SILCompilationError(
            f"gcc falhou ao compilar {source_path.name}:\n{result.stderr}"
        )
    return lib_path


@dataclass
class SILController:
    """Controlador PID rodando como código C compilado, via ctypes.

    Mesma interface pública de `DiscretePID`: construa com os ganhos e chame
    `.step(r, y)` a cada amostra. Internamente delega para `pid_step` (ou
    `pid_fixed_step`, se `fixed_point=True`) na biblioteca compartilhada.
    """

    Kp: float
    Ki: float
    Kd: float = 0.0
    Ts: float = 5.0e-3
    u_max: float = 24.0
    tau_f: float = 0.01
    Kaw: float = 1.0
    fixed_point: bool = False
    build_dir: Path | None = None

    def __post_init__(self) -> None:
        pid_model = DiscretePID(
            Kp=self.Kp, Ki=self.Ki, Kd=self.Kd, Ts=self.Ts,
            u_max=self.u_max, tau_f=self.tau_f, Kaw=self.Kaw,
        )
        self._tmpdir = None
        if self.build_dir is None:
            self._tmpdir = tempfile.TemporaryDirectory(prefix="nexabot_sil_")
            build_dir = Path(self._tmpdir.name)
        else:
            build_dir = Path(self.build_dir)

        self.generated = generate_pid_controller(pid_model, output_dir=build_dir)
        self.lib_path = compile_shared_library(self.generated.source_path, build_dir)
        self._lib = ctypes.CDLL(str(self.lib_path))

        if self.fixed_point:
            self._struct = _PidFixedCStruct()
            self._lib.pid_fixed_init.argtypes = [
                ctypes.POINTER(_PidFixedCStruct),
                ctypes.c_double, ctypes.c_double, ctypes.c_double,
                ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
            ]
            self._lib.pid_fixed_init.restype = None
            self._lib.pid_fixed_reset.argtypes = [ctypes.POINTER(_PidFixedCStruct)]
            self._lib.pid_fixed_reset.restype = None
            self._lib.pid_fixed_step.argtypes = [
                ctypes.POINTER(_PidFixedCStruct), ctypes.c_int32, ctypes.c_int32,
            ]
            self._lib.pid_fixed_step.restype = ctypes.c_int32
            self._lib.pid_double_to_fixed.argtypes = [ctypes.c_double]
            self._lib.pid_double_to_fixed.restype = ctypes.c_int32
            self._lib.pid_fixed_to_double.argtypes = [ctypes.c_int32]
            self._lib.pid_fixed_to_double.restype = ctypes.c_double

            self._lib.pid_fixed_init(
                ctypes.byref(self._struct), self.Kp, self.Ki, self.Kd,
                self.Ts, self.u_max, self.tau_f, self.Kaw,
            )
        else:
            self._struct = _PidCStruct()
            self._lib.pid_init.argtypes = [
                ctypes.POINTER(_PidCStruct),
                ctypes.c_double, ctypes.c_double, ctypes.c_double,
                ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
            ]
            self._lib.pid_init.restype = None
            self._lib.pid_reset.argtypes = [ctypes.POINTER(_PidCStruct)]
            self._lib.pid_reset.restype = None
            self._lib.pid_step.argtypes = [
                ctypes.POINTER(_PidCStruct), ctypes.c_double, ctypes.c_double,
            ]
            self._lib.pid_step.restype = ctypes.c_double

            self._lib.pid_init(
                ctypes.byref(self._struct), self.Kp, self.Ki, self.Kd,
                self.Ts, self.u_max, self.tau_f, self.Kaw,
            )

    def reset(self) -> None:
        """Zera o estado interno do controlador em C (REQ-SAFE-004)."""
        if self.fixed_point:
            self._lib.pid_fixed_reset(ctypes.byref(self._struct))
        else:
            self._lib.pid_reset(ctypes.byref(self._struct))

    def step(self, r: float, y: float) -> float:
        """Executa um passo do controlador em C e devolve u[k] em volts."""
        if self.fixed_point:
            r_fx = self._lib.pid_double_to_fixed(float(r))
            y_fx = self._lib.pid_double_to_fixed(float(y))
            u_fx = self._lib.pid_fixed_step(ctypes.byref(self._struct), r_fx, y_fx)
            return self._lib.pid_fixed_to_double(u_fx)
        return float(self._lib.pid_step(ctypes.byref(self._struct), float(r), float(y)))

    def __del__(self) -> None:
        # Libera explicitamente a referência à lib antes do TemporaryDirectory
        # ser removido, para não tentar apagar um .so ainda mapeado no Linux
        # (na prática o dlclose acontece no GC do ctypes; isto só evita
        # ResourceWarning em execuções muito rápidas de script).
        self._lib = None


@dataclass
class EquivalenceReport:
    """Resultado de `compare_model_vs_code`: erro amostra a amostra."""

    n_amostras: int
    erro_maximo_abs: float
    erro_medio_abs: float
    erro_rms: float
    amostra_pior_caso: int
    saidas_modelo: np.ndarray
    saidas_codigo: np.ndarray


def compare_model_vs_code(
    r_sequence,
    y_sequence,
    Kp: float,
    Ki: float,
    Kd: float = 0.0,
    Ts: float = 5.0e-3,
    u_max: float = 24.0,
    tau_f: float = 0.01,
    Kaw: float = 1.0,
    fixed_point: bool = False,
) -> EquivalenceReport:
    """Roda `DiscretePID` (modelo) e `SILController` (código C) sobre a
    mesma sequência (r[k], y[k]) e devolve o erro amostra a amostra.

    `r_sequence` e `y_sequence` devem ter o mesmo comprimento; em cada
    amostra k, ambos os controladores recebem exatamente (r[k], y[k]) —
    nenhum realimenta a saída do outro, para isolar o erro de codegen do
    erro de simulação de malha fechada.
    """
    r_arr = np.asarray(r_sequence, dtype=float)
    y_arr = np.asarray(y_sequence, dtype=float)
    if r_arr.shape != y_arr.shape:
        raise ValueError("r_sequence e y_sequence precisam do mesmo formato")

    modelo = DiscretePID(Kp=Kp, Ki=Ki, Kd=Kd, Ts=Ts, u_max=u_max, tau_f=tau_f, Kaw=Kaw)
    codigo = SILController(
        Kp=Kp, Ki=Ki, Kd=Kd, Ts=Ts, u_max=u_max, tau_f=tau_f, Kaw=Kaw,
        fixed_point=fixed_point,
    )

    n = len(r_arr)
    u_modelo = np.empty(n)
    u_codigo = np.empty(n)
    for k in range(n):
        u_modelo[k] = modelo.step(r_arr[k], y_arr[k])
        u_codigo[k] = codigo.step(r_arr[k], y_arr[k])

    erro = np.abs(u_modelo - u_codigo)
    pior = int(np.argmax(erro))

    return EquivalenceReport(
        n_amostras=n,
        erro_maximo_abs=float(erro[pior]),
        erro_medio_abs=float(np.mean(erro)),
        erro_rms=float(np.sqrt(np.mean(erro**2))),
        amostra_pior_caso=pior,
        saidas_modelo=u_modelo,
        saidas_codigo=u_codigo,
    )
