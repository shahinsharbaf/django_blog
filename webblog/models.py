from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='post/')
