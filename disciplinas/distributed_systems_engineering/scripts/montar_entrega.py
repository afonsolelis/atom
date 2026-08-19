#!/usr/bin/env python3
"""Monta o pacote completo de `entrega_final/` em um único comando.

O pacote espelha a árvore de pastas dos originais recebidos em `documentos/`:
uma pasta por unidade, com o material didático, o questionário, os slides e a
subpasta da ficha de validação, mais `Instrumentos Avaliativos/`.

Etapas:
    1. limpa a árvore gerada anteriormente;
    2. preenche os quatro modelos de unidade;
    3. preenche os quatro questionários, a avaliação final e o trabalho PBL;
    4. copia as quatro fichas de validação, sem alteração (elas só podem ser
       preenchidas depois da gravação);
    5. copia os 17 decks HTML e o script de tela cheia que eles carregam;
    6. escreve o `index.html` de navegação do pacote;
    7. valida os DOCX e grava `validacao_docx.json`;
    8. reescreve `MANIFESTO_SHA256.md`.

Uso:
    PYTHONPATH=/tmp/dse-docx-libs python3 scripts/montar_entrega.py
"""

from __future__ import annotations

import hashlib
import html
import shutil
import sys
from pathlib import Path
from urllib.parse import quote

sys.path.insert(0, str(Path(__file__).resolve().parent))

import preencher_docx  # noqa: E402
import preencher_instrumentos  # noqa: E402
import validar_entrega  # noqa: E402
from docx_comum import (  # noqa: E402
    DISCIPLINA,
    DOCUMENTOS,
    ENTREGA,
    FICHA_VALIDACAO,
    RAIZ,
    SUBPASTA_VALIDACAO,
    arquivo_ficha,
    pasta_slides,
    pasta_unidade,
)

DATA_DA_CONSOLIDACAO = "1º de agosto de 2026"

TITULO_UNIDADE = preencher_docx.TITULO_UNIDADE

TITULO_AULA = {
    0: "Apresentação da disciplina — mercado, percurso e fio condutor da NexaOrder",
    1: "Pensar distribuído: conceitos, propriedades e compromissos",
    2: "Comunicação entre processos: APIs, RPC e mensageria",
    3: "Concorrência, relógios e ordenação de eventos",
    4: "Modelos de falha e desenho para recuperação",
    5: "Replicação e modelos de consistência",
    6: "Particionamento, CAP e escalabilidade de dados",
    7: "Consenso, eleição de líder e Raft",
    8: "Transações distribuídas, sagas e idempotência",
    9: "Decomposição em serviços e limites de domínio",
    10: "Arquitetura orientada a eventos",
    11: "Contêineres, Kubernetes e reconciliação",
    12: "Segurança e comunicação confiável entre serviços",
    13: "Observabilidade e diagnóstico distribuído",
    14: "Resiliência, testes distribuídos e engenharia do caos",
    15: "Processamento distribuído, edge e serverless",
    16: "Projeto integrado e avaliação arquitetural",
}


def aulas_da_unidade(unidade: int) -> list[int]:
    numeros = list(range((unidade - 1) * 4 + 1, unidade * 4 + 1))
    return [0] + numeros if unidade == 1 else numeros


def limpar_arvore() -> None:
    """Remove só o que este script gera, preservando README e manifesto."""
    for unidade in (1, 2, 3, 4):
        shutil.rmtree(pasta_unidade(unidade), ignore_errors=True)
    shutil.rmtree(ENTREGA / "Instrumentos Avaliativos", ignore_errors=True)
    shutil.rmtree(ENTREGA / "assets", ignore_errors=True)
    shutil.rmtree(ENTREGA / "docx", ignore_errors=True)  # layout antigo
    (ENTREGA / "index.html").unlink(missing_ok=True)


