import os
import telebot
from flask import Flask, request

# Vercel se token lega
TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Yahan apne commands likho
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Bot Vercel par successfully chal raha hai!")

# Vercel aur Telegram ko connect karne ka rasta
@app.route('/api/webhook', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return "OK", 200
    else:
        return "Error", 403

# 404 error hatane ke liye home page
@app.route('/')
def index():
    return "Bot is alive!"
