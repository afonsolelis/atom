"""Gera os DOCX de entrega a partir dos modelos do Drive (documentos/) e do Markdown.

Uso:  python scripts/gerar_docx.py            (gera tudo em entregas_docx/)

Cada DOCX parte de uma cópia do modelo original: mantém cabeçalho, logo, a tabela da
coordenação, a caixa de validação e o "Plano de Ensino"; remove as orientações e os
exemplos do template (inclusive as credenciais da Biblioteca Virtual) e escreve o
conteúdo do Markdown dentro das caixas. Os modelos em documentos/ não são alterados.
"""
from __future__ import annotations

import copy
import re
import sys
from pathlib import Path

import docx
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Cm

RAIZ = Path(__file__).resolve().parent.parent
DOC = RAIZ / "documentos"
SAIDA = RAIZ / "entregas_docx"
DISCIPLINA = "Red Team & Blue Team Strategies"
PROFESSOR = "Afonso Cesar Lelis Brandão"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
FONTE = "Times New Roman"


# ---------------------------------------------------------------- utilidades XML
def texto(el) -> str:
    return "".join(t.text or "" for t in el.iter(W + "t"))


def tag(el) -> str:
    return el.tag.split("}")[1]


def tabela_de(el):
    """Devolve o <w:tbl> de um elemento do corpo (tbl direto ou dentro de sdt)."""
    if tag(el) == "tbl":
        return el
    if tag(el) == "sdt":
        for t in el.iter(W + "tbl"):
            return t
    return None


def liberar_linha(tc):
    """Linha de conteúdo: pode quebrar entre páginas e não se repete como cabeçalho."""
    tr = tc.getparent()
    trPr = tr.find(W + "trPr")
    if trPr is not None:
        for c in list(trPr):
            if tag(c) in ("cantSplit", "tblHeader"):
                trPr.remove(c)


def limpar_celula(cell):
    """Remove todo o conteúdo da célula, deixando um parágrafo vazio."""
    tc = cell._tc
    liberar_linha(tc)
    for child in list(tc):
        if tag(child) != "tcPr":
            tc.remove(child)
    p = OxmlElement("w:p")
    tc.append(p)


def set_titulo_celula(cell, novo: str):
    """Troca o texto do cabeçalho da caixa preservando a formatação do 1º run."""
    paras = cell.paragraphs
    alvo = next((p for p in paras if p.text.strip()), paras[0])
    runs = alvo.runs
    if runs:
        runs[0].text = novo
        for r in runs[1:]:
            r.text = ""
    else:
        alvo.add_run(novo)
    for p in paras:
        if p is not alvo:
            p._p.getparent().remove(p._p)


def remover_linhas(tbl_el, a_partir: int):
    rows = tbl_el.findall(W + "tr")
    for r in rows[a_partir:]:
        tbl_el.remove(r)


def bordas_tabela(tbl):
    tblPr = tbl._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for lado in ("top", "left", "bottom", "right", "insideH", "insideV"):
        e = OxmlElement(f"w:{lado}")
        e.set(qn("w:val"), "single")
        e.set(qn("w:sz"), "4")
        e.set(qn("w:color"), "808080")
        b.append(e)
    tblPr.append(b)


def sombrear(cell, cor="D9E2F3"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), cor)
    tcPr.append(shd)


# ------------------------------------------------------------ Markdown -> DOCX
INLINE = re.compile(
    r"(\*\*\*(.+?)\*\*\*|\*\*(.+?)\*\*|(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])|`([^`]+)`"
    r"|!\[([^\]]*)\]\(([^)]+)\)|\[([^\]]+)\]\(([^)]+)\)|<(https?://[^>]+)>)"
)


def _fmt(run, tam=12, bold=None, italic=None, mono=False):
    run.font.name = "Consolas" if mono else FONTE
    rpr = run._r.get_or_add_rPr()
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.append(rf)
    nome = "Consolas" if mono else FONTE
    for a in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rf.set(qn(a), nome)
    run.font.size = Pt(tam - 1 if mono else tam)
    if bold is not None:
        run.bold = bold
    if italic is not None:
        run.italic = italic


