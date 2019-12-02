from django.shortcuts import render

from django.http import  HttpResponse

def tutorials_index(request):
    html = 'tutorials.html'
    return render(request, html)

