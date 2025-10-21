from django.db import models

# Create your models here.

class library(models.Model):
    book_name = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)

class customers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

