from django.urls import path

from .views import *

urlpatterns = [
    path('create-contact/', create_contact, name='create_contact'),
    path('contacts/', login_required(ContactByUser.as_view(), login_url='home'), name='contact_list'),
    path('contact/<int:pk>', user_contact, name='contact'),
    path('search-contact/', login_required(Search.as_view(), login_url='home'), name='search_contact'),
]
