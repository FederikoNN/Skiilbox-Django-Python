from django.shortcuts import redirect, reverse
from .models import Profile
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView, FormView, \
    TemplateView
from .forms import RegisterForm


class LoginForm(LoginView):
    template_name = 'users/login.html'
    success_url = '/'


class LogoutForm(LogoutView):
    template_name = 'users/logout.html'


class SignUpForm(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        Profile.objects.create(
            user=user,
            phone=phone,
            city=city
        )
        new_user = authenticate(username=self.request.POST['username'],
                                password=self.request.POST['password1'])
        login(self.request, new_user)
        return redirect(reverse('main'))


class ProfileData(TemplateView):
    template_name = 'users/account_detail.html'
