from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView
from .models import Library


def book_list(request):
    book = Book.objects.all()
    context = {'book_list': book}

    return render(request, 'books/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_details.html'
    context_object_name = 'library'
