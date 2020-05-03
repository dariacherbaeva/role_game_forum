from django.db import models

from characters.models import Character
from foundation.models import SiteUser


# только для игровых тем
class Section(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.CharField(max_length=50)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True)
    first_post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='first_post')
    is_open = models.BooleanField()
    is_game = models.BooleanField()

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    text = models.TextField()
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)
    picture = models.ImageField(upload_to='photos', blank=True, null=True)
    when = models.DateTimeField()
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name='theme', blank=True, null=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)


class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
