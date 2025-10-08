# Roteiro das Aulas - Estrutura de Pontes

## Aula 1: Esforços Internos e Equilíbrio
- Esforços fundamentais: N (normal), V (cortante), M (momento)
- Relações diferenciais: dM/dx = V, dV/dx = -q(x)
- Estudo de caso: viga simplesmente apoiada L=6m com q=30kN/m e P=30kN
- Cálculo de reações, diagramas V(x) e M(x)
- Valores máximos: M_max=180kN·m, V_max=105kN

## Aula 2: Tipologias Estruturais
- Comparação: viga, arco, treliça, ponte estaiada
- Eficiência estrutural e consumo de material
- Trajetórias de carga em diferentes sistemas
- Esforços predominantes em cada tipologia

## Aula 3: Cargas Permanentes e Móveis
- Cargas permanentes (G): peso próprio, revestimento, guarda-corpo
- Cargas móveis (Q): TB-450, fator dinâmico φ=1,26
- Combinações: ELU (F_d=1,4G+1,4φQ) e ELS (F_ser=G+ψ₁φQ)
- Aplicação NBR 7188:2022

## Aula 4: Estudo de Caso - Fadiga
- Comparação normas 1987 vs 2014
- Análise de ciclos: 37,23×10⁶ ciclos em 34 anos
- Margem de segurança: MS=0,65 (35% sobrecarga)
- Conclusão: necessidade de reforço estrutural

## Aula 5: Dimensionamento de Vigas
- Cálculo de esforços: M_Ed=9883kN·m, V_Ed=1601kN
- Armadura longitudinal: A_s=178cm² (20φ32mm)
- Armadura transversal: φ8mm c/20cm
- Verificação de flechas: a_f > a_lim (necessário aumento de altura)

## Aula 6: Transversinas e Tabuleiros
- Distribuição transversal de cargas (η₁=0,25, η₂=0,33, η₃=0,42)
- Dimensionamento de transversinas: M_Ed=133kN·m, A_s=6,2cm²
- Verificação de tabuleiro: laje em duas direções
- Cisalhamento de punção: τ_Ed > τ_Rd (necessário aumento de espessura)

## Aula 7: Concreto Protendido
- Força de protensão: P₀=7778kN, perdas imediatas e diferidas
- Verificação de tensões: σ_topo=10,06MPa < 21MPa, σ_base=-1,31MPa > -3MPa
- Otimização: P_min=7778kN, P_max=13260kN
- Detalhamento: 41 cordoalhas φ12,7mm

## Aula 8: Estudo de Caso - Acidentes
- Análise de 47 acidentes (1980-2007): 23 mortes, 156 feridos
- Causas: 32% projeto, 28% execução, 25% manutenção, 15% uso
- Modos de falha: 40% vigas, 30% apoios, 20% fundações, 10% tabuleiros
- Recomendações: verificações ELU/ELS, controle de qualidade

## Aula 9: Ações Dinâmicas
- Fator dinâmico: φ=1,4-0,007×L (L=25m → φ=1,225)
- Posicionamento crítico: M_max no centro, V_max no apoio
- Efeitos de ressonância: f₁=3,5Hz, v_cr=339km/h
- Verificação de conforto: a_max=0,39m/s² < 0,5m/s²

## Aula 10: Vibrações e Frequência Natural
- Frequência natural: f₁=3,14Hz (fórmula aproximada)
- Amortecimento: ξ=2%, frequência amortecida ≈ f₁
- Verificação de ressonância: f_exc/f₁=0,25 < 0,5
- Critérios: 3Hz ≤ f₁ ≤ 10Hz

## Aula 11: Patologias Estruturais
- Fissuras: flexão (paralelas), cisalhamento (45°), retração
- Corrosão: carbonatação, cloretos, galvânica
- Delaminação: separação entre camadas
- Efeitos: redução de 35% na capacidade resistente

## Aula 12: Estudo de Caso - Patologias (BR-423/AL)
- Patologias após 20 anos: 25% corrosão, 35% delaminação
- Análise quantitativa: A_s,ef=92cm², M_Rd,ef=528kN·m
- Problemas de drenagem: 80% dos pontos obstruídos
- Ambiente agressivo: marinho, alta umidade

## Aula 13: Fundações e Apoios
- Transmissão de cargas: viga → apoio → pilar → bloco → estacas
- Dimensionamento: R_max=1200kN, n=4 estacas φ0,4m
- Verificação de tensões: σ=325kPa < 400kPa
- Estabilidade: γ=10,8 > 2,0

## Aula 14: Interação Solo-Estrutura
- Recalques diferenciais: Δδ_max=15mm
- Momentos adicionais: M_adic=5,6kN·m
- Flechas adicionais: a_adic=8,75mm
- Critério: Δδ_max < L/500=50mm

## Aula 15: Reforços Estruturais
- Deficiência: M_def=400kN·m (33% sobrecarga)
- Reforço à flexão: A_s,ref=547cm²
- Reforço ao cisalhamento: A_sw,ref=2,8cm²/m
- Protensão externa: P_ref=267kN

## Aula 16: Estudo de Caso - Inspeção e Reforço
- Patologias após 40 anos: 30% corrosão, 40% delaminação
- Reforço: protensão externa (P_ref=500kN), estacas adicionais
- Verificações pós-intervenção: M_Rd=1500kN·m ≥ M_Ed
- Programa de monitoramento: inspeção semestral
