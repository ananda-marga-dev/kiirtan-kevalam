# Generated by Django 2.2 on 2019-05-04 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0005_auto_20190504_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='liked_songs',
            field=models.ManyToManyField(null=True, related_name='liked_songs', through='Song.IsFavourite', to='Song.Song'),
        ),
    ]
