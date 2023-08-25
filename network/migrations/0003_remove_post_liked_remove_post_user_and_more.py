# Generated by Django 4.0 on 2023-08-24 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_like_profile_post_like_post_like_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='target',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
