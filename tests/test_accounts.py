from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from accounts.views import SignUpView
from accounts.models import CustomUser


class TestAccounts(SimpleTestCase):

    def test_accounts_signup_page_url(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, SignUpView)

