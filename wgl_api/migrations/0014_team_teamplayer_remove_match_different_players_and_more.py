# Generated by Django 5.0.1 on 2024-03-25 20:51

import computedfields.resolver
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgl_api', '0013_remove_game_best_of_remove_game_require_livestream'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_num', models.SmallIntegerField(default=1)),
                ('player_ids', models.JSONField(default=list)),
                ('place', models.SmallIntegerField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('score_formatted', models.CharField(max_length=12, null=True)),
                ('forfieted', models.BooleanField(default=False)),
                ('predictions', models.JSONField(blank=True, editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(null=True)),
                ('score_formatted', models.CharField(max_length=12, null=True)),
                ('video_id', models.CharField(max_length=11, null=True)),
                ('video_timestamp', models.IntegerField(null=True)),
                ('mu_before', models.FloatField()),
                ('mu_after', models.FloatField(null=True)),
                ('sigma_before', models.FloatField()),
                ('predictions', models.JSONField(blank=True, editable=False, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(computedfields.resolver._ComputedFieldsModelBase, models.Model),
        ),
        migrations.RemoveConstraint(
            model_name='match',
            name='different_players',
        ),
        migrations.RemoveField(
            model_name='match',
            name='contest_reason',
        ),
        migrations.RemoveField(
            model_name='match',
            name='forfeited_player',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_mu_after',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_mu_before',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_score',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_score_formatted',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_sigma_before',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p1_video_url',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_mu_after',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_mu_before',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_score',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_score_formatted',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_sigma_before',
        ),
        migrations.RemoveField(
            model_name='match',
            name='p2_video_url',
        ),
        migrations.RemoveField(
            model_name='match',
            name='predictions',
        ),
        migrations.RemoveField(
            model_name='match',
            name='result',
        ),
        migrations.AddField(
            model_name='match',
            name='num_teams',
            field=models.SmallIntegerField(default=2),
        ),
        migrations.AddField(
            model_name='match',
            name='players_per_team',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='team',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wgl_api.match'),
        ),
        migrations.AddField(
            model_name='match',
            name='teams',
            field=models.ManyToManyField(related_name='match_teams', to='wgl_api.team'),
        ),
        migrations.AddField(
            model_name='teamplayer',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wgl_api.player'),
        ),
        migrations.AddField(
            model_name='team',
            name='players',
            field=models.ManyToManyField(to='wgl_api.teamplayer'),
        ),
    ]
