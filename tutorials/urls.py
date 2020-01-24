from django.urls import path
from . import views
from .views import HomeListView, TutorialsDetailView,TutorialReviewCreateView
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
    path('', views.HomeListView.as_view(), name='tutorials_index'),
    path('<int:id>/', TutorialsDetailView.as_view(), name='tutorials_detail'),
    path('books/new/', TutorialReviewCreateView.as_view(), name='tutorials_create_review'),
]