def copiar_fichas() -> list[Path]:
    print("FICHAS DE VALIDAÇÃO DE VIDEOAULA (cópia sem alteração):")
    destinos = []
    for unidade in (1, 2, 3, 4):
        origem = (
            DOCUMENTOS
            / f"Unidade {unidade}"
            / SUBPASTA_VALIDACAO[unidade]
            / f"{FICHA_VALIDACAO[unidade]}.docx"
        )
        if not origem.exists():
            print(f"  ! não encontrada: {origem.name}")
            continue
        destino = arquivo_ficha(unidade)
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(origem, destino)
        destinos.append(destino)
        print(f"  OK -> {destino.relative_to(ENTREGA)}")
    return destinos


def copiar_slides() -> int:
    """Copia os decks HTML preservando os caminhos relativos que eles usam.

    Cada deck referencia `../../assets/fullscreen-button.js` e `../../index.html`.
    Como os arquivos passam de `unidade_N/slides/` para
    `entrega_final/Unidade N/SLIDES - …/`, a profundidade se mantém e basta que o
    pacote tenha o próprio `assets/` e o próprio `index.html` na raiz.
    """
    print("SLIDES (17 decks HTML):")
    destino_assets = ENTREGA / "assets"
    destino_assets.mkdir(parents=True, exist_ok=True)
    shutil.copy2(RAIZ / "assets" / "fullscreen-button.js", destino_assets)

    total = 0
    for unidade in (1, 2, 3, 4):
        origem = RAIZ / f"unidade_{unidade}" / "slides"
        destino = pasta_slides(unidade)
        destino.mkdir(parents=True, exist_ok=True)
        for numero in aulas_da_unidade(unidade):
            deck = origem / f"aula{numero}.html"
            if not deck.exists():
                print(f"  ! deck ausente: {deck}")
                continue
            shutil.copy2(deck, destino / deck.name)
            total += 1
        if (origem / "assets").is_dir():
            shutil.copytree(origem / "assets", destino / "assets", dirs_exist_ok=True)
        print(f"  OK -> {destino.relative_to(ENTREGA)}/ ({len(aulas_da_unidade(unidade))} decks)")
    return total