def add_inline(par, s: str, tam=12, bold=False, italic=False):
    s = s.replace("\\*", "\x00").replace("\\_", "_").replace("\\|", "|").replace("\\#", "#")
    pos = 0
    for m in INLINE.finditer(s):
        if m.start() > pos:
            _fmt(par.add_run(s[pos:m.start()].replace("\x00", "*")), tam, bold, italic)
        g = m.groups()
        if g[1]:
            add_inline(par, g[1], tam, True, True)
        elif g[2]:
            add_inline(par, g[2], tam, True, italic)
        elif g[3]:
            add_inline(par, g[3], tam, bold, True)
        elif g[4]:
            _fmt(par.add_run(g[4]), tam, bold, italic, mono=True)
        elif g[6]:
            _fmt(par.add_run(f"[Imagem: {g[5]} — {g[6]}]"), tam, bold, True)
        elif g[7]:
            add_inline(par, g[7], tam, bold, italic)
            if g[8].strip() != g[7].strip():
                _fmt(par.add_run(f" ({g[8]})"), tam, bold, italic)
        elif g[9]:
            _fmt(par.add_run(g[9]), tam, bold, italic)
        pos = m.end()
    if pos < len(s):
        _fmt(par.add_run(s[pos:].replace("\x00", "*")), tam, bold, italic)


def fmt_par(par, recuo=0.0, antes=0, depois=6):
    pf = par.paragraph_format
    pf.alignment = WD_ALIGN_PARAGRAPH.LEFT
    pf.line_spacing = 1.15
    pf.space_before = Pt(antes)
    pf.space_after = Pt(depois)
    pf.first_line_indent = Cm(0)
    if recuo:
        pf.left_indent = Cm(recuo)


