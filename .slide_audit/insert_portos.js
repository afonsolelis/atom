// Inserts the UniFECAF standard "Audiodescrição" slide (all decks) and the
// "Sobre o professor" split slide (aula1-16) right after the cover, before the
// slide-sumario, for the Portos/Aeroportos/Ferrovias discipline. Idempotent.
const fs = require('fs');
const path = require('path');

const DISC = path.resolve(__dirname, '..', 'portos_aeroportos_e_ferrovias');
const UNIT_DIRS = ['unidade_1', 'unidade_2', 'unidade_3', 'unidade_4'].map((u) => path.join(DISC, u, 'slides'));

const ANCHOR = '  <section class="slide slide-sumario">';

const AUDIO = `  <section class="slide slide-audio">
    <div class="audio-canto-tl" aria-hidden="true"><svg viewBox="0 0 150 130"><use href="#audio-canto-tl"/></svg></div>
    <div class="audio-canto-br" aria-hidden="true"><svg viewBox="0 0 360 250"><use href="#audio-canto-br"/></svg></div>
    <div class="slide-content">
      <div class="audio-logo">
        <svg width="180" height="44" viewBox="0 0 271 67" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
      </div>
      <h1>Audiodescrição</h1>
      <p class="audio-texto">Esta apresentação segue a identidade visual da UniFECAF: fundo em azul-marinho, títulos em verde-claro e cartões brancos com o conteúdo de cada slide. As bordas trazem mosaicos de triângulos coloridos — verde, azul, amarelo e magenta. O conteúdo é conduzido pelo Prof. Afonso Cesar Lelis Brandão ao longo da videoaula.</p>
    </div>
  </section>`;

const PROF = `  <section class="slide slide-prof">
    <div class="prof-grid">
      <div class="prof-lado-claro">
        <div class="prof-logo-claro">
          <svg width="200" height="49" viewBox="0 0 271 67" aria-label="UniFECAF"><use href="#logo-marca"/></svg>
        </div>
        <div class="prof-foto" role="img" aria-label="Espaço reservado para a foto do professor Afonso Cesar Lelis Brandão"></div>
      </div>
      <div class="prof-lado-escuro">
        <div class="prof-canto-topo" aria-hidden="true"><svg width="110" height="110"><use href="#prof-canto-amarelo"/></svg></div>
        <div class="prof-triangulos-boundary" aria-hidden="true">
          <svg width="200" height="100%" viewBox="0 0 200 400" preserveAspectRatio="xMidYMid meet"><use href="#prof-cluster"/></svg>
        </div>
        <div class="prof-canto-rodape" aria-hidden="true"><svg width="90" height="60" viewBox="0 0 120 80"><use href="#prof-mini-cluster"/></svg></div>
        <h2 class="prof-nome">Afonso Cesar Lelis Brandão</h2>
        <p class="prof-cargo">Professor de Engenharia Civil · UniFECAF</p>
        <p class="prof-descricao">Professor de Engenharia Civil na UniFECAF. Conduz o aluno do <strong>diagnóstico de gargalos logísticos</strong> ao <strong>projeto de infraestrutura</strong> de portos, aeroportos e ferrovias — aprendendo a <em>diagnosticar, ler e defender tecnicamente</em> soluções de transporte que poucos colegas de graduação dominam.</p>
      </div>
    </div>
  </section>`;

function deckList() {
  const out = [];
  for (const d of UNIT_DIRS) {
    if (!fs.existsSync(d)) continue;
    for (const f of fs.readdirSync(d)) if (f.endsWith('.html')) out.push(path.join(d, f));
  }
  return out;
}

let changed = 0, skipped = 0;
for (const deck of deckList()) {
  const aula = (deck.match(/aula\d+/) || ['?'])[0];
  let html = fs.readFileSync(deck, 'utf8');
  if (html.includes('class="slide slide-audio"')) {
    console.log(`${aula.padEnd(7)} SKIP (ja tem slide-audio)`);
    skipped++;
    continue;
  }
  if (!html.includes(ANCHOR)) {
    console.log(`${aula.padEnd(7)} WARN: anchor slide-sumario nao encontrado — pulando`);
    continue;
  }
  const isAula0 = aula === 'aula0';
  const block = AUDIO + (isAula0 ? '' : `\n\n${PROF}`);
  html = html.replace(ANCHOR, `${block}\n\n${ANCHOR}`);
  fs.writeFileSync(deck, html, 'utf8');
  console.log(`${aula.padEnd(7)} OK  + Audiodescricao${isAula0 ? '' : ' + Sobre o professor'}`);
  changed++;
}
console.log(`\nDecks alterados: ${changed} | pulados: ${skipped}`);
