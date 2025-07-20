from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView  # Import both views explicitly
from . import views

urlpatterns = [
    # Function-based view
    path('', list_books, name='home'),
    path('books/', list_books, name='list_books'),
    
    # Class-based view
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    
    # Role-specific views
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    
    # Book CRUD operations
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]