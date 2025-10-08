# Aula 2: Tipologias Estruturais e Trajetórias de Carga

## Estudo de Caso
Ponte rodoviária de vão médio ($L = 30\,\mathrm{m}$) sobre rio urbano. O projeto deve considerar diferentes tipologias estruturais para otimizar custos e funcionalidade. Analisar as opções: viga de concreto armado, arco, treliça metálica e ponte estaiada, considerando as trajetórias de carga e implicações para o cálculo estrutural.

Dados do projeto:
- Vão principal: $L = 30\,\mathrm{m}$
- Carga permanente: $g = 25\,\mathrm{kN/m}$ (peso próprio + revestimento)
- Carga móvel: $q = 12\,\mathrm{kN/m}$ (NBR 7188)
- Altura livre: $h = 8\,\mathrm{m}$ (navegação fluvial)

### Esquema do caso (SVG)
<img src="./assets/aula2_ponte.svg" alt="Esquema: comparação de tipologias estruturais" width="760" />

Leitura do esquema:
- Comparação entre viga, arco, treliça e estaiada
- Trajetórias de carga indicadas para cada tipologia
- Esforços predominantes em cada elemento
- Conexão com fundações e apoios

## Conceitos principais

### Tipologias Estruturais Fundamentais

**Viga (Sistema Isostático)**
- Comportamento: flexão pura com tração na fibra inferior
- Trajetória: cargas → viga → apoios → fundações
- Esforços predominantes: $M$ (momento fletor) e $V$ (cortante)
- Vantagens: simplicidade construtiva, cálculo direto
- Limitações: vãos limitados ($L < 40\,\mathrm{m}$ para concreto)

**Arco (Sistema Isostático)**
- Comportamento: compressão axial predominante
- Trajetória: cargas → arco → apoios → fundações
- Esforços predominantes: $N$ (normal de compressão)
- Vantagens: eficiência estrutural, vãos maiores
- Limitações: empuxo horizontal nos apoios

**Treliça (Sistema Isostático)**
- Comportamento: barras tracionadas e comprimidas
- Trajetória: cargas → cordas → diagonais → montantes → apoios
- Esforços predominantes: $N$ (normal) em cada barra
- Vantagens: leveza, transparência, vãos grandes
- Limitações: complexidade de ligações, manutenção

**Ponte Estaiada (Sistema Hiperestático)**
- Comportamento: cabo tracionado + mastro comprimido
- Trajetória: cargas → tabuleiro → estais → mastro → fundações
- Esforços predominantes: $T$ (tração nos cabos), $N$ (compressão no mastro)
- Vantagens: vãos muito grandes, estética
- Limitações: complexidade de cálculo, manutenção especializada

### Trajetórias de Carga

**Compressão vs Tração**
- **Compressão**: concreto e aço trabalham bem; eficiência alta
- **Tração**: apenas aço resiste; necessidade de armadura
- **Implicação**: sistemas com predominância de compressão são mais eficientes

**Rigidez Global**
- **Flexão**: rigidez proporcional a $EI$ (módulo × inércia)
- **Axial**: rigidez proporcional a $EA$ (módulo × área)
- **Implicação**: sistemas axiais são mais rígidos para vãos grandes

### Isostaticidade vs Hiperstaticidade

**Sistema Isostático**
- Equações de equilíbrio suficientes para determinar reações
- Cálculo direto: $\sum F = 0$ e $\sum M = 0$
- Exemplos: viga biapoiada, arco de 3 articulações, treliça simples

**Sistema Hiperestático**
- Mais reações que equações de equilíbrio
- Necessita compatibilidade de deslocamentos
- Exemplos: viga contínua, pórtico, ponte estaiada

## Exemplo de cálculo do case

### 1) Análise da Viga de Concreto Armado

**Reações de apoio**:
$$R_A = R_B = \frac{gL + qL}{2} = \frac{25 \times 30 + 12 \times 30}{2} = 555\,\mathrm{kN}$$

**Momento máximo**:
$$M_{\max} = \frac{(g+q)L^2}{8} = \frac{37 \times 900}{8} = 4162{,}5\,\mathrm{kN \cdot m}$$

**Trajetória de carga**: cargas → viga → apoios → fundações
- Esforço predominante: flexão (tração na fibra inferior)
- Necessidade de armadura longitudinal significativa

### 2) Análise do Arco

**Empuxo horizontal** (arco parabólico):
$$H = \frac{(g+q)L^2}{8f} = \frac{37 \times 900}{8 \times 6} = 693{,}75\,\mathrm{kN}$$

Onde $f = 6\,\mathrm{m}$ é a flecha do arco.

**Força normal máxima** (no topo):
$$N_{\max} = H = 693{,}75\,\mathrm{kN}$$

**Trajetória de carga**: cargas → arco → empuxo horizontal → fundações
- Esforço predominante: compressão axial
- Eficiência estrutural alta (concreto trabalha bem à compressão)

### 3) Análise da Treliça

**Força na corda superior** (compressão):
$$N_{\text{corda}} = \frac{M_{\max}}{h_{\text{treliça}}} = \frac{4162{,}5}{4} = 1040{,}6\,\mathrm{kN}$$

Onde $h_{\text{treliça}} = 4\,\mathrm{m}$ é a altura da treliça.

**Força na diagonal** (tração):
$$N_{\text{diagonal}} = \frac{V_{\max}}{\sin \alpha} = \frac{555}{\sin 45°} = 784{,}6\,\mathrm{kN}$$

**Trajetória de carga**: cargas → cordas → diagonais → montantes → apoios
- Esforços: compressão nas cordas superiores, tração nas inferiores
- Eficiência: aproveitamento ótimo do material

### 4) Análise da Ponte Estaiada

**Força no estai** (tração):
$$T_{\text{estai}} = \frac{(g+q)L}{2 \sin \beta} = \frac{37 \times 30}{2 \times \sin 30°} = 1110\,\mathrm{kN}$$

Onde $\beta = 30°$ é o ângulo do estai.

**Força no mastro** (compressão):
$$N_{\text{mastro}} = T_{\text{estai}} \cos \beta = 1110 \times \cos 30° = 961{,}5\,\mathrm{kN}$$

**Trajetória de carga**: cargas → tabuleiro → estais → mastro → fundações
- Esforços: tração nos cabos, compressão no mastro
- Vantagem: vãos muito grandes com eficiência

### 5) Comparação de Eficiência

**Consumo de material** (ordem de grandeza):
- Viga: $100\%$ (referência)
- Arco: $60\%$ (mais eficiente)
- Treliça: $40\%$ (muito eficiente)
- Estaiada: $30\%$ (mais eficiente, mas complexa)

**Implicações para cálculo**:
- **Viga**: cálculo direto por equilíbrio
- **Arco**: considerar empuxo horizontal
- **Treliça**: análise de cada barra individualmente
- **Estaiada**: análise não-linear complexa

## Erros comuns (evite)

- Confundir sistemas isostáticos com hiperestáticos na escolha da tipologia
- Não considerar as trajetórias de carga na definição dos esforços
- Subestimar a complexidade de cálculo de sistemas hiperestáticos
- Ignorar as limitações de vão de cada tipologia estrutural

## Encaminhamentos

- Pratique a identificação de sistemas isostáticos vs hiperestáticos
- Analise as trajetórias de carga em estruturas existentes
- Próxima aula: cargas normativas e combinações (NBR 7188)