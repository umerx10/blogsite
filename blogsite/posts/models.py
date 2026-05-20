from django.db import models
from django.contrib.auth.models import User
# Create your models here.

categories=[
    ('tech' ,  'Technology'),
    ('edu' ,   'education'),
    ('life' ,   'lifestyle'),
    ('other' ,  'Other'),
]

class Post(models.Model):

    author=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content=models.TextField()
    date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=10, choices=categories)

    def __str__(self):
        return self.title
