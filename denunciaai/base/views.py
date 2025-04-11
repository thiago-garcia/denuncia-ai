from django.http import HttpResponse
from django.shortcuts import render # noqa


def home(request):
    return HttpResponse('Home')
