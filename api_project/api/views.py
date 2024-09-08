from rest_framework.generics.ListAPIView
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly

class BookViewSet(viewsets.ModelViewSet):
    # A ViewSet for viewing and editing book instances.
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookList(ListAPIView):

  """
    A ViewSet for viewing and editing book instances.
    Requires authentication for all actions.
    Only admin users can modify data; others can only view it.
"""
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view
    permission_classes = [IsAdminOrReadOnly]