# Generated by Django 5.0.1 on 2024-05-08 00:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgl_api', '0017_youtube_remove_player_yt_username_player_youtube'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='youtube',
        ),
        migrations.AddField(
            model_name='player',
            name='yt_username',
            field=models.CharField(default='lofigirl', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username can only contain alphanumeric characters, underscores, hyphens, and periods.', regex='^[\\w.-]+$')]),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='YouTube',
        ),
    ]
