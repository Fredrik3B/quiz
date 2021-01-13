from django.shortcuts import render

# Create your views here.
def quizside(request):
    return render(request, 'quiz/quizside.html')

def play_quiz(requset):
    return render(request, 'quiz/play_quiz.html')


