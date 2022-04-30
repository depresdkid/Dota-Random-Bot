from random import randint
from enum import Enum
import telebot
import api
import config as cf

api = api.Api(cf.STEAM_TOKEN)

bot = telebot.TeleBot(cf.TELEGRAM_TOKEN)

markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
rand_bun = telebot.types.KeyboardButton('Рандом')

markup.add(rand_bun)


def rand_item(price_range=0):
    if price_range == 0:
        price_range = range(0, 10000)
    elif price_range == 1:
        price_range = range(0, 1001)
    elif price_range == 2:
        price_range = range(1000, 3001)
    elif price_range == 3:
        price_range = range(3001, 10000)

    items = api.clear_items
    item_num = randint(0, len(items))
    while items[item_num].cost not in price_range:
        item_num = randint(0, len(items))

    return items[item_num]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Привет {0.first_name}!'.format(
        message.from_user), parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def send_command(message):
    if message.text == 'Рандом':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="0-1000",
                                                        callback_data='add_item_1_1'))
        keyboard.add(telebot.types.InlineKeyboardButton(text="1000-3000",
                                                        callback_data='add_item_2_1'))
        keyboard.add(telebot.types.InlineKeyboardButton(text="3000+",
                                                        callback_data='add_item_3_1'))
        bot.send_message(
            message.chat.id, api.heroes[randint(0, len(api.heroes))] + " через\n",
            reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith("add_item"):
        count = int(call.data[-1])
        price = int(call.data[-3])
        if count < 6:
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton(text="0-1000",
                                                            callback_data='add_item_1_' + str(count)))
            keyboard.add(telebot.types.InlineKeyboardButton(text="1000-3000",
                                                            callback_data='add_item_2_' + str(count)))
            keyboard.add(telebot.types.InlineKeyboardButton(text="3000+",
                                                            callback_data='add_item_3_' + str(count)))
            item = rand_item(price)
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text=call.message.text + "\n" + str(count) + " " + item.localized_name,
                                  reply_markup=keyboard)
        if count == 5:
            item = rand_item(price)
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text=call.message.text + "\n" + str(count) + " " + item.localized_name)


bot.polling(non_stop=True)
