from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня получилось! Fisting is 300$')


def second_page(request):
    return HttpResponse('А это вторая страница \n Oh, sheet! I am sorry!')
