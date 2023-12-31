# Generated by Django 4.2.2 on 2023-09-04 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_song_is_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='datetime_deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='дата удаления'),
        ),
        migrations.AddField(
            model_name='song',
            name='datetime_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='дата обновления'),
        ),
    ]
