from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LogInForm
from time import sleep

# Create your views here.
def register(request):
    template_name = "accounts/register.html"
    if request.user.is_authenticated:
        messages.warning(request, "Du er allerede logget inn, for å registrere en ny bruker må du først logge deg ut")
        prev_page = request.META.get('HTTP_REFERER')
        if not prev_page:
            return redirect("quiz:quiz")
        return redirect(prev_page)
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Brukeren {username} er laget")
            login(request, user)
            return redirect("quiz:quiz")

        else:
            return render(request, template_name, {"form":form})

    form = CreateUserForm()
    return render(request, template_name, {"form":form})







def login_user(request):
    if request.user.is_authenticated:
        messages.warning(request, "Du er allerede logget inn, vil du logge inn som en annen bruker må du først logge deg ut")
        prev_page = request.META.get('HTTP_REFERER')
        if not prev_page:
            return redirect("quiz:quiz")
        return redirect(prev_page)
    if request.method == 'POST':
        form = LogInForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Du er nå logget inn som {username}")
                redirect_url = request.GET.get('next', 'quiz:quiz')
                return redirect(redirect_url)
            else:
                messages.error(request, "Brukeren finnes allerede")
        else:
            messages.error(request, "Feil brukernavn eller passord")

    form = LogInForm()
    return render(request, "accounts/login.html", {"form":form})


def logout_user(request):
    logout(request)
    # messages.info(request, f"Gratulerer {username}, du er nå logget ut")
    redirect_url = request.GET.get('next', 'quiz:quiz')
    return redirect(redirect_url)
