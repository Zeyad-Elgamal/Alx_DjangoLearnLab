from django.urls import path
from .views import list_books, LibraryDetailView  # Import views

urlpatterns = [
    path('books/', list_books, name='list_books'),  # Function-based view for listing books
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),  # Class-based view for library details
]
