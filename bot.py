# from secrets import choice
# import telebot
# from telebot import types
# from config import TOKEN
# bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['start'])
# def start(message):
#     text = "Привет друг, сегодня мы узнаем о погоде"
#     bot.send_message(message.chat.id, text)
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     item1 = types.KeyboardButton('Покажи погоду')
#     item2 = types.KeyboardButton('Покажи дату')
#     item3 = types.KeyboardButton('Покажи число')

#     markup.add(item1, item2, item3)
#     text = 'Выбери действие'
#     bot.send_message(message.chat.id, text, reply_markup=markup)
# @bot.message_handler(content_types=['text'])
# def lol(message):
#     if message.chat.type=='private':
#         text = pop(message.text)
#         bot.send_message(message.chat.id, result[1])
# bot.polling(non_stop=True)

import telebot
from telebot import types
from config import TOKEN
from main import furunkl

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    text = "Hello everyone, I`m weather bot, send me your city name"
    bot.send_message(message.chat.id, text)


@bot.message_handler(content_types=['text'])
def lol(message):
    if message.chat.type == "private":
        text = furunkl(message.text)
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)