class Escritor:
    """Escreve blocos Markdown num contêiner (célula ou documento)."""

    def __init__(self, cont, alt_letras=False, estilo_titulo=None):
        self.cont = cont
        self.estilo_titulo = estilo_titulo
        self.alt_letras = alt_letras  # "a." -> "a)" nas alternativas das questões
        self.primeiro = True

    def par(self):
        if self.primeiro and hasattr(self.cont, "paragraphs") and self.cont.paragraphs and not self.cont.paragraphs[0].text:
            p = self.cont.paragraphs[0]
        else:
            p = self.cont.add_paragraph()
        self.primeiro = False
        return p

    def titulo(self, txt, nivel):
        p = self.par()
        if self.estilo_titulo and nivel <= 3:
            p.style = self.estilo_titulo
            fmt_par(p, antes=10, depois=4)
            add_inline(p, txt, 12, bold=True)
            return
        tam = {1: 14, 2: 13, 3: 12, 4: 12}.get(nivel, 12)
        fmt_par(p, antes=10 if nivel <= 3 else 6, depois=4)
        add_inline(p, txt, tam, bold=True)
        if nivel <= 2:
            for r in p.runs:
                r.font.color.rgb = RGBColor(0x00, 0x20, 0x57)

    def paragrafo(self, linhas, recuo=0.0, italic=False, mono=False):
        p = self.par()
        fmt_par(p, recuo=recuo, depois=2 if mono else 6)
        for i, ln in enumerate(linhas):
            if i:
                p.add_run().add_break()
            if mono:
                _fmt(p.add_run(ln), 12, mono=True)
            else:
                add_inline(p, ln.rstrip(), italic=italic)

    def tabela(self, linhas):
        cel = [[c.strip() for c in re.split(r"(?<!\\)\|", ln.strip().strip("|"))] for ln in linhas]
        cel = [r for r in cel if not all(re.fullmatch(r":?-{2,}:?", c) for c in r if c)]
        if not cel:
            return
        ncol = max(len(r) for r in cel)
        t = self.cont.add_table(rows=len(cel), cols=ncol)
        self.primeiro = False
        bordas_tabela(t)
        for i, r in enumerate(cel):
            for j in range(ncol):
                c = t.cell(i, j)
                p = c.paragraphs[0]
                fmt_par(p, depois=0)
                add_inline(p, r[j] if j < len(r) else "", 10, bold=(i == 0))
                if i == 0:
                    sombrear(c)
        self.cont.add_paragraph()  # respiro após a tabela

    def escrever(self, md: str):
        linhas = md.splitlines()
        i = 0
        buf: list[str] = []

        def flush():
            nonlocal buf
            if buf:
                self.paragrafo(buf)
                buf = []

        while i < len(linhas):
            ln = linhas[i]
            s = ln.strip()
            if not s or re.fullmatch(r"-{3,}|\*{3,}", s):
                flush(); i += 1; continue
            m = re.match(r"^(#{1,6})\s+(.*)", s)
            if m:
                flush(); self.titulo(m.group(2), len(m.group(1))); i += 1; continue
            if s.startswith("```"):
                flush(); i += 1; code = []
                while i < len(linhas) and not linhas[i].strip().startswith("```"):
                    code.append(linhas[i]); i += 1
                i += 1
                self.paragrafo(code or [""], recuo=0.5, mono=True)
                continue
            if s.startswith("|"):
                flush(); tab = []
                while i < len(linhas) and linhas[i].strip().startswith("|"):
                    tab.append(linhas[i]); i += 1
                self.tabela(tab); continue
            if s.startswith(">"):
                flush(); bloco = []
                while i < len(linhas) and linhas[i].strip().startswith(">"):
                    bloco.append(linhas[i].strip()[1:].strip()); i += 1
                # parágrafos dentro da citação
                atual: list[str] = []
                for b in bloco + [""]:
                    if b:
                        atual.append(b)
                    elif atual:
                        self.paragrafo(atual, recuo=0.75, italic=True); atual = []
                continue
            m = re.match(r"^(\s*)([-*+]|\d+[.)])\s+(.*)", ln)
            if m and not re.match(r"^\*[a-e][.)]", s):
                flush()
                ind = len(m.group(1).expandtabs(2)) // 2
                marcador = "•" if m.group(2) in "-*+" else m.group(2)
                item = [f"{marcador} {m.group(3)}"]
                i += 1
                while i < len(linhas) and linhas[i].strip() and not re.match(r"^\s*([-*+]|\d+[.)])\s+|^\s*[#|>]", linhas[i]) \
                        and linhas[i].startswith("  "):
                    item.append(linhas[i].strip()); i += 1
                self.paragrafo(item, recuo=0.6 + 0.6 * ind)
                continue
            # alternativas de questão (a. / *a. / a) )
            m = re.match(r"^(\*?)([a-e])[.)]\s+(.*)", s)
            if m:
                flush()
                letra = f"{m.group(1)}{m.group(2)}{')' if self.alt_letras else '.'}"
                p = self.par(); fmt_par(p, recuo=0.4, depois=2)
                add_inline(p, f"{letra} " if not m.group(1) else "", 12)
                if m.group(1):
                    _fmt(p.add_run(f"{letra} "), 12, bold=True)
                add_inline(p, m.group(3).rstrip())
                i += 1
                continue
            buf.append(ln.strip() if not ln.endswith("  ") else ln.rstrip())
            # quebra de linha explícita (dois espaços) mantém no mesmo parágrafo
            if not ln.endswith("  ") and (i + 1 >= len(linhas) or not linhas[i + 1].strip()):
                flush()
            i += 1
        flush()


def escrever_celula(cell, md: str, **kw):  # kw: alt_letras, estilo_titulo
    limpar_celula(cell)
    Escritor(cell, **kw).escrever(md)


def escrever_doc_apos(doc, ancora_el, md: str, **kw):
    """Escreve no fim do documento (antes do sectPr) e devolve nada."""
    Escritor(doc, **kw).escrever(md)


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace('"', "").replace("“", "").replace("”", "")).strip().lower()


def preencher_campos(tbl, linhas, estilo=None):
    """Mantém as linhas e os rótulos do modelo e escreve o conteúdo ao lado/abaixo de cada rótulo.

    linhas: {indice_da_linha: [(rotulo, valor_inline_md|None, bloco_md|None), ...]}
    Parágrafos do modelo que não são rótulos (orientações, exemplos, credenciais) saem.
    """
    rows = tbl.rows
    for ri, itens in linhas.items():
        cell = rows[ri].cells[0]
        originais = list(cell.paragraphs)
        liberar_linha(cell._tc)
        tc = cell._tc
        for child in list(tc):
            if tag(child) != "tcPr":
                tc.remove(child)
        for rotulo, inline, bloco in itens:
            base = next((p for p in originais if _norm(p.text).startswith(_norm(rotulo)[:25])), None)
            if base is not None:
                el = copy.deepcopy(base._p)
                tc.append(el)
                par = docx.text.paragraph.Paragraph(el, cell)
                # remove quebras/linhas extras do rótulo e mantém a formatação do 1º run
                for br in list(el.iter(W + "br")):
                    br.getparent().remove(br)
                set_titulo_par(par, rotulo)
            else:
                par = cell.add_paragraph()
                fmt_par(par, depois=2)
                _fmt(par.add_run(rotulo), 12, bold=True)
            if inline:
                add_inline(par, " " + inline, 12, bold=False)
            if bloco:
                e = Escritor(cell, estilo_titulo=estilo)
                e.primeiro = False
                e.escrever(bloco)
        if not list(tc.iter(W + "p")):
            tc.append(OxmlElement("w:p"))
    # linhas além das usadas saem
    remover_linhas(tbl._tbl, 1 + max(linhas))


