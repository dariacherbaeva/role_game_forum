# Generated by Django 3.0.5 on 2020-04-26 14:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0008_auto_20200412_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='year',
            field=models.IntegerField(blank=True, default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(12)]),
        ),
    ]
