import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from quiz.models import Quizark

class User(AbstractUser):
    favoritter = models.ManyToManyField(Quizark)

class Player(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    right = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_start = models.DateTimeField(auto_now_add=True)
    temporary = models.BooleanField(default=True)

    def __str__(self):
        return self.user
