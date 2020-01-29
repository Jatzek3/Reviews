from django.contrib import admin

from .models import TutorialsReview,TutorialsReviewComment

admin.site.register(TutorialsReview)
admin.site.register(TutorialsReviewComment)