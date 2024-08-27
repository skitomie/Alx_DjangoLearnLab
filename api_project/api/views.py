from rest_framework.generics.ListAPIView
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookViewSet(viewsets.ModelViewSet):
    # A ViewSet for viewing and editing book instances.
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer