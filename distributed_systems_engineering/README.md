# Distributed Systems Engineering

Produção de conteúdo EAD do NEaD.

- Professor-conteudista: Afonso Cesar Lelis Brandão
- Coordenação indicada no e-mail: Osvaldo
- Acompanhamento da produção: Carolina Bastos
- Contato sobre videoaulas: Maico Pereira Gomes
- Valor informado para o pacote: R$ 6.000,00
- Situação: conteúdo concluído — 4 unidades (16 aulas), 160 questões, roteiros das 16 videoaulas, roteiro do vídeo introdutório, entrega de trabalho (PBL), avaliação final dissertativa, e os 17 decks de slides em HTML (padrão UniFECAF/Átomo 3.0, mesmo modelo de `data_engineering_and_pipelines/`). Pendências: validação pela coordenação do NEaD e agendamento/gravação das videoaulas (ver `CRONOGRAMA.md`)

## Escopo contratado

- 4 templates de unidade;
- 160 questões, sendo 40 por unidade;
- 1 vídeo introdutório;
- 16 videoaulas, sendo 4 por unidade;
- 1 trabalho;
- 1 avaliação final com 10 questões dissertativas.

## Estrutura de arquivos

```text
distributed_systems_engineering/
├── README.md
├── CRONOGRAMA.md
├── DIRETRIZES_PRODUCAO.md
├── roteiro_video_introdutorio.md
├── instrumentos_avaliativos/
│   ├── entrega_trabalho.md
│   └── avaliacao_dissertativa.md
├── unidade_1/
│   ├── unidade_1.md
│   ├── questoes_uni1.md
│   ├── roteiros_20min.md
│   └── slides/
│       ├── aula0.html … aula4.html
│       └── assets/foto-professor.jpg
├── unidade_2/  (aula5.html–aula8.html)
├── unidade_3/  (aula9.html–aula12.html)
└── unidade_4/  (aula13.html–aula16.html)
```

## Fontes recebidas

- E-mail de início da produção enviado por Carolina Bastos;
- [Pasta da disciplina no Google Drive](https://drive.google.com/drive/u/0/folders/13uV2_1eiv5l4spsE-iif3DdeYomR8aHa);
- tutoriais, templates, instrumentos e slides oficiais extraídos do arquivo `a.zip`;
- [análise detalhada dos materiais](ANALISE_MATERIAIS_RECEBIDOS.md);
- plano de aprendizagem: ainda precisa ser incorporado ao projeto.

## Próxima etapa

O conteúdo em Markdown foi produzido a partir de `PLANO_APRENDIZAGEM_PROPOSTO.md` (proposta provisória elaborada a partir do título e da ementa da disciplina, ainda não confrontada com um plano oficial do NEaD) e das regras de `DIRETRIZES_PRODUCAO.md`. Antes da entrega institucional:

1. confirmar com a coordenação (Carolina Bastos) se o plano de aprendizagem proposto é aceito como definitivo, ou se há um plano oficial divergente a ser incorporado;
2. validar com a equipe a distribuição das 40 questões por unidade (20 asserção-razão + 20 interpretação), adotada provisoriamente conforme `ANALISE_MATERIAIS_RECEBIDOS.md`;
3. definir a modalidade e agendar as gravações das 16 videoaulas e do vídeo introdutório;
4. exportar os decks HTML (`unidade_N/slides/aulaN.html`) para PDF (Chrome → Imprimir → Salvar como PDF, paisagem, sem margens, gráficos de fundo ativados) caso a entrega institucional exija PDF/PPTX em vez do HTML; os roteiros (`unidade_N/roteiros_20min.md`) continuam sendo a referência de fala e indicações de edição para quem gravar.

Os documentos serão mantidos em Markdown durante a produção e convertidos para DOCX na etapa final.
