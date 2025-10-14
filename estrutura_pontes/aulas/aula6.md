# Aula 6: Transversinas e Tabuleiros de Ponte

## Objetivos da Aula

Ao final desta aula, o aluno será capaz de:
- Entender o papel das transversinas na distribuição transversal
- Dimensionar transversinas (M_Ed, V_Ed, A_s) sob cargas típicas
- Verificar o tabuleiro como laje (1D/2D) e punção
- Relacionar escolhas de geometria com desempenho e detalhamento

## Estudo de Caso

Ponte rodoviária com 3 vigas principais ($L = 30\,\mathrm{m}$) e transversinas intermediárias. Dimensionar as transversinas para distribuição transversal de cargas e verificar o tabuleiro como laje em duas direções, incluindo verificação de cisalhamento de punção.

Dados do projeto:

- Vão: $L = 30\,\mathrm{m}$
- Número de vigas: $n = 3$
- Espaçamento entre vigas: $s = 3{,}0\,\mathrm{m}$
- Espessura da laje: $t = 0{,}25\,\mathrm{m}$
- Carga móvel: $q = 5{,}0\,\mathrm{kN/m^2}$

### Esquema do caso

<img src="https://res.cloudinary.com/dyhjjms8y/image/upload/v1760304335/estrutura_pontes/aula6_ponte.svg" alt="Esquema: transversinas e tabuleiro" width="760" />

Leitura do esquema:

- 3 vigas principais com transversinas
- Distribuição transversal de cargas
- Tabuleiro como laje em duas direções
- Verificação de cisalhamento de punção

## Conceitos principais

### Papel das Transversinas

**Função estrutural**:

- Distribuir cargas transversais entre vigas principais
- Rigidizar a estrutura transversalmente
- Reduzir a flexão longitudinal das vigas principais
- Melhorar o comportamento global da ponte

**Comportamento**:

- Flexão transversal (momento $M_y$)
- Cisalhamento transversal (cortante $V_y$)
- Torção (momento $T$)

### Distribuição Transversal de Cargas

**Método simplificado**:
$$R_i = \frac{P}{n} \left(1 + \frac{e \cdot y_i}{\sum y_i^2}\right)$$

Onde:

- $P$ = carga total
- $n$ = número de vigas
- $e$ = excentricidade da carga
- $y_i$ = distância da viga $i$ ao centro de gravidade

**Coeficiente de distribuição**:
$$\eta_i = \frac{R_i}{P/n}$$

### Tabuleiro como Laje em Duas Direções

**Comportamento**:

- Flexão em duas direções ($M_x$ e $M_y$)
- Cisalhamento em duas direções ($V_x$ e $V_y$)
- Torção ($M_{xy}$)

**Métodos de cálculo**:

- Teoria clássica de placas
- Método das faixas
- Análise por elementos finitos

### Cisalhamento de Punção

**Conceito**:

- Tensão de cisalhamento em torno de cargas concentradas
- Verificação em torno de pilares ou cargas pontuais
- Tensão crítica na superfície de punção

**Verificação**:
$$\tau_{Ed} = \frac{V_{Ed}}{u \cdot d} \leq \tau_{Rd}$$

Onde:

- $V_{Ed}$ = força cortante de cálculo
- $u$ = perímetro de punção
- $d$ = altura útil da laje

## Exemplo de cálculo do case

### 1) Distribuição Transversal de Cargas

**Carga por viga (carga distribuída)**:
$$q_{viga} = \frac{q \times s}{n} = \frac{5{,}0 \times 3{,}0}{3} = 5{,}0\,\mathrm{kN/m}$$

**Carga concentrada (TB-450)**:

- Peso total: $P = 450\,\mathrm{kN}$
- Excentricidade: $e = 1{,}5\,\mathrm{m}$ (centro da pista)

**Coeficientes de distribuição**:
$$\eta_1 = \frac{1}{3} \left(1 + \frac{1{,}5 \times (-3{,}0)}{3{,}0^2 + 0^2 + 3{,}0^2}\right) = 0{,}25$$

$$\eta_2 = \frac{1}{3} \left(1 + \frac{1{,}5 \times 0}{3{,}0^2 + 0^2 + 3{,}0^2}\right) = 0{,}33$$

$$\eta_3 = \frac{1}{3} \left(1 + \frac{1{,}5 \times 3{,}0}{3{,}0^2 + 0^2 + 3{,}0^2}\right) = 0{,}42$$

**Cargas nas vigas**:

- Viga 1: $P_1 = 0{,}25 \times 450 = 112{,}5\,\mathrm{kN}$
- Viga 2: $P_2 = 0{,}33 \times 450 = 148{,}5\,\mathrm{kN}$
- Viga 3: $P_3 = 0{,}42 \times 450 = 189{,}0\,\mathrm{kN}$

### 2) Dimensionamento das Transversinas

**Momento na transversina**:
$$M_{Ed} = \frac{q_{trans} \times L_{trans}^2}{8} + \frac{P_{trans} \times L_{trans}}{4}$$

Onde:

- $q_{trans} = 2{,}0\,\mathrm{kN/m}$ (peso próprio)
- $L_{trans} = 9{,}0\,\mathrm{m}$ (comprimento da transversina)
- $P_{trans} = 50{,}0\,\mathrm{kN}$ (carga concentrada)

$$M_{Ed} = \frac{2{,}0 \times 81}{8} + \frac{50{,}0 \times 9{,}0}{4} = 20{,}25 + 112{,}5 = 132{,}75\,\mathrm{kN \cdot m}$$

