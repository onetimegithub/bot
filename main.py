import telebot
import requests
import random
from telebot import types
import my_config

bot = telebot.TeleBot(token=my_config.bot_token)
name = "Калибара"

energ = 70
sati = 10
happy = 100



def f():
    global sati
    global energ
    sati += 20
    energ += 10

def play():
    global happy
    global sati
    global energ
    sati -= 5
    energ -= 5
    happy += 10

def sleep():
    global sati,energ,happy
    energ = 70
    happy -= 5
    sati -= 10

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Привет!\nЯ бот для частного использования.")

@bot.message_handler(commands=["help"])
def help(message):
    bot.reply_to(message, "Команды:\n\n/feed\n/sleep\n/play\n/setname\n")


@bot.message_handler(commands=["feed"])
def feed(message):
    f()
    check(message)

@bot.message_handler(commands=["play"])
def playH(message):
    play()
    check(message)

@bot.message_handler(commands=["sleep"])
def sleepH(message):
    sleep()
    check(message)


def check(message):
    global sati,energ,happy
    if sati <= 0:
        bot.reply_to(message, f"🍴 Ваш {name} умер от голода")
    elif sati >= 150:
        bot.reply_to(message, f"☹️ Ваш {name} переел")

    if energ <= 0:
        bot.reply_to(message, f"😴 Ваш {name} умер от нехватки сил")
    elif energ >= 200:
        bot.reply_to(message, f"😡 Ваш {name} Получил бешенство")

    if happy <= 0:
        bot.reply_to(message, f"☹️ Ваш {name} грустный")
    elif happy > 0:
        bot.reply_to(message, f"😁 Ваш {name} весёлый")

# @bot.message_handler(commands=["game"])
# def games(message):
#     import random
#     one = random.randint(1,100)
















@bot.message_handler(commands=["setname"])
def nameset(message):
    try:
        a = message.text.split()[1]
    except:
        return
    global name
    name = a
    bot.reply_to(message, f"Имя {name} Установлено")

bot.polling(none_stop=True, interval=0)














