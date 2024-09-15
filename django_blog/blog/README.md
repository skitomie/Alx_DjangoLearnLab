# Blog Post Management
This Django blog app allows users to:
- View a list of all blog posts
- View the details of each post
- Create new blog posts (only authenticated users)
- Edit and delete posts (only the author of the post)

## Features
- Class-based views for handling CRUD operations.
- Permissions to restrict post editing and deletion to the post’s author.
- Fully functional form for creating and editing blog posts using Django’s ModelForm.

## How to Use
- Navigate to `/posts/` to view all posts.
- Go to `/posts/new/` to create a new post (must be logged in).
- Click on any post to view details, and edit or delete the post if you are the author.
