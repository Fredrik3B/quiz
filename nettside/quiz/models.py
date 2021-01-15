from django.db import models
from .utils import file_parser

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Quizark(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField()
    question = models.ManyToManyField(Question, blank=True)
    playing_id = models.IntegerField(default=False)
    is_playing = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        questions = file_parser(self.file.name)
        super(Quizark, self).save(*args, **kwargs)
        for question, answer in questions.items():
            new_question = Question(question=question, answer=answer)
            new_question.save()
            self.question.add(new_question)

    def __str__(self):
        return self.title
