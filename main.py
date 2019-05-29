from flask import Flask, request
import telebot
import time
import timetable
import os


BOT_KEY = os.environ['BOT_KEY']
bot = telebot.TeleBot(BOT_KEY)

heroku_url = 'https://protected-hollows-60635.herokuapp.com/'

bot.remove_webhook()
time.sleep(2)
bot.set_webhook(url=heroku_url)

app = Flask(__name__)


@app.route('/', methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Send me name of your groupe and get your timetable \
\\    for todady. For example тк-71 ")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, timetable.today_timetable(message.text))


app.run(debug=True)
#https://protected-hollows-60635.herokuapp.com/

