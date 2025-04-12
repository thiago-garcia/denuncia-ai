from django.shortcuts import render # noqa


def home(request):
    return render(request, 'base/home.html', {})
