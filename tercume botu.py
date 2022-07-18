import telebot
from telebot import *
import googletrans
from googletrans import Translator 
translator = Translator()
#Xos Gelmisiniz mesajini Bura Daxil ed  in
welcome_message='Salam 😊 Bota xoşgəlmisiniz. Azərbaycancadan ingilis dilinə tərcümə etmək üçün /en , istənilən dildən azərbaycancaya tərcümə etmək istəyirsinizsə /tercume butonuna klikləyin'

#Bot Tokeni bura daxil edin 
#Numune bottoken='abcd'

bottoken='1801568916:AAEToeCtmwjKkuU2mv9Eb9ff0xF9w4vUUvI'


bot = telebot.TeleBot(bottoken)

@bot.message_handler(commands=['start'])
def start(message):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/en')
    item2 = types.KeyboardButton('/tercume')
    markup.add(item1,item2)
    bot.send_message(message.chat.id,f'{welcome_message}',reply_markup= markup)

@bot.message_handler(commands=['tercume'])
def chk(message):
    msg = bot.send_message(message.chat.id, "İstənilən dildən azərbaycaya tərcümə edilməsi üçün sözü yazıb göndərin 😊")
    bot.register_next_step_handler(msg, search)

def search(message):
    msg=message.text
    a=translator.translate(msg, dest='az')
    s = a.text
    print(s)
    bot.send_message(message.chat.id, a.text)

@bot.message_handler(commands=['en'])
def chk(message):
    msg = bot.send_message(message.chat.id, "Azərbaycancadan ingiliscəyə tərcümə edilməsi üçün sözü yazıb göndərin 😊")
    bot.register_next_step_handler(msg, search2)

def search2(message):
    msg=message.text
    a=translator.translate(msg, dest='en')
    s = a.text
    print(s)
    bot.send_message(message.chat.id, a.text)
bot.polling()