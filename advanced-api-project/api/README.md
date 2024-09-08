# Book API

This API provides CRUD operations for managing books. The API uses Django REST Framework's generic views and enforces permission-based access control.

## Endpoints
- `/books/`: Retrieve a list of all books (GET).
- `/books/<id>/`: Retrieve a single book by ID (GET).
- `/books/create/`: Create a new book (POST, authenticated users only).
- `/books/update/<id>/`: Update an existing book (PUT, authenticated users only).
- `/books/delete/<id>/`: Delete a book (DELETE, authenticated users only).
...
## Advanced Query Capabilities

The Book API supports filtering, searching, and ordering via query parameters.

### Filtering
- Filter by `title`, `author`, or `publication_year`:  
  Example: `/api/books/?author=1`

### Searching
- Search by `title` or `author name`:  
  Example: `/api/books/?search=python`

### Ordering
- Order by `title` or `publication_year`:  
  Example: `/api/books/?ordering=publication_year`

  ## Testing the API

We use Django's built-in testing framework to ensure the API endpoints behave correctly.

### Running Tests

To run the test suite, use the following command:

```bash
python manage.py test api
