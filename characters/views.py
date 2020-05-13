from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from characters.models import Character, Subject, Faculty


class CharacterListView(ListView):
    model = Character
    template_name = 'characters/characters.html'


class MyCharacterListView(LoginRequiredMixin, ListView):
    model = Character
    template_name = 'characters/my_characters.html'

    def get_queryset(self):
        return Character.objects.filter(player=self.request.user)


@login_required
def add_character(request, character_id):
    character = Character.objects.get(id=character_id)
    character.player = request.user
    character.save()
    return redirect('Characters:characters')


@login_required()
def give_up_character(request, character_id):
    character = Character.objects.get(id=character_id)
    character.player = None
    character.save()
    return redirect('Characters:characters')


class CreateCharacterView(LoginRequiredMixin, CreateView):
    model = Character
    template_name = 'characters/new_character.html'
    fields = ['name', 'last_name', 'age', 'blood_status', 'description', 'faculty', 'year', 'photo']
    success_url = reverse_lazy('Characters:my_characters')

    def form_valid(self, form):
        form.instance.player = self.request.user
        form.instance.is_canon = False
        return super(CreateCharacterView, self).form_valid(form)


class CharacterDeleteView(LoginRequiredMixin, DeleteView):
    model = Character
    success_url = reverse_lazy('Characters:characters')


class SubjectsListView(ListView):
    template_name = 'foundation/about_school.html'
    model = Subject
    context_object_name = 'subjects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faculties'] = Faculty.objects.all()
        return context
