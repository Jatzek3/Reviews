from django.db import models


class ExercisesReview(models.Model):
    exercises_review = models.TextField()

    def __str__(self):
        return self.exercises_review
