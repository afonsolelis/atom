#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera os entregáveis em .docx da disciplina a partir do Markdown, preenchendo
os templates ORIGINAIS da pasta da disciplina no Google Drive (baixados sem
alteração para tools/_templates_pristine/).

Fidelidade ao template:
  - as tabelas do(a) coordenador(a), a caixa "Plano de Ensino" e os campos de
    validação são mantidos intactos;
  - cada conteúdo entra na caixa correspondente do template (texto base,
    roteiro, quiz, material complementar, título/desafio/fonte/entregável/
    solução do PBL);
  - os textos de orientação (dentro e fora das caixas) e os exemplos são
    removidos, como o próprio template manda;
  - formatação: Times New Roman 12, espaçamento 1,15, alinhamento à esquerda,
    sem recuo (orientação do template);
  - fórmulas LaTeX entram como imagem (MathJax -> PNG); imagens entram
    embutidas, com texto alternativo e indicação entre colchetes + link.

Uso (a partir da pasta da disciplina):
    python3 tools/gerar_docx.py              # tudo
    python3 tools/gerar_docx.py unidades     # só os 4 templates de unidade
    python3 tools/gerar_docx.py questoes     # só as Questões UNI1–4
    python3 tools/gerar_docx.py avaliacao    # só a avaliação final
    python3 tools/gerar_docx.py trabalho     # só a entrega de trabalho

Requisitos: python-docx, Pillow, cairosvg; Node com `npm install` em tools/
(mathjax-full) para as fórmulas.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))

from docx import Document  # noqa: E402
from docx.oxml.ns import qn  # noqa: E402

import docx_comum as dc  # noqa: E402

DISC = TOOLS.parent
PRISTINE = TOOLS / "_templates_pristine"
SAIDA = DISC / "entrega_docx"
NOME = dc.DISCIPLINA


def stats_novo(base_dir):
    s = dc.new_stats()
    s["base_dir"] = str(base_dir)
    return s


def formula_index(md):
    return dc.build_formula_index(md)


def abrir(template_nome):
    return Document(PRISTINE / template_nome)


def salvar(doc, nome):
    SAIDA.mkdir(parents=True, exist_ok=True)
    destino = SAIDA / nome
    dc.unlock_rows_and_breaks(doc)
    doc.save(destino)
    return destino


def preencher_xxxx(doc):
    """'Nome da disciplina: XXXX' / 'Conteudista: XXXX'."""
    for p in doc.paragraphs:
        low = p.text.strip().lower()
        if "xxxx" not in low:
            continue
        valor = NOME if low.startswith("nome da disciplina") else dc.CONTEUDISTA
        feito = False
        for r in p.runs:
            if "XXXX" in r.text:
                r.text = r.text.replace("XXXX", "" if feito else valor)
                feito = True


def substituir_texto_celula(cell, texto):
    """Troca o texto de uma célula de cabeçalho preservando a formatação do
    primeiro run (cor, negrito, fonte do template)."""
    ps = cell.paragraphs
    runs = [r for p in ps for r in p.runs]
    if not runs:
        ps[0].add_run(texto)
        return
    runs[0].text = texto
    for r in runs[1:]:
        r.text = ""


def remover_caixa_inteira(t):
    """Remove a tabela e, se ela estiver sozinha num content control (w:sdt),
    remove o sdt inteiro."""
    el = t._tbl
    pai = el.getparent()
    if pai is not None and pai.tag == qn("w:sdtContent"):
        sdt = pai.getparent()
        if len([c for c in pai if c.tag == qn("w:tbl")]) == 1:
            sdt.getparent().remove(sdt)
            return
    pai.remove(el)


def remover_orientacoes_corpo(doc, manter_prefixos):
    """Remove parágrafos de nível de corpo (fora das caixas) que não sejam
    títulos (Heading) nem os campos de identificação do template."""
    removidos = 0
    for p in list(doc.paragraphs):
        txt = p.text.strip()
        if not txt:
            continue
        estilo = (p.style.name if p.style else "").lower()
        if estilo.startswith("heading") or estilo.startswith("título"):
            continue
        if txt.lower().startswith(manter_prefixos):
            continue
        p._p.getparent().remove(p._p)
        removidos += 1
    return removidos


def secoes_h3(linhas):
    out, tit, buf = [], None, []
    for ln in linhas:
        if re.match(r"^###\s+", ln):
            out.append((tit, buf))
            tit, buf = ln[3:].strip(), []
        else:
            buf.append(ln)
    out.append((tit, buf))
    return out


# =================================================================== unidades
RE_TEXTO = re.compile(r"^Aula (\d+) — (?!Roteiro)(.+)$")
RE_ROTEIRO = re.compile(r'^Aula (\d+) — Roteiro da Videoaula \d+: "?(.+?)"?$')

