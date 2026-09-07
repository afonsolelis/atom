# Notebooks passo a passo

Um notebook por aula, **dentro da pasta da unidade**, na mesma convenção dos
slides:

```
unidade_1/notebooks/aula_01_primeiro_contato.ipynb   ...  aula_04
unidade_2/notebooks/aula_05_malha_fechada.ipynb      ...  aula_08
unidade_3/notebooks/aula_09_requisito_formal.ipynb   ...  aula_12
unidade_4/notebooks/aula_13_geracao_de_codigo.ipynb  ...  aula_16
```

Você abre, roda célula por célula, muda os números e vê o resultado mudar.

Estes notebooks são a resposta a um problema real: a primeira versão desta
disciplina entrava em Kirchhoff, espaço de estados e Laplace sem nunca ter
explicado o que é `rad/s`. Aqui a explicação vem antes, em português, e o
código vem depois.

## Como abrir

No terminal, a partir da pasta da disciplina:

```bash
cd projeto_nexabot
uv venv .venv
uv pip install --python .venv/bin/python -e .
.venv/bin/jupyter lab ..
```

Se o Jupyter abrir e a primeira célula rodar sem erro, está tudo certo.

## Estrutura de todo notebook

| Seção | O que é |
| --- | --- |
| **O que você vai fazer aqui** | O objetivo, em três linhas, sem jargão |
| **Antes de começar** | Os conceitos que a aula usa, explicados do zero |
| **Passo a passo** | Uma célula por ideia, com o texto explicando antes de rodar |
| **Mexa aqui** | Você altera um valor e prevê o que vai acontecer |
| **Aprofundamento** | Opcional — o conteúdo que saiu da videoaula |
| **Se deu erro** | Os erros mais prováveis e o que fazer |

## Os números

Nenhum notebook inventa valor. Todos importam de
`projeto_nexabot/nexabot/params.py`, que é a fonte única de verdade da
disciplina. Se o motor mudar, muda lá e os dezesseis notebooks acompanham.

## Como estes arquivos são gerados

O `.ipynb` é artefato, e ele é gravado na pasta da unidade correspondente. O
que se revisa é o fonte em `tools/notebooks/aula_NN.py`, que declara as células
como texto Python legível — JSON de notebook é impossível de revisar em diff.

```bash
python3 tools/nbkit.py          # reconstrói todos
python3 tools/nbkit.py 3        # só a aula 3
python3 tools/nbkit.py --check  # valida sem escrever
```

O construtor confere que todo código compila, que as seções obrigatórias
existem e que nenhuma célula de código aparece sem um texto explicando antes.
