from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import Book, Library

def list_books(request):
    book = Book.objects.all()
    context = {'list_books': book}

    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
