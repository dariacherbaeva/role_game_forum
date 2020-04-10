# Generated by Django 3.0.5 on 2020-04-07 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foundation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_who', to='foundation.SiteUser')),
                ('subscriptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='who', to='foundation.SiteUser')),
            ],
        ),
    ]
