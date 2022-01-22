from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})


def adv_django(request, *args, **kwargs):
    return render(request, 'advertisement/adv_django.html', {})


def adv_python_advanced(request, *args, **kwargs):
    return render(request, 'advertisement/adv_python_advanced.html', {})


def adv_python_basic(request, *args, **kwargs):
    return render(request, 'advertisement/adv_python_basic.html', {})


def adv_sql(request, *args, **kwargs):
    # images = Image.objects.all()
    return render(request, 'advertisement/adv_sql.html', {})


def adv_web(request, *args, **kwargs):
    return render(request, 'advertisement/adv_web.html', {})
