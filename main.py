
import os

from flask import Flask, request

import telebot

import timetable

TOKEN = os.environ['BOT_KEY']
SECRET = os.environ['SERET']
HEROKU_APP_URL = os.environ['HEROKU_APP_URL']

bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Send me name of your groupe and get your timetable \
\\    for todady. For example тк-71 ")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, timetable.today_timetable(message.text))


@server.route(f'/{TOKEN}', methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route(f"/{SECRET}")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f'{HEROKU_APP_URL}/{TOKEN}')
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
