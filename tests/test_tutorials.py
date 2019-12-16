from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from tutorials.views import HomeListView, TutorialsDetailView
from tutorials.models import TutorialsReview


class TestExercises(SimpleTestCase):

    def test_tutorials_index_url(self):
        url = reverse('tutorials_index')

        self.assertEquals(resolve(url).func.view_class, HomeListView)

    def test_tutorials_detail_url(self):
        # You have to add kwarg argument so the test will receive
        # proper URL
        url = reverse('tutorials_detail',  kwargs={'id': 1})

        self.assertEquals(resolve(url).func.view_class, TutorialsDetailView)


class TestTutorialsViews(TestCase):

    # setUP will make code easier to write and read
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('tutorials_index')
        # Create an instance of TutorialReview so the test_tutorial_detail_get
        # will return code200 instead of 404
        self.tutorial = TutorialsReview.objects.create()
        self.detail_url = reverse('tutorials_detail', kwargs={'id': self.tutorial.id})

    def test_tutorials_index_get(self):

        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tutorials.html')

    def test_tutorials_detail_get(self):

        response = self.client.get(self.detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tutorials_detail.html')


