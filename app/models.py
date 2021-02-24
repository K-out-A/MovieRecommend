from django.db import models

# Create your models here.

class UserModel(models.Model):
    username = models.CharField(max_length=100)
    passward = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    movie1 = models.CharField(max_length=100)
    movie2 = models.CharField(max_length=100)
    movie3 = models.CharField(max_length=100)

