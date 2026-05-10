from bot import bot
import time as tm
from config import chat_ID
import os




def porcentagem(p):
    
    p = p/100
    return p;


def desligamento():

    bot.send_message(chat_ID, 'Desligando em 60 segundos... \n\n'
                '--------------------------------\n\n'
                '/cancel - para cancelar a ação')
    
    os.system('shutdown /s /t 60')
