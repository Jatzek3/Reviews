from django.db import models


class BooksReview(models.Model):
    name = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField()
    quality = models.CharField(max_length=10, null=True)
    difficulty = models.CharField(max_length=10, null=True)
    skill_level = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name
