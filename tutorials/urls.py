from django.urls import path
from . import views

urlpatterns = [
    path('',views.tutorials_index, name='tutorials_index'),
]