def campos_md(md: str) -> dict:
    """Lê '- **Campo:** valor' do material complementar."""
    out = {}
    for m in re.finditer(r"(?m)^- \*\*([^*]+?):\*\*\s*(.*)$", md):
        out.setdefault(m.group(1).strip(), m.group(2).strip())
    return out


# --------------------------------------------------------------- Markdown util
def secoes(md: str, nivel: int):
    """Divide o markdown em [(título, corpo)] no nível de cabeçalho dado."""
    pat = re.compile(rf"(?m)^{'#' * nivel} (?!#)(.*)$")
    partes = []
    ms = list(pat.finditer(md))
    for k, m in enumerate(ms):
        fim = ms[k + 1].start() if k + 1 < len(ms) else len(md)
        partes.append((m.group(1).strip(), md[m.end():fim].strip("\n")))
    return partes


def sem_md(s: str) -> str:
    return re.sub(r"[*`]", "", s)


# ----------------------------------------------------------------- unidades
def gerar_unidade(u: int):
    modelo = DOC / f"Unidade {u}" / f"TEMPLATE - Unidade {u}_nome da disciplina.docx"
    d = docx.Document(modelo)
    md = (RAIZ / f"unidade_{u}" / f"unidade_{u}.md").read_text(encoding="utf-8")
    sec2 = dict(secoes(md, 2))
    aulas = [(t, c) for t, c in secoes(md, 2) if t.startswith("Aula ")]
    assert len(aulas) == 4, aulas
    n0 = (u - 1) * 4 + 1

    corpo = d.element.body
    elems = list(corpo.iterchildren())

    # cabeçalho
    for p in d.paragraphs[:8]:
        if p.text.strip().startswith("Nome da disciplina"):
            set_titulo_par(p, f"Nome da disciplina: {DISCIPLINA}")
        elif p.text.strip().startswith("Conteudista"):
            set_titulo_par(p, f"Conteudista: {PROFESSOR}")
    # o modelo da U2 veio com "Unidade 1" por dentro: corrige cabeçalho e plano de ensino
    for sec in d.sections:
        for hdr in (sec.header, sec.first_page_header, sec.even_page_header):
            for wt in hdr._element.iter(W + "t"):
                wt.text = re.sub(r"UNIDADE \d", f"UNIDADE {u}", wt.text or "")
    for el in elems:
        if tag(el) == "sdt" and "Plano de Ensino" in texto(el):
            for t in el.iter(W + "t"):
                t.text = re.sub(r"Unidade \d", f"Unidade {u}", t.text or "")

    caixas = []  # (elemento do corpo, tbl, título)
    remover = []
    inicio_orient = False
    for el in elems:
        tg, tx = tag(el), texto(el).strip()
        tbl = tabela_de(el)
        if tg == "p":
            if tx.startswith("Orientações para Produção de Material Escrito"):
                inicio_orient = True
                # no modelo o conteúdo começa na página 2: se ainda não houver quebra antes, o título das
                # orientações vira uma quebra de página; se houver, ele só sai
                ant = el.getprevious()
                ja_tem = ant is not None and any(b.get(qn("w:type")) == "page" for b in ant.iter(W + "br"))
                if ja_tem:
                    remover.append(el)
                    continue
                for ch in list(el):
                    if tag(ch) != "pPr":
                        el.remove(ch)
                r = OxmlElement("w:r"); br = OxmlElement("w:br"); br.set(qn("w:type"), "page"); r.append(br); el.append(r)
                continue
            if inicio_orient and tx and not re.match(r"^\s*(QUIZ NÃO AVALIATIVO|ATIVIDADE VERIFICADORA|MATERIAL COMPLEMENTAR)", tx):
                remover.append(el)
            continue
        if tbl is not None and inicio_orient:
            caixas.append((el, tbl, tx))

    def box(prefixo):
        for el, tbl, tx in caixas:
            if tx.upper().startswith(prefixo.upper()):
                return el, tbl
        raise KeyError(prefixo)

    usados = set()

    H3 = d.styles["Heading 3"]

    def caixa(prefixo, titulo):
        el, tbl_el = box(prefixo)
        usados.add(el)
        tbl = docx.table.Table(tbl_el, d._body)
        set_titulo_celula(tbl.rows[0].cells[0], titulo)
        return tbl

    def preencher(prefixo, titulo, linhas_md: list[str]):
        tbl = caixa(prefixo, titulo)
        remover_linhas(tbl._tbl, 1 + len(linhas_md))
        for k, conteudo in enumerate(linhas_md):
            escrever_celula(tbl.rows[1 + k].cells[0], conteudo, estilo_titulo=H3)

    # Unidade 1: relação com a atuação profissional + vídeo introdutório
    if u == 1:
        rel = sec2["Relação da disciplina com a atuação profissional"]
        vid_t = next(t for t in sec2 if t.startswith("Roteiro do vídeo introdutório"))
        preencher_campos(caixa("Relação da disciplina", "Relação da disciplina com atuação profissional + Roteiro do vídeo introdutório"), {
            1: [('"Por que essa disciplina é relevante para sua atuação profissional?"', None, rel),
                ("Vídeo Introdutório (Até 2 minutos)", None, sec2[vid_t])]}, H3)

    for k, (titulo, corpo_aula) in enumerate(aulas):
        n = n0 + k
        subs = secoes(corpo_aula, 3)
        rot = [(t, c) for t, c in subs if t.startswith("Roteiro da Videoaula")]
        texto_base = re.split(r"(?m)^### Roteiro da Videoaula.*$", corpo_aula)[0].strip()
        texto_base = re.sub(r"(?m)^### Texto base\s*$", "", texto_base)
        preencher(f"TEXTO BASE AULA {k + 1 if u == 2 else n}", f"TEXTO BASE AULA {n}",
                  [f"## {titulo}\n\n{texto_base}"])
        rt, rc = rot[0]
        nome_video = rt.split("—", 1)[1].strip() if "—" in rt else rt
        preencher(f"ROTEIRO VIDEOAULA {k + 1 if u == 2 else n}:", f"ROTEIRO VIDEOAULA {n}: {sem_md(nome_video)}", [rc])

    # Quiz: mesmas 2 linhas e rótulos do modelo
    quiz = sec2["Quiz não avaliativo"]
    qp = re.split(r"(?m)^### Feedback\s*$", quiz)
    preencher_campos(caixa("QUIZ", "QUIZ Não Avaliativo (Perguntas de verdadeiro ou falso e/ou múltipla escolha)"), {
        1: [("Com base no texto, elabore as perguntas:", None, qp[0].strip())],
        2: [("Resposta com explicação para o estudante ter um feedback caso acerte ou erre a questão:", None, qp[1].strip())]}, H3)

    aai = next((c for t, c in sec2.items() if t.startswith("AAI")), None)
    if aai:
        pa = re.split(r"(?m)^\*\*Resposta esperada:\*\*\s*$", aai)
        perg = re.sub(r"(?m)^\*\*Pergunta:\*\*\s*$", "", pa[0]).strip()
        preencher_campos(caixa("AAI", "AAI – Atividade avaliativa individual"), {
            1: [("Pergunta:", None, perg), ("Resposta esperada:", None, pa[1].strip())]}, H3)

    mat = dict(secoes(sec2["Material complementar"], 3))
    mk = lambda pref: campos_md(next(c for t, c in mat.items() if t.lower().startswith(pref)))
    QA = "Qual aula o material deverá entrar?"
    f = mk("direto da fonte")
    preencher_campos(caixa("DIRETO DA FONTE", "DIRETO DA FONTE (LIVRO DA BIBLIOTECA VIRTUAL)"), {
        1: [("Elabore um texto provocativo para leitura:", None, f["Texto provocativo"])],
        2: [("Nome do livro:", f["Nome do livro"], None), ("Capítulo:", f["Capítulo"], None),
            ("Link de acesso:", f["Link de acesso"], None), (QA, f["Aula em que entra"], None)]})
    f = mk("para mergulhar")
    links = "\n".join(f"- **{k}:** {v}" for k, v in f.items() if k.startswith(("Indicação", "Link")))
    preencher_campos(caixa("PARA MERGULHAR", "PARA MERGULHAR NO ASSUNTO (SAIBA MAIS)"), {
        1: [("Elabore um texto provocativo para explorar mais o conteúdo:", None, f["Texto provocativo"])],
        2: [("Links:", None, links), (QA, f["Aula em que entra"], None)]})
    f = mk("podcast")
    preencher_campos(caixa("PODCAST", "PODCAST (curadoria | até 45min)"), {
        1: [("Elabore um texto provocativo para estimular a escuta do podcast:", None, f["Texto provocativo"]),
            ("NOME DO PODCAST:", f["Nome do podcast"], None), ("NOME DO EPISÓDIO:", f["Nome do episódio"], None)],
        2: [("Link:", f["Link"], None), (QA, f["Aula em que entra"], None)]})
    f = mk("artigo")
    preencher_campos(caixa("ARTIGO CIENTÍFICO", "ARTIGO CIENTÍFICO"), {
        1: [("Elabore um texto provocativo para leitura do artigo científico:", None, f["Texto provocativo"])],
        2: [("Link:", f["Link"], None), (QA, f["Aula em que entra"], None)],
        3: [("Referência bibliográfica do artigo no formato ABNT:", None, f["Referência ABNT"])]})

    # caixas sem conteúdo nesta unidade (vídeo introdutório e AAI fora da U1) e o título solto delas
    for el, tbl, tx in caixas:
        if el not in usados:
            remover.append(el)
    if not aai:
        for el in elems:
            if tag(el) == "p" and texto(el).strip().startswith("ATIVIDADE VERIFICADORA"):
                remover.append(el)
    for el in remover:
        if el.getparent() is not None:
            el.getparent().remove(el)
    return d, f"Unidade {u}", f"TEMPLATE - Unidade {u}_{DISCIPLINA}.docx"


