from django.shortcuts import render
from django.contrib.auth.decorators import staticmethod
from .models import Book
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .forms import ExampleForm
from .models import MyModel



# Create your views here.

@staticmethod
    def can_create(user):
        return user.is_staff

    def can_delete(self, user):
        if user.is_staff:
            return True
        return False

def book_list(request):
    books = Book.objects.all()  
    return render(request, 'bookshelf/book_list.html', {'books': books})

def raise_exception():
    raise PermissionDenied("You do not have permission to access this page.")

class ExampleForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ('field1', 'field2')
