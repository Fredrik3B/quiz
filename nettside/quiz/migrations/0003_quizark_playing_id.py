# Generated by Django 3.1.4 on 2021-01-14 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210112_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizark',
            name='playing_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
