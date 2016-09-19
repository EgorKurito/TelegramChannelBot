# Импорт нужных библиотек и пакетов
import telegram, logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler

from datetime import datetime
from time import sleep

# Основные переменные
updater = Updater(token = BOT_TOKEN)

# 
x_morning = (time)
x_day = (time)
x_evening = (time)
# 
y_morning = (time)
y_day = (time)
y_evening = (time)

# Логи бота
root = logging.getLogger()
root.setLevel(logging.INFO)

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  level = logging.INFO)

logger = logging.getLogger(__name__)

# Старт бота
def start(bot, update):
    bot.sendMessage(chat_id = update.message.chat_id, text = "Запущен")

    while True:
        d = datetime.today()
        time_x = d.strftime('%H:%M')
        if time_x in x_morning:
            blogforman(bot, update)
            sleep(59)
        if time_x in x_day:
            blogforman(bot, update)
            sleep(59)
        if time_x in x_evening:
            blogforman(bot, update)
            sleep(59)
        if time_x in y_morning:
            ohwhoops(bot, update)
            sleep(59)
        if time_x in y_day:
            ohwhoops(bot, update)
            sleep(59)
        if time_x in y_evening:
            ohwhoops(bot, update)
            sleep(59)

# Функция отвечающая за парсинг фото для 'channelexample'
def blogforman(bot, update):
    i = 0
    while True:
        for file in os.listdir("images/"):
            if file.split('.')[-1] == 'jpg':
                bot.sendPhoto(chat_id = '@channelexample', photo = open('images/' + file, 'rb'))
                os.remove('images/' + file)
                i = i+1
                if i >4:
                    return False

# Функция отвечающая за парсинг фото для 'channelexample'
def ohwhoops(bot, update):
    n = 0
    while True:
        for file in os.listdir("images/"):
            if file.split('.')[-1] == 'jpg':
                bot.sendPhoto(chat_id = '@channelexample', photo = open('images/' + file, 'rb'))
                os.remove('images/' + file)
                n = n+1
                if n >4:
                    return False

# Главная функция запускающая процессы в боте
def main():
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
