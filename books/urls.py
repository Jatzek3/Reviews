from django.urls import path
from . import views
from books.views import HomeListView, BooksReviewDetailView, BookReviewCreateView

urlpatterns = [
    path('', HomeListView.as_view(), name='books_index'),
    path('<int:id>/', BooksReviewDetailView.as_view(), name='books_detail'),
    path('books/new/', BookReviewCreateView.as_view(), name='books_create_review'),
]