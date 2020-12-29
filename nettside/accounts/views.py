from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from time import sleep

# Create your views here.
def register(request):
    template_name = "accounts/register.html"
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Brukeren {username} er laget")
            login(request, user)
            return redirect("quiz:quiz")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request, template_name, {"form":form})

    form = UserCreationForm()
    return render(request, template_name, {"form":form})







def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
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

    form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form":form})


def logout_user(request):
    logout(request)
    # messages.info(request, f"Gratulerer {username}, du er nå logget ut")
    redirect_url = request.GET.get('next', 'quiz:quiz')
    return redirect(redirect_url)
