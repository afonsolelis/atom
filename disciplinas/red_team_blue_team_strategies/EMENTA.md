# Ementa e plano de aprendizagem — Red Team & Blue Team Strategies

> **Ementa oficial**, enviada pela coordenação do curso (Osvaldo) em 18/11/2026 ([documento no Google Drive](https://docs.google.com/document/d/1hrSLYINyfY-ZhAIFWrbrfcpOA8UmvW9R/edit)).
> Os textos abaixo, da ementa à bibliografia, são transcritos do documento oficial. O mapa das 16 aulas desdobra o roteiro de aprendizagem oficial (4 tópicos por unidade, 1 aula por tópico). A proposta provisória de 13/11/2026 foi substituída.

## Ementa

Estratégias ofensivas e defensivas de segurança da informação aplicadas a exercícios de simulação de adversário. Aborda planejamento de operações de red team, emulação de ameaças com base na matriz MITRE ATT&CK, técnicas de intrusão, movimentação lateral e persistência, bem como a atuação do blue team em monitoramento, detecção, caça a ameaças, resposta a incidentes e fortalecimento de controles, incluindo a colaboração entre as equipes (purple team).

## Objetivo geral

Planejar e conduzir exercícios de simulação de adversário em ambientes controlados e autorizados, articulando as ações do red team com a detecção, a resposta e a melhoria contínua conduzidas pelo blue team.

## Objetivos específicos

1. Compreender o ciclo de uma operação de red team e suas regras de engajamento.
2. Mapear técnicas de ataque na matriz MITRE ATT&CK e planejar a emulação de ameaças.
3. Executar técnicas de reconhecimento, exploração e movimentação lateral em laboratório.
4. Detectar, investigar e responder a atividades maliciosas com ferramentas de monitoramento.
5. Produzir relatórios e planos de melhoria a partir de exercícios purple team.

## Competências

Planejar e executar exercícios de red team e blue team em ambientes autorizados, aplicando emulação de adversário, detecção, resposta a incidentes e melhoria de controles com base em frameworks reconhecidos.

## Habilidades

Planejar engajamentos e regras de atuação; emular técnicas do MITRE ATT&CK; realizar reconhecimento e exploração em laboratório; analisar logs e tráfego; criar regras de detecção; conduzir resposta a incidentes; elaborar relatórios técnicos e executivos.

## Atitudes

- Ética e conduta profissional estritamente dentro do escopo autorizado.
- Mentalidade de adversário combinada com visão de defesa.
- Rigor na documentação de ações, evidências e achados.
- Colaboração entre equipes ofensivas e defensivas.
- Atualização contínua diante de novas técnicas e ameaças.

## Roteiro de aprendizagem (oficial)

1. **Planejamento de Operações e Emulação de Adversário**
   - Papéis e objetivos: red team, blue team, white team e purple team.
   - Regras de engajamento, escopo, autorização e aspectos legais.
   - MITRE ATT&CK: táticas, técnicas e construção de planos de emulação.
   - Inteligência de ameaças aplicada ao planejamento da operação.
2. **Técnicas Ofensivas em Ambiente Controlado**
   - Reconhecimento e enumeração de serviços e usuários.
   - Exploração de vulnerabilidades e obtenção de acesso inicial.
   - Escalada de privilégios, movimentação lateral e persistência.
   - Evasão básica de defesas e limpeza de rastros em laboratório.
3. **Defesa, Monitoramento e Detecção**
   - Arquitetura de monitoramento: logs, SIEM e telemetria de endpoints.
   - Detecção baseada em assinaturas, comportamento e regras.
   - Caça a ameaças: hipóteses, consultas e análise de anomalias.
   - Hardening de sistemas e redução da superfície de ataque.
4. **Resposta a Incidentes e Purple Team**
   - Ciclo de resposta a incidentes: preparação, detecção, contenção, erradicação e recuperação.
   - Coleta de evidências e linha do tempo do incidente.
   - Exercícios purple team: validação de detecções contra técnicas emuladas.
   - Relatório final: achados, riscos, recomendações e métricas de melhoria.

## Unidades e aulas

| Unidade | Aula | Título | Videoaula |
|---|---|---|---|
| 1 — Planejamento de Operações e Emulação de Adversário | 1 | Red, Blue, White e Purple Team: papéis e objetivos | Videoaula 1 |
| 1 | 2 | Regras de engajamento, escopo, autorização e aspectos legais | Videoaula 2 |
| 1 | 3 | MITRE ATT&CK: táticas, técnicas e planos de emulação | Videoaula 3 |
| 1 | 4 | Inteligência de ameaças aplicada ao planejamento da operação | Videoaula 4 |
| 2 — Técnicas Ofensivas em Ambiente Controlado | 5 | Reconhecimento e enumeração de serviços e usuários | Videoaula 5 |
| 2 | 6 | Exploração de vulnerabilidades e obtenção de acesso inicial | Videoaula 6 |
| 2 | 7 | Escalada de privilégios, movimentação lateral e persistência | Videoaula 7 |
| 2 | 8 | Evasão básica de defesas e limpeza de rastros em laboratório | Videoaula 8 |
| 3 — Defesa, Monitoramento e Detecção | 9 | Arquitetura de monitoramento: logs, SIEM e telemetria de endpoints | Videoaula 9 |
| 3 | 10 | Detecção baseada em assinaturas, comportamento e regras | Videoaula 10 |
| 3 | 11 | Caça a ameaças: hipóteses, consultas e análise de anomalias | Videoaula 11 |
| 3 | 12 | *Hardening* de sistemas e redução da superfície de ataque | Videoaula 12 |
| 4 — Resposta a Incidentes e Purple Team | 13 | Ciclo de resposta a incidentes: preparação, detecção, contenção, erradicação e recuperação | Videoaula 13 |
| 4 | 14 | Coleta de evidências e linha do tempo do incidente | Videoaula 14 |
| 4 | 15 | Exercícios *purple team*: validação de detecções contra técnicas emuladas | Videoaula 15 |
| 4 | 16 | Relatório final: achados, riscos, recomendações e métricas de melhoria | Videoaula 16 |

## Tecnologias sugeridas (oficial) e onde aparecem

Nos slides, todas as ferramentas aparecem em laboratórios simulados no navegador, contra a plataforma fictícia Rede Tatame. Nenhum laboratório traz código de exploração, *payload* ou técnica de evasão operacional.

| Tecnologia | Uso indicado na ementa | Aulas |
|---|---|---|
| Kali Linux | plataforma de testes de segurança em laboratório | 5, 6, 7 |
| Metasploit Framework | exploração em ambiente controlado | 6, 7 |
| MITRE ATT&CK Navigator | planejamento e cobertura de técnicas | 3, 15, 16 |
| Wazuh ou Security Onion | monitoramento, detecção e análise de eventos | 9, 10, 11, 13 |
| Wireshark | análise de tráfego e investigação de incidentes | 5, 9, 14 |

## Bibliografia básica (oficial)

1. WEIDMAN, Georgia. *Testes de invasão*: uma introdução prática ao hacking. São Paulo: Novatec, 2014.
2. STALLINGS, William. *Criptografia e segurança de redes*: princípios e práticas. 6. ed. São Paulo: Pearson, 2015.
3. NAKAMURA, Emilio Tissato; GEUS, Paulo Lício de. *Segurança de redes em ambientes cooperativos*. São Paulo: Novatec, 2007.

## Bibliografia complementar (oficial)

1. ENGEBRETSON, Patrick. *The basics of hacking and penetration testing*. 2nd ed. Waltham: Syngress, 2013.
2. BEJTLICH, Richard. *The practice of network security monitoring*. San Francisco: No Starch Press, 2013.
3. SANDERS, Chris; SMITH, Jason. *Applied network security monitoring*. Waltham: Syngress, 2013.
4. NATIONAL INSTITUTE OF STANDARDS AND TECHNOLOGY. *Computer security incident handling guide*. Gaithersburg: NIST, 2012. (SP 800-61 Rev. 2).
5. ANDERSON, Ross. *Security engineering*. 3. ed. Hoboken: Wiley, 2020.

## Biblioteca Virtual ("Direto da fonte" do material complementar)

Obras confirmadas na Biblioteca Virtual em 13/11/2026 e usadas na seção *Direto da fonte* de cada unidade:

- SILVA, Michel Bernardo Fernandes da. *Cibersegurança*: uma visão panorâmica sobre a segurança da informação na internet. Rio de Janeiro: Freitas Bastos, 2023. *E-book*. Disponível em: <https://plataforma.bvirtual.com.br/Acervo/Publicacao/208076>.
- SOARES, Cleber; FRANCO, Deivison Pinheiro; SANTOS, Joas Antonio dos. *Introdução à segurança ofensiva*: uma abordagem para pentesters e red teams. Rio de Janeiro: Brasport, 2023. *E-book*. Disponível em: <https://plataforma.bvirtual.com.br/Acervo/Publicacao/213767>.
- LEVI, Hiago Kin. *Confronto cibernético*: técnicas e táticas de enfrentamento e resposta a ameaças persistentes avançadas (APTs). Rio de Janeiro: Brasport, 2026. *E-book*. Disponível em: <https://plataforma.bvirtual.com.br/Acervo/Publicacao/235882>.
- SANTOS, Joas Antonio dos. *Introdução ao Red Team Operations 2.0*: um guia básico para suas operações de Red Team. Rio de Janeiro: Brasport, 2024. *E-book*. Disponível em: <https://plataforma.bvirtual.com.br/Acervo/Publicacao/220894>.
- STALLINGS, William. *Criptografia e segurança de redes*: princípios e práticas. 6. ed. São Paulo: Pearson, 2015. *E-book*. Disponível em: <https://plataforma.bvirtual.com.br/Acervo/Publicacao/22446>.
