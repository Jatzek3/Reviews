from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from home.views import home_index


class TestHome(SimpleTestCase):

    def test_accounts_tutorials_index_url(self):
        url = reverse('home_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_index)

    # need to implement test for each instance