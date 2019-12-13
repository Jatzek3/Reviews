from django.urls import path
from . import views
from exercises.views import HomeListView

urlpatterns = [
    path('',HomeListView.as_view(), name='exercises_index'),
    path('<int:review_id>/', views.detail_view, name='detail_not_logged')
]