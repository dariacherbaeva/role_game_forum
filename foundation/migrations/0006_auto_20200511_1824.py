# Generated by Django 3.0.5 on 2020-05-11 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foundation', '0005_siteuser_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
