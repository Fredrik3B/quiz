from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import Quizark

class User(AbstractUser):
    favoritter = models.ManyToManyField(Quizark)
