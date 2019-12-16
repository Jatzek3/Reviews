from django.test import SimpleTestCase,TestCase, Client
from django.urls import reverse, resolve
from exercises.views import HomeListView, ExercisesDetailView
from exercises.models import ExercisesReview


class TestExercises(SimpleTestCase):

    def test_exercises_index_url(self):
        url = reverse('exercises_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeListView)

    def test_exercise_detail_url(self):
        url = reverse('exercises_detail',  kwargs={'id': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ExercisesDetailView)


class TestExercisesViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('exercises_index')
        self.exercise = ExercisesReview.objects.create()
        self.detail_url = reverse('exercises_detail', kwargs={'id': self.exercise.id})

    def test_exercises_index_get(self):

        response = self.client.get(self.index_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'exercises.html')

    def test_exercises_detail_get(self):

        response = self.client.get(self.detail_url)
        print(self.client.get(response))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'exercises_detail.html')



