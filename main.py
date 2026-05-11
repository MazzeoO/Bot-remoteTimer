# Bot-remoteTimer
# Author: Gabriel Mazzeo

import threading
from bot import bot
from tim import contador
import comandos
import config

threading.Thread(target=contador, daemon=True).start()

bot.send_message(config.chat_ID, 'Bot Iniciado...')

bot.infinity_polling()