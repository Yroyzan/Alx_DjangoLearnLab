from rest_framework import serializers
from . models import Author, Book
from datetime import datetime


# BookSerializer for conversion data to json file
class BookSerializer(serializers.ModelSerializer):
	class meta:
		model = Book
		fields = '__all__' # all fields

	# serializers.ValidationError valdiate publication year
	def valdiate_pulication_year(self, data):
		year = datetime.now().year
		if data > year:
			raise serializers.ValidationError('unvalid publication_date')
		return data


# AuthorSerializer for conversion data to json file
class AuthorSerializer(serializers.ModelSerializer):
	books = BookSerializer(many=True, read_only=True) # nested serializers for related many objects
	class meta:
		model = Author
		fields = ['name'] # all fileds