# relationship_app/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'template_name.html')  # Change 'template_name.html' to your actual template
