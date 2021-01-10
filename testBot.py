from dotenv import load_dotenv
import os
# from telegram import telegram
import telegram
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
load_dotenv() 

TOKEN = os.environ.get("BOT_API")
CHAT_ID=os.environ.get("G_ID")
print(TOKEN,CHAT_ID)
bot = telegram.Bot(token=TOKEN)
# bot.send_message(chat_id=CHAT_ID,text="SSSSS")
# print(a)
bot.sendMessage(chat_id=CHAT_ID, text="SSSS")