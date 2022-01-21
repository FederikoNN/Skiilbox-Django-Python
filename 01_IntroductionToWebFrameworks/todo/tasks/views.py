from django.http import HttpResponse
import random

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        order = ['<li>Установить python</li>',
                 '<li>Установить django</li>',
                 '<li>Запустить сервер</li>',
                 '<li>Порадоваться результату</li>',
                 '<li>Поменять код немножко</li>']
        random.shuffle(order)

        return HttpResponse('<ul>'
                            f'{"".join(order)}'
                            '</ul>')
