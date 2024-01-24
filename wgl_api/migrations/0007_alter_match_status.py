# Generated by Django 5.0.1 on 2024-01-24 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgl_api', '0006_remove_match_player_1_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='status',
            field=models.CharField(choices=[('Cancelled', 'Cancelled'), ('Result contested', 'Result contested'), ('Finished', 'Finished'), ('Ongoing', 'Ongoing')], default='Ongoing', max_length=16),
        ),
    ]
