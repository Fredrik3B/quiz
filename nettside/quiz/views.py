from django.shortcuts import render

# Create your views here.
def quizside(request):
    return render(request, 'quiz/quizside.html')
