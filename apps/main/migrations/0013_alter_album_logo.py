# Generated by Django 4.2.2 on 2023-07-19 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_album_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='logo',
            field=models.ImageField(blank=True, default='media/default_cover.png', null=True, upload_to='album_covers/%Y/', verbose_name='логотип'),
        ),
    ]