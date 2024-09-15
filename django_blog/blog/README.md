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


# Comment System
This blog app allows users to:
- View comments under each blog post.
- Add new comments (only for authenticated users).
- Edit and delete comments (only by the comment's author).

## Features
- Comments are linked to specific blog posts and users.
- Comment authors can edit or delete their comments.
- CRUD operations for comments are handled using class-based views.

## How to Use
- To add a comment, navigate to a post detail page and submit the comment form.
- Logged-in users can edit or delete their own comments by using the respective buttons next to their comment.
