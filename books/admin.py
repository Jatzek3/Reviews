from django.contrib import admin

from .models import BooksReview, BooksReviewComment

admin.site.register(BooksReview)
admin.site.register(BooksReviewComment)         # Adds a possibility to see the model in django.admin view