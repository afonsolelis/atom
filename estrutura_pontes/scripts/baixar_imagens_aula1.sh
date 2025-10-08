#!/usr/bin/env bash
set -euo pipefail

# Baixa imagens de referência da Aula 1 via API do Wikipedia (REST summary)
# Saída: arquivos em ./imagens/aula1_*.{jpg,png,webp}

mkdir -p imagens

UA="Mozilla/5.0 (compatible; AulaPontesBot/1.0; +https://example.edu)"

pages=(
  "Pont_du_Gard"
  "The_Iron_Bridge"
  "Millau_Viaduct"
  "Brooklyn_Bridge"
  "Salginatobel_Bridge"
)

fetch_url() {
  local page="$1"
  curl -sL -H "User-Agent: $UA" "https://en.wikipedia.org/api/rest_v1/page/summary/${page}" \
    | python3 - << 'PY'
import sys, json
try:
    d = json.load(sys.stdin)
except Exception:
    print("")
    raise SystemExit(0)
print(d.get("originalimage",{}).get("source") or d.get("thumbnail",{}).get("source",""))
PY
}

for page in "${pages[@]}"; do
  url="$(fetch_url "$page")"
  name="$(echo "$page" | tr 'A-Z' 'a-z' | tr -cs 'a-z0-9' '_')"
  if [[ -n "$url" ]]; then
    ext="${url##*.}"
    case "$ext" in
      jpg|jpeg|png|gif|webp) : ;;
      *) ext="jpg" ;;
    esac
    out="imagens/aula1_${name}.${ext}"
    echo "Baixando $page -> $out"
    curl -sL -H "User-Agent: $UA" "$url" -o "$out"
  else
    echo "Aviso: sem imagem para $page (verifique a URL/slug)." >&2
  fi
done

echo "Concluído. Arquivos em ./imagens:"
ls -1 imagens | sed 's/^/ - /'

