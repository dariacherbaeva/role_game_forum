from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from foundation.models import SiteUser


class Faculty(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    animal = models.ImageField(upload_to='photos')


class Character(models.Model):
    is_canon = models.BooleanField()
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    BLOOD_STATUS_CHOICES = [
        ('p', 'pure-blood'),
        ('h', 'half-blood'),
        ('m', 'muggle-born')
    ]
    blood_status = models.CharField(max_length=1, choices=BLOOD_STATUS_CHOICES)
    description = models.TextField()
    player = models.ForeignKey(SiteUser, on_delete=models.CASCADE, blank=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, default=None)
    year = models.IntegerField(validators=[MinValueValidator(1),
                                           MaxValueValidator(12)], blank=True, default=0)
    photo = models.ImageField(upload_to='photos')


class Subject(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Character, on_delete=models.CASCADE)

