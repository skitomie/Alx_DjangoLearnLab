Book.objects.filter(author="John Doe")

Library.objects.get(name=library_name)

Library.objects.get(name="library_name")

books.all()

Author.objects.filter(name=author_name)
#Author.objects.get(name=author_name)
Librarian.objects.get(library=library_name)