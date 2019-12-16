from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from tutorials.views import HomeListView, TutorialsDetailView
from tutorials.models import TutorialsReview


class TestExercises(SimpleTestCase):

    def test_tutorials_index_url(self):
        url = reverse('tutorials_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeListView)

    def test_tutorials_detail_url(self):
        url = reverse('tutorials_detail',  kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TutorialsDetailView)


class TestTutorialsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('tutorials_index')
        self.tutorial = TutorialsReview.objects.create()
        self.detail_url = reverse('tutorials_detail', kwargs={'id': self.tutorial.id})

    def test_tutorials_index_get(self):

        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tutorials.html')

    def test_tutorials_detail_get(self):

        response = self.client.get(self.detail_url)
        print(self.client.get(response))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tutorials_detail.html')


