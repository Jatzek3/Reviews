from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from tutorials.views import HomeListView, TutorialsDetailView


class TestExercises(SimpleTestCase):

    def test_tutorials_index_url(self):
        url = reverse('tutorials_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeListView)

    def test_tutorials_detail_url(self):
        url = reverse('tutorials_detail',  kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TutorialsDetailView)