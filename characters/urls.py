from django.urls import path

from characters.views import CharacterListView, MyCharacterListView, add_character, CreateCharacterView, \
    SubjectsListView, give_up_character, CharacterDeleteView

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='characters'),
    path('my_characters/', MyCharacterListView.as_view(), name='my_characters'),
    path('take_character/<int:character_id>', add_character, name='take'),
    path('give_up_character/<int:character_id>', give_up_character, name='give_up'),
    path('new_character/', CreateCharacterView.as_view(), name='new'),
    path('school/', SubjectsListView.as_view(), name='school'),
    path('delete/<int:pk>', CharacterDeleteView.as_view(), name='delete'),
]
