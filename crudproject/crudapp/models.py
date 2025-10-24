from django.db import models

class library(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    