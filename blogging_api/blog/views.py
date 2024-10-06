from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Tag

from django.utils import timezone
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# View to list all blog posts
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

# View to show the details of a specific post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# View to create a new post
def post_new(request):
    from .forms import PostForm
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# API views for listing and creating posts
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'author']
    search_fields = ['title', 'content', 'tags__name']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#class PostCreateView(LoginRequiredMixin, CreateView):
 #   from .forms import PostForm
  #  model = Post
   # fields = ['title', 'content', 'category', 'tags']
    #template_name = 'blog/post_form.html'


# API view for post details, updates, and deletion
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        if self.request.user == serializer.instance.author:
            serializer.save()
        else:
            raise PermissionError("You do not have permission to update this post.")


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_form.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)
    