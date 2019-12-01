from django.db import models


class TutorialsReview(models.Model):
    tutorials_review = models.TextField()

    def __str__(self):
        return self.tutorials_review