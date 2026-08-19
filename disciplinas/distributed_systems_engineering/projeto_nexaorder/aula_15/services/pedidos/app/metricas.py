"""Métricas com proteção contra cardinalidade — Unidade 4, Aula 13.

O erro mais custoso ao adotar correlação com entusiasmo é reaproveitar o
trace_id — ou qualquer identificador por requisição — como rótulo de
métrica. Cada requisição gera um valor novo de dimensão, e o sistema de
métricas passa a armazenar uma série temporal por requisição: o custo de
armazenamento e consulta cresce sem limite.

`ContadorComRotulos` torna esse erro impossível de cometer silenciosamente:
recusa qualquer dimensão não declarada de antemão e recusa uma dimensão
declarada assim que ela ultrapassa um número razoável de valores distintos
— o sinal de que um identificador por requisição foi usado por engano em
lugar de um atributo agregável (rota, código de status, região).
"""

from __future__ import annotations

from dataclasses import dataclass, field


class DimensaoDeAltaCardinalidade(Exception):
    """Levantada quando uma dimensão de métrica recebe mais valores
    distintos do que uma dimensão agregável deveria ter, ou quando recebe
    uma dimensão não declarada (ver docs/observabilidade.md)."""


@dataclass
class ContadorComRotulos:
    nome: str
    dimensoes_permitidas: frozenset[str]
    limite_valores_distintos_por_dimensao: int = 50
    _valores_vistos: dict[str, set[str]] = field(default_factory=dict, init=False)
    _contagens: dict[tuple, int] = field(default_factory=dict, init=False)

    def incrementar(self, **rotulos: str) -> None:
        nao_declaradas = set(rotulos) - self.dimensoes_permitidas
        if nao_declaradas:
            raise DimensaoDeAltaCardinalidade(
                f"dimensão(ões) não declarada(s) para '{self.nome}': {sorted(nao_declaradas)}"
            )

        for nome_dimensao, valor in rotulos.items():
            vistos = self._valores_vistos.setdefault(nome_dimensao, set())
            vistos.add(str(valor))
            if len(vistos) > self.limite_valores_distintos_por_dimensao:
                raise DimensaoDeAltaCardinalidade(
                    f"dimensão '{nome_dimensao}' de '{self.nome}' ultrapassou "
                    f"{self.limite_valores_distintos_por_dimensao} valores distintos — "
                    "provável identificador por requisição usado como rótulo de métrica"
                )

        chave = tuple(sorted(rotulos.items()))
        self._contagens[chave] = self._contagens.get(chave, 0) + 1

    def valor(self, **rotulos: str) -> int:
        chave = tuple(sorted(rotulos.items()))
        return self._contagens.get(chave, 0)

    def total(self) -> int:
        return sum(self._contagens.values())
