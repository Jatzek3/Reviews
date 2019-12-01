from django.shortcuts import render

from django.http import  HttpResponse

def index(request):
    return HttpResponse("This is books tutorial app")

def detail(request, tutorials_review_id):
    return HttpResponse("You are looking at bookreview" % tutorials_review_id)