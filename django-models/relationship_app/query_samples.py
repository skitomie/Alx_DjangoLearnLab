Book.objects.filter(author="John Doe")

Library.objects.get(name=library_name)

Library.objects.get(name="library_name")

books.all()


author_name = "author_name"
Book.objects.filter(author_name)
#Author.objects.get(name=author_name)
