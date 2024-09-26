from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

def check_role(role):
    def decorator(user):
        return user.is_authenticated and user.userprofile.role == role
    return decorator

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return HttpResponse("This is the Admin view.")

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return HttpResponse("This is the Librarian view.")

@user_passes_test(check_role('Member'))
def member_view(request):
    return HttpResponse("This is the Member view.")

# Define the functions for adding, editing, and deleting books
@login_required
def add_book(request):
    # Logic to add a book goes here
    return render(request, 'add_book.html')  # Ensure this template exists

@login_required
def edit_book(request, book_id):
    # Logic to edit a book goes here
    return render(request, 'edit_book.html')  # Ensure this template exists

@login_required
def delete_book(request, book_id):
    # Logic to delete a book goes here
    return render(request, 'delete_book.html')  # Ensure this template exists
