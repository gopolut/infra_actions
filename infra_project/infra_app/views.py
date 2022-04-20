from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Fisting is 300$')


def second_page(request):
    return HttpResponse('А это вторая страница! Ну и кабачок, я понимаю твоего батю!')
