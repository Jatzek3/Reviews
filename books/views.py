from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import BooksReview


class HomeListView(ListView):
    """Class to show the list of reviews"""
    queryset = BooksReview.objects.all()        # Queryset Collection of items is fetched to a variable
    template_name = 'books.html'                # This template will display all book reviews in a list
    model = BooksReview                         # Model which will be displayed in a List


class BooksReviewDetailView(DetailView):
    """Class to show display of single review"""
    queryset = BooksReview.objects.all()        # Take the collections of objects from all Book review
    template_name = 'books_detail.html'         # Django will use this template do display the data
    model = BooksReview                         # Model which will be displayed

    def get_object(self, queryset=None):        # Method which allows specified review to be displayed(Why Query set deafult None?>
        id_ = self.kwargs.get("id")             # get specified ID to be taken, could have been done on the row bellow
        return get_object_or_404(BooksReview, id=id_)   # If specified ID of a review doesn't exist return 404


class BookReviewCreateView(CreateView):
    """View class for creating a Model"""
    model = BooksReview                         # Model which will be created
    template_name = 'create_review.html'        # Template name to be used when creating new review Used one template bcs all models are the same
    fields = '__all__'                          # All fields will will be displayed to fill. We could also specfy ['name', 'author', etc ]

