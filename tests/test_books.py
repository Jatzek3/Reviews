from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from books.views import HomeListView, BooksReviewDetailView
from books.models import BooksReview


class TestBooksURLs(SimpleTestCase):

    def test_books_index_url(self):
        url = reverse('books_index')

        self.assertEquals(resolve(url).func.view_class, HomeListView)

    def test_books_detail_url(self):
        # You have to add kwarg argument so the test will receive
        # proper URL
        url = reverse('books_detail',  kwargs={'id': 1})

        self.assertEquals(resolve(url).func.view_class, BooksReviewDetailView)


class TestBooksViews(TestCase):

    # setUP will make code easier to write and read
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('books_index')
        # Create an instance og BookReview so the test_books_detail_get
        # will return code200 instead of 404
        self.book = BooksReview.objects.create()
        self.detail_url = reverse('books_detail', kwargs={'id': self.book.id})

    def test_books_index_get(self):

        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books.html')

    def test_books_detail_get(self):

        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'books_detail.html')


