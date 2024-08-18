from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.list_books, name='list_book'),
    path('library/', views.detailView.as_view(), name='library_details'),
]