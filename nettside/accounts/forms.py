
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Repeat password'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


