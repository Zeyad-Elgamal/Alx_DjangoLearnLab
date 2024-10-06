from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # Logic to create a book
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # Logic to delete a book
    return render(request, 'bookshelf/delete_book.html')
