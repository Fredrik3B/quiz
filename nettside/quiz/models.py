from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)

class Quizark(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    question = models.ManyToManyField(Question)

