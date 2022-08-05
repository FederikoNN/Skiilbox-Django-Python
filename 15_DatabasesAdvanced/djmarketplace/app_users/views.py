import datetime

from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, UpdateView, ListView
from .models import Account
from django.contrib.auth.views import LoginView, LogoutView, FormView
from .forms import RegisterForm, DepositForm
import logging

logger = logging.getLogger(__name__)


class LoginForm(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        logger.info(
            f'{datetime.datetime.now()} Login user '
            f'{self.request.user.username}')
        return self.get_redirect_url() or self.get_default_redirect_url()


class LogoutForm(LogoutView):
    template_name = 'users/logout.html'


class SignUpForm(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        Account.objects.create(user=user)
        new_user = authenticate(username=self.request.POST['username'],
                                password=self.request.POST['password1'])
        login(self.request, new_user)
        return redirect(reverse('my_account', kwargs={'pk': user.id}))


class MyAccountView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/my_account.html'
    context_object_name = 'my account'


class DepositView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = DepositForm
    template_name = 'users/deposit_account.html'

    def form_valid(self, form):
        account = self.request.user.account
        account.balance += self.object.balance
        account.save(update_fields=['balance'])
        logger.info(
            f'{datetime.datetime.now()} User {self.request.user.username} '
            f'deposit to balance on {self.object.balance}.')
        return redirect(
            reverse('my_account', kwargs={'pk': self.request.user.id}))
