from django.urls import path

from characters.views import CharacterListView

urlpatterns = [
    path('characters/', CharacterListView.as_view(), name='characters'),
]

