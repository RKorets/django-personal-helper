from django.urls import path
from .views import *

urlpatterns = [
    path('create-note/', create_note, name='create_note'),
    path('create-tag/', create_tag, name='create_tag'),
    path('delete_tag/<int:tag_id>/', delete_tag, name='delete_tag'),
    path('tags/', login_required(TagsByUser.as_view(), login_url='home'), name='tags'),
    path('note/<int:pk>', user_note, name='note'),
    path('notes/', login_required(NoteByUser.as_view(), login_url='home'), name='notes_list'),
    path('notes_by_tag/<int:tag_id>/', notes_by_tag, name='notes_list'),
    path('search-note/', login_required(Search.as_view(), login_url='home'), name='search_notes'),
    path('search-tag/', login_required(SearchTag.as_view(), login_url='home'), name='search_tag'),
]
