from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import TemplateView


def book_list(request):
    book = Book.objects.all()
    context = {'book_list': book}

    return render(request, 'books/list_books.html', context)

class DetailView(TemplateView):
    model = Book
    template_name = 'books/library_details.html'
