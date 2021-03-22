from django.db import models
from django.urls import reverse
import uuid


# Create your models here.

class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing model object
        """
        return self.name


class Language(models.Model):
    Languages = (("English", "En"), ("Russian", "Ru"), ("French", "Fr"), ("Deutsch", "De"),)
    name = models.CharField(max_length=100, choices=Languages, default="En", help_text="Enter the book's language")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book (but not specifying a copy)
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField("ISBN", max_length=13, help_text="13 Character \
    <a href=\"https://www.isbn-international.org/content/what-isbn\">ISBN number</a>")
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('book-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    Model representing specific copy of a book
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
        help_text="Unique ID for this particular book across whole library", )
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved'),)

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return "{id} ({title})".format(id=self.id, title=self.book.title)


class Author(models.Model):
    """
    Model representing book author
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        return "{0}, {1}".format(self.first_name, self.last_name)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
