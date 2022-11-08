import telebot

from model.CurrencyEnum import CurrencyEnum
from manager.CurrencyManager import CurrencyManager
from dao.UserDAO import UserDAO

bot = telebot.TeleBot("5353396400:AAFeoPndk9hR6mfj6saOo6JzoBWKDN3Rod0")
currencyManager = CurrencyManager()
userDAO = UserDAO()

@bot.message_handler(commands=['convert'])
def convert(message):
    try:
        user = userDAO.find_by_id(message.chat.id)
        from_value = float(message.text.split(' ')[1])

        resp = currencyManager.translate(CurrencyEnum(user[1]), CurrencyEnum(user[2]), from_value)
        bot.reply_to(message, '{0} {1} = {2} {3}'.format(from_value, user[1], str(resp), user[2]))
    except:
        bot.reply_to(message, "Bad input")

@bot.message_handler(commands=['c'])
def convert_fast(message):
    try:
        from_currency = CurrencyEnum(message.text.split(' ')[1])
        to_currency = CurrencyEnum(message.text.split(' ')[2])
        from_value = float(message.text.split(' ')[3])

        resp = currencyManager.translate(from_currency, to_currency, from_value)
        bot.reply_to(message, '{0} {1} = {2} {3}'.format(from_value, from_currency.value, str(resp), to_currency.value))
    except:
        bot.reply_to(message, "Bad input")

@bot.message_handler(commands=['st'])
def convert_fast(message):
    try:
        user = userDAO.find_by_id(message.chat.id)
        bot.reply_to(message, 'Current info :\nid: {0}\nfrom_currency: {1}\nto_currency: {2}'.format(user[0], user[1], user[2]))
    except:
        bot.reply_to(message, "Some error")

@bot.message_handler(commands=['start'])
def start(message):
    userDAO.save_or_update(message.chat.id, CurrencyEnum.BYN, CurrencyEnum.BYN)
    bot.reply_to(message, "Hello, you can use /help command to know about bot's functions")

@bot.message_handler(commands=['setfrom'])
def set_from(message):
    try:
        choose = CurrencyEnum(message.text.split(' ')[1])

        userDAO.save_or_update(message.chat.id, choose, None)
        bot.reply_to(message, "Ok")
    except:
        bot.reply_to(message, "Bad input")

@bot.message_handler(commands=['setto'])
def set_to(message):
    try:
        choose = CurrencyEnum(message.text.split(' ')[1])

        userDAO.save_or_update(message.chat.id, None, choose)
        bot.reply_to(message, "Ok")

    except:
        bot.reply_to(message, "Bad input")

@bot.message_handler(commands=['cs'])
def currencies(message):
    currencies = ""

    for e in CurrencyEnum:
        currencies += e.value + ", "

    bot.reply_to(message, 'Actual currencies: {0}'.format(currencies))

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "1./set from CURRENCY\n2./set to CURRENCY\n3./convert VALUE - to convert value based on your settings\n"
                          "4./cs - to show actual currencies\n5./c FROM_CURRENCY TO_CURRENCY VALUE\n6./st - to show current settings")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()