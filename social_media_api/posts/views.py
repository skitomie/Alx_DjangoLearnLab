from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Like
from notifications.models import Notification
from django.shortcuts import generic.get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)



class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        following_users = user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


"""
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"detail": "You already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        Like.objects.create(user=request.user, post=post)
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post
        )
        return Response({"detail": "Post liked successfully"}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()
        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)
        return Response({"detail": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        generics.get_object_or_404(Post, pk=pk)
"""



class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to fetch the post or return a 404 error if not found
        post = get_object_or_404(Post, pk=pk)

        # Use get_or_create to either retrieve an existing like or create a new one
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"detail": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)

        # Create a notification for the post author
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post
        )

        return Response({"detail": "Post liked successfully"}, status=status.HTTP_200_OK)

class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        # Use get_object_or_404 to fetch the post or return a 404 error if not found
        post = generic.get_object_or_404(Post, pk=pk)

        # Attempt to find the like record
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"detail": "Post unliked successfully"}, status=status.HTTP_200_OK)

        return Response({"detail": "You have not liked this post"}, status=status.HTTP_400_BAD_REQUEST)
