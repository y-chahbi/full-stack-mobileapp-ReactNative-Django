from django.db import models

# Create your models here.


# user - 

class User(models.Model):
    first_name = models.CharField(max_length=12)
    last_name = models.CharField(max_length=12)
    age  = models.IntegerField()
    username = models.CharField(max_length=16)
    email    = models.EmailField()
    password = models.CharField(max_length=30)
    Created_at = models.DateField()