**Cortante na transversina**:
$$V_{Ed} = \frac{q_{trans} \times L_{trans}}{2} + \frac{P_{trans}}{2} = \frac{2{,}0 \times 9{,}0}{2} + \frac{50{,}0}{2} = 9{,}0 + 25{,}0 = 34{,}0\,\mathrm{kN}$$

**Seção da transversina**:

- $b = 0{,}3\,\mathrm{m}$ (largura)
- $h = 0{,}6\,\mathrm{m}$ (altura)
- $d = 0{,}55\,\mathrm{m}$ (altura útil)

**Armadura de flexão**:
$$A_s = \frac{M_{Ed}}{0{,}9 \times d \times f_{yd}} = \frac{132{,}75}{0{,}9 \times 0{,}55 \times 435} = 0{,}00062\,\mathrm{m^2}$$

$$A_s = 6{,}2\,\mathrm{cm^2}$$

**Armadura mínima**:
$$A_{s,min} = 0{,}15\% \times b \times h = 0{,}0015 \times 0{,}3 \times 0{,}6 = 0{,}00027\,\mathrm{m^2}$$

$$A_{s,min} = 2{,}7\,\mathrm{cm^2} < A_s = 6{,}2\,\mathrm{cm^2}$$

Condição atendida (✓).

### 3) Verificação do Tabuleiro

**Laje em duas direções**:

- $L_x = 3{,}0\,\mathrm{m}$ (direção transversal)
- $L_y = 30{,}0\,\mathrm{m}$ (direção longitudinal)
- Relação: $L_y/L_x = 10{,}0 > 2{,}0$ (laje em uma direção)

**Momento na direção principal**:
$$M_x = \frac{q \times L_x^2}{8} = \frac{5{,}0 \times 9{,}0}{8} = 5{,}625\,\mathrm{kN \cdot m/m}$$

**Momento na direção secundária**:
$$M_y = 0{,}2 \times M_x = 0{,}2 \times 5{,}625 = 1{,}125\,\mathrm{kN \cdot m/m}$$

**Armadura principal**:
$$A_{sx} = \frac{M_x}{0{,}9 \times d \times f_{yd}} = \frac{5{,}625}{0{,}9 \times 0{,}22 \times 435} = 0{,}000065\,\mathrm{m^2/m}$$

$$A_{sx} = 0{,}65\,\mathrm{cm^2/m}$$

**Armadura secundária**:
$$A_{sy} = 0{,}2 \times A_{sx} = 0{,}2 \times 0{,}65 = 0{,}13\,\mathrm{cm^2/m}$$

**Armadura mínima**:
$$A_{s,min} = 0{,}15\% \times 1{,}0 \times 0{,}25 = 0{,}000375\,\mathrm{m^2/m}$$

$$A_{s,min} = 3{,}75\,\mathrm{cm^2/m} > A_{sx} = 0{,}65\,\mathrm{cm^2/m}$$

**Armadura adotada**: $A_{sx} = A_{sy} = 3{,}75\,\mathrm{cm^2/m}$

### 4) Verificação de Cisalhamento de Punção

**Carga concentrada**:
$$P = 450\,\mathrm{kN}$$

**Perímetro de punção**:
$$u = 2\pi r = 2\pi \times 0{,}3 = 1{,}88\,\mathrm{m}$$

Onde $r = 0{,}3\,\mathrm{m}$ é o raio da área de contato.

**Tensão de cisalhamento**:
$$\tau_{Ed} = \frac{P}{u \times d} = \frac{450}{1{,}88 \times 0{,}22} = 1087{,}5\,\mathrm{kPa}$$

**Tensão resistente**:
$$\tau_{Rd} = 0{,}25 f_{ctd} = 0{,}25 \times 2{,}0 = 0{,}5\,\mathrm{MPa}$$

**Verificação**:
$$\tau_{Ed} = 1{,}09\,\mathrm{MPa} > \tau_{Rd} = 0{,}5\,\mathrm{MPa}$$ ✗

**Necessário**: Aumentar a espessura da laje ou usar armadura de punção.

### 5) Armadura de Punção

**Armadura necessária**:
$$A_{sw} = \frac{(\tau_{Ed} - \tau_{Rd}) \times u \times d}{f_{ywd}}$$

$$A_{sw} = \frac{(1{,}09 - 0{,}5) \times 1{,}88 \times 0{,}22}{435} = 0{,}00056\,\mathrm{m^2}$$

$$A_{sw} = 5{,}6\,\mathrm{cm^2}$$

**Distribuição**:

- Estribos: $\phi 8{,}0\,\mathrm{mm}$ c/ $15\,\mathrm{cm}$
- Área: $A_{sw} = 3{,}35\,\mathrm{cm^2/m} \times 1{,}88\,\mathrm{m} = 6{,}3\,\mathrm{cm^2}$ ✓

### 6) Detalhamento

**Transversinas**:

- Armadura longitudinal: $4 \phi 16{,}0\,\mathrm{mm}$
- Estribos: $\phi 6{,}3\,\mathrm{mm}$ c/ $20\,\mathrm{cm}$

**Tabuleiro**:

- Armadura principal: $\phi 8{,}0\,\mathrm{mm}$ c/ $15\,\mathrm{cm}$
- Armadura secundária: $\phi 8{,}0\,\mathrm{mm}$ c/ $15\,\mathrm{cm}$
- Armadura de punção: $\phi 8{,}0\,\mathrm{mm}$ c/ $15\,\mathrm{cm}$
