from django.http import HttpResponse


def test(request):
    return HttpResponse("Hello World!")


def second_test(request):
    return HttpResponse("Segunda Página!")
