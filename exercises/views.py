from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import ExercisesReview


class HomeListView(ListView):
    queryset = ExercisesReview.objects.all()
    template_name = 'exercises.html'
    model = ExercisesReview


class ExercisesDetailView(DetailView):
    queryset = ExercisesReview.objects.all()
    template_name = 'exercises_detail.html'
    model = ExercisesReview

    def get_object(self, queryset=None):

        id_ = self.kwargs.get("id")
        return get_object_or_404(ExercisesReview, id=id_)


class ExercisesReviewCreateView(CreateView):
    """View function for creating a Model"""
    model = ExercisesReview
    template_name = 'create_review.html'
    fields = '__all__'

