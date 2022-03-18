import datetime
import humanize
import requests
import json
import sys
from random import randint
string="Can you believe it guys? {0}, just {1} away. {0} is in {1}! Woohoo! I am so happy about this information. {0}! Just {1} away, oh wow. Can you believe it? {0}! Just in {1}! It got here so fast! {0}! Just {1} away!"
delta=int(sys.argv[2])
text=sys.argv[1]
time_string=humanize.precisedelta(delta, minimum_unit='seconds', suppress=(), format='%0.0f')
# time_string=humanize.precisedelta(datetime.timedelta(days=0,hours=randint(0,23),seconds=randint(0,59)), minimum_unit='seconds', suppress=(), format='%0.0f')
formatted_string=string.format(text, time_string)


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://emojify.net/',
    'Origin': 'https://emojify.net',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

json_data = {
    'input': formatted_string,
    'density': 100,
    'shouldFilterEmojis': True,
}

r = requests.post('https://api.emojify.net/convert', headers=headers, json=json_data)

data=json.loads(r.text)["result"]
print(data)
