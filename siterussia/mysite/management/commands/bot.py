import telebot
from telebot.types import WebAppInfo
from mysite.models import Post
from telebot import TeleBot, types

#
bot = telebot.TeleBot("6385747594:AAGtS9bS-1CWaV-OH9-Z_1-Jcyq8jiCGEuw", parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Города')
    btn2 = types.KeyboardButton('Природа')
    btn3 = types.KeyboardButton('Культура')
    btn4 = types.KeyboardButton('История')
    btn5 = types.KeyboardButton('Люди')
    btn6 = types.KeyboardButton('Разное')
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5, btn6)
    bot.send_message(message.from_user.id, 'Выбери категорию', reply_markup=markup)
    # markup2 = types.ReplyKeyboardMarkup()
    # btn7 = types.KeyboardButton('Перейти на сайт')
    # markup2.row(btn7)
    # bot.send_message(message.chat.id, 'Выбери категорию', reply_markup=markup2)
    # bot.register_next_step_handler(message, user_name)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    list = ['Города', 'Природа', 'Культура', 'История' 'Люди', 'Разное']

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


                      # btn = types.InlineKeyboardButton(result[i].title, callback_data=str(result[i].slug))
                      # i = i + 1
                      # if i <= len(result)-1:
                      #     btn1 = types.InlineKeyboardButton(result[i].title, callback_data=str(result[i].slug))
                      # else:
                      #     markup.row(btn)
                      # i = i + 1
                      # if i <= len(result)-1:
                      #     btn2 = types.InlineKeyboardButton(result[i].title, callback_data=str(result[i].slug))
                      #     markup.row(btn, btn1, btn2)
                      # else:
                      #     markup.row(btn, btn1)

                i = 0
                while i <= len(result)-1:
                    button(i)
                    i = i + 3

                    # markup.add(types.InlineKeyboardButton(str(el), callback_data=str(el.slug)))
                bot.send_message(message.chat.id, 'Выбирете интересующий вас в категории ' + message.text, reply_markup=markup)



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
        markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
        bot.send_message(call.message.chat.id, el.content[:150] + '...')
        if el.photo:
           foto = 'media/' + str(el.photo)
           file = open(str(foto), 'rb')
           bot.send_photo(call.message.chat.id, file, reply_markup=markup)
        else:
           bot.send_photo(call.message.chat.id, "Фото", reply_markup=markup)


    # elif call.data == 'nature':
    #     result = Post.objects.filter(cat_id=2)
    #     for el in result:
    #         markup = types.InlineKeyboardMarkup()
    #         url = 'https://openrussianow.ru/post/' + str(el.slug)
    #         markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
    #         foto = 'media/' + str(el.photo)
    #         file = open(str(foto), 'rb')
    #         bot.send_message(call.message.chat.id, el.content[:150] + '...')
    #         bot.send_photo(call.message.chat.id, file, reply_markup=markup)
    #
    # elif call.data == 'nature':
    #     result = Post.objects.filter(cat_id=2)
    #     for el in result:
    #         markup = types.InlineKeyboardMarkup()
    #         url = 'https://openrussianow.ru/post/' + str(el.slug)
    #         markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
    #         foto = 'media/' + str(el.photo)
    #         file = open(str(foto), 'rb')
    #         bot.send_message(call.message.chat.id, el.content[:150] + '...')
    #         bot.send_photo(call.message.chat.id, file, reply_markup=markup)
    #
    # elif call.data == 'nature':
    #     result = Post.objects.filter(cat_id=2)
    #     for el in result:
    #         markup = types.InlineKeyboardMarkup()
    #         url = 'https://openrussianow.ru/post/' + str(el.slug)
    #         markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
    #         foto = 'media/' + str(el.photo)
    #         file = open(str(foto), 'rb')
    #         bot.send_message(call.message.chat.id, el.content[:150] + '...')
    #         bot.send_photo(call.message.chat.id, file, reply_markup=markup)
    #
    # elif call.data == 'culture':
    #     result = Post.objects.filter(cat_id=3)
    #     for el in result:
    #         markup = types.InlineKeyboardMarkup()
    #         url = 'https://openrussianow.ru/post/' + str(el.slug)
    #         markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
    #         foto = 'media/' + str(el.photo)
    #         file = open(str(foto), 'rb')
    #         bot.send_message(call.message.chat.id, el.content[:150] + '...')
    #         bot.send_photo(call.message.chat.id, file, reply_markup=markup)
    #
    # elif call.data == 'history':
    #     result = Post.objects.filter(cat_id=4)
    #     for el in result:
    #         markup = types.InlineKeyboardMarkup()
    #         url = 'https://openrussianow.ru/post/' + str(el.slug)
    #         markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
    #         foto = 'media/' + str(el.photo)
    #         file = open(str(foto), 'rb')
    #         bot.send_message(call.message.chat.id, el.content[:150] + '...')
    #         bot.send_photo(call.message.chat.id, file, reply_markup=markup)
    #
    # elif call.data == 'people':
    #     result = Post.objects.filter(cat_id=5)
    #     for el in result:
    #         markup = types.InlineKeyboardMarkup()
    #         url = 'https://openrussianow.ru/post/' + str(el.slug)
    #         markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
    #         foto = 'media/' + str(el.photo)
    #         file = open(str(foto), 'rb')
    #         bot.send_message(call.message.chat.id, el.content[:150] + '...')
    #         bot.send_photo(call.message.chat.id, file, reply_markup=markup)
    #
    # elif call.data == 'other':
    #     result = Post.objects.filter(cat_id=6)
    #     for el in result:
    #         markup = types.InlineKeyboardMarkup()
    #         url = 'https://openrussianow.ru/post/' + str(el.slug)
    #         markup.add(types.InlineKeyboardButton('Смотреть', url=str(url)))
    #         foto = 'media/' + str(el.photo)
    #         file = open(str(foto), 'rb')
    #         bot.send_message(call.message.chat.id, el.content[:150] + '...')
    #         bot.send_photo(call.message.chat.id, file, reply_markup=markup)


bot.polling(none_stop=True)