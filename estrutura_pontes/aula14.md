# Aula 14: Interação Solo-Estrutura e Recalques

## Estudo de Caso
Ponte rodoviária contínua de 3 vãos ($L = 25\,\mathrm{m}$ cada) com recalques diferenciais nos apoios. Analisar os efeitos dos recalques na estrutura, incluindo esforços adicionais, deslocamentos e verificação de segurança.

Dados do projeto:
- Vãos: $L_1 = L_2 = L_3 = 25\,\mathrm{m}$
- Recalque total: $\delta_1 = 20\,\mathrm{mm}$, $\delta_2 = 10\,\mathrm{mm}$, $\delta_3 = 15\,\mathrm{mm}$
- Recalque diferencial: $\Delta\delta = 10\,\mathrm{mm}$
- Rigidez da viga: $EI = 50000\,\mathrm{kN \cdot m^2}$

### Esquema do caso (SVG)
<img src="./assets/aula14_ponte.svg" alt="Esquema: recalques e efeitos na estrutura" width="760" />

Leitura do esquema:
- Ponte contínua com recalques
- Efeitos nos esforços e deslocamentos
- Verificação de segurança
- Sinais nos aparelhos de apoio

## Conceitos principais

### Recalque Total vs Diferencial

**Recalque total**:
- Deslocamento vertical de um apoio
- Efeito: deslocamento global da estrutura
- Consideração: em análises de flechas

**Recalque diferencial**:
- Diferença entre recalques de apoios adjacentes
- Efeito: esforços adicionais na estrutura
- Consideração: em análises de esforços

### Efeitos em Vigas Contínuas

**Esforços adicionais**:
- Momentos fletores adicionais
- Cortantes adicionais
- Reações de apoio modificadas

**Deslocamentos adicionais**:
- Flechas adicionais
- Rotações adicionais
- Deslocamentos horizontais

### Sinais em Aparelhos de Apoio

**Deslocamentos horizontais**:
- Dilatação térmica
- Retração do concreto
- Cargas móveis
- Recalques diferenciais

**Rotações**:
- Flexão da viga
- Recalques diferenciais
- Cargas assimétricas
- Variações de temperatura

## Exemplo de cálculo do case

### 1) Análise dos Recalques

**Recalques dos apoios**:
- Apoio 1: $\delta_1 = 20{,}0\,\mathrm{mm}$
- Apoio 2: $\delta_2 = 10{,}0\,\mathrm{mm}$
- Apoio 3: $\delta_3 = 15{,}0\,\mathrm{mm}$
- Apoio 4: $\delta_4 = 0{,}0\,\mathrm{mm}$ (referência)

**Recalques diferenciais**:
- $\Delta\delta_{12} = \delta_1 - \delta_2 = 20{,}0 - 10{,}0 = 10{,}0\,\mathrm{mm}$
- $\Delta\delta_{23} = \delta_2 - \delta_3 = 10{,}0 - 15{,}0 = -5{,}0\,\mathrm{mm}$
- $\Delta\delta_{34} = \delta_3 - \delta_4 = 15{,}0 - 0{,}0 = 15{,}0\,\mathrm{mm}$

### 2) Cálculo dos Esforços Adicionais

**Método dos deslocamentos**:
$$M_{ij} = \frac{2EI}{L} \left(2\theta_i + \theta_j - \frac{3\Delta}{L}\right)$$

Onde:
- $\theta_i, \theta_j$ = rotações nos nós
- $\Delta$ = deslocamento relativo
- $L$ = comprimento do elemento

**Para o vão 1-2**:
$$M_{12} = \frac{2 \times 50000}{25} \left(2\theta_1 + \theta_2 - \frac{3 \times 0{,}010}{25}\right)$$

$$M_{12} = 4000 \left(2\theta_1 + \theta_2 - 0{,}0012\right)$$

**Para o vão 2-3**:
$$M_{23} = \frac{2 \times 50000}{25} \left(2\theta_2 + \theta_3 - \frac{3 \times (-0{,}005)}{25}\right)$$

$$M_{23} = 4000 \left(2\theta_2 + \theta_3 + 0{,}0006\right)$$

**Para o vão 3-4**:
$$M_{34} = \frac{2 \times 50000}{25} \left(2\theta_3 + \theta_4 - \frac{3 \times 0{,}015}{25}\right)$$

$$M_{34} = 4000 \left(2\theta_3 + \theta_4 - 0{,}0018\right)$$

### 3) Equações de Equilíbrio

**Nó 2**:
$$M_{21} + M_{23} = 0$$

$$4000 \left(2\theta_2 + \theta_1 - 0{,}0012\right) + 4000 \left(2\theta_2 + \theta_3 + 0{,}0006\right) = 0$$

$$4\theta_2 + \theta_1 + \theta_3 - 0{,}0006 = 0$$

**Nó 3**:
$$M_{32} + M_{34} = 0$$

$$4000 \left(2\theta_3 + \theta_2 + 0{,}0006\right) + 4000 \left(2\theta_3 + \theta_4 - 0{,}0018\right) = 0$$

$$4\theta_3 + \theta_2 + \theta_4 - 0{,}0012 = 0$$

### 4) Solução do Sistema

**Condições de contorno**:
- $\theta_1 = 0$ (apoio fixo)
- $\theta_4 = 0$ (apoio fixo)

