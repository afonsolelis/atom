"""Matriz de rastreabilidade requisito -> modelo -> código gerado -> teste.

Varre o projeto inteiro (`.py`) atrás de identificadores `REQ-<FAMÍLIA>-NNN`
em docstrings e comentários, classifica cada arquivo onde um requisito
aparece em uma das quatro colunas da matriz (Modelo, Código gerado, Teste,
Outros) e emite uma tabela Markdown.

Isto é rastreabilidade "de baixo para cima": em vez de manter uma planilha
separada que inevitavelmente fica desatualizada, a matriz é derivada do
próprio código — se um requisito for citado em `nexabot/controllers.py` e
em `tests/test_controllers.py`, a matriz mostra essa cobertura
automaticamente; se um requisito só aparecer em um lugar, a lacuna também
fica visível.

**Funciona mesmo com módulos ausentes.** A Unidade 4 é construída em
paralelo por várias frentes (`nexabot/supervisor.py`, `nexabot/fmu/`,
`nexabot/cosim.py`, os `aula_NN/` de outras aulas, ...); este módulo trata
a ausência de qualquer um deles como um aviso, não como erro — a matriz
gerada hoje mostra o estado real do projeto hoje, e melhora sozinha
conforme os demais módulos forem chegando.

Rastreabilidade: REQ-CODEGEN-002 (rastreabilidade automática), e este
próprio módulo é a ferramenta que produz a evidência de rastreabilidade
citada nos objetivos de DO-178C/ISO 26262 discutidos na Aula 16
(`nexabot/rastreabilidade.py` continua honesto: ele produz uma EVIDÊNCIA,
não uma certificação).
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

REQ_PATTERN = re.compile(r"REQ-[A-Z][A-Z0-9]*-\d{3}")

# Diretórios ignorados ao varrer o projeto em busca de identificadores REQ-*.
IGNORAR_DIRS = {
    ".venv", "__pycache__", ".git", ".hypothesis", ".pytest_cache",
    "node_modules", ".mypy_cache", ".ruff_cache",
}

# Classificação de caminho -> coluna da matriz. Testada em ordem; a primeira
# regra cujo padrão bate com o caminho relativo (posix, a partir da raiz do
# projeto) decide a coluna. Um arquivo que não bate em nenhuma regra cai em
# "Outros".
CategoriaRegras = tuple[tuple[str, str], ...]

REGRAS_CATEGORIA: CategoriaRegras = (
    (r"^nexabot/codegen/generated/", "Código gerado"),
    (r"^nexabot/codegen/templates/", "Código gerado"),
    (r"^nexabot/codegen/(derive|generate)\.py$", "Código gerado"),
    (r"^nexabot/firmware/", "Código gerado"),
    (r"^tests/", "Teste"),
    (r"^aula_\d+/", "Teste"),  # scripts de aula = evidência de teste/demonstração ao vivo
    (r"^nexabot/", "Modelo"),
)


def _categoria(caminho_relativo: str) -> str:
    for padrao, categoria in REGRAS_CATEGORIA:
        if re.match(padrao, caminho_relativo):
            return categoria
    return "Outros"


def _iter_arquivos_py(root: Path):
    for path in sorted(root.rglob("*.py")):
        if any(parte in IGNORAR_DIRS for parte in path.parts):
            continue
        yield path


@dataclass
class Ocorrencia:
    """Um requisito citado em um arquivo, já classificado por categoria."""

    caminho: str  # relativo à raiz do projeto, estilo posix
    categoria: str
    trecho: str  # linha onde o identificador apareceu, para contexto
    janela: str  # trecho + linha anterior/seguinte, para descrições que quebram linha


@dataclass
class EntradaMatriz:
    """Uma linha da matriz de rastreabilidade: um requisito e onde ele aparece."""

    requisito: str
    descricao: str = "(descrição não encontrada automaticamente)"
    ocorrencias: list[Ocorrencia] = field(default_factory=list)

    def arquivos_por_categoria(self, categoria: str) -> list[str]:
        vistos: list[str] = []
        for oc in self.ocorrencias:
            if oc.categoria == categoria and oc.caminho not in vistos:
                vistos.append(oc.caminho)
        return vistos


def _descricoes_canonicas() -> dict[str, str]:
    """Tenta obter descrições oficiais de `nexabot.requisitos` (REQ-SAFE-*).

    Módulo de outra frente de trabalho da Unidade 3 — importado
    defensivamente: se ainda não existir (ou falhar ao importar por
    qualquer motivo), a matriz simplesmente usa descrições extraídas por
    heurística do próprio texto-fonte, com um aviso.
    """
    try:
        from . import requisitos as mod_requisitos
    except ImportError:
        return {}
    except Exception:
        return {}

    descricoes: dict[str, str] = {}
    try:
        for r in getattr(mod_requisitos, "REQUISITOS", []):
            descricoes[r.id] = r.descricao
    except Exception:
        pass
    return descricoes


def _descricao_heuristica(ocorrencias: list[Ocorrencia], requisito: str) -> str | None:
    """Tenta extrair uma descrição curta a partir do texto ao redor de
    ocorrências de `requisito` nos comentários/docstrings do projeto (best
    effort — só para preencher a coluna quando não há registro formal como
    `nexabot.requisitos.REQUISITOS`).

    Prioriza ocorrências na categoria "Modelo" (o módulo que originalmente
    declara o requisito, por convenção deste projeto) sobre citações em
    testes/scripts de aula, e usa uma janela de 3 linhas — não só a linha
    do match — porque a descrição às vezes continua na linha seguinte de
    um docstring (ex.: `nexabot/controllers.py`).
    """
    ordenadas = sorted(ocorrencias, key=lambda oc: 0 if oc.categoria == "Modelo" else 1)

    for oc in ordenadas:
        # Caso mais comum neste projeto: "REQ-<FAMÍLIA>-NNN (descrição curta)" —
        # extrai só o parêntese que segue ESTE identificador específico,
        # não a linha inteira (que pode citar vários REQ-* de uma vez).
        m = re.search(rf"{re.escape(requisito)}\s*\(([^)]+)\)", oc.janela)
        if m:
            return m.group(1).strip()[:160]

    for oc in ordenadas:
        limpo = oc.trecho.strip().lstrip("#*\"' ").strip()
        # remove o próprio identificador do início do trecho, se estiver lá
        limpo = re.sub(rf"^{re.escape(requisito)}\s*[:\-–]?\s*", "", limpo)
        limpo = re.sub(r"^\(([^)]*)\)\s*", r"\1 — ", limpo)
        if limpo and limpo != requisito:
            return limpo[:160]
    return None


@dataclass
class ResultadoVarredura:
    """Resultado completo de `construir_matriz`: entradas + avisos."""

    entradas: list[EntradaMatriz]
    avisos: list[str]
    n_arquivos_lidos: int
    n_arquivos_com_erro: int


def construir_matriz(root: Path = PROJECT_ROOT) -> ResultadoVarredura:
    """Varre `root` e monta a matriz de rastreabilidade completa."""
    avisos: list[str] = []
    ocorrencias_por_req: dict[str, list[Ocorrencia]] = {}
    n_lidos = 0
    n_erro = 0

    for path in _iter_arquivos_py(root):
        try:
            texto = path.read_text(encoding="utf-8")
        except Exception as exc:
            n_erro += 1
            avisos.append(f"não foi possível ler {path}: {exc!r}")
            continue
        n_lidos += 1

        rel = path.relative_to(root).as_posix()
        categoria = _categoria(rel)

        linhas_arquivo = texto.splitlines()
        for numero_linha, linha in enumerate(linhas_arquivo):
            for match in REQ_PATTERN.finditer(linha):
                req_id = match.group(0)
                janela = " ".join(
                    linhas_arquivo[max(0, numero_linha - 1): numero_linha + 2]
                )
                ocorrencias_por_req.setdefault(req_id, []).append(
                    Ocorrencia(caminho=rel, categoria=categoria, trecho=linha, janela=janela)
                )

    descricoes_canonicas = _descricoes_canonicas()
    if not descricoes_canonicas:
        avisos.append(
            "nexabot.requisitos ainda não disponível (ou sem REQUISITOS) — "
            "descrições de REQ-SAFE-* preenchidas por heurística de texto."
        )

    entradas: list[EntradaMatriz] = []
    for req_id in sorted(ocorrencias_por_req):
        ocorrencias = ocorrencias_por_req[req_id]
        descricao = descricoes_canonicas.get(req_id)
        if descricao is None:
            descricao = _descricao_heuristica(ocorrencias, req_id) or (
                "(descrição não encontrada automaticamente — ver ocorrências)"
            )
        entradas.append(EntradaMatriz(requisito=req_id, descricao=descricao, ocorrencias=ocorrencias))

    for modulo_esperado in (
        "nexabot.supervisor", "nexabot.cosim", "nexabot.modelcheck",
        "nexabot.timed", "nexabot.mbt", "nexabot.fmu",
    ):
        caminho_provavel = root / (modulo_esperado.replace(".", "/") )
        if not (caminho_provavel.with_suffix(".py").exists() or caminho_provavel.is_dir()):
            avisos.append(f"módulo {modulo_esperado} ainda não existe neste checkout — ignorado.")

    return ResultadoVarredura(
        entradas=entradas, avisos=avisos, n_arquivos_lidos=n_lidos, n_arquivos_com_erro=n_erro,
    )


def _fmt_arquivos(lista: list[str]) -> str:
    if not lista:
        return "—"
    return "<br>".join(f"`{f}`" for f in lista)


def matriz_para_markdown(resultado: ResultadoVarredura) -> str:
    """Renderiza `ResultadoVarredura` como uma tabela Markdown completa."""
    linhas = [
        "# Matriz de rastreabilidade — Projeto NexaBot",
        "",
        "Gerada automaticamente por `nexabot/rastreabilidade.py` a partir dos",
        "identificadores `REQ-*` encontrados em docstrings e comentários do",
        "projeto (varredura estática de texto, não de execução). Reflete o",
        "estado do repositório no momento em que o script foi rodado — não é",
        "mantida manualmente.",
        "",
        f"- Arquivos `.py` lidos: **{resultado.n_arquivos_lidos}**"
        + (f" ({resultado.n_arquivos_com_erro} com erro de leitura)" if resultado.n_arquivos_com_erro else ""),
        f"- Requisitos distintos encontrados: **{len(resultado.entradas)}**",
        "",
    ]

    if resultado.avisos:
        linhas.append("## Avisos")
        linhas.append("")
        for aviso in resultado.avisos:
            linhas.append(f"- {aviso}")
        linhas.append("")

    linhas.append("## Matriz requisito -> modelo -> código gerado -> teste")
    linhas.append("")
    linhas.append("| Requisito | Descrição | Modelo | Código gerado | Teste | Outros |")
    linhas.append("|---|---|---|---|---|---|")
    for entrada in resultado.entradas:
        modelo = _fmt_arquivos(entrada.arquivos_por_categoria("Modelo"))
        gerado = _fmt_arquivos(entrada.arquivos_por_categoria("Código gerado"))
        teste = _fmt_arquivos(entrada.arquivos_por_categoria("Teste"))
        outros = _fmt_arquivos(entrada.arquivos_por_categoria("Outros"))
        descricao = entrada.descricao.replace("|", "\\|")
        linhas.append(f"| `{entrada.requisito}` | {descricao} | {modelo} | {gerado} | {teste} | {outros} |")

    linhas.append("")
    linhas.append(
        "**Nota de honestidade técnica:** esta matriz é evidência de "
        "rastreabilidade — um artefato que um processo de certificação "
        "(DO-178C, ISO 26262) exigiria como *insumo*. Gerá-la não certifica "
        "nada; certificação envolve auditoria independente, qualificação de "
        "ferramenta e um processo aprovado por uma autoridade/organismo "
        "certificador. Ver `aula_16/02_evidencias.py`."
    )
    return "\n".join(linhas) + "\n"


def gerar_e_salvar(
    root: Path = PROJECT_ROOT, output_path: Path | None = None
) -> tuple[ResultadoVarredura, Path]:
    """Constrói a matriz e grava o Markdown em `output_path`
    (`<root>/rastreabilidade.md` por padrão)."""
    resultado = construir_matriz(root)
    destino = output_path if output_path is not None else root / "rastreabilidade.md"
    destino.write_text(matriz_para_markdown(resultado), encoding="utf-8")
    return resultado, destino


if __name__ == "__main__":
    resultado, destino = gerar_e_salvar()
    print(f"Matriz gerada com {len(resultado.entradas)} requisitos -> {destino}")
    for aviso in resultado.avisos:
        print(f"aviso: {aviso}")
