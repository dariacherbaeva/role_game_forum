from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from foundation.models import SiteUser


class Faculty(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    animal = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name


class Character(models.Model):
    is_canon = models.BooleanField()
    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.IntegerField()
    BLOOD_STATUS_CHOICES = [
        ('p', 'чистокровный(ая)'),
        ('h', 'полукровка'),
        ('m', 'магглорождённый(ая)')
    ]
    blood_status = models.CharField(max_length=1, choices=BLOOD_STATUS_CHOICES)
    description = models.TextField()
    player = models.ForeignKey(SiteUser, on_delete=models.CASCADE, blank=True, default=None, null=True)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True, default=None, null=True)
    year = models.IntegerField(validators=[MinValueValidator(0),
                                           MaxValueValidator(12)], blank=True, default=0)
    photo = models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name + " " + self.last_name


class Subject(models.Model):
    name = models.CharField(max_length=30)
    teacher = models.ForeignKey(Character, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

