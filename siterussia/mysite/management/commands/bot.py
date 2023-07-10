import time

import telebot
from telebot.types import WebAppInfo

from mysite.management.commands.key_bot import key
from mysite.models import Post
from telebot import TeleBot, types

#
bot = telebot.TeleBot(key, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('🏙Города')
    btn2 = types.KeyboardButton('🌲Природа')
    btn3 = types.KeyboardButton('🪆Культура')
    btn4 = types.KeyboardButton('📖История')
    btn5 = types.KeyboardButton('👨‍👩‍👧‍👦Люди')
    btn6 = types.KeyboardButton('🍀Разное')
    btn7 = types.KeyboardButton('➡Смотреть сайт')

    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    markup.row(btn7)
    bot.send_message(message.from_user.id, 'Выбери категорию', reply_markup=markup)

    # bot.register_next_step_handler(message, user_name)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    list = ['🏙Города', '🌲Природа', '🪆Культура', '📖История', '👨‍👩‍👧‍👦Люди', '🍀Разное']

    if message.text in list:
                result = Post.objects.filter(cat_id=list.index(message.text)+1)
                markup = types.InlineKeyboardMarkup()

                def button(i):
                    btn = types.InlineKeyboardButton(result[i].title, callback_data=str(result[i].slug))
                    i = i + 1
                    if i <= len(result) - 1:
                        btn1 = types.InlineKeyboardButton(result[i].title, callback_data=str(result[i].slug))
                        i = i + 1
                        if i <= len(result) - 1:
                             btn2 = types.InlineKeyboardButton(result[i].title, callback_data=str(result[i].slug))
                             markup.row(btn, btn1, btn2)
                        else:
                             markup.row(btn, btn1)

                    else:
                        markup.row(btn)

                i = 0
                while i <= len(result)-1:
                    button(i)
                    i = i + 3

                    # markup.add(types.InlineKeyboardButton(str(el), callback_data=str(el.slug)))
                bot.send_message(message.chat.id, 'Выбирете интересующее вас в категории: ' + message.text, reply_markup=markup)
    elif message.text == '➡Смотреть сайт':
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Перейти', url='https://openrussianow.ru'))
        bot.send_message(message.chat.id, "Сайт: openrussianow.ru", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Неверная команда. Выбери категорию из меню")
        bot.send_message(message.chat.id, "/start")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    # markup = types.InlineKeyboardMarkup()
    # markup.add(types.InlineKeyboardButton('Смотреть', url='https://openrussianow.ru'))
  post = Post.objects.all()

  for el in post:
    # print(el.slug)
    if call.data == str(el.slug):
        markup = types.InlineKeyboardMarkup()
        url = 'https://openrussianow.ru/post/' + str(el.slug)
        markup.add(types.InlineKeyboardButton('Смотреть на сайте', url=str(url)))
        bot.send_message(call.message.chat.id, el.content[:150] + '...')
        if el.photo:
           foto = 'media/' + str(el.photo)
           file = open(str(foto), 'rb')
           bot.send_photo(call.message.chat.id, file, reply_markup=markup)
        else:
           bot.send_message(call.message.chat.id, "Здесь должно быть Фото", reply_markup=markup)




# bot.polling(none_stop=True)
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        time.sleep(15)