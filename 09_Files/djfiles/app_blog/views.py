from _csv import reader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, reverse, render
from django.views.generic import CreateView, ListView, DetailView
from .models import Post, Gallery
from .forms import PostForm, UploadPostsForm


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
