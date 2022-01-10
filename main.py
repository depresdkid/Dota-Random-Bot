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
def send_command(message):
    if message.text == 'Рандом':
        # после 303 идут лесные и ивентовые айтемы
        item_num = randint(0, 303)
        while api.items[item_num].startswith("Рецепт"):
            item_num += 1
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.add(telebot.types.InlineKeyboardButton(text="Добавить предмет",
                                                        callback_data='add_item_1'))
        bot.send_message(
            message.chat.id, api.heroes[randint(0, len(api.heroes) - 1)] + " через\n1 " + api.items[item_num],
            reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data.startswith("add_item"):
        count = int(call.data[-1])
        if count < 6:
            keyboard = telebot.types.InlineKeyboardMarkup()
            keyboard.add(telebot.types.InlineKeyboardButton(text="Добавить предмет",
                                                            callback_data='add_item_' + str(count + 1)))
            item_num = randint(0, 303)
            while api.items[item_num].startswith("Рецепт"):
                if api.items[item_num].startswith("DOTA_Tooltip"):
                    item_num += 1
                else:
                    item_num += 1
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text=call.message.text + "\n" + str(count + 1) + " " + api.items[item_num],
                                  reply_markup=keyboard)
        if count == 5:
            item_num = randint(0, 303)
            while api.items[item_num].startswith("Рецепт"):
                item_num += 1
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.id,
                                  text=call.message.text + "\n" + str(count + 1) + " " + api.items[item_num])


bot.polling(non_stop=True)
