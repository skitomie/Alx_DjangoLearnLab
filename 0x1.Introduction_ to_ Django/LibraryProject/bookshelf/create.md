from bookshelf.models import Book

new_book = Book.objects.create(title = "Meditations", author = "Ryan Holiday", publication_year = "2020")

new_book.save()
