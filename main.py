# from flask import Flask, request
# import telebot
# import time
# import timetable
# import os
# import logging


# BOT_KEY = os.environ['BOT_KEY']
# bot = telebot.TeleBot(BOT_KEY)

# heroku_url = f'https://protected-hollows-60635.herokuapp.com/{BOT_KEY}/'

# bot.remove_webhook()
# time.sleep(2)
# bot.set_webhook(url=heroku_url)

# app = Flask(__name__)

# logger = telebot.logger
# telebot.logger.setLevel(logging.INFO)

# @app.route(f'/{BOT_KEY}/', methods=["POST"])
# def webhook():
#     bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
#     print("Message")
#     return "ok", 200


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Send me name of your groupe and get your timetable \
# \\    for todady. For example тк-71 ")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, timetable.today_timetable(message.text))


# app.run(debug=True, port=8443)
# #https://protected-hollows-60635.herokuapp.com/

import os

from flask import Flask, request

import telebot

TOKEN = os.environ['BOT_KEY']
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your_heroku_project.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8443)))