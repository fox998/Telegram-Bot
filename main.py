import telebot
import timetable

bot = telebot.TeleBot("896283170:AAEvIuBZNbjtqAnDC8B3ZBgJtuMP5V3AL0g")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, timetable.today_timetable(message.text))

bot.polling()
