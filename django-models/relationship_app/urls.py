# relationship_app/urls.py

from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('', views.index, name='index'),  # Ensure this points to an existing view
]