ROW2_CAMPOS = ("nome do livro", "capítulo", "link de acesso", "link:", "links:",
               "qual aula")


def _campo(linha):
    m = re.match(r"^\s*-\s+\*\*(.+?)\*\*", linha)
    return m.group(1).strip().lower() if m else None


def dividir_material(linhas):
    """Separa uma subseção do material complementar nas linhas do template:
    [0] texto provocativo (+ NOME DO PODCAST / NOME DO EPISÓDIO);
    [1] campos de link / livro / 'Qual aula';
    [2] referência ABNT (só no artigo)."""
    r1, r2, r3 = [], [], []
    alvo = r1
    for ln in linhas:
        c = _campo(ln)
        if c is not None:
            if c.startswith("referência"):
                alvo = r3
            elif c.startswith(ROW2_CAMPOS):
                alvo = r2
            else:
                alvo = r1
        alvo.append(ln)
    return r1, r2, r3


def fill_unidade(u):
    md_path = DISC / f"unidade_{u}/unidade_{u}.md"
    md = md_path.read_text(encoding="utf-8")
    doc = abrir(f"TEMPLATE - Unidade {u}_nome da disciplina.docx")
    fi = formula_index(md)
    st = stats_novo(md_path.parent)
    preencher_xxxx(doc)
    feitos = []

    for titulo, corpo in dc.parse_h2(md):
        if titulo.lower().startswith("vídeo introdutório"):
            t = dc.find_table(doc, "relação da disciplina")
            dc.render_blocks(t.rows[1].cells[0], corpo, fi, st, first=True)
            feitos.append("intro")
            continue
        m = RE_ROTEIRO.match(titulo)
        if m:
            n, nome_video = int(m.group(1)), m.group(2).strip()
            t = dc.find_table(doc, r"roteiro videoaula\s*0*%d(?!\d)" % n, regex=True)
            substituir_texto_celula(t.rows[0].cells[0], f"ROTEIRO VIDEOAULA {n}: {nome_video}")
            dc.render_blocks(t.rows[1].cells[0], corpo, fi, st, first=True)
            feitos.append(f"roteiro{n}")
            continue
        m = RE_TEXTO.match(titulo)
        if m:
            n = int(m.group(1))
            t = dc.find_table(doc, r"texto base aula\s*0*%d(?!\d)" % n, regex=True)
            dc.render_blocks(t.rows[1].cells[0], [f"### Aula {n} — {m.group(2)}", ""] + corpo,
                             fi, st, first=True)
            feitos.append(f"texto{n}")
            continue
        tl = titulo.lower()
        if tl.startswith("quiz"):
            t = dc.find_table(doc, "quiz")
            perg, resp = [], []
            for sub, linhas in secoes_h3(corpo):
                if not sub:
                    continue
                q, a, em_resp = [], [], False
                for ln in linhas:
                    if re.match(r"^\*\*(Resposta correta|Feedback)", ln.strip()):
                        em_resp = True
                    (a if em_resp else q).append(ln)
                perg += [f"### {sub}", ""] + q
                resp += [f"### {sub}", ""] + a
            dc.render_blocks(t.rows[1].cells[0], perg, fi, st, first=True)
            dc.render_blocks(t.rows[2].cells[0], resp, fi, st, first=True)
            feitos.append("quiz")
            continue
        if tl.startswith("material complementar"):
            alvos = {"direto da fonte": "direto da fonte", "para mergulhar": "para mergulhar",
                     "podcast": "podcast", "artigo científico": "artigo científico"}
            for sub, linhas in secoes_h3(corpo):
                if not sub:
                    continue
                chave = next((k for k in alvos if sub.lower().startswith(k)), None)
                if not chave:
                    continue
                t = dc.find_table(doc, alvos[chave])
                partes = dividir_material(linhas)
                for ri, parte in enumerate(partes, start=1):
                    if ri < len(t.rows):
                        dc.render_blocks(t.rows[ri].cells[0], parte, fi, st, first=True)
                feitos.append(chave)
            continue

    # Unidades 2–4: o template não traz a caixa de vídeo introdutório; a
    # tabela "Texto Dialógico × Acadêmico" fica solta (orientação) — sai.
    tdial = dc.find_table(doc, "texto dialógico")
    if tdial is not None:
        remover_caixa_inteira(tdial)
    removidos = remover_orientacoes_corpo(
        doc, ("template de produção", "nome da disciplina", "conteudista", "template átomo"))
    destino = salvar(doc, f"TEMPLATE - Unidade {u}_{NOME}.docx")
    return destino, feitos, removidos, st


