from rich.console import Console

import pyautogui
import random
import time


console = Console()
console.print("Início:", time.strftime("%H:%M:%S"))


TEXTOS = [
    "top demais",
    "ok",
    "demais",
    "uau",
    "wowwww",
    "amem",
    "eu esses dias",
    "q",
]

TEXTOS.extend(
    [
        "triste isso",
        "kkkkkkkkkk",
        "sempre",
        "chega de internet",
        "amo isso",
        "Adorei!",
        "Que demais!",
        "Muito útil, obrigado!",
        "Hahaha ótimo!",
        "Incrível produção!",
        "Gostei demais do conteúdo",
        "Compartilhei com os amigos",
        "Mais vídeos assim, por favor!",
        "Ótima edição!",
        "Qual é a música?",
        "Marquei alguém que vai curtir",
        "Excelente trabalho!",
        "Interessante, aprendi algo novo",
        "Top demais",
        "Chorei de rir",
        "Sensacional!",
        "Vou tentar fazer também",
        "Perfeito, voltarei a ver",
        "Isso me inspirou",
        "Simplesmente maravilhoso!",
        "Fiquei impressionado",
        "Uau, que qualidade!",
        "Esse vídeo merece mais views",
        "Gostei muito da ideia",
        "Já salvei aqui",
        "Mandou bem!",
        "Quero mais conteúdos assim",
        "Valeu por compartilhar!",
        "Ficou muito bom",
        "Aprendi muito com isso",
        "Que vídeo incrível!",
        "Muito criativo",
        "Show de bola!",
        "Eu precisava ver isso hoje",
        "Genial!",
        "Estou sem palavras",
        "Gostei do jeito que foi explicado",
        "Esse conteúdo é ouro",
        "Incrível como ficou bem feito",
        "Parabéns pelo trabalho",
        "Muito top",
        "Tô impressionado com isso",
        "Não sabia disso",
        "Assistiria mil vezes",
        "Já estou seguindo a página",
        "Quero parte 2",
        "Simplesmente perfeito",
        "Muita criatividade",
        "Gostei demais dessa ideia",
        "Amei cada segundo",
        "Muito bem feito",
        "Isso sim é conteúdo de qualidade",
        "Sensacional a forma como foi feito",
        "Esse vídeo merece ser visto",
        "Ficou excelente",
        "Gostei tanto que assisti duas vezes",
        "Quero mais dicas assim",
        "Maravilhoso trabalho",
        "Ficou perfeito!",
        "Incrível ver isso",
        "Muito interessante mesmo",
        "Ficou demais",
        "Curti muito",
        "Ótima dica",
        "Aprendi algo novo hoje",
        "Que capricho!",
        "Esse vídeo é inspirador",
        "Mandou muito bem!",
        "Muito bom conteúdo",
        "Que lindo!",
        "Gostei do estilo do vídeo",
        "Ótimo conteúdo",
        "Parabéns, ficou incrível",
        "Top top top",
        "Muito bacana",
        "Adorei a criatividade",
        "Super interessante",
        "Isso é muito bom!",
        "Quero compartilhar com todo mundo",
        "Essa edição tá demais",
        "Que vídeo divertido",
        "Gostei bastante",
        "Fenomenal!",
        "Que talento!",
        "Muito bem explicado",
        "Amei!",
        "Espetacular!",
        "Gostei de cada detalhe",
        "Muito massa!",
        "Curti demais",
        "Ficou show!",
        "Gostei e já segui",
        "Vídeo incrível",
        "Muito show",
        "Incrível ideia",
        "Gostei do resultado",
        "Parabéns pela criatividade",
        "Bom demais",
        "Muito bem pensado",
        "Adorei o conteúdo",
        "Excelente dica",
    ]
)


class Acao:
    def __init__(self, nome, x, y):
        self.nome = nome
        self.x = x
        self.y = y

    def click(self):
        pyautogui.mouseDown(self.x, self.y)
        pyautogui.mouseUp()

    def digitar(self):
        # coment_input.click()

        texto = random.choice(TEXTOS)
        console.print("Texto:", texto)
        pyautogui.typewrite(texto)
        pyautogui.keyDown("enter")
        pyautogui.KEYBOARD_KEYS


proximo = Acao("proximo", 3000, 587)
like = Acao("like", 2440, 562)
comentario = Acao("comentario", 1288, 874)
coment_input = Acao("comentando", 3535, 1011)

# estranho

# proximo = Acao("proximo", 1114, 519)
# like = Acao("like", 788, 617)
# coment_input = Acao("comentando", 1368, 796)

_gostou = False
_comentou = False


def obter_acao(padrao: Acao = None):
    global _gostou
    global _comentou

    gostou_numero = random.randint(0, 100)
    if gostou_numero < 25 and not _gostou:
        _gostou = True
        return like
    elif _gostou:
        _gostou = False

    coment_numero = random.randint(0, 100)
    if coment_numero < 3 and not _comentou:
        _comentou = True
        return coment_input
    elif _comentou:
        _comentou = False

    return padrao


def obter_segundos_espera():
    if not _gostou:
        return random.randint(6, 16)
    else:
        return random.randint(10, 20)


while True:
    _a = obter_acao(proximo)
    console.print(f"Ação: {_a.nome}")
    _a.click()

    if _comentou:
        _a.digitar()

    _espera = obter_segundos_espera()

    while _espera > 0:
        with console.status(f"Aguardando {_espera} segundos") as espera_status:
            time.sleep(1)
            _espera -= 1
            espera_status.update(f"Aguardando {_espera} segundos")
