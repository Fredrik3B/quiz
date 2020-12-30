
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Brukernavn'}))
    password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Passord'}))
    password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Gjenta passord'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


