from django.urls import path
from . import views


app_name = 'quiz'

urlpatterns = [
        path(r'', views.quizside, name='quiz'),
]
