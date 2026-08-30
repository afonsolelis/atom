"""Model checker de estados explícitos, escrito do zero — coração da Aula 10.

A ideia central da verificação por estados explícitos é simples e cabe em
poucas dezenas de linhas: (1) enumere todo o espaço de entradas possível;
(2) explore por busca em largura (BFS) todo o espaço de estados alcançável
a partir do estado inicial, aplicando a função de transição a cada entrada
possível; (3) para cada transição alcançada, verifique cada invariante; (4)
se alguma falhar, reconstrua o caminho da raiz da árvore de busca até a
transição violadora — esse caminho *é* o contraexemplo.

Este módulo não usa nenhuma ferramenta externa de verificação (nada de
NuSMV/SPIN/TLC): o objetivo pedagógico é que o estudante veja o mecanismo,
não apenas o resultado de uma caixa-preta.
"""

from __future__ import annotations

import itertools
import time
from collections import deque
from dataclasses import dataclass, field
from typing import Callable

from .requisitos import Requisito
from .supervisor import ESTADO_INICIAL, Entradas, Estado, Saidas, transition

TransitionFn = Callable[[Estado, Entradas], tuple[Estado, Saidas]]

#: Campos booleanos de `Entradas` que compõem o espaço de entrada explorado.
CAMPOS_BOOL = (
    "comando_partir",
    "comando_parar",
    "obstaculo",
    "emergencia",
    "falha_encoder",
    "rearme",
)

#: Amostras de velocidade usadas na exploração: 0.0 (parado, dispara a
#: transição DESACELERANDO -> OCIOSO) e um valor acima da tolerância V_TOL
#: (robô em movimento). Duas amostras bastam porque nenhuma transição do
#: supervisor discrimina a velocidade além de "parado ou não".
VELOCIDADES_AMOSTRA = (0.0, 0.6)


def gerar_entradas_possiveis() -> list[Entradas]:
    """Enumera o espaço de entradas abstrato usado na verificação exaustiva."""
    entradas = []
    for combinacao in itertools.product((False, True), repeat=len(CAMPOS_BOOL)):
        campos = dict(zip(CAMPOS_BOOL, combinacao))
        for v in VELOCIDADES_AMOSTRA:
            entradas.append(Entradas(velocidade=v, **campos))
    return entradas


@dataclass(frozen=True)
class Transicao:
    """Uma aresta (origem, entrada) -> (destino, saída) do grafo de estados."""

    origem: Estado
    entrada: Entradas
    destino: Estado
    saida: Saidas


@dataclass
class ResultadoExploracao:
    """Resultado completo de uma busca em largura no espaço de estados."""

    estado_inicial: Estado
    estados_alcancaveis: set = field(default_factory=set)
    transicoes: list = field(default_factory=list)
    predecessores: dict = field(default_factory=dict)  # estado -> Transicao que o alcançou primeiro
    tempo_s: float = 0.0

    @property
    def n_estados(self) -> int:
        return len(self.estados_alcancaveis)

    @property
    def n_transicoes(self) -> int:
        return len(self.transicoes)


def explorar(
    transition_fn: TransitionFn = transition,
    estado_inicial: Estado = ESTADO_INICIAL,
    entradas_possiveis: list[Entradas] | None = None,
) -> ResultadoExploracao:
    """Busca em largura exaustiva no espaço de estados do supervisor.

    Devolve todos os estados alcançáveis, todas as transições exploradas
    (origem x entrada, para toda entrada possível, a partir de todo estado
    alcançável) e uma árvore de predecessores que permite reconstruir o
    caminho mais curto da inicial até qualquer estado alcançado.
    """
    entradas_possiveis = entradas_possiveis if entradas_possiveis is not None else gerar_entradas_possiveis()

    t0 = time.perf_counter()
    resultado = ResultadoExploracao(estado_inicial=estado_inicial)
    resultado.estados_alcancaveis.add(estado_inicial)
    fila = deque([estado_inicial])

    while fila:
        origem = fila.popleft()
        for entrada in entradas_possiveis:
            destino, saida = transition_fn(origem, entrada)
            t = Transicao(origem, entrada, destino, saida)
            resultado.transicoes.append(t)
            if destino not in resultado.estados_alcancaveis:
                resultado.estados_alcancaveis.add(destino)
                resultado.predecessores[destino] = t
                fila.append(destino)

    resultado.tempo_s = time.perf_counter() - t0
    return resultado


def reconstruir_caminho(resultado: ResultadoExploracao, estado_alvo: Estado) -> list[Transicao]:
    """Reconstrói o caminho (lista de transições) da inicial até `estado_alvo`."""
    if estado_alvo == resultado.estado_inicial:
        return []
    caminho: list[Transicao] = []
    atual = estado_alvo
    while atual != resultado.estado_inicial:
        t = resultado.predecessores[atual]
        caminho.append(t)
        atual = t.origem
    caminho.reverse()
    return caminho