**Sistema de equações**:
$$4\theta_2 + \theta_3 - 0{,}0006 = 0$$
$$4\theta_3 + \theta_2 - 0{,}0012 = 0$$

**Solução**:
$$\theta_2 = 0{,}0002\,\mathrm{rad}$$
$$\theta_3 = 0{,}0004\,\mathrm{rad}$$

### 5) Cálculo dos Momentos

**Momento no vão 1-2**:
$$M_{12} = 4000 \left(2 \times 0 + 0{,}0002 - 0{,}0012\right) = 4000 \times (-0{,}001) = -4{,}0\,\mathrm{kN \cdot m}$$

**Momento no vão 2-3**:
$$M_{23} = 4000 \left(2 \times 0{,}0002 + 0{,}0004 + 0{,}0006\right) = 4000 \times 0{,}0014 = 5{,}6\,\mathrm{kN \cdot m}$$

**Momento no vão 3-4**:
$$M_{34} = 4000 \left(2 \times 0{,}0004 + 0 - 0{,}0018\right) = 4000 \times (-0{,}001) = -4{,}0\,\mathrm{kN \cdot m}$$

### 6) Cálculo das Reações

**Reação no apoio 1**:
$$R_1 = \frac{M_{12}}{L} = \frac{-4{,}0}{25} = -0{,}16\,\mathrm{kN}$$

**Reação no apoio 2**:
$$R_2 = \frac{M_{21} - M_{23}}{L} = \frac{4{,}0 - 5{,}6}{25} = -0{,}064\,\mathrm{kN}$$

**Reação no apoio 3**:
$$R_3 = \frac{M_{32} - M_{34}}{L} = \frac{-5{,}6 - (-4{,}0)}{25} = -0{,}064\,\mathrm{kN}$$

**Reação no apoio 4**:
$$R_4 = \frac{M_{43}}{L} = \frac{4{,}0}{25} = 0{,}16\,\mathrm{kN}$$

### 7) Verificação de Segurança

**Momento máximo adicional**:
$$M_{\max} = 5{,}6\,\mathrm{kN \cdot m}$$

**Momento de serviço**:
$$M_{ser} = \frac{qL^2}{8} = \frac{5{,}0 \times 25^2}{8} = 390{,}6\,\mathrm{kN \cdot m}$$

**Momento total**:
$$M_{total} = M_{ser} + M_{\max} = 390{,}6 + 5{,}6 = 396{,}2\,\mathrm{kN \cdot m}$$

**Verificação**:
$$M_{total} = 396{,}2\,\mathrm{kN \cdot m} < M_{Rd} = 500{,}0\,\mathrm{kN \cdot m}$$ ✓

### 8) Análise de Deslocamentos

**Flecha adicional no vão 2-3**:
$$a_{adic} = \frac{L^2}{16EI} \left(M_{23} - M_{32}\right) = \frac{25^2}{16 \times 50000} \left(5{,}6 - (-5{,}6)\right)$$

$$a_{adic} = \frac{625}{800000} \times 11{,}2 = 0{,}000781 \times 11{,}2 = 0{,}00875\,\mathrm{m} = 8{,}75\,\mathrm{mm}$$

**Flecha total**:
$$a_{total} = a_{est} + a_{adic} = 15{,}0 + 8{,}75 = 23{,}75\,\mathrm{mm}$$

**Verificação**:
$$a_{total} = 23{,}75\,\mathrm{mm} < a_{lim} = \frac{L}{250} = \frac{25000}{250} = 100{,}0\,\mathrm{mm}$$ ✓

### 9) Sinais nos Aparelhos de Apoio

**Deslocamento horizontal**:
$$\Delta H = \alpha \Delta T \times L = 10^{-5} \times 30 \times 25 = 0{,}0075\,\mathrm{m} = 7{,}5\,\mathrm{mm}$$

**Rotação**:
$$\theta = \frac{\Delta\delta}{L} = \frac{0{,}010}{25} = 0{,}0004\,\mathrm{rad} = 0{,}023°$$

**Força horizontal**:
$$H = K_h \times \Delta H = 5000 \times 0{,}0075 = 37{,}5\,\mathrm{kN}$$

**Momento**:
$$M = K_r \times \theta = 10000 \times 0{,}0004 = 4{,}0\,\mathrm{kN \cdot m}$$

### 10) Critério Prático para Limitar Efeitos

**Recalque diferencial máximo**:
$$\Delta\delta_{max} = \frac{L}{500} = \frac{25000}{500} = 50{,}0\,\mathrm{mm}$$

**Verificação**:
$$\Delta\delta_{max} = 50{,}0\,\mathrm{mm} > \Delta\delta_{real} = 15{,}0\,\mathrm{mm}$$ ✓

**Flecha adicional máxima**:
$$a_{adic,max} = \frac{L}{1000} = \frac{25000}{1000} = 25{,}0\,\mathrm{mm}$$

**Verificação**:
$$a_{adic} = 8{,}75\,\mathrm{mm} < a_{adic,max} = 25{,}0\,\mathrm{mm}$$ ✓

## Erros comuns (evite)

- Ignorar os efeitos dos recalques diferenciais
- Não considerar os esforços adicionais
- Subestimar a importância dos sinais nos apoios
- Não verificar os limites práticos

## Encaminhamentos

- Pratique a análise para diferentes configurações de recalques
- Analise os efeitos em estruturas hiperestáticas
- Próxima aula: reforços estruturais e verificações de estabilidade