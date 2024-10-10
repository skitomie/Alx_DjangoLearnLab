from django.urls import path
from .views import  PostCreateView, PostRetrieveUpdateDestroyView, CategoryListView, PostListView

urlpatterns = [
     path('posts/', PostListView.as_view(), name='post-list'),  # For listing posts
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]