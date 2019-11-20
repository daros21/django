from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Publisher(models.Model):
    name = models.CharField(max_length=300)

class Book(models.Model):
    title = models.CharField(max_length=300)
    pages = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    pub_date = models.DateField()

    def __str__(self):
        return f"{self.title}"

    @property
    def authors_text(self):
        return " | ".join([str(author) for author in self.authors.all()])

class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()


class Notification(models.Model):
    note = models.TextField()

    def __str__(self):
        return self.note

