from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import Post, User, Category, Tag

class PostAPITests(APITestCase):

    def setUp(self):
        # Create a user
        self.client = APIClient()  # Use APIClient instead of default client
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.category = Category.objects.create(name='Test Category')
        self.post = Post.objects.create(
            title='Test Post',
            content='This is a test post.',
            author=self.user,
            category=self.category
        )

def test_create_post(self):
    self.client.login(username='testuser', password='testpass')

    # Create category and tag before creating the post
    category = Category.objects.create(name='Test Category')
    tag = Tag.objects.create(name='Test Tag')

    # Post data with category and tags
    post_data = {
        'title': 'New Post',
        'content': 'This is a new post.',
        'category': category.id,  # Ensure category is passed as ID
        'tags': [tag.id],  # Ensure tags is a list of tag IDs
    }

    response = self.client.post(reverse('post_list'), post_data, format='json')

    print(response.data)  # To see the response data in case of failure
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_posts(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check that the post we created is there

    def test_update_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(reverse('post_detail', args=[self.post.id]), {
            'title': 'Updated Post',
            'content': 'This is an updated post.',
            'category': self.category.id
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, 'Updated Post')

    def test_delete_post(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
