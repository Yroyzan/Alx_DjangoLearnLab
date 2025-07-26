from django.urls import path, include
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

login_view = LoginView.as_view(template_name='relationship_app/login.html')
logout_view = LogoutView.as_view(template_name='relationship_app/logout.html')

urlpatterns = [
    path('list_books/', views.list_books, name='list_books'),
    path('Library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('register/', views.register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/', views.edit_book, name='edit_book'),
    path('delete_book/', views.delete_book, name='delete_book')
]