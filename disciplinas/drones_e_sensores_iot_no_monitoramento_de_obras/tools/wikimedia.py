"""Busca e verifica imagens do Wikimedia Commons para os decks e o texto.

Uso:
  python tools/wikimedia.py buscar "tower crane construction" [n]
  python tools/wikimedia.py info "File:Nome.jpg" ["File:Outro.jpg" ...]

`info` imprime, para cada arquivo, a URL de miniatura (1600 px), a URL
original, o autor e a licença — o que vai no atributo data-credito dos slides.
Só use nos slides/texto imagens que passaram por `info` (existem de fato).
"""
import json
import time
import re
import sys
import urllib.parse
import urllib.error
import urllib.request

API = "https://commons.wikimedia.org/w/api.php"
sys.stdout.reconfigure(encoding="utf-8")
UA = {"User-Agent": "Mozilla/5.0 (material didatico; atom-coursework/1.0)"}


def get(params):
    url = API + "?" + urllib.parse.urlencode({**params, "format": "json"})
    for tentativa in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code != 429:
                raise
            time.sleep(5 * (tentativa + 1))  # limite de taxa do Commons
    sys.exit("Commons recusou (429) depois de 6 tentativas; tente de novo em alguns minutos.")


def limpa(html):
    return re.sub(r"<[^>]+>", "", html or "").strip()


def buscar(q, n=20):
    d = get({"action": "query", "list": "search", "srsearch": q, "srnamespace": 6, "srlimit": n})
    for x in d["query"]["search"]:
        t = x["title"]
        if re.search(r"\.(jpe?g|png|webp)$", t, re.I):
            print(t)


def info(titulos):
    d = get({"action": "query", "titles": "|".join(titulos), "prop": "imageinfo",
             "iiprop": "url|extmetadata|size", "iiurlwidth": 1280})
    for p in d["query"]["pages"].values():
        if "imageinfo" not in p:
            print(f"!! NÃO EXISTE: {p['title']}")
            continue
        ii = p["imageinfo"][0]
        for k in ("url", "thumburl"):
            if ii.get(k):
                ii[k] = ii[k].split("?")[0]
        m = ii.get("extmetadata", {})
        autor = limpa(m.get("Artist", {}).get("value"))
        lic = limpa(m.get("LicenseShortName", {}).get("value"))
        print(f"{p['title']}\n  thumb: {ii.get('thumburl')}\n  orig:  {ii['url']} ({ii['width']}x{ii['height']})"
              f"\n  credito: {autor} / Wikimedia Commons ({lic})\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    if sys.argv[1] == "buscar":
        buscar(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 20)
    else:
        info(sys.argv[2:])
