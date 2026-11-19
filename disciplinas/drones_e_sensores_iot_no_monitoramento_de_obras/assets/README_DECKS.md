# Decks de slides — como montar

Os 17 decks (`unidade_N/slides/aula0.html` … `aula16.html`) **não são arquivos únicos**: compartilham os arquivos desta pasta, no mesmo esquema de `disciplinas/red_team_blue_team_strategies/`.

| Arquivo | Papel |
|---|---|
| `deck.css` | padrão visual UniFECAF (cópia do deck de Red Team) |
| `sprite.js` | logo e triângulos do padrão (símbolos SVG) |
| `deck.js` | navegação; dispara `slide:enter` / `slide:leave` |
| `obra.css` + `obra.js` | fotos em tela cheia, galerias, cenas 3D (three.js r128 via cdnjs), animações e calculadoras |
| `foto-professor.jpg`, `favicon.svg` | professor e ícone |

**Referência:** `unidade_1/slides/aula0.html`. Copie a estrutura dela (capa, sumário, slides de conteúdo com `mosaico-bg`, `slide-fim`). A Aula 0 tem ainda Audiodescrição e Sobre o professor; as demais aulas começam por capa + sumário.

Ordem dos scripts no fim do `<body>`: `obra.js`, depois o `<script>` com `Obra.register(...)` da aula (se houver), e por último `deck.js`.

## Tipos de slide

- `slide slide-capa`, `slide slide-sumario`, `slide slide-fim` — iguais à Aula 0.
- **Conteúdo**: `<section class="slide">` + `<div class="mosaico-bg">…</div>` + `<div class="slide-content">` com `kicker`, `h2` e corpo (`slide-content-box`, `colunas`, `stat-grid`, `versus`, `timeline`, `galeria`, `callout-azul`).
- **Foto em tela cheia**: `slide slide-foto` com `.foto-bg` (background-image + `role="img"` + `aria-label`), `.foto-veu` e `.credito`.
- **Visualização**: `slide slide-viz` + `mosaico-bg` + `.viz-grid` com `.viz[data-viz]` à esquerda e `.viz-lado` à direita. Se a visualização tiver controles deslizantes, ponha `<div data-controles></div>` dentro do `.viz-lado` (é onde eles aparecem).

## Fotos

- **Somente Wikimedia Commons**, verificadas com `python tools/wikimedia.py info "File:Nome.jpg"` (dá a URL de miniatura de 1280 px, o autor e a licença). Busca: `python tools/wikimedia.py buscar "termo em inglês"`.
- Use a URL `thumb.wikimedia.org/...1280px-...` que o script imprime.
- **Toda foto leva `<p class="credito">Foto: Autor — Wikimedia Commons (licença)</p>`** e `alt`/`aria-label` descritivo.

## Visualizações prontas (`data-viz`)

| nome | o que mostra | opções (`data-opts`, JSON) |
|---|---|---|
| `canteiro3d` | canteiro 3D: prédio subindo, grua, escavação com sensores, gateway, nuvem e drone em varredura; referências de escala (pessoa de 1,75 m e caminhão de ≈ 10 m) | `drone`, `sensores`, `guindaste`, `predio` (bool) |
| `gemeo3d` | prédio real × gêmeo digital; simula recalque, malha aberta/fechada | — |
| `drone3d` | quadricóptero com vista explodida; rótulos das peças só aparecem na vista explodida | — |
| `malha` | grandeza monitorada × tempo: malha aberta × fechada, níveis de atenção/alerta | `nome`, `unidade`, `eixo`, `atencao`, `alerta`, `taxa`, `residual`, `max`, `horas` (≤ 72 → eixo em horas), `vel`, `acaoNo` (`atencao`/`alerta`), `manual`, `atrasoAberta`, `atrasoFechada`, `intMin`/`intMax`/`intPasso`/`intIni`, `intUnid` (`h`/`min`), `base` (grandeza invertida, ex.: NA abaixo do fundo), `rotFechada`, `rotAberta`, `dec` |
| `sensor` | alvo: precisão × veracidade (viés) × exatidão (VIM), com viés e dispersão; mosca de ±2 mm (viés ≤ 1 mm = veraz; dispersão ≤ 1 mm = preciso) | — |
| `amostragem` | Nyquist e aliasing, critério estrito f<sub>s</sub> > 2 f<sub>max</sub> | `f0` (Hz), `fsMin`, `fsMax`, `fsPasso`, `fsIni` |
| `rede` | alcance Wi-Fi (≈ 200 m ao ar livre: só os 2 sensores do canteiro) × LoRaWAN (3 km, urbano) × NB-IoT × 4G sobre mapa de 4 km | — |
| `cobertura` | voo em faixas: autonomia × área (A = v·t<sub>útil</sub>·d); o voo recomeça ao mexer num controle | `area` (ha), `v` (m/s), `t` (min úteis), `d` (m) |
| `calc` | calculadora declarativa com barras animadas | ver abaixo |

