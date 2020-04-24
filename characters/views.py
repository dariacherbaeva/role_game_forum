from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from characters.models import Character, Subject, Faculty


class CharacterListView(ListView):
    model = Character
    template_name = 'characters/characters.html'


class MyCharacterListView(ListView):
    model = Character
    template_name = 'characters/my_characters.html'


# class PlayerToCharacterView(UpdateView):
#   model = Character
#  fields = ['player']


def add_character(request, character_id):
    character = Character.objects.get(id=character_id)
    character.player = request.user
    character.save()
    return redirect('Characters:characters')


class CreateCharacterView(CreateView):
    model = Character
    template_name = 'characters/new_character.html'
    fields = ['name', 'last_name', 'age', 'blood_status', 'description', 'faculty', 'year', 'photo']
    success_url = reverse_lazy('Characters:my_characters')

    def form_valid(self, form):
        form.instance.player = self.request.user
        form.instance.is_canon = False
        return super(CreateCharacterView, self).form_valid(form)


class SubjectsListView(ListView):
    template_name = 'foundation/about_school.html'
    model = Subject
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faculties'] = Faculty.objects.all()
        return context
