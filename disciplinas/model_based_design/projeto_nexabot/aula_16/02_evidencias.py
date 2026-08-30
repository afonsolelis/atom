#!/usr/bin/env python3
"""Aula 16 — Script 2/3: o que este pipeline produz, e o que ele NÃO é.

O que este script faz
----------------------
Inventaria as evidências que o pipeline aberto da Unidade 4 efetivamente
produz (matriz de rastreabilidade, comparação SIL, suíte de regressão, CI)
e as associa a OBJETIVOS de dois padrões de certificação citados na
disciplina — DO-178C (software aeronáutico) e ISO 26262 (segurança
funcional automotiva) — junto com uma nota HONESTA sobre o que falta para
que essas evidências virassem, de fato, certificação.

Isto não é modéstia performática: afirmar que um pipeline de código aberto
"certifica" um sistema é uma afirmação **falsa e potencialmente perigosa**
em um contexto de engenharia de sistemas ciberfísicos com requisitos de
segurança. DO-178C e ISO 26262 são PROCESSOS DE CERTIFICAÇÃO — de
FERRAMENTA (qualificação de ferramenta, DO-330 / ISO 26262-8 cláusula 11) e
de PRODUTO (auditoria independente por um organismo certificador/DER,
evidência de processo ao longo de todo o ciclo de vida) — não uma
propriedade que uma suíte de scripts adquire sozinha.

Como rodar
----------
    .venv/bin/python aula_16/02_evidencias.py

Saída esperada (resumo)
------------------------
Uma tabela evidência -> objetivo(s) de norma relacionados -> o que ainda
falta para virar certificação, e uma seção final resumindo os requisitos de
qualificação de ferramenta que `gcc`/`nexabot.codegen` NÃO cumprem hoje.
"""

from __future__ import annotations

from dataclasses import dataclass


def linha(char: str = "-", n: int = 100) -> str:
    return char * n


@dataclass(frozen=True)
class Evidencia:
    nome: str
    produzida_por: str
    objetivos_relacionados: str
    o_que_falta_para_certificar: str


EVIDENCIAS: list[Evidencia] = [
    Evidencia(
        nome="Rastreabilidade requisito -> modelo -> código -> teste",
        produzida_por="nexabot/rastreabilidade.py -> rastreabilidade.md",
        objetivos_relacionados=(
            "DO-178C Tabela A-3/A-7 (rastreabilidade de requisitos de baixo "
            "nível ao código-fonte e aos casos de teste); "
            "ISO 26262-6 Tabela 1 (rastreabilidade de requisitos de software)"
        ),
        o_que_falta_para_certificar=(
            "Revisão INDEPENDENTE da completude/correção da matriz (aqui é "
            "gerada e lida pela mesma pessoa/ferramenta); processo formal de "
            "gestão de requisitos com aprovação e controle de mudança; "
            "cobertura de 100% dos requisitos (esta matriz mostra uma lacuna "
            "real: o requisito contínuo de limite de velocidade ainda não "
            "possui evidência de verificação)."
        ),
    ),
    Evidencia(
        nome="Equivalência numérica SIL (código gerado x modelo)",
        produzida_por="nexabot/sil.py + aula_14/02_equivalencia.py, 03_regressao.py",
        objetivos_relacionados=(
            "DO-178C Tabela A-5 (verificação de que o código-fonte é "
            "conforme aos requisitos de baixo nível / ao projeto); "
            "ISO 26262-6 Tabela 9 (verificação de unidade de software)"
        ),
        o_que_falta_para_certificar=(
            "Cobertura estrutural de código medida e reportada formalmente "
            "(MC/DC para DAL A/B, branch coverage para ASIL C/D — este "
            "projeto tem `coverage` instalado mas não integrado como "
            "GATE de aceitação); análise de robustez (entradas fora do "
            "domínio, injeção de falhas de hardware); revisão por pessoa "
            "independente de quem escreveu o código."
        ),
    ),
    Evidencia(
        nome="Geração automática de código com rastreabilidade embutida",
        produzida_por="nexabot/codegen/ (derive.py, generate.py, templates/*.j2)",
        objetivos_relacionados=(
            "DO-178C Seção 12.2 / DO-330 (qualificação de ferramenta de "
            "desenvolvimento — um gerador de código que SUBSTITUI revisão "
            "humana precisa ser qualificado); "
            "ISO 26262-8 Cláusula 11 (confiança no uso de ferramentas de "
            "software, TCL — Tool Confidence Level)"
        ),
        o_que_falta_para_certificar=(
            "QUALIFICAÇÃO FORMAL da ferramenta de geração (não apenas "
            "'testada por nós'): classificação de TCL/impacto de erro, "
            "validação com um conjunto de casos aprovado por processo, "
            "documentação do ambiente de qualificação e análise específica "
            "do uso de gcc como compilador. Qualificação só é necessária "
            "quando o uso e a verificação independente das saídas assim o "
            "determinarem; aqui essa análise formal não foi realizada."
        ),
    ),
    Evidencia(
        nome="CI executando testes + equivalência + rastreabilidade a cada mudança",
        produzida_por=".github/workflows/mbd-ci.yml",
        objetivos_relacionados=(
            "DO-178C Seção 11 (dados de verificação e de gestão de "
            "configuração); ISO 26262-8 Cláusula 7-9 (gestão de "
            "configuração e de mudança)"
        ),
        o_que_falta_para_certificar=(
            "Gestão de configuração formal (baseline assinada, auditoria de "
            "mudança); ambiente de CI ele mesmo qualificado/controlado; "
            "aprovação por papel de qualidade independente antes de "
            "promover uma versão, não só 'CI verde'."
        ),
    ),
    Evidencia(
        nome="Watchdog de prazo + comando seguro em estouro (HIL)",
        produzida_por="nexabot/hil.py (Watchdog) + aula_15/03_watchdog_real.py",
        objetivos_relacionados=(
            "ISO 26262-6 Tabela 8 (mecanismos de detecção e controle de "
            "falha ao nível de software); "
            "DO-178C Tabela A-5 (robustez a condições anômalas)"
        ),
        o_que_falta_para_certificar=(
            "Análise formal de FMEA/FTA cobrindo este mecanismo (por que "
            "3xTs é o prazo certo, não um número escolhido ad-hoc); "
            "verificação em hardware-alvo real (aqui só em loopback local); "
            "certificação do próprio microcontrolador/driver como "
            "componente de segurança (fora do escopo deste laboratório)."
        ),
    ),
]


