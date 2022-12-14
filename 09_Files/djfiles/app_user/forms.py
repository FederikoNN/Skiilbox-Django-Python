from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    city = forms.CharField(max_length=30, required=False, help_text='Город')
    phone = forms.IntegerField(required=True, help_text='Телефон')
    about_user = forms.CharField(widget=forms.Textarea, required=False,
                                 help_text=' Расскажите о себе')
    avatar = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'avatar', 'phone', 'city',
            'about_user', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    password = None
    about_user = forms.CharField(widget=forms.Textarea, required=False,
                                 help_text=' Расскажите о себе')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'about_user')
