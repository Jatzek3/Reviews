from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is books app")

def detail(request, book_review_id):
    return HttpResponse("You are looking at bookreview" % book_review_id)