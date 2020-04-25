import telebot
from flask import Flask, request
import os

bot = telebot.TeleBot(token=os.getenv('TOKEN'))
server = Flask(__name__)

@bot.message_handler(commands=['start']) # welcome command message handler
def send_welcome(message):
    bot.reply_to(message, "Hey human!")

@bot.message_handler(commands=['help']) # help command message handler
def send_welcome(message):
    bot.reply_to(message, 'ALPHA VERSION = FEATURES MAY NOT WORK')

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=os.getenv('WEBHOOK') + os.getenv('TOKEN'))
    return "!", 200

@server.route('/' + os.getenv('TOKEN'), methods=['POST'])	
def getMessage():	
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])	
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.getenv('PORT', 5000)))
