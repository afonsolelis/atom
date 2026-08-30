"""Testes baseados em modelo (MBT) para o supervisor do NexaBot — Aula 12.

Três técnicas complementares, todas derivadas do MESMO modelo
(`nexabot.supervisor.transition`), nenhuma escrita "à mão" caso a caso:

1. Geração de casos de teste por cobertura de estados e de transições:
   percorremos o grafo de estados construído por `modelcheck.explorar` e
   emitimos, para cada estado e para cada transição distinta observada, um
   caso de teste concreto (sequência de entradas que o exercita).
2. Testes baseados em propriedades com `hypothesis.stateful`: uma máquina
   de estados que sorteia sequências de entradas e verifica, a cada passo,
   os requisitos de `nexabot.requisitos`.
3. Medição de cobertura: dada uma suíte de casos de teste, quantos dos
   estados e das transições possíveis do modelo ela de fato exercitou.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from hypothesis import strategies as st
from hypothesis.stateful import RuleBasedStateMachine, invariant, rule

from .modelcheck import ResultadoExploracao, Transicao, explorar, reconstruir_caminho
from .requisitos import REQUISITOS_TRANSICAO
from .supervisor import ESTADO_INICIAL, Entradas, Estado, Supervisor, transition


@dataclass(frozen=True)
class CasoDeTeste:
    """Um caso de teste concreto, gerado a partir do modelo."""

    id: str
    descricao: str
    entradas_sequencia: tuple  # tuple[Entradas, ...]
    estados_esperados: tuple  # tuple[Estado, ...] — inclui o estado inicial no índice 0

    def rodar(self) -> None:
        """Executa o caso contra um `Supervisor` novo e valida os estados esperados."""
        sup = Supervisor()
        assert sup.state == self.estados_esperados[0]
        for entrada, esperado in zip(self.entradas_sequencia, self.estados_esperados[1:]):
            sup.step(entrada)
            assert sup.state == esperado, (
                f"caso {self.id}: esperado {esperado.name}, obtido {sup.state.name}"
            )


def _caminho_para_caso(id_: str, descricao: str, caminho: list) -> CasoDeTeste:
    entradas = tuple(t.entrada for t in caminho)
    estados = (ESTADO_INICIAL,) + tuple(t.destino for t in caminho)
    return CasoDeTeste(id=id_, descricao=descricao, entradas_sequencia=entradas, estados_esperados=estados)


def gerar_casos_cobertura_estados(resultado: ResultadoExploracao | None = None) -> list[CasoDeTeste]:
    """Um caso de teste por estado alcançável: o caminho mais curto até ele.

    Como o caminho vem diretamente da árvore de busca em largura do model
    checker, visitar todos os estados alcançáveis garante 100% de cobertura
    de estados por construção.
    """
    resultado = resultado if resultado is not None else explorar()
    casos = []
    for estado in sorted(resultado.estados_alcancaveis, key=lambda e: e.name):
        caminho = reconstruir_caminho(resultado, estado)
        casos.append(
            _caminho_para_caso(
                id_=f"cobre_estado_{estado.name}",
                descricao=f"Alcança o estado {estado.name} a partir de {ESTADO_INICIAL.name}.",
                caminho=caminho,
            )
        )
    return casos


def gerar_casos_cobertura_transicoes(resultado: ResultadoExploracao | None = None) -> list[CasoDeTeste]:
    """Um caso de teste por transição (origem, destino) distinta observada.

    O espaço bruto de (estado x entrada) tem centenas de combinações, mas
    muitas levam ao mesmo par (origem, destino) com a mesma saída — por
    exemplo, dezenas de entradas diferentes mantêm o supervisor em OCIOSO.
    Para cobertura de transições o que importa é o par (origem, destino):
    escolhemos um representante de cada par e o caminho mais curto até a
    origem, formando um caso de teste mínimo que o exercita.
    """
    resultado = resultado if resultado is not None else explorar()
    representantes: dict[tuple[Estado, Estado], Transicao] = {}
    for t in resultado.transicoes:
        chave = (t.origem, t.destino)
        if chave not in representantes:
            representantes[chave] = t

    casos = []
    for (origem, destino), t in sorted(representantes.items(), key=lambda kv: (kv[0][0].name, kv[0][1].name)):
        caminho_ate_origem = reconstruir_caminho(resultado, origem)
        caso = _caminho_para_caso(
            id_=f"cobre_transicao_{origem.name}_para_{destino.name}",
            descricao=f"Exercita a transição {origem.name} -> {destino.name}.",
            caminho=caminho_ate_origem + [t],
        )
        casos.append(caso)
    return casos


def medir_cobertura(suite: list[CasoDeTeste], resultado_referencia: ResultadoExploracao | None = None) -> dict:
    """Mede a cobertura de estados e de transições (origem, destino) de uma suíte.

    Devolve um dicionário com contagens absolutas e percentuais em relação
    ao espaço de referência (todos os estados/transições alcançáveis do
    modelo, calculados por `modelcheck.explorar`).
    """
    resultado_referencia = resultado_referencia if resultado_referencia is not None else explorar()
    total_estados = resultado_referencia.estados_alcancaveis
    total_transicoes = {(t.origem, t.destino) for t in resultado_referencia.transicoes}

    estados_cobertos: set[Estado] = set()
    transicoes_cobertas: set[tuple[Estado, Estado]] = set()

    for caso in suite:
        estados_cobertos.update(caso.estados_esperados)
        for i in range(len(caso.estados_esperados) - 1):
            transicoes_cobertas.add((caso.estados_esperados[i], caso.estados_esperados[i + 1]))

    n_estados_cobertos = len(estados_cobertos & total_estados)
    n_transicoes_cobertas = len(transicoes_cobertas & total_transicoes)

    return {
        "estados_cobertos": n_estados_cobertos,
        "estados_totais": len(total_estados),
        "pct_estados": 100.0 * n_estados_cobertos / len(total_estados) if total_estados else 0.0,
        "transicoes_cobertas": n_transicoes_cobertas,
        "transicoes_totais": len(total_transicoes),
        "pct_transicoes": 100.0 * n_transicoes_cobertas / len(total_transicoes) if total_transicoes else 0.0,
    }


# --------------------------------------------------------------------------
# Testes baseados em propriedades (hypothesis.stateful)
# --------------------------------------------------------------------------
_ENTRADA_BOOL = st.booleans()
_ENTRADA_VELOCIDADE = st.floats(min_value=0.0, max_value=1.5, allow_nan=False, allow_infinity=False)


class SupervisorMachine(RuleBasedStateMachine):
    """Sorteia sequências de entradas e verifica os requisitos a cada passo.

    Diferente da geração por cobertura (determinística, exaustiva sobre o
    grafo pequeno), esta técnica sorteia entradas ao acaso e tenta *quebrar*
    os requisitos — é boa para achar sequências longas e inesperadas que a
    geração por cobertura, mais estruturada, não cobriria.
    """

    def __init__(self) -> None:
        super().__init__()
        self.supervisor = Supervisor()
        self.historico: list[tuple[Estado, Entradas, Estado]] = []

    @rule(
        comando_partir=_ENTRADA_BOOL,
        comando_parar=_ENTRADA_BOOL,
        obstaculo=_ENTRADA_BOOL,
        emergencia=_ENTRADA_BOOL,
        falha_encoder=_ENTRADA_BOOL,
        rearme=_ENTRADA_BOOL,
        velocidade=_ENTRADA_VELOCIDADE,
    )
    def passo(self, comando_partir, comando_parar, obstaculo, emergencia, falha_encoder, rearme, velocidade):
        entrada = Entradas(
            comando_partir=comando_partir,
            comando_parar=comando_parar,
            obstaculo=obstaculo,
            emergencia=emergencia,
            falha_encoder=falha_encoder,
            rearme=rearme,
            velocidade=velocidade,
        )
        estado_antes = self.supervisor.state
        saida = self.supervisor.step(entrada)
        estado_depois = self.supervisor.state
        self.historico.append((estado_antes, entrada, estado_depois))

        for req in REQUISITOS_TRANSICAO:
            assert req.verificar_transicao(estado_antes, entrada, saida, estado_depois), (
                f"{req.id} violado: {estado_antes.name} --[{entrada}]--> {estado_depois.name}"
            )

    @invariant()
    def estado_e_valido(self) -> None:
        assert self.supervisor.state in Estado


#: Classe pytest gerada pelo hypothesis (usada em tests/test_supervisor.py).
TestSupervisorMachine = SupervisorMachine.TestCase
