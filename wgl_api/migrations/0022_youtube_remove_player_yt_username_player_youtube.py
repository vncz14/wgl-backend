# Generated by Django 5.0.1 on 2024-05-08 02:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgl_api', '0021_remove_team_match'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.CharField(max_length=30, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_username', message='Username can only contain alphanumeric characters, underscores, hyphens, and periods.', regex='^[\\w.-]+$')])),
                ('video_id', models.CharField(max_length=11, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='player',
            name='yt_username',
        ),
        migrations.AddField(
            model_name='player',
            name='youtube',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wgl_api.youtube'),
        ),
    ]
