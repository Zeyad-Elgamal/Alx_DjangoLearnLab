from django.shortcuts import render
from .models import Book, Library  # Import the Book and Library models
from django.views.generic import ListView, DetailView  # Import ListView and DetailView

def index(request):
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
