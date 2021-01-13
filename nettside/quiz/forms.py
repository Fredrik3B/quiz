from django import forms
from random import randint

def random_user():
    adj = ["kul", "teit", "rar", "gul", "glittrende"]
    sub = ["pølse", "ku", "gris", "ape", "sykkel", "sko", "esel"]
    return adj[randint(0, len(adj))].capitalize() + sub[randint(0, len(sub))].capitalize()

class QuizCodeForm(forms.Form):
    code = forms.IntegerField(label='Kode: ', min_value=100000, max_value=999999)
    username = forms.CharField(required=False, max_length="100", initial=random_user)
