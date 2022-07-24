from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    city = forms.CharField(max_length=30, required=False, label=_('City'))
    phone = forms.IntegerField(required=True, label=_('Phone'))
    about_user = forms.CharField(widget=forms.Textarea, required=False,
                                 label=_('About you'))
    avatar = forms.ImageField(required=False, label=_('Avatar'))

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'avatar', 'phone', 'city',
            'about_user', 'password1', 'password2')


class EditProfileForm(UserChangeForm):
    password = None
    about_user = forms.CharField(widget=forms.Textarea, required=False,
                                 help_text=_('About you'))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'about_user')
