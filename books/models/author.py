# books/models/author.py

from django.db import models

class Author(models.Model):
    # Django automatically creates an 'id' (primary key) field.

    first_name = models.CharField(max_length=30)
    # CharField for the author's first name, with a max length of 30 characters.

    last_name = models.CharField(max_length=30)
    # CharField for the author's last name, with a max length of 30 characters.

    about = models.TextField(blank=True)
    # TextField is for longer strings, like a biography.
    # blank=True means this field is not required in forms.

    def __str__(self):
        # This defines the string representation of an Author object.
        # It will show the author's full name.
        return f"{self.first_name} {self.last_name}"
