from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, UpdateView, ListView
from .models import Account
from django.contrib.auth.views import LoginView, LogoutView, FormView
from .forms import RegisterForm, DepositForm


class LoginForm(LoginView):
    template_name = 'users/login.html'


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     promo = apps.get_model('app_shop', 'Promo')
    #     promotions = promo.objects.all()
    #     offers = self.object.user.all()
    #     promotions_cache_key = f'promotions:{self.object.username}'
    #     offers_cache_key = f'offers:{self.object.username}'
    #     promo_list = cache.get_or_set(promotions_cache_key, promotions,
    #     10 * 60)
    #     offers_list = cache.get_or_set(offers_cache_key, offers, 10 * 60)
    #     context['user'] = self.object
    #     context['promo_list'] = promo_list
    #     context['offers'] = offers_list
    # context['promo_list'] = cache.get_or_set(promotions_cache_key,
    #                                          promotions, 10 * 60)
    # context['offers'] = cache.get_or_set(offers_cache_key, offers,
    # 10 * 60)
    # context['purchases'] = self.object.buyer.all()
    # return context


class DepositView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = DepositForm
    template_name = 'users/deposit_account.html'

    def form_valid(self, form):
        account = self.request.user.account
        account.balance += self.object.balance
        account.save(update_fields=['balance'])
        return redirect(
            reverse('my_account', kwargs={'pk': self.request.user.id}))

