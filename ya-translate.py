import requests
import sys
import os
# print(os.environ['HOME'])
# print(os.environ['YANDEX_TRANSLATE_KEY'])

# print(sys.argv[0])

# Yandex Translate API key (from env)
key = os.environ['YANDEX_TRANSLATE_KEY']
ya_tr_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
# "from"-"to", for example en-ru, or only destination language, for example ru
lang = sys.argv[1]
text = sys.argv[2]

# print('text=' + text)
# print('lang=' + lang)

url = ya_tr_url + 'key=' + key + '&text=' + text + '&lang=' + lang
# print('url=' + url)
response = requests.get(url)

data = response.json()
code = (data['code'])
# print('code=' + str(code))
# print('data=' + str(data))

if code == 200:
    # print(text + " | " + data['text'][0])
    print(data['text'][0])
else:
    print('Wrong request!')
