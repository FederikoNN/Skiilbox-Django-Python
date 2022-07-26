from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse
from django.views.generic import DetailView, ListView
from .models import Balance, Promo, Shop
from django.contrib.auth.views import LoginView, LogoutView, FormView
from django.core.cache import cache
from .forms import RegisterForm


class LoginForm(LoginView):
    template_name = 'users/login.html'


class LogoutForm(LogoutView):
    template_name = 'users/logout.html'


class SignUpForm(FormView):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        Balance.objects.create(user=user)
        # new_user = authenticate(username=self.request.POST['username'],
        #                         password=self.request.POST['password1'])
        # login(self.request, new_user)
        return redirect(reverse('main'))


class MyAccountView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/my_account.html'
    context_object_name = 'my account'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        promotions = Promo.objects.all()
        offers = self.object.user.all()
        promotions_cache_key = f'promotions:{self.object.username}'
        offers_cache_key = f'offers:{self.object.username}'
        user_account_cache_data = {
            promotions_cache_key: promotions,
            offers_cache_key: offers
        }
        cache.set_many(user_account_cache_data)
        context['user'] = self.object
        context['promo_list'] = promotions
        context['offers'] = offers
        context['purchases'] = self.object.buyer.all()
        return context


class ShopListView(ListView):
    model = Shop
    template_name = 'shop/shop_list.html'
    context_object_name = 'shop_list'
