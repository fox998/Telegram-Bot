import telebot
import timetable
import os

bot = telebot.TeleBot(os.environ['BOT_KEY'])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Send me name of your groupe and get your timetable \
\\    for todady. For example тк-71 ")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, timetable.today_timetable(message.text))

bot.remove_webhook()
bot.polling()