@dataclass(frozen=True)
class Contraexemplo:
    """Um caminho da inicial até uma transição que viola um requisito."""

    requisito: Requisito
    caminho: list  # list[Transicao], a última é a transição violadora


def verificar_invariantes(
    resultado: ResultadoExploracao, requisitos_transicao: list[Requisito]
) -> list[Contraexemplo]:
    """Verifica cada requisito de transição em toda aresta explorada.

    Devolve a lista de contraexemplos encontrados (vazia se tudo passou).
    Para cada violação, o contraexemplo carrega o caminho completo desde o
    estado inicial até a transição que quebrou o requisito.
    """
    violacoes: list[Contraexemplo] = []
    for t in resultado.transicoes:
        for req in requisitos_transicao:
            if not req.verificar_transicao(t.origem, t.entrada, t.saida, t.destino):
                caminho_ate_origem = reconstruir_caminho(resultado, t.origem)
                violacoes.append(Contraexemplo(requisito=req, caminho=caminho_ate_origem + [t]))
    return violacoes


def verificar_alcancabilidade(
    resultado: ResultadoExploracao, requisito: Requisito
) -> tuple[bool, list[Transicao]]:
    """Verifica um requisito de alcançabilidade; devolve (alcançável?, caminho testemunha)."""
    for estado in resultado.estados_alcancaveis:
        if requisito.estado_alvo(estado):
            return True, reconstruir_caminho(resultado, estado)
    return False, []


def formatar_entrada(entrada: Entradas) -> str:
    """Representação compacta de uma entrada, só com os campos ativos (True)."""
    ativos = [nome for nome in CAMPOS_BOOL if getattr(entrada, nome)]
    v = f"v={entrada.velocidade:.2f}"
    return "{" + ", ".join(ativos + [v]) + "}"


def formatar_caminho(caminho: list[Transicao]) -> str:
    """Formata um caminho (contraexemplo ou testemunha) como texto legível."""
    if not caminho:
        return "(caminho vazio — já no estado inicial)"
    linhas = [f"  {caminho[0].origem.name}"]
    for t in caminho:
        linhas.append(f"    --[{formatar_entrada(t.entrada)}]--> {t.destino.name}")
    return "\n".join(linhas)


def imprimir_estatisticas(resultado: ResultadoExploracao) -> None:
    """Imprime uma tabela ASCII com as estatísticas da exploração."""
    largura = 46
    print("+" + "-" * largura + "+")
    print("| ESTATÍSTICAS DA EXPLORAÇÃO DE ESTADOS".ljust(largura + 1) + "|")
    print("+" + "-" * largura + "+")
    linhas = [
        ("estados alcançáveis", str(resultado.n_estados)),
        ("transições exploradas", str(resultado.n_transicoes)),
        ("tempo de exploração", f"{resultado.tempo_s * 1000:.3f} ms"),
    ]
    for rotulo, valor in linhas:
        print(f"| {rotulo:<28}{valor:>{largura - 30}} |")
    print("+" + "-" * largura + "+")
    print("| Estados alcançáveis:")
    for e in sorted(resultado.estados_alcancaveis, key=lambda x: x.name):
        print(f"|   - {e.name}")
    print("+" + "-" * largura + "+")


def verificar_tudo(
    transition_fn: TransitionFn = transition,
    requisitos_transicao: list[Requisito] | None = None,
    requisitos_alcancabilidade: list[Requisito] | None = None,
) -> dict:
    """Roda a exploração completa e verifica todos os requisitos aplicáveis.

    Função de conveniência usada pelos scripts de aula: devolve um relatório
    (dicionário) com a exploração, as violações de invariante encontradas e
    os resultados de alcançabilidade.
    """
    from .requisitos import REQUISITOS_ALCANCABILIDADE, REQUISITOS_TRANSICAO

    requisitos_transicao = requisitos_transicao if requisitos_transicao is not None else REQUISITOS_TRANSICAO
    requisitos_alcancabilidade = (
        requisitos_alcancabilidade if requisitos_alcancabilidade is not None else REQUISITOS_ALCANCABILIDADE
    )

    resultado = explorar(transition_fn=transition_fn)
    violacoes = verificar_invariantes(resultado, requisitos_transicao)
    alcancabilidade = {
        req.id: verificar_alcancabilidade(resultado, req) for req in requisitos_alcancabilidade
    }
    return {
        "resultado": resultado,
        "violacoes": violacoes,
        "alcancabilidade": alcancabilidade,
    }
