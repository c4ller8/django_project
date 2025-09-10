from django.urls import path
from . import views

app_name = 'episodes'  # This sets the application namespace

urlpatterns = [
    path('', views.episodes, name='list'),
]