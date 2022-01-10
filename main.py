import telebot
import requests
from random import randint
import config as cf


def get_list(list):
    hero_name = []
    list = list.json().get('result').get('heroes')
    if(not(list)):
        return 'Ошибка! Список героев не получен'
    for element in list:
        hero_name.append(element['localized_name'])
    return hero_name


def get_hero(token):
    response = requests.get(
        'https://api.steampowered.com/IEconDOTA2_570/GetHeroes/v0001/', params={'key': token, 'language': 'ru'})
    if response.status_code == 200:
        return get_list(response)
    else:
        print('Ошибка запроса')


heroes = get_hero(cf.STEAM_TOKEN)


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
        count_hero = randint(0, len(heroes) - 1)
        bot.send_message(
            message.chat.id, heroes[count_hero])


bot.polling(non_stop=True)
