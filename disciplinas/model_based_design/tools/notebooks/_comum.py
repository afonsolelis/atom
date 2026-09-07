"""Trechos compartilhados pelos dezesseis notebooks."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from nbkit import code, md  # noqa: F401,E402  (reexportado para os fontes)

# Toda primeira célula de código ajusta o caminho sozinha, para o notebook
# funcionar tanto aberto de `notebooks/` quanto de `projeto_nexabot/`.
#
# ATENÇÃO: toda célula de código é declarada como *raw string* (r"""...""").
# Sem o `r`, um `\n` dentro de um print viraria quebra de linha de verdade na
# hora do import e quebraria a string no notebook gerado.
ABERTURA_IMPORTS = r"""
import sys
from pathlib import Path

# Acha o pacote `nexabot` esteja o notebook aberto de onde estiver.
for candidato in [Path.cwd(), *Path.cwd().parents]:
    if (candidato / "projeto_nexabot" / "nexabot").is_dir():
        sys.path.insert(0, str(candidato / "projeto_nexabot"))
        break
    if (candidato / "nexabot" / "params.py").is_file():
        sys.path.insert(0, str(candidato))
        break
"""

RODAPE_ERRO = """
---

*Notebook da disciplina Model-Based Design for Cyber-Physical Systems ·
UniFECAF · Prof. Afonso Cesar Lelis Brandão. Os números vêm de
`projeto_nexabot/nexabot/params.py`, a fonte única de verdade da disciplina.*
"""
