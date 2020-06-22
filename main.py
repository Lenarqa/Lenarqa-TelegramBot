import telebot
import constant
import os
import random
import hashlib

from collections import Counter

TOKEN = 0;
inputToken = input();

digest = hashlib.sha256(inputToken.encode('utf-8')).digest();


if(digest == constant.tokenHesh):
    TOKEN = inputToken;
    print("good")
else: print("Token error")

bot = telebot.TeleBot(TOKEN)

upd = bot.get_updates()

last_upd = upd[-1]
massage_from_user = last_upd.message
print(massage_from_user)


@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/GiveMeLow')
    user_markup.row('/GiveMePicture')
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)

@bot.message_handler(commands=['GiveMeLow'])
def handle_start(message):
    bot.send_message(message.from_user.id, constant.gameLow)

@bot.message_handler(commands=['GiveMePicture'])
def handle_GiveMePicture(message):
        global GlobalPictureName
        directory = 'C:/Users/lenar/PycharmProjects/bot3/BotPicture'
        all_file_in_directory = os.listdir(directory)
        random_file = random.choice(all_file_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        print(img.name)
        pictureNameWithPng = os.path.basename(img.name)#получает изображение с форматом 1.jpg
        pictureName = os.path.splitext(pictureNameWithPng)[0]# убирает формат 1.jpg тепер просто 1
        GlobalPictureName = pictureName
        print(GlobalPictureName)
        print(type(GlobalPictureName))


@bot.message_handler(content_types=['text'])
def handler_text(message):
    print(GlobalPictureName)
    print("Пришло текстовое сообщение")
    print(type(message.text))
    print(type(GlobalPictureName))

    if Counter(message.text) == Counter(GlobalPictureName):
        bot.send_message(message.chat.id, "И это правильный ответ!")
    else:
        bot.send_message(message.chat.id, "Ты ошибся, правильный ответ {0}".format(GlobalPictureName))


bot.polling(none_stop=True, interval=0)




