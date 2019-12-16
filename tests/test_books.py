from django.test import SimpleTestCase
from django.urls import reverse, resolve
from books.views import HomeListView, BooksReviewDetailView


class TestBooks(SimpleTestCase):

    def test_accounts_books_index_url(self):
        url = reverse('books_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeListView)


    # Need to deal with test and <int:pk>
    # def test_accounts_books_detail_url(self):
    #     url = reverse('books_detail')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, BooksReviewDetailView.get_object())