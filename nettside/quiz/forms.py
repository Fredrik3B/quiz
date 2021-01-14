from django import forms
from .models import Quizark

def random_user():
    adj = ["kul", "teit", "rar", "gul", "glittrende"]
    sub = ["pølse", "ku", "gris", "ape", "sykkel", "sko", "esel"]
    return adj[randint(0, len(adj)-1)].capitalize() + sub[randint(0, len(sub)-1)].capitalize()

class QuizCodeForm(forms.Form):
    # Må fikse bug her
    code = forms.IntegerField(label='Kode: ', min_value=100000, max_value=999999)
    username = forms.CharField(required=False, max_length="100", initial=random_user)


class QuizCreateForm(forms.Form):
    quizark = forms.ModelChoiceField(queryset=Quizark.objects.all())

