from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests
# import aiohttp
from asgiref.sync import sync_to_async


@login_required(login_url='home')
def news_view(request):
    return render(request, 'news/news.html')


@sync_to_async
@login_required(login_url='home')
def crypto_news(request):
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

    # async with aiohttp.ClientSession() as session:
    #     async with session.post('http://example.com',
    #                             headers={'Content-Type': 'application/json'}) as response:
    #         context = await response.json()

    return render(request, 'news/crypto_news.html', context)
