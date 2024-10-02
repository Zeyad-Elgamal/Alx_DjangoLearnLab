# relationship_app/urls.py

from django.urls import path
from . import views  # Ensure this import is correct

urlpatterns = [
    path('', views.index, name='index'),  # Ensure this points to an existing view
]
from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view
]
