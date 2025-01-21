from dotenv import load_dotenv
import os
import telegram
load_dotenv() 

TOKEN = os.environ.get("BOT_API")
CHAT_ID=os.environ.get("G_ID")
print(TOKEN,CHAT_ID)
bot = telegram.Bot(token=TOKEN)
bot.sendMessage(chat_id=CHAT_ID, text="SSSS")