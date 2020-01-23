from django.db import models
from django.urls import reverse


class BooksReview(models.Model):
    name = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField()
    quality = models.CharField(max_length=10, null=True)
    difficulty = models.CharField(max_length=10, null=True)
    skill_level = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Method which returns to detail after saving  """
        return reverse('books_detail', args=[str(self.pk)])
