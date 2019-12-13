from django.shortcuts import render

from django.http import HttpResponse


def home_index(request):
    html = 'home.html'
    return render(request, html)