# Análise dos materiais recebidos

> Verificação documental executada antes do início da produção. Registra o que foi recebido, o que está íntegro, o que **não** foi recebido e quais decisões precisaram ser tomadas na ausência de instrução formal. Toda decisão adotada aqui é provisória até ratificação da coordenação.

## 1. Inventário e integridade

| Arquivo | Tipo | Tamanho | SHA-256 (prefixo) | Integridade |
| --- | --- | --- | --- | --- |
| `MODEL_BASED_DESIGN_FOR_CYBER_PHYSICAL_SYSTEMS.docx` | Ementa oficial | 169.117 bytes | `be6eadc932d2ee9b…` | Íntegro — ZIP OOXML válido, 13 partes, sem erro de CRC |
| `orientacoes_gravacao_EAD.pdf` | Diretrizes de gravação do Núcleo | 152.594 bytes | `049dcf383862cdbc…` | Íntegro — 2 páginas A4, PDF marcado (*tagged*), sem criptografia |
| `direcionamentos.md` | E-mail de encaminhamento transcrito | 1.055 bytes | `18348094144ed950…` | Íntegro |

**Detalhes da ementa (DOCX).** 63 parágrafos, nenhuma tabela, nenhuma imagem no corpo do documento; duas imagens (`image1.png`, `image2.png`) referenciadas apenas pelo cabeçalho, correspondentes à identidade institucional. O cabeçalho carrega um identificador numérico institucional. O documento **não** contém instruções internas de preenchimento, caixas de exemplo nem marcadores de gabarito — ou seja, é uma ementa acabada, não um modelo a preencher.

**Detalhes das diretrizes (PDF).** Produzido em Microsoft Word LTSC, criado e modificado em 21 de maio de 2026, duas páginas, conteúdo textual integralmente extraível.

**Conclusão da verificação de integridade:** os três documentos recebidos estão corretos, legíveis e consistentes entre si. Nenhum arquivo corrompido, truncado ou protegido.

## 2. O que a ementa oficial efetivamente determina

A ementa fixa, de forma clara e sem ambiguidade:

- ementa descritiva da disciplina;
- objetivo geral e cinco objetivos específicos;
- uma competência central, seis habilidades e cinco atitudes;
- um roteiro de aprendizagem em **quatro blocos temáticos**, cada um com **quatro tópicos**;
- cinco tecnologias sugeridas;
- três referências básicas e cinco complementares.

## 3. O que **não** foi recebido — lacunas documentais

Esta é a diferença mais relevante em relação à disciplina irmã `distributed_systems_engineering`, que recebeu 34 arquivos institucionais. Aqui **não foram fornecidos**:

| Item ausente | Consequência | Decisão adotada |
| --- | --- | --- |
| Modelo (TEMPLATE) de unidade em DOCX | Não há caixas institucionais a preencher | **Resolvido:** localizados os modelos oficiais do Núcleo em `data_engineering_and_pipelines/tools/_templates_pristine/` e adotados (ver seção 3.1) |
| Modelo de questionário por unidade | Quantidade e tipologia das questões não informadas | **Resolvido:** o modelo oficial determina 40 questões; adotadas 40 por unidade (20 asserção-razão + 20 interpretação) |
| Modelo de avaliação final | Formato não informado | **Resolvido:** adotado o modelo oficial "Avaliação final (10 discursivas)", que coincide com o formato desta disciplina |
| Modelo de entrega de trabalho | Formato do PBL não informado | **Resolvido:** adotado o modelo oficial "TEMPLATE ENTREGA DE TRABALHO", com as caixas TÍTULO, DESAFIO, FONTE DE PESQUISA, ENTREGÁVEL e SOLUÇÃO |
| Modelo de slides (PPTX) | Padrão visual dos decks não informado | Adotado o deck HTML autocontido do repositório, com identidade UniFECAF |
| Guia "Como Fazer um Bom Vídeo" | Não recebido nesta disciplina | Usadas as diretrizes do PDF do Núcleo |
| Fichas de validação | Não recebidas | Não produzidas |
| Número de unidades e de videoaulas | **Não informado em nenhum documento** | Inferido: 4 unidades × 4 videoaulas = 16, a partir dos quatro blocos de quatro tópicos do roteiro de aprendizagem |
| Carga horária da disciplina | Não informada | Não declarada no material |
| Prazo de entrega | Não informado | A confirmar com a coordenação; ver `CRONOGRAMA.md` |

