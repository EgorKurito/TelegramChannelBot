# Импорт нужных библиотек и пакетов
import telegram, logging
import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler

from datetime import datetime
from time import sleep

# Основные переменные
updater = Updater(token = '280467809:AAG9oeB9H2zsgHy-eZLz_YpuqXO7Mi8pQ3I')

# BlogForMan time
BFM_morning = ('9:45')
BFM_day = ('14:45')
BFM_evening = ('19:45')
# OhWhoops time
OW_morning = ('10:15')
OW_day = ('15:15')
OW_evening = ('20:15')

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
        if time_x in BFM_morning:
            blogforman(bot, update)
            sleep(59)
        if time_x in BFM_day:
            blogforman(bot, update)
            sleep(59)
        if time_x in BFM_evening:
            blogforman(bot, update)
            sleep(59)
        if time_x in OW_morning:
            ohwhoops(bot, update)
            sleep(59)
        if time_x in OW_day:
            ohwhoops(bot, update)
            sleep(59)
        if time_x in OW_evening:
            ohwhoops(bot, update)
            sleep(59)

# Функция отвечающая за парсинг фото для 'BlogForMan'
def blogforman(bot, update):
    i = 0
    while True:
        for file in os.listdir("blogforman_images/"):
            if file.split('.')[-1] == 'jpg':
                bot.sendPhoto(chat_id = '@blogforman', photo = open('blogforman_images/' + file, 'rb'))
                os.remove('blogforman_images/' + file)
                i = i+1
                if i >4:
                    return False

# Функция отвечающая за парсинг фото для 'Oh Whoops'
def ohwhoops(bot, update):
    n = 0
    while True:
        for file in os.listdir("ohwhoops_images/"):
            if file.split('.')[-1] == 'jpg':
                bot.sendPhoto(chat_id = '@ohwhoops', photo = open('ohwhoops_images/' + file, 'rb'))
                os.remove('ohwhoops_images/' + file)
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
