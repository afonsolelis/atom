# Ambiente e pilha tecnológica

> Guia de instalação e conferência do laboratório da disciplina. As versões abaixo foram **instaladas e exercitadas** durante a produção do material, não copiadas de documentação. Este é também o roteiro que o estudante segue na Aula 1.

## 1. Versões verificadas

| Componente | Versão verificada | Papel na disciplina |
| --- | --- | --- |
| Python | 3.12.3 | Linguagem base |
| `uv` | 0.12.7 | Gerenciador de ambiente e de pacotes |
| NumPy | 2.5.2 | Álgebra numérica |
| SciPy | 1.18.1 | Integração, otimização, processamento de sinais |
| `python-control` | 0.10.2 | Espaço de estados, função de transferência, LQR, discretização |
| SymPy | 1.14.0 | Derivação simbólica do modelo e da equação de diferenças |
| Matplotlib | 3.11.1 | Figuras |
| Jinja2 | 3.1.6 | Templates de geração de código C |
| Hypothesis | 6.165.10 | Testes baseados em propriedades e em modelo |
| pytest | 9.1.1 | Execução da suíte de testes |
| coverage | 7.16.0 | Cobertura |
| FMPy | 0.3.31 | Carga e execução de FMUs FMI |
| pySerial | 3.5 | Ponte HIL com o alvo embarcado |
| GCC | 13.3.0 | Compilação do código gerado e do FMU |

## 2. Instalação em cinco comandos

O `uv` substitui `pip`, `venv` e `virtualenv`, resolve dependências em segundos e é o padrão de fato do ecossistema Python em 2026. Ele é o primeiro comando da Aula 1.

```bash
# 1. Instalar o uv (Linux e macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Entrar no projeto
cd projeto_nexabot

# 3. Criar o ambiente virtual
uv venv .venv

# 4. Instalar a pilha
uv pip install --python .venv/bin/python \
    numpy scipy matplotlib sympy control \
    jinja2 hypothesis pytest coverage fmpy pyserial

# 5. Conferir o ambiente
.venv/bin/python aula_01/01_ambiente.py
```

No Windows, o interpretador do ambiente é `.venv\Scripts\python.exe` e o instalador do `uv` é
`powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`.

O script `aula_01/01_ambiente.py` imprime um relatório de prontidão item a item. **Nenhuma aula deve ser gravada com esse relatório apontando pendência.**

## 3. Ferramentas externas (opcionais, apresentadas como contraparte industrial)

Estas ferramentas ampliam a disciplina, mas **nenhum laboratório obrigatório depende delas**. O caminho canônico de cada aula roda apenas com a pilha da seção 1 mais o GCC.

| Ferramenta | Aula | Instalação | Papel |
| --- | --- | --- | --- |
| OpenModelica | 8 | <https://openmodelica.org/download/> | Modelagem física em Modelica e exportação de FMU pela interface gráfica |
| NuSMV | 10 | <https://nusmv.fbk.eu/> | *Model checking* LTL/CTL industrial |
| UPPAAL | 11 | <https://uppaal.org/> (licença acadêmica gratuita) | Autômatos temporizados com interface gráfica |
| PlatformIO | 15 | `uv tool install platformio` ou extensão do VS Code | Compilação e gravação do firmware ESP32 |

**Por que existe um caminho sem elas.** Um estudante EAD que não consegue instalar uma ferramenta não pode ficar sem a aula. Por isso a disciplina implementa, em Python, um verificador de estados explícitos, um verificador de autômato temporizado de tempo discreto e um alvo HIL em *loopback*. O estudante vê o mecanismo funcionando e depois conhece a ferramenta industrial que faz o mesmo em escala.

## 4. Hardware opcional da Aula 15

| Item | Especificação | Custo aproximado |
| --- | --- | --- |
| Placa | ESP32-DevKitC (ou equivalente com ESP32-WROOM-32) | Baixo |
| Cabo | USB-C ou micro-USB de dados | — |

Sem a placa, a Aula 15 roda integralmente com o back-end de *loopback*: o controlador C compilado executa como processo separado e conversa com a planta em Python pelo mesmo protocolo de linha usado com a placa real. A troca entre os dois back-ends é uma linha de configuração.

## 5. Estrutura do laboratório

```
projeto_nexabot/
├── .venv/                       ambiente virtual (não versionado)
├── pyproject.toml               dependências fixadas
├── nexabot/                     pacote de biblioteca
│   ├── params.py                parâmetros identificados (fonte única de verdade)
│   ├── plant.py                 planta em espaço de estados e integrador RK4
│   ├── controllers.py           PID contínuo e discreto, alocação de polos, LQR
│   ├── identificacao.py         identificação de parâmetros por mínimos quadrados
│   ├── viz.py                   tabelas e gráficos ASCII para gravação de tela
│   ├── cosim.py                 mestre de co-simulação FMI
│   ├── fmu/                     FMU FMI 3.0 da planta, em C
│   ├── supervisor.py            máquina de estados de segurança
│   ├── requisitos.py            propriedades formais verificáveis
│   ├── modelcheck.py            verificador de estados explícitos
│   ├── timed.py                 autômato temporizado e watchdog
│   ├── mbt.py                   geração de testes a partir do modelo
│   ├── codegen/                 SymPy + Jinja2 -> C
│   ├── sil.py                   ponte SIL por ctypes
│   ├── hil.py                   ponte HIL (loopback e serial)
│   ├── firmware/                programa do alvo e projeto PlatformIO
│   └── rastreabilidade.py       matriz requisito -> modelo -> código -> teste
├── aula_01/ … aula_16/          laboratório por aula, scripts numerados
├── tests/                       suíte pytest
├── data/                        dados de ensaio
└── figuras/                     PNGs gerados
```

## 6. Convenção dos laboratórios

Cada diretório `aula_NN/` contém scripts numerados na ordem exata de execução durante a gravação, e um `README.md` com os comandos e a saída esperada. O último script de cada aula é sempre `NN_desafio.py`: um esqueleto com enunciado e critério de aceitação, para o estudante completar.

Os scripts imprimem em tabela ASCII e desenham gráficos no próprio terminal. Isso é deliberado: em captura de tela, uma janela do Matplotlib que abre por cima do terminal quebra o ritmo da aula. As figuras PNG são geradas em paralelo, em `figuras/`, para uso no material escrito e nos slides.

## 7. Conferência antes de gravar

```bash
cd projeto_nexabot
.venv/bin/python aula_01/01_ambiente.py     # relatório de prontidão
.venv/bin/python -m pytest -q                # suíte completa
```

Ambos precisam terminar sem falha. Em seguida, execute uma vez todos os scripts da aula que será gravada, conferindo a saída contra o `README.md` daquele diretório.
