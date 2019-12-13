from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import ExercisesReview

class HomeListView(ListView):
    queryset = ExercisesReview.objects.all()
    template_name = 'exercises.html'
    model = ExercisesReview
    # model = ExercisesReview
    #
    # def exercises_index(request):   #Hoepage
    #     html = 'exercises.html'
    #     return render(request, html)


class ExercisesDetailView(DetailView):
    queryset = ExercisesReview.objects.all()
    template_name = 'books_detail.html'
    model = ExercisesReview


    def get_object(self, queryset=None):

        id_ = self.kwargs.get("id")
        return get_object_or_404(ExercisesReview,id=id_)
