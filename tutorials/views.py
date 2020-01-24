from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import TutorialsReview


class HomeListView(ListView):
    """Class to show the list of reviews"""
    queryset = TutorialsReview.objects.all()         # Queryset Collection of items is fetched to a variable
    template_name = 'tutorials.html'                 # This template will display all book reviews in a list
    model = TutorialsReview                          # Model which will be displayed in a List


class TutorialsDetailView(DetailView):
    """Class to show display of single review"""
    queryset = TutorialsReview.objects.all()         # Take the collections of objects from all Book review
    template_name = 'tutorials_detail.html'          # Django will use this template do display the data
    model = TutorialsReview                          # Model which will be displayed

    def get_object(self, queryset=None):             # Method which allows specified review to be displayed(Why Query set deafult None?>

        id_ = self.kwargs.get("id")                  # get specified ID to be taken, could have been done on the row bellow
        return get_object_or_404(TutorialsReview, id=id_)   # If specified ID of a review doesn't exist return 404


class TutorialReviewCreateView(CreateView):
    """View function for creating a Model"""
    model = TutorialsReview                          # Model which will be created
    template_name = 'create_review.html'             # Template name to be used when creating new review Used one template bcs all models are the same
    fields = '__all__'                               # All fields will will be displayed to fill

