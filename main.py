import requests
from pprint import pprint
import time
from bot_token import BOT_TOKEN

API_URL: str = 'https://api.telegram.org/bot'
TEXT: str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 100

API_CATS_URL = 'https://aws.random.cat/meow'

offset: int = -1
counter: int = 0
chat_id: int

while counter < MAX_COUNTER:

    # print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

    updates = requests.get(
        f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            try:
                TEXT = result['message']['text']
            except:
                req = requests.get(API_CATS_URL)
                if req.status_code == 200:
                    pic = req.json()['file']
                requests.get(
                    f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={pic}')
                break
            print(TEXT)
            requests.get(
                f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1
