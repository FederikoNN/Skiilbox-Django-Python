from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View, generic
# from django.views.generic import TemplateView
from .forms import NewsCreationForm, NewsCommentForm
from .models import News, Comment


class NewsCreationFormView(View):
    def get(self, request):
        news_form = NewsCreationForm()
        return render(request, 'news/news_creation_page.html',
                      context={'news_form': news_form})

    def post(self, request):
        news_form = NewsCreationForm(request.POST)
        if news_form.is_valid():
            news_form.save()
            return HttpResponseRedirect('/news_list/')
        return render(request, 'news/news_creation_page.html',
                      context={'news_form': news_form})


class NewsEditFormView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_edit_form = NewsCreationForm(instance=news)
        return render(request, 'news/news_edit.html',
                      context={'news_edit_form': news_edit_form, 'news': news,
                               'news_id': news_id})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        news_edit_form = NewsCreationForm(request.POST, instance=news)
        if news_edit_form.is_valid():
            news.save()
            return HttpResponseRedirect('/news_list')
        return render(request, 'news/news_edit.html',
                      context={'news_edit_form': news_edit_form, 'news': news,
                               'news_id': news_id})


class NewsListView(generic.ListView):
    model = News
    ordering = ['-date_create']
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'


class NewsSinglePageView(View):
    def get(self, request, news_id):
        news = News.objects.get(id=news_id)
        comments = Comment.objects.filter(news_comment=news_id)
        comment_form = NewsCommentForm(instance=news)
        return render(request, 'news/news_single_page.html',
                      context={'news_id': news_id,
                               'comments': comments,
                               "news": news,
                               'comment_form': comment_form})

    def post(self, request, news_id):
        news = News.objects.get(id=news_id)
        comment = Comment(news_comment=news)
        comment_form = NewsCommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            news.activity += 1
            comment_form.save()
            news.save()
            return HttpResponseRedirect('/news_list')
        return render(request, 'news/news_single_page.html',
                      context={'comment_form': comment_form,
                               'news_id': news_id})
