# Generated by Django 3.1.4 on 2021-01-12 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizark',
            name='question',
            field=models.ManyToManyField(blank=True, to='quiz.Question'),
        ),
    ]
