import json
from pprint import pprint 

with open('data/sample.json') as f:
  feeds = json.load(f)

pprint(feeds)
msg_str = ''

for FEED in feeds:
    msg_str+= FEED['name'] +'\n\n'
    for POST in FEED['posts']:
        temp = (POST['title'],POST['author'],POST['link'])
        msg_str += "\n".join(temp) + '\n\n'

print(msg_str)