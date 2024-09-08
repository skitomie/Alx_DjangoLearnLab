from django.db import models


# Author model represents the author of books.
# A single author can write multiple books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# AuthorSerializer serializes the Author model and includes nested books.
# The BookSerializer handles individual book serialization.
# Custom validation ensures publication year is valid.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title