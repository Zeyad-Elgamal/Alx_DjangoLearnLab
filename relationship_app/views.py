# relationship_app/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'template_name.html')  # Change 'template_name.html' to your actual template
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Fetch all books from the database
    return render(request, 'list_books.html', {'books': books})
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
