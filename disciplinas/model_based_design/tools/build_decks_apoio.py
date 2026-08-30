#!/usr/bin/env python3
"""Gera os decks de apoio que faltavam nas videoaulas 1–4 e 6–8.

Reaproveita o sistema visual do deck validado da Aula 9 e produz arquivos
HTML autocontidos. Os decks são cartões de apoio; a demonstração principal
continua ocorrendo no terminal/editor, conforme os roteiros de 20 minutos.
"""

from __future__ import annotations

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
BASE = ROOT / "unidade_3/slides/aula9.html"

DECKS = {
    1: {
        "unidade": 1,
        "titulo": "O NexaBot que esquece a própria velocidade",
        "sumario": ["CPS e ciclo MBD", "Modelo físico do motor", "Malha aberta sob carga", "Contrato reproduzível"],
        "conceitos": [
            ("Do físico ao executável", "Motor, engrenagem, roda, sensor e software precisam aparecer no mesmo argumento de engenharia."),
            ("Modelo mínimo", "Corrente e velocidade angular formam os estados; tensão é a entrada e velocidade é a saída."),
            ("Resultado central", "Com 12 V e carga variável, a malha aberta não sustenta a velocidade: o erro motiva a realimentação."),
        ],
        "comandos": ["aula_01/01_ambiente.py", "aula_01/02_malha_aberta.py", "aula_01/03_ciclo_mbd.py", "aula_01/04_v_model.py"],
        "atividade": "Altere a carga no script de malha aberta, registre a velocidade final e explique por que o modelo é necessário antes do controlador.",
    },
    2: {
        "unidade": 1,
        "titulo": "Um motor sem manual: identificando parâmetros",
        "sumario": ["Equações elétrica e mecânica", "Espaço de estados", "Dados de ensaio", "Validação retida"],
        "conceitos": [
            ("Estados físicos", "A corrente responde rapidamente; a velocidade carrega a dinâmica mecânica mais lenta."),
            ("Identificação", "O ajuste usa mínimos quadrados não lineares com região de confiança, sem chamar TRF de Levenberg–Marquardt."),
            ("Validação", "Ajuste e validação usam conjuntos distintos; erro baixo no ajuste não prova generalização."),
        ],
        "comandos": ["aula_02/01_espaco_estados.py", "aula_02/02_gera_dados.py", "aula_02/03_identifica.py", "aula_02/04_valida.py"],
        "atividade": "Repita a identificação com outra semente de ruído e compare erro de ajuste, erro retido e parâmetros recuperados.",
    },
    3: {
        "unidade": 1,
        "titulo": "Dois polos, uma pergunta: dá para ignorar o mais rápido?",
        "sumario": ["Função de transferência", "Polos e escalas", "Bode e margem", "Ganho proporcional"],
        "conceitos": [
            ("Constantes exatas", "Os polos dão aproximadamente 2,98 ms e 138,60 ms; L/R e a aproximação mecânica são valores desacoplados."),
            ("Estabilidade contínua", "Para a planta de segunda ordem do laboratório, não existe ganho proporcional positivo finito que cruze a instabilidade."),
            ("Limite da conclusão", "Estabilidade não garante desempenho, robustez nem respeito ao limite de 24 V."),
        ],
        "comandos": ["aula_03/01_funcao_transferencia.py", "aula_03/02_polos.py", "aula_03/03_bode.py", "aula_03/04_estabilidade.py"],
        "atividade": "Varra ganhos proporcionais positivos e diferencie estabilidade, margem e qualidade da resposta.",
    },
    4: {
        "unidade": 1,
        "titulo": "Correto na matemática, impossível no driver",
        "sumario": ["Controlabilidade", "Observabilidade", "Realimentação", "Restrição de 24 V"],
        "conceitos": [
            ("Posto pleno", "Controlabilidade e observabilidade dizem o que é possível no modelo linear, não o esforço físico exigido."),
            ("Realimentação e observador", "O laboratório calcula polos, ganho de estado e reconstrução dos estados a partir da saída."),
            ("Resultado central", "Todas as combinações LQR testadas excedem 24 V; a especificação precisa ser reformulada."),
        ],
        "comandos": ["aula_04/01_controlabilidade.py", "aula_04/02_pole_placement.py", "aula_04/03_lqr.py", "aula_04/04_observador.py"],
        "atividade": "Aumente a penalização do esforço no LQR ou relaxe a dinâmica e procure uma solução compatível com o driver.",
    },
    6: {
        "unidade": 2,
        "titulo": "O integrador que não sabia parar",
        "sumario": ["PID e métricas", "Ziegler–Nichols", "Saturação", "Anti-windup"],
        "conceitos": [
            ("Sintonia é ponto de partida", "Ganho crítico e período crítico geram uma regra inicial; requisitos de sobressinal e acomodação decidem a aceitação."),
            ("Windup", "Comando calculado além de ±24 V continua carregando o integrador e piora a recuperação."),
            ("Back-calculation", "A diferença entre comando saturado e não saturado realimenta o integrador e limita o acúmulo."),
        ],
        "comandos": ["aula_06/01_ganho_critico.py", "aula_06/02_ziegler_nichols.py", "aula_06/03_anti_windup.py", "aula_06/04_compara_sintonias.py"],
        "atividade": "Compare duas sintonias com a mesma referência, reportando sobressinal, acomodação, ISE e tempo em saturação.",
    },
    7: {
        "unidade": 2,
        "titulo": "Trinta amostras por constante de tempo",
        "sumario": ["Euler, Tustin e ZOH", "Contrato discreto", "Varredura de Ts", "Atraso de um ciclo"],
        "conceitos": [
            ("Amostragem nominal", "Ts=5 ms representa 27,7 amostras pela constante modal exata e 29,6 pela aproximação desacoplada."),
            ("Duas fronteiras", "O modelo linear cruza |p|=1 em 27,70 ms; a simulação saturada só é classificada instável perto de 44,34 ms."),
            ("Atraso importa", "Em Ts=5 ms, um ciclo de atraso reduz a margem de fase de cerca de 66,19° para 43,61°."),
        ],
        "comandos": ["aula_07/01_euler_tustin_zoh.py", "aula_07/02_escolha_de_ts.py", "aula_07/03_atraso_um_ciclo.py"],
        "atividade": "Repita a varredura com a sintonia PI e compare o limite linear com a classificação não linear saturada.",
    },
    8: {
        "unidade": 2,
        "titulo": "Dois relógios, um só resultado",
        "sumario": ["FMI 3.0", "Model Exchange e Co-Simulation", "Passo de comunicação", "Erro de acoplamento"],
        "conceitos": [
            ("FMU isolada", "A planta empacotada reproduz a referência monolítica com erro numérico desprezível."),
            ("Acoplamento", "O erro cresce monotonicamente quando o passo de comunicação aumenta de 1 para 50 ms."),
            ("Leitura correta", "Nos passos testados a co-simulação permanece limitada; erro crescente não deve ser rebatizado como divergência."),
        ],
        "comandos": ["aula_08/01_build_fmu.py", "aula_08/02_inspeciona_fmu.py", "aula_08/03_cosim.py", "aula_08/04_erro_de_acoplamento.py"],
        "atividade": "Use bisseção para encontrar o maior passo cujo erro RMS fique abaixo de 1% da amplitude de referência.",
    },
}