### `calc` (sem escrever JavaScript)

```html
<div class="viz" data-viz="calc" data-opts='{
  "inputs":  [{"id":"A","label":"Área do canteiro","min":1,"max":50,"step":1,"value":10,"unit":"ha"}],
  "outputs": [{"label":"Custo convencional","expr":"A*1800","unit":"R$"},
              {"label":"Custo com drone","expr":"2500+A*350","unit":"R$"},
              {"label":"Economia","expr":"(o1-o2)/o1*100","unit":"%","dec":1,"destaque":true}],
  "barras":  [{"label":"Convencional","expr":"o1","unit":"R$"},{"label":"Drone","expr":"o2","unit":"R$"}],
  "nota": "Valores ilustrativos."
}'></div>
```

`expr` é uma expressão JavaScript sobre os ids das entradas e as saídas anteriores (`o1`, `o2`…). Pode devolver texto (ex.: `"m<=0.25?'Classe 3, até 250 g':'Classe 3'"`).

### Visualização própria de uma aula

```html
<script>
Obra.register('minha-viz', (host, opts, painel) => {
  const { ctx } = Obra.canvas2d(host);             // ou Obra.cena3d(host, opts, ({THREE, scene, rotulo}) => update)
  const lp = Obra.loop((t, dt) => { /* desenha */ });
  return { start: lp.start, stop: lp.stop };       // pode devolver uma Promise (cena3d já devolve)
});
</script>
```

Comportamentos comuns (em `obra.js`):

- **Rótulos 3D não se sobrepõem**: a cada quadro, os rótulos visíveis são ordenados por altura e o de baixo desce até ficar livre; todos ficam dentro da cena.
- **HUD × botões**: `botoes()` publica a largura do grupo de botões em `--ctrl-w`, e o HUD (chips) se limita ao espaço à esquerda dele, sem passar por baixo.
- **`malha`**: `manual` ≥ 24 h aparece em dias (168 h = "semanal"); use `residual: 0` quando a narração diz que a curva "parou de subir" depois da ação.
- **Créditos** (`.credito`): 11 px sobre fundo 70 % opaco, legíveis na exportação em PDF.

Helpers em `window.Obra`: `canvas2d`, `cena3d`, `loop`, `slider(painel, {...})`, `botoes(host, [[texto, fn, ligado]])`, `hud`/`chip`, `fmt` (número pt-BR), `droneModelo(THREE)`, `caixa(THREE, w, h, d, cor)`.

## Conferência

`python tools/capturar_slides.py unidade_1/slides/aulaN.html <pasta>` tira um PNG por slide (Chrome real, com WebGL) e lista erros de console e conteúdo transbordando o cartão. **Olhe os PNGs** antes de dar o deck por pronto.

Regras de texto: pt-BR, sem MathJax (fórmulas em texto/Unicode, ex.: `σ = E·ε`, ou `.formula`), números com vírgula decimal, valores ilustrativos sinalizados como tal.
