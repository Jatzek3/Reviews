from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("This is books exercises app")

def detail(request, exercises_review_id):
    return HttpResponse("You are looking at exercises review" % exercises_review_id)