### 3.1 Modelos institucionais localizados e adotados

Os modelos oficiais **não vieram no pacote desta disciplina**, mas foram localizados no próprio repositório, preservados em `disciplinas/data_engineering_and_pipelines/tools/_templates_pristine/`. São da mesma variante e do mesmo Núcleo das Engenharias e Tecnologia, e o conjunto está completo:

- `TEMPLATE - Unidade 1` a `Unidade 4`
- `40 Questões - UNI1` a `UNI4`
- `Avaliação final_(10 discursivas)`
- `TEMPLATE ENTREGA DE TRABALHO`

A coincidência decisiva é a avaliação final de **10 discursivas**, que é exatamente o formato desta disciplina — confirmando que se trata da variante correta, e não do modelo genérico do Átomo 3.0, cuja avaliação tem 30 objetivas mais 10 discursivas.

Os dez modelos foram copiados para `tools/_templates_pristine/`, renomeados para esta disciplina, e são a base de toda a entrega. Os scripts sempre partem dessas cópias pristinas, de modo que a geração é repetível e não acumula resíduo.

Uma observação sobre a numeração das caixas: os modelos usam a **numeração contínua da disciplina**. O modelo da Unidade 3, por exemplo, traz "TEXTO BASE AULA 9" a "AULA 12" e "ROTEIRO VIDEOAULA 9" a "12", não 1 a 4. As caixas de relação profissional e de AAI existem apenas em algumas unidades — o que é coerente com o contrato desta disciplina, que concentra a AAI na Unidade 1.

**Pendência de coordenação remanescente:** confirmar que o reaproveitamento dos modelos da disciplina irmã é aceito, ou fornecer o pacote específico desta disciplina, caso exista.

**Ponto que exige ratificação formal:** a divisão em 4 unidades e 16 videoaulas é uma **inferência do conteudista**, ancorada na estrutura de quatro blocos da própria ementa e na prática das demais disciplinas do Núcleo. Ela não consta de nenhum documento recebido.

## 4. Conflitos identificados entre os documentos

### 4.1 Duração das videoaulas — 12 a 18 minutos contra 20 minutos

- O e-mail de encaminhamento informa "tempo mínimo de cada vídeo: 12-18 min, porém caso esteja com aplicação prática pode exceder esse tempo, sem problemas".
- A determinação posterior do responsável pelo projeto fixa **20 minutos** por videoaula.

**Resolução adotada:** 20 minutos, com narração dimensionada em 2.200 a 2.700 palavras faladas por aula. O e-mail autoriza explicitamente exceder a faixa quando houver aplicação prática, o que é o caso de todas as 16 aulas desta disciplina. Não há conflito real, e sim uma faixa mínima ampliada por autorização expressa.

### 4.2 Ferramentas proprietárias da ementa contra a exigência de prática reproduzível

- A ementa sugere MATLAB, Simulink, Stateflow e o Simulink Support Package for Arduino — todos proprietários e sob licença acadêmica que não acompanha o egresso.
- As diretrizes do Núcleo exigem que o aluno "veja tela, código, arquitetura, ferramenta, processo, configuração, análise, erro, correção e solução funcionando", em conteúdo "conectado ao mercado atual (2026)", e **convidam expressamente o professor a analisar criticamente a ementa e propor ajustes**.

