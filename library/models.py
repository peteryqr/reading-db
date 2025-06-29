from django.db import models

# Create your models here.

class LibraryUser(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    liked_books = models.ManyToManyField('Book', blank=True, related_name='liked_by_users')

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
