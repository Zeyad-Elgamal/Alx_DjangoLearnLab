from django.urls import path
from .admin_view import admin_view # type: ignore
from .librarian_view import librarian_view # type: ignore # type: ignore
from .member_view import member_view # type: ignore
import views # type: ignore
from .views import list_books, LibraryDetailView, register # type: ignore
from django.contrib.auth.views import LoginView, LogoutView
from .views import add_book, edit_book, delete_book # type: ignore

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/', LibraryDetailView.as_view(), name = "library-detail"),
    path('login/', LoginView.as_view(template_name= 'relationship_app/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(template_name= 'relationship_app/logout.html'), name = 'logout'),
    path('register/', views.register.as_view(), name = "register"),
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian-view'),
    path('member/', member_view, name='member-view'),
    path('add_book/', add_book, name='add-book'),
    path('edit_book/', edit_book, name='edit-book'),
    path('delete_book/', delete_book, name='delete-book'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
from django.urls import path
from .views import admin_view, librarian_view, member_view # type: ignore

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]
from django.urls import path
from .views import add_book, edit_book, delete_book # type: ignore

urlpatterns = [
    path('add/', add_book, name='add-book'),
    path('edit/<int:book_id>/', edit_book, name='edit-book'),
    path('delete/<int:book_id>/', delete_book, name='delete-book'),
]




'''from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    
    # Add other URL patterns here
]


from django.urls import path
from . import views

urlpatterns = [
    path('add_book/', views.add_book, name='add_book'),
    path('bedit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    
    # Other URL patterns...
]
'''