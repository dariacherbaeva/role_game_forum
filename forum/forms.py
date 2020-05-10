from django.forms import ModelForm

from characters.models import Character
from forum.models import Post, Theme


class GamePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['character', 'text', 'picture', 'theme']

    def __init__(self, user, *args, **kwargs):
        super(GamePostForm, self).__init__(*args, **kwargs)
        self.fields['character'].queryset = Character.objects.filter(player=user)
        self.fields['theme'].queryset = Theme.objects.filter(is_game=True)


class SystemPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'picture', 'theme']

    def __init__(self, *args, **kwargs):
        super(SystemPostForm, self).__init__(*args, **kwargs)
        self.fields['theme'].queryset = Theme.objects.filter(is_game=False)
