from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.list_books, name='list_books'),
    path('library/<int:pk>', views.detailView.as_view(), name='library_detail'),
]