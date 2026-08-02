"""Janela por tempo de evento, com marca d'água — Unidade 4, Aula 15.

A distinção central do roteiro: tempo de evento é o instante em que o fato
ocorreu no domínio de negócio (a tentativa de pagamento, no relógio do
cliente); tempo de processamento é o instante em que o pipeline
efetivamente processa aquele evento — segundos ou minutos depois. Uma
janela baseada em tempo de processamento é simples, mas pode dividir um
único padrão de fraude em dois grupos que nunca disparam o alerta juntos,
só porque a rede atrasou parte dos eventos (ver
`test_janela_evento.py::test_janela_por_tempo_de_evento_agrupa_mesmo_com_atraso_de_rede`
para a reprodução exata do exemplo do roteiro).

Este módulo nunca lê o relógio: todo tempo (evento e processamento) é
passado explicitamente pelo chamador, o que o torna determinístico e
testável sem `time.sleep`. `app/main.py` é quem, na borda real, converte
`time.time()` em milissegundos ao ingerir uma tentativa.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Tentativa:
    dispositivo_id: str
    tempo_evento_ms: int
    tempo_processamento_ms: int


@dataclass
class JanelaPorTempoDeEvento:
    """Conta tentativas por dispositivo dentro de uma janela deslizante de
    `duracao_ms`, agrupadas pelo instante em que o fato ocorreu — não pelo
    instante em que chegaram ao pipeline."""

    duracao_ms: int
    tolerancia_atraso_ms: int
    _tentativas_por_dispositivo: dict[str, list[Tentativa]] = field(default_factory=dict, init=False)
    _marca_dagua_ms: int = field(default=0, init=False)

    def ingerir(self, tentativa: Tentativa) -> None:
        self._tentativas_por_dispositivo.setdefault(tentativa.dispositivo_id, []).append(tentativa)

    def avancar_marca_dagua(self, tempo_processamento_atual_ms: int) -> int:
        """A marca d'água é `tempo_processamento_atual - tolerancia_atraso`:
        uma estimativa de até que ponto, no tempo de evento, o pipeline já
        recebeu a maior parte dos dados. Só avança — nunca recua, mesmo que
        chegue um evento com tempo de processamento anterior ao atual."""
        self._marca_dagua_ms = max(
            self._marca_dagua_ms, tempo_processamento_atual_ms - self.tolerancia_atraso_ms
        )
        return self._marca_dagua_ms

    def esta_fechada(self, fim_da_janela_ms: int) -> bool:
        """Uma janela só deveria ser tratada como definitiva quando a
        marca d'água já ultrapassou seu fim — ou seja, quando o pipeline
        já admite não esperar mais eventos atrasados que caberiam nela."""
        return self._marca_dagua_ms >= fim_da_janela_ms

    def contagem_na_janela(self, dispositivo_id: str, fim_da_janela_ms: int) -> int:
        """Quantas tentativas daquele dispositivo têm tempo de EVENTO
        dentro de [fim_da_janela - duracao, fim_da_janela] — considerando
        todas as tentativas já ingeridas até agora, atrasadas ou não."""
        inicio_da_janela_ms = fim_da_janela_ms - self.duracao_ms
        tentativas = self._tentativas_por_dispositivo.get(dispositivo_id, [])
        return sum(1 for t in tentativas if inicio_da_janela_ms <= t.tempo_evento_ms <= fim_da_janela_ms)

    def contagem_por_tempo_de_processamento(self, dispositivo_id: str, fim_da_janela_ms: int) -> int:
        """A contagem que um pipeline ingênuo, baseado em tempo de
        PROCESSAMENTO, produziria — existe só para demonstrar a divergência
        do roteiro; não é o que este módulo recomenda usar para decidir."""
        inicio_da_janela_ms = fim_da_janela_ms - self.duracao_ms
        tentativas = self._tentativas_por_dispositivo.get(dispositivo_id, [])
        return sum(
            1 for t in tentativas if inicio_da_janela_ms <= t.tempo_processamento_ms <= fim_da_janela_ms
        )
