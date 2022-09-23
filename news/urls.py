from django.urls import path, include
from .views import *

urlpatterns = [
    path('news/', news_view, name='news'),
    path('news/crypto_news/', crypto_news, name='crypto_news'),
]
