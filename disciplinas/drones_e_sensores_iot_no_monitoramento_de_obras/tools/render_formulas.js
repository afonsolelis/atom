/**
 * Converte fórmulas LaTeX em SVG usando MathJax 3 sob Node.
 *
 * Lê da entrada padrão um JSON no formato
 *     [{ "id": "<hash>", "tex": "<latex>", "display": true|false }, ...]
 * e escreve na saída padrão
 *     { "<hash>": { "svg": "<svg…>", "widthEx": 26.5, "heightEx": 5.4 }, … }
 *
 * `fontCache: 'none'` é obrigatório: com o cache ligado, o MathJax emite os
 * glifos como referências `<use>` para um `<defs>` compartilhado, e o
 * rasterizador não as resolve, produzindo uma imagem em branco. Sem o cache,
 * cada glifo vira um `<path>` completo, autocontido e rasterizável.
 */
const { mathjax } = require('mathjax-full/js/mathjax.js');
const { TeX } = require('mathjax-full/js/input/tex.js');
const { SVG } = require('mathjax-full/js/output/svg.js');
const { liteAdaptor } = require('mathjax-full/js/adaptors/liteAdaptor.js');
const { RegisterHTMLHandler } = require('mathjax-full/js/handlers/html.js');
const { AllPackages } = require('mathjax-full/js/input/tex/AllPackages.js');

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const doc = mathjax.document('', {
  InputJax: new TeX({ packages: AllPackages }),
  OutputJax: new SVG({ fontCache: 'none' }),
});

let entrada = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (bloco) => { entrada += bloco; });
process.stdin.on('end', () => {
  const itens = JSON.parse(entrada);
  const saida = {};
  for (const item of itens) {
    try {
      const node = doc.convert(item.tex, { display: !!item.display });
      const svg = adaptor.innerHTML(node);
      const mw = svg.match(/width="([\d.]+)ex"/);
      const mh = svg.match(/height="([\d.]+)ex"/);
      saida[item.id] = {
        svg,
        widthEx: mw ? parseFloat(mw[1]) : null,
        heightEx: mh ? parseFloat(mh[1]) : null,
        erro: /merror/.test(svg) ? 'MathJax reportou erro de sintaxe' : null,
      };
    } catch (e) {
      saida[item.id] = { svg: null, erro: String(e && e.message ? e.message : e) };
    }
  }
  process.stdout.write(JSON.stringify(saida));
});