def slide(classe: str, conteudo: str, aula: int, unidade: int) -> str:
    return f'''<section class="slide {classe}">
  <div class="mosaico-bg"><svg preserveAspectRatio="none"><use href="#mosaico-frame"/></svg></div>
  <div class="slide-content">{conteudo}</div>
  <div class="slide-footer"><span>Model-Based Design · Unidade {unidade}</span><span>Aula {aula} — Videoaula {aula}</span></div>
</section>'''


def montar(aula: int, dados: dict, prefixo: str, sufixo: str) -> str:
    unidade = dados["unidade"]
    titulo = escape(dados["titulo"])
    secoes = []
    secoes.append(slide("slide-capa active", f'<p class="kicker">Model-Based Design for Cyber-Physical Systems</p><h1>Aula {aula}</h1><h2>{titulo}</h2>', aula, unidade))
    secoes.append(slide("", '<p class="kicker">Acessibilidade</p><h2>Audiodescrição</h2><div class="slide-content-box"><p>Deck com identidade UniFECAF: fundo azul-marinho, triângulos amarelos, verdes e cianos e cartões claros. A aula alterna estes cartões com editor e terminal; comandos são exibidos em fonte monoespaçada.</p></div>', aula, unidade))
    secoes.append(slide("slide-prof", '<p class="kicker">Sobre o professor</p><h2>Afonso Cesar Lelis Brandão</h2><div class="slide-content-box"><p>Professor-conteudista da disciplina. Nesta videoaula, conduz a demonstração reproduzível do NexaBot com ferramentas abertas em Python.</p></div>', aula, unidade))
    itens = "".join(f"<li>{escape(x)}</li>" for x in dados["sumario"])
    secoes.append(slide("slide-section", f'<p class="kicker">Título + sumário</p><h2>{titulo}</h2><div class="slide-content-box"><ol class="lista-numerada">{itens}</ol></div>', aula, unidade))
    for cabecalho, texto in dados["conceitos"]:
        secoes.append(slide("", f'<p class="kicker">Conceito-chave</p><h2>{escape(cabecalho)}</h2><div class="slide-content-box"><p>{escape(texto)}</p></div>', aula, unidade))
    comandos = "<br>".join(f'<span class="prompt">$</span>.venv/bin/python {escape(c)}' for c in dados["comandos"])
    secoes.append(slide("", f'<p class="kicker">TELA: terminal</p><h2>Demonstração reproduzível</h2><div class="slide-content-box"><div class="codigo-bloco">{comandos}</div><p>Execute na ordem e compare a saída com o roteiro da aula.</p></div>', aula, unidade))
    secoes.append(slide("", f'<p class="kicker">Atividade prática</p><h2>Agora é sua vez</h2><div class="slide-content-box"><p>{escape(dados["atividade"])}</p></div>', aula, unidade))
    secoes.append(slide("slide-fim", f'<p class="kicker">Encerramento</p><h1>Aula {aula} concluída</h1><p>{titulo}</p>', aula, unidade))
    titulo_html = f"Aula {aula} — {titulo} · Model-Based Design"
    prefixo_aula = prefixo.replace("Aula 9 — Um requisito, três leituras: da ambiguidade à propriedade formal · Model-Based Design", titulo_html)
    return prefixo_aula + '<div class="deck" id="deck">\n' + "\n".join(secoes) + "\n</div>\n\n" + sufixo


