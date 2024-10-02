from django.shortcuts import render
from .models import Book, Library  # Import the Book and Library models
from django.views.generic import ListView, DetailView  # Import ListView and DetailView

def index(request):
<<<<<<< HEAD
    return render(request, 'index.html')  # Ensure you have an index.html template

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Ensure the correct template path

class BookListView(ListView):  # Add this class
    model = Book  # Specify the model to be used
    template_name = 'relationship_app/list_books.html'  # Ensure this path is correct
    context_object_name = 'books'  # Name for the object in the template context

class LibraryDetailView(DetailView):
    model = Library  # Specify the model to be used
    template_name = 'relationship_app/library_detail.html'  # Ensure this path is correct
    context_object_name = 'library'  # Name for the object in the template context
=======
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
>>>>>>> origin/main
