# Generated by Django 5.0.1 on 2024-02-27 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wgl_api', '0010_remove_match_p1_sigma_after_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='shortcode',
            field=models.CharField(default='wsr-speedrun', max_length=20),
            preserve_default=False,
        ),
    ]
