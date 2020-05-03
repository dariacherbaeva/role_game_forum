from django.forms import ModelForm

from forum.models import Post


class GamePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['character', 'text', 'picture']


class SystemPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'picture']
