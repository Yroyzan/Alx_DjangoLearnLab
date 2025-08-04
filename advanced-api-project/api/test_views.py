# advanced_api_project/books/tests/test_views.py
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword') #use login here

        self.book1 = Book.objects.create(title='Test Book 1', author='Test Author 1', publication_year=2020)
        self.book2 = Book.objects.create(title='Test Book 2', author='Test Author 2', publication_year=2021)

    def test_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_book_detail(self):
        url = reverse('book-detail', args=[self.book1.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')

    def test_book_create(self):
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    def test_book_update(self):
        url = reverse('book-update', args=[self.book1.pk])
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.get(pk=self.book1.pk).title, 'Updated Book')

    def test_book_delete(self):
        url = reverse('book-delete', args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_book_list_filter(self):
        url = reverse('book-list') + '?publication_year=2020'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    def test_book_list_search(self):
        url = reverse('book-list') + '?search=Author 2'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 2')

    def test_book_list_ordering(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book 2')

    def test_unauthenticated_create(self):
        self.client.logout() #logout to test unauthenticated
        url = reverse('book-create')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN) #403 is more accurate for session auth.

    def test_unauthenticated_update(self):
        self.client.logout()
        url = reverse('book-update', args=[self.book1.pk])
        data = {'title': 'Updated Book', 'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_delete(self):
        self.client.logout()
        url = reverse('book-delete', args=[self.book1.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)