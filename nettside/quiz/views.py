from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import QuizCodeForm, QuizCreateForm
from accounts.models import Player
from datetime import datetime
from random import randint

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

class CreateQuiz(LoginRequiredMixin, View):
    template_name = "quiz/create_quiz.html"

    def create_quiz_code(self):
        # lager unik quiz kode ut ifra minuttene nå + 4 random tall
        minute = str(datetime.now().minute)
        four_random = ""
        for i in range(4):
            four_random += str(randint(0, 9))
        print(minute + four_random)
        return minute + four_random


    def get(self, request):
        form = QuizCreateForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        print("hh")
        form = QuizCreateForm(request.POST)

        if form.is_valid():
            new_quiz = form.cleaned_data["quizark"]
            return redirect("quiz:play_quiz", quiz_id=self.create_quiz_code())

        return render(request, self.template_name, {'form': form})