def set_titulo_par(p, novo):
    runs = p.runs
    if runs:
        runs[0].text = novo
        for r in runs[1:]:
            r.text = ""
    else:
        p.add_run(novo)


def limpar_vazios(d):
    """Remove sequências de parágrafos vazios (deixa no máximo um)."""
    anterior_vazio = False
    for el in list(d.element.body.iterchildren()):
        if tag(el) == "p" and not texto(el).strip() and not list(el.iter(W + "drawing")) and not list(el.iter(W + "sectPr")):
            if anterior_vazio:
                el.getparent().remove(el)
            anterior_vazio = True
        else:
            anterior_vazio = False


# ---------------------------------------------------- questões / avaliação final
def gerar_questionario(modelo: Path, md_path: Path, titulo_doc: str, nome: str, pasta: str, alt=True):
    d = docx.Document(modelo)
    md = md_path.read_text(encoding="utf-8")
    corpo = d.element.body
    elems = list(corpo.iterchildren())
    achou = False
    for el in elems:
        tx = texto(el).strip()
        if tag(el) == "p" and (tx.startswith("QUESTIONÁRIO") or tx.startswith("AVALIAÇÃO FINAL")):
            achou = True
        if not achou or tag(el) == "sectPr":
            continue
        if tag(el) == "p" and tx.startswith("Disciplina:"):
            set_titulo_par(docx.text.paragraph.Paragraph(el, d._body), f"Disciplina: {DISCIPLINA}")
            continue
        if tag(el) == "p" and tx.startswith("Professor-conteudista:"):
            set_titulo_par(docx.text.paragraph.Paragraph(el, d._body), f"Professor-conteudista: {PROFESSOR}")
            continue
        if tag(el) == "p" and (tx.startswith("QUESTIONÁRIO") or tx.startswith("AVALIAÇÃO FINAL") or tx.startswith("Questões autorais")):
            continue
        corpo.remove(el)
    # conteúdo: das questões em diante (os metadados do .md ficam de fora)
    ini = re.search(r"(?m)^\*\*Orientações ao estudante\*\*|^## Questões", md)
    conteudo = md[ini.start():] if ini else md
    sect = corpo.find(W + "sectPr")
    Escritor(d, alt_letras=alt).escrever(conteudo)
    # sectPr precisa continuar sendo o último filho
    if sect is not None:
        corpo.remove(sect); corpo.append(sect)
    limpar_vazios(d)
    return d, pasta, nome


