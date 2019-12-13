from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TutorialsReview


class HomeListView(ListView):
    queryset = TutorialsReview.objects.all()
    template_name = 'tutorials.html'
    model = TutorialsReview


class TutorialsDetailView(DetailView):
    queryset = TutorialsReview.objects.all()
    template_name = 'books_detail.html'
    model = TutorialsReview

    def get_object(self, queryset=None):

        id_ = self.kwargs.get("id")
        return get_object_or_404(TutorialsReview, id=id_)
