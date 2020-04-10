from django.views.generic import ListView

from characters.models import Character


class CharacterListView(ListView):
    model = Character
    template_name = 'characters/characters.html'
