from django.db import models

# Author model to be mapped in db
class Author(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
# Book model to be mapped in db
class Book(models.Model):
	title = models.CharField(max_length=100)
	publication_year = models.IntegerField()
	# foreign key for one to many
	author = models.ForeignKey(Author, on_delete=models.CASCADE) 

	
	def __str__(self):
		return self.title

