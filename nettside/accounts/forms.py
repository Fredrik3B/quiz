
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        username = forms.CharField(max_length=100)
        password1 = forms.CharField(max_length=100)
        password2 = forms.CharField(max_length=100)

