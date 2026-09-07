#!/usr/bin/env bash
# run.sh — executor do laboratório NexaBot.
#
# Um único ponto de entrada para preparar o ambiente e rodar as aulas, para
# que gravar uma videoaula seja "./run.sh 2" e não uma sequência de cinco
# comandos com o caminho do interpretador na mão.
#
#   ./run.sh setup        cria .venv e instala o projeto (idempotente)
#   ./run.sh 2            roda os scripts da aula_02 em ordem, com pausa
#   ./run.sh 2 3          roda só o script 3 da aula_02
#   ./run.sh 2 --direto   roda a aula_02 inteira sem pausar entre scripts
#   ./run.sh todas        roda as 16 aulas em sequência, sem pausa
#   ./run.sh check        pytest + todos os scripts, com relatório final
#   ./run.sh testes       só a suíte pytest
#   ./run.sh lista        lista as aulas e seus scripts
#   ./run.sh python ...   atalho para .venv/bin/python
#
# Não use `set -e`: o roteiro precisa capturar o código de saída de cada
# script para montar o relatório em vez de morrer no primeiro erro.
set -uo pipefail

RAIZ="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$RAIZ/.venv/bin/python"

if [[ -t 1 ]]; then
    VERDE=$'\033[92m'; VERMELHO=$'\033[91m'; AMARELO=$'\033[93m'
    AZUL=$'\033[94m';  NEGRITO=$'\033[1m';   ZERA=$'\033[0m'
else
    VERDE=''; VERMELHO=''; AMARELO=''; AZUL=''; NEGRITO=''; ZERA=''
fi

erro()  { printf '%s\n' "${VERMELHO}${NEGRITO}erro:${ZERA} $*" >&2; }
aviso() { printf '%s\n' "${AMARELO}aviso:${ZERA} $*" >&2; }

uso() {
    cat <<'AJUDA'
run.sh — executor do laboratório NexaBot

  ./run.sh setup          cria .venv e instala o projeto (idempotente)
  ./run.sh 2              roda os scripts da aula_02 em ordem, com pausa
  ./run.sh 2 3            roda só o script 3 da aula_02
  ./run.sh 2 --direto     roda a aula_02 inteira sem pausar entre scripts
  ./run.sh todas          roda as 16 aulas em sequência, sem pausa
  ./run.sh check          pytest + todos os scripts, com relatório final
  ./run.sh testes         só a suíte pytest
  ./run.sh lista          lista as aulas e seus scripts
  ./run.sh python ...     atalho para .venv/bin/python

Flags:
  --direto, -y            não pausa entre os scripts
  --parar, -x             interrompe na primeira falha

A aula aceita 2, 02, aula2 ou aula_02.
AJUDA
}

# ---------------------------------------------------------------- ambiente

# Procura o uv no PATH e nos lugares onde o instalador oficial o deixa.
acha_uv() {
    if [[ -n "${UV:-}" && -x "${UV}" ]]; then printf '%s' "$UV"; return 0; fi
    local c
    for c in "$(command -v uv 2>/dev/null || true)" \
             "$HOME/.local/bin/uv" "$HOME/.cargo/bin/uv" "/tmp/contrato-uv/uv"; do
        [[ -n "$c" && -x "$c" ]] && { printf '%s' "$c"; return 0; }
    done
    return 1
}

setup() {
    local uv
    if ! uv="$(acha_uv)"; then
        erro "uv não encontrado. Instale com:"
        printf '  curl -LsSf https://astral.sh/uv/install.sh | sh\n' >&2
        return 1
    fi
    printf '%s\n' "${AZUL}${NEGRITO}==> Preparando o ambiente${ZERA} (uv: $uv)"
    [[ -d "$RAIZ/.venv" ]] || "$uv" venv --python 3.12 "$RAIZ/.venv" || return 1
    # -e . instala o próprio nexabot em modo editável: os scripts passam a
    # importar `nexabot` de qualquer diretório, sem depender do cwd.
    "$uv" pip install --python "$PY" -e "$RAIZ" || return 1
    printf '%s\n\n' "${VERDE}${NEGRITO}Ambiente pronto.${ZERA}"
    "$PY" "$RAIZ/aula_01/01_ambiente.py"
}

