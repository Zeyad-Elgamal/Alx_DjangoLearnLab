from django.contrib import admin
from django.urls import path, include
from relationship_app.views import index  # Import the index view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Redirect the root URL to the index view
    path('relationship_app/', include('relationship_app.urls')),  # Include your app's URL patterns
]
