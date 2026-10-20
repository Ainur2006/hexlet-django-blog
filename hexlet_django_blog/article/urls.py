from django.urls import path

from hexlet_django_blog.article import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('<str:tags>/<int:article_id>/', views.IndexView.as_view(), name='article'),
]