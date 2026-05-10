from bot import bot
from config import chat_ID
import system
import time as tm

tempo_restante = 0 
tempo_inicial = 0

def contador():

    global tempo_restante
    global tempo_inicial

    while True:

        if tempo_restante > 0:

            tempo_restante -= 1

            if tempo_restante == int(tempo_inicial * 0.15):
                bot.send_message(chat_ID, 'Contagem quase acabando \n\n'
                '--------------------------------\n\n'
                '/settime - para mudar a contagem\n'
                '/time - para ver a contagem\n'
                '/acres - para acrescentar mais tempo\n'
                '/exit - para encerrar (O computador sera desligado)')

            if tempo_restante == 0:
                bot.send_message(chat_ID, 'Tempo acabou')
                system.desligamento();

        tm.sleep(1)