Book.objects.filter(author="John Doe")

Library.objects.get(name=library_name)

Library.objects.get(name="library_name")

books.all()

Book.objects.filter(author=author)
#Author.objects.get(name=author_name)


Library.objects.get(librarian=librarian)