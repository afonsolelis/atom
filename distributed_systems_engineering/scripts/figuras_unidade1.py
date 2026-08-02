#!/usr/bin/env python3
"""Gera as 13 figuras autorais da Unidade 1 em SVG + PNG.

Cada função corresponde a um "Recurso visual N" descrito em
`unidade_1/unidade_1.md`; o texto alternativo registrado aqui é o mesmo do
markdown e vai para o elemento <desc> do SVG e para a propriedade de
acessibilidade da imagem no DOCX.

Uso:
    PYTHONPATH=/tmp/dse-docx-libs python3 scripts/figuras_unidade1.py       # todas
    PYTHONPATH=/tmp/dse-docx-libs python3 scripts/figuras_unidade1.py 8 9   # só 8 e 9
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from figuras_kit import (  # noqa: E402
    AMARELO,
    AZUL,
    AZUL_CLARO,
    AZUL_MEDIO,
    BORDA,
    BRANCO,
    CINZA_BG,
    CINZA_TXT,
    MAGENTA,
    MAGENTA_TXT,
    MUTE,
    VERDE,
    VERDE_CLARO,
    Figura,
)

RAIZ = Path(__file__).resolve().parents[1]
DESTINO = RAIZ / "unidade_1" / "assets" / "figuras"


# ============================================================ Recurso visual 1
def figura_1() -> Figura:
    fig = Figura(
        1050,
        615,
        "Arquitetura distribuída da NexaOrder",
        "diagrama mostra um cliente enviando uma compra a um gateway, que se "
        "comunica com quatro serviços independentes conectados por rede.",
    )
    fig.retangulo(440, 62, 585, 452, CINZA_BG, BORDA, 2, 16, "9 7")
    fig.texto(732, 92, "Serviços autônomos — estado, execução e falha próprios", 15, MUTE)

    fig.caixa(30, 255, 150, 84, "Cliente", None, AZUL, AZUL, BRANCO)
    fig.caixa(250, 255, 175, 84, "API Gateway", "ponto único de entrada", BRANCO, AZUL)
    fig.caixa(465, 255, 195, 84, "Pedidos", "registra a intenção", BRANCO, AZUL_MEDIO, AZUL_MEDIO)
    fig.caixa(795, 112, 205, 78, "Estoque", "reserva o item", BRANCO, AZUL_MEDIO, AZUL_MEDIO)
    fig.caixa(795, 254, 205, 78, "Pagamento", "autoriza a cobrança", BRANCO, AZUL_MEDIO, AZUL_MEDIO)
    fig.caixa(795, 396, 205, 78, "Expedição", "prepara o envio", BRANCO, AZUL_MEDIO, AZUL_MEDIO)

    fig.seta(182, 297, 246, 297, AZUL)
    fig.etiqueta(214, 272, "comprar", MUTE, 14)
    fig.seta(425, 297, 462, 297, AZUL)
    fig.seta(660, 285, 792, 160, AZUL_CLARO, 2.4, "7 6")
    fig.seta(660, 297, 792, 293, AZUL_CLARO, 2.4, "7 6")
    fig.seta(660, 309, 792, 425, AZUL_CLARO, 2.4, "7 6")
    fig.etiqueta(742, 372, "mensagens pela rede", MUTE, 14, CINZA_BG)

    fig.faixa(
        30,
        540,
        995,
        52,
        "Para o cliente, uma única operação: “comprar”. Para a arquitetura, uma "
        "sequência de mensagens, estados intermediários e falhas possíveis.",
    )
    return fig


# ============================================================ Recurso visual 2
def figura_2() -> Figura:
    fig = Figura(
        1100,
        500,
        "Linha do tempo de uma falha ambígua",
        "linha do tempo evidencia que o pagamento foi processado, mas a resposta "
        "se perdeu, levando o serviço solicitante a observar apenas o timeout.",
    )
    for rotulo, y, cor in (
        ("Serviço de Pedidos", 110, AZUL),
        ("Provedor de pagamento", 310, AZUL_MEDIO),
    ):
        fig.caixa(25, y - 34, 215, 68, rotulo, None, BRANCO, cor, cor, corpo=17)
        fig.linha(250, y, 1065, y, BORDA, 2.5)

    fig.seta(330, 118, 470, 302, AZUL)
    fig.etiqueta(352, 210, "1 — POST /cobranças", AZUL, 15, BRANCO, "start")

    fig.caixa(
        500, 282, 265, 56, "2 — cobrança processada", "o efeito já ocorreu", BRANCO, VERDE, VERDE
    )

    fig.seta(800, 302, 880, 192, MAGENTA, 2.4, "8 7")
    fig.linha(866, 178, 894, 206, MAGENTA, 3.4)
    fig.linha(894, 178, 866, 206, MAGENTA, 3.4)
    fig.etiqueta(910, 260, "3 — resposta se perde", MAGENTA_TXT, 15, BRANCO, "start")

    fig.caixa(925, 82, 140, 56, "4 — timeout", None, BRANCO, MAGENTA, MAGENTA_TXT, corpo=17)

    fig.seta(250, 400, 1065, 400, MUTE, 2)
    fig.texto(1058, 428, "tempo", 15, MUTE, "end")

    fig.faixa(
        25,
        438,
        1050,
        44,
        "O silêncio observado pelo serviço de pedidos é compatível com cinco "
        "histórias diferentes — inclusive com a cobrança já efetivada.",
        CINZA_BG,
        AZUL,
    )
    return fig


# ============================================================ Recurso visual 3
def figura_3() -> Figura:
    fig = Figura(
        1050,
        625,
        "Carga versus latência",
        "gráfico relaciona carga e latência; a latência cresce lentamente até o "
        "ponto de saturação e depois aumenta de forma abrupta.",
    )
    x0, x1 = 120, 985
    y0, y1 = 470, 90
    lat_max = 900.0
    base = 60.0

    def px(u: float) -> float:
        return x0 + u * (x1 - x0)

    def py(latencia: float) -> float:
        return y0 - min(latencia, lat_max) / lat_max * (y0 - y1)

    fig.retangulo(px(0.70), y1, px(0.94) - px(0.70), y0 - y1, MAGENTA, "none", 0, 0, None, 0.07)

    for valor in (100, 300, 600, 900):
        fig.linha(x0, py(valor), x1, py(valor), BORDA, 1.2, "4 6")
        fig.texto(x0 - 14, py(valor) + 6, f"{valor} ms", 14, MUTE, "end")

    pontos = []
    passo = 0.94 / 60
    u = 0.0
    while u <= 0.94 + 1e-9:
        pontos.append((px(u), py(base / max(1e-3, 1 - u))))
        u += passo
    caminho = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pontos)
    fig.caminho(caminho, AZUL, 3.4)

    fig.linha(px(0.70), y0, px(0.70), py(200) - 6, MAGENTA, 2, "7 6")
    fig.circulo(px(0.70), py(200), 7, MAGENTA)
    fig.etiqueta(px(0.70) - 18, py(200) - 18, "ponto de saturação", MAGENTA_TXT, 15, BRANCO, "end")

    fig.seta(x0, y0, x1 + 30, y0, MUTE, 2.2)
    fig.seta(x0, y0, x0, y1 - 22, MUTE, 2.2)
    for u_marca, rotulo in ((0.25, "25%"), (0.5, "50%"), (0.7, "70%"), (0.9, "90%")):
        fig.linha(px(u_marca), y0, px(u_marca), y0 + 7, MUTE, 2)
        fig.texto(px(u_marca), y0 + 26, rotulo, 14, MUTE)

    fig.texto((x0 + x1) / 2, y0 + 56, "carga (fração da capacidade)", 15, CINZA_TXT, "middle", "600")
    fig.texto(x0 - 46, y1 - 34, "latência p95", 15, CINZA_TXT, "start", "600")
    fig.texto(px(0.80), py(430), "filas crescem;", 15, MAGENTA_TXT, "end", "600")
    fig.texto(px(0.80), py(370), "a latência dispara", 15, MAGENTA_TXT, "end", "600")

    fig.faixa(
        30,
        548,
        990,
        56,
        "Antes da saturação, mais carga custa pouca latência. Depois dela, a mesma "
        "carga adicional custa muito — por isso o percentil importa mais que a média.",
        CINZA_BG,
        AZUL,
    )
    return fig


# ============================================================ Recurso visual 4
def figura_4() -> Figura:
    fig = Figura(
        1100,
        720,
        "Estilos arquiteturais iniciais",
        "quatro pequenos diagramas comparam a organização e o fluxo de "
        "comunicação dos estilos arquiteturais apresentados.",
    )
    cartoes = [(30, 30), (565, 30), (30, 375), (565, 375)]
    largura, altura = 505, 315
    for (cx, cy) in cartoes:
        fig.retangulo(cx, cy, largura, altura, BRANCO, BORDA, 2, 14)

    # cliente-servidor
    cx, cy = cartoes[0]
    fig.texto(cx + 24, cy + 44, "Cliente-servidor", 20, AZUL, "start", "700")
    for i, yy in enumerate((cy + 90, cy + 158, cy + 226)):
        fig.caixa(cx + 34, yy, 130, 48, f"Cliente {i + 1}", None, BRANCO, AZUL_MEDIO, AZUL_MEDIO, corpo=15)
        fig.seta(cx + 168, yy + 24, cx + 288, cy + 150 + i * 32, AZUL_CLARO, 2)
    fig.caixa(cx + 292, cy + 130, 160, 104, "Servidor", None, AZUL, AZUL, BRANCO, corpo=17)
    fig.texto(cx + 24, cy + 288, "Coordenação concentrada no servidor.", 15, MUTE, "start")

    # camadas
    cx, cy = cartoes[1]
    fig.texto(cx + 24, cy + 44, "Camadas", 20, AZUL, "start", "700")
    camadas = ("Apresentação", "Aplicação", "Domínio", "Dados")
    for i, nome in enumerate(camadas):
        topo = cy + 76 + i * 50
        fig.caixa(cx + 90, topo, 320, 42, nome, None, CINZA_BG, AZUL_MEDIO, AZUL, corpo=16, raio=8)
        if i < len(camadas) - 1:
            fig.seta(cx + 250, topo + 42, cx + 250, topo + 48, AZUL_CLARO, 2, None, 7)
    fig.texto(cx + 24, cy + 288, "Coordenação entre camadas adjacentes.", 15, MUTE, "start")

    # peer-to-peer
    cx, cy = cartoes[2]
    fig.texto(cx + 24, cy + 44, "Peer-to-peer", 20, AZUL, "start", "700")
    pares = [
        (cx + 150, cy + 110),
        (cx + 350, cy + 110),
        (cx + 150, cy + 232),
        (cx + 350, cy + 232),
    ]
    for i, (ax, ay) in enumerate(pares):
        for bx, by in pares[i + 1 :]:
            fig.linha(ax, ay, bx, by, AZUL_CLARO, 2)
    for i, (ax, ay) in enumerate(pares):
        fig.circulo(ax, ay, 34, BRANCO, AZUL_MEDIO, 2.4)
        fig.texto(ax, ay + 6, f"P{i + 1}", 17, AZUL_MEDIO, "middle", "700")
    fig.texto(cx + 24, cy + 288, "Coordenação distribuída entre os pares.", 15, MUTE, "start")

    # serviços
    cx, cy = cartoes[3]
    fig.texto(cx + 24, cy + 44, "Serviços", 20, AZUL, "start", "700")
    fig.caixa(cx + 34, cy + 130, 130, 62, "Gateway", None, AZUL, AZUL, BRANCO, corpo=16)
    for i, nome in enumerate(("Pedidos", "Estoque", "Pagamento")):
        topo = cy + 84 + i * 68
        fig.caixa(cx + 258, topo, 190, 52, nome, None, BRANCO, AZUL_MEDIO, AZUL_MEDIO, corpo=16)
        fig.seta(cx + 168, cy + 161, cx + 254, topo + 26, AZUL_CLARO, 2)
    fig.texto(cx + 24, cy + 288, "Coordenação por contratos explícitos.", 15, MUTE, "start")
    return fig


# ============================================================ Recurso visual 5
def figura_5() -> Figura:
    fig = Figura(
        1150,
        700,
        "Fluxo HTTP síncrono do pedido",
        "diagrama de sequência mostra chamadas HTTP encadeadas e bloqueantes "
        "entre cliente, pedidos, estoque e pagamento até a resposta final.",
    )
    atores = [
        ("Cliente", 120, AZUL),
        ("Gateway", 340, AZUL_MEDIO),
        ("Pedidos", 590, AZUL_MEDIO),
        ("Estoque", 830, AZUL_MEDIO),
        ("Pagamento", 1050, AZUL_MEDIO),
    ]
    for nome, x, cor in atores:
        fig.caixa(x - 88, 34, 176, 58, nome, None, BRANCO, cor, cor, corpo=17)
        fig.linha(x, 92, x, 600, BORDA, 2, "6 7")

    fig.retangulo(114, 140, 12, 400, AMARELO, "none", 0, 4)

    mensagens = [
        (150, 120, 340, "POST /pedidos", AZUL, False),
        (196, 340, 590, "POST /pedidos", AZUL, False),
        (256, 590, 830, "POST /reservas", AZUL_MEDIO, False),
        (306, 830, 590, "201 reserva confirmada", VERDE, True),
        (366, 590, 1050, "POST /cobranças", AZUL_MEDIO, False),
        (432, 1050, 590, "201 cobrança autorizada", VERDE, True),
        (492, 590, 340, "201 pedido criado", VERDE, True),
        (540, 340, 120, "201 pedido criado", VERDE, True),
    ]
    for y, origem, destino, rotulo, cor, tracejado in mensagens:
        recuo = 6 if destino > origem else -6
        fig.seta(origem + recuo, y, destino - recuo, y, cor, 2.3, "8 6" if tracejado else None)
        fig.etiqueta((origem + destino) / 2, y - 12, rotulo, cor, 14)

    fig.etiqueta(150, 350, "cliente bloqueado", MAGENTA_TXT, 15, BRANCO, "start", "700")
    fig.etiqueta(150, 374, "durante toda a cadeia", MAGENTA_TXT, 15, BRANCO, "start")

    fig.faixa(
        30,
        624,
        1090,
        52,
        "A latência percebida se aproxima da soma do caminho crítico e, com etapas "
        "obrigatórias e falhas independentes, a disponibilidade é o produto das etapas.",
        CINZA_BG,
        AZUL,
    )
    return fig


# ============================================================ Recurso visual 6
def figura_6() -> Figura:
    fig = Figura(
        1150,
        600,
        "Fila versus publicação-assinatura",
        "comparação visual entre o padrão de fila, em que cada mensagem vai a um "
        "único consumidor, e o padrão de publicação-assinatura, em que cada "
        "mensagem é entregue a todos os assinantes do tópico.",
    )
    for x in (30, 590):
        fig.retangulo(x, 30, 530, 500, BRANCO, BORDA, 2, 14)

    # fila
    fig.texto(60, 74, "Fila (ponto a ponto)", 20, AZUL, "start", "700")
    fig.caixa(220, 100, 150, 54, "Produtor", None, AZUL, AZUL, BRANCO, corpo=16)
    fig.seta(295, 154, 295, 194, AZUL, 2.3)
    fig.retangulo(95, 200, 400, 64, CINZA_BG, AZUL_MEDIO, 2.2, 10)
    for i, marca in enumerate(("m1", "m2", "m3")):
        cx = 165 + i * 130
        fig.retangulo(cx - 52, 212, 104, 40, BRANCO, AZUL_MEDIO, 2, 8)
        fig.texto(cx, 239, marca, 17, AZUL_MEDIO, "middle", "700")
        fig.seta(cx, 264, 165 + i * 130, 366, AZUL_CLARO, 2.2)
        fig.caixa(165 + i * 130 - 62, 370, 124, 62, f"Instância {chr(65 + i)}", None, BRANCO, AZUL_MEDIO, AZUL_MEDIO, corpo=15)
    fig.faixa(60, 452, 470, 52, "Cada mensagem é entregue a um único consumidor entre os que competem.", CINZA_BG, AZUL, 15)

    # publicação-assinatura
    fig.texto(620, 74, "Publicação-assinatura", 20, AZUL, "start", "700")
    fig.caixa(780, 100, 150, 54, "Produtor", None, AZUL, AZUL, BRANCO, corpo=16)
    fig.seta(855, 154, 855, 194, AZUL, 2.3)
    fig.retangulo(655, 200, 400, 64, AMARELO, AMARELO, 2.2, 10)
    fig.texto(855, 239, "Tópico  PedidoCriado", 18, AZUL, "middle", "700")
    for i, nome in enumerate(("Estoque", "Fraude", "Recomendação")):
        cx = 725 + i * 130
        fig.seta(855, 264, cx, 366, VERDE, 2.2)
        fig.caixa(cx - 62, 370, 124, 62, nome, None, BRANCO, VERDE, VERDE, corpo=14)
    fig.faixa(620, 452, 470, 52, "Cada mensagem publicada é entregue a todos os assinantes do tópico.", CINZA_BG, AZUL, 15)

    fig.faixa(
        30,
        548,
        1090,
        40,
        "Novos assinantes podem ser acrescentados sem alterar o produtor — ao custo de não haver resposta imediata.",
        BRANCO,
        MUTE,
        15,
    )
    return fig


# ============================================================ Recurso visual 7
def figura_7() -> Figura:
    fig = Figura(
        1150,
        760,
        "Dois fluxos de criação de pedido",
        "diagrama comparativo mostra, à esquerda, uma cadeia de chamadas "
        "síncronas bloqueantes e, à direita, uma cadeia assíncrona que respeita "
        "as pré-condições de estoque, pagamento e expedição, sem bloquear a "
        "resposta inicial ao cliente.",
    )
    for x in (30, 590):
        fig.retangulo(x, 30, 530, 640, BRANCO, BORDA, 2, 14)

    # síncrono encadeado
    fig.texto(60, 74, "Síncrono encadeado", 20, AZUL, "start", "700")
    etapas = ("Pedidos", "Estoque", "Pagamento", "Expedição")
    for i, nome in enumerate(etapas):
        topo = 110 + i * 96
        fig.caixa(200, topo, 230, 58, nome, None, BRANCO, AZUL_MEDIO, AZUL_MEDIO, corpo=17)
        if i < len(etapas) - 1:
            fig.seta(315, topo + 58, 315, topo + 92, AZUL, 2.3)
            fig.etiqueta(325, topo + 82, "aguarda", MUTE, 13, BRANCO, "start")
    fig.caixa(60, 110, 110, 58, "Cliente", None, AZUL, AZUL, BRANCO, corpo=16)
    fig.seta(172, 139, 196, 139, AZUL, 2.3)
    fig.caminho("M 434 427 L 496 427 L 496 502 L 115 502", MAGENTA, 2.4, "none", "8 6")
    fig.seta(115, 502, 115, 174, MAGENTA, 2.4)
    fig.etiqueta(300, 490, "resposta única, após toda a cadeia", MAGENTA_TXT, 14)
    fig.faixa(60, 594, 470, 66, "Latência ≈ soma das etapas. A indisponibilidade de qualquer uma delas indisponibiliza o fluxo inteiro.", CINZA_BG, AZUL, 15)

    # orientado a eventos
    fig.texto(620, 74, "Orientado a eventos", 20, AZUL, "start", "700")
    fig.caixa(750, 104, 200, 50, "Pedidos", None, BRANCO, AZUL_MEDIO, AZUL_MEDIO, corpo=17)
    fig.seta(746, 129, 700, 129, VERDE, 2.3)
    fig.etiqueta(694, 110, "202 processando", VERDE, 14, BRANCO, "end")

    sequencia = [
        ("evento", "PedidoCriado", 168),
        ("servico", "Estoque", 230),
        ("evento", "EstoqueReservado", 292),
        ("servico", "Pagamento", 354),
        ("evento", "PagamentoAprovado", 416),
        ("servico", "Expedição", 478),
        ("evento", "PedidoEnviado", 540),
    ]
    for tipo, nome, topo in sequencia:
        if tipo == "evento":
            fig.retangulo(750, topo, 200, 44, AMARELO, AMARELO, 2, 22)
            fig.texto(850, topo + 29, nome, 15, AZUL, "middle", "700")
        else:
            fig.caixa(750, topo, 200, 44, nome, None, BRANCO, AZUL_MEDIO, AZUL_MEDIO, corpo=16, raio=10)
        if topo < 540:
            fig.seta(850, topo + 44, 850, topo + 60, MUTE, 2, None, 7)
    fig.seta(950, 182, 992, 168, VERDE, 2)
    fig.caixa(996, 146, 104, 44, "Fraude", None, BRANCO, VERDE, VERDE, corpo=14, raio=10)
    fig.seta(950, 196, 992, 224, VERDE, 2)
    fig.caixa(996, 202, 104, 44, "Recomendação", None, BRANCO, VERDE, VERDE, corpo=11, raio=10)
    fig.texto(1048, 268, "consumidores", 13, MUTE)
    fig.texto(1048, 286, "independentes", 13, MUTE)
    fig.faixa(620, 594, 470, 66, "Resposta imediata ao cliente; a sequência causal é preservada pelos eventos de pré-condição.", CINZA_BG, AZUL, 15)

    fig.faixa(
        30,
        690,
        1090,
        44,
        "Não há resposta universalmente correta: a escolha depende de quanto a experiência do cliente tolera confirmação não imediata.",
        BRANCO,
        MUTE,
        15,
    )
    return fig


# ============================================================ Recurso visual 8
def figura_8() -> Figura:
    fig = Figura(
        1150,
        640,
        "Linha do tempo dos relógios lógicos de Lamport",
        "diagrama de raias mostra os relógios lógicos de Pedidos, Estoque e "
        "Pagamento evoluindo por eventos locais e mensagens trocadas, "
        "evidenciando como o recebimento de mensagem ajusta o contador local.",
    )
    raias = (
        ("Pedidos (Pd)", 120),
        ("Estoque (Es)", 270),
        ("Pagamento (Pg)", 420),
    )
    for nome, y in raias:
        fig.caixa(25, y - 30, 195, 60, nome, None, BRANCO, AZUL_MEDIO, AZUL_MEDIO, corpo=16)
        fig.linha(230, y, 1090, y, BORDA, 2.5)

    def evento(
        x: float, y: float, carimbo: int, rotulo: str, destaque: bool = False, acima: bool = False
    ) -> None:
        fig.circulo(x, y, 17, AMARELO if destaque else BRANCO, AZUL, 2.6)
        fig.texto(x, y + 7, str(carimbo), 18, AZUL, "middle", "700")
        fig.texto(x, y - 32 if acima else y + 46, rotulo, 13, MUTE)

    # Pedidos
    evento(300, 120, 1, "local")
    evento(410, 120, 2, "envio")
    evento(770, 120, 5, "recebimento", True, acima=True)
    # Estoque
    evento(560, 270, 3, "recebimento")
    evento(660, 270, 4, "envio")
    # Pagamento — só eventos locais, sem troca de mensagem
    for i, x in enumerate((300, 380, 460, 540, 620)):
        evento(x, 420, i + 1, "local", destaque=(i == 4))

    fig.seta(424, 133, 546, 256, AZUL_CLARO, 2.4)
    fig.etiqueta(400, 205, "“reservar item”, carimbo 2", AZUL_MEDIO, 14, BRANCO, "start")
    fig.seta(674, 257, 756, 135, AZUL_CLARO, 2.4)
    fig.etiqueta(690, 205, "“reserva confirmada”, carimbo 4", AZUL_MEDIO, 14, BRANCO, "start")

    fig.retangulo(700, 348, 420, 92, CINZA_BG, MAGENTA, 2, 10, "7 6")
    fig.texto(910, 376, "Mesmo carimbo 5 nas duas raias,", 15, MAGENTA_TXT, "middle", "700")
    fig.texto(910, 400, "sem mensagem entre elas: coincidência", 15, MAGENTA_TXT)
    fig.texto(910, 424, "de contagem, não causalidade.", 15, MAGENTA_TXT)

    fig.retangulo(230, 500, 470, 56, BRANCO, AZUL, 2, 10)
    fig.texto(252, 534, "Recebimento:", 16, AZUL, "start", "700")
    fig.formula(
        382,
        534,
        [
            ("C ← max(C", "base"),
            ("local", "sub"),
            (", C", "base"),
            ("msg", "sub"),
            (") + 1", "base"),
        ],
        16,
    )

    fig.seta(230, 590, 1090, 590, MUTE, 2)
    fig.texto(1082, 614, "tempo", 15, MUTE, "end")
    return fig


# ============================================================ Recurso visual 9
def figura_9() -> Figura:
    fig = Figura(
        1050,
        540,
        "Comparação de dois relógios vetoriais concorrentes",
        "comparação posição a posição de dois relógios vetoriais evidencia que "
        "nenhum dos dois eventos precede causalmente o outro, caracterizando "
        "concorrência.",
    )
    fig.caixa(
        50, 40, 400, 104,
        "Cancelamento no Estoque",
        "V(a) = (2, 3, 0)",
        BRANCO, MAGENTA, MAGENTA_TXT, CINZA_TXT, 19, 20,
    )
    fig.caixa(
        600, 40, 400, 104,
        "Aprovação no Pagamento",
        "V(b) = (2, 1, 2)",
        BRANCO, AZUL_MEDIO, AZUL_MEDIO, CINZA_TXT, 19, 20,
    )

    fig.texto(210, 210, "posição", 15, MUTE, "middle", "700")
    fig.texto(430, 210, "V(a)", 15, MAGENTA_TXT, "middle", "700")
    fig.texto(525, 210, "", 15, MUTE)
    fig.texto(620, 210, "V(b)", 15, AZUL_MEDIO, "middle", "700")

    linhas = (
        ("Pedidos", 2, "=", 2, MUTE),
        ("Estoque", 3, ">", 1, MAGENTA_TXT),
        ("Pagamento", 0, "<", 2, AZUL_MEDIO),
    )
    for i, (nome, esquerda, simbolo, direita, cor) in enumerate(linhas):
        y = 258 + i * 62
        fig.retangulo(50, y - 30, 950, 52, CINZA_BG if i % 2 == 0 else BRANCO, "none", 0, 8)
        fig.texto(210, y + 4, nome, 17, CINZA_TXT)
        fig.texto(430, y + 4, str(esquerda), 19, MAGENTA_TXT, "middle", "700")
        fig.texto(525, y + 4, simbolo, 20, cor, "middle", "700")
        fig.texto(620, y + 4, str(direita), 19, AZUL_MEDIO, "middle", "700")
        nota = {
            "=": "empate nesta posição",
            ">": "a está à frente aqui",
            "<": "b está à frente aqui",
        }[simbolo]
        fig.texto(700, y + 4, nota, 15, MUTE, "start")

    fig.faixa(
        50,
        460,
        950,
        56,
        "Nenhum vetor domina o outro em todas as posições: os eventos são concorrentes — "
        "nenhum causou o outro.",
        AMARELO,
        AZUL,
        17,
    )
    return fig


# ============================================================ Recurso visual 10
def figura_10() -> Figura:
    fig = Figura(
        1150,
        570,
        "Ordem parcial versus ordem total",
        "comparação entre um grafo de ordem parcial, com eventos concorrentes sem "
        "relação direta, e uma linha única de ordem total, evidenciando que a "
        "ordem total não recupera relações causais inexistentes.",
    )
    for x in (30, 590):
        fig.retangulo(x, 30, 530, 420, BRANCO, BORDA, 2, 14)

    fig.texto(60, 74, "Ordem parcial (happened-before)", 19, AZUL, "start", "700")
    nos = {
        "a": (130, 180),
        "b": (290, 180),
        "d": (450, 180),
        "c": (180, 330),
        "e": (340, 350),
    }
    for origem, destino in (("a", "b"), ("b", "d"), ("c", "d")):
        ox, oy = nos[origem]
        dx, dy = nos[destino]
        angulo = ((dy - oy) ** 2 + (dx - ox) ** 2) ** 0.5
        fig.seta(
            ox + 30 * (dx - ox) / angulo,
            oy + 30 * (dy - oy) / angulo,
            dx - 32 * (dx - ox) / angulo,
            dy - 32 * (dy - oy) / angulo,
            AZUL,
            2.4,
        )
    for nome, (x, y) in nos.items():
        concorrente = nome in ("b", "e")
        fig.circulo(x, y, 28, BRANCO, MAGENTA if concorrente else AZUL_MEDIO, 3 if concorrente else 2.6)
        fig.texto(x, y + 8, nome, 20, MAGENTA_TXT if concorrente else AZUL_MEDIO, "middle", "700")
    fig.texto(60, 415, "Nenhum caminho de setas liga b a e, nem e a b:", 15, MAGENTA_TXT, "start", "600")
    fig.texto(60, 437, "são concorrentes, e nenhum causou o outro.", 15, MAGENTA_TXT, "start", "600")

    fig.texto(620, 74, "Ordem total imposta", 19, AZUL, "start", "700")
    fig.linha(650, 260, 1090, 260, BORDA, 2.5)
    for i, nome in enumerate(("a", "c", "b", "e", "d")):
        x = 690 + i * 88
        fig.circulo(x, 260, 26, BRANCO, MUTE, 2.4)
        fig.texto(x, 268, nome, 19, CINZA_TXT, "middle", "700")
        if i < 4:
            fig.seta(x + 28, 260, x + 60, 260, MUTE, 2, None, 8)
    fig.etiqueta(870, 200, "desempate por identificador de processo", MUTE, 14)
    fig.texto(620, 415, "A posição relativa de c e e é arbitrária:", 15, MUTE, "start")
    fig.texto(620, 437, "a ordem total não afirma causalidade.", 15, MUTE, "start")

    fig.faixa(
        30,
        470,
        1090,
        56,
        "Impor uma ordem total sobre eventos concorrentes produz uma decisão única e "
        "determinística — mas não recupera a causalidade que nunca existiu.",
        CINZA_BG,
        AZUL,
    )
    return fig


# ============================================================ Recurso visual 11
def figura_11() -> Figura:
    fig = Figura(
        1100,
        570,
        "Particionamento de rede entre zonas",
        "diagrama mostra duas zonas isoladas por um rompimento de rede, cada uma "
        "seguindo operante e aceitando requisições sem saber do estado da outra.",
    )
    for x, nome in ((40, "Zona de disponibilidade A"), (620, "Zona de disponibilidade B")):
        fig.retangulo(x, 80, 440, 330, BRANCO, AZUL_MEDIO, 2.2, 14)
        fig.texto(x + 220, 118, nome, 18, AZUL, "middle", "700")
        fig.caixa(x + 105, 150, 230, 78, "Réplica do estoque", "aceita reservas", BRANCO, VERDE, VERDE)
        fig.caixa(x + 130, 300, 180, 62, "Clientes locais", None, CINZA_BG, BORDA, CINZA_TXT, corpo=16)
        fig.seta(x + 220, 296, x + 220, 234, VERDE, 2.3)
        fig.etiqueta(x + 230, 272, "requisições aceitas", MUTE, 13, BRANCO, "start")

    fig.linha(484, 255, 528, 255, MUTE, 3)
    fig.linha(572, 255, 616, 255, MUTE, 3)
    fig.linha(536, 235, 564, 275, MAGENTA, 4)
    fig.linha(564, 235, 536, 275, MAGENTA, 4)
    fig.etiqueta(550, 205, "comunicação rompida", MAGENTA_TXT, 15)

    fig.faixa(
        40,
        446,
        1020,
        84,
        "Nenhum dos lados está “caído”: ambos continuam vivos e aceitando reservas para os "
        "mesmos itens. O resultado é uma divergência de estado (split-brain) que precisará "
        "ser reconciliada depois.",
        CINZA_BG,
        AZUL,
    )
    return fig


# ============================================================ Recurso visual 12
def figura_12() -> Figura:
    fig = Figura(
        1100,
        620,
        "Estados do circuit breaker",
        "diagrama de máquina de estados mostra o disjuntor alternando entre "
        "fechado, aberto e semiaberto, com as condições de transição indicadas "
        "em cada seta.",
    )
    fig.caixa(150, 230, 230, 96, "Fechado", "chamadas fluem", BRANCO, VERDE, VERDE)
    fig.caixa(720, 230, 230, 96, "Aberto", "rejeita de imediato", BRANCO, MAGENTA, MAGENTA_TXT)
    fig.caixa(435, 450, 230, 96, "Semiaberto", "chamadas de teste", BRANCO, AMARELO, AZUL)

    fig.seta(384, 262, 716, 262, MAGENTA, 2.6)
    fig.etiqueta(550, 214, "taxa de erro 12/20 = 60% > limite de 50%", MAGENTA_TXT, 15)

    fig.seta(762, 330, 636, 444, MUTE, 2.4)
    fig.etiqueta(628, 386, "após o intervalo definido", MUTE, 14, BRANCO, "end")

    fig.seta(452, 452, 300, 330, VERDE, 2.4)
    fig.etiqueta(322, 396, "testes bem-sucedidos", VERDE, 14, BRANCO, "end")

    fig.seta(690, 522, 890, 332, MAGENTA, 2.4, "8 6")
    fig.etiqueta(906, 436, "teste falhou", MAGENTA_TXT, 14, BRANCO, "start")

    fig.faixa(
        60,
        70,
        980,
        84,
        "No estado aberto, o próprio serviço de pedidos rejeita a chamada sem esperar o "
        "timeout de rede — liberando conexões para operações que não dependem da "
        "dependência degradada.",
        CINZA_BG,
        AZUL,
    )
    return fig


# ============================================================ Recurso visual 13
def figura_13() -> Figura:
    fig = Figura(
        1100,
        700,
        "Anteparos de recursos por dependência (bulkhead)",
        "diagrama mostra o serviço de pedidos dividido em dois compartimentos de "
        "recursos isolados, um para chamadas de pagamento e outro para consultas, "
        "ilustrando o padrão bulkhead.",
    )
    fig.caixa(150, 24, 264, 72, "Chamadas ao pagamento", "dependência lenta", BRANCO, MAGENTA, MAGENTA_TXT, corpo=17, corpo_sub=14)
    fig.caixa(686, 24, 264, 72, "Consultas de pedidos", "não dependem do pagamento", BRANCO, VERDE, VERDE, corpo=17, corpo_sub=14)
    fig.seta(282, 96, 282, 170, MAGENTA, 2.6)
    fig.seta(818, 96, 818, 170, VERDE, 2.6)

    fig.retangulo(120, 116, 860, 388, BRANCO, AZUL, 2.6, 16)
    fig.texto(550, 148, "Serviço de Pedidos", 20, AZUL, "middle", "700")

    def compartimento(x: float, titulo: str, cor: str, ocupadas: int, nota: str) -> None:
        fig.retangulo(x, 176, 264, 300, CINZA_BG, cor, 2.2, 12)
        fig.texto(x + 132, 212, titulo, 17, cor, "middle", "700")
        for i in range(20):
            coluna, linha = i % 5, i // 5
            cx = x + 34 + coluna * 42
            cy = 238 + linha * 44
            fig.retangulo(cx, cy, 32, 30, cor if i < ocupadas else BRANCO, cor, 1.8, 5)
        fig.texto(x + 132, 452, nota, 16, cor, "middle", "700")

    compartimento(150, "Conexões — pagamento", MAGENTA_TXT, 20, "20/20 ocupadas")
    compartimento(686, "Conexões — consultas", VERDE, 4, "4/20 ocupadas")

    fig.seta(282, 504, 282, 556, MAGENTA, 2.6)
    fig.seta(818, 504, 818, 556, VERDE, 2.6)
    fig.caixa(150, 558, 264, 72, "Esgotado", "falha rápido, sem esperar", BRANCO, MAGENTA, MAGENTA_TXT, corpo=18, corpo_sub=14)
    fig.caixa(686, 558, 264, 72, "Segue atendendo", "capacidade preservada", BRANCO, VERDE, VERDE, corpo=18, corpo_sub=14)

    fig.faixa(
        20,
        648,
        1060,
        44,
        "O esgotamento do compartimento de pagamento não consome os recursos das consultas: "
        "a degradação fica contida na dependência que a originou.",
        CINZA_BG,
        AZUL,
    )
    return fig


# ==================================================================== execução
FIGURAS = {
    1: ("figura-01-arquitetura-nexaorder", figura_1),
    2: ("figura-02-falha-ambigua", figura_2),
    3: ("figura-03-carga-latencia", figura_3),
    4: ("figura-04-estilos-arquiteturais", figura_4),
    5: ("figura-05-fluxo-http-sincrono", figura_5),
    6: ("figura-06-fila-pub-sub", figura_6),
    7: ("figura-07-dois-fluxos-pedido", figura_7),
    8: ("figura-08-relogios-lamport", figura_8),
    9: ("figura-09-vetores-concorrentes", figura_9),
    10: ("figura-10-ordem-parcial-total", figura_10),
    11: ("figura-11-particionamento-rede", figura_11),
    12: ("figura-12-circuit-breaker", figura_12),
    13: ("figura-13-bulkhead", figura_13),
}


def main(argumentos: list[str]) -> None:
    alvos = [int(a) for a in argumentos] if argumentos else sorted(FIGURAS)
    for numero in alvos:
        nome, construtor = FIGURAS[numero]
        svg, png = construtor().gravar(DESTINO / nome)
        print(f"{numero:2d}  {svg.relative_to(RAIZ)}  {png.relative_to(RAIZ)}")


if __name__ == "__main__":
    main(sys.argv[1:])
