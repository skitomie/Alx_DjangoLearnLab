from django.contrib import admin

# Register your models here.
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Fields to display in the list view
    search_fields = ('title', 'author')  # Fields to search in the admin interface
    list_filter = ['publication_year']  # Fields to filter by in the admin interface

admin.site.register(Book, BookAdmin)