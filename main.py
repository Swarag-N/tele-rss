import feedparser
from pprint import pprint
import json
from datetime import datetime
from dotenv import load_dotenv
import os
import telegram
load_dotenv() 

with open('data/rss.json') as f:
  feeds = json.load(f)



today = datetime.today().day
today_match = f', {today}'

FEED_DATA=[]

for feed in feeds['feeds']:
    tempFeedData = feedparser.parse(feed['link'])
    # print(tempFeedData)
    # TODO Write Advance Logic to give 1-Only Todays && 2-Upto Five only
    temp = []
    # print(tempFeedData['feed']['subtitle'])
    for i in range(5):
        post = tempFeedData['entries'][i]
        # pprint(post)
        req_data = {}
        req_data['title'] = post['title']
        req_data['link'] = post['link']
        req_data['author'] = post['author']
        temp.append(req_data)
    dataTemp = {
        'name':feed['name'],
        'posts':temp
    } 
    FEED_DATA.append(dataTemp)

pprint(FEED_DATA)

msg_str = ''

for FEED in FEED_DATA:
    msg_str+= FEED['name'] +'\n\n'
    for POST in FEED['posts']:
        temp = (POST['title'],POST['author'],POST['link'])
        msg_str += "\n".join(temp) + '\n\n'

print(msg_str)

TOKEN = os.environ.get("BOT_API")
CHAT_ID=os.environ.get("G_ID")
bot = telegram.Bot(token=TOKEN)
bot.sendMessage(chat_id=CHAT_ID, text=msg_str)