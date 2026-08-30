# Aula 16 — Rastreabilidade e o limite honesto da "certificação"

Unidade 4, Aula 16 (fecha a disciplina): a matriz de rastreabilidade
requisito -> modelo -> código gerado -> teste (`nexabot/rastreabilidade.py`)
e uma discussão tecnicamente honesta sobre o que um pipeline de MBD aberto
produz (evidência) e o que ele não é (certificação DO-178C/ISO 26262).

## Como rodar

```bash
cd projeto_nexabot
.venv/bin/python aula_16/01_matriz_rastreabilidade.py
.venv/bin/python aula_16/02_evidencias.py
.venv/bin/python aula_16/03_desafio.py
```

## Scripts

| Script | O que mostra | Saída esperada (resumo) |
|---|---|---|
| `01_matriz_rastreabilidade.py` | Varre o projeto por identificadores `REQ-*`, monta e imprime a matriz, grava `rastreabilidade.md` na raiz | Tabela com um requisito por linha; contagem de requisitos sem evidência de teste |
| `02_evidencias.py` | Associa cada evidência produzida pelo pipeline (rastreabilidade, equivalência SIL, CI, watchdog) a objetivos de DO-178C/ISO 26262 e ao que falta para virar certificação de verdade | Tabela evidência -> objetivo -> lacuna, seguida de um resumo executivo |
| `03_desafio.py` | Identifica lacunas reais de cobertura de teste na matriz do momento e propõe (ou pede que o estudante escreva) um caso de teste para fechá-las | Lista de lacunas atuais + proposta de teste para uma delas (ou confirmação de que não há lacunas conhecidas) |

## Nota sobre `rastreabilidade.md`

É gerado na RAIZ do projeto (`projeto_nexabot/rastreabilidade.md`), não
dentro de `aula_16/`, porque é um artefato do projeto inteiro (consumido
pelo CI, `.github/workflows/mbd-ci.yml`), não só desta aula. Ele muda a
cada execução, conforme o estado do repositório no momento — não é mantido
manualmente.

## Honestidade técnica (o ponto central da aula)

DO-178C e ISO 26262 são processos de certificação de PRODUTO e de
FERRAMENTA — não uma propriedade que uma suíte de scripts adquire sozinha.
Este laboratório produz `EVIDÊNCIA` (rastreabilidade, equivalência
numérica, CI reprodutível, detecção de falha) que um processo de
certificação real exigiria como insumo; ele não substitui auditoria
independente nem qualificação formal de ferramenta (gcc, SymPy, Jinja2,
`nexabot/codegen/` incluído). Ver `02_evidencias.py` para o detalhamento
requisito por requisito.
