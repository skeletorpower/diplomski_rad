# Generated by Django 2.2.5 on 2019-11-15 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animations', '0002_dislike_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='animationId',
        ),
        migrations.AddField(
            model_name='animation',
            name='dislikes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='animation',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Dislike',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
    ]
