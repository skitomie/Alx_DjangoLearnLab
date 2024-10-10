from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer, PostListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated



# View for listing and searching posts
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'content', 'tags', 'author']
    ordering_fields = ['published_date', 'category']

# View for creating a new post
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
"""
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, 
                       SearchFilter, 
                       OrderingFilter]
    
    filterset_fields = ['category', 
                        'author']
    
    search_fields = ['title', 
                     'content', 
                     'tags__name', 
                     'author__username']
    
    ordering_fields = ['published_date', 
                       'category']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
"""
class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().author != self.request.user:
            raise permissions.PermissionDenied("You cannot edit someone else's post.")
        serializer.save()

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

