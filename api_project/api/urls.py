from django.urls import path, include
from .views import BookList
from .views import BookViewSet
from rest_framework.routers import DefaultRouter

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)

# The API URLs are now determined automatically by the router.

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
]