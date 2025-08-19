from django.test import  pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework import status
from posts.models import Post, Comment
from accounts.models import CustomUser # Added this import

User = get_user_model()

@pytest.mark.django_db
class PostTests:

    def setup_method(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.user2 = CustomUser.objects.create_user(username='testuser2', password='testpassword2')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Test Content')

    def test_create_post(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'New Post', 'content': 'New Content'}
        response = self.client.post('/posts/', data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Post.objects.count() == 2

    def test_get_post(self):
        response = self.client.get(f'/posts/{self.post.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Test Post'

    def test_update_post(self):
        self.client.force_authenticate(user=self.user)
        data = {'title': 'Updated Post', 'content': 'Updated Content'}
        response = self.client.put(f'/posts/{self.post.id}/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['title'] == 'Updated Post'

    def test_update_post_not_author(self):
        self.client.force_authenticate(user=self.user2)
        data = {'title': 'Updated Post', 'content': 'Updated Content'}
        response = self.client.put(f'/posts/{self.post.id}/', data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/posts/{self.post.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Post.objects.count() == 0

    def test_delete_post_not_author(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(f'/posts/{self.post.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_posts(self):
        response = self.client.get('/posts/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1

@pytest.mark.django_db
class CommentTests:

    def setup_method(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        self.user2 = CustomUser.objects.create_user(username='testuser2', password='testpassword2')
        self.post = Post.objects.create(author=self.user, title='Test Post', content='Test Content')
        self.comment = Comment.objects.create(post=self.post, author=self.user, content='Test Comment')

    def test_create_comment(self):
        self.client.force_authenticate(user=self.user)
        data = {'post': self.post.id, 'content': 'New Comment'}
        response = self.client.post('/comments/', data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Comment.objects.count() == 2

    def test_get_comment(self):
        response = self.client.get(f'/comments/{self.comment.id}/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['content'] == 'Test Comment'

    def test_update_comment(self):
        self.client.force_authenticate(user=self.user)
        data = {'post': self.post.id, 'content': 'Updated Comment'}
        response = self.client.put(f'/comments/{self.comment.id}/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['content'] == 'Updated Comment'

    def test_update_comment_not_author(self):
        self.client.force_authenticate(user=self.user2)
        data = {'post': self.post.id, 'content': 'Updated Comment'}
        response = self.client.put(f'/comments/{self.comment.id}/', data)
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_comment(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f'/comments/{self.comment.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Comment.objects.count() == 0

    def test_delete_comment_not_author(self):
        self.client.force_authenticate(user=self.user2)
        response = self.client.delete(f'/comments/{self.comment.id}/')
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_list_comments(self):
        response = self.client.get('/comments/')
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data['results']) == 1
