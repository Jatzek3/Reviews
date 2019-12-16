from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home_index


class TestHome(SimpleTestCase):

    def test_accounts_tutorials_index_url(self):
        url = reverse('home_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_index)


    # Need to deal with test and <int:pk>
    # def test_accounts_books_detail_url(self):
    #     url = reverse('books_detail')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, BooksReviewDetailView.get_object()