# ------------------------------------------------------------ entrega de trabalho
def gerar_trabalho():
    modelo = DOC / "Instrumentos Avaliativos" / "TEMPLATE ENTREGA DE TRABALHO - nomedadisciplina.docx"
    d = docx.Document(modelo)
    md = (RAIZ / "instrumentos_avaliativos" / "entrega_trabalho.md").read_text(encoding="utf-8")
    s2 = dict(secoes(md, 2))
    corpo = d.element.body
    for el in list(corpo.iterchildren()):
        tx = texto(el).strip()
        if tag(el) == "p" and re.match(r"^(ATENÇÃO|EXCLUIR AS ORIENTAÇÕES|TODOS OS ITENS)", tx):
            corpo.remove(el)
        if tag(el) == "tbl" and tx.startswith("O CASE existe"):
            corpo.remove(el)
    caixas = {texto(t._tbl).strip().upper(): t for t in d.tables}

    def pegar(pref):
        return next(t for k, t in caixas.items() if k.startswith(pref.upper()))

    def preencher(pref, titulo, conteudo):
        t = pegar(pref)
        set_titulo_celula(t.rows[0].cells[0], titulo)
        remover_linhas(t._tbl, 2)
        escrever_celula(t.rows[1].cells[0], conteudo)

    preencher("TÍTULO", "TÍTULO:", s2["Título"])
    preencher("DESAFIO", "DESAFIO:", s2["Desafio"])
    preencher("FONTE DE PESQ", "FONTE DE PESQUISA:", s2["Fonte de pesquisa"])
    preencher("5. ENTREGÁVE", "5. ENTREGÁVEL E DISTRIBUIÇÃO DA PONTUAÇÃO:",
              s2["Entregável e distribuição da pontuação"] + "\n\n## Roteiro do estudante\n\n" + s2["Roteiro do estudante"])
    preencher("6. SOLUÇÃO", "6. SOLUÇÃO: (esse item será removido antes do case ser disponibilizado ao aluno)", s2["Solução"])
    limpar_vazios(d)
    return d, "Instrumentos Avaliativos", f"TEMPLATE ENTREGA DE TRABALHO - {DISCIPLINA}.docx"


