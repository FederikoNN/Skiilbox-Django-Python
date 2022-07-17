import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.urls import reverse
from .forms import NewsCommentForm
from .models import News, Tag


class NewsCreationFormView(CreateView):
    model = News
    template_name = 'news/news_creation_page.html'
    fields = ['title', 'description', 'tags']
    success_url = ''

    def form_valid(self, form):
        news = form.save(commit=False)
        news.user = self.request.user
        news.save()
        form.save_m2m()
        return redirect(reverse('main'))


class NewsEditFormView(LoginRequiredMixin, UpdateView):
    model = News
    template_name = 'news/news_edit.html'
    fields = ['title', 'description', 'date_edit', 'tags']
    initial = {'date_edit': datetime.datetime.now()}

    def get_object(self, queryset=None):
        if not self.request.user.has_perm('can_publish'):
            raise PermissionDenied
        return super(NewsEditFormView, self).get_object()


class NewsListView(ListView):
    model = News
    ordering = ['-date_create']
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags_list'] = Tag.objects.all()
        return context

    def get_queryset(self):
        queryset = super(NewsListView, self).get_queryset()
        if self.request.GET.get('tag'):
            return queryset.filter(tags__title=self.request.GET.get('tag'))
        return queryset.filter(is_active=True)


# class NewsListTagSearch(ListView):
#     model = News
#     ordering = ['tag', '-date_create']
#     template_name = 'news/tag_search.html'
#     context_object_name = 'news_list_tag_search'
#
#     def get_queryset(self, tag=None):
#         queryset = super(NewsListTagSearch, self).get_queryset()
#         tag = self.request.GET
#         print(tag)
#         return queryset.filter(tag='политика')


class NewsSinglePageView(DetailView):
    model = News
    template_name = 'news/news_single_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = self.object
        context['comments'] = self.object.news.all()
        context['comment_form'] = NewsCommentForm
        return context

    def post(self, request, **kwargs):
        news_object = self.get_object()
        username = request.POST.get('user_name')
        comment_form = NewsCommentForm(request.POST)
        if comment_form.is_valid():
            news_object.activity += 1
            new_comment = comment_form.save(commit=False)
            new_comment.news_comment = news_object
            if request.user.username:
                new_comment.user_name = request.user.username
                new_comment.user = request.user
            else:
                new_comment.user_name = f'{username} (Anonymous)'
            new_comment.save()
            news_object.save()
            return redirect(reverse('comments', kwargs={'pk': news_object.id}))
            # return HttpResponseRedirect('/news_list')
        return render(request, 'news/news_single_page.html',
                      context={'comment_form': comment_form})
