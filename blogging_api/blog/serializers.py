from rest_framework import serializers
from .models import Post, Category, Tag
from django.contrib.auth.models import User


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
                   'title', 
                   'content',
                   'author',
                   'category', 
                   'tags', 
                   'published_date', 
                   ]  # Adjust fields as needed
        read_only_fields = ['id', 'published_date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 
                  'username', 
                  'email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [  'id',
                    'name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 
                  'name']
        
class PostSerializer(serializers.ModelSerializer):
    #author = UserSerializer(read_only=True)
    #category = CategorySerializer()
   # tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id',
                   'title', 
                   'content',
                   'author',
                   'category', 
                   'tags', 
                   'published_date', 
                  ]

