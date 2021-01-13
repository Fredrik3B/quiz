from django.shortcuts import render
from .forms import QuizCodeForm
from accounts.models import Player

# Create your views here.
def quizside(request):
    return render(request, 'quiz/quizside.html')

def quizcode(request):
    if request.method == "POST":
        form = QuizCodeForm(request.POST)
        if form.is_valid():
            quiz_code = form.cleaned_data['code']
            if request.user.is_authenticated:
                player = Player.objects.create(user=request.user)
            else:
                randusername = form.cleaned_data['username']
                player = Player.objects.create(username=randusername, temporary=True)
            request.session["player"] = player.uuid
            return redirect("quiz:play_quiz", quiz_id=quiz_code)


    form = QuizCodeForm()
    return render(request, 'quiz/quizcode.html')

def play_quiz(requset, quiz_id):
    return render(request, 'quiz/play_quiz.html')


