from django.db import models
from .author import Author
from .genre import Genre # Import Genre for Many-to-Many relationship

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=255)
    pub_date = models.DateField() # Corrected to DateTimeField as per DBML 'timestamp'
    page_count = models.IntegerField() # Corrected to IntegerField()
    authors = models.ManyToManyField(Author, related_name='books')
    genres = models.ManyToManyField(Genre, related_name='books_by_genre') # Many-to-Many with Genre
    cover_image = models.CharField(max_length=255)

    def __str__(self):
        return self.title
