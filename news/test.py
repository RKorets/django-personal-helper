import requests
from pprint import pprint

coin = 'usd'
coin1 = 'btc'
coin2 = 'eth'
coin3 = 'usdt'
coin4 = 'busd'
coin5 = 'dash'
coin6 = 'zec'
coin7 = 'shib'
coin8 = 'trx'
coin9 = 'ltc'
coin10 = 'xrp'

context = requests.get(
    f'https://yobit.net/api/3/ticker/{coin1}_{coin}-{coin2}_{coin}-{coin3}_{coin}-{coin4}_{coin}-{coin5}_{coin}-{coin6}_{coin}-{coin7}_{coin}-{coin8}_{coin}-{coin9}_{coin}-{coin10}_{coin}?ignore_invalid=1').json()

print(context)
