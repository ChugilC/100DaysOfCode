import os
from dotenv import load_dotenv
import telebot
import requests

load_dotenv()

API_KEY = os.getenv("TELEGRAM_API_KEY")

URL = "https://icanhazdadjoke.com/"
HEADERS = {
    "Accept": "application/json"
}

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=["joke"])
def send_joke(message):
    response = requests.get(url=URL, headers=HEADERS).json()
    joke = response["joke"]
    bot.reply_to(message, joke)

bot.polling()