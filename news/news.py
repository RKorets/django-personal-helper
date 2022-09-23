import requests
from pprint import pprint


def get_info():
    response = requests.get('https://yobit.net/api/3/info')

    with open("info.txt", "w") as f:
        f.write(response.text)

    return response.text


def get_pairs(coin1='btc', coin='usd',
              coin2='eth', coin3='usdt',
              coin4='busd', coin5='dash',
              coin6='zec', coin7='shib',
              coin8='trx', coin9='ltc', coin10='xrp'):
    response = requests.get(
        f'https://yobit.net/api/3/ticker/{coin1}_{coin}-{coin2}_{coin}-{coin3}_{coin}-{coin4}_{coin}-{coin5}_{coin}-{coin6}_{coin}-{coin7}_{coin}-{coin8}_{coin}-{coin9}_{coin}-{coin10}_{coin}?ignore_invalid=1').json()
    pprint(response)


def main():
    # print(get_info())
    print(get_pairs())


if __name__ == '__main__':
    main()
