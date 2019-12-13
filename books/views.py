from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import BooksReview


class HomeListView(ListView):
    queryset = BooksReview.objects.all()
    template_name = 'books.html'
    model = BooksReview


class BooksReviewDetailView(DetailView):
    queryset = BooksReview.objects.all()
    template_name = 'books_detail.html'
    model = BooksReview

    def get_object(self, queryset=None):

        id_ = self.kwargs.get("id")
        return get_object_or_404(BooksReview, id=id_)
