from bookshelf.models import Book

updated_book.delete()
# Output: (1, {'bookshelf.Book': 1})

Book.objects.all()
# Output: <QuerySet []>
