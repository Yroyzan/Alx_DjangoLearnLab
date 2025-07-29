from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
	class mata:
		model = Book
		fields = '__all__'