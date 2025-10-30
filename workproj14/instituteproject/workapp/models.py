from django.db import models

class cirtificate(models.Model):
    studentname = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    date = models.DateField()
    
