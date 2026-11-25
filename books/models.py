from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    
    # String choices which equal a value integer to calculate 'mean' rating
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
    added_on = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=Rating, default=1)
    
    class Meta:
        ordering = ["-added_on"]
    

class Comment(models.Model):
    
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField(max_length=200, blank=False)
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    