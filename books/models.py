from django.db import models


class BooksReview(models.Model):
    books_review = models.TextField()

    def __str__(self):
        return self.books_review


