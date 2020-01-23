from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import TutorialsReview


class HomeListView(ListView):
    queryset = TutorialsReview.objects.all()
    template_name = 'tutorials.html'
    model = TutorialsReview


class TutorialsDetailView(DetailView):
    queryset = TutorialsReview.objects.all()
    template_name = 'tutorials_detail.html'
    model = TutorialsReview

    def get_object(self, queryset=None):

        id_ = self.kwargs.get("id")
        return get_object_or_404(TutorialsReview, id=id_)


class TutorialReviewCreateView(CreateView):
    """View function for creating a Model"""
    model = TutorialsReview
    template_name = 'create_review.html'
    fields = '__all__'

