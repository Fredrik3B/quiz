from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("logg-inn/", views.login_user, name="login"),
    path("logg-ut/", views.logout_user, name="logout"),
]



""" accounts/ login/ [name='login']
accounts/ logout/ [name='logout']
accounts/ password_change/ [name='password_change']
accounts/ password_change/done/ [name='password_change_done']
accounts/ password_reset/ [name='password_reset']
accounts/ password_reset/done/ [name='password_reset_done']
accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
accounts/ reset/done/ [name='password_reset_complete']"""
