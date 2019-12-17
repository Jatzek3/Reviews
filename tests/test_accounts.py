from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from accounts.views import SignUpView
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm
from  accounts.models import CustomUser


class TestAccounts(SimpleTestCase):

    def test_accounts_signup_page_url(self):
        url = reverse('signup')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, SignUpView)


class TestAccountsForms(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username="jacek1",
                                              password="Abrakadabra1",
                                              email="jacekkawalec@yahoo.com",
                                              age="33")

    def test_CustomUserCreationForm_with_valid_data(self):

        form = CustomUserCreationForm(data={"username":"jacek2",
                                            "password1":"Abrakadabra1",
                                            "password2":"Abrakadabra1",
                                            "email": "jacekkawalec@yahoo.com",
                                            "age": "33"})
        self.assertTrue(form.is_valid())

    def test_CustomUserCreationForm_with_invalid_data(self):
        form = CustomUserCreationForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})

        self.assertFalse(form.is_valid())

    def test_CustomUserChangeForm_with_valid_data(self):
        form = CustomUserChangeForm(data={"username": "jacek2",
                                            "password1": "Abrakadabra1",
                                            "password2": "Abrakadabra1",
                                            "email": "jacekkawalec@yahoo.com",
                                            "age": "33"})

        self.assertTrue(form.is_valid())

    def test_CustomUserChangeForm_with_invalid_data(self):
        form = CustomUserCreationForm(data={'email': "", 'password': "mp", 'first_name': "mp", 'phone': ""})

        self.assertFalse(form.is_valid())