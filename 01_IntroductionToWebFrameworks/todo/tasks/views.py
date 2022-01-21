from django.http import HttpResponse
import random

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        order = ['Установить python',
                 'Установить django',
                 'Запустить сервер',
                 'Порадоваться результату',
                 'Поменять код немножко']
        random.shuffle(order)
        order = ['<li>' + i_order + '</li>' for i_order in order]
        http_string = '<ul>' + ''.join(order) + '</ul>'

        return HttpResponse(http_string)
