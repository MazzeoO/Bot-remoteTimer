from bot import bot
import os
import tim

@bot.message_handler(['start'])
def start(msg):
    bot.reply_to(msg, 'Bem-Vindo \n\n'
                '--------------------------------\n\n'
                '/settime - para mudar a contagem\n'
                '/time - para ver a contagem\n'
                '/exit - para encerrar (O computador sera desligado)')
    teste = True

@bot.message_handler(commands=['id']) #para descobrir o ID do chat
def pegar_id(msg):

    bot.reply_to(msg, f"Seu ID é: {msg.chat.id}")

@bot.message_handler(commands=['settime'])
def settempo(msg):

    texto = msg.text.split()

    if len(texto) > 1:

        tim.tempo_restante = int(texto[1])
        tim.tempo_inicial = tim.tempo_restante

        bot.reply_to(msg, f"Tempo definido: {tim.tempo_restante} segundos")

    else:
        bot.reply_to(msg, "Use: /settime 60")

@bot.message_handler(commands=['time'])
def tempo(msg):

    minutos = tim.tempo_restante // 60
    segundos = tim.tempo_restante % 60

    bot.reply_to(
        msg,
        f"Tempo restante: {minutos:02d}:{segundos:02d}"
    )

@bot.message_handler(commands=['acres'])
def acres(msg):

    texto = msg.text.split()

    if len(texto) > 1:

        acrescimo = int(texto[1])
        tim.tempo_restante += acrescimo
        tim.tempo_inicial = tim.tempo_restante

        bot.reply_to(msg, f"Tempo definido: {tim.tempo_restante} segundos")

    else:
        bot.reply_to(msg, "Use: /acres 60")


@bot.message_handler(commands=['exit'])
def exit(msg):


    bot.reply_to(msg, 'Desligando em 60 segundos... \n\n'
                '--------------------------------\n\n'
                '/cancel - para cancelar a ação')
    

    os.system('shutdown /s /t 60')

@bot.message_handler(commands=['cancel'])
def cancel(msg):

    os.system('shutdown /a')

    bot.reply_to(msg, 'Desligamento CANCELADO! \n\n'
                '--------------------------------\n\n'
                '/settime - para mudar a contagem\n'
                '/time - para ver a contagem\n'
                '/exit - para encerrar (O computador sera desligado)')
    