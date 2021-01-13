from django.shortcuts import render, redirect
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
                print(request.user)
                player = Player.objects.create(username=request.user.username, user=request.user)
                print(player)
            else:
                randusername = form.cleaned_data['username']
                player = Player.objects.create(username=randusername, temporary=True)
            request.session["player"] = player.uuid.hex
            return redirect("quiz:play_quiz", quiz_id=quiz_code)


    form = QuizCodeForm()
    return render(request, 'quiz/quizcode.html', {"form": form})

def play_quiz(request, quiz_id):
    print(request.session["player"])
    return render(request, 'quiz/play_quiz.html')


