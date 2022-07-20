from _csv import reader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, reverse, render
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from .models import Profile, Post, Gallery
from django.contrib.auth.views import LoginView, LogoutView, FormView
from .forms import RegisterForm, EditProfileForm, PostForm, UploadPostsForm


class LoginForm(LoginView):
    template_name = 'djfiles/login.html'


class LogoutForm(LogoutView):
    template_name = 'djfiles/logout.html'


class SignUpForm(FormView):
    form_class = RegisterForm
    template_name = 'djfiles/register.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        phone = form.cleaned_data.get('phone')
        city = form.cleaned_data.get('city')
        about_user = form.cleaned_data.get('about_user')
        Profile.objects.create(
            user=user,
            phone=phone,
            city=city,
            about_user=about_user
        )
        # new_user = authenticate(username=self.request.POST['username'],
        #                         password=self.request.POST['password1'])
        # login(self.request, new_user)
        return redirect(reverse('main'))


class EditProfileFormView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = 'djfiles/edit_profile.html'

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


class PostCreationFormView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'djfiles/post_creation_page.html'
    success_url = '/'

    def form_valid(self, form):
        post = form.save(commit=False)
        files = self.request.FILES.getlist('images')
        post.user = self.request.user
        post.save()
        for image in files:
            post.images.add(Gallery.objects.create(image=image))
        return redirect(reverse('main'))


class PostsListView(ListView):
    model = Post
    ordering = ['-date_create']
    template_name = 'djfiles/posts_list.html'
    context_object_name = 'posts_list'


class PostSinglePageView(DetailView):
    model = Post
    template_name = 'djfiles/post_single_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['post'] = self.object
        context['images'] = self.object.images.all()
        return context


@login_required
def load_posts(request):
    if request.method == 'POST':
        upload_file_form = UploadPostsForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            posts_file = upload_file_form.cleaned_data['file'].read()
            post_str = posts_file.decode('utf-8').split('\n')
            csv_reader = reader(post_str, delimiter=";", quotechar='"')
            for row in csv_reader:
                print(row)
                Post.objects.create(
                    title=row[0],
                    description=row[1],
                    user=request.user
                )
            return redirect(reverse('main'))
    else:
        upload_file_form = UploadPostsForm()

    context = {
        'form': upload_file_form
    }
    return render(request, 'djfiles/upload_posts_file.html', context=context)
