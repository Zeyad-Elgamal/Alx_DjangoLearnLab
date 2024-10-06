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

@permission_required('bookshelf.view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'bookshelf/book_list.html', {'books': books})
def search_books(request):
    query = request.GET.get('q')
    results = Book.objects.raw(f'SELECT * FROM bookshelf_book WHERE title LIKE "%{query}%"')
    return render(request, 'bookshelf/book_list.html', {'results': results})
from django.db.models import Q

def search_books(request):
    query = request.GET.get('q')
    results = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    return render(request, 'bookshelf/book_list.html', {'results': results})
