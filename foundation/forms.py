from django.contrib.auth.forms import UserCreationForm
from django import forms

from foundation.models import SiteUser


class SiteRegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60)
    photo = forms.ImageField

    class Meta:
        model = SiteUser
        fields = ('username', 'email', 'password1', 'password2')
