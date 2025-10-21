from django.db import models
# Create your models here.
class movie(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()



class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    




