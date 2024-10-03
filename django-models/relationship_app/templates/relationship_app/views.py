from django.shortcuts import render
from .models import Book  # Ensure the Book model is imported

def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the list_books template
