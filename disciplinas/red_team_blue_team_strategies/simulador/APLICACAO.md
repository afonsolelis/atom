# Aplicação padrão da disciplina: a plataforma da Rede Tatame

Todos os laboratórios da disciplina usam o mesmo sistema como alvo e como ambiente defendido: a plataforma distribuída da **Rede Tatame**, uma rede **fictícia** de academias de jiu-jitsu. O cenário é o mesmo da demonstração da palestra da Alliance (repositório `aulas`) e do simulador da Aula 06 de Data Collection (repositório `aulas_mackenzie`), agora visto pelo ângulo da segurança. O Red Team ataca este sistema em exercícios autorizados, o Blue Team o monitora e o Purple Team mede a evolução dele aula a aula.

O simulador em [`index.html`](index.html) roda a plataforma no navegador e é embutido nos slides (`?embed=1`). Este arquivo é a fonte única de nomes, endereços e números: ao escrever um laboratório, use só o que está aqui.

## A rede

- 240 academias e 36.000 alunos em quatro regiões, cada uma com um cluster Kafka próprio:

| Região | Academias | Alunos |
|---|---|---|
| `sa-saopaulo` | 96 | 14.400 |
| `us-virginia` | 72 | 10.800 |
| `eu-estocolmo` | 48 | 7.200 |
| `ap-sydney` | 24 | 3.600 |

- Sede administrativa em São Paulo, com cerca de 120 colaboradores (financeiro, atendimento às academias, TI, produto).
- Cerca de 30% dos alunos são menores de idade (turmas *kids*). Há dados de saúde (atestados), biometria facial das catracas e dados de pagamento. Tudo isso pesa na LGPD e no PCI DSS.

## Arquitetura

```text
 App do aluno ─┐                         ┌─ svc-identidade (OAuth 2.0, JWT, MFA)
 Portal gestão ┼─ CDN/WAF ─ API gateway ─┼─ svc-alunos ── db-alunos (PostgreSQL)
 Catracas IoT ─┘   (edge)  (api.tatame)  ├─ svc-checkin
                                         ├─ svc-cobranca ── PagaFácil (parceiro de pagamento)
                                         ├─ svc-graduacao
                                         └─ svc-notificacoes (e-mail, push)
            todos publicam em ──> Kafka: tatame.eventos · tatame.auditoria · tatame.seguranca
                                    ├─ CEP (motor de regras em tempo real: negócio e segurança)
                                    ├─ data lake (bucket tatame-lake) ─> Elasticsearch
                                    └─ encaminhador para o SIEM do SOC
 Sede: AD corp.tatame.local · notebooks com EDR · VPN · e-mail corporativo
```

| Componente | Nome | Endereço | Observação |
|---|---|---|---|
| Site institucional | `www.tatame.com.br` | 203.0.113.10 | CDN |
| App do aluno (API) | `app.tatame.com.br` | 203.0.113.20 | atrás do WAF |
| Portal das academias | `gestao.tatame.com.br` | 203.0.113.21 | login com MFA |
| API gateway | `api.tatame.com.br` | 203.0.113.22 | valida JWT, limita taxa |
| Homologação esquecida | `hml-gestao.tatame.com.br` | 203.0.113.45 | fora do inventário, sem WAF (achado da Aula 5/6) |
| VPN da sede | `vpn.tatame.com.br` | 203.0.113.30 | appliance "NetGuard" (fictício) |
| E-mail | MX `mx1.tatame.com.br` | 203.0.113.40 | SPF/DMARC em `p=quarantine` |
| Status | `status.tatame.com.br` | terceirizado | fora do escopo |
| Pagamentos | `api.pagafacil.example` | terceiro | **sempre fora do escopo** |
| Rede de serviços (nuvem) | VPC `10.40.0.0/16` | | `svc-*` em 10.40.1.0/24, bancos em 10.40.9.0/24 |
| Rede da sede | `10.10.0.0/16` | | AD `SRV-AD-01` 10.10.1.10, arquivos `SRV-ARQ-01` 10.10.1.20, ERP `SRV-ERP-01` 10.10.1.30 |
| Catracas das academias | `10.80.<academia>.0/24` | | leitor facial, *heartbeat* a cada 30 s |
| Rede de pagamentos | `10.40.99.0/24` | | escopo PCI, **fora do escopo** dos exercícios |

Tópicos Kafka: `tatame.eventos` (6 partições, chave = academia), `tatame.auditoria` (logins, mudanças de permissão, acessos administrativos) e `tatame.seguranca` (alertas do CEP). O identificador do aluno é anonimizado na borda com HMAC-SHA-256; o nome nunca trafega no Kafka.

## Pessoas (fictícias)

| Pessoa | Papel |
|---|---|
| Marina Prado | CISO, assina as autorizações dos exercícios |
| Luiza Ferraz | analista de SOC nível 2 (Blue Team) |
| Rafael Tavares | engenheiro de detecção |
| Bruno Sato | líder do Red Team interno |
| Caio Mendes | administrador de TI da sede |
| Carla Dias | analista do financeiro (alvo do *phishing* simulado) |
| Felipe Nogueira | filiado dono de academias em `us-virginia` |

Hosts da sede seguem o padrão `NB-<ÁREA>-NNN` (ex.: `NB-FIN-031`) e `SRV-<FUNÇÃO>-NN`.

## Adversário emulado

O **Grupo Cobalto Austral** é um grupo fictício de *ransomware* usado nos exercícios de emulação (Unidades 2 e 4). Ele entra por *phishing* ou por credenciais vazadas, abusa de contas válidas, move-se para os servidores da sede e tenta extorquir com dados de alunos. As técnicas são descritas pelos IDs do MITRE ATT&CK, sem comandos de ataque.

## Cenários do simulador

| Cenário | Aulas | O que acontece | Técnicas ATT&CK |
|---|---|---|---|
| `phishing` | 1, 7 | campanha simulada contra o financeiro, clique e tentativa de login | T1566.002, T1078 |
| `recon` | 5, 6 | levantamento externo, subdomínio de homologação exposto, varredura | T1593, T1596, T1595 |
| `api-abuso` | 6, 10 | *credential stuffing* no app e acesso a dados de outro aluno (BOLA) | T1110.004, T1190 |
| `ransomware` | 2, 8, 12, 13 | cadeia completa do Cobalto Austral, da conta válida à criptografia na sede | T1078, T1021.001, T1003, T1486, T1490 |
| `catraca` | 4, 9 | catraca de uma academia passa a enviar volume anômalo e um firmware não assinado | T1495, T1499 |
| `exfiltracao` | 11, 14 | ferramenta de acesso remoto não aprovada e cópia de dados para bucket externo | T1219, T1567.002 |

Cada cenário gera eventos nos mesmos tópicos que o tráfego legítimo. Se a fonte de telemetria estiver ligada e a regra do CEP correspondente estiver ativa, nasce um alerta no SOC; senão, o passo passa despercebido. Ligar e desligar fontes e regras é o que as aulas exploram.

Na aba Cenários, **Reiniciar** (no topo) volta fontes e regras ao padrão; **Repetir com as fontes e regras atuais** roda o mesmo cenário de novo mantendo os ajustes feitos, para o ciclo de reteste do Purple Team. Cada passo mostra também a fase da Cyber Kill Chain correspondente à técnica.
