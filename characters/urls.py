from django.urls import path

from characters.views import CharacterListView, MyCharacterListView, add_character, CreateCharacterView, \
    SubjectsListView

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='characters'),
    path('my_characters/', MyCharacterListView.as_view(), name='my_characters'),
    path('take_character/<int:character_id>', add_character, name='take'),
    path('new_character/', CreateCharacterView.as_view(), name='new'),
    path('school/', SubjectsListView.as_view(), name='school'),
]
