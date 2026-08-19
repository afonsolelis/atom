"""Funções como serviço: custo de inicialização a frio — Unidade 4, Aula 15.

Simula o que importa da execução de uma FaaS para efeitos de latência: se
o ambiente já estava "quente" (uma invocação recente manteve uma instância
viva) ou "frio" (é preciso inicializar antes de executar). Não modela
provisionamento real de uma plataforma — modela só o efeito observável que
motiva a decisão de onde usar FaaS: latência adicional, e onde ela
importa (ver docs/processamento.md e docs/adr/0015-*.md para o porquê de
não integrar uma plataforma FaaS real neste sandbox)."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ResultadoInvocacao:
    nome_funcao: str
    latencia_total_ms: float
    houve_inicializacao_a_frio: bool


@dataclass
class AmbienteFaas:
    """Cada função tem sua própria janela de aquecimento: se invocada
    dentro de `janela_de_aquecimento_ms` da última invocação, reaproveita
    o ambiente (sem custo de inicialização a frio); caso contrário, paga o
    custo novamente."""

    custo_inicializacao_a_frio_ms: float = 400.0
    janela_de_aquecimento_ms: float = 300_000.0  # 5 minutos — valor de exemplo
    _ultima_invocacao_ms: dict[str, float] = field(default_factory=dict, init=False)

    def invocar(self, nome_funcao: str, agora_ms: float, duracao_execucao_ms: float) -> ResultadoInvocacao:
        ultima = self._ultima_invocacao_ms.get(nome_funcao)
        ambiente_quente = ultima is not None and (agora_ms - ultima) <= self.janela_de_aquecimento_ms
        self._ultima_invocacao_ms[nome_funcao] = agora_ms

        custo_frio_ms = 0.0 if ambiente_quente else self.custo_inicializacao_a_frio_ms
        return ResultadoInvocacao(
            nome_funcao=nome_funcao,
            latencia_total_ms=custo_frio_ms + duracao_execucao_ms,
            houve_inicializacao_a_frio=not ambiente_quente,
        )
