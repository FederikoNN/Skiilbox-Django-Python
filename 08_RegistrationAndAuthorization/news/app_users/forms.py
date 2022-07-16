from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    phone = forms.IntegerField(required=True, help_text='Телефон')

    class Meta:
        model = User
        fields = ('username', 'phone', 'city', 'password1', 'password2')
