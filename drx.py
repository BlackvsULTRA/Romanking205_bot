import telebot
import json

with open('config.json') as f:
    config = json.load(f)

bot = telebot.TeleBot(config['token'])

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "Bot is working ✅")

bot.infinity_polling(skip_pending=True)