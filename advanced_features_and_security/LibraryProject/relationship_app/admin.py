from django.contrib import admin
from .models import Library, Book
from .models import Author, Librarian

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Author)
admin.site.register(Librarian)

