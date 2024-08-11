from bookshelf.models import Book

new_book = Book(title = "Meditations", author = "Ryan Holiday", publication_year = "2020")

new_book.save()
