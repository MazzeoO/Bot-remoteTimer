from bot import bot
import os
import tim
import volume as vol

@bot.message_handler(['start'])
def start(msg):
    bot.reply_to(msg, 'Bem-Vindo \n\n'
                '--------------------------------\n\n'
                '/settime - para mudar a contagem\n'
                '/time - para ver a contagem\n\n' \
                '/volume- menu de configuração do menu\n'
                '/exit - para encerrar (O computador sera desligado)')

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
    


# --------- VOLUME ---------------

@bot.message_handler(commands=['volume'])
def volume(msg):

     bot.reply_to(msg, f'Configurações de Volume \n\n'
                '--------------------------------\n\n' \
                'Volume Atual: \n\n'
                '/setvol - para mudar o Volume\n'
                '/volup - para aumentar o volume 1%\n'
                '/voludown - para abaixar o volume 1%\n' \
                '/mt - muta e desmuta o volume')
     

@bot.message_handler(commands=['setvol'])
def volume(msg):

    texto = msg.text.split()

    if len(texto) > 1:

        vol.setVol(int(texto[1]))

        bot.reply_to(msg, f"Volume mudado para: {texto[1]}%")

    else:
        bot.reply_to(msg, "Use: /setvol 50")



@bot.message_handler(commands=['volup'])
def volup(msg):

        volA = vol.volup()

        bot.reply_to(msg, f"Volume aumentado para: {volA}%")



@bot.message_handler(commands=['voldown'])
def voldown(msg):

        volA = vol.voldown()

        bot.reply_to(msg, f"Volume Abaixado para: {volA}%")


@bot.message_handler(commands=['mt'])
def mt(msg):

        m = vol.volmute()

        if m == 1:
             bot.reply_to(msg, f"Volume Mutado")
        elif m == 0:
             bot.reply_to(msg, f"Volume Demutado")