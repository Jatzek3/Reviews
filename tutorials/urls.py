from django.urls import path
from . import views
from .views import HomeListView

urlpatterns = [
    path('',views.HomeListView.as_view(), name='tutorials_index'),
]