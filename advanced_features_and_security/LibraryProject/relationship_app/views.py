from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import MyModel

# Create your views here.


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')  # Redirect to your book list view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_books')  
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def is_admin(user):
    if user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=user)
            return profile.role == 'Admin'
        except UserProfile.DoesNotExist:
            return False #User does not have a profile
    return False

def is_librarian(user):
    if user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=user)
            return profile.role == 'Librarian'
        except UserProfile.DoesNotExist:
            return False
    return False

def is_member(user):
    if user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=user)
            return profile.role == 'Member'
        except UserProfile.DoesNotExist:
            return False
    return False

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
  

@permission_required('relationship_app.can_change_book')
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books') 
   

@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books') 
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})

class ExampleForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('field1', 'field2')






