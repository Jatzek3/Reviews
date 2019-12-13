from django.urls import path
from . import views
from books.views import HomeListView, BooksReviewDetailView

urlpatterns = [
    path('', views.HomeListView.as_view(), name='books_index'),
    path('<int:id>/', BooksReviewDetailView.as_view(), name='books_detail'),
]