exige_ambiente() {
    if [[ ! -x "$PY" ]]; then
        erro "ambiente não encontrado em .venv — rode primeiro: ./run.sh setup"
        exit 1
    fi
    if ! "$PY" -c 'import nexabot' 2>/dev/null; then
        erro "o pacote nexabot não está importável — rode: ./run.sh setup"
        exit 1
    fi
}

# ------------------------------------------------------------------- aulas

# Aceita 2, 02, aula_02 e aula2; devolve sempre o nome do diretório.
resolve_aula() {
    local bruto="$1" n
    n="${bruto#aula_}"; n="${n#aula}"; n="${n#0}"
    if ! [[ "$n" =~ ^[0-9]+$ ]] || (( n < 1 || n > 16 )); then
        erro "aula inválida: '$bruto' (esperado 1..16)"
        return 1
    fi
    printf 'aula_%02d' "$n"
}

# Ecoa os scripts de uma aula na ordem numérica do nome do arquivo.
scripts_da_aula() {
    local aula="$1"
    find "$RAIZ/$aula" -maxdepth 1 -name '[0-9]*.py' -type f | sort
}

lista() {
    local aula f
    for aula in $(seq -f 'aula_%02g' 1 16); do
        [[ -d "$RAIZ/$aula" ]] || continue
        printf '%s\n' "${NEGRITO}${aula}${ZERA}"
        while read -r f; do
            printf '  %s\n' "$(basename "$f")"
        done < <(scripts_da_aula "$aula")
    done
}

# Roda um script e devolve o código de saída dele.
roda_script() {
    local f="$1" rotulo="$2"
    printf '\n%s\n' "${AZUL}${NEGRITO}────── ${rotulo} ──────${ZERA}"
    ( cd "$RAIZ" && "$PY" "$f" )
}

pausa() {
    # Só pausa em terminal interativo: em CI ou com saída redirecionada a
    # pausa travaria o processo para sempre.
    [[ -t 0 && -t 1 && "$PAUSAR" == "sim" ]] || return 0
    printf '\n%s' "${AMARELO}[Enter] próximo script · [q] sair: ${ZERA}"
    local tecla; read -r tecla
    [[ "$tecla" == "q" ]] && { printf '\n'; exit 0; }
    return 0
}

