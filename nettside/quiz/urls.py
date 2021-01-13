from django.urls import path
from . import views
from . import api


app_name = 'quiz'

urlpatterns = [
    path(r'', views.quizside, name='quiz'),
    path(r'quiz/', views.quizcode, name='quizcode'),
    path(r'quiz/<int:quiz_id>/', views.play_quiz, name='play_quiz'),
    path(r'quiz/<int:quiz_id>/api/', api.QuizAPI.as_view(), name='play_quiz_api'),
]
