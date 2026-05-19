# Template de Apresentação HTML — UniFECAF

Apresentação HTML single-file seguindo a identidade visual da **UniFECAF** (azul institucional `#002057` + amarelo de destaque), com acentos sutis herdados do template Átomo 3.0.

## Como usar

1. **Copie** este `index.html` para a pasta da aula:
   ```
   <disciplina>/unidade_N/slides/aulaN.html
   ```
2. **Edite** o conteúdo dos slides (cada `<section class="slide">` é um slide).
3. **Abra no navegador** — é só clicar duas vezes no `.html` ou arrastar pro Chrome/Firefox.

## Logo da UniFECAF

O logo **oficial** é carregado direto do site institucional via URL:

```
https://www.unifecaf.com.br/_next/static/media/unifecaf-logo-branco.edf5ffe3.svg
```

É a versão branca, ideal para fundo escuro — usada na capa, divisores de seção e slide de encerramento. Os slides internos (fundo claro) **não exibem o logo**, apenas a decoração de triângulo no canto. Padrão de decks profissionais — evita poluição visual.

**Nota:** se o site institucional trocar o hash da URL (`edf5ffe3`), o logo pode quebrar. Nesse caso, atualize a `href` do `<symbol id="logo-marca">` no `index.html`.

## Navegação

- `←` `→` — anterior / próximo
- `Espaço` / `PageDown` — próximo
- `Home` / `End` — primeiro / último
- `#3` na URL — pula direto para o slide 3
- Botões no canto inferior direito

## Exportar para PDF

Abra a apresentação no Chrome e **Imprimir → Salvar como PDF**:

- Layout: paisagem
- Tamanho do papel: A4 ou personalizado (1280 × 720 já está no CSS)
- Margens: nenhuma
- Marcar "Gráficos de fundo"

Cada slide vira uma página automaticamente.

## Tipos de slide

| Classe CSS | Quando usar |
| --- | --- |
| `slide slide-capa` | Slide 1 — capa **azul UniFECAF** com logo branco, título e docente |
| `slide slide-prof` | "Sobre o professor" — split branco/azul com foto à esquerda, dados à direita |
| `slide slide-section` | Divisor de seção/módulo (fundo azul + número grande amarelo) |
| `slide` (default) | Slide de conteúdo padrão (com triângulo decorativo sutil no canto) |
| `slide slide-quote` | Citação destacada (fundo amarelo) |
| `slide slide-fim` | Encerramento (fundo azul + logo + "Obrigado!") |

### Slide "Sobre o professor" (`slide-prof`)

Layout split 50/50:

- **Lado branco (esquerda):** logo UniFECAF preto (filtro CSS) + placeholder de foto quadrada com aparência de "céu + colina" (substitua por `<img src="./assets/foto-professor.jpg">` quando tiver a foto real)
- **Lado azul (direita):** nome, cargo, descrição curta, e-mail e LinkedIn — com decorações de triângulos coloridos (cluster na boundary, amarelo no canto superior, mini-cluster no canto inferior)

Para colocar a foto real, troque a div `.prof-foto` por:

```html
<div class="prof-foto">
  <img src="./assets/foto-professor.jpg" alt="Foto do(a) professor(a)"/>
</div>
```

Dentro de qualquer slide você pode usar:

- `<div class="colunas">` — grid 2 colunas (texto + imagem)
- `<div class="pontos-chave">` + `.ponto` — grid de cards coloridos
- `<div class="col-imagem">` — placeholder de imagem (substitua por `<img>`)
- `<div class="slide-footer">` — rodapé com nome da disciplina/aula

## Paleta de cores (CSS variables)

| Variável | Cor | Uso |
| --- | --- | --- |
| `--azul-fecaf` | `#002057` | **Cor primária** — capa, divisores, encerramento, títulos |
| `--amarelo` | `#F0CE29` | Destaque, "FECAF" no logo, slide de quote, números |
| `--azul-medio` | `#1F44A8` | Subtítulos, ênfase secundária |
| `--azul-claro` | `#2BBBE0` | Bordas de pontos-chave |
| `--magenta` | `#E91E63` | Tag `<strong>`, accent forte pontual |
| `--verde-claro` | `#8DD17E` | Acento pontual |
| `--verde-escuro` | `#1F8A4E` | Acento pontual |
| `--cinza-bg` | `#F2F4F8` | Fundo padrão dos slides de conteúdo |

## Símbolos SVG reutilizáveis

Símbolos embutidos no `<svg>` invisível no início do `<body>`:

- `#logo-marca` — logo oficial UniFECAF (branco, referencia `./logo/unifecaf-branco.svg`)
- `#trio-canto` — decoração sutil de canto superior direito
- `#faixa-triangulos` — faixa amarelo/branco no rodapé da capa

Use com (atenção ao `viewBox` correto do logo, 271×67):

```html
<svg width="380" height="94" viewBox="0 0 271 67"><use href="#logo-marca"/></svg>
```

## Customização por disciplina

Para uma identidade levemente diferente por disciplina, edite só a paleta no topo do CSS (`:root { --azul-fecaf: ... }`). O resto se ajusta sozinho.
