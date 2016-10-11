from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    isbn = models.CharField(max_length = 13)
    stock = models.IntegerField(default=0)
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class Cost(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)        #Many to one relationship between books and Cost (multiple prices, 1 book)
    book_cost = models.IntegerField(default=0)                      #integer for cost of investment in book (what I Pay)
    user = models.CharField(max_length = 20)

    def __str__(self):
        return self.book.title
