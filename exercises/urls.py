from django.urls import path
from . import views
from exercises.views import HomeListView, ExercisesDetailView, ExercisesReviewCreateView
"""
From django docs
path(route, view, kwargs=None, name=None)
    ROUTE
    The route argument should be a string or gettext_lazy() (see Translating URL patterns) 
    that contains a URL pattern. The string may contain angle brackets (like <username> above) 
    to capture part of the URL and send it as a keyword argument to the view. The angle brackets 
    may include a converter specification (like the int part of <int:section>)
    VIEW
    The view argument is a view function or the result of as_view() for class-based views. 
    It can also be an django.urls.include().
    KWARGS (TO BE LEARNED)
    The kwargs argument allows you to pass additional arguments to the view function or method.
    NAME
    It will make easier to include selected URL and allow URL reversing
"""
urlpatterns = [
    path('', HomeListView.as_view(), name='exercises_index'),
    path('<int:id>/', ExercisesDetailView.as_view(), name='exercises_detail'),
    path('exercises/new/', ExercisesReviewCreateView.as_view(), name='exercises_create_review'),
]