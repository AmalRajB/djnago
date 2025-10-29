from django.db import models

class todolist(models.Model):
    title = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    
