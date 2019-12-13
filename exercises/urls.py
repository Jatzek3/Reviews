from django.urls import path
from . import views
from exercises.views import HomeListView, ExercisesDetailView

urlpatterns = [
    path('', HomeListView.as_view(), name='exercises_index'),
    path('<int:id>/', ExercisesDetailView.as_view(), name='exercises_detail'),
]