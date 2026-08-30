#!/usr/bin/env bash
# Roda o NuSMV sobre nexabot/nusmv/supervisor.smv e imprime o resultado de
# cada propriedade LTL/CTL.
#
# Uso:
#   bash nexabot/nusmv/instalar_nusmv.sh   # uma vez
#   bash nexabot/nusmv/rodar_verificacao.sh
set -euo pipefail

DESTINO="${NUSMV_HOME:-$HOME/.local/opt/nusmv}"
RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
SMV="$RAIZ/nexabot/nusmv/supervisor.smv"

if [ ! -x "$DESTINO/bin/NuSMV" ]; then
    echo "NuSMV não encontrado em $DESTINO/bin/NuSMV."
    echo "Rode primeiro: bash nexabot/nusmv/instalar_nusmv.sh"
    exit 1
fi

echo "Verificando $SMV com NuSMV..."
echo
LD_LIBRARY_PATH="$DESTINO/fakelib:${LD_LIBRARY_PATH:-}" "$DESTINO/bin/NuSMV" "$SMV"