# =================================================================== questões
def linhas_questoes(md, a_partir_de):
    """Converte o Markdown das questões para o fluxo do template:
    '### Questão N (tipo)' -> 'N.'; '### N. Feedback' fica; títulos '## '
    de seção são dispensados, exceto 'Feedbacks'."""
    linhas = md.split("\n")
    ini = next(i for i, l in enumerate(linhas) if re.match(a_partir_de, l))
    out = []
    for ln in linhas[ini:]:
        m = re.match(r"^### Questão (\d+)", ln)
        if m:
            out.append(f"### {m.group(1)}.")
            continue
        if re.match(r"^## Feedbacks", ln):
            out += ["---", "### FEEDBACKS"]
            continue
        if re.match(r"^## ", ln):
            continue
        out.append(ln)
    return out


def fill_linear(template_nome, md_path, saida_nome):
    md = md_path.read_text(encoding="utf-8")
    doc = abrir(template_nome)
    fi = formula_index(md)
    st = stats_novo(md_path.parent)
    dc.set_placeholder(doc, ("disciplina:",), NOME)
    dc.set_placeholder(doc, ("professor-conteudista:",), dc.CONTEUDISTA)
    removidos = dc.cut_body_after(doc, lambda t: t.lower().startswith("professor-conteudista"),
                                  keep_matched=True)
    dc.render_blocks(doc, linhas_questoes(md, r"^## Questões"), fi, st, alts=True)
    return salvar(doc, saida_nome), removidos, st


def fill_questoes():
    out = []
    for u in range(1, 5):
        out.append(fill_linear(f"Questões - UNI{u}_nomedadisciplina.docx",
                               DISC / f"unidade_{u}/questoes_uni{u}.md",
                               f"Questões - UNI{u}_{NOME}.docx"))
    return out


def fill_avaliacao():
    nome_t = "Avaliação final_(30 questões múltipla escolha + 10 discursivas)_nomedadisciplina.docx"
    return fill_linear(nome_t, DISC / "instrumentos_avaliativos/avaliacao_final.md",
                       nome_t.replace("nomedadisciplina", NOME))


# =================================================================== trabalho (PBL)
def fill_trabalho():
    md_path = DISC / "instrumentos_avaliativos/entrega_trabalho.md"
    md = md_path.read_text(encoding="utf-8")
    doc = abrir("TEMPLATE ENTREGA DE TRABALHO - nomedadisciplina.docx")
    fi = formula_index(md)
    st = stats_novo(md_path.parent)
    mapa = [("título", "título"), ("desafio", "desafio"), ("fonte de pesquisa", "fonte de pesquisa"),
            ("5. entregável", "entregável"), ("6. solução", "solução")]
    feitos = []
    for titulo, corpo in dc.parse_h2(md):
        tl = titulo.lower()
        for chave, needle in mapa:
            if tl.startswith(chave):
                t = dc.find_table(doc, needle)
                dc.render_blocks(t.rows[1].cells[0], corpo, fi, st, first=True)
                feitos.append(chave)
                break
    removidos = dc.remove_paragraphs_with_prefix(
        doc, ("atenção:", "excluir as orientações", "todos os itens são obrigatórios",
              "a resposta esperada deverá"))
    destino = salvar(doc, f"TEMPLATE ENTREGA DE TRABALHO - {NOME}.docx")
    return destino, feitos, removidos, st


# =================================================================== main
def resumo(st):
    faltas = st["faltantes"]
    return (f"fórmulas {dc.stats_total_imagens(st)} ok / {len(faltas)} como texto; "
            f"imagens {st.get('imagens', 0)} ok / {len(st.get('imagens_falha', []))} falha")


def main():
    alvo = sys.argv[1] if len(sys.argv) > 1 else "tudo"
    if alvo in ("tudo", "unidades"):
        for u in range(1, 5):
            d, feitos, rem, st = fill_unidade(u)
            print(f"[U{u}] {d.name}\n      caixas: {', '.join(feitos)}\n"
                  f"      orientações removidas: {rem}; {resumo(st)}")
            for f in st.get("imagens_falha", []):
                print("      ! imagem:", f)
            for f in st["faltantes"]:
                print("      ! fórmula como texto:", f[:80])
    if alvo in ("tudo", "questoes"):
        for d, rem, st in fill_questoes():
            print(f"[Q] {d.name} — orientação/exemplos removidos: {rem}; {resumo(st)}")
    if alvo in ("tudo", "avaliacao"):
        d, rem, st = fill_avaliacao()
        print(f"[AF] {d.name} — orientação/exemplos removidos: {rem}; {resumo(st)}")
    if alvo in ("tudo", "trabalho"):
        d, feitos, rem, st = fill_trabalho()
        print(f"[PBL] {d.name} — caixas: {', '.join(feitos)}; avisos removidos: {rem}; {resumo(st)}")


if __name__ == "__main__":
    main()
