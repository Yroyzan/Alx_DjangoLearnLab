from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
# "books/update", "books/delete"
urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/create/', BookCreateView.as_view(), name='book_create'),
    path('books/update<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/delete<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
]