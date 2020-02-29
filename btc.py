import telebot
import random
import requests
import html2text
import json



bot = telebot.TeleBot('1040927005:AAHJskwLb0xl7QRC8VsOoVrmGwYngyvXqVQ')

start='Це бот курсу біткоїн'
@bot.message_handler(commands=['eur'])
def start_message(message):
    s=requests.get('https://api.exmo.com/v1/ticker/')
    a=s.json()
    eur=a['BTC_EUR']['buy_price']
    bot.send_message(message.chat.id, eur)

@bot.message_handler(commands=['usd'])
def start_message(message):
    s=requests.get('https://api.exmo.com/v1/ticker/')
    a=s.json()
    usd=a['BTC_USD']['buy_price']
    bot.send_message(message.chat.id, usd)

@bot.message_handler(commands=['uah'])
def start_message(message):
    s=requests.get('https://api.exmo.com/v1/ticker/')
    a=s.json()
    uah=a['BTC_UAH']['buy_price']
    bot.send_message(message.chat.id, uah)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Це бот для відстеження курсу біткоїн. Введітьдля віображення курсу біткоїна\n /usd  до долара \n /eur - до євро \n /uah - до гривні')


bot.polling()
