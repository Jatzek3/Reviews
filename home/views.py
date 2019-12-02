from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    html = 'home.html'
    return render(request, html)