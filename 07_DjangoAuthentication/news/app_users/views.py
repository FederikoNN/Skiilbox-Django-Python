from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class LoginForm(LoginView):
    template_name = 'users/login.html'


class LogoutForm(LogoutView):
    template_name = 'users/logout.html'
