# Aula 15: Reforços Estruturais e Verificações de Estabilidade

## Estudo de Caso
Ponte rodoviária de 30 anos com necessidade de reforço estrutural. Analisar as opções de reforço à flexão (aço adicional, laminados) e ao cisalhamento, incluindo protensão externa e verificação de estabilidade global.

Dados do projeto:
- Idade: 30 anos
- Vão: $L = 35\,\mathrm{m}$
- Seção: retangular $b \times h = 0{,}6 \times 2{,}0\,\mathrm{m}$
- Capacidade atual: $M_{Rd} = 800{,}0\,\mathrm{kN \cdot m}$
- Momento necessário: $M_{Ed} = 1200{,}0\,\mathrm{kN \cdot m}$
- Deficiência: $M_{def} = 400{,}0\,\mathrm{kN \cdot m}$

### Esquema do caso (SVG)
<img src="./assets/aula15_ponte.svg" alt="Esquema: reforços estruturais" width="760" />

Leitura do esquema:
- Reforço à flexão com aço adicional
- Reforço ao cisalhamento com estribos
- Protensão externa
- Verificação de estabilidade

## Conceitos principais

### Reforço à Flexão

**Aço adicional**:
- Armadura longitudinal adicional
- Aplicação: face tracionada
- Vantagens: simplicidade, baixo custo
- Limitações: redução do cobrimento

**Laminados de aço**:
- Chapa de aço colada
- Aplicação: face tracionada
- Vantagens: alta resistência, baixo peso
- Limitações: complexidade de aplicação

**Protensão externa**:
- Cabos externos tensionados
- Aplicação: face tracionada
- Vantagens: alta eficiência, reversibilidade
- Limitações: complexidade, manutenção

### Reforço ao Cisalhamento

**Estribos adicionais**:
- Armadura transversal adicional
- Aplicação: alma da viga
- Vantagens: simplicidade, eficiência
- Limitações: redução da seção

**Chapa de aço**:
- Chapa colada na alma
- Aplicação: face lateral
- Vantagens: alta resistência
- Limitações: complexidade de aplicação

**Protensão externa**:
- Cabos inclinados
- Aplicação: alma da viga
- Vantagens: alta eficiência
- Limitações: complexidade

### Estabilidade Global

**Prevenção de colapso progressivo**:
- Redundância estrutural
- Caminhos alternativos de carga
- Verificação de estabilidade
- Monitoramento estrutural

**Sequência de intervenção**:
1. Análise da estrutura existente
2. Identificação das deficiências
3. Projeto do reforço
4. Execução do reforço
5. Verificação pós-reforço

## Exemplo de cálculo do case

### 1) Análise da Estrutura Existente

**Capacidade atual**:
$$M_{Rd,0} = 800{,}0\,\mathrm{kN \cdot m}$$

**Momento necessário**:
$$M_{Ed} = 1200{,}0\,\mathrm{kN \cdot m}$$

**Deficiência**:
$$M_{def} = M_{Ed} - M_{Rd,0} = 1200{,}0 - 800{,}0 = 400{,}0\,\mathrm{kN \cdot m}$$

**Percentual de deficiência**:
$$\eta = \frac{M_{def}}{M_{Ed}} = \frac{400{,}0}{1200{,}0} = 33{,}3\%$$

### 2) Reforço à Flexão com Aço Adicional

**Área de armadura adicional**:
$$A_{s,ref} = \frac{M_{def}}{f_{yd} (d - 0{,}4x)} = \frac{400{,}0}{435 \times (1{,}80 - 0{,}4 \times 0{,}30)} = \frac{400{,}0}{435 \times 1{,}68} = 0{,}547\,\mathrm{m^2}$$

$$A_{s,ref} = 547{,}0\,\mathrm{cm^2}$$

**Número de barras**:
$$n = \frac{A_{s,ref}}{A_{barra}} = \frac{547{,}0}{\pi \times 2{,}5^2/4} = \frac{547{,}0}{4{,}91} = 111{,}4 \approx 112 \text{ barras}$$

**Distribuição**:
- Camada 1: 56 barras $\phi 25{,}0\,\mathrm{mm}$
- Camada 2: 56 barras $\phi 25{,}0\,\mathrm{mm}$

### 3) Reforço com Laminados de Aço

**Área de chapa necessária**:
$$A_{chapa} = \frac{M_{def}}{f_{yd,chapa} (d - 0{,}4x)} = \frac{400{,}0}{300 \times (1{,}80 - 0{,}4 \times 0{,}30)} = \frac{400{,}0}{300 \times 1{,}68} = 0{,}794\,\mathrm{m^2}$$

$$A_{chapa} = 794{,}0\,\mathrm{cm^2}$$

**Dimensões da chapa**:
- Largura: $b_{chapa} = 0{,}6\,\mathrm{m}$
- Comprimento: $L_{chapa} = 35{,}0\,\mathrm{m}$
- Espessura: $t_{chapa} = \frac{794{,}0}{60 \times 3500} = 0{,}0038\,\mathrm{m} = 3{,}8\,\mathrm{mm}$

### 4) Reforço com Protensão Externa

