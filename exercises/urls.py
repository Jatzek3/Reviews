from django.urls import path
from . import views
from exercises.views import HomeListView, ExercisesDetailView, ExercisesReviewCreateView

urlpatterns = [
    path('', HomeListView.as_view(), name='exercises_index'),
    path('<int:id>/', ExercisesDetailView.as_view(), name='exercises_detail'),
    path('exercises/new/', ExercisesReviewCreateView.as_view(), name='exercises_create_review'),
]