from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import BooksReview

class HomeListView(ListView):
    queryset = BooksReview.objects.all()
    template_name = 'books.html'
    model = BooksReview
    # model = ExercisesReview
    #
    # def exercises_index(request):   #Hoepage
    #     html = 'exercises.html'
    #     return render(request, html)


def detail_view(request, review_id): # for details about each review if not logged in(Log in to add a comment)
    return HttpResponse("This is detail view of %s" % review_id)

#def detail_comment_view(request, review_id):  # for details about each review if logged in
#    return HttpResponse("This is detail view of %s" % review_id )

