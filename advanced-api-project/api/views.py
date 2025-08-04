from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework 
from rest_framework import generics, filters
from django.urls import reverse_lazy
from .models import Book
from .serializers import BookSerializer


class BookListView(ListView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Fields for filtering
    search_fields = ['title', 'author']  # Fields for searching
    ordering_fields = ['title', 'publication_year']  # Fields for ordering


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html' # Create this template
    context_object_name = 'book'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'publication_year'] # Specify the fields to include in the form
    template_name = 'book_form.html' # Create this template
    success_url = reverse_lazy('book_list') # Redirect after successful creation

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year'] # Specify the fields to include in the form
    template_name = 'book_form.html' # Create this template
    success_url = reverse_lazy('book_list') # Redirect after successful update

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html' # Create this template
    success_url = reverse_lazy('book_list')
	

