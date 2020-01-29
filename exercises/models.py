from django.db import models
from django.urls import reverse
from django.utils import timezone


class ExercisesReview(models.Model):
    name = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField()
    quality = models.CharField(max_length=10, null=True)
    difficulty = models.CharField(max_length=10, null=True)
    skill_level = models.CharField(max_length=10, null=True)

    def __str__(self):
        """This method will enable proper string representation"""
        return self.name

    def get_absolute_url(self):
        """Method which returns to detail after saving"""
        return reverse('exercises_detail', args=[str(self.pk)])


class ExercisessReviewComment(models.Model):

    exercise = models.ForeignKey('exercises.ExercisesReview', on_delete=models.CASCADE, related_name='comments') # this links specified comment to a model
#    commenter = CustomUser.get_username()  # User which is commenting will be shown in html
    date = timezone.now()                       # Date when comment is created
    comment = models.TextField()                # the inside of a comment

    def __str__(self):                          # Proper string represetnation
        return self.comment