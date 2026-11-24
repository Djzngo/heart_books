from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    
    class Rating(models.IntegerChoices):
        WASTEOFTIME = 1
        NOTGREAT = 2
        OK = 3
        PRETTYGOOD = 4
        AWESOME = 5
    
    title = models.CharField(max_length=50, unique=False)
    author = models.CharField(max_length=50, unique=False)
    published = models.DateField(blank=True)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(choices=Rating, default=1)