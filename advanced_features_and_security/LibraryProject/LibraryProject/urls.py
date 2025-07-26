"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from relationship_app import views
from bookshelf import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.list_books, name='home'),
    path('relationship_app/', include('relationship_app.urls')),
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    path('can_create/', views.can_create, name='can_create'),
    path('can_delete/', views.can_delete, name='can_delete')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
