import telebot
import d2api
from telebot import types
import random
import config as cf

api = d2api.APIWrapper(cf.STEAM_TOKEN)
heroes = api.get_heroes(language='ru', itemizedonly=True).get('heroes')



bot = telebot.TeleBot(cf.TELEGRAM_TOKEN)

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
rand_bun = types.KeyboardButton('Рандом')

markup.add(rand_bun)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет {0.first_name}!'.format(message.from_user), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_comand(message):

    if(message.text == 'Рандом'):
        count_hero = random.randint(0, len(heroes))
        bot.send_message(message.chat.id, heroes[count_hero].get('localized_name'))

bot.polling(non_stop=True)
