**Using Postman:**

1. GET: Send a GET request to /api/books/ to list all books.

2. POST: Send a POST request to /api/books/ with a JSON payload to create a new book.

3. PUT: Send a PUT request to /api/books/<id>/ with a JSON payload to update an existing book.

4. DELETE: Send a DELETE request to /api/books/<id>/ to delete a book.

**Using curl commands in the terminal:**

1. List Books: curl -X GET http://127.0.0.1:8000/api/books/

2. Create Book: curl -X POST -d "title=New Book&author=Author Name" http://127.0.0.1:8000/api/books/

3. Update Book: curl -X PUT -d "title=Updated Book&author=Updated Author" http://127.0.0.1:8000/api/books/1/

4. Delete Book: curl -X DELETE http://127.0.0.1:8000/api/books/1/
