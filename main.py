import speech_recognition as sr #reconhecimento de voz
import pyttsx3 #texto para fala
from datetime import datetime
from comandos_web import yt, wiki
from random import choice
import os

machine = pyttsx3.init()
r = sr.Recognizer()


def falar(texto):
    # funcao responsavel pelas falas
    machine.say(texto)
    machine.runAndWait()


def cumprimetar():
    # meus cumprimentos
    hour = datetime.now().hour
    now = datetime.now()

    if (hour >= 6) and (hour < 12):
        falar(f'Bom dia senhor')
        periodo = 'manhã'

    elif (hour >= 12) and (hour < 18):
        falar(f'Boa tarde senhor')
        periodo = 'tarde'

    elif (hour >= 18) and (hour < 24):
        falar(f'Boa noite senhor')
        periodo = 'noite'

    elif (hour >= 24) and (hour < 6):
        falar('Olá senhor, sem sono?')
        periodo = 'madrugada'

    falar(f'Eu sou o Nero, como posso te ajudar nesta {periodo}?')


def captura_comando():
    #função responsavel por identificar se existe um comando ou não
    with sr.Microphone() as source:
        print('Escutando...')
        voz = r.listen(source)

        try:

            print('Compreendendo...')

            comando = r.recognize_google(voz, language='pt-BR')

            print(f'Comando: {comando}')

            return comando

        except Exception as e:

            print(f'Erro ao rconhecer o comando: {e}')

            return None

if __name__ == '__main__':

    while True:
        comando = captura_comando().lower()

        if 'nero' in comando:
            cumprimetar()

        if 'encerrar' in comando or 'parar' in comando:

            hour = datetime.now().hour
            if hour >= 18 or hour < 6:
                falar('Tenha uma boa noite senhor!')
            else:
                falar('Tenha um bom dia, se cuide!')
                break

        elif 'youtube' in comando:
            falar('O que vamos ver no youtube?')
            pesquisar = captura_comando().lower()
            yt(pesquisar)
            falar('Abrindo o vídeo...')

        elif 'wikipedia' in comando:
            falar('O que quer que eu procure na wiki?')
            pesquisar = captura_comando().lower()
            resposta = wiki(pesquisar)
            falar(f'De acordo com a wikipedia: {resposta}')
            falar('Por praticidade, estarei escrevendo os resultados senhor')
            print(resposta)

        pass