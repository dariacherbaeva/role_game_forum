# Generated by Django 3.0.5 on 2020-04-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20200419_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='theme',
            name='is_game',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='is_open',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