def escrever_index() -> Path:
    def cartao(unidade: int, numero: int) -> str:
        alvo = quote(
            f"{pasta_slides(unidade).name}/aula{numero}.html", safe="/+"
        )
        pasta = quote(pasta_unidade(unidade).name, safe="/+")
        rotulo = "Apresentação da disciplina" if numero == 0 else f"Aula {numero}"
        return (
            f'      <a href="{pasta}/{alvo}"><strong>{rotulo}</strong>'
            f"<span>{html.escape(TITULO_AULA[numero])}</span></a>"
        )

    secoes = [
        '    <section class="unit" aria-labelledby="intro">'
        '<h2 id="intro">Vídeo introdutório</h2><div class="grid">',
        cartao(1, 0),
        "    </div></section>",
    ]
    for unidade in (1, 2, 3, 4):
        secoes.append(
            f'    <section class="unit" aria-labelledby="u{unidade}">'
            f'<h2 id="u{unidade}">Unidade {unidade} — '
            f"{html.escape(TITULO_UNIDADE[unidade])}</h2><div class=\"grid\">"
        )
        secoes += [
            cartao(unidade, n) for n in aulas_da_unidade(unidade) if n != 0
        ]
        secoes.append("    </div></section>")

    conteudo = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{DISCIPLINA} — pacote de entrega</title>
  <style>
    :root {{ color-scheme: dark; font-family: Inter, Arial, sans-serif; }}
    * {{ box-sizing: border-box; }}
    body {{ margin: 0; min-height: 100vh; background: #001640; color: #fff; }}
    header {{ padding: 4rem max(5vw, 1.5rem) 2rem; background: linear-gradient(135deg, #002057, #1f44a8); }}
    header p {{ max-width: 70ch; color: #d9e8ff; }}
    main {{ padding: 2rem max(5vw, 1.5rem) 4rem; }}
    .unit {{ margin-bottom: 2rem; }}
    h1, h2 {{ margin-top: 0; }}
    h2 {{ color: #8dd17e; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(245px, 1fr)); gap: 1rem; }}
    a {{ display: block; min-height: 118px; padding: 1.25rem; border: 1px solid #2bbbe0; border-radius: 14px; color: #002057; background: #fff; text-decoration: none; }}
    a:hover, a:focus-visible {{ outline: 4px solid #f0ce29; outline-offset: 2px; transform: translateY(-2px); }}
    a strong {{ display: block; margin-bottom: .55rem; color: #1f44a8; }}
    a span {{ line-height: 1.4; }}
  </style>
</head>
<body>
  <header>
    <h1>{DISCIPLINA}</h1>
    <p>Pacote de entrega. Os DOCX ficam nas pastas <strong>Unidade 1</strong> a
    <strong>Unidade 4</strong> e em <strong>Instrumentos Avaliativos</strong>.
    Os cartões abaixo abrem os 17 decks; dentro de cada um, navegue com as setas
    do teclado, Page Up/Page Down ou os controles na tela.</p>
  </header>
  <main>
{chr(10).join(secoes)}
  </main>
</body>
</html>
"""
    destino = ENTREGA / "index.html"
    destino.write_text(conteudo, encoding="utf-8")
    print(f"  OK -> {destino.relative_to(ENTREGA)}")
    return destino


def escrever_manifesto(arquivos: list[Path]) -> Path:
    linhas = []
    for caminho in sorted(arquivos, key=lambda p: str(p)):
        digest = hashlib.sha256(caminho.read_bytes()).hexdigest()
        linhas.append(f"{digest}  {caminho.relative_to(RAIZ)}")

    destino = ENTREGA / "MANIFESTO_SHA256.md"
    conteudo = f"""# Manifesto SHA-256 do pacote final

Data da consolidação: {DATA_DA_CONSOLIDACAO}

Os hashes abaixo identificam os {len(arquivos)} arquivos que compõem o pacote
final: os 14 DOCX institucionais preenchidos e o relatório automatizado de
validação. Os 17 decks HTML e o `index.html` de navegação acompanham o pacote e
não entram no manifesto, por serem regenerados a partir das fontes do
repositório. Para conferir os hashes a partir da raiz do repositório, execute:

```bash
sed -n '/^```text$/,/^```$/p' entrega_final/MANIFESTO_SHA256.md \\
  | sed '1d;$d' | sha256sum --check --strict
```

```text
{chr(10).join(linhas)}
```
"""
    destino.write_text(conteudo, encoding="utf-8")
    print(f"  OK -> {destino.relative_to(RAIZ)} ({len(arquivos)} arquivos)")
    return destino


def main() -> int:
    print("=" * 66)
    print("LIMPEZA DA ÁRVORE ANTERIOR")
    limpar_arvore()

    print("=" * 66)
    gerados: list[Path] = []
    for unidade in (1, 2, 3, 4):
        print(f"Unidade {unidade}:")
        gerados.append(preencher_docx.preencher_unidade(unidade))

    print("=" * 66)
    gerados += preencher_instrumentos.fazer_questoes()
    gerados.append(preencher_instrumentos.fazer_avaliacao())
    gerados.append(preencher_instrumentos.fazer_entrega())

    print("=" * 66)
    gerados += copiar_fichas()

    print("=" * 66)
    decks = copiar_slides()

    print("=" * 66)
    print("NAVEGAÇÃO:")
    escrever_index()

    print("=" * 66)
    print("VALIDAÇÃO:")
    codigo = validar_entrega.main()

    print("=" * 66)
    print("MANIFESTO:")
    escrever_manifesto(gerados + [ENTREGA / "validacao_docx.json"])

    print("=" * 66)
    print(f"Pacote em {ENTREGA.relative_to(RAIZ)}: {len(gerados)} DOCX e {decks} decks.")
    return codigo


if __name__ == "__main__":
    raise SystemExit(main())
