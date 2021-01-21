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
    created = models.DateTimeField(auto_now_add=False)

    def save(self, *args, **kwargs):
        super(Quizark, self).save(*args, **kwargs)
        questions = file_parser(self.file.name)
        for question, answer in questions.items():
            if not Question.objects.filter(question=question):
                new_question = Question(question=question, answer=answer)
                new_question.save()
                self.question.add(new_question)

    def __str__(self):
        return self.title
