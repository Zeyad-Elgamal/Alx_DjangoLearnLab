from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Library
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect("list-books")

class LibraryDetailView(ListView):
    model = Library
    context_object_name = "library"
    template_name = "relationship_app/library_detail.html"
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Library
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.http import HttpResponse

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "relationship_app/list_books.html", context)

# Function-based view to delete a book and redirect to the book list
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list-books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

# Class-based view to show library details
class LibraryDetailView(ListView):
    model = Library
    context_object_name = "library"
    template_name = "relationship_app/library_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library"] = Library.objects.all()
        return context

# Function-based view to handle user registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list-books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {"form": form})
