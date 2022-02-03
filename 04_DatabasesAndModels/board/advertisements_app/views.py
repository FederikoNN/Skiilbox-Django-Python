# from django.http import HttpResponse
# from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView
from .models import Advertisement


class About(TemplateView):
    template_name = 'advertisements_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бесплатные объявления'
        context['name'] = 'ООО "Пайтон адвертисментс"'
        context['description'] = """
        Расскажите о себе. Найдите поставщиков. Расширьте связи. 
        Сосредоточьтесь на бизнесе. Все необходимые инструменты доступны 
        сразу после регистрации.
        """
        return context


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisement_list.html'
    context_object_name = 'advertisement_list'


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views_count += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
