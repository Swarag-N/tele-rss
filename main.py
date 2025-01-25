import feedparser
from pprint import pprint
import json
from datetime import datetime
from dotenv import load_dotenv
import os
import telegram
import asyncio
load_dotenv() 

with open('data/rss.json') as f:
  feeds = json.load(f)



today = datetime.today().day
today_match = f', {today}'

FEED_DATA=[]

for feed in feeds['feeds']:
    tempFeedData = feedparser.parse(feed['link'])
    # TODO Write Advance Logic to give 1-Only Todays && 2-Upto Five only
    temp = []
    for i in range(5):
        post = tempFeedData['entries'][i]
        # pprint(post)
        req_data = {}
        req_data['title'] = post['title']
        req_data['link'] = post['link']
        req_data['author'] = post.get('author', "Confidential")
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


async def main():
    TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
    TELEGRAM_CHANNEL_ID=os.environ.get("TELEGRAM_CHANNEL_ID")
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.sendMessage(chat_id=TELEGRAM_CHANNEL_ID, text=msg_str)


if __name__ == "__main__":
    asyncio.run(main())