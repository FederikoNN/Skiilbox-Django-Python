from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse
from django.views.generic import UpdateView
from .models import Profile
from django.contrib.auth.views import LoginView, LogoutView, FormView
from .forms import RegisterForm, EditProfileForm


class LoginForm(LoginView):
    template_name = 'users/login.html'


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
        about_user = form.cleaned_data.get('about_user')
        avatar = form.cleaned_data.get('avatar')
        Profile.objects.create(
            user=user,
            phone=phone,
            city=city,
            about_user=about_user,
            avatar=avatar
        )
        # new_user = authenticate(username=self.request.POST['username'],
        #                         password=self.request.POST['password1'])
        # login(self.request, new_user)
        return redirect(reverse('main'))


class EditProfileFormView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'users/edit_profile.html'
    redirect_field_name = 'login'

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        user.first_name = form.cleaned_data.get('first_name')
        user.last_name = form.cleaned_data.get('last_name')
        user.profile.about_user = form.cleaned_data.get('about_user')
        user.save()
        user.profile.save()
        # new_user = authenticate(username=self.request.POST['username'],
        #                         password=self.request.POST['password1'])
        # login(self.request, new_user)
        return redirect(reverse('main'))
