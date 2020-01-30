from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from accounts.models import CustomUser


class BooksReview(models.Model):
    name = models.CharField(max_length=100, null=True)
    author = models.CharField(max_length=50, null=True)
    description = models.TextField()
    quality = models.CharField(max_length=10, null=True)
    difficulty = models.CharField(max_length=10, null=True)
    skill_level = models.CharField(max_length=10, null=True)

    def __str__(self):
        """This function will enable proper string representation"""
        return self.name

    def get_absolute_url(self):
        """Method which returns to detail after saving """
        return reverse('books_detail', args=[str(self.pk)])


class BooksReviewComment(models.Model):

    book = models.ForeignKey('books.BooksReview', on_delete=models.CASCADE, related_name='comments') # this links specified comment to a model
    commenter = str(User.username)  # User which is commenting will be shown in html
    date = timezone.now()                       # Date when comment is created
    comment = models.TextField()                # the inside of a comment

    def __str__(self):                          # Proper string represetnation
        return self.comment
