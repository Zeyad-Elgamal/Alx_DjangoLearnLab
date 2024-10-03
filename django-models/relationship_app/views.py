from django.views import View
from django.shortcuts import render
from .models import Library  # Importing the Library model
class LibraryDetailView(View):
    def get(self, request, library_id):
        # Get the library object based on the provided ID
        library = Library.objects.get(id=library_id)
        
        # Assuming you have a related name for the books, e.g., 'books'
        books = library.books.all()  # Adjust according to your relationship
        
        context = {
            'library': library,
            'books': books,
        }
        
        return render(request, 'relationship_app/library_detail.html', context)

