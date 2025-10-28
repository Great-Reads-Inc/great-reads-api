from django.db import models
from django.contrib.auth.models import User # Import Django's built-in User model
from .book import Book
from .status import Status

class SavedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(null=True, blank=True) # smallint, can be null
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True) # status_id int
    date_added = models.DateTimeField(auto_now_add=True) # timestamp, automatically set on creation
    date_read = models.DateTimeField(null=True, blank=True) # timestamp, can be null
    review = models.CharField(max_length=200, blank=True) # varchar(200), can be blank

    def __str__(self):
        return f"{self.book.title} saved by {self.user.username}"