**Resolução adotada:** substituição da espinha dorsal ferramental por uma pilha aberta em Python, mantendo **integralmente** os conteúdos, objetivos, competências e habilidades da ementa. A tabela de correspondência ferramental item a item está em `PLANO_APRENDIZAGEM_PROPOSTO.md`, seção "Adequações propostas à ementa oficial". OpenModelica e UPPAAL, já presentes na ementa, permanecem. Nenhum tópico foi suprimido; três acréscimos foram feitos (FMI 3.0, integração contínua e aritmética em ponto fixo), todos justificados pela exigência de atualidade de mercado.

**Esta é a decisão de maior impacto do projeto e requer ratificação explícita da coordenação.**

### 4.3 Adequação de uma referência básica

A terceira referência básica — TANENBAUM; BOS, *Sistemas operacionais modernos* — não trata de design baseado em modelos nem de controle. Ela é, porém, pertinente ao subconjunto de escalonamento, tempo real e jitter da Unidade 4.

**Resolução adotada:** a referência é mantida e utilizada especificamente na Aula 15 (tempo real, jitter e watchdog), que é onde ela de fato se aplica. Foram propostas quatro referências complementares adicionais, mais próximas do núcleo da disciplina, listadas no plano de aprendizagem.

### 4.4 Ausência de definição sobre gravação em estúdio

O e-mail veda a gravação nos estúdios da UniFECAF e determina captura por OBS Studio, Loom ou similar, com tela e câmera. Isso é consistente com o desenho hands-on adotado e não gera conflito; apenas condiciona todo o material a ter laboratório executável, o que foi atendido por `projeto_nexabot/`.

## 5. Verificação da viabilidade técnica da pilha proposta

Antes de escrever qualquer roteiro, a pilha foi instalada e exercitada, e os números do fio condutor foram conferidos por execução:

| Verificação | Resultado |
| --- | --- |
| Criação de ambiente com `uv` e instalação da pilha | Concluída |
| `python-control` 0.10.2, NumPy 2.5.2, SciPy 1.18.1, Matplotlib 3.11.1, SymPy 1.14.0 | Importados e exercitados |
| Matrizes de estado do NexaBot | $A = [[-342{,}857,\ -12{,}857],\ [180{,}0,\ -0{,}32]]$ |
| Polos contínuos | $-335{,}96$ e $-7{,}215$ |
| Constantes de tempo | Modais exatas: $2{,}9765\ \mathrm{ms}$ e $138{,}598\ \mathrm{ms}$; aproximações desacopladas: $L/R=2{,}9167\ \mathrm{ms}$ e $JR/(K_tK_e)=148{,}148\ \mathrm{ms}$ |
| Ganho estático | $21{,}2164\ \mathrm{rad/(s\,V)}$ |
| Tensão de regime para 1,0 m/s | $18{,}85\ \mathrm{V}$ (de 24 V disponíveis) |
| Controlabilidade e observabilidade | Posto 2 em ambas as matrizes |
| Simulação de degrau a 18,85 V | 399,63 rad/s em 1 s, equivalente a 0,999 m/s |
| Compilador C (gcc) para geração de código e SIL | Disponível |
| FMUs de referência FMI 3.0 | Acessíveis |

Nenhum número citado no material didático é estimado: todos são reproduzíveis pelos scripts de `projeto_nexabot/`.

## 6. Pendências para a coordenação

1. Ratificar a divisão em 4 unidades e 16 videoaulas de 20 minutos.
2. Ratificar a substituição ferramental por pilha aberta em Python, mantidos os conteúdos da ementa.
3. Fornecer, se existirem, os modelos institucionais DOCX de unidade, questionário, avaliação final, entrega de trabalho e slides — ou confirmar que a estrutura adotada da variante TECH do Átomo 3.0 é aceita.
4. Confirmar que o reaproveitamento dos modelos oficiais da disciplina irmã do mesmo Núcleo é aceito (ver seção 3.1), ou fornecer o pacote específico desta disciplina.
5. Confirmar o formato da avaliação final (10 dissertativas).
6. Informar carga horária e prazo de entrega.
7. Confirmar o padrão de slides.
