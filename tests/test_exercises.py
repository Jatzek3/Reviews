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