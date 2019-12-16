from django.test import SimpleTestCase
from django.urls import reverse, resolve
from exercises.views import HomeListView, ExercisesDetailView


class TestExercises(SimpleTestCase):

    def test_accounts_exercises_index_url(self):
        url = reverse('exercises_index')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeListView)


    # Need to deal with test and <int:pk>
    # def test_accounts_books_detail_url(self):
    #     url = reverse('books_detail')
    #     print(resolve(url))
    #     self.assertEquals(resolve(url).func.view_class, BooksReviewDetailView.get_object())