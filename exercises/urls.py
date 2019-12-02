from django.urls import path
from . import views

urlpatterns = [
    path('',views.exercises_index, name='exercises_index'),
]