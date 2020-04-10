from django.db import models

from characters.models import Character
from foundation.models import SiteUser


class Section(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Theme(models.Model):
    name = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    first_post = models.ForeignKey('Post', on_delete=models.CASCADE)
    is_open = models.BooleanField
    is_game = models.BooleanField


class Post(models.Model):
    author = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    text = models.TextField
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    picture = models.ImageField
    when = models.DateTimeField()


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)


class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
