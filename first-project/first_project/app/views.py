import datetime

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя функцию `reverse`
    pages = {
        'Главная страница': reverse(''),
        'Показать текущее время': reverse('current_time/'),
        'Показать содержимое рабочей директории': reverse('workdir/')
    }
    
    # context и параметры render менять не нужно подробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет, возвращается просто текст
    current_time = datetime.datetime.now().time().strftime('%H:%M')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # по аналогии с `time_view`, напишите код, который возвращает список файлов в рабочей директории

    raise NotImplemented