def main() -> None:
    print(linha("="))
    print("Aula 16 — O que este pipeline produz (evidência) x o que ele NÃO faz (certificação)")
    print(linha("="))

    for ev in EVIDENCIAS:
        print(f"\n{linha('-')}")
        print(f"Evidência: {ev.nome}")
        print(f"Produzida por: {ev.produzida_por}")
        print(f"Objetivo(s) de norma relacionados:\n  {ev.objetivos_relacionados}")
        print(f"O que falta para virar certificação:\n  {ev.o_que_falta_para_certificar}")

    print("\n" + linha("="))
    print("Resumo executivo (honesto)")
    print(linha("="))
    print("""
1. DO-178C e ISO 26262 estruturam processos de garantia/certificação do
   software/sistema final, auditado por um organismo independente ao
   longo do ciclo de vida, e tratam também da confiança em FERRAMENTAS
   (DO-330 / ISO 26262-8 cláusula
   11 -- a necessidade e o nível de qualificação dependem do impacto de um
   possível erro e de ele poder ser detectado por verificação posterior).

2. Este projeto usa gcc, SymPy, Jinja2 e um gerador de código PRÓPRIO
   (nexabot/codegen/) SEM qualificação formal de nenhum deles. A suíte de
   equivalência SIL (aula_14) reduz o RISCO de erro de tradução. Ela pode
   integrar a estratégia de verificação, mas não substitui a análise formal
   de confiança e qualificação aplicável a cada uso da ferramenta.

3. Código aberto ou licença comercial não decide a qualificação. Se uma
   ferramenta de geração como nexabot/codegen elimina uma verificação e um
   erro seu pode chegar ao produto sem ser detectado, a equipe precisa
   qualificá-la no nível aplicável ou introduzir verificação independente
   suficiente. A decisão deve ser documentada para o uso concreto.

4. O que este laboratório efetivamente demonstra: COMO produzir os
   ARTEFATOS DE ENTRADA que um processo de certificação exigiria
   (rastreabilidade, evidência de equivalência, CI reprodutível,
   detecção de falha) -- não como obter uma certificação. Uma equipe que
   quisesse certificar o NexaBot de verdade usaria estes artefatos como
   PONTO DE PARTIDA de um processo formal com um organismo certificador,
   não como o processo em si.
""")


if __name__ == "__main__":
    main()