def main() -> None:
    base = BASE.read_text(encoding="utf-8")
    prefixo, restante = base.split('<div class="deck" id="deck">', 1)
    _, sufixo = restante.split("<!-- Navegação -->", 1)
    sufixo = "<!-- Navegação -->" + sufixo
    for aula, dados in DECKS.items():
        destino = ROOT / f"unidade_{dados['unidade']}/slides/aula{aula}.html"
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(montar(aula, dados, prefixo, sufixo), encoding="utf-8")
        print(f"[ok] {destino.relative_to(ROOT)}")

    # Alguns decks recebidos já seguiam o visual novo, mas não continham o
    # slide "Sobre o professor". Insere-o logo após a Audiodescrição.
    bloco_prof = '''
<section class="slide slide-prof">
  <div class="mosaico-bg"><svg preserveAspectRatio="none"><use href="#mosaico-frame"/></svg></div>
  <div class="slide-content">
    <p class="kicker">Sobre o professor</p>
    <h2>Afonso Cesar Lelis Brandão</h2>
    <div class="slide-content-box"><p>Professor-conteudista da disciplina. Conduz a jornada prática do NexaBot com modelos executáveis, Python e ferramentas abertas.</p></div>
  </div>
</section>
'''
    finais = [ROOT / f"unidade_{(a - 1) // 4 + 1}/slides/aula{a}.html" for a in range(1, 17)]
    fragmentos = sorted((ROOT / "unidade_4/slides").glob("_body*.html"))
    for destino in finais + fragmentos:
        texto = destino.read_text(encoding="utf-8")
        if 'class="slide slide-prof"' in texto:
            continue
        inicio = texto.find('class="slide slide-audio"')
        if inicio < 0:
            raise RuntimeError(f"slide de Audiodescrição não encontrado em {destino}")
        fim = texto.find("</section>", inicio)
        if fim < 0:
            raise RuntimeError(f"fim do slide de Audiodescrição não encontrado em {destino}")
        fim += len("</section>")
        destino.write_text(texto[:fim] + "\n" + bloco_prof + texto[fim:], encoding="utf-8")
        print(f"[ok] slide-prof inserido em {destino.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
