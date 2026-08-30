#!/usr/bin/env bash
# Instala o NuSMV localmente, no diretório do usuário, SEM privilégios de
# root — o NuSMV não é um pacote empacotado no apt/apt-get do Ubuntu/Debian
# (testado no ambiente desta disciplina: "E: Impossível encontrar o pacote
# nusmv"), então usamos o binário Linux 64-bit oficial, pré-compilado, do
# próprio site do projeto.
#
# Uso:
#   bash nexabot/nusmv/instalar_nusmv.sh
#
# Instala em $NUSMV_HOME (padrão: ~/.local/opt/nusmv). Depois de instalado,
# use nexabot/nusmv/rodar_verificacao.sh para verificar supervisor.smv.
set -euo pipefail

VERSAO="2.7.1"
DESTINO="${NUSMV_HOME:-$HOME/.local/opt/nusmv}"
URL="https://nusmv.fbk.eu/distrib/${VERSAO}/NuSMV-${VERSAO}-linux64.tar.xz"

if [ -x "$DESTINO/bin/NuSMV" ]; then
    echo "NuSMV já instalado em $DESTINO/bin/NuSMV — nada a fazer."
    exit 0
fi

echo "Baixando NuSMV ${VERSAO} (binário Linux 64-bit oficial) de:"
echo "  $URL"
mkdir -p "$DESTINO"
TMPFILE="$(mktemp --suffix=.tar.xz)"
trap 'rm -f "$TMPFILE"' EXIT
curl -fsSL -o "$TMPFILE" "$URL"
tar xf "$TMPFILE" -C "$DESTINO" --strip-components=1

# --- ABI de libedit: o binário oficial foi ligado contra libedit.so.0 -----
# Distribuições recentes (ex.: Ubuntu 24.04 "noble") só trazem libedit.so.2.
# A API usada pelo NuSMV (edição de linha simples do prompt interativo) é
# estável entre essas versões, então um symlink local resolve sem root e
# sem recompilar nada:
mkdir -p "$DESTINO/fakelib"
LIBEDIT_REAL="$(ldconfig -p 2>/dev/null | awk '/libedit\.so\.2( |$)/ {print $NF; exit}')"
if [ -z "$LIBEDIT_REAL" ]; then
    echo "AVISO: libedit.so.2 não encontrada por ldconfig. Se o NuSMV falhar"
    echo "com 'error while loading shared libraries: libedit.so.0', instale"
    echo "libedit2 (sem sudo: 'apt-get download libedit2 && dpkg-deb -x"
    echo "libedit2_*.deb /tmp/libedit_extraido' e aponte para a .so extraída)."
else
    ln -sf "$LIBEDIT_REAL" "$DESTINO/fakelib/libedit.so.0"
fi

echo
echo "NuSMV instalado em: $DESTINO/bin/NuSMV"
echo "Teste com: bash nexabot/nusmv/rodar_verificacao.sh"
