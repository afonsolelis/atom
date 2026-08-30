"""Gerador de código C do PID discreto do NexaBot a partir do modelo.

Lê os ganhos e parâmetros de uma instância de `nexabot.controllers.DiscretePID`
(o modelo de referência), obtém as equações de diferenças por derivação
simbólica (`nexabot.codegen.derive`, SymPy) e renderiza `pid_controller.c` /
`pid_controller.h` pelos templates Jinja2 em `templates/`.

O arquivo gerado carrega, no topo, um bloco de RASTREABILIDADE: requisito de
origem, versão do modelo, hash SHA-256 dos parâmetros e data de geração — de
forma que qualquer C encontrado em produção possa ser ligado de volta ao
modelo e ao commit que o gerou.

Uso típico:

    >>> from nexabot.controllers import DiscretePID
    >>> from nexabot.codegen.generate import generate_pid_controller
    >>> pid = DiscretePID(Kp=2.0, Ki=40.0, Kd=0.02)
    >>> result = generate_pid_controller(pid)
    >>> result.header_path.name
    'pid_controller.h'
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import jinja2

from .. import __version__ as MODEL_PACKAGE_VERSION
from ..controllers import DiscretePID
from . import derive

TEMPLATE_DIR = Path(__file__).parent / "templates"
DEFAULT_OUTPUT_DIR = Path(__file__).parent / "generated"

# Requisitos de origem deste gerador (ver docstrings de nexabot/controllers.py
# e nexabot/params.py — REQ-CTRL-* é a fonte da verdade, este módulo só a lê).
REQUISITOS_ORIGEM = (
    "REQ-CTRL-001",  # rastreamento de velocidade
    "REQ-CTRL-002",  # saturação do atuador
    "REQ-CTRL-003",  # anti-windup
    "REQ-CODEGEN-001",  # equivalência numérica código gerado x modelo
    "REQ-CODEGEN-002",  # rastreabilidade automática no cabeçalho gerado
)

FIXED_SHIFT_DEFAULT = 16  # Q16.16

_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(str(TEMPLATE_DIR)),
    trim_blocks=True,
    lstrip_blocks=True,
    keep_trailing_newline=True,
)


@dataclass(frozen=True)
class GeneratedFiles:
    """Resultado de uma geração: caminhos e metadados de rastreabilidade."""

    header_path: Path
    source_path: Path
    params_hash: str
    generated_at_iso: str
    gains: dict
    equations: dict[str, str]


def _pid_gains(pid: DiscretePID) -> dict:
    """Extrai do `DiscretePID` só os campos que definem o comportamento
    numérico (não o estado interno, que é sempre zerado na geração)."""
    return {
        "Kp": pid.Kp,
        "Ki": pid.Ki,
        "Kd": pid.Kd,
        "Ts": pid.Ts,
        "u_max": pid.u_max,
        "tau_f": pid.tau_f,
        "Kaw": pid.Kaw,
    }


def compute_params_hash(gains: dict) -> str:
    """Hash SHA-256 determinístico dos parâmetros (chaves ordenadas, repr
    de ponto flutuante completo via `repr`, para não perder precisão)."""
    payload = json.dumps(
        {k: repr(float(v)) for k, v in sorted(gains.items())},
        ensure_ascii=False,
    )
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _traceability_block(
    gains: dict,
    params_hash: str,
    generated_at_iso: str,
    equations: dict[str, str],
    requisitos=REQUISITOS_ORIGEM,
) -> str:
    gains_line = ", ".join(f"{k}={v!r}" for k, v in gains.items())
    lines = [
        "/* " + "=" * 76,
        " * ARQUIVO GERADO AUTOMATICAMENTE — NÃO EDITAR MANUALMENTE",
        " *",
        " * Qualquer edição manual será perdida na próxima geração e quebra a",
        " * cadeia de rastreabilidade requisito -> modelo -> código -> teste",
        " * (ver nexabot/rastreabilidade.py e rastreabilidade.md).",
        " *",
        f" * Requisitos de origem   : {', '.join(requisitos)}",
        " * Modelo de referência   : nexabot.controllers.DiscretePID"
        f" (pacote nexabot v{MODEL_PACKAGE_VERSION})",
        " * Gerador                : nexabot/codegen/generate.py"
        " + templates Jinja2 (pid_controller.c.h.j2)",
        f" * Parâmetros do modelo   : {gains_line}",
        f" * Hash SHA-256 (params)  : {params_hash}",
        f" * Gerado em (UTC)        : {generated_at_iso}",
        " *",
        " * Equações derivadas simbolicamente por SymPy a partir da forma",
        " * contínua do PID (Kp + Ki/s + Kd.s/(1+tau_f.s)), via discretização",
        " * de Euler para trás (ver nexabot/codegen/derive.py):",
        f" *   {equations['integral']}",
        f" *   {equations['derivada']}",
        " " + "=" * 77 + " */",
    ]
    return "\n".join(lines)


def generate_pid_controller(
    pid: DiscretePID,
    output_dir: Path | str = DEFAULT_OUTPUT_DIR,
    fixed_shift: int = FIXED_SHIFT_DEFAULT,
    header_name: str = "pid_controller.h",
    source_name: str = "pid_controller.c",
) -> GeneratedFiles:
    """Renderiza `pid_controller.h`/`.c` a partir dos ganhos de `pid`.

    Os ganhos e parâmetros vêm diretamente da instância de `DiscretePID`
    (o modelo); as equações de diferenças vêm de `derive.derive_all()`
    (SymPy). Nada nesse caminho é digitado manualmente em C.
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    gains = _pid_gains(pid)
    params_hash = compute_params_hash(gains)
    generated_at_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    recorrencias = derive.derive_all()
    equations = {k: v.equacao_str for k, v in recorrencias.items()}

    traceability = _traceability_block(gains, params_hash, generated_at_iso, equations)
    header_guard = f"{header_name.upper().replace('.', '_')}_"

    header_template = _env.get_template("pid_controller.h.j2")
    source_template = _env.get_template("pid_controller.c.j2")

    ctx = {
        "traceability_block": traceability,
        "header_guard": header_guard,
        "header_name": header_name,
        "fixed_shift": fixed_shift,
    }

    header_text = header_template.render(**ctx)
    source_text = source_template.render(**ctx)

    header_path = output_dir / header_name
    source_path = output_dir / source_name
    header_path.write_text(header_text, encoding="utf-8")
    source_path.write_text(source_text, encoding="utf-8")

    return GeneratedFiles(
        header_path=header_path,
        source_path=source_path,
        params_hash=params_hash,
        generated_at_iso=generated_at_iso,
        gains=gains,
        equations=equations,
    )


if __name__ == "__main__":
    # Execução direta: gera com os ganhos de exemplo e imprime o resultado.
    pid_exemplo = DiscretePID(Kp=2.0, Ki=40.0, Kd=0.02)
    resultado = generate_pid_controller(pid_exemplo)
    print(f"Gerado: {resultado.header_path}")
    print(f"Gerado: {resultado.source_path}")
    print(f"Hash dos parâmetros: {resultado.params_hash}")
