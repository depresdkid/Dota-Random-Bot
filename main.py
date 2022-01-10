import telebot
from random import randint

import api
import config as cf

api = api.Api(cf.STEAM_TOKEN)

bot = telebot.TeleBot(cf.TELEGRAM_TOKEN)

markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
rand_bun = telebot.types.KeyboardButton('Рандом')

markup.add(rand_bun)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет {0.first_name}!'.format(
        message.from_user), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_comand(message):
    if(message.text == 'Рандом'):
        # после 303 идут лесные и ивентовые айтемы
        item_num = randint(0, 303)
        if api.items[item_num].startswith("Рецепт"):
            item_num += 1
        bot.send_message(
            message.chat.id, api.heroes[randint(0, len(api.heroes) - 1)] + " через " + api.items[item_num])


bot.polling(non_stop=True)