**Força de protensão necessária**:
$$P_{ref} = \frac{M_{def}}{e_{ref}} = \frac{400{,}0}{1{,}5} = 266{,}7\,\mathrm{kN}$$

Onde $e_{ref} = 1{,}5\,\mathrm{m}$ é a excentricidade do cabo.

**Área de cabo necessária**:
$$A_{p,ref} = \frac{P_{ref}}{f_{ptk}} = \frac{266{,}7}{1900} = 0{,}140\,\mathrm{m^2}$$

$$A_{p,ref} = 140{,}0\,\mathrm{cm^2}$$

**Número de cordoalhas**:
$$n_{cordoalhas} = \frac{A_{p,ref}}{A_{cordoalha}} = \frac{140{,}0}{1{,}0} = 140 \text{ cordoalhas}$$

### 5) Reforço ao Cisalhamento

**Cortante atual**:
$$V_{Rd,0} = 200{,}0\,\mathrm{kN}$$

**Cortante necessário**:
$$V_{Ed} = 300{,}0\,\mathrm{kN}$$

**Deficiência de cisalhamento**:
$$V_{def} = V_{Ed} - V_{Rd,0} = 300{,}0 - 200{,}0 = 100{,}0\,\mathrm{kN}$$

**Armadura adicional**:
$$A_{sw,ref} = \frac{V_{def}}{0{,}9 \times d \times f_{ywd}} \times s = \frac{100{,}0}{0{,}9 \times 1{,}80 \times 435} \times 0{,}20 = 0{,}028\,\mathrm{m^2/m}$$

$$A_{sw,ref} = 2{,}8\,\mathrm{cm^2/m}$$

**Estribos adicionais**:
- $\phi 8{,}0\,\mathrm{mm}$ c/ $15\,\mathrm{cm}$

### 6) Verificação de Estabilidade Global

**Momento de instabilidade**:
$$M_{inst} = \frac{\pi^2 EI}{L^2} = \frac{\pi^2 \times 30000 \times 0{,}4}{35^2} = \frac{118{,}3 \times 12000}{1225} = 1158{,}4\,\mathrm{kN \cdot m}$$

**Momento de cálculo**:
$$M_{Ed} = 1200{,}0\,\mathrm{kN \cdot m}$$

**Verificação**:
$$M_{Ed} = 1200{,}0\,\mathrm{kN \cdot m} < M_{inst} = 1158{,}4\,\mathrm{kN \cdot m}$$ ✗

**Necessário**: Aumentar a rigidez ou reduzir o vão efetivo.

### 7) Prevenção de Colapso Progressivo

**Redundância estrutural**:
- Múltiplos caminhos de carga
- Apoios redundantes
- Elementos de reserva
- Monitoramento contínuo

**Caminhos alternativos**:
- Carga → viga principal → apoios
- Carga → transversinas → vigas laterais
- Carga → tabuleiro → vigas principais

**Verificação de estabilidade**:
$$\gamma_{est} = \frac{M_{inst}}{M_{Ed}} = \frac{1158{,}4}{1200{,}0} = 0{,}97 < 1{,}0$$ ✗

### 8) Sequência de Intervenção

**Fase 1: Análise**:
- Inspeção estrutural
- Ensaios de materiais
- Análise de capacidade
- Identificação de deficiências

**Fase 2: Projeto**:
- Dimensionamento do reforço
- Verificação de estabilidade
- Detalhamento construtivo
- Especificações técnicas

**Fase 3: Execução**:
- Preparação da estrutura
- Aplicação do reforço
- Controle de qualidade
- Verificação de execução

**Fase 4: Verificação**:
- Ensaios de carga
- Verificação de capacidade
- Monitoramento estrutural
- Relatório final

### 9) Checklist de Verificação Pós-Reforço

**Verificações estruturais**:
- Capacidade à flexão: $M_{Rd} \geq M_{Ed}$ ✓
- Capacidade ao cisalhamento: $V_{Rd} \geq V_{Ed}$ ✓
- Estabilidade global: $\gamma_{est} \geq 1{,}0$ ✗
- Fissuração: $w_k \leq w_{lim}$ ✓

**Verificações de durabilidade**:
- Proteção contra corrosão ✓
- Drenagem adequada ✓
- Impermeabilização ✓
- Monitoramento ✓

**Verificações de execução**:
- Qualidade dos materiais ✓
- Posicionamento das armaduras ✓
- Aderência do reforço ✓
- Controle de qualidade ✓

### 10) Monitoramento Pós-Reforço

**Parâmetros a monitorar**:
- Deformações da estrutura
- Abertura de fissuras
- Corrosão da armadura
- Capacidade resistente

**Frequência de monitoramento**:
- Inspeção visual: mensal
- Medição de deformações: trimestral
- Ensaios de corrosão: semestral
- Verificação de capacidade: anual

## Erros comuns (evite)

- Não verificar a estabilidade global
- Ignorar a sequência de intervenção
- Não considerar o monitoramento pós-reforço
- Subestimar a complexidade da execução

## Encaminhamentos

- Pratique o dimensionamento de diferentes tipos de reforço
- Analise os efeitos na estabilidade global
- Próxima aula: estudo de caso nacional sobre inspeção, deterioração e reforço