# Generated by Django 3.0.5 on 2020-05-11 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0006_auto_20200511_1824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteuser',
            name='is_active',
        ),
    ]
