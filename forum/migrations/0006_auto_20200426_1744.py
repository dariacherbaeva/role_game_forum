# Generated by Django 3.0.5 on 2020-04-26 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_auto_20200419_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='theme',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='theme', to='forum.Theme'),
        ),
        migrations.AlterField(
            model_name='theme',
            name='first_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_post', to='forum.Post'),
        ),
    ]