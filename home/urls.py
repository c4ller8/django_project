from django.urls import path
from . import views

app_name = 'home'  # This sets the application namespace

urlpatterns = [
    path('', views.index, name='index'),
]
# This path is '' (empty) relative to the project's root.
