from django.shortcuts import render

from django.http import HttpResponse


def exercises_index(request):
    html = 'exercises.html'
    return render(request, html)

