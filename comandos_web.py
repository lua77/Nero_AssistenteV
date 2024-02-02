import wikipedia
import pywhatkit as kit

def wiki(pesquisar):
    resposta = wikipedia.summary(pesquisar, 5)

    return resposta


def yt(pesquisar):
    kit.playonyt('pesquisar')

