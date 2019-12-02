from django.shortcuts import render

from django.http import HttpResponse

def books_index(request):
    html = 'books.html'
    return render(request, html)