def main():
    SAIDA.mkdir(exist_ok=True)
    gerados = []
    for u in (1, 2, 3, 4):
        gerados.append(gerar_unidade(u))
        gerados.append(gerar_questionario(
            DOC / f"Unidade {u}" / f"40 Questões - UNI{u}_nomedadisciplina.docx",
            RAIZ / f"unidade_{u}" / f"questoes_uni{u}.md", "", f"40 Questões - UNI{u}_{DISCIPLINA}.docx", f"Unidade {u}"))
    gerados.append(gerar_trabalho())
    gerados.append(gerar_questionario(
        DOC / "Instrumentos Avaliativos" / "Avaliação final_(10 discursivas)_nomedadisciplina.docx",
        RAIZ / "instrumentos_avaliativos" / "avaliacao_final.md", "",
        f"Avaliação final_(10 discursivas)_{DISCIPLINA}.docx", "Instrumentos Avaliativos", alt=False))
    ementa = docx.Document()
    st = ementa.styles["Normal"]; st.font.name = FONTE; st.font.size = Pt(12)
    Escritor(ementa).escrever((RAIZ / "EMENTA.md").read_text(encoding="utf-8"))
    gerados.append((ementa, ".", f"Ementa proposta - {DISCIPLINA}.docx"))
    for d, pasta, nome in gerados:
        destino = SAIDA / pasta / nome
        destino.parent.mkdir(parents=True, exist_ok=True)
        d.save(destino)
        print(destino.relative_to(RAIZ))


if __name__ == "__main__":
    sys.exit(main())