# Roda a aula inteira (ou um script). Alimenta RELATORIO e FALHAS.
roda_aula() {
    local aula="$1" so_este="${2:-}"
    local arquivos=() f rc primeiro=sim
    while read -r f; do arquivos+=("$f"); done < <(scripts_da_aula "$aula")

    if (( ${#arquivos[@]} == 0 )); then
        erro "nenhum script encontrado em $aula"
        return 1
    fi

    if [[ -n "$so_este" ]]; then
        local achado=""
        for f in "${arquivos[@]}"; do
            [[ "$(basename "$f")" == $(printf '%02d' "$so_este")_* ]] && achado="$f"
        done
        if [[ -z "$achado" ]]; then
            erro "script $so_este não existe em $aula (veja ./run.sh lista)"
            return 1
        fi
        arquivos=("$achado")
    fi

    local nome
    for f in "${arquivos[@]}"; do
        [[ "$primeiro" == "sim" ]] || pausa
        primeiro=nao
        nome="$(basename "$f" .py)"
        roda_script "$f" "$aula/$(basename "$f")"
        rc=$?
        RELATORIO+=("$(printf '%-8s %-30s %s' "$aula" "$nome" "$rc")")
        if (( rc != 0 )); then
            # Os *_desafio.py são esqueletos para o estudante completar e
            # alguns saem com código 1 enquanto o TODO não foi implementado
            # (ex.: aula_08/05_desafio). Isso é o enunciado funcionando, não
            # uma quebra do ambiente — por isso não entra em FALHAS.
            if [[ "$nome" == *_desafio ]]; then
                PENDENTES+=("$aula/$nome")
                printf '%s\n' "${AMARELO}~~ $aula/$nome: desafio sem implementação (esperado)${ZERA}"
            else
                FALHAS+=("$aula/$(basename "$f") (saída $rc)")
                printf '%s\n' "${VERMELHO}${NEGRITO}!! $aula/$(basename "$f") saiu com código $rc${ZERA}"
                [[ "$PARAR_NA_FALHA" == "sim" ]] && return "$rc"
            fi
        fi
    done
    return 0
}

imprime_relatorio() {
    printf '\n%s\n' "${NEGRITO}Relatório${ZERA}"
    local linha aula script rc
    for linha in "${RELATORIO[@]}"; do
        read -r aula script rc <<<"$linha"
        if [[ "$rc" == "0" ]]; then
            printf '  %s %-8s %s\n' "${VERDE}OK   ${ZERA}" "$aula" "$script"
        elif [[ "$script" == *_desafio ]]; then
            printf '  %s %-8s %s (a implementar)\n' "${AMARELO}PEND ${ZERA}" "$aula" "$script"
        else
            printf '  %s %-8s %s (saída %s)\n' "${VERMELHO}FALHA${ZERA}" "$aula" "$script" "$rc"
        fi
    done
    printf '\n'
    if (( ${#PENDENTES[@]} > 0 )); then
        printf '%s\n' "${AMARELO}${#PENDENTES[@]} desafio(s) sem implementação — esperado, é o exercício do estudante.${ZERA}"
    fi
    if (( ${#FALHAS[@]} == 0 )); then
        local ok=$(( ${#RELATORIO[@]} - ${#PENDENTES[@]} ))
        printf '%s\n' "${VERDE}${NEGRITO}Ambiente OK: $ok de ${#RELATORIO[@]} scripts rodaram sem erro.${ZERA}"
        return 0
    fi
    printf '%s\n' "${VERMELHO}${NEGRITO}${#FALHAS[@]} de ${#RELATORIO[@]} scripts falharam:${ZERA}"
    local x; for x in "${FALHAS[@]}"; do printf '  - %s\n' "$x"; done
    return 1
}

testes() { exige_ambiente; ( cd "$RAIZ" && "$PY" -m pytest -q "$@" ); }

# --------------------------------------------------------------------- cli

RELATORIO=(); FALHAS=(); PENDENTES=()
PAUSAR=sim
PARAR_NA_FALHA=nao

# Separa as flags dos argumentos posicionais.
POS=()
for arg in "$@"; do
    case "$arg" in
        --direto|--sem-pausa|-y) PAUSAR=nao ;;
        --parar|-x)              PARAR_NA_FALHA=sim ;;
        -h|--help)               uso; exit 0 ;;
        *)                       POS+=("$arg") ;;
    esac
done
set -- ${POS[@]+"${POS[@]}"}

comando="${1:-}"

case "$comando" in
    ''|-h|--help|ajuda)
        uso
        ;;
    setup|instalar)
        setup
        ;;
    testes|test|pytest)
        shift; testes "$@"
        ;;
    lista|list)
        lista
        ;;
    python|py)
        exige_ambiente; shift; ( cd "$RAIZ" && exec "$PY" "$@" )
        ;;
    check|conferir)
        # Modo não interativo: usado antes de gravar e espelhado no CI.
        exige_ambiente
        PAUSAR=nao
        printf '%s\n' "${AZUL}${NEGRITO}==> Suíte pytest${ZERA}"
        if testes; then
            printf '%s\n' "${VERDE}pytest OK${ZERA}"
        else
            FALHAS+=("pytest")
            printf '%s\n' "${VERMELHO}pytest FALHOU${ZERA}"
        fi
        for aula in $(seq -f 'aula_%02g' 1 16); do
            [[ -d "$RAIZ/$aula" ]] && roda_aula "$aula"
        done
        imprime_relatorio
        ;;
    todas|all)
        exige_ambiente
        PAUSAR=nao
        for aula in $(seq -f 'aula_%02g' 1 16); do
            [[ -d "$RAIZ/$aula" ]] && roda_aula "$aula"
        done
        imprime_relatorio
        ;;
    *)
        exige_ambiente
        aula="$(resolve_aula "$comando")" || exit 1
        roda_aula "$aula" "${2:-}"
        # Um script só: o próprio código de saída dele já é a resposta.
        if (( ${#RELATORIO[@]} > 1 )); then
            imprime_relatorio
        elif (( ${#FALHAS[@]} > 0 )); then
            exit 1
        fi
        ;;
esac
