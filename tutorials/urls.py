from django.urls import path
from . import views
from .views import HomeListView, TutorialsDetailView,TutorialReviewCreateView

urlpatterns = [
    path('', views.HomeListView.as_view(), name='tutorials_index'),
    path('<int:id>/', TutorialsDetailView.as_view(), name='tutorials_detail'),
    path('books/new/', TutorialReviewCreateView.as_view(), name='tutorials_create_review'),
]