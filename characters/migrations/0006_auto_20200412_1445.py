# Generated by Django 3.0.5 on 2020-04-12 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('characters', '0005_auto_20200412_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='player',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
