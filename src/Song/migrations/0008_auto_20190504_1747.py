# Generated by Django 2.2 on 2019-05-04 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Song', '0007_auto_20190504_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='liked_songs',
            field=models.ManyToManyField(related_name='liked_songs', through='Song.IsFavourite', to='Song.Song'),
        ),
    ]
