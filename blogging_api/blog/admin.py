from django.contrib import admin
from .models import Post, Category, Tag # Import your models

# Register your models here
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)