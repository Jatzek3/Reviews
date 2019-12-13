from django.urls import path
from . import views
from books.views import HomeListView

urlpatterns = [
    path('',views.HomeListView.as_view(), name='books_index'),
]