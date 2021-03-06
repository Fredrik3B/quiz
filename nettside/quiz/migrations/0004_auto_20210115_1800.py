# Generated by Django 3.1.4 on 2021-01-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizark_playing_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizark',
            name='is_playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='quizark',
            name='playing_id',
            field=models.IntegerField(default=False),
        ),
    ]
