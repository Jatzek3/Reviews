from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from books.views import HomeListView, BooksReviewDetailView
from books.models import BooksReview
import json


class TestBooks(SimpleTestCase):

    def test_books_index_url(self):
        url = reverse('books_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeListView)

    def test_books_detail_url(self):
        url = reverse('books_detail',  kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, BooksReviewDetailView)
