from django.urls import path
from . import views
from .views import HomeListView, TutorialsDetailView

urlpatterns = [
    path('', views.HomeListView.as_view(), name='tutorials_index'),
    path('<int:id>/', TutorialsDetailView.as_view(), name='tutorials_detail'),
]