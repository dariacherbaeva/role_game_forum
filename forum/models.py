from typing import Any

from django.db import models
from django.db.models import Model
from rest_framework import serializers

from characters.models import Character
from foundation.models import SiteUser


# for game themes only
class Section(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        return Section.objects.create(**validated_data)

    def update(self, instance: Model, validated_data: Any):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


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
        return self.author.username + '^' + self.text


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('post', 'user'),)

    def __str__(self):
        return self.post.text + ': ' + self.user.username


class Dislike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('post', 'user'),)

    def __str__(self):
        return self.post.text + ': ' + self.user.username
